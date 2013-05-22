from optparse import OptionParser
import shutil
import os
import sys
import time

types = {'directory': 'Directory',
         '': 'Text',
         '.apk': 'Android',
         '.iso': 'Software',
         '.sql': 'Databases',
         '.odb': 'Databases',
         '.mwb': 'Databases',
         '.jnlp': 'Java',
         '.aspx': 'Scripts',
         '.pl': 'Scripts',
         '.js': 'Scripts',
         '.application': 'Software',
         '.xlsx': 'Documents',
         '.JPG': 'Graphics',
         '.csv': 'Databases',
         '.swf': 'Flash',
         '.c': 'Scripts',
         '.sh': 'Scripts',
         '.py': 'Scripts',
         '.phtml': 'Scripts',
         '.xls': 'Documents',
         '.dotx': 'Documents',
         '.sql.gz': 'Databases',
         '.tgz': 'Databases',
         '.tar.gz': 'Databases',
         '.pdf': 'PDFs',
         '.doc': 'Documents',
         '.docx': 'Documents',
         '.exe': 'Software',
         '.air': 'Software',
         '.msi': 'Software',
         '.jar': 'Libraries',
         '.zip': 'Zipped',
         '.rar': 'Zipped',
         '.tar': 'Zipped',
         '.gz': 'Zipped',
         '.7z': 'Zipped',
         '.bz2': 'Zipped',
         '.htm': 'Documents',
         '.html': 'Documents',
         '.xls': 'Documents',
         '.php': 'Scripts',
         '.odt': 'Documents',
         '.ppt': 'Documents',
         '.xcf': 'Photoshop',
         '.psd': 'Photoshop',
         '.log': 'Logs',
         '.aux': 'Latex',
         '.dvi': 'Latex',
         '.tex': 'Latex',
         '.mp3': 'Music',
         '.ogg': 'Music',
         '.wav': 'Music',
         '.mp4': 'Movies',
         '.mkv': 'Movies',
         '.flv': 'Movies',
         '.avi': 'Movies',
         '.png': 'Graphics',
         '.jpg': 'Graphics',
         '.jpeg': 'Graphics',
         '.gif': 'Graphics',
         '.tiff': 'Graphics',
         '.raw': 'Graphics',
         '.bak': 'Bk',
         '.bk': 'Bk',
         '.eps': 'Graphics',
         '.bmp': 'Graphics',
         '.epub': 'Books',
         '.fb2': 'Books',
         '.mobi': 'Books',
         '.djvu': 'Books',
         '.rpm': 'Software',
         '.dmg': 'Software',
         '.txt': 'Text',
         '.mht': 'Text',
         '.xml': 'Documents',
         '.dll': 'Windows DLLs',
         '.pptx': 'Documents',
         '.odp': 'Documents',
         '.wbk': 'Documents',
         '.torrent': 'Torrents'}


def ensure_dir(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for type, dir in types.items():
        path = os.path.join(destination, dir)
        if not os.path.exists(path):
            os.makedirs(path)


def sort_files(folder_name, dest):
    files = os.listdir(folder_name)

    for file in files:
        p = os.path.join(folder_name, file)
        if os.path.isdir(p) is True:
            if file not in list(types.values()):
                d = os.path.join(dest, types['directory'])
                try:
                    shutil.move(p, d)
                    print("Moving " + p + " to " + d)
                except:
                    print("Can`t access to {0}, {1}".format(p, sys.exc_info()))
                print("Moving " + p + " to " + d)
        else:
            ext = os.path.splitext(p)[1]
            if ext in list(types.keys()):  # if types.has_key(ext): deprecated
                d = os.path.join(dest, types[ext])
                try:
                    shutil.move(p, d)
                    print("Moving " + p + " to " + d)
                except:
                    print("Can`t access to {0}, {1}".format(p, sys.exc_info()))
            else:
                print("Leaving " + p)


def main():
    parser = OptionParser(usage="Usage: %prog [options] filename")
    parser.add_option("-d", "--destination", dest="destination", help="Directory you want to move files or directories to")
    (options, args) = parser.parse_args()

    if args:
        directory = args[0]
    else:
        directory = os.getcwd()

    destination = options.destination

    if not os.path.exists(directory):
        print("Invalid directory", directory)
        sys.exit(1)

    if not destination:
        print("Invalid destination")
        sys.exit(1)

    ensure_dir(destination)
    sort_files(directory, destination)

    print(time.time())

if __name__ == "__main__":
    main()
