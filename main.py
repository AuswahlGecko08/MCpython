

# Base Game
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# WorldGen
from perlin_noise import PerlinNoise
import random


# Customizability
CustomWidth = input("World Width?")
CustomLength = input("World Length?")

CustomHeight = input("World Height?")

CustomAmp = input("Hill Height?")

CustomFreq = input("Space Between Hills?")

app = Ursina()

# Variables

terrain_width = int(CustomWidth)
terrain_length = int(CustomLength)
Stone_height = int(CustomHeight)



player = FirstPersonController()
player.speed = 8


# WorldGen

Sky(color=color.cyan)




SeedGen = random.randint(4000, 5000)

noise = PerlinNoise(octaves=2, seed=SeedGen)
amp = int(CustomAmp)
freq = int(CustomFreq)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            
            texture='assets/Voxel.png',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

class Grass(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            
            texture='assets/Grass.png',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )



class Dirt(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            
            texture='assets/Dirt.png',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

class Stone(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            
            texture='assets/Stone.png',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )






for i in range(terrain_width*terrain_length):
    cube = Entity(model="cube", parent=scene, texture="assets/Grass.png", collider="mesh", color=color.hsv(0, 0, random.uniform(.9, 1.0)))
    cube.x = floor(i/terrain_width)
    cube.z = floor(i%terrain_width)
    cube.y = floor(noise([cube.x/freq, cube.z/freq])*amp) + 2

for i in range(terrain_width*terrain_length):
    cube = Entity(model="cube", texture="assets/Dirt.png", collider="mesh")
    cube.x = floor(i/terrain_width)
    cube.z = floor(i%terrain_width)
    cube.y = floor(noise([cube.x/freq, cube.z/freq])*amp) + 1



while Stone_height > 0:
    Stone_height = Stone_height - 1

    for i in range(terrain_width*terrain_length):
        cube = Entity(model="cube", texture="assets/Stone.png", collider="mesh")
        cube.x = floor(i/terrain_width)
        cube.z = floor(i%terrain_width)
        cube.y = floor(noise([cube.x/freq, cube.z/freq])*amp) - Stone_height
    


        

def input(key):
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
            Audio(sound_file_name="assets/Place.wav")

    if key == 't':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Dirt(position=hit_info.entity.position + hit_info.normal)
            Audio(sound_file_name="assets/Place.wav")
    if key == 'g':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Stone(position=hit_info.entity.position + hit_info.normal)
            Audio(sound_file_name="assets/Place.wav")
    if key == 'v':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Grass(position=hit_info.entity.position + hit_info.normal)
            Audio(sound_file_name="assets/Place.wav")
    if key == 'escape':
        quit()
        
    if key == 'left mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
        Audio(sound_file_name="assets/Break.wav")
        


app.run()
