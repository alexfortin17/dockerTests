f = open('newfile.txt','w')
f.write("Ceci est un nouveau texte")
f.close()

g = open('testfile1.txt','a')
g.write('\n')
g.write('vomi2')
g.close()

n = open('./testDir/insidetest1.txt','a')
n.write('\n')
n.write('inside test 2')
n.close()

