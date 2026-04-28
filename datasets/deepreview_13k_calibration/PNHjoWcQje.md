# StepTool: A Step-grained Reinforcement Learning Framework for Tool Learning in LLMs

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Despite having powerful reasoning and inference capabilities, Large Language Models (LLMs) still need external tools to acquire real-time information retrieval or domain-specific expertise to solve complex tasks, which is referred to as tool learning. Existing tool learning methods primarily rely on tuning with expert trajectories, focusing on token-sequence learning from a linguistic perspective. However, there are several challenges: 1) imitating static trajectories limits their ability to generalize to new tasks. 2) even expert trajectories can be suboptimal, and better solution paths may exist. In this work, we introduce StepTool, a novel step-grained reinforcement learning framework to improve tool learning in LLMs. It consists of two components: Step-grained Reward Shaping, which assigns rewards at each tool interaction based on tool invocation success and its contribution to the task, and Step-grained Optimization, which uses policy gradient methods to optimize the model in a multi-step manner. Experimental results demonstrate that StepTool significantly outperforms existing methods in multi-step, tool-based tasks, providing a robust solution for complex task environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces StepTool, a step-grained reinforcement learning framework designed to enhance tool learning algorithms through two key components: Reward Shaping and Step-grained Optimization. Experimental results on multi-step, tool-based tasks indicate that the proposed method outperforms existing approaches

### Strengths
1. The use of step-grained reinforcement learning (RL) in tool learning is novel, and the multi-step RL formulation is well-suited for this purpose.
2. The experimental setup is robust and demonstrates the effectiveness of the approach.

### Weaknesses
* The author should consider more benchmark algorithm for comparison to illustrate the proposed method.

* The authors should provide more implementations for the benchmark algorithm PPO for fair comparison.

### Questions
* What are the differences between PPO and StepTool in the experiment? Do they use different reward models or apply different KL penalties?

* Could the authors provide more details on the reward shaping used in tool learning?
Specifically:
   - Do we know the values of  r\_t\^{SC} and the *IsSolved()* function?
   - Are these values predefined, or does the reward function need to learn them?
   - What are the main challenges of reward shaping in the context of tool learning?

### Soundness
3

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
This paper proposes to apply (multi-step) RL for optimizing LLM tool use capabilities. To instantiate this, they design a step-level (aka process-level) reward consisting of terms that reward the correctness of the tool call, the relevance of the tool call to the successful completion, and the final success reward. Experimental results show small to medium improvements over non-RL baselines.

### Strengths
The paper is reasonably well-written and the application of RL to this setting is very natural. Similar applications of RL to other domains (e.g. coding) have shown good success, so it’s not unexpected that RL would work well here. The evaluation of the method is thorough, covering a range of relevant models and decoding strategies.

### Weaknesses
This paper is essentially a direct application of RL for LLM tool use, and has quite limited technical contributions or novelty beyond that - for example, as far as I can tell the method consists of a tool-use specific reward, and standard multi-step RL (see question 2). As such, the main contributions of this paper are conclusively demonstrating using empirical evidence that RL improves upon fine-tuning baselines. For this, I found the experimental results to be convincing enough, but relatively weak - for example, some metrics improve by only 1-2%, such as the tool invocation success rates in figure 4. The paper also lacks a thorough comparison to existing multi-step RL methods for language models, which is a significant oversight given the existing literature. The novelty is further diminished by the fact that the reward function is a straightforward combination of rule-based and LLM-based annotations, without any sophisticated design or optimization. The experimental results, while showing some improvement, do not demonstrate a substantial leap in performance, and the gains are not consistent across all metrics and tasks, raising questions about the robustness of the approach.

### Questions
1. How are rule-based and LLM-based reward annotation combined exactly? I couldn't find a statement of this in the text.
2. The “step-grained optimization” component of StepTool seems to just be the standard formulation of multi-turn RL (e.g. https://arxiv.org/abs/2402.19446).  Are there any differences? If not, it should not be stated in an independent subsection.
3.  Related to above: what is the difference between PPO and StepTool in the experiments? 
4. Appendix A/eq. 2 seems to be a standard result in RL and should be omitted (and just cited instead). 
5. What discount factor ($\gamma$) is used in the experiments?
6. Pass@k metrics would be useful to understand whether the model discovers new knowledge throughout RL training (i.e. exploration), or is simply re-weighting its prior (see https://arxiv.org/pdf/2403.04642). 
7. Does SFT on expert GPT-4 data followed by RL do better than RL alone?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the concept of step-grained reward shaping to enhance the reinforcement learning process. The proposed method focuses on the design of auxiliary rewards aimed at facilitating task completion. However, the reliance on these manually designed rewards raises questions about potential conflicts with the ground truth reward and issues related to reward hacking. A deeper discussion on these points is necessary, along with clarification on how contribution metrics

### Strengths
* The paper addresses an challenge for LLM tool using by proposing auxiliary rewards to guide the learning process, which could improve the efficiency of solving complex tasks for LLMs.

### Weaknesses
 * The reliance on auxiliary rewards introduces the risk of conflicts with the ground truth reward, which is a significant concern that the authors need to address more thoroughly. The potential for reward hacking must be discussed in detail.
* The paper lacks empirical analysis on the average number of tools called during task execution and how the complexity of tasks influences the length of action sequences. An exploration of whether long sequences stem from planning or task decomposition issues would enhance the understanding of the framework's practical applicability.

### Questions
1. Could the authors elaborate on how the auxiliary rewards might conflict with the ground truth reward and the implications of such conflicts?
2. How exactly are the contribution metric/reward trained? 
3. What is the average number of tools utilized per task, and how does this correlate with the difficulty of the tasks? If the step length is excessive, could this indicate deficiencies in planning or task decomposition?

Minor Comments:
* Line 176 contains an inaccuracy: “advantage which compares the expected return of a given action to the average return for that state.” The state value refers to the expected overall value of a state, not the average return.

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
The paper introduces StepTool, a step-grained RL framework to improve tool learning in LLMs. StepTool enhances LLMs' ability to handle multi-step tasks by step-level reward shaping and optimization. Step-level reward shaping focuses on both the success of tool invocations and their contributions to task completion. Step-grained optimization is proposed based on policy gradient  to optimize the model in a interactive manner.

### Strengths
In general, it is a feasible RL framework for enhancing LLM, while the key lies in the design of the reward function for tool learning.

### Weaknesses
1. What is the difference between StepTool and PPO besides reward shaping in the experiments?
2. There exists many works [1,2,3,4] leveraging RL methods for language-argumented sequential decision-making problem. And the tool learning is a subset of language-argumented sequential decision-making problem. Thus authors should compare more carefully with these works instead of saying "Due to the lack of publicly available implementation details for some concurrent works, we choose two classic optimization methods: supervised fine-tuning (SFT) and PPO" in lines 346-347.
3. If StepTool has no core difference from the above works at the algorithm level, reward shaping alone does not seem to be enough to support an ICLR accepted article.

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
