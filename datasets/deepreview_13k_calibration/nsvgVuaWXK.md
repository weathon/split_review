# Provably Efficient Learning in Partially Observable Contextual Bandit

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
In this paper, we investigate transfer learning in partially observable contextual bandits, 
where agents have limited knowledge from other agents and partial information about hidden confounders.
We first convert the problem to identifying or partially identifying causal effects between actions and rewards through optimization problems.
To solve these optimization problems, we discretize the original functional constraints of unknown distributions into linear constraints, 
and sample compatible causal models via sequentially solving linear programmings to obtain causal bounds with the consideration of estimation error. 
Our sampling algorithms provide desirable convergence results for suitable sampling distributions. 
We then show how causal bounds can be applied to improving classical bandit algorithms and affect the regrets with respect to the size of action sets and function spaces.
Notably, in the task with function approximation which allows us to handle general context distributions,
our method improves the order dependence on function space size compared with previous literatures.
We formally prove that our causally enhanced algorithms outperform classical bandit algorithms and achieve orders of magnitude faster convergence rates. 
Finally, we perform simulations that demonstrate the efficiency of our strategy compared to the current state-of-the-art methods.
This research has the potential to enhance the performance of contextual bandit agents in real-world applications where data is scarce and costly to obtain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies partially observable contextual bandits, where the context comprises 2 variables W, U and the agent have access to W only while U is hidden. The problem is mapped to the framework of causal effects between actions and rewards and formulated as an optimization problem that is solved using sampling and LP techniques. The proposed algorithms are shown to have orders of magnitude better regret than classical bandit algorithms.

### Strengths
- The considered problem is important and has multiple applications.
- The approach is novel.
- The resulting regrets are smaller than those of existing bandit algorithms.

### Weaknesses
 - The writing of the paper can be substantially improved. Many of the definitions and arguments are not clear to me from a theoretical aspect. Please see my questions below regarding this.

- The regret definition is written in terms of W only (not U). At each time slot, do you compete with a policy that has access to the true function $f^*$ and both realizations of W, U or you compete against policy that has access to $f^*$, W and take expectation over U?

- What is h(a) in table (1)? 

- What is sup/inf in equation (1)? Is it either inf or sup, both will work? Do you mean that one will give an upper bound and the other a lower bound? This should be clearly stated. In the same paragraph you mention that (1) gives a bound on the causal effects. Causal effects between which variables? What is the mathematical formula for the causal effect to see that (1) gives an upper bound?

- If the algorithms are applied in the famous case of contextual linear bandits, what would be the resulting regret in that case?

- The works in [1,2,3] consider contextual linear bandits with known context distribution without observing the realization. Even though the setup is more limited, I believe the authors need to provide a comparison when the results of the paper are limited to the setups of [1,2,3].

The paper has a novel idea, but it is hard to follow the math and verify the results. I suggest the authors make the paper more clear and rigorous. Please explain the results with more math and logic. A table of notations would also help. I will update my score after reading the authors response.

### Questions
Please see. weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers a transfer learning in a causal bandit problem where a bandit agent receives observational data from an expert agent. In particular, some of the covariates used in the agent is unavailable but partial information is available. Overall, this paper combines the (improved) causal bounds by Li and Pearl and the idea of transfer learning by Zhang and Bareinboim. There are several considerations in improving causal bounds (tigher bounds) and obtaining them pratically (sequential linear programming, estimation error, sampling then optimization). Further, bandit algorithm also has improvement through considering dependency among policies.

### Strengths
This paper is more than the combination of transfer learning algorithm (ZB) and causal bounds (LP). 
- incorporation of estimation error (in Appendix, which should be in the main paper. It can be only two or three sentences). To make use of small number of available data, naively using maximum likelihood estimates can be misleading. The use of estimation error into bounds is simple yet an important step (especially in transfer learning setting where some of the arms might be truncated) BTW, epsilon in the Algorithm 1 should be highlighted.
- (Eq 3) tigther bounds than Li and Pearl, which is shown to not satisfy constraints over the available information
- practical sampling approach (Eq 4) which avoids rejection sampling.
- The sample, then optimization approach.

### Weaknesses
No specific weakness other than the organization, which will be mentioned in the questions (and suggestions) section.

- The paper seems abruptly trimmed or cut during submission. There is no conclusion or discussion. For example, Table 1 should be after Theorem 3.4. Without providing context, it is too abrupt. Further, it seems that table next Table 1 does not have a proper caption. Increase arraystretch to represent table better.
- The organization near Eq 5 and 6 are awkward.
- BTW, lines 1,3,4,6 could be one-liner and Fig 1 can be a lot smaller to afford more space… 
- There are many pointers to Appendix which somewhat distracts the flow.
- In Page 8 near at the end, I don’t get the argument here about instrumental variables. If they rely on IV, you may argue that your method is free of IV requirement. It is a bit unnecessary to mention that finding IV is an open problem in academia (Economics?).  
- adjust the two plots in Figure 2

### Questions
- Given that ICLR will allow an additional one page, it is expected that the authors will incorporate necessary, important information currently trimmed or in Appendix. 
- The paper seems abruptly trimmed or cut during submission. There is no conclusion or discussion. For example, Table 1 should be after Theorem 3.4. Without providing context, it is too abrupt. Further, it seems that table next Table 1 does not have a proper caption. Increase arraystretch to represent table better.
- The organization near Eq 5 and 6 are awkward. 
- BTW, lines 1,3,4,6 could be one-liner and Fig 1 can be a lot smaller to afford more space… 
- There are many pointers to Appendix which somewhat distracts the flow.
- I suggest Causal Bounds as a separate section and use subsection/paragraph properly. Causal bounds can be described irrelevant to the transfer learning problem. Current paragraphs “Causal Bounds” and “Sampling valid causal models” as a whole can be in the section and can be restructured. 
- In Page 8 near at the end, I don’t get the argument here about instrumental variables. If they rely on IV, you may argue that your method is free of IV requirement. It is a bit unnecessary to mention that finding IV is an open problem in academia (Economics?).  
- adjust the two plots in Figure 2

By the way, this paper would be more like for AISTATS, CLeaR (causal conference), NeurIPS, ICML ... I wonder why the authors pick the ICLR as the 'best' revenue to present the results. I don't see any part 'representation learning' involved. Given the type of the audience, I rate this paper 'marginally above' the threshold. Otherwise, I will raise to 'accept'.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies PO contextual bandits. In this setting information is transferred between an expert who already has prior information about the joint distribution in this setting, to solve for a setting with unobserved confounders.
- The paper uses linear programming to obtain sample complexity bounds on the regret.
- The paper carries out strong experimental evidence to suggest that the transfer learning algorithm can improve the performance of agents.

### Strengths
- The analysis is sound, though notations and clarity can be improved.
- The improvement in regret bound in the given setting is significant. Having said that the advantage to the agent to obtain the improvement in sample complexity is that P(X,Y,W) and separately P(U) is known. The alternative algorithms do not have access to such priors. This expertise from the expert who already knows the joint priors is "transferred" in the transfer learning setting.
- The paper provides a lower bound for their analysis, which is reasonably hard to find.
- The paper shows a significant improvement over baselines in Figure 2.

### Weaknesses
 - The transfer learning problem for PO Contextual bandits is not well motivated.
- The example on Page 3 is supposed to motivate, "direct approaches can lead to a policy function that is far from the true optimal policy". But I was not able to see this. How do you get the numbers 1.81? Rather, isn't the example motivating the need for considering U in the policy, if available?
- "The expert summarizes its experiences as the joint distribution Fˆ(a, y, w). However, there exists a latent confounder U that affects the causal effects between actions and rewards, making the observed contextual bandit model incomplete. The agent wants to be more efficient and reuse the observed Fˆ(a, y, w) along with the extra prior knowledge about U, i.e., Fˆ(u), to find the optimal policy faster." This is the motivation for the paper.

- The claim on sample complexity of the joint distribution F(a, y , w, u) given F(u) as well as F(a, y ,w) separately, is quite different from learning the full joint distribution from scratch. Therefore the comparison with existing sample complexity analysis is slightly misleading. Specifically, "Our regret demonstrates an improvement in dependence on policy space Π from P(|Π|) to P(log |Π|) compared with ...." is not entirely fair.

- x_ijkl is not very informative as a subscript. Please consider revising this terminology?

---

### Experiments
- The experiments show "that solving non-linear optimization is quite unstable".
- The baselines considered are clear, but the setting is quite unclear. Specifically, is the setting considered general enough, or is it tailored to favor the algorithm proposed in the paper?

### questions:
 - The authors claim improving regret from sqrt(|P|) to sqrt(log(|P|)), but Table 1 shows regret proportional to sqrt(|A|) for the algorithms proposed.
- In page 3 the authors say, "expert agent can observe the contextual variable in U,W". But also say in Figure 1 caption that "U is the unobserved context". Then why can any expert agent view this?
- Page 4 para 2, what is "skewness from F(u)"?
- If there is an expert who has already learnt the joint distribution F(a, y, w), and further only finite  
- In equation 1, can you specify what sets the sup and inf are over?

### Questions
- The authors claim improving regret from sqrt(|P|) to sqrt(log(|P|)), but Table 1 shows regret proportional to sqrt(|A|) for the algorithms proposed.
- In page 3 the authors say, "expert agent can observe the contextual variable in U,W". But also say in Figure 1 caption that "U is the unobserved context". Then why can any expert agent view this?
- Page 4 para 2, what is "skewness from F(u)"?
- If there is an expert who has already learnt the joint distribution F(a, y, w), and further only finite  
- In equation 1, can you specify what sets the sup and inf are over?

---

### Minor Suggestions/Typos:
- Table 1: rows 1,3,5 are the classical algorithms?
- Consider changing: "...investigate partially observable contextual bandits, we found few papers focusing on transfer learning in partially observable contextual bandits." --> "...we found few papers focusing on transfer learning in this setting."
- mainly select the arm 1--> mainly selects arm 1.
- Can the notations in Equation 2 be simplified?
- "sequentially solving linear programmings" --> sequentially solve linear programs".

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this research, the authors focus on the difficulties associated with transfer learning in situations involving partially observable contextual bandits (TLPOCB), motivated by real-world scenarios like autonomous driving. Traditional bandit algorithms lack prior knowledge and can be computationally intensive. Although transfer learning techniques, which utilize knowledge from related tasks, are applied, they often encounter the problem of biased learned strategies due to incomplete information transfer from experts to agents. To address these issues, the authors introduce novel causal bounds for TLPOCB tasks and develop algorithms that improve learning efficiency.

### Strengths
The writing is clear and the problem presented is interesting. The proposed algorithms improve on the existing methods in Li and Pearl (2022).

### Weaknesses
The problem setup is spread out into multiple sections and it takes the reader a long time to understand the main topic to be explored. I believe a dedicated section for setup will streamline the reader's understanding.
Some relevant references are missing. For example, there is a line of work including [1],[2],[3] which study the sequential problem under partial observation, characterized by graphs. I think a comparison is needed.

### Questions
Since this paper is dealing with a subtle topic at the intersection of bandit, transfer learning, and partial monitoring, a thorough comparison with the existing work should be expected, detailing the connection and difference, which seems missing in the current version.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
