# Post-Nonlinear Causal Relationship with Finite Samples: A Maximal Correlation Perspective

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Bivariate causal discovery aims to determine the causal relationship between two random variables from passive observational data (as intervention is not affordable in many scientific fields), which is considered fundamental and challenging. Designing algorithms based on the post-nonlinear (PNL) model has aroused much attention for its generality. However, the state-of-the-art (SOTA) PNL-based algorithms involve highly non-convex objectives due to the use of neural networks and non-convex losses, thus optimizing such objectives is often time-consuming and unable to produce meaningful solutions with finite samples. In this paper, we propose a novel method that incorporates maximal correlation into the PNL model learning (short as MC-PNL) such that the underlying nonlinearities can be accurately recovered. Owing to the benign structure of our objective function, when modeling the nonlinearities with linear combinations of random Fourier features, the target optimization problem can be solved rather efficiently and rapidly via the block coordinate descent. We also compare the MC-PNL with SOTA methods on the downstream synthetic and real causal discovery tasks to show its superiority in time and accuracy. Our code is available at https://anonymous.4open.science/r/MC-PNL-3C09/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers bivariate causal discovery without confounders. Under the assumption that the true model follows the post-nonlinear (PNL) model, prior work does causal discovery by learning the functions f_1,f_2 and then using some dependence measure to compare the dependence between the residuals and the input under both hypotheses. This paper proposes an alternate two-stage method, where the first stage learns the functions using a soft-version of HGR maximal correlation regularized by a dependency measure (Renyi, 1959) and the second stage is an independence test between the residual and the input. The dependency measure regularization is motivated by pointing out the con of maximal correlation that it doesn't provide usable residuals for the downstream independence test. Experimental results show that the proposed method is competitive w.r.t existing methods.

### Strengths
Bivariate causal discovery is an important, fundamental problem in causal inference. This paper advances the literature by providing an algorithm that uses a variant of maximal correlation to learn nonlinear functions of the PNL model. A major contribution of this paper is a systematic study of how to use maximal correlation based methods for causal discovery. Experimental results seem comprehensive in the sense that they cover a wide variety of datasets both simulated and real, barring a few concerns that I elaborate in the following section.

### Weaknesses
1) The writing can be improved greatly. Few assertions are vague (e.g. "HSIC can get easily stuck at "meaningless" local minima", IGCI cannot provide "transparent and interpretable transformations") and undefined in the main paper (e.g. randomized dependence coefficient is not defined clearly despite it being used in the proposed method).
2) It was also not clear to me how a dependence measure, HGR correlation, was used to motivate learning nonlinear functions; after all it is irrelevant whether X and Y are dependent.
3) The main contributions seem overstated. Among a host of different causal disvoery methods compared in Table 2, the proposed method MC-PNL is faster compared to only AB-PNL by 300x, while there exists a competitive method in IGCI that is 60x faster than the proposed method. Overall, the experimental results don't seem to give the impression that MC-PNL outperforms other benchmarks. Furthermore, the abstract and introduction do not clearly state that the comparison is primarily with other PNL-based methods, leading to an overstatement of the method's general contribution.
4) While one of the disadvantages of the PNL algorithms is claimed to be the optimization issue, thus motivating the RFF parametrization and linear HSIC kernel, neither is the experimental performance of this variant discussed, nor is its theoretical properties. MC-PNL still uses a gradient-based algorithm for the universal kernel and banded loss regularizer.


### Questions
1) The authors repeatedly use the word "meaningful" (pg 5, under eq 9, pg 6, first para in 4.1) while criticizing existing methods without providing much explanation as to what is "meaningful". While the usage in pg 5 is backed by the observation that residuals can be matched to arbitrary noise profiles, other usages are unclear. These assertions seem important but without knowing the meaning it's unclear what the criticism means.
2) Is it supposed to be < -\delta in Line 3 in Algorithm 2? 
3) Is there any ablation study done to determine the parameters of the RFF?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a maximal correlation-based method for discovering causal relationships under the post-nonlinear causal model. Some theoretical guarantees are given. A few synthetic experiments are conducted as proof of concept. A simple real data analysis is also performed, comparing the proposed method against several existing benchmarks.

### Strengths
Overall, the paper is clearly written, with sufficient details on the motivation, theoretical results, and experiments.

The paper is trying to address an important question in causal inference, possibly drawing attention from fields such as causal inference, robust machine learning, and computational biology.

In general, causal discovery algorithms are difficult to scale up. However, this paper also discusses how to convexify the proposed algorithm so one can, at least in principle, solve the optimization problem to recover the final causal structure.

### Weaknesses
The numerical experiments look very simple (at least to me), and hence not entirely convincing about the use of overparameterized neural networks.

The optimization of over-parameterized neural nets itself, together with the "implicit regularization" effect of gradient-based methods, is a big problem in practice. I would hope that the authors discuss this in a remark.

When $f_{1}$ is a linear function in some basis of $X$, say $\beta^{\top} \phi (X)$, the proposed model is reduced to the single-index model. For single-index models, the identifiability of the parameter $\beta$ will be problematic, and often one assumes $\beta$ to be on the unit sphere. Is there a similar concern when one expands the modeling of $f_{1}$ to a purely nonlinear one?

I do not have much else to say about the "weaknesses" but I do want to mention that in the Questions section, I list several questions and comments on the paper.

### Questions
1. Why use maximal correlation? There are obviously many "nonparametric correlations" at our disposal, e.g. d-corr, maximal information coefficients (by Reshef et al.), and many others.

2. Is there any connection between the proposed method (or any other related method) and canonical correlation analysis (CCA)? From the formulation of the optimization problem alone, they look quite similar.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the practical problem of the post-nonlinear model that focuses on the over-fitting issue and optimization issue in solving the non-linear function of PNL. The authors discuss several drawbacks of the independent test method, e.g., HSIC, and show that the randomized dependence coefficient (RDC) has the advantage in measuring the non-linear dependence, based on a set of simulation experiments. Moreover, The authors propose a novel method that incorporates maximal correlation into the PNL model learning (short as MC-PNL) such that the underlying nonlinearities can be accurately recovered. The experiment results verify the ability of non-linear function fitting of the proposed method and show that MC-PNL outperforms the baselines in causal discovery application.

### Strengths
1. The paper is well-written and easy to follow.

2. The authors gave a good overview on the related literature.

3. The authors provide a novel framework to deal with PNL learning, in which the maximal correlation constraints may be beneficial to fit the non-linear function of the PNL model.

### Weaknesses
1. There are extra assumptions to ensure the correctness of Lemma 4, such as "composition of PNL functions and un-mixing nonlinearities are linear" (provided in Proof Sec. F), which should be incorporated into the claim of Lemma 4. Specifically, the assumption that the composition of the PNL functions and the unmixing nonlinearities results in a linear function is a strong condition that limits the applicability of the lemma. This assumption needs to be explicitly stated in the lemma itself, not just in the proof, to ensure clarity and to allow readers to properly assess the scope of the theoretical result. The current presentation makes it seem more general than it actually is.


2. The contribution of this paper is a proposed learning framework for PNL with some correctness analysis. My main concern is whether the theoretical contribution is insufficient due to the identification bound of PNL has not improved. While the proposed method offers a practical approach, the lack of improvement in the fundamental identifiability bound raises questions about the significance of the theoretical contribution. The paper should more clearly articulate the limitations of the current identifiability results and discuss the potential for future work to address these limitations. The current discussion focuses more on the practical aspects without fully acknowledging the theoretical constraints.


3. In the "NONLINEAR FUNCTION FITTING" experiment, there are only two group generation mechanisms are used. More results with more types of non-linear functions should be provided if possible. The current experiments are limited in scope and do not fully demonstrate the robustness of the proposed method across a diverse range of nonlinear functions. The use of only two generation mechanisms may not be sufficient to generalize the findings to other types of nonlinearities. It is important to include more complex and varied nonlinear functions to provide a more comprehensive evaluation of the proposed method's capabilities.

### Questions
Have you applied this method to real-world data?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
