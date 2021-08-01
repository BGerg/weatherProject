import argparse


def parse():
    parser = argparse.ArgumentParser(description='Get weather data from wttr.com'
                                                 'print it, create statistics or'
                                                 'evaluation',
                                     epilog='Enjoy the the weather and the program :)')

    parser.add_argument('-c',
                        '--city',
                        action='store',
                        type=str,
                        default='Miskolc',
                        metavar='',
                        help='set the city for which you want weather data (default Miskolc)')
    parser.add_argument('-s',
                        '--saveto',
                        action='store',
                        type=str,
                        default='weatherdata.json',
                        metavar='',
                        help='set the json output file name (default filename: weatherdata)')
    parser.add_argument('-a',
                        '--all',
                        type=bool,
                        default='False',
                        help='Show all possible weather data')
    parser.add_argument('-f',
                        '--filter',
                        nargs='+',
                        help='Show the chosen weather data')
    parser.add_argument('query_mode',
                        help='Chose from these modes: current, service, aggregate')


    return parser.parse_args()
