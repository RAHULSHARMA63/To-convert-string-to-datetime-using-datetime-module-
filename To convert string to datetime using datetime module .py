from datetime import datetime

my_date_string = "Mar 1 2021 11:51AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)