from getArticle import get_inlinks_from_name, get_inlinks_from_url

import argparse as arg
import networkx as nx

G = nx.DiGraph()

def addNodeAndLinks(node, links):
    global G
    G.add_node(node)
    G.add_nodes_from(links)
    for link in links:
        G.add_edge(node, link)

argparser = arg.ArgumentParser(description="Create a GEXF scrape from a BFS on a wikipedia archive", prog="Wikipedia 2 Gexf")
argparser.add_argument( "-n", "--name", help="Article Name", type=str)
argparser.add_argument( "-u", "--url", help="Article URL", type=str)
argparser.add_argument( "-d", "--depth", default=1, help="Depth of BFS")
argparser.add_argument("file", help="Output file")
args = argparser.parse_args()

if args.name == None and args.url == None:
    print("Please specify a name or a URL!")
    exit()


if args.name != None:
    startingTitle = args.name
    nextLinks = get_inlinks_from_name(args.name)
else:
    startingTitle = args.url
    nextLinks = get_inlinks_from_url(args.url)

addNodeAndLinks(startingTitle, nextLinks)
linkBuf = []

for d in range(0, int(args.depth)):
    for name in nextLinks:
        name = name.split("|")[0]
        b = get_inlinks_from_name(name)
        addNodeAndLinks(name, b)
        linkBuf += b
    
    nextLinks = linkBuf
    linkBuf = []


nx.write_gexf(G, args.file)