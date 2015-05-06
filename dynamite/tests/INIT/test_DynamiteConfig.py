__author__ = 'brnr'

if __name__ == '__main__':
    x = {'Dynamite': {
      'Service': {
        'apache': {
          'unit_is_template': True,
          'base_instance_prefix_number': 8080,
          'name_of_unit_file': 'apache@.service',
          'max_instance': 5,
          'service_announcer': 'zurmo_apache_discovery',
          'etcd_path': '/services/apache/scaling_rules',
          'scale_down_policy': {
            'ScalingPolicy': 'scale_down'
            },
          'scale_up_policy': {
            'ScalingPolicy': 'scale_up'
            },
          'service_dependency': ['zurmo_application', 'zurmo_config'],
          'min_instance': 2
        },
        'haproxy': {
          'min_instance': 1,
          'max_instance': 1,
          'service_announcer': 'zurmo_haproxy_discovery',
          'unit_is_template': False,
          'etcd_path': '/services/haproxy/scaling_rules',
          'name_of_unit_file': 'haproxy.service',
          'base_instance_prefix_number': 80
        }
      },
      'UnitFiles': {
        'PathList': ['C:\\Users\\brnr\\PycharmProjects\\unit2json\\github\\com\\sandorkan\\unit2json', '/etc/dynamite/unit_files']
      },
      'FleetAPIEndpoint': {
        'IP': '172.17.8.101',
        'Port': 49153
      },
      'ScalingPolicy': {
        'scale_up': {
          'comparative_operator': 'gt',
          'cooldown_period_unit': 'minute',
          'metric': {
            'service': 'zurmo_haproxy',
            'name': 'response_time'
          },
          'period_unit': 'second',
          'period': 15,
          'cooldown_period': 1,
          'threshold': 250,
          'treshold_unit': 'micro_second'
        },
        'scale_down': {
          'comparative_operator': 'lt',
          'cooldown_period_unit': 'minute',
          'threshold_unit': 'percent',
          'metric': 'cpu_load',
          'period_unit': 'second',
          'period': 30,
          'cooldown_period': 1,
          'threshold': 30
        }
      }
    }}

    print(x['Dynamite'])
    print(x['Dynamite']['FleetAPIEndpoint'])
    print(x['Dynamite']['FleetAPIEndpoint']['IP'])