# textualheatmap

**Create interactive textual heatmaps for Jupiter notebooks.**

There is a framework agnostic interface `lrcurve.PlotLearningCurve`
that works well with PyTorch and Tensorflow and a keras wrapper
`lrcurve.KerasLearningCurve` that uses the keras callback interface.

`textualheatmap` works with python 3.6 or newer and is distributed under the
MIT license.

![Gif of textualheatmap](gifs/readme_header.gif)

## Install

```bash
pip install -U textualheatmap
```

## API

* [`textualheatmap.TextualHeatmap`](lrcurve/textual_heatmap.py)

## Example
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AndreasMadsen/python-textualheatmap/blob/master/notebooks/general_example.ipynb)

```python
from textualheatmap import TextualHeatmap

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
```

![Gif of learning-curve for keras example](gifs/general_example.gif)

## Citation

If you use this in a publication, please cite my [Distill publication](https://distill.pub/2019/memorization-in-rnns/) where I first demonstrated this visualization method.

```bib
@article{madsen2019visualizing,
  author = {Madsen, Andreas},
  title = {Visualizing memorization in RNNs},
  journal = {Distill},
  year = {2019},
  note = {https://distill.pub/2019/memorization-in-rnns},
  doi = {10.23915/distill.00016}
}
```

## Sponsor

Sponsored by <a href="https://www.nearform.com/research/">NearForm Research</a>.
