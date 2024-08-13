def frequency(seq):
  freq = {}
  for ele in seq:
    if ele not in freq:
      freq[ele] = 1
    else:
      freq[ele] += 1

  (min_freq, max_freq) = ([],[])
  for key in freq.keys():
    if not min_freq:
      min_freq.append(key)
    if not max_freq:
      max_freq.append(key)
    if min_freq and freq[min_freq[0]] > freq[key]:
      min_freq.clear()
      min_freq.append(key)
    elif freq[key] == freq[min_freq[0]] and key not in min_freq:
      min_freq.append(key)
    if max_freq and freq[max_freq[0]] < freq[key]:
      max_freq.clear()
      max_freq.appen(key)
    elif freq[key] == freq[max_freq[0]] and key not in max_freq:
      max_freq.append(key)
  return (sorted(min_freq), sorted(max_freq))

print(frequency([13,12,11,13,14,13,7,11,13,14,12]))
print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]))
print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))