

AUGMENTATION_FLIPH = "flipH"
AUGMENTATION_FLIPV = "flipV"
AUGMENTATION_ROTATION = "rot"
AUGMENTATION_SCALE = "scale"
AUGMENTATION_RANDOM = "random"
AUGMENTATION_NONE = "none"




AUGMENTATION_CHOICES = [
                AUGMENTATION_NONE,
                AUGMENTATION_FLIPH,
                AUGMENTATION_FLIPV,
                AUGMENTATION_ROTATION,
                AUGMENTATION_SCALE,
                AUGMENTATION_RANDOM
                ]


LAYER_BACKGROUND = "BG"
LAYER_PARATEXT= "Para"
LAYER_DECORATION = "Deco"
LAYER_TEXT = "Text"
LAYER_TITLE = "Title"
LAYER_HEADINGS = "Head"

LAYER_CHOICES = [
                LAYER_BACKGROUND,
                LAYER_PARATEXT,
                LAYER_DECORATION,
                LAYER_TEXT,
                LAYER_TITLE,
                LAYER_HEADINGS
]


DICT_COLORS_GT = {
                LAYER_BACKGROUND    : (0,0,0),      # Black
                LAYER_PARATEXT      : (255,255,0),  # Yellow
                LAYER_DECORATION    : (0,255,255),  # Cyan
                LAYER_TEXT          : (255,0,255),  # Magenta
                LAYER_TITLE         : (255,0,0),    # Red
                LAYER_HEADINGS      : (0,255,0)     # Lime
}

kPIXEL_VALUE_FOR_MASKING = -1
kNUMBER_CHANNELS = 3


KEY_RESULT="result"
