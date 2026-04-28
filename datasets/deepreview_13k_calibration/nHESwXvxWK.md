# Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems.

- Decision: Accept
- Avg Score: 4.00
- Scores: 1, 8, 1, 6

## Abstract
Ill-posed linear inverse problems arise frequently in various applications, from computational photography to medical imaging.
A recent line of research exploits Bayesian inference with informative priors to handle the ill-posedness of such problems.
Amongst such priors, score-based generative models (SGM) have recently been successfully applied to several different inverse problems.
In this study, we exploit the particular structure of the prior defined by the SGM to define a sequence of intermediate linear inverse problems. As the noise level decreases, the posteriors of these inverse problems get closer to the target posterior of the original inverse problem. 
To sample from this sequence of posteriors, we propose the use of Sequential Monte Carlo (SMC) methods.
The proposed algorithm, \algo, is shown to be theoretically grounded and we provide numerical simulations showing that it outperforms competing baselines when dealing with ill-posed inverse problems in a Bayesian setting.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a method for addressing ill-posed inverse problems by employing a diffusion-based neural network model guided by Monte Carlo sampling. They refer to their approach as the MCGDiff (Monte Carlo Guided Diffusion) algorithm. Their algorithm is specifically applied to Score-based Generative Models (SGMs) and is used for various image-related tasks, including inpainting, super-resolution, deblurring, and colorization. To model prior distributions, the authors utilize Gaussian Mixed Models (GMM) and Funnel Mixture Models (FMM).

### Strengths
A substantial portion of the research paper is devoted to providing a comprehensive background on the use of diffusion models for solving ill-posed inverse problems. Additionally, the paper includes detailed mathematical proofs regarding the algorithm's performance, covering both noiseless and noisy cases. This comprehensive coverage enhances the clarity and rigor of the research.

The authors' consideration of the broader applicability of their work beyond their experimental investigation of image data is commendable. It highlights the potential relevance and impact of their findings in a wider context of inverse problems.

The comparative results presented in the image context are particularly noteworthy. The research demonstrates impressive performance, especially in the way the generated posterior sampling distributions align with the exact ones. This underscores the effectiveness and accuracy of the proposed approach when compared to competing methods.

### Weaknesses
It would have been intriguing to explore the performance of the MCGDiff algorithm on non-image data. While the research focuses on image-related tasks, extending the investigation to other data types would provide a broader perspective on the algorithm's applicability and effectiveness across various domains. Specifically, the current evaluation lacks a rigorous analysis of how the choice of prior distribution (GMM or FMM) impacts the quality of the results across different data modalities. The paper would benefit from a more detailed discussion on the sensitivity of the algorithm to the hyperparameters of these prior models, and how these choices might need to be adapted for non-image data. Furthermore, the computational cost associated with the Monte Carlo sampling, especially when applied to high-dimensional non-image data, is not thoroughly addressed. An analysis of the scalability of the method, including the computational resources needed for different problem sizes, would be valuable.

### Questions
1. Are there any plans to release your code for the MCGDiff algorithm to facilitate further research and practical applications in the broader community?

2. Have you explored the application of the MCGDiff algorithm in addressing inverse problems beyond image-related tasks, and if so, could you share any insights into its performance and adaptability in those contexts?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article propose a sequential Monte-Carlo method to solve linear inverse problems such as deblurring, super-resolution or inpainting with score-based generative priors (aka generative diffusion models) through the design of an efficient sampler.  The method is embodied into their proposed MCGdiff algorithm, which is proved to be sampling conditionally in a consistent manner from the diffusion posteriors. They evaluate the performance of their algorithm on various numerical simulation, demonstrating state of the art results on several imaging inverse problem applications.

### Strengths
The paper is dense but accessible and sufficiently well written, and although terse at time, thorough and complete. It is also well illustrated althought Fig. 1 is more puzzling than useful. The theory is well-developed, complete with all the proofs. 

In terms of results,  MCGdiff seems to provide very good quality samples in all illustrated problems in comparison with other diffusion-based models. It interesting to see it perform well on difficult cases.

Code is available.

### Weaknesses
The paper is detailed and the appendices can be hard to read. 
The authors don't really solve inverse problems in the traditional sense. They generate realistic samples learned from a distribution that are consistent with the observations. While this sounds exactly like solving inverse problems, the resulting images, although better than existing methods and very sharp and detailed, only resemble the ground truth. I mention this because these types of methods cannot yet be used in sensitive contexts like medical imaging or science in general.
There is a lack of control and interpretability on the generated images, as with all the current diffusion methods.
The code issues have not been addressed. From looking at the source, the diffusion code seems to be based on DDPM, which is not acknowledged in the main text or appendices. Speed issues have not been mentioned.
The bibliography is excellent except for the first paragraph of the introduction. Linear inverse problems as described have been studied mathematically for a very long time (Fredholm, etc) and in computer vision since the late 1980s at least. Perhaps the bibliography should mention this.

### Questions
- How could the results be made more interpretable or controllable.
- The experiments on GM seem to indicate that MCGdiff does sample from he posterior distribution but not necessarily in a "thorough manner" see Fig. 5 and 6 ; how can this be better handled?
- How do deal with noise present in the training dataset ?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A method is proposed to solve linear inverse problems using score-based generative models (SGM), i.e. denoising diffusion models, in a Bayesian manner using Sequential Monte Carlo (SMC).  Such statistical approaches allow one to sample from the posterior, or an approximation of it, which facilitates uncertainty quantificaiton.  Experiments are presented on simple distributions where the posterior is known, where validation can be performed.  Further experiments are then presented on real images to demonstrate practical application, although underlying true posteriors for validation are not available in these settings.  Anonymized code is made available.

### Strengths
Solving inverse problems using SGMs is a topical area of research at present, with a number of recent papers.  The key problem is to faithfully sample from the underlying posterior distribution.  It is not straightforward to integrate a likelihood into SGMs since it is difficult to consider a closed-form for the likelihood due to the dependence on time and thus noise level.  Existing approaches address this issue by various approximations (e.g. data consistency projections) but as far as I'm aware, and as the authors also state, no existing method fully solves this problem.  The authors claim they present the first provably consistent algorithm for condional sampling from the target posterior.  While I haven't checked all of the mathematical details I believe this is indeed the case.  Numerical experiments indeed confirm for the simple distributions that the sliced Wasserstein distance between the proposed method and the posterior recovered either analytically or by NUTS sampling is considerably smaller than for other SGM approaches for solving inverse problems.

### Weaknesses
The authors comment that standard image metrics, e.g. FID, are not suitable for evaluating Bayesian reconstruction methods for solving inverse problems.  Results from a handful of examples of inverse imaging problems are presented, which all look very compelling.  Nevertheless, it would be useful to summarise performance over a larger set of test images, if possible. While the visual results are promising, the lack of a quantitative summary across a broader dataset makes it difficult to assess the robustness and generalizability of the proposed method in practical scenarios. The absence of such metrics leaves open the question of how the method would perform under varying conditions or with different types of image data. Specifically, it is unclear how the method's performance might degrade with increasing noise levels or with more complex image structures, which are common challenges in real-world inverse problems.

### Questions
Could the authors propose a metric to summarise performance over a large set of test images (see discussion in Weaknesses)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed an interesting method that combines particle filtering with diffusion model, trying to mitigate the issue of ill-posed inverse problem. The idea is novel and the demonstration of the proposed algorithm looks good in two dimensional illustrations, but the results in image datasets doesn't give clear distinctions from other existing methods.

### Strengths
1. Interesting novel idea to integrate particle filtering method into the exploration of posterior under the diffusion model framework. 

2. Theoretical work looks solid and convincing.

### Weaknesses
1. It seems the contribution point 3 is mainly a support for the first two points, hardly it can be classified as an independent contribution. 

2. A pseudo-code or diagram describing the idea of this method would make it much easier to be interpreted

3. This method should be pretty slow as both diffusion model and particle filter are computationally heavy ones. Would be good to clearly state the limitation and also report the runtime etc.

4. It seems very difficult to conclude that the proposed method outperforms the others in image dataset, is there any other ways to quantitatively  demonstrate the advantage of the proposed method?

5. Does the intrinsic degeneracy issue from particle filter affect the stability and performance of the proposed method?

### Questions
1. It seems very difficult to conclude that the proposed method outperforms the others in image dataset, is there any other ways to quantitatively  demonstrate the advantage of the proposed method?

2. Does the intrinsic degeneracy issue from particle filter affect the stability and performance of the proposed method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
