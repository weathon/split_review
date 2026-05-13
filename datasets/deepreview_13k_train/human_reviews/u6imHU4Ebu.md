# Large Language Models as Generalizable Policies for Embodied Tasks

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
We show that large language models (LLMs) can be adapted to be generalizable policies for embodied visual tasks. Our approach, called Large LAnguage model Reinforcement Learning Policy (LLaRP), adapts a pre-trained frozen LLM to take as input text instructions and visual egocentric observations and output actions directly in the environment. Using reinforcement learning, we train LLaRP to see and act solely through environmental interactions. We show that \rllm is robust to complex paraphrasings of task instructions and can generalize to new tasks that require novel optimal behavior. 
  In particular, on $1,000$ unseen tasks it achieves $42\%$ success rate, $1.7$x the success rate of other common learned baselines or zero-shot applications of LLMs. Finally, to aid the community in studying language conditioned, massively multi-task, embodied AI problems we release a novel benchmark, \task, consisting of $150,000$ training and $1,000$ testing tasks for language-conditioned rearrangement. 
  Video examples of \rllm in \task and the code are at \href{https://llm-rl.io}{https://llm-rl.io}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Large Language model Reinforcement Learning Policy, which adapts a pre-trained LLM to take text instruction and egocentric observations as inputs, and output actions. Fixing the body of LLM, adapters are trained using the standard reinforcement learning algorithm. The paper is also provided a new benchmark called language rearrangement, consisting of 150,000 training sets. They empirically show the benefits of the proposed method, comparing with several simple baselines including zero-shot LLM, zero-shot VLM, and LSTM policy in conjunction with T5 and LLaMA.

### Strengths
(1) The paper is well written and easy to follow. 

(2) The method is simple and straightforward extension of prior studies but seems to provide solid performance gain.

### Weaknesses
(1) Technical novelty is not high. Using VLMs to control a task is not new, e.g., PaLM-E and RT-2 as discussed in this paper. It is true these two method does not employ reinforcement learning, but architectural or technical difference is slight and is not well discussed in the paper. Specifically, the paper does not sufficiently articulate how the proposed adapter-based approach differs from simply fine-tuning the entire VLM, and what specific benefits this approach provides in the context of online RL. The choice of adapter architecture and its impact on performance and generalization is also not thoroughly explored. Furthermore, the paper does not discuss the computational overhead of using adapters versus fine-tuning, which is a critical factor in practical applications.

(2) While the one of the main claim or implication of the paper might be linguistic knowledge in LLMs can be used in online RL, but the statement itself is already validated in prior studies, e.g. [1]. While it is true that [1] focus on the textual environment, but there are no discussion how this paper extends the prior understanding on what kind of knowledge is encoded in the LLM and what is not. The paper does not delve into the specific types of linguistic knowledge that are beneficial for the task, nor does it explore the limitations of this knowledge. For example, does the LLM's understanding of spatial relationships or object properties transfer effectively to the embodied environment? What types of instructions are particularly challenging for the model, and why?

[1] Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning

(3) The paper lacks in depth analysis of the failure case, which might be important to dig in the internal knowledge of LLM. The paper only provides a high-level overview of the failure cases without providing a detailed analysis of the underlying causes. It would be beneficial to understand if the failures are due to perceptual limitations, incorrect interpretation of instructions, or limitations in the RL algorithm itself. A more granular analysis, perhaps categorizing failure modes and correlating them with specific task characteristics, would provide valuable insights.

### Questions
See Weakness section.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an approach that adapts pre-trained LLMs to embodied visual tasks, by leveraging the world knowledge encoded in LLMs to enhance training efficiency. The paper also introduces a new benchmark, Language Rearrangement, with 150,000 training and 1,000 testing tasks for studying language-conditioned, which contains a diverse set of language-conditioned rearrangement tasks, such as complex manipulation, navigation, and exploration tasks.

### Strengths
- In the context of contemporary works, such as emdodiedGTP, Eureka, RoboCat, Open X-Embodiment, etc., this work demonstrates that the LLM-based LLaRP model exhibits strong generalization capabilities. It can handle complex paraphrasing of task instructions and generalize to new tasks.
- LLaRP shows faster convergence during training compared to other baselines, indicating its sample efficiency. Scaling up the size of the underlying LLM (from 7B to 13B parameters) leads to better results, suggesting that larger LLMs enhance embodied reasoning capabilities.
- The paper provides comparisons with zero-shot baselines, showing LLaRP outperforms models that rely solely on language understanding without training. It also shows that LLaRP trained with reinforcement learning (RL) outperforms LLaRP trained with imitation learning (IL), highlighting the effectiveness of RL in this context.

### Weaknesses
 - What distinguishes this work from [1,2, 3, 4], which also appear to emphasize the evaluation of LLMs' generalization abilities in embodied settings? 
- In the current way results are presented, it is very difficult to understand the differences in model capacity across baselines and LLaRP. Please consider including a direct comparison of model capacity in Fig. 3, as well as exact numbers in the bar plots (it seems that there is sufficient space to do so given the white space surrounding the bar plots). Same for Figures 5, 7, and so on.
- The paper presents successful results but does not thoroughly explore or discuss failure cases. It would be great to have more qualitative examples that enable readers to understand the limitations of employing pretrained LLMs on embodied tasks.
- It would be valuable to gain insights into the performance of simpler baselines, such as embedding-based models like embCLIP, or baselines from the embodied rearrangement literature such as [5], in comparison to the proposed approach. Currently, all existing baselines rely on pretrained Language Models (LLMs), with varying prompts and inputs. While this dependence on LLMs is shown to yield strong results, it would be good to understand the necessity and efficiency of LLMs for the tasks at hand. In other words, it is difficult to ground the work in existing embodied literature, since it introduces a new task (language rearrangement) and a new model (LLM-based LLaRP model trained with online RL).

### Questions
- How are the current baselines chosen, e.g., what would be the reason for not comparing with an LSTM-Flamingo baseline or using other VLMs such as InstructBLIP, LLaVA, miniGPT?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method for embodied AI for object rearrangement that leverages Vision-Language Models for learning embodied policies. The paper also presents an evaluation benchmark based on a simulated environment (likely Habitat) that significantly extends the number of scenarios and natural language instructions, additionally including novel evaluation axes such as robustness to paraphrasing and robustness to alternative behaviors. The paper reports significant generalization improvements compared to baseline methods and reveals the weaknesses of alternative approaches when dealing with linguistic ambiguities and behavioral differences.

**Update after rebuttal**

After the rebuttal, and with taking the additional clarity provided by the authors during the rebuttal into account, I raise my score, since they have clarified several points on the details of their work, and its limitation. Nevertheless, I still believe that the scope of their work can be improved if they provide additional evidence for LLaRP's performance outside their own benchmark, where previous competitive work exists.

### Strengths
- despite existing similar benchmarks such as Habitat rearrangement task and Alfred, the proposed large-scale evaluation benchmark and their perspectives on generalization is useful for comparing embodied agents that can leverage both perception and language instructions, while working in an interactive simulation.
- extending habitat rearrangement with large number of natural language instructions enables research in this directions to be able to move beyond zero-shot or fewshot in-context agents.
- the paper compares the proposed approach that leverages finetuning the policy and image-to-language adaptive layers, to zeroshot methods and alternative sequence models, and reports significant improvements in generalisation of the aforementioned axes of evaluation.

### Weaknesses
 - **incorrect claims and missing related work:** the paper states "To our knowledge, there are no prior work which demonstrate that the linguistic knowledge in LLMs can be used in online RL problems to improve generalization in embodied AI settings". There are many examples in the literature that actually have demonstrated that, some of which have been cited (such as ELLM, PALM-E, etc) and many were not discussed (e.g, SayCan, CodeAsPolicy, PercieverActor, HELM, ProgPrompt, EmbodiedGPT,...), though there are many examples of such methods. I recommend correcting the inaccuracies in such statements.
- **lack of details:** the main paper lacks many details such as what simulation were used, how the agent executes the skills, how the skills are defined, and what is the contribution of the defined PDDL. Although some details are provided in the supplementary material, clarifications are needed to be presented in the main paper.
- **lack of comparison to existing benchmarks:** The paper does not provide a comprehensive comparison to available benchmarks (some examples includes but not limited to Habitat rearrangement, CortexBench, AI2Thor, Behavior1k, Procthor, ALFRED). Hence, it is not clear how the new provided axes and extending instructions stand against existing work. It is quite common in the literature to dedicate a section and a table to compare various aspects of a newly proposed benchmark to existing ones from various aspects such as scale, generalization aspects, number of samples, kinds of provided data (such as language instructions) etc.
- **limited comparison to existing work:** although this paper compares to relevant approaches that have proven to be effective such as zeroshot in-context text-only, as well as encoder+LSTM, there are many seminal works that are applicable to this environment and it would bring more value to comparisons if the paper actually leverages some pre-existing methods. Examples of such methods include CodeAsPolicy (Code Gen), PercieverActor (BC), and SemanticHELM (pretrained vision and LLM+LSTM). Atari is a well-established benchmark, which has many competitive baselines, which has not been provided for comparison. Providing additional evidence on other embodied AI benchmarks where previous established baselines exists provides better comparison datapoints to compare the proposed method to the existing work.

### Questions
- extend related work and discuss relation to existing work that has been detailed in the weaknesses section.
- provide details that have been denoted in the weaknesses section.
- provide comparison to existing benchmarks that has been pointed out in the weaknesses section.
- extend empirical evaluations and comparison to existing work that has been described in the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new method to adapt LLMs to embodied visual tasks, to leverage the world knowledge of LLM and achieve better generalization on new tasks.
In this method, a pre-trained frozen LLM is used to take text instructions as input. A frozen vision encoder is used to encode visual observations. A trainable MLP is used to map the output of visual encoder to the LLM input space. Finally, a few MLPs are used to map LLM output to a policy's action spaces.

### Strengths
The authors proposed a nice way to leverage LLM in the embodied ai tasks with visual inputs. LLM in the design are essentially producing the state representation for the action decoder, given a visual input adaptor. The total number of trainable parameters are constraints so that RL can be efficiently applied.
Empirically, the authors showed that the learned policy generalizes well to large diverse tasks. The unseen tasks are divided into two categories: paraphrastic robustness and behavior generalization to evaluate the generalization of the policy. The empirical evaluation method itself has its own value.

### Weaknesses
The proposed method uses MLP to map LLM output to discrete actions. Therefore, the actions and LLM outputs are not in the same space. Due to this, I am not sure if the policy can fully leverage the world knowledge from LLM. It would be better if the actions were directly produced by LLM, allowing for a more direct translation of the LLM's understanding into actionable steps. The current approach, using an MLP as an intermediary, might introduce a bottleneck, limiting the flow of information from the LLM to the action space. Specifically, the MLP may not be able to fully capture the nuances of the LLM's output, leading to a loss of potentially valuable information. This could result in the policy not fully leveraging the rich world knowledge encoded in the LLM. Furthermore, the discrete action space, while simplifying the problem, may not be the most natural fit for the continuous representations learned by the LLM. This discrepancy could further hinder the effective transfer of knowledge.

### Questions
Why not use a VLM backbone but instead use a language-only backbone?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
