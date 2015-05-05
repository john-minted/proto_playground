from car_pb2 import Car
from car_oneof_pb2 import CarOneOf
from car_repeat_pb2 import CarRepeat


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


def main():

  test_oneof()
  print ''
  print ''
  test_repeat()

if __name__ == '__main__':
  print 'blah'
  main()
