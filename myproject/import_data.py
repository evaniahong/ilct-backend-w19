import pandas as pd
from business.models import Business

keys = ["Business Name", "GPS_X", "GPS_Y", "Address", "Student Discount", "Phone Number"]

try:
    filepath = "C:\\Users\\evani\\OneDrive\\Desktop\\ilct-backend-w19\\sample_data.csv"
    data = pd.read_csv(filepath)

except ImportError as exc:
    raise ImportError(
        "Couldn't import sample_data.csv"
    ) from exc

if sum(data.columns == keys) == len(data.columns):
    for i in range(0, len(data)):
        current_cell = data.iloc[i]

        b = Business(business_name = current_cell[0],
                     gps_x = str(current_cell[1]),
                     gps_y = str(current_cell[2]),
                     address = current_cell[3],
                     student_discount = current_cell[4],
                     phone_number = current_cell[5])
        try:
            b.save()
        except:
            print("error in importing item")
