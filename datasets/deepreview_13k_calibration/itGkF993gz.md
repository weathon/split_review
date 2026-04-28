# MAPE-PPI: Towards Effective and Efficient Protein-Protein Interaction Prediction via Microenvironment-Aware Protein Embedding

- Decision: Accept
- Avg Score: 5.67
- Scores: 3, 6, 8

## Abstract
Protein-Protein Interactions (PPIs) are fundamental in various biological processes and play a key role in life activities. The growing demand and cost of experimental PPI assays require computational methods for efficient PPI prediction. While existing methods rely heavily on protein sequence for PPI prediction, it is the protein structure that is the key to determine the interactions. To take both protein modalities into account, we define the microenvironment of an amino acid residue by its sequence and structural contexts, which describe the surrounding chemical properties and geometric features. In addition, microenvironments defined in previous work are largely based on experimentally assayed physicochemical properties, for which the ``vocabulary" is usually extremely small. This makes it difficult to cover the diversity and complexity of microenvironments. In this paper, we propose \textit{\underline{M}icroenvironment-\underline{A}ware \underline{P}rotein \underline{E}mbedding for PPI prediction} (MPAE-PPI), which encodes microenvironments into chemically meaningful discrete codes via a sufficiently large microenvironment ``vocabulary" (i.e., codebook). Moreover, we propose a novel pre-training strategy, namely \textit{Masked Codebook Modeling} (MCM), to capture the dependencies between different microenvironments by randomly masking the codebook and reconstructing the input. With the learned microenvironment codebook, we can reuse it as an off-the-shelf tool to efficiently and effectively encode proteins of different sizes and functions for large-scale PPI prediction. Extensive experiments show that MAPE-PPI can scale to PPI prediction with millions of PPIs with superior trade-offs between effectiveness and computational efficiency than the state-of-the-art competitors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary.

This paper is dedicated to developing protein-protein interaction models. The authors point out the efficiency bottleneck of protein structure modeling. They introduce the microenvironments of an amino acid residue. Based on this, they propose microenvironment-aware protein embeddings for PPI prediction, which encode microenvironment into chemically meaningful discrete codes. The authors leverage this design to enable masked codebook modeling training. Experiments are conducted to scale PPI prediction with millions of PPIs.

### Strengths
Pros.

1. The figures are nice and informative.
2. Various PPI baselines are considered, including both sequence- and structure-based approaches.

### Weaknesses
Cons.

1. The authors mention that "the complexity of protein structure modeling hinders its application to large-scale PPI prediction", and emphasize it as an efficiency limitation. Why? It is straightforward to see that complexity modeling hinders accurate modeling. However, it is not clear how it hinders the scalability of modeling and why it is inefficient. Specifically, what aspect of the structure modeling is computationally expensive, and how does this expense prevent scaling to larger datasets? Is it the all-pairs computation, the feature extraction, or the optimization process itself? The authors need to pinpoint the exact bottleneck.
2. Important references are missing. (i) https://arxiv.org/pdf/2208.06366.pdf, which does almost the same codebook learning and masked codebook modeling in vision; (ii) https://www.nature.com/articles/s41586-022-04599-z, which define microenvironments of an amino acid residue and do masked "token" prediction. Based on this omitted reference, the innovation of this work is limited. Also, it is inappropriate to claim "propose... MCM", since both microenvironments and MCM are pre-defined in the literature. The authors should clearly differentiate their approach from these existing methods and acknowledge the prior work.
3. What is the investigation of vocabulary redundancy? The authors create a sufficiently large vocabulary. Are they redundant? Or what is the relationship between vocabulary size or redundancy and archivable performance? The paper lacks a detailed analysis of how the size and composition of the codebook affect the final performance. How does the codebook size influence the granularity of the microenvironment representation, and what are the trade-offs between a large, potentially redundant vocabulary and a smaller, more compact one?
4. The efficiency claim is very confusing. "Extensive experiments show that MAPE-PPI can scale to PPI prediction with millions of PPIs" seems to suggest an inference efficiency. "predict unknown PPIs more efficiently and effectively" also seems to suggest an inference efficiency. However, in the introduction, the authors claim the training efficiency. Also, why the proposed design can enable efficiency? What are the computational and memory overheads of the sufficiently large vocabulary and two-stage training? More detailed time complexity analyses are needed. The authors need to clarify whether the efficiency gains are in training or inference, and provide a rigorous analysis of the computational costs associated with their approach, including the overhead of the codebook and the two-stage training process.
5. Only a single level of sequence similarity is considered. More like 30%, 50%, 90% are encouraged. Meanwhile, as the main results in Table 1, multiple runs of experiments are encouraged to show the prediction stability. The authors should explore the impact of sequence similarity on the model's performance across different thresholds. Additionally, the reported results should include multiple runs to ensure the robustness and stability of the findings.

### Questions
Refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a new method, named MPAE-PPI, for protein-protein interaction prediction. Based on the experimental results, their method showed superiority, compared with other existing methods on several real data sets.

### Strengths
The author describes the fundamental algorithm well; and they seem to give all relevant information to understand and reproduce their algorithm. 

The overall writing is satisfactory. The writing is fluent and clear and the ideas are easy to follow.

The proposed method is relative better than previous methods, which is not lack of significance.

### Weaknesses
(1) To make their results more convincing, they should compare their method with more latest structure-based methods. Specifically, the authors should consider methods that utilize protein structure information, such as those employing graph neural networks on protein structures or methods that incorporate structural embeddings. A comparison with methods that integrate structural information would provide a more comprehensive evaluation of the proposed method's performance.
(2) They just perform parameter sensitivity analysis on one dataset. It remains unclear whether the proposed method is sensitive to the hyper-parameters and how to setup the values in general cases. The analysis should include a broader range of datasets with varying characteristics to assess the robustness of the hyperparameter settings. Furthermore, the authors should explore the impact of different hyperparameter combinations, not just individual parameters, to understand potential interactions.
(3) Lack of description of the details of the datasets. The authors should provide a detailed description of each dataset, including the number of protein pairs, the distribution of interaction types, and any preprocessing steps applied. This information is crucial for reproducibility and for understanding the context of the experimental results.
(4) Lack of real world examples to demonstrate the effectiveness of their model. The authors should provide specific examples of how their model can be applied to real-world scenarios, such as drug discovery or disease pathway analysis. These examples should demonstrate the practical utility of their method beyond the benchmark datasets.

### Questions
(1) To make their results more convincing, they should compare their method with more latest structure-based methods. 
(2) They just perform parameter sensitivity analysis on one dataset. It remains unclear whether the proposed method is sensitive to the hyper-parameters and how to setup the values in general cases.
(3) Lack of description of the details of the datasets.
(4) Lack of real world examples to demonstrate the effectiveness of their model.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper starts with the biological concept of microenvironment and provides a new definition of it from a deep learning perspective. The authors adopt a variant of VQ-VAE to well formulate microenvironment discovery as a codebook learning problem, and propose a novel pre-training strategy specialized for microenvironments, i.e., capturing the dependencies between different microenvironments by randomly masking the codebooks and reconstructing the inputs. Extensive experiments on various datasets, metrics, and data partitions have adequately demonstrated the advantages of the proposed approach in terms of efficiency, effectiveness, generalization, and robustness. Overall, this paper has solid contributions and is expected to have a great impact on protein engineering, especially protein representation learning and PPI prediction.

### Strengths
(1) Starting from the perspective of microenvironments is a bright spot, compared to previous works on residue-level and protein-level modeling. More importantly, the definition of the microenvironment takes into account both sequence and structural contextual information, constructing it as a heterogeneous subgraph of the protein graph, which is well suited to existing deep learning models.

(2) One of the main contributions of this paper is the formulation of microenvironment discovery as a codebook learning problem that greatly extends the limited vocabulary of (20 types) amino acids while taking into account the structural context of proteins. To the best of my knowledge, this is the first work to implement both microenvironment discovery and embedding in a computational way.

(3) A novel pre-training approach for codebook masking modeling has been specifically proposed to capture dependencies between different microenvironments in the learned codebook.

(4) MAPE-PPI inherits the high efficiency of sequence-based methods, while enjoying the structure awareness of structure-based methods, showing a good trade-off between efficiency and effectiveness.

(5) Adequate experiments, including a variety of datasets, metrics, and data partitions, covering aspects of effectiveness, efficiency, generalizability, robustness, ablation study, and visualization.

### Weaknesses
 (1) This paper proposes masking codebook modeling as a pre-training task. Has this approach been used before in other domains (e.g., CV and NLP) or is it the originality of this paper? The authors are encouraged to explain more about the motivation for doing so and provide more experiments to demonstrate its advantages over previous existing masked modeling approaches.

 (2) Why does MAPE-PPI freeze the protein encoder instead of fine-tuning it?

 (3) This paper introduces validation sets for hyperparameter tuning and model selection in the data partition, which makes more sense than the previous data partition. The authors have also reproduced the results of HIGH-PPI using the same data partitioning as MAPE-PPI in Tables 1 and 2, right?

 (4) Some typos need to be corrected.

### Questions
It would be better for the authors to explain more about the issues in the weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
