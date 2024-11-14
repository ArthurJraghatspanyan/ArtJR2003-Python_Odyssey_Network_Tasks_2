import yaml

if __name__ == "__main__":
    with open("config.yml") as f:
        file = yaml.load(f, Loader=yaml.FullLoader)
    
    file['server']['port'] = 9090

    # print(file) 

    with open("config.yml", 'w') as fw:
        yaml.dump(file, fw)