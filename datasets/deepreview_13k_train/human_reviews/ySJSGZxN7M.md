# Dual-Branch HNSW Approach with Skip Bridges and LID-Driven Optimization

- Decision: Reject
- Scores: 1, 5, 5

## Abstract
The Hierarchical Navigable Small World (HNSW) algorithm is widely used for approximate nearest neighbor (ANN) search, leveraging the principles of navigable small-world graphs. However, it faces some limitations. The first is the local optima problem, which arises from the algorithm's greedy search strategy, selecting neighbors based solely on proximity at each step. This often leads to cluster disconnections. The second limitation is that HNSW frequently fails to achieve logarithmic complexity, particularly in high-dimensional datasets, due to the exhaustive traversal through each layer. To address these limitations, we propose a novel algorithm that mitigates local optima and cluster disconnections while improving inference speed. The first component is a dual-branch HNSW structure with LID-based insertion mechanisms, enabling traversal from multiple directions. This improves outlier node capture, enhances cluster connectivity, and reduces the risk of local minima. The second component introduces a bridge-building technique that adds shortcuts between layers, enabling direct jumps and speeding up inference. Experiments on various benchmarks and datasets showed that our algorithm outperforms the original HNSW in both accuracy and speed. We evaluated six datasets across Computer Vision (CV), deep learning (DL), and Natural Language Processing (NLP), showing improvements of 2.5% in NLP, 15% in DL, and up to 35% in CV tasks. Inference speed is also improved by 12% across all datasets. Ablation studies revealed that LID-based insertion had the greatest impact on performance, followed by the dual-branch structure and bridge-building components.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposed a branching scheme to accelerate HSNW search. Supposedly, this scheme could find out some more useful starting point in the layer-0 of the HSNW method. The experimental setup is completely wrong and thus I can't draw a conclusion that experiments validate the claim.

### Strengths
- Work on an important problem for practical application.

### Weaknesses
 - I implemented HSNW from scratch and published HSNW-related algorithm in top data mining conferences before. The experimental setup is completely nonsense to me. It should sort of follow-up the ANN-benchmark setup and that's a more reasonable way to show results. 

- Apparently, the algorithm doesn't compare to the real HSNW implementation in wall clock time, and only compare their own variations. 

- The algorithm seems to be implemented in Python only, which is sort of contradicting to the point of AKNN. Most HSNW algorithm is implemented in C, and there is a reason for that. Many algorithm improvement can't really benefit the search as the real-world hardware doesn't support well for the operations; or the asymptotic analysis doesn't align well with the real operation cost. Unless the authors showed their modified algorithm can accelerate in C (doubtful as there are so many branching and that possibly will cause memory read busy), it's not very convincing. 

- It reads to me that the method is only adding more operations in top layers. So it has to at least numerically show how many IP/distance calculation it saves for the layer-0. Otherwise, the computational cost can only go up......

- So even under the query time reported in Fig. 10, it's not very promising. Just based on the Figure 10, I will say it's not a really working method.

- The paper is not very straightforward to understand as it lacks a running example. I really don't know what exactly "exclude_set" contains. A running example or any pictorial example in Figure 3 helps.

The definition of LID (x) is unclear. LID(x) reads like query dependent, or say LID(q) is something we want. That means there will be a property per graph/query pair, but in Figure 2/3, there seem to be multiple high LID nodes. I'm not sure what exactly LID means.

### Questions
- The paper is not very straightforward to understand as it lacks a running example. I really don't know what exactly "exclude_set" contains. A running example or any pictorial example in Figure 3 helps.

The definition of LID (x) is unclear. LID(x) reads like query dependent, or say LID(q) is something we want. That means there will be a property per graph/query pair, but in Figure 2/3, there seem to be multiple high LID nodes. I'm not sure what exactly LID means.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper The proposed HNSW++ algorithm, which introduces a dual-branch structure, LID-based node insertion, and skip-layer bridges to address the limitations of the original HNSW, such as local optima and cluster disconnections. Experiments have shown the that the proposed method is competitive both in performance and in inference speed.

### Strengths
1. The dual-branch structure and LID-based insertion mechanism are well-motivated and novel.

1. The experiments have (partially) shown the effectiveness of the proposed method.

### Weaknesses
My major concerns are about experiments.

1. The proposed method is implemented in Python, which is not a good programming language model for comparing speed. The authors may provide a theoretical time complexity analysis to complement their empirical results. This would allow a fairer comparison of the algorithm's efficiency across different implementations.

2. The baselines are relatively weak, I did not see the advanced methods (e.g., IVFPQ) used in faiss[1]. I'd like to have authors justify their choice of baselines and explain why stronger baselines were not included.

### Questions
please refer to weaknesses

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
4

### Summary
This paper presents an enhanced Hierarchical Navigable Small World (HNSW) algorithm addressing limitations in local optima and scalability by introducing a dual-branch structure with LID-based insertion and a bridge-building shortcut technique. These innovations improve cluster connectivity, capture outliers more effectively, and reduce inference time. Experimental results across NLP, DL, and CV datasets demonstrate notable accuracy and speed improvements over the original HNSW algorithm.

### Strengths
1)This paper presents a novel enhancement to the HNSW algorithm, addressing key limitations related to local optima and inference speed. 
2)The research is evaluated across diverse benchmarks, including datasets from Computer Vision (CV), Deep Learning (DL), and Natural Language Processing (NLP). The experiments clearly support the proposed method's superiority in both accuracy and speed, with substantial performance gains.
3）The paper is well-written, with clear explanations of complex concepts and methods.

### Weaknesses
1)The related work section is overly concise, lacking a comprehensive review of current research, which limits contextual understanding of the contributions.
2)Although the paper claims improvements in inference speed, Figures 9 and 10 show only modest gains, casting doubt on the practical significance of this claim.
3)The experimental evaluations are relatively limited, with insufficient algorithmic comparisons; in particular, using only the GLOVE dataset for NLP benchmarks diminishes the persuasiveness of the results in this domain.

### Questions
The paper introduces an optimization algorithm for HNSW,  including pseudocode for the dual-branch structure, LID-based insertion, and bridge-building techniques would enhance clarity and understanding.

### Soundness
3

### Presentation
3

### Contribution
2
