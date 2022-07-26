from get_color_func import *

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def print_color_code():
  k = 1
  with open('manual.txt','w') as redme:
    for i in range(0,5):
      for j in range(0,5):
          pair_info = ['Pair number: ', str(k),' major color:',MAJOR_COLORS[i],' ',' minor_color:',MINOR_COLORS[j]]
          with open('manual.txt','a') as redme:
            redme.writelines(' '.join(map(str, pair_info)))
            redme.writelines('\n')
          print(pair_info)
          k=k+1

if __name__ == '__main__':
  print('Color Code Manual:')
  print_color_code()
  print('Manual is done :)')