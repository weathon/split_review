# Model Collapse Analysis and Improvement for Rectified Flow Models

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Generative models aim to produce synthetic data indistinguishable from real distributions, but iterative training on self-generated data can lead to \emph{model collapse (MC)}, where performance degrades over time. In this work, we provide the first theoretical analysis of MC in Rectified Flow by framing it within the context of Denoising Autoencoders (DAEs). We show that when DAE models are trained on recursively generated synthetic data with small noise variance, they suffer from MC with progressive diminishing generation quality. To address this MC issue, we propose methods that strategically incorporate real data into the training process, even when direct noise-image pairs are unavailable. Our proposed techniques, including Reverse Collapse-Avoiding (RCA) Reflow and Online Collapse-Avoiding Reflow (OCAR), effectively prevent MC while maintaining the efficiency benefits of Rectified Flow. Extensive experiments on standard image datasets demonstrate that our methods not only mitigate MC but also improve sampling efficiency, leading to higher-quality image generation with fewer sampling steps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to avoid model collapse in rectified flow model for generative modeling. From theoretical analysis, this paper shows that the training of rectified flow model is affected by the training samples and proposes reverse collapse-avoiding reflow by mixing synthetic and real reverse pairs. This paper shows a toy example on Gaussian data distribution, CIFAR-10, and CelebA-HQ256 dataset. Overall, this paper shows some point interesting to avoid model collapse in rectified flow model, however, it seems this paper is not ready for a strong submission. Therefore, I slightly lean to reject this paper, but may change my final rating after reading other reviewers' comments and authors' rebuttal.

### Strengths
+ This paper provides theoretical analysis for rectified flow model, and points out the connection/differences to diffusion models. The rectified model is more efficient in sampling than diffusion models.

+ According to the experiments with Gaussian distribution, this paper shows the effectiveness of the proposed solution.

### Weaknesses
 + Paper writing needs to improve. It seems this paper is completed in the rush and not ready for a strong submission. There are too many "?" in the Figure/Table/etc.
Line 310 Appendix?
Line 340 Figure ?
Line 372 Algorithm?
Line 417 Appendix ?
Line 514 Table ?

+ This paper claims the experiments are conducted for CIFAR-10 and CelebA-HQ256 datasets, however, the quantitative numbers and qualitative results are not shown in the main submission. Lacking of experiments is a fatal point and hard to make readers convinced.

+ As mentioned in the abstract and introduction, the proposed method can be used to generate high resolution images. However, 256x256 images are generated as reported, which is not enough. Higher resolution such as 1024x1024 will be more interesting.

### Questions
What is the relationship between \head{x}^{(i)} and x^{(i)}? Does the method sample x^{(i)} from the dataset randomly?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the issue of k-rectified flow, specifically focusing on the problem of drift that eventually leads to mode collapse. According to the authors, the root cause of this issue is that reflow relies solely on synthetic data, causing the generated distribution to drift too far from the original real image distribution over time. This insight stems from a theoretical framework based on Denoising Autoencoders. To mitigate this, the authors propose incorporating real images into the reflow process. By applying inversion on these images, they obtain inverted noise-real image pairs that can be integrated into the reflow process (RCA). Additionally, to improve efficiency, they introduce an online version that generates and mixes inverted noise-real image pairs dynamically.

### Strengths
The paper is technically rigorous, with a strong foundation in theoretical analysis that clearly leads to practical implementation. Using Denoising Autoencoders (DAEs) to illustrate mode collapse is particularly effective, as it provides a helpful visualization of the issue. The topic (mode collapse) is a fundamental limitation in k-rectified flow models, and addressing it could have significant impact on improving model stability. The proposed methods offers a well-rounded solution and quite efficient.

### Weaknesses
Presentation:
- The presentation lacks thoroughness and one major part is put into the supplementary material.
- A lot of missing/ undefined references
Experiments:
- Not in main paper
- A lot of promised results are not presented, all the outcome is only on toy samples (gaussian dataset). All the experiment upon real dataset such as upon CIFAR-10, CelebA-HQ are mentioned however no where to be found. Also lacks of metrics to check about mode collapse such as recall.
- Also no qualitative results upon the real datasets.
- Lack of ablation studies upon several aspects: amount of real dataset samples, mix ratio $\lambda$,...

### Questions
The author should address problems mentioned in weakness.

### Soundness
2

### Presentation
1

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
The paper analyses model collapse in rectified flow models, i.e. models that train on data-noise couplings induced by themselves. The main observation is that with the number of such reflow iterations the quality of the generated data decreases. The authors provide a theoretical investigation of the phenomena for the simplistic case of linear denoising autoencoders and based on that they propose several schemes of incorporating the original real data in the subsequent reflow iterations to prevent model collapse. The main idea is to map the original data to noise using the reverse ODE/SDE of the learned vector field. Experimentally, the authors justify the claims on gaussian data.

### Strengths
The motivation delivered in the introduction is clear. The investigated problem is interesting and the approach presented in the paper is, to the best of my knowledge, original. The authors also provide theoretical analysis of the problem.

### Weaknesses
The main weakness of the paper is the presentation. Frankly, the paper seems to be quite raw: there are a lot of typos, poor formatting of the equations (e.g. Equation 5), undefined variables (e.g. $\Phi$ in Line 264, $U^*$ in Line 278 or $E_j$ in Line 282), broken references to the results (e.g. Line 310, 340, 372, 417, 514), missing results (experiments on CelebA were claimed, but never presented in the paper). Besides this, most of the evaluation is limited to only toy data (Gaussian-to-Gaussian mapping) and the results on real data (CIFAR10) are mixed (see Questions). Because of this, and despite the listed strengths, I cannot vote for acceptance of the paper.

### Questions
Here are some questions to the authors and further concerns that influenced my decision:
- The connection between the theoretical analysis and the proposed method is unclear. How does integrating real data in the training help breaking the bound in Theorem 1? Appendix A.3 is the closest to discussing this, but given the poor presentation quality, it seems to be isolated from the rest of the paper.
- The mixing scheme in Equation 11 is questionable. As far as I understand, the pairs are created by mixing independent synthetic and real data with a convex interpolation. In principle, this can destroy the target distribution. Could the authors provide more details regarding this? Another interpretation could be training on both pairs without mixing them, but maybe with balancing the ratio between synthetic and real data, if needed.
- The FID on CIFAR from Figure 1 (4.67 at 10th Reflow-RCA) contradicts with the FID in Figure 5 that seems to be above 35. Could the authors clarify this?
- How do the performances of the full model on real data differ with and without RCA? Based on the results presented in Figure 5, RCA is also prone to model collapse, although not as much as the vanilla Reflow. So there is a question, whether the model actually benefits from more than 1-3 Reflow iterations. If not and if the decrease in quality due to model collapse is not significant for the first couple of Reflow iterations, then the advantages of using RCA are unclear.

### Soundness
1

### Presentation
1

### Contribution
2
