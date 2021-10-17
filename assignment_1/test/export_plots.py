import glob
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    try:
        txt_files = glob.glob("results/http/*.txt")
        found_files = 0
        
        for txt in txt_files:          
            datas = pd.read_csv(txt, delimiter=';', header=None)
            elapsed_time = datas.loc[:, 0] - datas.loc[:, 1]
            plot_title = txt.replace("results/","").replace("/", "_").replace(".txt", "")
            #plot_title = txt.removesuffix(".txt")
            #plot_title = plot_title.removeprefix("results/*")
            #plot_title = plot_title.capitalize()

            plt.figure(figsize=(8, 3))
            plt.title(plot_title)
            plt.plot(elapsed_time)
            plt.ylabel('Time elapsed')
            print(plot_title)
            #png_name = txt.removesuffix(".txt")
            plt.savefig("results/plots/"+plot_title + ".png")

            found_files += 1

        if(found_files == 0 ):
            print("No txt files found in results folder")

    except Exception as e:
       print(e)


