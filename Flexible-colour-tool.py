from maya import cmds as mc

colour_dict = {
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


def get_colour_index(menu_name):
    colour_name = mc.optionMenu(menu_name, query=True, value=True)
    return colour_dict.get(colour_name, -1)


def apply_colours_custom_suffix(*args):
    sel = mc.ls(sl=True, type="nurbsCurve")

    suffix_L = mc.textField('suffixField_L', query=True, text=True)
    suffix_R = mc.textField('suffixField_R', query=True, text=True)
    suffix_M = mc.textField('suffixField_M', query=True, text=True)

    colour_L = get_colour_index('colourMenu_L')
    colour_R = get_colour_index('colourMenu_R')
    colour_M = get_colour_index('colourMenu_M')

    for ctrl in sel:
        mc.setAttr(f"{ctrl}.overrideRGBcolours", 0)
        if suffix_L and suffix_L in ctrl and colour_L != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overridecolour", colour_L)
        elif suffix_R and suffix_R in ctrl and colour_R != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overridecolour", colour_R)
        elif suffix_M and suffix_M in ctrl and colour_M != -1:
            mc.setAttr(f"{ctrl}.overrideEnabled", 1)
            mc.setAttr(f"{ctrl}.overridecolour", colour_M)


def build_colour_custom_suffix_ui():
    if mc.window("colourCtrlUI", exists=True):
        mc.deleteUI("colourCtrlUI")

    # Show warning dialog
    mc.confirmDialog(
        title='Important!',
        message='This tool only works if your controls are properly named.\n\nMake sure prefixes|suffixes are correct!',
        button=['OK'],
        defaultButton='OK'
    )

    mc.window("colourCtrlUI", title="Flexible Control colour Tool", widthHeight=(300, 250))
    mc.columnLayout(adjustableColumn=True, rowSpacing=10)

    # LEFT
    mc.text(label="Left Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_L', placeholderText='_L')
    mc.optionMenu('colourMenu_L', label='colour')
    for colour in colour_dict:
        mc.menuItem(label=colour)
    mc.setParent('..')

    # RIGHT
    mc.text(label="Right Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_R', placeholderText='_R')
    mc.optionMenu('colourMenu_R', label='colour')
    for colour in colour_dict:
        mc.menuItem(label=colour)
    mc.setParent('..')

    # MIDDLE
    mc.text(label="Middle Controls (Suffix or Prefix)")
    mc.rowLayout(numberOfColumns=2, adjustableColumn=1, columnAlign=(1, 'right'))
    mc.textField('suffixField_M', placeholderText='_M')
    mc.optionMenu('colourMenu_M', label='colour')
    for colour in colour_dict:
        mc.menuItem(label=colour)
    mc.setParent('..')

    mc.separator(height=10, style='in')
    mc.button(label="Apply colours to Selected Controls", command=apply_colours_custom_suffix)

    mc.showWindow("colourCtrlUI")


# Run the UI
build_colour_custom_suffix_ui()
