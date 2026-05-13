# A Markov decision process for variable selection in Branch and bound

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Mixed-Integer Linear Programming (MILP) is a powerful framework used to address a wide range of NP-hard combinatorial optimization problems, often solved by Branch and bound (B\&B). A key factor influencing the performance of B\&B solvers is the variable selection heuristic governing branching decisions. Recent contributions have sought to adapt reinforcement learning (RL) algorithms to the B\&B setting to learn optimal branching policies, through Markov Decision Processes (MDP) inspired formulations, and ad hoc convergence theorems and algorithms. In this work, we introduce B\&B MDPs, a principled vanilla MDP formulation for variable selection in B\&B, allowing to leverage a broad range of RL algorithms for the purpose of learning optimal B\&B heuristics. Computational experiments validate our model empirically, as our branching agent outperforms prior state-of-the-art RL agents on four standard MILP benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies learning efficient branching strategies by reinforcement, and introduces B&B MDPs, a principled vanilla MDP formulation for variable selection, allowing to leverage a broad range of RL algorithms for the purpose of learning optimal B&B heuristics. The proposed method defines a Bellman optimality operator to unlock the full potential of approximate dynamic programming algorithms. On easy instances, DQNBBMDP consistently obtains best performance among RL agents

### Strengths
This paper overperforms the previous RL agents while narrowing the gap with the IL approach.

### Weaknesses
1. The primary innovations of BBMDP are unclear.
2. The experiments are conducted on a relatively small scale. The medium instances require only 1 minute to solve.
3. BBMDP's performance is not significantly superior to other RL methods. It is even inferior on the medium dataset.

### Questions
1. Could you clearly differentiate between BBMDP and TreeMDP?
2. Regarding the statement: “Yet, if the performance of IL heuristics are capped by that of the suboptimal branching experts they learn from, the performance of RL branching strategies are, in theory, only bounded by the maximum score achievable.” What does "suboptimal branching experts" refer to? Is it the strong branching rule?
3. On page 2, line 91, there's a mention of “Since ρ necessarily defines a total order on nodes.” Given that node selection and variable selection influence each other, what does it mean to have this fixed order?
4. Could you conduct tests on larger datasets, similar to those used by Gasse et al.?
5. Would it be possible to provide additional metrics, such as wins and P-D convergence plots?

### Soundness
3

### Presentation
1

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
The paper investigates an RL method for variable selection in branch-and-bound. It applies the general definition of MDP to B&B search so that general RL algorithms and theories can be applied to solve the problem. The MDP is solved with Q-learning. In experiments, the method is evaluated on four standard MILP benchmarks and compared against other RL methods. It achieve the best results compared to other RL methods, but still worse than IL methods.

### Strengths
1. The paper developed BBMDP tailored for B&B search that allows the application of a boarder range of developed RL methods.
2. The empirical results look promising in comparison to other RL methods.
3. The paper is well-written and easy to follow.

### Weaknesses
I don’t see major weaknesses, but have a couple of questions that could be of potential improvement to the paper:
1. Can you show the sample complexity of the methods compared to previous ones?
2. Is your methods also effective on larger instances? For instances that cannot be solved within the runtime limit, one can still evaluate the primal-dual gap/primal-dual integral to see if the method is effective or not.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel Markov Decision Process (MDP) framework, BBMDP, for optimizing variable selection in Branch and Bound (B&B) algorithms in Mixed Integer Programming (MIP). By restricting the node selection strategy to depth-first search (DFS), the authors derive a more canonical Bellman equation for BBMDP, enabling broader use of reinforcement learning frameworks. This approach offers greater robustness than existing TreeMDP models by preserving optimality and convergence properties. The authors apply Deep Q-learning to BBMDP, demonstrating improved performance over previous RL approaches on TreeMDP across multiple MILP benchmarks, with significant reductions in both computation time and the number of B&B nodes required. Results further suggest that BBMDP effectively narrows the gap between reinforcement learning and imitation learning methods.

### Strengths
1. The paper is well-written and easy to follow
2. The introduction of BBMDP provides a principled, canonical MDP formulation for variable selection in B&B, addressing limitations of previous TreeMDP approaches by enabling a broader application of reinforcement learning techniques with theoretical support.
3. The paper includes experiments on many standard MILP benchmarks

### Weaknesses
The adoption of a DFS node selection strategy allows for a more canonical Bellman operator and potentially broader applicability of current RL frameworks. However, the impact of this restriction on performance is not fully explored, and the paper lacks a discussion on potential trade-offs related to this design choice. Specifically, while DFS simplifies the MDP formulation, it is not generally considered an efficient node selection strategy for B&B, and the paper does not adequately address whether the performance gains from the simplified MDP outweigh the potential loss of efficiency from using DFS. A more thorough analysis of the implications of this design choice is needed, including a comparison against other node selection strategies.

The authors highlight BBMDP’s potential to support a wider range of RL algorithms, yet only DQN, which is also compatible with TreeMDP, is tested. Consequently, the empirical results do not demonstrate the benefits of BBMDP’s broader RL applicability. The paper should include experiments with other RL algorithms that leverage the specific advantages of the BBMDP framework, such as those that rely on multi-step temporal difference learning or model-based approaches, to substantiate the claim of wider applicability. Without such experiments, the claimed advantage remains theoretical.

For medium instance testing, only 20 instances are evaluated, which may be insufficient to reliably represent each problem class. Increasing the test set to at least 100 instances would provide a more robust assessment of performance across diverse scenarios. The limited number of instances raises concerns about the generalizability of the results and the robustness of the conclusions drawn from them. The paper should also include a more detailed analysis of the variance in performance across the instances, to better understand the consistency of the proposed method.

When comparing methods on node count and solution time, there are inconsistencies between the two metrics: a shorter runtime does not always correspond to fewer nodes processed. For instance, DQN-BBMDP sometimes achieves a lower node count yet requires more time, and vice versa when compared with IL approaches. This discrepancy suggests that the time spent processing each node may vary significantly between different methods, and this should be investigated further. The paper should include a more detailed analysis of the computational cost per node for each method.

While the proposed methods show improved performance and reduce the gap with IL approaches, a considerable performance disparity remains. The fact that IL methods still significantly outperform the proposed RL approach raises questions about the practical applicability of the method in its current form. The paper should discuss the limitations of the proposed approach in more detail and outline potential avenues for future research to close this performance gap.

Additionally, all tested problem classes are synthetic mathematical benchmarks, leaving the performance on realistic datasets unexamined. The lack of experiments on real-world datasets makes it difficult to assess the practical relevance of the proposed approach. The paper should include experiments on real-world instances to demonstrate the applicability of the method in practical settings.

### Questions
Besides the concerns raised in the weakness part, I have the following additional questions:

1. Why define R(s, a) = −2 for all transitions until episode termination? Is intuition behind the number -2? Is that the results of tuning?
2. Any intuition of why choosing the HL-Gauss cross-entropy loss?
3. Why not including IL-DFS to the medium problem classes? Will the drop of the performance of using DFS will become more significant for the larger instances?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses the issue that these alternative MDP formulations introduce approximations that undermine the asymptotic performance of RL branching agents in the general case. This paper introduces a B&B MDP formulation for variable selection in B&B, which preserves optimality without sacrificing the convergence properties brought by previous contributions. Computational experiments validate our model empirically, as our branching agent outperforms prior state-of-the-art RL agents on four standard MILP benchmarks.

### Strengths
1)	Original: This paper introduces a vanilla MDP formulation for variable selection in B&B, allowing the leveraging of a broad range of RL algorithms to learn optimal B&B heuristics.
2)	Quality:
The overall presentation is good
The paper discusses the related works about RL-based methods in a fairly clear manner.
3)	Clarity: 
Overall, the paper is clear and easy to follow, however, some writing is confusing, especially since some symbols are not defined.
4)	Significance: 
The paper studies introduce a vanilla MDP applied to the variable selection problem to learn optimal B&B branching strategies, which seems to be an important research direction.

### Weaknesses
1.	The related work about imitation learning for variable selection is insufficient,
2.	There is no pipeline to explain how the proposed method works.
3.	The proposed method seems to only apply to the binary integer programming problem, it is a little unclear to me how much technical novelty is in the B&B MDP and whether the contributions in this paper are significant enough.
4.	The experiment seems insufficient, only testing in easy and medium difficulty levels, lack of comparison in hard difficulty levels.
5.	The ideas in the paper took me some time to properly digest. I believe all of the information needed for the reader to digest is there, but think that the paper could make this process easier for the reader.

### Questions
1.	The meaning of symbols is confusing. For example, what’s the meaning of ($v, \varepsilon$) in Line 84?
2.	Why is the reward defined as -2 in the MDP definition, as I know, some papers define the reward as -1[1], can you explain it?
3.	This may be important because the convergence guarantees of RL algorithms are often made in the discounted setting with litter than 1, Why is this paper setting the discounted with 1. Is there any experimental or theoretical support for this point?
4.	According to Gasse et al. (2019), why was this paper not compared to the facilities dataset? Why was this paper not compared to the hard dataset? Why does this paper not report the average per-instance standard deviation in Table 1?
5.	Why did this paper only test 20 instances on the medium transfer instances instead of testing 100 instances like the easy difficulty level? What would happen if this method also tested the 100 instances on the medium difficulty level?
6.	For the variable selection problem, reinforcement learning seems to have no advantage over imitation learning both in training speed and testing effectiveness. So, what is the motivation behind our research in this paper?
7.	Some articles have already defined branching as MDP [1]. Can you summarize the differences between you and these articles?
8.	The contribution summary of the article is unclear. Can you further summarize it?
[1] Improving Learning to Branch via Reinforcement Learning. NeurIPS Workshop, 2020. https://openreview.net/forum?id=z4D7-PTxTb

### Soundness
2

### Presentation
3

### Contribution
2
