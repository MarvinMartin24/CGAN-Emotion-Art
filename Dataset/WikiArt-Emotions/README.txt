WikiArt Emotions Dataset
August 2018
Copyright (C) 2018 National Research Council Canada (NRC)
----------------------------------------------------------------


Contact: Saif Mohammad (saif.mohammad@nrc-cnrc.gc.ca)


Terms of Use: 
-------------------------------------------------

1. If you use this dataset, cite the paper below:

Saif M. Mohammad and Svetlana Kiritchenko. (2018). WikiArt Emotions: An Annotated Dataset of Emotions Evoked by Art. In Proceedings of the 11th edition of the Language Resources and Evaluation Conference, May 2018, Miyazaki, Japan.

2. Do not redistribute the data. Direct interested parties to this page: http://saifmohammad.com/WebPages/wikiartemotions.html

3. National Research Council Canada (NRC) disclaims any responsibility for the use of the dataset and does not provide technical support. However, the contact listed above will be happy to respond to queries and clarifications.



WikiArt Emotions Dataset
-------------------------------------------------

WikiArt Emotions is a dataset of 4,105 pieces of art (mostly paintings) that has annotations for emotions evoked in the observer. The pieces of art were selected from WikiArt.org's collection for four western styles (Renaissance Art, Post-Renaissance Art, Modern Art, and Contemporary Art). The art was annotated via crowdsourcing for one or more of twenty emotion categories (including neutral). In addition to emotions, the art was also annotated for whether it includes the depiction of a face and how much the observers like the art. 

We do not redistribute the art images, we provide only the annotations.


Art pieces annotated:
-------------------------------------------------

The pieces of art were selected from WikiArt.org's collection for twenty-two categories from four western styles (Renaissance Art, Post-Renaissance Art, Modern Art, and Contemporary Art). WikiArt.org shows notable art in each category in a Featured page. We selected ~200 items from the featured page of each category. Below is the list of the 22 categories with the number of art pieces annotated from each category.

Contemporary Art
   Minimalism	200
Modern Art
   Abstract Art	200
   Abstract Expressionism	200
   Art Informel	200
   Color Field Painting	200
   Cubism	200
   Expressionism	200
   Impressionism	200
   Lyrical Abstraction	200
   Magic Realism	153
   Neo-Expressionism	200
   Pop Art	200
   Post-Impressionism	200
   Surrealism	198

Post-Renaissance Art
   Baroque	200
   Neoclassicism	197
   Realism	200
   Rococo	200
   Romanticism	200

Renaissance Art
   Early Renaissance	119
   High Renaissance	104
   Northern Renaissance	192

Note that some pieces of art are associated with more than one style category.



Emotions:
-------------------------------------------------

Each piece of art was annotated with one or more of the twenty emotions:

Positive
   gratitude, thankfulness, or indebtedness
   happiness, calmness, pleasure, or ecstasy
   humility, modesty, unpretentiousness, or simplicity
   love or affection
   optimism, hopefulness, or confidence
   trust, admiration, respect, dignity, or honor
Negative
   anger, annoyance, or rage
   arrogance, vanity, hubris, or conceit
   disgust, dislike, indifference, or hate
   fear, anxiety, vulnerability, or terror
   pessimism, cynicism, or lack of confidence
   regret, guilt, or remorse
   sadness, pensiveness, loneliness, or grief
   shame, humiliation, or disgrace	
Other or Mixed
   agreeableness, acceptance, submission, or compliance
   anticipation, interest, curiosity, suspicion, or vigilance
   disagreeableness, defiance, conflict, or strife
   surprise, surrealism, amazement, or confusion
   shyness, self-consciousness, reserve, or reticence
   neutral													


Annotations:
-------------------------------------------------

Each piece of art was annotated by at least 10 workers. The annotations include:
1. all emotions that the image of art brings to mind;
2. all emotions that the title of art brings to mind;
3. all emotions that the art as a whole (title and image) brings to mind;
4. rating on a scale from -3 (dislike it a lot) to 3 (like it a lot);
5. whether the image shows the face or the body of at least one person or animal;
6. whether the art is a painting or something else (e.g., sculpture).
 
We asked annotators to identify the emotions that the art evokes in three scenarios:
   Scenario I: we presented only the image (no title), and asked the annotator to identify the emotions it evoked;
   Scenario II: we presented only the title of the art (no image), and asked the annotator to identify the emotions it evoked; 
   Scenario III: we presented both the title and the image of the art, and asked the annotator to identify the emotions that the art as a whole evoked.

We instructed the annotators so that:
- when answering the question about the title (scenario II), they should not try to recollect what they answered earlier for the image that goes with it. Their response should be based solely on the title. 
- when answering the question about the title-image combination (scenario III), they should not try to recollect what they answered earlier for the image alone or for the title alone. Their response should be based on what the art (title + image) evokes.  

To help the annotators focus only on the question at hand (and exclude influences from earlier responses), we showed five instances in scenario I in a random order, followed by five instances in scenario II in a different random order, followed by five in scenario III in another random order.



Annotation Aggregation:
-------------------------------------------------

1. The emotion responses were aggregated as follows: 
- if at least n% of the responses indicate that a certain emotion applies, then that label is chosen;
- if at least n% of the respondents indicate the neutral option and less than n% of the respondents indicate any of the other nineteen emotions, then the neutral label is chosen.

We provide datasets for different values of n:

- Ag3: 30% (three out of ten people)
- Ag4: 40% (four out of ten people)
- Ag5: 50% (five out of ten people)
- All: no threshold is used, the proportions of responses for each emotion are reported.

We recommend to use the Ag4 distribution.

2. The art ratings are averaged over all the responses for the piece.

3. The face/body responses were aggregated as follows: 
- if at least 50% of the responses indicate that the image shows a face, then the label 'face' is chosen;
- otherwise, if at least 50% of the responses indicate that the image shows a face or a body, then the label 'body' is chosen;
- otherwise, the label 'none' is chosen.

4. The painting/non-painting responses were aggregated as follows: 
- if at least 50% of the responses indicate that the art is a painting, then the label 'yes' is chosen;
- otherwise, the label 'no' is chosen.



File format:
-------------------------------------------------

The current distribution consists of the following data files:

1. "WikiArt-Emotions-Ag3.tsv", "WikiArt-Emotions-Ag4.tsv", "WikiArt-Emotions-Ag5.tsv", "WikiArt-Emotions-All.tsv"

These files contain the annotations aggregated as described above (one for each type of emotion responses aggregation: Ag3, Ag4, Ag5, and All). 

Each file provides the infomation on the art taken from the WikiArt.org website:
- ID;
- Style: Renaissance Art, Post-Renaissance Art, Modern Art, or Contemporary Art;
- Category: one or more of the 22 style categories (if the art is assigned to more than one category, the categories are separated by a comma);
- Artist;
- Title;
- Year of creation;
- Image URL;
- Painting Info URL;
- Artist Info URL.

Then, the annotations for the art follow:
- whether it is a painting or not;
- whether the image shows a face, a body, or none;
- average art rating;
- emotion annotations for the art (image and title): for Ag3, Ag4, Ag5, '1' indicates that the emotion is present, '0' indicates that the emotion is not present; for All, the proportion of responses indicating the emotion are shown;
- emotion annotations for the image only: for Ag3, Ag4, Ag5, '1' indicates that the emotion is present, '0' indicates that the emotion is not present; for All, the proportion of responses indicating the emotion are shown;
- emotion annotations for the title only: for Ag3, Ag4, Ag5, '1' indicates that the emotion is present, '0' indicates that the emotion is not present; for All, the proportion of responses indicating the emotion are shown.


2. "WikiArt-info.tsv"

This file provides the infomation on the art taken from the WikiArt.org website:
- ID;
- Style: Renaissance Art, Post-Renaissance Art, Modern Art, or Contemporary Art;
- Category: one or more of the 22 style categories (if the art is assigned to more than one category, the categories are separated by a comma);
- Artist;
- Title;
- Year of creation;
- Image URL;
- Painting Info URL;
- Artist Info URL.


3. "WikiArt-annotations.csv"

This file contains the original annotations by each worker without aggregation.

We asked annotators to identify the emotions that the art evokes in three scenarios:
   Scenario I: we presented only the image (no title), and asked the annotator to identify the emotions it evoked;
   Scenario II: we presented only the title of the art (no image), and asked the annotator to identify the emotions it evoked; 
   Scenario III: we presented both the title and the image of the art, and asked the annotator to identify the emotions that the art as a whole evoked.

We showed five instances in scenario I in a random order, followed by five instances in scenario II in a different random order, followed by five in scenario III in another random order.

Each line in the file contains the annotations by one worker for five pieces of art in three scenarios:
- worker ID
- WikiArt ID and annotated emotions for five pieces of art in scenario 1 (fields 'ImageOnly')
- WikiArt ID and annotated emotions for five pieces of art in scenario 2 (fields 'TitleOnly')
- WikiArt ID and annotated emotions for five pieces of art in scenario 3 (fields 'Art (image+title)')
- For scenario 3, we also provide annotations whether the art is a painting or something else (e.g., sculpture), whether the image shows the face or the body of at least one person or animal, and rating on a scale from -3 (dislike it a lot) to 3 (like it a lot).

In each scenario, an annotator selected one or more of the nineteen emotions or chose the 'Other' option (fields 'Emotions'). If more than one emotion are chosen, they are separated by a newline. If the 'Other' option was chosen, the annotator had to enter an emotion not included in the above list of the nineteen emotions or enter 'neutral' (fields 'Other Emotions'). The following shortenings were allowed: 'n' for 'neutral', and 'ol' for the titles that were in a language other than English.

A WikiArt ID can be matched to the full information on a piece of art using the file "WikiArt-info.tsv".

To preserve privacy, we replaced the CrowdFlower worker IDs with sequential IDs, but kept the same ID for all annotations performed by a particular worker. 



Further Information:
-------------------------------------------------

Saif M. Mohammad and Svetlana Kiritchenko. (2018). WikiArt Emotions: An Annotated Dataset of Emotions Evoked by Art. In Proceedings of the 11th edition of the Language Resources and Evaluation Conference, May 2018, Miyazaki, Japan.




CONTACT INFORMATION
-------------------------------------------------
Saif M. Mohammad
Senior Research Officer, National Research Council Canada
email: saif.mohammad@nrc-cnrc.gc.ca
phone: +1-613-993-0620

