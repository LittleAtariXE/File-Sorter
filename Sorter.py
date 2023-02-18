import os
import sys
import shutil
from time import sleep



class Settings:
    def __init__(self, count, target, dir_name, dest=None):
        self.count = int(count)
        self.target = str(target)
        self.dir_name = str(dir_name)
        self.dest = dest
        
    

class Sorter(Settings):
    def __init__(self, count, target, dir_name, dest=None):
        super().__init__(count, target, dir_name, dest)
        if not self.dest:
            self.dest = self.target + '/' + self.dir_name
        self.target_list = self.scan_dir()
        self.len_target = len(self.target_list)
        self.sorted = self.sort()
            
        
    
    def scan_dir(self):
        out = []
        if not os.path.exists(self.target):
            print("ERROR !! Target path not exist !!!!")
            sys.exit()
        
            
        for d in os.listdir(self.target):
            out.append(d)
        return out
    
    def sort(self):
        out = []
        d = int(self.len_target / self.count)
        c = self.len_target % self.count
        last = (self.count * d) - 1
        
        count = 1
        count_dir = 1
        out.append({str(self.dir_name + str(count_dir)): []})
        
        while count < self.len_target:
            if count % self.count == int():
                count_dir += 1
                out.append({str(self.dir_name + str(count_dir)): []})
            out[count_dir-1][self.dir_name + str(count_dir)].append(self.target_list[count-1])
            count += 1
        
        return out
    
    def do_it(self):


        if not os.path.exists(self.dest):
            os.mkdir(self.dest)
        if not self.target.endswith('/'):
            self.target = self.target + '/'
        if not self.dest.endswith('/'):
            self.dest = self.dest + '/'
        
        count = 0
        print('*' * 50)
        print("Total files to sorting: ", self.len_target)
        print("START !!!!")
        sleep(2)
        for d in self.sorted:
            for (k, i) in d.items():
                d_link = self.dest + str(k)
                os.mkdir(d_link)
                for f in i:
                    count += 1
                    print("Copying file No: ", count)
                    try:
                        shutil.copy2(self.target + f, d_link + '/' + f)
                    except Exception as e:
                        print("ERROR: ", e)
                        
                

def handle_args(args):
    if len(args) < 2:
        print("Error: No options ! add 'help'. example: 'python3 sorter.py help' ")
        sys.exit()
    if args[1] == 'help':
        print('HELP:')
        sys.exit()
    elif len(args) < 4:
        print('ERROR: Too few arguments')
        sys.exit()
        
    if len(args) > 4:
        return Sorter(args[1], args[2], args[3], args[4])
    else:
        return Sorter(args[1], args[2], args[3])
    
    
        
            
            
            
if __name__ == '__main__':
    sort = handle_args(sys.argv)
    sort.do_it()
    
    
    
            
            
        
        


########






    
    
    