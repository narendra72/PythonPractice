class car():
  def start(self):
    print("Car is starting now")

  def stop(self):
    print("Car is stop now")

class bmwcar(car):
  def play_music(self):
    print("Playing music in the car")


c1 = bmwcar()

c1.start()
c1.stop()
c1.play_music()

