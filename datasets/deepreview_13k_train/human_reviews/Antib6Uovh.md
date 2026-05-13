# A Theoretical Analysis of Self-Supervised Learning for Vision Transformers

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Self-supervised learning has become a cornerstone in computer vision, primarily divided into reconstruction-based methods like masked autoencoders (MAE) and discriminative methods such as contrastive learning (CL).  Recent empirical observations reveal that MAE and CL capture different types of representations: CL tends to focus on global patterns, while MAE adeptly captures  **both global and subtle local** information simultaneously. Despite a flurry of recent empirical investigations to shed light on this difference, theoretical understanding remains limited, especially on the dominant architecture **vision  transformers** (ViTs). In this paper, to provide rigorous insights, we model the visual data distribution by considering two types of spatial features: dominant global features and comparatively minuscule local features, and study the impact of imbalance among these features.  We analyze the training dynamics of one-layer softmax-based ViTs on both MAE and CL objectives using gradient descent. Our analysis shows that as the degree of feature imbalance varies, ViTs trained with the MAE objective effectively learn both global and local features to achieve near-optimal reconstruction, while the CL-trained ViTs favor predominantly global features, even under mild imbalance. These results provide a theoretical explanation for distinct behaviors of MAE and CL observed in empirical studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper is about understanding and contrasting the behavior of two pretraining techniques used for ViT architectures: Masked Auto-encoding and Contrastive Learning. They aim at providing convergence guarantees for this behavior as well. The overall conclusion is that the MAE learning objective learn both global and local behaviors, while contrastive learning has a bias towards only learning global behaviors.

### Strengths
Extensive, well-formulated, and thorough proofs.

### Weaknesses
- Not sure where they conducted their experiments and where the results are. They alluded to some experiments here: “line 377: However, we observe that the selected area does not necessarily depend on the location of p”. Where are these experiments located?
- This work lacks serious experimental validation. They need some kind of information bottleneck need experiments which play with the information gap and the size of the ViT tokens/patches. How do you measure this imbalance between local and global features?
- The abstract mentions “analysis” and never mentions “convergence guarantees”. Initially, I thought this paper would have extensive experimentation documenting the global and local behavior of ViT pre-trained with different objectives. But the paper isn’t about that.

### Questions
- Information gap: What are the bounds/range on this? Can we see a visualization or even a histogram that shows how this value changes for different sizes of local image patches/tokens? Maybe apply it to different samples from various datasets and comment on the behaviour observed? The reason I am asking this is because a lot of theorems you mentioned make assumptions about the ranges of information gap and I think some approximations on the information gap’s behavior on some standard or simulated datasets might help. 

- Orthonormality assumption: line 193. Why do you make that assumption? To maximize span?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper claim to present a theoretical analysis of self-supervised learning for Vision Transformers (ViTs), focusing on the differences between contrastive learning (CL) and masked autoencoders (MAE). The study introduces a novel framework to model visual data distribution, considering both dominant global features and minuscule local features. By analyzing the training dynamics of one-layer softmax-based self-attention using gradient descent on spatial structured data, the authors demonstrate that MAE effectively learns both global and local features, while CL tends to focus predominantly on global features. The research provides a rigorous theoretical explanation for empirically observed behaviors of MAE and CL in ViTs. It highlights how the degree of feature imbalance affects the learning process, offering insights into why MAE can capture both global and subtle local information simultaneously, while CL tends to emphasize global patterns.

### Strengths
1. This paper proposes a comprehensive framework to theoretically analyse attention mechanism for CL and MIM. The framework simplify the analysis, avoiding disentangling patches and positional encoding.
2. This work attempt to answers the empirical observations for CL and MIM with ViTs: the MIM captures diverse local patterns, while the CL focuses on the dominant patterns.
3. Base on the proposed theory, this paper finds that there are two phases to learn the feature-position correlations when information gap is positive.

### Weaknesses
1. Vision transformers and transformers in general consists of two main blocks multi-head self-attention block as well as so called FFN consisting of two point-wise convolutions. The discussion is based on only one-layer of self-attention (with over simplification to only one weight matrix for self-attention) within vision transformer. Thus it cannot fully explain the complex behaviour of ViTs. 
2. There are a lot of assumptions, such as the input data distribution and positional encoding. It is not clear the differences in real problems.
3. What is the insight from this work to develop new methods? How to prevent the attention collapse in CL?
4. The discussion is based on SGD. However, Adam is the popular optimizer for ViTs. 
5. The original MIM (first MIM work with ViTs which outperformed supervised pretraining) work SiT [1] from which idea of MAE [4] is derived/copied from (only MIM part of SiT is taken in MAE) combines both MIM and CL, a strategy proven to be better and more principled time and again. Furthermore, state-of-the-art methods like iBoT [2] and its extension DINOv2 [3] also follow combined MIM and CL. It would be more fruitful to build theoretical framework for this combined MIM and CL setting (which seems to be the way forward in SSL) rather than building framework for MIM and CL separately.

### Questions
- The theory particularly for CL seems to be build on the notion of dominant concept which takes most of the area of the input. This assumption is not valid for almost all practical datasets for SSL. For instance, the average object to total image area ratio is 0.35 in ImageNet. Which means the so called background is almost always going to be dominant concept according this paper's definition. In that case the attention from any part of the image should focus on the background most of the time. If this is the case the kNN evaluation of DINO and MoCo should not be so high for imagenet and more importantly for other datasets. 
- Is the proposed theory would still be valid for datasets where the global area is small? 
- What will happen if the local areas are larger than the global area? This situation is going to be the dominant case in most practical datasets.  
Minors: 
- what is $k_s$? It seems the sum of weights for global area.
- What $\Delta$ means? Can you explain in details, such as when $\Delta=-1,0,1$?

### Soundness
3

### Presentation
2

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
This paper provides a theoretical framework for understanding self-supervised learning (SSL) in vision transformers, comparing masked autoencoders (MAE) and contrastive learning (CL). It examines how these methods handle imbalances between global and local visual features, revealing that MAE learns both global and local features, resulting in diverse attention patterns, whereas CL tends to focus on global features, often collapsing into uniform attention patterns. This distinction supports empirical observations, showcasing MAE’s effectiveness in capturing spatially varied data, while CL is better suited for global pattern recognition.

### Strengths
1. This paper introduces a novel theoretical framework for analyzing self-supervised learning (SSL) in vision transformers, filling a gap in the field that has been primarily empirical. 
2. The paper effectively illustrates the differences in feature capture between MAE and CL, showing how MAE learns both global and local features, while CL focuses more on global features. 
3. Through a detailed gradient descent analysis of a single-layer transformer, the study offers concrete findings on how MAE and CL converge to distinct attention patterns, ensuring result reliability and reproducibility. The study focuses on a single-layer transformer model, which may overlook the dynamics of self-supervised learning in deeper or more complex networks.

### Weaknesses
The study focuses on a single-layer transformer model, which may overlook the dynamics of self-supervised learning in deeper or more complex networks.

### Questions
Given that this study primarily focuses on single-layer transformer models, how might the dynamics of self-supervised learning differ in deeper or more complex transformer architectures? Specifically, Could the authors discuss potential approaches or challenges in extending their analysis to multi-layer transformers? Are there specific aspects of the current proof techniques that may or may not generalize to deeper architectures?

### Soundness
3

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
This paper discusses the reasons for the different attention mechanisms between discriminative (contrastive-learning) and generative (MAE) approaches for self-supervised learning with solid proof. This mainly contributes to the community of how these two learning strategies can be chosen and also further pushes the detailed understanding of the mechanism behind these two methods.

### Strengths
1. The quality of the paper is great; details for the problem setup, statement, and proof are given in the easy-to-understand setup.
2. The theoretical analysis provides a solid step to understanding the detailed differences between the mechanisms and can help future researchers develop more approaches based on this analysis.

### Weaknesses
1. The finding within the Sec. B should appear in the main paper instead of the Appendix. Some of the sections, such as Sec. 2.3 and 2.4 can be shortened since there are some overlapped concepts. Afterward, the Fig. 4 and the explanation can be moved up to provide more insight into local and global differences.

2. The assumption that the same cluster exists across different \(\mathcal{D}_k\) as defined in Sec. 2.2 and depicted in Fig. 2, while perhaps not invalidating the proof, warrants further scrutiny. For contrastive learning (CL), positive pairs are strictly derived from the same image, whereas MAE emphasizes local feature reconstruction. The current assumption, while simplifying the analysis, might not fully capture the nuances of how these methods operate on different data distributions. This could potentially limit the generalizability of the theoretical findings to more complex scenarios where cluster structures vary significantly across different data subsets.

3. The analysis does not provide a clear, quantitative relationship between the ratio of positive to negative samples and the global convergence properties. While the proof establishes the need for a sufficient number of negative samples to prevent collapse, it does not specify the precise ratio required for optimal convergence. This is a critical practical consideration, as methods like MoCo demonstrate the importance of a large number of negative samples to avoid model collapse. The lack of a concrete ratio makes it difficult to translate the theoretical findings into practical guidelines for hyperparameter tuning.

### Questions
1. In the first paragraph of Sec. 2.1 about **Masked reconstruction-based learning**, should it be $\mathcal{M}_i \subset \mathcal{P}$ instead of $\mathcal{M}_i \subset [P]$?
2. Does the same cluster exist in different $\mathcal{D}_k$ defined in Sec. 2.2 and depicted in Fig.2? If this is true, should this assumption be a little bit overwhelming? For CL, only entities obtained from the same images are considered positive. As for MAE, only local features are important. I am sure changing this assumption won't affect the proof, but I want to clarify this.
3. From the proof, can we determine the required ratio between positive and negative samples to ensure the global convergence properties? Since approaches such as MoCo require more negative samples to prevent collapsing.

### Soundness
4

### Presentation
3

### Contribution
4
