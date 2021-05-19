import pulumi
from pulumi_azure import containerservice, core


containerservice.KubernetesCluster(
    resource_name='cloudskillsakscluster',
    default_node_group={
        'min_count': 2,
        'max_count': 10,
        'name': 'cloudskillsakscluster',
        'vm_size': 'Standard_D12_v2',
        'enable_auto_scaling': True
    },
    dns_prefix='mynewdnscloudskills',
    resource_group_name='cloudskills-rg',
    service_principal={
        'client_id': '',
        'client_secret': ''
    }
)