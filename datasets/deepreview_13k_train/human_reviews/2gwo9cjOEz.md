# Neural Tangent Kernels Motivate Graph Neural Networks with Cross-Covariance Graphs

- Decision: Reject
- Scores: 8, 5, 5

## Abstract
Neural tangent kernels (NTKs) provide a theoretical regime to analyze the learning and generalization behavior of over-parametrized neural networks. For a supervised learning task, the association between the eigenvectors of the NTK kernel and given data (a concept referred to as \emph{alignment} in this paper) can govern the rate of convergence of gradient descent, as well as generalization to unseen data. Building upon this concept, we investigate NTKs and alignment in the context of graph neural networks (GNNs), where our analysis reveals that optimizing alignment translates to optimizing the graph representation or the graph shift operator in a GNN. Our results further establish the theoretical guarantees on the optimality of the alignment for a two-layer GNN and these guarantees are characterized by the graph shift operator being a function of the \emph{cross-covariance} between the input and the output data. The theoretical insights drawn from the analysis of NTKs are validated by our experiments focused on a multi-variate time series prediction task for a publicly available dataset. Specifically, they demonstrate that GNNs with cross-covariance as the graph shift operator indeed outperform those that operate on the covariance matrix from only the input data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper draws on the idea that NTK based generalization is based on the associations of eigenvectors of the NTK with the data. Drawing on this alignment in the case of a GNN is used to derive the graph shift operator (i.e. equivalent of a graph laplacian) that is different from the input graph. To do this they solve an optimization to derive the graph as being the cross-covariance matrix of the input with the output.

### Strengths
Generalizing the NTK to GNNs expands the theory associated with this area, and the suggestion of using a cross covariance matrix involves a graph that uses both input and output variables as nodes, which is not commonly done in current GNNs. The theory could be useful in cases where the graph is not given but constructed as an affinity matrix from data as well.

### Weaknesses
The key weakness is that empirically VNNs and graphs that are based on covariance matrices rather than non-linear affinities have fared worse in practice. This may be an instance of the NTK not explaining the entire behavior of neural networks. Moreover the experimental validations seem fairy limited without comparison to GCNs and Graphormers and other modern graph neural network architecture. Specifically, the paper lacks a thorough investigation into how the proposed cross-covariance graph compares against other common graph construction methods, such as those based on Gaussian kernels or k-nearest neighbors using node feature similarities. The experiments also do not explore the sensitivity of the method to hyperparameter choices in the optimization used to derive the graph shift operator, which could significantly impact performance. Furthermore, the paper does not address the computational cost associated with constructing the cross-covariance matrix, which could be prohibitive for large graphs.

### Questions
Is this a case of the theory not explaining the entire empirical phenomenon? Can further experiments be performed on a variety of kernels to see what works better in practice on common datasts/

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors delve into the theoretical aspects of Neural Tangent Kernels (NTKs) and their influence on the learning and generalization behaviors of over-parameterized neural networks in supervised learning tasks. They introduce the concept of "alignment" between the eigenvectors of the NTK kernel and the given data, which appears to play a significant role in governing the rate of convergence of gradient descent and the generalization to unseen data. The paper specifically explores NTKs and alignment in the context of Graph Neural Networks (GNNs). The authors' analysis reveals that optimizing alignment corresponds to optimizing the graph representation or the graph shift operator within a GNN. This investigation leads to the establishment of theoretical guarantees concerning the optimality of certain design choices in GNNs.

### Strengths
* The paper is well-organized, with a clear delineation of concepts such as NTKs, alignment, and their relevance in the context of GNNs.

* The paper's findings have the potential to advance the understanding and analysis of Graph Neural Networks, providing theoretical insights that could be valuable for the community.

### Weaknesses
 * The paper seems to miss a crucial related work: Huang, W., Li, Y., Du, W., Yin, J., Da Xu, R. Y., Chen, L., & Zhang, M. (2021). "Towards deepening graph neural networks: A GNTK-based optimization perspective," ICLR 2022. Including and discussing this work could provide a more comprehensive perspective and strengthen the literature review section.

* The theoretical framework primarily relies on the existing NTK theory regarding optimization and generalization. While the authors have cited relevant works, a more distinct and innovative theoretical contribution that extends beyond the current NTK theories would enhance the paper's novelty and impact. The analysis, while technically sound, appears to be a direct application of existing NTK results to a specific GNN architecture, rather than a significant theoretical advancement in the understanding of NTKs themselves.

* The paper's discussion on alignment seems closely related to node classification and graph classification tasks. However, there appears to be a lack of relevant examinations or experiments to empirically validate the proposed concepts and theories in these tasks, making it difficult to assess their practical relevance and effectiveness. The theoretical results, while interesting, are not directly tied to standard GNN benchmarks, which limits the immediate impact of the work.

* The paper could significantly benefit from a more robust and comprehensive experimental section. Ensuring that the experiments thoroughly validate the theoretical findings, involve extensive comparisons with baseline methods, and are evaluated across various datasets and tasks is essential for demonstrating the approach's practical significance and effectiveness. The current experiments are limited in scope and do not provide sufficient evidence for the general applicability of the proposed approach.

* A more detailed and thorough comparison with existing NTK and GNN methods is necessary. The paper should highlight the proposed approach's novelty and advantages, supported by theoretical or empirical evidence, to clearly showcase the contributions and distinguish the work from existing literature. The lack of a clear comparison makes it difficult to assess the unique value of the proposed approach compared to other methods.

### Questions
* Could the authors elaborate on how the alignment concept is related to node and graph classification tasks? Are there any practical insights or guidelines on how to effectively apply the proposed theories to these tasks?

* Can the authors highlight the novel aspects of their theoretical framework that go beyond the existing Neural Tangent Kernel (NTK) theories? What are the unique contributions that differentiate this work from existing NTK-based studies?

* Are there plans to include more comprehensive experiments to validate the proposed theories and concepts? What datasets, tasks, and baselines are considered for these experiments?

*Will there be experiments conducted specifically to verify the proposed theorems, such as theorem 2 and theorem 3? If so, could you provide insights into how these verifications will be carried out empirically?

* Why the size of $\mathbf{y}_i$ is $\mathbb{R}^{n \times 1}$, given the size of $\mathbf{x}_i$ is $\mathbb{R}^{n \times 1}$? Is there a specific rationale behind this choice of dimensionality?

* Could you elucidate the rationale behind choosing the HCP-YA dataset for your experiments? How does this dataset align with the objectives and hypotheses of your study, especially considering that common node classification or graph classification tasks are typically used in related works?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study offers a theoretical analysis of Graph Neural Networks (GNNs), emphasizing their infinite-width limit behavior through the lens of the Neural Tangent Kernel (NTK). The research illuminates the constancy of the NTK in such scenarios, advancing the understanding of neural network learning dynamics. 

Furthermore, the paper explores the implications of varying training intensities across GNN layers, enhancing interpretability in a field often perceived as a 'black box.' The authors validate their theoretical assertions with detailed experiments, utilizing public datasets to ensure reproducibility and credibility.

This paper bridges complex theoretical insights with practical machine-learning applications, contributing substantially to the discourse on neural network training, optimization, and generalization. Its rigorous approach and novel findings mark a significant stride in understanding and leveraging the full potential of GNNs.

### Strengths
1. By exploring the constancy of the NTK in the infinite-width limit, the study sheds light on complex learning dynamics, enhancing the scientific understanding of how GNNs train and generalize. This rigorous theoretical foundation pushes the boundaries of existing knowledge in neural network behavior.
2. By dissecting layer-specific training implications, the paper contributes to the interpretability of neural networks, helping researchers to better understand and optimize their GNN models, which is particularly valuable in the 'black box' context of deep learning.

### Weaknesses
1. While the paper is strong in theoretical analysis, it may not provide extensive insight into the practical applications of the findings. The implications for real-world scenarios, particularly how these theoretical insights into GNNs and NTK behavior could be harnessed for tangible improvements in specific use cases, might not be thoroughly discussed. Specifically, the paper lacks concrete examples demonstrating how the theoretical findings translate to improved performance in practical tasks beyond the provided experiments. For instance, the benefits of NTK constancy could be more clearly linked to specific optimization strategies or architectural choices in real-world GNN applications. The current discussion is somewhat abstract and does not offer clear guidance on how practitioners could leverage the theoretical insights.
2. If the experiments were conducted within a narrow set of conditions or datasets, they might not fully represent the complexities of real-world data and scenarios. This limitation could raise questions about the generalizability of the findings and their robustness when applied to diverse, practical challenges in the field of machine learning. The paper should explicitly address the potential limitations of the experimental setup, including the specific characteristics of the datasets used and how these might influence the observed results. A more detailed analysis of the experimental design, including the choice of hyperparameters and evaluation metrics, would also be beneficial to assess the robustness of the conclusions.

### Questions
1. Given the depth of the research, what do the authors see as the next steps or future directions in this domain? Additionally, are there any inherent limitations or challenges in the proposed methods or findings that might need to be addressed in subsequent research?
2. Can the analysis be extended to deeper (more than 2 layers) GNNs where the aggregation operation is used in internal layers?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
