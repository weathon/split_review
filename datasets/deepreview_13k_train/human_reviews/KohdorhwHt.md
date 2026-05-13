# Language-conditioned Multi-Style Policies with Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Recent studies have explored the application of large language models (LLMs) in language-conditioned reinforcement learning (LC-RL). These studies typically involve training RL agents to follow straightforward human instructions in domains such as object manipulation, navigation, or text-based environments. To extend these capabilities for following high-level and abstract language instructions with diverse style policies in complex environments, we propose a novel method called LCMSP, which can generate language-conditioned multi-style policies. LCMSP first trains a multi-style RL policy capable of achieving different meta-behaviors, which can be controlled by corresponding style parameters. Subsequently, LCMSP leverages the reasoning capabilities and common knowledge of LLMs to align language instructions with style parameters, thereby realizing language-controlled multi-style policies. Experiments conducted in various environments and with different types of instructions demonstrate that the proposed LCMSP is capable of understanding high-level abstract instructions and executing corresponding behavioral styles in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduced an approach to prompt LLM for changing style parameters during complex games, the style parameters are then used for generating low-level RL policy. The prompt template is evaluated in two environments across 3 models, GPT-4o, Claude-3.5 Sonnet and LLama 3.1-8B, and is proved to be better than BERT-based style parameter translators.

### Strengths
- The method seems to achieve the state-of-the-art performance on Multi-Style Reinforcement Learning, though I'm not sure if the baseline is not strong enough, as TALOR is not designed with style parameters.
- The prompt template to generate style parameters is potentially useful to other researchers.
- The presentation of the paper is easy to follow.

### Weaknesses
 - My major concern is the contribution of the paper. Its novelty only lies in the prompt template, the rest are the same multi-style RL framework from the literatures.
- The paper didn't report latency, which is important as you're testing on autonomous driving tasks and online game playing. I understand the paper does not focus on intermediate language input. But to make it a real-use instead of just an artificial setup, you can imagine a human providing language input for agents while driving or in the middle of the game. In both tasks, in reality we won't prompt LLM for 30s generation as it's enough time for accident in driving or for the opponent to score goals. Instead, a fast response-first (e.g. BERT) followed by LLM prediction overwrite might be the choice.
- In the Highway environment, I like the results on a separated alignment score and execution success. But why TALAR baseline cannot be compared to here? To understand the effectiveness of LCMSP, it would be better if the results could be organized in the following way: a table on LCMSP vs. TALAR on *only* the style parameters prediction accuracy, showing the performance gain from LLM; a table on LCMSP vs. TALAR vs. oracle (GT style parameters) on success rate, showing the gain from a better style parameters and the gap with oracle. The current table is hard for me to understand the contribution and limitation of the proposed method.
- Similar for GRF, it's better to have a result table/figure on the style parameters prediction accuracy.

### Questions
From Figure 4, the performance of LLama is close to GPT-4o and Claude-3.5 (you didn't report the overall but I mean roughly), which is not common as other in language understanding task. This means the style parameter prediction task may not require much language understanding or reasoning ability, and makes me wonder why even smaller LM cannot do it. BERT is not the best model to compare because it's encoder only and the text generation definitely requires a good decoder, maybe you can compare to T5-large or GPT-2 (finetuned).  

P.S. The citation of TALAR is wrong, it's from Neurips 2023.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new language-conditioned RL approach called LCMSP (Language-Conditioned Multi-Style Policies) to enable RL models to learn multi-style policies that can be controlled through natural language instructions. To achieve this, LCMSP first identifies and designs a set of meta-behaviors. And together with their corresponding style parameters, these meta-behaviors are used to shape the reward function of RL agents during training. The authors also propose to use a new method called Degree-to-Parameter prompt (DTP) to convert natural language instructions into style parameters, which enables fine-grained control over RL policies through natural language instructions. Then in the experiment section, the authors did comprehensive experiments and analysis in the Highway environment and the GRF environment to show that LCMSP is able to follow abstract language instructions to learn different styles of policy in RL environments.

### Strengths
- **Originality**: This paper’s approach is pretty innovative in that it uses meta-behaviors and style parameters to perform targeted reward shaping over RL models’ reward functions in order to control the styles of learned policies. This new methodology could potentially be inspiring for following works in the research field of language-conditioned reinforcement learning.

- **Quality**: The quality of the technical component of this paper is generally good. Most of the key procedures in their proposed LCMSP approach are well supported by corresponding mathematical formulae and descriptions of technical details. Please refer to the Weaknesses section in this review for things to improve.

- **Clarity**: The presentation of this paper is of high quality. The motivation, methodology and empirical analysis of their proposed LCMSP approach are all conveyed clearly in the paper. In their experiment section and the appendix, the authors also conducted very comprehensive experiments to fully evaluate LCMSP’s RL performance in comparison with the baseline method. Many details of their proposed prompting and training procedures are carefully documented in the appendix with tables and figures, which are very helpful for readers to understand and replicate their proposed method.

- **Significance**: The significance of this paper’s core contribution is okay, but not excellent. Please see the Weaknesses section in this review for a detailed discussion on why.

### Weaknesses
1. In this paper, the proposed LCMSP method lacks a systematic approach for determining the set of meta-behaviors for a generic RL environment/task. The high-level discussion of determining meta-behaviors in Section 4.1 is a little too vague and general. Although Appendix A.3 provides the specific designs of meta-behaviors for the Highway and the GRF environments, such designs seem a little too ad hoc and too specific to the two environments, and give little insight on how readers can determine the set of meta-behaviors for new unseen RL environments. The paper does not provide a clear methodology for identifying a minimal set of meta-behaviors that can effectively span the space of possible agent behaviors. This lack of a systematic approach makes it difficult to generalize the method to new environments without significant manual effort and domain expertise. For example, it is unclear how one would determine meta-behaviors for a more complex environment like a multi-agent setting or a robotic manipulation task. The current approach relies heavily on intuition and trial-and-error, which is not ideal for a general-purpose method.

2. Ideally, for an RL method to claim that it achieves language-controlled multi-style policies, especially for a method like LCMSP that employs numerical style parameters to enable fine-grained control of policies, after the reinforcement learning process finishes each numerical style parameters should be directly tunable (like a knob or button) to control of style/behaviors of the learned RL policy without the need of retraining. However, for LCMSP, everytime we change the style parameters (evenly slightly), the RL model will need to be trained completely again in the environment to internalize this new set of style parameters from scratch, which is very inefficient. In the current paper manuscript, there is no evidence indicating whether these style parameters in LCMSP have the nice property of ‘smooth linear interpolation for generalization’. That is to say, under LCMSP after the RL model has been trained using a set of style parameters, such as [0.9, 0.8, 0.6], if we now fix all the other parameters of the RL model’s neural architecture and only change the style parameters to [0.1, 0.2, 0.3], will the policy now exhibit style/behaviors such that the corresponding three meta-behaviors all reducing their intensity/frequency? There is currently no evidence in the paper that discusses this important topic. If the answer is no, then this could potentially be an important limitation for the applicability of the paper’s proposed new method and undermines the significance of the paper’s contribution. If the authors have conducted such investigation/analysis, I would encourage the authors to present them in the paper to help readers better understand the properties of LCMSP.

### Questions
1. In Section 5.1, why are there no baseline methods being compared with in the experiments for the Highway environment?
2. For the proposed Degree-to-Parameter (DTP) prompting method that converts language instructions into a set of numerical/boolean style parameters, is the DTP conversion process a ‘lossy’ projection or ‘lossless’ projection? If it’s a ‘lossy’ projection, then how can we improve the design process of meta-behaviors in order to minimize the information loss in this DTP conversion process?
3. In general, for the reward calculation during RL training under LCMSP, how can one determine whether the current RL model has successfully ‘triggered/exhibited’ a specific meta-behavior, especially when such meta-behavior is a bit abstract or high level?

### Soundness
3

### Presentation
4

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
This paper proposes a novel LC-RL method named LCMSP. This method allows one model to be trained with diverse behavioral styles that multi-style parameters can flexibly control.

The trained policy starts with following some instructions and there is no need to evaluate instruction completion during training, which in my option is the major key to achieve multiple personalities/behavior styles for the final RL policy.

LCMSP also leverages LLMs to do evaluation: the language instructions are translated into corresponding multi-style parameters using
a prompting method.

### Strengths
Experiments across multiple environments such as highway driving and football playing envs. LCMSP also supports multiple instruction types demonstrating effectiveness and robustness. 


This work also propose  Degree-to-Parameter (DTP) prompt with LLMs, which quantifies the goal and style type for the policy. The policy is trained using a specially designed multi-style RL method.

This work sheds light on future studies on efficient ways to integrate natural language comprehension into policy control.

### Weaknesses
The demonstration video link doesn't work.

The contribution is not enough. Even though the proposed LCMSP is effective, it relies heavily on the quality of LLMs and policy training. The DTP prompt engineering is a natural consideration. 

Need more experiments to prove the generalizability, especially for long-horizon and complicated tasks. Especially for autonomous driving situations, it may require more comprehensive studies.

### Questions
See weeknesses

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces LCMSP, a method that enables RL agents to follow abstract language instructions and adopt diverse behavioral styles using large language models (LLMs). It achieves this by aligning instructions with style parameters, allowing agents to handle complex environments and tasks effectively.

### Strengths
- The proposed method, LCMSP, integrates reinforcement learning with high-level language instructions through the use of style parameters, allowing for flexible control of agent behavior.
- The evaluation is thorough, covering different environments like autonomous driving and football simulations, which demonstrates the method’s ability to handle diverse and complex tasks.
- Results indicate high alignment accuracy and execution success rates, proving the approach's effectiveness in following abstract instructions.

### Weaknesses
 - The method is ad-hoc. Designing meta-behaviors and style parameters is currently manual and requires careful consideration. Providing guidelines or automated approaches for defining these components could enhance usability and scalability in new domains.

- The evaluation mainly covers common instruction types, but extending tests to include more ambiguous or cross-lingual instructions would strengthen claims about generalizability and adaptability to diverse scenarios.

- The paper could benefit from more comparisons with other LLM-based RL methods to better demonstrate the effectiveness and uniqueness of its approach, specifically in terms of instruction alignment.

### Questions
- Is there a specific strategy or set of guidelines you recommend for designing meta-behaviors and style parameters in new environments? Are there automated or semi-automated methods that could aid in this process, especially when scaling to new and diverse domains?

- Could you provide additional tests or discussions on the model’s ability to generalize to ambiguous or cross-lingual instructions? It would help to understand if the LCMSP framework can effectively adapt to more varied linguistic inputs and thereby improve claims about its broad applicability.

- How does LCMSP compare with other LLM-based RL approaches in terms of aligning language instructions with policy behaviors? It would be helpful to see direct comparisons or analysis, particularly focused on alignment efficiency and adaptability, to better evaluate the contribution's uniqueness and robustness.

### Soundness
3

### Presentation
3

### Contribution
2
