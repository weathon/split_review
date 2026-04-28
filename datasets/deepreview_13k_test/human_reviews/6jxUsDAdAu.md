# Benign Overfitting in Out-of-Distribution Generalization of Linear Models

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Benign overfitting refers to the phenomenon where a over-parameterized model fits the training data perfectly, including noise in the data, but still generalizes well to the unseen test data. While prior work provide a solid theoretical understanding of this phenomenon under the in-distribution setup, modern machine learning often operates in a more challenging Out-of-Distribution (OOD) regime, where the target (test) distribution can be rather different from the source (training) distribution. In this work, we take an initial step towards understanding benign overfitting in the OOD regime by focusing on the basic setup of over-parameterized linear models under covariate shift. We provide non-asymptotic guarantees proving that, when the target covariance satisfies certain structural conditions, benign overfitting occurs in standard ridge regression even under the OOD regime. We identify a number of key quantities relating source and target covariance, which govern the performance of OOD generalization. Our result is sharp, which provably recovers prior in-distribution benign overfitting guarantee (Tsigler & Bartlett, 2023), as well as under-parameterized OOD guarantee (Ge et al., 2024) when specializing to each setup. Moreover, we also present theoretical results for a more general family of target covariance matrix, where standard ridge regression only achieves a slow statistical rate of $\mathcal{O}(1/\sqrt{n})$ for the excess risk, while Principal Component Regression (PCR) is guaranteed to achieve the fast rate $\mathcal{O}(1/n)$, where $n$ is the number of samples.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides an analysis of benign overfitting in the out-of-distribution regime. Both ridge regression and PCR are analyzed and have rates $O(\frac{1}{\sqrt{n}})$ and $O(\frac{1}{n})$.

### Strengths
The paper is very well written. It presents complex results with clarity and cohesion. The results are novel to the best of my knowledge and the setup under analysis is very interesting.

I didn't thoroughly check all the proofs. But the steps in the main text seem logical to me.

The differences between rates for Principal Components Regression and Ridge Regression are surprising and interesting.

### Weaknesses
I believe the paper could benefit from some simulation experiments confirming the theoretical results.

For instance, verifying the rates  $O(\frac{1}{\sqrt{n}})$ and $O(\frac{1}{n})$ hold for a small Gaussian example would strengthen the claim, and help to support that the mathematical proofs are correct.

### Questions
- Does the result in PCR requires the number of relevant components k to be known in advance? What is the effect if the number is mispecified

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This manuscript investigate benign overfitting in out-of-distribution (OOD) generalization, focusing on over-parameterized linear models under covariate shift. It extends the concept of benign overfitting from in-distribution cases to settings where the target distribution differs from the training (source) distribution. The authors provide non-asymptotic excess risk upper bounds for ridge and principal component regression under specific structural conditions on the target covariance. More precisely, the main contribution is an instance dependent upper bound on the bias and variance terms of the excess risk of ridge regression under OOD. In particular, this upper bound shows that benign overfitting transfers from the in-distribution to the OOD setting when the target distribution’s covariance along the high-variance (or "major") directions aligns well with the source distribution’s major directions.

The authors also provide a discussion of an example with significant shifts in the minor directions, showing that in this case ridge regression incur a high excess risk, despite overfitting being benign in-distribution. Finally, the authors show that doing principal component regression (i.e. ridge regression only on the major directions) can mitigate this phenomena, since it avoids the excess error contributions from misaligned minor directions.

### Strengths
The manuscript is well written and easy to follow. It contains a nice balance of formal and intuitive discussion. The review of the in-distribution benign overfitting results is a nice addition that helps highlighting the contributions. Overall, I think it is a good contribution on a topic of interest to the theoretical community at ICLR.

### Weaknesses
The lack of a matching lower bound as in the in-distribution case of [Tsigler & Bartlett, 2023] is a weak point of the manuscript. Another minor weakness is that the technical contribution is also somehow limited, as it mostly relies mostly on extending existing results.

### Questions
- What are the main challenges in proving a matching lower bound for ODD similar to the in-distribution case?
- The fact that the analysis of OOD boils down only to the alignements of the covariance of the source and target distribution is closely to the square loss and linear estimator. How much should we expect this to transfer to other tasks, such as linear classification for instance?  

- L39-42:
> "*However, over-parameterized models, such as deep neural networks and large language models (LLMs), which have more parameters than training samples, are widely used in modern machine learning.*"

This sentence is misleading and overly general. In fact, most of modern LLMs use more tokens than parameters for training. See for example Table 2.1 in [1].  

- L11 in the abstract: "over-paramterized"

**References**

- [1] Brown et al. [Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165). NeurIPS 2020

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers a model to study benign overfitting in the context of out-of-distribution (OOD) generalisation for overparameterized linear models. The authors focus on covariate shift. 

The authors prove the following results
* The paper derives an excess risk upper bound the above setting. This bound generalizes directly the one in [Tsigler&Bartlett 2023].
* The authors consider specific choices of covariance matrices to consider two opposite cases:
  * If the major directions of the shifted model are the same and the minor directions remain small the begning overfitting still is present reaching a $O(1/n)$ bound for the excess risk.
  * For any ridge parameter $\lambda >0$, under a different covariance model, the authors show a lower bound on the excess risk as $O(1/\sqrt{n})$.
* To mitigate this problem the authors also consider principal component regression and show that under specific conditions it always achieves the $O(1/n)$ rate.

### Strengths
* First work to provide non-asymptotic guarantees for benign overfitting under general covariate shift
* Provides practical insights into when ridge regression vs PCR should be used.
* Results generalize and recover previous known bounds as special cases fitting in nicely with the literature on the topics.

### Weaknesses
* The clarity of the paper could be improved. While it is very clear the discussion about previous results and how the current result generalise the old ones I feel that the assumptions for the original contributions are hidden in the appendix. The paper would greatly benefit from a clear statement of the assumptions at the beginning or just a discussion of them. A specific instance of this Theorem 5 where the result depends on the additional assumptions that $\beta^{\star}_{-k} = 0$ and the fact that the overlap gap between major and minor directions is large.
* Another problem that I find, connected to the previous one, is the lack of simulation studies to illustrate the theoretical findings. As the setting of linear regression with general covariances is generic enough one could back up the claim with experimental validation on real datasets.

### Questions
* Are the conditions considered in Section 3.1 the most general ones for which the rate of the excess risk is slow?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the over-paramterized ridge regression under covariate shift assumption. Specifically,

1. The manuscript shows the ridge regression exhibits “benign overfitting” given the shifts in minor direction for target domain is smaller than source domains’ counterpart.
2. When there is significant components in the minor directions, the manuscript shows ridge regression only achieves a lower rate, e.g. $n^{-\frac{1}{2}}$. It also show using the PCR can achieve the fast rate $n^{-1}$ as in-distribution learning.

### Strengths
1. The authors provide extensive context to introduce the background and problem, making the logic very easy to follow.
2. Clear discussion about the role of $\mathcal{T}$ and the overall magnitude of $\Sigma_{T,-K}$. 
3. The instance-specified lower bound for ridge regression for large shift in minor direction scenario.

### Weaknesses
## 

1. For the large shifts in minor direction case, while I really appreciate the instance-specified lower bound for ridge regression, the result for PCR is more like “Shoot The Arrow, Then Draw The Target.” Given the assumption that the true signal primarily lies in the major directions of the source, it is not surprising that PCR works well as one has priorly excluded those un-handleable/irreducible parts in covariate shift, which eventually works like the process in Section 3. 
2. The lower bound is instance specified. Although this is already a good example to show ridge regression is not a generic good choice for large shifts, but having the lower bound for general case make the contribution of the manuscript more convincing. Can authors elaborate more on the main obstacle for the lower bound in general case? 
3. The fast rate in PCR is not adaptive. Similar to (1), if you know the true cut-off $k$, you pick the correct number of eigenvectors, this degrades the technical contribution of this manuscript. It is desired to have adaptive estimator/learner to adapt to the unknown $k$ and achieve fast rate.
4. (Potentially) Reviewer is not coming from the research area that working on over-parameterized models. Therefore, the reviewer cannot assert the technical contribution or novelty of this manuscript (although I see a detailed discussion on OOD in the over-parameterized model in related work ). I would like to leave this judgment to my peer reviewers, who are more familiar with this area.

### Questions
1. As the comment I raised in W3, is it possible to provide adaptive rate for PCR?
2. While the lower bound for ridge regression is instance-specified, the general intuition is that ridge regression typically fit the space in the whole scale. However, I would like to know if there is any special case that ridge regression can attain fast rate in large shifts.

### Soundness
3

### Presentation
4

### Contribution
2
