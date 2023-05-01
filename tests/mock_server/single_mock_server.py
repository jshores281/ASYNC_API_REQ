

import asyncio
from aiohttp import web



async def handle_get(request):
    response_data = {'message': 'Hello, world!'}
    return web.json_response(response_data)



app = web.Application()
app.add_routes([web.get('/', handle_get)])
app.TCPSite(runner, 'localhost', 8001)

web.run_app(app)





"""
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8001)
    await site.start()
    print('Mock server started at http://localhost:8001')




asyncio.run(start_mock_server())
"""

