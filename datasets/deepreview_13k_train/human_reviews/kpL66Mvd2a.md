# Tree Search for Language Model Agents

- Decision: Reject
- Scores: 5, 8, 3, 6

## Abstract
Autonomous agents powered by language models (LMs) have demonstrated promise in their ability to perform decision-making tasks such as web automation. However, a key limitation remains: LMs, primarily optimized for natural language understanding and generation, struggle with multi-step reasoning, planning, and using environmental feedback when attempting to solve realistic computer tasks. 
Towards addressing this, we propose an inference-time search algorithm for LM agents to explicitly perform exploration and multi-step planning in interactive web environments. 
Our approach is a form of best-first tree search that operates within the actual environment space, and is complementary with most existing state-of-the-art agents. 
It is the first tree search algorithm for LM agents that shows effectiveness on realistic web tasks. 
On the challenging VisualWebArena benchmark, applying our search algorithm on top of a  GPT-4o agent yields a 39.7\% relative increase in success rate compared to the same baseline without search, setting a state-of-the-art success rate of 26.4\%. On WebArena, search also yields a 28.0\% relative improvement over a baseline agent, setting a competitive success rate of 19.2\%. 
Our experiments showcase the effectiveness of search for web agents, and we demonstrate that performance scales with increased test-time compute. 
We conduct a thorough analysis of our results to highlight improvements from search, limitations, and promising directions for future work.
Our code and models are publicly released at \href{https://jykoh.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a tree search algorithm for improving the performance of language model agents. By implementing a best-first search approach that operates in the environment's actual state space, the authors enable LM agents to achieve multi-step planning and exploration during inference. Experiments are conducted on VisualWebArena and WebArena benchmarks with improved performance, showing that introducing search allows agents to perform better on complex tasks.

### Strengths
1. Experiments are conducted on several practical benchmark datasets such as VisualWebArena and WebArena, showcasing its effectiveness in web-based tasks.

2. The search algorithm is compatible with a variety of LM agents and does not require fine-tuning or retraining.

3. Extensive hyper-parameter analysis is provided.

### Weaknesses
1. The search algorithm demands significant computational resources due to the increased number of environment interactions. This may limit its practical applicability in real-time or resource-constrained environments.

2. The success of the best-first search depends heavily on the quality of the value function. Although self-consistency techniques were used, further improvements in the value function are needed for optimal performance.

3. The paper briefly addresses the issue of destructive actions in search trajectories but lacks a comprehensive solution. This is a critical consideration for deployment in real-world web environments where irreversible actions are possible.

### Questions
1. How does the search algorithm perform on tasks with very high action complexity or longer required sequences? Are there any indications that increasing the search budget might lead to diminishing returns in such cases?

2. Can the authors provide more details on how the environment resets are managed during backtracking? Specifically, what challenges arise, and how might these affect the agent’s efficiency?

3. What were the key considerations in selecting the self-consistency technique for the value function? How does this compare to alternative approaches like reinforcement learning-based value functions?

4. Are there any safeguards or heuristics incorporated to prevent the agent from becoming stuck in specific repetitive or irrelevant actions during search?

### Soundness
3

### Presentation
2

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
This paper proposes a tree search algorithm for web agents.

The search algorithm expands states using best first search where the value of the state comes from LLM self-evaluation. Specifically, the value comes from self-evaluation of the parent state. This proceeds up to a max depth and search budget after which the algorithm linearly rolls out to complete the task. 

Their results show that tree search can significantly improve LLM-based web agents. 

They claim to be the first tree-search algorithm for web agents.

### Strengths
Originality: This paper proposes an original tree search algorithm for LLM based web agents. The paper also claims to be the first such algorithm.

Quality: The paper is of high quality. The results are pretty strong and clear. 

Clarity: The paper is generally clear and easy to follow. However, there could be some improvement here. 

Significance: There has been a trend of applying tree search and test time compute across many applications LLMs can be applied to. So it is not surprising to see a tree search algorithm for LLM web agents. However, in a first to the flag sense, it is significant. 

The results show that this is a meaningful route to improved performance and seems likely to inspire other works. It clearly clears the bar for publication significance. 

Value function approach seems smart: Multi-modal, Last d screenshots. Scores in 0, 0.5, 1 and averaging over multiple reasoning. This could be a source of a lot of noise but this seems to be a way of reducing that. The trade-off is more compute so the further balance is by only evaluating states when expanded, not when generated. 

“we generate 20 outputs from the model by prompting it with CoT reasoning (Wei et al., 2022), and aggregate the count of the action candidates. We use the top-b actions with the highest counts for branching.”  - This is a good way to generate distinct action candidates

### Weaknesses
WebArena results do not look strong relative to other modern works. However, some of those works seem to be a bit over-optimized for the benchmark, whereas this work is more general. 

There are some clarity issues to work out with the writing. 

The section on destructive actions, seems highly speculative. This is a major weakness of the approach in that in real world settings it is difficult to conduct search with lots of back tracking required. It is not even clear to me how backtracking could be conducted in these situations even excluding destructive actions. 

Another weakness of this method is that it involves more inference time compute. Furthermore, the algorithm may be especially slow, even among other search algorithms. The reason being is that, as per Algorithm 1, when you sample actions you execute all the actions (line 23 of Alg 1). This requires resetting the state $b$ times and rerunning the previous algorithms. This is a lot of time (though not necessarily compute) spent waiting to execute actions that may never actually end up being even searched over.

### Questions
1)
Algorithm 1 has “Backtrack and execute new actions to get to state s_p”
- How is this done in your implementation?

2)
Algorithm 1 has “””
for i ← 1 to b 
do: 
	Execute a_ip to get to state s_ip
”””
- How do you execute multiple actions from the same state in a web environment? This is similar to the above question. Essentially, how is backtracking done?

3)
Tab 2 shows GPT-4o gets 18.9% across the whole VWA benchmark. On the 200 question subset, the results without search are 24.5%. And with b=5, d=5 the results are 37% compared to 26.4% in table 2. This seems like a large discrepancy. Can this be attributed to the sampled questions? 

4)
Line 405: “(which is a sparse reward signal that returns either 0 or 1)”
- What about just showing the accuracy of the value function when the ground truth is available? I.e. Something like mean square error of the value function in cases when ground truth is available. 

5) 
How is tie-breaking done? Seems like it would make sense to break ties by depth and/or by the number of "votes" during generation. 

Suggestions:

Algorithm 1 should be in main section of paper. It is easier to be able to refer to it in the method section. 

“For example, a search budget of 10 indicates that at most 10 nodes will be expanded, after which the agent will commit to and execute the trajectory with the highest value” - This needs to be part of the algorithm. 
The reader needs a place to be able to refer to and understand how the algorithm works. They should not need to comb through ablation results to know how the method works. 

Line 404: “prompted zero-shot (with just the current observation)”
- Maybe note this is because LLaVa only accepts one screenshot

This is maybe nit-picky but wouldn't all the children of a state have the same value? In figure 1, (7) and (9) have different values. 

“Alloted” -> “allotted”

Line 483: backtrack -> backtracks

Figure 1 should be referred to in the text.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper addresses a critical limitation of language models (LMs) used in autonomous Web agents, particularly their difficulty in performing multi-step reasoning, planning, and utilizing environmental feedback in decision-making tasks. The authors propose an inference-time search algorithm that enhances the decision-making capabilities of LM agents by incorporating a best-first tree search method. To handle the challenge of lacking clear cut rewards in the diverse environments of Web, they propose a model-based value function to guide best-first search. The proposed approach allows the agents to effectively explore and evaluate multiple action paths within interactive web environments, thereby improving their performance.

### Strengths
1. The paper adeptly addresses several critical challenges faced by LLM agents in real-world web environments: the difficulty in obtaining clear rewards, the accumulation of errors, and the complexity of multimodal interactive web environments. The motivation for this research is both meaningful and reasonable.
2. The study introduces a tree search algorithm specifically tailored for LLM-based multi-step planning in web environments. This framework is both clear and straightforward.
3. The authors provide qualitative examples of agent trajectories in Section 5.3, which significantly aids in understanding the operational principles and effectiveness of the proposed method.
4. The paper is well-written, with clear and readable presentation of formulas, visualizations of figures and tables, and experimental results.

### Weaknesses
1. Lack of technical contribution. The integration of tree search techniques with LLM planning is not entirely novel, as there is existing research in this area, e.g., [1, 2, 3, 4]. Thus, the contribution of this paper in terms of technique novelty may need to be reconsidered, as it incrementally applies existing tree search-based LLM planning frameworks to the web agent domain.

[1] Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models (Released in 6 Oct 2023)

[2] When is Tree Search Useful for LLM Planning? It Depends on the Discriminator (Released in 16 Feb 2024)

[3] LLM Self-Training via Process Reward Guided Tree Search (Released in 6 Jun 2024)

[4] LiteSearch: Efficacious Tree Search for LLM (Released in 29 Jun 2024)


2. Lack a specially designed evaluation method for value function. The authors evaluate the impact of different value functions on the success rate of the entire framework in order to select a best value function, as mentioned between lines 401 and 412. However, assessing value functions based solely on the overall framework's outcome might be indirectly influenced by various potential factors. It would be beneficial for the authors to propose a dedicated evaluation method for value functions, essentially allowing for a more stable and accurate selection process.


3. The performance and credibility of the proposed framework seems limited, as observed in Table 2 (lines 324-341):
- The use of different baselines across two different datasets raises questions about the credibility of the experiments.
- On the WebArena benchmark, the authors only report the performance of two base LLMs augmented by their method, without the performance of the SOTA baselines augmented by their method, suggesting that the method may not universally integrate with diverse models or scenarios as claimed.
- Since the base LLMs already perform sub-optimally, the observed improvements after involving the proposed method are not surprising.
- The highest success rate achieved by the framework is 19.2% on the WebArena benchmark, which is considerably lower than multiple baselines, raising doubts about its efficacy.


4. Some mentioned future works should have been addressed in this paper:
- Integrating proposed search strategies into domain-specific SOTA baselines (mentioned as future work on lines 274 and 349).
- Experiments with larger search budgets (mentioned as future work on line 377).
- Mitigating the time cost of tree search-based LLM planning (mentioned as future work on line 502).

For instance, the study should report the performance of the domain-specific SOTA baselines augmented by the proposed method under the maximum step constraint setting used in the reported baselines, instead of just using the base LLMs and a small step constraint. Furthermore, addressing the time consumption of tree search for LLM planning is crucial for the feasibility of practical applications, making this an essential consideration.

Simply involving these crucial issues into future work may lead to skepticisms about the credibility and robustness of this study.

### Questions
Please refer to the 'Weaknesses' section.

### Soundness
2

### Presentation
3

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
This paper proposes a search-based approach to improve the performance of language model (LM) agents on realistic web automation tasks. Existing LM agents struggle with multi-step reasoning, planning, and using environmental feedback, which is crucial for success on open-ended web tasks. The authors introduce a best-first tree search algorithm that operates within the actual environment space and is complementary to existing state-of-the-art LM agents. The search procedure allows agents to explore a larger number of potentially promising trajectories at test time, reducing uncertainty through explicit exploration and multi-step planning. The authors evaluate their approach on the challenging VisualWebArena and WebArena benchmarks, demonstrating significant improvements over baseline LM agents and setting new state-of-the-art success rates.

### Strengths
1. The methodology presented in this paper is robust, as the application of tree search methods within a network environment proves to be an effective solution.
2. The structure of the paper is logically organized, beginning with an examination of existing issues and specifically addressing the challenge of implementing multi-step reasoning in network environments.
3. The authors propose a novel method, conduct rigorous testing, and perform comprehensive ablation studies.
4. The explanations are articulated clearly and are easily comprehensible; the combination of diagrams and text effectively illustrates the improvements achieved by the proposed method.
5. The experimental section is meticulously detailed, ensuring the reproducibility of the experiments, which enhances the credibility of the findings.

### Weaknesses
1. The authors' central concept is to apply tree search methods within a network environment to achieve enhanced performance. However, as tree search techniques are commonly used in other systems, this approach exhibits limited innovation. 
2. In Section 5.4, the authors acknowledge that this method may result in slow execution, a significant drawback often associated with tree search. Nevertheless, the paper does not present a comparison of execution times between this method and other approaches, nor does it provide an in-depth discussion of the temporal challenges involved. The discussion primarily revolves around the search budget c, yet c does not accurately reflect the time expenditure. Readers are more concerned with the issue of temporal efficiency rather than the selection of hyperparameters.

### Questions
1. In Figure 2, it can be observed that there is a noticeable improvement as the search budget c increases from 15 to 20. Have the authors attempted to experiment with a larger c? This might yield better results.
2. The parameter c is set as the maximum search budget. Have the authors tested the average number of searches conducted for both successful and unsuccessful cases? It might be beneficial to use a larger search budget during testing and observe how the training performance improves as c increases.

### Soundness
3

### Presentation
3

### Contribution
3
