# LNUCB-TA: Linear-nonlinear Hybrid Bandit Learning with Temporal Attention

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Existing contextual multi-armed bandit (MAB) algorithms struggle to simultaneously capture long-term trends as well as local patterns across all arms, leading to suboptimal performance in complex environments with rapidly changing reward structures. Additionally, they typically employ static exploration rates, which do not adapt to dynamic conditions. To address these issues, we present LNUCB-TA, a hybrid bandit model that introduces a novel nonlinear component (adaptive $k$-Nearest Neighbors ($k$-NN)) designed to reduce time complexity, and an innovative global-and-local attention-based exploration mechanism. Our method incorporates a unique synthesis of linear and nonlinear estimation techniques, where the nonlinear component dynamically adjusts $k$ based on reward variance, thereby effectively capturing spatiotemporal patterns in the data. This is critical for reducing the likelihood of selecting suboptimal arms and accurately estimating rewards while reducing computational time. Also, our proposed attention-based mechanism prioritizes arms based on their historical performance and frequency of selection, thereby balancing exploration and exploitation in real-time without the need for fine-tuning exploration parameters. Incorporating both global attention (based on overall performance across all arms) and local attention (focusing on individual arm performance), the algorithm efficiently adapts to temporal and spatial complexities in the available context. Empirical evaluation demonstrates that LNUCB-TA significantly outperforms state-of-the-art contextual MAB algorithms, including purely linear, nonlinear, and vanilla combination of linear and nonlinear bandits based on cumulative and mean rewards, convergence performance, and demonstrates consistency of results across different exploration rates. Theoretical analysis further proves the robustness of LNUCB-TA with a sub-linear regret bound.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces LNUCB-TA, a contextual multi-armed bandit model that combines adaptive k-Nearest Neighbors with LinUCB along with adaptive exploration rate, provide sub linear regret guarantee and measure empirical performance against standard bandit algorithms.

### Strengths
- The paper's presentation and clarity is good.
- To the best of my knowledge, the proofs in the main paper seem fine.

### Weaknesses
1. One of my main concerns is the implicit reward structure in eq (1). The authors assume that the true expected reward is a sum of a linear and the average of the rewards of a set of nearest neighbors. It should be noted that the k-Nearest Neighbour UCB (Reeve et al., 2018) did not assume such a decomposition, but rather make a margin and lipschitz assumption (see Assumption 1 and 3 in (Reeve et al., 2018)). Why do the authors need to make such a restrictive assumption?

2. In the *Existing Gaps and Intuition* section the authors say "Linear models, constrained by static parameter updates, often fail in scenarios with inherently nonlinear relationships between contextual features and rewards." However the authors do not discuss a series of works in non-linear bandits (see [1],[2],[3],[4],[5],[6],[7], [8],[9],[10]) and the author's contribution with respect to these works.

3. The authors talk about temporal or time-dependent changes in the reward, but do not again discuss the development in non-stationary bandits or discuss why those solutions are not effective in the current scenario (see eg. https://proceedings.mlr.press/v75/luo18a/luo18a.pdf, https://proceedings.mlr.press/v99/chen19b.html, https://arxiv.org/abs/2310.07786 and the references therein).

4. Since the authors stress upon non-linearity of reward functions, there are missing benchmarks in the Experiments Section specifically with respect to NeuralUCB [5], Neural Thompson Sampling [6], Neural SquareCB/FastCB [7], Neural-Linear [3].

### Questions
- Could the authors clarify why they make the specific restrictive assumption on the reward function in eq (1), specifically in the context of existing algorithms for non-linear reward functions?

- Could the authors specify in more detail how their solution differs from the k-Nearest Neighbour UCB (Reeve et al., 2018) along with a detailed explanation of the following sentence from Existing gaps and intuition: "While nonlinear approaches like k-NN-based models (Reeve et al., 2018) offer flexibility, they often struggle with computational efficiency and adaptability in dynamic environments."

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the problem of contextual bandits and develops a novel UCB style algorithm leveraging linear relationship between contextual features and reward for each arm along with non-linear estimation with k-NN . The developed algorithm addresses some important limitations found in existing algorithms like LinUCB that relies on linear relationship between the context in the reward formulation. By introducing an adaptive k-Nearest Neighbors that adjust with reward variance LNUBC TA encompasses the non-linearity that is computationally not explosive. Along with dynamic exploration term, LNUCB seem to perform much better than available state of the art algorithms in contextual MABs. The authors also provided theoretical regret guarantees which achieve sub-linear regret bounds.

### Strengths
1.	This work addresses the issue of computational efficiency when dealing with non-linearity in the contextual features which is an essentially an important component in the usage of these algorithms in real-world scenarios. Generally, most of the existing approaches to solve the non-linear relationship between contextual features and reward including KNN-UCB are computationally expensive and LNUCB-TA tend to solve the time complexity issues commonly associated with nonlinear models

2.	The work presents a solid theoretical guarantee in the form of regret to match the theoretical performance of the existing algorithm with its sub-linear regret bound. Thus, showcasing its solid performance.

3.	The work also presents a strong empirical result in various regimes with multiple datasets to showcase its performance in real-world scenario.

4.	The authors also provide a detail regarding the criteria’s for k-selection that is intuitively based on the variance in rewards for each arm at time $t$ thereby solving the previous gaps found in KNN-UCB and other algorithms.

### Weaknesses
1.	Though the problem setting is interesting, the paper studies the contextual MAB problem, it is an incremental work extending the basis of LinUCB and KNN UCB with the inclusion of adaptive KNN as the non-linear factor in the reward estimation.

2.	The work doesn’t include any results corresponding to the sample complexity of this algorithm to understand the sampling regiment. 

3.	The work also doesn’t include any detailed regret comparison to other algorithms that exist in the contextual Multi armed bandits problem space.

### Questions
1.	The concept of UCB itself involves considering the unit reward (total reward/ no of selection). What additional information does temporal attention brings to the estimated quantity in decision making and how do they differ? This can help understand the temporal attention term better.

2.	The work compares its empirical performance to LinUCB, LinUCB with KNN etc., however a detailed comparison of LNUBC TA ‘s theoretical regret bound guarantees with the aforementioned algorithm is not discussed. Having those details can help better understand the theoretical performance guarantees.

3.	The empirical evaluation focuses mainly on recommendation systems and network exploration. How would the model perform in other domains with different reward structures, such as healthcare or finance?

4.	Also, the algorithm seems to rely heavily on the fixed weight between linear and nonlinear components in the measuring quantity. Does this limit the performance of the algorithm in specific regimes? If so, a detailed discussion on it will help bring more clarity to those. Also, would it be possible to make the weight some form of a tunable parameter? 

5.	K-NN relies on the dimensionality of the context features. What happens when the contextual features are large enough that it suffers from large dimensional space. There seem to be no sufficient details on the potential limitations in high-dimensional feature spaces. Could you include more details about this?


6.	$f_a$ uses the observed rewards from $za_t$ for closest neighbors a_{k,t} in terms of context similarity based on Euclidian distance. Why was Euclidian distance metric chosen?

7.	Also, how does it react when there are many irrelevant features in high-dimensional context as it uses Euclidian ball?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work studies the contextual bandit problem with an introduction of k-NN designed to introduce nonlinearity and temporal dependency into the reward function. A set of theoretical analysis (regret upper bound) and experimental results is provided.

### Strengths
- The idea of introducing k-NN's to leverage inner structures (i.e., similarity) between arm contexts is an interesting direction. I appreciate the author's effort in this to introduce additional nonlinearity into the system.

- The overall writing and presentation (not from a technical perspective) is satisfying. 

As I do have many confusions over the setting and problem itself, I would love to hear clarifications from the authors to further judge this work.

### Weaknesses
I am currently holding many confusions over the setting of this work, and thus not readily at a stage to judge this work. I will take a deeper look into the technical contributions after I found myself understood the basics.


Major questions:
1. The reward defined in Eqn. (1) is weird to me in the sense that as an expected reward, it would depend on historically pulled arms and randomly realized reward through the k-NN function. I have not seen similar formulations in the bandit studies, including the previous k-NN UCB paper (Reeve et al., 2018), where I think the k-NN is not a part of the expected reward.

2. With that, is the $\mu_t^a$ vector unknown while also time-varying in Eqn. (1) given the subscript $t$?

3. Is the exploration-exploitation tradeoff discussed around Eqn. (2) a part of the formulation or algorithmic design?

4. The optimal action can also be defined with more clarity. In particular, for each arm, Eqn. (3) says there is an optimal context; however, is the context generated by environment, or is the context (instead of the arm) that the player is selecting (if so, I do not see context selection in the algorithm)? Also, I found no definition of the decision space $D$.

5. The regret definition in Eqn. (4) and its expansion in Eqn. (6) to connect with the single-step regret in Eqn. (5) is work worth debating: Eqn. (5) is measured with respect to the randomly realized reward $Y$, while Eqn. (5) is with respect to the expected rewards? Hopefully the authors can explain Eqn. (6) a bit better, especially clarify the notations.

6. It seems that I found no description of the estimation of $\mu_t^a$ anywhere in the algorithm?

7. Section 3.2 seems to be about selecting a proper $k$ for k-NN; however, is k a parameter that given in the reward defintion?

8. Also, I in general did not understand the purpose of Theorem 2, i.e., what is its statement?

Minor questions:

9. The notations of $\hat{Y}$ and $Y$ are used in a mixed way in Section 2.

### Questions
Please refer to weakness. I would love to re-examine this work with the questions addressed.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies a type of contextual bandit where the reward model is a mixture of linear and non-linear components. The non-linearity is captured by k-NN part, k-NN denotes the Nearest Neighbor. More formally, upon sampling an arm $a$ the observed reward is  $\hat{Y}\_t^a=o\_t^a\left(x_t, z_t\right)+\xi_t^a$, where $o\_t^a\left(x_t, z_t\right) = \mu\_t^a \cdot x_t^a+\mathrm{kNN}_{k, t}^a\left(x_t^a, z_t^a\right)$ and $z_t$ can be thought of as a nearest neighbor to $x_t$ which yields a similar reward in expectation to $x_t$. A motivating example that the paper gives is the traditional online recommendation system where the above linear component captures broad trends, such as higher click-through rates, while the adaptive k-NN component refines this by recognizing local patterns. They claim that the previous contextual bandit approaches cannot handle the mixture model (with the adaptive k-NN component) and so they propose a LNUCB-TA algorithm. The algorithm is mainly a LinUCB/UCB type algorithm where the confidence interval $U C B\_t^a=\left(\alpha\_{N_t^a}\right) \cdot \sqrt{\left(x_t^a\right)^{\top}\left(\Sigma\_t^a\right)^{-1} x\_t^a}$ has an attention component $\alpha\_{N_t^a}$. The $\alpha\_{N_t^a} $ basically interpolates between the global reward average $g$ and number of times each arm is sampled (I will discuss this again). They provide a regret bound in Theorem 1, and show that LNUCB-TA regret scales as $R\_T=\tilde{\mathcal{O}}(\sqrt{d T})$. Finally, they empirically validate their result against several benchmarks in real datasets.

### Strengths
1. This paper studies a new type of contextual bandit with mixture models. To my knowledge, this is somewhat novel.
2. The proposed UCB-type algorithm seems a valid approach. However, I have some concerns with the constants involved (to be discussed in the questions).
3. They theoretically analyze the algorithm and show it achieves sub-linear regret.

### Weaknesses
1. The paper needs to improve its writing significantly. The assumptions are mentioned in the Appendix. Please state them in the main paper, and a discussion on why they are important, The definition of BALL is mentioned in the appendix. I could not find the definition of the $\beta_t$ as well. Please point to it. These things will make the paper more readable in the next version.
2. The motivation is not clear to me. This requires a more detailed explanation. See my question 1.
3. The attention of the UCB requires more explanation. It is not clear to me how tight it is. Also how it reflects on the regret bound. See my question 2.
4. There are many questions on the theoretical proof of Theorem 1 as well as the technical novelty. I have some doubts regarding the approach. See my question 3.
5. How some of the linear contextual baselines are implemented is not clear from the draft.

### Questions
1. Why an adaptive kNN component is needed for linear contextual settings? The paper starts with a statement (line 75-76) "Despite advancements in MAB algorithms, existing algorithms predominantly fail to incorporate adaptive strategies for reward estimation as a function of the context." I am not sure I fully follow this. There are papers on kernel-UCB which uses reward estimation as a function of context "Finite-Time Analysis of Kernelised Contextual Bandits, Valko et al, 2013" or Neural UCB papers, or Collaborative Neural UCB papers that extend this idea to non-linear contextual settings, What is k-NN specifically bringing to the table when such models exist?
2.  The attention is basically defined as $\alpha_{N_t^a}= \frac{\alpha\_0}{\left(N_t^a+1\right)} \cdot\left(\kappa g+(1-\kappa) n\_t^a\right)$. Consider $\kappa = 1/2$, $\alpha\_0 = 2$, assume the average of global rewards $g \approx n_t^a$, then $\alpha_{N_t^a} \propto 1/\left(N_t^a+1\right)$. This is a very fast decay of UCB. So it is not clear to me how this is actually helping the exploration. Also not clear to me how you set $\kappa$.
3. In Theorem 1, it is not clear to me how the $\alpha\_{N\_t^a}$ is showing up in the proof. I suggest you write a more in-depth proof overview as the current proof overview from lines 376-386 is insufficient. How does the $\kappa$ not appear in the proof? In your Corollary 1, you state that $\Sigma\_t^a=$ $\left(X\_t^a\right)^T X\_t^a+\lambda I$ is the covariance matrix (Lattimore \& Szepesvári, 2020, equation 20.1) updated for arm $a$. However, in the book, the co-variance matrix is defined over all arms selected till time $t$. This is crucial as the co-variance matrix captures the information gathered from all arms, and is crucial to drive the informative sampling.
4. Assumption 3  in Appendix lines 873 seems like a very strong assumption. It states for all time steps t and for each arm, a,  true parameter vector $\mu^*$ resides within a confidence ball centered around the estimated parameter $\mu_t^a$. This confidence ball is denoted as $\mathrm{BALL}_{(t, a)}$. This should be rigorously proved instead of taking an assumption. Can you clarify this?
5. It would be also great if the authors explain in detail how the benchmarks LinUCB, LinTS are implemented for this setting. I also feel that more baslines like Kernel-UCB or Neural UCB should be used as a baseline to show that they fail in this setting.

### Soundness
2

### Presentation
2

### Contribution
2
