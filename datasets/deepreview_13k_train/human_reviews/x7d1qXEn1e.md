# A Restoration Network as an Implicit Prior

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Image denoisers have been shown to be powerful priors for solving inverse problems in imaging. In this work, we introduce a generalization of these methods that allows any image restoration network to be used as an implicit prior. The proposed method uses priors specified by deep neural networks pre-trained as general restoration operators. The method provides a principled approach for adapting state-of-the-art restoration models for other inverse problems. Our theoretical result analyzes its convergence to a stationary point of a global functional associated with the restoration operator. Numerical results show that the method using a super-resolution prior achieves state-of-the-art performance both quantitatively and qualitatively. Overall, this work offers a step forward for solving inverse problems by enabling the use of powerful pre-trained restoration models as priors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to improve a family of solutions to inverse problems called plug and play reconstruction methods by replacing their implicit priors. Instead of utilizing only denoisers, the proposed method suggests other reconstruction methods can also be utilized as priors. They provide a theoretical study with key assumptions to illustrate the convergence. They present a numerical study on the convergence for two applications considered, deblurring and super-resolution. Lastly, the authors present results on multiple datasets compared against related previous works, showing improvements in most cases, according to their evaluation method.

### Strengths
Originality: The main contribution of the work is extending the formulation of plug and play reconstruction methods to utilize implicit priors other than only denoisers.

Clarity: The theoretical analysis of their proposed idea is clearly presented.

Significance: While the performance numbers seem not necessarily significant in terms of improvements, it could lead to more improvements in subsequent works.

### Weaknesses
1) The method utilizes a pre-trained SwinIR [1]. However, according to the Table 2 from SwinIR, the performance of SwinIR for the task super-resolution is ~6db higher in terms of PSNR on set5, which is confusing. The authors should include the SwinIR for all of the test datasets as a baseline and explain the reason there is a performance drop after adapting their method.

2) There is another main weakness in the experimental results. There seems to be no discussion on the sources of randomness for the proposed method and the compared works. I would assume for the proposed method, there could be randomness involved in all three main stages: the pre-training, the refinement process, and the Algorithm 1 itself. The same issue could also be true for the considered compared methods. The experimental study should consider multiple runs for each of the mentioned stages and provide individual or combined analysis on the distribution of results rather than just a single run. The reviewers need to be sure whether the provided performance numbers are the worst single runs of compared methods versus the best single run of the proposed method, or are average cases for all considered methods. Without providing such analysis using multiple runs, it is hard to assess the significance of the results for the proposed method.

### Questions
3) The authors should include other evaluation metrics, such as SSIM and LPIPS, for the results. That would help to make sure the performance is not biased towards a single evaluation metric.

4) The authors mention one of the limitations for the proposed method is  “the assumption that the restoration prior used for inference performs MMSE estimation.” However, it is not clear if for the compared methods, they have included any of recent methods that are trained based on l_1 loss and SSIM to clarify how much this limitation affects the final performance in different applications.

5) Using a number of different implicit priors rather than only a single architecture while comparing their performance numbers before and after applying the proposed method would clarify to what extend the method is sensitive to the implicit prior’s performance.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In plug-and-play-type algorithms, a denoiser (such as a CNN trained to denoise images) is plugged in the place of the proximal operator which is part of the formally derived algorithm. This paper proposes a way of extending this approach in a way that allows the use not only denoisers but also other restoration networks (e.g., a trained super-resolution CNN). The extension is simple, although non-trivial, and the paper provides theoretical convergence guarantees and experimental validation.

### Strengths
As I mentioned above, the extension proposed in this paper is simple, although non-trivial, and the paper provides theoretical convergence guarantees and experimental validation. It is a solid paper and the authors show a clear and solid knowledge of the field and of the state of the art, which is comprehensively reviewed. In summary, although certainly not a breakthrough or a very exciting new method, it is a good quality piece of work.

### Weaknesses
Although this is a good quality paper, there are a few aspects that could be improved, some important, others less so. 

First, and most importantly, the paper lacks some discussion/analysis of why restoration networks for problems other than denoising can lead to better results than denoising regularizers. Do they learn better image priors? This is somewhat surprising, in that these other networks are expected to have learned (in addition to a "prior") also specific aspects of the particular problem in which they were trained. This begs the question: what problems yield the best restoration networks? Is this choice related to the main problem to be solved? It is unclear if the performance gain is due to a better prior or simply because the network is better suited to the specific inverse problem, which is a critical distinction that needs further investigation.

The previous comment is related to the following observation: although the authors present the method as working for general restoration networks, they end up only using restoration networks trained for super-resolution. Arguably, SR is a very particular type of inverse problem, in a sense, the one that is closer to pure denoising than any other inverse problem. The authors should comment on this. The lack of experiments with other types of restoration networks, such as those trained for deblurring or inpainting, limits the generalizability of the claims. It is essential to demonstrate the method's effectiveness across a wider range of inverse problems to support the claim of general applicability.

In Section 4, there is some confusion regarding necessary and sufficient conditions. The authors write "Our analysis will require several assumptions that act as sufficient conditions for our theoretical results." This sentence is self-contracting: if the assumptions are *required* they are *necessary* ("necessary" and "required" are synonyms). In fact, further down, the authors contradict that sentence, by writing "This mild assumption is necessary ...".

The first inequality in Theorem 2 is trivial and doesn't even need to be mentioned. 

Minor style issue: it is not good style to write "...discussion in Kamilov et al. (2023) on ..." or "... in Chapter 3 in Beck (2017) ...". Kamilov and Beck are not papers or books, but people. A nicer way to write these sentences is "...discussion in the work of Kamilov et al. (2023) on ..." or "...discussion in the paper by Kamilov et al. (2023) on ..." and "... in Chapter 3 of the book by Beck (2017) ...".

A probability density function is degenerate, not only if it is supported on a subspace, but on any zero-measure set in the ambient space, for example, a d-manifold, with d < n. 

Typo: "Our method is as a major extension ..." should be "Our method is a major extension ...".

### Questions
The form of Equation (9) suggests that using the regularizer trained to solve (4) is in some sense equivalent, or at least related, to analysis regularization/priors, where $p_s$ is a learned prior and ${\bf H}$ the analysis operator. See https://doi.org/10.1117/12.826663 
What do the authors think of this connection?

How much is lost by solving (10) and (11) by CG and how do the authors know that 3 iterations is enough? Would it be worth (at least for (10)) to give some careful thought to the form of the inversions needed; maybe it is possible to exploit the fact that bot ${\bf H}$ and ${\bf K}$ can are convolutions to obtain closed-form inversions using FFTs.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes the DRP method which utilizes a pre-trained restoration network as a prior to solve the inverse problem. Under several mild assumptions, it proves the convergence of DRP. In the experiments, two popular tasks (e.g., debluring and super-resolution) are considered to validate the effectiveness of the proposed method.

### Strengths
1. The paper is well written, and easy to follow.
2. It provides sound theory proof on the convergence of DRP.

### Weaknesses
1. As for evaluation metric, more commonly-used metrics should be employed to have a comprehensive comparison, such as SSIM, LPIPS.
2. More comparative methods should be considered, including the DIP prior-based methods DIPFKP (CVPR 2021) and BSRDM (CVPR 2022) and some directly trained based method, such as BSRNet (ICCV 2021), RealESRNet (ICCV 2021 workshop).
3. This is a non-blind method. The experiments only verify its simple case with known degradation. I wonder that is it able to handle the real-world case?
4.  As shown in the appendix, its performance is obviously inferior to DRUNet. Additionally, it relies on the SwinIR as a prior. It is necessary to conduct a comparison with SwinIR.

### Questions
1. According to my understanding, the motivation and idea of this work is very similar to IRCNN. The main difference to IRCNN is that it uses a more powerful restoration network SwinIR instead of DnCNN. The sprox operator in Eq. (5) corresponds to the sub-optimization problem Eq. (6a) of the paper of IRCNN. The core step 3 in Algorithm 1 corresponds to Eq. (6b) of IRCNN.
2. Following the last question, step 3 introduce the restoration prior in Algorithm 1. I'm interested in that how to induce the updated procedure of step 3. In other word, a more intuitive explanation on step 3 should be provided.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims at generalizing the idea of the implicit image prior parameterized by a pre-learned deep denoiser, for the plug-and-lay type image restoration. Specifically, the authors proposed the so-called deep restoration prior (DRP), which can be learned by more general image restoration tasks, such as super-resolution and deblurring. To demonstrate the effectiveness of the proposed method, the authors have trained a DRP based on super-resolution with a SwinIR architecture, and applied it to image deblurrring and super-resolution tasks.

### Strengths
1. The idea is interesting and provides some new perspectives of the implicit image prior.

2. Theoretical analysis has been provided.

### Weaknesses
1. The motivation of this work is not convincing enough. As I can understand, the aim of DRP is to better or more generally characterize the prior of images. However, it is doubtful whether this generalization is necessary since the deep denoising prior can be flexible enough by virtue of advanced neural network architectures.

2. The application of the proposed DRP is more complicated. Specifically, the additional degradation operator H can make the image restoration optimization process more complex, as can be observed in Algorithm 1. Besides, the additional operator H raises another question, that is how to choose this operator. The authors experimented with super-resolution prior, which assumes H to be downscaling, but it is unknown what if other operator is adopted, and which operator is the best.

3. The experimental comparison seems unfair. In specific, the authors used SwinIR for their DRP, while using DRUNet for DPIR, though DRUNet was adopted in the original DPIR work. It is necessary to re-implement DPIR with SwinIR, or re-implement DRP with DRUNet, such that the influences of network structure can be controlled.

### Questions
My concerns are provided in the "weaknesses" part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
