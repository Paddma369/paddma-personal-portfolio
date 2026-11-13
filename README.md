# Paddma Mal - Personal Engineering Portfolio

A single-page portfolio built with **Python + Flask**, plain HTML, CSS and JavaScript.
No database and no extra frameworks.

```
personal_portfolio/
├── app.py                 <- ALL your text, links, skills and projects live here
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html         <- page layout (rarely needs editing)
└── static/
    ├── css/style.css      <- colors, spacing, responsive layout
    ├── js/script.js       <- mobile menu, fade-in, contact form
    ├── favicon.svg        <- browser tab icon
    ├── images/            <- profile photo + project screenshots
    └── resume/resume.pdf  <- your resume
```

---

## 1. Run it on your computer (VS Code)

Open the `personal_portfolio` folder in VS Code (**File > Open Folder**), then open the
terminal (**Terminal > New Terminal**).

### Create the virtual environment (once)

**Windows (PowerShell):**
```
python -m venv venv
venv\Scripts\Activate.ps1
```
If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.
(In Command Prompt use `venv\Scripts\activate.bat`.)

**macOS / Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

You will see `(venv)` at the start of the terminal line when it is active.
In VS Code, if asked to pick an interpreter, choose the one inside `venv`.

### Install dependencies (once)
```
pip install -r requirements.txt
```

### Start the website
```
python app.py
```

### Open it in the browser
Go to **http://127.0.0.1:5000**

Leave the terminal running. While it runs, every time you save a file the page reloads
(refresh the browser to see changes). Stop the server with **Ctrl + C**.

---

## 2. Things you MUST replace

| What | Where | How |
|------|-------|-----|
| Profile photo | `static/images/profile.jpg` | Replace the file. Keep the name. Best size: 600 x 750 px (portrait). |
| Project screenshots | `static/images/` | Replace `p1db-automation.png`, `psu-logger.png`, `referral-portal.png`, `electronics-projects.png`. Keep the names. Best size: 1200 x 750 px. |
| Resume PDF | `static/resume/resume.pdf` | Replace the file. Keep the name. |
| LinkedIn URL | `app.py`, top of file | Change `LINKEDIN_URL`. |
| GitHub URL | `app.py`, top of file | Change `GITHUB_URL`. |
| Email | `app.py`, top of file | Change `EMAIL`. |

The files currently there are **placeholders** that say "PLACEHOLDER" on them.
Do not publish the site until you have replaced them.

### Change LinkedIn, GitHub and email
Open `app.py`. Near the top you will see:

```python
LINKEDIN_URL = "ADD_MY_LINKEDIN_URL"
GITHUB_URL = "ADD_MY_GITHUB_URL"
EMAIL = "ADD_MY_EMAIL"
```

Replace the text inside the quotes, for example:

```python
LINKEDIN_URL = "https://www.linkedin.com/in/your-name"
GITHUB_URL = "https://github.com/your-username"
EMAIL = "you@example.com"
```

Save the file. The icons in the hero, the contact section and the footer all update
automatically. While a value still says `ADD_MY_...` the site shows a small "add your link"
hint instead of a broken link.

### Photos and screenshots
- Easiest way: save your image with **exactly the same file name** and replace the old one.
- Use `.png` or `.jpg`. Keep each image under about 300 KB so the site loads fast on mobile
  (free tools like squoosh.app can shrink them).
- Hardware/lab photos or GUI screenshots both work well. Remove any confidential or
  company-internal information from screenshots before publishing.
- Want a different file name or format? Change the `"image"` value of that project in `app.py`.

### Resume
Replace `static/resume/resume.pdf`. The "Download Resume" and "View Resume" buttons use it
automatically.

---

## 3. Change project, skill and experience text

Everything is in `app.py` as simple Python lists. You do not need to edit the HTML.

- **Projects:** find `PROJECTS = [ ... ]`. Each project is one block with `title`, `description`,
  `features`, `tech`, `image`, and `link`.
- **GitHub button on a project:** put your repository URL in that project's `"link"`.
  While `"link"` is empty (`""`) no button is shown.
- **Add a project:** copy a whole `{ ... },` block, paste it after the last one, then edit the text.
- **Skills:** edit the `SKILLS` list. Add or remove names inside `"items"`.
- **Experience:** edit `EXPERIENCE`. To add a job, copy the block and change it.
- **Education:** edit `EDUCATION`.
- **Intro text / title / SEO description:** edit `PROFILE` and `ABOUT`.

Save `app.py`, refresh the browser, and the changes appear.

---

## 4. How the contact form works

There is **no server code** for the form. When a visitor fills it in and presses the button,
their own email app opens with the message already written, addressed to your `EMAIL`.
This keeps the site simple and avoids spam and storing personal data.
The three direct links (email, LinkedIn, GitHub) work as well.

---

## 5. Colors and design

All colors are at the top of `static/css/style.css` under `/* 1. DESIGN TOKENS */`.
Change `--accent` (teal) and the `--navy-...` values to restyle the whole site in one place.

---

## 6. Before putting it online

1. Replace all placeholder images, the resume and the three links.
2. In `app.py`, set `SITE_URL = "https://your-site-address"` so link previews (Open Graph)
   work properly, and replace `static/images/og-image.png` (1200 x 630) with your own preview image.
3. In the last line of `app.py`, change `debug=True` to `debug=False`.
4. For real hosting, use a production server such as `gunicorn app:app` (Render, Railway,
   PythonAnywhere and similar services work well with Flask). Then paste the website address
   into the "Website" field of your LinkedIn profile.

## 7. Troubleshooting

- **`python` not found:** try `py` (Windows) or `python3` (macOS/Linux).
- **`No module named flask`:** the virtual environment is not active. Activate it and run `pip install -r requirements.txt` again.
- **Changes not showing:** hard-refresh the browser (Ctrl + F5).
- **Port already in use:** change the last line of `app.py` to `app.run(debug=True, port=5001)`.
