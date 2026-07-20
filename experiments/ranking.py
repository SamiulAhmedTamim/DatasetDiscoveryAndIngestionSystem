import os
import sqlite3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB = os.path.join(ROOT, "deepshield.db")

print(DB)

conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor = conn.cursor()

cursor.execute("""

SELECT
title,
source,
quality_score,
trust_score,
ranking_score

FROM datasets

ORDER BY ranking_score DESC

LIMIT 20

""")

print("="*100)

print("TOP 20 DATASETS")

print("="*100)

for row in cursor.fetchall():

    title, source, quality, trust, ranking = row

    print(f"""

Title   : {title}
Source  : {source}
Quality : {quality}
Trust   : {trust:.2f}
Ranking : {ranking:.2f}

""")

conn.close()