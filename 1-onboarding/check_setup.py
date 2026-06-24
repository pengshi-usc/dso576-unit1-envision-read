# Setup check — confirms every package the course needs is installed.
# Run it from the repo root with:   uv run python 1-onboarding/check_setup.py
# You should see "OK" next to every package and "All good!" at the end.

import sys

print(f"Python {sys.version.split()[0]}\n")

# Import names (a few differ from the install name, e.g. snowflake.connector).
packages = [
    "streamlit", "pandas", "numpy", "matplotlib", "seaborn",
    "altair", "plotly", "psycopg", "sqlalchemy",
    "snowflake.connector", "openpyxl", "xlsxwriter", "jupytext",
]

ok = True
for name in packages:
    try:
        __import__(name)
        print(f"  OK   {name}")
    except Exception as e:
        ok = False
        print(f"  FAIL {name}  ->  {e}")

print("\nAll good! 🎉" if ok else "\nSomething is missing — run 'uv sync' again from the repo root.")
sys.exit(0 if ok else 1)
