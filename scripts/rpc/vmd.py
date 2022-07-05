def enable_vmd(client):
    """Enable VMD enumeration."""
    return client.call('enable_vmd')


def vmd_remove_device(client, addr):
    """Remove a device behind VMD"""
    return client.call('vmd_remove_device', {'addr': addr})
