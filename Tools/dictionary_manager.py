import pygame
from copy import deepcopy

class DictManager:
	def __init__(self, settings):
		# getting all the settings
		self.settings = settings

	def prime_group_del(self):
		if self.settings.delete:
			self.settings.prime_line.pop(self.settings.del_group)
			self.settings.delete = False
			self.settings.prime_group -= 1

	def input_values(self):

		self.settings.copy_inputs_entering.clear()
		self.settings.copy_inputs_entering = sorted(deepcopy(self.settings.inputs_entering))
		self.settings.input_value.clear()
		self.settings.calculated = "".join(self.settings.calculate)

		for index, inputs in enumerate(self.settings.copy_inputs_entering):
			self.settings.input_value[inputs] = False

	def update(self):
		if self.settings.generate_map:
			self.input_values()

			
		self.prime_group_del()
		