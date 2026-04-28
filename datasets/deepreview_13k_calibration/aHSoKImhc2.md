# NIMBA : Towards Robust and Principled Processing of Point Clouds With SSMs

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Transformers have become dominant in large-scale deep learning tasks across various domains, including text, 2D and 3D vision. However, the quadratic complexity of their attention mechanism limits their efficiency as the sequence length increases, particularly in high-resolution 3D data such as point clouds. Recently, state space models (SSMs) like Mamba have emerged as promising alternatives, offering linear complexity, scalability, and high performance in long-sequence tasks. The key challenge in the application of SSMs in this domain lies in reconciling the non-sequential structure of point clouds with the inherently directional (or bi-directional) order-dependent processing of recurrent models like Mamba. To achieve this, previous research proposed reorganizing point clouds along multiple directions or predetermined paths in 3D space, concatenating the results to produce a single 1D sequence capturing different views. In our work we introduce a method to convert point clouds into 1D sequences that maintains 3D spatial structure with no need for data replication, allowing Mamba’s sequential processing to be applied effectively in an almost permutation-invariant manner. In contrast to other works, we found that our method does not require positional embeddings, and allows for shorter sequence lengths while still achieving state-of-the-art results in ModelNet40 and ScanObjectNN datasets and surpassing Transformer-based models in both accuracy and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a improved approach to applying SSMs to 3D point cloud data. The study presents NIMBA, a Mamba-based model that uses a unique reordering strategy to convert 3D point clouds into 1D sequences while preserving spatial relationships, thus eliminating the need for positional embeddings and reducing data redundancy and computational overhead. Additionally, the NIMBA model demonstrates enhanced robustness to common data transformations.

### Strengths
1. The idea is simple and the paper is easy to follow.

2. Introducing Mamba to point clouds is non-trival and further improve the efficiency and robustness is important.

3. The analysis is soundness.

### Weaknesses
1. PointMamba, the article's main comparator, has been accepted by NeurIPS, and its methodology has been updated. The authors should revise the relevant descriptions in the article accordingly. Specifically, the comparison should be made against the latest version of PointMamba, taking into account any architectural or methodological changes that may impact performance. The current comparison with an older version may not accurately reflect the state-of-the-art.

2. In the paper, the authors assert that NIMBA does not rely on positional embedding (PE). However, the ablation study in section 4.3.1 indicates that NIMBA performs better with PE, contradicting their claim (see line 97). Additionally, the results in Table 2 also seem to include PE, leading to confusion. Furthermore, since PE is easy to compute and doesn't significantly increase computational burden, the claim that NIMBA can contribute without it raises questions, especially given that omitting PE results in decreased performance. The core issue is the model's reliance on PE for optimal performance, which undermines the claim of PE independence. The authors should clarify the role of PE and its impact on the model's overall design and performance.

3. The reviewer is also unsure how NIMBA validates global modeling with a sequence length N in the causal modeling Mamba. While sequence order can help preserve geometric relationships, the point patches still struggle to interact with each other. The causal nature of Mamba, processing the sequence sequentially, might limit the model's ability to capture long-range dependencies between distant patches. The authors should provide a more detailed explanation of how NIMBA achieves global modeling, given the inherent limitations of causal sequence processing, and how information is effectively propagated across the entire point cloud.

### Questions
See Weakness. Besides, there are few other suggestions:

1. Details in the writing require verification. For instance, the caption in Table 5 seems inaccurate; a full stop is missing at the end of lines 339 and 360.

2. The reviewers understand that the authors trained from scratch to better highlight the difference between each setting. However, stronger data augmentation and pre-training fine-tuning could still be added to demonstrate the upper limit of NIMBA's performance.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides detailed introductions to existing Mamba-based point cloud analysis strategies. Then, this paper proposes a point cloud state space method named NIMBA to remove positional embedding and avoid data replication in related methods. Experiments demonstrate that the NIMBA outperforms PointMamba in robustness while facing spatial variations.

### Strengths
1. The target to remove positional embedding and avoid data replication is valuable.
2. The overall writing is fluent and clear.

### Weaknesses
1. Since point clouds are 3D data, would ordering them along a single axis be sub-optimal? Specifically, while a single axis ordering may provide a starting point, the inherent 3D structure of point clouds suggests that a more sophisticated initial ordering strategy, or a method that considers inter-point relationships in 3D space, could be more effective. The current approach risks losing crucial spatial information by projecting the 3D data onto a 1D sequence.
2. Point clouds are highly spatially scattered and disordered. A manually pre-defined $r$ may not be suitable for all scenes. The fixed radius $r$ for determining neighborhood relationships might not adapt well to varying point densities or object scales within a scene. A static $r$ could lead to either over-segmentation in dense regions or under-segmentation in sparse regions, thereby limiting the method's robustness across diverse point cloud datasets. An adaptive approach to determine neighborhood relationships would be more beneficial.
3. This paper can provide an inference time analysis to present an improvement in efficiency by avoiding data replication. While the paper mentions avoiding data replication, a detailed analysis of inference time, comparing the proposed method with methods that replicate data, would provide a more concrete understanding of the practical benefits of the approach. This analysis should include not only the raw inference time but also the computational cost of the reordering strategy.

### Questions
1. Does Figure 2 illustrate that feeding wrong ordering centers to MAMBA Layers?

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
The paper introduces a novel method for processing 3D point clouds using State Space Models (SSMs), specifically the Mamba model. The key innovation is a strategy to convert 3D point clouds into 1D sequences that preserves the spatial structure without requiring data replication, thus enabling efficient sequential processing by Mamba in a permutation-invariant manner. The authors claim that their method surpasses Transformer-based models in accuracy and efficiency and does not require positional embeddings. The paper reports state-of-the-art results on ModelNet40 and ScanObjectNN datasets and demonstrates improved robustness against data transformations such as rotations and jittering.

### Strengths
1、The linear complexity of SSMs like Mamba, as opposed to the quadratic complexity of Transformer models, makes NIMBA highly scalable for high-resolution 3D data.

2、The paper shows that NIMBA is more robust to data transformations such as rotations and jittering, which is crucial for real-world applications where data can be subject to various distortions.

3、The elimination of positional embeddings and sequence replication makes the model more principled and less reliant on artificial constructs for sequence ordering.

### Weaknesses
1、One of the contributions proposed in this paper is the reordering strategy. However, this serialization strategy should be compared and discussed with the Point Cloud Mamba[1]. In the Point Cloud Mamba, many methods are discussed and compared, but they are all missing in this paper. There is even no specific discussion and comparison in the ablation studies. Furthermore, the performance of NIMBA's reordering strategy is dependent on the choice of the threshold parameter, which may require careful tuning for different datasets.

2、The paper notes that NIMBA shows limited improvement when scaled, suggesting that there may be optimization challenges that need to be addressed. There is a noted decline in performance when integrating NIMBA with Mamba2 or in hybrid architectures, indicating potential issues with model integration. Specifically, the lack of scaling improvements suggests a potential bottleneck in the model's architecture or training process that prevents it from effectively leveraging increased model capacity. The performance degradation in hybrid architectures raises concerns about the compatibility of NIMBA with other models and its ability to generalize beyond its specific training setup.

3、Comparative Analysis: The paper primarily compares NIMBA with Mamba-based models; a more comprehensive comparison with other state-of-the-art methods, especially those using different SSMs [1], [2], could provide a fuller picture of NIMBA's performance. Furthermore, this paper claims to surpass the transformer-based method, but it lacks many comparisons with such methods, such as PointBert[3], PointM2AE[4]. The absence of comparisons with transformer-based models, which are a common baseline in point cloud processing, makes it difficult to fully assess the claimed superiority of NIMBA. The limited comparison with other SSM-based methods also restricts the understanding of NIMBA's relative performance within the broader landscape of sequence-based point cloud processing.

4、 How was the threshold parameter determined, and how sensitive is the model's performance to changes in this parameter? How does the removal of positional embeddings affect the model's interpretability, and can the learned representations be easily understood?

5、While the paper claims efficiency improvements, are there specific computational cost analyses, especially for large-scale datasets? The lack of detailed computational cost analysis, particularly for large-scale datasets, makes it difficult to validate the claimed efficiency improvements. A thorough evaluation should include metrics such as training time, inference time, and memory usage, especially when compared to other methods.

### Questions
Refer to weakness part.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces NIMBA, a new method for point cloud analysis using state-space models (SSMs). The key contribution is a new strategy that converts 3D point clouds into 1D sequences while preserving spatial structure, eliminating the need for positional embeddings. NIMBA builds on the Mamba architecture to improve efficiency and accuracy in tasks like object classification and segmentation. The authors demonstrate that NIMBA outperforms both transformer-based and other SSM-based methods on multiple datasets such as ModelNet40 and ScanObjectNN, showing enhanced robustness to noise and spatial transformations.

### Strengths
1. The paper proposes a novel method for converting 3D point clouds into sequences without replication or positional embeddings.
2. Significance: NIMBA achieves state-of-the-art results on multiple datasets, outperforming both transformer and SSM-based baselines.
3. The methodology is well-structured, with clear comparisons to prior work, though some sections could be streamlined for better readability.

### Weaknesses
1. Scaling limitations: The model shows limited improvement when scaled, suggesting potential optimization challenges. It would be better if they could verify the effectiveness on larger point cloud datasets, like nuScenes, and Waymo. The lack of significant performance gains with increased model size raises concerns about the inherent scalability of the approach, particularly when dealing with more complex and larger point cloud datasets. The authors should investigate whether the bottleneck lies in the sequence conversion strategy or the Mamba architecture itself.
2. Performance declines were observed when replacing the Mamba block with the Hydra block, indicating possible limitations in hybrid architectures. This suggests that the proposed method might be highly sensitive to the specific architecture of the sequence processing block. The authors need to explore the reasons behind this performance drop, such as potential incompatibility between the NIMBA's sequence representation and the Hydra block's processing mechanism, or whether the Hydra block is not as effective as Mamba for this specific type of sequential data.
3. some typos should pay attention to, e.g., 
  a) line 099: positional emebddings might be positional embeddings;
  b) line 352: flattered by ordering might be flattened by ordering;
  c) line 377: environment might be environment
  d) line 523: conclusion and Fig. 2 show
  and some formatting issues

### Questions
1. Could the authors provide more intuition behind the choice of the proximity threshold of 0.8?
2. Have the authors considered alternative strategies for scaling the model to larger datasets, like nuScenes and Waymo?
3. Hybrid models: what are the potential avenues to optimize NIMBA when integrated with hybrid architectures like Hydra?

### Soundness
4

### Presentation
3

### Contribution
3
