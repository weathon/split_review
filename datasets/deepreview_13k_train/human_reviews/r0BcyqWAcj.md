# Loci-Segmented: Improving Scene Segmentation Learning

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Current slot-oriented approaches for compositional scene segmentation from images and videos rely on provided background information or slot assignments.
We present a segmented location and identity tracking system, Loci-Segmented (\locis*), which does not require either of this information.
It learns to dynamically segment scenes into interpretable background and slot-based object encodings, separating rgb, mask, location, and depth information for each.
The results reveal largely superior video decomposition performance in the MOVi datasets and in another established dataset collection targeting scene segmentation.
The system's well-interpretable, compositional latent encodings may serve as a foundation model for downstream tasks

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends the location and identity tracking architecture Loci to scene segmentation by adding a pre-trained dynamic background
module, a hyper-convolution encoder module, and a cascaded decoder module. The proposed method and each components are validated to be effectiveness by extensive experiments.

### Strengths
The experiments are extensive.

### Weaknesses
1. The work is a little incremental, compared to Loci, so that its novelty is slim.
2. The principle and motivation of the proposed modules are not clearly explained.

### Questions
see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an architecture for unsupervised scene segmentation given RGB or RGBD video input. The method builds on the "Loci" paper, but re-designs many components and adds in a pre-trained foreground/background segmentation model. The main result is that this combination of changes greatly improves results, both qualitatively and quantitatively.

### Strengths
Quantitatively the method here clearly outperforms prior work (on the mIOU metric) in the the MOVI-* datasets.

### Weaknesses
Overall this paper is very difficult to follow. The "Loci" method, on which this is based, is never quite made clear on its own, and then every subsequent section makes big changes to the architecture without much motivation, and without a connecting story or high-level idea. 

The section on the "Background Module" never mentions this, but the abstract and the section on "Segmentation Preprocessing" describe the background module as "pre-trained", apparently for a segmentation task that "distinguishes foreground entities from the background context". My guess is that much of the performance gain is coming from this. It is unclear how this pre-training is done, what data is used, and what the architecture of this module is. This lack of detail makes it hard to assess the true contribution of the proposed method.

I have a variety of smaller questions which the authors may like to answer, but overall it seems to me that this paper needs a very heavy rewrite.

### Questions
What are Gestalt codes? 

What are the two predictions about object positions? The paper says "we introduce a dedicated background processing module that generates both predictions about object positions as pixel densities".

The paper mentions using something called "GateL0RD units" but these are never really described. 

The paper says that the "Gestalt codes are binarized to create an information bottleneck that fosters the development of factorized compositional entity encodings." I am unclear on why binarization will make the representation compositional. 

Section 2.1 focuses on improving Loci's "object tracking abilities", but the earlier section (describing Loci) never mentioned any object tracking happening, and tracking is never mentioned again. What is the idea here? 

The paper mentions that the decoder "reconstructs the predicted scene via slot-wise density maps as object masks." What are slot-wise density maps? 

The paper briefly mentions an "L0 loss on gate openings" but it is not clear what ground truth is used for this loss. Is it maybe just a regularization term, penalizing the L0 norm?

Section 2.2 introduces a depth input and an equation to normalize it, but it is not clear where this fits with the inner loop described in the previous section.

For Table 2 it would be great to clarify what dataset these experiments happen in, and what the metrics are.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This work focuses on the compositional scene representation and proposes a scene segmentation neural network based on the previous model named Loci. To build their model, they extend Loci with three modifications, including a pre-trained dynamic background
module, a hyper-convolution encoder module, and a cascaded decoder module. Extensive experiments conducted on the MOVi dataset show the effectiveness of the proposed method. Besides, the proposed method can generate well-interpretable latent representations and may serve as a foundation-model-like interpretable basis for solving downstream tasks.

### Strengths
1. Good performance. The proposed method achieves good performance on the MOVi dataset.
2. The proposed can generate well-interpretable latent representations, which is helpful in building interpretable foundation models.

### Weaknesses
To ACs and authors: I am not an expert in this field and cannot find any strong reasons to reject this work. Please refer to other reviewers' comments for rebuttal and decision.

### Questions
None.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Loci-s (Loci-Segmented) to tackle the problem of slot-oriented scene representation. Loci-s is an extension of the Loci architecture with structure change, additional inputs and etc. The proposed methods shows state-of-the-art performance on the challenging MOVi-E dataset, demonstrating its ability to deal with complex environments.

### Strengths
1)This paper extends the Loci model to Loci-s with several innovations.
2)The advancements in Loci-s collectively contribute to a 32.06% relative improvement in IoU on the challenging MOVi-E dataset compared to state-of-the-art models like SAVi++.

### Weaknesses
1)Since the proposed method is built upon Loci, I think there should be more comparisons between Loci and Loci-s in the experimental section.

2)The authors mentioned that instead of the residual structure used in Loci, the encoder and decoder subnetworks in Loci-s have been revamped to adopt a ConvNeXt-like architecture. I wonder how much performance improvement is brought by this structure change. Specifically, it would be beneficial to see an ablation study that isolates the impact of this architectural change from other modifications.

3)“The third methodology involves the deployment of a specialized segmentation network akin to YOLACT (Bolya et al., 2019). ” How is this segmentation network trained, and what is its performance? It is unclear what loss function is used, and what the performance of this segmentation network is in terms of standard metrics like mIoU or pixel accuracy.

4)The proposed method incorporates some additional input information for performance boost, e.g. the segmentation input (seg), depth map (sd). How much is the time cost? It would be helpful to understand the computational overhead of incorporating these additional inputs, both in terms of training and inference time. A breakdown of the time cost associated with each input would also be valuable.

5)(NOT IMPORTANT) Seems there is a missing reference (shown as ?) in sentence “Loci is rather closely related to other slot-based object processing architectures (Elsayedet al.; ?; Kipf et al., 2022; Wu et al., 2023)...”

### Questions
Same as weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
