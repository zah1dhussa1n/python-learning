import csv
with open("final2csv.csv","w") as final2csv:
    spamwriter=csv.writer(final2csv,delimiter=",")
    spamwriter.writerow(["Punjab","balochistan","kalat","kharan"])
    spamwriter.writerow(["KPK","sindh","gilgit","kaaan","kharkan"])
