# Breaking the Curse of Multiagency in Robust Multi-Agent Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Standard multi-agent reinforcement learning (MARL) algorithms are vulnerable to sim-to-real gaps. To address this, distributionally robust Markov games (RMGs) have been proposed to enhance robustness in MARL by optimizing the worst-case performance when game dynamics shift within a prescribed uncertainty set. Solving RMGs remains under-explored, from problem formulation to the development of sample-efficient algorithms. A notorious yet open challenge is if RMGs can escape the curse of multiagency, where the sample complexity scales exponentially with the number of agents. In this work, we propose a natural class of RMGs where the uncertainty set of each agent is shaped by both the environment and other agents' strategies in a best-response manner. We first establish the well-posedness of these RMGs by proving the existence of game-theoretic solutions such as robust Nash equilibria and coarse correlated equilibria (CCE). Assuming access to a generative model, we then introduce a sample-efficient algorithm for learning the CCE whose sample complexity scales polynomially with all relevant parameters. To the best of our knowledge, this is the first algorithm to break the curse of multiagency for RMGs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a new multi-agent problem class, which is a new class of robust Markov Games with fictitious uncertainty sets. The authors define solution concepts – robust Nash equilibrium and robust coarse correlated equilibrium for this new class of games and also prove the existence of these. The authors then propose a novel algorithm called Robust-Q-FTRL to find robust CCE for their class of robust Markov Games and also establish its sample complexity. Using their approach in their class if problems, the authors break the curse of multi-agency in MARL.

### Strengths
1. The paper is well written. All concepts and claims are clearly defined and claims are backed by theoretical justifications.
2. While the authors provide a detailed theoretical analysis, I am unable to verify the correctness of their results, though I could not find any error.
3. The authors clearly state their algorithm which can be applied to practical problems.

### Weaknesses
 1. The authors do not provide any numerical examples. While they claim that their approach is scalable, some numerical examples will be useful to understand scalability and the sample efficiency claims better. Can the authors include a small simulation study to demonstrate the scalability and sample efficiency of their approach compared to baselines, even if only on a toy problem? Specifically, it would be beneficial to see how the algorithm performs with an increasing number of agents and state-space size, to validate the claim of breaking the curse of multi-agency. The absence of empirical validation makes it difficult to assess the practical relevance of the theoretical results.
2. The authors do not provide any comparison of their approach with other approaches in literature in terms of numerical computations. It is unclear how the proposed algorithm's performance compares to existing methods in terms of convergence speed and computational overhead. A numerical comparison, even if on a simplified problem, would help to contextualize the theoretical contributions.
3. The authors do not comment on whether the policies learned using their algorithms are strategy proof from a learning perspective, i.e., do they perform well when other agents use different learning algorithms. This is a crucial aspect in multi-agent settings, as the robustness of the learned policies should not only be against environmental uncertainty but also against the behavior of other learning agents. The lack of discussion on this aspect raises questions about the practical applicability of the proposed method in dynamic multi-agent environments.

### Questions
1. What is the $(s, \mathbf{a})$-rectangularity condition? An explicit definition for this would be useful to readers with limited background in this class of problems.  Can the authors provide a brief formal definition of the $(s,a)$-rectangularity condition in the main text, along with a sentence or two explaining its significance in robust MDPs/Markov games?
2. How are the uncertainty sets defined in this work practically meaningful? Can the authors to provide 1-2 concrete examples of how their fictitious uncertainty sets could model real-world uncertainties in multi-agent systems, and how this compares to uncertainty modeling in previous work?
3. What are the real-world scenarios which are modelled well by this class of RMGs with fictitious uncertainty sets?
4. When the authors compare with prior art in Table 1, aren’t the game models also different in the different works? Are there any trade-offs due to this?
5. Is the sample complexity improvement obtained by the authors primarily dependent on their robust Markov game definition which is different from the other works in literature?
6. Doesn’t the uncertainty set become very large and potentially intractable in problems with large state spaces?
7. Is it necessary that the uncertainty set be defined as part of the problem? In practical use cases, how does one define these sets? Specifically, can the authors discuss guidelines or heuristics for how practitioners could define appropriate uncertainty sets for real-world multi-agent problems, and whether there are ways to learn or adapt the uncertainty sets from data?
8. While I agree that the proofs are too long to be included in the main paper, but considering the fact that the primary contribution of this work is theoretical, it would be very helpful if the authors can provide short proof sketches or key proof ideas for all their claims in the main paper itself.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of the “curse of multiagency” in robust MARL by introducing a new class of robust Markov games with a fictitious uncertainty set. This kind of uncertainty set allows any one agent to consider uncertainties arising from both the environment and the policies of other agents. Then, the authors prove the existence of robust Nash equilibrium and propose an algorithm Robust-Q-FTRL, which learns an approximate coarse correlated equilibrium with polynomial sample complexity, thus breaking the curse of multiagency in RMG for the first time. No experiment validation is provided.

### Strengths
Strengths:

1. The main body of this paper is well-written.
2. The proposed uncertainty set is interesting.
3. The proposed algorithm effectively reduces sample complexity, avoiding the exponential growth issue in multi-agent systems caused by the joint action space.

### Weaknesses
Weakness:

1.  The approach assumes access to a generative model with a true nominal transition kernel for sample generation, which is infeasible in real-world applications. This is a strong assumption, as access to the true nominal transition kernel implies knowledge of the underlying environment dynamics, which is rarely available in practice. Furthermore, the paper does not discuss how the algorithm would perform if the generative model is misspecified or if the samples are noisy, which are more realistic scenarios.
2.  Although the paper provides theoretical evidence for overcoming the curse of multiagency, further experimental validation is needed to determine whether the algorithm itself breaks the curse or if the new problem formulation inherently possesses this advantage, potentially enabling other algorithms to achieve similar results. In addition, additional experimental evidence is needed to demonstrate that the new uncertainty set yields more robust policies compared to the previously classic (s, a)-rectangularity uncertainty sets. The paper should provide a clear comparison of the performance of the proposed algorithm with existing methods under various uncertainty levels and different types of environmental perturbations. Without such experiments, it is difficult to assess the practical significance of the theoretical results.
3.  While reading through the proof section, I noticed typos and unclear expressions, e.g., on lines 1044, 1170, and 1175. Additionally, the proofs lack tight cohesion between sections as seen in the main body, and there are missing references to some essential equations, which makes the reading experience somewhat challenging. The lack of clear and consistent notation further complicates the understanding of the theoretical results. For example, the use of similar symbols for different concepts makes it difficult to follow the mathematical derivations.

### Questions
Questions:

1. Does the definition of the policy imply that the final solution can be an un-stationary policy?
2. Are the fictitious uncertainty sets un-stationary? That is, does each period have a distinct uncertainty set?
3. In a robust Markov game (MG) setting where the uncertainty set differs at each time step, is it valid to interchange the max operators in the definition of the optimal robust value function at each time step?
4. You assume that sampling from the true nominal transition kernel is possible. However, if this is feasible, why is robustness necessary? To address the sim-to-real gap, wouldn’t it be more appropriate to assume that sampling from the true nominal transition kernel isn’t possible?
5. Additionally, could you explain why the estimation method in Algorithm 1 differs from that in standard MG settings?
6. My understanding of the fictitious uncertainty set is that it involves a policy-based adjustment to the classic reference transition kernel (nominal transition kernel), which is then used as the basis for constructing the uncertainty set. This implies two rounds of adjustment in creating the uncertainty set, adding an extra step compared to traditional uncertainty sets. Does this make the new uncertainty set more conservative? How do you quantify the difference between the fictitious uncertainty set and a conventional uncertainty set without the initial adjustment?
7. Could you elaborate on the reason for breaking the curse of multiagency? Is it mainly due to the FTRL algorithm, or does the fictitious uncertainty set contribute to this outcome?
8. Could additional experimental results be provided to verify the convergence of the algorithm and demonstrate that the robust policy in this setting achieves better robustness compared to the classical (s, a)-rectangularity setting?
9. Line 65, Kearns & Singh, 1999 is not about solving finite-horizon multi-player general-sum Markov games, why cite this?

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
4

### Summary
This paper proposes a sample-efficient algorithm for robust general-sum and Markov games (RMGs), breaking the curse of dimensionality in RMGs and achieving optimal sample complexity for CCE with respect to the action space size.

### Strengths
This paper proposes a sample-efficient algorithm for robust general-sum and Markov games (RMGs), breaking the curse of dimensionality in RMGs and achieving optimal sample complexity for CCE with respect to the action space size.

### Weaknesses
The sample complexity optimality with respect to $A_i$ is achieved at the expense of an increased horizon $H$. Additionally, while the existence of a robust Nash equilibrium (NE) is proven, only the sample complexity for robust CCE is derived, which affects the completeness of the work.

The paper's claims regarding sample complexity improvements need further clarification. The introduction of the policy-induced $(s, a_i)$-rectangularity condition is presented as a key contribution, but the practical impact of this condition is not sufficiently demonstrated. Specifically, the paper lacks a concrete example or comparison that illustrates how this condition leads to improved sample complexity compared to the $(s, a)$-rectangularity condition used in previous work. This makes it difficult to assess the significance of this new approach.

The presentation of constraints on $N$ and $K$ as separate entities, rather than combining them as $N = KH$, is also unclear. The rationale behind this separation is not adequately explained, and it is not evident why this distinction is necessary or beneficial for the analysis. This lack of clarity makes it harder to understand the practical implications of the sample complexity results.

The paper suffers from poor organization and numerous typographical errors. The reference to "Section 2.2 for details" on page 3, when the relevant content is in Section 3.1, is a significant error. Furthermore, the algorithm description appears late in the paper, on page 8, which disrupts the logical flow of the presentation. These issues detract from the readability and overall quality of the work.

### Questions
1. Could the authors discuss the challenges involved in deriving sample complexity bounds for robust NE within the existing framework? Additionally, proposing the derivation of robust NE sample complexity as a direction for future work would help address the question of completeness and open avenues for further research.
2. Could the authors include a concrete example or comparison showing how the policy-induced $(s, a_i)$-rectangularity condition improves sample complexity relative to the $(s, a)$-rectangularity condition used in previous work? Such a comparison would help readers understand the practical impact of this new approach.
3. Could the authors clarify why separate constraints on $N$ and $K$ are presented, rather than combining them as $N = KH$? If there are specific advantages or insights gained from keeping these constraints separate, an explanation would enhance the clarity and completeness of the analysis.
4. The paper lacks clear organization and contains numerous typos. For instance, on page 3, it refers to "Section 2.2 for details," whereas the relevant content is actually in Section 3.1. Additionally, the algorithm description does not appear until page 8. A thorough proofreading pass to correct section references and typographical errors is also recommended to enhance readability.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies robust reinforcement learning in the multi-agent setting. The authors propose a new uncertainty set called "fictitious uncertainty set", where depends on the joint policy of agents. Based on the new notion, they establish the existence of robust NE and CCE. After that, they propose the Robust-Q-FTRL algorithm, and under the generative model assumption, they establish sample complexity only scaling with the number of actions of all agents.

### Strengths
The robust multi-agent learning setting is interesting and reasonable to me. 

Although under a different setting compared with previous works considering rectangular uncertainty set, the sample complexity results "break the curse of multi-agency".

### Weaknesses
1. **About paper writing**: I think there are several parts of the paper writing should be improved to avoid confusion.

* If I understand correctly, starting from Section 3.2, the definition of value functions are associated with the fictitious RMGs, instead of the rectangular uncertainty sets. In another word, one should interpret $V^{\pi,\sigma_i}_{i,h}$ through the definition in Eq.(26), instead of Eq. (5), which are different in the uncertainty set w.r.t. the inf operator.

    However, I did not find a declaration of this abuse of notation (and personally, I would recommend use different notations to avoid confusion). This is crucial because it makes significant difference in how to interpret the results. Under the definition of Eq.(26), the uncertainty set varies for different policies $\pi$, rather than that one first fix the uncertainty set by an arbitrary reference policy $\pi$ and then use that to define the NE/CCE.

* The "technical insights" paragraph in Section 4.3 does not explain clearly how the proposed algorithms avoid the curse of multi-agency. This is crucial to evaluate the technical novelty of this work (also see my second point in the following).

2. **The fundamental reason for avoiding curse of multi-agency is not clear to me**.

* Comparing with previous works, this paper consider a different uncertainty set, it is not clear to me whether it is the key variation making the problem more tractable than before. Especially, by definition, the new uncertainty set only quantifies the uncertainty of the (weighted) marginal transition function. If this is the essential reason, claiming avoiding curse of multi-agency as advantage over previous work would be unfair.

* Besides, this paper relies on generative model assumption, I'm also curious whether it is a common assumption in previous literature?

3. **The proposed uncertainty set may not be sufficient to quantify the uncertainty**. I'm curious what would be the benefits of considering new uncertainty set, and is it reasonable to consider such set in practice? For example, under what scenarios (what kind of model difference between simulator and practice), the propose uncertainty set would be useful.

Besides, technically speaking, the new uncertainty set may be insufficient to capture the sim-to-real gap. Note that the ratio $\pi_h(a_i,a_{-i}|s) / \pi_{i,h}(a_i|s)$ could varies a lot for different $a_{-i}$, given that this paper considers correlated policies. Consider the scenario where the sim-to-real gaps of $P^0_{h,s,\textbf{a}}$ are very large for some $(s,\textbf{a})$, while, coincidently, the learned CCE only has low ratio $\pi_h(a_i,a_{-i}|s) / \pi_{i,h}(a_i|s)$ on them. In that case, fictitious uncertainty set is not sufficient to quantify the uncertainty.

Furthermore, the fictitious uncertainty set can be much more conservative than a rectangular uncertainty set on those $(s,a)$ with low policy value. For a fixed threshold $\sigma_i$, if the policy value on some $(s,a)$ is very small, the transition function in the uncertainty set can vary significantly on that $(s,a)$, leading to a more pessimistic uncertainty quantification than rectangular sets. This is because the policy value acts as a weight term in the fictitious uncertainty set definition. Although the proposed fictitious uncertainty set may sometimes provide better uncertainty quantification, it is not clear when this occurs, and more importantly, if we can know it is better in advance without knowledge of the equilibrium policy or other information.

### Questions
1. Is the proposed Algorithm 1 overall computationally tractable? I found a related discussion in Sec. 4.2, but it is about the Q value estimation.

### Soundness
2

### Presentation
2

### Contribution
2
