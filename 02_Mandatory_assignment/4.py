#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
d = {
    "date": 8,
    "month": "Mar",
    "year": 85
}

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

print(d["date"],'-', month_converter(d["month"]),'-', d["year"])

#Create a dict suitable for decoding month names to numbers.

date_Decoder = {
    "date": 8,
    "month": "Mar",
    "year": 85
}

#Create a function which uses string operations to split the date into 3 items using the "-" character.
def myfunktion(date_Decoder):
    x1 = date_Decoder.get("date")
    x2 = date_Decoder.get("month")
    x3 = date_Decoder.get("year")
    print(x1,"-",x2,"-",x3) 
myfunktion(date_Decoder)

#Translate the month, correct the year to include all of the digits.

 

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).