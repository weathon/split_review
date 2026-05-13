# Cost-Effective Online Multi-LLM Selection with Versatile Reward Models

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
With the rapid advancement of large language models (LLMs),  the diversity of multi-LLM tasks and the variability in their pricing structures have become increasingly important, as costs can vary greatly between different LLMs. To tackle these challenges, we introduce the \textit{C2MAB-V}, a \underline{C}ost-effective \underline{C}ombinatorial \underline{M}ulti-armed \underline{B}andit with \underline{V}ersatile reward models for optimal LLM selection and usage.  This online model differs from traditional static approaches or those reliant on a single LLM without cost consideration. With multiple LLMs deployed on a scheduling cloud and a local server dedicated to handling user queries, \textit{C2MAB-V} facilitates the selection of multiple LLMs over a combinatorial search space, specifically tailored for various collaborative task types with different reward models. Based on our designed online feedback mechanism and confidence bound technique, \textit{C2MAB-V} can effectively address the multi-LLM selection challenge by managing the exploration-exploitation trade-off across different models, while also balancing cost and reward for diverse tasks. The NP-hard integer linear programming problem for selecting multiple LLMs with trade-off dilemmas is addressed by: i) decomposing the integer problem into a relaxed form by the local server, ii) utilizing a discretization rounding scheme that provides optimal LLM combinations by the scheduling cloud, and iii) continual online updates based on feedback. Theoretically, we prove that \textit{C2MAB-V} offers strict guarantees over versatile reward models,  matching state-of-the-art results for regret and violations in some degenerate cases. Empirically, we show that \textit{C2MAB-V} effectively balances performance and cost-efficiency with nine LLMs for three application scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Main problem statement: the problem statement is clear and well-motivated (i.e. the setup of selecting a subset of LLMs/experts to answer a given query, in a cost and reward-sensitive environment. I do think combinatorial bandits are a reasonable way to model this problem, although I do have some nits about it which I’ll mention below).
Idea - the technical/intellectual contribution of the paper isn’t inherently about LLMs, in my opinion.I think the main idea is a new combinatorial bandit algorithm (which they dub C2MAB-V), which attempts to do exploration/exploitation and bandit-feedback updates in tandem with solving the submodular optimization described in Eq.3. I certainly have not seen this algorithm in the literature before, but I should caveat by saying that I am not an expert on combinatorial bandits. (As an aside, I do see a paper of Karthik’s referenced here on comb. bandits, so it may be worth getting his gut-check?) In addition to the new algorithm, the authors also derive a regret bound.
Novelty - Both the C2MAB-V and its regret analysis (Theorem 1) are novel as far as I (a non-expert) know.
Evaluation - the empirical evaluations are interesting and suggest that C2MAB-V does empirically outperform other “naive” alternatives such as always going with the best/most expensive model. I am curious to know why the y-axis in Fig 4 is reward / budget violation. The presence of the budget violation term there is a bit puzzling to me. Any feasible solution of (3) should be budget feasible and so budget should never really be violated (i.e. the denominator should always be zero)?
Benchmark - In Fig 4., evaluation is done against a good set of benchmarks including eps-greedy, Thompson sampling, and combinatorial UCB
Practical deployability?
I have some “weak” concerns about the practical “deployability” of the ideas proposed here in the context of LLMs. Some alternative ways that cost and performance tradeoffs may potentially be navigated for practical large-scale systems involve avoiding the appeal to MAB altogether, and its unclear whether this paper can prescribe into any insights about the relative merits of leveraging MAB versus other approaches. One such approach is Mixture-of-Experts (MoE) where the experts are directly absorbed as “sub-models” inside a larger model and the task of identifying which expert to direct a task to is also captured inside the model and learnt in the pre-training phase. Another approach is to appeal to “Composition of Experts (https://arxiv.org/pdf/2405.07518)”, where given some expert models, a new model is trained to learn to route a given task to the best set of experts. Based on this paper, can we draw any conclusions vis-a-vis MoE vs CoE vs MAB-combination of different LLMs?
One other deployability challenge that I see (and I don’t think was adequately addressed in the paper) is the contextual nature of the problem. Given a task, it seems to me that the context for that task (e.g. the required expertise e.g. medicine vs biology vs math) is needed to meaningfully identify the potential reward and also cost, and we’d need the bandit feedback to be contextual. In the method described by the authors, it is unclear whether and how the context is captured. I do believe the regret analysis itsef would also change substantially based on whether the algorithm describes a non-contextual vs a contextual implementation (since uncertainty quantification is far more nuanced in the contextual setup)

### Strengths
I think the core explore-exploit algorithm that was introduced is new (to this reviewer), interesting, and also comes with potentially new regret guarantees.

### Weaknesses
Main problem statement: the problem statement is clear and well-motivated (i.e. the setup of selecting a subset of LLMs/experts to answer a given query, in a cost and reward-sensitive environment. I do think combinatorial bandits are a reasonable way to model this problem, although I do have some nits about it which I’ll mention below).
Idea - the technical/intellectual contribution of the paper isn’t inherently about LLMs, in my opinion.I think the main idea is a new combinatorial bandit algorithm (which they dub C2MAB-V), which attempts to do exploration/exploitation and bandit-feedback updates in tandem with solving the submodular optimization described in Eq.3. I certainly have not seen this algorithm in the literature before, but I should caveat by saying that I am not an expert on combinatorial bandits. (As an aside, I do see a paper of Karthik’s referenced here on comb. bandits, so it may be worth getting his gut-check?) In addition to the new algorithm, the authors also derive a regret bound.
Novelty - Both the C2MAB-V and its regret analysis (Theorem 1) are novel as far as I (a non-expert) know.
Evaluation - the empirical evaluations are interesting and suggest that C2MAB-V does empirically outperform other “naive” alternatives such as always going with the best/most expensive model. I am curious to know why the y-axis in Fig 4 is reward / budget violation. The presence of the budget violation term there is a bit puzzling to me. Any feasible solution of (3) should be budget feasible and so budget should never really be violated (i.e. the denominator should always be zero)?
Benchmark - In Fig 4., evaluation is done against a good set of benchmarks including eps-greedy, Thompson sampling, and combinatorial UCB
Practical deployability?
I have some “weak” concerns about the practical “deployability” of the ideas proposed here in the context of LLMs. Some alternative ways that cost and performance tradeoffs may potentially be navigated for practical large-scale systems involve avoiding the appeal to MAB altogether, and its unclear whether this paper can prescribe into any insights about the relative merits of leveraging MAB versus other approaches. One such approach is Mixture-of-Experts (MoE) where the experts are directly absorbed as “sub-models” inside a larger model and the task of identifying which expert to direct a task to is also captured inside the model and learnt in the pre-training phase. Another approach is to appeal to “Composition of Experts (https://arxiv.org/pdf/2405.07518)”, where given some expert models, a new model is trained to learn to route a given task to the best set of experts. Based on this paper, can we draw any conclusions vis-a-vis MoE vs CoE vs MAB-combination of different LLMs?
One other deployability challenge that I see (and I don’t think was adequately addressed in the paper) is the contextual nature of the problem. Given a task, it seems to me that the context for that task (e.g. the required expertise e.g. medicine vs biology vs math) is needed to meaningfully identify the potential reward and also cost, and we’d need the bandit feedback to be contextual. In the method described by the authors, it is unclear whether and how the context is captured. I do believe the regret analysis itsef would also change substantially based on whether the algorithm describes a non-contextual vs a contextual implementation (since uncertainty quantification is far more nuanced in the contextual setup)

### Questions
No direct questions, but I welcome responses from the authors on the deployability and other aspects raised above.

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
3

### Summary
This paper formulates the multi-LLM selection problem as a combinatorial bandit problem. The authors develop an online bandit algorithm for online multi-LLM selection where different types of reward modes are applied. Also, the authors consider a computational cost constraint on the LLM selection. The paper provides analysis for regret and constraint violation.  The performance is evaluated based on  the SciQ dataset.

### Strengths
This paper has the following strengths:
+ This paper consider an interesting problem which selects LLM models on cloud. 
+ This paper provides good formulations for online LLM selection problem. Different reward models are considered. Budget constraint of the scheduling cloud is also modeled.
+ Performance analysis is provided for the combinatorial bandit problem.

### Weaknesses
The paper can be improved in the following aspects.
- This paper considers the LLM selection problem. However the reward are modeled as some simple equations in page 5 and look like some toy models. These models cannot accurately reflect the real evaluation of combinatorial LLMs.
- The algorithm design is a simple extension of combinatorial bandits. The analysis of the algorithm also loos similar as the previous results on combinatorial bandits. It would be better if the authors can present the new challenges and techniques used in the algorithm and analysis.
- The empirical results are carried out for only one dataset.  Also, the choices of the parameters like budget threshold, $\alpha$, etc are not explained. This is not enough to verify the proposed algorithms.

### Questions
Please see the questions above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a model of Cost-effective Combinatorial Multi-armed Bandit with Versatile reward for the optimal selection of multiple large language models (LLMs). The proposed approach aims to manage the exploration-exploitation trade-off while balancing costs and rewards in a collaborative LLM setting, using an online learning framework. The paper provides a theoretical analysis of regret and budget violation bounds, demonstrating that the proposed approach C2MAB-V matches state-of-the-art results in certain degenerate cases. Empirical experiments validate its effectiveness in balancing cost-efficiency and performance across three scenarios with nine LLMs.

### Strengths
1. The formulation of the problem as a cost-effective combinatorial multi-armed bandit with versatile reward models is interesting and applicable in real-world scenarios where cost-efficiency is crucial. The paper reads well and includes examples/intuition to help the reader.

2.  The authors provide a rigorous theoretical analysis of the regret and budget violations of the proposed algorithm, achieving results that match the state-of-the-art in several degenerate cases. Plus, the case-by-case analysis for different reward models provides enough insights about the discretization rounding procedure, which is crucial for understanding the proposed method.

3. The paper presents extensive empirical evaluations using various LLMs across three application scenarios, providing strong evidence for the proposed method's effectiveness.

### Weaknesses
1. The algorithms and theoretical analysis presented are natural extensions of previous approaches, specifically in the combinatorial multi-armed bandit literature. Also, I do not believe that non-linear rewards pose a significant challenge for the analysis, as the paper assumes that the reward function is Monotone and Lipschitz. Therefore, the regret analysis can be converted to the accumulated impact of overestimating rewards, just as most of the literature does. Hence, I cannot give a score higher than 6 (accept).

2. Lines 1240-1241 contain content that seems unrelated to the context and should be revised or removed.

3. The literature on Combinatorial Multi-Armed Bandit with Knapsack Constraints is highly relevant to this paper's content, yet it has not been formally reviewed in Section 2.1 (Related Work). I highly recommend the authors Incorporate a formal review of these works in the revised paper.

### Questions
1. I noticed that LLaMA 2 was used for comparison in the experiments, but LLaMA 3 has also been released. I am curious why there was no comparison with LLaMA 3 in the experiments.

2. When the reward function is linear, can instance-dependent performance bounds be derived based on a sub-optimality gap defined by the extreme points?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the problem of the selection of multiple large language models (LLMs) with versatile reward models in an online manner. A framework named C2MAB-V, i.e., a cost-effective combinatorial online model with a versatile reward structure, has been proposed to select multiple LLMs based on specific task and requirements while adhering to the budget constraint. The performance of C2MAB-V has been both analyzed theoretically and evaluated via experiments. On the theoretical side, both the regret and violation bounds are provided. On the numerical side, the performance of C2MAB-V has been evaluated with nine LLMs under various settings.

### Strengths
- This paper studies a timely and interesting problem in the context of LLMs, in particular considering the selection of multiple LLMs with versatile reward models and in an online manner 
- A new framework named C2MAB-V, i.e., a cost-effective combinatorial online model with a versatile reward structure, has been proposed to select multiple LLMs based on specific task and requirements while adhering to the budget constraint.
- Both the regret and violation bounds for C2MAB-V have been provided.
- The performance of C2MAB-V is further evaluated via extensive experiments, e.g., including nine LLMs under various settings.

### Weaknesses
 - Despite the studied problem is timely and interesting, the intrinsic nature of the problem is not quite new. In other words, it is still a combinatorial online optimization problem but simply framed in a new LLM setting. 
- Likewise, the proposed online algorithm C2MAB-V is not much in difference with the exiting methods as mentioned in the related works. 
- The paper is very dense and sometimes hard to understand. For instance, it introduces three reward models, i.e., AWC, SUC, AIC. What are the fundamental differences between these models? What are the impacts on the algorithm designs and analysis? It is not quite clear and the analysis seems to only focus on one model, and not sure if you need to present all of them in the main paper. For instance, it may be better to just present AWC which has the regret analysis in Section 5, and then has a new section just to discuss the extension to SUC and AIC models with numerical evaluations. 

Minor:
- This paper is framed very densely and many spaces are squeezed. For instance, there is almost no space between lines 243 and 244.

### Questions
- In section 3, a subset $S_t$ is selected from the available LLMs set $\mathcal{K}$. This is termed as an "action" and satisfies $|S_t|\leq K$. Right after that, $N=\max_{S\in\mathcal{S}}|S|$ is defined as the maximum number of LLMs that can be simultaneously active. What are the differences or the relations between $K$ and $N$? 
- This paper introduces three reward models, i.e., AWC, SUC, AIC. What are the fundamental differences between these models? What are the impacts on the algorithm designs and analysis? The performance analysis in Section 5 is only for AWC. What about the performance guarantees under SUC and AIC. If there is no such results, what's the point to present these models in Sections 3 and 4, which make the paper very dense and hard to follow. 
- For a budget constraint $\rho$, why does the definition of $V(T)$ require a max operator? In many constrained RL or constrained MDPs, the violation constraint is naturally defined without a max operator. Can you elaborate on this? 
- In Section 4.1, several relaxation strategies for LLM selection have been discussed. However, are the solutions to these relaxations feasible to the "original" problem defined in Section 3 with the constraint that must be satisfied? This may be obviously infeasible. Can you clarify how to further design the solutions on top of the solutions to these relaxation problems? 
- For the violation bound in Theorem 2, the right hand size of (8) has two terms, one in the order of $\mathcal{O}(\sqrt{K/T})$ and the other $\mathcal{O}(K/T)$. The authors claimed that the violation decreases at a rate of $\mathcal{O}(\sqrt{K/T})$. In addition, why "the overall violation is shown to be $\mathcal{O}(\sqrt{KT})$ as claimed in lines 457-458? 
- How tight is the upper bound in Theorem 1? The coefficient can be extremely large on the right hand size of (7) associated with the $T$ terms. similarly for the constant term $(K+1)r^*$ that is in the order of $(K+1)NL$.

### Soundness
2

### Presentation
2

### Contribution
2
