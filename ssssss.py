import os
import xml.etree.ElementTree as ET
import random
import math
import argparse
from tqdm import tqdm



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--indir', type=str,default='E:\datasets')
    parser.add_argument('-p', '--percent', type=float, default=0.2)
    parser.add_argument('-t', '--train', type=str, default='./datasets/train.csv')
    parser.add_argument('-v', '--val', type=str, default='./datasets/val.csv')
    parser.add_argument('-c', '--classes', type=str, default='./datasets/class.csv')
    args = parser.parse_args()
    return args

def get_file_index(indir, postfix):
    print(indir)
    file_list = []
    i=1
    for root, dirs, files in os.walk(indir):
        print(i)

        for name in files:
            if postfix in name:
                file_list.append(os.path.join(root, name))
    return file_list

args=parse_args()

li_st=get_file_index(args.indir,".jpg")