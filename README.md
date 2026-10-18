# Waterside Stays

Website for Waterside Stays, short-let property care for landlords in Fulham & Chelsea.

## Editing

The page content lives in `src/page.html`. After changing it, run `python3 build.py` to regenerate `index.html`, which is the file GitHub Pages serves.

The enquiry form posts to `FORM_ENDPOINT` in the script at the bottom of the page. Leave it empty until a Formspree (or similar) form exists; until then the form asks visitors to email instead.
