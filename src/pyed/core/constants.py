line_types = ["line", "dashed", "dotted", "dashed_dotted"]
arrow_types = ["none", "standard", "white_delta", "diamond", "white_diamond", "short",
               "plain", "concave", "convex", "circle", "transparent_circle", "dash",
               "skewed_dash", "t_shape", "crows_foot_one_mandatory",
               "crows_foot_many_mandatory", "crows_foot_many_optional", "crows_foot_one",
               "crows_foot_many", "crows_foot_optional"]
font_styles = ["plain", "bold", "italic", "bolditalic"]
horizontal_alignments = ['left', 'center', 'right']
vertical_alignments = ['top', 'center', 'bottom']
autoSizePolicy_values = ["node_width", "node_size", "node_height", "content"]

# For each placement model, all valid params
valid_model_params = {
    "internal": ["t", "b", "c", "l", "r", "tl", "tr", "bl", "br"],
    "corners": ["nw", "ne", "sw", "se"],
    "sandwich": ["n", "s"],
    "sides": ["n", "e", "s", "w"],
    "eight_pos": ["n", "e", "s", "w", "nw", "ne", "sw", "se"],
    "custom": [None],
    "two_pos": ["head", "tail"],
    "centered": ["center"],
    "six_pos": ["shead", "thead", "head", "stail", "ttail", "tail"],
    "three_center": ["center", "scentr", "tcentr"],
    "center_slider": None,
    "side_slider": None,
    "free": ["anywhere"],
}
