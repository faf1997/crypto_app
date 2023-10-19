from kivy.lang import Builder

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem




Builder.load_string('''
<ItemConfirm>
    
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"

''')



class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False