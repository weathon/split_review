# Enhancing lensless imaging via Explicit Learning of Model Mismatch

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Emerging lensless imaging techniques hold promise for miniaturized cameras, but their effectiveness is constrained by challenges like model mismatch from the point spread function (PSF), which undermines reconstruction methods dependent on accurate PSF modeling. To address this issue, we propose a joint Maximum a Posteriori (MAP) approach to simultaneously estimate model mismatch error (${\rm M^{2}}$E) and reconstruct high-resolution images from lensless imaging measurements. Specifically, we propose an explicit latent space representation for ${\rm M^{2}}$E to improve robustness against PSF inaccuracies. Additionally, we develop a multi-stage reconstruction network by unfolding the joint MAP estimator with a learned Laplacian Scale Mixture (LSM) prior and ${\rm M^{2}}$E representation (${\rm M^{2}}$ER) through end-to-end optimization. Extensive experiments show that our method surpasses current state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Proposes a two-step learning-based algorithms for reconstructing lensless images. The approach first estimates the forward model (or more accurately the bias introduced by inverting the measurement forward model). It then uses this forwad model estimate within an interative reconstruction network. The proposed method is tested on existing methods as well as a new dataset captured by the authors using their own lensless camera. The proposed method noticeably outperforms existing methods.

### Strengths
---Outperforms existing methods on experimentally captured datasets
---Introduces a new dataset
---Method is novel (to my knowledge)

### Weaknesses
The proposed method was trained and tested on a subset of the phlatcam dataset (images presented on a display) where there is relatively little model mismatch. The new dataset was also restricted 2D images presented on a display at a fixed distance from the sensor. There is no evidence the proposed method generalizes to real-world 3D scenes.

Many (generally minor) mathematical errors:
--- "Biased" seems an inappropriate term for \hat{O}. That estimate of O may be unbiased, it's just noisy. Similarly, is fig 7's PSF "biased" or just measured.
---The text says (5) to (6) is just taking a logarithm. This step also required Bayes' rule. It's also missing a constant.
---In general, a joint maximum a posteriori estimation problem (7) (bivariate optimization) cannot be split into two independent optimization problems (8a,8b)
---Equation (8b) doesn't make any sense. You have two unknowns, \mathcal{A} and x, but you are only optimizing for one of them. Should \mathcal{A} be \mathcal{A}^*?

Presentation:
---Line 318 would be more recognizable as FFT based deconvolution by moving the inverse inside the parenthesis. 
---The paper seems to be citing the latest paper to mention a result, rather than the paper where it was first introduced. For instance, it cites a 2024 paper to describe a convolutional model for a lensless camera. 
---What does it mean to "mine" a variable?

### Questions
How well does the proposed method work on images of 3D scenes? How well does the proposed method work on the webcam captures and other real-world scenes found in the phlatcam and flatnet papers?

Would the proposed method work with diffusercams?

### Soundness
2

### Presentation
2

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
This paper addresses challenges in lensless imaging, where model mismatches, such as inaccuracies in the point spread function (PSF), impair the effectiveness of image reconstruction. The authors propose a Maximum a Posteriori (MAP) framework to jointly estimate model mismatch error (M2E) and improve image resolution. They introduce a multi-stage reconstruction network called M2LNet, which explicitly learns M2E through a gaussian latent space representation to enhance robustness against PSF inaccuracies. M2LNet, utilizing a Laplacian Scale Mixture prior, demonstrates improvements over current methods across two datasets. Extensive experiments validate its efficacy, showcasing superior image quality and computational efficiency.

### Strengths
1, The paper takes a unique approach by directly incorporating an explicit latent space representation of M2E within the reconstruction framework. By explicitly quantifying and integrating M2E into the multi-stage reconstruction process, the model improves robustness against inaccuracies in the point spread function (PSF), which is often a challenge in lensless imaging. 

2, The proposed M2LNet framework is designed as a multi-stage reconstruction network, where each stage is unfolded from a MAP estimator and optimized in an end-to-end fashion, reducing manual finetuning burden.

3, The proposed method outperforms many existing baseline methods on two dataset, showing the effectiveness of this proposal.

### Weaknesses
1, The technical contribution to the broader field of computational imaging appears limited or, at the very least, unclear in the current form of this paper. Joint forward-model calibration and image reconstruction through unfolding algorithms are already well-explored in inverse imaging problems. The distinction between this approach and other end-to-end deep unfolding methods for lens design—where alternative estimation of PSF and image reconstruction are similarly implemented—remains unclear. Specifically, the paper does not adequately articulate how the proposed method's approach to modeling model mismatch error (M2E) differs fundamentally from existing techniques that also aim to refine the forward model within an iterative reconstruction framework. The use of a latent space representation for M2E, while novel, needs further justification as to why this is a superior approach compared to directly estimating the PSF parameters or using other forms of model adaptation. The paper should clarify whether the learned latent space is interpretable and how it relates to physical parameters of the imaging system.

2, The proposed M2LNet, along with the baseline methods, is evaluated on the authors' proprietary datasets rather than on publicly available datasets, making it difficult to assess the fairness and generalizability of the results. While one dataset is claimed to be publicly available, the paper does not provide sufficient detail about the dataset's characteristics, such as the diversity of scenes, noise levels, and the range of PSF variations. This lack of transparency makes it difficult to compare the results with other methods and to determine the practical applicability of the proposed approach. The absence of a comprehensive evaluation on well-established public datasets is a significant limitation, hindering the reproducibility and validation of the reported performance gains.

### Questions
1, The proposed method relies on two assumptions: that the M2E follows a Gaussian distribution, and that the distribution of pixel values in the underlying scene follows a Laplacian distribution. Providing a more detailed theoretical justification for these assumptions would be beneficial, especially for readers from different fields who may not be familiar with these choices.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of model mismatch error (M2E) in lensless imaging, which occurs due to inaccuracies in the point spread function (PSF) model. The authors propose a novel method called M2LNet that simultaneously estimates M2E and reconstructs high-resolution images from lensless measurements. The contributions of this work including: 1) Joint MAP Estimation: Formulate lensless image reconstruction as a joint Maximum a Posteriori (MAP) problem to co-estimate M2E and reconstruct the underlying scene. 2) M2E Representation (M2ER): Introduces an explicit learning model for M2E, improving robustness against PSF inaccuracies by learning both the feature (mean) and uncertainty (variance) in the latent space. 3) Multi-Stage Reconstruction Network (MSRN): Develops a multi-stage network by unfolding the MAP estimator with a learned Laplacian Scale Mixture (LSM) prior and M2E representation (M2ER), optimizing all parameters end-to-end. The extensive experiments on datasets captured by PHlatCam and FinCam prototypes demonstrate that M2LNet significantly surpasses some existing methods in terms of image quality and reconstruction accuracy.

### Strengths
1. The explicit learning of M2E with a dedicated MAP module is a novel approach that addresses the limitations of previous methods, which either ignored M2E or treated it as a noise correction step.
2. The paper builds upon a solid theoretical framework, providing a clear mathematical formulation of the lensless imaging problem and the proposed solutions.
3. The paper is well-structured and organized, presenting the problem, methodology, experiments, and results in a clear and logical manner.

### Weaknesses
1. It is good to focus on the M2E, but I think the design of the M2ER is simple.
2. While the paper compares M2LNet with some existing state-of-the-art methods, the comparison is not sufficient, some recent works are not presented and compared in this work.
3. Some of the ablation study of the work is confusing.

### Questions
1. It is good to focus on the M2E in lensless imaging, but I think the design of the reconstruction model is simple.
2. what is the differences of ‘TFR + MSRN + M2ER’ and ‘Full model’ in your ablation study in Table. 3? There is a significant improvement in the reconstruction results in both PSNR and SSIM, which is not presented clearly.
3.In the ablation study on loss function in Table.3, the ‘Lmse + 1.0 * Lp’ presents the best performance, why do you choose to use ‘0.01 * Lp ’in the following tests.
4. The color highlight in Table.1 is confusing. 
5.Some most recent related works are not mentioned and compared in the paper, like the following References, it would be better to compare all the SOTA works to demonstrate the performance of the proposed method.

R1: Lensless Imaging Based on Dual-Input Physics-Driven Neural Network[J], Advanced Photonics Research, 5, 11, 2024.
R2: DeepLIR: Attention-Based Approach for Mask-Based Lensless Image Reconstruction[C], Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2024: 431-439.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on  inaccuracy in lensless imaging reconstruction caused by mismatched point spread function (PSF) models. It introduces a unrolling model, using a Maximum a Posteriori (MAP) framework with a Laplacian Scale Mixture (LSM) prior. The method iteratively estimates both the image and model mismatch error (M2E) by updating reconstructions (x^{k+1}) based on prior estimates (x^k, A^k), and obtaining the parameters (A^{k+1}) through the M2ER (model mismatch error representation) model. Experimental results demonstrate that this approach improves reconstruction quality compared to state-of-the-art methods.

### Strengths
1. The presentation is very clean and straightforward.
2. The equations and variables are well defined, helping in understanding the methodology.
3. Combining the unrolling method with traditional statistical model-based denoising and deep learning-based denoising is a promising approach to improve reconstruction accuracy.
4. The dataset is large, and the comparison methods are well-chosen, leading reliability to the results.

### Weaknesses
The main concern for me is about the problem setting, especially in Eq. (5), (7), and (8). See my questions below.

 1. The equation (5) is equivalent to p(A, x | x^) p(x^) = p(A, x, x^) = p(x | A, x^)  p(A | x^)  p(x^). Applying the log-likelihood, we get log p(A, x | x^) + log p(x^) = log p(x | A, x^) + log p(A | x^) + log p(x^) = log p(x | A, x^) + log p(A | x^) + log p(Ax + ksi). How does this lead to equation (6)? I don’t think adding log p(x) makes it proportional to log p(A, x | x^). Could you provide a step-by-step derivation of Equation (6) from Equation (5) and explain why introducing log p(x) supports your proportionality claim?

 2. From equation (7) to (8a), why is A* = arg max_A log p(A | x^) + log p(x^ | A, x) equivalent to (8a)? I think you treat the second term, log p(x^ | A, x), as a constant, but in general, it isn’t. Do you make any assumptions in this step? If so, could you justify the reasonableness of this assumption?

 3. Similarly, from equation (7) to (8b), you remove the term log p(A | x^). However, log p(A | x^) = log p(A | Ax + ksi). Why is this term always considered a constant when handle x?

 4. For equation (16), I think this is a discrete model for w_i. Why do you use an integral here? Is this intended to represent a continuous approximation of the discrete model?

 5. I am also curious how much adding L_p in the loss function can improve accuracy.

 6. Will your model extend to Poisson or negative binomial noise for low-light images?

### Questions
1. The equation (5) is equivalent to p(A, x | x^) p(x^) = p(A, x, x^) = p(x | A, x^)  p(A | x^)  p(x^). Applying the log-likelihood, we get log p(A, x | x^) + log p(x^) = log p(x | A, x^) + log p(A | x^) + log p(x^) = log p(x | A, x^) + log p(A | x^) + log p(Ax + ksi). How does this lead to equation (6)? I don’t think adding log p(x) makes it proportional to log p(A, x | x^). Could you provide a step-by-step derivation of Equation (6) from Equation (5) and explain why introducing log p(x) supports your proportionality claim?

2. From equation (7) to (8a), why is A* = arg max_A log p(A | x^) + log p(x^ | A, x) equivalent to (8a)? I think you treat the second term, log p(x^ | A, x), as a constant, but in general, it isn’t. Do you make any assumptions in this step? If so, could you justify the reasonableness of this assumption?

3. Similarly, from equation (7) to (8b), you remove the term log p(A | x^). However, log p(A | x^) = log p(A | Ax + ksi). Why is this term always considered a constant when handle x?

4. For equation (16), I think this is a discrete model for w_i. Why do you use an integral here? Is this intended to represent a continuous approximation of the discrete model?

5. I am also curious how much adding L_p in the loss function can improve accuracy.

6. Will your model extend to Poisson or negative binomial noise for low-light images?

### Soundness
3

### Presentation
3

### Contribution
2
