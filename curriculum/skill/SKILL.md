---
name: curriculum-packet-generator
description: >
  Generate printable, TEKS-aligned weekly curriculum packets for homeschool families (grades K-5).
  Produces math and ELA worksheets matching the Skip School v4 design system and Ashley Larkin's
  quality bar. Use this skill for any request involving curriculum packets, worksheets, weekly
  packets, printable worksheets, TEKS-aligned content, homeschool curriculum, grade-level worksheets,
  or the curriculum subscription product.
---

# Curriculum Packet Generator

## Purpose

Generate weekly, printable, TEKS-aligned curriculum packets for Skip School's subscription product.
Output is structured JSON that feeds into the HTML template system (v4 design).

## Design System (v4, Approved)

### Two-Bar Header (every page)
- **Bar 1 (white):** Skip School logo top-left, "Grade X, Week Y, Subject" top-right
- **Bar 2 (colored):** Full-width subject banner with page title in white

### Five-Color System
- **Navy #0d203b:** Computation, number operations (addition, subtraction, multiplication, division)
- **Green #2c6e49:** Reading comprehension (fiction and nonfiction)
- **Coral #c44536:** Grammar, vocabulary, writing skills
- **Teal #1a7a6d:** Geometry, measurement, data and graphs
- **Purple #5b4a8a:** Fractions, money, time
- **Gold #b8860b:** Extension page (premium tier)

### Page Elements
- **Ashley's Tip:** Yellow-bordered box on first worksheet page only. 2-3 sentences, first person, practical.
- **Try This at Home:** Appears on EVERY worksheet page above the footer. Real-world activity tied to page content.
- **Footer:** Gold stars + learning tip + small faded Skip School logo
- **Extension Page:** Gold banner. Hands-on activities, field trips, family challenges tied to the week's content.

### Print Rules
- Every page must fit on exactly one 8.5x11 sheet
- Height fixed at 11in with overflow:hidden
- Content generation must be aware of page capacity
- If content exceeds one page, split at a logical break point

### Fonts
- Fraunces (serif): titles, Ashley's Tip header, banner titles
- DM Sans (sans-serif): all body text, problems, instructions

## Content Generation Rules

### Standards Alignment
- Every page cites specific TEKS standards in the header
- Standards come from references/teks-scope-sequence.md for the given grade and week
- Math and ELA are separate sections within each packet

### Difficulty Scaffolding
- Problems scaffold within each page: start accessible, build to challenge
- Star-marked challenge problems (2-3 per math page) for advanced students
- Grade K-2: simpler formats, more visual support
- Grade 3-5: STAAR-style questions, multi-step problems

### Personalization Tiers

**Tier 1 (Base, $19/mo):** Grade-level packet following scope and sequence. Generic name line.
**Tier 2 (Focus Track, $29/mo):** Base + 3-4 supplemental pages targeting parent-selected focus areas.
**Tier 3 (Personal Tutor, $49/mo):** Base + supplements + child's name in problems, difficulty calibrated to profile, learning style adaptations, monthly boost packet.

### Voice Rules (Kid-Facing)
- Clear, simple instructions
- Encouraging but not patronizing
- Footer tips teach a strategy
- No classroom language ("turn in your paper," "ask your teacher")
- Story problems use realistic homeschool-friendly scenarios

### Voice Rules (Ashley's Tips, Parent-Facing)
- First person
- Specific and practical
- Honest about difficulty
- 2-3 sentences max

### Anti-Patterns
- No visual-dependent problems that can't render in HTML/SVG
- No licensed characters or copyrighted content
- No ambiguous answers
- No repeating the same problem type for an entire page
- No content above grade-level decoding ability
- No em-dashes or double-dashes (use commas, colons, semicolons, periods)

## Output Format

Generate a JSON file that the template system converts to HTML:

```json
{
  "grade": 3,
  "week": 5,
  "date_range": "October 7-11, 2026",
  "child_name": null,
  "ashleys_tip": "This week we're...",
  "pages": [
    {
      "title": "Multiplication: 2s, 5s, and 10s",
      "subtitle": "Solve each problem. Build speed and accuracy!",
      "subject": "math",
      "color": "computation",
      "teks": "TEKS 3.4D, 3.4E",
      "try_this": {
        "icon": "lightbulb",
        "text": "Grab a bag of M&Ms and sort into equal groups..."
      },
      "footer_tip": "Multiplication is just skip counting!",
      "sections": [
        {
          "type": "section_header",
          "text": "Speed Round!"
        },
        {
          "type": "problems_grid",
          "columns": 4,
          "problems": ["1. 2x3=___", "2. 5x4=___", ...]
        },
        ...
      ]
    }
  ],
  "extension_page": {
    "activities": [...],
    "field_trips": [...],
    "family_challenge": {...}
  },
  "answer_key": [...]
}
```

## Section Types for JSON

- `section_header`: Bold header text
- `instruction`: Italic instruction text
- `remember_box`: Highlighted tip box with subject-color border
- `problems_grid`: Grid of problems (specify columns: 2, 3, or 4)
- `problems_list`: Vertical list of problems with answer blanks
- `story_problem`: Numbered story problem with equation/answer lines
- `passage`: Reading passage in bordered box
- `mc_questions`: Multiple choice questions with A-D options
- `sequence`: Number sequence with blanks
- `compare`: Comparison problems with circles for >, <, =
- `svg_shapes`: SVG geometry shapes with dimensions
- `svg_grid`: Grid squares for area counting
- `svg_clocks`: Clock faces for time problems

## References

- `references/teks-scope-sequence.md`: Full K-5 scope and sequence, 36 weeks per grade
- `references/page-templates.md`: Structural templates for every page type
- `references/focus-area-banks.md`: Problem banks for Tier 2 supplements
