from maya import cmds as mc

color_dict = {
    "None": -1,
    "Black": 1,
    "Dark Grey": 2,
    "Light Grey": 3,
    "Dark Blue": 5,
    "Blue": 6,
    "Sky Blue": 18,
    "Green": 14,
    "Dark Green": 7,
    "Red": 13,
    "Pink": 9,
    "Orange": 21,
    "Yellow": 17,
    "Brown": 10,
    "White": 16
}


def get_color_index(menu_name):
    color_name = mc.optionMenu(menu_name, query=True, value=True)
    return color_dict.get(color_name, -1)


def apply_colors_custom_suffix(*args):
    sel = mc.ls(sl=True, type="nurbsCurve")

    suffix_L = mc.textField('suffixField_L', query=True, text=True)
    suffix_R = mc.textField('suffixField_R', query=True, text=True)
    suffix_M = mc.textField('suffixField_M', query=True, text=True)

    color_L = get_color_index('colorMenu_L')
    color_R = get_color_index('colorMenu_R')
    color_M = get_color_index('colorMenu_M')

    for ctrl in sel:

        if suffix_L and suffix_L in ctrl and color_L != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideRGBColors", 0)
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideColor", color_L)
        elif suffix_R and suffix_R in ctrl and color_R != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideRGBColors", 0)
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideColor", color_R)
        elif suffix_M and suffix_M in ctrl and color_M != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideRGBColors", 0)
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overrideColor", color_M)


def build_color_custom_suffix_ui():
    if mc.window("colorCtrlUI", exists=True):
        mc.deleteUI("colorCtrlUI")

    # Show warning dialog
    mc.confirmDialog(
        title='Important!',
        message='This tool only works if your controls are properly named.\n\nMake sure prefixes|suffixes are correct!',
        button=['OK'],
        defaultButton='OK'
    )

    mc.window("colorCtrlUI", title="Flexible Control Color Tool", widthHeight=(300, 250))
    mc.columnLayout(adjustableColumn=True, rowSpacing=10)

    # LEFT
    mc.text(label="Left Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_L', placeholderText='_L')
    mc.optionMenu('colorMenu_L', label='Color')
    for color in color_dict:
        mc.menuItem(label=color)
    mc.setParent('..')

    # RIGHT
    mc.text(label="Right Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_R', placeholderText='_R')
    mc.optionMenu('colorMenu_R', label='Color')
    for color in color_dict:
        mc.menuItem(label=color)
    mc.setParent('..')

    # MIDDLE
    mc.text(label="Middle Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_M', placeholderText='_M')
    mc.optionMenu('colorMenu_M', label='Color')
    for color in color_dict:
        mc.menuItem(label=color)
    mc.setParent('..')

    mc.separator(height=10, style='in')
    mc.button(label="Apply Colors to Selected Controls", command=apply_colors_custom_suffix)

    mc.showWindow("colorCtrlUI")


# Run the UI
build_color_custom_suffix_ui()
