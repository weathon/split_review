# Self-supervision Meets Bootstrap Estimation: New Paradigm for Unsupervised Reconstruction with Uncertainty Quantification

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Deep learning-based self-supervised reconstruction (SSR) plays a vital role in diverse domains, including unsupervisedly reconstructing magnetic resonance imaging (MRI). Current powerful methodologies for self-supervised MRI reconstruction usually rely on capturing the relationships between different views or transformations of the same data such as serving as inputs and labels respectively, which show notable influence from analogous approaches in computer vision. Although yielding somewhat promising results, their designs are often heuristic without deep insights into reconstructed object characteristics, and the analytical and mathematical principles of such methods are not expressive. This paper addresses these issues by a novel SSR paradigm, BootRec, that not only provides a theoretical foundation for self-supervised reconstruction but also facilitates the development of downstream algorithms. Self-supervised MRI reconstruction is modeled as error-oriented parameter estimation - Bootstrap estimation for SSR (BootRec). In BootRec, we demonstrate the mathematical equivalence between bootstrapping in a sample set and the commonly used re-undersampling operation for SSR. This insight is further incorporated into designing models to estimate the variances and errors of MRI SSR results without accessing labeled data. The error estimation serves as the loss function for unsupervisedly training the models. Empirical experiments show that our new paradigm BootRec enables effective uncertainty quantification and advanced MRI reconstruction performance against other zero-shot methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel self-supervised approach for MRI reconstruction using bootstrap sampling. The method involves re-subsampling the undersampled k-space, reconstructing each resampled measurement, and formulating a loss function based on the reconstruction of the original measurement and the mean squared error of the resampled reconstruction.

### Strengths
The approach presents an innovative concept and demonstrates commendable performance. Notably, the training loss trajectory aligns consistently with that of training on self-supervised MSE, as shown in Figure 6.

### Weaknesses
The primary challenge with this paper lies in its presentation, making it difficult for readers to follow. Some issues include:
- Excessive Equations and Notations: The paper is overwhelmed with equations and notations, overshadowing the fundamental concept. The core idea appears to be sampling, but the multitude of equations adds unnecessary complexity without aiding comprehension. For instance, the use of multiple summation and product symbols within single equations, such as in the loss function, makes it difficult to parse the core operations. The paper would benefit from simplifying these expressions, perhaps by introducing intermediate variables or using more descriptive notation.
- Confusing Notations: Notations like the two 'U's in Equation (6) are ambiguous and visually similar, leading to confusion and hindering understanding. Specifically, the use of the same letter 'U' to represent both a random variable and a vector without clear differentiation makes it hard to track the mathematical operations. This lack of clarity extends to other symbols, making it challenging to discern the purpose of each variable within the equations.
- Unexplained Figures: Figures, such as Figure 4, lack detailed explanations, leaving readers without essential context to interpret the visual data. For example, the axes and the specific data points in Figure 4 are not clearly explained, making it difficult to understand what the figure is intended to demonstrate. The lack of a detailed caption further exacerbates this issue.
- Lack of Explaining Prior Works: Assumptions about the reader's familiarity with existing work, especially (Yaman, 2022)'s zero-slot learning, create gaps in understanding. The absence of pertinent details hampers comprehension. The paper does not adequately explain the relevance of zero-shot learning to the proposed method, leaving the reader to infer the connection, which is not ideal for a clear and self-contained presentation.

Another concerns the authors might take into consider for improving this paper:
- Unclear Significance of Variance: The paper lacks clarification on why the variance (uncertainty) of bootstrap resampled reconstruction is important. Address the relevance of this aspect, especially in comparison to uncertainty quantification for raw measurement reconstruction.
- Theoretical Foundation: While the paper claims to provide a "theoretical foundation," it predominantly relies on equations without substantive theoretical analysis. A more comprehensive exploration of the theoretical underpinnings is essential to substantiate this claim.

### Questions
See the weakness part.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper titled: Self-supervision Meets BOOTSTRAP Estimation: New Paradigm for Unsupervised Reconstruction with Uncertainty quantification proposes a novel SSR methods with BootStraping for MRI reconstruction, with the ability of uncertainty estimation and quantification.

### Strengths
1. Uncertainty quantification for MRI reconstruction is an open problem, based on my knowledge, I think this paper is the first one to quantify MRI uncertainty in an unsupervised or self-supervised manner from under-sampled MRI.

2. I like the idea of using BootStrap to resample the undersampling pattern, and from the Figure 7 plots, the results outperform SSDU and other SOTAs in terms of quantitative metrics.

3. The algorithm is well-written and delivered.

### Weaknesses
1. I think one of my biggest concerns is how the proposed method compared with other existing approaches for uncertainty quantification, there have been a wide range of works on this topic, they are either sampling based [Uncertainty Quantification in Deep MRI Reconstruction] or directly estimation the absolute residual error [Rigorous Uncertainty Estimation for MRI Reconstruction], this paper lack the comparisons with other approaches, please discuss/cite them. Specifically, the paper should compare against methods that explicitly model uncertainty, not just methods that produce a reconstruction; for example, Bayesian neural networks or methods that estimate aleatoric and epistemic uncertainty separately. The current comparison is insufficient to demonstrate the advantage of the proposed method in terms of uncertainty quantification.

2. For the reconstruction results, the authors only showed an PSNR and SSIM plot (Figure 7) without any visual results to inspect on the details, the only visual results is Figure 5, which also doesn't deliver much information. I think this paper demonstrates a proof-of-concept, but lack evaluations. The lack of visual results makes it difficult to assess the practical utility of the method. It is important to show not just quantitative metrics, but also visual examples of the reconstructions, including error maps, to understand where the method succeeds and fails.

3. What is the purpose of estimating MSE, this can be generalized to an open question, how to use the uncertainty estimation results for diagnosis, I can imagine it would be useful if we compute uncertainty in latent space, but could you elaborate on how to use uncertainty estimation for down-stream task? The paper needs to clarify how the estimated MSE relates to actual uncertainty in the reconstruction and how this uncertainty can be used in downstream tasks such as diagnosis or clinical decision-making. Simply estimating MSE is not sufficient; the paper needs to articulate the practical value of this estimation.

### Questions
1. How to quantitatively evaluate the quality of your uncertainty estimation results.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper interprets a popular self-supervised MRI reconstruction approach: self-training with secondary undersampling [1,2], as bootstrapping. The repeated secondary undersamplings are modeled as a virtual sample set, and the secondary sampling masks are aggregated as a sampling distribution for bootstrapping. The authors then propose to use the bootstrapped error to estimate the true underlying reconstruction error. Qualitative results are shown on public MRI datasets and some correlations between estimated errors and the true underlying errors can be observed.

### Strengths
The problem of estimating the error in MRI reconstruction is of practical value. It links to the trustworthiness of deep learning based image reconstruction. 
 
The authors link the secondary undersampling technique [1,2] to bootstrapping. This is a very interesting interpretation. 

Correlations between estimated reconstruction errors and the true underlying reconstruction errors can be observed.

### Weaknesses
An important prior work [3] for modeling aleatoric and epidemic uncertainties for deep learning MRI reconstruction is missing. 

The detailed approach and its mathematical framework of the prior works: self-supervised MRI reconstruction using self-training on secondary undersampling [1,2], need to be introduced in Sec. 2, as they are the basis for the entire manuscript. 

The manuscript in general lacks clarity: it is difficult to find the key arguments and the core take-home information from the abstract and the introduction. 

The writing style is also sloppy with key concepts arbitrarily named, used, but left unexplained. E.g., the first paragraph of Sec. 3.2: the narration is quite casual. Also, what does the paragraph under Eq. 8 mean? What does the starting paragraph in Sec. 4.3 mean? This sloppy writing may make readers who are not familiar with secondary undersampling based MRI reconstruction, extremely difficult to follow. The writing does not meet the high standards of ICLR. 

Despite the interesting interpretation of bootstrapping, the manuscript does not make significant theoretical/methodological breakthroughs beyond the existing secondary undersampling based MRI reconstruction approaches [1,2], not to mention that secondary undersampling is not the only approach for unsupervised/zero-shot MRI reconstruction and/or error estimation. 

Sec. 5.2: There is a lack of quantitative evaluation of the quality of error estimations. The authors also fail to compare with the well-established Bayesian deep learning based image reconstruction [3]. Notebly, unlike the proposed approach, Bayesian deep learning allows to explicitly separate aleatoric uncertainty and epistemic uncertainty. 



### Questions
Is the most fundamental assumption mentioned at the starting of the manuscript: modeling U as independent Bernoulli’s, unrealistic? In practice sampling patterns are subjects to the physical constraints of the gradient system of the scanners, and the resultant sampling patterns (both original and secondary) are by no means independent.  

The authors are suggested to improve the clarity of writings and illustrations.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel self-supervised MRI reconstruction paradigm in which the reconstruction process is modeled as parameter estimation, leveraging the idea of bootstrapping. To mitigate the high variance incurred by randomly generating a sample set, this paper proposes to get the distribution of the observations by mapping the observation to a virtual sample set. The authors conduct both theoretical and empirical analyses for the proposed method.

### Strengths
1. The idea is novel and interesting. 
2. The demonstrated equivalence between the sample set bootstrapping and the re-undersampling is inspiring. 
3. The results are promising to an extent. 
4. The paper is well written.

### Weaknesses
1. It is highly expected that the paper includes a comparison with other typical methods for MRI reconstruction, such as [1] and [2]. Although the authors argue that deep learning models may suffer from unreliability, as the fast growing of vision transformers, their appealing performance should not be ignored. Thus, a comparison with such methods will make the results more convincing. Although these methods may not focus on zero-shot, the testing performance can still be compared. Specifically, the paper should benchmark against methods like those proposed in [1], which introduces a self-supervised learning framework for MRI reconstruction, and [2], which presents a deep learning approach for image reconstruction. These comparisons are crucial to contextualize the performance of the proposed method within the current state-of-the-art, especially given the rapid advancements in transformer-based models that have shown impressive results in various image reconstruction tasks.

2. I think the paper lacks a discussion of the differentiability of the aggregation function h. Although the classical MSE loss is differentiable, due to the use of the aggregation function in the MSE which is adopted to train a model, the authors are highly encouraged to discuss the differentiability of the aggregation function. The aggregation function plays a critical role in the proposed method, and its differentiability directly impacts the feasibility of gradient-based optimization. A thorough analysis of how the aggregation function affects the gradient flow during backpropagation is necessary to ensure the stability and convergence of the training process.

### Questions
1. Is the uncertainty in this paper partially from the resampling operation due to the use of bootstrap? More insights will be helpful. 

2. Although reconstruction is an important topic in MRI, are there any other reasons that make the proposed method tie to MRI reconstruction? In other words, whether the proposed method is suitable for potential reconstruction tasks in natural image domains?

3. Is that possible to use the Monte Carlo method in this work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
