import random
import heapq
import matplotlib.pyplot as plt

# simulation params
CAPACITY = 10
SIM_TIME = 7200

random.seed(42)

# global state
events = []
queue = []
busy = False
logs = []
missed = 0
total_people = 0
total_cars = 0
arrival_times = {}
times = []
area = 0
last_time = 0
t_points = []
cars_over_time = []

def update_area(t):
    global area, last_time
    dt = t - last_time
    area += dt * (len(queue) + (1 if busy else 0))
    last_time = t

def schedule(t, car, people, etype):
    heapq.heappush(events, (t, car, people, etype))

def do_arrival(t, car, people):
    global busy, missed, total_people, total_cars
    update_area(t)
    logs.append((t, car, "Arriving", len(queue) + (1 if busy else 0)))
    total_people += people
    total_cars += 1
    arrival_times[car] = t

    if len(queue) >= CAPACITY:
        missed += 1
    elif busy:
        queue.append((car, people))
    else:
        busy = True
        delay = random.uniform(60, 120)
        schedule(t + delay, car, people, "Testing")

def do_testing(t, car, people):
    update_area(t)
    logs.append((t, car, "Testing", len(queue) + (1 if busy else 0)))
    duration = 4 * 60 * people
    schedule(t + duration, car, people, "Leaving")

def do_leaving(t, car, people):
    global busy
    update_area(t)
    logs.append((t, car, "Leaving", len(queue) + (1 if busy else 0)))
    times.append(t - arrival_times[car])

    if queue:
        next_car, next_people = queue.pop(0)
        delay = random.uniform(60, 120)
        schedule(t + delay, next_car, next_people, "Testing")
    else:
        busy = False

# generate arrivals
t = 0
car = 1
while t < SIM_TIME:
    t += random.uniform(30, 120)
    if t < SIM_TIME:
        people = random.randint(1, 5)
        schedule(t, car, people, "Arrival")
        car += 1

# run
while events:
    t, car, people, etype = heapq.heappop(events)
    if etype == "Arrival":
        do_arrival(t, car, people)
    elif etype == "Testing":
        do_testing(t, car, people)
    elif etype == "Leaving":
        do_leaving(t, car, people)
    t_points.append(t)
    cars_over_time.append(len(queue) + (1 if busy else 0))

for x in logs:
    print(x)

print("Total cars missed:", missed)
print("Average people per car:", round(total_people / total_cars, 2))
print("Average cars in system:", round(area / last_time, 2))

plt.step(t_points, cars_over_time)
plt.xlabel("Time")
plt.ylabel("Cars")
plt.title("Cars over time")
plt.grid()
plt.show()

plt.hist(times, bins=20)
plt.xlabel("Time in system")
plt.ylabel("Frequency")
plt.title("Dwell time")
plt.grid()
plt.show()

# capacity comparison - reset everything and rerun for each cap
for cap in [10, 12, 14, 16]:
    events2 = []
    queue2 = []
    busy2 = False
    missed2 = 0
    total_people2 = 0
    total_cars2 = 0
    arrival_times2 = {}
    area2 = 0
    last_time2 = 0

    t = 0
    car = 1
    while t < SIM_TIME:
        t += random.uniform(30, 120)
        if t < SIM_TIME:
            people = random.randint(1, 5)
            heapq.heappush(events2, (t, car, people, "Arrival"))
            car += 1

    while events2:
        t, car, people, etype = heapq.heappop(events2)
        dt = t - last_time2
        area2 += dt * (len(queue2) + (1 if busy2 else 0))
        last_time2 = t

        if etype == "Arrival":
            total_people2 += people
            total_cars2 += 1
            arrival_times2[car] = t
            if len(queue2) >= cap:
                missed2 += 1
            elif busy2:
                queue2.append((car, people))
            else:
                busy2 = True
                heapq.heappush(events2, (t + random.uniform(60, 120), car, people, "Testing"))
        elif etype == "Testing":
            heapq.heappush(events2, (t + 4 * 60 * people, car, people, "Leaving"))
        elif etype == "Leaving":
            if queue2:
                nc, np = queue2.pop(0)
                heapq.heappush(events2, (t + random.uniform(60, 120), nc, np, "Testing"))
            else:
                busy2 = False

    print(f"Capacity {cap}: cars missed = {missed2}")