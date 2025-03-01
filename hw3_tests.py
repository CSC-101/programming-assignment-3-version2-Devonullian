import data
import build_data
import unittest

from data import CountyDemographics

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def population_total(county_population: list[CountyDemographics]) -> list[int]:
        population_total = sum(CountyDemographics.population)
        return population_total

    # test population_total
    def population_total_test(self):
        input = self.population_total
        result = self.population_total(input)
        expected = 318857056
        self.assertEqual(expected, result)


    # Part 2
    def filter_by_state(county_population: list[CountyDemographics], CA):
        CA = CountyDemographics({},{},{},{},{},{},'CA')
        if CountyDemographics.state == 'CA':
            return list[CA]
        else:
            return []

    # test filter_by_state
    def filter_by_state_test(self):
        input = CountyDemographics({},{},{},{},{},{},'TX')
        result = self.filter_by_state(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def population_by_education(county_population: list[CountyDemographics], Bachelor_Degree) -> float:
        Bachelor_Degree = CountyDemographics({},{},"Bachelor's Degree or Higher",{},{},{},{})
        if CountyDemographics.education == "Bachelor's Degree or Higher":
            return list[Bachelor_Degree]
        else:
            return []

    def population_by_ethnicity(county_population: list[CountyDemographics], Two_or_More_Races) -> float:
        Two_or_More_Races = CountyDemographics({},{},{'Two or More Races'},{},{},{},{})
        if CountyDemographics.ethnicity == "Two or More Races":
            return sum[Two_or_More_Races]
        else:
            return []

    def population_below_poverty_level(county_population: list[CountyDemographics], people) -> float:
        people = CountyDemographics({},{},{},{},'Persons Below Poverty Level',{},{})
        if CountyDemographics.income == 'Persons Below Poverty Level':
            return list[people]
        else:
            return []

    # test population_by_education
    def population_by_education_test(self):
        input = CountyDemographics({},{},{"Bachelor's Degree or Higher"},{},{},{},{})
        result = self.population_by_education(input)
        expected = 19511409.1
        self.assertEqual(expected, result)

    # test population_by_ethnicity
    def population_by_ethnicity_test(self):
        input = CountyDemographics({},{},{},{'Two or More Races'},{},{},{})
        result = self.population_by_ethnicity(input)
        expected = 2361395.1
        self.assertEqual(expected, result)

    # test population_below_poverty_level
    def population_below_poverty_level_test(self):
        input = CountyDemographics({},{},{},{},{'Persons Below Poverty Level'},{},{})
        result = self.population_below_poverty_level_test(input)
        expected = 10771171.4
        self.assertEqual(expected, result)

    # Part 4
    def percent_by_education(education: list[CountyDemographics], Bachelor_Degree) -> float:
        Bachelor_Degree: CountyDemographics({},{},"Bachelor's Degree or Higher",{},{},{})
        if CountyDemographics == Bachelor_Degree:
            return (sum[Bachelor_Degree]/CountyDemographics.population) * 100
        else:
            return []

    def percent_by_ethnicity(ethnicity: list[CountyDemographics], Two_Or_More_Races) -> float:
        Two_Or_More_Races: CountyDemographics({},{},{'Two or More Races'},{},{},{},{})
        if CountyDemographics == Two_Or_More_Races:
            return sum[Two_Or_More_Races]/CountyDemographics.population
        else:
            return []

    def percent_below_poverty_level(income: list[CountyDemographics]) -> float:
        income = CountyDemographics({},{},{},{},{'Persons Below Poverty Level'},{},{})
        if CountyDemographics == income:
            return sum[income]/CountyDemographics.population
        else:
            return []

    # test percent_by_education
    def percent_by_education_test(self):
        input = (sum[CountyDemographics.Bachelor_Degree]/CountyDemographics.population) * 100
        result = self.percent_by_education(input)
        expected = 6.1
        self.assertEqual(expected, result)

    # test percent_by_ethnicity
    def percent_by_ethnicity_test(self):
        input = (sum[CountyDemographics.Two_Or_More_Races]/CountyDemographics.population) * 100
        result = self.percent_by_ethnicity(input)
        expected = 0.7
        self.assertEqual(expected, result)

    # test percent_below_poverty_level
    def percent_below_poverty_level_test(self):
        input = (sum[CountyDemographics.income]/CountyDemographics.population) * 100
        result = self.percent_by_ethnicity(input)
        expected = 3.4
        self.assertEqual(expected, result)

    # Part 5
    def education_greater_than(education: list[CountyDemographics.Bachelor_Degree],  education_1: str, education_2: float) -> list[CountyDemographics]:
        education_1: CountyDemographics.Bachelor_Degree
        education_2: 100 * (sum(education_1))//CountyDemographics.population
        if education_2 >= 60:
            return education
        else:
            return None

    def education_less_than(education_A: list[CountyDemographics.Bachelor_Degree], education_1: str, education_2: float) -> list[CountyDemographics]:
        education_1: CountyDemographics.Bachelor_Degree
        education_2: 100 * (sum(education_1))//CountyDemographics.population
        if education_2 <= 30:
            return education_A
        else:
            return None

    def ethnicity_greater_than(ethnicity: list[CountyDemographics.Two_Or_More_Races], ethnicity_1: str, ethnicity_2: float) -> list[CountyDemographics]:
        ethnicity_1: CountyDemographics.Two_Or_More_Races
        ethnicity_2: 100 * (sum(ethnicity_1))//CountyDemographics.population
        if ethnicity_2 >= 5:
            return ethnicity
        else:
            return None

    def ethnicity_less_than(ethnicity_A: list[CountyDemographics.Two_Or_More_Races], ethnicity_1:str, ethnicity_2: float) -> list[CountyDemographics]:
        ethnicity_1: CountyDemographics.Two_Or_More_Races
        ethnicity_2: 100 * (sum(ethnicity_1))//CountyDemographics.population
        if ethnicity_2 <= 1:
            return ethnicity_A
        else:
            return None

    def below_poverty_level_greater_than(people: list[CountyDemographics.income], people_1: str, people_2: float) -> list[CountyDemographics]:
        people_1: CountyDemographics.income
        people_2: 100 * (sum(people_1))//CountyDemographics.income
        if people_2 >= 15:
            return people
        else:
            return None

    def below_poverty_level_less_than(people_A: list[CountyDemographics.income], people_1: str, people_2: float) -> list[CountyDemographics]:
        people_1: CountyDemographics.income
        people_2: 100 * (sum(people_1))//CountyDemographics.income
        if people_2 <= 15:
            return people_2
        else:
            return None

    # test education_greater_than
    def education_greater_than_test(self):
        input = self.education
        result = self.education_greater_than(input)
        expected = 0
        self.assertEqual(expected, result)

    # test education_less_than
    def education_less_than_test(self):
        input = self.education_A
        result = self.education_less_than(input)
        expected = 5
        self.assertEqual(expected, result)

    # test ethnicity_greater_than
    def ethnicity_greater_than_test(self):
        input = self.ethnicity
        result = self.ethnicity_greater_than(input)
        expected = 2
        self.assertEqual(expected, result)

    # test ethnicity_less_than
    def ethnicity_less_than_test(self):
        input = self.ethnicity_A
        result = self.ethnicity_less_than(input)
        expected = 2
        self.assertEqual(expected, result)

    # test below_poverty_level_greater_than
    def below_poverty_level_greater_than(self):
        input = self.poverty_level_greater_than
        result = self.poverty_level_greater_than(input)
        expected = 4
        self.assertEqual(expected, result)

    # test below_poverty_level_less_than
    def below_poverty_level_less_than(self):
        input = self.poverty_level_less_than
        result = self.poverty_level_greater_than(input)
        expected = 3
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
