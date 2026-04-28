# Incidental Polysemanticity: A New Obstacle for Mechanistic Interpretability

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Polysemantic neurons — neurons that activate for a set of unrelated features — have been seen as a significant obstacle towards interpretability of task-optimized deep networks, with implications for AI safety. The classic origin story of polysemanticity is that the data contains more "features" than neurons, such that learning to perform a task forces the network to co-allocate multiple unrelated features to the same neuron, endangering our ability to understand networks' internal processing. In this work, we present a second and non-mutually exclusive origin story of polysemanticity. We show that polysemanticity can arise incidentally, even when there are ample neurons to represent all features in the data, a phenomenon we term incidental polysemanticity. Using a combination of theory and experiments, we show that incidental polysemanticity can arise due to multiple reasons including regularization and neural noise; this incidental polysemanticity occurs because random initialization can, by chance alone, initially assign multiple features to the same neuron, and the training dynamics then strengthen such overlap. Our paper concludes by calling for further research quantifying the performance-polysemanticity tradeoff in task-optimized deep neural networks to better understand to what extent polysemanticity is avoidable.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper investigates the emergence of polysemanticity in neural networks, demonstrating that it arises not solely from bottleneck dimensions (extending Elhage et al.'s work). The authors propose that incidental polysemanticity occurs during random initialization and early training, providing mathematical derivations to support this claim.

### Strengths
- The paper focuses on origins for polysemanticity, a central and important problem in mechanistic interpretability
- The paper provides thorough walkthroughs of mathematical derivations and explains individual resulting terms (feature benefit, interference, regularization)

### Weaknesses
In general, I am unsure about the weight of novel contributions in this paper relative to the bar of an ICLR acceptance. I will defer to the AC in this regard.

Critiques on Section 1, L1 Regularization
I am not surprised that random initialization determines whether true features are encoded monosemantic or binary. The authors clearly show how random initialization arguments are reflected in experiments on training dynamics and scaling the number of hidden neurons. However, I am unsure how these findings translate into language models, which are not explicitly trained with an L1 regularization.

Critiques on Section 3, Neural Noise
- Without context from Elhage et al. it is unclear, why kurtosis is the main metric tracking sparsity in this context. An accompanying background section motivating kurtosis would be useful
- Section 3.2 quickly summarizes the mathematical analysis of this section. A motivation of why highlighting bipolar noise would be useful. (Gaussian noise is a natural choice)

### Questions
--

### Soundness
3

### Presentation
3

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
Polysemanticity describes the quality of an internal feature/neuron in which the feature will have a high activation for multiple features, indicating that the feature is associated with more than one feature. The prevailing theory on polysemanticity is that it is necessary: when the feature space is smaller than the number of features, then neurons must represent multiple features. This paper explores the possibility that polysemanticity may not occur necessarily, but as a feature of training. Particularly the paper looks at sparsity enforcement in the hidden layer, and observes unnecessary and random, or incidental polysemanticity.

### Strengths
Toy model is illustrative and easy to apprehend.
In-depth and accessible discussion in section 2.
Favorable results matching theory in section 2.
Well written and easy to follow.

### Weaknesses
The examples for incidental polysemanticity are explored with L1 regularization of internal representation, or noise injections, and when the feature dimension is larger than necessary. The main question is why polysemanticity occurs in typical settings, and it is unclear how these results apply to the more typical scenarios. This lessens the paper's contribution significance. This paper could be improved by elucidating more how the content applies to more typical scenarios or providing content more in alignment with those scenarios.

Section 3/4 discuses how noise is tied to sparsity, but does not verify that noise is tied to polysemanticity. The paper could be improved by providing experiments showing how noise causes incidental polysemanticity.

### Questions
I don't see any baseline polysemantic neurons count for your model, with no regularization or noise. Is this because there is no way to define them, as there is no winner-takes-all enforcement? It would be beneficial to establish some sort of baseline.

Section 4, on noise injections, explains the relationship between noise injections and sparsity, but I fail to see a discussion on what this has to do with polysemantic neurons. Are there experiments on the number of incidentally polysemantic neurons with noise injections? This would be beneficial.

Is there an example of incidental polysemantic neurons when m < n, or the feature space is smaller than the required number of features? This would help move the scenario of the ecperiemnt closer to what is typical.

Can you explain how incidental polysemanticity with L1 regularization relates to the base case? Is it that the scenario where the feature space dimension is much smaller than the number of features is similar to a scenario with feature sparsity? Making this more clear would help readers understand your contribution.

Can you explain how noise injections relate to explaining the cause of polysemanticity in the typical case? Perhaps I be unfamiliar with how common these types of noise injections are.

An interesting experiment (if they have not been done) is to train an autoenoder in a more normal scenario: without regularization, noise, and with m < n. Then check if the number of polysemantic neurons is greater than n-m. If so, then this could be evidence of incidental polysemnticity in a typical scenario.

Minor Issues:
051) In that case
135) By $W_i = f_i$ , do you mean $W_i=e_i$?
Figure 3, graph not displaying range bars for last two points.

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
Polysemantic neurons that are activated by different natural concepts have attracted the attention of researchers recently due to their influence on feature interpretability. In this paper, the authors introduce a new scenario where polysemanticity might be caused by non-task factors in the training process. In the toy models, they consider two conditions. i.e., the $l_1$ training regularization and hidden layer noise. With the theoretical and empirical evidence, they reproduce the polysemanticity in the toy models and analyze the learning dynamics in the training process.

### Strengths
1. The theoretical analysis of the training dynamics in toy models is solid and cooperates well with the empirical evidence.
2. The paper is well-organized and easy to follow. The main insight is clear and the two conditions in the toy models are explained well.
3. Analyzing the mechanism of polysemantyicity is important and this paper proposes an insightful perspective.

### Weaknesses
1. This paper focuses on the polysemanticity that is not related to the tasks. It would be better to add more discussions on the differences between incidental polysematicity and the original task-related polysemanticity. For example, as polysemanticity is not related to the tasks, can we get rid of the performance-interpretability trade-off? Besides, in the neural networks, how can we distinguish the incidental polysemanticity?
2. The analysis in this paper is conducted on the toy models. I understand it is for the ease of theoretical analysis. However, it would be better to provide some insights into the polysmenaticity in the neural networks trained on real-world data and add some additional experiments or discussions.
3. The explanation and motivation of Figure 6 is a little confusing and it is perhaps a digression from the main topic of the paper. It would be better to provide more discussions of the new insights.
4. In this paper, the authors mainly focus on how to obtain polysemantic neurons. However, in real-world data, the main challenge lies in obtaining the monosemantic neurons. Consequently, is it possible to provide some insights about how to attain monosemanticity based on the analysis in this paper?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
