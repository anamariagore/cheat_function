# Assignment 3.2P Solutions (CHEAT FUNCTION) - 2022 Programming in Psychological Science
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 28-Jan-22     Ana-Maria Gore               Original code
# 28-Jan-22     Ana-Maria Gore             description changes

def cheat(exercise):
    """
    CHEAT FUNCTION returns the solutions to the Week 1 Python exercises from the Programming in Psychological Science (2022) course
    """
    if int(exercise) == 1:
        print("import numpy as np")
    elif int(exercise) == 2:
        print("another_array = np.zeros((2, 4, 6))\nprint(another_array[0,3,-1])")
    elif int(exercise) == 3:
        print("""Unlike in R, if we make a copy by using "=", we do not copy the elements but the source of where those elements are stored.
        So, if we make any changes to the "copy" (in this case: 'another_array'), we make the same changes to the original variable (in this case: 'new_array').
        To make a true new copy of the numpy array, we have to use the .copy() function.""")
    elif int(exercise) == 4:
        print("""the function %paste doesn't work in a script because it is not a part of python language.
        It is an additional command of the iPython that makes the terminal more interactive.""")
    elif int(exercise) == 5:
        print("""change the working directory: %cd 'new_directory'\nprint the current working directory: %pwd
        list the contents of the working directory: %ls\nlist current workspace variables: %env""")
    elif int(exercise) == 6:
        print("pip install pip-install-test")
    elif int(exercise) == 7:
        print("""#Because if there is a missing value in a list then you cannot calculate the mean.
              sample_scores = sample_scores[np.logical_not(np.isnan(sample_scores))] #removing the missing value
              print(np.mean(sample_scores))""")
    elif int(exercise) == 8:
        print("v = np.array(range(1,17))\na = np.reshape(v**2, (2,2,2,2))\nprint(a)")
    elif int(exercise) == 9:
        print("import pandas as pd\ndict = pd.read_csv(r'/Users/ana-maria/InsectSprays.csv').to_dict()\nprint(dict.keys())")
    elif int(exercise) == 10:
        print("""language = ["R", "Python"]*5
        code_type = np.repeat(["forloop1", "forloop2", "forloop3", "forloop4", "forloop5"],2)
        df = pd.DataFrame(list(zip(language, code_type, speed_sec)),columns =["language", "code_type", "speed_sec"])
        print(df)""")
    else:
        print("The exercise cannot be found. The function offers solutions to exercises from 1 to 10")
