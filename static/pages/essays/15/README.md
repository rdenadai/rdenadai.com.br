# Self-organizing map (Kohonen Map)

### Description

The Self-organizing map (also know as Kohonen Map) were thought by Teuvo Kohonen in the early 90's. The idea is to use a type of "Neural Network" to generate a small latent space (dimension) using a unsupervised approach.

Given this, the overall idea is that the map is built using units ("neurons") that are placed in the latent space of the data, than, for each iteration, some units will get closer to the nearest data point and units that are closer to that one will get a little closer.

Image bellow demonstrate the SOM map (SizeX by Sizey) and it's mapping using weight w<sub>ij</sub> given the points in their latent space given by x<sub>n</sub>.

![SOM application][1]

### Algorithm

At a higher level the algorithm work following the steps:

- Initialize a 2D map
- for each epoch do:
  - Randomly select a sample
  - Calculate and get the BMU (Best match unit)
  - Given the BMU calculate the neighbors
  - Update the learning rate

If you known Neural Networks and their process, in a way some of the steps are the same (just a few of them of course).

#### **Code Example**

<pre><code class="language-python">

</code></pre>

[My SOM Implementation][2]

### Libraries

- [**Minisom**][3] : "_MiniSom is a minimalistic implementation of the Self Organizing Maps._"

- [**SOMPY**][4] : "_A Python Library for Self Organizing Map (SOM)_"

### Papers

- [The self-organizing map][5]
- [Essentials of the self-organizing map][6]

### Links

- [Wikipedia : Self-organizing map][7]
- [Introduction to Self-Organizing Maps (SOMs)][8]

[1]: /static/pages/essays/14/kohonen.gif
[2]: https://github.com/rdenadai/AI-Study-Notebooks/blob/master/code/som/som.py
[3]: https://github.com/JustGlowing/minisom
[4]: https://github.com/sevamoo/SOMPY
[5]: https://ieeexplore.ieee.org/abstract/document/58325
[6]: https://www.sciencedirect.com/science/article/abs/pii/S0893608012002596
[7]: https://en.wikipedia.org/wiki/Self-organizing_map
[8]: https://heartbeat.fritz.ai/introduction-to-self-organizing-maps-soms-98e88b568f5d
