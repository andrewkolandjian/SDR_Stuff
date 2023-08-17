from pcdr import ook_modulate, gnuradio_send
import time as t

def md(dat):
    return ook_modulate(dat, bit_length=int(1500))

forward=md([1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0])
backward=md([1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0])
left=md([1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0])
right=md([1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0])


## What I'm about to write is called a "closure"
## It's a function that returns a function.
def make_move_func(data_to_send):
    def actually_send_data():
        gnuradio_send(data_to_send, center_freq=27.16e6, samp_rate=2e6, if_gain=47)       
    return actually_send_data

M_forward = make_move_func(forward)
M_left = make_move_func(left)
M_right = make_move_func(right)
M_backward = make_move_func(backward)

while 2==2:
    M_forward()
    M_forward()
    M_left()
    M_left()
    M_backward()
    M_forward()

