# Data Distribution Valuation with Incentive Compatibility

- Decision: Reject
- Scores: 5, 1, 3

## Abstract
Data valuation is a class of techniques for quantitatively assessing the value of data for applications like pricing in data marketplaces. Existing data valuation methods define a value for a dataset $D$. However, in many use cases, users are interested not only in the value of a dataset, but in the distribution from which the dataset was sampled. For example, consider a buyer trying to evaluate whether to purchase data from different vendors. The buyer may observe (and compare) only a small sample from each vendor prior to purchasing the data, to decide which vendor's data distribution is most useful to the buyer. The core question of this work is how should we compare the values of data distributions from their samples? Under a Huber model for statistical heterogeneity across vendors, we propose a maximum-mean discrepancy (MMD)-based valuation method which enables theoretically principled and actionable policies for comparing data distributions from samples. We show theoretically that our method achieves incentive-compatibility, thus incentivizing the data vendors to report their data truthfully.
We demonstrate the efficacy of our proposed valuation method against several existing baselines, on multiple real-world datasets (e.g., network intrusion detection, credit card fraud detection) and downstream applications (classification, regression).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of evaluating datasets from heterogeneous distributions. The paper adopts a Huber model on the dataset, assuming each dataset can be contaminated by samples from some noise distribution for a small factor. The principal aims to elicit truthful datasets from the data providers, and at the same time, the payment also distinguishes dataset qualities. The paper proposes to use the negative Maximum Mean Discrepancy (MMD) as the value of a distribution and to use an estimator of the MMD as the payment to incentivize truthful reports.

### Strengths
The paper studies an interesting problem and is well-motivated.

### Weaknesses
 * MMD as a valuation doesn’t reflect data distribution’s performance on a real decision problem / proper loss function. In contrast divergence-based valuations correspond to the value of dataset on a proper loss.

* I suggest the author compare the results to previous results in information elicitation. Specifically, this following paper seems relevant. It studies elicitation with sample access to the distribution to be elicited. Suppose the principal has sample access to ground truth distribution, and sets it as a reference, it seems like the approach in this paper could be applied.

    Frongillo, Rafael, Dhamma Kimpara, and Bo Waggoner. "Proper losses for discrete generative models."

* Suppose all N-1 distributions have the same deterministic bias, while only one distribution is the ground truth distribution. It seems like it is impossible in this case to discover or incentivize the most valuable dataset.

Minor comments:
* typo: Page 7, Subsequently, each Pi follows a Huber: Pi =(1−εi)P∗ +Q , missing εi before Q.

### Questions
* Impossibility results: as my comment 3 in Weakness, I wonder if the authors can prove impossibility results on discovering the truth. This can help justify the current approach in the paper. 

* Why is this bad? In the paper: “To elaborate, there is no need to explicitly learn the distributions P, P ′ to obtain their distribution divergence (e.g., in Kullback-Leibler divergence-based valuations”. Explicitly learning the distribution doesn’t sound like a drawback to me. The selection of MMD is not well-motivated. Are there other metrics that can achieve similar results?

* Following the previous point, if the authors believe learning the explicit distribution is not feasible, is it possible to construct estimators of KL divergence from samples and directly estimate KL divergence similarly as the approach in this paper?

* Definition of IC is unclear to me, especially the part with wlog.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies data valuation, focusing on proposing valuation metric that encourages truthful reporting of data vendors (incentive compatibility). The model assumes Huber classes of distribution, where each vendor $i$ holds a mixture $P_i$ of some arbitrary distribution (stochastic or adversarial) and some ground-truth distribution $P^*$, and presents a sample from it to the user. The user hopes to evaluate the quality of the distribution (presumably in terms of proximity to $P^*$) through the samples, when both $P_i$ and $P^*$ may be unknown. Further, the designed metric should encourage vendors to report truly i.i.d. samples from their distribution, instead of making up artificial samples. The proposed solution uses the idea of maximum mean discrepancy (MMD), applying an estimator of MMD on the samples. Theoretical analysis and empirical evaluation are both offered.

### Strengths
The problem studied in this paper is meaningful and interesting.

### Weaknesses
 - [Quality] I find the setting studied in this paper slightly confusing. In particular, I am not sure if the author(s)' definition of IC is in line with my usual understanding: it looks like the definition of $\gamma$ -IC (Def. 1 and Cor. 1) depends on the choice of $\tilde{P}$ (instead of "for all $\tilde{P}$ in certain class"), which seems unusual. The approach in this paper is to propose a natural candidate for the metric, and then studies its IC property (as opposed to characterizing the class of IC designs) - there is nothing wrong with it, but I find it slightly misleading to refer to Cor. 1 as $\gamma$ -IC. I am quite certain that manipulating the dataset would quite often lead to better metrics. For example, a vendor could potentially generate samples that are specifically designed to maximize the MMD score, even if they do not accurately reflect the underlying distribution. Moreover, the empirical results also seem insufficient in justifying the true IC (in the way I would define it) - the alternative distribution considered is overly specific and somewhat naive, and clearly cannot represent the class of all possible manipulations. For instance, the considered manipulation seems to only consider a simple shift in the mean, which is a very limited form of data manipulation. Overall, I am not convinced of the correctness (or significance) of the main claim.
- [Clarity] Certain parts in the paper are confusing to read with slightly informal tone, primarily due to the lack of formal and rigorous mathematical statements. For instance, the wording of Def. 1 (and also the Problem Statement) is imprecise (and, to my previous point, likely nonstandard).

### Questions
- First and foremost, please verify if Def. 1 is consistent with the standard notion of IC.
- I am curious why the problem is phrased "data valuation"? I see nothing about pricing in this work, and to me "evaluation" seems like a better fit?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to assess the value of a data distribution (instead of a sampled dataset), and claims that this method satisfies incentive-compatibility (IC) in the sense that data providers have no incentives to mis-report their data.

The main idea of the method is the following: First, assume that each provider's distribution $P_i$ is a mixture of a reference (ground truth) distribution $P^*$ and a noise distribuiton $Q_i$. Then, the maximum mean discrepancy (MMD) $d(P_i, P^*$) between $P_i$ and the reference distribution $P^*$ is a value measure for $P_i$. Since $d(P_i, P^*)$ is unknown, the authors approximate it by $\hat d(D_i, D^*)$ using sampled datasets $D_i$, $D^*$. In addition, since the reference distribution $P^*$ is also unknown, the authors propose to use the average of all data providers' distributions as a proxy, $P_N$. Hence, the final metric is $\hat \nu(D_i) = \hat d(D_i, D_N)$, where $D_N$ is the aggregate of all providers' datasets.

The authors then prove that this metric $\hat \nu$ satisfies IC if: Roughly speaking, (1) $d(P_{-i}, P^*)$ is small (_the average distribution of providers other than $i$ is closed to the reference $P^*$_) or $d(\tilde P_i, P^*)$ is large (_the report of $i$ is far from $P^*$_) (from Corollary 1); (2) the size $m_i$ of each sampled dataset $D_i$ is large enough (from Theorem 1).

The authors then present some experimental results to support their theoretical claims.

### Strengths
1. The use of Huber model (each provider's distribution $P_i$ is a mixture of a reference distribution $P^*$ and a noise distribuiton $Q_i$) is natural and interesting.
  
2. The main problem -- measuring the value of a data distribution, not just a sampled dataset of limited size -- is well motivated as in the introduction.

### Weaknesses
Although the problem of data distribution valuation is well motivated, I don't think the authors' solution to this problem is satisfactory:

1. A main idea in the authors' solution is to use the MMD $\hat d(D_i, D_N)$ estimated from samples to approximate the true MMD $d(P_i, P^*)$. This is basically a law of large number, where good estimation can be obtained if the number of samples is large enough. However, the motivation of data distribution valuation is exactly the lack of samples. As written in the Introduction, "data vendors offer a preview in the form of a sample dataset to prospective buyers. Buyers use these sample datasets to decide whether they wish to pay for a full dataset or data stream." The key tension is how the buyers can evaluate the value of a full dataset given access to only a limited-size preview dataset. **This is at odd with the authors' approach of using many samples to estimate the value of the distribuiton.** Specifically, the authors' approach requires a substantial number of samples from each provider to accurately estimate the MMD, which undermines the core motivation of evaluating distributions from limited previews. The reliance on a large number of samples to estimate the MMD effectively shifts the problem from valuing distributions from limited data to valuing distributions with ample data, which is not the problem the paper claims to address.

2. Another idea in the authors' solution is to use the average distribution $P_N$ of every one's distribution as the reference distribution $P^*$. This requires $P_N$ to be closed to $P^*$; in other words, the noisy parts $Q_i$ in everyone's distribution cancel out when averaged (Proposition 2). **This is a strong limitation.** As the authors point out (in page 17), it is possible that a majority of data providers are off from $P^*$ while only a few are close to $P^*$. In this case, the authors' solution does not work. This reliance on the average distribution being close to the true distribution is a significant assumption that limits the applicability of the method in real-world scenarios where data quality and distribution can vary widely. The method is particularly vulnerable to scenarios where a significant portion of the data providers are biased or provide low-quality data, which would skew the average distribution and make it a poor proxy for the true reference distribution.

3. **My biggest concern is the definition of Incentive-Compatibility (Definition 1)**, which says that "a vendor with actual data distribution $P$ will not choose to report data from distribution $\tilde P$ where **w.l.o.g.** $d(P, P^*) < d(\tilde P, P^*)$". I don't understand why this is "without loss of generality". A vendor can definitely report data from a distribution $\tilde P$ that is closer to $P^*$ than the actual distribution $P$ is: $d(\tilde P, P^*) < d(P, P^*)$. In the standard definition of IC (like in [Chen et al 2020]), a player should be disincentivized to mis-report anything. The authors' definition of IC is not aligned with standard game-theoretic definitions, which require that a mechanism should disincentivize any misreporting, not just misreporting that makes the reported distribution further from the ground truth. This definition of IC is overly restrictive and does not capture the full range of possible misreporting strategies that a rational agent might employ.

### Questions
**Question:**

In Section 6.2 (experiment about incentive compatibility), the authors let the vendors misreport $\tilde D_i$ by adding zero-mean Gaussian noise to the original data $D_i$:

(1) Why cannot the vendors use other form of misreporting?  Did you try other form of misreporting? 

(2) And why does adding Gaussian noise ensures $d(\tilde P_{i'}, P^*) > d(P_{i'}, P^*)$ ?

**Suggestion:**

Maybe a better motivation/theme of this work should be "how to value heterogeneous datasets", instead of "how to value data distribution instead of dataset". As I argued in Weakness 1, the authors' approach is not about valuing data distributions using limited-size preview datasets; it is more about how to value heterogeneous datasets.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
