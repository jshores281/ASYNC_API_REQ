
# get athousand GET requests from private server

import asyncio
import aiohttp
import time



URL = "http://127.0.0.1:8000/{}"
endpoint = ["vault1"]


results = []
start = time.time()

endpoints = endpoint




# event loop
def get_tasks(session):
	tasks = []
	for ep in endpoints:
		tasks.append(asyncio.create_task(session.get(URL.format(ep), ssl=False)))
	return tasks





async def get_req():
	async with aiohttp.ClientSession() as session:
		tasks = get_tasks(session)
		tasks = [session.get(URL.format(ep), ssl=False) for ep in endpoints]

		responses = await asyncio.gather(*tasks)
		for response in responses:
			results.append(await response.json())
		for ordered_resp in results:
			print(ordered_resp)




asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_req())






end = time.time()
total_time = end - start

print("It took {} seconds to make {} API calls".format(total_time, len(endpoints)))
