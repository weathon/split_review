# ACC-Debate: An Actor-Critic Approach to Multi-Agent Debate

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Large language models (LLMs) have demonstrated a remarkable ability to serve as general-purpose tools for various language-based tasks. 
  Recent works have demonstrated that the efficacy of such models can be improved through iterative dialog between multiple models, frequently referred to as multi-agent debate (MAD).
  While debate shows promise as a means of improving model efficacy, most works in this area treat debate as an emergent behavior, rather than a learned behavior. 
  In doing so, current debate frameworks rely on collaborative behaviors to have been sufficiently trained into off-the-shelf models. 
  To address this limitation, we propose \ours, an \textbf{A}ctor-\textbf{C}riti\textbf{c} based learning framework to produce a two-agent team specialized in debate.
  We demonstrate that \ours~ outperforms SotA debate techniques on a wide array of benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Multi-Agent Debate (MAD) is an approach to improve the reasoning abilities of LLMs. Different from existing methods that treat debate as an emergent behavior, this paper proposes to treat debate as a learned behavior. It proposes an Actor-Critic based learning framework, which uses reward to find the positive and negative trajectories, and then uses the trajectories to DPO the training preference of the positive sample.

### Strengths
1. Authors propose a multi-agent debate method for training LLMs, rather than just utilizing the capabilities of LLMs.

2. The expression of reinforcement learning is clear.

3. The idea of guided-debate is simple but interesting and fits well in DPO training framework.

### Weaknesses
The goal of equation 1 is to optimize Actor and Critic by optimizing the two models separately rather than simultaneously, which may result in a failure to achieve the global optimum at the same time. Although it is also mentioned in the paper that PARTIAL TRAJECTORY REWARD solves the dependency relationship between rounds, more theoretical analysis on why equation 1 can achieve global optimum is needed.

### Questions
1. The evaluation of r is directly related to the judgment of positive and negative sample trajectories. So how does the reward function learn, and what is its architecture? Is it based on the LLM itself or some other structure?

2. What is your rationale for choosing their current set of benchmarks, and why datasets like GSM8K and MATH were not included?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ACC-Debate, a framework that trains two agents, an "actor" and a "critic", to collaboratively solve tasks through structured debate. The framework also incorporates a new off-policy data generation method called "guided debate," which effectively collects positive samples while reducing computational costs. Experimental results show that ACC-Debate outperforms existing debate methods on several benchmarks, indicating that targeted training enhances model collaboration.

### Strengths
This paper presents a practical framework for training a team of large language models (LLMs), offering a structured approach to enhance collaborative performance. The proposed method is straightforward and well-defined, making it easily applicable to multi-agent tasks.

### Weaknesses
The use of convergence to the correct answer as the reward function for data selection, along with incorporating the correct answer in the prompt for guided debate, may increase the likelihood of false positives (i.e., correct answers reached by flawed processes). This can result in diminished performance after multiple training rounds. The paper would benefit from a thorough analysis of this issue to understand its impact on the robustness of the trained agents. The paper should include an analysis of this issue to understand its impact on trained agents.

### Questions
1. Experimental settings are unclear, especially the implementation of Monte Carlo estimation for the reward function.
2. Figure 1 only shows natural debate as a negative sample, inconsistent with Algorithm 1.
3. Equation on Lines 189-190 lacks a reference number.
4. Typo on Line 234: "line improvement" should be "improvement."

### Soundness
2

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
3

### Summary
The paper proposes ACC-Debate, an Actor-Critic framework to improve multi-agent debate among LLMs. In traditional multi-agent debates, LLMs often show only emergent collaboration, meaning they aren't specifically trained to work together. The ACC-Debate approach, however, aims to jointly train a team of models (an actor and a critic) to improve reasoning and problem-solving through iterative dialogue.

### Strengths
- The paper introduces a new, joint training paradigm for LLMs focused specifically on collaborative problem-solving in debates, unlike previous approaches that rely on emergent collaboration.
- The introduction of the guided-debate data generation approach seems to produce higher-quality training samples, making the learning process more effective and efficient.
- ACC-Debate shows improvements over SoTA debate methods on various benchmarks (BoolQ, MMLU, BBH, SCIQ, ARC).

### Weaknesses
 - The training pipeline (Figure 1) is unclear. Either in the caption or the paper itself should explain what the green box means, and what the "+" and "-" refers to. Also, from the figure, it seems like ACC-Debate first uses the usual natural debate, then guided debate, followed with training the actor/critic LLMs and iteratively refine the process. I thought the ACC-Debate process only involves guided debate and then iteratively improve the training examples for better training results. Would appreciate some clarifications here.
- Equation 5 seems to be incorrect. Since the authors only observed at most 5 rounds of debate, where $t$ = 0, 1,... 4, why is the percent improvement $\frac{acc_5 - acc_0}{acc_0}$?
- Typo on the y-axis in Figure 2: improvment -> improvement
- What are some error cases of using this ACC-Debate framework, where ACC-Debate fails to improve performance, such as when the actor does not change its response despite the critic’s feedback or when the debate converges on an incorrect answer?
- The authors should conduct ablation studies to examine the effect of the number of debate rounds on final accuracy. This would help determine the optimal number of debate rounds needed for effective debate and identify potential diminishing returns on performance improvement.

### Questions
See above weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new method for training a 2-agent system (Actor & Critic) to better solve tasks collaboratively through debate. This training should provide an improvement over the use of off-the-shelf LLMs which have not been trained with this purpose in mind. 
The authors show how the training of this method works and evaluate it on well-known datasets.

### Strengths
1. Originality. The paper presents a new framework for improving the multi-agent debate (MAD). This is an interesting direction to generate LLMs that learn to collaborate better. 
2. Partial Trajectory Reward is an interesting method to provide reward over the rounds of debate. 
3. Robust experimentation and method presentation. The paper presents how the system works and is easy to understand how the training was made.

### Weaknesses
1. Minimal improvement. Given the confidence intervals, the improvements achieve after training are not very significant in most cases, when compare to other MAD methods. 
2. ACC Debate. The paper presents a method for multi-agent collaboration and mentions the use of Multi-Agent Debate. However, they focused on a the specific case of a Critic dialogue. Even, after reading section 5.3 it is not clear on the impact of using the critic. Unlike this method, the others it's compared with use traditional models of MAD. In my point of view, the kind of debate presented is an actor + critic/judge debate. Therefore, should it also be compared with some other critic system?
3. Generalizability. A note is made for scalability. However, there is no remark on the generalizability of the method. I assume the results are presented for the models trained on the same datasets. What happens when if the model is trained on all of them and later evaluated for each one of them.

### Questions
- How do you think that results can be further improved? Can further training or training with more data obtain better results?
- The accuracy improvement of traditional MAD is not very large. But it does provide better factuality. Have you considered using other metric other than accuracy?
- Due to the use of the ACC Debate, this is hardly scalable to be implemented with more agents in the debate, is there a way to do so?

### Soundness
4

### Presentation
2

### Contribution
3
