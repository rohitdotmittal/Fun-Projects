import argparse as ap


parser = ap.ArgumentParser(description='Process some integers')
parser.add_argument('square', help="display the square of a given number", type=int)
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()
print (args.square**2)

def test_function(x=0):
  return x


if __name__== '__main__':
  test_function()
