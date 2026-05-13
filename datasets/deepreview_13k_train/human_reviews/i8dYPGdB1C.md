# Near-Optimal Online Learning for Multi-Agent Submodular Coordination: Tight Approximation and Communication Efficiency

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
Coordinating multiple agents to collaboratively maximize submodular functions in unpredictable environments is a critical task with numerous applications in machine learning, robot planning and control. The existing approaches, such as the OSG algorithm,  are often hindered by their poor approximation guarantees and the rigid requirement for a fully connected communication graph. To address these challenges, we firstly present a $\textbf{MA-OSMA}$ algorithm, which employs the multi-linear extension to transfer the discrete submodular maximization problem into a continuous optimization, thereby allowing us to reduce the strict dependence on a complete graph through consensus techniques. Moreover, $\textbf{MA-OSMA}$ leverages a novel surrogate gradient to avoid sub-optimal stationary points. To eliminate the computationally intensive projection operations in $\textbf{MA-OSMA}$, we also introduce a projection-free $\textbf{MA-OSEA}$ algorithm, which effectively utilizes the KL divergence by mixing a uniform distribution. Theoretically, we confirm that both algorithms achieve a regret bound of $\widetilde{O}(\sqrt{\frac{C_{T}T}{1-\beta}})$ against a  $(\frac{1-e^{-c}}{c})$-approximation to the best comparator in hindsight, where $C_{T}$ is the deviation of maximizer sequence, $\beta$ is the spectral gap of the network and $c$ is the joint curvature of submodular objectives. This result significantly improves the $(\frac{1}{1+c})$-approximation provided by the state-of-the-art OSG algorithm. Finally, we demonstrate the effectiveness of our proposed algorithms through simulation-based multi-target tracking.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author(s) propose a continuous surrogate approximation of multi-agent submodular maximization problems and solve via mirror ascent approach to (i) achieve tight approximation, and (ii) reduce communication density among agents. The proposed approach is evaluated in multi-robot target tracking examples.

### Strengths
1. The contribution is novel and sound, and the theoretical results are strong.  
2. The paper is well presented in general. The authors clearly motivated challenges existing in the literature and this work’s objectives.
3. The efficacy of the proposed approach is validated using sufficient amount of empirical evidence.

### Weaknesses
1. Problem formulation
- I think the author(s) should list the assumptions made in this section explicitly, such as those in lines 177 and 159.
- I think this section is a bit unconnected with the motivating example. I would appreciate a bit more introduction about why and how problems like multi-agent tracking can be formulated as online submodular maximization problems. For example, I am a bit confused here why the objective function is revealed after agents make decisions and why the objective function is guaranteed to be submodular?
2. Experiments:
- Is all the targets being strictly homogeneous in type a requirement from the algorithm? What if different targets are of different types?
3. Contribution: this work builds upon a few existing methods in the literature. The novelty of the approaches can be better specified; cf. Question 3.
4. While submodular optimization has a variety of applications, the problem studied in this work seems to be more specific to robotics applications. I think is relatively less relevant to this venue.
5. Other minor points:
- Line 70: “Furthermore” – hyperlink is redundant
- Figure 3: It can be shown in the caption or in the figure that 3 rows represent different target types. Right now, it’s a bit hidden in the text.

### Questions
1. Line 157: The assumption that different agents must have mutually disjoint action sets looks odd to me. Taking multi-target tracking task as an example, wouldn’t different agents totally have access to execute the same action?
2. Multi-linear extension: I would appreciate that if the author(s) could speak more about how good the continuous relaxation is compared to the original submodular maximization problem and under which conditions. Right now, the presentation just takes this relaxation for granted.
3. In Algorithm 1, what enables the relaxed requirement of a sparse communication graph stated in the contribution statement? Is this part of the author(s) contribution or something enabled by the fact of using existing online mirror ascent methods? A related point is that the author(s) claim that the novelty of their proposed non-oblivious surrogate function for the multi-linear extension objective is the curvature information. Is accounting for the curvature information in non-oblivious surrogate approximation of multi-linear extension a well-recognized challenge in the literature? 
4. The requirement that the objective function needs to be monotone submodular seems to be strong. Can the author(s) elaborate on how restrictive this is?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes two algorithms MA-OSMA and MA-OSEA that collaboratively solve an online, multi-agent submodular optimization problem. Both algorithms produce $\left(\frac{1-e^{-c}}{c} \right)$ sub-optimal solutions in contrast to $\frac{1}{1+c}$ approximate solutions produced by state of the art methods. They also achieve a regret bound of $\tilde O\left( \sqrt\frac{C_TT}{1-\beta} \right)$. The MA-OSMA algorithm requires a costly projection step, this is then removed by using a KL divergence and "mixing uniform distribution" argument in MA-OESA. The method is then illustrated via numerical simulations.

### Strengths
The paper addresses an interesting and relevant problem - motivated by multi-agent robotic problems. The main contributions of the paper are:
- Improving on the state of the art performance bounds of the OSG algorithm by approving the approximation quality to $\frac{1-e^{-c}}{c}$ where $c$ encodes the curvature of the problem.
- The second algorithm, MA-OESA, removes the need for a projection step which allegedly is computationally expensive.

### Weaknesses
I believe there are several areas where this paper can be improved - mostly in the area of presentation and clarity of exposition.

- In section 2.1 the authors state that "each agent $i$ within $\mathcal N$ is equipped with a unique and discrete set of actions". But in the numerical section this seems to be contradicted as the simulation considers the case where each agent has exactly the same choices: up, down, left, right, diagonal etc. Are they unique or identical?!

- In the formulation (1), what is the set $\mathcal A$? Is it just a subset of $\mathcal V$?

- In terms of motivation, it is not clear why the algorithm from Vondrak or Bian et al, cannot be used to achieve the $\frac{1-e^{-c}}{c}$ bound. 

- It's a bit weird to claim that your own algorithm "skillfully harnesses" something. I suggest removing this from the abstract and body.

- The explanation of how to circumvent the fact that KL-divergence is not Lipschitz is not clear at all. The text is full of jargon. What does "mixing a uniform distribution" mean? Neither Theorem 5 nor remark 9 seem to have any parameters from uniform distribution. Please provide some intuition about what is going on here.


- The OSG method should be described and compared to MA-OSMA and MA-OESA in a more direct way. What is the main difference between the algorithms, how do the necessary assumptions differ etc. Why is it that it only achieves $\frac{1}{1+c}$-accurate solutions? This will strengthen the numerical section where it is shown in simulations that the proposed methods out-perform it.

### Questions
- The paper lacks any discussion of how the performance of the two algorithms differ beyond what is in Table 1. How costly is the projection step? How do the two methods differ beyond a factor of $\log T$ regret?
- Does the spectral information show up anywhere in the regret bound of the OSG algorithm? Likewise, do any of the connection graph properties appear in the derivation of the approximation ratio in MA-OSMA or MA-OSEA. It seems like they need to appear somewhere and here they appear in the regret bound - was this an active choice? It seems like there is trade-off between approximation ratio and Regret.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies a multi-agent online submodular maximization problem (MA-OSM). In each step, each agent independently selects a decision from a unique decision set, queries local marginal gains of an underlying submodular function, and exchanges information with neighboring agents. By leveraging a novel surrogate function approach for the multi-linear extension of submodular functions, the paper proposes an online algorithm that achieves a tight approximation ratio relative to the offline solution under a connected communication graph, with a regret bound of $O\left(\sqrt{\frac{C_T T}{1 - \beta}}\right)$, where $C_T$ is the deviation of the maximizer sequence and $\beta$ is the spectral gap of the network. The paper further develops a projection-free variant of the first algorithm, and attains the same approximation ratio with a slight loss in the regret guarantee. Numerical results effectively illustrate the performance of the proposed algorithms compared to prior work, which has sub-optimal approximation ratios.

### Strengths
-  The proposed algorithms improve the approximation ratio of prior work from $\frac{1}{1+c}$ to the tight ratio $\frac{1-e^{-c}}{c}$. Additionally, this improvement is achieved with limited feedback requirements, rather than needing a complete communication graph.

- The use of surrogate functions to overcome limitations related to stationary points in the original multi-linear extension is both effective and inspiring. 

- The paper is well presented, with a coherent flow, clear contributions, and strong results.

### Weaknesses
 - There is some ambiguity regarding the communication complexity of the proposed algorithms. Although they attain a tight approximation ratio, it is unclear if the communication complexity is also tight. Based on the title, the paper seems to claim tight communication efficiency; however, this aspect is not clearly addressed. Specifically, while the paper relaxes the requirement of a complete communication graph, it does not provide a formal analysis of the number of communication rounds or the amount of information exchanged per round, which is crucial for assessing the practical scalability of the algorithms. Additionally, the paper appears to assume a static communication graph, which may not apply to applications like multi-target tracking as discussed in the numerical section. The lack of discussion on how the algorithm would adapt to dynamic changes in the communication topology is a significant limitation.

- In the proposed algorithm, each agent is required to query the local marginal gain oracle multiple times. While this is common in prior work, it is not evident if/how such an oracle would exist in practical applications. The paper does not delve into the practical challenges of implementing such an oracle, especially in scenarios where the underlying submodular function is not explicitly known or is computationally expensive to evaluate. This raises concerns about the applicability of the proposed algorithms to real-world problems where obtaining precise marginal gain information is difficult or impossible.

### Questions
- Could you provide formal comments on the tightness of the communication complexity for both proposed algorithms?
- Since the proposed algorithms can be viewed as an online implementation of offline approximation algorithms, it would be beneficial to provide a formal comparison with the work of [Razazadeh and Kia 2023] in the main paper. 
- The regret guarantee depends on $C_T$, the deviation of the maximizer sequence. Please specify how $C_T$ varies and impacts the regret guarantee. 
- what does the subscript $d$ denote in the regret definition?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes an algorithm for online multi-agent submodular optimization problem, which is then extended to a projection-free variant. The main contribution is that the proposed algorithm relaxes the complete graph assumption and achieves tighter approximation ratio, as compared to the SOTA algorithm.

### Strengths
The paper is overall well-written. The proposed algorithm removes the limitation of complete graph assumption as compared to the SOTA algorithm. It also achieves a tighter approximation ratio as compared to the SOTA algorithm.

### Weaknesses
1. The algorithm's reliance on the curvature parameter $c$ presents a practical challenge. While the authors acknowledge that this parameter may be unknown a priori, a more thorough discussion of its implications is warranted. Specifically, how sensitive are the algorithm's performance and the theoretical guarantees to variations in $c$? An analysis of the algorithm's behavior under different settings of $c$ would be beneficial.

2. The computational cost of the algorithm is a concern. In line 11 of Algorithm 1 and line 12 of Algorithm 2, the objective function needs to be evaluated for $2\sum_i|\mathcal{V}_i|$ times. This can be very inefficient, especially when dealing with complex objective functions $f_t$ that are expensive to evaluate or when the action space is large. It would be helpful to analyze the computational complexity of these steps in more detail and discuss potential strategies for mitigating this cost in practical applications. For example, are there alternative formulations or approximations that could reduce the number of function evaluations without significantly impacting the performance guarantees?

3. The experimental evaluation, while providing valuable insights, could be strengthened. Specifically, the paper lacks a direct verification of the theoretical results. Including a figure that illustrates the ratio between the empirical objective value and the optimal value across different problem instances would provide strong evidence supporting the theoretical claims. Additionally, exploring the algorithm's performance under a wider range of scenarios, including different graph topologies and varying numbers of agents and actions, would enhance the empirical validation.

### Questions
1. Can the authors comment on how to select $c$ in practice?
2. The algorithm introduces a set of hyperparameters such as step size $\eta_t$, mixing parameter, and the weight matrix. Can the authors comment on how to select these hyperparameters?
3. In figure 3, I can understand the utility column. But can the authors elaborate on the other two columns and why are they also interesting?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents two algorithms for solving the multi-agent online submodular maximization problem, accompanied with a convergence analysis for each. Both algorithms achieve near-optimal approximation ratio while requiring less restrictive assumptions about the graph structure (connected instead of complete). Notably, the second algorithm further gets rid of the projection step by using a specific Bergman divergence (KL divergence) within the mirror descent framework. The effectiveness of the proposed algorithms is also validated through a simulated multi-target tracking task.

### Strengths
1. The paper's contributions and the structure are clearly delivered, with additional remarks are provided to enhance understanding. The appendix is well-organized and easy to read.
2. The contributions are interesting and compelling. They advance prior work to a near-optimal approximation ration and substantially relaxing the assumptions regarding graph connectivity.

### Weaknesses
1. Overall, the writing could be improved. This paper is heavy on notations & definitions, and the authors should be more careful when introducing definitions/abbreviations/notations. Specific examples are listed below:

- Line 16: What do OSG, MA-OSMA, MA-OSEA stand for? The contribution "...skilfully (typo) harnessing the KL divergence..." is too technical and detailed for an abstract. A more high-level intuition is expected at this stage.

- Line 49: The abbreviation MA-OSM is introduced twice.

- Line 138: Typo "lowercase."

- "Notations" paragraph: On Line 142, avoid starting a sentence with math notations. The lowercase "s" is used without an explicit definition.

- Line 154: "MA-OSM" is introduced again.

- Line 225: Consider using a different notation than "F" for clarity.

- Theorem 2: Is the phrase "for any x,y" missing?

- Algorithm 1: Using $\eta_t$ suggests an adaptive step size, but it is set to a constant in Remark 8.

- Assumption 5: Is $\mathbb{E}[\tilde{\nabla}F_t^s(x)\mid x]=\nabla F_t^s(x)$ derived from the estimation procedure, or is it an assumption? Constant $G$ is not defined.

- Theorem 5: notation $\gamma$ should be redefined, as its first definition occurs early in the paper and the other one in Algorithm 2 appears only afterwards, which is shown later in the paper. Consider using a different set of parameters than $C_1,C_2,C_3$, which are already used in Theorem 3.

- Line 992: typo "y"->"x"

- Line 1058: "argmin"?

- Line 1100: is $=[y_{t,i}]_{\mathcal{V}\setminus \mathcal{V}_i}$ a typo?

- Line 1126: Typo - $x$ should be $y_{t,i}$ in the first term on RHS.

- Line 1029+1030: Typo $F^A$ should be $F^s$.

- Line 1183: Can you provide more specific references to the results in Nedic&Ozdaglar, 2009 and Horn&Johnson, 2012?

- Line 1291: Typo - $F^A$ should be $F^s$.

- Line 1374: Typo - "the first equation of Lemma 12."

- Line 1420: Typo - $f$ missing.

2. Algorithm 2: It would be beneficial to provide more insights into the difference between Algorithm 1&2.

3. The related work section is not informative enough to provide a high-level overview of earlier work, provide more detailed explanation and comparison of the works listed in Table 1 more in detail would be helpful.

4. Line 83: Please provide citations for these "well-established consensus techniques."

5. For the simulations, error bars are missing from the plot and 5 iterations seems insufficient for drawing robust conclusions.

### Questions
1. The comparison of prior work can be better clarified. For now, the contribution part in the introduction doesn't provide a clear picture of how the improvements are made and why they are novel.
2. The paper would benefit from more detailed insights into improvements and associated trade-offs? E.g. regarding the connectivity of the graph, while the prior work assume a complete graph, but they only require a directed acyclic graph (as indicated in Figure 1). In contrast, the completeness is no longer needed but the edges need to be undirected. Why is this trade-off beneficial? Another similar question comes from the regret bound: it is degrading from $\tilde{\mathcal{O}}(\sqrt{C_T*T})$ to $\mathcal{O}(\sqrt{C_T * T/(1-\beta)})$. Although the simulations suggest improved performance, a theoretical explanation of why this compromise in the regret bound is reasonable would be valuable. Could you provide more insights?
3. Could you elaborate on how to sample from different actions under the constraint "$\sum_{a\in\mathcal{V}_i}x_a\leq 1$" without requiring normalization?
4. Can you clarify the novelty of Theorem 2 compared to Corollary 7 in Zhang et al. 2024 in Remark 3? The results look very similar, apart from the difference in curvature.
5. Can you explain more on the difference between Distributed-CG and this paper? The two seem closely related but Distributed-CG is only mentioned in the appendix.
6. Line 1402: Can you provide a more detailed explanation of why the first inequality follows from the monotonicity of $f_t$? It is applied several time but the connection between the monotonicity of $F$ and monotonicity of $f$ is not clear 
7. Does this paper offer any novel insights into optimization, beyond those already established in the literature?

### Soundness
3

### Presentation
2

### Contribution
3
