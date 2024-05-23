import argparse
import nmap

def argument_parser():
    parser=argparse.ArgumentParser(description="TCP port scanner, will accept hostname/IP address along with a list of ports to scan.")
    parser.add_argument("-o","--host",nargs="?",help="hostname or IP address")
    parser.add_argument("-p","--ports",nargs="?",help="comma separated list of ports to scan. Example:'22,80,443,8080'")
    var_args=vars(parser.parse_args())
    return var_args

def nmap_scan(host_id,port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id,port_num)
    print(nm_scan[host_id])
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    name = nm_scan[host_id]['tcp'][int(port_num)]['name']
    result=f"[*]{host}tcp/{port}{state}{name}"
    return result

if __name__ == '__main__':
    try:
        user_args=argument_parser()
        host = user_args["host"]
        ports = user_args["ports"].split(",")
        for port in ports:
            print(port)
            print(nmap_scan(host,port.strip()))
    except AttributeError:
        print("Error in input. Please provide the command line arguments before running the script.")