def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ linear O(n) ]


    """

    if len(s1) != len(s2): 
        return False

    for i in range(len(s1)): #O(n) as it is based on the length of the string
        if s1[i] != s2[i]:   
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [ linear O(n) ]

    """

    if "hippo" in animals or "platpypus" in animals: #O(n) as this is searching in a list
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ linear O(n) ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later

    #Since we drop the constants and are only looking at the largest growing term, this is O(n)
    s = set(numbers) #O(n) linear

    for x in s: #Appending to a list is constant O(1)
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ quadratic O(n^2) ]

    """

    result = []

    #Nested for loops are always quadratic and since appending is constant that's dropped
    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [ not sure what the name is -> O(n^3) ]

    """

    result = []

    #The nested for loops results in a quadratic runtime but due to the deletion
    #in a list that has O(n) runtime, it results to O(n) x O(n^2) = O(n^3)
    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
