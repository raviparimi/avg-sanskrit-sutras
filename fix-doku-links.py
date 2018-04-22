#!/usr/bin/env python
import sys
import argparse
import glob
import re
import tempfile
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True, help='Directory containing sutra files')
    args = parser.parse_args()
    all_files = []
    for i in range(1, 9):
        all_files.extend(glob.glob('{}/{}/*.html'.format(args.dir, i)))
    spat = re.compile(r'(/dokuwiki/doku.php\?id=sutras:((\d{1,3}(?!\d)-){2}\d{1,3}(?!\d)))')
    repls = []
    for sfile in all_files:
        with open(sfile, "r") as fh:
            contents = fh.read()
        search = spat.search(contents)
        if search is not None:
            sutra = search.groups()[1]
            print 'Content for {} needs to be replaced'.format(sutra)
            url = 'http://avg-sanskrit.org/sutras/{}.html'.format(sutra)
            new_contents = spat.sub(url, contents)
            _, temp_file = tempfile.mkstemp()
            with open(temp_file, "wb") as fhw:
                fhw.write(new_contents)
                repls.append((sfile, temp_file))
    # Finally, replace files
    for old_file, new_file in repls:
        try:
            print "Moving {} to {}".format(new_file, old_file)
            os.rename(new_file, old_file)
        except Exception as ex:
            print "Failed to move file: {}".format(ex)

if __name__ == '__main__':
    sys.exit(main())

