# Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Large Language Model (LLM) based multi-agent systems (MAS) show remarkable potential in collaborative problem-solving, yet they still face critical challenges: low communication efficiency, poor scalability, and a lack of effective parameter-updating optimization methods. We present \textbf{\optima}, a novel framework that addresses these issues by significantly enhancing \textit{both} communication efficiency and task effectiveness in LLM-based MAS through LLM training. \optima employs an \textit{iterative generate, rank, select, and train} paradigm with a reward function balancing task performance, token efficiency, and communication readability. We explore various RL algorithms, including Supervised Fine-Tuning, Direct Preference Optimization, and their hybrid approaches, providing insights into their effectiveness-efficiency trade-offs. We integrate Monte Carlo Tree Search-inspired techniques for DPO data generation, treating conversation turns as tree nodes to explore diverse interaction paths. Evaluated on common multi-agent tasks, including information-asymmetric question answering and complex reasoning, \optima shows consistent and substantial improvements over single-agent baselines and vanilla MAS based on Llama 3 8B, achieving up to \textit{2.8x performance gain with less than 10\% tokens} on tasks requiring heavy information exchange. Moreover, \optima's efficiency gains open new possibilities for leveraging inference-compute more effectively, leading to improved inference-time scaling laws. By addressing fundamental challenges in LLM-based MAS, \optima shows the potential towards scalable, efficient, and effective MAS\footnote{\url{https://chenweize1998.io/optima-project-page}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a collaborative training method for systems of LLMs, Optima. Optima features a carefully crafted reward function that incentivizes the communications readibility, task performance, and token efficiency. Additionally, a variant of Optima employs MCTS to sample diverse trajectories. Trajectories are then trained on using SFT or DPO. The authors evaluate their algorithm on diverse complex reasoning and information-asymmetric question answering tasks and observe performance improvements in both tasks performance and token efficiency.

### Strengths
The authors tackle an extremely timely problem with significant community interest - how to optimise LLM agents for collaborative tasks.
There are several algorithmic innovations, and the empirical evaluation is extensive.
The observed improvements are significant.
Last but not least, there is a very extensive treatment of related work.

### Weaknesses
 * lack of theoretical examination of why the reward function used is working 
* lack of evaluation of models other than llama 8bn (other/smaller models would have been interesting to see).

### Questions
* what about systemic biases/safety misalignment arising from training?
* can we extend this to systems of more than 2 agents, and how does this scale?
* could you provide assurance that results are not from training on test data (lacks details)

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a framework that improve the effectiveness and efficiency of LLMs in multi-agent dialogue systems by iteratively optimizing data and training LLMs using SFT/DPO. For iSFT, it use sampling to generate better data; for iDPO, it use MCTS to generate paired data. Additionally, a carefully designed reward function ensures the system's overall effectiveness and efficiency in task performance.

### Strengths
The paper is well-structured and easy to understand, addressing an important problem with a clearly articulated methodology. The data generation mechanism for MAS is interesting and may facilitate further improvements in MAS, including frameworks like AutoGen.

### Weaknesses
1.	While this paper offers a well-structured approach to enhancing the effectiveness and efficiency of MAS, iSFT and iDPO have been extensively explored in prior works. Thus, the main contributions here—reward function design and data improvement mechanism in MAS—offer limited novelty within the existing research landscape.

2.	A thorough and fair experimental comparison is very important if the novelty is limited. Another key weakness of this paper is unfair comparison. As this framework has trained LLM to maximize a delicate reward, it’s slightly unfair to compare with prompt-tuning method like CoT, SC, etc.

3.	This paper focuses on LLM-based MAS, but the definition of the problem and the specific methods do not adequately reflect the multi-agent aspect. It appears that the multi-agent scenario is only evaluated in the experiments. The methods are relatively general and do not address the key issues in MAS.

Other trivial weakness in this paper:

1.	Fact error in abstract: iSFT and iDPO with reward filters can be considered as RL, but SFT and DPO are not RL.

2.	The language modeling loss in equation 1 is not defined.

### Questions
1.	Figure 3(a) need further elaboration. How does Optima influence MAS’s inference scaling law comparing to baseline?
2.	I would appreciate further discussion on the advantage of optimizing the effectiveness and efficiency of a MAS versus optimizing these aspects of a single LLM using similar reward functions.
3.	Would improvements in effectiveness and efficiency facilitate the design of communication topologies within MAS?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates inter-agent communication and task inference effectiveness within LLM-based MAS. It introduces a framework based on an iterative generate, rank, select, and train paradigm to address these challenges. The core of this framework is iteration, and build iSFT and iDPO based on the iteration paradigm. The iSFT leverages prompt formats to create a diverse dataset. Subsequently, it removes these formats and fine-tunes the model based on the generated trajectories. The iDPO employs Monte Carlo Tree Search (MCTS) to generate diverse data through multi-agent conversations (MAD), alternating between MCTS-based data generation and model updates using DPO.
The authors evaluate this framework across several benchmarks using Llama 3 8B as the baseline model. They achieve promising results compared to Chain-of-Thought (CoT), SC (n=8), MAD, and AutoForm.

### Strengths
The method is written with significant detail, which is easy to follow.

Introducing an effective and efficient LLM-based frameework, which can be treated as a foundational model, seems important and interesting.

Experiments are provided for various environments and demonstrate promising results.

### Weaknesses
1. Unfair Comparison: The methods in OPTIMA do show less token consumption and higher accuracy compared to other approaches. However, the comparisons between iSFT, iDPO, or iSFT-DPO and other methods may be unfair. The authors did not clarify whether OPTIMA’s training is conducted online or offline (I assume it is offline). If it is online, the token consumption should not be lower than CoT (since MCTS requires searching across 24 trajectories). If it is offline, then the token consumption comparison is unfair, as the OPTIMA methods fine-tune the model on diverse prompts or multiple sampled data, which would have already consumed a significant amount of tokens during the post-training phase. The paper, however, only compares token consumption during the inference process. This is problematic because the reported token savings during inference may be offset by the substantial token costs incurred during the fine-tuning stages of iSFT and iDPO. A fair comparison would necessitate accounting for the total token consumption, including both training and inference, to provide a holistic view of efficiency. Furthermore, the comparison is skewed because the baselines are primarily prompt-based methods, which do not involve any fine-tuning. To ensure a fair evaluation, the baselines should also be fine-tuned, or at least compared against fine-tuned versions, to provide a more balanced assessment of the proposed methods.

2. Lack of Novelty: The methods iSFT and iDPO seem to lack innovation. iDPO merely combines MCTS from ToT with DPO, while iSFT simply adds a step of supervised fine-tuning (SFT) after removing the prompt. These methods seem incremental rather than novel, similar approaches can already be found, such as [1], [2], [3], [4], [5]. The core idea of iterative refinement through a generate, rank, select, and train loop is not new, and the specific implementations of iSFT and iDPO do not introduce significant novelties. The application of these techniques to multi-agent systems, while potentially useful, does not fundamentally alter the underlying methodology.

3. Reward Function: The authors mention the reward function multiple times, but it is only briefly defined in line 146. Meanwhile, in line 79, the reward is described as the core element of OPTIMA’s success. This undermines the credibility of the proposed method since the reward function is not thoroughly explained or explored. The lack of detail makes it difficult to understand how the reward function is constructed and whether it is truly effective in guiding the training process. A more comprehensive explanation, including the specific mathematical formulation and the rationale behind each component, is needed to validate the claims made about its importance.

4. Scalability: The authors frequently mention the scalability of OPTIMA, which seems exaggerated. There is no detailed discussion of the framework's ability to scale up in the experiments. Additionally, the token consumption during fine-tuning with iSFT and iDPO would increase significantly as the number of agents grows, which could limit the scalability of the framework. The paper does not provide any concrete evidence to support the claim that OPTIMA can scale effectively to larger multi-agent systems. The potential increase in computational costs during fine-tuning, especially with more agents, raises concerns about the practical scalability of the proposed approach.

### Questions
As the weakness mentioned.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces OPTIMA, a novel framework designed to optimize Large Language Model (LLM)-based multi-agent systems (MAS), which shows the potential towards scalable, efficient, and effective LLM-based MAS.. The key focus is on enhancing communication efficiency and task effectiveness through an iterative generate, rank, select, and train paradigm. OPTIMA utilizes a hybrid of reinforcement learning (RL) techniques, including Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO), along with Monte Carlo Tree Search (MCTS)-inspired data generation. The framework is evaluated on two multi-agent settings: (a) information exchange, including information-asymmetric question answering and  (b) debate, encompassing mathematical and reasoning tasks. OPTIMA’s efficiency gains open new possibilities for leveraging inference-compute more effectively, potentially leading to improved inference-time scaling laws.

### Strengths
1, Clarity: The paper is well written and have full proof for their argument, the concepts in this paper are easy to follow and understand.
2, Quality: The performance of their designed pipeline is impressive and outperform the baseline a lot.
3, Originality: The paper introduced a new way to enable the development of MAS that are not only effective and efficient but also maintain interpretable communication patterns, which solves the core issues of communication efficiency and collective optimization.

### Weaknesses
1, The method is only evaluated on two tasks: (a) information exchange, including information-asymmetric question answering and  (b) debate, encompassing mathematical and reasoning tasks.  Although the performance of proposed method is great on those two tasks, but not sure how this method will perform on the other more complex tasks such as: StarCraft II, Hanabi and so on. (those two environment are broadly used in reinforcement learning tasks and there are also works of using LLM to play those two games)

2, The scalability of this method. The number of agents in showed tasks are limited,. And because the proposed method are aimed to solve the problem of multi-agent tasks, using more agents in environment(maybe at least 4 or 5 agents?) will be more convincible.

3, They use Llama 3 8B as their base model across all benchmarks. However, can this method still have significant improvement compared to baseline if using other base models still remains as a question and need further proof.

### Questions
The method proposed in this paper is great, but still I have following concerns which may need further experiments:
1, More tasks study will make this proposed method more convincible, including using more complex tasks and more agents in a task. (StarCraft II, Hanabi and any other tasks which are broadly used in using LLM in MAS problems)

2, Try at least one more base model on all the tasks such as Llama 3.2 or Llama 3 70B

### Soundness
3

### Presentation
3

### Contribution
3
