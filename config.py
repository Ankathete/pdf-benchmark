import os


def tearup(batchId: str, industries: list):
    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs(f'data/{batchId}')
        print("Data directories created")
    for industry in industries:
        if not os.path.exists(f'data/{batchId}/{industry}'):
            os.makedirs(f'data/{batchId}/{industry}')
            print(f"Data directory for {industry} created")
