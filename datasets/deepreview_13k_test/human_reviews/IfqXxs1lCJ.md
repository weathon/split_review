# On the Evaluation of Generative Models in Distributed Learning Tasks

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
The evaluation of deep generative models including generative adversarial networks (GANs) and diffusion models has been extensively studied in the literature. While the existing evaluation methods mainly target a centralized learning problem with training data stored by a single client, many applications of generative models concern distributed learning settings, e.g. the federated learning scenario, where training data are collected by and distributed among several clients.
In this paper, we study the evaluation of generative models in distributed learning tasks with heterogeneous data distributions. First, we focus on the Fréchet inception distance (FID) and consider the following FID-based aggregate scores over the clients: 1) FID-avg as the mean of clients' individual FID scores, 2) FID-all as the FID distance of the trained model to the collective dataset containing all clients' data. We prove that the model rankings according to the FID-all and FID-avg scores could be inconsistent, which can lead to different optimal generative models according to the two aggregate scores. Next, we consider the kernel inception distance (KID) and similarly define the KID-avg and KID-all aggregations. Unlike the FID case, we prove that KID-all and KID-avg result in the same rankings of generative models. We perform several numerical experiments on standard image datasets and training schemes to support our theoretical findings on the evaluation of generative models in distributed learning problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the extension of FID and KID scores from centralized setting to distributed setting. Average of scores at each client is compared to the corresponding centralized score. Authors prove that the FID score rankings may not match, while KID scores always do. Experiments confirm this theoretical claim.

### Strengths
- Important setting: Distributed learning and evaluation of generative models is an increasingly important topic
- The theoretical analysis is accurate and empirical results adequately support the theory

### Weaknesses
- The paper’s main contribution is a very simple observation. In essence, the FID score is an infimum of an expected distance, whereas KID is expectation of the kernel distance. Hence, KID ranking consistency directly follows from linearity of expectation, while FID does not follow the same. This observation alone does not constitute a significant contribution.
- The simple observation would’ve still constituted as a good contribution if the authors provide some actionable insights. For example, one possible conclusion could be that one should use KID rather than FID in distributed settings — however, authors do not compare models obtained via these two methods in detail. Another possible direction could be to modify FID so that the new score behaves well under averaging.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied the evaluation of generative models in distributed learning settings, in particular, the federated learning scenario. The paper showed that in distributed settings, the way to aggregate evaluation metrics may affect rankings of generative models. For FID score, the paper theoretically showed that FID-avg which is the mean of clients’ individual FIDs, can be inconsistent with FID-all, which is the FID score computed on the collective dataset, leading to different model rankings. On the other hand, for another evaluation metric KID (kernel inception distance), KID-avg and KID-all are always consistent for ranking models. Experimental results were provided to support the theoretical findings.

### Strengths
1. The paper provided theoretical findings on evaluation metrics for generative models in distributed settings. The results could be of interest and are worth discussing when training and comparing generative models in the distributed manner.

2. The paper provided experimental results on toy datasets and real image datasets, to show that while FID scores can be inconsistent, the KID scores are always consistent.

### Weaknesses
1. For FID scores, while the paper gave theoretical formulations for FID-avg and FID-all, the formulations can only distinguish different rankings of generators based on their distances to corresponding covariance matrices. It would be more informative to characterize the gap between FID-avg and FID-all with the distances between clients’ data distributions. This could allow one to estimate the degree of FID score inconsistency based on how different clients’ datasets are.

2. In experiments, it seems that most results for FID scores come from ``simulated’’ generators, that is, treating a class of images from CIFAR-10 or CIFAR-100 as the output of a generator. Such simulation does not well represent real generators trained on the multi-class dataset, or the general federated learning protocol (even when each client owns one class of images only). Hence the results do not sufficiently reveal if inconsistency between FID-avg and FID-all is an actual issue in practice. Moreover, the FID scores are quite large and far from optimal, in which case the consistency of the evaluation metric may not be a most important property to pursuit.

### Questions
In Figure 2, do the KID scores imply that the plane generator is better than the DDPM model, while the former generates much less diverse images? This may raise a question of how to properly evaluate the models apart from consistency.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the evaluation of generative models in the distributed/federated setting and studies two popular metrics, Fréchet Inception Distance (FID) and Kernel Inception Distance (KID). In particular, the authors consider two distributed evaluation modes: (all) the metrics are computed against the global data distribution, i.e., the mixture defined over the clients’ distributions; and (avg) the metrics are computed against the distribution of each individual client and then averaged to define a single score. The authors prove that in the case of KID, both evaluation modes rank generative models in the exact same manner, but that in the case of FID, the rankings defined by FID-avg and FID-all can vary significantly. The theoretical results are further supported by extensive empirical results on popular benchmarks for image generation in a federated setting with heterogeneous client distributions.

### Strengths
- To the best of my knowledge, the main results of the paper are novel, and the supporting arguments, both theoretical and empirical, seem to be sound. The evaluation of generative models is an important and challenging topic that becomes even more difficult in the federated setting, which thus far has received little attention in the literature.
- The paper is very well written and easy to read. The authors do a good job of introducing the relevant concepts and literature around generative models and federated learning.
- The experiments are extensive and support the main theoretical claims of the paper. The authors also shared their code, and I have no reason to believe the results are not reproducible.

### Weaknesses
- The need for the two modes of evaluation the authors consider (all and avg) is not well motivated in the paper. Among the cited previous works on federated learning for generative models, most if not all rely on some form of FID-all, typically by computing FID scores on a separate test dataset. Are there any examples in the literature where scores similar to FID-avg or KID-avg were considered? I imagine one would be interested in FID-avg in the context of personalization or when privacy concerns prevent the usage of FID-all, for example, but that is never discussed in detail in the current version of the paper.
- Following on the previous point, although the paper is well presented, novel and sound, I am not entirely convinced of its significance.
- The discussion of the results could exploit a few points more in depth. For instance, the authors could comment on how their results could be used to guide the selection of an appropriate metric. From where I stand, it seems the results favor KID-avg, since it can be computed in a distributed manner (thus preserving privacy) but still retains the same ranking of KID-all, which captures the global distribution.

Minor points:
- Theorem 1: “distributions” is misspelled, and I believe “following” should be singular.

### Questions
1. In Section 5.1., the authors note that “[…] counterintuitively, the ‘ideal estimator’ did not reach the minimum average of the Fréchet distances”. Could they share any intuition as to why that is the case? Does that indicate taking the average among clients is a poor metric to optimise for?
2. Would it not be possible to also show the optimal value (referent to the true distribution) for the KID metric in the experiments of Section 5.1.?
3. In page 7, the authors comment on the effect of privacy considerations when choosing between FID-all or FID-avg: “[…] a distributed computation of FID-all is more challenging than obtaining FID-avg due to privacy considerations”. This shows an interesting trade-off between the two modes that the authors could explore a bit further. While FID-all can be more challenging to compute from a privacy perspective, wouldn’t FID-avg favor a model that fits the distributions of only one or a few of clients very well, thus potentially “memorizing” the data of these clients?
4. Empirically, does the ranking provided by KID matches any of those given by FDI-all or FDI-avg? It is not clear to me whether we can infer that from the plots, but it would be interesting to know how the rankings of FDI and KID compare in the experiments (even though the theoretical results have nothing to say here).
5. On a similar note, for the experiments of Section 5.1. as well as those with DDPM, one could compute (estimates of) the log-likelihood of the data. Have the authors considered how the ranking defined by the log-likelihood compare with the other metrics? The log-likelihood should provide consistent rankings, differently from the density metric of Naeem et al.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
