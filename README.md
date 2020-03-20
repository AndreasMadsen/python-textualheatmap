# textualheatmap

**Create interactive textual heatmaps for Jupiter notebooks.**

There is a framework agnostic interface `lrcurve.PlotLearningCurve`
that works well with PyTorch and Tensorflow and a keras wrapper
`lrcurve.KerasLearningCurve` that uses the keras callback interface.

`textualheatmap` works with python 3.6 or newer and is distributed under the
MIT license.

![Gif of textualheatmap](gifs/show_meta.gif)

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

data = [[
    # GRU data
    {"token":" ",
     "meta":["the","one","of"],
     "heat":[1,0,0,0,0,0,0,0,0]},
    {"token":"c",
     "meta":["can","called","century"],
     "heat":[1,0.22,0,0,0,0,0,0,0]},
    {"token":"o",
     "meta":["country","could","company"],
     "heat":[0.57,0.059,1,0,0,0,0,0,0]},
    {"token":"n",
     "meta":["control","considered","construction"],
     "heat":[1,0.20,0.11,0.84,0,0,0,0,0]},
    {"token":"t",
     "meta":["control","continued","continental"],
     "heat":[0.27,0.17,0.052,0.44,1,0,0,0,0]},
    {"token":"e",
     "meta":["context","content","contested"],
     "heat":[0.17,0.039,0.034,0.22,1,0.53,0,0,0]},
    {"token":"x",
     "meta":["context","contexts","contemporary"],
     "heat":[0.17,0.0044,0.021,0.17,1,0.90,0.48,0,0]},
    {"token":"t",
     "meta":["context","contexts","contentious"],
     "heat":[0.14,0.011,0.034,0.14,0.68,1,0.80,0.86,0]},
    {"token":" ",
     "meta":["of","and","the"],
     "heat":[0.014,0.0063,0.0044,0.011,0.034,0.10,0.32,0.28,1]},
    # ...
],[
    # LSTM data
    # ...
]]

heatmap = TextualHeatmap(
    width = 600,
    show_meta = True,
    facet_titles = ['GRU', 'LSTM']
)
# Set data and render plot, this can be called again to replace
# the data.
heatmap.set_data(data)
# Focus on the token with the given index. Especially useful when
# `interactive=False` is used in `TextualHeatmap`.
heatmap.highlight(159)
```

![Gif of learning-curve for keras example](gifs/show_meta.gif)

```python
heatmap = TextualHeatmap(
    show_meta = False,
    facet_titles = ['LSTM', 'GRU'],
    rotate_facet_titles = True
)
heatmap.set_data(data)
heatmap.highlight(159)
```

![Gif of learning-curve for keras example](gifs/no_meta_and_rotated.gif)

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
