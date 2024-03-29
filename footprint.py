from collections import namedtuple
from typing import *

Block = namedtuple('block', ['footprint', 'value'])
Pin = namedtuple('pin', ['block_name', 'pin_name'])

###############################################################################################################################################################################################

"""1. Generating Header"""

def gen_header() -> str:
    return '(export (version D))'

###############################################################################################################################################################################################

"""2. Generating Blocks"""

def gen_block_comp(block_name: str) -> str:
    return '(comp (ref {})'.format(block_name)

def gen_block_value(block_value: str) -> str:
    return '(value {})'.format(block_value)

def gen_block_footprint(block_footprint: str) -> str:
    return '(footprint {})'.format(block_footprint)

def gen_block_tstamp(block_name: str) -> str:
    return '(tstamp {}))'.format(block_name)

def block_exp(dict: Dict[str, Block]) -> str:
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
        result = '(components' 
        for (block_name, block) in dict.items():
            result += '\n' + gen_block_comp(block_name) + '\n' + gen_block_value(block[1]) + '\n' + gen_block_footprint(block[0]) + '\n' + gen_block_tstamp(block_name)
        return result + ')'

###############################################################################################################################################################################################

"""3. Generating Nets"""

def gen_net_header(net_count: int, net_name: str) -> str:
    return '(net (code {}) (name "{}")'.format(net_count, net_name)

def gen_net_pin(block_name: str, pin_name: str) -> str:
    return "(node (ref {}) (pin {}))".format(block_name, pin_name)

def net_exp(dict: Dict[str, List[Pin]]) -> str:
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
        result = '(nets'
        net_count = 1
        for (net_name, pin_list) in dict.items():
            result += '\n' + gen_net_header(net_count, net_name)
            net_count += 1
            for i in range(len(pin_list)):
                pin = pin_list[i]
                result += '\n' + gen_net_pin(pin[0], pin[1])
                if i == len(pin_list) - 1:
                    result += ')'
        return result + '\n' + ')'

###############################################################################################################################################################################################

"""4. Generate Full Netlist"""

def generate_netlist(blocks_dict, nets_dict):
    return gen_header() + '\n' + block_exp(blocks_dict) + '\n' + net_exp(nets_dict) + '\n' + ')'

###############################################################################################################################################################################################

"""5. Test Data"""

blocks_dict = {'U1': Block('Package_DIP:DIP-4_W7.62mm', 'LM555'),
            'R3': Block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '1k'),
            'R1': Block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '4k7'),
            'R2': Block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '10k'),
            'C1': Block('Capacitor_SMD:CP_Elec_3x5.3', '100\u03BCF'),
            'C2': Block('Capacitor_SMD:C_0201_0603Metric', '10n'),
            'D1': Block('LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder', 'LED')
              }

block_test1 = blocks_dict
block_test2: Dict[str, Block] = {}
block_test3 = {'A': Block('Capacitor', '10k'), 'B': Pin('LED', 'LED')}
block_test4 = {1: Block('Capacitor', '10k'), 2: Block('LED', 'LED')}
# Extra test case: block_test5 = {'A': Block('Capacitor', '10k'), 'B': Block('LED', 'LED')}


nets_dict = {'Net-(R3-Pad1)': [Pin('U1', '3'), Pin('R3', '1')],
            'Net-(C1-Pad1)': [Pin('U1', '2'), Pin('U1', '5'), Pin('U1', '6'), Pin('R2', '2'), Pin('C1', '1'), Pin('C2', '1')],
            'Net-(R1-Pad2)': [Pin('R2', '1'), Pin('R1', '2'), Pin('U1', '7')],
            '+9V': [Pin('R1', '1'), Pin('U1', '4'), Pin('U1', '8')],
            'GND': [Pin('D1', '1'), Pin('C2', '2'), Pin('C1', '2'), Pin('U1', '1')],
            'Net-(D1-Pad2)': [Pin('D1', '2'), Pin('R3', '2')]
            }

net_test1 = nets_dict
net_test2: Dict[str, List[Pin]] = {}
net_test3 = {'Net1': [Pin('U1', '3'), Pin('U2', '1')], 'Net2': [Block('R2', '4'), Pin('R3', '1')]}
net_test4 = {1: [Pin('U1', '3'), Pin('U2', '1')], 2: [Block('R2', '4'), Pin('R3', '1')]}
# Extra test case: net_test5 = {'Net3': [], 'Net4': [Pin('R2', '4'), Pin('R3', '1')]}
