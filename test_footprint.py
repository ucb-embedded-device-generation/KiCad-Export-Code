import unittest
from footprint import *
from collections import namedtuple

class TestFootprint(unittest.TestCase):
	def test_block_exp(self):
		"""Five test cases found in footprint.py."""
		self.assertEqual(block_exp(block_test1), 
			'(components\n(comp (ref U1)\n(value LM555)\n(footprint Package_DIP:DIP-4_W7.62mm)\n(tstamp U1))\n(comp (ref R3)\n(value 1k)\n(footprint OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical)\n(tstamp R3))\n(comp (ref R1)\n(value 4k7)\n(footprint OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical)\n(tstamp R1))\n(comp (ref R2)\n(value 10k)\n(footprint OptoDevice:R_LDR_4.9x4.2mm_P2.54mm_Vertical)\n(tstamp R2))\n(comp (ref C1)\n(value 100μF)\n(footprint Capacitor_SMD:CP_Elec_3x5.3)\n(tstamp C1))\n(comp (ref C2)\n(value 10n)\n(footprint Capacitor_SMD:C_0201_0603Metric)\n(tstamp C2))\n(comp (ref D1)\n(value LED)\n(footprint LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder)\n(tstamp D1)))')
		
		# with self.assertRaises(TypeError):
		# 	block_exp(block_test2)

		with self.assertRaises(TypeError):
			block_exp(block_test3)

		with self.assertRaises(TypeError):
			block_exp(block_test4)

	def test_net_exp(self):
		self.assertEqual(net_exp(net_test1),
			'(nets\n(net (code 1) (name "Net-(R3-Pad1)")\n(node (ref U1) (pin 3))\n(node (ref R3) (pin 1)))\n(net (code 2) (name "Net-(C1-Pad1)")\n(node (ref U1) (pin 2))\n(node (ref U1) (pin 5))\n(node (ref U1) (pin 6))\n(node (ref R2) (pin 2))\n(node (ref C1) (pin 1))\n(node (ref C2) (pin 1)))\n(net (code 3) (name "Net-(R1-Pad2)")\n(node (ref R2) (pin 1))\n(node (ref R1) (pin 2))\n(node (ref U1) (pin 7)))\n(net (code 4) (name "+9V")\n(node (ref R1) (pin 1))\n(node (ref U1) (pin 4))\n(node (ref U1) (pin 8)))\n(net (code 5) (name "GND")\n(node (ref D1) (pin 1))\n(node (ref C2) (pin 2))\n(node (ref C1) (pin 2))\n(node (ref U1) (pin 1)))\n(net (code 6) (name "Net-(D1-Pad2)")\n(node (ref D1) (pin 2))\n(node (ref R3) (pin 2)))\n)')
				
		# with self.assertRaises(TypeError):
		# 	net_exp(net_test2)

		with self.assertRaises(TypeError):
			net_exp(net_test3)

		with self.assertRaises(TypeError):
			net_exp(net_test4)


if __name__ == '__main__':
	unittest.main()
	

"""
Notes on arguments:
blocks: Dict[str, Block] (block_name to Block definition)
nets: Dict[str, List[Pin]] (net name to list of connected pins)

Notes on namedtuple: 
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. 
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead
of position index.
collections.namedtuple(typename, field_names[, verbose=False][, rename=False])
"""
