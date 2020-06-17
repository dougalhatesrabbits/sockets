import pickle
import msgpack
import json
import timeit
import numpy as np

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[3])



num_tests = 10

obj = np.random.normal(0.5, 1, [240, 320, 3])

command = 'pickle.dumps(obj)'
setup = 'from __main__ import pickle, obj'
result = timeit.timeit(command, setup=setup, number=num_tests)
print("pickle:  %f seconds" % result)

command = 'json.dumps(obj.tolist())'
setup = 'from __main__ import json, obj'
result = timeit.timeit(command, setup=setup, number=num_tests)
print("json:   %f seconds" % result)

command = 'msgpack.packb(obj.tolist())'
setup = 'from __main__ import msgpack, obj'
result = timeit.timeit(command, setup=setup, number=num_tests)
print("msgpack:   %f seconds" % result)