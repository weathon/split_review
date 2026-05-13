# KAAN: Kolmogorov-Arnold Activation Network --- a Flexible Activation Enhanced KAN

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Kolmogorov-Arnold Networks (KANs) have led to a significant breakthrough in the foundational structures of machine learning by applying the Kolmogorov-Arnold representation theorem. Through this approach, the target conditional distribution is expressed as the summation of multiple continuous univariate B-spline functions. The unique and complex computational structure of B-splines makes it hard to understand directly since the properties of each grid are not determined by its own parameters but are also influenced by the parameters of adjacent grids. Besides, it is challenging to trim and splice at components level under B-spline. To address this issue, we analyze the structural configurations of Multi-Layer Perceptrons (MLPs) and KANs, finding that MLP can be represented in a form conforming to Kolmogorov-Arnold representation Theorem (KAT). Therefore, we propose MLP style KAN framework Kolmogorov-Arnold Activation Network (KAAN), which is more straightforward, flexible and transferable. To verify the flexibility and transferability of our approach, we extend it to Convolutional Neural Network (CNN). Also, we demonstrate that parameter sharing is beneficial not only for efficiency but also for effectiveness. KAAN shows better representation capacity than MLP on several benchmarks. Furthermore, our experiment results lead us to conclude that this method is feasible for integrating modern network approaches such as CNNs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Authors propose Kolmogorov-Arnold activations inspired from KANs (Kolmogorov-Arnold Networks) and replace B-splines in KANs to achieve similar or better performance than MLPs. Authors show that MLPs can be represented in a form conforming to Kolmogorov-Arnold representation Theorem (KAT). Using MLP-like equipped with Kolmogorov-Arnold activations, authors experiment and compare different basis functions. Experiments also demonstrate successful integration with Convolutional Neural Networks (CNNs) which achieving comparable performance.

### Strengths
1. The paper is written clearly and concisely, and is easy to read. 
2. The proposed activation makes KANs more flexible and easy to deploy which would encourage the scientific community to experiment with these networks.
3. Experiments clearly demonstrate that the proposed activation function allows KANs to be trained while achieving comparable performance to MLPs and even ResNets.

### Weaknesses
1. Novelty is missing: KAN arxiv report (Liu et. al 2024) already gives a MLP-like interpretation of KANs which allows stacking of layers similar to MLPs which is similar to section 3 in the paper.
2. Authors have essentially replaced splines, which is a core contribution of the original KAN paper (provides higher degree of control to model univariate functions) with learnable activation functions. There is already literature covering learnable activation functions with different basis like Polynomial or sinusoidal basis (in context of MLPs). Therefore I feel the paper doesn’t bring new insights into Neural Networks or KANs.

### Questions
1. I would suggest authors to reevaluate the core contributions and rewrite the paper. If the main contribution is empirical in nature, I would suggest doing more experiments on transformer-like architectures or showing taks where MLPs or KANs fail to learn underlying functions correctly but the proposed method can.
2. What is the meaning of “KAN faces the challenges of being unintuitive and inflexible.” This is a highly subjective statement, giving concrete examples of what inflexible and unintuitive means would help readers. Does KAAN help give more flexibility or intuition? If so, how? What is the takeaway?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents Kolmogorov-Arnold Activation Networks, an extension of Kolmogorov-Arnold Networks, that uses MLP/CNN-like architecture with flexible activation functions defined for each edge between neurons.

### Strengths
1. The proposed approach clearly works on the presented tasks, and in some cases provides a performance improvement.
2. The KAAN parametrization is compatible with standard ANN architectures.
3. Related to the previous point, this parametrization might be helpful for neural architecture search/meta-learning/similar approaches that adapt neural networks’ architectures, as the nonlinearity parameters are designed to be differentiable.

### Weaknesses
2. Memory and computation time requirements

The computational requirements of KAANs appear to be much higher than for corresponding standard MLPs/CNNs. Eq. 6 uses several weights per connection (one for each activation type) and additionally parametrizes the activations. This should increase both memory consumption and running time of KAANs compared to standard networks.

The increased number of parameters in KAANs also (unless I missed something) suggests the performance improvements (Tabs. 3-5) are very modest compared to standard networks that use several times fewer parameters. 

3. Lack of interpretability

Throughout the paper, KAANs are called intuitive. However, I do understand how KAANs are more intuitive than standard MLPs (if anything, they are more convoluted). The results in Tabs. 3-5 indirectly confirm my concern: there’s no clear winner across different combinations of activation functions.

Lines 300-311 discuss the potential uses cases for each activation function, but all of those apply to standard ANN architectures that don’t define edge-based nonlinearities. 

4. Poor writing

The paper needs some writing improvements. Here are some instances I’ve noticed, although text needs overall polish.
1. [Line 30] “There were not many breakthroughs until KANs” [rephrased] – I would disagree, and suggest Transformers as an obvious architectural breakthrough. But, the list can expand with for instance capsule networks (https://www.sciencedirect.com/science/article/pii/S1319157819309322) and gflownets (https://arxiv.org/abs/2111.09266). 
2. The introduction contains many terms, such as LANs and TANs, but they’re not cited until related work. 
3. “No many” instead of “not many” in line 30, extra bracket in line 81, typo in line 205, non-plural “Experiment” name for Sec. 5

### Questions
1. What are the parameter counts/VRAM consumption/running time for the tested KAANs vs. MLPs/CNNs? 
2. Is it possible to compare KAANs with standard networks that use the same number of parameters?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel architecture named KAANs, which enhances the efficiency of MLP by incorporating a method inspired by KANs. Theoretically, the paper begins by establishing that MLPs are a subset of KANs and then deviates from traditional KANs by replacing B-spline activation functions with linear combinations of basis functions. Experimentally, the paper evaluates 7 different combinations of basis functions as activation functions across various AI-related tasks, demonstrating that KAANs achieve higher accuracy than both MLPs and KANs.

While the theoretical foundation is robust and compelling, the KAANs just replace activation functions in MLPs with more complex functions. when trying to search for the optimal combination of basis functions along with the most effective weights, the concept go back to the learnable activation functions.  Therefore, it appears that the paper has elegant theory but not enough contributions on practical level.

### Strengths
The theoretical framework is elegantly and solidly constructed.

It points out that “MLP represents a specific instance of KAN”

It points out that“any continuous univariate basis functions can be used as activation function”

KAANs offer greater flexibility and fewer limitations than traditional KANs, making them more adaptable to various structures.

The paper conducts extensive experiments across a multitude of AI-related tasks.

### Weaknesses
The paper experiments with various combinations of basis functions, where different combinations excel in different tasks. This variability raises questions about how to determine the most effective combination for a given task. Specifically, the lack of a systematic method to select basis functions introduces a significant practical hurdle. The paper does not provide clear guidelines on how to choose the optimal basis function for a new task, making the method less practical for real-world applications. The experimental results show that the performance of KAANs is highly dependent on the chosen basis functions, and without a selection method, the user is left with an impractical trial-and-error approach.

Although KAANs outperform MLPs and KANs in the experiments, the comparison may not be entirely fair. The more complex activation functions used in KAANs require greater computational power compared to MLPs, potentially skewing the results. The paper does not provide a detailed analysis of the computational cost associated with the different basis functions. Furthermore, the comparison to KANs is also problematic since KANs often require longer training times to converge. The paper does not address this discrepancy, making it difficult to assess the true efficiency of KAANs relative to KANs. A fair comparison would require either adjusting the training time or providing a more detailed analysis of the convergence rate for both methods.

### Questions
My opinion could shift towards acceptance if the authors could address one of the following points:

Develop a method to identify the most optimal combination of basis functions.

Find a specific combination of basis functions that consistently outperforms others.

Demonstrate that in certain specific tasks, KAANs offer a significant advantage.

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
The authors proposed a novel framework of viewing MLPs and a special case of KANs and proposed as a inspiration KAAN, where each nonlinear activation function is parametrized by a linear combination of basis functions. They conducted extensive experiments on challenging datasets including Tabular datasets and Cifar-10, and introduced a convolutional version as well. The article presented an interesting perspective and should be treated as a nice improvement on KANs, with the following limitations.

1. While KAAN seems interesting, it seems still such a way of parametrization of nonlinearity in KANs, with more complicated nonlinearity. This improvement is at best incremental and would need more support from numerical evidence.

2. The referee would envision that KAANs suffer from less interpretability than KANs; especially on symbolic regression. Could the authors comment on this restriction?

3. It would be interesting to elaborate more on the perspective in Sec 3.2 and gain more motivation on the comparison between KANs and MLPs.

4. How does (C)KAAN perform on more challenging tests?

### Strengths
1. The authors proposed a novel framework of viewing MLPs and a special case of KANs 

2. They conducted extensive experiments on challenging datasets including Tabular datasets and Cifar-10, and introduced a convolutional version as well.

### Weaknesses
1. While KAAN seems interesting, it seems still such a way of parametrization of nonlinearity in KANs, with more complicated nonlinearity. This improvement is at best incremental and would need more support from numerical evidence.

2. The referee would envision that KAANs suffer from less interpretability than KANs; especially on symbolic regression. Could the authors comment on this restriction?

### Questions
1. It would be interesting to elaborate more on the perspective in Sec 3.2 and gain more motivation on the comparison between KANs and MLPs.

2. How does (C)KAAN perform on more challenging tests?

### Soundness
3

### Presentation
3

### Contribution
3
