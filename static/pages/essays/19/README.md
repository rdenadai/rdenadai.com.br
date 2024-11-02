# Exploring Fuzzy Matching

Recently, I was helping implement a feature on the [Marmite](https://github.com/rochacbruno/marmite) project, which was adding a static search into the project. The idea of course, allow users to search content inside their markdown files.

For this the author of the Marmite project suggested the usage of [Fuse.js](https://www.fusejs.io/). On their website, they describe themselves as "Powerful, lightweight fuzzy-search library, with zero dependencies".

The library itself was very easy to use, and very straightforward to add to the project, but after that it got me thinking about how fuzzy matching works.

In past years I have worked in another project where we had the need to match names of researchers from different sources (as SciELO, PubMed, etc). For this, at the time, we used the [Jaro-Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) algorithm, and it worked well (the idea of this algorithm is to measure the similarity between strings, specially if the have a "common prefix").
