# Emergent Orientation Maps —— Mechanisms, Coding Efficiency and Robustness

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Extensive experimental studies have shown that in lower mammals, neuronal orientation preference in the primary visual cortex is organized in a disordered "salt-and-pepper" pattern. In contrast, higher-order mammals display a continuous variation in orientation preference, forming structured pinwheel-like patterns. Despite these observations, the spiking mechanisms underlying the emergence of these distinct topological structures and their functional roles in visual processing remain poorly understood. To address this, we developed a self-evolving spiking neural network model with Hebbian plasticity, trained using physiological parameters characteristic of rodents, cats, and primates, including retinotopy, neuronal morphology, and connectivity patterns. Our results identify critical factors, such as the degree of input visual field overlap, neuronal density, and the balance between localized connectivity and long-range competition, that determine the emergence of either salt-and-pepper or pinwheel-like topologies. Furthermore, we demonstrate that pinwheel structures exhibit lower wiring costs and enhanced sparse coding capabilities compared to salt-and-pepper organizations. They also maintain greater coding robustness against noise in naturalistic visual stimuli. These findings suggest that such topological structures confer significant computational advantages in visual processing and highlight their potential application in the design of brain-inspired deep learning networks and algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates how the pattern of orientation map emerges from a recurrent spiking network model with synaptic plasticity, and concludes that the feedforward input overlap is crucial for forming different map patterns, i.e., salt-and-pepper vs. pinwheel structures.

### Strengths
1. Biological plausibility of the recurrent spiking network model with plasticity. The model is well supported by neurobiological experiments and is quite similar to the conventional recurrent spiking network used in neuroscience studies.

### Weaknesses
1. Although the authors claim they provide a spiking network mechanism of orientation map, the spiking dynamics seem unnecessary, because none of the results rely on spike timing information. All learning rules are based on the firing rate of neurons only. This makes the spiking network model look like a "strawman" a bit. I envision the spiking network model with spike-time-dependent plasticity rule might have different mechanisms from the rate-based Hebbian rules. Anyhow, I think the author can provide some explanations about how much we could gain about the orientation map formation from the proposed spiking network model. 

2. I am still debating about the contribution of this work to ICLR society. That is, how much we could gain from this study to develop the next-generation AI algorithm? Or how the results in the paper can be incorporated into the modern deep learning algorithms? Another thing is although the model is biologically plausible, all learning rules and network model architecture are not new.

3. It is uncommon to see the title of the paper PDF differ from the title shown in the OpenReview. This makes me concerned that the paper might not be well prepared, at least in the submission stage.

### Questions
1. What is the $z_j(t)$ in Eq. 3?

2. Could the authors comment on the differences between the current model with Hansel & Vreeswijk, J. Neurosci., 2012?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors study functional organization of the primary visual cortex across animal species. Depending on the species, primary visual cortex is organized in a continuum going between disordered salt-and-pepper and ordered pinwheel structures. Authors model these functional organizations with an E-I spiking neural network that is equipped with two types of Hebbian-like plasticity rules. An important finding is that  the degree of synaptic organization depends crucially on the overlap of feedforward inputs incoming to the network. They also find that once learned, the pinwheel organisation is stable and promotes efficient processing of visual information.

### Strengths
Authors presented a rather convincing paper with a clear and timely scope. The paper is technically correct and rigorous in methods. It brings potentially important and new insights into why biological neural networks organise in a continuum of salt-and-pepper and pinwheel structures.

### Weaknesses
Major weakness of this paper are the presentation, the lack of justification and elaboration on modelling and parameter choices, and insufficient comment on results. While the presentation is rather transparent, the clarity of the text can be substantially improved. Also, the text contains a number of typos.

1) I recommend to omit all abbreviations besides the very common ones, such as  V1, E-I and potentially FF. The acronym of the network, SESNN, is also an exception and is useful to have. All other acronyms seem counterproductive. While authors have compiled a list of acronyms in the Appendix A.7, frequent use of diverse acronyms throughout the text impedes readers that are less familiar with the topic of self-organising maps to appreciate the results.  

2) On many places, the text is rather difficult to follow, with long and unnecessarily complicated sentences. In some cases, sentences are not grammatically correct. See for example line 275, Figure Caption 3a and h, lines 368-371. On page 9, there are references to Figure 6, but likely authors want to refer to their Figure 4. In line 262, authors refer to the third panel of fig 2a, but it might rather be the first panel?

3) It is not clarified enough what is the difference in effects between the Hebbian Oja's and Correlation Measuring type of learning. The only reasoning I gathered is that Hebbian Oja plasticity rule has the desired property of normalization that prevents too strong E-E connectivity.  What is the drawback of using Hebbian Oja's plasticity for E-I and I-I connectivity? Authors should go deeper into explaining this, as it seems to be crucial for the results they obtain.

4) In Eq. 7, authors define the energy cost of synaptic transmission as inversely proportional to the connection strength. While this is an interesting choice, it is not intuitive why a quantity inversely proportional to the connection strength is used as the metabolic cost. Also, it is not well justified why is the information capacity computed as the entropy of the weight distribution. Could authors elaborate on that and provide references if applicable?

5) The measure of reliability in Eq. 10 is based on the encoding capability of single neurons. Today, however, there is ample evidence suggesting that in the cortex, signal processing is better captured on the level of neural populations.

### Questions
1) Seen that Eq. 4 is the one actually used for modelling, it is not clear what is the purpose of Eq. 3? Also, it is unclear what the variable z in Eq. 3 stands for.

2) Why is the "neural connectivity parameter" (max weight) higher for E compared to I neurons? At the same time, authors report that E-I connectivity should be stronger compared to E-E connectivity.

3)  In lines 173-174, authors comment on their choice of hyperparameters and state that "their approach is consistent with empirical findings". It remains unclear how specific hyperparameters of their model relate to empirical findings. Could authors be more specific?

4) How is the coefficient in Eq. 8 different from a well-known measure of the cross-correlogram on neural spike trains (Bair et al., J.Neurosci. 2001)?

5) A recent study showed that efficient encoding of uncorrelated stimulus features with E-I spiking networks does not require E-E connectivity (Koren et al., eLife 2024). However, your study seems to suggest the necessity of E-E connectivity. Could authors comment on this discrepancy?

6) One of the take-home messages of the paper seems to be that the pinwheel structure is more efficient than the salt-and-pepper structure. However, salt-and-pepper organization can be observed in biological brains, and it seems unlikely that it would survive evolution if it was inefficient. Moreover, authors show that salt-and-pepper type of organisation arises when the overlap of inputs to E neurons is small, which is the case in some animal species. All together, it seems to me that there is no single "most efficient" type of structure, but that there are multiple efficient solutions depending on a specific model parameter. Rather than making a simplistic (and not quite correct ?) conclusion and point to one and only best solution, it would seem to me more appealing if these results are interpreted more carefully to give us better insights about biology.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Authors propose a comprehensive model of the primary visual cortex encompassing anatomical factors, such as natural image inputs, precise and realistic representation of neuronal responses, as well as spiking mechanisms in order to understand the emergence of pinwheel structures. They successfully show that the model can reproduce the emergence of different orientation maps in the visual cortex and that it is compatible with the maps of different species as a function of different factors such a neuron density or RF overlap.

### Strengths
The paper is clearly written and presents a novel approach to analyzing the emergence of orientation maps in the visual cortex. The proposed model is well-motivated and supported by mathematical formalization. The authors provide a detailed explanation of the model and its components, which enhances the understanding of the proposed method.

### Weaknesses
Stating in the abstract that the subject in "largely unexplored" is a strong claim that needs to be supported by a more extensive literature review. The paper could benefit from a more in-depth discussion of related work to provide context for the proposed approach. Your extensive bibliography provides already a good illustration of the number of works on the subject, and more for instance on the emergence of orientation maps in the visual cortex from haphazard wiring, or from the emergence of both types of maps using pooling mechanisms in a sparse deep predictive coding network, could be useful. More generally, it would be useful to highlight the difference of your work with [Stevens et al., 2013].

### Questions
It has been proven multiple times that the anatomy of V1 is efficient for processing visual information. How do you think your model could be used to understand the emergence of orientation maps in the visual cortex? Is the tiling of receptive fields a possible factor ? (see eg https://doi.org/10.1016/j.neuron.2016.07.015 )

The model uses 1/ static images, 2/ images represented on a Cartesian grid. Extensions using dynamic images or images represented on a polar grid could be interesting. The evaluation of the model is limited to the comparison of the orientation maps with experimental data. A more quantitative evaluation of the model's performance on other tasks could provide a more comprehensive assessment of its capabilities.

### Soundness
4

### Presentation
4

### Contribution
3
