def throw_me_an_error():
  val1 = 14
  val2 = 0
  return val1 / val2

def throw_me_an_error_v2():
  val1 = 14
  val2 = 0
  try:
    return val1 / val2
  except Exception as e:
    print(f'Exception: {e}')



#print(f'1st Version of Function:\n')
#throw_me_an_error()
print(f'2nd Version of Function:\n')
throw_me_an_error_v2()
