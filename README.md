# MCG — Maverick Consulting Group (website replica)

A self-contained **Python (Flask)** rebuild of [mcg-asia.com](https://www.mcg-asia.com/).
Backend and frontend both live inside this single Python project.

> This is an independent homage/replica for learning purposes. Text content is
> paraphrased from the public site; it is not affiliated with Maverick Consulting Group.

## Structure

```
mcg-asia/
├── run.py                 # entry point
├── requirements.txt
├── README.md
└── app/
    ├── __init__.py        # Flask app + routes (the "backend")
    ├── content.py         # all site content as Python data
    ├── templates/         # Jinja2 HTML templates (the "frontend")
    │   ├── base.html
    │   ├── home.html
    │   ├── service.html
    │   ├── expertise.html
    │   ├── case_studies.html
    │   ├── team.html
    │   ├── insights.html / insight.html
    │   ├── arabia.html / contact.html / 404.html
    └── static/
        ├── css/style.css
        └── js/main.js
```

## Run

```bash
cd mcg-asia
python3 -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
python run.py
```

Then open http://127.0.0.1:5055

## Routes
| Path | Page |
|------|------|
| `/` | Home |
| `/services/<slug>` | Six service pages |
| `/our-expertise` | Industry expertise |
| `/case-studies` | Case studies |
| `/our-team` | Team |
| `/featured-insights` + `/featured-insights/<slug>` | Insights list + article |
| `/mcg-arabia` | MCG Arabia |
| `/contact-us` | Contact form (POST handled server-side) |

## Editing content
All copy lives in `app/content.py` — edit the Python dictionaries/lists and reload.
