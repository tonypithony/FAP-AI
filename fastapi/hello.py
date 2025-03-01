# pip install fastapi uvicorn httpie requests httpx

from fastapi import FastAPI, Body
import uvicorn
import asyncio

app = FastAPI()

# @app.get('/hi/{who}') # http://127.0.0.1:9000/hi/Tony --> "Hello? Tony?"
@app.get('/hi') # http://127.0.0.1:9000/hi?who=Tony
async def green(who, ik="me:)"):
	await asyncio.sleep(1)
	return f"Hello? {who}? it's {ik}"

@app.post('/hi') # http://192.168.100.90:9000/hi?who=Jonny&ik=Thony --> "Hello? Jony? it's Thony"
def greet(who:str = Body(embed=True), ik:str = Body(embed=True)):
	return f"Hello? {who}? it's {ik}"

if __name__ == "__main__":
    uvicorn.run("hello:app", host="0.0.0.0", port=9000, reload=True) # http://0.0.0.0:9000/docs
    # loading ASGI app. Import string "app" must be in format "<module>:<attribute>".
