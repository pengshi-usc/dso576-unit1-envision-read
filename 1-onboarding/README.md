# 1 — Onboarding

Your first stop. These two scripts confirm your computer is fully set up for DSO-576.
Run both from the **repo root** (the `dso576-unit1-envision-read` folder), after `uv sync`.

## 1. Check your packages

```bash
uv run python 1-onboarding/check_setup.py
```

Prints `OK` next to each required package and `All good! 🎉` when everything is installed.
If you see any `FAIL`, run `uv sync` again from the repo root and re-run this.

## 2. Check Streamlit

```bash
uv run streamlit run 1-onboarding/app.py
```

Opens a browser page titled *"Setup works! 🎉"* with a chart. Press **Ctrl + C** in the terminal to stop it.

---

Once both pass, you're ready for class. 🎉
