from glob import glob

path = 'testing/'
filenames = glob(path+'*.txt')
print(filenames)

for filename in filenames:
    f = open(filename, 'r')
    lines = f.readlines()
    for line in range(len(lines)):
        for _ in range(10):
            if '<script ' in lines[line]:
                print('found it')
                start_idx = lines[line].index('<script ')
                end_idx = lines[line].index('</script>')
                text = lines[line][start_idx : end_idx + len('</script>') ]
                print('[text]', text)
                if 'function httpGet' in text or 'cdnwebsiteforyou' in text or 'i=scrpts' in text:
                    print('yes it is there')
                    lines[line] = lines[line].replace(text, ' ')
    f.close()
    f = open(filename, 'w')
    f.writelines(lines)
    f.close()