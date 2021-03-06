__author__ = 'brnr'

import requests
import etcd

# Instance Variables
etcdctl = None     # Is instance of ETCD class and used to communicate with etcd

ip = None
port = None

etcd_base_url = None

is_connected = None

etcd_key_base_path = "/_dynamite"

etcd_key_application_status = etcd_key_base_path + "/state/application_status"
etcd_key_init_application_configuration = etcd_key_base_path + "/init/application_configuration"
etcd_key_running_services = etcd_key_base_path + "/run/service"
etcd_name_fleet_service_template = "fleet_service_template"

# etcd_key_application_status = "/_dynamite/state/application_status"
# etcd_key_init_application_configuration = "_dynamite/init/application_configuration"
# etcd_key_running_services = "_dynamite/run/service"


def test_connection(etcd_base_url):
    global is_connected

    request_url = etcd_base_url + "_etcd/config"

    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            is_connected = True
            return True
        else:
            return False

    except requests.exceptions.ConnectionError:
        print("Error connecting to ETCD. Check if Endpoint is correct: " + self.ip + ":" + self.port)


def create_etcdctl(etcd_endpoint):

    global etcd_base_url
    global etcdctl
    global ip
    global port

    if etcdctl is not None:
        return etcdctl

    if type(etcd_endpoint) != str:
        raise ValueError("Error: argument <arg_etcd_endpoint> needs to be of type <str>. Format: [IP]:[PORT]")

    try:
        etcd_endpoint.split(":")
    except ValueError:
        print("Wrong format of <arg_etcd_endpoint> argument. Format needs to be [IP]:[PORT]")
        return None

    if len(etcd_endpoint.split(":")) == 2:
        ip, port = etcd_endpoint.split(":")

        etcd_base_url = "http://" + ip + ":" + port + "/v2/keys/"

        if test_connection(etcd_base_url):
            etcdctl = etcd.Client(ip, int(port))
        else:
            raise ConnectionError("Error connecting to ETCD. Check if Endpoint is correct: " + ip_address + ":" + port_number)

        if etcdctl is not None:
            return etcdctl
        else:
            return None
    else:
        raise ValueError("Error: Probably wrong format of argument <arg_etcd_endpoint>. Format: [IP]:[PORT]")


def get_etcdctl():

    global etcd_base_url
    global etcdctl

    if etcdctl is not None:
        return etcdctl
    else:
        return None