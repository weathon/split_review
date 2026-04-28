# Differentially Private Federated Learning with Time-Adaptive Privacy Spending

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Federated learning (FL) with differential privacy (DP) provides a framework for collaborative machine learning, enabling clients to train a shared model while adhering to strict privacy constraints. The framework allows each client to have an individual privacy guarantee, e.g., by adding different amounts of noise to each client’s model updates. One underlying assumption is that all clients spend their privacy budgets uniformly over time (learning rounds). However, it has been shown in the literature that learning in early rounds typically focuses on more coarse-grained features that can be learned at lower signal-to-noise ratios while later rounds learn fine-grained features that benefit from higher signal-to-noise ratios. Building on this intuition, we propose a time-adaptive DP-FL framework that expends the privacy budget non-uniformly across both time and clients. Our framework enables each client to save privacy budget in early rounds so as to be
able to spend more in later rounds when additional accuracy is beneficial in learning more fine-grained features. We theoretically prove utility improvements in the case that clients with stricter privacy budgets spend budgets unevenly across rounds, compared to clients with more relaxed budgets, who have sufficient budgets to distribute their spend more evenly. Our practical experiments on standard benchmark datasets support our theoretical results and show that, in practice, our algorithms improve the privacy-utility trade-offs compared to baseline schemes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach for DP FL wherein instead of making the clients spend the privacy budget uniformly over all communication rounds, as in traditional DP FL approaches, the clients allocate their privacy budgets non-uniformly over time. Specifically, the method suggests that clients save their privacy budgets in early communication rounds since coarse-grained features are learnt in early rounds and spend more in later rounds where more fine grained features are learned.

### Strengths
1. The approach is novel and intuitive.
2. The privacy analysis of the algorithm is provided.

### Weaknesses
1. Insufficient experimental evaluation - Only two datasets and baselines are considered.



### Questions
1. What is the $\delta$ for experiments in Table 1 and Figure 2? Can you elaborate on why such an high $\epsilon$ in 10, 20, 30 is acceptable? How many number of communication rounds are considered?

Minor:
1. Clearly defining notations, and relationships between different notations would make paper easier to understand, like DP to RDP mapping.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies federated learning with distributed differential privacy, where each client adds noise to its model update/gradient before sending to the server, and a trusted server aggregates the noisy updates for an overall $(\epsilon,\delta)$ aggregated model. The authors point out that the early rounds are less sensitive to noise while later rounds are heavily affected by the introduction of noise. Hence, the paper proposes that privacy budget can be saved in early rounds so that the later rounds can spend more privacy budget as they need it more. To achieve this, the paper proposes to use a lower sub-sampling rate in earlier rounds and normal sampling rate in the later rounds/spending rounds. The paper proves that given a set of sampling rates, one can optimize the assignment of these sampling rates to clients (based on their personalized privacy budget) to minimize an upper bound of the expected clipping bias. Empirical evaluation shows that spend-as-you-go achieves higher performance under the same privacy budgets.

### Strengths
* Improving the performance of DP-FL is an important and interesting problem
* The adaptive spending scheme is intuitive and well motivated
* Theoretical analysis provides insights on the algorithm and bounds the expected clipping bias
* The paper is well written and easy to read

### Weaknesses
 * In section 3, the algorithm for the spend-as-you-go budgeting scheme and the FL training loop are described in great details. However, the motivation of each design choice is not clearly explained. I suggest the authors to edit the section to include explain the rationale behind each design choice that defers from the conventional FL algorithm.
* The configuration of the hyperparamters of the proposed method are not explained. For example, how are the set of lower sampling rates determined? Why do we choose the values presented in the Appendix? Also, how is the switching round $T_n$ chosen?
* The paper could benefit from additional experiments.
  * I would like to see the empirical evaluation on the effects of the set of sampling rates and the switching time.
  * I suggest the authors to also include the non-private baseline in the figures for reference.
  * If I understand correctly, the proposed adaptive spending scheme also works for non-personalized FL (all clients share the same budget) as well as non-FL (i.e., DP-SGD). Will the spending scheme also bring performance improvements? It would be interesting to see how the proposed scheme would perform in these settings.

### Questions
I raise a few questions in the earlier section of weaknesses when I list my concerns. I would appreciate it if the authors could address the questions listed above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of heterogeneous client-level DPFL with non-uniform privacy expending across time (and clients). The reasoning behind the idea is that, as claimed, saving privacy budgets in early rounds lets clients with stricter privacy requirements (with smaller clipping threshold or larger noise scales) spend privacy unevenly across rounds compared to clients with more relaxed privacy requirements. This enables them to spend more privacy in later rounds when more fine-grained features are learned.

### Strengths
* The problem of time-adaptive privacy spending is interesting. 
* The existing related works are mentioned and discussed clearly.

### Weaknesses
There are multiple weaknesses in the  work as mentioned below.

* The current writing of the draft is hard to understand, and requires one to read it multiple times to get a clear understanding of the work.
* There are some big assumptions that make one to hesitate about the applicability of the work. 
* Some of the theoretical analysis seem to be incorrect (see the questions below).
* The existing close algorithms (e.g., adaptive clipping threshold) are not evaluated.  
* The existing datasets in the experimental results are pretty simple (MNIST and FMNIST). Running experiments with more complex datasets, e.g., CIFAR10/100, will improve the work.

### Questions
I ask the following questions based on their order in the draft.

* In line 169, the authors claim that it is unfair to compare with the adaptive clipping methods. However, these methods are proposed for reducing the noise level as the training continues, and are directly related to the goal of this paper, even more than IDPSGD-based method (I-DPFedAvg). As such, comparison to these baselines is crucial. Also, they have proposed some methods for reducing the extra privacy leakage for tuning clipping thresholds adaptively. So there is no barrier for comparing the proposed method with them. 

* The privacy analysis done in alg.1 is performed **before** training starts. It gets $c$, $q$, $\{q_n\}$, $\{M_n^t\}$ and $T$ all as hyperparameters, and as output, returns $\{q^t\}$, $\{q_n^t\}$, and $\{c_n^t\}$. First, having this many hyperparameters before training is unrealistic and makes the applicability of the proposed method limited indeed. Second, I think the privacy analysis in alg1 is incorrect. The reason is that a client can compute the amount of privacy that it has spent **only after each round that it really participates** in the FL. The value of sampling rate $q_n^t$ implicitly determines the number of times the client $n$ participates during the total $T$ rounds. It is impossible to account for the amount of privacy a client spends before even starting training. What if simply out of randomness, the client $n$ turns out to participate in all rounds $T$ (as if its sampling rate $q_n^t$ was 1 for all $t$). How do you explain about this scenario? How can you claim that you can always run alg.1 before even starting the training, and return the set of $q_n^t$ based on its result?


* The threat model considered is based on having "honest-but-curious" clients and "honest" server. How does the analysis in your paper and the proposed method work if you consider an "honest-but-curious" server? For instance the very recent work [1] below also aims at improving utility in the system by a noise-aware aggregation (it should be added to your related works). Does your algorithm work in this threat model too?

"Noise-Aware Algorithm for Heterogeneous Differentially Private Federated Learning", ICML 2024 (https://arxiv.org/pdf/2406.03519v3)

* How do you determine the set $\{q_n^t\}$ and $\{M_n^t\}$ in your experiments? Especially, where is the latter coming from?

Some minor comments:
* line 119 and 122: $(\epsilon, \delta)$-DP is the common notation
* line 137: provide a brief introduction to SGM
* the order of lines 14 and 15 in alg1 should be exchanged.
* line 6 in alg2 needs "5"inputs (one input is missing)

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
This paper proposes a differentially private federated learning algorithm with flexible noise injected over the training time. They do so by manipulating the client sampling rate: smaller rate for the first course of the training (saving phase) and larger rate for the later part of the training (spending phase). The author intensively analyzes the privacy accounting for both phases and shows how to select the optimal client sampling rate.

### Strengths
1. The idea of cutting down the privacy budget spent in the early training phase is fascinating and quite new.
2. Extensive theoretical analysis of the proposed method is given.
3. Experimental results show a moderate amount of privacy budget saved throughout the training, supporting the proposed mechanism.

### Weaknesses
Limited empirical comparison with other adaptive differential privacy methods.

### Questions
1. When do clients decide to switch from privacy saving to spending phase? 
2. Is the data sensitivity taken into account when computing the differential privacy noise scale?
3. Would model heterogeneity be a challenge with the proposed algorithm?

### Soundness
3

### Presentation
3

### Contribution
3
