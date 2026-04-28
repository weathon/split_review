# What Does it Mean for a Neural Network  to Learn a "World Model"?

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 3, 5

## Abstract
We propose an abstract but precise definition of what it means for a neural net to learn and use a "world model." The goal is to give an operational meaning to terms that are often used informally, in order to provide a common language for experimental investigation. Our definition is based on ideas from the linear probing literature, and formalizes the notion of a computation that factors through a representation of the data generation process. We also describe a set of conditions to check that such a "world model" is not a trivial consequence of the neural net's data or task.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper provides a conceptual framework for defining latent world models potentially learned by neural networks. This framework defines world models by their position in a commutative diagram relating to the world being implicitly modeled, the data (sampled from this world) that the network is trained on, and the latent representations learned by the network. The paper also includes several guidelines for instantiating this framework, like how to avoid trivial instantiations or study "local" world models covering narrower contexts than the network was trained on.

### Strengths
The paper clearly motivates and describes the underlying problem: how should we conceptualize the notion of "world models" in the context of latent neural network representations? This problem is indeed important and deserving of study, and the core idea of defining a commutative diagram over a network's training data, the "world" that training data is sampled from, and latent representations learned by the network is innovative.

### Weaknesses
Beyond simply defining the research question (how should we conceptualize the notion of "world models" in the context of latent neural network representations?) and drawing a commutative diagram that is useful for conceptualizing this question, **the paper does not provide a clear or meaningful contribution.**
While articulating the central question is helpful, this alone is not a sufficient contribution for an ICLR conference paper.

Indeed, the paper is styled more as a blog post than a conference paper: beyond its highly informal prose and prominent citations of tweets (Lecun, 2024) and blog posts (Andreas, 2024), it also **lacks the theoretical rigor that is necessary for a conceptual submission such as this one**; and it is not obvious that the proposed framework could be adequately formalized at all. For example:
- In sec 3.2.1, the framework requres "simple function classes" $F_W$ and $F_Z$ that restrict the range of functions that map between certain nodes in the commutative diagram in order to avoid a trivial definition. But "simple" is never formally defined -- instead, a few possible examples are provided without justification -- and it is never explained *how* requiring these functions to be "simple" actually resolves the triviality.
    - Furthermore, one of the examples provided in sec 3.2.1 of one such "simple" function class is that of two-layer MLPs, which are universal approximators; or in sec 3.4, another example for $F_W$ is listed as the space of "human computable functions". Either case would seem to strain any reasonable interpretation of "simple".
- Section 3.5.1 is concerned with preventing another possible triviality, this time the existence of another "simple" function that maps directly from inputs to a potential world model; but it is unclear both (1) why this is a problem, and (2) how the provided definition prevents this triviality.
    - E.g., word co-occurrence statistics are provided as an example of a "trivial" world model, as many interesting features of a potential world model can be approximated using linear projections from such statistics. However, this is simply another way of discussing the "distributional hypothesis" underpinning modern LLMs -- i.e., that sufficient knowledge of word co-occurrences is sufficient to understand much of natural-language semantics -- and the paper considers LLMs as serious candidates for learning world models. Why, then, is the existence of "simple functions" mapping from co-occurrence statistics to certain world model features understood as presenting a "trivial" case to be avoided?

Another key weakness is that the paper fails to reference several closely related works and relevant areas of study. For example:
- [1, 2] are also centrally concerned with conceptualizing how world models should be understood in the context of foundation models, and [2] also focuses on the intersection of interpretability and world modeling.
- The description in section 2.1 of "world models" as studied in cognitive science is lacking. For instance, predictive coding is one of the leading formalizations of world models in cognitive science [3,4], but predictive coding is never discussed.
- The "random control function" proposed in lines 372-381 appears to be equivalent to "control probes" as defined by [5], but [5] is never cited. Note that, on line 74-75, it is stated that "much of this paper may be seen as a reframing of ideas in Belinkov (2022)", and Belinkov (2022) discusses [5] at length. Thus, the failure to cite [5] is particularly concerning, and may be a sign of plagiarism.

### Questions
Definitions:
- As discussed above, how does constraining $F_W$ and $F_Z$ to be "simple function classes" resolve the triviality discussed in section 3.2.1?
- On line 328-329, what does it mean that "$F_X$ parallels $F_Z$" (328-329)? Is it simply that the two function classes should be equivalent, or satisfy some shared notion of simplicity? As with the topic of "simple function classes" throughout the paper, this should be formalized.
- How should "A" in figure 1 (bottom right side of commutative diagram) be interpreted in any case outside of robotics? I do not see any examples of "A" provided elsewhere, including in Table 1; and it is not clear how, why, or whether "A" and "Y" would be different in any other case. If A and Y are collapsed into the same node, does this lead to other potential problems with the diagram?

Conceptual question:
- The commutative diagram is discussed in terms of absolute equality (e.g., as in line 229-230). Is it possible to relax this assumption and allow for commutation to be approximate instead of exact? E.g., it seems that, especially if the intent is to make extensive use of "simple" functions under this framework, it would be more reasonable to expect approximations than learning exact mapping functions. What would the consequences of such approximation be?

### Soundness
2

### Presentation
1

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
This work seeks to establish minimum criteria by which one can say that a neural network encodes a world model. By establishing these criteria, this work aims to provide common  (and precise) language by which interpretability researchers can discuss the inner mechanisms of neural networks.

### Strengths
The goal of this work is necessary and important for shaping the discourse around neural networks, model interpretability, and the relationship between the field of deep learning and other fields that require more high-level/abstract models (such as cognitive science). Importantly, this fairly high-level paper is grounded in (and makes reference to) recent empirical work in interpretability. The paper is extremely well-written, clear-eyed and explicit about its purview and limitations, and ultimately succeeds in its goals.

### Weaknesses
The authors refer to the debate concerning whether LLMs actually understand text (523), and also mention that world models might connect to this issue (055). Making this connection a bit more explicit, even in an appendix, would be enlightening. This would potentially provide an important starting point for reframing the debate around understanding in more scientific terms.

Why do the authors say that learning probabilistic causal models is “a very strong meaning for a world model” (125)? In general, this section might be expanded a bit.

### Questions
Why do the authors say that learning probabilistic causal models is “a very strong meaning for a world model” (125)? In general, this section might be expanded a bit.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a set of criteria for saying a neural net learns a "world model".  This is a purely theoretical paper with no experiments.

### Strengths
It is helpful to have clear definitions of what we mean by a "world model".

### Weaknesses
Since I am more on the experiment side, I don't understand what follows from this paper.  How does the proposal relate to prior work?  Is the proposed framework falsifiable?  What follows from this contribution?

The word "understanding" is mentioned nearly a dozen times, but I don't know what that means.  Maybe that is the point of the last paragraph.  But that begs the question, what is a world model?  Is that what you propose?  But that sounds circular.

The first paragraph of the conclusion claims to have unified work on interpretability.  The paper mentions interpretability nearly a dozen times but I'm having trouble seeing the connection between this paper and those references.

### Questions
Can you help me understand the consequences of this paper?  What follows from this contribution?

Would it be possible to test your ideas?  If so, how?  What would an experiment look like?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an abstract criterion for claiming that a world models is being implemented in a neural network. The definition is based on the existence of some commutative functions mapping the hidden representation to a salient aspect of the network's behavior. Models should be 'interpretable' and 'causal'; interpretable meaning that the model is some pre-specified type of function of the world/representation, and causal meaning that the model predicts behavior just as the representation predicts outputs.

### Strengths
The paper does an extensive review of the literature, and motivates each aspect of the central diagram.

### Weaknesses
Usually for a definition to become accepted, it should demonstrate that it includes most clear-cut cases and excludes others. Some of this is done for intermediate steps (like the sentiment neuron, and word embeddings), but it feels important to do this for the full definition. That is, what kinds of models/analyses does the diagram in Figure 1 accept and reject?

As it stands, the definition remains very abstract, and has not demonstrated its utility with theoretical results or for empirical analysis. While the authors say it is 'straightforward to operationalize experimentally', that isn't obvious to me given its level of abstraction -- the hard part seems to be precisely in applying the high-level concept to specific cases. In other words, its not clear to me how much a commutative diagram by itself, without specifying what the sets or functions are, allows us to judge networks theoretically or develop/understand methods for interpretability. If there is a good demonstration of this, I think it should be included and highlighted.

### Questions
Is the idea behind this definition that, for any analysis trying to infer a world model, one should be able to point to components of the analysis and say, this is $\phi_1$, this is $W$, this is $g$, etc.? Or, maybe equivalently, that $Z$ only represents a world model if a commutative diagram like that exists?

### Soundness
2

### Presentation
3

### Contribution
2
