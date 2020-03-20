
import uuid
import json
import os.path as path
import IPython

web_assets_dir = path.join(path.dirname(path.realpath(__file__)), 'web_assets')

class TextualHeatmap:
    """Create interactive textual heatmaps for Jupiter notebooks.

    This is useful for PyTorch or pure TensorFlow. You should properly use
    `KerasLearningCurve` if you use keras.

    Line description: dict with the properties `name` and `color`.
    Axis description:

    Example:
        heatmap = TextualHeatmap(
            show_meta = True,
            facet_titles = ['LSTM', 'GRU']
        )
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
        heatmap.highlight(1)

    Arguments:
        show_meta: The meta texts on top of each facet (Default: False).
        facet_titles: The title on each facet (Default: ['Heatmap']).
        rotate_facet_titles: If true, the facet titles will be rotated 90deg (Default: False).
        width: The width of the heatmap (Default: 600).
        interactive: Should the heatmap be interactive on mouseover. (Default: True)
        debug: Depending on the notebook, a JavaScript evaluation does not provide
            a stack trace in the developer console. Setting this to `true` works
            around that by injecting `<script>` tags instead.
    """
    def __init__(self,
                 show_meta = False,
                 facet_titles = ['Heatmap'],
                 rotate_facet_titles = False,
                 width = 600,
                 interactive = True,
                 display_fn=IPython.display.display,
                 debug=False
    ):
        if not isinstance(width, int) or width <= 0:
            raise ValueError(f'width must be a positive number, was {width}')

        if not isinstance(show_meta, bool):
            raise ValueError('show_meta must be a boolean')

        if not isinstance(interactive, bool):
            raise ValueError('interactive must be a boolean')

        if not isinstance(facet_titles, list):
            raise ValueError('facet_titles must be a list')
        for facet_title_i, facet_title in enumerate(facet_titles):
            if not isinstance(facet_title, str):
                raise ValueError(f'facet_title["{facet_title_i}"] must a string')

        if not isinstance(rotate_facet_titles, bool):
            raise ValueError('rotate_facet_titles must be a boolean')

        # Store settings
        self._debug = debug
        self._display = display_fn
        self._settings = {
            'id': str(uuid.uuid4()),
            'width': width,
            'showMeta': show_meta,
            'facetTitles': facet_titles,
            'rotateFacetTitles': rotate_facet_titles,
            'interactive': interactive
        }

        # Prepear data containers
        self._data = []
        self._display(self._create_inital_html())
        self._data_element = self._display(
            IPython.display.Javascript('void(0);'),
            display_id=True
        )
        self._highlight_element = self._display(
            IPython.display.Javascript('void(0);'),
            display_id=True
        )

    def _create_inital_html(self):
        with open(path.join(web_assets_dir, 'textual_heatmap.css')) as css_fp, \
             open(path.join(web_assets_dir, 'textual_heatmap.js')) as js_fp:
            return IPython.display.HTML(
                f'<style>{css_fp.read()}</style>'
                f'<script>{js_fp.read()}</script>'
                f'<div id="{self._settings["id"]}" class="textual-heatmap"></div>'
                f'<script>'
                f'  window.setupTextualHeatmap({json.dumps(self._settings)});'
                f'</script>'
            )

    def set_data(self, data):
        """Sets the data and render the heatmap.

        `data` is a list of `FacetData`. Each `FacetData` is a
        list of `TokenData`.

            TokenData = {"token": str, "meta": List[str], "heat": List[float]}

        Arguments:
            data: List[List[TokenData]] - Heatmap data.
        """
        disp = IPython.display.HTML(
            f'<script>'
            f'  window.setDataTextualHeatmap({json.dumps(self._settings)}, {json.dumps(data)});'
            f'</script>'
        )
        self._data_element.update(disp)

    def highlight(self, index):
        """Select a token index to be highlighted on the heatmap.

        This will affect all facets in the heatmap.

        Arguments:
            index: integer - The token index to highlight.
        """
        disp = IPython.display.HTML(
            f'<script>'
            f'  window.highlightTextualHeatmap({json.dumps(self._settings)}, {index});'
            f'</script>'
        )
        self._highlight_element.update(disp)
