# Waxing-and-Waning: a Generic Similarity-based Framework for Efficient Self-Supervised Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Deep Neural Networks (DNNs), essential for diverse applications such as visual recognition and eldercare, often require a large amount of labeled data for training, making widespread deployment of DNNs a challenging task. Self-supervised learning (SSL) emerges as a promising approach, which leverages inherent patterns within data through diverse augmentations to train models without explicit labels. However, while SSL has shown notable advancements in accuracy, its high computation costs remain a daunting impediment, particularly for resource-constrained platforms. To address this problem, we introduce SimWnW, a similarity-based efficient self-supervised learning framework. By strategically removing less important regions in augmented images and feature maps, SimWnW not only reduces computation costs but also eliminates irrelevant features that might slow down the learning process, thereby accelerating model convergence. The experimental results show that SimWnW effectively reduces the amount of computation costs in self-supervised model training without compromising accuracy. Specifically, SimWnW yields up to 54\% and 51\% computation savings in training from scratch and transfer learning tasks, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for improving the efficiency of SSL methods by discarding features in augmented images and feature maps that are deemed less important, saving computation and reducing the risk of slowing the learning process by providing irrelevant features. The authors propose to remove blocks from pairs of augmented images that share high semantic similarity, in order to prevent unnecessary processing of irrelevant information such as image backgrounds. To this end, they provide a method for semantic matching of block pairs in images, their removal, and the treatment of the resulting feature maps throughout the network. Authors show results for training from scratch and transfer learning compared to a number of other SSL methods, in most cases showing barely degraded performance - or even improved performance - at a significantly reduced computational cost.

### Strengths
The authors provide a sensible method for improving computational efficiency of SSL methods, one of their main challenges currently. The authors are very thorough in motivating and describing their method, using illustrative examples throughout the paper. Experimental results are impressive, the proposed method shows good performance in its ability to reduce computational cost while retaining model performance.  A very sound paper overall, with good experimental design. Given that the authors spend some time sculpting the manuscript to improve its readability for the rebuttal, I think it represents an interesting and valuable addition to the CVPR proceedings.

### Weaknesses
Overall readability of the paper could be improved, I’m having a bit of a hard time understanding some of the specifics of the approach as outlined in 3.1 and 3.2. Specifically, the block matching as outlined in paragraphs 1 and 2 under 3.1 seem to overlap; from my understanding you first search for most similar block pairs (paragraph 1) after which you calculate similarity for all block pairs (paragraph 2)? Why not calculate similarity for all block pairs directly?

Under 4.1, you indicate that, for a given pair of original and augmented image, you divide the first into blocks and loop for a similar block in the paired image. However, instead of performing an exhaustive search over all possible blocks in the augmented image, you narrow the search to “a specific region surrounding a block’s counterpart in the paired augmented image” to ensure semantic consistency. Where does this block’s counterpart come from? Is it simply the same augmentation applied to the block in the original image, i.e. the location of the original block under a flip? In this case, why would the same block in the augmented image not be the most similar block? Semantically, their content is identical is it not? Could you give an intuition as to why you would want to pair image blocks in the same region in the online and target images but not simply pair exact matches under augmentation?

### Questions
Could you give a little more explanation for figure 1. In my opinion, the first two paragraphs of 3.1 read a bit confusingly. What is the distinction between the block matching described in the first paragraph and the similarity calculation after the creation of block pairs in the second paragraph? Aren’t they overlapping?

How does computational complexity of the block-matching factor into the overall training complexity? I.e. do the FLOPs listed in tables 1 and 2 contain the overhead for your method? I think this should definitely be taken into account.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim to improve the training efficiency of self-supervised learning (SSL) and they propose a similarity-based SSL framework called SIMWNW. SIMWNW removes less important regions (remove most similar regions in two views) in augmented images and feature maps and saves the training cost. Experimental results show that SIMWNW reduces the amount of computation costs in SSL.

### Strengths
1. This paper is well-written and easy to follow.
2. The authors analyze the importance of different regions on augmented images by removing and reusing similar blocks for the two branches.
3. The authors show that the removed region will shrink after convolution operation and they propose to expand the size of removed region in the feature map.
4. Experimental results show that the proposed method can achieve comparable accuracy using fewer training FLOPs.

### Weaknesses
1. Compared with the training FLOPs, the actual time used for training is more important, and the authors did not report it. How much the proposed method can reduce the training time is what we are concerned about. Steps such as matching in the method cannot actually be reflected intuitively through FLOPs.
2. In Table1 and Table2, the authors should list the accuracy of the baseline methods using the same training overhead. For example, how much lower will simclr be than the proposed method when using 80% overhead?
3. Do the training FLOPs in Table2 refer to pre-training or downstream fine-tuning? If it is the former, why is it different from Table1？If it is the latter, how is the proposed method used in single-branch supervised learning?
4. From Figure 6, I cannot see the obvious advantages of the proposed method. I suggest the author change the horizontal axis to training hours.
5. Some related works [1], [2].

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to enhance the efficiency of self-supervised learning (SSL). Based on contrastive SSL methods, such as SimCLR and SimSiam, this paper proposes to reuse and remove the similar regions so as to save computation. To achieve this, this paper first identifies the similarities between regions. However, directly operating on regions would face the region shrinking problem caused by convolution layers, this paper proposes to expand the size of removed region. Compute savings in FLOPs in observed in ImageNet benchmarks.

### Strengths
+ Self-supervised learning is computation expensive, this paper proposes to reduce the pretraining cost while preserving the accuracy, which is important topic for the community. 

+ The idea of reusing and replacing similar regions is intuitive. Also I am not sure if there are other similar works proposing similar ideas, it is good to see these simple yet effective training techniques.

### Weaknesses
 - This paper claims that the proposed method is efficient regrading the FLOPs. However, reduced FLOPs may not directly lead to time saving given that the proposed method requires dedicated sparse computation of convolutional kernel. It is important to report the real run time saving to claim efficiency.

- In the title, authors claim the proposed method is generic. It is worth to apply SimWnW to self-supervised vision transformers as well. Moreover, the reuse and replace strategies are expected to be applicable to ViTs since there would be no region shrinking problem in ViTs.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an efficient SSL approach called SimWnW. Through studying the impact of similar and dissimilar image regions on SSL performance, the authors find that similar regions are less important and removing them in augmented images (and in feature maps) can significantly reduce the computation cost and improve model convergence. To remove similar regions, the authors propose a new method under the ResNet/ConvNet settings. Specifically, a waxing-and-waning process is proposed for region removal while mitigating the region shrinking problem in convolutional layers. Experiments show that SimWnW can reduce the computation cost of SSL without compromising accuracy -- SimWnW yields up to 54% and 51% computation savings in training from scratch and transfer learning tasks, respectively.

### Strengths
- The paper offers a comprehensive exploration of the impact of similar/dissimilar regions on SSL accuracy, which lays a good foundation for a region removal-based method to improve SSL efficiency.
- Strong results in efficiency boost are achieved for two representative SSL frameworks.
- Decent analysis is provided for region removal-related hyper-parameters like similarity threshold and block size.

### Weaknesses
 - The key hyper-parameter of block removing portion is unspecified, and convincing explanations are missing (see questions below).
- The comparisons with recent related works seem insufficient, e.g. (Addepalli et al., 2022) and (Koc¸yigit et al., 2023).
- The proposed waxing-and-waning method is customed too much to ConvNets. It seems hard to translate to transformers and hence transformer-based SOTA SSL methods (this makes the paper title a bit overclaim).

### Questions
Key question around the portion of block removal:
- Intuitively, comparing similar blocks won't generate too much useful signal for SSL. This is validated by Fig. 2 where the performance of "Similar Blocks (x\%)" is consistently worse than "Dissimilar Blocks (x\%)". On the other hand, comparing dissimilar blocks (after removing similar ones), despite being more useful, has a key hyper-parameter of the removing portion (1-x)\% which can significantly affect the learning quality. Specifically, if we remove too much, comparing those top dissimilar blocks either makes learning too hard or the dissimilar blocks may not even be semantically related (which hurts SSL quality). If we gradually increase x\%, the retained blocks would include both dissimilar and relatively similar blocks, which makes the learning signals more balanced for SSL.
- Fig. 2 shows that SSL performance peaks at "Dissimilar Blocks (75\%)". What's the actually used x\% after region removal in SimWnW? If it's 75\% or higher, then it shouldn't lead to that much of computation saving. Fig. 7(a) shows some hint about x in terms of similarity threshold. 1) When the default threshold is set to 20, what's the corresponding x\%? 2) With the default similarity threshold 20, the SSL performance remains about the same but the training cost is increasing. So again, the computation saving is still concerning. Any comments?
- One side question, why the compute saving on ImageNet is much smaller than CIFAR 10/100? This suggests the amount of removed blocks from high-resolution ImageNet images is smaller than that of low-resolution CIFAR images, given the same similarity threshold (if that's how it works). Any intuitions about why this is the case?

Other minor questions:
- To find similar blocks, what's the neighborhood size for searching? Does it depend on augmentation parameters? - since how we crop/rotate/flip images will impact the block locations a lot.
- For "block matching" in pixel space, is PSNR an accurate enough metric? What if the found correspondence is wrong and how well can SimWnW tolerate such errors?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
