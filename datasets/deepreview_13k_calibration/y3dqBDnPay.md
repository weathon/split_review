# HyperRep: Hypergraph-Based Self-Supervised Multimodal Representation Learning

- Decision: Reject
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Self-supervised representation learning on multimodal data plays a pivotal role in proficiently integrating and embedding information from various sources without the need for additional labeling. Notably, the majority of existing methods overlook the complex high-order inter- and intra-modality correlations characteristic of real-world multimodal data. In this paper, we introduce HyperRep, which combines the strength of hypergraph-based modeling with a self-supervised multimodal fusion information bottleneck principle. The former captures high-order correlations using hypergraphs to represent inter- and intra-modality relations, while the latter constrains the solution space, ensuring a more effective fusion of multimodal data. Our extensive experiments on four public datasets for three downstream tasks demonstrate HyperRep's superiority, as it consistently delivers competitive results against state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a self-supervised representation learning method on multimodal data based on hypergraph-based learning called HyperRep by combining the strength of hypergraph-based modeling with a self-supervised multimodal fusion information bottleneck principle. The extensive experiments on four public datasets including three downstream tasks demonstrate the advantages of the proposed method, which are also validated by the comparison with the state-of-the-art approaches.

### Strengths
1.	The idea of using hypergraph-based self-supervised multimodal representation learning is interesting as it captures the high-order relationships in multimodal data.
2.	Compared to most multimodal learning work using semi-supervised approaches which requires additional label information, the proposed approach is employing self-supervised learning. The derived hypergraph attention module and propagation is a good extension from current approaches.
3.	The author also introduced multimodal fusion information bottleneck (MFB) principle, in order to maximize the mutual information between the instance and each modality. The corresponding upper bound and lower bound are derived.
4.    The experimental evaluation is detailed and extensive.

### Weaknesses
1. Overall, while the idea is interesting, the scope is relatively narrow as it combines self-supervised learning with multimodal representation learning based on hypergraph. However, hypergraph attention network for multimodal learning has been explored in
https://openaccess.thecvf.com/content_CVPR_2020/papers/Kim_Hypergraph_Attention_Networks_for_Multimodal_Learning_CVPR_2020_paper.pdf
Compared to this CVPR 2020 paper, the only novel part for the manuscript seems to be adding self-supervised learning on top of it. However, that novelty is relatively small.

2. The performance gain appears to be incremental as the paper serves as an extension to recent work.

### Questions
1 The author needs to distinguish the work better with the previous work especially many module presented in this paper such as hypergraph attention module has been published before. So a reference shoud be given and explain the difference if there is any.

2.While the lower bound and upper bound are derived, it is important to show how to leverage these bounds for optimization.

3.The contribution of the paper is not very clear.

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
This paper aims to solve the existing challenges in self-supervised representation learning, where most of the existing work overlooks the high-order inter- and intra-modality correlations characteristics and lacks effective fusion principles. To tackle these issues, the author proposed HyperRep, which combined hypergraph-based modeling and self-supervised multimodal fusion principle to achieve superior representation learning.

### Strengths
1. The paper is well-written and nicely-structured.

2. The paper proposed hypergraph-based representation learning creatively uses graph structure to represent the inter- and intra-modal relationships for multi-modal data, which helps the model capture high-order correlations of the instances.

3. The proposed MFB loss leverages the bottleneck principle to encourage the model to capture the most informative aspects of the data and is demonstrated over multiple downstream tasks.

4. The authors conducted diverse ablation studies that demonstrate the effectiveness of different components of the proposed method and the ability of handling missing modalities. This makes the method suitable for real-world applications.

5. There is a consistent improvement in performance over all three downstream tasks, clustering, text to video retrieval and action localization over prior baselines.

### Weaknesses
1. In the hypergraph construction process, which is a preprocessing step for the data, has a computational complexity of O(n^2d). This may limit the scalability of the method for datasets with a large amount of instances or more complex data (high-resolution images). The quadratic complexity with respect to the number of instances *n* is a significant bottleneck, especially considering that *d* represents the dimensionality of the feature space, which can also be quite large. This preprocessing step could become prohibitively expensive for large-scale datasets, making the method impractical in many real-world scenarios. Furthermore, while the authors mention pre-trained models handle feature extraction, the hypergraph construction still operates on the extracted features, meaning that high-dimensional feature vectors from complex data will still contribute to the computational burden.

2. Lacking experiment that provides a detailed analysis of the interpretability of the learned representations. It is unclear how the model is capturing the high-order correlations and what specific features or relationships are being encoded in the learned representations. Without a clear understanding of what the model has learned, it is difficult to trust the results or to generalize the method to new tasks or datasets. The authors should provide more insight into the internal workings of the model.

3. It would be better to add the results from baseline methods in Figure 9. The absence of baseline results makes it difficult to assess the relative performance of the proposed method. A direct comparison with existing methods is crucial to understand the advantages and limitations of the proposed approach.

4. In Table 3, it looks like row 1 (high order correlation) has a big say in the final scores, while InfoNCE doesn't seem to make much of a difference in the end results. It would have been really helpful to have a deeper analysis of this, maybe with some t-SNE results, to better grasp how these representations work. The ablation study suggests that the high-order correlation component is the primary driver of performance, while the InfoNCE loss contributes minimally. This raises questions about the necessity of the InfoNCE component and the overall design of the loss function. A more detailed analysis is needed to understand the interplay between these two components and their impact on the learned representations.

### Questions
How are the k-NN selected for both training and validation phase?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes HyperRep, a self-supervised representation learning method for multimodal data that leverages hypergraphs to capture high-order inter- and intra-modality correlations. HyperRep also uses an information bottleneck principle to fuse multimodal data effectively. The paper shows that HyperRep outperforms existing methods on various downstream tasks.

### Strengths
1. This paper provides sufficient and detailed formal definitions and necessary proofs.
2. The application of hypergraphs in this paper may inspire the field of multimodal self-supervised learning.
3. The authors conducted extensive ablation experiments on multiple datasets.

### Weaknesses
1. Motivation: The paper highlights the use of hypergraphs to capture higher-order correlations among modalities. However, I find the paper insufficient in explaining and analyzing why higher-order correlations are essential for multimodal self-supervised learning. This is especially relevant since most existing methods, such as the CLIP[1] series and ImageBind[2], rely on pair-wise multimodal self-supervision.
2. Method: The paper could improve the clarity and presentation of MFB. For instance, how does Eq. 12 relate the mutual information of shared and instance features? A clearer explanation of the illustration would be helpful. Also, the MFB module in Figure 2 is vague, and a more specific illustration could enhance the readers’ comprehension of the method.
3. Experiment: The paper lacks comparisons with recent (2023) methods, as the only one mentioned has a huge performance gap with the classical methods. Could the paper also compare with more popular Foundation models, such as VideoCLIP[3] and OmniVL[4]? Moreover, Table 1 shows that graph-based methods perform poorly, and Table 2 reveals a drastic performance drop after removing higher-order correlations. However, AGC achieves high performance without using higher-order correlations. Does this imply that higher-order correlations are crucial for the proposed method, but not for the multimodal self-supervised learning task?

### Questions
How come the MIL-NCE performance in Table II differs so much from the original paper? Are there any differences in the experimental settings?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces HyperRep, a hypergraph-based self-supervised multimodal representation learning method that captures high-order correlations in real-world multimodal data. The proposed approach balances the benefits of contrastive methods and preserves the unique aspects of each data point, achieved through the construction of dual types of hypergraphs. The paper presents experimental results on several downstream tasks, demonstrating that HyperRep delivers consistently competitive results against state-of-the-art methods.

### Strengths
The idea of using hyperedge to facilitate multi-modal fusion is interesting.

The paper is clear and easy to follow.

### Weaknesses
For the Hypergraph propagation module figure (Fig. 3), a more detailed and clearer introduction should be helpful.

There are a few typos. Please find and correct them.

### Questions
1. May the author explain whether  HyperRep requires pre-trained encoder for each modal or it trains these encoders using the MFB loss? If pre-trained encoders are used, may the author provide ablation about the encoders used in the experiment?
2. May the author explain the intuition behind using the instance hyperedge features for the downstream task, not the instance feature itself?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
