# Global Convergence of Policy Gradient in Average Reward MDPs

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
We present the first comprehensive finite-time global convergence analysis of policy gradient for infinite horizon average reward Markov decision processes (MDPs). Specifically, we focus on ergodic tabular MDPs with finite state and action spaces. Our analysis shows that the policy gradient iterates converge to the optimal policy at a sublinear rate of $O(\frac{1}{T})$, where $T$ represents the number of iterations. Performance bounds for discounted reward MDPs cannot be easily extended to average reward MDPs as the bounds grow proportional to the fifth power of the effective horizon. Recent work on such extensions makes a smoothness assumption that has not been verified. Thus, our primary contribution is in providing the first complete proof that the policy gradient algorithm converges globally for average-reward MDPs, without such an assumption. We also obtain the corresponding finite-time performance guarantees. In contrast to the existing discounted reward performance bounds, our performance bounds have an explicit dependence on constants that capture the complexity of the underlying MDP. Motivated by this observation, we reexamine and improve the existing performance bounds for discounted reward MDPs. We also present simulations that empirically validate the result.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a comprehensive global convergence analysis for policy gradient in infinite-horizon average-reward MDPs. It proposes a novel proof framework for the smoothness of the average reward objective, which settles the intrinsic challenge of divergence face by the standard analysis technique that regards the average-reward setting as a limiting case of the discounted-reward setting (as $\gamma \to 1$). Based on the smoothness results, it further analyzes the convergence properties of policy gradient in the average-reward setting, and concludes with an instance-specific bound convergence bound. Simulation results are presented to justify the analysis and reveal the influence of instance-related constants.

### Strengths
1. The paper is overall well-written, and the flow is friendly to first-time readers. 
2. The research problem is of theoretical interest and importance, which is sufficiently motivated and justified by a thorough review of literature.
3. The technical contributions are solid, rigorous, and clearly articulated (as summarized in Section 1.2). The proofs are checked to be correct and are largely self-contained.
4. Table 1 is especially appreciated since it gives a high-level yet clear idea of the instance-related constants involved in the bound.
5. I like the discussion presented in Section 3.2 that relates the new results to existing results in the classical discounted-reward setting, as well as a brief hint on the reason why instant-specific bounds may be tighter and thus more useful in applications.

### Weaknesses
1. The simulation results do help to promote the understanding of the instance-related constants, but it can be improved to include more direct and more convincing evidence under the principle of controlled variables. E.g., exemplary MDP families might be explicitly constructed with certain constant(s) varying and all the others fixed, so that the curves clearly reflect how the performance depends on the varying constant(s). It is not sufficient to only vary the proportion of actions yielding a reward of -1, as this may not fully isolate the effect of $C_r$ from other constants. The experimental design should ensure that only the target constant is changing while all others remain invariant, which requires careful construction of the MDP families.
2. There are a few typesetting issues: (a) Use $\verb|\citep|$ and $\verb|\citet|$ correctly for the author-year format, and avoid using $\verb|\cite|$ — specifically, only use $\verb|\citet|$ when it's a part of the sentence. (b) On line 223 and below, use $\verb|\ll|$ ($\ll$) instead of $<<$. (3) There are a few typos and grammatical issues (e.g., the inconsistency of tenses used in the literature review, where I would recommend the use of present tenses only).

### Questions
1. It is briefly touched upon in *Notes on Limitations and Future Work* that the approach can be generalized to "parametric classes of policies". I wonder if the authors have any rough ideas on how this could be done, and further, if it is also doable to extend the tabular MDP setting to generic MDPs with infinite state-action spaces (probably with function approximation, like linear/low-rank MDPs).
2. The relationship with discounted-reward MDPs is discussed in Section 3.2, where it's written that "the constants can be derived through an *analogous* process". Is it possible to (at least) sketch how the final results should look like in the appendix?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies convergence of Policy Gradient (PG) in average-reward MDPs and present non-asymptotic bounds on the global convergence of an error function defined in terms of gains of the optimal policy and the output policy by PG. For the class of unichain MDPs (cf. Assumption 1), the authors present convergence rate to the globally optimal solution (of the reward maximization problem in the long run), but without any assumption on the smoothness of the value functions involved. Such smoothness assumptions were key in the analysis in discounted MDPs. The presented convergence rates decay as $O(1/k)$ where the involved constants depend on MDP-dependent quantities. These results also lead to improved convergence analysis of discounted MDPs.

### Strengths
Policy Gradient (PG) and its variants are among interesting and important algorithms in RL. Their convergence properties for the class of discounted MDPs are very well-studied and by now well-understood. However, their counterparts for average-reward MDPs are less explored, especially when the interest lies in globally optimal solution. This is mostly due to the challenges involved in the average-reward setting, rather than the interest in the problem. 

One strength of the approach taken in the paper is to depart from the classical approach of using a discounted MDP as a proxy, which further leads to sub-optimal bounds. This way the authors eliminate the smoothness assumption that is typically made in the convergence analysis of PG in the context of discounted MDPs. 

The paper admits a good organization. Its technical part is written mostly clearly and precisely, apart from some inconsistent or undefined notations (see comments below). However, there are some inconsistencies in the presentation and advertisement of the results between the introductory part and the main technical part; further on this below. The writing quality is overall fine, but some parts could still benefit from a more careful polishing.  

As a positive aspect, the paper delivers a good and accurate review of related literature, to my best knowledge. Yet another positive aspect is reporting numerical results, albeit on toy problems.

### Weaknesses
Key Comments and Questions:
-
- The opening of the paper (Abstract and Introduction) talk about regret bounds for PG (scaling as $O(\log(T))$). Figuratively speaking, these are cumulative measures of error incurred by the algorithm. But they are not defined anywhere – or do I miss something? – and the core part of the paper only deals with per-step error measures. Please clarify. The connection between the per-step error analysis and the stated regret bound is not made explicit, and it's not immediately obvious how the $O(1/k)$ convergence rate translates to the claimed $O(\log(T))$ regret. A more detailed explanation of this connection is needed, including a precise definition of the regret being considered.
- Despite some interesting results, one key limitation of the paper is the restriction to the class of unichain MDPs (cf. Assumption 1). They are far easier to deal with and are much less relevant in modeling practical RL tasks when compared to the more interesting class of communicating MDPs. Without this assumption, one will not get a closed-form value function in Lemma 1, which is key to establish the results. In other words, it renders unlikely, in my opinion, that the technical tools developed or promoted here could be used beyond the restricted class of MDPs satisfying Assumption 1. The authors should discuss the implications of this assumption more thoroughly, including the types of real-world problems that can and cannot be modeled under this restriction. Furthermore, a discussion of potential approaches to extend the analysis beyond unichain MDPs would be valuable.
- A key question is how bad the MDP-dependent constant $C_{PL}$ could be. Even though a convergence rate of $O(1/k)$ is superior to those decaying as $O(1/k^p)$ for some $p<1$, the involved MDP-constants (e.g., in Theorem 1) could be prohibitively large in some MDPs (that are not necessarily pathological). More precisely, I expect it could be exponentially large in the size of state-space $|\mathcal S|$. The paper should provide a more detailed analysis of the constant $C_{PL}$, perhaps by exploring its dependence on specific MDP parameters. It would be beneficial to include examples of MDPs where this constant is particularly large, and discuss the practical implications of such large constants on the convergence behavior. This analysis should also consider the impact of the state space size on this constant.
- In the first paragraph of Section 1, you discuss approaches for determining the optimal policy (i.e., planning algorithms) for average-reward MDPs. Yet you mostly cite papers dealing with the learning problem. Could you clarify, or correct if relevant? The cited papers appear to focus on learning algorithms, which estimate the optimal policy from data, rather than planning algorithms, which compute the optimal policy given a model of the environment. This distinction should be made clear, and the relevant literature on planning algorithms for average-reward MDPs should be cited.

Minor Comments:
-
- In line 50, you use $\pi_k$ but it is not defined yet. 
- Regarding refs: Please check formatting guidelines. In many places you must use \citep or \citet instead of \cite so that you get (A & B, year) instead of A & B (year); for instance, in the first paragraph of Section 1. But they are correctly used in Section 1.1. This issue renders rather distracting when reading the paper. 
- The work (Lin Xiao, 2022) is cited twice. Is there any difference between them? 
- Line 133 (and elsewhere): Using $\Delta(\mathcal A)$ instead of $\Delta \mathcal A$ could make things more readable.  
- Inconsistent notations: In Eq. (8) you used $d_\mu(\pi^*)$ whereas later you used $d_{\mu,\gamma}^{\pi^*}$ to denote essentially the same thing. 
- Unless I am missing something, the textbook (Boyd and Vandenberghe, 2004) does not include definition of $L$-smoothness, etc.  
- Table 1: Make precise the norms used for $C_p$ and $C_m$.

Typos:
-
- Line 82: is , Bai et al. ==> remove “,”
- Line 198: … relationBertsekas …. ==> … relation (Bertsekas, …)
- Line 251: Further is the function is ==> Further if … 
- Line 269: euclidean norm ==> Euclidean norm ---- to be consistent with an earlier use of this term. 
- Line 346: in the Lemma below ==> … lemma …
- Line 384 and elsewhere in Section 3.2: To be consistent with notations used elsewhere, use $|\mathcal S|$ instead of $S$ since the latter is not defined. 
- Line 398: By $L$, did you mean $L_2^{\Pi}$?
- Line 388: a verb might be missing.

### Questions
See above.

### Soundness
3

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
3

### Summary
The author show that Project Policy Gradient ascent for average reward MDPs can achieve an $O(\frac{1}{\eps})$ rate to the optimal policy.  To attain this rate, the authors prove the smoothness property of the objective. Additional experiments are conducted to validate the proposed rates.

### Strengths
- First proof of global convergence of Project Policy Gradient for average reward MDPs.

### Weaknesses
 - Missing comparison to [1]. This work improves the convergence rate of [2] and show the rate of Policy Mirror Descentt is linear. Projected Policy Gradient is an instance of Policy Mirror Descent when the squared Eucliden distance is used as the mirror map.
- The clarity of the writing could be improved, 
 - The precise definition of $d^\pi(s)$ should be given
 - It's not clear what the step-size used in Thereom 1 Is
- A reference / proof for Eq. 8 should be given. 
- Formatting errors: 155: Bellman equation equation 3, 181: discount factorBertsekas (2007), 202: \textit{equation 8}


### Questions
- When presenting the convergence rates of the related works, why was the dependence of $\epsilon$ omitted?
- Could the remark of Theorem 1 be clarified. Why is the bound $$\frac{\sigma}{k^p}$$ less meaningful for the inital $k$? Isn't $k$ the number of iterations? Also note that for softmax policies, there exists faster convergence rates shown in [1] compared to [2].
- Is it possible to show that the $O(\frac{1}{\epsilon})$ bound is tight? 


[1] Liu, J., Li, W., & Wei, K. (2024). Elementary analysis of policy gradient methods.
[2] Mei, J., Xiao, C., Szepesvari, C., & Schuurmans, D. (2020, November). On the global convergence rates of softmax policy gradient methods.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents the convergence rate analysis of the projected policy gradient algorithm for tabular average reward Markov decision processes (MDPs). Assuming access to the exact gradient, the authors proved a convergence rate of $\mathcal{O}(1/T)$ where $T$ is the number of iterations. To prove the result, they established the smoothness property of the value function for ergodic MDPs, which is of separate interest.

### Strengths
1. New state-of-the-art convergence rate of $\mathcal{O}(1/T)$ for projected gradient descent algorithm for average reward MDPs.
2. New smoothness result of the value function for the same setting.
3. Despite some weaknesses stated below, the paper is overall nicely written.

### Weaknesses
1. The authors should rewrite the related works and put their work in context. First, they should separate the related works into two groups: ones that use exact gradients (and hence, are more of a planning problem), and others that use gradient estimates (and therefore, are more of a learning problem). Authors should note that some papers explicitly fall into the second group while many others discuss problems of both kinds. The work of the authors falls into the first group. This should be highlighted both in the abstract as well as in the introduction. Furthermore, the authors should clarify the specific assumptions made in each related work, such as whether they assume access to a generative model or use sample-based methods, and how these assumptions compare to those of the current paper.

2. While mentioning the convergence rate established by earlier works, the authors only focused on the $1-\gamma$ factors while completely ignoring the $\epsilon$ related factor. For example, equation (1) does not show any dependence on $\epsilon$. Is there any specific reason for that? I think it makes the comparison quite confusing. The authors should explicitly state whether the $\epsilon$ factor is a constant or a variable, and if it is a variable, how it scales with other parameters of the problem. This is crucial for a fair comparison of convergence rates.

3. Although one of the results of (Xiao 2022b) proves a convergence rate of $\mathcal{O}\left((1-\gamma)^{-5}\epsilon^{-1}\right)$, in the same paper, they also provide a better result. Specifically, using policy mirror descent, which can be thought of as a generalization of the policy gradient, they establish a linear convergence rate of $\mathcal{O}\left((1-\gamma)^{-1}\log\left((1-\gamma)^{-1}\epsilon^{-1}\right)\right)$. I am surprised that the authors failed to mention the linear convergence rate. The authors should also discuss the conditions under which the linear convergence rate is achieved in the related work, and whether these conditions are applicable to their setting.

4. Some of the state-of-the-art results mentioned are outdated. For example, (Bai et. al. 2023) is no longer the only work that establishes a regret bound for average reward MDP. A recent paper [1] supersedes their result. The authors should conduct a thorough literature review to ensure that all relevant state-of-the-art results are included and accurately represented. This includes a careful examination of the assumptions and limitations of each cited work.

5. To my understanding, the concept of regret makes sense only for a learning problem, not for a planning problem. In my opinion, the author should solely stick to the convergence rate result. The authors should clarify why they included regret in their analysis, given that their focus is on a planning problem with access to the exact gradient. If the regret is included to motivate future work, this should be explicitly stated.

### Questions
1. Since a linear convergence rate is already available in the discounted setup (Xiao 2022b), is it possible to achieve the same in the average reward setup? What are the fundamental challenges to obtain it?

2. Please mention in Table 1 that the constants $C_e$ and $\lambda$ are taken from Assumption 1. It will help the reader.

3. Is the smoothness result only valid for ergodic MDPs or is it possible to extend it to a larger class?

### Soundness
3

### Presentation
2

### Contribution
2
