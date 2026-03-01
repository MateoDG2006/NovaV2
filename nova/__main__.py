import uvicorn

def main():
    uvicorn.run(
        "nova.api:app",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()