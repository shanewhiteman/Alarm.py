# Command-Line Alarm clock
# Todo: 
# - get date and time
# - implement args

from datetime import datetime
import sys
import argparse

VERSION = f"{sys.argv[0]} VERSION 1.0.0"

def argParse():
    parser = argparse.ArgumentParser(usage=f"{sys.argv[0]} [OPTION]", description="Command-Line Alarm Clock", formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50))
    parser.add_argument("-12", "--standard", help="use standard time in HH:MM AM/PM format ex: 1:38 PM", metavar="TIME", required=False, type=str)
    parser.add_argument("-24", "--military", help="use military time in HH:MM AM/PM format ex: 13:38 PM", metavar="TIME", required=False, type=str)
    parser.add_argument("-v", "--version", help="view version of alarm.py", action="store_true", required=False)
    args = parser.parse_args()

    if args.standard:
        print(f"{sys.arg[2]}")
        validate_standard()

    if args.military:
        print(f"{sys.argv[2]}")

    if args.version:
        print(VERSION)
        get_time()

    if len(sys.argv) > 4:
        parser.print_help()
        sys.exit(1)

def get_time():
    now = datetime.now()

    current_time = now.strftime("%I:%M %p")
    print(current_time)

#def alarm_ring():
    #futuretime = datetime.time(arr)

    #ringtime = futuretime.strftime("%-I:%M %p")
    #print(ringtime)

def validate_standard():
    alarm_time = sys.argv[2]

    if len(alarm_time) != 8:
        return "Invalid time format!"
    
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format!"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format!"
        elif alarm_time[6:7] != ('AM' or 'PM'):
            return "Please add AM or PM!"
        else:
            return "ring"

def main():
    argParse()

main()
