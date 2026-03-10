#!/usr/bin/env python3
"""
Skip School Curriculum Packet Generator
========================================
Reads a JSON content file and produces a styled HTML worksheet packet
matching the v4 design system.

Usage:
    python generate_packet.py content.json output.html [--logo-path /path/to/logo.png]

The JSON format is defined in curriculum/skill/SKILL.md.
The HTML template is in curriculum/templates/worksheet-template.html.
"""

import json
import sys
import os
import base64
import argparse
from pathlib import Path

# Color mapping
COLORS = {
    "computation": "clr-computation",
    "reading": "clr-reading",
    "grammar": "clr-grammar",
    "geometry": "clr-geometry",
    "fractions": "clr-fractions",
    "extensions": "clr-extensions",
}

ACCENT_COLORS = {
    "computation": "#0d203b",
    "reading": "#2c6e49",
    "grammar": "#c44536",
    "geometry": "#1a7a6d",
    "fractions": "#5b4a8a",
    "extensions": "#b8860b",
}

TRY_THIS_ICONS = {
    "lightbulb": "&#128161;",
    "book": "&#128218;",
    "speech": "&#128172;",
    "pencil": "&#9999;&#65039;",
    "star": "&#11088;",
    "magnify": "&#128269;",
    "plant": "&#127793;",
    "game": "&#127922;",
}


def get_logo_b64(logo_path):
    """Read logo file and return base64 string."""
    if not logo_path or not os.path.exists(logo_path):
        return ""
    with open(logo_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_section(section, accent_color):
    """Render a single content section to HTML."""
    t = section["type"]
    html = ""

    if t == "section_header":
        html = f'<div class="sh">{section["text"]}</div>\n'

    elif t == "instruction":
        html = f'<div class="inst">{section["text"]}</div>\n'

    elif t == "remember_box":
        html = f'<div class="rembox" style="border-left-color:{accent_color};"><strong>{section.get("label", "Remember:")}</strong> {section["text"]}</div>\n'

    elif t == "problems_grid":
        cols = section.get("columns", 4)
        cls = f"g{cols}"
        html = f'<div class="{cls}">\n'
        for p in section["problems"]:
            html += f'<div class="pc">{p}</div>\n'
        html += '</div>\n'

    elif t == "problems_list":
        for p in section["problems"]:
            html += f'<div class="pc" style="line-height:2;">{p}</div>\n'

    elif t == "story_problem":
        for sp in section["problems"]:
            html += f'<div class="sp">\n'
            html += f'<span class="sn" style="color:{accent_color};">#{sp["number"]}</span> {sp["text"]}\n'
            if sp.get("equation_line", True):
                html += '<div class="al">Equation: <span class="abl"></span></div>\n'
            if sp.get("answer_line", True):
                html += '<div class="al">Answer: <span class="abl"></span></div>\n'
            html += '</div>\n'

    elif t == "passage":
        html = '<div class="pbox">\n'
        for para in section["paragraphs"]:
            html += f'<p>{para}</p>\n'
        html += '</div>\n'

    elif t == "mc_questions":
        for q in section["questions"]:
            html += f'<div class="mcq"><div class="qt">{q["number"]}. {q["text"]}</div><div class="opts">\n'
            for opt in q["options"]:
                html += f'<div>{opt}</div>\n'
            html += '</div></div>\n'

    elif t == "sequence":
        for s in section["sequences"]:
            html += f'<div class="seq">{s}</div>\n'

    elif t == "compare":
        cols = section.get("columns", 4)
        cls = f"g{cols}"
        html = f'<div class="{cls}">\n'
        for c in section["comparisons"]:
            html += f'<div class="pc">{c}</div>\n'
        html += '</div>\n'

    elif t == "svg_shapes":
        html = '<div style="display:flex;justify-content:space-between;margin:8px 0;">\n'
        for shape in section["shapes"]:
            html += f'<div style="text-align:center;">\n'
            html += f'<div style="color:{accent_color};font-weight:700;font-size:11pt;">#{shape["number"]}</div>\n'
            html += shape["svg"] + '\n'
            html += f'<div style="font-size:10pt;text-align:left;padding-left:4px;">{shape["answer_lines"]}</div>\n'
            html += '</div>\n'
        html += '</div>\n'

    elif t == "svg_grid":
        html = shape_data = section.get("svg", "")
        if "label" in section:
            html = f'<div class="sh">{section["label"]}</div>\n'
            html += f'<div style="display:flex;align-items:center;gap:20px;margin:6px 0;">{section["svg"]}'
            html += f'<div style="font-size:11pt;">{section["answer_text"]}</div></div>\n'

    return html


def render_page(page, grade, week, logo_b64, footer_logo_b64, ashleys_tip=None, is_first=False):
    """Render a single worksheet page to HTML."""
    color_class = COLORS.get(page["color"], "clr-computation")
    accent = ACCENT_COLORS.get(page["color"], "#0d203b")
    subject_label = page.get("subject", "Math").capitalize()

    logo_img = f'<img class="logo" src="data:image/png;base64,{logo_b64}" alt="Skip School">' if logo_b64 else '<span style="font-weight:800;font-size:14pt;"><span style="color:#fbc926;">SKIP</span><span style="color:#0d203b;">SCHOOL</span></span>'
    footer_logo = f'<img class="fl" src="data:image/png;base64,{footer_logo_b64}" alt="">' if footer_logo_b64 else ''

    html = f'<div class="page" style="--ac:{accent};">\n'

    # Logo bar
    html += f'<div class="logo-bar">{logo_img}<span class="gw">Grade {grade} &middot; Week {week} &middot; {subject_label}</span></div>\n'

    # Subject banner
    html += f'<div class="subject-bar {color_class}"><h1>{page["title"]}</h1>'
    if page.get("subtitle"):
        html += f'<div class="sub">{page["subtitle"]}</div>'
    html += '</div>\n'

    # Content area
    html += '<div class="page-inner">\n'

    # Name/Date
    html += '<div class="nd"><span><span class="l">Name:</span> <span class="b n"></span></span><span><span class="l">Date:</span> <span class="b d"></span></span></div>\n'

    # Ashley's tip (first page only)
    if is_first and ashleys_tip:
        html += f'<div class="atip"><div class="ah">Ashley\'s Note:</div><div class="at">{ashleys_tip}</div></div>\n'

    # Sections
    for section in page.get("sections", []):
        html += render_section(section, accent)

    html += '</div>\n'  # end page-inner

    # Try This box
    if page.get("try_this"):
        icon = TRY_THIS_ICONS.get(page["try_this"].get("icon", "lightbulb"), "&#128161;")
        html += f'<div class="trybox"><span class="tryicon">{icon}</span><div><div class="trylabel">Try This at Home</div><div class="trytext">{page["try_this"]["text"]}</div></div></div>\n'

    # Footer
    html += f'<div class="footer"><span class="st">&#9733;</span><span class="tip">{page.get("footer_tip", "")}</span>{footer_logo}</div>\n'
    html += '</div>\n'  # end page

    return html


def render_cover(data, logo_b64, footer_logo_b64):
    """Render the cover page."""
    logo_img = f'<img class="cl" src="data:image/png;base64,{logo_b64}" alt="Skip School">' if logo_b64 else ''
    footer_logo = f'<img class="fl" src="data:image/png;base64,{footer_logo_b64}" alt="">' if footer_logo_b64 else ''

    math_focus = ""
    ela_focus = ""
    for p in data.get("pages", []):
        if p.get("subject") == "math" and not math_focus:
            math_focus = p["title"]
        elif p.get("subject") == "ela" and not ela_focus:
            ela_focus = p["title"]

    page_count = len(data.get("pages", []))
    has_ext = "extension_page" in data and data["extension_page"]
    ext_text = " + extensions" if has_ext else ""

    html = '<div class="page">\n<div class="cover-inner">\n'
    html += f'{logo_img}\n'
    html += '<div class="ctag">Weekly Curriculum Packet</div>\n'
    html += '<div class="cdiv"></div>\n'
    html += f'<div class="ct">Grade {data["grade"]}: Math + ELA</div>\n'
    html += f'<div class="cs">Week {data["week"]} &middot; {data.get("date_range", "")}</div>\n'
    html += '<div class="cdet">\n'
    html += f'<div class="cdr"><span class="cl2">Student</span><span class="cv">_____________________</span></div>\n'
    if math_focus:
        html += f'<div class="cdr"><span class="cl2">Math Focus</span><span class="cv">{math_focus}</span></div>\n'
    if ela_focus:
        html += f'<div class="cdr"><span class="cl2">ELA Focus</span><span class="cv">{ela_focus}</span></div>\n'
    html += f'<div class="cdr"><span class="cl2">Pages</span><span class="cv">{page_count} worksheets{ext_text}</span></div>\n'

    # Collect TEKS
    all_teks = set()
    for p in data.get("pages", []):
        if p.get("teks"):
            all_teks.add(p["teks"])
    if all_teks:
        html += f'<div class="cdr"><span class="cl2">Standards</span><span class="cv">{", ".join(sorted(all_teks)[:4])}</span></div>\n'

    html += '</div>\n'  # end cdet
    html += '</div>\n'  # end cover-inner
    html += f'<div class="footer"><span class="st">&#9733;</span><span class="tip">skipschool.ai &middot; Aligned to Texas TEKS</span>{footer_logo}</div>\n'
    html += '</div>\n'  # end page

    return html


def render_extension_page(ext_data, grade, week, logo_b64, footer_logo_b64):
    """Render the extension page."""
    logo_img = f'<img class="logo" src="data:image/png;base64,{logo_b64}" alt="Skip School">' if logo_b64 else ''
    footer_logo = f'<img class="fl" src="data:image/png;base64,{footer_logo_b64}" alt="">' if footer_logo_b64 else ''

    html = '<div class="page" style="--ac:#b8860b;">\n'
    html += f'<div class="logo-bar">{logo_img}<span class="gw">Grade {grade} &middot; Week {week} &middot; Extensions</span></div>\n'
    html += '<div class="subject-bar clr-extensions"><h1>This Week\'s Extensions</h1><div class="sub">Real-world activities, field trips, and family challenges.</div></div>\n'
    html += '<div class="page-inner">\n'
    html += '<div class="nd"><span><span class="l">Name:</span> <span class="b n"></span></span><span><span class="l">Date:</span> <span class="b d"></span></span></div>\n'

    for act in ext_data.get("activities", []):
        html += '<div class="ext-item">\n'
        html += f'<div class="ext-subj">{act["subject"]}</div>\n'
        html += f'<div class="ext-title">{act["title"]}</div>\n'
        html += f'<div class="ext-desc">{act["description"]}</div>\n'
        html += '</div>\n'

    for ft in ext_data.get("field_trips", []):
        html += '<div class="ext-fieldtrip">\n'
        html += f'<div class="ft-label">{ft.get("icon", "&#127793;")} {ft.get("label", "Field Trip Idea")}</div>\n'
        html += f'<div class="ft-title">{ft["title"]}</div>\n'
        html += f'<div class="ft-desc">{ft["description"]}</div>\n'
        html += '</div>\n'

    if ext_data.get("family_challenge"):
        fc = ext_data["family_challenge"]
        html += '<div class="ext-item">\n'
        html += f'<div class="ext-subj">&#127942; Family Challenge</div>\n'
        html += f'<div class="ext-title">{fc["title"]}</div>\n'
        html += f'<div class="ext-desc">{fc["description"]}</div>\n'
        html += '</div>\n'

    html += '</div>\n'  # end page-inner
    html += f'<div class="footer"><span class="st">&#9733;</span><span class="tip">Learning doesn\'t stop at the worksheet. The best lessons happen in the real world!</span>{footer_logo}</div>\n'
    html += '</div>\n'  # end page

    return html


def generate_packet(content_path, output_path, logo_path=None, footer_logo_path=None):
    """Main generation function."""
    with open(content_path, 'r') as f:
        data = json.load(f)

    # Load logos
    logo_b64 = get_logo_b64(logo_path)
    footer_logo_b64 = get_logo_b64(footer_logo_path)

    # Load template
    template_dir = Path(__file__).parent.parent / "templates"
    template_path = template_dir / "worksheet-template.html"
    with open(template_path, 'r') as f:
        template = f.read()

    # Build pages HTML
    pages_html = ""

    # Cover page
    pages_html += render_cover(data, logo_b64, footer_logo_b64)

    # Worksheet pages
    for i, page in enumerate(data.get("pages", [])):
        pages_html += render_page(
            page,
            grade=data["grade"],
            week=data["week"],
            logo_b64=logo_b64,
            footer_logo_b64=footer_logo_b64,
            ashleys_tip=data.get("ashleys_tip") if i == 0 else None,
            is_first=(i == 0),
        )

    # Extension page
    if data.get("extension_page"):
        pages_html += render_extension_page(
            data["extension_page"],
            grade=data["grade"],
            week=data["week"],
            logo_b64=logo_b64,
            footer_logo_b64=footer_logo_b64,
        )

    # Fill template
    title = f"Skip School Grade {data['grade']} Week {data['week']}"
    output_html = template.replace("{{PACKET_TITLE}}", title)
    output_html = output_html.replace("{{PAGES}}", pages_html)

    with open(output_path, 'w') as f:
        f.write(output_html)

    print(f"Generated: {output_path}")
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Skip School curriculum packet")
    parser.add_argument("content", help="Path to JSON content file")
    parser.add_argument("output", help="Output HTML path")
    parser.add_argument("--logo", help="Path to header logo PNG", default=None)
    parser.add_argument("--footer-logo", help="Path to footer logo PNG", default=None)
    args = parser.parse_args()

    generate_packet(args.content, args.output, args.logo, args.footer_logo)
