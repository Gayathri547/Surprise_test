def kaki():
    fp = open("/home/applines-05/Documents/Surprise_test/kaki.txt")
    #print(fp.readlines())
    line = fp.read()
    word = line.split()
    print("the words which have least length are\n")
    for i in word:
        if len(i)<5:
            print(i)
    fp.close()
kaki()
