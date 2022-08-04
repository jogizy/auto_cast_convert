# auto_cast_convert
Convert newly video found on specified directory.


<b>STEP 1:</b>

Specify your "ROOT" video directory:
<code>folder_path = "G:\My Videos"</code>


<b>STEP 2 (WINDOWS):</b>

Requirement #1: Having python3 & pip3 installed.

Requirement #2: On terminal: <code>pip install cast_convert</code>

Requirement #3: Download ffmpeg, ffprobe, ffplay binaries and add them into "ENVIRONMENT VARIABLES" otherwise cast_convert will crash.


<b>STEP 3 (OPTIONAL) Adding in qBittorrent:</b>

  Open qBittorrent --> OPTIONS --> DOWNLOADS --> LAUNCH EXTERNAL PROGRAM:
  
  <code>C:\Python37\python.exe "G:\My Videos\auto_cast_convert.py"</code>
  
  <i>*NOTE: video_list.txt will be generated in your qBittorrent installation path. Example: C:\Program Files\qBittorrent\video_list.txt</i>
  
  <i>*NOTE2: Because video_list.txt isn't created yet, only the FIRST time qBittorrent will launch this script after any torrent completion, it won't work.</i>
