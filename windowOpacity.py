
from PySide import QtGui
import maya.cmds as cmds
import shiboken
import maya.OpenMayaUI as mui

cmds.lsUI(windows = True)

def _getWindow(window_name):
    '''
    Get a pointer to the chose window
    '''
    ptr = mui.MQtUtil.findWindow(window_name)
    return shiboken.wrapInstance(long(ptr), QtGui.QWidget)


def _sliderValue():
    '''
    Get value from slider
    '''
    return cmds.floatSliderGrp('opacity_slider', q = True, value = True)
    

window_ptr = _getWindow('scriptEditorPanel1Window')


window_ptr.setWindowOpacity(value)



###########
def createSlider():
    '''
    Make window with slider.
    '''
    window = cmds.window('slider', title='floatSliderGrp Example')
    cmds.columnLayout()
    cmds.floatSliderGrp('opacity_slider' ,label='Group 1', field=True, minValue=0.0, maxValue=1.0, fieldMinValue=0.0, fieldMaxValue=1, value=1 )
    cmds.showWindow( 'slider' )
