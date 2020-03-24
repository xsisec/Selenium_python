import os
import sys
import unittest
import time


# Log message to console and a Py log.
def log(msg) :
    if msg == "" :
        return
    header = ''
    message = "%s%s: %s" % (header, time.strftime("%H:%M:%S"), msg)
    fileWrite = open("PyLog.log", "a")
    fileWrite.write(message)
    fileWrite.close()
    print(message)
    sys.stdout.flush()


class SoftwareTest(unittest.TestCase) :

    def setUp(self) :
        # Setting up Test
        log("Setting up Test")

        log("Invoke extended Super class methods, ostensibly a base class for this test")
        # super(GameAppiumTest, self).setUp()
        log("setup complete!")

    # Test start.
    def test_stt(self) :
        log("Testing Stuff")


if __name__ == '__main__' :
    unittest.main(failfast=False, buffer=False, catchbreak=False)