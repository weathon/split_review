# Inner Information Analysis Algorithm for Deep Neural Network based on Community

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Deep learning has achieved advancements across a variety of forefront fields. However, its inherent 'black box' characteristic poses challenges to the comprehension and trustworthiness of the decision-making processes within neural networks. To mitigate these challenges, we introduce InnerSightNet, an inner information analysis algorithm designed to illuminate the inner workings of deep neural networks through the perspectives of community. This approach is aimed at deciphering the intricate patterns of neurons within deep neural networks, thereby shedding light on the networks' information processing and decision-making pathways. InnerSightNet operates in three primary phases, 'neuronization-aggregation-evaluation'. Initially, it transforms learnable units into a structured network of neurons. Subsequently, these neurons are aggregated into distinct communities according to representation attributes. The final phase involves the evaluation of these communities' roles and functionalities, to unpick the information flow and decision-making. By transcending focus on single-layer or individual neuron, InnerSightNet broadens the horizon for deep neural network interpretation. InnerSightNet offers a unique vantage point, enabling insights into the collective behavior of communities within the overarching architecture, thereby enhancing transparency and trust in deep learning systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Review report: Inner Information Analysis Algorithm for Deep Neural Network Based on Community 
The present manuscript converts learnable units in Deep Neural Networks, such as kernels in CNNs, into networks and then groups the neurons into communities based on their representational attributes. To achieve this clustering, the authors develop the InnerSightNet. By subsequently analyzing the communities, the authors gain insights into the inner working of Deep Neural Networks such as relating certain communities to specific features in the underlying test data and detecting irrelevant neurons.

### Strengths
Strengths 
-	The main idea of the manuscript, to group learnable units into a network of neurons and then analyze the communities within this network, is very clever and interesting.
-	The general approach to InnerSightNet is described very clearly. In particular, Algorithm 1 is helping in understanding the different steps.  
-	It is intriguing to see that the interdependence of different communities of neurons, such as c_1 and c_2 in the first layer of the CNN as reported in Table 1, is reflected in the 2-dimensional topological representation in Figure 3.

### Weaknesses
Weaknesses
- The different terms in Eq. (1) could be motivated more clearly, especially given the fact that this step is crucial to transform the kernels of a CNN in a structured network. Specifically, the rationale for using the Kullback-Leibler (KL) divergence between kernel distributions and the subsequent division by the normalized cosine similarity, which is either +1 or -1, needs further justification. The choice to separate positive and negative value regions, $\kappa^{+}$ and $\kappa^{-}$, is not sufficiently explained in the context of feature representation within the kernels. Furthermore, the exact nature of the data $X_i$ used to compute these kernel correlations should be explicitly defined.
- While the general structure of InnerSightNet is described very clearly, the more detailed description is cumbersome to follow. Especially the aggregation step, which is heavy in notation but also lacks a definition of some variables such as $l_d$, $\tau_{g_k, j}$ and $s$. The lack of clarity in these definitions makes it difficult to reproduce the results and understand the precise mechanics of the aggregation process.
- The section “Community function analysis and finding key communities” is rather descriptive and only offers a shallow discussion regarding the explainability of community structures for MNIST. The discussion here could be greatly improved by more directly linking the observation from panel (a) and (b) together, as has been done with community $c_{10}$ in the first layer. The analysis lacks a more in-depth exploration of the functional roles of identified communities, particularly in relation to specific features or patterns within the input data. A more rigorous analysis should be provided to support the claims made about the importance of specific communities.

### Questions
Questions 
-	In Eq. (1), could you motivate the distinction in positive and negative value regions more clearly as well as the choice to divide by the normalized cosine similarity, which is essentially either +1 or -1? Could you also specify what exactly data X_i refers to? 
-	Are the accuracy drops in closing communities in Figure 1a) and Table 1 reported with or without retraining the network? 
-	In Table 1, why don’t you report the accuracy after closing the corresponding communities for all possible combinations of the communities in the respective layers? For instance, in the first layer, why are c_0 and c_1 not closed together? Could you also close communities together across layers? 
-	Could you elaborate on the practical implications of your results, especially regarding parts of the model that fit to noisy data, cf. lines 458 until 464? 
-	In lines 1109 to 1112 you write “This phenomenon raises a question: in common sense, cat and dog images contain more information than handwritten digital, why is there actually less community division? Our explanation is ‘task-related’. Due to the fact that cat and dog classification is a binary task, the number of effective neurons for binary classification is indeed less than that for ten class tasks.” Would it be possible to simply restrict MNIST to classifying between 0 and 1 to test for this observation?


Additional comments
-	The axis and legend labels in the Figures are barely readable. 
-	In line 53, it should be “one aims” instead of “one aims”. 
-	In line 108, it seems inappropriate to cite a review paper to represent community detection in networks. 
-	In line 146, the citation “David et al. Bau et al. (2017)” seems to contain a typo. 
-	In line 161 and in line 188, the citation “Newman et al. Newman (2006” seems to contain a typo. 
-	In Definition 2, it would be helpful to distinguish 
-	In line 238, the citation “Lange et al. Lange et al. (2022)” contains a typo.
-	In Eq. (11), it is a bit unfortunate to use delta as a variable again as it also appeared in Eq. (1). 
-	In line 264, “sgn is the symbol function” was meant to be sign function? 
-	In line 323, the citation “Wanatabe et al. Wanatabe et al. (2018)” contains a typo. 
-	From line 370 onwards, c_10 should be changed to c_{10} in LaTex

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
The paper proposes an algorithm designed to enhance the interpretability of deep neural networks by analyzing internal neuron communities. The approach transforms neurons into structured communities, aggregates them based on their functional attributes, and evaluates the information flow across these groups. The study applies the method to both linear and convolutional networks, demonstrating improvements in turning off noisy neurons.

### Strengths
1. InnerSightNet introduces a unique perspective by focusing on community-based analysis of neurons, rather than on a single layer or individual neuron.
2. The three primary phases (neuronization, aggregation, evaluation) adaptively ensure the best number of communities.
3. InnerSightNet is shown to enhance interpretability and can be applied to network pruning to reduce model size while maintaining competitive performance.

### Weaknesses
1. The paper compares InnerSightNet with methods such as Filan et al. (2021), Hod et al. (2021), and Liu et al. (2023) in the experiments. However, it does not sufficiently explain the methodologies of these baselines. A more detailed introduction to these approaches is needed to help the readers understand how InnerSightNet improves upon or differs from them. Specifically, the paper lacks a discussion on the specific algorithms used by these baselines, such as the clustering techniques employed by Filan et al. and Hod et al., or the geometric embedding and training modifications in Liu et al. Without this, it is difficult to assess the novelty and advantage of the proposed method.
2. While the method performs well on relatively small networks like those used in the MNIST and AFHQ datasets, it remains unclear how the algorithm scales to deeper networks. The paper does not provide any analysis of the computational complexity of InnerSightNet, nor does it discuss potential bottlenecks that might arise when applying it to larger models with significantly more layers and parameters. This lack of scalability analysis is a major concern, as it limits the practical applicability of the method to real-world scenarios.

### Questions
1. What is the runtime of InnerSightNet for different network sizes? How fast the algorithm converges compared to baseline methods?
2. How scalable is InnerSightNet when applied to deeper networks like transformers？

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the InnerSightNet algorithm, which clusters neurons in the same layer of MLPs and convolutional kernels in the same layer of CNNs from a community perspective. Through experiments that mask certain neuron clusters and perform perturbation analysis, it demonstrates that some clusters play a key role in task performance, some clusters can be pruned, and some clusters introduce noise.

### Strengths
1. Novelty: The introduction of a community-based perspective for analyzing DNNs is original and provides a fresh viewpoint for understanding the role neurons play.
2. Comprehensive Framework: The multi-phase algorithm (neuronization, aggregation, evaluation) is well-structured, combining theoretical and practical insights.
3. Detailed Evaluation: The paper evaluates the communities formed in DNNs through accuracy drop tests and sensitivity analyses, showcasing the impact of each community on network performance.

### Weaknesses
1. Scalability: The paper doesn't address the scalability of InnerSightNet on very large-scale neural networks. It is unclear how well the algorithm would perform or how computationally feasible it is for networks with millions of neurons. The analysis of computational complexity, particularly with respect to the EM algorithm's convergence and the multi-step startup strategy, needs further elaboration. The paper should include a more detailed analysis of how the runtime scales with network size, dataset size, and the number of communities identified.
2. Transferability: The experiments are only conducted on image recognition tasks. Can this method be applied to the interpretability of NLP models? The findings are limited to the functions of different clusters which follows conventional research pattern. The paper lacks a thorough investigation into the applicability of InnerSightNet to different architectures beyond CNNs and MLPs, such as recurrent neural networks or transformers, which are commonly used in NLP. The analysis should also explore whether the community structures identified in image models translate to other modalities.
3. Usability: The mathematical theory of the algorithm is more solid compared to previous works, but the overall improvement in tasks like noise reduction and pruning is very limited. The paper needs to provide more concrete evidence of the practical benefits of using InnerSightNet for noise reduction and pruning. The reported improvements in accuracy are marginal, and the paper should demonstrate more significant gains in model performance or efficiency.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
