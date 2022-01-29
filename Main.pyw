# region <<<<=====================================[Application Information]======================================>>>>

# APP NAME:
# PinBoreNotchCalculator

# APP USAGE:
# USED TO CALCULATE NOTCH LOCATION (X and Y) TO USE IT IN PIN BORE PROGRAMS.

# VERSION:
# PinBoreNotchCalculatorVersion1.0.0

# LANGUAGE:
# Python 3.7

# FRAME WORKS:
# Kivy and Kivymd to build the App and design the Layout.

# CREATED BY:
# Moemen Alatweh
# EMAIL:
# malatweh@rwbteam.com
# moemenatweh@hotmail.com

# endregion <<<<==================================[Application Information]======================================>>>>


# region <<<<=====================================[Application Requirements]=====================================>>>>

# FROM kivy.config IMPORT Config TO CONTROL APP CONFIGURATION SETTINGS.
from kivy.config import Config
# MAKE THE APP HAVE FIXED CONFIGURATION(BY PUT False) THAT'S MAKE THE USER CAN'T CHANGE ANY THING AS MAXIMIZE
# THE SCREEN FOR FULL SCREEN OR CHANGE THE SIZE, TO KEEP THE APP ORGANIZED.
Config.set('graphics', 'resizable', False)
# IMPORT (MDApp) TO CREATE THE APP
from kivymd.app import MDApp
# FROM kivy.core IMPORT Window TO BE ABLE TO CONTROL APP WINDOW SIZE.
from kivy.core.window import Window
# FROM kivy.uix.image IMPORT (AsyncImage) IF NEED TO USE IMAGE FROM WEBSITE , USE (Image) IF PHOTO ON LOCAL COMPUTER
from kivy.uix.image import AsyncImage
# FROM kivy.lang IMPORT Builder THAT'S A METHOD TO CREATE THE TEXT INPUT (KV Part)
from kivy.lang.builder import Builder
# FROM kivy.uix.screenmanager IMPORT ScreenManager, and Screen TO CREATE APP SCREEN AND MANEGE THEM
from kivy.uix.screenmanager import ScreenManager, Screen
# IMPORT BUTTONS TO DO ACTIONS
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
# IMPORT boxlayout THAT'S INCLUDE ALL APP COMPONENTS
from kivymd.uix.boxlayout import MDBoxLayout
# USE MDDialog TO SHOW DIALOG WINDOW OF MESSAGES
from kivymd.uix.dialog import MDDialog
# USE Clipboard TO BE ABLE TO COPY VALUES TO WINDOWS OPERATION SYSTEM
from kivy.core.clipboard import Clipboard
# IMPORT MATH LIBRARY TO USE SIN(ANGLE)
import math

# endregion <<<<====================================[Application Requirements]====================================>>>>


# region <<<<========================================[Screen Builder KV]=========================================>>>>
Screens_Builder = """
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'HomeScreen'
    MDLabel:
        text: '4 Cycle PinBore Notch Calculator'
        pos_hint: {'center_x':0.73,'center_y':0.85}
        font_size: '32sp'
        bold: True
        italic: True
        theme_text_color: "Primary"
        tooltip_text: self.text
            
    MDLabel:
        text: 'Enter Values Below to Calculate Notch Location'
        pos_hint: {'center_x':0.78,'center_y':0.63}
        font_size: '18sp'
        bold: True
        italic: True
        theme_text_color: "Secondary"        
            
    MDTextField:
        id: PilotBoreDepth
        hint_text: "Pilot Bore Depth"
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        input_filter: "float"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.20, 'center_y': 0.50}
        size_hint_x:None
        width:119
        height:10 
             
    MDTextField:
        id: PinHoleDiameter
        hint_text: "Pin Hole Diameter"
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        input_filter: "float"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.50}
        size_hint_x:None
        width:127
        height:10    
        
    MDTextField:
        id: PilotToPin
        hint_text: " Pilot To Pin"
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        input_filter: "float"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.80, 'center_y': 0.50}
        size_hint_x:None
        width:92
        height:10        
        
    MDTextField:
        id: NotchAngle
        hint_text: "   Notch Angle"
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        input_filter: "float"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.35, 'center_y': 0.40}
        size_hint_x:None
        width:110
        height:10         
        
    MDTextField:
        id: Offset
        hint_text: "        Offset"
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        input_filter: "float"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.66, 'center_y': 0.40}
        size_hint_x:None
        width:110
        height:10       
            
    MDRaisedButton:                                                                         
        text: 'CALCULATE'
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        pos_hint: {'center_x':0.5,'center_y':0.25}
        on_press : 
            root.calculate_notch_location()   
        
    MDRaisedButton:                                                                         
        text: 'RESET'
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        pos_hint: {'center_x':0.5,'center_y':0.15}  
        on_press : 
            root.reset_fields()  
     
    MDLabel:
        text: '             Version 1.0.1'
        pos_hint: {'center_x':1.32,'center_y':0.07}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1 
                
    MDLabel:
        text: 'Created by: Moemen Alatweh'
        pos_hint: {'center_x':1.32,'center_y':0.04}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1
    
    MDLabel:
        text: 'malatweh@rwbteam.com'
        pos_hint: {'center_x':1.33,'center_y':0.01}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1                        

"""
# endregion <<<<=======================================[Screen Builder KV]========================================>>>>


# region <<<<===========================================[Home Screen]============================================>>>>


class HomeScreen(Screen):

    def calculate_notch_location(self):
        # TO ACCESS VALUES FROM TextField WE USE THE "ID" FOR EACH ONE
        pilot_bore_depth = self.ids["PilotBoreDepth"].text
        print("PilotBoreDepth = " + pilot_bore_depth)

        pin_hole_diameter = self.ids["PinHoleDiameter"].text
        print("PinHoleDiameter = " + pin_hole_diameter)

        pilot_to_pin = self.ids["PilotToPin"].text
        print("PilotToPin = " + pilot_to_pin)

        notch_angle = self.ids["NotchAngle"].text
        print("NotchAngle = " + notch_angle)

        offset = self.ids["Offset"].text
        print("Offset = " + offset)
        print()

        # TO MAKE SURE ALL FIELDS HAVE VALUES (ALL FIELDS ARE REQUIRED TO GET RIGHT CALCULATION)
        if (pilot_bore_depth != "" and pin_hole_diameter != "" and pilot_to_pin != "" and notch_angle != "" and
                offset != ""):
            print("Start Calculation")
            X_distance_from_origin_to_pin_center = format(float(pilot_bore_depth) - abs(float(pilot_to_pin)) -
                                                          (float(pin_hole_diameter) / 2), '.4f')
            print("X_distance_from_origin_to_pin_center = " + X_distance_from_origin_to_pin_center)

            # MATH FOR NOTCH
            # IT FIGURED OUT BY DRAWING TRIANGLE IN SOLID-WORK AND USE Trigonometric MATH AND Pythagorean THEOREM
            # SEE WORD FILE OF THE MATH FOR MORE INFORMATION
            # WE USE (math.radians(notch_angle)) BECAUSE WE NEED USE ANGLE IN DEGREES
            Y_value_for_notch_math = float(round((float(pin_hole_diameter) / 2) *
                                                 (math.sin(math.radians((180 - float(notch_angle))))), 4))
            print("Y_value_for_notch_math = " + str(Y_value_for_notch_math))

            X_value_for_notch_math = float(round((float(pin_hole_diameter) / 2) *
                                                 (math.cos(math.radians((180 - float(notch_angle))))), 4))

            print("X_value_for_notch_math = " + str(X_value_for_notch_math))

            # MAKE IT global TO BE ABLE TO USE IT IN OTHER Functions
            global Y_distance_from_origin_to_circlip_notch
            Y_distance_from_origin_to_circlip_notch = format(float(Y_value_for_notch_math) + float(offset), '.4f')
            print("Y_distance_from_origin_to_circlip_notch = " + Y_distance_from_origin_to_circlip_notch)

            # MAKE IT global TO BE ABLE TO USE IT IN OTHER Functions
            global X_distance_from_origin_to_circlip_notch
            X_distance_from_origin_to_circlip_notch = format(
                float(X_distance_from_origin_to_pin_center) + float(X_value_for_notch_math), '.4f')
            print("X_distance_from_origin_to_circlip_notch = -" + X_distance_from_origin_to_circlip_notch)

            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window, font_size=16)
            copy_X_value = MDRectangleFlatButton(text='Copy X-Value', theme_text_color="Custom",
                                                 text_color=(1, 1, 0, 1), on_release=self.copy_x_distance, font_size=16)
            copy_Y_value = MDRectangleFlatButton(text='Copy Y-Value', theme_text_color="Custom",
                                                 text_color=(0, 153/255, 1, 1),
                                                 on_release=self.copy_y_distance, font_size=16)

            self.home_screen_message_window = MDDialog(title='[color=248f24]Success Message[/color]', text=(
                '[color=ffffff]X-Distance From Origin to Circlip Notch = [/color]' +
                '[b][i][color=ffff00]-' + X_distance_from_origin_to_circlip_notch + '[/color][/i][/b]' + '\n' +
                '[color=ffffff]Y-Distance From Origin to Circlip Notch = [/color]' +
                '[b][i][color=0099ff]' + Y_distance_from_origin_to_circlip_notch + '[/color][/i][/b]'),
                        size_hint=(0.7, 1.0), buttons=[copy_X_value, copy_Y_value, close_button], auto_dismiss=False)
            # TO OPEN THE DIALOG WINDOW
            self.home_screen_message_window.open()

        else:
            print("All Fields are Required")
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window, font_size=16)
            self.home_screen_message_window = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                '[color=ffffff]All Fields are [b][i]REQUIRED[/i][/b], Please Enter ALL Values and Try Again.[/color]'),
                                            size_hint=(0.7, 1.0), buttons=[close_button], auto_dismiss=False)
            # TO OPEN THE DIALOG WINDOW
            self.home_screen_message_window.open()

            # TO INDICATE ANY MISSING FIELD, WE MAKE FIELDS ON FOCUS MODE,
            # THEN ANY EMPTY FIELDS WILL CHANGE TO RED COLOR TO INDICATE IT IS REQUIRED
            self.ids["PilotBoreDepth"].focus = True
            self.ids["PinHoleDiameter"].focus = True
            self.ids["PilotToPin"].focus = True
            self.ids["NotchAngle"].focus = True
            self.ids["Offset"].focus = True

    # TO COPY X-VALUE
    # WE HAVE "-" AS TEXT BECAUSE THIS VALUE ALWAYS WILL BE NEGATIVE (i.e: BELOW THE ORIGIN POINT)
    def copy_x_distance(self, obj):
        Clipboard.copy("-" + X_distance_from_origin_to_circlip_notch)
        print("Copied X_value=-" + X_distance_from_origin_to_circlip_notch)

    # TO COPY Y-VALUE
    def copy_y_distance(self, obj):
        Clipboard.copy(Y_distance_from_origin_to_circlip_notch)
        print("Copied Y_value=" + Y_distance_from_origin_to_circlip_notch)

    # TO RESET ALL FIELDS WHEN USER CLICK ON RESET BUTTON
    def reset_fields(self):
        self.ids["PilotBoreDepth"].text = ""
        self.ids["PinHoleDiameter"].text = ""
        self.ids["PilotToPin"].text = ""
        self.ids["NotchAngle"].text = ""
        self.ids["Offset"].text = ""

    # TO CLOSE MESSAGE WINDOW
    def close_home_screen_window(self, obj):
        self.home_screen_message_window.dismiss()

# endregion <<<<==========================================[Home Screen]===========================================>>>>


# region <<<<==========================================[Screen Manager]==========================================>>>>
# Create the screen manager


sm = ScreenManager()
sm.add_widget(HomeScreen(name='HomeScreen'))


# endregion <<<<=========================================[Screen Manager]========================================>>>>


# region <<<<=======================================[Application Builder]========================================>>>>

class PinBoreNotchCalculator(MDApp):

    def build(self):
        # TO CONTROL SIZE OF THE SCREEN (Window.size = (WIDTH, HEIGHT))
        Window.size = (900, 650)
        # TO CHOOSE BACKGROUND MODE OF APP WHETHER DARK OR LIGHT
        self.theme_cls.theme_style = "Dark"
        # TO SET DEFAULT COLOR OF APP ELEMENTS(LABELS,BUTTONS...ETC)
        self.theme_cls.primary_palette = "Red"
        # TO SET DEFAULT COLOR CONCENTRATION(DARKNESS AND BRIGHTNESS) OF APP ELEMENTS(LABELS,BUTTONS...ETC)
        self.theme_cls.primary_hue = "900"
        # LOAD (builder_screen) TO USE IT IN THE APP
        builder_screen = Builder.load_string(Screens_Builder)
        # TO DEFINE (Screen() THAT USED TO DISPLAY THE APP) AS (app_screen) TO USE IT LATER
        app_screen = Screen()

        # BoxLayout FOR ENTIRE APP INCLUDE ALL WIDGETS AND ELEMENTS, SHOULD ADD ALL APP COMPONENTS FOR THIS BOX LAYOUT.
        # (orientation='vertical') TO ORGANIZE APP ELEMENTS VERTICALLY,
        # (spacing=20) TO MAKE SPACE BETWEEN APP ELEMENTS,
        # (padding=15) TO MAKE SPACE BETWEEN WALL BORDERS AND APP ELEMENTS,
        # (md_bg_color= [32/255.0, 32/255.0, 32/255.0, 1]) TO CHANGE THE COLOR BY ADJUSTING RGB VALUE
        # (CHECK: https://www.w3schools.com/colors/colors_picker.asp?colorhex=edfeff)
        app_box_layout = MDBoxLayout(orientation='vertical', spacing=20, padding=15,
                                     md_bg_color=[32 / 255.0, 32 / 255.0, 32 / 255.0, 1])

        # TO ADD PICTURE FOR THE APP FROM WEBSITE
        app_image = AsyncImage(source='https://www.wiseco.com/Images/Downloads/Wiseco_Black_CMYK.gif', size_hint_y=None,
                               height=70, allow_stretch=True, pos_hint={'center_x': 0.5, 'center_y': 0.10},
                               color=[150 / 255.0, 0 / 255.0, 0 / 255.0, 1])
        # TO ADD app_image TO app_box_layout TO DISPLAY IT IN THE APP SCREEN
        app_box_layout.add_widget(app_image)

        # TO ADD Screens_Builder THAT'S CREATE ABOVE
        app_box_layout.add_widget(builder_screen)

        # ADD app_box_layout THAT CONTAIN ALL ELEMENTS AND WIDGETS OF THE APP TO app_screen
        # TO DISPLAY IT IN THE APP SCREEN.
        app_screen.add_widget(app_box_layout)
        return app_screen


PinBoreNotchCalculator().run()

# endregion <<<<=====================================[Application Builder]=======================================>>>>
