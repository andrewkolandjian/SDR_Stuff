from guizero import App, TextBox, Tk, PushButton
from pcdr import ook_modulate, gnuradio_send
import time as t



## this is just stylistic preference; feel free to change back
def md(dat):
    return ook_modulate(dat, bit_length=int(1500))

forward_data=md([1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0])
backward_data=md([1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0])
left_data=md([1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0])
right_data=md([1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0])




## What I'm about to write is called a "closure"
## It's a function that returns a function.
def make_move_func(data_to_send):
    def actually_send_data():
        gnuradio_send(data_to_send, center_freq=27.16e6, samp_rate=2e6, if_gain=47)       
    return actually_send_data



app = App()
# # When the mouse enters the TextBox
# app.when_key_pressed = highlight
# # When the mouse leaves the TextBox
# app.when_key_released = lowlight

# So make_move_func(ookmodded_left) returns the function that actually sends the data
# If you want, after you're done, you can show Dean; he may be interested

## Let's not test it now since we're about to start the test
f_btn = PushButton(app, text = "Forward", command=make_move_func(forward_data))
f_btn = PushButton(app, text = "Left", command=make_move_func(left_data))
f_btn = PushButton(app, text = "Right", command=make_move_func(right_data))
f_btn = PushButton(app, text = "Backward", command=make_move_func(backward_data))

app.display()

