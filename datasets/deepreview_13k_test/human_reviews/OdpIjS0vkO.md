# More is Better: when Infinite Overparameterization is Optimal and Overfitting is Obligatory

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
In our era of enormous neural networks, empirical progress has been driven by the philosophy that *more is better.*
Recent deep learning practice has found repeatedly that larger model size, more data, and more computation (resulting in lower training loss) optimizing to near-interpolation improves performance. In this paper, we give theoretical backing to these empirical observations by showing that these three properties hold in random feature (RF) regression, a class of models equivalent to shallow networks with only the last layer trained.

Concretely, we first show that the test risk of RF regression decreases monotonically with both the number of features and samples, provided the ridge penalty is tuned optimally. In particular, this implies that infinite width RF architectures are preferable to those of any finite width. We then proceed to demonstrate that, for a large class of tasks characterized by powerlaw eigenstructure, training to near-zero training loss is *obligatory:* near-optimal performance can *only* be achieved when the training error is much smaller than the test error. Grounding our theory in real-world data, we find empirically that standard computer vision tasks with convolutional neural kernels clearly fall into this class. Taken together, our results tell a simple, testable story of the benefits of overparameterization and overfitting in random feature models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provides a unified formulation of the generalization error for random feature (RF) and kernel ridge regressions (KRR). While it is heuristically derived, it covers some expressions of the generalization error obtained in the previous work and gives us a quantitative understanding depending on the width (# of random features), sample size, teacher noise, and ridge penalty. This theoretical evaluation matches well empirical experiments. In addition, by focusing on the KRR limit, the authors succeeded in obtaining a more detailed evaluation for the case of power-law eigenstructure. That is, they provide an explicit formulation of the generalization error depending on the exponents of the student's and teacher's eigenstructures.

### Strengths
(i) While there are numerous individual analyses of RF and KRR under various conditions, this study attempts to provide a unified perspective. This endeavor, even if the derivation is heuristic, will be important for establishing a foundation for understanding.

(ii) While tackling such a significant (big) question, the study also provides technically solid contributions. In particular, this work gives novel continuum approximations for the generalization errors depending on the power-law eigenstructures (in particular, Lemma 1,10). This enables us to quantitatively understand the obligatory conditions for the "more is better" in the case of overfitting. This work also includes other technically solid and informative results such as remarks on the appropriate scaling of target noise (eq. 7), connection to the previous work (Section E), and the sophisticated evaluation of the power-law eigenstructures (Section B).

(iii) The paper is very well structured and articulated, with various efforts made to facilitate the reader's comprehension. This implies the author's deep understanding of RF and KRR.

### Weaknesses
(i) While the analysis for the power-law eigenstructure is solid and concrete, the other part seems not so surprising as the theory. I mean, the heuristic derivation is rather straightforward.  It seems that the authors just substituted a heuristically-derived terms for the kernel matrix of RF (eqs.26-30) into a well-known expression of the generalization error (eqs.13, 14). I understand that providing a unified formulation itself is a very curious and interesting attempt, though.  Please refer to my Question (i) for more details. 



(ii) The definition of overfitting in this paper is unique, and its relation to the ridgeless case seems unclear. considering a ridgeless case seems appropriate when talking about overfitting to training samples. Indeed, Mei & Montanari 2019 have reported a certain condition where generalization error is minimized in a ridgeless setting and this was one of the main contributions.
In contrast, the current study does not directly analyze the ridgeless case but rather allows a non-zero fitting ratio in its analysis. For example, while Theorem 2 contemplates the optimal ridge, it's not explicitly stated when the optimal ridge becomes zero. I am also curious whether the noise condition in Corollary 1 works as a necessary and sufficient condition where the ridge-less case gives the best performance (I mean, the generalization error is minimized).

### Questions
**Major ones**

(i)  Regarding Weakness (i), eq.(13) seems a starting point to derive the omniscient risk estimate. However, the authors give not enough explanation on how and which paper has derived this equation.  As long as I know, Sollich, 2001, Bordelon et al., 2020 obtained this expression for KRR by using some heuristic derivations. Did the other work that you cited, i.e., Jacot et al., 2020a; Simon et al., 2021; Loureiro et al., 2021; Dobriban &Wager, 2018; Wu & Xu, 2020; Hastie et al., 2020; Richards et al., 2021,  explicitly give this expression (13) as well? If so, under what conditions does each study derive? Are they mathematically rigorous?  Because this equation is the starting point of all other analyses, it should be clearly and carefully described. 

(ii) I am confused about what the authors try to claim in Figure 2. Do you intend to claim that overfitting is obligatory only for the noiseless case ($\sigma_{rel}^2=0$)? For $\sigma_{rel}^2>0$, the minimal test MSE is obtained for non-zero fitting ratios. This implies that the generalization is the best for non-overfitting situations and the overfitting seems *not* obligatory. This point is unclear.
 
**Minor ones**

(iii) In Section 5, the authors focused on the KRR limit (k -> infty). I am curious about at what point the finite-k case becomes hard to analyze. 

(iv) Page 6: The definition of the fitting ratio seems to be wrong. It should not be R_tr /te:=E_te/E_tr but 
would be E_tr/E_te.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies how scaling the model size and the dataset size affects the performance of random features models.
While "classical" learning theory predicts that scaling the model can hurt performance, causing the model to overfit the data, this seems not to be true when learning with modern tools, e.g. neural networks. In practice, it seems that the bigger the model is, the better the performance it gets.
This paper recovers this behavior in the setting of learning ridge regression with random features. Namely, the authors establish that, for a correctly tuned ridge regression, the model's test error always improves with the number of features and the number of training samples. That is, the "double descent" phenomenon can be eliminated by correctly tuning the model's parameters. Additionally, the authors show that overfitting is necessary to achieve good performance in some settings with low noise. That is, not only overfitting doesn't hurt performance, but it also enables reaching optimal test error.

### Strengths
The paper shows two important results on the behavior of random feature models: first, that they can always improve with scale (both in terms of number of features and number of examples), and second, that overfitting might be necessary in some problem settings. To my understanding, these results unify previously studied settings, and present theoretical results that are more aligned with behaviors of large models in practice. The experiments seem to be convincing that the assumptions made in the analysis are reasonable in practical settings.

### Weaknesses
One point that I think the authors should clarify is in which cases the analysis is "rigorous", in a sense that the results follow from the problem assumptions, and in which cases the derivations are loose. It would be helpful, even for the "nonrigorous" steps, where some quantity is approximated, to state what are the precise bounds on the estimations. For the theorem statements in the paper, the way they are currently written, it is not clear if they truly follow from the assumptions, or are there some additional approximations (beyond the one covered in Assumption A) that are used in the analysis.

Additionally, for the results in Section 5, it is not clear what is the role that the noise plays in the analysis. Clearly, for large enough noise, overfitting hurts performance, i.e. - there is a predictor for which train error might be high (or even very high). While I understand that the noise might need to be scaled down (i.e., not analyze the setting of constant noise), it seems that the results in the paper only cover relatively low noise setting. What happens for higher noise levels? Do we expect overfitting to be unnecessary, or even hurt performance?

Minor:
Page 7, Target noise paragraph - "unlike is conventional" is probably a typo.

### Questions
See above

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to provide theoretical backing for the recent empirical study about the scaling "law" of large language models, i.e. larger model size + more data + more compute = more performance. To this end, the authors propose to study the random-feature (RF) regression model and show that their approximation to the test error strictly decreases when more data points and more width are provided. Then, they characterize which tasks obtain optimal performance when the training error is much smaller than the test error. Finally, some empirical evidence supporting the theory is provided.

### Strengths
The paper is very well written and polished. I believe the idea is original, although I'm not very familiar with this field beyond the standard NTK/NNGP theory (see my question below, though)---my confidence reflects this. The presentation is in general, clear; although some specific parts can be improved. More importantly, the paper's aim to formalize the common beliefs in the field---in what people call scaling "law"---is laudable.

### Weaknesses
First, as I mentioned before, in some parts, the presentation can be improved. Here is a non-exhaustive list:

1. How are the approximations of the train and test errors on page 4 derived. I think it is crucial to at least provide intuitions about them and quantify the approximation errors. This is because much of the results of the paper rely on those approximations.
2. The term "interpolation" keeps coming up without being defined. Maybe it is obvious for people in this specific field; however, for the benefit of a broader audience, the authors should be more verbose.

Second, I'm unsure about the significance of the theoretical results. Mainly because the authors claim that the test error becomes better as $n$, $k$ increase because the RF model converges to the kernel regression limit. However, it is a bit hard to believe since kernel machines (RFs, GPs) are in general worse than their finite-width NNs counterpart (kernel machines = linear models => no representation learning). As the authors mentioned on page 5, Thm. 1 works since intuitively RF -> kernel machine; the latter is the ideal limiting process. If this is the case, doesn't this imply that GPs should be better than standard NNs?

### Questions
1. Could the authors please address the above concerns?
2. The authors mentioned that "we do not want to take a fixed noise variance" and then argued that it is better to scale it proportional to the uncaptured signal. I'm not sure if this is realistic since $\sigma^2$ is the aleatoric (irreducible) uncertainty inherent in the data (think about the noise resulting from some measurement error in a sensor). How do you handle this, then? Maybe you should instead argue using the language of GPs, and thus give you the freedom to talk about _epistemic uncertainty_, which decreases as $n$ increases?
3. How should one relate Thm. 1 and Fig. 1? In the former, the test error should always decrease, but in the latter, the test error saturates. Note that, I think Fig. 1 is the "correct" behavior: kernel machines are not powerful and thus the test error is bounded away from zero, higher than DNN's. (As for the train error, this seems fine since infinite-width => linearity => quadratic loss => global optimum is achievable.)
4. How does this paper relate to the work of [Bowman & Montufar (NeurIPS 2022)](https://arxiv.org/abs/2206.02927), which also studies the large-width large-data regime?

Thanks!

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
