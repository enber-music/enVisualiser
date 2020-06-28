# Made by enber music, 2020
# Free for any use
# Please credit/link to: https://github.com/enber-music/enVisualiser 
# Feel free to check out my other stuff - https://soundcloud.com/enber_music | https://www.youtube.com/channel/UC4tFNpjQsE5Jlv_iBCDKO3A

import bpy
from bpy import context
import math


#################################################################################
########################## CONTROL PARAMETERS ###################################
#################################################################################

audiofile = "C:\\Users\\Public\\Desktop\\audio_file.mp3" # use double '\\' between directories
no_bars = 64 # number of points generating audio response
baroffset=0.25 # Generally between 0.1 and 1 works best
grav_speed = 20 # controls speed and distance particles travel before stopping
no_parts = 5000 # number of particles
part_life = 75 # how long particles last

#################################################################################
#################################################################################


bpy.context.scene.gravity[0] = 0
bpy.context.scene.gravity[1] = grav_speed * -1
bpy.context.scene.gravity[2] = grav_speed * 0.05 * -1

bpy.ops.sequencer.delete()

scene = context.scene

if not scene.sequence_editor:
    scene.sequence_editor_create()
 
soundstrip = scene.sequence_editor.sequences.new_sound("track", audiofile, 1, 1)

# auto frame code courtesy of https://github.com/doakey3/Bizualizer/blob/master/operators/audio_to_vse.py
frame_start = 300000
frame_end = -300000
for strip in scene.sequence_editor.sequences:
    try:
        if strip.frame_final_start < frame_start:
            frame_start = strip.frame_final_start
        if strip.frame_final_end > frame_end:
            frame_end = strip.frame_final_end - 1
    except AttributeError:
        pass

if frame_start != 300000:
    scene.frame_start = frame_start
if frame_end != -300000:
    scene.frame_end = frame_end
####################################################################################################

bpy.ops.mesh.primitive_ico_sphere_add(radius=0.5, subdivisions=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
bpy.context.object.name = "ParticleIco"
part_mat = bpy.data.materials["PARTICLE"]
bpy.context.object.active_material = part_mat
bpy.context.object.hide_render = True

bpy.context.scene.frame_set(1)

xlocation = 0
freqlow = 0
freqhigh = 0
barlog=1
logintvl = 0.0
logintvl = math.log(20000.0)/math.log(no_bars)
   
i=0

while i < no_bars:

    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
    obj = bpy.context.object
    obj.location = (-(2 * i) * baroffset, 0.0, 0.0)
    obj.scale = (0.05,0.05,0.05)
    obj.keyframe_insert(data_path="location", index=2, frame=0)

    bpy.context.object.name = "musicbar"
    freqlow = i**logintvl
    freqhigh = (i+1)**logintvl
    
    bpy.context.area.ui_type = 'FCURVES'
    bpy.ops.graph.sound_bake(filepath=audiofile, low=freqlow, high=freqhigh)
    
    ps = obj.modifiers.new("part", 'PARTICLE_SYSTEM')
    psys = obj.particle_systems[ps.name]
    psys.settings.render_type = 'OBJECT'
    psys.settings.instance_object = bpy.data.objects["ParticleIco"]
    psys.settings.count = no_parts
    psys.settings.mass = 100  
    psys.settings.lifetime = part_life
    psys.settings.userjit = 1
    psys.settings.frame_end = frame_end
    
    fcurve = obj.animation_data.action.fcurves[0]
    envo = fcurve.modifiers.new(type='ENVELOPE')
    envo.default_min = 0.0
    # linear scale first 500Hz so less extreme
    if freqhigh < 500:
        envo.default_max = (1 - (freqhigh/500 )) + 0.2
    else:
        envo.default_max = 0.2
        
    envo.control_points.add(frame = 0)
    
    # don't render particles below 35Hz (as these are mostly flat)
    if freqhigh < 35:
        bpy.context.object.hide_render = True
    
    print (scene.frame_end)
    i = i + 1

bpy.context.area.ui_type = 'TEXT_EDITOR'  
    
