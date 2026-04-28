# Neural Dynamic Pricing: Provable and Practical Efficiency

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Despite theoretical guarantees of existing dynamic pricing (DP) methods, their strong model assumptions may not reflect real-world conditions and are often unverifiable. This poses major challenges in practice since the performance of an algorithm may significantly degrade if the assumptions are not satisfied. Moreover, many DP algorithms show unfavorable empirical performance due to the lack of data efficiency. 
    To address these challenges, we design a practical contextual DP algorithm that utilizes regression oracles. Our proposed algorithm assumes only Lipschitz continuity on the true conditional probability of purchase.
    We prove $\tilde{\mathcal{O}}(T^{\frac{2}{3}}\text{regret}_R(T)^{\frac{1}{3}})$ regret upper bound where $T$ is the horizon and $\text{regret}_R(T)$ is the regret of the oracle. The bound is nearly minimax optimal in the canonical case of finite function class, and our analysis generically applies to other function approximators including neural networks. To the best of our knowledge, our work is the first algorithm to utilize the powerful generalization capability of neural networks with provable guarantees in dynamic pricing literature.
    Extensive numerical experiments show that our algorithm outperforms existing state-of-the-art dynamic pricing algorithms in various settings, which demonstrates both provable efficiency and practicality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a contextual dynamic pricing algorithm called DP-IGW, which aims to address some of the limitations in the existing dynamic pricing literature, such as strong modeling assumptions or poor performance under real-world conditions. 
The idea of DP-IGW is to leverage regression oracles (in particular, neural networks) to enable contextual dynamic pricing.
The main assumption is that the function $f^\star$ that maps the contexts $x$ and prices $p$ to the probability of selling at a price $p$ when the context is $x$ is uniformly Lipschitz in the prices (Assumption 5.2 --- note that it is assumed that the same $L$ works for all contexts).
The authors prove that the algorithm achieves an upper regret bound of order $T^{2/3} \mathrm{Regret}_R(T)^{1/3}$, where $\mathrm{Regret}_R(T)$ is the regret after $T$ time steps of the regression oracle used by DP-IGW. 
The regret rate is proved to be optimal only in the special case where $f^\star$ belongs to a known _finite_ family and the regression oracle only outputs regressors in this family.
Experiments illustrate the theoretical findings.

### Strengths
- The paper is mostly clear in its descriptions, presenting both algorithmic and theoretical insights with sufficient effectiveness.

- The problem is of broad interest, and the idea of mixing neural network technology with dynamic pricing is appealing.

### Weaknesses
The originality of the contribution appears somewhat limited, given that the key ideas are adaptations of somewhat standard techniques. This is not necessarily a reason to reject a paper. In fact, it could even be a plus to have a simple change that leads to a large improvement. It is not clear to me that this is the case here, though. The lower bound near-matches the upper bound only in a very narrow case (finite $\mathcal F$), and I am not sure about the optimality of this approach in the general case. The algorithm's reliance on a uniform Lipschitz constant across all contexts is also a potential limitation. While the authors assume that the same $L$ works for all contexts, this may not hold in many real-world scenarios, where the sensitivity of demand to price changes can vary significantly depending on the context. This assumption could lead to suboptimal performance in cases where the Lipschitz constant varies widely across different contexts. Furthermore, the practical implications of the theoretical results are not fully clear. While the authors provide an upper bound on the regret, the bound involves the regret of the regression oracle, which may not be readily available or easily interpretable in practice. This makes it difficult to assess the practical performance of the algorithm in real-world scenarios.

### Questions
- I suggest the authors close the gap between the upper and lower bound in the general case, or at least in a significantly broader case.

- Can the assumption be relaxed to: for all contexts $x$, there exists a Lipschitz constant $L_x$ such that $f^\star(x,\cdot)$ is $L_x$-Lipschitz? What about piece-wise Lipschitz?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper designs a practical contextual DP algorithm that utilizes regression oracles. Our proposed algorithm assumes only Lipschitz continuity on the true conditional probability of purchase. It proves a $O(T^{2/3} reg_R(T)^{1/3})$ regret upper bound which is nearly minimax optimal in the canonical case of finite function class. Numerical experiments are conducted to verify the theory.

### Strengths
1. the presentation is clear.
2. the author provides both theoretical and experiments to verify their results.

### Weaknesses
The novelty is not enough.
- Recent works have already considered using function approximation (e.g. [1]), so replacing such semi-parametric / non-parametric regression oracles with neural networks is not meaningful enough.
- The authors state that their algorithm is fully sequential and flexible w.r.t. model assumptions, but both issues are tackled in the bandit settings, e.g., [2]. Since DP and bandits are extremely similar in problem structures, this paper is merely a combination of the two techniques and is not of much real significance.
- The paper does not compare its assumption and regret with previous works, so no superiority of the proposed algorithm is illustrated.
- The experiment does not highlight under which circumstances will it perform better than other models (e.g. log concavity of cdf $F_0$).

### Questions
No questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses limitations in current dynamic pricing (DP) algorithms, particularly those that rely on assumptions unfit for real-world applications and show poor data efficiency. The authors propose a new algorithm, DP-IGW, which incorporates neural networks as regression oracles and employs an exploration method called inverse gap weighting (IGW) to enhance data utilization and adaptability. Their method assumes minimal model assumptions, specifically Lipschitz continuity, and provides nearly optimal regret bounds, demonstrating both theoretical and practical efficiency across various settings.

### Strengths
1. By using neural networks as regression oracles, DP-IGW leverages their powerful generalization capabilities, allowing it to adapt to complex, high-dimensional data while maintaining provable guarantees.
2. The paper is technical sound. The authors provide a near-optimal regret bound, which establishes the efficiency and reliability of DP-IGW in theory. 
3. The paper is well-written. The authors have a good summary of the current literature.

### Weaknesses
1. The design ideas and proof techniques seem to be very similar to Simchi-Levi and Xu (2022). Is there any technical challenge and contribution that the authors want to highlight?
2. For the lower bound (Section 5.2), I am wondering the purpose of the section. Usually, we are expecting a matched lower bound with the upper bound as Simchi-Levi and Xu (2022). The lower bound in Section 5.2 does not directly match with the upper bound, and even under different assumptions (i.e., the difference between Assumption 5.2 and Assumption 5.4). Does this mean that it is very hard to directly get a lower bound under Assumption 5.2?
2. Although the use of neural networks offers powerful generalization, it also introduces challenges like potential overfitting, sensitivity to hyperparameters, and higher computational demands. I will not push along this line, but want to point out this since the paper is a very practical relevant paper.

### Questions
Please see the weakness above.

### Soundness
3

### Presentation
3

### Contribution
3
