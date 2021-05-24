# Command-Line Alarm clock for Windows
# Todo: 
# - get date and time
# - implement args

from datetime import datetime
import sys
import argparse

def argParse():
    parser = argparse.ArgumentParser(usage=f"{sys.argv[0]} [OPTION]", description="Command-Line Alarm Clock", formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50))
    parser.add_argument("-12", "--standard", nargs=2, help="use standard time in HH:MM AM/PM format ex: 1:38 PM", metavar=("TIME", "TYPE"), required=False, type=str)
    parser.add_argument("-24", "--military", help="use military time in HH:MM format ex: 13:38", metavar="TIME", required=False, type=str)
    parser.add_argument("-c", "--current", help="returns current time", action="store_true", required=False)
    args = parser.parse_args()

    if args.standard:
        #print(f"{sys.argv[2]} {sys.argv[3]}")
        validate_standard(parser)

    if args.military:
        #print(f"{sys.argv[2]}")
        validate_military(parser)

    if args.current:
        currentTime = get_timeNow()
        print(currentTime)

    if len(sys.argv) > 4:
        parser.print_help()
        sys.exit(1)

def get_timeNow():
    now = datetime.now()

    currentTime = now.strftime("%#I:%M %p") # '#' for windows decimal values without the padded 0.
    return currentTime

def validate_standard(parser):
    alarmTime = sys.argv[2]
    typography = sys.argv[3]

    if len(alarmTime) > 5:
        #print("length error")
        return parser.print_help()
    
    elif int(alarmTime[0:2]) > 12:
        #print("hour error")
        return parser.print_help()

    elif int(alarmTime[3:5]) > 59:
        #print("minute error")
        return parser.print_help()

    elif not(typography == 'AM' or typography == 'PM'):
        #print("typography error")
        return parser.print_help()
    
    alarmTime = f"{alarmTime} {typography}"
    #set_alarm(alarmTime)

def validate_military(parser):
    alarmTime = sys.argv[2]

    if len(alarmTime) > 5:
        return parser.print_help()
    
    elif int(alarmTime[0:2]) > 24:
        return parser.print_help()

    elif int(alarmTime[3:5]) > 59:
        return parser.print_help()
    
    #set_alarm(alarmTime)

#def set_alarm(alarmTime):
    #print("Alarm set")

    #currentTime = get_timeNow()

    #while True:
        #if alarmTime == currentTime:
            #print("ring")
        #else:
            #continue
    
def main():
    argParse()

main()
