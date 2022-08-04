from pathlib import Path
import subprocess
video_file_list = []
saved_file_list = []
extension_list = [".mkv",".avi",".mp4",".webm"]
folder_path = "G:\My Videos"
save_path = "video_list.txt"
#qBittorrent --> OPTIONS --> DOWNLOADS --> LAUNCH EXTERNAL PROGRAM:
#C:\Python37\python.exe "G:\My Videos\auto_cast_convert.py"

#read folders and trim extension
def fetch_list():
    l_list = []
    for p in Path(folder_path).rglob('*'):
        if str(p).endswith(tuple(extension_list)):
            l_list.append(str(p))
    return l_list

#trim 'castconvert' strings
def trim_list(a_list):
    l_list = a_list.copy()
    for elem in a_list:
        if (str(elem).__contains__("castconvert")):
            l_list.remove(elem)
    return l_list

#print a list and quantity
def show_file_list(a_list, a_msg):
    for elem in a_list:
        print(elem)
    print(a_msg + str(len(a_list)))

#write save
def write_save(a_list):
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(a_list))
        print("UPDATED SAVE LIST.")

#append 1 element to the save
def append_save(a_elem):
    with open(save_path, 'a', encoding='utf-8') as f:
        f.write('\n'+a_elem)
        print("ADDED '"+a_elem+"' TO SAVE LIST.")

#read save
def read_save():
    with open(save_path, 'r', encoding='utf-8') as f:
        l_list = f.read().splitlines()
        return l_list

#compare both lists
def compare(a_list_1, a_list_2):
    l_list = a_list_2.copy()
    for elem1 in a_list_1:
        for elem2 in a_list_2:
            if elem1 == elem2:
                l_list.remove(elem1)
    return l_list

#convert a list
def convert_list(a_list):
    for elem in a_list:
        subprocess.call('cast_convert convert "'+str(elem)+'"')
        append_save(str(elem))

#RUN
video_file_list = fetch_list()
video_file_list = trim_list(video_file_list)
try:
    saved_file_list = read_save()
except:
    print("SAVE FILE DOESN'T EXIST. Creating one...")
    write_save(video_file_list)
saved_file_list = read_save()
difference_list = compare(saved_file_list, video_file_list)
show_file_list(difference_list, "NEWLY VIDEO(S): ")
convert_list(difference_list)
write_save(video_file_list)


