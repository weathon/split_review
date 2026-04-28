# MissDiff: Training Diffusion Models on Tabular Data with Missing Values

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
The diffusion model has shown remarkable performance in modeling data distributions and synthesizing data. However, the vanilla diffusion model requires complete or fully observed data for training. Incomplete data is a common issue in various real-world applications, including healthcare and finance, particularly when dealing with tabular datasets. This work presents a unified and principled diffusion-based framework for learning from data with missing values under various missing mechanisms. We first observe that the widely adopted ``impute-then-generate'' pipeline may lead to a biased learning objective. Then we propose to mask the regression loss of Denoising Score Matching in the training phase. We prove the proposed method is consistent in learning the score of data distributions, and the proposed training objective serves as an upper bound for the negative likelihood in certain cases. 
The proposed framework is evaluated on multiple tabular datasets using realistic and efficacious metrics and is demonstrated to outperform state-of-the-art diffusion model on tabular data with ``impute-then-generate'' pipeline by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors propose a diffusion generative model that learns the complete score function from missing observations. The proposed method not only impute missing components, but also generate new samples from the data distribution in "one-shot". The proposed method is justified through minimizing a likelihood upper bound of the observed data. Experiments demonstrate that the proposed method outperforms the state-of-the-art methods on tabular datasets.

### Strengths
The propose method is novel to my best knowledge. 

It has nice intuition and theoretical justifications (minimizing an upper bound of  KL[p_0|p_theta])

Indeed, some existing methods do have to perform two stage inference to generate new samples. The one-short approach is not only algorithmically simpler but also avoids biases introduced in imputation step. 

The proposed method avoids unstable adversarial training which is what many existing works (such as Yoon et al., 2018 and Li et al., 2019) rely on.

### Weaknesses
This paper lacks a proper motivation for generating new samples in addition to imputing missing data. In the second paragraph in the Introduction, there is one sentence on "deep generative models can be used to... enhance the performance of image classification tasks". However, I suggest authors discuss why imputation alone is not enough, and why additional samples need to be generated and back it up with specific examples. 

The authors do not explain why other generator based imputation algorithm, such as GAIN or misGAN, could not be straightforwardly extended to generate new samples while imputing missing values. Both GAIN and misGAN train a generator G which outputs a complete sample. The generator is then "tweaked" to impute missing data (similar to the tweaking authors have done in line 9, algorithm 2). If they can be straightforwardly modified to generate new images, I think authors should also compare them in the experiments or at least acknowledge them as earlier unified imputation/generation algorithms. 

The idea of misGAN is also very similar to the proposed algorithm. On the high level, it tries to generate samples looks like the observed data  after masking. It trains a generator by minimizing a divergence between observed data (p_obs) and generated samples (p_theta). The KL divergence between p_obs and p_theta is the same as the cross entropy in Theorem 3.3 up to a constant. I would appreciate discussions on the similarities and differences between the proposed method and misGAN.
   - There is another work that similarly maximizes the observed likelihood using normalizing flow:  https://arxiv.org/pdf/2003.12628 which I think could also be straightforwardly extended to generating new samples.

1. Why does the imputation work? 

Algorithm 2 describes the imputation algorithm which is similar to the reverse process described in eq 2 using a **joint score model**. However, the training process only add noise to the observed coordinates, and the unobserved coordinates does not contribute to the loss (due to "odot M"), so the learned score model seems to be a "marginal score".

This is different from training a conditional score model then using it to sample from a conditional probability distribution. What is the justification of authors' imputation process? 

Could authors please write down: 

What is the optimal solution of equation 5? what is the corresponding forward process and backward process that give rise to the imputation algorithm? 

2. equation (12) in Li et al., 2019 defines the imputer of misGAN. I can just set m = [0, 0, 0... ] in (12) to generate new sample, right?

3. The same question above. Equation (2) and (3) in Yoon et al., 2018 defines the imputer of GAIN. Can I just set m = [0, 0, 0, ...] to generate new sample straightforwardly from GAIN? 

4. If yes to question 2 and 3 , what is the unique advantage of the proposed unified framework for imputing/generating samples comparing to misGAN and GAIN?

### Questions
1. Why does the imputation work? 

Algorithm 2 describes the imputation algorithm which is similar to the reverse process described in eq 2 using a **joint score model**. However, the training process only add noise to the observed coordinates, and the unobserved coordinates does not contribute to the loss (due to "odot M"), so the learned score model seems to be a "marginal score".

This is different from training a conditional score model then using it to sample from a conditional probability distribution. What is the justification of authors' imputation process? 

Could authors please write down: 

What is the optimal solution of equation 5? what is the corresponding forward process and backward process that give rise to the imputation algorithm? 

2. equation (12) in Li et al., 2019 defines the imputer of misGAN. I can just set m = [0, 0, 0... ] in (12) to generate new sample, right?

3. The same question above. Equation (2) and (3) in Yoon et al., 2018 defines the imputer of GAIN. Can I just set m = [0, 0, 0, ...] to generate new sample straightforwardly from GAIN? 

4. If yes to question 2 and 3 , what is the unique advantage of the proposed unified framework for imputing/generating samples comparing to misGAN and GAIN?

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
3

### Summary
The authors present MissDiff, a diffusion based model to handle datasets with missing data. In addition to the generation task, it can also impute missing values.  Theoretical results is provided showing the connection between the training objective of MissDiff and the maximum likelihood objective of observed data. Experiments applied on multiple tabular datasets demonstrate its usefulness.

### Strengths
Strengths: 
1. The paper is well-written and motivated. 
2. Experimental results demonstrate MissDiff's performance advantages over existing approaches.
3. Authors also provide promising simulation results.

### Weaknesses
Weakness
1.  The paper's theoretical claims appear overstated, particularly regarding its potential as a "general framework" for handling incomplete data. Author claim "our method and theoretical guarantees aim to provide a general framework for learning on incomplete data and generate complete data."
Missing data assumptions are crucial for statistical efficiency.  And theoretical results presented in the paper ignoring these observations. Ignoring observations with missing elements may lead to invalid inference (imputation) and loss of statistical efficiency. As a result, MissDiff might have better experimental results and can't derive the identifiability result.
My questions are: 
- Could authors clarify how do the theoretical guarantees change under different missing data mechanisms (e.g. MCAR, MAR, MNAR)?
It seems to me MissDiff is a general imputation framework, what's the strong assumption under the hood? 
- Can any connections be built between (partial) identifiability and diffusion? If not, can authors demonstrate why the "general framework" considered in the paper is better than assuming missing data mechanisms (from a theoretical and utility perspective)? For example, when we don't have a user-defined assumption, how MissDiff can benefit users?

2. The technical novelty is limited. The algorithm is not that much different from score-based diffusion. This is a minor concern.

Overall,  W1 is my main concern. While MissDiff shows promising empirical results, its theoretical foundations and technical innovations worth more development. It would be very exciting to see an **identifiable** diffusion based models for imputation, e.g., [1], or the 

### Questions
See above, also

1. Have you considered how ignoring observations with missing elements impacts statistical efficiency and identifiability of the model? Could you provide analysis on this? 

2. Results in table 4 and appendix C2 provide some analysis on Q1. But why MICE is not compared? From my experience, MICE is a pretty strong baseline for these two scenarios (MAR and NMAR).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces *MissDiff*, a novel imputation method designed to address missing values in tabular datasets. Motivated by recent advances in using generative models like VAEs and GANs for imputation, *MissDiff* incorporates a diffusion model to handle incomplete data. Experimental results demonstrate the effectiveness of this approach, highlighting its potential to improve imputation accuracy.

### Strengths
see summary.

### Weaknesses
- The authors claim that the imputation-then-gernerate method may lead to inconsistent estimator. However, MISSDIFF the author proposed is trying to fill 0 to the observed data (the i-th element of $x_{obs}$ equals to 0, when the i-th element is missing) and use this imputed data to train the model. The only difference is that the author use a mask to relieve the effect of the loss function. As such, since MISSDIFF is also kind of  imputation-then-gernerate method, why MISSDIFF does not suffer from the issue of imputation method? Is there any intuition to explain the superiority of MISSDIFF?
- The proof of Thereom 3.2 is not convincing. In the footnote 8, page 15, the author claim the score function of gaussian product the mask with the partial-observed data can recover the one with fully observed data. However, the property does not hold for $s_{\theta}(x(t),t)$. If one impute the i-th element of x(t) by 0, then possibly every element of $s_{\theta}(x(t),t)$ will change. In that case, how to show the equation line at 773-778? Specifically, the objective function in line 773-778 involves an expectation over $p(x^{obs}_0, m)$, which implies that the score function $s_{\theta}$ is conditioned on the observed data $x^{obs}_t$. However, the proof attempts to relate this to the score function of the complete data $x_t$, which is not directly accessible during training. The justification for using the masked score matching objective to recover the complete data score is not clear, especially given that the input to the score network is the partially observed data, not the complete data.
- I did not see any challenge in extending the proposed method to scale up for addressing missing data issues in high-dimensional cases, such as image imputation. Could you provide relevant results to demonstrate the method's effectiveness in these scenarios?

### Questions
See weakness.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Motivated by missingness in tabular data, this paper proposes a way to learn diffusion models via score-matching with missing values. The paper includes experiments on both real and synthetic data demonstrating the advantages of this approach versus baseline approaches.

### Strengths
1. This paper offers a general, rigorous framework for learning diffusion models from data with missingness. I think the tabular ML subfield, and other ML subfields that face missingness will benefit from this analysis. Furthermore, future multimodal models that combine textual and tabular data will surely benefit from this framework. 

2. The paper comes with extensive experiments, for example with varying missingness rates, incomplete-columns, and incomplete rows. And the experiments evaluate not only MCAR, but also the more realistic MAR and NMAR scenarios, showing benefits for these settings as well.

### Weaknesses
1.  Missing related work: There are works that utilize the ability of gradient-boosted decision trees (GBDTs) to handle missing features in order to avoid the impute-then-generate framework. Examples include [ForestDiffusion 1, DiffPuter 2] that use diffusion modeling and [UnmaskingTrees 3] that uses autoregression modeling. In particular, it is not clear whether the diffusion modeling approaches in [1, 2] can be seen as instances of the authors' proposed framework. (Granted, I realize that [1, 2, 3] may be parallel works, and that these rely on GBDTs for missingness, which is not a very general solution. So while I think these are relevant related works, I would like to emphasize that these do not diminish the potential impact of MissDiff, which is the first to enable the leap to neural networks, which will be important for modeling textual fields, and which is the first to be rigorously shown to not rely on assumptions like MCAR.)

2.  It would be preferable to report how MissDiff performs on the imputation benchmark of [ForestDiffusion 1], for the following reasons. First, it has a larger and more diverse set of 27 datasets. Second, unlike Zheng & Charoenphakdee (2022)'s benchmark, this one shows that MissForest is better than GAIN, which is frankly more plausible. Third, without any further reimplementation work, it would enable one to compare MissDiff to the current claimed SotA diffusion [2] and autoregression [3] methods. Fourth, it should be simple to run MissDiff on this benchmark during the rebuttal period.

### Questions
- [UPDATE: addressed] Line 351 "MICE based on random forest (MissForest) (Stekhoven, 2015)". MissForest is not exactly following the MICE framework using random forest. Are you comparing to MICE-Forest (presumably the implementation of AnotherSamWilson/miceforest) or truly MissForest (presumably the implementation of epsilon-machine/missingpy)? Please clarify such details in the manuscript.

- [UPDATE: addressed] While leaving the architectural details to the manuscript appendix is fine, it would be nice if  the main text indicated that a neural network model architecture is used.

### Soundness
3

### Presentation
3

### Contribution
4
