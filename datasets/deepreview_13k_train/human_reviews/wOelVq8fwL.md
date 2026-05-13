# Adapting LLM Agents Through Communication

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Recent advancements in large language models (LLMs) have shown potential for human-like agents. To help these agents adapt to new tasks without extensive human supervision, we propose the Learning through Communication (LTC) paradigm, a novel training approach enabling LLM agents to improve continuously through interactions with their environments and other agents. Through iterative exploration and PPO training, LTC empowers the agent to assimilate short-term experiences into long-term memory. To optimize agent interactions for task-specific learning, we introduce three structured communication patterns: Monologue, Dialogue, and Analogue—tailored for common tasks such as decision-making, knowledge-intensive reasoning, and numerical reasoning. We evaluated LTC on three datasets: ALFWorld (decision-making), HotpotQA (knowledge-intensive reasoning), and GSM8k (numerical reasoning). On ALFWorld, it exceeds the instruction tuning baseline by 12% in success rate. On HotpotQA, LTC surpasses the instruction-tuned LLaMA-7B agent by 5.1% in EM score, and it outperforms the instruction-tuned 9x larger PaLM-62B agent by 0.6%. On GSM8k, LTC outperforms the CoT-Tuning baseline by 3.6% in accuracy. The results showcase the versatility and efficiency of the LTC approach across diverse domains. We will open-source our code to promote further development of the community.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method that uses LLM based agents to solve tasks that require reasoning and sequential decision making. Authors propose a paradigm for learning through communication where communication can be 1.) monologue - self communication, 2.) dialogue - multi-agent communication or 3.) analogue - communicating with a teacher agent. Authors provide results on three environments  1.) ALFworld - sequential decision making environment that require performing household tasks, 2.) GSM8K - grade school math problem solving and 3.) HotPotQA - reasoning and language understanding.

### Strengths
- The paper is well written and easy to read.
- The paper provides a  comprehensive summary of related work and the contributions of the paper are well placed in the relevant literature
- Environments considered in the paper are diverse and capture essential features of reasoning and sequential decision making

### Weaknesses
 - Multi-agent interactions highlighted in the paper are not properly formulated and motivated.
- Authors are not considering any environments that require multi-agent interactions. This reviewer is not convinced that the paper adds value in terms of communication between multiple agents that would lead to better performance.
- Authors have not provided the code and hence the results are not reproducible.

### Questions
- According to the provided discussion the only difference between dialogue and analogue is in analogue, teacher roles can directly provide reward signals and new examples. What is the significance of this distinction?
- How does this approach extend to multi-agent environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new training paradigm called Learning through Communication (LTC), which enables large language model (LLM) agents to adapt to new tasks through interaction. The major contributions include the LTC method itself, the introduction of task-specific communication patterns (Monologue, Dialogue, Analogue), and empirical evidence that LTC outperforms instruction-tuning baselines on decision-making, knowledge-intensive reasoning, and numerical reasoning tasks. The paper demonstrates LTC's effectiveness and efficiency, with significant gains in success rates and accuracy, along with reduced token usage during inference.

### Strengths
Novelty of the Learning Method: The proposed Learning through Communication (LTC) framework is a commendable advancement. It is an inventive approach that enables language models to dynamically adapt to new tasks through iterative interactions. The methodology is well-conceived, blending language modeling with reinforcement learning objectives in a manner that is both theoretically sound and practically viable.

Comprehensive Evaluation: The authors have conducted a rigorous empirical evaluation of the LTC framework across a variety of tasks and datasets. The breadth of the evaluation—spanning decision-making, knowledge-intensive reasoning, and numerical reasoning—is impressive. This comprehensive testing not only demonstrates the applicability of LTC to a wide range of tasks but also provides a convincing argument for its efficacy compared to existing baselines.

### Weaknesses
Model Comparisons: The LTC method's performance is compared to that of models with and without tuning. However, the paper states that the combined method of ReAct and CoT-SC surpasses LTC by 1.9%. This suggests that while LTC has strengths, there may be specific configurations of existing methods that outperform it, which could be a point of concern regarding the robustness and superiority of LTC.

Scope of Evaluation: While LTC is shown to perform well across three tasks, the evaluation might still be limited in scope. The paper hints at future work to explore more diverse communication patterns and involve communication with humans. This suggests that the current evaluation may not fully capture the LTC's performance in more varied or complex interactive settings such as ScienceWorld, and Mind2Web.

Generalization to Human Interaction: The paper outlines future work to involve communication with humans during the learning process, which is not covered in the current evaluation. This omission indicates that the paper does not address the challenge of human-agent interaction, which is critical for practical applications of LLM agents

### Questions
1. The LTC method relies heavily on predefined communication patterns. Have the authors considered how LTC might generalize to tasks that require more flexible or less structured forms of communication?

2. Given that certain combined methods like ReAct and CoT-SC have outperformed LTC, what are the authors' perspectives on the limitations of LTC in its current form? Are there specific enhancements they are considering to improve upon these existing methods?

3. The paper suggests future work will involve human communication. Can the authors provide preliminary insights into how they expect human-in-the-loop interactions to affect the learning process and the adaptability of the LTC method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for adapting LLMs to target domains via RL in domain-specific environments, through distillation from oracle feedback (linguistic and scalar rewards). Evaluation is performed on three NLP tasks (grounded instruction following, multi-hop question answering, and math story reasoning). Results show that the proposed method, which affords exploration during learning with oracle feedback, improves over methods that finetune models only with static domain-specific training data.

### Strengths
The paper explores several different tasks and compares against existing methods. It shows relatively strong results showing that exploration and language-like feedback can improve LLMs on domain specific tasks.

### Weaknesses
Concern about experimental setup:
* The ablation in Fig 5 doesn't seem to disentangle the contributions of exploration and "communication". In particular, performing exploration and receiving non-linguistic feedback (e.g., in the environment) doesn't seem to be evaluated. And on the other hand, training with static instruction-tuning data augmented with "communication" traces sampled using the same method as LTC (without sampling agent actions, but using the static demonstrations instead) is not evaluated.

Writing feedback: I found the paper was relatively confusing in the terminology used.
* I would suggest renaming the approach away from "through communication". This phrase is very vague, and there really isn't any true communication happening here at all: the learning setting is to just prompt the model(s) to replicate what a dialogue might look like in the domain. It is much more reminiscent of work on distillation and learning from oracles, like DAgger (as briefly mentioned in a footnote on page 7).
* Framing this as continual learning also seems wrong. Fine-tuning with LTC is performed on some held-out set of examples from these datasets' training sets, right? So how is this continual?
* Some of the language around LLMs is too anthropomorphizing. E.g., "human-like" LLM agents, "the agent's brain".
* Minor nitpick, but the whole learning setup is RL, not just the training phase, as the exploration part of the proposed approach is certainly part of a general RL framework.
* There seems to be a bug in Fig 7 with the "question".

One recurring issue with the clarity is that some terminology used is either overly ambiguous, or overly specific. For example:
* "generate trajectories in a self-talk style"
* references to "masks" in the introduction
* "decision-making" as ALFWorld's task -- more precisely, the task is grounded instruction following
* References to a value and a log-prob list in Section 3.1; this is underspecified and seems somewhat irrelevant without having introduced PPO in depth
* "Analogue" as the third communication pattern -- why does it have this name?
* "action tokens" in 4.2
* In the experimental section this is particularly confusing. As a general point, some existing methods are introduced and compared against without intuition on why the experiment is performed (unless the reader is very familiar with the existing approaches). E.g., what data are ReAct-Tuning and CoT-Tuning trained on? There's a self-reference to Section 4.2.

Distinguishing from some existing work would be useful. In particular, work on continual learning for language tasks such as:
* Gao et al. 2022 ("Simulating Bandit Learning from User Feedback for Extractive Question Answering"), and 2023 ("Continually Improving Extractive QA via Human Feedback")
* Kojima et al. 2021 ("Continual Learning for Grounded Instruction Generation by Observing Human Following Behavior")
* More recent work on RLAIF (e.g., Lee et al. 2023, or self-instruct, Yang et al. 2023)

### Questions
* The points on the righthand side of Figure 1 seem somewhat arbitrary. ICL is less efficient at inference time, but LTC requires a lot more compute for finetuning.
* How are rewards derived? Is this different in each environment?
* Did you evaluate the quality of the teacher agents? How often are they making mistakes?
* Why not perform a 3x3 experiment combining the three datasets and the three "communication" patterns?
* What are the actual steps for training? It seems the model starts as LLaMA-7B, then is instruction-tuned on a domain-general dataset, then instruction fine-tuned with data sampled from GPT-3/4, and _then_ LTC is applied? 
* What is the stopping condition for LTC training? Just when the training data has ran out?
* Why are the results in Table 1 very low precision?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new way of adapting LLMs to new tasks through learning from communication. The authors introduce three communication patterns: Monologue with the LLM interact with the environment and learn from the system provided reward; Dialogue with two LLMs play different roles and the student LLM learn from the teacher's actions; and Analogue with a teacher model provide feedback and reward for student agent's actions. With the different communication patterns, the authors propose to tune the model with both language modeling loss and PPO. Experimental results on three different benchmarks demonstrate the effectiveness of LTC, with additional discussion and ablation validate the design choices.

### Strengths
1. The paper introduces a new paradigm of adapting LLMs to downstream tasks that is different from instruction tuning and or prompting. The authors designs three communication patterns considering interaction with the environment and use of multiple LLM agents. While RL with environment and learn from stronger teacher LLMs are things that have been explored in previous works. The paper summarizes these into the three categories, and has additional design to better orchestrate the different components.
2. Experimental results on three different benchmark datasets shows that the proposed learning from communication method can achieve better performance than direct instruction tuning.

### Weaknesses
1. The authors proposes three different communication patterns which is nice, however, the experiments only study one pattern for each task. This makes it unclear on what are the pros and cons comparing these three communication patterns, whether each of them could generalize across different tasks and how to choose the right communication pattern. I feel it would be great to have more thorough comparison among the three patterns, and just with the baseline instruction tuning and prompting.
2. The experiment is only done with the 7B model. It is not clear whether the method could apply to smaller models, and more importantly whether it could scale up and how much improvement it could bring to models of larger size.

### Questions
1. Have you tried the three patterns across tasks, or they are only tested on the specific task?
2. How many instruction data by GPT 3/4 (as mentioned in section 4.2) are used?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
