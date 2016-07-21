# ShopTraffic - Track & measure the traffic of your business!
ShopTraffic is a simple utility that helps you measure everything that happens in your business, so you can have a better understanding of your customers.

* Place the tracker device in your store
* Our device identifies customers via a WiFi connection on their phones
* Begin measuring and analyzing the traffic of your customers to evaluate and optimize your business performance!


### Technical details
Our device is a simple Raspberry Pi with a WiFi dongle. The Raspberry Pi detects new customers by their WiFi connections - we search for new WiFi connections with the airodump-ng library, and keep a record for every customer we find.

Every piece of data that we collect is sent to our Redshift Cluster via ironSource Atom, which makes it extremely easy for us to collect the enormous amount of data our device produces.

Once we've collected enough data on our customers, we can begin analyzing everything that's happening in the store! By using simple SQL queries we can calculate so many interesting facts about the behavior of the customers and the store -
* How long does the average customer tend to stay in our store?
* What are the peak hours in which customers enter our store?
* How frequently do customers return?
* How often do we welcome a new customer?
