# Training-Free Message Passing for Learning on Hypergraphs

- Decision: Accept
- Scores: 3, 10, 5, 8

## Abstract
Hypergraphs are crucial for modelling higher-order interactions in real-world data. Hypergraph neural networks (HNNs) effectively utilise these structures by message passing to generate informative node features for various downstream tasks like node classification. However, the message passing module in existing HNNs typically requires a computationally intensive training process, which limits their practical use. To tackle this challenge, we propose an alternative approach by decoupling the usage of hypergraph structural information from the model learning stage. This leads to a novel training-free message passing module, named TF-MP-Module, which can be precomputed in the data preprocessing stage, thereby reducing the computational burden. We refer to the hypergraph neural network equipped with our TF-MP-Module as TF-HNN. We theoretically support the efficiency and effectiveness of TF-HNN by showing that: 1) It is more training-efficient compared to existing HNNs; 2) It utilises as much information as existing HNNs for node feature generation; and 3) It is robust against the oversmoothing issue while using long-range interactions. Experiments based on seven real-world hypergraph benchmarks in node classification and hyperlink prediction show that, compared to state-of-the-art HNNs, TF-HNN exhibits both competitive performance and superior training efficiency. Specifically, on the large-scale benchmark, Trivago, TF-HNN outperforms the node classification accuracy of the best baseline by $10\%$ with just $1\%$ of the training time of that baseline.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes TF-HNN, a training-free hypergraph neural network that removes the need for computationally intensive message passing during training. By shifting hypergraph structural processing to the preprocessing stage, TF-HNN reduces computational complexity. The model achieves efficient, robust node feature generation without oversmoothing, utilizing as much structural information as traditional HNNs. Experiments show that TF-HNN outperforms state-of-the-art HNNs in accuracy and training speed, especially on large-scale benchmarks.

### Strengths
1. The paper is well-structured and easy to follow.
2. The summary of hypergraph neural networks is comprehensive, particularly with the insights provided in Table 1 and the related analysis.

### Weaknesses
Major weaknesses:
1  Proposition 4.2 shows the similarity between the proposed method and APPNP [1], yet the paper does not cite APPNP. Specifically, Eq (6) and Eq (14) appear to apply APPNP after performing clique expansion on the hypergraph. This connection should be discussed more thoroughly, referencing APPNP's Eq (7) and Eq (8) to clarify the relationship and implications of this similarity in the context of hypergraph learning. While the experimental results demonstrate superiority, this oversight is a significant limitation on the paper's originality.

2  Equations (4a) to (4d) result from removing learnable parameters from several baselines, corresponding to the different scenarios in the authors' proposed framework. While these modifications reasonably reduce training time, there is insufficient ablation study to explain the performance improvements. The authors' comparison of the impact from the weighted $S$ of TF-HNN in node classification is commendable. However, they should also present the performance of these modified baselines to clearly demonstrate the impact of removing the learnable parameters.

Minor weakness:

Chien et al.'s work [2] provides the challenging YELP dataset, where many baseline methods yield unsatisfactory performance. Including results on this dataset would enhance the paper's quality and offer a more comprehensive evaluation of the proposed method.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper proposes a novel approach called TF-HNN (Training-Free Hypergraph Neural Network) to address the high computational complexity during training in existing hypergraph neural networks (HNNs). The key innovation is a training-free message passing module (TF-MP-Module) that decouples the processing of hypergraph structural information from the model learning stage. The authors first derive a theoretical framework that provides a unified view of existing HNN approaches, identifying the feature aggregation function as the core component processing hypergraph structure. Based on this insight, they remove the learnable parameters and non-linear activations from the feature aggregation functions of four state-of-the-art HNNs to make them training-free. Further, they consolidate the feature aggregation across layers into a single propagation step, resulting in the proposed TF-MP-Module. Extensive experiments on seven real-world datasets for the tasks of node classification and hyper-link prediction demonstrate the competitive performance of TF-HNN, with very less training time. TF-HNN is the first approach to shift the processing of structure to pre-processing stage, which significantly enhances training efficiency.

### Strengths
1. The paper makes a significant contribution by addressing the issue of high computational complexity of Hypergraph learning algorithms. 
2. The proposed solution, TF-HNN is novel and elegant, which decouples the processing of structural information from the model training stage. 
3. Authors provide a strong theoretical foundation for TF-HNN, the unified framework presented in the paper links all the popular HNN approaches, which shows that TF-HNN is designed by keeping many existing methodologies in mind, and hence provides a comprehensive mechanism for efficient training.
4. Extensive experiments on diverse real-world datasets for node classification and hyperedge prediction tasks demonstrate the competitive performance of TF-HNN against state-of-the-art HNN baselines while requiring significantly less training time.
5. The paper is well-written, with a clear motivation, rigorous theoretical analysis, and thorough empirical evaluation supporting the proposed method's effectiveness and efficiency.

### Weaknesses
I do not see any weak points in this paper. This is a very well written paper, with significant contributions. Please refer to the questions sections for the questions I have.

### Questions
1. An assumption is made about the structure of hypergraph i.e., absence of isolated nodes or empty hyperedges, for the theoretical results. What happens if isolated nodes or empty hyperedges are present? I am not able to see why this assumption is required, and what breaks if it is violated?
2. It is commendable that the proposed TF-HNN performs significantly better than the baselines, but it is also a bit strange to see the baselines performing so poor, particularly on trivago. I understand the boost in training time, but not able to fully understand why there is a 10% improvement, it seems to me  that the learning ability of any SOTA HNN should be similar to TF-HNN. I may have missed something, but curios to hear what the authors have to say on this.

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
3

### Summary
This paper introduces an efficient hypergraph learning scheme that performs message passing prior to learning neural network parameters. The proposed framework, called TF-HNN, includes a TF-MP-Module in which training-free message passing is performed. Using the updated features from the TF-MP-Module, TF-HNN learns an MLP model without a heavy computational burden. Despite its high learning efficiency, TF-HNN demonstrates either superior or competitive performance in hypergraph learning tasks. Theoretical analysis supports the design of the proposed method.

### Strengths
1. The design of the proposed method is very interesting.
2. The proposed method is both highly efficient and effective.
3. The paper is clearly written and well-organized, making the research easy to follow.

### Weaknesses
It appears that there is an issue regarding the hyperparameters. The combinations of hyperparameters used in the experiments shown in Table 13 and Table 14 are quite diverse. For example, the value of alpha ranges from 0.05, 0.15, 0.3, 0.6, 0.65, to 0.7. The learning rate also varies, with values like 0.0006, 0.0001, 0.005, 0.001, and 0.0002. What method was used for hyperparameter search? Additionally, upon reviewing the attached anonymous GitHub link, it appears that the optimal hyperparameters were selected based on performance on the test set rather than the validation set. Were the hyperparameters selected in a fair manner? An analysis of hyperparameter sensitivity should be added.

 The search space for hyperparameters is extremely large, raising concerns about the computational cost and fairness of comparisons with other methods. The reported hyperparameter search time for Cora, the smallest dataset, is not particularly meaningful given the scale of other datasets like Trivago, which has 172,738 nodes. The computational cost of hyperparameter tuning on such large datasets could be prohibitively high, and it is unclear if the same search strategy was applied to all baselines. Furthermore, the paper lacks a discussion on how the hyperparameter search space was determined, and whether it was tailored to each dataset or kept consistent across all experiments. This lack of transparency makes it difficult to assess the validity of the experimental results.

It is also unclear why the hyperparameter settings for the Trivago dataset are not included in Table 13. While the authors mention using a smaller search space for Trivago, this detail is not specified in the paper. Additionally, the paper states that experiments were conducted on a single RTX 3090 GPU, but it is unclear if this is accurate given that hyperparameter searches are computationally expensive. The lack of clarity regarding the hardware used for different experiments further complicates the evaluation of the results.

### Questions
Isn’t too much time being spent on hyperparameter search due to the extensive hyperparameter search range?

If the hyperparameters were indeed selected based on the validation set, could you demonstrate this by providing heatmaps of the hyperparameters across the various validation and test sets used in the experiments?

**minor comments**
- line 209: shonw -> shown
- line 144: Ortega et al. (2018) -> (Ortega et al. (2018))

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a scalable hypergraph neural network (HNN) that reduces the computational cost associated with message passing at each training epoch by decoupling the message passing step.

To achieve this, they (1) establish a general framework that explains popular HNN models, and (2) simplify this framework by removing learnable components and non-linearity, resulting in a single linear operator.

They demonstrate the effectiveness of their approach on both small- and large-scale hypergraphs, showing improvements over several existing HNN models.

### Strengths
- S1. Given that real-world hypergraphs are often large, scalable HNNs are necessary in practice. 
- S2. Although the model design is quite trivial, the theoretical motivation (i.e., building a general unified framework and simplifying it) of the model design is systematic and interesting.
- S3. Experiments are comprehensive.

### Weaknesses
 ***Major comments.***

- ***W1. Regarding Proposition 3.2.*** My understanding is that the key idea is the existence of a clique expansion that satisfies the property outlined in Proposition 3.2.
In practice, however, the authors use a fixed clique expansion as described in Equation 5.
To what extent does this chosen clique expansion align with the one referenced in Proposition 3.2?
While the exact formulations may differ, it would be helpful to know if the high-level characteristics of these clique-expanded graphs are similar.
This is essential, in my view, as it clarifies whether the theoretical analysis effectively supports the proposed method.

- ***W2. Regarding Proposition 4.1.*** Could you clarify what is meant by the "entropy of information"? Does this refer to mutual information between features and node labels? Further elaboration on this point would help in understanding the key takeaway from this proposition.

- ***W3. Regarding the Initial Message Passing Operator Computation Complexity*** Although the message passing operator incurs a one-time computation cost, the time required for this process should be reported. If this initial computation is substantial and exceeds the typical training time of existing HNNs, it could limit the practical efficiency of the proposed method.

***Minor comments.***
- In Lines 52-53, the text mentions that $n^{k}$ memory is required. While this is accurate for dense tensor formats, typical tensor representations are stored in a sparse format, and sparse operations are well-supported in modern deep-learning libraries. Thus, storing a dense incidence tensor is generally not necessary in practice. It may be helpful to revise this part to reflect real-world scenarios.
- In Lines 79-80, the period "." is missing.
- Please provide clarification on the source of the datasets used.

### Questions
Refer to the Weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
