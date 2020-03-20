from nose.tools import *

from textualheatmap.textual_heatmap import TextualHeatmap

class DisplayHandle:
    def __init__(self, display_objects):
        self.display_objects = display_objects

    def update(self, obj):
        self.display_objects.append(obj)

def display_replacer(display_objects):
    def display(obj, display_id=None):
        display_objects.append(obj)
        return DisplayHandle(display_objects)
    return display

def test_readme_example():
    # Unfortunetly the notebooks are really the best way to test if
    # things are working.
    display_objects = []

    heatmap = TextualHeatmap(
        show_meta = True,
        facet_titles = ['LSTM', 'GRU'],
        display_fn=display_replacer(display_objects)
    )
    heatmap.set_data([[], []])
    heatmap.set_data([
        [{
            "token": 'a',
            "meta": ['and', 'africa', 'america'],
            "heat": [1, 0, 0]
        }, {
            "token": 'n',
            "meta": ['and', 'anecdote', 'antelope'],
            "heat": [0.3, 0.7, 0]
        }, {
            "token": 'd',
            "meta": ['and', 'andante', 'andosol'],
            "heat": [0.2, 0.3, 0.5]
        }],
        [{
            "token": 'a',
            "meta": ['and', 'africa', 'america'],
            "heat": [1, 0, 0]
        }, {
            "token": 'n',
            "meta": ['and', 'anecdote', 'antelope'],
            "heat": [0.1, 0.9, 0]
        }, {
            "token": 'd',
            "meta": ['and', 'andante', 'andosol'],
            "heat": [0.1, 0.1, 0.8]
        }]
    ])
    heatmap.highlight(0)
    heatmap.highlight(1)

    assert_equal(len(display_objects), 7)

@raises(ValueError)
def test_width_is_string():
    TextualHeatmap(
        width = 'string',
        display_fn=display_replacer([])
    )

@raises(ValueError)
def test_facet_titles_is_not_list():
    TextualHeatmap(
        facet_titles='string',
        display_fn=display_replacer([])
    )

@raises(ValueError)
def test_TextualHeatmap_has_non_string_item():
    TextualHeatmap(
        facet_titles=[1, 'string'],
        display_fn=display_replacer([])
    )

@raises(ValueError)
def test_rotate_facet_titles_is_non_boolean():
    TextualHeatmap(
        rotate_facet_titles='string',
        display_fn=display_replacer([])
    )

@raises(ValueError)
def test_width_is_not_integer():
    TextualHeatmap(
        width='string',
        display_fn=display_replacer([])
    )

@raises(ValueError)
def test_interactive_is_not_boolean():
    TextualHeatmap(
        interactive='string',
        display_fn=display_replacer([])
    )
