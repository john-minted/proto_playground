from car_pb2 import Car
from car_oneof_pb2 import CarOneOf
from car_repeat_pb2 import CarRepeat
from car_nested_pb2 import CarNested

def test_nested():
  """Test nested messages
  """
  print '### test nested messages ###'
  car_nested = CarNested()
  car_nested.id.id = 1
  print 'car id: ' + str(car_nested.id.id)


def test_not_set_is_none():
  """Show if an unset field shows up as none
  """
  print '### test not set is none ###'
  car1 = Car()
  num_wheels = car1.num_wheels
  if num_wheels is None:
    print 'not setting car1.num_wheels makes num_wheels None'
  else:
    print 'num_wheels type is {0}'.format(type(num_wheels))
    print 'num_wheels is {0}'.format(num_wheels)

  print 'running HasField shows if field is set'
  if car1.HasField('num_wheels'):
    print 'car1 has num_wheels set'
  else:
    print 'car1 does not have num_wheels set'


def test_oneof():
  """Show that schema with oneof can be backwards compatible with
  schema without oneof
  """
  print '### test car oneof ###'
  car1 = Car()
  car1.num_wheels = 4
  # car1.color = 'red'
  car1.brand = 'corvette'
  car1_bytes = car1.SerializeToString()
  print '-- car1 --'
  print car1_bytes

  car1_reloaded = Car()
  car1_reloaded.ParseFromString(car1_bytes)
  print '-- car1 loaded --'
  print car1_reloaded.num_wheels
  print car1_reloaded.color
  print car1_reloaded.brand

  car1_oneof = CarOneOf()
  car1_oneof.ParseFromString(car1_bytes)
  print '-- car1 oneof --'
  print car1_oneof.num_wheels
  print car1_oneof.color
  print car1_oneof.brand


def test_repeat():
  """Check how to process repeated attributes
  """
  print '### test car repeat ###'
  car = CarRepeat()
  print 'empty car seats list: len = {0}'.format(len(car.seats))
  car.seats.add()
  car.seats.add()
  car.seats[0].color = 'gross'
  car.seats[1].color = 'black'
  print 'added 2 car seats'
  print 'type:  ' + str(type(car.seats))
  print 'new len = {0}'.format(len(car.seats))

  print '--- new car w/o repeat field set ---'
  car_no_set = CarRepeat()
  print 'has name field: ' + str(car_no_set.HasField('name'))
  print 'len car_repeat.seats: ' + str(len(car_no_set.seats))
  try:
    if car_no_set.HasField('seats'):
      print 'call to HasField = true'
    else:
      print 'call to HasField = false'
  except ValueError as e:
    print 'cannot call HasField on repeat: ' + str(e)


def main():

  test_not_set_is_none()
  print ''
  print ''
  test_oneof()
  print ''
  print ''
  test_repeat()
  print ''
  print ''
  test_nested()


if __name__ == '__main__':
  print 'blah'
  main()
