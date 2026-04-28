# Impact of Agent Behavior in Distributed SGD and Federated Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Distributed learning has gained significant interest recently as it allows for the training of machine learning models across a set of *heterogeneous* agents in a privacy-preserving manner with the growing amount of distributed data. In this paper, we conduct an asymptotic analysis of Generalized Distributed SGD (GD-SGD) under various communication patterns among agents, including Distributed SGD (D-SGD) and its variants in Federated Learning (FL), as well as the increasing communication interval in the FL setting. We examine the influence of agents' sampling strategies, such as *i.i.d.* sampling, shuffling methods and Markovian sampling, on the overall convergence speed of GD-SGD. We prove that all agents will asymptotically reach consensus and identify the optimal model parameter, while also analyzing the impact of sampling strategies on the limiting covariance matrix that appears in the Central Limit Theorem (CLT). Our results theoretically and empirically support recent findings on linear speedup and asymptotic network independence, and generalize previous findings on the efficient Markovian sampling strategies from vanilla SGD to GD-SGD. Overall, our results provide a deeper understanding of the convergence speed of GD-SGD and emphasize the role of *each* agent's sampling strategy, moving beyond a focus on the worst-case agent commonly found in existing literature.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides an asymptotic convergence analysis of generalized distributed SGD (i.e., with a time-varying communication graph, c.f., Kolosokova et al.). It underlines the dependence of the limiting covariance matrix on each client's data-sampling strategy. The paper's main contribution is identifying that while non-asymptotic analyses of GD-SGD using Markovian sampling rely on the mixing time of the worst agent, the asymptotic analysis can benefit from every agent (not just the slowest one), improving their sampling strategies (c.f., Corollary 3.4). Simulations are provided to judge how quickly optimization enters the asymptotic phase and whether client sampling strategies affect the convergence rate.

### Strengths
The paper is well-written, and the results are rigorously discussed. The paper highlights an essential difference between asymptotic and finite time bounds and how the latter might sometimes be misleading while looking at client sampling strategies. While the idea of looking at asymptotic regimes and Markovian sampling is not new (as can be seen in Table 1), the paper offers an interesting insight.

### Weaknesses
I thank the authors for their detailed response. I have gone through the responses and the other reviews. I have decided to retain my score. I believe there are additional technical challenges over previous works, such as dealing with consensus error and non-iid sampling. But again, any extension of serial results to the distributed setting must deal with that analysis. So overall, my impression is that the work closely builds on existing tools in the literature. I appreciate the asymptotic viewpoint and concede that the algorithms presented hit the asymptotic regime in the experiments, thus making it worthwhile to study the regime. 

Regarding the experiments, the current experiments do validate the theoretical results, when the local steps are not growing, using $a=0.9$. However, why do the authors use this step size when logarithmically growing the local steps? Overlooking this issue, I would have liked to see how other step-size schemes pan out. In particular, if the step size were tuned optimally (i.e., tuning $a$) for each instance for a fixed number of time steps, I would imagine shifting the asymptotic regime for different instances. This could, in turn, change the relative performance of different sampling schemes. The non-convex experiments offered in the appendix are very "convex-like", and it would be good to have more comprehensive experiments using even a simple neural network. Finally, the simulation doesn't have data heterogeneity. I believe this makes it harder to comprehend the differences between the agents, which the paper claims is a benefit of the asymptotic analysis over the non-asymptotic one.

The authors write in response to the reviewer qxNb: 

> The core of our contribution lies in the generality of our model and the unified results we offer within the broad framework of decentralized learning, where we uncover that the sampling strategy of each individual agent affects the overall performance while the effect of communication pattern contributes only via its leading eigenvector (stationary distribution) under the most general setup.    

In the current write-up, this takeaway is obfuscated by the technical results. The discussion below corollary 3.4 can be revised with more examples. This relates to the limitation that the authors do not discuss the practical relevance of their results. Which federated learning applications can benefit from non-iid sampling, or where can the Markovian sampling suggested in this paper be implemented efficiently? Is there a natural decentralized setting where this is possible? What is the additional computational cost of doing this? How can this be implemented in online settings where the data is not stored on the device? Some of these questions might have simple answers, but providing this context is important, otherwise, the work comes off as a mechanical composition of two existing techniques: asymptotic analyses and consensus error-based analyses---something most reviewers have complained about. While there is not much time left in the discussion period, hopefully the authors can address these issues in their revision.

### Questions
- Can the authors comment on technical comparison to related works, as I mentioned above? 
- What were the technical challenges of going to the distributed setting from the known serial analyses? Are any novel techniques needed? Theorem 3.2 seems like a corollary for an existing result.
- What is the step-size schedule in the experiments?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work revolves around distributed learning and specifically studies  the asymptotic behavior of Generalized Distributed Gradient SGD under various communication patterns and sampling strategies. The authors provide theoretical results showing asymptotic consensus convergence across clients and analyze the impact of different sampling strategies on the limiting covariance matrix. Those results provide useful insights and the generalized framework under consideration incorporates numerous results as special cases such as SGD and Distributed SGD. Experimental results on CIFAR10 further support the theoretical findings.

### Strengths
-This paper studies an interesting framework in distributed learning. Analyzing the Generalized Distributed SGD provides useful insights and the derived theoretical results are aligned with the results from numerous prior works (observed as special cases).

-The importance of sampling strategies for the convergence rate is being explored as well as different communication patterns in Generalized Distributed SGD.

### Weaknesses
 -The theoretical results of this paper appear to be straightforward extensions of existing works (Morral et al., 2017; Koloskova et al., 2020; Hu et al., 2022). As a result the theoretical contribution, novelty and impact of this work appears to be marginal.

-The analysis although insightful is asymptotic in nature which somewhat diminishes the impact of the results. The asymptotic convergence results, while mathematically sound, do not provide practical guidance on the convergence rate in finite time, which is crucial for real-world applications. The lack of finite-time analysis limits the applicability of the theoretical findings.

-Although, there is extensive description on how the current findings are aligned with known results, the authors do not emphasize enough on the new challenges they had to overcome in order to derive their theoretical results or discuss how their work is more challenging from related works. The paper needs to clearly articulate the specific technical hurdles that were overcome to achieve the generalized framework and the novel aspects of the analysis compared to existing literature.

-The structure of the introduction could be improved curving out a related work section.

-The experimental results provided are limited to the CIFAR10 dataset. The paper lacks experiments on diverse datasets and model architectures, which limits the generalizability of the empirical findings. The experiments should include a broader range of datasets and models to demonstrate the robustness of the proposed approach.

### Questions
See weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript studies the asymptotic convergence of a generalized distributed SGD method (GD-SGD) for distributed leaning problem. The authors consider various communication patterns and different sampling strategies, including iid sampling and Markovian sampling, for GD-SGD. They show the influence of sampling strategies on the limiting covariance matrix according to the definition of Loewner ordering, which is also examined in a regularized logistic regression task.

### Strengths
1. The authors analyze the asymptotic convergence of the D-SGD algorithm under more general communication topologies and different sampling strategies including iid sampling and Markovian sampling. The theoretical analysis seems solid.

2. The paper is well-written and easy to follow.

### Weaknesses
1. There have been many studies on communication topology in existing work, e.g., [Koloskova et al. (2020), Wang et al. (2021)]. Generally speaking, as long as assumption 2.5 is made, the consistency of the distributed learning algorithm can be guaranteed, so the GD-SGD algorithm designed in this paper is not novel. The paper's contribution in this aspect is incremental, as the consistency under Assumption 2.5 is a well-established result in the field of distributed optimization. The authors do not sufficiently highlight the novelty of their specific algorithm within the broader context of existing distributed SGD methods with similar consistency guarantees.

2. Technically, the main proof techniques used in the paper can be found in [Li et al. (2022)] and [Hu et al. (2022)], except for the expansion of the communication patterns. Therefore, combined with the first weakness, the technical contribution of the paper is insufficient. The extension to more general communication patterns, while valuable, does not represent a significant leap in proof techniques. The core arguments and mathematical tools employed appear to be largely adapted from the cited works, and the paper does not introduce fundamentally new analytical approaches.

3. The analysis and comparison of different sampling strategies in Cor. 3.4 are trivial. The authors only give a qualitative comparison of different sampling strategies based on existing work [Hu et al. (2022)]. In fact, this simple relationship can be easily generalized in existing works with both asymptotical and non- asymptotical results. From this point of view, the contribution of this article seems to be over-claimed. The comparison lacks depth and does not provide new insights beyond what is already known. The authors should have provided a more rigorous quantitative analysis of the different sampling strategies, rather than relying on qualitative comparisons.

4. Logistic regression is a toy model, it is better to further consider other real-world models.

### Questions
One of the key concern of the reviewer is on the fundamental difference in proof techniques compared to [Li et al. (2022)] and [Hu et al. (2022)]; the authors should properly address this. 

Another concern of the reviewer is that the results established in this paper are in an asymptotic sense; can these results be extended to non-asymptotic ones?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
