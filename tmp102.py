import mraa as m

# Init I2C
x = m.I2c(6)

# Some addresses
_i2caddr              = 0x48

# Check that we're connected to the TMP102 chip
try:
    x.address(_i2caddr)
    print "Test 1 = " + str(x.readWordReg(0x00))
    print "Test 2 = " + str(x.read(2))
    print "Test 3 = " + str(x.readByte())
except:
    print "TMP102 Device Not Connected!"