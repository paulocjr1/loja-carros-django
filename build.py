"""Prepare the Django database schema during a Vercel deployment."""

import os
import subprocess
import sys


database_url = (
    os.environ.get("DATABASE_URL")
    or os.environ.get("DATABASE_POSTGRES_PRISMA_URL")
    or os.environ.get("DATABASE_POSTGRES_URL")
)
if not database_url:
    raise SystemExit(
        "DATABASE_URL is required on Vercel. Connect a PostgreSQL database first."
    )

os.environ["DATABASE_URL"] = database_url
subprocess.run(
    [sys.executable, "manage.py", "migrate", "--noinput"],
    check=True,
)
