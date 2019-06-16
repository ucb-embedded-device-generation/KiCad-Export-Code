def print_block_comp(block_name: str) -> str:
    return '(comp (ref {})'.format(block_name)

def print_block_value(block_value: str) -> str:
    return '(value {})'.format(block_value)

def print_block_footprint(block_footprint: str) -> str:
    return '(footprint {})'.format(block_footprint)

def print_block_tstamp(block_name: str) -> str:
    return '(tstamp {}))'.format(block_name)

def block_exp(dict: dict[]) -> str:
        """Given a dictionary of block_names (strings) as keys and Blocks (namedtuples) as corresponding values

        Example:
        (components
        (comp (ref U1)
        (value LM555)
        (footprint Package_DIP:DIP-4_W7.62mm)
        (tstamp U1))
        (comp (ref R3)
        (value 1k)
        (footprint OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical)
        (tstamp R3))

        """
        result = '(components ' 
        for (block_name, block) in dict.items():
            result += print_block_comp(block_name) + ' ' + print_block_value(block.value) + ' ' + print_block_footprint(block.footprint) + ' ' + print_block_tstamp(block_name) + ' '
        return result + ')'


###############################################################################################################################################################################################


def print_net_header(net_count: int, net_name: str) -> str:
    return '(net (code {}) (name "{}")'.format(net_count, net_name)

def print_net_pin(block_name: str, pin_name: str) -> str:
    return "(node (ref {}) (pin {})))".format(block_name, pin_name)

def connections_exp(dict: dict[]) -> str:
        """Given a dictionary of net names (strings) as keys and a list of connected Pins (namedtuples) as corresponding values

        Example:
        (nets
            (net (code 1) (name "Net-(R1-Pad2)")
              (node (ref R2) (pin 1))
              (node (ref R1) (pin 2)))
            (net (code 3) (name GND)
              (node (ref C2) (pin 2))
              (node (ref C1) (pin 2))
              (node (ref R4) (pin 2)))
              
        """
                
        result = '(nets '
        net_count = 1
        for (net_name, pin_list) in dict.items():
            result += print_net_header(net_count, net_name) + ' '
            net_count += 1
            for i in range(len(pin_list)):
                pin = pin_list[i]
                result += print_net_pin(pin.block_name, pin.pin_name) + ' '
        return result + ')'
