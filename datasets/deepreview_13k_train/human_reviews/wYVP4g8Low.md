# Local Control Networks (LCNs): Optimizing Flexibility in Neural Network Data Pattern Capture

- Decision: Reject
- Scores: 5, 1, 3, 3

## Abstract
The widespread use of multilayer perceptrons (MLPs) often relies on a fixed activation function (e.g., ReLU, Sigmoid, Tanh) for all nodes within the hidden layers. While effective in many scenarios, this uniformity may limit the network’s ability to capture complex data patterns. We argue that employing the same activation function at every node is suboptimal and propose leveraging different activation functions at each node to increase flexibility and adaptability. To achieve this, we introduce Local Control Networks (LCNs), which leverage B-spline functions to enable distinct activation curves at each node. Our mathematical analysis demonstrates the properties and benefits of LCNs over conventional MLPs. In addition, we demonstrate that more complex architectures, such as Kolmogorov–Arnold Networks (KANs), are unnecessary in certain scenarios, and LCNs can be a more efficient alternative. Empirical experiments on various benchmarks and datasets validate our theoretical findings. In computer vision tasks, LCNs achieve marginal improvements over MLPs and outperform KANs by approximately 5%, while also being more computationally efficient than KANs. In basic machine learning tasks, LCNs show a 1% improvement over MLPs and a 0.6% improvement over KANs. For symbolic formula representation tasks, LCNs perform on par with KANs, with both architectures outperforming MLPs. Our findings suggest that diverse activations at the node level can lead to improved performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the use of B-spline functions to enable distinct, learnable activation curves at each node in a neural network, arguing that fixed activation functions limit a model's ability to capture complex data patterns.

### Strengths
- The method, though loosely inspired by Kolmogorov–Arnold Networks (KANs), is novel and presents an interesting approach to adaptive activation functions.
- The mathematical formulation is thorough, and the description is clearly articulated, making the technical details easy to follow

### Weaknesses
 - Comparisons with MLPs and KANs show only marginal improvements. The limited performance gains cast doubt on the practical utility of LCNs, given their added complexity. Specifically, the reported 1% average improvement over MLPs on basic tasks is not substantial enough to justify the increased architectural complexity. Furthermore, while the authors claim better performance than KANs in computer vision tasks, the 5% improvement is still modest, and it's unclear if this advantage holds across a wider range of datasets and network configurations. The lack of a more significant performance boost raises concerns about whether the added complexity of learnable activation functions is truly warranted.
- Throughout the paper, the authors claim that LCNs improve explainability, yet they do not provide any concrete example to illustrate how  LCNs would be more interpretable than other methods. A real example would significantly strengthen this claim. The assertion that individual neurons specialize in detecting features like edges or textures is not substantiated with any visualization or analysis of the learned B-spline functions. Without empirical evidence, this claim remains speculative. It is necessary to show how the learned B-spline functions can be analyzed to provide insights into the model's decision-making process.
- The authors present theoretical arguments for efficiency, such as sparse gradient updates, but there’s no indication of how this translates to actual hardware efficiency. Theoretical sparsity may not correspond to measurable hardware speedups, which is a critical consideration for practical use. The claim that LCNs have the potential for reduced computational load is not supported by any experimental data on actual hardware. The authors need to demonstrate that the theoretical sparsity translates into tangible benefits in terms of training time or energy consumption.

**Minor**
- While the authors suggest LCNs are "simple," the architecture is still complex compared to conventional activation function setups in MLPs.
- There are a few typos (e.g. "putting it" on line 51 -> "putting them." (?))

### Questions
Maybe I'm missing something but why do the models in Figures 3 and 4 etc. vary in the number of parameters? Shouldn't they be standardized to the same number of parameters for a fair comparison?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper introduces Local Control Networks (LCNs), a novel neural network architecture that replaces the traditional fixed activation functions with adaptive, node-specific B-spline functions. The authors argue that using a uniform activation function across all nodes in MLPs limits expressiveness and adaptability. Using B-spline-based activations in each node, LCNs aim to enhance flexibility and enable more localized pattern capture, potentially improving performance and computational efficiency.

### Strengths
1. using variable activation functions has been recently popularized by KANs but KANs have a high computational burden. The proposed methods seems to be more computationally efficient
2. local support property for localized updates and robustness to input perturbations is important in certain areas.

### Weaknesses
1. While the paper has been written in a beginner-friendly manner, almost 2 pages are dedicated to writing out the simple chain rules derivative expressions which most readers familiar with ML would be aware of. It would have been better to use that space to provide more experimental details.
2. Sevaral claims like " LCN exhibited faster learning" aren't backed up by numbers.
3. KANs have been shown to not work well for vision tasks, once the problem complexity increases (https://arxiv.org/abs/2407.16674), why won't LCNs suffer from the same issue? Especially given the current experiments which are extremely basic and problems where MLPs achieve near-perfect accurary.
4. Fig 3 arbitrarily stops the number of parameters for MLPs at a low value while scaling the same for LCNs
5. "This flexibility improves the network’s capacity to capture both global and localized data patterns, resulting in enhanced accuracy
and efficiency across a range of tasks." -- The paper doesn't really show any performance (accuracy or otherwise) improvement over MLPs, so these claims need to be seriously reconsidered.

### Questions
See weaknesses for more details

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to use B-Splines instead of fixed activation functions in neural networks. They explain the idea, derive a formulation and show some empirical results.

### Strengths
The paper is very well written and, mostly, easy to follow. The question whether distinct activation functions confer a benefit to neural networks is an interesting, albeit theoretical question (research into architectures and activation functions has become of less interest, since the ML community realized that compute/scale is the single most important performance factor).

### Weaknesses
The empirical results do not match the confident presentation. The performance of LCNs is mixed, sometimes better / sometimes worse than MLPs and KANs. The analysis suggests explanations and theoretical insights without going into any real detail. Many sections read like they were written by an **LLM** trying to convince, rather than actually understand and explain - see questions below. See, e.g., line 195: 'The authors define ... to support the use in the LCN model.' (seriously?)

MLPs with ReLUs have universal approximation capabilities, so it does not makes sense to argue for a need for more flexible nonlinearities. The argument that fixed activation functions lack adaptability is not sufficiently justified, given that the network learns the weights that determine the input to the activation function; this should provide sufficient flexibility.

49: The motivation of KANs was not to provide more flexible activation functions.

53: multiple activation functions also coexist in KANs.

Fig 1: top left, typo

ReLUs have 0 gradient for any input <0, how is this not a vanishing gradient problem? The explanation that the gradient is 1 for positive inputs does not address the issue of dead neurons and the resulting sparsity of gradient updates. The authors need to clarify how this sparsity is addressed by their method.

Fig 1: What *exactly* does it mean that different input feature patterns are treated differently? The explanation that B-splines learn adaptive functions to activate different patterns is vague and needs more detail. How does this differ from the way standard networks learn features?

Fig 1: Why should lead localized support of the activation function lead to sparse gradients? The explanation that only a subset of neurons is activated does not explain why this is necessarily sparse, as opposed to simply a different activation pattern.

114: 'capturing subtle patterns', this has been confusing me multiple times: The role of a nonlinearity is to help the model perform computation on the inputs; The authors seem to suggest that it is used to model the data manifold instead? This may be the case in some ML settings, but certainly not on any of the standard datasets used in the paper, where the task is just to compute something given the inputs.

139-143: how is this connected to the paper?

144-151: The explanation of KANs needs much more detail, especially since they are quite relevant to this paper

386: This contradicts the earlier sections on KANs being compact and efficient? The authors need to clarify the practical limitations of KANs that lead to this contradiction.

404: What exactly do you mean with 'high dimensional noise that makes KANs falter'? The explanation that KANs are sensitive to noisy features is not sufficient. How does this sensitivity manifest, and why are LCNs more robust?

447: LCNs are not consistently better?!?

Where are the symbolic regression results?

### Questions
ReLUs have 0 gradient for any input <0, how is this not a vanishing gradient problem?

Fig 1: What *exactly* does it mean that different input feature patterns are treated differently? 

Fig 1: Why should lead localized support of the activation function lead to sparse gradients?

114: 'capturing subtle patterns', this has been confusing me multiple times: The role of a nonlinearity is to help the model perform computation on the inputs; The authors seem to suggest that it is used to model the data manifold instead? This may be the case in some ML settings, but certainly not on any of the standard datasets used in the paper, where the task is just to compute something given the inputs.

139-143: how is this connected to the paper?

144-151: The explanation of KANs needs much more detail, especially since they are quite relevant to this paper

386: This contradicts the earlier sections on KANs being compact and efficient?

404: What exactly do you mean with 'high dimensional noise that makes KANs falter'?

447: LCNs are not consistently better?!?

Where are the symbolic regression results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present Local Control Networks (LCNs), which uses B-spline-based activation functions to provide node-wise diversity in activation functions across a single layer. The authors argue that allowing each neuron to have a unique activation function provides more flexibility and adaptability, which enhances the network's ability to capture complex data patterns. The paper compares LCNs with Kolmogorov–Arnold Networks (KANs) and traditional Multi-Layer Perceptrons (MLPs), showing some improvements in performance, convergence speed, and computational efficiency, particularly in basic machine learning and computer vision tasks.

### Strengths
1)  The use of B-spline functions for neuron-specific activation provides a novel way of allowing each neuron to adapt its behavior, which is promising for capturing complex and localized patterns in data.

2) The non-linearity is preserved. The issue with ReLU, where the neurons get stuck with zero gradient, is resolved here. The vanishing gradient issue faced with tanh and sigmoid functions is also resolved here.

3) The dropout mechanism is also automatically implemented with B-spline, reducing the unexpressive nodes to zero.

4)  The paper provides empirical results comparing LCNs with KANs and MLPs across multiple benchmarks, including basic ML tasks, computer vision datasets (MNIST, FMNIST), and symbolic regression tasks.

5) The local support property of B-splines reduces the impact of irrelevant neurons on the gradient, leading to a form of regularization that helps improve generalization and potentially reduces overfitting.

Overall, the idea is certainly interesting and seems to have some compute advantages over KANs and accuracy advantages over MLPs.

### Weaknesses
1) The paper could be written better. There are lots of repeated lines and not enough explanation. Many of the notations are not explained in terms of what they represent, specially in the equations.

2) Figure 1, with comparisons between MLP and LCN, was well formed. I would have liked to see the comparison between LCN and KAN in a similar way, as it is the SOTA work being referred to in every section.

3) Explanation and visualization of B-spline could have been given (optional).

4) While it is mentioned that LCNs are more computationally efficient than KANs, the empirical evidence supporting this is minimal, and the figures comparing LCNs and KANs lack sufficient metrics. There is no detailed figure-wise analysis of how B-spline activations compare with KAN's univariate function combinations.

5) There is no ablation study that explores the impact of different B-spline configurations (e.g., degree of the spline, number of basis functions) on the performance of LCNs. Such a study would be critical to understand the role of the various components in the model's success.

6) The numbers for experiments in symbolic representation tasks are not given. It is just mentioned in text that the LCN performs superior. It would be useful to say the margin by which it will perform better.

7) The experiments are wrt to the LCN, and MLP mostly. It would be interesting to see the difference in expressive power between CNNs and LCNs in the image classification tasks with MNIST and FMNIST.

### Questions
1) How much computational overhead does LCNs have over MLPs and CNNs?

2) Could you provide ablations with different B-spline configurations?

3) Can you prove mathematically that such network converges well? (optional)

4) It would help if the numbers in the symbolic representation tasks were given.

5) Could you give a detailed comparison with KANs?


I think the novelty in the paper is interesting and could be explored further and well-analyzed in order for the paper to emerge as a good paper.

### Soundness
2

### Presentation
2

### Contribution
2
