domains = ['www.gooogle.com',
            'openai.com',
            'localhost',
            'WWW.YOUNUS.COM']

cleaned =[
    # Data Transformation- Step 2
    d.lower().replace('www.','')

    # For Loop -step 1
    for d in domains

    # Data Filtering -Step 3 but Optional
    if '.' in d

]

print(cleaned)