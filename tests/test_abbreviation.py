from abbreviation import Abbreviation


def test_abbreviation():
    """Setup function to test Abbreviation class"""
    data = ['Friday']
    abb = Abbreviation(exclude_abbreviation={'Friday': ['FR', 'FRI', 'FRID'],
                                             'pointConstraint': ['PO']})
    result = abb.abbreviate(data, length=2)
    print(len(result))
