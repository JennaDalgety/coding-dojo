def soaring_iq():

  iq = 101
  iq_raise = .01
  

  while iq_raise < .99:
    iq += iq_raise
    iq_raise += .01

  print iq


soaring_iq()