import csv
def blankNum(value):
    if value == '' or value == '-':
        return 0
    else:
        return float(value)

with open("Dec 11. Data for Seed Script - Sheet1.csv") as f:
    reader = csv.reader(f)
    with open(r"C:\Users\Hp\PyCharmProjects\pythonProject9\project.txt" , 'a') as textFile:
        for i in reader:
            textFile.write(f'''\n\n\tBrand.objects.create(name='{i[0]}', price_range={blankNum(i[1])}, urls=['{i[2]}'], parent_company='{i[3]}',\\
            planet_goy_rating = {blankNum(i[4])}, animal_goy_rating = {blankNum(i[6])}, people_goy_rating = {blankNum(i[5])},\\
            policy_fti_rating = {blankNum(i[7])}, governance_fti_rating = {blankNum(i[8])}, knowshow_fti_rating = {blankNum(i[9])}, \\
            spotlight_fti_rating = {blankNum(i[10])}, traceability_fti_rating = {blankNum(i[11])}, \\
            goy_link='{i[12]}', location='{i[13]}')''')
