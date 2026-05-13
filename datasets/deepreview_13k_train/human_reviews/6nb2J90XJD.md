# Unsupervised Multiple Kernel Learning for Graphs via Ordinality Preservation

- Decision: Accept
- Scores: 3, 8, 5, 6

## Abstract
Learning effective graph similarities is crucial for tasks like clustering, yet selecting the optimal kernel to evaluate such similarities in unsupervised settings remains a major challenge. Despite the development of various graph kernels, determining the most appropriate one for a specific task is particularly difficult in the absence of labeled data. Existing methods often struggle to handle the complex structure of graph data and rely on heuristic approaches that fail to adequately capture the global relationships between graphs. To overcome these limitations, we propose Unsupervised Multiple Kernel Learning for Graphs (UMKL-G), a model that combines multiple graph kernels without requiring labels or predefined local neighbors. Our approach preserves the topology of the data by maintaining ordinal relationships among graphs through a probability simplex, allowing for a unified and adaptive kernel learning process. We provide theoretical guarantees on the stability, robustness, and generalization of our method. Empirical results demonstrate that UMKL-G outperforms individual kernels and other state-of-the-art methods, offering a robust solution for unsupervised graph analysis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors propose an unsupervised multiple kernel learning method that produces a weighted sum of kernels given a set of kernels and a dataset.

### Strengths
- Multiple kernel learning is a relevant topic. In particular, the unsupervised creation of a suitable kernel from a set of kernels given a dataset is a nontrivial problem.

### Weaknesses
 - the basic definition (Def. 1) is imprecise and I could not follow the paper, as it remains unclear (to me) which ordinal relationship is supposed to be maintained. The definition appears circular, as it only refers to the learned kernel values \(k\) without specifying an external reference for the ordinal relationship. It is not clear what properties the triplet \((i,j,r)\) must fulfill for the ordinal relationship to be preserved. The paper does not explicitly state whether the initial kernel values \(k_{ij}(w_0)\) are fixed or if they are also subject to change during the learning process. This lack of clarity makes it difficult to understand the core mechanism of the proposed method. For instance, if \(k_{ij}(w_0) < k_{ir}(w_0)\), it's unclear if the method aims to maintain this relationship or if it allows for a reversal during the learning process. The definition should clearly state the conditions under which the ordinal relationship is preserved and what happens if those conditions are not met.

### Questions
I have severe problems understanding
> Definition 1:
> Consider the graph $G_i$ where its similarities to $G_j$ and $G_r$ are respectively given by the learned kernel values $k_{ij}$ and $k_{ir}$. 
> The ordinal relationship between $G_j$ and $G_r$ with respect to $G_i$ are preserved if, for any weights $w$: $k_{ij} > k_{ir}$. 

It seems that this definition is self-referential, as only the learned kernel values $k$ are mentioned. Is there another similarity that should be preserved? If $k$ is to be learned, then it probably should retain the ordinal relationship of another similarity (or similarities?). Or am I missing something? I am sorry, but this does not make sense to me right now and I have to recommend to reject this paper at the current point in time.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The article introduces a novel approach for unsupervised multiple kernel learning on graphs. The task is to combine several weak kernels for unsupervised learning scenarios by learning a set of weights. The main idea is to preserve the data topology by maintaining ordinal relationships, i.e., the order of similarities between graphs. This is achieved through a designed probability simplex. The authors provide comprehensive theoretical results, addressing aspects such as robustness to kernel perturbations and generalization capabilities. Finally, the approach is experimentally evaluated by performing graph clustering tasks on standard molecular datasets.

### Strengths
- The approach offers a novel solution to an understudied problem.
- The technical quality of the theoretical part of the work is high.
- The theoretical analysis is comprehensive, featuring a range of results on properties and detailed proofs. 
- While the authors present their work in the realm of graph kernels, their approach can be applied to arbitrary kernels.

### Weaknesses
 - While most parts of the article are well described, some central intuitions that motivate the approach are not sufficiently addressed. For instance, why is P a more accurate representation of the data's inherent geometry'? This claim needs further justification, as it's not immediately clear why emphasizing certain connections through the probability simplex necessarily leads to a more 'accurate' geometric representation, rather than simply a different one that may be beneficial for the task at hand. The authors should clarify whether 'accurate' refers to a better reflection of the underlying manifold structure or simply improved performance in downstream tasks.
- The evaluation is fairly limited, relying solely on the clustering task. I understand that due to space limitations, the authors focused on the theoretical parts. However, a more comprehensive evaluation (even if it's on synthetic data) should have been done. Particularly, none of the theorems of section 4.6 are evaluated in the experiments. It is crucial to validate the theoretical claims empirically, especially those concerning robustness to kernel perturbations and generalization capabilities. The absence of such validation leaves a gap in the assessment of the practical relevance of these theoretical results.
- Some details on the baseline methods, UMKL, and sparse-UMKL, are unclear. For instance, the statement that the authors "experimented with an approach that learns graph representations and kernel weights simultaneously" requires further elaboration. The precise architecture of the GCN used, the optimization procedure, and how the joint learning is implemented should be detailed. Without these specifics, it's difficult to assess the validity of the comparison.
Minor weaknesses:
- Some of the numbers in Table 1 do not coincide with the numbers in the supplementary. (E.g., ACC for BZR and MUTAG.)
- It would be helpful if the authors could include the definitions of the clustering metrics in the appendix.

### Questions
1. I would appreciate it if the authors could comment on the limited experimental evaluation (see weaknesses). 
2. Can you explain why any parameter o>1 results in exactly the same performance for the selected clustering metrics? Can this be generalized or is it only the case in the considered experiments?
3. What ground truth was used e.g. for the clustering accuracy metric (ACC)? 
4. Did the authors consider the simple baseline where each weight is set to 1/M?
5. It is mentioned in section 4.5 that the learned composite kernel can directly be applied in supervised tasks. Have the authors tested this on graph classification tasks using the molecular benchmark graph datasets? 
6. Can the authors elaborate on the choice of representing graphs using a GCN for the baseline methods?

### Soundness
3

### Presentation
3

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
The paper introduces Unsupervised Multiple Kernel Learning for Graphs (UMKL-G), a method that combines multiple graph kernels without the need for labeled data. By preserving ordinal relationships among graphs through a probability simplex, UMKL-G aims to provide a unified, adaptive kernel learning approach for unsupervised graph-level clustering.

### Strengths
1. The paper presents an interesting concept by preserving ordinal relationships among graphs in an unsupervised setting, addressing a unique aspect of unsupervised kernel learning.
2. The authors provide proofs for stability, robustness, and generalization, which strengthen the theoretical foundation of the method.
3. The empirical validation across eight datasets provides a reasonable breadth of testing for the proposed approach.

### Weaknesses
1. Although the paper claims novelty in ordinal preservation, the methodology heavily relies on established techniques in probability simplex construction and multiple kernel learning. The main contribution appears to be an incremental adaptation rather than a breakthrough.
2. The method does not convincingly outperform modern baselines or recent self-supervised clustering methods, especially given that existing techniques like sparse-UMKL and GCN-based methods already achieve comparable results in unsupervised scenarios. This raises questions about the practical impact and added value of UMKL-G.
3. While the paper proposes potential extensions to broader data types (referred to as UMKL-X), there is no experimental evidence or conceptual framework supporting its effectiveness beyond graph-specific tasks. This reduces confidence in the generalizability and adaptability of the approach across different types of structured data.

### Questions
1. How does UMKL-G handle datasets with minimal ordinal relationships, or where graph similarities are uniform across samples?
2. Could the authors clarify the method’s sensitivity to the initial weight settings and the power hyperparameter o in the kernel concentration step?

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
4

### Summary
The paper proposes a new way to combine multiple graph kernels into a unified kernel value. The algorithm preserves topology through ordinal relations. This is mainly achieved by capturing important neighborhood structures by boosting the stronger similarities between graphs towards a set of target probabilities.

### Strengths
- Theoretical results are provided that guarantee stability and robustness of the method (e.g. Lipschitz continuity, robustness to kernel perturbations).
- UMKL-G outperforms existing methods on graph clustering benchmarks, demonstrating robust performance in unsupervised contexts on real and synthetic datasets.
- The method is applicable to a variety of datasets, making it versatile and potentially useful for many applications.

### Weaknesses
 - It is not entirely clear to me how this work differs significantly from existing MKL approaches, apart from the focus on ordinal relations. That is, the methodology, although well executed, seems to me an incremental extension of existing techniques.
- Some parts of the paper are technical and dense, which although I appreciate very much, makes the text particularly complicated to follow.
- Comparisons with other techniques, in particular more recent methods based on Graph Neural Networks (GNN), are limited. This reduces the perception of how competitive UMKL-G is compared to emerging technologies.
- Perhaps some focus on scalability is lacking, as testing on large datasets limits the evaluation of the method's effectiveness in real, large-scale scenarios.
- Large parts of the introduction and Section 2 are redundant. 
The writing is dense and the explanation of concepts complex. Greater clarity could make the work more accessible to a wider range of readers.

### Questions
- How does UMKL-G really stack up against GNN-based methods for clustering graphs? A more in-depth comparison could be useful to estimate the applicability despite methodological differences.
- What is the impact of the scalability of the method?

### Soundness
3

### Presentation
3

### Contribution
3
