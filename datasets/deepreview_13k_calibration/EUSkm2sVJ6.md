# How much of my dataset did you use? Quantitative Data Usage Inference in Machine Learning

- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 8, 8, 8, 6

## Abstract
How much of a given dataset was used to train a machine learning model? This is a critical question for data owners assessing the risk of unauthorized data usage and protecting their right (United States Code, 1976). However, previous work mistakenly treats this as a binary problem—inferring whether \textit{all or none} or \textit{any or none} of the data was used—which is fragile when faced with real, non-binary data usage risks. To address this, we propose a fine-grained analysis called Dataset Usage Cardinality Inference (\ourmethod{}), which estimates the exact proportion of data used. Our algorithm, leveraging debiased membership guesses, matches the performance of the optimal MLE approach (with a maximum error <0.1) but with significantly lower (e.g., $300 \times$ less) computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper formalizes the problem of dataset cardinality inference, which aims to measure _how much_ of a given dataset has been used in model training. The paper shows how existing out-of-the-box membership inference methods fail to solve this problem and show how that can be remedied with de-biasing. Experimental results show the benefits of the proposed approach.

### Strengths
This paper introduces on a very important problem and gives some solid baselines to tackle it. 

The method, error metrics, experimental settings, baselines, and evaluations are thoughtfully designed (in general). For example, I particularly appreciate:
- the extra mile effort in deriving confidence intervals;
- the use of dataset selection methods in experimental evaluations;
- an analysis of why the confidence intervals are large around $p=1/2$;
- the experimental setting of book copyright infringement;

### Weaknesses
The main drawback, in my opinion, is that there are approximations involved in deriving the confidence estimates, making them potentially incorrect. There appear to be two approximations (please correct me if I'm mistaken):
1. replacing $TPR_i$, $FPR_i$ with a single TPR/FPR across all samples, so the de-biasing is not exact;
2. assuming independence of $\hat p_i$'s to compute the confidence intervals.

While the authors empirically show in Fig 4 that the correlations in item 2 above are small, it would be nice to see that the bias induced by item 1 is also not too large. Specifically, the use of a single global TPR and FPR for debiasing each sample's membership score may introduce a bias if the true TPR and FPR vary significantly across different data points. This is especially concerning when the data points are not uniformly sampled or when the model's performance varies significantly across different regions of the input space. For example, if the model is more confident on some data points than others, the TPR and FPR could be different for those points, and using a global value could lead to inaccurate estimates of the membership probabilities.

Finally, I would have liked to see some approaches for rigorously correct (asymptotic or non-asymptotic) confidence intervals in addition to the heuristic ones used here. I believe that the XBern confidence intervals given by [Pillutla et al](https://arxiv.org/abs/2305.18447) can be used (XBern confidence intervals for $TPR_i$ and $FPR_i$ can automatically adapt to the correlation, leading to better intervals for $\hat p$).

**Other comments**: 
- I do not understand the derivation of footnote 1. It would be nice to expand on it (possibly in the supplement). 
- Figure 2 can be clearer if the x axis is in log scale
- Missing relevant refs: [Kandpal et al](https://arxiv.org/pdf/2310.09266) for membership inference of users (groups of data) and is related to dataset inference, [Vyas et al](https://arxiv.org/pdf/2302.10870) for copyright protection, [Zhang et al.](https://arxiv.org/pdf/2406.15968) for a recent MIA

### Questions
- **Poor results around $p=0$**: The results of Table 4 show that the method is not very reliable around $p=0$. This would make it unsuitable to answer the question of _if_ a dataset has been used. Are any modifications possible to adapt the proposed method to [dataset inference](https://arxiv.org/abs/2406.06443)?

- Further, how does the proposed method work if our goal is to provide a multiplicative guarantee of the form that $\hat p / p \in (1/c, c)$? These would be more realistic in the small $p$ regime.

- Like differential privacy is designed to protect against membership inference, are there any provable protections against DUCI?
- Why do you think MIA Guess fails to work?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this manuscript the authors identify key issues of current techniques that aim to ascertain if a dataset was used to train a Machine Learning model. To alleviate these problems:

1. The authors formally define the concept of Data Usage Cardinality Inference (DUCI). The authors state that, compared to other binary types of inference, DUCI better reflects real world scenarios, where models are trained on fractions of different datasets. 
2. The authors propose a way of de-biasing current models that estimate individual membership, i.e. if one individual sample was part of the training dataset. Then, they propose to use these unbiased estimators to compute the overall proportion of the dataset used for training. They also present an asymptotic method to design a confidence interval for this overall proportion used for training. 

Finally, the authors provide some numerical experiments where they compare the proposed procedure with four other adapted techniques that also perform DUCI. Throughout their experiments, the authors' de-biased method outperforms the other four techniques.

### Strengths
Identifying the dataset used to train a Machine Learning model could have a direct impact on privacy rights or copyright infringement, as mentioned in the Introduction. Hence, I think that this article deals with a relevant problem. I also appreciate that their proposed procedure is cost-effective and intuitive. In my opinion, there is a lot of merit in noticing that Member Identification methods suffer from biases and then presenting an straight-forward tool to address this issue.

### Weaknesses
I think that the main weakness here is the presentation. A lot of times the authors describe mathematical objects by vaguely saying what they are or make rushed arguments. However, this approach is not intuitive enough to give any insight about the matter nor formal enough to have any actual meaning. This overshadows the interesting contributions made in this paper.

From Lines 108-115, I wonder what is "a number of population data", what is $\theta(x)_y$ (as this is the first time they use this notation with y as a subscript; in fact, what is y?). What is the reference model modelling, i.e. are these models for membership inference or are these models that represent a real world classifier or regressor?. In Line 285-286, it is difficult to understand what "the probability of observing that i-th record’s likelihood to be a member is greater than randomly sampled population data points" means. This is not even relevant to understand the paper main contributions, so it should be remove it the authors are not willing to explain it clearly or should be rewritten, if they prefer to do so.

Dependence/correlation of records is handled in a confusing manner. In particular, the authors pose the question "Will the ignorance of “correlations” between records make our method sub-optimal?" in Lines 490-491. The answer here is clearly "Yes", as the authors themselves have stated in Lines 444-448 that under special sampling one should divide the dataset into subgroups and then de-bias using the TPR and FPR within each subgroup. However, this additional step, which accounts for possible high-correlation, is not carefully mentioned in Section 4, so I would not assume that this is a fundamental part of their proposed technique. However, it reads as if Lines 489-497 argue that correlation between records is not an issue and that there seems to be limited potential to improve their method in this regard. Maybe the authors here are considering different methods of sampling or different settings but this is not clearly stated in Lines 489-497. This is something that should be addressed. 

Regarding the numerical experiments, there are two things to consider: two methods were adapted from Individual Membership Attacks and the other two baseline estimators were inspired by maximum likelihood estimation but rely on additional modeling decisions, like assuming some joint/mean logits follow a normal distribution. Although this choice is based on a theoretical result, as mentioned in Line 298, it is not clear to me that this assumption would not hinder the performance of these baselines. The authors do mention in Line 276 that they use MIA Guess and MIA Score "To demonstrate the importance of debiasing [...]", but I think they would need to address why the MLE with joint logits is presented as an idealized baseline. At least the MLE with average logits has good performance in various experiments, so there is evidence in favor of presenting it as an idealized baseline. However, I feel like the experiments in this paper do indicate that the proposed method performs well, under the scenarios considered here.

### Questions
What is the the sampling error mentioned in Line 228 in this particular setting?. 
What is the definition of weak independence in Line 269?.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a new variation of membership attack: estimating the fraction of data from training set. Unlike normal MIA, which determine individual membership, the proposed task estimate the data usage directly. The proposed algorithm is based on the fact that the  unbiased data usage estimator can be written as a function of FPR and TPR (Eq. 6) of MIA. In other words, the proposed estimator can adapt any existing MIA attack with FPR and TPR evaluation. The experiments demonstrate the effectiveness.

### Strengths
This paper introduces a new task in privacy attacks. The main contribution is a practical and scalable data usage estimator that could encourage further research in this area.

### Weaknesses
My main concern is that this method requires known training set for estimating FPR and TPR. In practice, the train set is usually private (see following reference Zhang at el 2024).



Zhang, Jie, Debeshee Das, Gautam Kamath, and Florian Tramèr. "Membership Inference Attacks Cannot Prove that a Model Was Trained On Your Data." arXiv preprint arXiv:2409.19798 (2024).

### Questions
1. In Figure 3, the length of confidence interval seems to be large compared to the absolute error. Is this true?

2. Would this debiasing method downgrade the test power?

3. Is there any connection with auditing differential privacy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Given a dataset, this paper presents an algorithm (DUCI) which estimates the proportion of that dataset used in the training of a model. The algorithm estimates the false positive rate (FPR) and true positive rate (TPR) of the membership inference guess across the entire dataset to avoid the accumulation of errors that occurs when estimating the FPR and TPR of each individual in the dataset. They conduct experiments to compare the performance of their algorithm (DUCI) against traditional membership inference baselines and an idealized, computationally inefficient MLE baseline. They also analyze the performance of DUCI and membership inference baselines under special sampling conditions and varying dataset sizes.

### Strengths
The paper is well motivated and addresses a gap in the literature by taking a fine grained approach to the data usage problem.

The proposed approach (DUCI) is significantly more computationally efficient compared to previous approaches.

### Weaknesses
I don't see any major weaknesses. It would be nice to show a comparison between DUCI and SOTA “binary” data usage algorithms for the specific case for when p=1 and p=0 to demonstrate that DUCI still has comparable performance to “binary” data usage algorithms in these specific cases.

### Questions
If TPR=FPR, how does this affect the debiasing results?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes an algorithm framework that can figure out whether data points in the data sets are used to train a model. This problem seems interesting, and there are some works on a similar problem called membership inference. The authors propose that instead of predicting each member by {0,1}, a better way is to predict a probability in [0,1] and design an algorithm for DUCI based on this idea. The authors also did many experiments comparing their method with several baselines on errors and confidence intervals.

### Strengths
This paper studies an interesting problem and proposes a new algorithm to predict a probability in [0,1] instead of {0,1} for the problem. Though the authors proposed a specific algorithm, the technique here can be used for any algorithm that serves the purpose of membership query. This paper is well-written and easy to read. The authors also did experiments thoroughly by comparing with baselines and on different datasets.

### Weaknesses
Though this paper has some novelty, the technique here seems to be quite simple and straightforward. It is hard for me to say this paper has good contribution confidently.

### Questions
The authors mention two possible improvements in Appendix G. I think this paper would be really strong if the authors could be more concrete on how to apply one of the ideas to their algorithm and show some results.

### Soundness
3

### Presentation
3

### Contribution
2
