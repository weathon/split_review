# Diminishing Exploration: A Minimalist Approach to Piecewise Stationary Multi-Armed Bandits

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
The piecewise-stationary bandit problem is an important variant of the multi-armed bandit problem that further considers abrupt changes in the reward distributions. The main theme of the problem is the trade-off between exploration for detecting environment changes and exploitation of traditional bandit algorithms. While this problem has been extensively investigated, existing works either assume knowledge about the number of change points $M$ or require extremely high computational complexity. In this work, we revisit the piecewise-stationary bandit problem from a minimalist perspective. We propose a novel and generic exploration mechanism, called diminishing exploration, which eliminates the need for knowledge about $M$ and can be used in conjunction with an existing change detection-based algorithm to achieve near-optimal regret scaling. Simulation results show that despite oblivious of $M$, equipping existing algorithms with the proposed diminishing exploration generally achieves better empirical regret than the traditional uniform exploration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers stochastic multi-armed bandits with structured nonstationarity, specifically where the arms change value at $M$ points throughout the time horizon $T$ (where $M$ is unknown) but are otherwise stationary. The authors develop a new algorithm to handle the exploration aspect of this problem, which they combine with an existing change-detection algorithm.

They show theoretically that this approach achieves sublinear, $\mathcal{O}(\sqrt{MT})$ regret with computational complexity $\mathcal{O}(KT)$, and show strong empirical performance on a simulator based on a public dataset from Yahoo.

### Strengths
1. Nonstationarity is an important challenge for multi-armed bandits essential to making this approach useful for a broad range of real-world problems. This paper is part of the literature on "active methods" in piecewise-stationary bandits that actively try to detect and adapt to change points. This paper overcomes a limiting assumption in existing work, which is the assumption that the number of change points are known a priori (thus the existing algorithms could tune specifically with that knowledge). This advance could help make MAB solvers with piecewise stationarity more useful.

2. The authors propose a novel approach for exploration, using a "diminishing exploration" approach where the amount of exploration decays with time. This method does not require prior knowledge of the number of change points $M$, and can be paired with a range of existing change detection algorithms. The algorithm moves from an exploration stage, then update initial estimates of $u$, then act following a UCB approach (based on M-UCB), while doing a per-timestep check for change detection. The authors add a heuristic that adds a skipping mechanism (algorithm 2) to ignore potentially unnecessary arms, with a tuning parameter $\eta$ that describes how conservative to be in skipping. 

3. The authors show theoretically that the regret is bounded by $\tilde{\mathcal{O}} \sqrt{MKT})$. This result is found by studying the number of times the optimal arm changes $S$ (referred to as the number of "super-segments").

### Weaknesses
1. The choice to model nonstationarity as a series of piecewise-stationary with a fixed number of change points is not very well justified. What are some examples for why this assumption would arise, rather than a smoother type of nonstationarity? The paper does not discuss the limitations of this assumption, such as the fact that real-world nonstationarity may not always manifest as abrupt changes, but rather as gradual drifts or more complex patterns. This piecewise-stationary assumption may limit the applicability of the proposed method in scenarios where the nonstationarity is more continuous or stochastic.

2. Related to #1, this paper compares to other literature in piecewise-stationary bandits (theoretically and empirically), but there is a greater amount of literature on nonstationary bandits. One possible analysis that could help strengthen the usefulness of this paper is to empirically evaluate your method on more general nonstationary settings, and compare your performance with existing methods for nonstationary bandits. I imagine this would be a more realistic model for the vast array of real-world settings. If you are able to perform well even in those settings, that would be extremely useful. However even if not, it would still be useful to show/quantify. The paper should consider evaluating against algorithms designed for more general forms of nonstationarity, such as those that use sliding window approaches or adaptive learning rates, to better understand the strengths and limitations of the proposed method.

3. Algorithm 2 (the skipping mechanism) is a heuristic approach, but the importance of this heuristic is not studied. It would help to include an ablation to shows the impact of this heuristic --- how much of the improved performance depends on this? The paper lacks a detailed analysis of the skipping mechanism's impact on both regret and computational efficiency. It is unclear how the tuning parameter $\eta$ affects the performance and how to choose an appropriate value for different scenarios. A more thorough empirical study is needed to understand the trade-offs introduced by this heuristic.

4. GLR-UCB seems to perform very similarly with and without your diminishing exploration approach? Same as CUSUM-UCB, with and without diminishing exploration, as T scales and on the Yahoo dataset. The paper does not provide a clear explanation for why the diminishing exploration approach does not lead to more significant improvements in the performance of GLR-UCB and CUSUM-UCB, particularly as the time horizon $T$ increases. The results suggest that the diminishing exploration may not be as effective as expected in these specific settings, and further analysis is needed to understand the conditions under which it is most beneficial.

### Questions
1. Experiments describe that evaluations beyond 20,000 timesteps was infeasible because of long runtime. But Figure 4d appears to show up to $T=200,000$?

2. The M-UCB and GLR-UCB approaches that this algorithm builds off of does not seem to be described? How do they work? What does the "M" in M-UCB stand for?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper revisits a well-studied problem, the piecewise stationary multi-armed bandit problem, and proposes a new exploration scheme, referred to as "diminishing exploration (DE)", which can be used in conjunction with change detection-based approaches. Regret bounds have been developed for the proposed algorithms, and preliminary experiment results are demonstrated in Section 6.

### Strengths
- The paper is well-written and the authors clearly present their main ideas. 

- The diminishing exploration (DE) approach can be applied to many change detection based algorithms.

### Weaknesses
 - This paper seems to lack novelty. The standard piecewise stationary bandits have been extensively studied in the past decade. Also, the main idea of this paper, the diminishing exploration (DE), seems to be quite straightforward.

- There is also not much novelty in the analysis techniques. The regret analyses in this paper seem standard.

- The assumptions in this paper also seem restrictive. For instance, Assumption 4.2 seems both unnatural and unnecessary. It seems that some assumptions (e.g. Assumption 4.2) are from previous literatures, but it is better to get rid of such unnatural and unnecessary assumptions. Can the authors develop regret bounds for DE without such restrictive assumptions? Please explain.

### Questions
Please try to address the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the non-stationary stochastic bandit problem, where the reward distributions of arms can change over time. The challenge is to balance the trade-off between variations in these distributions and following a bandit algorithm to optimize the current reward at each stage. To this end, the paper proposes a new change detection algorithm using a diminishing exploration rate, which can be coupled with existing change detection frameworks and bandit algorithms. The paper provides a theoretical guarantee for the proposed algorithm, demonstrated by an optimal regret guarantee. Additionally, it extends the problem to a specific setting involving arm changes and shows a regret guarantee for this case as well. Lastly, a numerical study with simulation experiments demonstrates significant improvement over existing algorithms.

### Strengths
1. The paper is clearly written and easy to follow. The comparison with existing work in Table 1 is particularly helpful in understanding the contributions of this paper.
2. The proposed diminishing rate is novel in this specific non-stationary bandit setting. In addition, the algorithm does not require knowledge of the total variation and is relatively easy to implement.
3. The claims are well-supported by the theoretical guarantees. Clear explanations of the theorems are provided, aiding in understanding the key takeaways.
4. Extensive numerical experiments are conducted to demonstrate the algorithm’s performance, showing significantly smaller regret compared to existing benchmarks.

### Weaknesses
1. If I understand this paper correctly, one of the main contributions of the paper is that the proposed algorithm does not require knowledge of $M$ and achieves a $\sqrt{MT}$ guarantee and $KT$ computation complexity. One of my major concerns is that, based on Table 1, it seems like (Wei & Luo 2021) has studied the setting without knowledge of $M$, proposing the algorithm Master, which also achieves optimal regret and the same computational complexity. So I am a bit confused by the paper's claim that it studies this novel setting with an optimal guarantee.

2. Additionally, aside from this single parameter change (exploration rate), it would be helpful to understand what other novelties are introduced. Based on the current modification, it is somewhat unclear how the algorithm stands out in terms of novelty.

3. The second concern is about the choice of $\alpha$. It seems like the paper never explicitly states how to choose the parameter $\alpha$, which, however, is key in the algorithm and used in almost all cases. Also, the regret bound has a dependency on $\alpha$. Therefore, without this, it is hard to quantify how we can deploy this algorithm without parameter tuning and how the regret really changes with $T$.

4. The paper lists the statement about the computational complexity in Table 1, which is $KT$. However, it seems like there is no theoretical or formal statement explaining why this is true. A further demonstration would be very helpful.

5. I have a further question: Why not consider the line of work on total variation (TV) in non-stationary bandits? There is a rich body of work in that area.

### Questions
I would kindly refer to the weakness part. I would appreciate the authors' responses to the main points.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper targets piece-wise stationary bandit setting. In this paper, a diminishing exploration mechanism is proposed. Apparently, the mechanism does not require the prior knowledge of the number of stationary segments. This mechanism can be integrated into those algorithms that rely on change point detectors. The authors claim that by using their mechanism in optimizing the forced exploration, they achieve better empirical regret than the traditional forced exploration methods.

### Strengths
Their work is authentic and original.

### Weaknesses
1. Usually in these kind of settings, there is an assumption that sets a minimum distance between any two consecutive change points in the environment. This type of assumption exists to make sure that the change-point-detector-based algorithm have (statistically) enough time to detect any possible change in the environment and hence the algorithm is able to detect any change to the environment. Naturally, this implies that, as we get more distance from a change point in the environment, the probability of facing another change in the environment is more than the time when we were closer to the last change point. Hence we need to collect more samples from various arms to see if there has been a change that makes our current decisions sub-optimal. This argument (which i believe is correct) has contradiction with the nature of your method in decreasing forced exploration as we get distance from the last change point.

2. The experiments section needs to be clarified more by providing more clear information about the setups. Specifically, the parameters used for the baselines and the proposed method are not clearly stated. The description of the environment is also not detailed enough, making it hard to reproduce the results.

3. The number of arms involved in the synthetic data experiment is low and it raises the question about the performance of the proposed technique in scenarios with more arms. The experiments do not explore the performance of the proposed method as the number of arms increases, which is a critical aspect for many real-world applications.

4. The writing of the text is not smooth to follow. It can definitely be improved.

### Questions
The effect of the mechanism is not motivated within the context of real-life applications. For instance, the question i can ask is; in which application scenario reducing this forced exploration can play an important role? you might want to point to applications with large number of arms. Then I can ask; then why do the experiments focus on small number of arms and do not show the performance of the proposed method in scenarios with a large number of arms?

### Soundness
2

### Presentation
2

### Contribution
1
