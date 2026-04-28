# Martryoshka: Learning to Drive Black-Box LLMs with LLMs

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Despite the impressive generative abilities of black-box large language models (LLMs), their inherent opacity hinders further advancements in capabilities such as reasoning, planning, and personalization.  Existing works aim to enhance LLM capabilities via domain-specific adaptation or in-context learning, which require additional training on accessible model parameters, an infeasible option for black-box LLMs.  To address this challenge, we introduce Martryoshika, a lightweight white-box LLM controller that guides a large-scale black-box LLM generator by decomposing complex tasks into a series of intermediate outputs. Specifically, we consider the black-box LLM as an environment, with Martryoshika serving as a policy to provide intermediate guidance through prompts for driving the black-box LLM.  Martryoshika is trained to pivot the outputs of the black-box LLM aligning with preferences during iterative interaction, which enables controllable multi-turn generation and self-improvement in optimizing intermediate guidance. Empirical evaluations on three diverse tasks demonstrate that Martryoshika effectively enhances the capabilities of black-box LLMs in complex, long-horizon tasks, including reasoning, planning, and personalization. By leveraging this pioneering controller-generator framework to mitigate dependence on model parameters, Martryoshika provides a transparent and practical solution for improving black-box LLMs through controllable multi-turn generation using white-box LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an approach to enhance the capabilities of black-box Large Language Models (LLMs) by employing a lightweight white-box LLM as a controller. The proposed framework, Martryoshka, addresses the opacity of black-box LLMs by decomposing complex tasks into a series of intermediate outputs, which are used to guide the black-box LLM through iterative interactions. This controller-generator framework allows for controllable multi-turn generation and self-improvement in optimizing intermediate guidance, leading to improved performance in reasoning, planning, and personalization tasks.

### Strengths
The method proposed in this paper is successfully applied in a white-box + black box framework, and  shows its  effectiveness in reasoning, planning, and personalization tasks compared with black-box LLMs.

### Weaknesses
1. The key idea of Martryoshka is to train a white-box LLM to generate CoT or planning steps, then combine them with the original prompt and send them to black-box LLMs. The  methodology used to train white-box LLMs is a SFT phase combined with a DPO phase, which is a common and  trivial way for enhence domain specific  abilities (like math, coding, instruction following etc.) of certain LLMs. The method used in Martryoshka for training white-box LLMs simply changes the enheced abilities to 'CoT generation' or 'planing generation'. There is concern about the novelty of this methodology.
2. The proposed idea of control black-box LLMs with white-box is not convincing in practical. A potential  problem is if we already have SFT data and pair data for RLHF of a certain task, why don't we simply  train a domain-specify model by using 'while-box' LLMs? In many benchmarks, 'while-box' LLMs are already superior than black-box LLMs like GPT-4o in specific domains. For example, Llama3.1  series outperform GPT-4o in 10/13 benchmarks, including the GSM8K which is tested in this paper.

### Questions
I  suggest the author discuss the following questions：
1. What specific advantages does your white-box + black-box framework offer over fine-tuning a white-box model?
2. Are there scenarios where your approach would be preferable to domain-specific fine-tuning of white-box models?
3. How does your method compare to fine-tuned white-box models on the same tasks?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Black-box LLMs, like GPT-4, are powerful tools that have shown promise in a wide range of tasks. However, it is difficult to control these models. Prior works have used in-context prompting to achieve this. In contrast, this paper trains a lightweight LLM, called Martryoshka, that controls the larger black box LLM to generate output that matches certain preferences. They provide an algorithm for training this lightweight LLM controller, and show the applicability of their algorithm in a wide range of tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to follow.
3. Tested on mathematical reasoning, planning and personalization — 3 sufficiently different benchmarks, showing broad applicability of the paper’s methods.

### Weaknesses
 **(Major concerns)**

Major concerns I have about this paper are:

1. The appendices seem to imply the method is much more complicated in practice to implement, than the main paper suggests. In fact, there are many key implementation steps without which the method probably doesn’t work. I would mention one:

> In cases where no positive generation exists for some data points, we utilize a more powerful model, such as gpt-4o, to produce several strong intermediate generations, thereby increasing the likelihood of obtaining positive samples.

The paper does not mention (or I could not find) what fraction of data is generated by gpt-4o/why is this needed at all. If data is generated by gpt-4o, then the paper’s method becomes distillation and not self-improvement, which is very different from what I first understood the paper to be.


2. The examples provided in the appendix raised more questions.

E.g., in page 26, for GSM-HARD, the following is the decomposition by Martryoshka:

Let’s break down this problem: 

> 1. How much does the lemon tree cost to plant? 2. How much money will Carlos earn from selling lemons each year? 3. How much money will Carlos spend on watering and feeding the tree each year? 4. How many years will it take for Carlos to start earning money on the lemon tree?

The same done by the vanilla model is:

> Let’s break down this problem: 1. How much does the lemon tree cost to plant? 2. How much money will Carlos earn from selling lemons each year? 3. How much will it cost Carlos to water and feed the tree each year? 4. How many years will it take before Carlos starts earning money on the lemon tree?

The only difference between these two seems to be in slight differences in wording in question 3. Do the authors have any intuition on why such slight differences result in correct vs incorrect answers?


3. What is the data generation/API and training cost for these models?

4. Finally, does this method generalize? Eg given a Martryoshka model that has been trained to generate guidance on one task, generalize to an unseen task? If not, then every downstream user needs to train their own Martryoshka model every time they face a new task, which can be a weakness of this paper.

**(Minor concerns)**

>  Martryoshka adopts on-policy learning to iteratively enhance training data quality, inherently self-improving intermediate guidance for the continual enhancement of black-box LLM capabilities.

The paper mentions collecting on-policy data to improve training data quality. Citations for prior work that focuses on this issue is important. For example, [1] talks about online DPO being superior to the offline variant, [2] talks about the general importance of on-policy data for LLM alignment, [3] talks about the importance of online data from a theoretical perspective. Adding discussions on these, plus other relevant work would be important.

Also an interesting direction to think about for the authors is [5]. The authors are not training/updating the weights of the environment, but the idea of training an attacker or in this case controller policy, to drive the environment into behaving a certain way, has been studied in red-teaming/jail breaking literature and should be cited/credited as such. Similar ideas also appear in [6], though they do not train the controller policy as far as I understand.

### Questions
**(Question 1: choice of method)**
Any particular reason the authors employ iterative DPO, instead of directly using an online RL method like REINFORCE/PPO?

**(Question 2: Understanding multi-turn interaction in the paper)**

I do not understand the purpose of multi-turn interactions. Could the authors give an example trajectory obtained from the multi-turn interaction? I imagine the steps are:

1. the controller breaks the task into subgoals 
2. sends it to the black-box LLM 
3. obtains a response from the black box LLM, measure task success
4. The controller receives task success as the observation, and generates another break down of the task into subgoals?

Did I understand it correctly? If so, why is the controller policy only trains using single turn interactions in equation 9 and iterative guidance optimization? If I understand it correctly, the authors only train the model on positive guidance vs negative guidance, in a single turn setting, using DPO. This improves the controller at generating guidance at a single turn, but one can do more: if one uses the entire trajectory, define trajectory level reward, and use the multi-turn DPO formulation from Agent-Q [4], one can ideally create a controller policy that can keep improving the model’s generation using a multi-turn interaction system at test time, instead of just single step guidance generation. I am confused: could the authors clarify whether they indeed use a multi-turn DPO/multi-turn interaction at inference time (all the examples I saw on the appendix are of single turn interactions), or the multi-turn interaction is only used to generate more data? In that case, I do not see the purpose of using multi-turn interactions, once could attain as much data by just generating the single turn interaction more times.


# References

[1] Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study, https://arxiv.org/abs/2404.10719

[2] Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data, https://arxiv.org/abs/2404.14367

[3] The Importance of Online Data: Understanding Preference Fine-tuning via Coverage, https://arxiv.org/abs/2406.01462

[4] Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents, https://arxiv.org/abs/2408.07199

[5] Red Teaming Game: A Game-Theoretic Framework for Red Teaming Language Models, https://arxiv.org/html/2310.00322v3

[6] Automated Black-box Prompt Engineering for Personalized Text-to-Image Generation, https://arxiv.org/abs/2403.19103

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper fine-tunes a white-box model, like Llama, to generate improved prompts—such as question analysis—for black-box models like GPT. The approach combines supervised behavior cloning and iterative guidance optimization, achieving better performance than using the original white-box and black-box models directly.

### Strengths
1. The writing is clear and straightforward.
2. They address various tasks, including personalization, math, and planning, and design specific workflows for each.

### Weaknesses
I'm confused about the necessity of using a white-box model as a controller. This setup follows a standard agent workflow: the first agent performs analysis and decomposes the task into steps, while the second agent generates the final answer. This is a common approach in agent research, offering no much novelty. Here, they replace the first agent with a white-box model (Llama) and apply SFT and RL to improve it. However, during SFT, they use GPT-4 or GPT-3.5 to generate training data for Llama, so a more appropriate baseline comparison would be GPT-4 + GPT-4 rather than Llama + GPT-4. I also question if Llama-SFT-IGO + GPT-4 actually outperforms GPT-4 + GPT-4, especially since current results show only marginal improvement of Llama-SFT-IGO + GPT-4 over Llama + GPT-4.

### Questions
What's the result of directly using two black-box models directly, rather than first distilling the black-box models onto white-box models and then applying RL?

### Soundness
3

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
This paper presents a novel multi-turn framework where a white-box LLM (e.g., Llama) generates prompts, and a black-box LLM (e.g., GPT-4) responds to each prompt in turn. It proposes a DPO-based algorithm to train such white-box LLM. It demonstrates superior performance in various personalization, reasoning, and planning tasks.

### Strengths
- The paper is well-written and easy to follow. Specifically, Figure 1 alone clearly illustrates the paper’s goal.
- The paper evaluates the proposed method across three different tasks, demonstrating its broad applicability.
- The plug-and-play experiment is impressive, showing that training a white-box LLM specifically for a particular black-box LLM is unnecessary, thereby demonstrating its generalizability.

### Weaknesses
 - The proposed method definitely echoes black-box prompt optimization, as mentioned by the author in the related work section. The only difference is single-turn versus multi-turn interaction. Also, there is some recent work on black-box prompt optimization for non-classification tasks [1].
- I believe that the naive DPO is not suitable for multi-turn MDPs when the transition dynamics are non-deterministic [2]. The authors should justify why they use DPO instead of REINFORCE or PPO.
- The proposed method uses more capable LLMs (e.g., GPT-4) for training, which makes the comparison unfair. The authors should provide results for the proposed method using the same LLM as the baseline models.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
