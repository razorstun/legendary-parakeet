Advance Python Modules

- Collection Modules - Counter, defaultdict (defaultdict(lamba: 0)), namedtuple(typr_name, field)
- Opening and reading files and folders
    - os.getcwd() - get current working directory
    - shutil.move(file_path,dest)
    - os.listdir()
    - os.unlink(path)
    - os.rmdir(path)
    - shutil.rmtree(path)
    - pip install send2trash - send2trash(path)
    - os.walk()

- Datetime Module 
    - datetime.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
    - datetime.date.today()
    - datetime.datetime()

- Math and Random Modules
    - Math - math.floor(), math.ceil(), round(), math.pi, math.e, math.inf, math.nan, math.log(), math.deegrees(), math.radians()
    - random - random.randint(a,b), random.seed() then random.randint(a,b), random.choice(list_name)
     - sample with replacement - random.choices(population=list_name,k=10)
     - sample without replacement - random.sample(population=list_name,k=10)
     - random.shuffle(list)
     - random.uniform(a=0,b=100)
     - random.gauss(mu=0,sigma=1)

- Python Debugger
    - pdb module - one can pause the operation mid script and check what the variables & objects holds at thst time
    - pdb.set_trace()

- Regular Expression
    - It allow us to search for general patterns in text data
    - r"" -\d is for digits - \d\d\d == \d{3}
    - re.search(pattern,text) - gives the match object if pattern matches - .span() to get the index of the pattern a tuple - .start()/.end()
    - re.findall(pattern, text) - to get all matches - only returns back list of all match string
    - for match in re.finditer(pattern,text): - gives all the match object if pattern matches
        print(match)
        print(match.span())
        print(match.group())
    - \d = digit, \w = alphanumeric, \s = whitespace, \D = A non digit, \W = non-alphanumeric, \S = non-whitespace
    - Quantifiers - + = occurs one or more times, {3} = occurs exactly 3 times, {2,4} = occurs 2 to 4 times, {3,} = occurs 3 or more times, * = occur zero or more times, ? = once or none
    - () to group pattern - re.search(r"(\W\d{2})-(\d{3})-(\d{3})-(\d{4})",text)
    - we can also compile the group pattern and pass it into re.search(pattern,text)
    - we can use | operator to search for one or more pattern - re.search(r'cat|dog',"The cat is here")
    - we can use the wildcard . to get the word with partial pattern
    - we can use ^ to starts with and $ to find ends with
    - r"[^\d]" to exclusion all digits from sentence and re.findall(r"[^c.t ]+",sa) to remove specific letter, smbols, numbers
    - re.findall(r'[\w]+-[\w]+',pattern) to find all pattern witj - in between
    - re.search(r'cat(fish|nap|claw)',pattern) combine or with other pattern

- Timing with code
    - we can use time module to check the time taken wile running the code - calculate difference between start and end time.time()
    - we can also use timeit module
        - it takes 3 arg stmt(The statment to check), setup(logic of the statement), number(no of time to run)
        -   import timeit
            stmt =  '''
                    func_one(100)
                    '''
            setup = '''
                    def func_one(n):
                        return list(map(int,range(n)))
                    '''
            timeit.timeit(stmt,setup,number=1000)

- Unzipping and Zipping file
    - zipfile module to zip file
        -   comp_file = zipfile.ZipFile(zip_file_name.zip,'w')
            comp_file.write('file1_name',compress_type=zipfile.ZIP_DEFLATED)
            comp_file.write('file2_name',compress_type=zipfile.ZIP_DEFLATED)
            comp_file.close()
    - zipfile to Unzip
        -   zip_obj =zipfile.ZipFile('comp_file','r')
            zip_obj.extractall(newfoldername)
    - zip entire directory using shutil
        -   import shutil
            dir_path = "path"
            out_file_name = ''
            shutil.make_archive(out_file_name,'zip',dir_path)
    - unzip using shutil
        -   shutil.unpack_archive(zip_file_path,'final_unzip','zip')
    

