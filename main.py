from testers import Tester
if __name__ == '__main__':
  tester = Tester()
  tester.test_number_to_pair(4, 'White', 'Brown')
  tester.test_number_to_pair(5, 'White', 'Slate')
  tester.test_pair_to_number('Black', 'Orange', 12)
  tester.test_pair_to_number('Violet', 'Slate', 25)
  tester.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
