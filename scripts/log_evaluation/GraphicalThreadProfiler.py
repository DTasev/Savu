import pandas as pd
import argparse
import tempfile
import os


def convert(log_file_list, path, log_level):

    for log_file in log_file_list:
        the_key = ""
        the_interval = 0  # millisecs
        frame = get_frame(log_file, the_key, 'DEBUG')
        machine_names = get_machine_names(frame)
        if log_level != 'DEBUG':
            frame = get_frame(log_file, the_key, log_level)
        html_filename = \
            set_file_name('/'.join([path, os.path.basename(log_file)]))
        render_template(frame, machine_names, the_interval, html_filename)
        print "html file created:", html_filename
        print "Open the html file in your browser to view the profile."

    return frame


def get_frame(log_file, the_key, log_level):
    import itertools

    names = ['L', 'Time', 'Machine', 'CPU', 'Type', 'Message']
    data = pd.io.parsers.read_fwf(log_file, widths=[2, 13, 6, 6, 7, 1000],
                                  names=names)
#    data = pd.io.parsers.read_fwf(file, widths=[2, 13, 5, 6, 7, 1000],
#                                  names=names)

    data['Key'] = data['Machine'] + data['CPU']
    frame = ((data[data.Type == log_level])[data.columns[[6, 5, 1]]])
    frame.insert(0, 'Index', range(len(frame)))
    frame = frame.sort_values(by=['Key', 'Index'])
    del frame['Index']

    startTime = (frame.groupby('Key').first()).Time
    nElems = frame.groupby('Key').size()

    shift = []
    for i in range(len(nElems)):
        shift.append([startTime[i]]*nElems[i])
    shift = list(itertools.chain(*shift))

    frame.Time = frame.Time - shift
    frame = frame[frame.Key.str.contains(the_key)]
    frame.insert(3, "Time_end", frame.Time.shift(-1))
    frame.Message = frame.Message.str.strip('\n')
    frame.Message = frame.Message.str.replace("'", "")

    return frame


def get_machine_names(frame):
    machine_names = frame.copy(deep=True)
    machine_names = machine_names[frame.Message.str.contains('Rank')]
    machine_names.Message = [m.split(':')[-1].strip() for m in frame.Message
                             if 'Rank' in m]
    machine_names = machine_names.drop(['Time', 'Time_end'], axis=1)
    machine_names.Key = [k.split('CPU')[0] for k in machine_names.Key]
    machine_names.Key = [k.split('GPU')[0] for k in machine_names.Key]
    machine_names = machine_names.groupby('Key').first()
    machine_names['Machine'] = machine_names.index.values

    return machine_names


def render_template(frame, machine_names, the_interval, outfilename):
    from jinja2 import Template
    import template_strings as ts

    frame = frame[(frame.Time_end - frame.Time) > the_interval].values

    f_out = open(outfilename, 'w')
    style = os.path.dirname(__file__) + '/style_sheet.css'
    template = Template(ts.set_template_string_single(1300))

    f_out.write(template.render(vals=map(list, frame[:, 0:4]),
                                machines=map(list, machine_names.values),
                                style_sheet=style))
    f_out.close()

    return frame


def set_file_name(filename):

    dir_path = os.path.dirname(filename)
    temp = os.path.basename(filename).split('.')
    filename = temp[0] + '_' + temp[1] + '.html'
    outfilename = dir_path + '/' + filename

    return outfilename


def __option_parser():
    """ Option parser for command line arguments.
    """
    parser = argparse.ArgumentParser(prog='savu_profile')

    parser.add_argument('file', help='Savu output log file')
    parser.add_argument('-l', '--loglevel', default='INFO',
                        help='Set the log level.')
    parser.add_argument('-f', '--find', nargs='*', default=[],
                        help='Find lines containing these entries')
    parser.add_argument('-i', '--ignore', nargs='*', default=[],
                        help='Ignore lines containing these entries')
    return parser.parse_args()


def main():

    args = __option_parser()

    filename = args.file
    if not filename.startswith(os.path.sep):
        filename = os.getcwd() + os.path.sep + filename

    # create the log file for profiling
    name, ext = os.path.basename(filename).split('.')
    log_filename = '/'.join([tempfile.mkdtemp(), name + '_' + ext + '.log'])

    lfilter = ['L '] + args.find
    with open(filename, 'r') as finput:
        with open(log_filename, 'w') as foutput:
            for line in finput:
                filter_line = [True if t in line else False for t in lfilter]
                keep_line = [False if t in line else True for t in args.ignore]
                line = False if False in filter_line + keep_line else line
                if line:
                    foutput.write(line)

    convert([log_filename], os.path.dirname(filename), args.loglevel)


if __name__ == "__main__":
    main()
