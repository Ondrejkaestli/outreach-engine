import csv, datetime, pathlib
BASE = pathlib.Path(__file__).resolve().parents[1]
daily = BASE / "kpi_daily.csv"
week_ago = datetime.date.today() - datetime.timedelta(days=7)
visitors=clicks=sales=rev=0
by_channel={}
if daily.exists():
    with open(daily, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            d = datetime.date.fromisoformat(r["Date"])
            if d >= week_ago:
                visitors += int(r.get("Visitors",0) or 0)
                clicks   += int(r.get("Clicks",0) or 0)
                s = int(r.get("Sales",0) or 0); sales += s
                rev     += float(r.get("Revenue",0) or 0)
                ch = r.get("Channel","other")
                by_channel[ch]=by_channel.get(ch,0)+s
report = f"""Weekly KPIs
Visitors: {visitors}
Clicks:   {clicks}
Sales:    {sales}
Revenue:  CHF {rev:.2f}
Sales by channel: {by_channel}
"""
print(report)
(BASE / "queue" / "weekly_report.txt").write_text(report, encoding="utf-8")
