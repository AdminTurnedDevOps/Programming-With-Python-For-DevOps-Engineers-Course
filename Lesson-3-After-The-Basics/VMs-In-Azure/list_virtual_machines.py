from azure.cli.core import get_default_cli as azcli
import logging
import sys


def list_vms(resource_group):
    
    try:
        version = azcli().get_cli_version()
        print(f'AZ CLI version installed: {version}')
        
    except Exception as e:
        logging.error(msg='Azure CLI is not installed...')
        print(e)
    
    try:
        azcli().invoke(['vm', 'list', '-g', resource_group])
    
    except Exception as d:
        logging.error(msg='Please check your Azure CLI profile to confirm you have access to this resource...')
        print(d)


resource_group = sys.argv[1]


if __name__ == '__main__':
    print('Running as main program...')
    list_vms(resource_group)

else:
    print('Running as imported program...')
    list_vms(resource_group)