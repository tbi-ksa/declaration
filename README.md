# TBI — Entrepreneur declaration of experience

Single-page tool at [tbi-ksa.github.io/declaration/](https://tbi-ksa.github.io/declaration/). A service of **TBI Saudi Executive Education** for applicants to the Executive UK PGDBM programme (Pearson UK Level 7), delivered with B International Management Consulting.

## What it does

An applicant fills the declaration of experience required for admission, prints it on their own company letterhead, signs it, stamps it and saves a PDF — entirely in the browser. Nothing is uploaded to a server.

| Step | What happens |
|------|--------------|
| **Your details** | Cohort (Jeddah · Riyadh · Dammam), name, company, industry, years, designation, place, date. Programme wording is editable per cohort. |
| **Company letterhead** | Upload a letterhead PDF; the letter prints on page 1. The header and footer are detected automatically and the text start position defaults from them; a slider keeps manual control. |
| **Signature and stamp** | Draw, type or upload a signature, or sign from a phone (scan the QR code, sign with a finger, the signature lands on the desktop). Upload a stamp image; white background is removed on export. Both are dragged into position on the live preview. |
| **Review and export** | Checklist of every blank, then a signed PDF named `Declaration-of-Experience-<name>-<date>.pdf`. |

Every PDF carries a **document ID** in its footer — a SHA-256 over the recorded fields and digests of the signature, stamp and letterhead — with the same record embedded in the PDF metadata. The "Verify a received PDF" panel in step 4 lets admissions confirm a received file's record matches its ID. This is an integrity check against edited copies, not a cryptographic signature.

## Phone signing

Exact procedure, as shown on the page under "How phone signing works":

1. **Scan the QR code** with the phone camera. It opens the page on the phone in signing mode with the pairing code filled in (`#sign=<code>` in the address). Fallback: open the page on the phone, tap "signing from a phone?" in the header, type the code.
2. **The phone announces itself.** With a valid code present it publishes a "connected" ping; the desktop status changes to "Phone connected".
3. **Sign with a finger** in the box. Clear and redo freely; nothing is sent until step 4.
4. **Tap "Send to desktop".** The phone publishes the pen strokes (quantised coordinates, a few kilobytes, chunked at 3000 characters) under the pairing code. No image, letterhead or applicant details leave the phone.
5. **The desktop redraws the strokes** at 1200 px wide into the signature image, places it above the "Signature" line and shows "Signature received". "New code" pairs again.

The desktop shows a QR code and a 6-character pairing code. The phone opens the page with `#sign=<code>`, records the pen strokes and sends them as a few kilobytes of coordinates; the desktop redraws them into the signature image. Transport is a public pub/sub relay (`RELAY` in `index.html`, currently `https://ntfy.sh`), used with `Cache: no` so nothing is stored on the relay; only strokes travel, never the PDF, the letterhead or the applicant's details. The topic is `tbi-decl-<code>` with a 32-character alphabet, so a code is not guessable in practice. To bring the relay in-house, point `RELAY` at a self-hosted ntfy instance; the page needs no other change.

## Build

There is no build. `index.html` is the whole site; `fonts/` holds the self-hosted brand faces. Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8080
```

Libraries load from cdnjs at pinned versions: pdf-lib 1.17.1 (PDF assembly), pdf.js 3.11.174 (live preview), qrcodejs 1.0.0 (pairing QR).

## Deploy

GitHub Actions (`.github/workflows/deploy.yml`) publishes the repository root to GitHub Pages on push to `main`.

## Editing the letter

The declaration text lives in `runs()` inside `index.html`. Cohort places are in `COHORTS`; default programme wording is in `DEFAULT_WORDING`. Layout metrics (Times 11.5 pt, 1.55 line height, margins) are in `buildPdf()` — the preview renders the same PDF, so what is seen is what prints.

## Design

Tokens are derived from the TBI design system source-of-truth at `~/.claude/skills/tbi-design/colors_and_type.css`: navy `#091E3D`, accent blue `#0068A8`, gold `#D4A843` for the export action, Avenir Next for headings, Segoe UI for body, Klein Bold for eyebrows.

## Voice rules (from `tbi-design`)

Sentence case. No exclamation marks, no superlatives. Quiet verb-led CTAs — "Save signed PDF", "Use this signature" — never "Learn more" or "Click here". No emoji.

## Related

- [tbi-ksa/insights](https://github.com/tbi-ksa/insights) — TBI Research, market-signal insights and capability guides.

## Source

`src/declaration.html` is the shared source (also published as the claude.ai artifact, where phone signing uses the artifact database). `index.html` is generated from it:

```bash
python3 src/build-pages.py index.html
```
