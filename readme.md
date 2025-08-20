# Wikipedia 2 Gexf
### *There's a converter for everything these days!*

Wiki2Gexf is a python (3.13.5) project that allows you to run a breadth-first search on a locally stored (and indexed) Wikipedia archive, and then export this search to a .gexf format.

Example renders made in Gephi:
Chicory: A Colorful Tale             |  Wikipedia: Unusual Articles
:-------------------------:|:-------------------------:
<img width="2048" height="2048" alt="chicory" src="https://github.com/user-attachments/assets/578afd5d-14b9-48c6-bdb2-edeca05b6b34" /> | <img width="2048" height="2048" alt="strange2" src="https://github.com/user-attachments/assets/34c9d903-f9ac-44e9-b693-0f404258cc3b" />

## Setup/Install Guide
- To start, `clone` this repository. You will need to install the `NetworkX` package for Gexf functionality.
- Next: you will need to download two wikipedia archive files from [https://dumps.wikimedia.org/](https://dumps.wikimedia.org/). **MAKE SURE THEY HAVE THE SAME DATE**
  1. pages-articles-multistream.xml.bz2 --> The (heavily compressed) text archive of Wikipedia, should be well over 20GB. **Torrent if possible! DO NOT EXTRACT!**
  2. pages-articles-multistream-index.txt.bz2 --> The index of the byte offset for all articles in the multistream archive.
- Extract the index file
- Place both the index and the multistream files in the same directory as this repository.
- 
