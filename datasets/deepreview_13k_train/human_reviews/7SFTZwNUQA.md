# Patch-Based Diffusion Models Beat Whole-Image Models for Mismatched Distribution Inverse Problems

- Decision: Reject
- Scores: 5, 6, 5, 5, 5

## Abstract
Diffusion models have achieved excellent success in solving inverse problems
due to their ability to learn strong image priors,
but existing approaches require a large training dataset of images
that should come from the same distribution as the test dataset.
When the training and test distributions are mismatched,
artifacts and hallucinations can occur in reconstructed images due to the incorrect priors.
In this work, we systematically study out of distribution (OOD) problems where a known training distribution is first provided.
We first study the setting where only a single measurement obtained from the unknown test distribution is available.
Next we study the setting where a very small sample of data belonging to the test distribution
is available, and our goal is still to reconstruct an image from a measurement that came from the test distribution.
In both settings, we use a patch-based diffusion prior
that learns the image distribution solely from patches.
Furthermore, in the first setting, we include a self-supervised loss
that helps the network output maintain consistency with the measurement.
Extensive experiments show that in both settings,
the patch-based method can obtain high quality image reconstructions 
that can outperform whole-image models
and can compete with methods that have access to large in-distribution training datasets.
Furthermore, we show how whole-image models are prone to memorization and overfitting,
leading to artifacts in the reconstructions, while a patch-based model can resolve these issues.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper considers the problem of adapting diffusion models trained on a domain A  to the task of solving reconstruction problems on another domain B, and investigate the cases where a single measurement from B or a small number of samples from B are available.
To that end, the authors investigate deep diffusion image prior (DDIP) adaption methods, which were originally proposed to be used with whole-image diffusion models, and combine with the recently proposed patch-based diffusion models. The experimental results on CT and natural image datasets shows that patch-based diffusion models are more robust to fine-tuning on small dataset as well as to adapting the network weights for single-measurement domain adaption.

### Strengths
- The considered domain adaption tasks are important for practical application.
- The observation that patch-based diffusion models are more robust to finetuning / out-of-distribution tasks is interesting and relevant.

### Weaknesses
 - While it is important to improve upon the considered tasks, and the paper presents good results on that task, I am unsure about the contribution of the paper. The paper combines the existing SCD/DDIP method with the recently proposed patch-based diffusion models and their inverse-problem solver (PaDIS), but it seems that this is only a matter of replacing the whole-image with patch-based diffusion models and their score calculation method. The robustness to OOD data of patch-based models is important, but the relation to the experiments on small datasets presented by [1] is unclear.
- The results in Table 1 show that the main performance gains are due to using SCD/DDIP and using that with Patch-based DMs increases the PSNR by at most 1dB. While this is certainly an improvement, using the patch-based model in-distribution already increases the PSNR.
- In section 3, the authors introduce the patch-based diffusion prior method, where they seem to have copied Figure 1 and the text (with small adaptions) from the original paper. I think this should be stated more clearly. Moreover, some parts in the argumentation seem to missing. As an example, L.198-199: "represents the aforementioned bordering region", but the bordering region has not really been mentioned before (in contrast to the original text). Restating the assumed probability distribution in L.195, but it would be helpful to also state the motivation (the calculation of the score model based on the patch scores).

### Questions
- In their appendix, [1] provide experimental results when training whole image and patch-based models on training datasets of different sizes, and similarly observe that PaDIS remains visually more consistent in contrast to the whole-image models. Could the authors elaborate how their experiments and observations relate and potentially complement those of [1]?
- See also the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to use patch-based diffusion models for solving inverse problems with mismatched training and test distributions. The authors address the challenge of artifacts and hallucinations in image reconstructions when the training and test datasets are not aligned. They propose a patch-based approach that leverages image patches to learn priors, demonstrating the effectiveness of the proposed method in scenarios with limited data availability.

### Strengths
1. The writing is clear so easy to follow.

2. The motivation of using patch-based prior for better generalizability is reasonable.

3. The proposed method addresses an important practical problem.

### Weaknesses
1. It is not clear why Eq. (11) can address "The image that is being reconstructed might not come from the distribution of the training images". I recommend the authors to provide more detailed discussion. Specifically, the connection between minimizing the data consistency term and the network's ability to generalize to out-of-distribution data remains unclear. The loss function in Eq. (11) seems to only enforce data consistency with the measurement *y*, but it is not obvious how this directly alters the learned prior to accommodate a different data distribution. A more detailed explanation of how this adjustment occurs and why it is effective is needed.

2. The proposed method is similar to Deep Diffusion Image Prior for Efficient OOD Adaptation in 3D Inverse Problems. It could be beneficial to discuss the similarity and difference to highlight the contribution of this paper. The paper should more clearly articulate what specific aspects of their method are novel compared to existing approaches, and why these novel aspects are important. For example, a more detailed comparison of the training and fine-tuning procedures, and the specific architectural choices would be beneficial.

### Questions
I would like to see what the results would be like when applying the method to the black whole imaging problem [1] where the true prior is unavailable.

[1] Wu, Zihui, et al. "Principled Probabilistic Imaging using Diffusion Models as Plug-and-Play Priors." arXiv preprint arXiv:2405.18782 (2024).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper shows that the patch-based diffusion model can be a good solution for mismatching distribution inverse problems, compared to the conventional whole-image diffusion model. The authors study this setting where (1) only measurements are available and (2) very small ID samples are available, the results are decent.

### Strengths
1. The paper is easy to follow.
2. The topic of mismatching distribution inverse problems is timely and important.
3. Using patch-based diffusion models for mismatching distribution inverse problems is natural.

### Weaknesses
1. I doubt the contribution of the work. As it is not new to solve inverse problems with patch-based diffusion models[1], the finding of this paper 'whole-image models are prone to memorization and overfitting, while a patch-based model can resolve these issues' is already clarified in [1]. The paper does not sufficiently distinguish its contributions from existing work. While the authors apply patch-based diffusion to a mismatch setting, the core idea of using patches to mitigate overfitting is not novel and lacks a clear, unique contribution.

2. Lack of theoretical analysis. It is straightforward that patch-based diffusion models are suited for mismatching distribution inverse problems, as they can avoid memorization and overfitting ID data. It would be good if the authors could provide some theory on this argument. The paper lacks a theoretical justification for why patch-based models are more robust to distribution shifts. A theoretical framework explaining the generalization properties of patch-based models in this context would significantly strengthen the work.

3. Minor:

      Errors in Eq. 2 and Eq. 3;

      Better to repaint Fig. 1 instead of directly copying it from [1] without citation.

### Questions
1. Can the authors provide some figures of training data? I have seen Fig. 20 but I still can not imagine the training data.
2. Why Fig. 6 does not have the same notations as Fig. 3? It looks really confusing.
3. I am wondering if the proposed method can scale up. Since patch-based diffusion models should aim for large images, the experiments on CelebA 256*256 are insufficient.

I am willing to raise the score if the concerns are well-addressed.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the use of diffusion models in inverse problems, particularly when there’s a mismatch between the training and test data distributions (out-of-distribution, OOD). The authors investigate two settings: one where only a single measurement from an unknown test distribution is available, and another where a small sample from the test distribution is accessible. They propose a patch-based diffusion model that learns image priors from patches rather than entire images. This model includes a self-supervised loss to enhance consistency with the given measurement in the single-measurement scenario. Their experiments demonstrate that this patch-based approach produces high-quality reconstructions.

### Strengths
- The paper addresses an important and practical problem that commonly arises in real-world scenarios, where the generative prior distribution differs from the target distribution. This focus on out-of-distribution (OOD) issues has strong applicability in diverse settings.

- The experimental results show that the proposed patch-based model achieves better performance compared to whole-image models, underscoring the effectiveness of a patch-based approach in handling OOD challenges for inverse problems.

### Weaknesses
 - Limited novelty. I believe that the paper’s primary contribution—a combination of a patch-based model with self-supervised loss (e.g., deep image priors) to address out-of-distribution (OOD) issues in inverse problems—builds on existing concepts. While the integration of these components to tackle a specific challenge is interesting, the novelty is somewhat limited, as each component’s effectiveness has been demonstrated in prior works. Additionally, there is a lack of theoretical justification or clear intuition for the design of Algorithm 1, which would strengthen the proposed approach.

- The experimental setup lacks clarity. Specifically, it is not explained how the authors achieve the “Whole image, correct*” model or which sampling algorithm is used. Key hypothetical models are described ambiguously, and the term “best baselines” in Table 2 is undefined, making it challenging to understand the comparisons being drawn.

- Lack of analysis. Why the proposed algorithm 1 or patch-based model is better than previous models is not clearly demonstrated in the paper.

- Missing baselines. The paper does not include comparisons with strong baseline methods for inverse problem-solving using diffusion models, such as DPS [1], DDS [2], DDNM [3], and DAVI [4]. These methods are relevant in both single-measurement and limited-sample settings. In particular, [4] addresses OOD settings, making it a highly relevant benchmark for this work.

### Questions
Please provide clarity on points raised under the weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This works tackles the challenging problem of solving inverse problems where only a few samples are available from the test distribution. Authors propose a patch-based diffusion prior in this scenario, that learns the image distribution from patches, and not from whole images. Authors argue that whole-image models are prone to overfitting to the data distribution, and thus are unable to provide sufficient performance when the test samples come from out of distribution. Numerical experiments are provided to verify these findings.

### Strengths
- The problem is well motivated and important. In a multitude of real-world applications, it is infeasible to collect large datasets for training diffusion models on the target distribution. However, finding ways to leverage the strong prior provided by diffusion models to tackle such problems is a valuable direction.

- The key idea of using patch-based diffusion instead of whole-image diffusion is intuitive and sensible. The patch-based model is less prone to overfitting to the available source data distribution, and thus can perform better in the presence of distribution shifts. Moreover, patch-based models can be trained more data-efficiently which is crucial in the data scarce domain.

- The experimental results, if verified on larger scale experiments, are promising.

### Weaknesses
 - The clarity of the paper could be greatly improved. In particular, I had a difficult time following 3.1, which is central to understanding the proposed algorithm and led to downstream confusions throughout the paper. Specific questions follow under 'Questions'. The explanation of how the patches are extracted and used within the diffusion framework is not sufficiently clear. The roles of $M$ and $k$ in equation (8) are not defined before their use, and the outer product's range should be clarified as $P^2$ based on the paper's notation, not $M^2$. The patch offset should also be explicitly defined as having two indices, one for row and one for column, to avoid ambiguity. The framework, particularly equation (8), requires a more thorough and precise introduction.

- If I understand correctly, the experimental results are reported on 10 samples. This is not enough to report statistically meaningful results.

- Many claims in the experimental section are vague or not supported properly by the experiments (see more details under 'Questions').

- How is it possible that the proposed method, without training, outperforms diffusion approaches that leverage training data? This sounds very counter-intuitive.

- The discussion on diversity of generated samples is very vague. What do authors mean by samples "show some unrealistic features"? IT is unclear based on the Figure 7 which features are considered realistic/unrealistic. Claims about sample diversity would be more convincing if authors reported specific metrics about diversity, such as Recall.

- Table 3 is in the appendix, and therefore it should either moved to the main paper or the discussion about Table 3 should be moved to the appendix.

### Questions
Questions/feedback on clarity: 

- 3.1. is difficult to follow without already knowing the framework the authors adapt. Why is the bordering region added? What is $M$ here, and what is $k$? What does $i$ denote? Is $x$ an image patch or the whole image, as it has been used throughout the paper for both. Why only the x-positions of patches are concatenated as input, why not both x and y coordinates?

- Probably due to the unclear nature of 3.1. I was unable to properly follow 3.2 in some parts. What do authors mean by "the outermost product is computationally very expensive"?

Questions/feedback on experiments:

- How many samples have been used to produce the results reported in Table 1?

- I recommend reporting perceptual metrics such as LPIPS as well, especially for image deblurring and superresolution.

- How is it possible that the proposed method, without training, outperforms diffusion approaches that leverage training data? This sounds very counter-intuitive.

- Which dataset has been used to produce Figures 4 and 5?

- The discussion on diversity of generated samples is very vague. What do authors mean by samples "show some unrealistic features"? IT is unclear based on the Figure 7 which features are considered realistic/unrealistic. Claims about sample diversity would be more convincing if authors reported specific metrics about diversity, such as Recall.

- Table 3 is in the appendix, and therefore it should either moved to the main paper or the discussion about Table 3 should be moved to the appendix.

### Soundness
2

### Presentation
1

### Contribution
3
