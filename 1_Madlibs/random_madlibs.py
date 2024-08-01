from sample_madlibs import cricket,data_analysis,madlib,retro_gaming
import  random

if __name__ == "__main__":
    m = random.choice([cricket, data_analysis, madlib, retro_gaming])
    m.madlib()