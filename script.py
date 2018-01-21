import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=float, help='Speed of remote control cars')
    parser.add_argument('-a', nargs='+', help='List of csv files with actual data (eg: --actual=file1,file2...)')
    parser.add_argument('-e', nargs='+', help='List of csv files with expected data (eg: --expected=file1,file2...)')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()