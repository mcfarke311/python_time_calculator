def add_time(start, duration, startDay = None):
  
  # list of valid days in order to keep track of day difference if startDay is supplied
  validDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
  if startDay:
    startDayIndex = validDays.index(startDay.lower())

  # see whether current time is AM or PM
  curTimePM = (start.split(' ')[-1] == 'PM')

  # get current times hours and minutes
  curHours, curMinutes = start.split(':')
  curMinutes = curMinutes.split(' ')[0]

  # cast current time indicators as integers and convert to 24hour clock for easier calculations
  curHours = int(curHours)
  curMinutes = int(curMinutes)
  if curTimePM:
    curHours += 12

  # parse duration argument into hours and minutes cast as integers
  addHours, addMinutes = duration.split(':')
  addHours = int(addHours)
  addMinutes = int(addMinutes)

  # figure out if adding the minutes together rolls over the hour
  newHours = curHours
  newMinutes = curMinutes + addMinutes
  newHours += (newMinutes // 60)
  newMinutes %= 60

  # add our new hours and see if we roll over days
  newHours += addHours
  daydifference = newHours // 24
  newHours %= 24

  # determine if our final time will be in morning or afternoon
  newAMPM = 'AM'
  if newHours // 12 == 1:
    newAMPM = 'PM'

  # convert time back to 12hour time
  newHours %= 12
  if newHours == 0:
    newHours = 12
  
  # figure out how many days have passed since our initial time
  daydiffstring = ""
  if daydifference == 1:
    daydiffstring = " (next day)"
  if daydifference > 1:
    daydiffstring = " (%d days later)" % daydifference

  # if a start day was supplied, figure out what the end day is
  newDay = ""
  if startDay:
    newDayIndex = (startDayIndex + daydifference) % 7
    newDay = ", " + validDays[newDayIndex].capitalize()

  # format our final time string
  new_time = "%d:%02d %s%s%s" % (newHours, newMinutes, newAMPM, newDay, daydiffstring)

  return new_time