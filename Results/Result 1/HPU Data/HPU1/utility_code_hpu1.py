def hpu1_get():

    f = open("hpu1.dat", 'r')
    for line in f:
        lines = line.split()
        filename = "dataset/test-%d.dat" % (int(lines[0]))
        g = open(filename,'w')
        num = int(lines[1])
        string = ""
        index = 3
        for i in range (0,num):
            string += lines[index] + " " + lines[index+1] + " " + lines[index+2] + " " + lines[index+3] + "\n"
            index += 4
        g.write(string)
    
if __name__ == '__main__':
    print hpu1_get()
