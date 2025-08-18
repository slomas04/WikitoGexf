import argparse as arg
import json
import os
import time
import networkx as nx

argparser = arg.ArgumentParser(description="Merge two sociogram databases", prog="Database Merger")
argparser.add_argument( "-x", "--x", help="Database X", required=True, type=str)
argparser.add_argument("file", help="Output file")
args = argparser.parse_args()

G = nx.DiGraph()

with open(args.x, "r") as file_inst:
            jsonDict = json.load(file_inst)
            for user in jsonDict['users']:
                G.add_node(user['username'])
            for user in jsonDict['users']:
                if "following" in user:
                    for fId in user['following']:
                        G.add_edge(user['username'], fId[1])

nx.write_gexf(G, args.file)

