# Graph Regularized Encoder Training for Extreme Classification

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Deep extreme classification (XC) aims to train an encoder and label classifiers to tag a data point with the most relevant subset of labels from a very large universe of labels. XC applications in ranking, recommendation and tagging routinely encounter tail labels, for which the amount of training data is exceedingly small. One way to tackle the tail label problem is to use additional data - often structured as a graph associated with documents and labels - graph metadata. Graph Convolutional Networks (GCNs) present a convenient but computationally expensive way to leverage this graph metadata and enhance model accuracies in these settings. However, GCNs struggle to make predictions for a novel test point when it has no edge in the graph. The paper notices that in these settings, it is much more effective to use graph data to regularize encoder training than to implement a GCN. Based on these insights, an alternative paradigm RAMEN  is presented to utilize graph metadata in XC settings that offers a significant performance boost with zero increase in inference computational costs. RAMEN scales to datasets with millions of labels and offers prediction accuracy up to 15% higher on benchmark datasets than state of the art methods, including those that use graph metadata to train GCNs. RAMEN also offers 10% higher accuracy over the best baseline on a proprietary recommendation dataset sourced from click logs of a popular search engine. Code for RAMEN  will be released publicly upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The goal of the RAMEN model is to leverage graph metadata during training without introducing extra inference time costs. The graph data is used to regularize the encoder $\mathcal{E}$ by embedding points close to the representations of correct labels and distant from the representations of incorrect labels. The authors propose a contrastive regularization loss function that utilizes this graph metadata to improve classification accuracy, especially for rare labels.

### Strengths
**Evaluation and Performance**: The experimental results are promising. RAMEN demonstrates  improvements in multi-labels performance over multiple baseline methods.

**Effective method**: Table 3 shows that RAMEN show impressive gain in term of inference and training.

### Weaknesses
 **Presentation**: The model figure could be more detailed. Currently, it repeats parts of the abstract verbatim, and a more informative figure would have helped clarify the steps, especially how the graph metadata regularizes the encoder through the loss function. Specifically, the figure should illustrate the flow of data, from input documents and labels to the encoder, then to the graph metadata, and finally to the contrastive loss calculation. A clear depiction of how the graph's structure influences the selection of positive and negative pairs is also needed. Similarly, an introductory figure outlining the overall method would improve readability. This figure should provide a high-level overview of the RAMEN model, showing how the graph metadata is integrated into the training process. Table 4 also needs cropping; important parts are not visible, making it hard to interpret. The lack of clear axis labels and the truncated bars make it difficult to assess the results presented in the table.

**Clarity of Contributions:** The contributions of the paper are difficult to follow. From what I understand, there is a contrastive loss that uses the graph metadata to define positive and negative examples, but this is not explained in sufficient detail, making it hard to fully grasp the model’s novelty and mechanisms. The paper needs to clearly articulate how the graph is constructed, what the nodes and edges represent, and how this structure is used to generate positive and negative samples for the contrastive loss. The description of the training process is also vague. It is unclear how the document, label, and anchor sets interact during training, and how the loss function is applied to each of these components. Also the training with

**Typos**: There are some typo errors. For example, Line 1035 has a "(?)" and Line 1036 seems to have an incomplete reference "Lem[...]".

### Questions
1. In the metadata graph regularization, is the graph primarily used to define positive and negative links for the contrastive loss? Please clarify if the positive and negative examples come solely from this graph.

2. Theorem 1: If I understand correctly, the theorem suggests that if an adjacency matrix can be approximated by a non-GCN (e.g., feedforward network or transformer), it implies the existence of another non-GCN that can approximate $\phi(AXW)$ However, is this new network permutation invariant? The usual motivation for using GCNs is precisely their permutation invariance across the matrix $A$. Therefore, I am not fully convinced by this argument based on my current understanding of the theorem.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents RAMEN, a method for extreme classification with graph metadata, primarily focusing on ranking and recommendation scenarios. While the authors address the challenge of handling new users and items without graph edges, **they notably overlook the well-established concept of "cold-start" recommendation - a significant oversight in the recommendation systems literature**. The absence of comparisons with existing cold-start solutions and related work makes it difficult to properly evaluate the paper's true contributions to the field. Additionally, the experimental validation is limited by the relatively small dataset size of 1.3 million samples, which fails to demonstrate the method's efficacy in large-scale, real-world applications. Without addressing these fundamental concerns - namely, the missing cold-start comparisons and limited dataset scale - the paper's claims of superiority over existing methods remain inadequately supported. These limitations significantly impact the paper's potential contribution to the field and its suitability for publication at a prestigious venue like ICLR 2025.

### Strengths
1. Graph Regularization Approach: Instead of using complex GCN, the paper proposes a simpler yet effective approach of using graph data for regularization. The method is theoretically supported and mathematically sound.
2. Inference Efficiency: RAMEN achieves faster prediction by eliminating graph traversal during test time, while maintaining accuracy. The two-stage comparison with GCN methods is clearly visualized and demonstrates practical advantages.
3. Multi-Graph Flexibility: The system can handle multiple graph types simultaneously and integrates easily with existing systems. This versatility is well-demonstrated through experimental results and architectural design

### Weaknesses
1. Critical Cold-Start Problem Oversight:The paper fundamentally fails to acknowledge or address the cold-start problem, despite directly tackling scenarios where new items have no graph connections. This is not merely a terminology issue - it's a severe oversight that ignores decades of research in recommendation systems. The absence of comparisons with established cold-start solutions makes it impossible to validate the authors' claims of superiority.
2. Inadequate Dataset Scale: Using only a 1.3M dataset in an era where real-world recommendation systems handle hundreds of millions of users/items is a critical limitation. This small-scale evaluation raises serious doubts about RAMEN's practical applicability and scalability claims. The paper's claims about handling "extreme" classification become questionable when tested on such modest datasets.
Missing Technical Validation
3. The paper lacks crucial technical validations, including ablation studies, complexity analysis, and detailed parameter sensitivity tests. The implementation details are vague, making reproduction difficult. Without these essential technical components, the paper's theoretical contributions remain unsubstantiated by empirical evidence, particularly for real-world deployment scenarios.

### Questions
Shown in weakness

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel approach, RAMEN, for extreme classification (XC) that effectively utilizes graph metadata to regularize encoder training. The method shows significant performance improvements over state-of-the-art techniques, with up to 15% higher prediction accuracies on benchmark datasets. The theoretical foundation provided by Theorem 1 and its extensions is a strong aspect of the paper, validating the approach. The extensive experimental results, including ablation studies, further demonstrate the effectiveness of RAMEN. However, the paper could benefit from addressing some weaknesses.

### Strengths
1. The paper presents a novel method, RAMEN, for leveraging graph metadata in extreme classification (XC) settings. It offers an alternative to Graph Convolutional Networks (GCNs) by using graph data to regularize encoder training.
2. The paper conducts extensive experiments on multiple benchmark datasets and a proprietary dataset.

### Weaknesses
1. The process of tuning the regularization constants using the bandit learning approach may be hard to follow for some readers. The initialization of the constants and the perturbation process every 30 iterations, along with the update rule using the estimated gradient, involves multiple steps and concepts. Specifically, the paper lacks a clear explanation of how the bandit algorithm's exploration-exploitation trade-off is balanced in the context of regularization parameter tuning. It is unclear how the chosen bandit algorithm (e.g., UCB, Thompson Sampling) influences the convergence and stability of the training process. Furthermore, the specific method used to estimate the gradient for the bandit update is not sufficiently detailed, making it difficult to assess the practical implementation and potential sensitivity to noise.
2. The Related Work of this paper lists many references related to XC methods without providing in-depth analysis of how the proposed method in this paper (RAMEN) overcomes the limitations of these existing methods in a more detailed and unique way. While it gives an overview of the field's development, it doesn't clearly distinguish the novelty and superiority of the new approach in a concise manner. The paper should include a more detailed comparison, highlighting specific shortcomings of existing methods that RAMEN addresses, such as scalability issues, handling of sparse label spaces, or the inability to effectively utilize graph metadata. Without this, the contribution of RAMEN is not as clearly established.
3. The method and its associated theoretical concepts may be complex for some readers to understand. The notation and mathematical derivations, especially in the sections related to Theorem 1 and its proof, could be a barrier to a broader audience. The paper would benefit from more intuitive explanations of the core concepts, such as the specific meaning of the regularization terms in relation to the encoder's embedding space. The paper should also provide more concrete examples to illustrate how the theoretical results translate into practical improvements in the model's performance.

### Questions
Terms like "in-batch negatives anchors" and the specific way the loss function  and regularization functions interact to encourage the encoder to embed data points and labels in a certain way could be better explained.

### Soundness
3

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
3

### Summary
The paper introduces RAMEN, a novel approach designed to enhance extreme classification (XC) tasks by leveraging graph metadata to regularize encoder training. RAMEN effectively addresses the limitations of GNN-based methods, such as computational inefficiency and vulnerability to noisy graph data. By utilizing graph metadata as a regularizer rather than integrating GCN layers directly, RAMEN achieves significant performance improvements, up to 15% higher accuracy on benchmark datasets, while maintaining scalability and minimizing inference costs. The method demonstrates robust performance across various datasets, including proprietary recommendation systems, underscoring its applicability and effectiveness in handling both dense and sparse label scenarios.

### Strengths
1. **Innovative Methodology:** The paper proposes a novel graph-regularized training framework, RAMEN, specifically designed for extreme classification tasks. This method effectively mitigates the limitations of traditional GCN-based approaches, such as high computational overhead and sensitivity to noisy graph structures. By regularizing the encoder with graph metadata during training, RAMEN enhances model robustness and efficiency, enabling scalability to datasets with millions of labels without increasing inference costs.
   
2. **Comprehensive Experimental Validation:** The authors conduct extensive experiments across multiple benchmark datasets, including LF-WikiSeeAlsoTitles-320K, LF-WikiTitles-500K, and LF-AmazonTitles-1.3M, as well as a proprietary dataset (G-EPM-1M). RAMEN consistently outperforms baseline methods, including both text-based and graph-based approaches, by up to 15% in precision metrics. Additionally, ablation studies demonstrate the effectiveness of key components such as bandit learning for regularization constants and graph pruning for handling noisy metadata. The real-world application in sponsored search further validates RAMEN's practical utility, showcasing significant improvements in impression and click yields during A/B testing.

### Weaknesses
1. **Related Work Presentation:** The related work section primarily lists references without adequate categorization or in-depth analysis. This approach limits the ability to understand how RAMEN differentiates itself from existing methodologies and fails to provide insightful connections between prior studies and the proposed approach. A more structured review, categorizing related works based on their methodologies and highlighting comparative strengths and weaknesses, would enhance the comprehensiveness and clarity of the literature context.
   
2. **Clarity and Formal Description:** The presentation of certain concepts, particularly the comparison between GCN-based extreme classification methods and RAMEN, lacks clarity. The paper would benefit from a more precise formal description of GCN-based extreme classification methods, including explicit definitions and step-by-step explanations. Additionally, outlining the limitations of these methods in a clear, point-wise manner would aid readers in better understanding the motivations behind RAMEN and the specific challenges it addresses.

### Questions
1. **Concrete Examples of Graph Metadata:**  
   Can the authors provide specific examples of the types of graph metadata utilized in their experiments? For instance, what defines an anchor set in the different datasets (e.g., LF-WikiSeeAlsoTitles-320K, LF-WikiTitles-500K, LF-AmazonTitles-1.3M), and how are these metadata graphs constructed and integrated within the RAMEN framework?

2. **Robustness to Noisy Graphs:**  
   How does RAMEN perform when exposed to explicitly added noisy graph metadata? Specifically, if additional irrelevant or incorrect edges are introduced into the metadata graphs, what impact does this have on RAMEN's accuracy and robustness compared to traditional GCN-based methods? Have the authors conducted any experiments to evaluate RAMEN's resilience to such noise?

3. **Adaptability to Other Domains:**  
   The experiments presented focus on datasets derived from Wikipedia and Amazon. How adaptable is RAMEN to other domains that have different types of graph metadata, such as social networks, biomedical data, or recommendation systems in other industries? Have the authors conducted any preliminary tests in these diverse domains, or are there plans to evaluate RAMEN's performance in such settings?

### Soundness
3

### Presentation
1

### Contribution
2
