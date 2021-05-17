import pulumi
from pulumi_azure import containerservice, core


containerservice.KubernetesCluster(
    resource_name='cloudskillsaks',
    default_node_group={
        'min_count': 1,
        'max_count': 1,
        'name': 'cloudskillsaks',
        'vm_size': 'Standard_D12_v2',
        'enable_auto_scaling': True
    },
    dns_prefix='cloudskillsdns',
    resource_group_name='cloudskills-rg',
    service_principal={
        'client_id': '',
        'client_secret': ''
    }
)