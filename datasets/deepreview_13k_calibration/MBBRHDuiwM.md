# URLOST: Unsupervised Representation Learning without Stationarity or Topology

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 5, 8, 3, 8

## Abstract
Unsupervised representation learning has seen tremendous progress but is constrained by its reliance on data modality-specific stationarity and topology, a limitation not found in biological intelligence systems. For instance, human vision processes visual signals derived from irregular and non-stationary sampling lattices yet accurately perceives the geometry of the world. We introduce a novel framework that learns from high-dimensional data lacking stationarity and topology. Our model combines a learnable self-organizing layer, density adjusted spectral clustering, and masked autoencoders. We evaluate its effectiveness on simulated biological vision data, neural recordings from the primary visual cortex, and gene expression datasets. Compared to state-of-the-art unsupervised learning methods like SimCLR and MAE, our model excels at learning meaningful representations across diverse modalities without depending on stationarity or topology. It also outperforms other methods not dependent on these factors, setting a new benchmark in the field. This work represents a step toward unsupervised learning methods that can generalize across diverse high-dimensional data modalities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the topic of self-supervised representation learning and how to extend current popular frameworks to data modalities beyond natural images or text for which these methods have been initially designed. This is particularly relevant for the processing of scientific data which at this point would be hard to integrate into frameworks like MAEs. The authors propose to add a preprocessing block before the classic MAE which allows to aggregate data into the correct format even in the absence of prior information about the data's structure. This preprocessing blocks involves spectral clustering with density adjustment followed by a self-organizing map embedding layer. The authors show that the approach is more effective when process high-dimensional unstructured real-world data (2 natural science datasets + a modified version of CIFAR10) than applying the standard MAE framework to this data.

### Strengths
- relevance: this paper aims at extending existing SSL methods to novel modalities (notably modalities found in various scientific fields) for which current methods and their associated architecture of choice (e.g., MAE with ViT backbones) are not adapted because designed to suit standard data modalities (e.g., images) with known structure. This topic is relevant as SSL methods are often shown to be powerful but designed (both joint embedding methods and masked image modeling) to suit specific modalities which limit their applicability to a broader range of data. Even for standard modalities like natural images, approaches such as MAE rely on assumptions that might not generalize across datasets. 
- presentation: paper is well written and easy to follow, the overall state of the paper is good.
- experimental evidence: the experimental evidence to support the proposed method is quite convincing (see weaknesses below for information and experiments missing) as the authors conduct experiments on 3 real-world datasets on which results show superiority to the standard MAE baseline which is the most relevant related work with confidence intervals.

### Weaknesses
 - sensitivity of the method to choice of hyperparameters: the proposed method relies on spectral clustering for which a number of hyper parameters should be defined (like the number of clusters and hyperparameters linked to cluster density). These hyperparameters seem crucial in order to achieve high performance and are data-driven. Specifically, the number of clusters directly impacts the granularity of the learned representations, and the density adjustment parameters influence the size and uniformity of the clusters, which could lead to instability if not chosen carefully. The paper lacks a thorough analysis of how these parameters interact and affect the final performance across different datasets. 
- motivation: while it is clear that an aggregation/clustering of the input dimensions is necessary, the intuition behind aggregating dimensions that cluster together is missing; While the proposed method seems to work well, the paper would benefit from some additional intuition as to why one might want to combine elements that are similar in the same patch and compare this approach to the information found in standard image patches. There is little understanding of how MAE work, and most of their design choices are empirically driven, therefore it remains unclear whether MAE work better when pixels within a patch are identical. The paper should provide a more detailed discussion on the underlying assumptions and how they relate to the specific data modalities being considered.
- missing experimental baseline numbers and details: multiple information regarding the experimental setup is missing thereby reducing the ability to judge the soundness of the experimental setup (see question below) and a couple of experiments seem to be missing in order to confidently conclude that the proposed method is an effective alternative to the standard MAE baseline (see questions below). For example, the performance of the standard MAE on the permuted and foveated CIFAR10 datasets is not reported, making it difficult to assess the true benefit of the proposed method. Additionally, the paper should include a comparison with a non-masked scenario to fully evaluate the impact of the masking strategy.
- missing information about the work's limitations which might include the computational cost and scalability of the proposed method. The paper does not discuss the computational overhead introduced by the spectral clustering and self-organizing map steps, which could be significant for large datasets. Furthermore, the scalability of the method to even higher dimensional data should be addressed, as the computational cost of spectral clustering can increase rapidly with the number of dimensions.

### Questions
- can authors elaborate on why a set of linear projectors (non-shared in this case, a different layer for each cluster) cannot replace the use of self-organising maps? seems like the point here is that operation should not be shared between clusters rather than the type of operation used.
- how were representations trained in table 3? standard MAE? 
- can authors provide numbers for 1) URLOST with CIFAR10 2) MAE (Patch) with Permuted CIFAR and Foveat CIFAR; 
- can authors explain by such a high number of epochs is needed (10,000), is this only necessary for URLOST, prior work recommend 800-1600 epochs for standard MAEs. 
- what is the dimensionality of the representation in the beta-VAE vs the MAE; how do the size of models compare? the VAE used seems very shallow. 
- what is the range of beta parameter that was considered? 
- is the MAE in table 2 also with patch size 4? 
- what is the masking ratio in the MAE and URLOST (75%), can authors provide a comparison with 0% masking to show a non-masking scenario with equivalent architecture ?
- how is k selected ? how variable are results _across datasets_ for varying k, alpha, and beta parameters ? 

Minor: 
- typo in line 55
- bold number in table 1 for CIFAR10 is wrong, should be SimCLR

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
3

### Summary
This work introduces URLOST, a new framework for unsupervised representation learning aiming to overcomes limitations in handling high-dimensional data with unknown stationarity and topology, towards going beyond traditional methods that rely on structured data assumptions, such as grid-like images or time sequences. The proposed method combines a learnable self-organizing layer, density-adjusted spectral clustering, and a masked autoencoder (MAE) to capture learning representations from various data modalities.

Demonstrated on synthetic biological vision data, neural recordings, and gene expressions, URLOST shows a good performance, outperforming existing baselines in capturing complex, irregular structures without prior domain knowledge. The paper highlights areas for future work, such as integrating clustering into the model's end-to-end learning process and enhancing the self-organizing layer.

### Strengths
The strengths of the paper lie in its introduction of URLOST, a new combined framework for unsupervised representation learning towadrs addressing the challenges of high-dimensional data with unknown stationarity and topology. By combining a learnable self-organizing layer, density-adjusted spectral clustering, and a masked autoencoder, URLOST can captures learning representations from various data modalities. Its demonstrated performance on synthetic biological vision data, neural recordings, and gene expressions shows that it outperforms baselines, enlightening its capability to handle complex and irregular structures in an unsupervised mode.

The work is nicely conceived and the presentation is tidy. Its bio-inspired sense makes the work basically intriguing.

### Weaknesses
Several aspects of the work can be improved:
1) While the paper primarily motivates unsupervised learning, the experiments predominantly focus on supervised tasks (classification). This disconnect diminishes the relevance of the initial claims made in the first half of the paper. Specifically, the paper trains the URLOST model in an unsupervised manner but then evaluates the learned representations using a linear classifier trained with labels. This approach, while common, does not fully validate the unsupervised learning claims, as the evaluation is inherently tied to a supervised task.
2) The use of foveated preprocessing is an intriguing aspect; however, there is a noticeable drop in performance (in Table 1), likely attributed to this process. This raises the question of whether foveated preprocessing detracts from overall performance. The paper does not provide a clear explanation of why foveation, which is generally considered beneficial in biological vision, leads to a decrease in performance in this context. This discrepancy needs to be addressed with a more thorough analysis.
3)  Although the MAE appears to perform worse on the foveated dataset, this could simply be due to its training on the original dataset. Thus, the comparison does not effectively support the goal of emulating the biological process of foveation for benefits. The paper lacks a controlled experiment where the MAE is also trained on the foveated dataset to provide a fair comparison and validate the claim that URLOST is better suited for this type of data.
4) While the Vision Transformer (ViT) serves as the backbone, the paper lacks clarity on how attention is utilized in the experiments. It would be beneficial for the community to understand the potential relationship between the foveated process and visual attention. The paper should delve into the specific attention patterns that emerge during the foveated processing and how these patterns might differ from standard image processing.
5) The comparison against the MAE seems somewhat rudimentary. For example, the reported performance on CIFAR-10 indicates that several top models significantly outperform the authors' results (Table 1):
	Rank	Model		Percentage correct
	1		ViT-H/14		99.5
	2		DINOv2 		99.5
	3		µ2Net		99.49
	4		ViT-L/16		99.42
It seems the claimed better performance over the baseline was quite embarrassed by the top runners above. The paper needs to clarify that the goal is not to achieve state-of-the-art performance on CIFAR-10 but to demonstrate the effectiveness of the proposed method on data with less structure. However, the comparison to MAE is still not convincing given the large performance gap.
6) The meaning and algorithm behind the permutation of CIFAR-10 images are unclear. Providing examples of permuted images would clarify this aspect. The rationale for permuting pixels should also be addressed, as such transformations may hinder human recognition and contradict the stated bio-inspired motivation. The paper needs to explain why this specific permutation is used and whether other permutation strategies would yield similar results. The connection to biological plausibility needs to be better justified.
7) In Section 2, the proposed method appears to aggregate several state-of-the-art techniques with limited novel mathematical contributions. Incorporating theoretical exploration of its bio-inspired aspects would significantly enhance the paper's quality. The paper should provide a more detailed analysis of the theoretical underpinnings of the proposed method, particularly concerning the combination of self-organizing maps, spectral clustering, and masked autoencoders.

### Questions
No extra questions. See the above comments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The submission proposes a route to implementing masked autoencoders (MAE) when the data does not have a known structure and yet is too granular for each component of the input to be its own “patch”.  In other words, there’s prior knowledge about the dataset that its components could probably be meaningfully grouped, but no grouping is available.
The method clusters the components by mutual information and spectral clustering, with an additional density correction applied.  After components have been grouped, all groups must be mapped to a shared representation space so that the transformer can compare them; for this the authors use a learned projection for each group that they call a self-organizing layer.
There are a fairly comprehensive suite of comparisons: to MAE without grouping the components and to SimCLR with a CNN and ViG architecture, on a couple CIFAR10 variants, gene expression data, and on V1 neural recording data.

### Strengths
The premise to handle more diverse datasets than images with a ViT setup (and MAE pretraining, though it seems more general than a specific pretraining method) by clustering input components is strong.  The experiments cover a good range of complexity, starting with standard CIFAR10, permuting the pixels, and then remapping the visual field entirely.  Then the V1 and gene expression experiments represent actual use cases.  The comparisons are sufficient to demonstrate the utility of the method.

### Weaknesses
The clustering is the heart of the proposed method and comes with multiple design choices or parameters whose selection is not obvious. While the experimental results demonstrate the method works, results supporting these design decisions are a bit weak. As far as I can tell, the only results regarding the effect of the density adjusted spectral clustering are with respect to the foveated CIFAR10 data (Table 3b, Table 4)? Why should we assume gene expression is best processed with the same parameters, considering how structured the synthesized foveated CIFAR10 is? By contrast, the self-organizing layer is pretty intuitive, yet a large chunk of the manuscript and appendices are dedicated to it.

Related work could be strengthened. Consider discussing the relation to FlexiViT (Beyer et al., CVPR 2023), where different patch sizes are mapped to the same representation space by learnable transformations, and PatchGT (Gao et al., LoG 2022), where nodes of a graph are clustered with spectral clustering, and the representation of each “patch” is a learned function of the subgraph.


### Questions
- Why is SimCLR with the proposed clustering pipeline (and ViT architecture) not included as a baseline for the CIFAR10-based experiments?  Why not ViG with patches found by URLOST?  Unless I have misunderstood, the proposed method is ultimately about “patchifying” data for use with a downstream transformer, which means there’s nothing tying the paper to MAE.  Such a shift away from exclusively linking the method with MAE would broaden its potential impact.
- There is no need for explicit positional encoding information per cluster, correct?  Presumably the self-organizing layers can encode identifying information per cluster.
- Line 265: “Moreover, since CNN can only process signal with stationarity and topology” is an incomplete sentence and also incorrect, as CNNs can absolutely process signals without stationarity.  Overall, I felt the stationarity part of the motivation to be much less important than the topology. 
- Why is MAE bolded in Table 1 when it was outperformed by SimCLR?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method to learn useful representations of data without assuming the relationships between dimensions of topological structure, translation invariance, as in images/sounds.

### Strengths
The paper is well motivated and the task tackled is important and relevant to the community.

### Weaknesses
A lot of work has gone in to the paper, but unfortunately it is quite difficult to follow; and the proposed method seems very expensive (computing entropy, eigenvalues, clustering, etc). On the first point, to reach a broad audience, specific effort should be made regarding aspects less familiar to the general ML community. I find the method and data transformations difficult to parse.

* Clarity
   * [036-041] Unclear references to topology and stationarity -  core aspects of the paper
      * Is the topology property that dimensions are ordered such that correlation (or similar) is expected between the signal at "nearby" dimensions? 
      * Stationarity seems very entwined with topology, does stationarity require topology? If not how? 
      * What assumptions *is* the model making?
   * [225] unclear how permuting pixels leaves stationarity intact
   * [259] unclear how reducing density prevents redundant sampling.
* [095] A fully connected NN doesn't assume topology/spatial invariance and seems a key benchmark, but is not considered/mentoined.
* [183] How does a vector denote a cluster? the cluster mean, indexes of cluster members?
* [337] Given $\beta$-VAE results in Table 2 are close on the real datasets, have optimal parameters/architecture been used? Why is this not compared to in Table 1? 
* The proposed method seems expensive but no mention of this is made.

Minor
* [031] unsupervised representation learning (UL) and self-supervised representation learning (SS) are not the same. SSL is a subset of UL, e.g. a $\beta$-VAE performs UL but not SSL, whereas SimCLR performs SSL (and so UL).
* Several typos
   * [037] "arised", [055] "singal" etc

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper suggests a novel way unsupervised representation learning pipeline, which consists of three stages: clustering, self-organising layers and masked autoencoder training. The authors try to tackle the assumptions of stationarity and topological ordering of the data for self-supervised learning.

### Strengths
* great motivation: important problem of topological ordering and stationarity assumptions is raised. Biological inspiration is also interesting.
* novel ideas, especially, when it comes to clustering and self-organized layers instead of patching. This potentially allows to aggregate features on different scales, which could be highly beneficial in many cases (for example, action tracking could be composed of motions tracking)
* making the code available is great for reproducibility

### Weaknesses
 * While the authors criticise graph neural networks for not being scalable and the paper is proposed as a new self-supervised approach, the scalability aspect is not addressed, both from the perspective of time (and spectral clustering can become slow) or performance . The datasets used in the paper are fairly small, while even for transcriptomics or neuroscience there are quite big datasets publicly available now.
* Topology is mentioned a lot, however, I do not fully understand, where exactly authors show that their method is not relying on topology. I would suggest authors to take a point cloud dataset (for example, 3D Point Cloud Classification on ModelNet40 ) and perform a comparison on it. The transcriptomics vectors are still ordered (like each position corresponds to a specific gene), which could be also thought as topological organisation (like a flattened picture).
* The experiments are missing the error bars or confidence intervals, which makes it a bit hard to understand how robust is the method and how significant are the improvements.
*  while the paper motivation is highly biologically grounded, the actual image dataset has very low signal-to-noise ratio, eg  a lot of natural scenes do not so nicely isolate a single object in the center of the image such as CIFAR. I would inspire the authors to use a more noisy multi-object classification or segmentation dataset
* while avoiding stationarity assumption is one of the main paper motivations, I felt like a textbook case of non-stationary data, eg time series, is missing. I would suggest to include some non-stationary timeseries classification example, for example, for epilepsy, to prove illustrate this point in a much more convincing manner.
* I find the biological motivation sometimes more confusing than helping, for instance, lines 471-476, mention self-organising maps, without giving a brief introduction on what they are.

### Questions
* if I permute all images in the same way, why would it ruin the topology? As far as I understand it, I will just transform it but the ordering is still preserved

### Soundness
2

### Presentation
2

### Contribution
2
