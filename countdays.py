from datetime import date

print("Welcome to days' counter :)")

year = int(input('Enter the year of your date: '))
month = int(input('Enter the month of your date: '))
day = int(input('Enter the day of your date: '))
occasion = input('What is your occasion? ')

print('Your date is: '+str(year)+'/'+str(month)+'/'+str(day))

today = date.today()
specified_date = date(year,month,day)
occasion_day = (specified_date - today).days

if occasion_day > 1:
    print('The remaining days for your ' + occasion + ' are: ' + str(occasion_day) + ' days')
elif occasion_day == 1:
    print('Be patient! your '+ occasion + ' will be Tomorrow')
elif occasion_day < 1 and occasion_day == 0:
    print('Congratulations! your ' + occasion + ' is Today!')
else:
    print('Wrong date! try again please')
