s1=os.listdir('/home/debian8/data-back/financials')
s2=os.listdir('/home/debian8/data-back/holders')
s3=os.listdir('/home/debian8/data-back/options')
s4=os.listdir('/home/debian8/data-back/profile')
s5=os.listdir('/home/debian8/data-back/price')
s1=set(s1)
s2=set(s2)
s3=set(s3)
s4=set(s4)
s5=set(s5)
s=s1&s2&s3&s4&s5
with open("/tmp/test.csv","w") as f:
    for item in s:
        f.write(item + "\n")
    
 