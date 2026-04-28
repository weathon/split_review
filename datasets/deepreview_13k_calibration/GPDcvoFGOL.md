# Interpreting the Second-Order Effects of Neurons in CLIP

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
\vspace{-0.2em}
We interpret the function of individual neurons in CLIP by automatically describing them using text. Analyzing the direct effects (i.e. the flow from a neuron through the residual stream to the output) or the indirect effects (overall contribution) fails to capture the neurons' function in CLIP. Therefore, we present the ``second-order lens'', analyzing the effect flowing from a neuron through the later attention heads, directly to the output. We find that these effects are highly selective: for each neuron, the effect is significant for $<2\%$ of the images. Moreover, each effect can be approximated by a single direction in the text-image space of CLIP. We describe neurons by decomposing these directions into sparse sets of text representations. The sets reveal polysemantic behavior---each neuron corresponds to multiple, often unrelated, concepts (e.g. ships and cars). Exploiting this neuron polysemy, we mass-produce ``semantic'' adversarial examples by generating images with concepts spuriously correlated to the incorrect class. Additionally, we use the second-order effects for zero-shot segmentation and attribute discovery in images. Our results indicate that a scalable understanding of neurons can be used for model deception and for introducing new model capabilities.\footnote{Project page and code: \url{https://yossigandelsman.io/clip_neurons/}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents a novel approach for examining potential second-order effects of neurons of CLIP representations and how these can be used in the context of zero-shot segmentation and generation of adversarial images. 

To this end, the authors focus on the contribution of each individual neuron to the output in terms of second-order effects via the computation of the additive contribution of each neuron through the MSAs and projection to the input space. 

The experimental evaluation focuses on the empirical analysis of the obtained effects and how these insights can be used in the context of generating "semantic" adversarial examples and using said effects for zero-shot segmentation.

### Strengths
This paper draws inspiration from recent approaches that aim to examine and evaluate the functionality of each neuron in a given architecture. Automated interpretability constitutes an important challenge for modern architectures and this work aims to approach this in a different way via the contribution of neurons to the output representation and the information flow through the MSA blocks.

### Weaknesses
The connection of the proposed approach to highly relevant work is a bit lacking. Can the authors provide a discussion on [1], highlighting the differences in the decomposition and analysis of the direct effects of the neurons?

I find the focus on a single dataset, i.e., ImageNet, to be a bit restrictive in terms of analysing the behavior of the proposed approach. Indeed, most approaches in this line of work considered additional datasets, e.g., Waterbirds, CUB and Places365. The same applies for the adversarial examples setting, where the authors only consider CIFAR-10. What happens when trying to generate adversarial examples in a more complicated dataset, e.g., CUB or ImageNet?

Did the authors reproduce the results for all the method in Table 4? Since they are different than the ones reported [1], I would expect that to be the case. 

Can the authors provide the weights of the texts corresponding to the sparse decomposition of each neuron? A full list for some neurons would also be helpful. 
Qualitatively, what are the differences when choosing a different sparse set size m. 

What is the motivation behind the consideration a binary classification task instead of a classical setting? What classifier is used and how is it trained?

The authors mention that the generated adversarial images lie on the manifold of generated images differently from non-semantic adversarial attacks. Can the authors elaborate on this claim?

What is the complexity of the proposed approach compared to other interpretability focused methods?

### Questions
Please see the Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an interpretability study focused on understanding the second-order effects of neurons in CLIP. The authors propose a novel "second-order lens" to analyze neuron contributions that flow through attention heads to the model output.

### Strengths
1. The technical contributions are sound  and interesting.
2. The paper is well written. 
3. The paper included thorough evaluations.

### Weaknesses
Generally good paper so please see questions.

### Questions
1. What happens if you apply the same method to the text encoder in CLIP?
2. Have the authors tried it on other variants of CLIP like MaskCLIP?
3. Do the findings of this paper apply to other domains like medical imaging (MedCLIP)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an approach to generalize the first order effects of a neuron in attention networks into second order effects through successive layers. This methodology helps uncover the sparseness of the neuron second order effect as well as the decomposition of each neurons second order effect into a single direction vector.

### Strengths
- Extensive empirical validation of second order effects (e.g. second order effect neuron sparseness)
- Intuitive and interesting applications of second order effect control in the semantic adversarial example generation
- Increased understanding of internal attention model mechanism through semantic adversarial examples
- Improved segmentation results over TextSpan

### Weaknesses
 - Sparse coding to find textual descriptions of neurons may be very computationally expensive
- Not considering nonlinearities in second order effects (Eqn 5)

### Questions
- Are there any gradient based approaches to finding textual descriptions of each neuron's second order effect?
- Were any additional text to image models evaluated other than DeepFloyd IF, if so was there similar success to images generated with DeepFloyd IF?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to interpret the functional of individual neurons in CLIP by investigating their "second order" effects at the joint text-image output space. Specifically, a neuron's contribution to the output feature space is defined as the summing of the effects flowing from the neuron through the later attention heads, to the output. Experimental results show several observations: (1) the effects of an individual neuron are highly selective. (2) Each neuron's contribution in the output feature space can be approximated by a single direction, which can be decomposed into representations of a sparse set of texts. (3) By exploiting the polysemantic property of neuron, it is possible to generate adversarial images that fool the CLIP classifier. (4) The semantic-awareness of neurons can be utilized for semantic segmentation.

### Strengths
1. The paper is well motivated, as exploring the functions of neurons in CLIP model facilitates better understanding of its representation learning mechanism, and guide further improvements
2. The paper proposes to study the "second order" effect of neurons, which is demonstrated to show a clearer signal of their contribution comparing to first order and indirect effects
3. The paper shows an interesting finding that each neuron's contribution to the joint text-image output space is approximately a single direction vector, and implies a ploysemy property.
4. The paper further exploits the finding of 3 for generating adversarial images and application of semantic segmentation, showing that by taking advantage of polysemy neuron's output representations, it's possible to fool the CLIP classifier by using words that's spuriously correlated with a wrong class; and that by aggregating the activation maps of neurons that highly correlated with a query concept, its semantic segmentation mask can be acquired.

### Weaknesses
Please see questions

### Questions
1. In the related work section, the paper lists several other neurons interpretability works that explore what concepts the neuron activated on, and saying that in contrast their work focuses on the neuron's contribution to the output space. My question is: what is the relation between the two approaches (exploring what examples the neurons activate on vs. exploring their contribution in the output space), what are the advantages / limitations of one over the other, does one show complementary aspects that the other cannot  observe?

### Soundness
3

### Presentation
3

### Contribution
3
