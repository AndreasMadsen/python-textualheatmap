;(function () {
    'use strict';

    function viridisSubset(ratio) {
        const colormap = [
            '#365d8d', '#355e8d', '#355f8d', '#34608d', '#34618d',
            '#33628d', '#33638d', '#32648e', '#32658e', '#31668e',
            '#31678e', '#31688e', '#30698e', '#306a8e', '#2f6b8e',
            '#2f6c8e', '#2e6d8e', '#2e6e8e', '#2e6f8e', '#2d708e',
            '#2d718e', '#2c718e', '#2c728e', '#2c738e', '#2b748e',
            '#2b758e', '#2a768e', '#2a778e', '#2a788e', '#29798e',
            '#297a8e', '#297b8e', '#287c8e', '#287d8e', '#277e8e',
            '#277f8e', '#27808e', '#26818e', '#26828e', '#26828e',
            '#25838e', '#25848e', '#25858e', '#24868e', '#24878e',
            '#23888e', '#23898e', '#238a8d', '#228b8d', '#228c8d',
            '#228d8d', '#218e8d', '#218f8d', '#21908d', '#21918c',
            '#20928c', '#20928c', '#20938c', '#1f948c', '#1f958b',
            '#1f968b', '#1f978b', '#1f988b', '#1f998a', '#1f9a8a',
            '#1e9b8a', '#1e9c89', '#1e9d89', '#1f9e89', '#1f9f88',
            '#1fa088', '#1fa188', '#1fa187', '#1fa287', '#20a386',
            '#20a486', '#21a585', '#21a685', '#22a785', '#22a884',
            '#23a983', '#24aa83', '#25ab82', '#25ac82', '#26ad81',
            '#27ad81', '#28ae80', '#29af7f', '#2ab07f', '#2cb17e',
            '#2db27d', '#2eb37c', '#2fb47c', '#31b57b', '#32b67a',
            '#34b679', '#35b779'
        ];
        const n = colormap.length - 1;
        return colormap[Math.max(0, Math.min(n, Math.floor(ratio * n)))];
    }

    class TextualHeatmap {
        constructor(settings) {
            this.container = document.getElementById(settings.id);
            this.container.style.width = settings.width + 'px';
            this.facets = settings.facetTitles
                .map((facetName) => new TextualHeatmapFacet(settings, this.container, facetName));

            for (let i = 0; i < this.facets.length; i++) {
                this.facets[i].onmouseover = this.highlight.bind(this);
            }
        }

        setData(data) {
            for (let i = 0; i < this.facets.length; i++) {
                this.facets[i].setData(data[i]);
            }
        }

        highlight(index) {
            for (let i = 0; i < this.facets.length; i++) {
                this.facets[i].highlight(index);
            }
        }
    }

    class TextualHeatmapFacet {
        constructor(settings, root, facetName) {
            this.settings = settings;
            this.highlightIndex = null;
            this.data = [];
            this.root = root;
            this.onmouseover = null;

            this.facet = document.createElement('div');
            this.facet.classList.add('facet');
            this.facet.classList.toggle('hide-meta-content', !settings.showMeta);
            this.facet.classList.toggle('rotate-facet-title', settings.rotateFacetTitles);
            this.root.appendChild(this.facet);

            this.meta = document.createElement('div');
            this.meta.classList.add('meta-content');
            this.facet.appendChild(this.meta);

            const item = document.createElement('div');
            item.classList.add('meta-content-item');
            this.meta.appendChild(item);

            this.content = document.createElement('div');
            this.content.classList.add('token-content');
            this.facet.appendChild(this.content);

            this.title = document.createElement('div');
            this.title.classList.add('facet-title');
            const titleSpan = document.createElement('span');
            titleSpan.appendChild(document.createTextNode(facetName));
            this.title.appendChild(titleSpan);
            this.facet.appendChild(this.title);
        }

        setData(data) {
            this.data = data;

            while (this.content.childNodes.length > 0) {
                this.content.removeChild(this.content.firstChild);
            }

            for (let i = 0; i < data.length; i++) {
                const tokenNode = document.createElement('span');
                tokenNode.appendChild(document.createTextNode(data[i].token));
                if (this.settings.interactive) {
                    tokenNode.addEventListener('mouseover', () => this.onmouseover(i), false);
                }
                this.content.appendChild(tokenNode);
            }

            if (this.highlightIndex !== null) {
                this.highlight(this.highlightIndex);
            }
        }

        highlight(index) {
            this.highlightIndex = index;

            for (let i = 0; i < this.data.length; i++) {
                this.content.childNodes[i].style.backgroundColor = viridisSubset(this.data[index].heat[i]);
                this.content.childNodes[i].classList.toggle('selected', i === index);
            }

            if (this.settings.showMeta) {
                while (this.meta.childNodes.length > 0) {
                    this.meta.removeChild(this.meta.firstChild);
                }

                for (let i = 0; i < this.data[index].meta.length; i++) {
                    const item = document.createElement('div');
                    item.classList.add('meta-content-item');
                    item.appendChild(document.createTextNode(this.data[index].meta[i]));
                    this.meta.appendChild(item);
                }

                if (this.data[index].meta.length === 0) {
                    const item = document.createElement('div');
                    item.classList.add('meta-content-item');
                    this.meta.appendChild(item);
                }
            }
        }
    }

    window.setupTextualHeatmap = function (settings) {
        document.getElementById(settings.id).instance = new TextualHeatmap(settings);
    };

    window.setDataTextualHeatmap = function (settings, data) {
        document.getElementById(settings.id).instance.setData(data);
    };

    window.highlightTextualHeatmap = function (settings, index) {
        document.getElementById(settings.id).instance.highlight(index);
    };
})();