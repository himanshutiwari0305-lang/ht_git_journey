import csv

with open("FileHandling/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])   # header
    writer.writerow(["Himanshu", 45, "Delhi NCR"])
    writer.writerow(["Rekha", 40, "Delhi NCR"])
    writer.writerow(["MataRani", 65, "Delhi NCR"])
    writer.writerow(["Reyansh", 10, "Delhi NCR"])
    writer.writerow(["Shreyas", 5, "Delhi NCR"])
