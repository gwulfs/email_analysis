f = open('positive.txt');
content = [x.strip('\n').lower() for x in f.readlines()];
content = set(content)
content = list(content)
f.close();