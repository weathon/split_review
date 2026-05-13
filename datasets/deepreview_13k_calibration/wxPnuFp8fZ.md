# Self-Supervised Diffusion MRI Denoising via Iterative and Stable Refinement

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 5, 10, 5

## Abstract
Magnetic Resonance Imaging (MRI), including diffusion MRI (dMRI), serves as a ``microscope'' for anatomical structures and routinely mitigates the influence of low signal-to-noise ratio scans by compromising temporal or spatial resolution. However, these compromises fail to meet clinical demands for both efficiency and precision. Consequently, denoising is a vital preprocessing step, particularly for dMRI, where clean data is unavailable. In this paper, we introduce Di-Fusion, a fully self-supervised denoising method that leverages the latter diffusion steps and an adaptive sampling process. Unlike previous approaches, our single-stage framework achieves efficient and stable training without extra noise model training and offers adaptive and controllable results in the sampling process. Our thorough experiments on real and simulated data demonstrate that Di-Fusion achieves state-of-the-art performance in microstructure modeling, tractography tracking, and other downstream tasks. Codes are available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a novel self-supervised denoising method Di-Fusion that leverages the latter diffusion steps and an adaptive sampling process.  Di-Fusion outperforms two slightly older methods and a state-of-the-art approach on   and on downstream processes like tractography.

### Strengths
Paper is easy to follow.
Results across multiple real and simulated datasets, suggesting generalizability of approach.
Baseline is a recent state-of-the-art.
The authors released their code to the reviewers, which is well-written, informative and aides reproducibility.

### Weaknesses
Did the authors consider using: https://arxiv.org/pdf/2305.00042  and    https://arxiv.org/pdf/2309.05794  as baselines?
Better signpost the extensive results in the supplementary materials.
Some parts of the paper read a bit odd and should be checked for oddities e.g. from the introduction 'The MRI, including ...', 'Consequently, the denoising technique plays a crucial role..'

### Questions
Please see weaknesses above.

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
3

### Summary
This paper introduces Di-Fusion, a fully self-supervised diffusion MRI (dMRI) denoising method designed to enhance the signal-to-noise ratio (SNR) of MRI data without requiring clean reference data. The authors leverage novel late diffusion steps and an adaptive sampling process to create a single-stage framework that operates without an explicit noise model. Di-Fusion demonstrates superior performance over state-of-the-art denoising methods in tasks such as microstructure modeling and tractography. The method’s efficacy is validated through extensive quantitative and qualitative evaluations on real and simulated data.

### Strengths
- **Flexibility with data and noise models**: Instead of relying on explicit noise models or clean training data, the method relies on an N2N training strategy and pixel shuffling to reorganize the noise, providing strong generalization potential across different noise distributions. This suggests that the method has the potential to be applied to a wider range of denoising scenarios, such as cryo-EM.
- Compared to the current state-of-the-art method, DDM^2, this approach demonstrates comprehensive improvements. Not only does it outperform in terms of performance, but it is also simpler to implement. Notably, this method does not require additional denoiser training, significantly enhancing its practical usability.
- As a study on dMRI denoising, this paper conducts thorough and comprehensive experiments, including extensive comparisons and analyses on downstream task performance. This renders the work methodologically and experimentally well-rounded.

### Weaknesses
Please refer to the **Questions** section for details.

### Questions
- To my understanding, the primary goal of dMRI denoising is to reduce the number of gradients required during acquisition, thus accelerating DWI scanning. In downstream tasks based on DTI, the authors compare DTI metrics computed from noisy images with those from denoised images. Why did the authors not use more DWI data to compute a clean DTI metric as a reference for comparison?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new self-supervised learning-based denoising method for diffusion MRI (dMRI). The proposed method leveraged the diffusion modeling concept, but instead of training a diffusion model with “clean images” as x_0 and noise as x_T, it utilized two diffusion weighted images (DWIs) with different diffusion encodings at both ends of a “diffusion-like” process. A denoising network was trained by predicting one DWI using a linear combination of two DWIs and an added noise term. The linear combination coefficients are time-dependent and determined via a scheduling strategy similar to training a diffusion model. The network was then used for a conditional sampling step for generating the final denoised images. The idea to utilize images acquired with different diffusion encodings to denoise one of them is interesting and the training strategy is an interesting approach to leverage the diffusion modeling concept, especially with training only latter diffusion steps to reduce hallucinations. However, several key assumptions made are questionable and the overall methodology and presentation lacks clarity. Evaluation using only dMRI signal model goodness of fit is limited and can be biased. There are a few overstatements that can mislead the readers. Detailed comments can be found below.

### Strengths
A diffusion-like modeling that learns the relationship between two DWI volumes with different diffusion encodings to denoise one or each other.

Training only later step diffusion to avoid hallucination

A fusion strategy that exploits linear combination of two DWIs with different contrasts with time-dependent coefficients and iterative refinement.

Extensive evaluations using both simulations that exactly followed the assumptions for the proposed methodology and practical magnitude DWI data.

### Weaknesses
There are statements that can be misleading in the context of MR physics (aka domain knowledge). For example, "the noise predominantly originates from physical interferences (Fadnavis et al., 2020a)". This statement about physical interferences is  both vague and inaccurate. This work is dealing with thermal noise or noise resulting from thermal noise in the measurements, which is not really physical interferences depending on how ones interpret them. Another example, "Different clinical applications require varying numbers of diffusion vectors and acquisition strategies, which makes modeling the noise distribution and further implementing denoising techniques challenging". Acquiring DWIs with varying numbers of diffusion vectors had nothing to do with the difficulty of  modeling noise distribution.

Many key assumptions for the proposed method was built on do not hold which made the theoretical/mathematical foundations questionable, e.g.,
a) It seems that the authors assumed DWIs acquired with different diffusion encodings had the same underlying “clean” image and were corrupted by independent noise. This is inaccurate. In fact, two DWIs can have rather different contrasts due to the diffusion encoding effects, e.g., different diffusion encoding directions. More specifically, x and x’ cannot be simply modeled as the same y plus different noise. What are the implications of this assumption not met?

b) Line 111: The authors claimed that that the proposed method does not require an explicit noise model. This is an overstatement. The J-invariance assumption, which formed the basis of the training objective in Eq. (9) implicitly requires that the noise distribution be zero-means and conditionally independent. Furthermore, additive noise model was assumed, x = y + n1 (Line 200). In dMRI, the magnitude images with higher b-values (stronger diffusion weightings) can have lower SNR for which additive noise may not hold. These need to be clarified.

-  Overall, the presentation lacks clarity and there seem to be some concerning inaccuracies.
a) The linear combination relationship claimed in Section 3.1 does not seem accurate. I checked the derivation. Eq. 31 is correct which is known (so this is not a contribution of the authors), but I'm not sure about going from Eq. 31 to 32 as F_theta predicts x_0, but they are not equal, and there is also an additional term of sigma_t^2*z. Therefore, I don't think it's a correct statement to say x_(t-1) is a linear interpolation between x_out and x_t. But is this really needed for the proposed method? I really don’t see a connection between what’s argued theoretically and what’s actually being implemented.

b) There are a few other inaccurate mathematical statements and notations which are confusing. For example, Eq. 7, the left side has q(x1:T |xt*) which is a joint distribution for x1 to xT, and the right side is a Gaussian distribution for xt. 
On Line 160: {xt}1:T was described as”obtained from the reverse process.” However, in
Figure 1 and on the right side of Equation (7) on Line 186, it appears that xt is a corrupted version of xt*.  This interpretation, along with the notation in the Fig. 1, implies that {xt}1:T would represent a forward process. It appears to this reviewer the authors had not been using a consistent definition of forward and reverse diffusion which made the overall description rather confusing. These are just examples of inconsistencies found.

c) According to the J-invariance property, the noise should ideally have zero mean
and be conditionally independent of the target output. This requirement is necessary to ensure that the expected loss for self-supervised training asymptotical approaching the supervised loss. However, the input to F(.) in Eq. (9) includes xt*, which is a linear combination of x and x’ (Eq. (6)). Given that x serves as the supervision signal for the loss, this implies a correlation between the input x∗t and the target x, which would violate the conditional independence requirement for J-invariance.

### Questions
In Eq. (5) on Line 155, the authors highlighted a specific term as the ”major difference” between xt−1 and x^bar_t−1. Could the authors clarify why this particular term is considered the primary source of difference? Furthermore, can the authors elaborate on the underlying reason(s) for the “drift” in the model and how it emerges during the reverse diffusion process?

According to the definition of the Fusion process in Eq. (6)  and the “forward process” in Eq. (7), it appears that the starting point for the forward process changes based on t, as x_t* is dependent on t. This dependence implies that the Fusion process dynamically adjusts the starting point of the forward process at each step, which is unconventional compared to typical diffusion models. Could the authors clarify the rationale behind this design?

Other more recent self-supervised denoising methods should be compared, if not for all, e.g., Noise2Score and Recorrupted2Recorrupted etc.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This is a new denoising method for dMRI data. Combines DL-based diffusion models with a bit of fusion. The fusion process stabilizes issues that DDM2 has.

I suggest that the authors refrain from large claims. For example, it says that it outperforms the other methods. But I do not see any speed or memory comparisons. 

In the comparisons I would also add MPPCA. I would also cite Patch2Self2 (CVPR 24). Patch2Self has clearly outperformed MPPCA however still many people use MPPCA.

The paper does a great job on the methodological sections. 
In providing code and using open source standards.

However, at least a thorough review of language is required.

Qualitatively it is hard to see large advantages over Patch2Self but nonetheless the method is useful. 

In the revision please report time and memory usage. I would also compare against Patch2Self2 if possible.

Also it would be important to explain the setup. What GPUs were used for training?

### Strengths
Great way to stabilize the diffusion process.

### Weaknesses
Refrain from large claims. For example, it says that it outperforms the other methods. But I do not see any speed or memory comparisons.

In the comparisons I would also add MPPCA. I would also cite Patch2Self2 (CVPR 24). Patch2Self has clearly outperformed MPPCA however still many people use MPPCA.

The paper does a great job on the methodological sections.
In providing code and using open source standards.

However, at least a thorough review of language is required.

Qualitatively it is hard to see large advantages over Patch2Self but nonetheless the method is useful.

In the revision please report time and memory usage. I would also compare against Patch2Self2 if possible.

Also it would be important to explain the setup. What GPUs were used for training?

### Questions
What is the actual minimum number of B0 and DWI volumes required ?

Can this work with data that have a single B0? Would that be denoised?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method for denoising diffusion MRI data sets.

This is a well-studied problem with many solutions in the literature. It is an important problem, as diffusion MRI is widely used for neuroscience and for clinical medicine. Recent years have seen a trend towards using self-supervised approaches to characterise the noise distribution and separate noise from the underlying signal.  This submission falls very much in this category, but proposes a different algorithm to those that are popular in the literature.

Experiments compare against five baselines and results appear competitive with other methods, sometimes surpassing them.

### Strengths
The algorithm appears novel, although I found it hard to tell from the literature review how novel it is - whether it takes ideas from other areas and repurposes them for this problem, or if this is an algorithm specifically designed for diffusion MRI.

The problem is an important one with widespread application.

Results appear competitive on a few example images shown in the figures.

### Weaknesses
The baselines chosen do not include the most widely used denoising methods.  A clear omission is the random-matrix theory approaches proposed by Veraart et al in a series of very highly cited papers starting with Neuroimage 2016.

The only quantitative results use simulations, which seem likely to be skewed towards to capabilities of the proposed algorithm.

The qualitative results on actual human data are questionable as to whether they show improvement over baselines.  Even if they do, these are single cherry-picked examples and it is not clear whether these are advantages that manifest over large collections of images/scenarios.

### Questions
Corresponding to weaknesses listed above.

### Soundness
3

### Presentation
2

### Contribution
2
