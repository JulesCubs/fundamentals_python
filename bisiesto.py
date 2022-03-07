def isYearLeap(year):
    if year % 4 == 0 or year % 100 == 0 or year % 400 :
        return True
    else:
        return False

def daysInMonth(year, month):
    if isYearLeap(year) and month == 2:
        return 29
    elif month == 2:
            print("Entra a febrero", month)
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11 :
        return 30
    else: 
        return 31

def dayOfYear(year, month, day):
    result = 0
    for i in range(1, month) :
        result += daysInMonth(year, i)
    
    return result + day


print(dayOfYear(2000, 12, 31))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	day = testResults [i]
	print(yr, mo, day, "->", end="")
	result = dayOfYear(yr, mo, day)
	print("El dia del año es:", result)
	# result = daysInMonth(yr, mo)
    # 	if result == testResults[i]:
    # 		print("OK")
    # 	else:
    # 		print("Error")