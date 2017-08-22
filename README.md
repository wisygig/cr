# Challenge Rating Calculator

Work in progress, for consideration as a capstone project for the Springboard Data Science workshop.

## Installation

    git clone https://github.com/wisygig/cr.git
    cd cr
    python3 -m venv .
    source bin/activate
    pip install -r requirements.txt

## Motivating Problem

In 2000, Wizards of the Coast (WOTC) released portions of the [Dungeons and Dragons](http://dnd.wizards.com/) ruleset under an open source licence, the [open gaming licence (OGL)](https://en.wikipedia.org/wiki/Open_Game_License).
With the release of the 5th edition of the game's rule set, they have continued this tradition.

The most recent version of the OGL released a [set of rules](http://dnd.wizards.com/articles/features/systems-reference-document-srd) for running and playing the game.
Along with rules for creating player characters, a bestiary of example monsters was also published.
For each monster, a Challenge Rating (CR) is included, as well as huristics to evaluate how difficult an encounter with a group of monsters would be.
However, rules for evaluating the CR of a monster from a description of the monster's game features are omitted.

This submission poses the following questions.
* Can we compute the challenge rating of an creature purely from OGL released examples?
* Given a partially completed entry, can we propose other completions, with the intent of preserving a similarity clustering.

## Client
* Principle client would be hobbyists looking to craft new monsters, as well as independent scenerio authors looking to publish content under the OGL.

## Data sources
* [5e SRD](http://dnd.wizards.com/articles/features/systems-reference-document-srd)
* The json file [5e SRD monsters.json](https://dl.dropboxusercontent.com/s/iwz112i0bxp2n4a/5e-SRD-Monsters.json) is a formatted verison of the beastiary provided by the SRD, and is due to redditor [/u/droiddruid](https://www.reddit.com/user/droiddruid).


## Related projects

* There has been a strong tradition of random and procedural generation within the hobby, since the genesis of the hobby. Two modern examples include:
  * [donjon](https://donjon.bin.sh/)
  * [Abulafia](http://www.random-generator.com/)
* [Janelle Shane](http://lewisandquark.tumblr.com/post/159363915392/new-dd-magic-spells-designed-by-neural-network) - plays with recurent neural nets to create new spell names

## Approach

* The tnitial problem is principally a regression problem, focused on feature extraction.
Since the sample population is very small, great care must be taken to avoiding overfitting.
* The problem of generating a monster entry from a selection of features can be thought of as a variation of the technique used in Google's [DeepDream](https://github.com/google/deepdream).
Given a data point and target value, we can perform gradient descent with respect to the unselected data features.

## Deliverables

* This GitHub repository.
* A slide deck summarizing the project.
* A live version of the model.

## License
This work falls under the purview of the [OGL](http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf).

