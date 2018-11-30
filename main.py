import cPickle as pickle
import random
import sys
import os
import re
import platform
import kivy
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial

def main():
	start_over = True
	while start_over == True:
		Level_data = read_map()
		Ricks_Game = Game_UI(Level_data)
		Ricks_Game.clear_screen()
		keep_playing = 'True'
		while keep_playing == 'True':
			keep_playing = Ricks_Game.display_room()
			if keep_playing == 'Dead':
				sot = raw_input('You have died do you want to continue? [Y|N] : ')
				if sot.upper() == 'Y':
					start_over = True

				else:
					start_over = False



class RMCYTARoot(BoxLayout):
	pass

class RMCYTAApp(App):
ss	repeat_cmd = ''    def IIP(self,mynumber):
        if int(mynumber) == 2:
            return True
        if int(mynumber) % 2 == 0:
            return False
        else:
            if int(mynumber) > 3 and int(mynumber) < -3:
                for x in range(3,int(mynumber)):
                    if int(mynumber) % 2 != 0:
                        if x == (int(mynumber) - 1):
                            return True
                        else:
                            continue
                    else:
                        continue
            else:
                return True

	ROOM_INFO = Label()
	CMD_INFO = Label()
	CMD_IN = ObjectProperty(None)
	CMD_results = Popup()
	HUD_Scroll1 = ScrollView(size_hint=(None, None))
	HUD_Scroll2 = ScrollView(size_hint=(None, None))
	HUD_GUI = ScrollView(size_hint=(None, None))
	s = Slider()
	s2 = Slider()

	def build(self):
		self.icon = 'rm.png'
		self.HUD_Scroll1 = ScrollView(size_hint=(700, 200), size=(700, 200),text_size=(700, None), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x = True)
		self.HUD_Scroll2 = ScrollView(size_hint=(None, None), size=(300, 200),text_size=(500, None), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x = True)
		self.HUD_GUI = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, 20),pos_hint={'center_x': .5, 'center_y': .5})
		self.HUD_GUI2 = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, 20),pos_hint={'center_x': .5, 'center_y': .5})
		self.HUD_GUI3 = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, 20),pos_hint={'center_x': .5, 'center_y': .5})
		self.g_init()
		layout = BoxLayout(padding=7, orientation='vertical')
		layout2 = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, 15),pos_hint={'center_x': .5, 'center_y': .5})
		HUD = BoxLayout(spacing=10)
		room_info = self.display_room()
		cmd_result = ''
		self.ROOM_INFO = Label(text=room_info,halign='center',valign='top',font_size='12sp',text_size=(700, None), markup = True)
		self.CMD_INFO = Label(text=cmd_result,halign='left',font_size='12sp',text_size=(700, 300), markup = True)
		self.CMD_IN = TextInput(text='', multiline=False)
		self.CMD_IN.bind(on_text_validate=self.Execute_CMD)
		self.HUD_Scroll1.add_widget(self.ROOM_INFO)
		btn1 = Button(text="Go!",size_hint = (.2,.6))
		btnN = Button(text="Go N!",size_hint = (.2,.6))
		btnN.bind(on_press=self.Execute_N)
		btnS = Button(text="Go S!",size_hint = (.2,.6))
		btnS.bind(on_press=self.Execute_S)
		btnE = Button(text="Go E!",size_hint = (.2,.6))
		btnE.bind(on_press=self.Execute_E)
		btnW = Button(text="Go W!",size_hint = (.2,.6))
		btnW.bind(on_press=self.Execute_W)
		btnU = Button(text="Go U!",size_hint = (.2,.6))
		btnU.bind(on_press=self.Execute_U)
		btnD = Button(text="Go D!",size_hint = (.2,.6))
		btnD.bind(on_press=self.Execute_D)
		btnA = Button(text="Attack!",size_hint = (.2,.6))
		btnA.bind(on_press=self.Execute_A)
		btnGA = Button(text="Get All!",size_hint = (.2,.6))
		btnGA.bind(on_press=self.Execute_GA)
		btnI = Button(text="Inventory",size_hint = (.2,.6))
		btnI.bind(on_press=self.Execute_Inv)

		self.HUD_GUI.add_widget(btnU)
		self.HUD_GUI.add_widget(btnN)
		self.HUD_GUI.add_widget(btnGA)

		self.HUD_GUI2.add_widget(btnW)
		self.HUD_GUI2.add_widget(btnA)
		self.HUD_GUI2.add_widget(btnE)

		self.HUD_GUI3.add_widget(btnD)
		self.HUD_GUI3.add_widget(btnS)
		self.HUD_GUI3.add_widget(btnI)

		btn1.bind(on_press=self.Execute_CMD)
		layout2.add_widget(btn1)
		layout2.add_widget(self.CMD_IN)
		layout.add_widget(layout2)
		layout.add_widget(self.HUD_Scroll1)
		layout.add_widget(self.HUD_GUI)
		layout.add_widget(self.HUD_GUI2)
		layout.add_widget(self.HUD_GUI3)
		return layout

	def restart(self,btn):
		self.g_init()
		self.ROOM_INFO.text = self.display_room()
		self.CMD_results.dismiss()

	def quit(self,btn):
		self.CMD_results.dismiss()
		sys.exit(0)

	def Repeat_CMD(self,btn):
		self.CMD_IN.text = self.repeat_cmd
		self.CMD_results.dismiss()
		self.Execute_CMD(btn)

	def Execute_N(self,btn):
		self.CMD_IN.text = 'N'
		self.Execute_CMD(btn)

	def Execute_S(self,btn):
		self.CMD_IN.text = 'S'
		self.Execute_CMD(btn)

	def Execute_E(self,btn):
		self.CMD_IN.text = 'E'
		self.Execute_CMD(btn)

	def Execute_W(self,btn):
		self.CMD_IN.text = 'W'
		self.Execute_CMD(btn)

	def Execute_U(self,btn):
		self.CMD_IN.text = 'U'
		self.Execute_CMD(btn)

	def Execute_D(self,btn):
		self.CMD_IN.text = 'D'
		self.Execute_CMD(btn)

	def Execute_GA(self,btn):
		self.CMD_IN.text = 'get all'
		self.Execute_CMD(btn)

	def Execute_Inv(self,btn):
		self.CMD_IN.text = 'inventory'
		self.Execute_CMD(btn)


	def Execute_A(self,btn):
		if len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters']) > 0:
			monster = random.choice(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].keys())
			self.CMD_IN.text = 'hit {0}'.format(monster)
		else:
			self.CMD_IN.text = 'hit none'
		self.Execute_CMD(btn)

	def Execute_CMD(self,btn):
		results_layout =  BoxLayout(padding=7, orientation='vertical')
		results_layout2 = BoxLayout(padding=7, orientation='horizontal',size_hint=(1, 15),pos_hint={'center_x': .5, 'center_y': .5})
		self.repeat_cmd = self.CMD_IN.text
		dead,results = self.CMD_Prompt(str(self.CMD_IN.text))
		if dead == False:
			Res_Scroll1 = ScrollView(size_hint=(700, 300), size=(700, 300),text_size=(700, 300), do_scroll_x = True,pos_hint={'center_x': .5, 'center_y': .5})
			rtitle = Label(text=results,font_size='12sp',valign='top',text_size=(700, None), markup = True)
			Res_Scroll1.add_widget(rtitle)
			restart = Button(text='Restart',size_hint = (.5,1))
			quit = Button(text='Quit',size_hint = (.5,1))
			restart.bind(on_press=self.restart)
			quit.bind(on_press=self.quit)
			results_layout2.add_widget(restart)
			results_layout2.add_widget(quit)
			results_layout.add_widget(Res_Scroll1)
			results_layout.add_widget(results_layout2)
			self.CMD_results = Popup(title='Your move results.', content=results_layout,auto_dismiss=False, markup=True)
		else:
			Res_Scroll1 = ScrollView(size_hint=(700, 300), size=(700, 300),text_size=(700, 300), do_scroll_x = True,pos_hint={'center_x': .5, 'center_y': .5})
			rtitle = Label(text=results,font_size='12sp',valign='top',text_size=(700, None), markup = True)
			Res_Scroll1.add_widget(rtitle)
			content = Button(text='Done!',size_hint = (1,1))
			repeat = Button(text='Repeat last!',size_hint = (1,1))
			results_layout.add_widget(Res_Scroll1)
			results_layout2.add_widget(repeat)
			results_layout2.add_widget(content)
			results_layout.add_widget(results_layout2)
			self.CMD_results = Popup(title='Your move results.', content=results_layout,auto_dismiss=False, markup=True)
			content.bind(on_press=self.CMD_results.dismiss)
			repeat.bind(on_press=self.Repeat_CMD)

		self.CMD_results.open()
		self.CMD_IN.text = ''
		self.ROOM_INFO.text = self.display_room()


	def read_map(self):
		output_return = ''

		if os.path.isfile('lvldata.pickle'):
			# output_return = output_return + '\n' + '[RMCYTA] Reading level cache'
			pickle_in = open('lvldata.pickle',"rb")
			Level_data = pickle.load(pickle_in)
			return Level_data
		else:
			sys.exit(0)

	def g_init(self):
		self.Level_data = self.read_map()
		self.char_pos = ['0','0','0','0']
		self.char_stats = [2000,20,20,0,5,50]
		self.char_inv = {'dgps' :{'count': 1 , 'item_name' : 'dgps', 'item_class' : 'DGPS', 'item_value' : 0 , 'item_description' : 'Your Demensional GPS.'}, 'hands': {'count': '1', 'item_class' : 'MW', 'item_name' : 'Hands', 'item_value' : 0 , 'item_description' : 'Your own two hands.'},'T-Shirt': {'item_class' : 'A', 'item_name' : 'T-Shirt', 'item_value' : 0 , 'item_description' : 'The shirt on your Back.', 'count': '1'}}
		self.char_armor = {}
		self.char_weapon = {}
		self.char_weapon['Equiped'] = {'item_name' : 'hands', 'item_value' : 0 , 'item_class' : 'MW', 'item_description' : 'Your own two hands.'}
		self.char_armor['Equiped'] = {'item_name' : 'T-Shirt', 'item_value' : 0  , 'item_description' : 'The shirt on your Back.'}
		self.char_comps = {}

	def clear_screen(self):
		# Clear command as function of OS
		command = "cls" if platform.system().lower()=="windows" else "clear"

		# Action
		os.system(command)

	def Paint_Brush(self,Selected_Color):
		Selected_Color = Selected_Color.lower()
		if Selected_Color == 'reset':
			reset='[/color]'
			return reset
		if Selected_Color == 'bold':
			bold='[b]'
			return bold
		if Selected_Color == 'italics':
			italics='[i]'
			return italics
		if Selected_Color == 'underline':
			underline='[u]'
			return underline
		if Selected_Color == 'strikethrough':
			strikethrough='[s]'
			return strikethrough
		if Selected_Color == 'bold_off':
			bold_off='[/b]'
			return bold_off
		if Selected_Color == 'italics_off':
			italics_off='[/i]'
			return italics_off
		if Selected_Color == 'underline_off':
			underline_off='[/u]'
			return underline_off
		if Selected_Color == 'strikethrough_off':
			strikethrough_off='[/s]'
			return strikethrough_off
		if Selected_Color == 'fg_black':
			fg_black='[color=#2F4F4F]'
			return fg_black
		if Selected_Color == 'fg_red':
			fg_red='[color=#DC143C]'
			return fg_red
		if Selected_Color == 'fg_green':
			fg_green='[color=#7FFF00]'
			return fg_green
		if Selected_Color == 'fg_yellow':
			fg_yellow='[color=#FFD700]'
			return fg_yellow
		if Selected_Color == 'fg_blue':
			fg_blue='[color=#1E90FF]'
			return fg_blue
		if Selected_Color == 'fg_magenta':
			fg_magenta='[color=#FF00FF]'
			return fg_magenta
		if Selected_Color == 'fg_cyan':
			fg_cyan='[color=#20B2AA]'
			return fg_cyan
		if Selected_Color == 'fg_white':
			fg_white='[color=#00FF7F]'
			return fg_white
		if Selected_Color == 'bg_black':
			bg_black=''
			return bg_black
		if Selected_Color == 'bg_red':
			bg_red=''
			return bg_red
		if Selected_Color == 'bg_green':
			bg_green=''
			return bg_green
		if Selected_Color == 'bg_yellow':
			bg_yellow=''
			return bg_yellow
		if Selected_Color == 'bg_blue':
			bg_blue=''
			return bg_blue
		if Selected_Color == 'bg_magenta':
			bg_magenta=''
			return bg_magenta
		if Selected_Color == 'bg_cyan':
			bg_cyan=''
			return bg_cyan
		if Selected_Color == 'bg_white':
			bg_white=''
			return bg_white
		if Selected_Color == 'bg_default':
			bg_default=''
			return bg_default
		else:
			bg_default=''
			return bg_default

		return

	def Paint_SVAR(self,SVAR,FGC,BGC):
		SVAR_MOD='{0}{1}{2}{3}'.format(self.Paint_Brush(FGC),self.Paint_Brush(BGC),SVAR,self.Paint_Brush('reset'))
		return SVAR_MOD



	def display_room(self):
		output_return = ''
		output_return = output_return + '\n' + self.short_cd()
		output_return = output_return + '\n' + self.Paint_SVAR('{0}'.format(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_title'],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_Description']),'fg_yellow','bg_white')
		output_return = output_return + '\n' + self.Paint_SVAR('{0}'.format(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_Description']),'fg_cyan','bg_black')

		if 'monsters' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			monster_I_states = { 'Lurking' : 'in the corner.', 'Hiding' : 'in the shadows', 'Panting' : 'just out of sight', 'hanging' : 'from the rafters' }
			monster_O_states = { 'Lurking' : 'behind some rocks.', 'Hiding' : 'in the shadows', 'Panting' : 'just out of sight', 'tracking' : 'your every move' }
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_ioo'] == 'I':
				monster_states = monster_I_states
			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_ioo'] == 'O':
				monster_states = monster_O_states
			else:
				monster_states = monster_I_states
			for Monster, Data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].items():
				state = random.choice(monster_states.keys())
				surface = monster_states[state]
				output_return = output_return + '\n' + self.Paint_SVAR('There is a {0} {1} {2}.'.format(Monster,state,surface),'fg_red','bg_black')
		if 'items' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			item_I_states = {'sitting' : 'on the floor', 'laying' : 'on the shelf', 'propped' : 'in the corner', 'shoved' : 'in the corner', 'laying' : 'on the floor', 'sitting' : 'on the shelf'}
			item_O_states = {'sitting' : 'on the ground', 'laying' : 'in the shadows', 'propped' : 'in against some rocks', 'covered' : 'by some dirt', 'laying' : 'on the ground'}
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_ioo'] == 'I':
				item_states = item_I_states
			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_ioo'] == 'O':
				item_states = item_O_states
			else:
				item_states = item_I_states
			for item, Data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'].items():
				state = random.choice(item_states.keys())
				surface = item_states[state]

				output_return = output_return + '\n' + self.Paint_SVAR('There is a {0} {1} {2}.'.format(item,state,surface),'fg_yellow','bg_black')
		if 'objects' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			for r_object, Data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['objects'].items():
				output_return = output_return + '\n' + self.Paint_SVAR('There is a {0} against the wall.'.format(r_object),'fg_green','bg_black')

		if 'companions' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			companion_states = { 'Standing proudly' : 'in the corner.', 'Ready to attack' : 'from the shadows.', 'Moving stealthly' : 'into accack position.', 'Eagerly waiting' : 'prepared for battle.' }
			for  companion, Data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions'].items():
				state = random.choice(companion_states.keys())
				surface = companion_states[state]
				output_return = output_return + '\n' + self.Paint_SVAR('{0} is {1} {2}'.format(companion,state,surface),'fg_magenta','bg_black')

		if len(self.char_comps.keys()) > 0:
			companion_states = { 'Standing proudly' : 'in the corner.', 'Ready to attack' : 'from the shadows.', 'Moving stealthly' : 'into accack position.', 'Eagerly waiting' : 'prepared for battle.' }
			for  companion, Data in self.char_comps.items():
				state = random.choice(companion_states.keys())
				surface = companion_states[state]
				output_return = output_return + '\n' + self.Paint_SVAR('Your companion {0} is {1} {2}'.format(companion,state,surface),'fg_magenta','bg_black')
		output_return = output_return + self.show_moves()
		# keep_playing = self.CMD_Prompt()

		return output_return

	def read_save(self,sfile):
		output_return = ''
		sfile = '{0}.pickle'.format(sfile)
		if os.path.isfile(sfile):
			output_return = output_return + '\n' + self.Paint_SVAR('[RMCYTA] Reading Save Game.','fg_green','bg_black')
			pickle_in = open(sfile,"rb")
			Char_Save = pickle.load(pickle_in)
			self.Level_data = Char_Save['Level_data']
			self.char_pos = Char_Save['char_data']['char_pos']
			self.char_weapon = Char_Save['char_data']['char_weapon']
			self.char_armor = Char_Save['char_data']['char_armor']
			self.char_stats = Char_Save['char_data']['char_stats']
			self.char_inv = Char_Save['char_data']['char_inv']
			self.char_comps = Char_Save['char_data']['char_comps']
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('[RMCYTA] Reading level cache failed. {0} does not exist.'.format(sfile),'fg_red','bg_black')
		return output_return

	def write_save(self,sfile):
		output_return = ''
		sfile = str('{0}.pickle'.format(sfile))
		output_return = output_return + '\n' + self.Paint_SVAR('[CDDB Cache] Writing Save','fg_green','bg_black')
		#output_return = output_return + '\n' + Artist_Track_list
		Char_Save = {'Level_data': self.Level_data, 'char_data' : {'char_comps': self.char_comps, 'char_pos' : self.char_pos, 'char_stats' : self.char_stats, 'char_inv' : self.char_inv, 'char_armor' : self.char_armor, 'char_weapon' : self.char_weapon } }
		with open(sfile, 'w+') as pickle_out:
			pickle.dump(Char_Save, pickle_out)
			pickle_out.close()

		return output_return

	def display_inv(self):
		#self.clear_screen()
		output_return = ''
		for item, value in self.char_inv.items():
			output_return = output_return + '\n' + self.Paint_SVAR('------------------------------------------------------------','fg_cyan','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('|Name: {0} |C: {1} |St: {2} |Q: {3}'.format(item, self.char_inv[item]['item_class'],self.char_inv[item]['item_value'],self.char_inv[item]['count']),'fg_yellow','bg_black')
		else:
			pass
		output_return = output_return + '\n' + self.Paint_SVAR('------------------------------------------------------------','fg_cyan','bg_black')
		return output_return

	def short_cd(self):
		output_return = ''
		output_return = output_return + '\n' + self.Paint_SVAR('---------------------------------------------------------------------------','fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('H:{0}|PF:{1}|AT:{2}|DF:{3}|SHM:{4}|AMMO:{5}'.format(self.char_stats[0],self.char_stats[3],self.char_stats[1],self.char_stats[2],self.char_stats[4],self.char_stats[5]),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('---------------------------------------------------------------------------','fg_cyan','bg_black')
		return output_return

	def display_char(self):
		output_return = ''

		#self.clear_screen()
		output_return = output_return + '\n' + self.Paint_SVAR('Health : {0}'.format(self.char_stats[0]),'fg_red','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Strength : {0}'.format(self.char_stats[1]),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Weapon : {0}'.format(self.char_weapon['Equiped']['item_name']),'fg_red','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Defense : {0}'.format(self.char_stats[2]),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Armor : {0}'.format(self.char_armor['Equiped']['item_name']),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Portal Fluid : {0}'.format(self.char_stats[3]),'fg_green','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Shmeckles : {0}'.format(self.char_stats[4]),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Ammunition : {0}'.format(self.char_stats[5]),'fg_red','bg_black')
		return output_return

	def display_companion(self,companion):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('Name : {0}'.format(self.char_comps[companion.lower()]['name']),'fg_white','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Health : {0}'.format(self.char_comps[companion.lower()]['description']),'fg_white','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Health : {0}'.format(self.char_comps[companion.lower()]['stats'][0]),'fg_red','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Strength : {0}'.format(self.char_comps[companion.lower()]['stats'][1]),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Weapon : {0}'.format(self.char_comps[companion.lower()]['weapon']['Equiped']['item_name']),'fg_red','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Defense : {0}'.format(self.char_comps[companion.lower()]['stats'][2]),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Armor : {0}'.format(self.char_comps[companion.lower()]['armor']['Equiped']['item_name']),'fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('Ammunition : {0}'.format(self.char_comps[companion.lower()]['stats'][3]),'fg_red','bg_black')

		return output_return

	def lookat(self,item):

		output_return = ''

		if item.upper() == 'DGPS' and 'dgps' in self.char_inv:
			output_return = output_return + '\n' + self.display_DGPS()
		if 'objects' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			if item in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['objects']:
				output_return = output_return + '\n' +self.display_object(item)
		if 'items' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			if item in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items']:
				output_return = output_return + '\n' +self.display_item(item)
		if 'monsters' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			if item in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters']:
				output_return = output_return + '\n' + self.display_monster(item)
		if item.lower() in self.char_inv:
			output_return = output_return + '\n' + self.display_inv_item(item)

		if item.lower() in self.char_comps:
			output_return = output_return + '\n' + self.display_companion(item)
		# else:
		# 	output_return = output_return + '\n' + 'That item does not exist. Put the toadstools down.'
		return output_return

	def display_DGPS(self):
		output_return = ''

		if 'dgps' in self.char_inv:
			output_return = output_return + '\n' + self.Paint_SVAR('You Look at the readout on your demensional GPS.','fg_yellow','bg_white')
			output_return = output_return + '\n' + self.Paint_SVAR(' ____________________________','fg_yellow','bg_green')
			output_return = output_return + '\n' + self.Paint_SVAR('||--D--||--Z--||--X--||--Y--||','fg_yellow','bg_green')
			output_return = output_return + '\n' + self.Paint_SVAR('||--{0}--||--{1}--||--{2}--||--{3}--||'.format(self.char_pos[0],self.char_pos[1],self.char_pos[2],self.char_pos[3]),'fg_yellow','bg_green')
			output_return = output_return + '\n' + self.Paint_SVAR('||_____||_____||_____||_____||','fg_yellow','bg_green')
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('You Look don\'t have your demensional GPS.','fg_red','bg_black')

		return output_return

	def display_monster(self,monster_name):
		output_return = ''

		#self.clear_screen()
		output_return = output_return + '\n' + self.Paint_SVAR('	Name : {0} \n	Description : {1} \n		Health : {2}\n		Attack : {3}\n		Defense {4}'.format(monster_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][monster_name]['description'],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][monster_name]['stats'][0],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][monster_name]['stats'][1],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][monster_name]['stats'][2]),'fg_red','bg_black')
		return output_return

	def display_object(self,object_name):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('{0}'.format(object_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['objects'][object_name]),'fg_green','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('{1}'.format(object_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['objects'][object_name]),'fg_green','bg_black')

		return output_return

	def display_item(self,item_name):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('-------------------------------------------','fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Name: {0}'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Description: {1}'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_description']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Class: {1}'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_class']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Value: {1}'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_value']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('-------------------------------------------','fg_cyan','bg_black')

		return output_return

	def display_inv_item(self,item_name):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('-------------------------------------------','fg_cyan','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Name: {0}'.format(item_name,self.char_inv[item_name]),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Description: {1}'.format(item_name,self.char_inv[item_name]['item_description']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Class: {1}'.format(item_name,self.char_inv[item_name]['item_class']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('|Value: {1}'.format(item_name,self.char_inv[item_name]['item_value']),'fg_yellow','bg_black')
		output_return = output_return + '\n' + self.Paint_SVAR('-------------------------------------------','fg_cyan','bg_black')

		return output_return

	def display_other_room(self,direction):
		output_return = ''

		self.char_pos = self.char_pos
		if direction[0].upper() in ['N','S','E','W','U','D']:
			if self.check_move(direction) == True:
				if direction.upper() == 'N' or direction.upper() == 'NORTH':
					self.char_pos[2] = str(int(self.char_pos[2]) + 1)
				elif direction.upper() == 'S' or direction.upper() == 'SOUTH':
					self.char_pos[2] = str(int(self.char_pos[2]) - 1)
				elif direction.upper() == 'E' or direction.upper() == 'EAST':
					self.char_pos[3] = str(int(self.char_pos[3]) + 1)
				elif direction.upper() == 'W' or direction.upper() == 'WEST':
					self.char_pos[3] = str(int(self.char_pos[3]) - 1)
				elif direction.upper() == 'U' or direction.upper() == 'UP':
					self.char_pos[1] = str(int(self.char_pos[1]) + 1)
				elif direction.upper() == 'D' or direction.upper() == 'DOWN':
					self.char_pos[1] = str(int(self.char_pos[1]) - 1)
				output_return = output_return + '\n' + self.Paint_SVAR('{0}'.format(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_title']),'fg_yellow','bg_white')
				output_return = output_return + '\n' + self.Paint_SVAR('{0}'.format(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_Description']),'fg_cyan','bg_black')

			else:
				output_return = output_return + '\n' + self.Paint_SVAR('The view in that direction is obstructed.','fg_cyan','bg_white')

		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} isn\'t a direction.','fg_cyan','bg_white').format(direction)


		return output_return

	def call_phone(self,number):
		output_return = ''

		if number == '77198364211':
			output_return = output_return + '\n' + self.Paint_SVAR('You call your Space Uber and wait for it to arrive','fg_yellow','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('Your space-uber arrives and takes you back to your house.','fg_yellow','bg_black')
			self.char_pos = ['0','0','-1','1']

		else:
			messages = { '0': 'You dial the number and hear someone answer in an alien language, they sound angry.', '1': 'You dial the number but recieve an error tone and message telling you to check the number.','2': 'You dial the number and get Rick\'s Pizzaria, home of the Super Rick Double Topping Deal.', '3': 'You try to dial the number but drop the phone, you quickly pick it up.'}
			rndom = random.choice(messages.keys())
			MSG = messages[rndom]
			output_return = output_return + '\n' + self.Paint_SVAR(MSG,'fg_yellow','bg_black')

		return output_return

	def store(self,selection):
		output_return = ''
		if selection.lower() == 'list':
			store_items = self.Level_data[self.char_pos[0]]['store']['items']
			y = 0
			for item, data in store_items.items():
				output_return = output_return + '\n' + self.Paint_SVAR('------------------------------------','fg_blue','bg_black')
				output_return = output_return + '\n' + self.Paint_SVAR('{1}. {0}  : '.format(item,y),'fg_blue','bg_white')
				output_return = output_return + '\n' + self.Paint_SVAR('--| Desc:	 {0}   '.format(store_items[item]['item_description']),'fg_green','bg_black')
				output_return = output_return + '\n' + self.Paint_SVAR('--| Class:	{0}   '.format(store_items[item]['item_class']),'fg_green','bg_black')
				output_return = output_return + '\n' + self.Paint_SVAR('--| Strength: {0}   '.format(store_items[item]['item_value']),'fg_green','bg_black')
				output_return = output_return + '\n' + self.Paint_SVAR('--| Price:	{0}   '.format(store_items[item]['item_cost']),'fg_yellow','bg_black')
				y += 1
			output_return = output_return + '\n' + self.Paint_SVAR('------------------------------------','fg_blue','bg_black')
			return output_return
		else:
			try:
				selection = int(selection)
			except:
				output_return = output_return + '\n' + self.Paint_SVAR('Select from the list bub.','fg_yellow','bg_black')

			y = 0
			store_items = self.Level_data[self.char_pos[0]]['store']['items']
			for item, data in store_items.items():
				y += 1
			if (y - selection) > 0 and y >= selection:
				pass
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Select from the list bub.','fg_yellow','bg_black')
				selection = False
			x = 0
			for item, data in store_items.items():
				if x == int(selection):
					s_item = item
					break
				x += 1
			if int(self.char_stats[4]) > int(store_items[item]['item_cost']):
				output_return = output_return + '\n' + self.Paint_SVAR('You purchase a {0} for {1} shmeckles'.format(item,store_items[item]['item_cost']),'fg_green','bg_white')
				self.char_stats[4] = int(self.char_stats[4]) - int(store_items[item]['item_cost'])
				if item in self.char_inv:
					self.char_inv[item]['count'] = int(self.char_inv[item]['count']) + 1
				else:
					self.char_inv[item] = store_items[item]
					# self.char_inv[item].pop('item_cost')
					self.char_inv[item]['count'] = 1


			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You don\'t have the shmeckles to buy {0}'.format(item),'fg_cyan','bg_white')

			return output_return

	def check_move(self,direction):
		if direction[0].upper() in ['N','S','E','W','U','D']:
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['M'+direction.upper()] == 'Y':
				return True,True
			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['M'+direction.upper()] == 'L':
				return True,False
			else:
				return False,False
		else:
			output_return = ''
			output_return = output_return + '\n' + self.Paint_SVAR('{0} isnt a direction.'.format(direction),'fg_cyan','bg_black')
			return output_return

	def show_moves(self):
		output_return = ''

		for dir in ['North','South','East','West','Up','Down']:
			door,lock = self.check_move(dir[0])
			if door == False:
				continue
			elif door == True and  lock == False:
				if dir[0] == 'N':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][str(int(self.char_pos[2]) + 1)][self.char_pos[3]]['Room_title']
				elif dir[0] == 'S':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][str(int(self.char_pos[2]) - 1)][self.char_pos[3]]['Room_title']
				elif dir[0] == 'E':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][str(int(self.char_pos[3]) + 1)]['Room_title']
				elif dir[0] == 'W':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][str(int(self.char_pos[3]) - 1)]['Room_title']
				elif dir[0] == 'U':
					Room_title = self.Level_data[self.char_pos[0]][str(int(self.char_pos[1]) + 1)][self.char_pos[2]][self.char_pos[3]]['Room_title']
				elif dir[0] == 'D':
					Room_title = self.Level_data[self.char_pos[0]][str(int(self.char_pos[1]) - 1)][self.char_pos[2]][self.char_pos[3]]['Room_title']
				output_return = output_return + '\n' + self.Paint_SVAR('To the {0} the door to {1} is locked.'.format(dir,Room_title),'fg_cyan','bg_black')

			elif door == True and lock == True:
				if dir[0] == 'N':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][str(int(self.char_pos[2]) + 1)][self.char_pos[3]]['Room_title']
				elif dir[0] == 'S':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][str(int(self.char_pos[2]) - 1)][self.char_pos[3]]['Room_title']
				elif dir[0] == 'E':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][str(int(self.char_pos[3]) + 1)]['Room_title']
				elif dir[0] == 'W':
					Room_title = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][str(int(self.char_pos[3]) - 1)]['Room_title']
				elif dir[0] == 'U':
					Room_title = self.Level_data[self.char_pos[0]][str(int(self.char_pos[1]) + 1)][self.char_pos[2]][self.char_pos[3]]['Room_title']
				elif dir[0] == 'D':
					Room_title = self.Level_data[self.char_pos[0]][str(int(self.char_pos[1]) - 1)][self.char_pos[2]][self.char_pos[3]]['Room_title']
				output_return = output_return + '\n' + self.Paint_SVAR('To the {0} is {1}.'.format(dir,Room_title),'fg_cyan','bg_black')
			else:
				continue

		return output_return
	def execute_trap(self,trap_trigger):
		output_return = ''

		if trap_trigger in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps']:
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['trap_class'].upper() == 'P':
				output_return = output_return + '\n' + self.portal_trap(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['Trap_Portal_Dest'],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['Trap_Portal_MSG'])
			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['trap_class'].upper() == 'I':
				if 'count' not in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]:
					self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['count'] = '3'

				else:
					self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['count'] = str(int(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['count']) - 1)
				if int(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['count']) > 0:

					for item, data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger].items():
						# output_return = output_return + '\n' + item
						if 'item_name' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger][item]:
							# output_return = output_return + '\n' + item
							break

					output_return = output_return + '\n' + self.item_trap(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger][item],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['Trap_Portal_MSG'])
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('That doesnt seem to work.','fg_cyan','bg_white')

			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['trap_class'].upper() == 'SD':
				output_return = output_return + '\n' + self.secret_door_trap(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['SD'],self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps'][trap_trigger]['Trap_Portal_MSG'])
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('That doesnt seem to work.','fg_cyan','bg_white')

		return output_return

	def secret_door_trap(self,SD,Trap_MSG):
		output_return = ''

		output_return = output_return + '\n' + Trap_MSG
		self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['M' + SD.upper()] = 'Y'
		self.display_room()
		return output_return

	def item_trap(self,item,Trap_MSG):
		output_return = ''

		output_return = output_return + '\n' + Trap_MSG
		output_return = output_return + '\n' + self.Paint_SVAR('A {0} falls out.'.format(item['item_name']),'fg_yellow','bg_black')
		self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item['item_name']] = item

		return output_return

	def portal_trap(self,Trap_coord,Trap_MSG):
		output_return = ''

		self.char_pos = Trap_coord
		output_return = output_return + '\n' + Trap_MSG

		return output_return

	def spawn_monster(self):
		output_return = ''

		Monster_List = self.Level_data[self.char_pos[0]]['monsters']
		Monster = random.choice(Monster_List.keys())
		num_monsters = random.randint(1,6)
		for num_of_monsters in range(0,num_monsters):
			if random.randint(0,99) > 40:
				output_return = output_return + '\n' + self.Paint_SVAR('A {0} appears from the darkness.'.format(Monster),'fg_red','bg_black')
				if 'monsters' not in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
					self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'] = {}
				self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster] = Monster_List[Monster]
			return output_return

	def spawn_eyeholeman(self):
		output_return = ''

		Monster_List = {'eye-hole man' : {'name': 'eye-hole man', 'description' : 'It\'s the Eye-Hole Man. Those are his Eye-Holes.', 'stats': [random.randint(1000,3000),random.randint(100,1000),random.randint(100,1000)] }}
		Monster = 'eye-hole man'
		if random.randint(0,99) > 60:
			output_return = output_return + '\n' + self.Paint_SVAR('The {0} appears from the darkness.'.format(Monster),'fg_red','bg_black')
			if 'monsters' not in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
				self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'] = {}
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster] = Monster_List[Monster]
		return output_return

	def take_all_items(self,move):
		output_return = ''
		if len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'].keys()) > 0:
			for item, data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'].items():
				output_return = output_return + '\n' + self.take_item(move,item)
		return output_return

	def take_item(self,sMove,item_name):
		inv_pos = len(self.char_inv) -1
		t_item = item_name.lower()
		t_item = re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), t_item)
		output_return = ''

		if item_name.lower() in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items']:
			item_name = item_name.lower()
		elif item_name.upper() in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items']:
			item_name = item_name.upper()
		elif t_item in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items']:
			item_name = t_item
		if item_name.lower() == 'eye holes':
			self.spawn_eyeholeman()
		if item_name in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items']:
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_class'].upper() == 'AMMO':
				output_return = output_return + '\n' + self.Paint_SVAR('You pick up the {0} and gain {1} ammo!'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_value']),'fg_green','fg_white')
				self.char_stats[5] = self.char_stats[5] + int(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_value'])
				del self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]
			elif self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_class'].upper() == 'G':
				output_return = output_return + '\n' + self.Paint_SVAR('You pick up the {0} and gain {1} shmeckles!'.format(item_name,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_value']),'fg_green','fg_white')
				self.char_stats[4] = self.char_stats[4] + int(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]['item_value'])
				del self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You {0} the {1}'.format(sMove,item_name),'fg_green','fg_white')
				if item_name in self.char_inv:
					self.char_inv[item_name]['count'] = int(self.char_inv[item_name]['count']) + 1
				else:
					self.char_inv[item_name] = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]
					self.char_inv[item_name]['item_name'] = item_name
					self.char_inv[item_name]['count'] = 1
				del self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name]
		else:
			output_return = output_return + '\n' + self.Paint_SVAR("You can\'t {0} the {1}. Are you on the perception enchance laser hookah right now?".format(sMove,item_name),'fg_cyan','bg_white')
		return output_return

	def drop_item(self,sMove,item_name):
		output_return = ''
		return output_return
		inv_pos = len(self.char_inv) -1
		t_item = item_name.lower()
		t_item = re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), t_item)
		if item_name.lower() in self.char_inv:
			item_name = item_name.lower()
		elif item_name.upper() in self.char_inv:
			item_name = item_name.upper()
		elif t_item in self.char_inv:
			item_name = t_item
		if item_name in self.char_inv:
			output_return = output_return + '\n' + self.Paint_SVAR('You {0} the {1} on the ground'.format(sMove,item_name),'fg_green','fg_white')
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_name] = self.char_inv[item_name]
			self.char_inv[item_name]['count'] = int(self.char_inv[item_name]['count']) - 1
			if self.char_inv[item_name]['count'] == 0:
				del self.char_inv[item_name]
		else:
			output_return = output_return + '\n' + self.Paint_SVAR("You can\'t {0} the {1}. You don't have it.".format(sMove,item_name),'fg_cyan','bg_white')

		return output_return

	def M_drop_item(self,Monster):
		output_return = ''
		if 'drop_unq' in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster]:
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster]['drop_unq'] == 'Y':
				if random.randint(0,99) > 65:
					if len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster]['unq_item'].items()) > 0:
						item_drop = random.choice(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster]['unq_item'].keys())
						output_return = output_return + '\n' + self.Paint_SVAR('{0} dropped {1} as it collapsed.'.format(Monster,item_drop),'fg_green','bg_blue')
						self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_drop] = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster]['unq_item'][item_drop]
		random_drops = self.Level_data[self.char_pos[0]]['items']
		item_drop = random.choice(random_drops.keys())
		if random.randint(0,99) > 30:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} dropped {1} as it collapsed.'.format(Monster,item_drop),'fg_green','bg_blue')
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'][item_drop] = random_drops[item_drop]
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('A cloud of dust rises above your defeated enemy, the bastard was broke.','fg_green','bg_blue')

		return output_return

	def use_item(self,item_name,move):
		output_return = ''

		t_item = item_name.lower()
		t_item = re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), t_item)
		if item_name.lower() in self.char_inv:
			item_name = item_name.lower()
		elif item_name.upper() in self.char_inv:
			item_name = item_name.upper()
		elif t_item in self.char_inv:
			item_name = t_item
		if item_name in self.char_inv:
			if item_name.upper() == 'DGPS' and 'dgps' in self.char_inv:
				output_return = output_return + '\n' + self.display_DGPS()
			elif self.char_inv[item_name]['item_class'].upper() == 'W':
				output_return = output_return + '\n' + self.equip_weapon(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'MW':
				output_return = output_return + '\n' + self.equip_weapon(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'A':
				output_return = output_return + '\n' + self.equip_armor(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'P':
				output_return = output_return + '\n' + self.drink_potion(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'K':
				output_return = output_return + '\n' + self.Paint_SVAR('You cant use {0} like that.'.format(item_name),'fg_cyan','fg_white')
			elif self.char_inv[item_name]['item_class'].upper() == 'PG':
				output_return = output_return + '\n' + self.use_PG(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'PF':
				output_return = output_return + '\n' + self.use_PF(item_name,move)
			elif self.char_inv[item_name]['item_class'].upper() == 'CR':
				output_return = output_return + '\n' + self.learn_craft(item_name)
			elif self.char_inv[item_name]['item_class'].upper() == 'CI':
				output_return = output_return + '\n' + self.Paint_SVAR('{0} is a crafting item morty, What will you make with it.'.format(item_name),'fg_cyan','bg_white')

		else:
			output_return = output_return + '\n' + self.Paint_SVAR('You dont have {0}, maybe the gozorpazorpians took it.'.format(item_name),'fg_cyan','bg_white')

		return output_return

	def give_item(self,companion,item):
		output_return = ''
		t_item = companion.lower()
		t_item = re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), t_item)
		if companion.lower() in self.char_comps:
			companion = companion.lower()
		elif companion.upper() in self.char_comps:
			companion = companion.upper()
		elif t_item in self.char_comps:
			companion = t_item
		if companion in self.char_comps:
			# item = raw_input('What do you want to give {0}? : '.format(companion)).lower()
			if item.lower() == 'ammo':
				try:
					ammount = 25
				except:
					output_return = output_return + '\n' + self.Paint_SVAR('Thats not an ammount!','fg_cyan','bg_white')
					return
				if int(self.char_stats[5]) > int(ammount):
					self.char_comps[companion.lower()]['stats'][3] = int(self.char_comps[companion.lower()]['stats'][3]) + ammount
					self.char_stats[5] = int(self.char_stats[5]) - ammount
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('You don\'t have that ammount!','fg_cyan','bg_white')

			elif item.lower() in self.char_inv:
				if companion.lower() == 'jerry':
					if item.lower() == 'jerrys tablet':
						pass
					else:
						output_return = output_return + '\n' + self.Paint_SVAR('{0} can\'t use {1}'.format(companion,self.char_inv[item.lower()]['item_name']),'fg_white','bg_green')
						return output_return
				if self.char_inv[item.lower()]['item_class'].upper() == 'W' or self.char_inv[item.lower()]['item_class'].upper() == 'MW':
					if self.char_comps[companion.lower()]['weapon'] == {}:
						output_return = output_return + '\n' + self.Paint_SVAR('{0} Equips {1}'.format(companion,self.char_inv[item.lower()]['item_name']),'fg_white','bg_green')
						self.char_comps[companion.lower()]['weapon']['Equiped'] = self.char_inv[item.lower()]
						self.char_comps[companion.lower()]['weapon']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['stats'][1] = int(self.char_comps[companion.lower()]['stats'][1]) + int(self.char_inv[item.lower()]['item_value'])
					else:
						output_return = output_return + '\n' + self.Paint_SVAR('{0} is wearing {1} already'.format(companion,self.char_comps[companion.lower()]['weapon']['Equiped']['item_name']),'fg_cyan','bg_white')
						# if raw_input('Do you want to change?').upper() == 'Y':
						output_return = output_return + '\n' + self.Paint_SVAR('{0} Equips {1} and hands you {2}.'.format(companion, self.char_inv[item.lower()]['item_name'],self.char_comps[companion.lower()]['weapon']['Equiped']['item_name']),'fg_white','bg_green')
						self.char_inv[self.char_comps[companion.lower()]['weapon']['Equiped']['item_name']] = self.char_comps[companion.lower()]['weapon']['Equiped']

						self.char_comps[companion.lower()]['stats'][1] = int(self.char_comps[companion.lower()]['stats'][1]) - int(self.char_comps[companion.lower()]['armor']['Equiped']['item_value'])
						self.char_comps[companion.lower()]['stats'][1] = int(self.char_comps[companion.lower()]['stats'][1]) + int(self.char_inv[item.lower()]['item_value'])
						self.char_comps[companion.lower()]['weapon']['Equiped'] = self.char_inv[item.lower()]
						self.char_comps[companion.lower()]['weapon']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['weapon']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['stats'][1] = int(self.char_comps[companion.lower()]['stats'][1]) + int(self.char_inv[item.lower()]['item_value'])
						self.char_inv.pop(item.lower())


				elif self.char_inv[item.lower()]['item_class'].upper() == 'A':
					if self.char_comps[companion.lower()]['armor'] == {}:
						output_return = output_return + '\n' + self.Paint_SVAR('{0} Equips {1}'.format(companion,self.char_inv[item.lower()]['item_name']),'fg_white','bg_green')
						self.char_comps[companion.lower()]['armor']['Equiped'] = self.char_inv[item.lower()]
						self.char_comps[companion.lower()]['armor']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['stats'][2] = int(self.char_comps[companion.lower()]['stats'][2]) + int(self.char_inv[item.lower()]['item_value'])
					else:
						output_return = output_return + '\n' + self.Paint_SVAR('{0} is wearing {1} already'.format(companion,self.char_comps[companion.lower()]['armor']['Equiped']['item_name']),'fg_cyan','bg_white')
						output_return = output_return + '\n' + self.Paint_SVAR('{0} Equips {1} and hands you {2}.'.format(companion, self.char_inv[item.lower()]['item_name'],self.char_comps[companion.lower()]['armor']['Equiped']['item_name']),'fg_white','bg_green')
						self.char_inv[self.char_comps[companion.lower()]['armor']['Equiped']['item_name']] = self.char_comps[companion.lower()]['armor']['Equiped']
						self.char_comps[companion.lower()]['stats'][2] = int(self.char_comps[companion.lower()]['stats'][2]) - int(self.char_comps[companion.lower()]['armor']['Equiped']['item_value'])
						self.char_comps[companion.lower()]['stats'][2] = int(self.char_comps[companion.lower()]['stats'][2]) + int(self.char_inv[item.lower()]['item_value'])
						self.char_comps[companion.lower()]['armor']['Equiped'] = self.char_inv[item.lower()]
						self.char_comps[companion.lower()]['armor']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['armor']['Equiped']['item_name'] = item.lower()
						self.char_comps[companion.lower()]['stats'][2] = int(self.char_comps[companion.lower()]['stats'][2]) + int(self.char_inv[item.lower()]['item_value'])
						self.char_inv.pop(item.lower())


						# else:
						# 	output_return = output_return + '\n' + self.Paint_SVAR('You continue wearing {0}'.format(self.char_armor['Equiped']),'fg_yellow','bg_white')

				elif self.char_inv[item.lower()]['item_class'].upper() == 'P':
					output_return = output_return + '\n' + self.Paint_SVAR('{2} drinks {0} and regain {1} Health.'.format(item.lower(),self.char_inv[item.lower()]['item_value'],companion),'fg_white','bg_cyan')
					self.char_comps[companion.lower()]['stats'][0] = int(self.char_comps[companion.lower()]['stats'][0]) + int(self.char_inv[item.lower()]['item_value'])
					self.char_inv[item.lower()]['count'] = int(self.char_inv[item.lower()]['count']) - 1
					if self.char_inv[item.lower()]['count'] == 0:
						del self.char_inv[item.lower()]

			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You dont have any {0}.'.format(item),'fg_cyan','bg_white')
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} is not a member of you party.'.format(companion),'fg_cyan','bg_white')
		return output_return

	def learn_craft(self,recipe):
		output_return = ''

		recipe_name = str(random.choice(self.char_inv[recipe]['recipe'].keys()))
		output_return = output_return + '\n' + self.Paint_SVAR('You learned how to make {0}'.format(recipe_name),'fg_yellow','bg_black')
		# output_return = output_return + '\n' + self.char_inv[recipe]['recipe'][recipe_name]
		self.Level_data['crafts'][recipe_name] = self.char_inv[recipe]['recipe'][recipe_name]
		# output_return = output_return + '\n' + self.Level_data['crafts']
		return output_return

	def craft_item(self,craft_item):
		output_return = ''

		recipes = self.Level_data['crafts']
		if craft_item.lower() == 'list':
			for recipe, data in recipes.items():
				output_return = output_return + '\n' + self.Paint_SVAR('Recipe - {0} - ingredients: '.format(recipe),'fg_cyan','bg_blue')
				for ingredient in recipes[recipe]['req_items']:
					output_return = output_return + '\n' + self.Paint_SVAR('	{0}.'.format(ingredient),'fg_cyan','bg_blue')
		t_item = craft_item.lower()
		t_item =  t_item.capitalize()

		if craft_item.lower() in recipes:
			haveit = 0
			X = 0
			for item in recipes[craft_item]['req_items']:
				if item in self.char_inv:
					if 'req_c_items' in recipes[craft_item]:
						output_return = output_return + '\n' + self.Paint_SVAR('you have {0} / {1} - {2}- ingredients: '.format(self.char_inv[item]['count'],recipes[craft_item]['req_c_items'][X],item),'fg_cyan','bg_blue')
						if int(self.char_inv[item]['count']) >= int(recipes[craft_item]['req_c_items'][X]):
							haveit += 1
					else:
						haveit += 1
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('you dont have  ingredient - {0}.'.format(item),'fg_cyan','bg_blue')
				X += 1

			if haveit >= len(recipes[craft_item]['req_items']):
				X = 0
				for item in recipes[craft_item]['req_items']:
					if 'req_c_items' in recipes[craft_item]:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - int(recipes[craft_item]['req_c_items'][X])
	 					if self.char_inv[item]['count'] == 0:
	 						del self.char_inv[item]
					else:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - 1
						if self.char_inv[item]['count'] == 0:
							del self.char_inv[item]
					X += 1

				recipes[craft_item].pop('req_items')
				output_return = output_return + '\n' + self.Paint_SVAR('You craft {0}.'.format(craft_item),'fg_cyan','bg_white')
				if craft_item in self.char_inv:
					self.char_inv[craft_item.lower()]['count'] = int(self.char_inv[craft_item.lower()]['count']) + 1
				else:
					self.char_inv[craft_item.lower()] = recipes[craft_item]
					self.char_inv[craft_item.lower()]['count'] = 1
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You dont have the items craft {0}.'.format(craft_item),'fg_red','bg_white')

		elif craft_item.upper() in recipes:
			craft_item = craft_item.upper()
			haveit = 0
			X = 0
			for item in recipes[craft_item]['req_items']:
				if item in self.char_inv:
					if 'req_c_items' in recipes[craft_item]:
						output_return = output_return + '\n' + self.Paint_SVAR('you have {0} / {1} - {2}- ingredients: '.format(self.char_inv[item]['count'],recipes[craft_item]['req_c_items'][X],item),'fg_cyan','bg_blue')
						if int(self.char_inv[item]['count']) >= int(recipes[craft_item]['req_c_items'][X]):
							haveit += 1
					else:
						haveit += 1
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('you have  ingredient - {0}.'.format(item),'fg_cyan','bg_blue')
				X += 1

			if haveit >= len(recipes[craft_item]['req_items']):
				X = 0
				for item in recipes[craft_item]['req_items']:
					if 'req_c_items' in recipes[craft_item]:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - int(recipes[craft_item]['req_c_items'][X])
	 					if self.char_inv[item]['count'] == 0:
	 						del self.char_inv[item]
					else:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - 1
						if self.char_inv[item]['count'] == 0:
							del self.char_inv[item]
					X += 1

				recipes[craft_item].pop('req_items')
				output_return = output_return + '\n' + self.Paint_SVAR('You craft {0}.'.format(craft_item),'fg_cyan','bg_white')
				if craft_item in self.char_inv:
					self.char_inv[craft_item.lower()]['count'] = int(self.char_inv[craft_item.lower()]['count']) + 1
				else:
					self.char_inv[craft_item.lower()] = recipes[craft_item]
					self.char_inv[craft_item.lower()]['count'] = 1

		elif t_item in recipes:
			craft_item = t_item
			haveit = 0
			X = 0
			for item in recipes[craft_item]['req_items']:
				if item in self.char_inv:
					if 'req_c_items' in recipes[craft_item]:
						output_return = output_return + '\n' + self.Paint_SVAR('you have {0} / {1} - {2}- ingredients: '.format(self.char_inv[item]['count'],recipes[craft_item]['req_c_items'][X],item),'fg_cyan','bg_blue')
						if int(self.char_inv[item]['count']) >= int(recipes[craft_item]['req_c_items'][X]):
							haveit += 1
					else:
						haveit += 1
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('you have  ingredient - {0}.'.format(item),'fg_cyan','bg_blue')
				X += 1


			if haveit >= len(recipes[craft_item]['req_items']):
				X=0
				for item in recipes[craft_item]['req_items']:
					if 'req_c_items' in recipes[craft_item]:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - int(recipes[craft_item]['req_c_items'][X])
	 					if self.char_inv[item]['count'] == 0:
	 						del self.char_inv[item]
					else:
						self.char_inv[item]['count'] = int(self.char_inv[item]['count']) - 1
						if self.char_inv[item]['count'] == 0:
							del self.char_inv[item]
					X= X + 1
				recipes[craft_item].pop('req_items')
				output_return = output_return + '\n' + self.Paint_SVAR('You craft {0}.'.format(craft_item),'fg_cyan','bg_white')
				if craft_item in self.char_inv:
					self.char_inv[craft_item.lower()]['count'] = int(self.char_inv[craft_item.lower()]['count']) + 1
				else:
					self.char_inv[craft_item.lower()] = recipes[craft_item]
					self.char_inv[craft_item.lower()]['count'] = 1
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You dont have the items craft {0}.'.format(craft_item),'fg_red','bg_white')
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('You dont know how to craft {0}.'.format(craft_item),'fg_red','bg_white')

		return output_return

	def use_PG(self,item_name,move):
		output_return = ''


		if int(self.char_stats[3]) > 20:
			self.char_stats[3] = int(int(self.char_stats[3]) -20)
			# move = list(move)
			D = move[0]
			Z = move[1]
			X = move[2]
			Y = move[3]
			if D in self.Level_data:
				if Z in self.Level_data[D]:
					if X in self.Level_data[D][Z]:
						if Y in self.Level_data[D][Z][X]:
							self.char_pos = [D,Z,X,Y]
							output_return = output_return + '\n' + self.Paint_SVAR('You open a portal to {0}, You hesitate for a moment and then jump in.'.format(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_title']),'fg_yellow','bg_white')
						else:
							self.bad_portal_dest()
					else:
						self.bad_portal_dest()
				else:
					self.bad_portal_dest()
			else:
				self.bad_portal_dest()
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} is not enough portal fluid.'.format(int(self.char_stats[3])),'fg_red','bg_white')

		return output_return

	def bad_portal_dest(self):
		#self.clear_screen()
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('You enter the portal, but find a world filled with giant butts spewing toxic gasses.\n You quickly rush back through the portal to safety.','fg_cyan','bg_white')
		return output_return

	def equip_armor(self,item_name,move):
		output_return = ''

		if self.char_armor == {}:
			output_return = output_return + '\n' + self.Paint_SVAR('You Equip {0}'.format(self.char_inv[item_name]['item_name']),'fg_white','bg_green')
			self.char_armor['Equiped'] = self.char_inv[item_name]
			self.char_armor['Equiped']['item_name'] = item_name
			self.char_stats[2] = int(self.char_stats[2]) + int(self.char_inv[item_name]['item_value'])
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('Your wearing {0} already'.format(self.char_armor['Equiped']['item_name']),'fg_cyan','bg_white')
			# if raw_input('Do you want to change?').upper() == 'Y':
			output_return = output_return + '\n' + self.Paint_SVAR('You Equip {0}'.format(self.char_inv[item_name]['item_name']),'fg_white','bg_green')
			self.char_stats[2] = int(self.char_stats[2]) - int(self.char_armor['Equiped']['item_value'])
			self.char_stats[2] = int(self.char_stats[2]) + int(self.char_inv[item_name]['item_value'])
			self.char_armor['Equiped'] = self.char_inv[item_name]
			self.char_armor['Equiped']['item_name'] = item_name
			# else:
			# 	output_return = output_return + '\n' + self.Paint_SVAR('You continue wearing {0}'.format(self.char_armor['Equiped']),'fg_yellow','bg_white')

			return output_return

	def equip_weapon(self,item_name,move):
		output_return = ''

		if self.char_weapon == {}:
			output_return = output_return + '\n' + self.Paint_SVAR('You Equip {0}'.format(self.char_inv[item_name]['item_name']),'fg_white','bg_green')
			self.char_weapon['Equiped'] = self.char_inv[item_name]
			self.char_stats[1] = int(self.char_stats[1]) + int(self.char_inv[item_name]['item_value'])
			self.char_weapon['Equiped']['item_name'] = item_name
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('Your wearing {0} already'.format(self.char_weapon['Equiped']['item_name']),'fg_cyan','bg_white')
			# if raw_input('Do you want to change?').upper() == 'Y':
			output_return = output_return + '\n' + self.Paint_SVAR('You Equip {0}'.format(self.char_inv[item_name]['item_name']),'fg_white','bg_green')
			self.char_stats[1] = int(self.char_stats[1]) - int(self.char_weapon['Equiped']['item_value'])
			self.char_stats[1] = int(self.char_stats[1]) + int(self.char_inv[item_name]['item_value'])
			self.char_weapon['Equiped'] = self.char_inv[item_name]
			self.char_weapon['Equiped']['item_name'] = item_name
			# else:
			# 	output_return = output_return + '\n' + self.Paint_SVAR('You continue wearing {0}'.format(self.char_weapon['Equiped']),'fg_white','bg_blue')

		return output_return

	def drink_potion(self,item_name,move):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('You consume {0} and regain {1} Health.'.format(item_name,self.char_inv[item_name]['item_value'],move),'fg_white','bg_cyan')
		self.char_stats[0] = int(self.char_stats[0]) + int(self.char_inv[item_name]['item_value'])
		self.char_inv[item_name]['count'] = int(self.char_inv[item_name]['count']) - 1
		if self.char_inv[item_name]['count'] == 0:
			del self.char_inv[item_name]
			return output_return

	def use_PF(self,item_name,move):
		output_return = ''
		output_return = output_return + '\n' + self.Paint_SVAR('You use {0} and regain {1} Portal Fluid.'.format(item_name,self.char_inv[item_name]['item_value'],move),'fg_yellow','bg_green')
		self.char_stats[3] = int(self.char_stats[3]) + int(self.char_inv[item_name]['item_value'])
		self.char_inv[item_name]['count'] = int(self.char_inv[item_name]['count']) - 1
		if self.char_inv[item_name]['count'] == 0:
			del self.char_inv[item_name]

		return output_return

	def unlock_door(self,direction):
		output_return = ''
		if direction.upper() in ['N','S','E','W','U','D',]:
			if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['M' + direction[0].upper()] == 'L':
				D_KEY = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['keys'][direction[0].upper() + 'K']
				# output_return = output_return + '\n' + D_KEY
				if D_KEY.lower() in self.char_inv:
					output_return = output_return + '\n' + self.Paint_SVAR('You unlock the door with {0}'.format(D_KEY),'fg_yellow','bg_green')
					self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['M' + direction[0].upper()] = 'Y'
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('The door to the {0} is not locked.'.format(direction),'fg_cyan','fg_black')
			return output_return
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} is not a direction.'.format(direction),'fg_cyan','fg_black')
		return output_return

	def join_comp(self,companion):
		output_return = ''
		if 'companions' in 	self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			if companion.lower() in	self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions']:
				output_return = output_return + '\n' + self.Paint_SVAR('{0} joined your party.'.format(companion),'fg_green','bg_black')
				self.char_comps[companion.lower()] = self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions'][companion.lower()]
				self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions'].pop(companion.lower())

		return output_return

	def drop_comp(self,companion):
		output_return = ''

		if 'companions' not in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions'] = {}
		if companion.lower() in	self.char_comps:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} left your party.'.format(companion),'fg_green','bg_black')
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['companions'][companion.lower()] = self.char_comps[companion.lower()]
			self.char_comps.pop(companion.lower())

		return output_return

	def kill_comp(self,companion):
		output_return = ''

		output_return = output_return + '\n' + self.Paint_SVAR('{0} has died. They are no longer in your party.'.format(companion),'fg_red','bg_black')
		if companion.lower() in	self.char_comps:
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'].update({self.char_comps[companion.lower()]['weapon']['Equiped']['item_name'] : self.char_comps[companion.lower()]['weapon']['Equiped']})
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['items'].update({self.char_comps[companion.lower()]['armor']['Equiped']['item_name'] : self.char_comps[companion.lower()]['armor']['Equiped']})

			self.char_comps.pop(companion.lower())

		return output_return

	def use_ammo(self,ammount):
		output_return = ''

		if self.char_weapon['Equiped']['item_class'].upper() == 'MW':
			return True
		elif int(self.char_stats[5]) > int(ammount):
			output_return = output_return + '\n' + self.Paint_SVAR('You used {0} Ammunition'.format(ammount),'fg_green','bg_black')
			self.char_stats[5] = int(self.char_stats[5]) - int(ammount)
			return True
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('You\'re out of Ammunition'.format(ammount),'fg_green','bg_black')
			return False

		return output_return
	def comp_use_ammo(self,companionammount):
		output_return = ''

		if self.char_comps[companion.lower()]['weapon']['Equiped']['item_class'].upper() == 'MW':
			return True
		elif int(self.char_comps[companion.lower()]['stats'][5]) > int(ammount):
			output_return = output_return + '\n' + self.Paint_SVAR('{1} used {0} Ammunition'.format(ammount),'fg_green','bg_black')
			self.char_comps[companion.lower()]['stats'][5] = int(self.char_comps[companion.lower()]['stats'][5]) - int(ammount)
			return True
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} is out of Ammunition'.format(companion),'fg_green','bg_black')
			return False

		return output_return

	def battle_calc_player(self,monster):
		output_return = ''

		#self.clear_screen()
		AT_RT = int(int(self.char_stats[1]) * 3)
		DF_RT = int(int(monster['stats'][2]) * 2)
		A_score = random.randint(0, AT_RT)
		D_score = random.randint(0, DF_RT)
		if self.use_ammo(1) == True:
			if A_score >= D_score:
				A_hit = int(A_score / 10)
				output_return = output_return + '\n' + self.Paint_SVAR('You hit {0} with your {2} for {1}.'.format(monster['name'],A_hit,self.char_weapon['Equiped']['item_name']),'fg_red','bg_green')
				monster['stats'][0] = int(int(monster['stats'][0]) - A_hit)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You tried to hit the {0} with your {1}, but slipped on some goop and fell over.'.format(monster['name'],self.char_weapon['Equiped']['item_name']),'fg_yellow','bg_blue')
			# self.battle_calc_comp(monster)
		if int(monster['stats'][0]) < 1:
			output_return = output_return + '\n' + self.Paint_SVAR('You killed {0}.'.format(monster['name']),'fg_green','bg,blue')
			self.M_drop_item(monster['name'])
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].pop(monster['name'])
		else:
			pass

		return output_return			# self.battle_calc_comp(monster)

	def auto_attack(self):
		output = ''
		#self.clear_screen()
		dead = True
		if 'monsters' not in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]:
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'] = {}
		if len(self.char_comps.items()) > 0 and len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].keys()) > 0:
			for companion, c_data in self.char_comps.items():
				if len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].keys()) > 0:
					c_monster = random.choice(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].keys())
					output = output + '\n' + self.battle_calc_char_comp(companion, self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][c_monster])

		for Monster, Data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].items():
			dead, moutput = self.battle_calc_comp(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster])
			output = output + '\n' + moutput
		return dead, output


	def battle_calc_char_comp(self,companion,monster):
		output_return = ''

		AT_RT = int(int(self.char_comps[companion.lower()]['stats'][1]) * 3)
		DF_RT = int(int(monster['stats'][2]) * 2)
		A_score = random.randint(0, AT_RT)
		D_score = random.randint(0, DF_RT)
		if A_score >= D_score:
			A_hit = int(A_score / 10)
			output_return = output_return + '\n' + self.Paint_SVAR('{0} hits {1} for {2}.'.format(companion,monster['name'],A_hit),'fg_yellow','bg_red')
			monster['stats'][0] = int(int(monster['stats'][0]) - A_hit)
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} tried to hit {1}, but {0} and dodged away.'.format(companion,monster['name']),'fg_yellow','bg_green')
		if int(monster['stats'][0]) < 1:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} killed {1}.'.format(companion,monster['name']),'fg_black','bg_red')
			self.M_drop_item(monster['name'])
			self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].pop(monster['name'])

		else:
			DF_RT = int(int(self.char_comps[companion.lower()]['stats'][2]) * 2)
			AT_RT = int(int(monster['stats'][1]) * 3)
			A_score = random.randint(0, AT_RT)
			D_score = random.randint(0, DF_RT)
			if A_score >= D_score:
				A_hit = int(A_score / 10)
				output_return = output_return + '\n' + self.Paint_SVAR('{0} was hit by {1} for {2}.'.format(companion,monster['name'],A_hit),'fg_yellow','bg_red')
				self.char_comps[companion.lower()]['stats'][0] = int(int(self.char_comps[companion.lower()]['stats'][0]) - A_hit)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('{0} tried to hit {1}, but {1} blinded it with some dust and dodged away.'.format(monster['name'],companion),'fg_yellow','bg_green')
			if int(self.char_stats[0]) < 1:
				output_return = output_return + '\n' + self.Paint_SVAR('{0} was killed by {1}.'.format(companion,monster['name']),'fg_black','bg_red')
				self.kill_comp(companion)

		return output_return



	def battle_calc_comp(self,monster):
		output_return = ''

		DF_RT = int(int(self.char_stats[2]) * 2)
		AT_RT = int(int(monster['stats'][1]) * 3)
		A_score = random.randint(0, AT_RT)
		D_score = random.randint(0, DF_RT)
		if A_score >= D_score:
			A_hit = int(A_score / 10)
			output_return = output_return + '\n' + self.Paint_SVAR('You were hit by {0} for {1}.'.format(monster['name'],A_hit),'fg_yellow','bg_red')
			self.char_stats[0] = int(int(self.char_stats[0]) - A_hit)
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('{0} tried to hit the you, but you blinded it with some dust and dodged away.'.format(monster['name']),'fg_yellow','bg_green')
		if int(self.char_stats[0]) < 1:
			output_return = output_return + '\n' + self.Paint_SVAR('You were killed by {0}.'.format(monster['name']),'fg_black','bg_red')
			return False, output_return
			# sys.exit(0)

		return True, output_return


	def complete_move(self,direction):
		output_return = ''

		#self.clear_screen()
		(Exists, Unlocked) = self.check_move(direction)
		if Exists == True and Unlocked == True:
			if direction.upper() == 'N' or direction.upper() == 'NORTH':
				self.char_pos[2] = str(int(self.char_pos[2]) + 1)
			elif direction.upper() == 'S' or direction.upper() == 'SOUTH':
				self.char_pos[2] = str(int(self.char_pos[2]) - 1)
			elif direction.upper() == 'E' or direction.upper() == 'EAST':
				self.char_pos[3] = str(int(self.char_pos[3]) + 1)
			elif direction.upper() == 'W' or direction.upper() == 'WEST':
				self.char_pos[3] = str(int(self.char_pos[3]) - 1)
			elif direction.upper() == 'U' or direction.upper() == 'UP':
				self.char_pos[1] = str(int(self.char_pos[1]) + 1)
			elif direction.upper() == 'D' or direction.upper() == 'DOWN':
				self.char_pos[1] = str(int(self.char_pos[1]) - 1)
			output_return = output_return + self.spawn_monster()
			output_return = output_return + '\n' + self.Paint_SVAR('You proceed {0} to {1}.'.format(direction,self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['Room_title']),'fg_yellow','bg_white')
		elif Exists == True and Unlocked == False:
			output_return = output_return + '\n' + self.Paint_SVAR('You can\'t proceed {0} the door is locked.'.format(direction),'fg_yellow','bg_white')
		else:
			output_return = output_return + '\n' + self.Paint_SVAR('You proceed {0} but hit your head on the wall blocking your way.'.format(direction),'fg_cyan','bg_white')

		return output_return

	def CMD_Prompt(self,Move):
		output_return = ''
		dead = True
		# output_return = output_return + '\n' + 'What would you like to do ? : \n'
		# Move = raw_input('|-#-|-#-|:  ')

		sMove = (Move.lower()).split(' ')


		if sMove[0] == 's' or sMove[0] == 'n' or sMove[0] == 'e' or sMove[0] == 'w' or sMove[0] == 'd' or sMove[0] == 'u' :
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			output_return = output_return + '\n' +self.complete_move(sMove[0])
		elif sMove[0] == 'south' or sMove[0] == 'north' or sMove[0] == 'east' or sMove[0] == 'west' or sMove[0] == 'down' or sMove[0] == 'up' :
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			output_return = output_return + '\n' + self.complete_move(sMove[0])

		elif sMove[0] == 'go' or sMove[0] == 'move' or sMove[0] == 'walk' or sMove[0] == 'run':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			output_return = output_return + '\n' + self.complete_move(sMove[1])

		elif sMove[0].lower() == 'inventory' or sMove[0].lower() == 'inv' or sMove[0].lower() == 'i':
			output_return = output_return + '\n' + self.display_inv()

		elif sMove[0].lower() == 'stat' or sMove[0].lower() == 'status':
			output_return = output_return + '\n' + self.display_char()

		elif sMove[0] == 'l' or sMove[0] == 'investigate' or sMove[0] == 'look' or sMove[0] == 'show' or sMove[0] == 'check':
			if len(sMove) == 1:
				output_return = output_return + '\n' + self.display_room()
			elif len(sMove) > 2:
				if sMove[2] == 's' or sMove[2] == 'n' or sMove[2] == 'e' or sMove[2] == 'w' or sMove[2] == 'd' or sMove[2] == 'u':
					output_return = output_return + '\n' + self.display_other_room(sMove[2].upper())
				elif sMove[2] == 'south' or sMove[2] == 'north' or sMove[2] == 'east' or sMove[2] == 'west' or sMove[2] == 'down' or sMove[2] == 'up':
					output_return = output_return + '\n' + self.display_other_room(sMove[2].upper())
				elif sMove[2] == 'inv' or sMove[2] == 'inventory' or sMove[2] == 'stuff':
					output_return = output_return + '\n' + self.display_inv()
				elif sMove[2] == 'myself' or sMove[2] == 'me' or sMove[2] == 'self':
					output_return = output_return + '\n' + self.display_char()
				else:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					if sMove[1].lower == 'at':
						myMove = re.sub('at','', myMove)
					elif sMove[1].lower == 'the':
						myMove = re.sub('the','', myMove)
					myMove = myMove.lstrip()
					myMove = myMove.rstrip()
					output_return = output_return + '\n' + myMove
					output_return = output_return + '\n' + self.lookat(myMove)

			elif len(sMove) > 1:
				if sMove[1] == 's' or sMove[1] == 'n' or sMove[1] == 'e' or sMove[1] == 'w' or sMove[1] == 'd' or sMove[1] == 'u':
					output_return = output_return + '\n' + self.display_other_room(sMove[1].upper())
				elif sMove[1] == 'south' or sMove[1] == 'north' or sMove[1] == 'east' or sMove[1] == 'west' or sMove[1] == 'down' or sMove[1] == 'up':
					output_return = output_return + '\n' + self.display_other_room(sMove[1].upper())
				elif sMove[1] == 'inv' or sMove[1] == 'inventory' or sMove[1] == 'stuff':
					output_return = output_return + '\n' + self.display_inv()
				elif sMove[1] == 'myself' or sMove[1] == 'me' or sMove[1] == 'self':
					output_return = output_return + '\n' + self.display_char()
				else:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					if sMove[1].lower == 'at':
						myMove = re.sub('at','', myMove)
					elif sMove[1].lower == 'the':
						myMove = re.sub('the','', myMove)
					myMove = myMove.lstrip()
					myMove = myMove.rstrip()
					output_return = output_return + '\n' + myMove
					output_return = output_return + '\n' + self.lookat(myMove)

		elif sMove[0] == 'g' or sMove[0] == 't' or sMove[0] == 'pick' or sMove[0] == 'take' or sMove[0] == 'grab' or sMove[0] == 'steal' or sMove[0] == 'get':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if len(sMove) == 1:
				output_return = output_return + '\n' + self.take_all_items(sMove[0])
			else:
				if dead == False:
					output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
					return dead,output_return

				if sMove[1].lower() == 'all' or sMove[1].lower() == 'a':
					output_return = output_return + '\n' + self.take_all_items(sMove[0])
				else:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					if sMove[1].lower == 'at':
						myMove = re.sub('at','', myMove)
					elif sMove[1].lower == 'the':
						myMove = re.sub('the','', myMove)
					elif sMove[1].lower == 'up':
						myMove = re.sub('up','', myMove)
					myMove = myMove.lstrip()
					myMove = myMove.rstrip()
					output_return = output_return + '\n' + self.take_item(sMove[0],myMove)

		elif sMove[0] == 'use' or sMove[0] == 'u':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if 'portal gun' in Move.lower():
				if 'portal gun' in self.char_inv:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					myMove = re.sub('portal gun','', myMove.lower())
					myMove = myMove.lstrip()
					pmove = myMove.rstrip()
					pmove = pmove.split('.')
					if len(pmove) != 4:
						output_return = output_return + '\n' + self.Paint_SVAR('You must enter a DCO Address. \nUse VALID Demensional CoOridinates in \'D.Z.X.Y\' format.','fg_cyan','bg_white')
					else:
						output_return = output_return + '\n' + self.use_PG('portal gun',pmove)
				else:
						output_return = output_return + '\n' + self.Paint_SVAR('You don\'t have a portal gun.','fg_cyan','bg_white')
			else:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				if sMove[1].lower == 'at':
					myMove = re.sub('at','', myMove)
				elif sMove[1].lower == 'the':
					myMove = re.sub('the','', myMove)
				myMove = myMove.lstrip()
				myMove = myMove.rstrip()
				output_return = output_return + '\n' + self.use_item(myMove,Move[0])

		elif sMove[0]  == 'wear' or  sMove[0]  == 'equip':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			myMove = re.sub(sMove[0].lower(),'', Move.lower())
			if sMove[1].lower == 'at':
				myMove = re.sub('at','', myMove)
			elif sMove[1].lower == 'the':
				myMove = re.sub('the','', myMove)
			myMove = myMove.lstrip()
			myMove = myMove.rstrip()
			output_return = output_return + '\n' + self.use_item(myMove,Move[0])

		elif sMove[0] == 'hit' or sMove[0] == 'shoot' or sMove[0] == 'attack' or sMove[0] == 'kill' or sMove[0] == 'destroy':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				if len(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].items()) > 0:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					if sMove[1].lower == 'at':
						myMove = re.sub('at','', myMove)
					elif sMove[1].lower == 'the':
						myMove = re.sub('the','', myMove)
					myMove = myMove.lstrip()
					Monster = myMove.rstrip()
					for MMonster, data in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'].items():
						search = re.compile('^{0}'.format(Monster))
						if len(re.findall(search,MMonster)) > 0:
							Monster = MMonster
							break

					if Monster in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters']:
						output_return = output_return + '\n' + self.battle_calc_player(self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monster])
					else:
						output_return = output_return + '\n' + self.Paint_SVAR('Your swinging blindly morty. What are you trying to hit?','fg_cyan','bg_black')
						# self.battle_calc_comp(self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['monsters'][Monser])
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('Now your just swinging at shadows morty. theres nothing here.','fg_cyan','bg_black')
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Your swinging blindly morty. What are you trying to hit?','fg_cyan','bg_black')

		elif sMove[0] == 'unlock':
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				direction = myMove.rstrip()[0]

				output_return = output_return + '\n' + self.unlock_door(direction)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('What did you want to unlock?','fg_cyan','bg_black')

		elif sMove[0] == 'buy' or sMove[0] == 'store' or sMove[0] == 'browse':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if 'dgps' in self.char_inv:
				if len(sMove) == 1:
					output_return = output_return + '\n' + self.Paint_SVAR('You login to the RM Online interdemensional store.','fg_green','bg_blue')
					output_return = output_return + '\n' + self.store('list')
				else:
					myMove = re.sub(sMove[0].lower(),'', Move.lower())
					myMove = myMove.lstrip()
					myMove = myMove.rstrip()
					output_return = output_return + '\n' + self.Paint_SVAR('You login to the RM Online interdemensional store.','fg_green','bg_blue')
					output_return = output_return + '\n' + self.store(myMove)

			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You must have your DGPS to login to the RM Online interdemensional store.','fg_cyan','bg_black')


		elif sMove[0] == 'call':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				number = myMove.rstrip()
				output_return = output_return + '\n' + self.call_phone(number)

			else:
				output_return = output_return + '\n' + self.Paint_SVAR('You must dial a number to make a call.','fg_cyan','bg_black')

		elif sMove[0].upper() == 'IM_DR_WHO':
			output_return = output_return + '\n' + self.Paint_SVAR('You are imbued with power from the Infinite Rick?','fg_yellow','bg_black')
			self.char_stats[0] = 9999999999
			self.char_stats[3] = 9999999999
			self.char_stats[4] = 9999999999
			self.char_inv['portal gun'] = {'item_name': 'portal gun', 'item_description' : 'It\'s Ricks portal gun', 'item_class': 'PG', 'item_value': '0', 'count' : 1 }
			self.char_comps = {'noob noob': {'name' : 'noob noob', 'stats' : [999,999,999,999], 'description' : 'Its your friend noob noob.', 'weapon': {'Equiped':{ 'item_name' : 'Noob Noobs Mop', 'item_value' : 0 , 'item_class' : 'MW', 'item_description' : 'It\'s NoobNoobs mop.','count': '1'}}, 'armor' : {'Equiped':{'item_class' : 'A', 'item_name' : 'T-Shirt', 'item_value' : 0  , 'item_description' : 'The shirt on your Back.','count': '1'}} } }
		elif sMove[0] == 'drop':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				direction = myMove.rstrip()

				output_return = output_return + '\n' + self.drop_item(sMove[0],myMove)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('What did you want to drop?','fg_cyan','bg_black')

		elif sMove[0] == 'invite':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				companion = myMove.rstrip()
				output_return = output_return + '\n' + self.join_comp(companion)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Who did you want to invite?','fg_cyan','bg_black')


		elif sMove[0] == 'dismiss':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				companion = myMove.rstrip()
				output_return = output_return + '\n' + self.drop_comp(companion)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Who did you want to dismiss?','fg_cyan','bg_blue')

		elif sMove[0] == 'help':
			output_return = output_return + '\n' + self.Paint_SVAR('Some of the possible moves(try others) :','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('look (item|monster|direction|companion|inventory): Look at the desired item.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('use (item|weapon|armor): Use the desired item.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('[i|inv|inventory]: Show inventory.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('[stat|status]: Show character status.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('take (item|weapon|armor|all): Take the desired item.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('craft (item|weapon|armor): Craft the desired item.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('craft list: Show your craft list.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('[N|S|E|W|U|D] : Move in the desired direction.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('unlock (N|S|E|W|U|D) : Unlock the door the desired direction.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('[hit|attack|shoot|kill] (monster) : Attack the desired monster.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('[invite|dismiss] (companion) : invite a companion.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('give [item|weapon|armor|ammo] (companion) : give the desired companion the desired item.','fg_magenta','bg_black')
			output_return = output_return + '\n' + self.Paint_SVAR('Try using other commands, some commands are room specific.','fg_magenta','bg_black')

		elif sMove[0] == 'give':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:

				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				myMove = myMove.rstrip()
				target = None
				for companion,data in self.char_comps.items():
					if companion in Move:
						target = companion
						break
				if target == None:
					output_return = output_return + '\n' + self.Paint_SVAR('Who did you want to give something to?','fg_cyan','bg_black')
				else:

					item = re.sub(sMove[0].lower(),'', Move.lower())
					item = re.sub(companion,'', item.lower())
					item = item.lstrip()
					item = item.rstrip()
					if sMove[1] == 'jerry':
						if sMove[2] == 'jerrys':
							item = 'jerry' + item
					output_return = output_return + '\n' + self.give_item(companion,item)

			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Who did you want to give something to?','fg_cyan','bg_black')

		elif sMove[0] == 'save':
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				sfile = myMove.rstrip()
				sfile = re.sub('\ ','',sfile)
				output_return = output_return + '\n' + self.Paint_SVAR('Saving game as {0}.'.format(sfile),'fg_yellow','bg_black')
				output_return = output_return + '\n' + self.write_save(sfile)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Enter the file name for the save command.','fg_cyan','bg_blue')


		elif sMove[0] == 'load':
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				myMove = myMove.lstrip()
				sfile = myMove.rstrip()
				sfile = re.sub('\ ','',sfile)
				output_return = output_return + '\n' + self.Paint_SVAR('Loading game from {0}.'.format(sfile),'fg_yellow','bg_black')
				output_return = output_return + '\n' + self.read_save(sfile)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Enter the file name for the save command.','fg_cyan','bg_black')


		elif sMove[0] == 'craft' or sMove[0] == 'make' or sMove[0] == 'build' or sMove[0] == 'create':
			dead,output  = self.auto_attack()
			output_return = output_return + output
			if dead == False:
				output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
				return dead,output_return
			if len(sMove) > 1:
				myMove = re.sub(sMove[0].lower(),'', Move.lower())
				craft_item = myMove.lstrip()
				craft_item = craft_item.rstrip()
				output_return = output_return + '\n' + self.Paint_SVAR('Attempting to craft {0}.'.format(craft_item),'fg_yellow','bg_black')
				output_return = output_return + '\n' + self.craft_item(craft_item)
			else:
				output_return = output_return + '\n' + self.Paint_SVAR('Crafting failed.','fg_cyan','bg_black')


		# elif sMove[0] == 'exit' or sMove[0] == 'quit':
		# 	if raw_input('Are you sure you want to quit? [Y|N] : ').upper() == 'Y':
		# 		sys.exit(0)
		# 		return output_return

		else:
			try:
				if self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps']['Is_Trap'].upper() == 'Y':
					if Move.lower() in self.Level_data[self.char_pos[0]][self.char_pos[1]][self.char_pos[2]][self.char_pos[3]]['traps']:
						# output_return = output_return + '\n' + 'in trap execution'
						dead,output  = self.auto_attack()
						output_return = output_return + output
						if dead == False:
							output_return = output_return + '\n' + self.Paint_SVAR('You have died. Do you want to continue? ','fg_red','bg_black')
							return dead,output_return
						output_return = output_return + '\n' + self.execute_trap(Move.lower())
					else:
						output_return = output_return + '\n' + self.Paint_SVAR('I dont understand \'{0}\'. Wanna give an old man a break and tell me what you really want?'.format(Move),'fg_cyan','bg_black')
				else:
					output_return = output_return + '\n' + self.Paint_SVAR('I dont understand \'{0}\'. Wanna give an old man a break and tell me what you really want?'.format(Move),'fg_cyan','bg_black')
			except:
				output_return = output_return + '\n' + self.Paint_SVAR('I dont understand \'{0}\'. Wanna give an old man a break and tell me what you really want?'.format(Move),'fg_cyan','bg_black')
		return dead,output_return
if __name__ == "__main__":
	RMCYTAApp().run()
