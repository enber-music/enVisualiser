# enVisualiser
Blender audio visualiser

1. Start an instance of blender and delete the default point light

2. We need to create the material first so the script has something to add to the particles. Click on the default box and then click on the 'shading' tab at the top of the screen. Click the 'New' button to create the new material

![Add new material](https://github.com/enber-music/enVisualiser/blob/master/instruction_images/new_material.PNG)

3. Create a new material and call it 'PARTICLE' (case sensitive). You should delete the default boxes and replace with the ones below. To add a box, click on the 'Add' button then start typing to search for the specific box/node.
![Add new material](https://github.com/enber-music/enVisualiser/blob/master/instruction_images/PARTICLE_material.PNG)

4. You can now delete the default box.

5. In the top tabs click the '+' button to add workspace. Add General > Scripting
![Add scripting tab](https://github.com/enber-music/enVisualiser/blob/master/instruction_images/add_scripting.PNG)

6. Ensure that 'text editor' is selected (shift F11), click New 'data text block'
![Add new text](https://github.com/enber-music/enVisualiser/blob/master/instruction_images/new_text.PNG)

7. Copy-paste the contents of enVisualiser.py to this next text file

8. Change the parameter 'audiofile' to the audio file you want to work with and use '\\' between directories (see the description in the file for an example)
  audiofile = "**C:\\Users\\Public\\Desktop\\audio_file.mp3**" # use double '\\' between directories
  no_bars = 64 # number of points generating audio response
  baroffset=0.25 # Generally between 0.1 and 1 works best
  grav_speed = 20 # controls speed and distance particles travel before stopping
  no_parts = 5000 # number of particles
  part_life = 75 # how long particles last

9. Window > Toggle System Console, if you want to see the script run

10. Hit the play button at the top of the script
![Run script](https://github.com/enber-music/enVisualiser/blob/master/instruction_images/run_script.PNG)

11. The system console will print out the process. When it does, go back to layout and press spacebar to play your audio along with watching the visualisation :-)
