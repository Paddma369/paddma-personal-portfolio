"""
Paddma Mal - Personal Engineering Portfolio
===========================================

A small Flask app that renders a single-page portfolio.

HOW THIS FILE IS ORGANISED
--------------------------
1. SOCIAL LINKS   -> edit these three lines first
2. SITE DATA      -> your name, projects, skills, experience (plain Python lists)
3. ROUTES         -> the tiny bit of Flask code that shows the page

Most of the time you only need to edit sections 1 and 2.
You do NOT need to touch the HTML to change text or projects.
"""

from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# 1. SOCIAL LINKS  (edit these)
# ---------------------------------------------------------------------------
LINKEDIN_URL = "https://www.linkedin.com/in/paddma-mal-5a9705202/"   # e.g. "https://www.linkedin.com/in/your-name"
GITHUB_URL = "https://github.com/Paddma369/P1-dB_Automation"       # e.g. "https://github.com/your-username"
EMAIL = "paddmamal347@gmail.com"                 # e.g. "name@example.com"

# Optional: public address of the site once deployed (used for sharing previews).
# Leave empty while developing locally.
SITE_URL = ""


def _is_placeholder(value: str) -> bool:
    """True while a link still contains the ADD_MY_... placeholder text."""
    return (not value) or value.startswith("ADD_MY")


# ---------------------------------------------------------------------------
# 2. SITE DATA  (edit these)
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Paddma Mal",
    "title": "RF Technician | RF Testing & Automation | Aerospace & Satellite Communication",
    "short_title": "RF Technician | RF Testing & Automation",
    "tagline": (
        "RF Technician with 5+ years of experience in RF testing, screening, "
        "troubleshooting and automation of aerospace and satellite communication hardware."
    ),
    "meta_description": (
        "Paddma Mal is an RF Technician with 5+ years of experience in RF testing, "
        "screening, troubleshooting and Python-based test automation for aerospace "
        "and satellite communication hardware."
    ),
    "keywords": (
        "RF Technician, RF Testing, RF Test Automation, Satellite Communication, "
        "Aerospace Electronics, PyVISA, Python, P1dB, S-Parameters, Environmental Screening"
    ),
}

ABOUT = {
    "intro": (
        "I work as an RF Technician in aerospace and satellite communication hardware "
        "testing. I also build Python-based engineering tools that make testing faster, "
        "more repeatable and better documented."
    ),
    "experience_points": [
        "RF module testing",
        "RF submodule testing",
        "Functional testing",
        "RF characterization",
        "Environmental screening",
        "Troubleshooting",
        "Test setup and fixture validation",
        "Test automation",
        "Measurement data logging",
        "Engineering software / GUI development",
    ],
    "closing": (
        "Working with both hardware and software gives me a practical view of the whole "
        "test process, from the bench setup to the final data log."
    ),
}

# Each group becomes one card in the Skills section.
# "icon" is the name of an inline SVG icon defined in templates/index.html.
SKILLS = [
    {
        "title": "RF & Microwave",
        "icon": "wave",
        "items": [
            "S-Parameters", "S11", "S21", "S22", "P1dB", "Noise Figure",
            "Insertion Loss", "Return Loss", "Output Power", "Isolation",
            "Harmonics", "Spurious", "IMD", "RF Matching",
        ],
    },
    {
        "title": "RF Test Equipment",
        "icon": "instrument",
        "items": [
            "VNA / PNA", "Signal Generator", "Spectrum Analyzer", "Power Sensor",
            "Oscilloscope", "DMM", "RF Test Fixtures",
        ],
    },
    {
        "title": "Testing & Screening",
        "icon": "chamber",
        "items": [
            "Functional Testing", "Stabilization Baking", "Temperature Cycling",
            "Burn-in / Operating Life", "Active Temperature Cycling", "TVAC",
            "Vibration Testing", "PIND", "Test Setup Validation", "Failure Analysis",
        ],
    },
    {
        "title": "Programming & Automation",
        "icon": "code",
        "items": [
            "Python", "Flask", "PyVISA", "GUI Development", "Instrument Control",
            "Excel Automation", "Data Logging", "Test Automation",
        ],
    },
    {
        "title": "Electronics",
        "icon": "chip",
        "items": [
            "Arduino", "ESP32", "Relay Control", "PSU Control",
            "DMM Measurement", "Test Jig Development",
        ],
    },
]

# Main projects. To add a project, copy one block and change the text.
# "image" is just a file name inside static/images/.
# "link" can be "" (no button) or a URL. Leave it "" until you have a GitHub link.
PROJECTS = [
    {
        "title": "RF P1dB Test Automation",
        "label": "RF Automation",
        "image": "p1db-automation.png",
        "image_alt": "Screenshot of the Python GUI used for automated RF P1dB measurement",
        "description": (
            "A Python-based GUI that automates RF P1dB measurements by controlling a "
            "signal generator and a spectrum analyzer over PyVISA."
        ),
        "features": [
            "Instrument detection",
            "Signal generator control",
            "Spectrum analyzer control",
            "RF power sweep",
            "P1dB measurement",
            "Cable-loss compensation",
            "Measurement logging",
            "Excel result generation",
            "Simulation mode for development",
        ],
        "tech": ["Python", "PyVISA", "RF Test Instruments", "Excel"],
        "link": "",
        "link_text": "View on GitHub",
        "note": "",
    },
    {
        "title": "Multi-PSU Monitoring & Logging System",
        "label": "Test Automation",
        "image": "psu-logger.png",
        "image_alt": "Screenshot of the multi-channel PSU monitoring and logging GUI",
        "description": (
            "A Python-based 3-channel PSU monitoring and logging GUI for test units "
            "during environmental testing, built to support multiple PSUs and "
            "multiple test units at the same time."
        ),
        "features": [
            "Multiple PSU detection",
            "Multi-unit monitoring",
            "Voltage monitoring",
            "Current monitoring",
            "Automatic logging",
            "Excel data storage",
            "Test data management",
            "User-friendly GUI",
        ],
        "tech": ["Python", "GUI Development", "PSU Instrument Control", "Excel"],
        "link": "",
        "link_text": "View on GitHub",
        "note": "",
    },
    {
        "title": "Personal Candidate Referral Portal",
        "label": "Web Development",
        "image": "referral-portal.png",
        "image_alt": "Screenshot of the candidate referral portal application form",
        "description": (
            "A web-based portal for collecting candidate applications and resumes."
        ),
        "features": [
            "Online application form",
            "Resume upload",
            "Database integration",
            "Admin dashboard",
            "Candidate search",
            "Application status management",
            "Duplicate detection",
            "Candidate consent",
            "Cloud deployment",
        ],
        "tech": ["Python", "Flask", "HTML", "CSS", "JavaScript", "Supabase"],
        "link": "",
        "link_text": "View Project",
        "note": "Personal project. Not an official company website.",
    },
]

# Smaller "secondary" projects shown in a compact block.
ELECTRONICS_PROJECT = {
    "title": "Electronics & Embedded Projects",
    "label": "Hardware",
    "image": "electronics-projects.png",
    "image_alt": "Arduino and ESP32 electronics prototyping setup",
    "description": "Hands-on hardware projects that connect electronics with test automation.",
    "items": [
        "Arduino relay control",
        "ESP32 projects",
        "Automated DUT switching",
        "PSU / DMM test jig concepts",
        "Rain Detection and Automated Clothes Collector",
    ],
}

EXPERIENCE = [
    {
        "role": "RF Technician",
        "company": "Centum Electronics Limited",
        "period": "September 2021 – Present",
        "points": [
            "Aerospace and satellite communication hardware testing",
            "RF module and submodule testing",
            "RF measurements and characterization",
            "Screening and environmental testing",
            "Test fixture and setup validation",
            "Troubleshooting and failure analysis",
            "Test automation and engineering GUI development",
            "Measurement data logging",
        ],
    },
]

EDUCATION = [
        {
        "degree": "Diploma — Computer Science & Technology",
        "detail": "PASSOUT 2021",
    },
    {
        "degree": "B.Tech — Electronics & Communication Engineering",
        "detail": "Expected completion: 2027",
    },
]

# File names (inside static/). Replace the files, keep the names.
PROFILE_IMAGE = "images/profile.jpeg"
RESUME_FILE = "resume/resume.pdf"


# ---------------------------------------------------------------------------
# 3. ROUTES
# ---------------------------------------------------------------------------
@app.context_processor
def inject_site_data():
    """Makes these variables available in every template."""
    links = {
        "linkedin": LINKEDIN_URL,
        "github": GITHUB_URL,
        "email": EMAIL,
    }
    return {
        "profile": PROFILE,
        "about": ABOUT,
        "skills": SKILLS,
        "projects": PROJECTS,
        "electronics": ELECTRONICS_PROJECT,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "profile_image": PROFILE_IMAGE,
        "resume_file": RESUME_FILE,
        "links": links,
        # True when a link is still a placeholder (the template then shows a hint
        # instead of a broken link).
        "link_ready": {k: not _is_placeholder(v) for k, v in links.items()},
        "site_url": SITE_URL.rstrip("/"),
        "year": datetime.now().year,
    }


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # debug=True reloads the page automatically when you save a file.
    # Turn it OFF (debug=False) before deploying to the internet.
    app.run(debug=True)
