# Through the Dual-Prism: A Spectral Perspective on Graph Data Augmentation for Graph Classification

- Decision: Reject
- Scores: 8, 6, 5, 5

## Abstract
\vspace{-0.5em}
Graph Neural Networks (GNNs) have become the preferred tool to process graph data, with their efficacy being boosted through graph data augmentation techniques. Despite the evolution of augmentation methods, issues like graph property distortions and restricted structural changes persist. This leads to the question: \textit{Is it possible to develop more property-conserving and structure-sensitive augmentation methods?} Through a spectral lens, we investigate the interplay between graph properties, their augmentation, and their spectral behavior, and found that keeping the low-frequency eigenvalues unchanged can preserve the critical properties at a large scale when generating augmented graphs. These observations inform our introduction of the Dual-Prism (DP) augmentation method, comprising DP-Noise and DP-Mask, which adeptly retains essential graph properties while diversifying augmented graphs. Extensive experiments validate the efficiency of our approach, providing a new and promising direction for graph data augmentation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel graph data augmentation method called Dual-Prism (DP), which aims to retain essential graph properties while diversifying augmented graphs. The authors draw inspiration from the way prisms decompose and reconstruct light and how polarizers selectively filter light to design their own "polarizer". They conduct extensive experiments on diverse real-world datasets and demonstrate that their proposed methods can achieve state-of-the-art performance on most of the datasets. This work provides a promising new direction for graph data augmentation.

### Strengths
The Dual-Prism (DP) augmentation method proposed in this paper is a novel approach to graph data augmentation. The authors draw inspiration from optics to design their own "polarizer" that retains essential graph properties while diversifying augmented graphs. This innovative approach provides a new direction for graph data augmentation.

The authors conduct extensive experiments on 21 real-world datasets spanning various learning paradigms. The experimental results demonstrate that their proposed methods can achieve state-of-the-art performance on most of the datasets. This extensive evaluation provides strong evidence for the efficacy of the DP augmentation method. 

The authors provide empirical evidence to substantiate their approach. They explain the rationale behind their DP method and how it skillfully preserves graph properties while ensuring diversity in augmented graphs. This work also proposes the globally-aware and property-retentive augmentation methods, DP-Noise and DP-Mask, which are able to preserve inherent graph properties while simultaneously enhancing the diversity of augmented graphs.

### Weaknesses
The authors could delve deeper into the influence of various hyperparameters on the performance of the Dynamic Programming (DP) method. Although they provide some details on the hyperparameters used in their experiments, a more detailed exploration could potentially identify optimal hyperparameters for different types of graphs and learning tasks.

Moreover, it would be compelling to examine the effectiveness of the proposed DP method on larger and more complex graphs. Despite conducting experiments on 21 real-world datasets, extending this to larger, more complex graphs could further validate the efficiency of their proposed method and offer valuable insights into its scalability.

### Questions
The authors could enhance their study by further investigating the effect of various hyperparameters on the Dynamic Programming (DP) method's performance. While details of the used hyperparameters are given, a more comprehensive exploration could help identify optimal hyperparameters for diverse graph types and learning tasks. Additionally, testing the proposed DP method on larger and more complex graphs, beyond their 21 real-world datasets, could further validate the method's efficiency and provide insights into its scalability.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Graph neural networks (GNNs) have become the preferred tool to process graph data. This paper aims to develop property-conserving and structure-sensitive augmentation methods. Through a spectral lens, the authors investigate the interplay between graph properties, their augmentation, and their spectral behavior, and found that keeping the low-frequency eigenvalues unchanged can preserve the critical properties at a large scale when generating augmented graphs.

### Strengths
1. The writing is clear, and the paper is easy to follow.
2. Instead of proposing another random approach, the authors provide their rationale clearly and comprehensively based on empirical evidence.
3. The experiments are done extensively for 4 different tasks, on 21 datasets, and against numerous competitors.

### Weaknesses
1. Since the accuracy improvement over competitors is not dramatic, statistical tests such as the Wilcoxon signed-rank test would be beneficial.
2. Changing high-frequency eigenvalues is similar to making small, marginal changes to the graph structure while preserving the core properties, such as connectivity. In that sense, NodeSam [1] and MotifSwap [2] are better competitors than mixup-based approaches, which induce more changes to the structure.
3. Although this paper discusses extensively the reasons why we should focus on high-frequency eigenvalues, there is little discussion on how to actually modify them. Simply using random masking or adding random noise appears too naive. Additional discussion on this part, e.g., how to safely alter these eigenvalues to create plausible augmented graphs, or how we might mix-up the eigenvalues between different graphs, would be valuable.

[1] J. Yoo et al. “Model-Agnostic Augmentation for Accurate Graph Classification.” WWW 2022

[2] J. Zhou et al. "Data Augmentation for Graph Classification.” CIKM 2020

### Questions
1. How long does it take to eigendecompose the matrix L? Is the complexity linear with the size of a graph?
2. Apart from Figure 2b, could you provide more examples of augmented graphs resulting from changes to the eigenvalues?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the graph-level tasks with graph augmentation techniques. To be specific, they propose to perturb the high-frequency part of the given graphs to generate augmented graph samples, so as to boost the performance of graph-level tasks.

### Strengths
S1. The presentation of this paper is excellent, and the paper is well-organized.

S2. This paper includes comprehensive experiments, including supervised, unsupervised, and transfer learning settings.

S3. The proposed method is concise but its performance on the supervised learning tasks is good.

### Weaknesses
W1. The main concern of this paper is its novelty, which is low and being studied in many existing works.

W2. A minor drawback of this paper is its performance. It shows strong performance in the supervised settings but gets average performance in other settings. In addition, some experimental results are missing, which is not expected.

I will elaborate more in detail in the Questions setting.

### Questions
Q1. My main concern with this paper is its novelty. Which shares great overlap with this paper [1], as multiply mentioned by the authors. Though they are not invented for the same purpose, it is not hard to transfer the idea from [1] into the context of this paper.

Q2. In section 3.2, many observations have been mentioned by existing works. For example, **Obs 2. Low-frequency components display greater resilience to edge alterations** has been mentioned in existing work [2]. **Obs 4. Specific low-frequency eigenvalues are
closely tied to crucial graph properties.**, as this paper mentioned in Section 4.3, has been studied thoroughly by Chung in the spectral graph theory [3].

Q3. The proposed Algorithm 1 first decomposes the graph Laplacian L,  perturbs the high-frequency part (larger eigenvalues of L), and finally reconstructs the perturbed adjacency matrix. I think a simpler version is directly decomposing the adjacency matrix A and perturbing its (A's) small eigenvalues. From this perspective, it is similar to many classic low-rank approximation-based works on graphs.

Q4. The performance in the supervised setting is good, which is shown in Table 1. However, its performance in unsupervised learning (Table 3) and transfer learning settings (Table 4) is average.

Q5. A suggestion for this paper is to finish experiments in Tables 1,2, and 3, where now they are shown '-'. Ideally, if the experiments are not conducted in existing papers, authors should implement the baseline methods and report the results in those missing setting by themselves.

[1] Lin, Lu, Jinghui Chen, and Hongning Wang. "Spectral Augmentation for Self-Supervised Learning on Graphs." In The Eleventh International Conference on Learning Representations. 2023.

[2] Wang, Haonan, Jieyu Zhang, Qi Zhu, and Wei Huang. "Augmentation-free graph contrastive learning with performance guarantee." arXiv preprint arXiv:2204.04874 (2022).

[3] https://mathweb.ucsd.edu/~fan/mypaps/fanpap/111diameters.pdf

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on developing a more property-conserving and structure-sensitive augmentation method. To achieve this, authors first investigate the interplay between graph properties, their augmentation, and their spectral behavior to derive that keeping the low-frequency eigenvalues unchanged can preserve the critical properties at a large scale. They then propose Dual-Prism (DP), an augmentation method that adeptly retains essential graph properties while diversifying augmented graphs.

### Strengths
1. This paper is well-motivated. Developing a more property-conserving augmentation method has long been focused on.
2. Comprehensive experiments prove the performance of the proposed method.

### Weaknesses
1. It has long been proven that low-frequency information is valuable for graphs and the idea to augment more high-frequency components can be easily derived from previous works[1], which makes the proposal less innovative. What is the advantage of the proposed method in maintaining low-frequency information? The authors should also compare DP with SpCo[1] in the experiments.
2. The proposed method looks not efficient enough. It seems that Algorithm 1 involves eigenvalue decomposition and Laplacian Matrix reconstruction, which are both expensive. A time analysis would make the proposal more convincing.
3. The experiment currently lacks graphs with large node numbers such as ogbn-arxiv and ogbn-proteins[2]. 
4. Why is the improvement of the DP method over previous ones marginal in some cases in Tables 1 to 4?
5. In Obs 4, proof to the proposition "preserving key eigenvalues while modifying others enables the generation of augmented graphs that
uphold foundational properties"  is relatively insufficient, especially when the authors use the spectral variation defined only by a single previous work.
6. The font size in some figures is too small.

[1] Revisiting graph contrastive learning from the perspective of graph spectrum. Advances in Neural Information Processing Systems, 2022.\
[2] Open graph benchmark: Datasets for machine learning on graphs. Advances in Neural Information Processing Systems, 2020.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
