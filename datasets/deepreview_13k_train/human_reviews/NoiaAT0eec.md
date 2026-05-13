# Learning Mask Invariant Mutual Information for Masked Image Modeling

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Masked autoencoders (MAEs) represent a prominent self-supervised learning paradigm in computer vision. Despite their empirical success, the underlying mechanisms of MAEs remain insufficiently understood. Recent studies have attempted to elucidate the functioning of MAEs through contrastive learning and feature representation analysis, yet these approaches often provide only implicit insights. In this paper, we propose a new perspective for understanding MAEs by leveraging the information bottleneck principle in information theory. Our theoretical analyses reveal that optimizing the latent features to balance relevant and irrelevant information is key to improving MAE performance. Building upon our proofs, we introduce MI-MAE, a novel method that optimizes MAEs through mutual information maximization and minimization. By enhancing latent features to retain maximal relevant information between them and the output, and minimizing irrelevant information between them and the input, our approach achieves better performance. Extensive experiments on standard benchmarks show that MI-MAE significantly outperforms MAE models in tasks such as image classification, object detection, and semantic segmentation. Our findings validate the theoretical framework and highlight the practical advantages of applying the information bottleneck principle to MAEs, offering deeper insights for developing more powerful self-supervised learning models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a theoretical analysis of masked autoencoders (MAEs) based on information bottleneck theory. Based on the analysis, it indicates that MAE requires to balance the influences of relevant information and irrelevant information when optimizing the latent space. Therefore, the authors propose two loss functions to satisfy the information bottleneck constraints (One is to retain maximize relevant information between them and the output, and the other is to minimize irrelevant information between them and the input). Experiments show that the method outperforms MAE on image classification, object detection, and semantic segmentation

### Strengths
1.	This work proposes a theoretical analysis on the performance of MAE. It has proven that MAE under information bottleneck theory can achieve better performance theoretically.
2.	A novel but simple architecture is proposed to apply information bottleneck theory to MAE, which can improve its performance.
3.	Experiments are conducted on diverse tasks, which is convinced to prove the claim.

### Weaknesses
1.	The illustration of the model in Section 4.2 is not very clear. I am not sure about why the architecture can achieve the separation of the relevant and irrelevant parts of the latent space. Specifically, the mechanism by which the two loss functions, l_max_mi and l_min_mi, enforce this separation is not well-explained. It is unclear how the encoder is designed to explicitly disentangle these two types of information, and how the decoder uses only the relevant information for reconstruction. A more detailed explanation of the architectural choices and their impact on information separation is needed.
2.	There are several studies that introduce the isolation of the latent space with VAE, GAN, or diffusion model. Therefore, I am not sure about the novelty of the proposed MI-MAE in visual tasks. The paper does not adequately differentiate its approach from these existing methods. While the information bottleneck principle is mentioned, the practical implementation and its distinction from existing latent space manipulation techniques in VAEs, GANs, and diffusion models are not clearly articulated. The paper needs to provide a more detailed comparison, highlighting the unique aspects of MI-MAE.
3.	Experiments only cover several general visual tasks and the results seem not to be significantly better than MAE and other baselines. The performance gains, especially on ImageNet fine-tuning, are marginal. The paper needs to demonstrate more substantial improvements to justify the complexity of the proposed method. Furthermore, the experimental section lacks a thorough comparison with other methods that also employ latent space constraints. The paper should include more diverse experiments and comparisons to validate the effectiveness of MI-MAE.

### Questions
1.	Can you further illustrate how two new losses (l_max_mi, l_min_mi) work to constrain the hidden space that can separate relevant and irrelevant variables?
2.	What is the difference of the work compared with VAE, GAN, or diffusion model that can constrain latent space as well?
3.	The performance improvement of MI-MAE is not significant enough. I guess the assumptions of this work are too idealized, which is not a better method for application. Besides, although the theoretical analysis has revealed the relationship of MAE and information bottleneck theory, the solution is similar to other methods with latent constraints. Can you provide more experimental evidence to show the effectiveness of MI-MAE and the difference of the model with other methods with latent constraints, such as case studies, comparisons with more baselines.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studied Masked Autoencoders via information bottleneck: MAE can be interpreted as obtaining the simplest effective distortion to capture all information between masked and recovered images. Then it proposes to add two losses to improve MAE: maximize the mutual information between the latents of different masked views of the same image, and also minimize the mutual information between the latents and the input. The authors show a 0.5% improvement on ImageNet-1K with 400-epoch training compared to 1600-epoch MAE, and outperforms MAE on transfer tasks such as instance segmentation and semantic segmentation.

### Strengths
Originality: this is the first paper to study MAE under information bottleneck. It re-interprets MAE as minimizing a Lagrangian term that includes two terms: the simplest effective description of input and distortion of the network. It then argues that the MAE can only find a suboptimal solution. Finally it introduced two terms, based on explicit terms (MI maximization and minimization) to enforce IB principle, to improve MAE.

Significance: the knowledge of interpreting MAE from an IB viewpoint is useful for the community.

### Weaknesses
Clarity:

The overall motivation is clear, but many small explanations are missing.

(a) First, it is unclear from the discussions after Eq. (3), why MAE can only find a sub-optimal effective description. The reviewer would appreciate more explanations, such as specific constraints or limitations, preferably with formal proofs, that prevent MAE from finding the optimal solution. Specifically, what inherent limitations of the MAE architecture or training process lead to this sub-optimality? Is it a limitation in the expressiveness of the encoder/decoder, or a problem with the optimization landscape?

(b) Sorry if the reviewer has missed it, but it is not clear, after Eq. (4), why mitigating the bias $r$ would help MAE. What is the exact effect of $r$ on the upper bound? Why is improving that upper bound helpful for the LHS of Eq. (4)? And how does the LHS of Eq. (4) directly impact MAE, as the LHS in Eq. (4) is neither the $D_{IB}$ term nor the first MI term in RHS of Eq. (3)? Any mathematical derivation showing these would be very helpful. It would be beneficial to clarify how the bias term $r$ specifically influences the estimation of mutual information and how this, in turn, affects the overall objective function of MAE. A more detailed explanation of the relationship between the bias, the upper bound, and the mutual information terms is needed.

(c) Following up on the last question, there is no clear theoretical link to how the proposed losses can *directly* improve Eq. (3). It is briefly explained in Lines 226 - 227, that “maximizing the mutual information between the latent feature and $\zeta$ will help reduce $I(\hat{z}; X \cdot m | r)$”, but why? Are there any possible direct proofs? Even though this is true, how does reducing $I(\hat{z}; X \cdot m | r)$ directly affect the IB formulation in Eq. (3)? Any concrete steps showing these would be very helpful. A more rigorous explanation is required to show how maximizing the mutual information between latent features and minimizing the mutual information between latents and input directly translates to an improvement in the information bottleneck objective.

Quality:

The empirical improvement is unfortunately not substantial.

### Questions
Where is the proof of Eq. (12)? There is no clear description of the IB distortion term in Eq. (12); how did the authors derive such an error bound, by what theorems? There is the same issue for Eq. (14). Detailed proofs by stating the theorems used will be helpful. 

MINE is known for high variance; have the authors considered other alternative estimators?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed MI-MAE, extending the MAE framework by maximizing relevant and minimizing irrelevant information in latent representations. MI-MAE introduces mutual information-based losses in the encoder's latent space to enhance feature representation. The method optimizes two main loss types, maximizing mutual information across orthogonal masks to retain relevant information and minimizing mutual information between the input and latent space to filter out unnecessary data. Additionally, MI-MAE's setup includes generating multiple orthogonal masks per image, which are reconstructed to validate the relevant mutual information content across different patches. Experiments reveal that MI-MAE outperforms standard MAE configurations across some benchmarks, including ImageNet and COCO.

### Strengths
1. This work provides some new perspective in analyzing MAE with MI backed motivations, and resulting improvements demonstrated the practicability of applying mutual information maximization and minimization within latent representations and between inputs.
2. The paper demonstrates MI-MAE’s efficacy across a variety of vision tasks, including image classification, object detection, and semantic segmentation. In reported results, MI-MAE shows better efficiency in terms of number of training epoch comparing to MAE with comparable accuracy. 
3. This paper provides detailed ablations on effects of different components, such as mask generation strategies, loss functions, and loss weight configurations.

### Weaknesses
1. Increased complexity in training. Additional loss terms $l^{max_mi}$ and $l^{min_mi}$ requires weighting parameters introduced (i.e. $\lambda_1,\lambda_2, \lambda_3$) which are empirically determined, this makes the optimization more complicated than vanilla MAE. The process of tuning these weights is not well-defined, and the sensitivity of the model to these parameters is unclear. The paper lacks a systematic approach to setting these parameters, which could lead to inconsistent performance across different datasets or tasks.
2. This method uses an approximation network to estimate variational distributions for mutual information minimization. It also introduces another layer of approximation, which may not capture the true complexity of the mutual information in the latent space accurately. This could lead to sub-optimal representation learning if the approximation fails. The paper does not provide a detailed analysis of the approximation error or its impact on the final performance. The choice of a simple MLP might be insufficient to model the complex dependencies in the latent space, and alternative approximation methods should be considered.
3. This paper assumes that the model can effectively minimize information distortion in intermediate layers as data progresses through the encoder-decoder structure, which might lead to the over-compression relevant information. The paper does not provide any theoretical or empirical evidence to support this assumption. It is possible that the minimization of mutual information between the input and latent space could inadvertently remove useful information, especially if the approximation is not accurate.
4. Lack of robustness analysis. An important aspect of using information bottleneck is that it can increase the robustness of the pre-trained model. It is of interest to test out how this method performs in ImageNet-A/C validation set.

### Questions
Please refer to the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes to interpret Masked Autoencoders (MAE) using information bottleneck principle. It first conduct a theoretical analyses to show that balance the relevant and irrelevant information in the latent features is the key to improve MAE performance. Then it introduces an improved MI-MAE by maximizing the relevant information between input and latent features and minimize the relevant information between output and latent features. This is achieved by introducing two new losses functions beside the original reconstruction loss. Experiments on image classification, object detection and segmentation reveal the effectiveness of the proposed MI-MAE

### Strengths
+ This paper provides a new perspective in understanding the MAE using information bottleneck in information theory, which distinguishes itself with other methods. Moreover, this paper provide detailed proof on how to understand MAE and how to improve MAE with the idea of information bottleneck.

+ The paper introduces two types of mutual information based losses on the latent space. This is derived and supported by the theoretical  proof. 

+ Validation on various experiments show the effectiveness of MI-MAE. Specifically, MI-MAE can achieve better results compared with MAE even with 4X fewer pretraining epochs. The method can also be generalized to other mask image modeling method such as SimMIM.

### Weaknesses
 - The paper mentions that during each training iteration, it has 4 masks for each image, which can be regraded as data augmentation during training. For a fair comparison with MAE 400 epoch, it might be worth trying to run MAE with 4 augmented masks but without the proposed information losses to truly ablate the effectiveness of the information losses. To be more specific, we could compare (1) Standard MAE (already have). (2). MAE with 4 masks per image but no information losses (3). Full MI-MAE with 4 masks and information losses(already have).

- As demonstrated in Table 1, the MI-MAE generally performs better in linear probing (LIN) or fine-tuning with 1% (FT1%) of the data compared to full fine-tuning (FT). While the authors attempt to explain this phenomenon, the core reason behind this observation remains unclear. The paper should delve deeper into why the information bottleneck principle leads to such an outcome, especially since it is not a typical behavior observed in other methods. The explanation provided is not sufficiently detailed to fully justify this behavior.

- In the caption of Figure 1 Line 177-178, why the notions of two losses l(max_mi) and l(min_mi) doesn't follow \mathcal{L}_{\text{rec}} as the same format? I would recommend  standardizing the notation for consistency, if there isn't a specific reason for the difference.

### Questions
- As demonstrated in Table 1, the MI-MAE generally performs better in linear probing (LIN) or fine-tuning with 1% (FT1%) of the data compared to full fine-tuning (FT). Could the authors provide more details on why this occurs from the perspective of information bottleneck?

- In the caption of Figure 1 Line 177-178, why the notions of two losses l(max_mi) and l(min_mi) doesn't follow \mathcal{L}_{\text{rec}} as the same format? I would recommend  standardizing the notation for consistency, if there isn't a specific reason for the difference.

### Soundness
3

### Presentation
3

### Contribution
3
