# Balancing Stability and Plasticity in Continual Learning: the readout-decomposition of activation change (RDAC) framework

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Continual learning (CL) algorithms strive to equip neural networks with the ability to acquire new knowledge while preserving prior information. However, the stability-plasticity trade-off remains a central challenge in CL. This paper introduces a framework that dissects this trade-off, offering valuable insights into CL algorithms.
The framework first addresses the stability-plasticity dilemma and its relation to catastrophic forgetting. It presents the Readout-Decomposition of Activation Change (RDAC) framework that relates learning-induced activation changes in the range of prior readouts to the degree of stability, and changes in the null space to the degree of plasticity. 
In deep non-linear networks tackling split-CIFAR-110 tasks, the framework was used to explain the stability-plasticity trade-offs  of the popular regularization algorithms Synaptic intelligence (SI), Elastic-weight consolidation (EWC), and learning without Forgetting (LwF) and replay based algorithms Gradient episodic memory (GEM), and data replay. GEM and data replay excelled in preserving both stability and plasticity, while SI, EWC, and LwF traded off plasticity for stability. The inability of the regularization algorithms to maintain plasticity was linked to them restricting the change of activations in the null space of the prior readout. For one-hidden-layer linear neural networks, we additionally derived a gradient decomposition algorithm to restrict activation change only in the range of the prior readouts, to maintain high stability while not further sacrificing plasticity. 
Results demonstrate that the algorithm maintains stability without significant plasticity loss.
The RDAC framework not only informs the behavior of existing CL algorithms but also paves the way for novel CL approaches. Finally, it sheds light on the connection between learning-induced activation/representation changes and the stability-plasticity dilemma, also offering insights into representational drift in biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Readout-Decomposition of Activation Change (RDAC) framework to analyse plasticity and stability in networks performing continual learning. The framework projects the change in network activations upto the readout layer, onto the range and null space of the readout weights. The paper then hypothesizes that changes in the range-space projection between tasks represent changes in stability while changes in the null-space represent learning without changes in stability.

### Strengths
1. The paper is clearly written for the most part, and fairly easy to follow.
2. The RDAC framework is a neat idea to examine changes in the network weights / activations, and to analyse the stability-plasticity tradeoff during learning. The framework is simple enough that it can be applied to a variety of network architectures and tasks easily.

### Weaknesses
1. To the best of my understanding, the RDAC framework _interprets_ projections onto the null and range spaces and any changes thereof as representing stability and plasticity in the networks. This seems to be a logical leap that is not verified -- the experiments in section 4 and 5 simply analyse the changes of gradient projections for different networks in these spaces. While I find the connection between the various network hyperparameters and the changes in these spaces interesting, it is not clear whether they truly represent a stability / plasticity tradeoff without experiments also showing how changes in these subspaces are correlated with performance on the continual learning tasks.

2. The linear approximation in the RDAC framework is useful and makes it easy to analyse / apply to a variety of networks. However, given that it is non-trivial to derive a similar framework for non-linear activations or readouts, it is difficult to see how insights from the current linear framework can be extrapolated to the nonlinear setting. While the paper presents results on nonlinear networks in section 4, it is not clear whether these insights will extrapolate to other nonlinear networks. 

Furthermore, there are no experiments showing how tuning the regularisation strength for SI, EWC and LwF, or memory strength / replay-buffer size for GEM to achieve a particular balance of stability and plasticity affects network performance in these tasks. This also makes it hard to judge whether the insights derived from the RDAC framework on nonlinear tasks really hold, can be extrapolated to other networks / methods and whether they are useful in developing methods for continual learning.

3. Related to point 2, while it is non-trivial to derive results for nonlinear projections, it would be good to have at least some intuition on how incorrect / applicable insights from a linear approximation would be to nonlinear networks, and whether any future endeavour to derive results for nonlinear networks could correct them.

### Questions
1. Do the changes in the range / null space truly correlate with plasticity / stability in training the networks?

2. How do we interpret insights from a linear approximation of gradient projections from a nonlinear network?

3. How bad are these linear approximations, and how can we correct them?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces the Readout-Decomposition of Activation Change (RDAC) framework to analyze the stability-plasticity tradeoff in continual learning algorithms. Readout layer is similar to the final linear probing layers in continual-learning/SSL scenarios. They perform SVD decomposition to get the range and null spaces. The main idea is that the range lets us observe stability, the more changes in that range, the less stability we have. On the other hand, changes in the null space allow plasticity for learning new tasks. Regularization methods restrict changes in both the range and null space, sacrificing plasticity for stability. In contrast, replay methods allow changes in the null space, maintaining plasticity. 
Surprisingly, it may seem like replay-based methods should exhibit substantial catastrophic forgetting, since they allow significant changes to activations in the range of prior readouts. However, the paper shows this is not the case - these methods can maintain strong stability and plasticity. Finally, for a simple linear network, they derive a gradient decomposition algorithm that projects weight updates into the null space to maximize stability without reducing plasticity.

### Strengths
- It presents a novel perspective on analyzing continual learning through the lens of readout weights and their null spaces. This provides a new tool for disentangling stability vs plasticity.

- The gradient decomposition algorithm demonstrates a concrete application of the concepts that maintains stability and plasticity. I believe this gradient update method to be the biggest potential contribution of this paper. 

- The paper is clearly written and does a good job explaining and visualizing the key ideas.

### Weaknesses
Authors acknowledged some of these limitations.

- So the explanatory power of the framework for nonlinear networks is unclear. The analysis relies on precisely computing the readout null space, which may be difficult in nonlinear models where the spaces are less well-defined. It's also unclear if the insights will fully translate when there are multiple nonlinear layers. The analysis of activation changes is quite limited for the nonlinear network experiments. They only approximate the null spaces for complicated models, analyze a single layer rather than the whole network, and observe overall trends without an in-depth study like was done for the linear case. Specifically, the method relies on an SVD of the readout weights to define the range and null spaces, but in deep networks, the notion of a 'readout layer' becomes less clear. The authors analyze only the final layer before the classification, but it's not clear if the same analysis would hold for intermediate layers, or how the null space of one layer relates to the null space of another.

- The continual learning scenarios are relatively simple (Split CIFAR and MNIST). Needs more exploration on complicated dataset benchmarks and continual learning scenarios. The current experiments do not fully demonstrate the practical applicability of the method in more complex, real-world scenarios. The datasets used are relatively small and do not fully capture the challenges of more complex continual learning problems.

- No comparison against latest SOTA.

### Questions
If the authors are able to answer most of the questions and are able to further develop their algorithms as requested, this paper could significantly improve. This paper could have potential. The questions are very closely related to the weakness. 

- 1. You mention that your work is related to representational drift in biological networks. More details on the biological connections and plausibility of the concepts will be helpful.

- 2. Do you have ideas for extending gradient decomposition algorithms to deep nonlinear networks?

- 3. You propose the readout null space allows plasticity for new tasks. But how can you formally quantify or guarantee the capacity for plasticity? (Aka I want to see more maths justifying that the null space gives us plasticity. Information theory perspectives or more experimental results might help).

- 4. Any performance guarantees of your proposed optimization algorithm?

- 5. Please comment on any links to PCA, information theory, information bottle neck theory, rate-distortion theory etc. Some helpful pointers:

  - a. PCA

    - i. PCA finds the principal components that capture the directions of maximum variance in a dataset. The readout range identified in this paper spans the subspace aligned with the readout weights. So both are identifying meaningful linear subspaces in high-dimensional data.

    - ii. The readout null space identified is analogous to the null space in PCA - directions that have no variance or are unimportant for the purposes of reconstruction/readout.

  - b. Rate-distortion theory:

    - i. Replay methods allow greater changes in the null space (less compression), maintaining plasticity. Regularization methods over-compress, losing plasticity.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces the Readout-Decomposition of Activation Change (RDAC) framework, which aims to address the stability-plasticity trade-off in continual learning (CL) algorithms. This trade-off is a significant challenge in preserving prior information while acquiring new knowledge. The RDAC framework dissects this trade-off by linking learning-induced activation changes to stability and plasticity, thereby offering insights into CL algorithms.

Moreover, This paper presents a gradient decomposition algorithm for one-hidden-layer linear neural networks. This algorithm restricts activation changes within the range of prior readouts, maintaining stability without significant loss of plasticity.

The RDAC framework sheds light on the connection between learning-induced activation changes and the stability-plasticity trade-off, providing insights into representational drift in biological systems. The results show that GEM and data replay preserved stability and plasticity, while SI, EWC, and LwF traded off plasticity for stability.

### Strengths
The Readout-Decomposition of Activation Change (RDAC) framework addresses the stability-plasticity dilemma and its relation to catastrophic forgetting, and relates learning-induced activation changes to the degree of stability and plasticity. The paper contributes to ongoing efforts in understanding and solving the complexities of continual learning.


The paper also presents a gradient decomposition algorithm for one-hidden-layer linear neural networks to maintain high stability without sacrificing plasticity. Overall, the RDAC framework provides valuable insights into CL algorithms and offers potential for novel CL approaches.

### Weaknesses
Theoretical analyses on one-hidden-layer linear neural networks are not scalable or too instructive.

This paper lacks empirical results, comparisons, and practical implications, which could limit its applicability in real-world scenarios.

The paper focuses primarily on evaluating existing CL algorithms and does not propose any new algorithms or techniques.

Lack of code and hyper-parameter configuration.

### Questions
Have you considered evaluating the RDAC framework on other CL datasets or tasks? It would be interesting to see how the framework performs in different settings and if the results hold across a broader range of scenarios.

It would be helpful to have more empirical results and comparisons with other frameworks or approaches to validate the effectiveness of the RDAC framework. Are there any plans to conduct such experiments in the future?

How generalizable is the gradient decomposition algorithm for linear neural networks? Can it be extended to more complex network architectures, such as deep neural networks, and still maintain stability without sacrificing plasticity?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper considered balancing the learning forgetting trade-off in continual learning. Specifically, this paper considered the changement of representation \delat_h into two parts, the range of readout and Null space of readout space (maintains stability).  Then this paper derived a gradient decomposition algorithm to explicitly control the learning-forgetting trade-off. Empirical results demonstrated improved trade-off.

-----Post-rebuttal update
I would appreciate authors' efforts, which addressed my concerns. I would maintain my current evaluation.

### Strengths
**Disclaimer: I did not work on continual learning and thus I could not evaluate the novelty/significance parts of this paper.**  Below is my evaluation from a general view.

I would think this paper presents a clear and interesting analysis in the learning/forgetting trade-off in continual learning, which seems quite important in continual learning. I would agree with the authors with their analysis on the representation decomposition (Fig 1). 

The experimental parts clearly demonstrated the benefits of such an analysis by a better trade-off.

### Weaknesses
I would think the clarity part in gradient decomposition could be better elaborated. I would think a clear algorithm should be presented to show how to explicitly control the learning/forgetting trade-off.

### Questions
See the weakness parts.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
