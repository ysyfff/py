from string import Template
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template): #create subclass
    delimiter = '%'

fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
print t
date = time.strftime('%d%b%y')
print date
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    print base, ext, i
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)