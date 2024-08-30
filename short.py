import ast
print('url, then after /\nexample: https://google.com google makes url/google goto google.com')
def readat():
    f=open('dict.data','r')
    a=f.read()
    f.close()
    return(a)
def getreturnwebsite(short):
    return(ast.literal_eval(readat())[short])
def write(dataaaaa):
    f=open('dict.data','w')
    f.write(dataaaaa)
    f.close()
while(True):
    a=input("\nenter: ")
    a=a.split(' ')
    current=ast.literal_eval(readat())
    current[a[1]] = a[0]
    write(str(current))
    print(current)
    