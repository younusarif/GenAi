# Use case Nested Loop - Create report for each day in a month 
years = [2026,2027]
months =['Jan','Feb']
daays= range(1,29)
for y in years:
    for m in months:
        for d in daays:
            print(f'report-{y}-{m}-{d}.csv')

# Create SQl query using python
# Select count(*) FROM customers where id is NULL;
# Solve this query of SQL with Nested Loop
tables = ['customers','orders','products','prices']
columns =['id','create_date']
for t in tables:
    for c in columns:
        print(f'Select count (*) FROM {t} WHERE {c} is NULL; ') 