# Mostly Exploration-free Algorithms for Multi-Objective Linear Bandits

- Decision: Reject
- Scores: 5, 6, 3, 3, 3

## Abstract
We address the challenge of solving multi-objective bandit problems, which are increasingly relevant in real-world applications where multiple possibly conflicting objectives must be optimized simultaneously. Existing multi-objective algorithms often rely on complex, computationally intensive methods, making them impractical for real-world use. In this paper, we propose a novel perspective by showing that objective diversity can naturally induce free exploration, allowing for simpler, near-greedy algorithms to achieve optimal regret bounds up to logarithmic factors with respect to the number of rounds. We introduce simple and efficient algorithms for multi-objective linear bandits, which do not require constructing empirical Pareto fronts and achieve a regret bound of $\tilde{\mathcal{O}}(\sqrt{T})$ under sufficient objective diversity and suitable regularity. We also introduce the concept of objective fairness, ensuring equal treatment of all objectives, and show that our algorithms satisfy this criterion. Numerical experiments validate our theoretical findings, demonstrating that objective diversity can enhance algorithm performance while simplifying the solution process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of balancing multiple objectives in linear bandit problems, proposing a novel approach where objective diversity naturally induces "free exploration," allowing simpler algorithms to perform efficiently. Instead of relying on constructing Pareto fronts, which can be computationally intensive, the paper introduces two algorithms, MORR-Greedy and MORO-Greedy, which use round-robin and near-greedy selections to optimize multiple objectives without requiring explicit exploration. The algorithms achieve a regret bound of $\tilde{O}(dT)$, leveraging objective diversity to enhance performance and reduce the need for complex exploratory steps. This paper also introduces the concept of "objective fairness," ensuring equitable treatment across objectives.

### Strengths
By using objective diversity for free exploration, the proposed approach presents a new perspective on how multiple objectives can simplify rather than complicate the decision-making process.

### Weaknesses
1. It is hard for me to understand the concept of objective fairness as defined in Section 2.2.2. Is the equation in this section a correct definition of objective fairness? For example, could you provide an intuitive explanation of what the equation in Section 2.2.2 means in practical terms or in real-world applications. Particularly, could you clarify if this definition allows for objectives of different importance, and if so, how that would be incorporated and affect the final result? A clear explanation about these would be easier for me to understand the proposed results.

2. The parameter initialization for $\beta$ in Algorithm 1 is unclear to me. For example, could you provide specific guidelines or a step-by-step procedure for choosing the initial $\beta$ values. Also, the intuition behind Definition 4 and how it relates to algorithm performance are unclear to me. It would be better if a small case study or numerical examples showing how different initializations of $\beta$ might impact the algorithm's behavior and final performance can be provided.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers multi-objective linear bandit problems. Unlike existing complex methods, this study leverages "objective diversity" to enable free exploration, leading to efficient algorithms (MORR-Greedy and MORO-Greedy) that achieve good regret bounds without constructing empirical Pareto fronts.

### Strengths
1. The paper is clearly written. 
2. The idea of "objective diversity induces free exploration" is novel.
3. The proposed algorithm is simple and effective.
4. The concept of objective fairness is another contribution, ensuring equitable treatment across all objectives.

### Weaknesses
1. The introduction could more directly highlight practical scenarios where current multi-objective algorithms face scalability or computational limitations due to their reliance on Pareto front constructions and complex exploration mechanisms. Illustrating these challenges would provide a compelling reason for why a simpler, exploration-free method like MORR-Greedy is beneficial.
2. The proposed algorithms assume objective diversity to enable free exploration. Whether this diversity exists naturally in most multi-objective setups is not clear. In real-world scenarios, it is likely that objectives are correlated. Could you provide examples or discuss scenarios where objective diversity is likely to occur naturally, or address how your methods might perform when objectives are correlated?
2. The numerical experiments, while supportive of the theoretical claims, may be overly simplified. How the hyper-parameters are chosen is also not discussed.

### Questions
1. Why $\gamma$-regularity is a proper assumption? How likely it can happen in reality? Could you provide intuition or examples of when $\gamma$-regularity naturally occur in practical scenarios?
2. How do you show $T_0$ is independent of $T$? Since $T$ shows up in the expression of $\lambda$, I think it is necessary to show $T_0$ is of order $O(\sqrt{T})$. It seems that in the paper it is simply treated as a constant. 
3. Could you elaborate more on your claim that "objective diversity induces free exploration"? I am not clear on where this concept is applied within the proof.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles solving multi-objective linear bandit problems, where multiple, potentially conflicting objectives need to be optimized simultaneously. The authors propose to leverage the diversity among objectives to drive exploration, instead of relying on the diversity of the feature vectors (contexts) as traditionally done.  They introduce two near-greedy algorithms, MORR-Greedy (Multi-Objective Round Robin Greedy) and MORO-Greedy (Multi-Objective Random Objective Greedy), which are simpler and more computationally efficient than existing methods because they don't require constructing the empirical Pareto front in each round.

Under the assumptions of objective diversity (objective parameters spanning the feature space) and a newly introduced regularity condition (γ-regularity), the authors prove that their algorithms achieve a regret bound of sqrt(dT). They also introduce a concept called "objective fairness," ensuring that all objectives are considered equitably, and demonstrate that their algorithms satisfy this criterion.

### Strengths
Originality: The paper presents a novel perspective on multi-objective bandit problems by highlighting the potential of objective diversity to induce free exploration.  

Quality:  The paper mainly provides a theoretical analysis of how objective diversity aids the search, establishing regret bounds of  sqrt(dT) for the proposed MORR-Greedy and MORO-Greedy algorithms under the objective diversity and γ-regularity assumptions. The introduction and analysis of the objective fairness criterion further is interesting.

Clarity: The paper is generally well-written and clearly presents the problem setting, algorithms, and main results. 

Significance: If the theoretical results hold and generalize well, the paper's findings could have significant practical implications.

### Weaknesses
Major Soundness Issue: Under your setting, there is a stochastic linear bandit lower bound of d*sqrt(T) [see https://tor-lattimore.com/downloads/book/book.pdf], although for adversarial linear bandits, there is an upper bound of sqrt(dT) only for the action set being the L2 ball [see https://arxiv.org/pdf/1711.01037 {Sparsity, variance and curvature in multi-armed bandits}: it shows that for the $l_p$ norm ball linear bandit problem($p>2$), no algorithm could have better that Omega(d sqrt(T))]. 

Since your results should extend to the single-objective case, Pareto regret becomes regular cumulative regret and your assumptions on  γ-regularity still hold and K can be exponentially large. Then, it appears that your upper bound is too good to be true, can you explain this?

Connection to Pareto Front Approximation: The paper focuses on minimizing Pareto regret, but doesn't explicitly discuss how the proposed algorithms relate to the goal of approximating the Pareto front. Specifically, the fairness objective tries to address this by  inducing approximation to the maxima of the M objectives separately, it still does not approximate the Pareto front as there are multiple directions in the "middle" of the Pareto front that needs to be approximated. Adding this as a discussion is important and a recent paper (https://arxiv.org/abs/2307.03288) has shown that in general, there is in fact a T^{-1/M} lower bound. In light of the scalarizations framework of that paper, it appears that you are simply considering closeness in only M directions and it is unclear why this would lead to a good multiobjective search. As proposed in that paper, would it make more sense to have multiple random scalarization directions? 


Limited Empirical Validation:  While the paper includes some numerical experiments, they are relatively limited in scope. They do not involve the fairness objectives that were introduced and it would be also interesting to include hypervolume regret as a more robust version of multiobjective progress. It would also be interesting to see experiments with varying degrees of objective diversity and γ-regularity to understand how these factors impact algorithm performance.

Clarity on γ-Regularity: While the paper introduces the concept of γ-regularity, its practical implications and relationship to real-world datasets are not fully clear. Specifically, it is used to implicitly assume a feature diversity in terms of the isotropic nature of the gram matrix and provide a connection between objective and feature diversity. However, the analysis still hinges on the underlying feature diversity, making the messaging on the paper extremely confusing. More intuitive explanations and examples of datasets that exhibit (or do not exhibit) γ-regularity would be helpful. It would also be beneficial to discuss methods for estimating γ and α0 from data.

### Questions
Generally, no algorithm could have better that Omega(d sqrt(T)) regret for singleobjective optimization with K = exponentially many arms. Can you explain how your upper bound seems too good to be true?

Can you explain why you claim that "we do not assume any such diversity in the features", given that γ-regularity assumption connects objective with feature diversity?

In light of https://arxiv.org/abs/2307.03288, why is the fairness criterion good for multiobjective optimization and should fairness be defined with respect to more directions than just the maxima of M objectives?

### Soundness
2

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
This paper addresses the challenge of multi-objective linear bandits, specifically investigating whether an increasing number of objectives complicates the learning process. To address this question, the authors propose two algorithms that greedily select the optimal arms in each round by alternately dealing with one objective at a time. Theoretical analysis and numerical experiments demonstrate that the algorithms achieve relatively ideal performance.

### Strengths
The paper is easy to follow.

### Weaknesses
The motivation of the paper needs to be clearer. Can you give more description about the meaning of diverse objectives, which causes the drawbacks of existing methods?

The index of objective fairness is confusing; please provide an intuitive and illustrative explanation to clarify this part. For example, the change of this value in an experiment. 

My main concern is the selection strategy for sub-optimal arms. The authors claim that one of the main contributions is the consideration of objective fairness, which involves playing each Pareto optimal arm fairly. However, the algorithms select the arm by alternately maximizing each objective, which only results in selecting special solutions. The authors should refer to conclusions from the multi-objective optimization community. Given this, I highly recommend that the authors investigate the specific needs of this case.

Additionally, the two proposed algorithms differ only in their initial phase, with one using manually set parameters and the other using random parameters. Despite the theoretical analysis provided, I do not see any critical function of this part.

Finally, in the experimental study, the proposed algorithm performed exceptionally well with almost zero regret in all cases, even when the number of arms was up to 100. These results do not seem convincing. More details of the experimental setup should be provided, and using a real-world dataset could offer more powerful verification.

Overall, the quality of the paper needs further improvement.

### Questions
See the weakness above.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates multi-objective stochastic linear bandits with finite arms, contributing a novel approach by introducing objective fairness for multi-objective bandits.

### Strengths
1. The paper focuses on a central issue in multi-objective optimization.
2. The related work is well-organized.

### Weaknesses
1. **Lines 35-40**: The authors frequently mention the increased complexity associated with multi-objective problems but do not specify the complexity level of existing algorithms (Yahyaa and Manderick, 2015; Turgay et al., 2018; Lu et al., 2019; Kim et al., 2023). Could the authors clarify how much the proposed algorithm reduces this complexity? Including a comparison table would be helpful.

2. **Lines 221-233**: The concept of "objective fairness" is unclear. Is it represented by the parameter $p_\epsilon$, or is it a characteristic of a multi-objective bandit algorithm? Please provide a precise definition of objective fairness, similar to how the Pareto order is defined. Additionally, examples illustrating this concept would aid in comprehension. For instance, for two arms with expected rewards $[0,1]$ and $[1,0]$, what kind of decision sequence would qualify as fair?

3. **Line 252**: Are the values $\\{\beta_1, \dots, \beta_M\\}$ initialized according to Definition 4? I could not find the definition of "greedy selection." Please include examples demonstrating the initialization of $\\{\beta_1, \dots, \beta_M\\}$.

4. **Line 314**: The assumption $||\theta_m^*|| = 1$ is not common in single-objective or multi-objective bandit literature, as far as I could ascertain from the cited works (Abbasi-Yadkori et al., 2011; Chu et al., 2011; Agrawal & Goyal, 2013; Abeille & Lazaric, 2017). This assumption appears overly restrictive given that $\theta_m^*$ is unknown.

5. **Line 323**: Is this assumption prevalent in existing studies? Furthermore, why does the assumption that $\theta_1^*, \ldots, \theta_M^*$ span $\mathbb{R}^d$ imply objective diversity? This property seems only to support the objective value of a single fixed arm, while diversity typically refers to variability across different arms.

6. **Line 335**: I could not locate the definition of $\mathbb{B}_\alpha(\cdot)$. Please clarify if I have overlooked it.

7. **Line 375**: What is $T_0$?

8. **Theorem 1**: The term $\delta$ is missing from the regret bound. Perhaps your theorem specifies the expected regret bound $E[PR(T)]$ rather than $PR(T)$.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
