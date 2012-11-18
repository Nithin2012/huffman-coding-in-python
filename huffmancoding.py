from collections import Counter
      
class codeTree(object):
  def __init__(self, pairs, weight,left=None, right = None):
    self.pairs = pairs
    self.weight = weight
    self.left = left
    self.right = right
  
  def __repr__(self):
    return repr(self.pairs) + ", " + repr(self.weight)

  def _add_(self, other):
    total_weight = self.weight + other.weight
    for e in self.pairs:
      e[1] = "1" + e[1]
    for p in other.pairs:
      e[1] = "0" + e[1]
    new_pairs = self.pairs + other.pairs
    return codeTree(new_pairs, total_weight)

def frequency (s) :
    freqs = {}
    for ch in s :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs

def sortFreq (freqs) :
    chars = freqs.keys()
    tuples = []
    for l in chars :
        tuples.append((freqs[l],l))
    tuples.sort()
    return tuples

def make_codetree(tuples) :
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])                  
        theRest  = tuples[2:]                          
        combFreq = leastTwo[0][0] + leastTwo[1][0]     
        tuples   = theRest + [(combFreq,leastTwo)]     
        tuples.sort()                                  
    return tuples[0]  

def encoding(s):
  frq_tbl = Counter(s)
  table1 = []
  for i, j in frq_tbl.items():
    table1.append([i, j])
  table1 = sorted(table1, key = lambda p : p[1])
  print(table1)
  table = []
  for e in table1:
    sym = e[0]
    freq = e[1]
    table.append(codeTree([[sym, ""]], freq))
  while len(table) > 1:
    node1 = table.pop(0)
    node2 = table.pop(0)
    new_node = node1._add_(node2)
    table.append(new_node)
    table = sorted(table, key = lambda n : n.weight)
    print(table)
  print 'the huffman code of the given string'
  return dict(map(lambda p: (p[0], p[1]), table[0].pairs))

def decode (tree, r) :
    output = ""
    e = tree
    for x in r:
        if x == '0' : e = e[0]     
        else          : e = e[1]     
        if type(p) == type("") :     
            output += e              
            e = tree                
    return output

def main():
	print 'enter the string'
	s = raw_input()
	print 'the code table'	
	q = encoding(s)
	print q
	print 'enter the code'
	r = raw_input()
	freqs = frequency(r)
        tuples = sortFreq(freqs)
        tree = make_codetree(tuples)
	print (decode(tree,r))
if __name__ == '__main__':
	main()





























