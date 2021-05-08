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
