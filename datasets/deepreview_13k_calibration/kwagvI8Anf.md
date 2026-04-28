# A Precompute-Then-Adapt Approach for Efficient Graph Condensation

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 5, 3

## Abstract
Graph Neural Networks (GNNs) have shown great success in leveraging complex relationships in data but face significant computational challenges when dealing with large-scale graphs. To tackle this issue, graph condensation methods aim to compress large graphs into smaller, synthetic ones that can be efficiently used for GNN training. Recent approaches, particularly those based on trajectory matching, have achieved state-of-the-art (SOTA) performance in graph condensation tasks.  Trajectory-based techniques match the training behavior on a condensed graph closely with that on the original graph, typically by guiding the trajectory of model parameters during training. However, these methods require repetitive re-training of GNNs during the condensation process, making them impractical for large graphs due to their high computational cost, \eg, taking up to 22 days to condense million-node graphs. In this paper, we propose a novel Precompute-then-Adapt graph condensation framework that overcomes this limitation by separating the condensation process into a one-time precomputation stage and a one-time adaptation learning stage. Remarkably, even with only the precomputation stage, which typically takes seconds, our method surpasses or matches SOTA results on 3 out of 7 benchmark datasets. Extensive experiments demonstrate that our approach achieves better or comparable accuracy while being 96× to 2,455× faster in condensation time compared to SOTA methods, significantly enhancing the practicality of GNNs for large-scale graph applications. Our code and data are available at \url{https://anonymous.4open.science/r/GCPA-F6F9/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces "Precompute-then-Adapt," a fast and efficient framework for graph condensation in large-scale Graph Neural Networks (GNNs). Unlike traditional methods that require repeated, costly retraining, this approach divides the process into a one-time precomputation phase and a one-time adaptation stage. This novel framework achieves competitive or superior results on several benchmarks, reducing condensation time and making GNNs far more practical for large-scale applications.

### Strengths
S1: Efficiency: The proposed"Precompute-then-Adapt" framework does significantly reduce the graph condensation process’s time,  and it effectively solves the repeat training consumption on the large-scale graph for existing structure-free methods, which sounds rational to me.

S2: High Performance with Simplified Methodology: The framework achieves expressive performance on several benchmark datasets with various condensation ratios, even with just the initial precomputation phase. Its one-time precompute strategy with both structure aggregation and semantic aggregation looks simple but efficient, making the proposed methodology practical.

S3: Clarity: The paper is well-structured, with a clear and logical flow that makes it easy to read and follow. All the experiential results are clearly demonstrated.

### Weaknesses
I do have some concerned questions in terms of methodology and experiments:

W1: Unlike methods such as GCOND-X and SFGC, which mimic the GNN's learning behavior, the proposed method appears independent of specific GNN backbones, focusing instead on operations at the graph data level without involving models (one-time precomputation is not related to trained GNNs). This raises a question: how does the approach ensure similar performance on the original test graph set when no explicit GNN model-based constraints are applied? Specifically, the method precomputes node features and graph structure without any feedback from the GNN training process, which could lead to a mismatch between the condensed graph and the optimal input for a specific GNN architecture. The lack of model-specific adaptation during precomputation is a potential limitation.

W2: For the ablation study, it only shows w/o structure and w/o semantics, what about only with precompute features but without the feature adaption module and contrastive learning? It is unclear how much each component contributes to the overall performance, and isolating the impact of the precomputed features alone is necessary to understand the effectiveness of the adaptation module and contrastive learning.

W3: Also for the ablation study, what is w/o both mean? does that mean using random initialized features to input the feature adaption module? If so, it is not clear whether the feature adaptation module can still learn meaningful representations from random inputs.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper propose a simple but effective and efficiency method for directly sample and merge node features (after message passing). Then using the alignment loss to enhance such features. The results are quite strong.

### Strengths
1. The performance of this work is comprehensive, typically including the PubMed and Products.
2. The effectiveness and efficiency are both impressive.

### Weaknesses
1. The methods used by the authors are not particularly novel, especially the use of contrastive loss for feature adaptation.
2. I find the structure of the condensed graph somewhat unclear; it appears that the condensed graph may lack structure. I suggest clarifying this aspect within the context.
3. The deeper rationale behind this straightforward method isn’t entirely apparent to me, yet it yields strong results. From my perspective, the pre-computation stage resembles the initialization of previous methods. I’m curious about the adaptation stage, which seems to primarily refine features selected in the pre-computation phase. Is it possible that the entire adaptation stage could be ablated?
4. The precomputation component, as I understand it, involves two main steps: (1) performing message passing, akin to SGC (Simplified Graph Convolution), and (2) randomly sampling nodes within each class and calculating the mean representation of their features. It seems to me that pre-aggregating features in this manner might create a significant out-of-distribution (OOD) issue for the downstream GNNs. This is because the precomputed features are inherently different from the raw test features. Moreover, with this approach, there’s a risk that the final representation may become over-smoothed, which could diminish its effectiveness.
5. If the features are initialized randomly, how do you align the labels of the condensed graph with the actual classes? Specifically, random initialization creates arbitrary features, and the goal of adaptation is to cluster these features into coherent groups. For example, in the Cora dataset, you would aim to form 7 distinct groups. However, how can you guarantee that, say, the first group of features corresponds to the first class label in the original dataset?
6. It’s not intuitively clear whether the precomputed aggregation combined with a condensed, edge-less graph performs better than simply using the naive features with a condensed graph which has edges. More evidence is needed to demonstrate this.
7. If you’re enhancing the class-wise differences using contrastive learning, how can you be certain that the learned features are IID (independently and identically distributed) with respect to the original dataset? In other words, when you initialize 7 groups of random features, you use contrastive loss to regenerate these groups, increasing the inter-group difference. My question is, do the features in the 1st generated group share the same distribution as the real 1st class features?
8. The current precomputation and adaptation methods appear to be more of a technical and incremental contribution. Most importantly, I still cannot fully understand why they lead to such significant improvements. The vague description of the “compact, structure-free” representation is not entirely convincing.
9. The theoretical evidence, which demonstrates that this method approximates existing non-precompute methods, does not address the core issue. The key question remains: why not avoid the OOD problem entirely by using existing methods, rather than introducing this method and subsequently mitigating the OOD issue? It would be more compelling to provide evidence that this method is better than existing non-precompute methods.
10. The empirical evidence is strong, but it still lacks a deeper understanding. The paper mentions methods like K-Center, GCond, SGDD, and GCDM, involving at least three distinct designs. To strengthen the argument, I suggest starting with their no-structure variants to build a more coherent findings. For instance, the GCond-X and GCDM-X variants discussed in their respective papers, and you could leverage these to establish stronger connections and uncover new insights. The current direct comparisons leave too many uncertain variables.
11. Is the target feature distribution also precomputed? I could not find a clear statement to this effect in Lines 242–255 of the manuscript. If this is the case, it constitutes a critical ambiguity in the writing. I strongly recommend revising this section to make it explicit.

### Questions
1. Please provide a deeper insight into your method, as I find this simple approach and its strong results intriguing. However, I remain unconvinced, as it seems to me like only a minor improvement on current initialization techniques, even prior to gradient-based or trajectory-based matching.
2. You might consider starting with some more ablation study, current one is quite short.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel Precomputethen-Adapt graph condensation framework. The framework overcomes the efficiency limitation of the trajectory-matching condensation methods. By separating the condensation process into a one-time precomputation stage and a one-time adaptation learning stage, it achieves good experimental performance on the standard benchmark.

### Strengths
1. The approach this paper proposed reduces computational costs compared to previous gradient-matching or trajectory-matching methods.
2. The experimental results demonstrate the effectiveness of the method to some extent.

### Weaknesses
1. The novelty of this paper is limited. On the one hand, the so-called one-time precomputation stage in this paper, utilizing the mean value of sampled data features, is similar to some feature-matching dataset distillation methods; moreover, the story of "semantic" alignment was also proposed in [1]. On the other hand, the one-time adaptation learning process also just utilizes the commonly used graph contrastive loss.
2. The presentation of the paper is relatively weak. Basic concepts like Graph Condensation and Structure-Free Graph Condensation are repeatedly mentioned in both the introduction and related work sections, taking up a large portion of the main text. Additionally, the authors do not clearly explain the interrelationship between the two components.
3. In the experiments, the performance of the previous state-of-the-art methods is inconsistent with and significantly different from the performance reported in related technical papers. Was the baseline method carefully reproduced? Moreover, the method has an excessive number of hyperparameters and configurations, but the authors do not provide the hyperparameter settings for each dataset and condensation ratio or a principal tuning method, which undermines the effectiveness of the proposed method.
4. Since N' is the number of synthetic nodes, in eq 3, for i = 1, 2, . . . , N  ->  for i = 1, 2, . . . , N'.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
