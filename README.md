This is a project about SQL Injection - M183
Quick setup and how to run the Postman collections

1) Prepare the database

- Create a PostgreSQL database named `m183` and a `users` table. A small example schema (adjust if needed):

	CREATE TABLE users (
			id SERIAL PRIMARY KEY,
			first_name TEXT
	);

2) Set the DB password in the environment

On Windows PowerShell (adjust for your shell):

```powershell
$env:DB_PASSWORD = "your_postgres_password"
```

3) Install Python dependencies

This project expects `fastapi`, `uvicorn` and `psycopg2` (or `psycopg2-binary`). Create a virtualenv or use conda and install:

```powershell
# example (pip)
python -m pip install fastapi uvicorn psycopg2-binary
```

4) Start the server

```powershell
python main.py
```

The app will listen on http://127.0.0.1:8000 by default.

5) Postman collections

- `tests/M183.postman_collection.json` contains the 2.3 (update) demonstration (already present).
- `tests/M183_2.1.postman_collection.json` contains the 2.1 confidentiality-style SQLi demonstration.

How to import and run in Postman

1. Open Postman and choose Import -> File -> select `tests/M183_2.1.postman_collection.json`.
2. Ensure your FastAPI server is running and `DB_PASSWORD` is set.
3. Run the requests in order: "Add user - John", "Add user - Alice", then "Vulnerable read - normal (John)", then "Vulnerable read - SQLi (OR tautology)".

Notes and safety

- The endpoint `/vuln_users` is intentionally vulnerable and added for demonstration only. Do not deploy this code to production.
- The project demonstrates confidentiality-style SQL injection (2.1) by converting a single-record query into a query that returns many records via a tautology injection (`' OR '1'='1`).
