
#YsTorrent using python


YsTorrent is a CLI tool that downloads files from the BitTorrent network.


It is almost written from scratch with python 3.7, only the pubsub library was used to create events when a new peer is connected, or when data is received from a peer.
You first need to wait for the program to connect to some peers first, then it starts downloading.

YsTorrent needs a lot of improvements, but it does its job, you can :
-	Read a torrent file
-	Scrape udp or http trackers
-	Connect to peers
-	Ask them for the blocks you want
-	Save a block in RAM, and when a piece is completed and checked, write the data into your hard 		drive
-	Deal with the one-file or multi-files torrents
-	Leech or Seed to other peers

But you can’t :
-	Download more than one torrent at a time
-	Pause and resume download


### Installation
You can run the following command to install the dependencies using pip

`pip install -r requirements.txt`

## Running the program

###simply run this command

python3 YsTorrent.py "Filename"



The files will be downloaded in the same path as your main.py script.

### References :
 
[Kristen Widman's](http://www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-1 "Kristen Widman's blog") & the
[Bittorrent Unofficial Spec](https://wiki.theory.org/BitTorrentSpecification "Bittorrent Unofficial Spec"),thank you.



