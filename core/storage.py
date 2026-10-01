"""Django storage backend backed by a public Supabase Storage bucket."""

import json
import mimetypes
import os
import posixpath
import uuid
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from django.core.exceptions import ImproperlyConfigured
from django.core.files.base import ContentFile
from django.core.files.storage import Storage


class SupabaseStorage(Storage):
    """Store uploaded media in Supabase so it survives Vercel invocations."""

    def __init__(self):
        self.project_url = (
            os.environ.get("NEXT_PUBLIC_DATABASE_SUPABASE_URL")
            or os.environ.get("DATABASE_SUPABASE_URL")
            or os.environ.get("SUPABASE_URL")
        )
        self.service_key = (
            os.environ.get("DATABASE_SUPABASE_SERVICE_ROLE_KEY")
            or os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        )
        self.bucket = os.environ.get("SUPABASE_STORAGE_BUCKET", "veiculos")

        if not self.project_url or not self.service_key:
            raise ImproperlyConfigured(
                "Supabase Storage requires the Supabase project URL and service role key."
            )

        self.project_url = self.project_url.rstrip("/")

    def get_available_name(self, name, max_length=None):
        directory, filename = posixpath.split(name.replace("\\", "/"))
        extension = posixpath.splitext(filename)[1]
        unique_name = f"{uuid.uuid4().hex}{extension}"
        return posixpath.join(directory, unique_name) if directory else unique_name

    def _object_url(self, name):
        bucket = quote(self.bucket, safe="")
        path = quote(name, safe="/")
        return f"{self.project_url}/storage/v1/object/{bucket}/{path}"

    def _request(self, url, method, data=None, content_type=None):
        headers = {
            "apikey": self.service_key,
            "Authorization": f"Bearer {self.service_key}",
        }
        if content_type:
            headers["Content-Type"] = content_type
        request = Request(url, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise OSError(
                f"Supabase Storage request failed ({error.code}): {detail}"
            ) from error
        except URLError as error:
            raise OSError(f"Could not reach Supabase Storage: {error.reason}") from error

    def _save(self, name, content):
        data = b"".join(content.chunks())
        content_type = (
            getattr(content, "content_type", None)
            or mimetypes.guess_type(name)[0]
            or "application/octet-stream"
        )
        self._request(
            self._object_url(name),
            "POST",
            data=data,
            content_type=content_type,
        )
        return name

    def _open(self, name, mode="rb"):
        data = self._request(self._object_url(name), "GET")
        return ContentFile(data, name=name)

    def delete(self, name):
        bucket_url = f"{self.project_url}/storage/v1/object/{quote(self.bucket, safe='')}"
        data = json.dumps({"prefixes": [name]}).encode("utf-8")
        self._request(bucket_url, "DELETE", data=data, content_type="application/json")

    def exists(self, name):
        # get_available_name() generates a fresh UUID for every upload.
        return False

    def url(self, name):
        bucket = quote(self.bucket, safe="")
        path = quote(name, safe="/")
        return f"{self.project_url}/storage/v1/object/public/{bucket}/{path}"
