import requests
import re
import random

def extractProblem(year,contest,form,problem):

    # Fetch
    url = 'http://artofproblemsolving.com/wiki/index.php?title=%s_%s_%s_Problems/Problem_%s' % (year, contest, form, problem)
    res = requests.get(url)

    # Convert to single line string
    text = res.text
    text = "".join(text.splitlines())

    # Start and End point
    text = re.sub(r'.*id="Problem">Problem</span></h2>','',text)
    text = re.sub(r'<h2>.*?id="Solution.*','',text)

    # Remove HTML elements
    text = re.sub(r'<img.*?alt="','',text) # Starting img tag
    text = re.sub(r'<div.*?>','',text) # Starting div tag
    text = re.sub(r'\$"\s.*?"\s>','',text) # Ending Tag
    text = re.sub(r'".*?width.*?><\/div>','',text) # Alternate Ending Tag (div)
    text = re.sub(r'<p>|<\/p>','',text) # paragraphs
    text = re.sub(r'<a.*?>|<\/a>','',text) # links

    # Fractions
    text = re.sub(r'\\frac|\\tfrac','',text)
    text = re.sub(r'}{','/',text)

    # Latex Math
    text = re.sub(r'\\neq','not equals',text)
    text = re.sub(r'\\text','',text)
    text = re.sub(r'{rem}','remainder:',text)
    text = re.sub(r'\\lfloor\s{','floor: {',text)
    text = re.sub(r'\\rfloor','',text)
    text = re.sub(r'\\%','%',text)
    text = re.sub(r'\\mathrm','',text)
    text = text.replace('\\geq',' greater or equal to')
    text = text.replace('\\overline','(repeating)')
    text = text.replace('\\cdots',' ... ')

    # Latex Formatting
    text = re.sub(r'\\textbf','',text)
    text = re.sub(r'\\\s',' ',text)
    text = re.sub(r'\\qquad','',text)

    # Final Cleanup
    text = re.sub(r'{|}','',text)
    text = re.sub(r'$|\\[|]"','',text)
    text = re.sub(r'\$','',text)
    text = re.sub(r'\\left|\\right','',text)
    text = re.sub(r'\\\[|\\\]','',text)
    text = re.sub(r'\(\s','(',text) # Answer space
    text = re.sub(r'[^\s]\\choose',' choose',text) # choose

    return text

def generateRandom():
    contests = ["AMC 12", "AIME"]

    # AMC 12
    amc_12_contests = ["A", "B", "none"]
    amc_12_A_contests = list(range(2002,2018+1))
    amc_12_B_contests = list(range(2002,2018+1))
    amc_none_contests = list(range(2000,2001+1))
    amc_problems = list(range(1,25+1))

    # AIME
    aime_contests = ["I","II","none"]
    aime_I_contests = list(range(2000,2018+1))
    aime_II_contests = list(range(2000,2018+1))
    aime_none_contests = list(range(1983,1999+1))
    aime_problems = list(range(1,15+1))

    contest = random.choice(contests)
    if contest == "AMC 12":
        # AMC 12
        contest = "AMC"
        
        form = random.choice(amc_12_contests)
        if form == "A":
            # AMC 12A
            form = "12A"

            year = str(random.choice(amc_12_A_contests))
            problem = str(random.choice(amc_problems))
        
        if form == "B":
            # AMC 12B
            form = "12B"

            year = str(random.choice(amc_12_B_contests))
            problem = str(random.choice(amc_problems))

        if form == "none":
            # AMC 12B
            form = ""

            year = str(random.choice(amc_none_contests))
            problem = str(random.choice(amc_problems))

    if contest == "AIME":
        # AIME
        contest = "AIME"

        form = random.choice(aime_contests)
        if form == "I":
            # AIME I
            form = "I"

            year = str(random.choice(aime_I_contests))
            problem = str(random.choice(aime_problems))
        
        if form == "II":
            # AIME II
            form = "II"

            year = str(random.choice(aime_II_contests))
            problem = str(random.choice(aime_problems))
        
        if form == "none":
            # AIME
            form = ""

            year = str(random.choice(aime_none_contests))
            problem = str(random.choice(aime_problems))

    output = [year,contest,form,problem]
    print(output)
    return output

def extractRandom():
    settings = generateRandom()
    year = settings[0]
    contest = settings[1]
    form = settings[2]
    problem = settings[3]

    problemText = extractProblem(year,contest,form,problem)

    output = [year,contest,form,problem,problemText]
    return output
    