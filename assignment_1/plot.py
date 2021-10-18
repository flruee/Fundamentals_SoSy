import glob
import pandas as pd
import matplotlib.pyplot as plt
def main():
    da_name = "retrieve"
    files = glob.glob("results/ipfs/*"+da_name+"*.txt")
    #plt.figure(figsize=(8, 3))
    for file in files:
        if("cat" in file):
            continue
        datas = pd.read_csv(file, delimiter=';', header=None)
        elapsed_time = datas.loc[:, 1] - datas.loc[:, 0]
        label = ""
        if "csv" in file:
            label+="csv"
        elif "pickle" in file:
            label+="pickle"
        else:
            continue
        if "mb" in file.lower():
            if("100") in file:
                label+=" 100mb"
            else:
                label+=" 1mb"
        else:
            label += " 1gb"
        print(elapsed_time)
        plt.plot(elapsed_time, label=label)
        plt.ylabel('Time elapsed')

        #png_name = txt.removesuffix(".txt")
    plt.title(da_name)
    plt.xlabel("Run")
    plt.ylabel("Time elapsed (seconds)")
    plt.legend()
    plt.savefig("results/plots_2/"+da_name + ".png")
    print(files)
    

def main2():
    da_name = "Http download"
    files = glob.glob("results/http/*.txt")
    #plt.figure(figsize=(8, 3))
    for file in files:
        if("cat" in file):
            continue
        datas = pd.read_csv(file, delimiter=';', header=None)
        elapsed_time = datas.loc[:, 1] - datas.loc[:, 0]
        label = ""

        if "mb" in file.lower():
            if("100") in file:
                label+=" 100mb"
            else:
                label+=" 1mb"
        else:
            label += " 1gb"
        print(elapsed_time)
        plt.plot(elapsed_time, label=label)
        plt.ylabel('Time elapsed')

        #png_name = txt.removesuffix(".txt")
    plt.title(da_name)
    plt.xlabel("Run")
    plt.ylabel("Time elapsed (seconds)")
    plt.legend()
    plt.savefig("results/plots_2/"+da_name + ".png")
    print(files)
    
if __name__ == "__main__":
    main2()