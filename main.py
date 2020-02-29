
import uvicorn

if __name__=='__main__':
    uvicorn.run(
        'src.server:app',
        debug=True,
        reload=True
    )