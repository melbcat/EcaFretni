#	
#	encryption_info.py ... LC_ENCRYPTION_INFO load command.
#	Copyright (C) 2010  KennyTM~ <kennytm@gmail.com>
#	
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#	

from macho.loadcommands.loadcommand import LoadCommand

class EncryptionInfoCommand(LoadCommand):
	"""The encryption info load command."""

	def analyze(self):
		(self.cryptoff, self.cryptsize, self.cryptid) = self._o.readFormatStruct('3L')
			
	def __str__(self):
		return "<EncryptionInfo {}/{:x}>".format(self.cryptid, self.cryptoff)


LoadCommand.registerFactory('ENCRYPTION_INFO', EncryptionInfoCommand)
		
