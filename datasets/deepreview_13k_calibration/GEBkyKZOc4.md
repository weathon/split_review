# Rational Decision-Making Agent with Learning Internal Utility Judgment

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Large language models~(LLMs) have demonstrated remarkable advancements and have attracted significant efforts to develop LLMs into agents capable of executing intricate multi-step decision-making tasks beyond traditional NLP applications.
Existing approaches to LLM-based decision-making predominantly build upon the manually-designed external performance metrics to guide the decision-making process.
However, reliance on the external performance metrics as prior is problematic in real-world scenarios, where such prior may be unavailable, flawed, or even erroneous.
For genuine autonomous decision making, it is imperative for the agent to develop its rationality from its posterior experiences to judge decisions independently.
Central to the development of rationality is the construction of an internalized utility judgment, capable of assigning numerical utilities to each decision.
This paper proposes \model (\underline{Ra}tional \underline{D}ecision-Making \underline{Agent}), which fosters the development of its rationality through an iterative framework involving \textit{Experience Exploration} and \textit{Utility Learning}.
Within this framework, \elo is devised to assign Elo scores to individual decision steps to judge their utilities via pairwise comparisons. 
Consequently, these Elo scores guide the decision-making process to derive optimal outcomes.
Experimental results on the ToolBench dataset demonstrate \model's superiority over baselines, achieving over 10\% improvement in Pass Rate on diverse tasks. 
It offers higher-quality solutions and reduces costs (ChatGPT API calls), highlighting its effectiveness and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies how to improve the performance of LLM-agents on sequential decision making tasks. It discussed the drawbacks of relying on pre-defined external metrics to guide the decision making of LLM-agents. Furthermore, they propose to use Elo score together with Experience Exploration techniques.

### Strengths
The proposal of using Elo score is reasonable and points out an interesting direction of rethinking how evaluation metrics can guide the decision making of LLM agents.

Meanwhile, the experiments are good and extensive.

### Weaknesses
1) the paper is rather empirical and heuristic, with combination of two heuristic techniques.
2) Elo itself also has significant issues [1]. For examples, it may provide no useful signals sometimes. In other words, such a black-box use of Elo without significant extensions/more detailed discussions on its potential limitations is a sign of limited novelty.

### Questions
See weakness

### Soundness
2

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
This paper introduces a novel approach named RaDAgent that addresses the limitation of LLM-based agents' dependence on external performance measures for decision-making. Unlike existing methods that rely on potentially unreliable or unavailable external metrics, RaDAgent develops internal rationality through an iterative framework combining Experience Exploration and Utility Learning. Besides, the framework incorporates the Elo Rating system to learn and assign utilities to decision steps through pairwise comparisons, enabling agents to make autonomous decisions based on learned internal judgment.

### Strengths
The main strength of this paper are:
1. The paper proposes a novel idea by shifting away from the conventional reliance on external performance measures to an internal utility judgment approach for LLM-based agents. 
2. The framework provides a practical solution for developing internal rationality in LLM-based agents.
3. The experimental results demonstrate promising performance across multiple datasets,

### Weaknesses
 The  main weakness of this paper are:
1. The Elo rating system might oversimplify the complexity of decision utilities. Besides, the pairwise comparison approach could be time-consuming for complex tasks.
2. The convergence for the Elo-based utility learning lacks theoretical analysis. While the paper demonstrates empirical effectiveness of the Elo rating system in learning decision utilities, it fails to provide rigorous theoretical guarantees about the convergence properties of this approach. An analysis of whether and how quickly the Elo scores converge to stable values would strengthen the theoretical foundation of the approach and provide better understanding of its reliability in different scenarios.

### Questions
Since the paper lacks convergence analysis of this approach, I wonder how much additional computational overhead this method requires compared to existing approaches. The time cost of conducting multiple comparisons and updating Elo scores, especially for complex decision scenarios, could be substantial and needs to be evaluated against baseline methods.

### Soundness
3

### Presentation
3

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
This work proposes RaDAgent (Rational Decision-Making Agent) that utilizes experience exploration and utility learning. Notably, Elo scores are assigned to each step to evaluate its utilities, which helps the agent to derive the optimal decisions. The authors provide empirical evidence that validates the efficacy of the proposed method on several tasks such as Game of 24, WebShop, and ToolBench. They also show that LLMs and the decision-making approaches are complementary, mutually enhancing each other to achieve superior performance outcomes.

### Strengths
Overall, the idea of this work is novel and intuitive.

Overall, this paper is well-written and well-presented.

The proposed RaDAgent method significantly outperforms the baseline methods across most of tasks.

### Weaknesses
I would recommend putting the Related Work section after the Introduction so that readers can gain more background information of this work. Indeed, explaining how the literature or baselines work can help the readers better understand the motivation of authors' idea.

The authors need to enhance the language and fix typos/grammar issues, e.g., in line 96-97, "take action", line 139 "Elo score" should be plural, etc.

Line 97-98, in general, one would use different functions to represent the policy and transition functions in MDP. I would expect a better introduction of MDP on page 2. For example, one can use a tuple (S, A, R, P, \mu) to represent an MDP. Please see more details in RL paper or Sutton's RL book. In addition, \pi is often used to denote the policy (action generator).

Even though mentioning in the Limitation section by authors, I am still interested in if RaDAgent can be implemented in other (at least one state-of-the-art) LLMs (e.g., Claude, Llama), especially not the GPT-series. Also, why the authors choose GPT-series as their backbone LLM? If RaDAgent does not work for other LLMs like Claude, what could be the possible reasons?

### Questions
Please refer to the "weakness" section.

### Soundness
2

### Presentation
3

### Contribution
3
