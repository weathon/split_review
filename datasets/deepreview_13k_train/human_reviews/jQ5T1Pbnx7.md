# New Recipe for Semi-supervised Community Detection: Clique Annealing under Crystallization Kinetics

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Semi-supervised community detection methods are widely used for identifying specific communities due to the label scarcity. Existing semi-supervised community detection methods typically involve two learning stages \ie, learning in both initial identification and subsequent adjustment, which often starts from an unreasonable community core candidate.
Moreover, these methods encounter scalability issues because they depend on reinforcement learning and generative adversarial networks, leading to higher computational costs and restricting the selection of candidates. 
To address these limitations, we draw a parallel between crystallization kinetics and community detection to integrate the spontaneity of the annealing process into community detection.
Specifically, we liken community detection to identifying a crystal subgrain (core) that expands into a complete grain (community) through a process similar to annealing. Based on this finding, we propose CLique ANNealing (CLANN), which applies kinetics concepts to community detection by integrating these principles into the optimization process to strengthen the consistency of the community core. Subsequently, a learning-free Transitive Annealer was employed to refine the first-stage candidates by merging neighboring cliques and repositioning the community core, enabling a spontaneous growth process that enhances scalability.
Extensive experiments on diverse community detection datasets demonstrate that CLANN outperforms state-of-the-art methods across multiple real-world datasets, showcasing its exceptional efficacy and efficiency in community detection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript presents a novel method for community detection called CLANN. This method addresses challenges in semi-supervised community detection, particularly issues with community core consistency and scalability. The authors draw an analogy between community formation and crystallization kinetics, introducing two main components: the Nucleus Proposer and the Transitive Annealer. These components use cliques as starting points and leverage physics-based principles to optimize and expand communities effectively. The paper claims that CLANN surpasses existing state-of-the-art methods in accuracy and efficiency based on extensive experiments across various datasets.

### Strengths
1:The analogy with crystallization kinetics introduces a novel physics-grounded perspective for community detection, enriching the field with fresh conceptual insights.

2:Empirical evaluations show that CLANN outperforms established methods in both single and hybrid dataset scenarios, demonstrating its robustness and superior scalability.

3:The integration of the Nucleus Proposer and Transitive Annealer simplifies the growth process without relying on computationally heavy methods like GANs or reinforcement learning.

4:The paper provides extensive tests, including ablation studies and adaptability analyses, solidifying the validity of its contributions.

### Weaknesses
1:While the physics-based analogy is intriguing, it may be difficult for readers without a background in crystallization kinetics to grasp fully. More simplified explanations or visual aids could make this clearer.

2:Although the method improves scalability over GAN-based approaches, the process of clique enumeration can still be computationally expensive, potentially limiting applicability to extremely large graphs.

3:The experiments, though diverse, may benefit from including more real-world networks with varying characteristics to generalize the method's effectiveness further.

4:The paper does not thoroughly discuss the practical implementation details, such as computational resources required for different dataset sizes, which may affect the adoption of the model in real-world applications.

### Questions
1:Can you provide more intuitive examples or visual explanations of how crystallization kinetics translate to the community detection process? 

2:How does CLANN compare with simpler heuristic-based community detection methods in terms of performance and resource consumption?

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
2

### Summary
In community detection, semi-supervised methods are widely used to identify specific communities; however, existing methods often rely on high-cost models like Generative Adversarial Networks (GAN) or reinforcement learning, resulting in suboptimal initial community cores and limited scalability. There are two main issues with these methods: first, community core inconsistency, as growth-based methods often start from random nodes or k-hop ego networks, which do not accurately represent the structural characteristics of the community; and second, poor growth scalability, as using GAN or reinforcement learning to increase community core candidates is computationally intensive and fails to efficiently leverage existing information, limiting the number of core candidates. To address these issues, the authors propose a community detection model, CLANN, based on annealing and crystallization kinetics. This model comprises two key components: the Nucleus Proposer, which selects completely connected subgraphs (i.e., cliques) as community cores and integrates four crystallization principles to enhance core consistency; and the Transitive Annealer, which uses a learning-free annealing mechanism to merge adjacent cliques into final communities, thereby reducing computational cost and improving scalability. Experimental results show that CLANN outperforms existing community detection methods in terms of accuracy and efficiency across multiple real-world datasets, demonstrating its effectiveness and adaptability in diverse network analysis scenarios.

### Strengths
1.Innovative Approach: The paper creatively relates community detection to crystallization kinetics, introducing an annealing mechanism to enhance community core consistency and scalability with the novel CLANN model.

2.Scalability Improvement: The unsupervised Transitive Annealer significantly reduces computational complexity compared to GANs and reinforcement learning, improving performance on large-scale datasets.

3.Significant Performance Gains: Experiments show that CLANN outperforms existing methods in accuracy and efficiency across various real-world datasets, highlighting its broad applicability.

### Weaknesses
1.Questionable Validity of Physical Analogy: The analogy between community detection and crystallization kinetics is debatable, particularly regarding the relevance of energy minimization in community detection. The paper does not provide a clear justification for why minimizing an energy-based loss function directly translates to finding meaningful community structures. The connection between the physical concept of energy and the graph-theoretical concept of community structure is not rigorously established, making the analogy seem superficial.

2.Insufficient Explanation of Crystallization Dependency: The paper does not adequately clarify how the introduced crystallization principles apply to community detection and their role in model optimization. The specific mechanisms by which 'stability,' 'cohesion,' 'growth,' and 'equilibrium' are translated into concrete algorithmic steps or loss functions are not clearly explained. The paper lacks a detailed explanation of how these principles are mathematically formulated and integrated into the CLANN model, leaving the reader unsure of their precise impact on the final results.

3.Limited Adaptability to Different Network Structures: CLANN’s effectiveness on non-clique structures or noisy communities is not thoroughly assessed, raising doubts about its generalizability. The reliance on completely connected subgraphs (cliques) as initial community cores may limit its performance on real-world networks that often contain sparse connections, non-clique structures, or noisy links. The paper does not provide sufficient evidence to demonstrate the robustness of CLANN in such diverse network scenarios.

4.Lack of Theoretical Analysis: The method lacks in-depth theoretical validation, such as proofs of convergence and complexity for the Transitive Annealer, along with insufficient sensitivity analyses for hyperparameters. The absence of a formal convergence proof for the annealing mechanism raises concerns about its reliability and predictability. Furthermore, the lack of a detailed time complexity analysis makes it difficult to assess the scalability of the method, especially for large-scale networks. The paper also lacks a systematic sensitivity analysis of key hyperparameters, which is essential to understand how the model's performance varies with different parameter settings.

### Questions
1.Applicability of Physical Analogy: The analogy between community detection and crystallization lacks theoretical validation. Please clarify how crystallization principles (e.g., "stability," "cohesion") apply and impact core consistency and scalability.

2.Theoretical Support for CLANN: The model lacks theoretical analysis on convergence and complexity. Please provide complexity proof or detailed time complexity analysis, particularly for large datasets.

3.Parameter Sensitivity Analysis: The paper lacks a systematic sensitivity analysis of key hyperparameters (e.g., annealing temperature, loss weights). Please describe how performance varies with these parameters.

4.Applicability to Non-Clique Structures: CLANN’s reliance on cliques as cores raises questions about its adaptability to non-clique or noisy networks. Please test on such datasets to verify its general applicability.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel approach for semi-supervised community detection, named CLique ANNealing (CLANN), which integrates principles from crystallization kinetics with community detection. To address the issues with scalability and core selection inconsistency, CLANN introduces two main components Nucleus Proposer and Transitive Annealer, draws an analogy between community detection and crystallization, treating communities as grains growing from smaller, well-defined "clique" cores. Experiments conducted on datasets show that CLANN outperforms state-of-the-art methods in both efficacy and efficiency.

### Strengths
S1: The approach of using crystallization principles, especially the spontaneous annealing process, provides a compelling and physics-informed basis for community formation.
S2: The learning-free Transitive Annealer circumvents computational issues tied to reinforcement learning, showing superior scalability over existing methods.
S3: Empirical results indicate that CLANN consistently achieves higher performance across diverse datasets, particularly excelling in detecting distinct community structures within hybrid graphs.

### Weaknesses
W1: The CLANN model assumes high network density and consistency by analogizing community detection to crystallization growth. In practice, however, many graph networks (e.g., social networks, literature citation networks, etc.) may contain highly heterogeneous connectivity structures and low degree of node density, which could lead to difficulties for the annealing process to efficiently identify core or stable structures. In sparse or non-uniform networks, the use of an annealing process may lead to difficulties in forming coherent communities in the model, affecting the detection accuracy. Specifically, the reliance on clique-like structures as initial seeds may be problematic in graphs where such dense subgraphs are rare or absent, potentially leading to the algorithm failing to converge to meaningful community structures. The paper does not adequately address how the algorithm would perform in networks with power-law degree distributions, which are common in real-world scenarios.

W2: CLANN pre-screens the candidate set by a filtering mechanism when initializing candidate community cores to improve efficiency. However, on large-scale datasets, this mechanism still requires a lot of computational resources to traverse and filter the candidate cores. Especially in real-time application scenarios, the initialization process may be too slow, affecting the application efficiency of the algorithm. The paper lacks a detailed analysis of the computational complexity of this filtering step, particularly in relation to the size and density of the input graph. Furthermore, the paper does not provide a clear justification for the specific features used in the filter, and how these features are robust across different types of networks.

W3: For hyperparameters such as Transitive Threshold $\theta$, Temperature Prob. $P_{temp}$, further analysis is required. The paper does not provide sufficient guidance on how to tune these hyperparameters for different datasets. The lack of a principled approach to hyperparameter selection could limit the practical applicability of the method, as users may struggle to achieve optimal performance without extensive experimentation.

### Questions
Q1: Eq. 9 is not the same as the loss in Algo. 1? I think this needs more explanation. Also, at the same time the $ \gamma _G$ should be performing a parameter sensitivity analysis.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript introduces CLANN, a new community detection method motivated by the kinetics crystallization process. It integrates the Nucleus Proposer to learn to detect community cores and Transitive Annealer for spontaneous growth. Extensive experiments with various settings highlight the excellence of CLANN.

### Strengths
S1: The design of the method is inspired by the kinetics of the crystallization process, which provides strong motivation.

S2: Detailed formulas are used to express the approach more rigorously and scientifically.

S3: Extensive experiments are conducted to validate the method.

### Weaknesses
W1: I have two key concerns about the design of the loss functions

W1.1: In equation 7, the formulation of Integrity-Based Loss is used to guide the prediction of the state of undergrown, equilibrium, and overgrown states. It is modeled as a classification problem. However, the loss function used seems not to align with the Binary Cross Entropy.

The binary cross-entropy loss is:

$ 	ext{BCE}(y, \hat{y}) = - \frac{1}{N} \sum_{i=1}^N \left( y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right) $

where:
- \( y_i \) is the true label (0 or 1),
- \( \hat{y}_i \) is the predicted probability of the positive class,
- \( N \) is the total number of samples. 

while the authors seem to mix up the order in the bracket:

$ \sum_{g=1}^3 \left( (y_g^k - 1) \log(\hat{y}_g^k) - y_g^k \log(1 - \hat{y}_g^k) \right) $

W1.2: In the design of the integrity-based method, the overflow states are predefined, which limits the inclusion of many promising patterns, such as:
$(a_2 + \check{a}_2)$

===============

W2: I have two key concerns about the training process.

W2.1: A two-stage training method is used here: first, the Energy-Based Loss, Consistency-Based Loss, and Interface-Based Loss are trained together, followed by training the Integrity-Based Loss separately. This approach to multi-loss training is relatively unusual and lacks clear motivation. Won't the second loss disrupt the model trained in the first stage? How are these losses aligned?

W2.2: As seen in Figure 5, when Loss Amplification approaches 0, performance on many datasets actually improves, indicating that this loss does not enhance training and may even reduce performance (e.g., Consistency-Based Loss and Interface-Based Loss). Strangely, in the ablation study in Table 4, these losses appear to be beneficial.

===============

W3: Some claims and typos can be improved.

W3.1: The authors argue that previous reinforcement-learning-based methods face scalability issues (Line 017), and that the proposed method has better scalability compared to these approaches. CLARE itself is also a reinforcement learning-based method (Line 984). As shown in Figure 4, NP and CLANN demonstrate poorer scalability compared to CLARE. In the DBLP and LiveJournal datasets, NP and CLANN even exhibit faster growth in runtime.

W3.2: Line 157, "Propose" => "Proposer"

### Questions
Given that some losses do not statistically significantly improve performance (e.g., Integrity-Based Loss), would it be possible to reduce certain losses to make the model simpler and emphasize the more effective components?

### Soundness
3

### Presentation
2

### Contribution
3
