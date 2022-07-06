# This was referenced from...anfractuosity on GitHub
## https://github.com/raspberrypi/firmware/issues/1167#issuecomment-511798033

import picamera
from picamera import mmal 
import ctypes as ct

class PiCamera2(picamera.PiCamera):
    AWB_MODES = {
        'off':           mmal.MMAL_PARAM_AWBMODE_OFF,
        'auto':          mmal.MMAL_PARAM_AWBMODE_AUTO,
        'sunlight':      mmal.MMAL_PARAM_AWBMODE_SUNLIGHT,
        'cloudy':        mmal.MMAL_PARAM_AWBMODE_CLOUDY,
        'shade':         mmal.MMAL_PARAM_AWBMODE_SHADE,
        'tungsten':      mmal.MMAL_PARAM_AWBMODE_TUNGSTEN,
        'fluorescent':   mmal.MMAL_PARAM_AWBMODE_FLUORESCENT,
        'incandescent':  mmal.MMAL_PARAM_AWBMODE_INCANDESCENT,
        'flash':         mmal.MMAL_PARAM_AWBMODE_FLASH,
        'horizon':       mmal.MMAL_PARAM_AWBMODE_HORIZON,
        'greyworld':     ct.c_uint32(10)
        }
