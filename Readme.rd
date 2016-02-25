Each Folder hold the source code required for the given layer.

Version 0.1


Application	-> In the current implementation it is a web app that 
		   will send a signal to the sever to do an action
		->Will reside in the application server
		->Will be programmed in <--Insert the to be programing language here-->

Communication	->This takes care of the time keeping and the triggering
		  of the entire system. This is the layer that will communicate
		  with the physical layer.
		->Will be the link to the application server to the local server
		->Will be programmed mostly in python

Physical	->This layer takes care of the raw hardware and physical 
		  trigering system. 
		->Will reside in the local hardware.
		->Will be programmed in Arduino C.
