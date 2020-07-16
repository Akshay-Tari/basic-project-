import shutil, os, re

datepattern = re.compile(r"""^(.*?)
    ((0|1)?\d)
    ((0|1|2|3)?\d)-
    ((20|1)?\d\d)
    (.*?)$
    """,re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = datepattern.search(amerFilename)


beforePart = mo.group(1)
monthPart  = mo.group(2)
dayPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)


if mo == None:
   continue


        
        euroFilename = beforePart + dayPart + '-' + monthPart + yearPart + afterPart
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absworkingDir, euroFilename)

        print('Renaming" %s to %s...' % (amerFilename, euroFilename))
        shutil.move (amerFilename, euroFilename)

