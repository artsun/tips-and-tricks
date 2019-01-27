def iptonum(ip=''):
  """
  accepts string of dotted ip (exmpl: 192.168.1.2)
  returns int
  """
  ip = ip.split('.')
  num = list()
  [num.append(str(bin(int(i)))[2:]) for i in ip]
  num_new = list()
  [num_new.append((lambda x_ = x: '0'*(8-len(x_))+x_)(x))  for x in num]
  return int(''.join(num_new), 2)
