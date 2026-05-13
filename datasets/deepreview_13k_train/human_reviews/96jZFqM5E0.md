# Pre-Training for 3D Hand Pose Estimation with Contrastive Learning on Large-Scale Hand Images in the Wild

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
We present a contrastive learning framework based on in-the-wild hand images tailored for pre-training 3D hand pose estimators, dubbed HandCLR. Pre-training on large-scale images achieves promising results in various tasks, but prior 3D hand pose pre-training methods have not fully utilized the potential of diverse hand images accessible from in-the-wild videos. To facilitate scalable pre-training, we first prepare an extensive pool of hand images from in-the-wild videos and design our method with contrastive learning. Specifically, we collected over 2.0M hand images from recent human-centric videos, such as \textit{100DOH} and \textit{Ego4D}. To extract discriminative information from these images, we focus on the \textit{similarity} of hands; pairs of similar hand poses originating from different samples, and propose a novel contrastive learning method that embeds similar hand pairs closer in the latent space. Our experiments demonstrate that our method outperforms conventional contrastive learning approaches that produce positive pairs sorely from a single image with data augmentation. We achieve significant improvements over the state-of-the-art method in various datasets, with gains of 15\% on FreiHand, 10\% on DexYCB, and 4\% on AssemblyHands.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a contrastive learning method for the pre-training of 3D hand pose estimation based on large-scale in-the-wild hand images. A parameter-free adaptive weighting mechanism is introduced in the contrastive learning loss, which not only learns from similar samples but also adaptively weights the contrastive learning loss based on inter-sample distance. Experiments show improved performance compared with existing pre-training methods.

### Strengths
- The paper is well written and easy to follow.
- The motivation of finding similar hands derived from different video domains is technically sound, which can further benefit contrastive learning process from discriminating foreground hands in varying backgrounds.
- The experimental results in Table 3 demonstrate the generality of the proposed contrastive learning with adaptive weighting mechanism.

### Weaknesses
 - TempCLR [1] proposes a pre-train framework for 3D hand reconstruction with time-coherent contrastive learning, and shows better performance compared with PeCLR. Although TempCLR focuses on reconstruction tasks, the used parametric model can output 3D pose results. Therefore, more comparisons with TempCLR would be helpful.

- In the second column of Figure 6, HandCLR demonstrates advanced performance in hand-object occlusion. Does the proposed method exhibit robustness in similar severe occlusion scenarios involving hand-object interactions? More qualitative analysis in datasets like DexYCB or in-the-wild scenarios would be helpful.

- The proposed adaptive weighting mechanism is a straightforward approach that has proven effective; however, it lacks a clear articulation of its motivation, particularly regarding the challenges faced in 3D hand pose estimation tasks as mentioned in the introduction.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- The paper explores pretraining for hand pose estimation using a large number of 2D image samples.
- It introduces HandCLR, a contrastive learning-based method. This method expands the definition of positive and negative samples by using pairs with similar actions from different sources, improving upon previous methods that relied solely on data augmentation.
- The authors collected extensive pretraining datasets from 100DOH and Ego4D and studied effective methods for mining similar hand samples.
- They designed a Top-K sampling strategy for positive and negative samples and implemented adaptive weighting.
- Experiments show that the proposed method outperforms baselines in both pretraining and downstream finetuning tasks.

### Strengths
- The paper is well-written and easy to follow.
- The motivation behind the proposed method is sound, with comprehensive details from data preparation to training.
- The design of contrastive loss with weighting provides better gradient guidance for samples with different sources and similarities, which is both reasonable and effective.
- The numerous experiments reflect significant effort by the authors.
- The experimental section is logical and thorough, demonstrating performance improvements across different datasets and analyzing the impact of training samples, finetuning sample size, and various design modules.

### Weaknesses
 - Some presentation issues need improvement
    - Figure 6 should be updated to remove inappropriate "bbox" spelling marks. Additionally, all images in the paper should be replaced with vector versions to prevent blurry text, as seen in Figure 3.
- The article lacks references and discussions on self-supervised methods. The recent two works, S2Hand and HaMuCo, although not pre-training methods, also attempt to use unlabeled images and 2D off-the-shelf detectors to train 3D hand pose estimation models.
- Otherwise, the paper is relatively complete with no major weaknesses 

### Questions
- Why are the baseline metrics relatively poor? For example, Freihand dataset shows 18+ MPJPE, while recent works (i.e. MobRecon) often achieve <6 PA-MPJPE. Could you explain if Procrustes analysis accounts for such a large performance difference? If the author could explicitly address this performance gap or more clearly explain the difference between the baseline metrics and those of existing fully supervised methods, it would be better.
- Are the positive sample augmentations identical to those used for query images?
- Is Figure 4 showing results from the FreiHand dataset?
- Regarding minibatch construction, the authors mention using 2N samples (N query images and their corresponding positive samples). Using the top-1 method for defining positive samples, could there be cases where a negative sample $I_n$ for query image $I_m$ is actually very similar but not top-1 (e.g., top-K where K>1)? Do the authors have more detailed descriptions of how to increase the discrimination in positive/negative sample sampling, or is it solely addressed through adaptive weighting?
- How is diversity ensured in the reverse lookup of top-1 samples for each query image? Could there be cases where samples from videos j and k are mutually top-1 similar samples, potentially reducing training diversity by constantly pairing samples from the same two videos?
- What specific models were used as baselines in Tab.1?

- Since the baselines compared by the author all have open-source code, in order to enhance the reproducibility of the article and the usability for downstream tasks, it is hoped that the author will adhere to what is mentioned in the article and actually release the code

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the task of self-supervised learning for 3D hand pose estimation from monocular RGB. The authors build on prior work in the area and improve upon it in three main areas: 1) Use of noisy 2D supervision to mine positive samples 2) Adaptive weighting that weighs positive and negative samples based off of their distance of the 2D keypoints 3) Processing and use of Ego4D and 100DOH for self-supervision.
Their proposed method first constructs a pose embedding based off of the noisy acquired 2D keypoints using an off-the-shelf predictor. This pose embedding is then used to mine positive samples given a query image.
These positive samples are used within the contrastive loss as positive samples, whereas the remaining image in the batch is marked as negative. The positive and negative samples are weighted additionally using weights that are computed based off of the scaled euclidean distance of their 2D keypoints.
The self-supervised model is trained on Ego4D and/or 100DOH. Those datasets have been processed using an off-the-shelf hand detector model. Supervised training was done on a variety of supervised datasets. Experimental results show large improvement across all benchmark datasets compared to prior self-supervised models.

### Strengths
- The paper empirically verifies the improvement over prior self-supervised models. Self-supervision is a rather underexplored area in hand pose estimation and can lead to potentially great benefit as foundation models.
- The improvements are substantial
- The paper is easy to understand

### Weaknesses
 - The method shows great improvement over prior self-supervised methods through the use of noisy 2D annotations. However, its use is a rather involved process: it first needs to be embedded, then used during pre-training before then performing supervised fine-tuning. Instead, why not just use the noisy 2D annotations directly as a form of weak-supervision? In fact, this has been done in prior work [1] and has lead to substantial improvements. In order to properly verify the usefulness of the authors proposed method, there first needs to be a baseline showcasing that the straightforward addition of the noisy 2D annotation during pre-training or supervised training performs comparatively worse. Otherwise why should one employ the authors proposed method? Due to my own experiences in the field, I fear that the weak-supervision approach will outperform the authors proposed approach.
- The paper does not compare to other related work in the field for which test results on FreiHand, DexYCB and AssemblyHands are available. Without these, we cannot assess properly the value of this work and how it fits in overall.

### Questions
- How does this work compare to a weakly-supervised approach with noisy annotations?
- How does this work perform compared to other related work on the tested datasets?
- Instead of using weights, could one instead not use a more appropriate loss that will automatically lead to larger effects depending on the samples weights? For example, MSE will automatically weight the contributions of more distant samples stronger.
- L143-144: Why balance the number of left and right hand if they all end up being converted to right-handed images?
- Eq 1: Why not use the cosine similarity which is more popular for distances in feature space?
- Fig3: The colored boxes at the end of the model pipeline seems to be in the wrong order. E.g the figure shows positive samples minimizing alignment.
-L238-239: rough -> noisy
- Table 1: What is "baseline"? This needs to be explained in the image caption
- Table 1: Why are the worst result of SimCLR in bold? Shouldn't the most performant number be in bold?
- Not all figures and tables are referred to in text.
- Table 3: inconsistent capitalization of simclr etc. This also occurs occasionally in the text.

### Soundness
3

### Presentation
2

### Contribution
2
