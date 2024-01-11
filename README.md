ReadMe
Pokemon: Computer Chronicles - README
Overview of the Game:
Brief Introduction:
	•	Title: Pokemon:Computer Chronicles
	•	Genre: Top-down 2D Adventure
	•	Main Concept: The game incorporates coding languages as Pokémon-like entities using known materials in Burlington and a ICS Course Classroom. The primary objectives are navigating through maps, battling classmates using coding challenges, and reaching the final boss to become champion.
Strategy and Planning:
	•	Development Strategy: I opted for an iterative development approach. Initial stages focused on core mechanics, followed by the storyline, and then refining graphics and gameplay elements.
	•	Design Decisions:
	•	Top-Down View: A top-down perspective was chosen for easy navigation and exploration.
	•	Storyline Integration: Real classmates and teachers were integrated into the storyline for enhanced engagement.
	•	Feature Inclusions: Implemented a health system, and battle menu to add depth and strategy.
	•	
Challenges Faced:
	•	Map Rendering: Efficiently rendering maps using Pygame was challenging but rewarding. It took a long time to Configure needed tiles and to create the maps in addition to the base rendering code.
	•	Entity Interactions: Ensuring seamless interactions between player and NPCs. This caused issue due to spacing concerns and allowing the player to know where to go next.
	•	Debugging Tools and Techniques:
	•	Print Statements: Utilized print statements for tracking variables and debugging logic.
	•	ChatGPT: Leveraged ChatGPT for complex debugging scenarios.
	•	Tutorials & Forums: Engaged with Pygame tutorials and online forums for troubleshooting and guidance.
	•	Peer Help:I was not afraid to ask for help when stuck on bugs. Multiple people including Owen, Nitish, Nick and most importantly My teacher, Mr.bhinder helped when I experienced major issues I did not understand.
Code Showcase:
One aspect of the project I am particularly proud of is the Map Renderer. The following code snippet showcases the Map class responsible for loading, rendering, and camera positioning:
def render(self, screen, player):
        # Render the map on the screen
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                if tile not in map_tile_image:
                    x_pos = x_pos + 1
                    continue
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * SCALE - (self.camera[0] * SCALE), y_pos * SCALE - (self.camera[1] * SCALE), SCALE, SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        # draw all objects on map
        for object in self.objects:
            object.render(self.screen, self.camera)

The Map class encapsulates functionalities such as map loading, rendering, and camera adjustments, ensuring smooth and efficient gameplay. I am proud of it due to the time debugging Tile building etc.
Top Three TakeAways:
Pygame Usage: Mastered techniques for creating games using the Pygame library in python.
		Debugging Skills: Enhanced debugging proficiency using ChatGPT, print statements, and online resources.
		Iterative Development: Recognized the value of iterative development for incremental improvements and feature enhancements.

Analysis of Pygame as a Language:
Learning Curve:
	•	Pygame offers a moderate learning curve, supported by extensive documentation, tutorials, and a vibrant community. For those familiar with Python, the transition to Pygame is relatively smooth, facilitating quicker development cycles.
Functionalities:
	•	Pygame provides a comprehensive suite of functionalities crucial for 2D game development. This includes graphics rendering, sound management, input handling, and event management. The built-in modules and libraries simplify tasks such as sprite management, collision detection, and animation, accelerating development processes.
Limitations:
	•	Performance Optimization: One notable limitation of Pygame is its performance Issues. Often Pygame would crash in random scenarios. In addition Pyjama is based in the coding language of python. Which has a lot of limitations in game making and calling previous set of objects. Multiple times through my journey I have tried referencing variables but it would require the reformatting of a lot of code.
Overall Assessment:
	•	Despite its limitations, Pygame remains a valuable tool for aspiring game developers and hobbyists due to its ease of use, flexibility, and extensive documentation. However, for professional or commercial projects requiring advanced features, performance optimization, or cross-platform consistency, exploring alternative game engines or frameworks may be better.

Conclusion:
Creating “Pokemon”:Computer Chronichles was a eye-opening experience that honed my programming and game design skills.  I particularly enjoyed integrating real classmates and teachers into the storyline, enhancing engagement and personalization. This project has significantly improved my Python proficiency, problem-solving abilities, and understanding of game development principles. I look forward to applying these skills in future projects and endeavors.

Known Bugs/ Future additions:
	•	When defeating a NPC Trainer enter has to be pressed to continue the story
	•	Recent bug with opponent multiplayer returning as a non value instead of a value of 0
	•	Player can play through almost entire game without a Pokemon (no roadblock measures)
	•	Levels are not used or implemented in any way
	•	Hayden Highschool in alton village (map #04) has no building asset
	•	Classmate NPCs have no special dialogue/asset


