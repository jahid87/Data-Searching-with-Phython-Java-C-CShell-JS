corner=['posting dates','title and author','gutindex','project gutenberg collection between','gutenberg collection between','with','*','~']

while True:
    found='false'
    count=0;
    head=''
    inp = input('Enter ETEXT NO or Book title or Book author (press enter to finish): ')
    if inp=='':
        break
    with open('GUTINDEX.ALL', encoding='utf-8') as file:
        for line in file:
            if any(c in line.lower() for c in corner):
                continue
            else:
                *all, last = line.strip().split(' ')
                last = last.strip().strip('B').strip('C')
                if(last.isdigit() or 'by' in line.lower()):
                    if(last.isdigit()):
                        head=line
                    if(inp.strip().isdigit()):
                        *alls, lines = line.lower().split(' ')
                        lines = lines.strip().strip('b').strip('c')
                        res = (inp.lower() == lines)
                    else:
                        lines = line.lower()
                        res = (inp.lower() in lines)
                        
                    if res:
                        found='true'
                        count += 1
                        if(last.isdigit()):
                            print(str(count)+") "+line)
                        else:
                            print(str(count)+") "+head)
                            print(line)
                        for line in file:
                            *all, last = line.strip().split(' ')
                            if(last.isdigit() or line=='\n'):
                                break
                            print(line)
                        print('--------------')
                    
    if found=='false':
        print('Not found!');
                
                
