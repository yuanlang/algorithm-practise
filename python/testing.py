# This problem is all about unit testing.
# Your company needs a function that meets the following requirements:
# For a given array of n integers, the function returns the index of 
# the element with the minimum value in the array. If there is more 
# than one element with the minimum value, the returned index should be the smallest one.
# If an empty array is passed to the function, it should raise an Exception.
# Note: The arrays are indexed from 0.
# get_array() method in class TestDataEmptyArray has to return an empty array.
# get_array() method in class TestDataUniqueValues has to return an array of size
#  at least 2 with all unique elements, while method get_expected_result() of this 
# class has to return the expected minimum value index for this array.
# get_array() method in class TestDataExactlyTwoDifferentMinimums has to return 
# an array where there are exactly two different minimum values, while method 
# get_expected_result() of this class has to return the expected minimum value 
# index for this array.

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
        arr = []
        for i in range(10):
            arr.append(i)
        return arr

    @staticmethod
    def get_expected_result():
        # complete this function
        return 0

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        arr = []
        for i in range(2):
            arr.append(1)
        return arr

    @staticmethod
    def get_expected_result():
        # complete this function
        return 0


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

