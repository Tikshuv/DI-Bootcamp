import requests
import time

response = requests.post('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(response.elapsed.total_seconds())
response = requests.post('https://octopus.developers.institute/courses/')
print(response.elapsed.total_seconds())
response = requests.post('https://norvig.com/ngrams/sowpods.txt')
print(response.elapsed.total_seconds())
response = requests.post('https://www.google.com/')
print(response.elapsed.total_seconds())
s_time = time.time()
response = requests.post('https://www.google.com/')
e_time = time.time()
time_taken = round(e_time - s_time, 7)
print(time_taken)
