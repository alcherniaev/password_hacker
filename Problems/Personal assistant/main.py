import time
time_ = time.localtime()
user_time = time.strftime("%H:%M", time_)
print(f"It's {user_time}")
