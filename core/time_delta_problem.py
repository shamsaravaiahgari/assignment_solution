from datetime import datetime
for _ in range(int(input())):
    date1 = datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")
    print(abs(int((date1-date2).total_seconds())))