def hpu4_get():

    f = open("hpu4.dat", 'r')
    for line in f:
        lines = line.split()
        filename = "PennPed/test-%d.dat" % (int(lines[0]))
        g = open(filename,'r+')
        num = int(lines[1])
        string = "\n"
        index = 3
        for i in range (0,num):
            string += lines[index] + " " + lines[index+1] + " " + lines[index+2] + " " + lines[index+3] + "\n"
            index += 4
        g.seek(0,2)
        g.write(string)
    
if __name__ == '__main__':
    print hpu4_get()
