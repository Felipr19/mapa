import pygame
import sys


class Map():
    
    def __init__(self, map_template: list ,map_columns: int, map_rows: int):
        pygame.init()
        self.map_template = map_template
        self.screen = pygame.display.set_mode((map_columns*100, map_rows*100))
        
        pygame.display.set_caption("Drawing Multiple Blocks")

    
    def define_block_specifications(self, block_color: tuple, block_width: int, block_height: int): 
        self.block_color = block_color
        self.block_width = block_width
        self.block_height = block_height
        
        self.positions_of_blocks = list()
        
        for i, row in zip(self.map_template, range(len(self.map_template))):
            
            for reading_row, position_sub_element in zip(i, range(len(i))):
                
                if reading_row == 1:
                    self.positions_of_blocks.append((position_sub_element*100, row*100))
                    
                    
    def create_character(self):
        self.character_color = (255, 0, 0)
        self.character_initial_position = list()
        
        for i, row in zip(self.map_template, range(len(self.map_template))):
            for j, column in zip(i, range(len(i))):
                if j == 3:
                    self.character_initial_position.append((column*100, row*100))
                    self.character_initial_position = tuple(self.character_initial_position)
        
    def create_goal(self):
        self.goal_color = (0, 0, 0)
        self.goal_position = list()
        
        for i, row in zip(self.map_template, range(len(self.map_template))):
            for j, column in zip(i, range(len(i))):
                if j == 2:
                    self.goal_position.append((column*100, row*100))
                    self.goal_position = tuple(self.goal_position)
        
        

                    

    def display_map(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((255, 255, 255))

            for drawing in self.positions_of_blocks:
                pygame.draw.rect(self.screen, self.block_color, (drawing[0], drawing[1], self.block_width, self.block_height))
            

            pygame.draw.rect(self.screen, self.character_color, (self.character_initial_position[0][0], self.character_initial_position[0][1], self.block_height, self.block_width))
            pygame.draw.rect(self.screen, self.goal_color, (self.goal_position[0][0], self.goal_position[0][1], self.block_height, self.block_width))

            pygame.display.flip()
    
    
    
if __name__ == '__main__':
    map_template = [[1,2,1,1,1], [1,0,1,1,1], [1,0,1,0,1], [1,0,0,0,1], [1,3,1,1,1], [1,1,1,1,1]]
    test = Map(map_template, 5, 6)
    
    test.define_block_specifications((0,0,255), 100, 100)
    test.create_character()
    test.create_goal()
    
    test.display_map()

