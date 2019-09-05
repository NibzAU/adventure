### Map ######
"""
House - Downstair
			  [ Stairs ]
[   Garage	 ][  Hall  ][ Kitchen ]
[ Front door ][ Lounge ][ Dining  ]

House - Upstairs
			  [ bedroom 3][ Bedroom 2 ]
[  bathroom  ][         Hall          ][ Bedroom 1 ]
			  [  stairs  ]


"""

ZONENAME = ''
DESCRIPTION= 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
ITEMS = "items"

solved_places = { 'a1': False, 'a2': False, 'a3': False, 'a4': False,
				  'b1': False, 'b2': False, 'b3': False, 'b4': False,
				  'c1': False, 'c2': False, 'c3': False, 'c4': False,
				  'd1': False, 'd2': False, 'd3': False, 'd4': False
				}

zoneMap = {
	'a1': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"",
	    DOWN:"b1",
	    LEFT:"",
	    RIGHT:"a2",
        ITEMS: ['']
	},
	'a2': {
	    ZONENAME: 'Somewhere New',
	    DESCRIPTION: 'description',
	    EXAMINATION : 'examine',
		SOLVED: False,
		UP: "",
		DOWN: "b2",
		LEFT: "a1",
		RIGHT: "a3",
        ITEMS: ['']
	},
	'a3': {
		ZONENAME: '',
		DESCRIPTION: 'description',
		EXAMINATION : 'examine',
		SOLVED: False,
		UP: "",
		DOWN: "b3",
		LEFT: "a2",
		RIGHT: "a4",
        ITEMS: ['']
	},
	'a4': {
		ZONENAME: '',
		DESCRIPTION: 'description',
		EXAMINATION : 'examine',
		SOLVED: False,
		UP: "",
		DOWN: "b4",
		LEFT: "a3",
		RIGHT: "",
        ITEMS: ['']
	},
	'b1': {
		ZONENAME: '',
		DESCRIPTION: 'description',
		EXAMINATION : 'examine',
		SOLVED: False,
		UP: "a1",
		DOWN: "c1",
		LEFT: "",
		RIGHT: "b2",
        ITEMS: ['']
	},
	'b2': {
		ZONENAME: 'home',
		DESCRIPTION: 'this is your home',
		EXAMINATION: 'it looks like your home',
		SOLVED: False,
		UP: "a2",
		DOWN: "c2",
		LEFT: "b1",
		RIGHT: "b3",
        ITEMS: ['']
	},
	'b3': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"a3",
	    DOWN:"c3",
	    LEFT:"b2",
	    RIGHT:"b4",
        ITEMS: ['']
	},
	'b4': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"a4",
	    DOWN:"c4",
	    LEFT:"b3",
	    RIGHT:"",
        ITEMS: ['']
	},
	'c1': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"b1",
	    DOWN:"d1",
	    LEFT:"",
	    RIGHT:"c2",
        ITEMS: ['']
	},
	'c2': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"b2",
	    DOWN:"d2",
	    LEFT:"c1",
	    RIGHT:"c3",
        ITEMS: ['']
	},
	'c3': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"b3",
	    DOWN:"d3",
	    LEFT:"c2",
	    RIGHT:"c4",
        ITEMS: ['']
	},
	'c4': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"b4",
	    DOWN:"d4",
	    LEFT:"c3",
	    RIGHT:"",
        ITEMS: ['']
	},
	'd1': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"c1",
	    DOWN:"",
	    LEFT:"",
	    RIGHT:"d2",
        ITEMS: ['']
	},
	'd2': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"c2",
	    DOWN:"",
	    LEFT:"d1",
	    RIGHT:"d3",
        ITEMS: ['']
	},
	'd3': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"c3",
	    DOWN:"",
	    LEFT:"d2",
	    RIGHT:"d4",
        ITEMS: ['']
	},
	'd4': {
		ZONENAME: "",
		DESCRIPTION: "description",
	    EXAMINATION: "examine",
	    SOLVED: False,
	    UP:"c4",
	    DOWN:"",
	    LEFT:"d3",
	    RIGHT:"",
        ITEMS: ['']
	},
}
