# A Lightweight Method for Tackling Unknown Participation Statistics in Federated Averaging

- Decision: Accept
- Scores: 1, 6, 5, 6

## Abstract
In federated learning (FL), clients usually have diverse participation statistics that are unknown a priori, which can significantly harm the performance of FL if not handled properly. Existing works aiming at addressing this problem are usually based on global variance reduction, which requires a substantial amount of additional memory in a multiplicative factor equal to the total number of clients. An important open problem is to find a lightweight method for FL in the presence of clients with unknown participation rates. In this paper, we address this problem by \textit{adapting the aggregation weights} in federated averaging (FedAvg) based on the participation history of each client. We first show that, with heterogeneous participation statistics, FedAvg with non-optimal aggregation weights can diverge from the optimal solution of the original FL objective, indicating the need of finding optimal aggregation weights. However, it is difficult to compute the optimal weights when the participation statistics are unknown. To address this problem, we present a new algorithm called FedAU, which improves FedAvg by adaptively weighting the client updates based on online estimates of the optimal weights without knowing the statistics of client participation. We provide a theoretical convergence analysis of FedAU using a novel methodology to connect the estimation error and convergence. Our theoretical results reveal important and interesting insights, while showing that FedAU converges to an optimal solution of the original objective and has desirable properties such as linear speedup. Our experimental results also verify the advantage of FedAU over baseline methods with various participation patterns.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article tackles the problem of Federated Learning under heterogeneous client participation. The authors propose a correction of FedAvg algorithm which handles heterogeneous participation through estimation of optimal aggregation weights based on client participation history, in a new algorithm called FedAU. Theoretical results are derived, which highlight sub-optimality of classical FedAvg algorithm in this setting, as well as convergence analysis of FedAU. Numerical experiments illustrate the theoretical findings.

I have read the authors response, which thoroughly answered my questions. In this regard, I think the paper is very strong and updated my score accordingmy.

### Strengths
- The paper tackles an important practical limitation on existing FL algorithms, which often depend on a known, homogeneous client's participation rate. 
- The proposed algorithm is original as it tackles client participation heterogeneity using novel methodologies quite different from existing litterature mostly based on variance reduction techniques. In addition, the proposed algorithm enjoys favourable computational complexity compared to existing works.
- The proof techniques are also original and could be reused in other settings
- The paper is very clear and well-written, the problematic, related work and contributions are clearly highlighted, and scientific methodology is easy to follow. In particular, the authors made the effort of stating intuitive results and presenting formal theorems in a user-friendly manner.

### Weaknesses
 - The authors mention that the proof techniques, but I didn't find any sketch of the proof in the main text, which is a shame because it could help readers understand the novelty, and maybe reuse proof techniques.
- The numerical experiments are a bit disappointing in the sense that they do not really highlight how much of the theoretical results are observed in practice, but only that FedAU improves over FedAvg on the proposed use cases. It would have been interesting to see experiments highlighting convergence error for varying values of K or ground truth average participation rates (even on simple simulations)

### Questions
- In practice, what is the order of magnitude of the lowest participation rate that can be estimated? 
- Related question, did you perform any experiments to understand at what point the weights might explode (in the case where K is very large) ?
- It is also likely that clients participation rate pn actually vary over time, while remaining independent across t. Do you think your theoretical results could easily be adapted to such cases ?
- Concerning the theoretical results, using your proof techniques, do you recover existing results in the particular case where pn are homogeneous/known ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the FedAvg algorithm with unknown participation statistics. It first proves that FedAvg with non-optimal aggregation weights can diverge from the optimal solution of the original FL objective. Next, it proposes an adaptive method to estimate the participation weight and come up with the FedAU algorithm that can converge to the desired solution even under the unknown participation statistics. Numerical experiments validate the theoretical findings.

### Strengths
1. It shows that, with unknown participation statistics, FedAvg with non-optimal weight will diverge from the optimal solution of the original FL objective.

2. It proposes an interesting online Algorithm 2 to estimate the unknown participation weight.

3. It proposes FedAU algorithm that can converge to the desired solution even with unknown participation weight.

### Weaknesses
The linear speedup term in Eq.(8) seems unreasonable. According to the FedAvg result in reference [R1] (see Table 2), when only a subset of clients (say S clients) participate in the FedAvg, the linear speedup term should be O(1/sqrt{S*I*T}), not O(1/sqrt{N*I*T}).  I believe O(1/sqrt{S*I*T}) makes more sense since only S clients sample data and participate in algorithm update per iteration.

[R1] Karimireddy et.al., SCAFFOLD: Stochastic Controlled Averaging for Federated Learning, ICML 2020.

Why do you need both bounded variance assumption in (4) and bounded global gradient assumption in Theorem 2? The bounded gradient assumption is typically very restrictive and are not used in literature such as in [R1]. Can the bounded global gradient assumption be removed?

### Questions
1. Please clarify why does your linear speedup term is O(1/sqrt{N*I*T}) not O(1/sqrt{S*I*T}) as shown in reference [R1] with partial client sampling. I think O(1/sqrt{S*I*T}) makes more sense since only a subset of S participates in data sampling and model update per iteration.

2. Why do you need both bounded variance assumption in (4) and bounded global gradient assumption in Theorem 2? The bounded gradient assumption is typically very restrictive and are not used in literature such as in [R1]. Can the bounded global gradient assumption be removed?

### Soundness
3 good

### Presentation
3 good

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
This paper studies the problem of partial participation in federated learning. More specifically, the authors consider the FedAvg algorithm and assume that each client $m$ will participate with some unknow probability $p_m$. The authors show that if we are aiming to optimize the objective in equation (1), the non-adaptive aggregation weight in FedAvg will lead to a solution of optimizing another objective. In addition, the authors propose a new method that can compute the adaptive aggregation weight efficiently, and provide the corresponding convergence rate.

### Strengths
The strengths of the paper:
1. The authors provide a result to show that non-adaptive aggregation weight in FedAvg is bad for optimizing the objective in equation (1).
2. The authors develop an efficient method to estimate the adaptive aggregation weight that can be used in FedAvg.
3. The authors establish the convergence rate of the proposed method which demonstrates the effectiveness of the proposed method.

### Weaknesses
The weaknesses of the paper:
1. There is no (theoretical) comparison with existing baselines.
2. Several conditions in the established results are unclear.

### Questions
I have the following questions regarding the current paper:
1. What are the other baseline algorithms and their corresponding convergence rates?
2. According to Theorem 1, when we have full participation, i.e., $p_n=1$ and $w_n=1$, the objective in (2) will reduce to the objective in (1). Therefore, whether your results will recover the convergence rate of FedAvg with full participation? In addition, when we have partial participation with $p_n=p<1$ and $w_n=1$, the objective in (2) will also reduce to the objective in (1). How will your result look like compared to the existing results?
3. What is the expression on $\Psi_G$ in your theorems?
4. In Corollary 4, what do you mean by sufficient large $T$? Do you mean the results hold only asymptotically?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses a critical issue in federated learning (FL) where clients have varying and unknown participation rates, which can hinder FL's performance. Existing solutions often rely on global variance reduction, which consumes substantial memory resources. The paper introduces a lightweight method called FedAU, which adapts aggregation weights in FedAvg based on each client's participation history. FedAU resolves this problem by adaptively weighting client updates using online estimates of optimal weights, even without knowledge of participation statistics. Theoretical analysis shows that FedAU converges to the original objective's optimal solution with desirable properties such as linear speedup, and experimental results support its advantages over baseline methods in various participation scenarios.

### Strengths
The strengths of this paper's contributions are as follows:

1. The authors introduce a lightweight procedure named FedAU for estimating optimal aggregation weights for each client based on their participation history. This approach supports FL even when participation statistics are unknown, making it highly practical.

2. The paper provides a novel and thorough analysis of the convergence upper bound for FedAU. It employs a unique method to handle weight error in the convergence bound and shows that FedAU converges to the optimal solution of the original objective. Furthermore, it achieves desirable linear speedup in convergence when the number of FL rounds is sufficiently large.

3. Experimental results validate the advantages of FedAU over various datasets and baseline methods, particularly in scenarios with diverse participation patterns, including independent, Markovian, and cyclic patterns. This demonstrates the robustness and effectiveness of the proposed approach.

### Weaknesses
1. The theoretical results in the paper are founded on the assumption of a Bernoulli distribution for client participation. It does introduce an extra layer of specificity that might not hold universally. It would be beneficial for the authors to explicitly state this assumption within the paper, as the current presentation of the four assumptions largely omits this fact.

2. I wonder if there is a potential limitation in scenarios where clients rarely participate in the training process, as seen in cases like cross-device federated learning. In such instances, the online estimation of the aggregation weights (w_t) could be challenging or, at best, very inaccurate.

### Questions
see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
