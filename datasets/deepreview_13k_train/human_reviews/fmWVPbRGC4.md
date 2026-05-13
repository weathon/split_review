# Local vs distributed representations: What is the right basis for interpretability?

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Much of the research on the interpretability of deep neural networks has focused on studying the visual features that maximally activate individual neurons. 
However, recent work has cast doubts on the usefulness of such local representations for understanding the behavior of deep neural networks because individual neurons tend to respond to multiple unrelated visual patterns, a phenomenon referred to as ``superposition''. 
A promising alternative to disentangle these complex patterns is learning sparsely distributed vector representations from entire network layers, as the resulting basis vectors seemingly encode single identifiable visual patterns consistently. Thus, one would expect the resulting code to align better with human-perceivable visual patterns, but supporting evidence remains, at best, anecdotal.
To fill this gap, we conducted three large-scale psychophysics experiments collected from a pool of 560 participants.
Our findings provide (\textit{\textbf{i}}) strong evidence that features obtained from sparse distributed representations are easier to interpret by human observers and (\textit{\textbf{ii}}) that this effect is more pronounced in the deepest layers of a neural network. 
Complementary analyses also reveal that (\textit{\textbf{iii}}) features derived from sparse distributed representations contribute more to the model´s decision.
Overall, our results highlight that distributed representations constitute a superior basis for interpretability, underscoring a need for the field to move beyond the interpretation of local neural codes in favor of sparsely distributed ones.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the question of human interpretability of the features derived from deep neural network. They considered two types of features: (i) features that triggered maximal responses (maximally activating images) in certain network units; (ii) features that were obtained by applying sparse dictionary learning to the maximally activating images. They defined these two classes as local representation v.s. distributed representation, respectively. Using psychophysics experiments, the authors studied which type of features were more interpretable. They reported some evidence suggesting that the sparse features was more interpretable to human observers. Overall, this seems to be an interesting piece of work, despite that the effect size obtained in the experiments is fairly small.

### Strengths
Originality: While this is not the first study to use psychophysics to understand the interpretability of deep network features, human interpretability of deep network features remains an under-explored direction. Overall, the combined experimental and modeling approach is considered to be novel. 


Quality: The study is generally well-executed. Behavioral responses were collected from a large number of human subjects.  Three experiments were conducted. The first one was the main experiment. The remaining two were control experiments to help further interpreting the results. 


Clarity: The method and approach are generally well described, except for a few sections (see comments below about Section 4).


Significance: Understanding and interpolating the features of deep nets is an interesting and timely question. The approach used here, while not entirely novel, remains useful.

### Weaknesses
- The formulation of local v.s. distributed representation (two concepts that are essential to this paper) is messy and problematic in the current version. In the Introduction, the author referred to the grandmother cell as the local representation, and cited the paper by Quiroga et al (2005). I think the results in Quiroga et al (2005) was misinterpreted. The fact that, from a small of recorded neurons in the hippocampus in Quiroga et al (2005) one could already find a neuron that selective to a specific person, suggests that there is a large population of neurons that are selective to that person (yet being sparse). Thus, the results from Quiroga et al (2005) as well as other related studies instead favor a sparse and distributed representation.  I wonder if a better distinction would be “dense” v.s. “sparse”, rather than “local” v.s. “distributed”.

Thus, I think the overall pitch of the paper, i.e., the formulation of “local” v.s. “distributed”, is problematic. 


- One potential explanation for the main experimental results might be that the complexity of the features from the two classes (original maximally activating images v.s. sparse features obtained from them) did not match. Perhaps the sparse features used in the experiments are simpler and have less entropy compared to the maximally activating images. Would it be able to rule this out?

- The work only tested one version of ResNet50. It remains unclear whether the results would generalize to other deep nets. I understand that it would be too much to re-run the experiments using features from a different network for the current study. However, if the authors could compare the features in different networks (i.e., running these psychophysics in silico), that would likely strengthen the paper.

- The main effect, while being statistically significant, the effect size as reported in Section 4 was fairly small.  The paper needs to take the effect size into account when interpreting the results.

- While the number of subjects was large, the number of responses collected in each experiment (~5k) did not exceed the number in typical psychophysical experiments. Some of the statements regarding the scale of experiments should be toned down accordingly. 


- The AIC comparison in line 450-451 implies a small difference (i.e, 4) between the two models. I think the interpretation should be more nuanced. 

- How the Result section was presented can be improved. It would be useful if the authors could further unpack the meaning of the analyses performed there.

### Questions
What are the assumptions behind the logistic regression analysis in Section 4? It would be good to make these more explicitly so a naive reader would have a better sense of how the results should be interpreted. 


Line 301-303, it was not exactly clear in terms of how the particular direction was selected. What does “the most frequently the most activated” mean? Please clarify. 

Line 130: Re: “neurons’ tendency to respond to multiple unrelated visual elements”
What does “unrelated visual elements” mean? This seems to be fairly arbitrary. 

Are the comparisons in Fig. 4 statistically significant? What do the error bars represent?

Line 277-281, what were special about the 80 neurons selected? Are these a representative subset of all units in the network? If not, how do we know if the results would generalize to other neurons in the network?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this manuscript, the authors present the results of 3 psychophysics experiments on the interpretability of internal representations of a ResNet-50 trained on ImageNet. Following an established paradigm the authors showed images that highly activate a dimension and images that lowly activate a dimension in the deep neural network and asked subjects to infer whether a new test image activates the dimension or not. The main comparison is between the original neural dimensions and distributed directions determined by CRAFT, a dictionary learning method. The authors find better performance for the distributed representations. Nulling the most activated distributed direction also impaired network performance more than nulling the most active neuron. All effects get stronger for deeper layers in the network.

### Strengths
In general, interpretability of neural networks is a pressing matter and the sparse bases for interpretability are a recent development that is worth testing. To do so, the authors present a coherent set of experiments with state of the art methods. Both in terms of the psychophysical task and in terms of the statistical analysis, I believe the results are solid.

### Weaknesses
While the paper seems sound enough to me, the I doubt the importance of these results. It appears to be a solid confirmation of ideas we had before with established methods. This is good to do, but of somewhat limited impact.

- The results presented here are limited to a single network for a single network for a single task. Thus it remains unclear whether the effects described are general.
- All the technical steps were established before, i.e. there is no technical innovation in this paper
- As sparse dictionaries were developed as an XAI method, it is already a general believe in the literature that they are indeed more interpretable than the original neural activities, especially for deeper representations 
- The effect on interpretability appears to be quite gradual, i.e. while the difference is clearly significant, the features extracted by CRAFT are still far from optimally interpretable especially for earlier layers. Thus, the problem of interpreting DNN activations remains unsolved effectively.
- There could be somewhat deeper analysis of the data, for example which features are more or less interpretable, what proportions of features are interpretable, etc.

### Questions
Can the results be used to improve interpretability somehow?

Can the results be reused for other networks in some way?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors perform computational and psychophysics experiments to determine whether local representations are more interpretable and useful for model decisions than distributed representations. They conclude that distributed representations are more interpretable and models rely more on them.

### Strengths
* Well written
* Well referenced
* Addresses an important issue for the interpretability community
* Provides evidence of interpretability from human perception
* Provides evidence of feature importance for model decisions

I find it hard to comment on originality (e.g., the work is important/useful regardless of whether the methods themselves are novel). The 4th bullet above is to me an important component which is not always assessed rigorously in other work.

### Weaknesses
I provide a summary first and then elaborate.

* The paper makes general claims about distributed vs local representations but does not provide empirical evidence for this generality or theoretical arguments for why it should be expected.
* Does not make explicit the model of human cognition/perception that motivates the psychophysics experiments and their analyses.
* Does not provide theoretical insight for why sparse distributed representations obtained via NMF should match human-interpretable features.
* Dichotomizes local vs distributed in the interpretation of the results, even though the results indicate the difference might be one of degree.
* Properties of the sampling of neurons are unclear.

Line 093: “…growing consensus that distributed representations constitute a stronger basis for interpretability compared to local ones...” This is the main point of the introduction and should be elaborated and explained. It merits more space than the generic survey-like paragraphs that come before it. In particular, what is the theoretical rationale for why this should be the case? Or is this ‘consensus’ purely driven by empirical findings? In any case, it would be helpful to clarify.

Line 084: “representations driven by single features are more desirable because they are expected to be easier to understand by a human” Why is this so? Single features can be non-intelligible to humans. Otherwise the definition of feature would have human-intelligibility baked in, in which case the quoted statement is circular.

Line 257: “Measure the ambiguity, or perplexity, of the visual feature as a proxy for its interpretability.” But a neuron can be interpretable even though it is ‘ambiguous’ (e.g., because it responds to more than one feature). For instance, it seems to me that responding to a disjunction of features is an interpretable response.

Perhaps these issues can be clarified if the authors make explicit a (ideally formal) notion of human-intelligible feature.

The model of human perception is left implicit in the manuscript. What is the model of human cognition that motivates the predicition that coherence relates to interpretability?

Line 275 mentions “Representative sample of units”. What are they representative of? And how is the representativeness achieved? Relatedly, can the authors clarify why they select the 80 units reported in Zimmerman? How was this selection made?

Do the results generalize beyond ResNet50 and ImageNet? Do they generalize across modalities (vision, audition, language, etc)? As far as I can see, there is no empirical evidence of generalization in these directions in the paper, nor theoretical arguments why it should be expected. Nevertheless, the paper makes a general claim about local versus distributed representations. It would be helpful to have experiments testing generalization in these directions and/or rigorous theoretical arguments.

Figure 1: As with other figures in the manuscript, it might benefit from unambiguously pointing to figure elements in the text. For instance, “depicted in the images at the bottom” should presumably point only to the visual elements in orange, not to all visual elements at the bottom of panel (a). Furthermore, panel (a) contains multiple other elements in the graphs which are not discussed in the figure caption (e.g., axes, black and colored data points, “n_1” labels, etc.). It would be great if the authors can take the reader through each panel explaining how the schematic depicts the concepts the authors want us to take away. Additional issues include: orange and green colors are referenced in the figure caption but gray is not. Likewise, the explanation in Figure 4 could be clearer. For example, you can clearly identify each experiment and avoid ambiguoous referents such as “this set of images”.

Participants perform quite well in the local representation condition. This means, following the authors’ rationale, that the local representation is quite interpretable as well. However, the authors express a more dichotomic view throughout. Why is this so? It seems to me that a dichotomic interpretation of the results is not warranted. At the very least, consideration of mechanisms that use both local and distributed representations, and what each of these contribute to, is called for.


### Questions
Minor comments, suggestions and questions:

Line 214 reads “neuron in \mathcal{A}”. Shouldn’t this be a component of a vector $a \in \mathcal{A}”?

Line 213: why is v_c indexed by c if it is made to correspond to an image x_i indexed by i?

Line 215: notation for modified activations a’_i is using a font different from the one in the definition in the previous paragraph.

Line 242: “by measuring as the difference” should presumably be “by measuring the difference”

The parallel between the problems of XAI and neuroscience, highlighted in the second and third paragraphs of the introduction, has been drawn explicitly and elaborated on by Vilas et al (2024) in the context of interpretability.

Please clarify mathematical notation. For instance, in equation 1, is y_i a vector? How does equation 1 relate to importance?

Stimuli selection: is it possible that the selection of maximally and minimally activating images contribute to mischaracterization of the full neural function? Relatedly, why are there more strongly activating images than weakly activating images?

Could the authors plot/overlay the data points in the graphs (i.e., not just bars)? It could foster a more truthful appreciation of the effects.

Line 460 references figure 7, which appears in the appendix, as if it were in the main text. There are possibly other instances of this throughout.

Given the authors' conclusions favoring distributed representations, the results could be relevant to the following literature exploring feasible interpretability queries, most of which only explore axis-aligned queries: Adolfi et al., 2024; Barcelo et al., 2020.

It might be useful to relate local versus distributed representations to discussions of axis-aligned versus non-aligned features.

Barceló, P., Monet, M., Pérez, J., & Subercaseaux, B. (2020). Model Interpretability through the lens of Computational Complexity. Advances in Neural Information Processing Systems, 33, 15487–15498. https://proceedings.nips.cc/paper_files/paper/2020/hash/b1adda14824f50ef24ff1c05bb66faf3-Abstract.html

Adolfi, F., Vilas, M. G., & Wareham, T. (2024). The Computational Complexity of Circuit Discovery for Inner Interpretability (No. arXiv:2410.08025). arXiv. http://arxiv.org/abs/2410.08025

Vilas, M. G., Adolfi, F., Poeppel, D., & Roig, G. (2024). Position: An Inner Interpretability Framework for AI Inspired by Lessons from Cognitive Neuroscience. Proceedings of the 41st International Conference on Machine Learning, 49506–49522. https://proceedings.mlr.press/v235/vilas24a.html

### Soundness
2

### Presentation
3

### Contribution
3
