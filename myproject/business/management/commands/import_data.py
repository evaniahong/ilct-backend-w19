from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from business.models import Business
import csv
import pandas as pd

FILENAME = "./sample_data.csv"

mapping={
    "Business Name":"name",
    "GPS_X":"GPS_X",
    "GPS_Y":"GPS_Y",
    "Address":"Addr",
    "Student Discount":"Discount",
    "Phone Number":"Number",
}

keys = ["Business Name", "GPS_X", "GPS_Y", "Address", "Student Discount", "Phone Number"]

class Command(BaseCommand):
    help = 'importing data from file'

    def add_arguments(self, parser):
        parser.add_argument('--filename',default=FILENAME)
        parser.add_argument('--max', default=1000)

    @transaction.atomic
    def handle(self, *args, **options):
        filename = options['filename']
        limit = int(options['max'])

        try:
            data = pd.read_csv(filename)
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