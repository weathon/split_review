# Multi-label Cluster Discrimination for Visual Representation Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
\label{sec:abstract}
Contrastive Language Image Pre-training (CLIP) has recently demonstrated success across various tasks due to superior feature representation empowered by image-text contrastive learning. However, the instance discrimination method used by CLIP can hardly encode the semantic structure of training data. To handle this limitation, cluster discrimination has been proposed through iterative cluster assignment and classification. Nevertheless, most cluster discrimination approaches only define a single pseudo-label for each image, neglecting multi-label signals in the image.
In this paper, we propose a novel Multi-Label Cluster Discrimination method named MLCD to enhance representation learning. In the clustering step, we first cluster the large-scale LAION-400M dataset into one million centers based on off-the-shelf embedding features. Considering that natural images frequently contain multiple visual objects or attributes, we select the multiple closest centers as auxiliary class labels. In the discrimination step, we design a novel multi-label classification loss, which elegantly separates losses from positive classes and negative classes, and alleviates ambiguity on decision boundary. We validate the proposed multi-label cluster discrimination method with experiments on different scales of models and pre-training datasets. Experimental results show that our method achieves state-of-the-art performance on multiple downstream tasks including linear probe, zero-shot classification, and image-text retrieval.co/collections/DeepGlint-AI/mlcd-670d18d767cea37ea7436e69}{Hugging Face}.


\keywords{Visual Representation Learning, Instance Discrimination, Cluster Discrimination, Multi-label Learning}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a simple but effective method to facilitate the representation learning of the vision-language model. The method consists of two steps. In the clustering step, the authors cluster the dataset into enormous centers and utilize several closest centers as the class labels for every single image, enhancing the learning of semantic structure of training data. The discrimination step incorporates a multi-label classification loss to separate losses and promote distributed training. The experimental results are solid.

### Strengths
Originality: This work extends the discrimination power of CLIP model by introducing a multi-label loss to boost the semantic learning ability of the vision-language model.
Quality: The improvement achieved by the proposed method is remarkable on certain datasets, and the ablative study provides comprehensive and detailed insights into its functioning.
Clarity: This paper is reader-friendly and smooth. The experimental setting is quite reasonable.
Significance: This paper shows the benefit of using multi-label loss for clustering-based discriminative constrastive learning. This setting should be considered when developing powerful pre-trained vision-language model for downstream tasks.

### Weaknesses
(1) The novelty and originality of this work are limited. It seems like the method proposed in this paper incorporates several techniques introduced in the literature. It does not offer sufficient technical inspirations for the readers to follow. 
(2) With respect to the limited technical novelty of this work and overall moderate improvement (I see in Table 1 and Table 2), it may not seem to be worthwhile using such huge computing resources (80 NVIDIA A100 GPUs), especially considering that visual-language pre-training field has already achieved remarkable performance.
(3) According to my understanding, as proposed method is developed upon the feature embedding from the pre-trained CLIP model and it does not involve any textual information in the proposed multiple label loss. If this is correct, this paper should make this more clear.
(4) In Equation 5, two new items are further introduced into the multi-label loss. This is regarded as one of the key contributions by this paper. However, its efficacy does not seem to be clearly verified in the ablation study. This needs to be addressed.

### Questions
(1) As one of the main contributions of this paper, the authors claim that the modification of optimization loss can elegantly separate the positive class labels and negative class labels, resulting in promotion of the distributed training on large-scale training data. Please explain and experimentally demonstrate how this modification can facilitate the distributed learning more clearly. For example, in Subsection Distributed Multi-label Classification of Section 3.2 MULTI-LABEL CLUSTER DISCRIMINATION, The first sentence “Eq. 6 is able to distribute the weights associated with one million class centers across all GPUs with minimal communication overhead.” Why? 
(2) Some technical details are missing, e.g., in Section 4.1, the authors should explicitly point out the number of classes (k) and number of positive centers (l) they use when pre-training the model on LAION-400M dataset.
(3) In Table 3, the best results consist of both the proposed method in this paper and the FLIP (i.e., 89.1%). Notably, only the results of the proposed methodology have been highlighted.
(4) In Section 4.6, the meaning of the y-axis of the charts should be provided to improve the clarity of the paper.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new clustering-based unsupervised algorithm for vision foundation models pre-training. The key idea is to assign images into multiple clusters as pseudo labels for unsupervised representation learning. The motivation is that existing clustering-based pre-training methods assign each image into a single cluster, which enforces the models to focus on the most salient part of images and overlook the other regions that may also be meaningful. Besides, the authors also optimise the conventional margin loss formulation by decoupling the optimisations of positive and negative pairwise similarity. The proposed algorithm has been shown effective in severe classification-oriented downstream tasks including linear probe, zero-shot classification and retrieval.

### Strengths
The algorithm proposed in this paper is intuitive and effective in learning discriminative imagery feature representations. The analysis and decomposition of triplet loss make sense to me and are potentially beneficial to a wide range of applications as a generic improvement to a widely adopted metric learning design.

### Weaknesses
+ my key concern on the high-level idea is whether the top-k closest clusters to an image can really reveal what objects/attributes (will use “concepts” for clarity hereafter) are involved in it. At the cluster level, samples of the same clusters are likely to share more nearest clusters (in a global picture) but the concepts involved in each independent image are almost random. Is it possible that the multiple labels assigned to the same images provide models with additional knowledge about the co-occurrence/relevance of different concepts (cluster-to-cluster relationships) rather than actually telling models what is involved in images (sample-to-cluster relationships)? It will be interesting to see more exploration and analysis of why the multi-label clustering idea is beneficial. One simple verification can be pre-training on a dataset with known non-overlapping class structure, eg ImageNet, and see if the multi-label clustering still benefits.

+ The modifications made to triplet loss make sense to me but their effects are unclear. How will the proposed model perform if all its designs are kept unchanged except for replacing L’_MLCD (Eq.6) with L_MLC


+ What are the blue and green cells standing for in the grids pointing to the text “contrastive loss”?

+ Whilst Fig.2 is the first figure being referred to, Fig.1 is simply mentioned as the illustration of visual representation learning but it lacks further explanation/discussion.

+ In Eq.1, I assume the pairwise similarity is cosine similarity if following CLIP, but without normalisation of features, it is just an inner product. So I’m wondering if it is a mistake or my misunderstanding.

+ In Eq.1, the index in the cumulative sum starts from 0 to k while that in Eq.2 is from 1 to k, is this deliberate and why?

+ The exponential function is denoted as exp and e at the same time in Eq.3, which makes the equation really confusing when the feature representations are also denoted as e_i.

+ The ablation studies are a bit unclear to me. For example, when investigating the effects of sample ratio, the best linear probe performance is obtained when the sample ratio is set to 0.1, and the best result is 75.2. However, the linear probe performance of the proposed model shown in Table 5 is 84.6.

### Questions
Although the proposed method yielded impressive performance, it is also crucial for me to figure out the underlying reasons for the effectiveness. So further evidence and discussions about this will be helpful.

### Soundness
3 good

### Presentation
2 fair

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
This work focuses on addressing the limitations of instance discrimination commonly used in image-text contrastive learning, such as CLIP. The authors propose a multi-label cluster discrimination method aimed at improving the encoding ability. They employ offline clustering to assign multiple labels to each image and subsequently conduct multi-label classification to learn the semantic structure within a single image. The authors support their methods with extensive experiments and perform ablation studies to analyze the function of each component.

### Strengths
1. This work considers the multi-label properties of a single image and emphasizes the learning of better semantic structure in data.
2. The designed loss function elegantly separates the loss from positive and negative classes, which enhances the parallelism and scalability during training.
3. The experiments in this work are extensive and convincing, with thorough ablation studies.

### Weaknesses
 1. Clarity: 
   - This manuscript requires further refinement in terms of writing to facilitate reader comprehension, particularly by providing detailed explanations for the mathematical symbols used in the text, thus reducing reading barriers.
2. Experiments: 
   - In section $3.2, the authors claim efficient parallel computation and scalability of the model training process. However, is there quantitative data to support this point?
   - Does the incorporation of clustering significantly improve the training time? 
3. Reproducibility:
   - In section $3.2, you employ some distribution training techniques but details are not provided, which hinders the reproducibility of the work.

### Questions
1. The performance reported in the CLIP paper differs from your reproduced version. In Tab 1 and Tab 2, which may influence the validation of improvement of your model. Have you checked the implementation and settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
