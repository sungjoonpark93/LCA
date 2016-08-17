__author__ = 'SungJoonPark'
from subprocess import check_call
#check_call(['dot','-Tpng','temp.dot','-o','temp.png'])
check_call(['neato','temp2.dot','-n','-Tpng','-o','temp2.png'])