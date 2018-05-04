#main.py
import pyb
from pyb import Pin
import math
from array import array
from onewire import OneWire
TIMEOUT=40

#from ds18x20 import DS18X20
bits=bytearray(5)
for i in range(5):
	bits[i]=0
bits = array('b',[0,0,0,0,0])
i=0
dh11=Pin('Y10',mode=Pin.OUT)
# while(dh11.value()&(i<100)):
# 	print("i = %d"%i,'High')
# 	pyb.udelay(10)
# 	i = i + 1
dh11.low()
pyb.delay(20)#延迟18ms以上才有响应，怎么跟网上onewire协议（480～960us）不一致啊。
#dh11.high()
dh11=Pin('Y10',mode=Pin.IN)
pyb.udelay(10)

print('Hello!')

while(dh11.value()&(i<1000)):
	print("i = %d"%i,'High')
	pyb.udelay(10)
	i = i + 1

while((dh11.value()==0)&(i<1000)):
	print("i = %d"%i,'Low')
	pyb.udelay(10)
	i = i + 1

cnt = 7
idx = 0
i = 0
if pyb.elapsed_micros(start)>40:
    bits[idx]|=1<<cnt
    print('Hello',cnt,idx,bits)

if cnt==0 :
    cnt=7
    idx=idx+1
else:
    cnt=cnt-1
print('temp= ',bits[2],' humi = ',bits[0])
pyb.delay(20000) 
    
""" while(dh11.value()):

	cnt = 7
	idx = 0
	i = 0
	for i in range(40):
		loopCnt = TIMEOUT
		while(dh11.value()==0):
			loopCnt = loopCnt-1
			pyb.udelay(1)
			if(loopCnt==0):
				print('error01')
				break
#	return -2	
		start = pyb.micros()
		loopCnt = TIMEOUT
		while(dh11.value()==1):
			loopCnt = loopCnt-1
			pyb.udelay(1)
			if(loopCnt==0):
				print('error02,i=%d',i)
				break
#	return -2

		if pyb.elapsed_micros(start)>40:
			bits[idx]|=1<<cnt
			print('Hello',cnt,idx,bits)

		if cnt==0 :
			cnt=7
			idx=idx+1
		else:
			cnt=cnt-1
	print('temp= ',bits[2],' humi = ',bits[0])
	pyb.delay(20000) """
			



			




