import unittest
from footprint import *
from collections import namedtuple

"""Note: Named tuples assign meaning to each position in a tuple and allow for more readable,
self-documenting code. They can be used wherever regular tuples are used, and they add
the ability to access fields by name instead of position index.
collections.namedtuple(typename, field_names[, verbose=False][, rename=False])
"""
class TestFootprint(unittest.TestCase):
	def test_block(self):
		block = namedtuple('block', ['footprint', 'value'])

		block_dict1 = {'U1': block('Package_DIP:DIP-4_W7.62mm', 'LM555'),
          'R3': block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '1k'),
          'R1': block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '4k7'),
          'R2': block('OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical', '10k'),
          'C1': block('Capacitor_SMD:CP_Elec_3x5.3', '100\u03BCF'),
          'C2': block('Capacitor_SMD:C_0201_0603Metric', '10n'),
          'D1': block('LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder', 'LED')
          }

        block_dict2 = {'A': block('Capacitor', '10k'), 'B': block('LED', 'LED')}
        self.assertEqual(block_exp(dict1), '(components (comp (ref A) (value 10k) (footprint Capacitor) (tstamp A)) (comp (ref B) (value LED) (footprint LED) (tstamp B)))')

        block_dict3 = {'C': block_dict1['R1'], 'B': block_dict1['D1']}
        self.assertEqual(block_exp(block_dict3), )

        
                dict3 = {}
                with self.assertRaises(AssertionError):
                    block_exp(dict3)

                dict4 = {'A': block('Capacitor', '10k'), 'B': pin('LED', 'LED')}
                with self.assertRaises(TypeError):
                    block_exp(dict4)

                dict5 = {1: block('Capacitor', '10k'), 2: block('LED', 'LED')}
                with self.assertRaises(TypeError):
                    block_exp(dict5)

                
        def test_connections_exp(self):
        	pin = namedtuple('pin', ['block_name', 'pin_name'])

nets = {'Net-(R3-Pad1)': [pin('U1', '3'), pin('R3', '1')],
        'Net-(C1-Pad1)': [pin('U1', '2'), pin('U1', '5'), pin('U1', '6'), pin('R2', '2'), pin('C1', '1'), pin('C2', '1')],
        'Net-(R1-Pad2)': [pin('R2', '1'), pin('R1', '2'), pin('U1', '7')],
        '+9V': [pin('R1', '1'), pin('U1', '4'), pin('U1', '8')],
        'GND': [pin('D1', '1'), pin('C2', '2'), pin('C1', '2'), pin('U1', '1')],
        'Net-(D1-Pad2)': [pin('D1', '2'), pin('R3', '2')]
        }

                dict1 = {'Net1': [pin('U1', '3'), pin('U2', '1')], 'Net2': [pin('R2', '4'), pin('R3', '1')], 'Net3': [pin('C1', '1'), pin('C3', '2')]}
                self.assertEqual(connections_exp(dict1),
                        '(nets (net (code 1) (name "Net1") (node (ref U1) (pin 3))) (node (ref U2) (pin 1))) (net (code 2) (name "Net2") (node (ref R2) (pin 4))) (node (ref R3) (pin 1))) (net (code 3) (name "Net3") (node (ref C1) (pin 1))) (node (ref C3) (pin 2))) )')
                
                dict2 = {'Net3': [], 'Net4': [pin('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(AssertionError):
                    connections_exp(dict2)
                
                dict3 = {}
                with self.assertRaises(AssertionError):
                    connections_exp(dict3)

                dict4 = {'Net1': [pin('U1', '3'), pin('U2', '1')], 'Net2': [block('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(TypeError):
                    connections_exp(dict4)

                dict5 = {1: [pin('U1', '3'), pin('U2', '1')], 2: [block('R2', '4'), pin('R3', '1')]}
                with self.assertRaises(TypeError):
                    connections_exp(dict5)


if __name__ == '__main__':
    unittest.main()
class TestFootprint(unittest.TestCase):
  def test_block(self):
    

"""Arguments:
blocks: Dict[str, Block] (block_name to Block definition)
nets: Dict[str, List[Pin]] (net name to list of connected pins)
"""
