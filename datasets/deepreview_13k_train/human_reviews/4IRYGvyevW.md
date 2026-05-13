# Beyond the Lazy versus Rich Dichotomy: Geometry Insights in Feature Learning from Task-Relevant Manifold Untangling

- Decision: Reject
- Scores: 6, 6, 5, 5, 6

## Abstract
The ability to integrate task-relevant information into neural representations is a fundamental aspect of both human and machine intelligence. Recent studies have explored the transition of neural networks from the *lazy* training regime (where the trained network is equivalent to a linear model of initial random features) to the *rich* feature learning regime (where the network learns task-relevant features). However, most approaches focus on weight matrices or neural tangent kernels, limiting their relevance for neuroscience due to the lack of representation-based methods to study feature learning. Furthermore, the simple lazy-versus-rich dichotomy overlooks the potential for richer subtypes of feature learning driven by variations in learning algorithms, network architectures, and data properties.

In this work, we present a framework based on representational geometry to study feature learning. The key idea is to use the untangling of task-relevant neural manifolds as a signature of rich learning. We employ manifold capacity—a representation-based measure—to quantify this untangling, along with geometric metrics to uncover structural differences in feature learning. Our contributions are threefold: First, we show both theoretically and empirically that task-relevant manifolds untangle during rich learning, and that manifold capacity quantifies the degree of richness. Second, we use manifold geometric measures to reveal distinct learning stages and strategies driven by network and data properties, demonstrating that feature learning is richer than the lazy-versus-rich dichotomy. Finally, we apply our method to problems in neuroscience and machine learning, providing geometric insights into structural inductive biases and out-of-distribution generalization. Our work introduces a novel perspective for understanding and quantifying feature learning through the lens of representational geometry.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a geometric framework to examine the manifold of neural network representations, providing insights into the distinctions between lazy and rich training regimes in feature learning. Specifically, it revisits the manifold capacity concept introduced in Chung et al. (2018), theoretically demonstrating that manifold capacity can serve as an indicator of the underlying richness in feature learning. Based on empirical studies using synthetic data and two-layer neural networks, observations are made regarding the relationship between manifold capacity and the degree of feature learning, as well as the stages of feature evolution. The proposed geometric measures are further applied to neural networks in neuroscience and out-of-distribution generalization tasks to explore the broader implications of this approach.

### Strengths
- The novel application of manifold capacity and other effective geometric measures to investigate the lazy-vs-rich dichotomy is intriguing. It shows better alignment with the degree of feature learning compared to other metrics, such as weight changes or NTK-label alignments.
- Most of the derivations seem correct, though I could not verify every detail.

### Weaknesses
 - The theoretical derivation relies on a one-step gradient argument, but the fact is not mentioned in the manuscript. Moreover, the link between Theorem 2’s results and the increase in feature learning degree is not entirely clear, and additional commentary could enhance clarity. Specifically, the connection between the manifold capacities defined in Sections 2.1 and 2.2 and those discussed in Theorems 1 and 2 remains unclear. The manuscript would benefit from a more explicit explanation of how these different capacity definitions relate to each other and how they collectively support the claims about feature learning.
- It would be helpful to discuss the generalizability of the observations, such as those in Figure 4. Various hyperparameters (e.g., the choice of optimization algorithms, weight initialization methods, batch size, learning rate, and scheduling) could influence implicit biases in the algorithm, affecting neural representations, geometric metrics, and even the stages of learning.

- Regarding the proposed effective geometric measures to explain capacity changes, are there standard reference lengths compared to the radius? A simple manifold radius magnitude may not accurately capture the problem's complexity when the differences between manifold means scale identically.
- Additionally, the definitions and implications of axes alignment, center alignment, and center-axes alignment are less discussed compared to radius and dimensionality (e.g., in Figures 5b, 6c).
- When using geometric measures, which layer(s) should be analyzed? Are the results consistent across different layers?

- A minor comment: In Lines 170–171, the variable $\mathbf{s}$ is not properly defined in the text.

### Questions
- Regarding the proposed effective geometric measures to explain capacity changes, are there standard reference lengths compared to the radius? A simple manifold radius magnitude may not accurately capture the problem's complexity when the differences between manifold means scale identically.
- Additionally, the definitions and implications of axes alignment, center alignment, and center-axes alignment are less discussed compared to radius and dimensionality (e.g., in Figures 5b, 6c).
- When using geometric measures, which layer(s) should be analyzed? Are the results consistent across different layers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors focus on the feature learning in deep learning. They use manifold capacity as a metric to quantify the degree of richness of feature learning. Experiment results show that such capacity can reveal different learning stages in different settings. They also apply this to problems in neuroscience and out-of-distribution tasks.

### Strengths
-	Understanding feature learning in deep learning is an important and interesting research problem.
-	The paper proposes a metric called manifold capacity to measure the feature learning progress, which seems to be new.
-	Several experiments in different domains are presented to support the claim.

### Weaknesses
### weaknesses:
- Figure 2c lacks a clear explanation. The operations depicted are not defined, making it difficult to understand their meaning or purpose in the context of manifold capacity.

- Equation (1), defining model capacity, is confusing. It is unclear whether the manifolds {\mathcal{M}_i} are predefined or change as N increases. If they change, the selection process for these manifolds is not specified. Additionally, the range of values for y_i is not defined.

- Appendix C, which presumably details the computation of manifold capacity, introduces undefined notations such as T and λ. This lack of clarity hinders the reader's ability to understand the computational process.

- The method for computing manifold capacity should be included in the main text. At the very least, the conditions under which these values are computed should be explicitly stated. It is implied that exact computation is not possible without certain assumptions, but these assumptions are not mentioned.

- Theorem 1's statement in the main text is potentially misleading. The appendix reveals that these results are only proven for a single gradient step update. While extending beyond this is acknowledged as technically challenging, the main text should clarify this limitation to avoid misinterpretation.

- In section 3.2 and Figure 3b, the definitions of "wealthy" and "poor" regimes are unclear, as is their relationship to the input dimension. The presence of task-relevant features at initialization is also not adequately explained. Furthermore, the minimal change in the purple line representing capacity in Figure 3b during training is difficult to interpret. Does this imply that feature learning only changes slightly?

- Section 4 is difficult to follow, likely due to the missing definitions of metrics such as dimension and radius. Without these definitions, it is challenging to understand the analysis presented.


Typo:

- Line 173, $o_N(1) \to 1$ -> $o_N(1) \to 0$

### Questions
-	There seems to be no explanation for Figure 2c. I don’t know what does those operations mean.
-	I’m a bit confused about eq (1), the definition of model capacity. Are the manifold $\{\mathcal{M}_i\}$ predefined or they are changing when $N$ is increasing. If they are changing, how do you choose them? Also, what values should $y_i$ take?
-	When looking at Appendix C for the way to compute manifold capacity, several notions seem to be not defined, such as $T$, $\lambda$.

-	I believe the way of computing manifold capacity should be mentioned in the main text, or at least mentioned under what conditions are those values computed (I believe they cannot be exactly computed unless some conditions are assumed).

-	For Theorem 1, when looking at the actual statement in appendix, these results are proved only under the setting that with one gradient step update. Though it is understandable that going beyond this is technically difficult, I feel the statement in the main text gives the reader a wrong impression.

-	In section 3.2/figure 3b, it’s not clear to me what the definition of wealthy and poor regime are and how they are related to the input dimension. Also, I’m not sure why at initialization there will be task-relevant features (and I don’t know what are task-relevant features in this setting). Moreover, the purple line in capacity in figure 3b changes only a little bit throughout the training, I’m not sure how to interpret this (feature learning only changes a little?).

-	It’s a bit hard for me to follow section 4, presumably because the definition of these metric (e.g., dimension, radius,…) are missing.


Typo:

-	Line 173, $o_N(1) \to 1$ -> $o_N(1) \to 0$

### Soundness
2

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
2

### Summary
This paper proposed that manifold capacity is a better way to identify the process of feature learning than commenly used rich-lazy dichotomy. This claim is theoretically proved in a limited setting, and empirically verified.

### Strengths
- The idea of catching the richness by manifold capacity is potentially useful.
- The experiments verifies that manifold capacity captures different stages of learning.

### Weaknesses
 - The presentation is very confusing. For example, in the experiments, there are several critical measures, such as effective radius, dimension, center alignment etc. but they are not defined (at least not in the main paper).
- The main paper claimed that the Theorem 1 is proved for a 2-layer NN. However, the NN used in the proof is actually different from what people would expect to be a "2-layer NN", since based on Assumption 1: 1) the second layer is not trained but set to random; and 2) the choice of activation function is very limited as there is a rather strong condition on the activation function.

### Questions
In Section 2.1, what does "i-th input category" mean? In eq. (1), $P$ is the variable of the $\max$ operator, and for any $i \in [P]$, $\mathcal M_i$ is defined, and $\mathcal M_i$ is defined by $\mathcal X_i$. This somehow implies that $\mathcal X_i$ is also a part of the variable of the $\max$ operator, instead of pre-defined. Is it true?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper advocates the use of manifold capacity as a way of classifying as a measure of the regime of neural networks. Manifold capacity is a measure from neuroscience literature that quantifies the performance of a linear classifier over features for classification as a measure of the richness of classifiers. The authors advocate this measure over other measures such as "lazy regimes" during which features show limited change in learning. They use this to analyze 2-layer RELU networks

### Strengths
I think the use and introduction of manifold capacity as a measure is interesting for the ML community as a metric for representation learning. They relate manifold capacity to test accuracy in 2-layer networks and deeper networks empirically. They also relate to other measures such as weight changes and alignment, though this is mostly in the appendix.

### Weaknesses
The paper is haphazardly written. The difference between previous work and their problem statement is not well delineated. Their goals arent succinctly mentioned. The main theorem statement being nearly vacuous in the main paper. "In 2-layer neural networks trained with gradient descent in the rich regime the changes in capacity track the underlying degree of richness in feature learning." Since richness itself is defined as capacity, this is either circular or vacuous. 

A deeper read of the result in the appendix shows that they approximate the result of gradient descent and use a gaussian model to approximate a 2-layer network. This is perhaps the most interesting result in the paper but is not at all covered in the main paper. The authors should state that they prove that using SGD, models with high capacity converge to high accuracy or something less vacuous and offer the proof. 

Other features such as manifold radius and "alignment" are also not measured. The connection to "untangling" is also not mentioned. Weight changes are used mainly as a strawman to invoke connections to NTK and need not be done. 

Figure 2 is very confusing with a nonsensical caption, "Higher capacity means that a higher number of
manifolds per neuron can be packed in the neural state space." What does it mean to "pack manifolds into neurons." This kind of shoddy language obfuscates the message to the reader. 

As the current writing stands, this seems to contribute no more (and likely less by way of confusion) to the work in 2018 by Chung et al. which describes the full intuition of manifold capacity and outlines its use both in neuronal and neural networks.

### Questions
What does "untangling" specifically mean? 

What are the implications of the 2-layer results on deeper neural networks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel framework for understanding neural network feature learning beyond the “lazy” versus “rich” dichotomy by focusing on task-relevant manifold untangling using representational geometry. The authors introduce manifold capacity as a key metric to quantify feature learning richness, and explore how manifold geometric measures reveal distinct learning stages and strategies. This framework is applied in contexts ranging from standard machine learning tasks to neuroscience, offering insights into structural inductive biases and challenges in out-of-distribution (OOD) generalization.

### Strengths
1. The authors present both theoretical analysis and empirical evidence demonstrating that manifold capacity effectively quantifies the degree of feature learning. Comparisons with other metrics, such as accuracy and weight changes, further underscore the efficacy of manifold capacity in this context.
2. The authors offer insightful empirical findings on the relationship between manifold geometry and learning stages, with applications in neuroscience and OOD detection. Robust experiments substantiate these findings, providing a solid foundation for their conclusions.

### Weaknesses
1. The structure needs refinement, as it currently feels like the authors have packed too much content into the main paper, resulting in diminished clarity. The main paper covers a wide range of topics—from manifold capacity to manifold geometry, from theory to experiments—and the relationship between manifold capacity and various manifold geometry measures is weakly explained, relying primarily on Figure 2c with minimal analysis. I suggest that the authors avoid treating manifold geometry as a separate section, even though some interesting findings are presented. An alternative approach would be to frame geometry as an extension of capacity (or to present capacity itself as a facet of manifold geometry) and to provide necessary analysis (I notice there is analysis in the appendix. It's better to consolidate relevant analysis from the appendix into a concise summary in the main paper).
2. The algorithm is not clearly presented, which also appears to be a side effect of the structural issue noted above. Given that the paper aims to provide practical insights into feature learning, with applications in neuroscience and machine learning, it is important to ensure readability for readers unfamiliar with the manifold background. Thus, a clear algorithm outlining the process for computing capacity during training would be essential. The current description lacks the necessary detail for practical implementation. For example, how is the intrinsic dimensionality of the manifold estimated, and what specific methods are used to calculate the geometric measures? Without these details, the reproducibility of the results is questionable.

### Questions
1. Could the authors provide an example of the lazy regime? Specifically, how can a neural network be trained without actually modifying its internal features?

### Soundness
3

### Presentation
3

### Contribution
3
