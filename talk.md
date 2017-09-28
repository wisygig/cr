# pose problem
* historical precedence
    * 'collection of rules which provide tools for running a variety of social, asymmetric, scenerio-based games'
    * war game background -> simulationist tendencies
    * strong tradition of procedural generation
* srd-ogl data ->
    * semi-structured text
    * particular target, which is a heuristic
    * published a heuristic, but did not release (hence, proprietary)

# work in progress - report
* problems w/ data set
    * entirely human generated; labels may not be deterministic (how should we deal with this?)
        * cr should be distributional, use 'ordinal classification'
    * target values are part of a heuristic model
* exploratory analysis
    * useful for identifying features with strong correlations

# predictive models
* initial models
    * goal is to provide simple, explanatory models (bayesian priors?)
* feature extraction
    * use initial models to identify which examples poorly fit, clustering to prioritize feature extraction
* other methods
    * rnns - with a tigher bottleneck!
    * sentiment analysis
    * pre-trained network + embedding of corpus specific words
    * other neural networks
* deep-dreaming
    * application to perturbative generation

# future work
* interpreting 
* try using generative adversarial networks (GANs), due to embedding properties?

# notes
* how does `size` correspond to language used in `actions`?
* different use cases should be considered -> generating semi-structured text
* from other representations (power ratings, prose), generate stat blocks with target levels.


