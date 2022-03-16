import pulumi
from pulumi_azure import containerservice, core


containerservice.KubernetesCluster(
    resource_name='michaellevanakscluster',
    default_node_group={
        'min_count': 2,
        'max_count': 10,
        'name': 'michaellevanakscluster',
        'vm_size': 'Standard_D12_v2',
        'enable_auto_scaling': True
    },
    dns_prefix='mynewdnsmichaellevan',
    resource_group_name='michaellevan-rg',
    service_principal={
        'client_id': '',
        'client_secret': ''
    }
)