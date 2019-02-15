from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from business.models import Business
import csv
import pandas as pd

keys = ["business_name","gps_x","gps_y","address","student_discount","phone_number"]

class Command(BaseCommand):
    help = 'returning information based on key-to-value query'

    def add_arguments(self, parser):
        parser.add_argument('--key', required = True)
        parser.add_argument('--value', required = True)

    @transaction.atomic
    def handle(self, *args, **options):
        key = options['key']
        value = options['value']
        if key not in keys:
            print("No matching keys!")
            return

        if (key == "business_name"): lst = Business.objects.filter(business_name=value)
        if (key == "gps_x"): lst = Business.objects.filter(gps_x=value)
        if (key == "gps_y"): lst = Business.objects.filter(gps_y=value)
        if (key == "address"): lst = Business.objects.filter(address=value)
        if (key == "student_discount"): lst = Business.objects.filter(student_discount=value)
        if (key == "phone_number"): lst = Business.objects.filter(phone_number=value)

        if len(lst) == 0: 
            print("No relevant business found")
        else:
            print("{} business found:".format(len(lst)))
            cnt = 0
            for business in lst: 
                print(business)


