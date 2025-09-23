# PyAssignment Hub

A static framework for Python assignments:
- Upload *template.py* and *instructions.html* per assignment.
- (Optional) Add *tests_public.py* for local self‑checks in the browser (Pyodide).
- (Optional) Enable a *Socratic Hint Bot* (WebLLM, runs on-device; no answers or code).

**Zero backend.** Host the `docs/` folder on GitHub Pages and reuse every term.

## Structure
docs/
  index.html
  assignment.html
  assets/
    style.css
    site.js
  assignments/
    manifest.json
    fizzbuzz/
      manifest.json
      template.py
      instructions.html
      tests_public.py

## Add an assignment
1. Copy an existing folder under `docs/assignments/` and rename it.
2. Edit its `manifest.json`, `instructions.html`, `template.py` (and optional `tests_public.py`).
3. Add an entry in `docs/assignments/manifest.json` for your new slug.

### Manifest fields
{
  "slug": "fizzbuzz",
  "title": "FizzBuzz Basics",
  "tagline": "Loops, conditionals, modulo",
  "points": 10,
  "due": "2025-10-01",
  "self_check": true,
  "hints": true
}

## Self‑check tests
- Put public tests in `tests_public.py` (keep private tests on Gradescope).
- The hub concatenates the student's code and runs your tests in Pyodide.
- Official grading is still Gradescope.

## Hint Bot (optional)
- Uses WebLLM (browser‑only, no keys). Guardrails forbid code/answers.

## GitHub Pages
- Create a repo with the `docs/` folder at the root.
- Settings → Pages → Deploy from branch → `main` + `/docs`.

Starter generated 2025-09-23.
