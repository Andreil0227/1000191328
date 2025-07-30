import uvicorn


def start():
    uvicorn.run(
        "apibase64:app",
        host="10.13.165.6",
        port=8070,
        reload=True
    )


if __name__ == '__main__':
    start()