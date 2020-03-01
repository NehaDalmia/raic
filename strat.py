import model


class MyStrategy:
    def __init__(self):
        pass

    def findnodes(self,game,arrx,arry):
    	nodes=[]
    	k=0
    	for j in range(0,29):
    		y=j
    		x=-1
    		
    		for i in range(1,39):
    			if game.level.tiles[i][j]==model.Tile.WALL and i!=38:
    				
    				if x==-1:
    					if game.level.tiles[i][j+1]!=model.Tile.WALL:
    						x=i
    						nodes.append([x,y+1])    				        
    						if game.level.tiles[i+1][j]==model.Tile.LADDER or game.level.tiles[i+1][j]==model.Tile.EMPTY or game.level.tiles[i+1][j+1]==model.Tile.WALL or game.level.tiles[i+1][j+1]==model.Tile.PLATFORM:
    							x=-1
		    		else:
		    				if game.level.tiles[i+1][j]==model.Tile.LADDER or game.level.tiles[i+1][j]==model.Tile.EMPTY or game.level.tiles[i+1][j+1]==model.Tile.WALL or game.level.tiles[i+1][j+1]==model.Tile.PLATFORM or game.level.tiles[i+1][j]==model.Tile.PLATFORM:
		    					x=i
		    					nodes.append([x,y+1])
		    					x=-1
		    	if game.level.tiles[i][j]==model.Tile.PLATFORM:
		    		if x==-1:
		    			if game.level.tiles[i][j+1]!=model.Tile.WALL:
		    				x=i
		    		if game.level.tiles[i][j+1]!=model.Tile.WALL:
		    			if game.level.tiles[i+1][j]==model.Tile.LADDER or game.level.tiles[i+1][j]==model.Tile.EMPTY or game.level.tiles[i+1][j+1]==model.Tile.WALL or game.level.tiles[i+1][j+1]==model.Tile.PLATFORM or game.level.tiles[i+1][j]==model.Tile.WALL:
		    				x+=i
		    				nodes.append([x/2,y+1])
		    				x=-1
    	return nodes

    def findtarget(self,game,max):
        for j in range(1,max):
            for i in range(1,20):
                if game.level.tiles[20-i][29-j]==model.Tile.WALL or game.level.tiles[20-i][29-j]==model.Tile.PLATFORM:
                    return(20-i,30-j)

    def checkifjumpvalid(self,game,position,target_pos):
        
        for i in range(int(position.y),int(position.y)+12):
            if game.level.tiles[int(position.x)][i]==model.Tile.WALL:
                return False
            elif game.level.tiles[int(position.x)][i]==model.Tile.PLATFORM: #or game.level.tiles[int(position.x)][i]==model.Tile.LADDER:
                return True
            #elif game.level.tiles[int(position.x+2)][i]==model.Tile.PLATFORM or game.level.tile[int(position.x+2)][i]==model.Tile.WALL or game.level.tile[int(position.x-2)][i]==model.Tile.PLATFORM or game.level.tile[int(position.x-2)][i]==model.Tile.WALL:
            elif position.x>2 and position.x<38: 
            #return True
                if game.level.tiles[int (position.x+1)][i]==model.Tile.WALL or game.level.tiles[int (position.x-1)][i]==model.Tile.WALL and game.level.tiles[int (position.x)][i]==model.Tile.EMPTY:
                    return True

        return False

    def checkwall(self,game,x1,x2,y):

    	for i in range( x1, x2):
    		if(y+13<30):
    			if game.level.tiles[i][ y]==model.Tile.WALL and game.level.tiles[ i][ y+13]==model.Tile.WALL:
    				return 1

    	return 0
    			


    def get_action(self, unit, game, debug):
        # Replace this code with your own
        def distance_sqr(a,b,c):
            return (a.x - b) ** 2 + (a.y - c) ** 2
        
        target_pos = unit.position
        nearest_enemy = min(
            filter(lambda u: u.player_id != unit.player_id, game.units),
            key=lambda u: distance_sqr(u.position, unit.position.x,unit.position.y),
            default=None)
        nearest_weapon = min(
            filter(lambda box: isinstance(
                box.item, model.Item.Weapon), game.loot_boxes),
            key=lambda box: distance_sqr(box.position, unit.position.x,unit.position.y),
            default=None)
        jump=target_pos.y > unit.position.y and  self.checkifjumpvalid(game,unit.position,target_pos)
        aim=model.Vec2Double(0,0)
        if nearest_enemy is not None:
            aim = model.Vec2Double(
                nearest_enemy.position.x - unit.position.x,
                nearest_enemy.position.y - unit.position.y)

        nearest_weapon.position.x, nearest_weapon.position.y=self.findtarget(game,29)
        if(unit.position.y>=nearest_weapon.position.y):
        	target_pos=unit.position
        	jump=False
        	return model.UnitAction(
            velocity=target_pos.x - unit.position.x,
            jump=jump,
            jump_down=False,
            aim=aim,
            shoot=True,
            reload=False,
            swap_weapon=False,
            plant_mine=False)
        """for t in range(2,5):
        	if unit.position.y+t<28:
        		if (game.level.tiles[int (unit.position.x)][int (unit.position.y+t)]==model.Tile.WALL or game.level.tiles[int (unit.position.x+0.1)][int (unit.position.y+t)]==model.Tile.WALL or game.level.tiles[int (unit.position.x-1)][int (unit.position.y+t)]==model.Tile.WALL)and game.level.tiles[int (unit.position.x)][int (unit.position.y-1)]!=model.Tile.EMPTY  :
        		

        			nearest_weapon.position.x=unit.position.x-2
        			nearest_weapon.position.y
        			target_pos=nearest_weapon.position
        			print("strt")
        			return model.UnitAction(
            		velocity=target_pos.x - unit.position.x,
            		jump=jump,
            		jump_down=False,
            		aim=aim,
            		shoot=True,
            		reload=False,
            		swap_weapon=False,
            		plant_mine=False)"""

        k=0
        #print(unit.position)
        arrx=[[]]
        arry=[]
        arrx=self.findnodes(game,arrx,arry)
        print(arrx)
        print("\n\n\n\n\n\n")
        mini =1000000
        k=0
        flag=1        
        for i in arrx:
        	if flag==1:
                      
        		if (i[1]>unit.position.y or i[1]>unit.position.y+0.005) and i[1]-unit.position.y<=12:
        			
        			
        		
        			for j in arrx:
        				#if(j[1]>i[1]):
        					#break
        				"""print(j[0],"   ",j[1])
        				print(game.level.tiles[int (unit.position.x)][j[1]-1]==model.Tile.WALL or game.level.tiles[int (unit.position.x+0.3)][j[1]-1]==model.Tile.WALL)
        				print("C1=",float (-0.2)<(j[0]-unit.position.x)<float (0.2))
        				print("C2=",int (j[1])!=int (unit.position.y))"""
        				#if( float (-0.2)<(j[0]-unit.position.x)<float (0.2) and int (j[1])!=int (unit.position.y) and (game.level.tiles[int (unit.position.x)][j[1]-1]==model.Tile.WALL or game.level.tiles[int (unit.position.x+0.3)][j[1]-1]==model.Tile.WALL)):
        					
        					#continue
        				if distance_sqr(unit.position,j[0],j[1])<mini and j[1]==i[1] and self.checkifjumpvalid(game,unit.position,target_pos) :
        					#print(self.checkifjumpvalid(game,unit.position,target_pos))
        					mini=distance_sqr(unit.position,j[0],j[1])        
        					nearest_weapon.position.x=j[0]
        					nearest_weapon.position.y=j[1]
        			break
        target_pos=nearest_weapon.position
        debug.draw(model.CustomData.Log("Target pos: {}".format(target_pos)))
        debug.draw(model.CustomData.Log("Unit pos: {}".format(unit.position)))
        target_pos=nearest_weapon.position
        mini=100000
        minx=-1
        miny=-1
        jumptest=0
        for z in range(0,39):
        	if game.level.tiles[z][int (unit.position.y)]==model.Tile.LADDER and game.level.tiles[z][int (unit.position.y+2)]!=model.Tile.LADDER :
        		print("No ladder")
        		break
        	elif game.level.tiles[z][int (unit.position.y)]==model.Tile.LADDER :
        		print("Ladder")
        		if distance_sqr(unit.position,z,unit.position.y)<mini:
        			mini=distance_sqr(unit.position,z,unit.position.y)
        			minx=z
        			miny=unit.position.y
        if(mini!=100000):
        	if self.checkwall(game,int (z),int (unit.position.x),int (unit.position.y+1))==0:
        				
        			print("Ladder")

        			nearest_weapon.position.x=(minx+0.5)if (minx>unit.position.x) else (minx)
        			nearest_weapon.position.y=miny+2
        			target_pos=nearest_weapon.position
        			if(-0.1<target_pos.x-unit.position.x<0.1):
        				
        				jumptest=1
        aim=model.Vec2Double(0,0)
        if nearest_enemy is not None:
            aim = model.Vec2Double(
                nearest_enemy.position.x - unit.position.x,
                nearest_enemy.position.y - unit.position.y)
        jump=target_pos.y > unit.position.y and  self.checkifjumpvalid(game,unit.position,target_pos)
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x+1)][int(unit.position.y)]==model.Tile.WALL:
        	jump=True
        elif target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x-1)][int(unit.position.y)]==model.Tile.WALL:
        	jump=True
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x+1)][int(unit.position.y-1)]==model.Tile.EMPTY:
        	jump=True
        elif target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x-1)][int(unit.position.y-1)]==model.Tile.EMPTY:
        	jump=True
        if(jumptest==1):
        	jump=True
        
        




        return model.UnitAction(
            velocity=(target_pos.x - unit.position.x),
            jump=jump,
            jump_down=False,
            aim=aim,
            shoot=True,
            reload=False,
            swap_weapon=False,
            plant_mine=False)
       
       