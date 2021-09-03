import keyboard
import socket
import threading

class game :
    
    mainServers = []
    def animals() :
        
        cow = { "name": "", "sound": {  }, "animations": { "walking": "", "running": "" } }
        mushroomcow = { "name": "", "sound": {  }, "animations": { "walking": "", "running": "" } }
        pig = { "name": "", "sound": {  }, "animations": { "walking": "", "running": "" } }
        
    def animations() :
        
        def forward() :
            
            
            
        def backward() :
            
            
            
        def left() :
            
            
            
        def right() :
            
            
            
        def shift() :
            
            
            
        def jump() :
            
            
            
        def punch() :
            
            
            
        def useTool(toolId, usedButton) :
            
            self.usedButton = usedButton
            if toolId == 1 :
                
                """ if a sword is used, the sword anim is started """
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is clicked, the attack anim is used """
                    player.playerDatas.tool.ZRotation = 45
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is clicked, the defense anim is used """
                    player.playerDatas.tool.XRotation = 45
                    
                else :
                    
                    print ("Error during the usage of the sword !")
                    
            if toolId == 2 :
                
                """ if a pickaxe is used, the pickaxe anim is started """
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is clicked, the block destroying anim is used """
                    player.playerDatas.tool.ZRotation = 45
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is clicked, the defense anim is used """
                    player.playerDatas.tool.XRotation = 45
                    
                else :
                    
                    print ("Error during the usage of the pickaxe !")
                    
            if toolId == 3 :
                
                """ if an axe is used, the axe anim is started """
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is clicked, the destroying block anim is used """
                    player.playerDatas.tool.ZRotation = 45
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is clicked, the defense anim is used """
                    player.playerDatas.tool.XRotation = 45
                    
                else :
                    
                    print ("Error during the usage of the Axe !")
                    
            if toolId == 4 :
                
                """ if a shovel is used, the shovel anim is started """
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is clicked, the destroying block anim is used """
                    player.playerDatas.tool.ZRotation = 45
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is clicked, the defense anim is used """
                    player.playerDatas.tool.XRotation = 45
                    
                else :
                    
                    print ("Error during the usage of the shovel !")
                    
            if toolId == 5 :
                
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is clicked, the attack anim of the axe is used """
                    player.playerDatas.tool.ZRotation = 45
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is clicked, the defense anim of the axe is used """
                    player.playerDatas.tool.XRotation = 45
                    
                else :
                    
                    print ("Error during the usage of the hoe !")
                    
    def blocks() :
        
        dirtBlock = { "name": "dirt", "id": 0, "images": { "topImage": { "img": "", "size": { "x": 64, "y": 64 } }, "bottomImage": { "img": "", "size": { "x": 64, "y": 64 } }, "forwardImage": { "img": "", "size": { "x": 64, "y": 64 } }, "backImage": { "img": "", "size": { "x": 64, "y": 64 } }, "leftImage": { "img": "", "size": {"x": 64, "y": 64} }, "rightImage": { "img": "", "size": { "x": 64, "y": 64 } } } }
        cobbleBlock = { "name": "cobble", "id": "", "images": { "topImage": { "img": "", "size": { "x": 64, "y": "64" } }, "bottomImage": { "img": "", "size": { "x": 64, "y": 64 } }, "forwardImage": { "img": "", "size": { "x": 64, "y": 64 } }, "backImage": { "img": "", "size": { "x": 64, "y": 64 } }, "leftImage": { "img": "", "size": {"x": 64, "y": 64} }, "rightImage": { "img": "", "size": { "x": 64, "y": 64 } } } }
        cobblestoneBlock = { "name": "cobble stone", "id": "", "images": { "topImage": { "img": "", "size": { "x": 64, "y": 64 } }, "bottomImage": { "img": "", "size": { "x": 64, "y": 64 } }, "forwardImage": { "img": "", "size": { "x": 64, "y": 64 } }, "backImage": { "img": "", "size": { "x": 64, "y": 64 } }, "leftImage": { "img": "", "size": {"x": 64, "y": 64}}, "rightImage": { "img": "", "size": { "x": 64, "y": 64 } } } }
        lavaBlock = { "name": "Lava", "id": "", "images": {  } }
        lightBlock = { "name": "light", "id": "", "images": { "topImage": { "img": "", "size": { "x": 64, "y": 64 } }, "bottomImage": { "img": "", "size": { "x": 64, "y": 64 } }, "forwardImage": { "img": "", "size": { "x": 64, "y": 64 } }, "backImage": { "img": "", "size": { "x": 64, "y": 64 } }, "leftImage": { "img": "", "size": {"x": 64, "y": 64} } }, "rightImage": { "img": "", "size": { "x": 64, "y": 64 } } } }
        milkBlock = { "name": "Milk", "id": "", "images": {  } }
        spongeBlock = { "name": "Sponge", "id": "", "images": {  } }
        spongeWetBlock = { "name": "Wet sponge", "id": "", "images": {  } }
        waterBlock = { "name": "water", "id": "", "images": { "topImage": { "img": "", "size": { "x": 64, "y": 64 } }, "bottomImage": { "img": "", "size": { "x": 64, "y": 64 } }, "forwardImage": { "img": "", "size": { "x": 64, "y": 64 } }, "backImage": { "img": "", "size": { "x": 64, "y": 64 } }, "leftImage": { "img": "", "size": { "x": 64, "y": 64 } }, "rightImage": { "img": "", "size": { "x": 64, "y": 64 } } } }
        
    def chat() :
        
        chatBackground = { "color": "", "size": { "x": "", "y": "" } }
        chatText = { "color": "", "size": { "x": "", "y": "" } }
        
    def mobs() :
        
        creeper = { "name": "Creeper", "id": "", "explosion": { "radius": 3, "animation": "animations.explosions.creeper" }, "xp": 10 }
        zombie = { "name": "Zombie", "id": "", "hurting": { "radius": 1, "animation": "animations.hurting.zombie" }, "xp": 10 }
        
    def tools() :
        
        swords = { "vanillaSwords": { 1: { "name": "Wood sword", "images": {  }, "model": "" }, 2: { "name": "Cobble sword", "images": {  }, "model": "" }, 3: { "name": "Iron sword", "images": {  }, "model": "" }, 4: { "name": "Gold sword", "images": {  }, "model": "" }, 5: { "name": "Diamond sword", "images": {  }, "model": "" }, 6: { "name": "Emerald sword", "images": {  }, "model": "" }, 7: { "name": "Netherite sword", "images": {  }, "model": "" }, 8: { "name": "Obsidian sword", "images": {  }, "model": "" } }, "moddedSwords": {  } }
        pickaxes = { "vanillaPickaxes": { 1: { "name": "Wood pickaxe", "images": "", "model": "" }, 2: { "name": "Cobble pickaxe", "images": "", "model": "" }, 3: { "name": "Iron pickaxe", "images": "", "model": "" }, 4: {  }, 5: {  }, 6: {  }, 7: {  }, 8: {  } } }
        axes = {  }
        shovels = {  }
        hoes = {  }
        
    def gui() :
        
        
class player :
    
    def playerDatas() :
        
        playerXCord = 2
        playerYCord = 0
        playerZCord = 0
        playerCameraXCord = 2
        playerCameraYCord = 0
        playerCameraZCord = 0
        def playerSettings() :
            
            playerForwardButton = "z" AND "Z"
            playerLeftButton = "q" AND "Q"
            playerRightButton = "d" AND "D"
            playerBackButton = "s" AND "S"
            playerShiftButton = ""
            
        def tool() :
            
            toolId = 0
            XPos = 0
            YPos = 0
            ZPos = 0
            XRotation = 0
            YRotation = 0
            ZRotation = 0
            
    def move(key) :
        
        if key == playerDatas.playerSettings.playerForwardButton :
            
            playerDatas.ZPos += 0.5
            
        if key == playerDatas.playerSettings.playerBackButton :
            
            playerDatas.ZPos -= 0.5
            
        if key == playerDatas.playerSettings.playerLeftButton :
            
            playerDatas.XPos -= 0.5
            
        if key == playerDatas.playerSettings.playerRightButton :
            
            playerDatas.XPos += 0.5
            
        if key == playerDatas.playerSettings.playerShiftButton :
            
            game.animations.shift
            playerDatas.playerCameraXCord = playerXCord -0.5
            
class internet :
    
    def internetDatas() :
        
        internetClientReady = 0
        
    def internetClient() :
        
        icsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        icsocket.connect(mainServers, 15000)
        while True :
            
            internetDatas.internetClientReady = 1
            
    def internetServer() :
        
        issocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        issocket.listen(gethostbyname(gethost), 15001)
