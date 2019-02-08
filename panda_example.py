import pandas

pandas.set_option('display.max_columns', 10)
a={'measurement': [1,2],
   'Error_in_meas': [4,4],
   'Estimate': [68, 70.33],
   'Error_in_previous_estimate': [2, 2],
   'KG': [0.33, 0.25],
   'Error_in_current_estimate': [1.33, 1.00]}

print(pandas.DataFrame(a))