import csv, pathlib, datetime
BASE = pathlib.Path(__file__).resolve().parents[1]
queue = BASE / "queue" / "master-queue.csv"
ready_dir = BASE / "queue" / "ready"
ready_dir.mkdir(parents=True, exist_ok=True)

today = datetime.date.today().isoformat()
with open(queue, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        if row["date"] <= today:
            src = BASE / row["file"]
            text = src.read_text(encoding="utf-8")
            url = "https://ondrejkaestli.github.io/outreach-kit-site/" + row["utm"]
            out = ready_dir / f'{row["channel"]}-{pathlib.Path(row["file"]).stem}-{row["date"]}.txt'
            out.write_text(text.replace("{{SITE_URL}}", url), encoding="utf-8")
            print("Built:", out)
