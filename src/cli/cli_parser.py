import argparse


parser = argparse.ArgumentParser(description = 'Get weather data from wttr.com'
                                               ' and save to a json file',
                                 epilog = 'Enjoy the the weather and the program :)')

parser.add_argument('-c',
                    '--city',
                    action='store',
                    type=str,
                    default='Miskolc',
                    metavar='',
                    help='sets the city for which you want weather data (default Miskolc)')
parser.add_argument('-s',
                    '--saveto',
                    action='store',
                    type=str,
                    default='weatherdata',
                    metavar='',
                    help='set the json output file name (default filename: weatherdata)')

args = parser.parse_args()

city_name = args.city
json_file = args.saveto+".json"