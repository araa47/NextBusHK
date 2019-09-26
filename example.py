
import pprint 
import nextBusApi

# init 
bus = nextBusApi.NextBusArrivalTimeAPI() 
# Call get route_stop method 
route = bus.get_route_stop("NWFB", "2", "inbound")
# iterate through each point 
for points in route.get("data", []):
    # get stop number
    stop_number = points.get("stop")
    # Call get_stop method , to get details about the stop 
    stop_details = bus.get_stop(stop_number)
    # Get the data part of the response 
    stop_details = stop_details.get("data",{})
    # Print cleanly 
    pprint.pprint(stop_details)

# Get ETA for a certain bus 
eta = bus.get_eta("NWFB","001207", "2")
pprint.pprint(eta)
