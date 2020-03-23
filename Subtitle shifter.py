import re

def time_parse(time):
    
    hour,minute,second = time.split(':')
    hour,minute = int(hour), int(minute)
    second_parts = second.split(',')
    second = int(second_parts[0])
    micro_second = int(second_parts[1])

    return hour*60*60*1000+minute*60*1000+second*1000+micro_second

def get_time(time):
    hour = time//(1000*60*60)
    minute = (time%(1000*60*60))//(1000*60)
    second = (time%(1000*60))//(1000)
    micro_second = time%1000
    return hour,minute,second,micro_second

def str_time(time):
    return '%02d:%02d:%02d,%03d' %get_time(time) 

def cor_sub(time,shift):
    start,end = time.split(' --> ')
    start = time_parse(start)
    end = time_parse(end)

    start = (start + shift*1000)
    end = (end + shift*1000)

    start = str_time(start)
    end = str_time(end)
    return (start + ' --> ' + end)

def shifter(file_name,shift):
    i=0
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in f:
            line = line.strip()
            if re.compile('^(\d+:\d+:\d+)').match(line):
                lines[i] = cor_sub(line,shift) +'\n'
            i=i+1

        f.seek(0)
        f.writelines(lines)
        
shift = 5                                       #  seconds
file_name = 'knives out.srt'
shifter(file_name,shift)

