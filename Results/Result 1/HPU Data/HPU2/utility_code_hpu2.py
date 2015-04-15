def hpu2_get():

    f = open("hpu2.dat", 'r')
    for line in f:
        lines = line.split()
        filename = "PennPed/test-%d.dat" % (int(lines[0]))
        filename1 = "PennPed/new/test-%d.dat" % (int(lines[0]))
        g = open(filename,'r')
        num = int(lines[1])
        string = g.read()
        data = string.split('\n')
        index = 3
        i_data = 0
        response = ""
        for i in range (0,num):
            #print lines[index], i_data, data[i_data]
            if (lines[index]=='1'):
                response += str(data[i_data]) + "\n"
                #print "aviral"+response
            i_data += 1
            index += 1
        #print response
        response = response[:-1]
        #print response        
        h = open(filename1,'w')
        h.write(response)
        h.close()
        g.close()
    f.close()
    
if __name__ == '__main__':
    hpu2_get()
