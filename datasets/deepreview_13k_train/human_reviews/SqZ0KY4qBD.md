# Attention with Markov: A Curious Case of Single-layer Transformers

- Decision: Accept
- Scores: 8, 10, 5, 6

## Abstract
Attention-based transformers have achieved tremendous success across a variety of disciplines including natural languages. To deepen our understanding of their sequential modeling capabilities, there is a growing interest in using Markov input processes to study them. A key finding is that when trained on first-order Markov chains, transformers with two or more layers consistently develop an induction head mechanism to estimate the in-context bigram conditional distribution. In contrast, single-layer transformers, unable to form an induction head, directly learn the Markov kernel but often face a surprising challenge: they become trapped in local minima representing the unigram distribution, whereas deeper models reliably converge to the ground-truth bigram. While single-layer transformers can theoretically model first-order Markov chains, their empirical failure to learn this simple kernel in practice remains a curious phenomenon. To explain this contrasting behavior of single-layer models, in this paper we introduce a new framework for a principled analysis of transformers via Markov chains. Leveraging our framework,  we theoretically characterize the loss landscape of single-layer transformers and show the existence of global minima (bigram) and bad local minima (unigram) contingent on data properties and model architecture. We precisely delineate the regimes under which these local optima occur. Backed by experiments, we demonstrate that our theoretical findings are in congruence with the empirical results. Finally, we outline several open problems in this arena. Code is available at \url{https://anonymous.4open.science/r/Attention-with-Markov-A617/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors study a curious case of transformers via Markov Chains, in which one-layer transformer struggles to find the global minimum in the Markov task. They further provide theoretical and empirical studies, showing that weight tying can lead to bad local minima when Markovian switching is greater than one. They also extend the results to multi-state Markov Chains. Experiments in multi-layer transformers further show that they can reach the global minimum, which is an intriguing future direction.

### Strengths
1. The problem setup is interesting and concise.
2. The presentation is clear. 
3. The analysis is solid, containing both theory and extensive experiments.

### Weaknesses
The attention structure is missing here. Specifically, the Markov chain requires no attention structure, nor does theoretical analysis include the attention layer. It is more like "MLPs with Markov" instead of "attention with Markov". The paper does not sufficiently explore the role of the attention mechanism, which is a core component of transformers. The analysis focuses on the skip connection and the MLP layers, essentially treating the transformer as a complex MLP with a potentially redundant attention layer. This raises questions about the necessity of using a transformer architecture for the Markov chain task, given that the attention mechanism appears to be largely unused in the single-layer case. The theoretical analysis should also consider the attention layer's influence, even if it is minimal, to provide a more complete picture of the model's behavior.

### Questions
1. Can authors comment on the role of attention layers in the paper?
2. Can authors present the attention patterns of the transformers trained the Markov tasks?
3. If time permits, can authors train pure MLP layers on the Markov task?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper establishes a general and novel framework for the theoretical and empirical study of the attention mechanism on Markov data. They theoretically show that for one layer of Transformers, if the data comes from a Markov chain with binary states and transition probability given by P = (1-p, p \\ q, 1-q), the global minima of the next-token cross-entropy loss can recover the optimal risk. They theoretically show that there exist bad local minima with weight tying if p+q > 1, and without weight tying, local minima become saddle point. Empirically, they validate the theory and show those saddle point can be avoided if without weight tying. They also present experimental results on multi-state Markov chain and mention some open problems about deep Transformers.

I really like this paper. I think the framework is novel, interesting, and worth investigating. The theoretical and empirical results are solid, and the presentation is particularly clear. Although this is very initial research, they propose some future directions about why single-layer Transformers can sometimes be trapped in bad local minima when trained on the Markov data, and why deep Transformers can behave well and avoid local minima or saddle point. I think we should encourage this style of theoretical research since there are too much theoretical research with complex setups and heavy math, that explains nothing at all.

### Strengths
1. The theoretical results are solid and can be validated via experiments.

2. They establish a novel framework to investigate the attention mechanism on Markov data.

3. The presentation is particularly clear and comfortable.

### Weaknesses
Current, I do not see any big issues.

### Questions
/

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a framework for learning a first-order Markov chain using a single-layer transformer. Within this framework, the authors characterize the network’s loss landscape, identifying the presence of both global and bad local minima.

### Strengths
1. Examining the limitations of a single-layer transformer in learning a simple Markov kernel is an intriguing aspect of this work.

2. The authors characterize the roles of Markov switching probabilities and weight-tying in contributing to the presence of local optima.

3. Extensive experimental results are provided to support the theoretical insights

### Weaknesses
The main limitation of this paper is that the current results may not fully address their central question: systematically characterizing the learning gap of a single-layer transformer. The authors show that a bad local minimum exists when $p+q > 1$, but they do not rule out the possibility that only global optima exist when $p+q < 1$. Given that the results are primarily existence arguments, this does not entirely support the empirical observation that the transformer converges to a bad minimum in the $p+q > 1$ regime while learning the global minimum in the $p+q < 1$ regime. This implicit bias would benefit from additional theoretical support, such as insights from learning dynamics.  Moreover, the data model is overly simplified, which raises expectations for a more rigorous analysis that fully characterizes the solution learned by transformers rather than relying on existence arguments alone.



### Questions
1. See weakness.

2. In the proof sketch of Theorem 2 (line 363), the authors set $\mathbf{e} = \mathbf{a} = 0$, which implies that for the uni-embedding (line 213), $\mathbf{x}_n$ depends solely on the position encoding and lacks information from the state $x_n$. If I understand correctly, this setup could lead to problematic solutions for the model, as it is unable to fully utilize input information—potentially independent of the effects of weight tying. Could the authors clarify this point?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new framework for analyzing transformers through the lens of Markov chains, which is a novel and theoretically rich approach. This framework enhances our understanding of how transformers handle sequential data, particularly first-order Markov processes. Specifically, the theoretical characterization of the loss landscape for single-layer transformers, identifying the presence of both global minima (bigram) and bad local minima (unigram), is a good contribution. This helps explain the empirical observations and provides a solid foundation for future work.

### Strengths
+ The theoretical results are novel and informative.

+ The experiments are well-designed, providing solid support of the considered insights.

### Weaknesses
I found no explicit assumptions in the paper, which may imply that few assumptions are utilized in the theoretical analysis. Thus, I suggest that the authors list the assumptions that were used.

The set of words under consideration is too toyish, which is the primary concern.

### Questions
Could the authors clarify the difference between the following work [1] and the proposed results?

[1] Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality. COLT, 2024.

### Soundness
3

### Presentation
3

### Contribution
2
