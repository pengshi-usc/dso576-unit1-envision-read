# DSO-576 — Unit 1: Envision & Read

This is the course repository for **Unit 1 (Envision & Read)** of DSO-576, *Algorithmic Thinking with Python*. You'll **clone this repo and run one command** to install everything the course needs. Material is organized into numbered folders that grow as the unit goes on — it starts with **`1-onboarding/`**.

> **Brand-new to all this?** First set up your computer with the step-by-step **[DSO-576 setup guide](https://dso576-setup.vercel.app)** — it walks you through installing VS Code, Python (uv), GitHub, and the AI tools with zero experience assumed. Come back here when it tells you to clone the course repo.

---

## Get started (after your computer is set up)

You only need to copy and paste. From a terminal:

```bash
# 1. Download (clone) this repo
git clone https://github.com/pengshi-usc/dso576-unit1-envision-read.git

# 2. Go into it
cd dso576-unit1-envision-read

# 3. Install the exact set of packages the course uses
uv sync
```

`uv sync` reads `pyproject.toml` and `uv.lock` and builds an identical environment for everyone — you can't break the shared setup, and you never edit these files by hand.

---

## Check that everything works

```bash
# Confirms every required package is installed
uv run python 1-onboarding/check_setup.py
```

You should see `OK` next to every package and **`All good! 🎉`** at the end.

```bash
# Confirms Streamlit runs and opens in your browser
uv run streamlit run 1-onboarding/app.py
```

Your browser should open showing a chart titled *"Setup works! 🎉"*. Press **Ctrl + C** in the terminal to stop it.

If anything fails, re-run `uv sync` from the repo root, then try again. Still stuck? See the **[setup guide's help section](https://dso576-setup.vercel.app/help)** or bring the exact error to office hours.

---

## What's in this repo

| Folder | What it is |
|---|---|
| `1-onboarding/` | Setup checks: `check_setup.py` (package check) and `app.py` (Streamlit test). |
| *(more added through the unit)* | `2-…`, `3-…` folders appear as Unit 1 progresses. |

The Python environment includes: `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `altair`, `plotly`, `psycopg[binary]`, `sqlalchemy`, `snowflake-connector-python[pandas]`, `openpyxl`, `xlsxwriter`, `jupyter`, `ipykernel`, and `jupytext` — pinned in `pyproject.toml` / `uv.lock`.
