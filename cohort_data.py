"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.
    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}
    Arguments:
      - filename (str): the path to a data file
    Return:
      - set[str]: a set of strings
    """
    # sudo
    # open the file
    student_file = open(filename)
    houses = set()
    # loop through the file
    for line in student_file:
      # create individual list items from parsing out data 
      words = line.rstrip().split('|')
      
      house_names = words[2]
      # add house names (index 2) to a set
      if house_names not in houses:
        houses.add(house_names)
      
    houses.remove('')
    
    # return set 
    return houses

def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

     # open file
    student_file  = open(filename)
    # create empty student list 
    students = []   
    # create a for loop going line by line through file
    for line in student_file:
      # feed the data of loop into variable (remove whitespaces and split into list)
      line_list = line.rstrip().split('|')
      # if 5th item (index 4) == cohort
      if cohort == line_list[4] or cohort == 'All':
        # add to student list
        students.append(f"{line_list[0]} {line_list[1]}")
       
    # TODO: replace this with your code
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

      Rosters appear in this order:
      - Dumbledore's Army
      - Gryffindor
      - Hufflepuff
      - Ravenclaw
      - Slytherin
      - Ghosts
      - Instructors

      Each roster is a list of names sorted in alphabetical order.

      For example:
        >>> rosters = hogwarts_by_house('cohort_data.txt')
        >>> len(rosters)
        7

        >>> rosters[0]
        ['Alicia Spinnet', ..., 'Theodore Nott']
        >>> rosters[-1]
        ['Filius Flitwick', ..., 'Severus Snape']

      Arguments:
        - filename (str): the path to a data file

      Return:
        - list[list]: a list of lists
      """
    # sudo
    # open file
    student_file = open(filename)
    # lists of houses, ghosts, instructors
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    # loop through file by line
    for line in student_file:
    # parse each line
      first, last, house, _, cohort = line.rstrip().split('|')

    # if/elif to check third list item equals house name, assign to house list
      # if line_lst[4] == 'G':
      #   ghosts.append(f"{line_lst[0]} {line_lst[1]}")
      #   ghosts.sort()
      # elif line_lst[4] == 'I':
      #   instructors.append(f"{line_lst[0]} {line_lst[1]}")
      #   ghosts.sort()
      if house == 'Dumbledore\'s Army':
        # add first and last names to appropriate list and sort alphabetically
        dumbledores_army.append(f"{first} {last}")
        dumbledores_army.sort()
      elif house == 'Gryffindor':
        gryffindor.append(f"{first} {last}")
        gryffindor.sort()
      elif house == 'Hufflepuff':
        hufflepuff.append(f"{first} {last}")
        hufflepuff.sort()
      elif house == 'Ravenclaw':
        ravenclaw.append(f"{first} {last}")
        ravenclaw.sort()
      elif house == 'Slytherin':
        slytherin.append(f"{first} {last}")
        slytherin.sort()

      else:
        # if third list item == empty, check fifth element to check for ghost or instructor
        if cohort== 'G':
          ghosts.append(f"{first} {last}")
          ghosts.sort()
        else:
          instructors.append(f"{first} {last}")
          instructors.sort()

    # return concatenation of all lists
    roster = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]
    # TODO: replace this with your code

    return roster



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    all_data = []
    cohort_data = open(filename)
    
    for line in cohort_data:
      
      first, last, house, advisor, cohort_name = line.rstrip().split('|')
      all_data.append((f'{first} {last}', f"{house}", f"{advisor}", f"{cohort_name}"))

    return all_data

def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """


    for full_name, _, _, cohort_name in all_data(filename):
      if full_name == name:
          return cohort_name

# print(get_cohort_for("cohort_data.txt", "Hannah Abbot"))


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
