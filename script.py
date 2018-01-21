import csv
import argparse
from collections import OrderedDict


def get_info_from_reader(reader, speed):
    x_disp, y_disp, dist = .0, .0, .0
    for row in reader:
        meters = float(row[1]) * speed
        if row[0] in ('N', 'S'):
            y_disp += meters
        else:
            x_disp += meters
        dist += meters
    return round(x_disp, 2), round(y_disp, 2), round(dist, 2)


def get_info(speed, act_path, exp_path):
    car_info = {'act_x_disp': 0, 'act_y_disp': 0, 'exp_x_disp': 0, 'exp_y_disp': 0, 'act_dist': 0, 'exp_dist': 0}
    with open(act_path) as act_file:
        with open(exp_path) as exp_file:
            reader_act = csv.reader(act_file)
            reader_exp = csv.reader(exp_file)
            car_info['act_x_disp'], car_info['act_y_disp'], car_info['act_dist'] = get_info_from_reader(reader_act, speed)
            car_info['exp_x_disp'], car_info['exp_y_disp'], car_info['exp_dist'] = get_info_from_reader(reader_exp, speed)
    return car_info


def rcCar(speed, act, exp):
    assert len(act) == len(exp) == len(speed), "speed, actual and expected must have the same number of elements"
    cars_info = (get_info(speed[i], act[i], exp[i]) for i in range(len(act)))
    result = OrderedDict(act_x_disp=[], act_y_disp=[], exp_x_disp=[], exp_y_disp=[], act_dist=[], exp_dist=[])
    for car_info in cars_info:
        for key in result.keys():
            result[key].append(car_info[key])
    return tuple(result.values())


def plotRC(speed, act, exp):
    rc_car_info = rcCar(speed, act, exp)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--speed', type=float, nargs='+', help='List of the speed of each car (eg: --speed speed1 speed2 ...)')
    parser.add_argument('-a', '--act', nargs='+', help='List of csv files with actual data (eg: --act file1 file2 file3...)')
    parser.add_argument('-e', '--exp', nargs='+', help='List of csv files with expected data (eg: --exp file1 file2 file3...)')
    args = vars(parser.parse_args())
    result = rcCar(**args)
    print(result)


if __name__ == '__main__':
    main()
