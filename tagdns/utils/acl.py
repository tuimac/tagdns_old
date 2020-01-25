class Acl:
    def filter(targetip, acl):
        for iprange in acl:
            networkipBit = 0
            targetipBit = 0
            networkip, subnet = iprange.split("/")
            subnet = int(subnet)
            subnetBit = ((1 << subnet) - 1) << (32 - subnet)
            for octet in networkip.split("."): networkipBit = (networkipBit << 8) + int(octet)
            for octet in targetip.split("."): targetipBit = (targetipBit << 8) + int(octet)
            targetipBit = targetipBit & subnetBit
            if targetipBit == networkipBit: return 0
        return 5
