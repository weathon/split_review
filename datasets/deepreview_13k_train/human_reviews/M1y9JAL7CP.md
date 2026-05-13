# Policy Gradient Optimization for Markov Decision Processes with Epistemic Uncertainty and General Loss Functions

- Decision: Reject
- Scores: 6, 6, 6, 8

## Abstract
Motivated by many application problems, we consider Markov decision processes (MDPs) with a general loss function and unknown parameters. To mitigate the epistemic uncertainty associated with unknown parameters, we take a Bayesian approach to estimate the parameters from data and impose a coherent risk functional (with respect to the Bayesian posterior distribution) on the general loss function. Since this formulation usually does not satisfy the interchangeability principle, it does not admit Bellman equations and cannot be solved by approaches based on dynamic programming. Therefore, we develop a policy gradient optimization approach to address this problem.  We utilize the dual representation of the coherent risk measure and extend the envelope theorem to derive the policy gradient. Our extension of the envelope theorem
from the discrete case to the continuous case may be of independent interest. We then show the convergence of the proposed algorithm with a convergence rate of $\mathcal{O}((1-\epsilon)^t)$, where $t$ is the number of policy gradient iterations and $\epsilon$ is the accuracy. We further extend our algorithm to an episodic setting, and establish the consistency of the extended algorithm and provide bounds on the number of iterations needed to achieve an error bound $\mathcal{O}(\epsilon)$  in each episode.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel setting of sequential decision making, where intrinsic uncertainty is handled by considering a generic objective $F(\lambda, P)$ that is convex in the state-action occupancy measure $\lambda$, while epistemic uncertainty is further handled in a Bayesian setting by imposing a risk measure over the posterior distribution of parametrized models $P_{\theta} \sim \mu_N$. The paper then proposes BR-PG, a policy-gradient-based algorithm for the new setting, along with convergence and sample complexity guarantees. The paper also includes numerical simulations that provides a preliminary hint for the applicability of BR-PG in practical settings.

### Strengths
1. Most of the proofs in the appendix are checked to be correct. However, some results are cited from other papers that I didn't bother to read or check.
2. The paper proposes a very novel setting that I have never seen before. The setting seems generic to include many existing ones as special cases.
3. The paper is largely well-written. I particularly like the examples (especially the detailed one in Appendix E.1) that provide intuitions about the technical parts.

### Weaknesses
1. Although the setting is completely new to me, it remains unclear why we should be interested in this specific setting in the first place. A mixture (a) generic convex objectives, (b) Bayesian setting with risk measures, and (c) both the infinite-horizon and the episodic setting seems too much for an 8-page conference paper, which the authors also (kind of) fail to adequately motivate as a whole. Consequently, the contribution appears to be distracting and a little confusing.
    * Can you provide a detailed real-world setting where the new setting is beneficial? I see "self-driving car" multiple times in the paper, but it would be better to explain why autonomous driving exactly calls for this new modelling, and what's its edge over the classical MDP setting (preferably, via experimental results).
    * What happens if you remove some of the components of the proposed framework? Will the theoretical guarantee be tighter, or even recover some of the known results? How does the performance of the learned policy change (in terms of risk-sensitivity, for example)?
2. The algorithm seem to be not computationally efficient, in the sense that eq. (8) may be hard to solve, and that the posterior distribution $\mu_N$ may be hard to compute or sample from. The authors are urged to discuss how these steps are implemented in practice, and what is the computational complexity of them (even rough arguments of complexity will help here)
    * Since $\mu_N$ can only be approximated, will the performance of the algorithm degrade due to such approximation? Is it possible to reflect such approximation inthe sample complexity bound?
3. The assumptions, though claimed to be "mild/standard" by the authors, are actually a little hard to digest.
    * Assumption 3.2 seems to be restrictive and hard to verify for a generic risk measure. However, I probably shouldn't be too harsh on this point, as two concrete examples are included in the appendix, and more are ready in (Shapiro et. al., 2021).
    * In Theorem 2, it is additionally assumed that $\mu_N$ is a Radon measure, which should have been shown as a lemma if it holds in general (probably under some additional assumptions on $P_{\theta}$ that are *direct* and *mild*). It's weird to assume specific properties of an intermediate variable.
    * Assumption 4.1 seems artificial, or at least I didn't find an intuitive way to understand its physical meaning. Judging from the short proof of Theorem 3, it seems that this assumption only makes technical sense since it's exactly what's needed in the proof.
4. I find it hard to make sense of Theorem 6, since it only guarantees a "constant error bound" that does not converge to 0 as $N$ increases. It appears that having more data doesn't benefit the performance at all, but rather, only adds to the sample complexity of the algorithm. It is also a little surprising to see a sample complexity guarantee with no high-probability statement.
    * Besides, the dependency on $p$, the dimension of the parameter space, is not revealed in the main text. I do see on page 18 that $p$ appears in a factor of $\exp(C/p)$ for some constant $C$, but I'm not sure whether $C$ is positive or negative.
    * As a side note, the notation $L_{i,G}$ vs. $L_{G,i}$ needs to be consistent.
5. In Figure 2, it seems that the losses are roughly the same with $N=5$ and $N=50$ samples. Is this something expected? If so, how should we make sense of it?

### Questions
See above.

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
2

### Summary
The authors consider a  Bayesian risk formulation for MDP. The novel loss function considers both the epistemic uncertainty about the transition kernel and the performance measure of the policy. The policy gradients are estimated using the solution of a general coherent risk measure. In the offline setting, as the number of data points reaches infinity, the propose algorithm converges to the optimal policy at an $O(\frac{1}{t})$ rate. The algorithm is also shown to be extended to an episodic setting. Finally, numerical experiments are conducted to validate the proposed algorithm in the offline setting.

### Strengths
- The loss function considered both epistemic and intrinsic uncertainty is novel and the proposed algorithms are shown to achieve convergence to an optimal policy at an $O(\frac{1}{t})$ rate to in the offline setting with infinite data and asymptotic convergence in the episodic setting

### Weaknesses
 - For the numerical experiments, it would be clearer to show the sub-optimality gap of the optimal policy. While it seams that BR-PG is converging, it's not clear how close it converges to the optimal policy. More details about the implementation of BR-PG should be provided such as choice of step-size (i.e., why it was chosen to be $0.5$) and $r_n$. At the moment, it is difficult to understand what is the differences between the proposed algorithm and it's implementation.

 - Could the definition of the function $L_p$ in Assumption 3.1 be defined?
- In Theorem 4, is it possible to use a decreasing step-size so that the resulting rate is not biased if $r_N$ is finite?
- There are minor formatting error should be fixed. For example, there are missing spaces in Theorem 4:  "Assumption 3.1, 3.2, 3.3,4.1" and Theorem 5: " Assumption 3.1, 3.2, 3.3, 4.1, B.1, B.2 and B.3hold". Moreover, the paper should use the most recent template. The submission has "Under review as a conference paper at ICLR 2024" in the header.
- Minor spelling mistakes:
  - In section 3: "envelop theorem" -> "envelope theorem"
- Clarity
  - In Assumption 3.2, the policy parameter is denoted as $\theta$, but in Eq.3  it is parameterized by $\alpha$.

### Questions
- Could the definition of the function $L_p$ in Assumption 3.1 be defined?
- In Theorem 4, is it possible to use a decreasing step-size so that the resulting rate is not biased if $r_N$ is finite?
- There are minor formatting error should be fixed. For example, there are missing spaces in Theorem 4:  "Assumption 3.1, 3.2, 3.3,4.1" and Theorem 5: " Assumption 3.1, 3.2, 3.3, 4.1, B.1, B.2 and B.3hold". Moreover, the paper should use the most recent template. The submission has "Under review as a conference paper at ICLR 2024" in the header.
- Minor spelling mistakes:
  - In section 3: "envelop theorem" -> "envelope theorem"
- Clarity
  - In Assumption 3.2, the policy parameter is denoted as $\theta$, but in Eq.3  it is parameterized by $\alpha$.

### Soundness
2

### Presentation
2

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
The paper studies the policy gradient optimization problem for MDP with epistemic uncertainty and convex in occupancy measures. It first uses the dual representation to establish the policy gradient for this general objective. Then, the paper shows the O(1/t) convergence rate of the policy gradient algorithm, up to a gradient error term. The paper also extends the analysis to the episodic setting, providing bounds on the number of iterations required for achieving the desired accuracy. Finally, the paper uses numerical experiments to demonstrate the effectiveness of the algorithm.

### Strengths
* The paper develops rigorous theorems for both the infinite-discounted setting and the episodic setting.
* The paper provides numerical examples to illustrate the effectiveness of the algorithm, and the code is also released.

### Weaknesses
 * I think the paper lacks a comprehensive review of related literature. For example, the considered problem is closely related to general-utility RL (or convex RL), yet the only cited paper is (Zhang et al., 2020). Beyond, the cited paper, there are still many relevant works, such as [1-6] below. I suggest the author includes an additional section to discuss the related literature, including previous research on convex RL.
* The introduction of the problem formulation can be more clear. Specifically, the author can emphasize/reiterate that Eq (2) specifies the problem that the paper focuses on. I took a while to figure out research problem of the paper.
* I think the author should not ignore the sample complexity in the theoretical analysis. For example, in Theorem 4, the complexity indeeds comes from the gradient estimation error term. I think a better presentation can be, discuss the iteration complexity in the exact setting (1/t), and discuss the sample complexity in the sample based setting (seems to be 1/epsilon^4).

### Questions
* The overall flow of the paper is very similar to (Zhang et al., 2020). Could the author detailedly discuss the distinctions of the two works, and the new challenges in this more general formulation?
* In literature [2,3,5,6] mentioned above, they all use a relaxed assumption on the policy parameterization, i.e., a locally invertible mapping instead of a universally invertible mapping. Could the results in this paper also extend to the relaxed assumption?

Besides the two questions above, I hope author also responds to the weakness that I mentioned above. If these problems can be addressed, I am willing to reconsider the rating.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors build upon the work presented in DRQL (Zhang et al.) and the Envelope Theorem. They propose a novel algorithm aimed at managing environmental uncertainties, specifically targeting variations in the transition kernel. The proposed approach leverages offline training for model stability, which is subsequently tested online, thus addressing real-world dynamic uncertainties effectively. Additionally, the authors extend the method's application from discrete to continuous cases, demonstrated through OpenAI benchmark scenarios.

### Strengths
1. Novel Approach to Handling Environmental Uncertainty: The proposed method presents an innovative solution to managing uncertainty in dynamic environments, particularly useful in areas requiring robustness against fluctuating data distributions.
2. Solid Theoretical Foundation and Proof: The paper showcases a rigorous theoretical basis, with clear proofs supporting the stability and convergence of the method, adding confidence in the reliability of the algorithm.
3. Impressive Comparison Results in the Case Study: The authors provide compelling results from case study comparisons, particularly illustrating the method's advantages over traditional approaches in practical applications.

### Weaknesses
1. Additional Comparative Case Study: Including a comparative case study in a different environment could strengthen the evaluation by illustrating the method's adaptability across various domains. For example, assessing performance in a stochastic, multi-agent environment could provide insight into how the method handles complex dynamics beyond the controlled setup, such as the autonomous driving scenario. Specifically, it would be beneficial to see how the algorithm performs when faced with the challenges of decentralized decision-making and non-stationary policies of other agents, which are common in multi-agent systems.

2. Incorporation of a Real-World Dataset: Applying the algorithm to a specific real-world dataset, if feasible, could highlight its practical relevance and capability to handle real-life uncertainties. For instance, testing on a dataset related to robotics, such as sensor-based navigation or autonomous vehicle trajectory data, might illustrate how effectively the algorithm adapts to real-world conditions. This would involve demonstrating the algorithm's ability to handle noisy sensor data, partial observability, and the inherent complexities of real-world physics, which are not always captured in simulation environments.

3. Comparison with Assumptive Environments and BR-PG Method: A comparative analysis with assumed environments, along with the BR-PG method the authors propose, would provide a fuller understanding of the algorithm’s performance relative to established techniques. It is crucial to understand how much the performance degrades when the algorithm does not have access to the true transition probabilities, which is often the case in real-world applications. A comparison with the performance of the BR-PG method under the true transition probabilities would help to quantify the cost of learning the transition probabilities.

### Questions
Question: Could the authors elaborate on how the transition kernel adapts in real-world settings, particularly in dynamically changing conditions? Specifically, it would be insightful to understand how the episodic setting in Algorithm 2 might be adapted to handle evolving environments, such as those encountered in autonomous vehicle navigation. This could provide practical insights into the algorithm's adaptability and robustness in non-static scenarios.

Suggestion: It would be beneficial if the authors could elaborate on the model's practical utility in real-life applications like autonomous vehicles. Specifically, understanding how the transition kernel adapts to evolving environmental factors (e.g., weather, road conditions, traffic) and whether the model supports continuous real-time updates would offer a clearer picture of its suitability for such dynamic and safety-critical domains. Real-world examples or simulations of this adaptive capability could greatly enhance the relevance and applicability of the proposed approach.

### Soundness
4

### Presentation
4

### Contribution
4
