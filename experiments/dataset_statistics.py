import sqlite3
import statistics

DB = "deepshield.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

print("=" * 60)
print("DeepShield Dataset Statistics")
print("=" * 60)

# --------------------------------------------------
# Total datasets
# --------------------------------------------------
cursor.execute("SELECT COUNT(*) FROM datasets")
total = cursor.fetchone()[0]

print(f"Total datasets : {total}")

# --------------------------------------------------
# Source Distribution
# --------------------------------------------------
print("\nSource Distribution")
print("-" * 40)

cursor.execute("""
SELECT source, COUNT(*)
FROM datasets
GROUP BY source
ORDER BY COUNT(*) DESC
""")

rows = cursor.fetchall()

for source, count in rows:
    print(f"{source:20} {count}")

# --------------------------------------------------
# Average Quality Score
# --------------------------------------------------
cursor.execute("""
SELECT AVG(quality_score)
FROM datasets
""")

avg_quality = cursor.fetchone()[0]

print("\nAverage Quality Score :", round(avg_quality,2))

# --------------------------------------------------
# Average Trust Score
# --------------------------------------------------
cursor.execute("""
SELECT AVG(trust_score)
FROM datasets
""")

avg_trust = cursor.fetchone()[0]

print("Average Trust Score   :", round(avg_trust,2))

# --------------------------------------------------
# Quality Statistics
# --------------------------------------------------
cursor.execute("""
SELECT quality_score
FROM datasets
""")

qualities = [x[0] for x in cursor.fetchall()]

print("\nQuality Statistics")
print("-"*40)

print("Minimum :", min(qualities))
print("Maximum :", max(qualities))
print("Median  :", statistics.median(qualities))
print("Std Dev :", round(statistics.stdev(qualities),2))

# --------------------------------------------------
# Trust Statistics
# --------------------------------------------------
cursor.execute("""
SELECT trust_score
FROM datasets
""")

trusts = [x[0] for x in cursor.fetchall()]

print("\nTrust Statistics")
print("-"*40)

print("Minimum :", round(min(trusts),2))
print("Maximum :", round(max(trusts),2))
print("Median  :", round(statistics.median(trusts),2))
print("Std Dev :", round(statistics.stdev(trusts),2))

# --------------------------------------------------
# Top 10 Highest Trust
# --------------------------------------------------
print("\nTop 10 Trusted Datasets")
print("-"*70)

cursor.execute("""
SELECT title,
       source,
       trust_score
FROM datasets
ORDER BY trust_score DESC
LIMIT 10
""")

for title, source, trust in cursor.fetchall():
    print(f"{trust:6.2f} | {source:15} | {title}")

# --------------------------------------------------
# Top 10 Highest Quality
# --------------------------------------------------
print("\nTop 10 Quality Datasets")
print("-"*70)

cursor.execute("""
SELECT title,
       source,
       quality_score
FROM datasets
ORDER BY quality_score DESC
LIMIT 10
""")

for title, source, score in cursor.fetchall():
    print(f"{score:3} | {source:15} | {title}")

# --------------------------------------------------
# Modality Distribution
# --------------------------------------------------
print("\nDataset Modality")
print("-"*40)

cursor.execute("""
SELECT modality,
       COUNT(*)
FROM datasets
GROUP BY modality
ORDER BY COUNT(*) DESC
""")

for modality, count in cursor.fetchall():
    print(f"{str(modality):20} {count}")

# --------------------------------------------------
# Task Distribution
# --------------------------------------------------
print("\nTask Distribution")
print("-"*40)

cursor.execute("""
SELECT task,
       COUNT(*)
FROM datasets
GROUP BY task
ORDER BY COUNT(*) DESC
""")

for task, count in cursor.fetchall():
    print(f"{str(task):25} {count}")

# --------------------------------------------------
# Recent datasets
# --------------------------------------------------
print("\nMost Recent Datasets")
print("-"*70)

cursor.execute("""
SELECT title,
       updated
FROM datasets
ORDER BY updated DESC
LIMIT 10
""")

for title, updated in cursor.fetchall():
    print(updated, "|", title)

conn.close()

print("\nDone.")