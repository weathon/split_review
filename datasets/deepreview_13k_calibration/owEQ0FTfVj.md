# GlycanML: A Multi-Task and Multi-Structure Benchmark for Glycan Machine Learning

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Glycans are basic biomolecules and perform essential functions within living organisms. The rapid increase of functional glycan data provides a good opportunity for machine learning solutions to glycan understanding. However, there still lacks a standard machine learning benchmark for glycan property and function prediction. In this work, we fill this blank by building a comprehensive benchmark for \textbf{Glycan} \textbf{M}achine \textbf{L}earning (\textbf{\our{}}). The \our{} benchmark consists of diverse types of tasks including glycan taxonomy prediction, glycan immunogenicity prediction, glycosylation type prediction, and protein-glycan interaction prediction. Glycans can be represented by both sequences and graphs in \our{}, which enables us to extensively evaluate sequence-based models and graph neural networks (GNNs) on benchmark tasks. Furthermore, by concurrently performing eight glycan taxonomy prediction tasks, we introduce the \textbf{\ourmtl{}} testbed for multi-task learning (MTL) algorithms. Also, we evaluate how taxonomy prediction can boost other three function prediction tasks by MTL. Experimental results show the superiority of modeling glycans with multi-relational GNNs, and suitable MTL methods can further boost model performance.io/project}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to and succeed in providing a standard machine learning benchmark for **glycans**. It will clearly benefit the future research in studying glycan property and function prediction via application of machine learning models, and it will make positive impacts on bioinformatics and biological intelligence community. The proposed benchmark **GLYCANML** consists of multiple essential task in glycans research, and the benchmark also offers diverse data modalities, mainly sequence representations and graph representations. Additionally, the *GLYCANML-MTL* testbed is designed to support multi-task learning (MTL), where glycan taxonomy tasks are addressed collectively to assess knowledge transfer across related prediction tasks.

### Strengths
1. **Having a clear as well as straightforward motivation and contribution**. The benchmark is highly relevant for advancing glycan-related machine learning research, offering a platform to assess various models on tasks that are both scientifically and practically significant in fields like immunology and molecular biology.
2. **Well-written paper; addressing each detail of GLYCANML thoroughly**. The paper is comprehensive, including detailed dataset construction, task definitions, and experimental protocols. It also provides a robust comparison of baseline models, which supports its claims of model performance and suitability.
3. **High benchmark quality: multiple tasks and diverse modalities provided; allowing multitask learning and multimodal training**. The *GLYCANML-MTL* setup for multi-task learning offers a unique opportunity to test MTL methods in a real-world scenario with related biological tasks, demonstrating the potential to improve performance through shared learning.

### Weaknesses
1. **Broader Impact of the Datasets**. From my understanding the dataset is very good resource for the application related to Glycans. However, for machine learning, it is not clear how this dataset is different from previous ones and what new insights it can bring to the domain of graph learning or multi-task learning. Specifically, the paper does not articulate the unique structural properties of glycan graphs that would necessitate novel graph learning approaches, beyond what is already established for molecular graphs. Similarly, for multi-task learning, the paper does not sufficiently justify why the proposed tasks pose a unique challenge compared to existing multi-task benchmarks, particularly in terms of class imbalance and task relatedness.
2. **Lack of Multimodal Encoders**. The benchmark has sequence and graph representation, and it is good to show the performance of multimodal molecular encoders like MolFormer [1]. The absence of a thorough evaluation using such models is a notable oversight, especially given the availability of both sequence and graph data. This limits the benchmark's ability to assess the full potential of multimodal learning in the context of glycans.
3. **More Pretrained Model Performance**. The paper did not explicitly say whether using the checkpoints for Graphormer or not, and if indeed using the pretrained checkpoint, it will also surpise me that a pretrained model even fail to match the standard sequence models and graph models. Also, other pretrained models, such as MolCLR [2], can be presented. The lack of a comprehensive evaluation of pretrained models, including a clear statement on whether pretrained weights were used, makes it difficult to assess the true potential of the proposed benchmark and the baseline models.

### Questions
See above weaknesses.

### Soundness
4

### Presentation
3

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
This paper presents a benchmark for evaluating different graph encoders and multi-task learning frameworks on glycan data, covering four tasks with corresponding curated datasets. The benchmark results reveal interesting findings, such as the effectiveness of shallow CNNs as strong baselines and all-atom encoders fail to achieve better performance than GNN-based models.

### Strengths
- The application of machine learning on glycans is interesting and unexplored. The curated datasets can benefit the model development and future studies.
- The studied multi-task learning on glycans demonstrates the strong correlation between different tasks.

### Weaknesses
 - As a benchmark study, the GNN encoders and multi-task learning methods compared in the paper are not state-of-the-art. More advanced methods should be included in the benchmark for a comprehensive evaluation, such as [2,3,4,5]. Specifically, the choice of GNNs seems limited, and the benchmark would benefit from including more recent architectures that incorporate attention mechanisms or more sophisticated message-passing schemes. Furthermore, the multi-task learning methods explored do not fully represent the current landscape of techniques, which includes methods that dynamically adjust task weights or utilize gradient manipulation strategies.
- Without context such as cell type or antigen, predicting immunogenicity based solely on glycan input is not practically useful since immunogenicity is heavily influenced by the biological context. Immune recognition often involves complex molecular interactions influenced by surrounding biomolecules and cellular environments. The simplification of the problem to only consider glycan structure neglects the crucial role of the protein antigen and the specific cellular environment in determining immunogenicity. This limits the practical applicability of the benchmark for real-world immunological studies.
- One suggestion for Protein-Glycan Interaction Prediction is to conduct the splitting based on the sequence identity of binding sites instead of the whole protein sequence identity[1], which can provide a more solid evaluation protocol. Using whole protein sequence identity for splitting may lead to data leakage, where similar binding sites are present in both training and test sets, inflating performance metrics. A more rigorous evaluation would involve splitting based on the actual binding site sequences to ensure that the model is truly generalizing to novel interactions.

### Questions
- Why is the sequence identity threshold set to 0.5? A common choice would be 0.3 in protein-related studies [1,2].

[1] Evaluating Representation Learning on the Protein Structure Universe, ICLR2024.

[2] Learning from Protein Structure with Geometric Vector Perceptrons, ICLR2021

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper first benchmark paper on ML for Glycans.

### Strengths
Introducing an important problem in the field of biology to the machine learning community and creating a new problem is very significant.

### Weaknesses
 - Since biology is not my major field, there needs to be more emphasis on how biologically significant glycans are.
- There needs to be a discussion on how well this paper fits the ICLR conference.
- Collecting the benchmark dataset does not seem to pose significant challenges. What challenges are there?
- All data splits are based on motif-based splits, but there is no discussion on the biological significance of motifs. From the perspective of scientific discovery, is a motif-based approach appropriate for modeling the real world? It seems that data could also be split by methods such as random, monosaccharide composition, or glycosylation type, and there needs to be a discussion on this.

### Questions
- To my knowledge, glycans have not received much attention at ML conferences compared to proteins. Is there a specific reason for this?
- In a glycan planar graph, nodes are monosaccharides. What feature information is used in this case?

### Soundness
3

### Presentation
3

### Contribution
3
