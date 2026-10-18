# Wraps src/page.html into a standalone index.html for GitHub Pages.
from pathlib import Path
here = Path(__file__).parent
body = (here / "src/page.html").read_text()
head, _, rest = body.partition("</style>")
html = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + "</style>\n</head>\n<body>\n" + rest.lstrip() + "</body>\n</html>\n")
(here / "index.html").write_text(html)
