from datetime import date
import sys
year=date.today().year
before=date(year,3,20)
after=date(year,6,20) 

month=int(sys.argv[1])
day=int(sys.argv[2])

curr=date(year,month,day)

print(curr>before and curr<after)
