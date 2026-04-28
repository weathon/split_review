# Continuous Invariance Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 5, 8

## Abstract
Invariance learning methods aim to learn invariant features in the hope that they generalize under distributional shifts. Although many tasks are naturally characterized by continuous domains, current invariance learning techniques generally assume categorically indexed domains.  For example, auto-scaling in cloud computing often needs a CPU utilization prediction model that generalizes across different times (e.g., time of a day and date of a year), where `time' is a continuous domain index. 
In this paper, we start by theoretically showing that existing invariance learning methods can fail for continuous domain problems. Specifically, the naive solution of splitting continuous domains into discrete ones ignores the underlying relationship among domains, and therefore potentially leads to suboptimal performance. 
To address this challenge, we propose Continuous Invariance Learning (CIL), which extracts invariant features across continuously indexed domains. CIL is a novel adversarial procedure that measures and controls the conditional independence between the labels and continuous domain indices given the extracted features. Our theoretical analysis demonstrates the superiority of CIL over existing invariance learning methods. 
Empirical results on both synthetic and real-world datasets (including data collected from production systems) show that CIL consistently outperforms strong baselines among all the tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed the Continuous Invariance Learning(CIL) method that extends invariance learning from discrete categorical indexed domains to continuous domain in this paper.  Empirical results on both synthetic and real-world tasks demonstrated that CIL achieves improvements over baselines.

### Strengths
investigating invariant learning for continuous domains is an interesting idea. This paper presents some innovative contributions and can extend the invariance learning among discrete domains to continuous domains, which has certain reference significance for other studies. As a theoretical rooted work, it first proves that the existing method fails in the continuous domain through theoretical derivation, and then proves the effectiveness of its own method. Also, the empirical studies verify the effectiveness of the work.

### Weaknesses
Although the contributions of this work is worth noting, it still has some limitations in terms of problem definition and presentation. First is about the problem setting: in my view, when we talk about *continuous* in machine learning, it will reflect some time-series issues, i.e., the continual learning or lifelong learning framework. However, it seems in this work the notion of *continuous* is related to *many* domains. It’s more like we have several intermediate domains between two discrete domains. I’m wondering whether the notion of *continuous* is accurate here.
Second is about the presentation of the paper. Some fonts of the tables and figures are to small, making them hard to read. This article can be further optimized in terms of visualization. Besides, there are also many grammar errors, which makes the paper less readable, e.g., under Eq. 1, “…in among…”, in the subsection of *theoretical analysis of REx*, ‘Eq. equation 1’

### Questions
1. The real-world datasets implemented in this paper, such as the HousepPrice dataset, take the built year as the continuous domain index. While in real life, adjacent years are separated by 1 year. Can this be regarded as a continuous domain? Same question with the Insurance Fraud datasets.

2. In the paragraph *Existing Approximation Methods*, the authors let wt denote the optimal classifier for domain *t*. For the continuous domains, are there are continuous and infinite classifiers for each domain? How does such an assumption work in practice?

3. In the paragraph ‘Formulation’, the authors say that since if $y ⊥ t|Φ(x)$, the loss achieved by $g(Φ(x),y)$ would be similar to the loss achieved by h(Φ(x)). If the loss of $g(Φ(x),y)$ is similar to the loss of  $h(Φ(x))$, then will $y ⊥ t|Φ(x)$ hold？

4. In the paragraph ‘Empirical Verification’, the samples are simulated to distribute uniformly on the domain index $t$. According to figure 5, there is a step up of the ps(t). Please explain the reason.

5. As for the experiments on real-world dataset, I am wondering if it is more convincing to expand the verification on some mechanically related data sets. Because we usually think of information such as speed and speed as continuous rather than discrete.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of generalization in continuous domains. Specifically, they aim to learn invariant features in settings characterized by continuous domain. Previous methods are restricted to work with the discrete indexed domains. 

The authors demonstrate theoretically that when the number of domains is large and the number of samples from each domain is finite, existing methods can fail. Thus, discretizing continuous domains may not be a good solution. The authors then propose a min-max objective to learn invariant features by aligning domain distribution for each class of given features. To align the distributions, they use two domain predictors --- one uses invariant features, and the other uses label and invariant features. The goal is to learn features such that knowledge of labels does not increase the information about the domain. 

Authors tested their method on several toy and real-world datasets with continuous domains. Their approach outperforms in all the cases.

### Strengths
- The arguments in the paper flow well, and the problem formulation is interesting. This paper could be a benchmark (for datasets & settings) for future work exploring generalization over continuous domains. 
- Authors provide theoretical evidence to explain the failure of existing methods. This complements the empirical results that demonstrate the same.
- The authors demonstrate the superior performance of their method across various real-world and toy datasets

### Weaknesses
 - In almost all the datasets considered in the paper, the ground truth labels are independent of domains. However, it is possible to have domains where these are correlated --- different amounts of correlation in different domains. Why was such a toy environment not considered? It would be interesting to see how the proposed method performs in more correlated settings.

- The proposed approach relies on classes being discrete, whereas the prior method relies on the domain being discrete. This limitation should be highlighted in the paper.


------- 
Minor Typo Issues:
- Incorrect use of braces for citations (not an exhaustive list; please check the paper carefully): 
  - Sec 1. First para: use bracketed citations for He et al. (2016) etc,
  - Sec 2. .. following (Arjovsky et al., 2019) ... 
- Sec 1, Para 3 last line, incorrect brackets
- Sec 2: Invariance learning Para: ... to extracted Φ(x) ... -> to extract
- Sec 2: ...variance of the losses in among domains -> ...variance of losses among domains.
- Sec 3: Formulation para: Shouldn't soft regularization eqn have "- t" in the last two terms?
- Tables 3 and 4: Some values are too high in ID columns

### Questions
## Hyperparameters 
- What is the size of invariant features, i,e., $\phi (x)$? Is the method sensitive to the size of these features?
- What NN architecture & hyperparameters were used for training?

 
## On linear scaling of penalty  
- In the "Remark on the settings and assumption" paragraph, how does the penalty scale linearly with the number of environments when the spurious mask is used? We have assumed $\mathcal R^t(w, \phi) \sim \mathcal N (\mathcal R(w, \phi), \delta_R)$. So, shouldn't the variance penalty be $\delta_R$ when the spurious mask is used?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the invariant risk minimization (IRM) from discrete environment index to continuous environment index, in which there is no explicit environment partition and the domain variable is continuous. Authors first identify that some typical invariant representation learning algorithms, such as REx and IRMv1, may fail when the number of environments is large and there are only limited samples in each environment. Authors then propose a new regularization term by making $y$ is independent to $t$ (the domain index) given the extracted features $\Phi(X)$, and uses a min-max scheme to approximate the degree of independence by training two regression functions to fit 
$p(t|\Phi(X))$ and $p(t|\Phi(X),y)$.

### Strengths
1. The movation of extending invariant representation learning from discrete environment to continuous environment is nice and useful. 
2. Applications on Alipay and Wilds-time demonstrate the practical usages of the new method.

### Weaknesses
Frankly speaking, I really like the motivation of this paper. However, I just feel the main strategy (especially the way to measure conditional independence) is not novel to me, which has been used in previous extensions of IRM, such as InvRat (Chang et al., 2020) and IIBNet (Li et al., 2022). Moreover, the proof to Proposition 2 seems largely rely on result of (Li & Liu, 2021), including their assumptions.

1. The estimation on the degree of independence between y and t given $\Phi(X)$ does not seem novel to me. In fact, for discrete environment index $e$, both InvRat (Chang et al., 2020) and IIBNet (Li et al., 2022) use the same strategy to measure
$I(y;e|\Phi(x))$ ($I$ is the conditional mutual information) by minimizing the maximum difference of two prediction losses: 1) use $\Phi(X)$ to predict $y$; 2) use  $(\Phi(X),e)$ to predict $y$.

The only difference is that this paper changes the role of $y$ and $e$ and estimate $I(e;y|\Phi(x))$ by minimizing the maximum difference of two new prediction losses: 1) use $\Phi(X)$ to predict $e$; 2) use  $(\Phi(X),y)$ to predict $e$. 

Given the fact that the conditional mutual information is symmetric, i.e., $I(y;e|\Phi(X))=I(e;y|\Phi(X))$, and it is equivalent to write this condition with either $p(y|\Phi(X))=p(y|\Phi(X),e)$ or $p(e|\Phi(X))=p(e|\Phi(X),y)$, it does not make a big difference or novelty to change the prediction target. Although I admit that in continuous regime, learning two functions to predict e makes more sense.

2.  I would like to see some comparisons with environment partition approaches (see below), in which there is no explicit discrete environment index. In principle, those approaches should perform slighly better than manually environment splitting.

[1] Creager, Elliot, Jörn-Henrik Jacobsen, and Richard Zemel. "Environment inference for invariant learning." International Conference on Machine Learning. PMLR, 2021.

[2] Liu, Jiashuo, et al. "Heterogeneous risk minimization." International Conference on Machine Learning. PMLR, 2021.

Some other points:
1. Section I should be proof to Proposition 2, rather than Theorem 2?
2. How to manually split environments for IRMv1, IIBNet, etc? By clustering? or did I miss something in the supplementary material?

### Questions
Please see above weaknesses point 2 and minor point 2.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed Continuous Invariance Learning (CIL), a robust optimization algorithm targeting the continuous-domain setting. Through theoretical analysis, the authors show that existent methods fail to identify the spurious features when $\mathcal{T} \ge O(\sqrt{n})$, where $n$ is the sample size and $\mathcal{T}$ is the number of domains, whereas CIL can handle even the $\mathcal{T} \in O(n)$ case. Empirical experiments on both synthetic and real-world datasets indicate that CIL achieves SOTA performance.

### Strengths
CIL is motivated by a "duality" between domain and label due to the condition independence, which is an insightful observation. As a result, the method can target either continuous-domain discrete-label or discrete-domain continuous-label settings (the paper focuses on the former). It enjoys a strong theoretical guarantee and works well in practice, as indicated by the comprehensive experiments in which it outperforms all baselines.

### Weaknesses
While the method is titled "Continuous Invariance Learning", the theoretical analysis assumes countably many domains. For example, you can never have a domain with an irrational index like $\pi$ or $\sqrt{2}$. The authors may want to extend the theorems to cover the truly continuous setting. It is easy to see that the method itself applies to the truly continuous setting though.

According to Tables 3 and 4, CIL seems to perform poorly regarding in-domain prediction, with suboptimal accuracy and large variance. Moreover, I believe CIL has the potential to perform well in the discrete-domain continuous-label setting, but the authors didn't highlight or conduct experiments to demonstrate that.

Lesser issues:
1. Both $\mathcal{T}$ and $\mathcal{E}$ are used as the notation for domain indices, which is a little confusing.
2. In Table 5, you consider SWA as a baseline but didn't mention it in the main text.
3. The tables need some cleanup. In Table 4, you are claiming the accuracy for continuous IRMv1 under ID Alipay autoscaling is 885.7%. There are other issues like extra paratheses, missing space around paratheses, a missing period in the Table 3 caption, and an uncapitalized *method* in the Table 5 header.
4. In the paragraph starting with "Existing Approximation Methods": *Since is hard to validate* should be *Since it is hard to validate*.
5. In the paragraph just above subsection 4.2.4, *All The remaining data* should be *All the remaining data*.
6. In Appendix D.1: *Consider the following example, which has gained popularity* is repeated twice.

### Questions
What if I apply your method to a discrete-domain and discrete-label setting? How well does Appendix D.1's conclusion generalize to other cases? Does that depend on the relative cardinality of $\mathcal{Y}$ and $\mathcal{T}$?

In the introduction, you wrote *to regress over the continuous domain index $t$ using L1 or L2 loss*, but you only mention L2 loss in Section 3. What about the L1 loss?

Is $O(\sqrt{n})$ the slowest rate $|\mathcal{T}|$ can grow with respect to $n$ for REx/IRM to fail with a non-zero probability?

The proof in Appendix F is unclear: (i) the notations are not defined; (ii) the assumption that *each domain only contains one sample* contradicts *assuming we have infinite samples in each domain* in the main text; (iii) last sentence is confusing: did you mean *if $|\mathcal{E}| \ge \frac{\sigma_R \sqrt{n}}{\Delta \mathcal{G}^{-1}(1/4)}$ > 1/4, then REx can not identify the invariant feature with probability 1/4*?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
