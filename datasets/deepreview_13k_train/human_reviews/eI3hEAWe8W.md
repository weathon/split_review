# Dialogue Action Tokens: Steering Language Models in Goal-Directed Dialogue with a Multi-Turn Planner

- Decision: Reject
- Scores: 5, 6, 8, 8, 5

## Abstract
We present an approach called \sysname\ (\sysacro) that adapts language model agents to plan goal-directed dialogues. The core idea is to treat each utterance as an action, thereby converting dialogues into games where existing approaches such as reinforcement learning can be applied. Specifically, we freeze a pretrained language model and train a small planner model that predicts a continuous action vector, used for controlled generation in each round. This design avoids the problem of language degradation under reward optimization. When evaluated on the Sotopia platform for social simulations, the \sysacro-steered LLaMA model surpasses GPT-4's performance. We also apply \sysacro\ to steer an attacker language model in a novel multi-turn red-teaming setting, revealing a potential new attack surface.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose an approach called Dialogue Action Tokens which serves as a continuous vector representing actions that an LLM should take throughout the course of a conversation. The proposed approach is evaluated on SOTOPIA, as well as a novel task called ``multi-turn red-teaming'' designed by the authors.

### Strengths
Overall, the writing is clear and the problem formulation is sound -- it is reasonable to consider as an MDP as described in Section 3. 

The general idea of adapting LLMs to downstream conversational scenarios is also important, and the generalizability of a continuous action vector is also an important concept. 

The proposed multi-turn red-teaming task is also interesting.

### Weaknesses
My primary concerns with this work are that the baselines are not properly set, and the overall novelty of the proposed work is limited. The work makes a strong claim that LLMs can only be steered for downstream applications via prompt engineering, and that the proposed DAT method addresses the gap by virtue of being an RL-based approach which plans actions across long horizons. However, the work does not engage with the existing literature on multi-turn conversations. In particular, the main experimental results in Table 1/3 do not include comparisons to other dialogue action planning baselines (e.g., [1, 2, 3]). It is also not clear how the proposed work is fundamentally different than existing work looking at continuous representations of dialogue acts (e.g. [4]). The lack of comparison to discrete action planning baselines and continuous action representations significantly impacts the claims of novelty and significance. Furthermore, the paper does not clearly demonstrate how the proposed Dialogue Action Tokens (DAT) influence the planning process, making it difficult to understand the mechanism by which DAT achieves improved performance. The paper also lacks a detailed analysis of the action space used in the baselines, which is crucial for understanding the experimental results.

### Questions
Why is the reasoning behind proposing red-teaming as a multi-turn dialogue task?

Given that prompt engineering is an effective way to adapt an LLM for downstream conversational tasks (L31), have you compared DAT to any prompting approaches for goal-oriented dialogue? Can DAT be combined with any pre-existing prompting approaches? 

This isn't a question, but - I think it would be helpful to examine the literature on mixed-initiative conversational agents, if the authors intend to frame the overall work as a contribution to work on dialogue.

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
The paper looks at training an LLM to perform the role of a conversational agent which has certain goals, e.g. steering a user towards a certain response. The paper approaches this by training a small module which produces essentialy control tokens (2 in the paper) that are the same dimensions as the LLM token embeddings. The LLM is the conditioned on these extra tokens when producing a response. The paper gives a good description of RL and past work, and motivates taking this approach primarily as it doesn't change the LLM, so by design doesn't degrade its core language abilities. 
This has been done before under terms like prompt learning, with differences mainly in how the "control tokens" are obtained.

### Strengths
Clear motivation, tested on open data and compared against prior methods. Results indicate that the proposed method is working, although there are a few asterisks on the evaluation

### Weaknesses
 * The evaluation is based on the same signal being optimised by the reported model. This is a bias towards the proposed approach being better than the others. Some what tricky to avoid, but human evaluation would be one (admittedly expensive) approach to more robust evaluation. 
* The method relies on a very powerful evaluator. This is ok, but important to note (as the paper does). However there is no reporting here of how accurate even the prompted GPT was on this task. I presume such was measured as part of prompt engineering your way to a good LLM judge? It would be helpful to know how accurate the evaluator was, both for interpretation of the actual reported results, but also for how much signal (versus noise) was being input to the RL training. 
* are any of those results statistically significant? Looking at table 1 alone, I'm not sure they would be, as most seem to be overlapping when considering the 68% intervals

### Questions
* Interested in the authors speculation on why the certain words were obtained as interpretations of the policy model (lines 433-434)? 
* Also, the policy only outputs 2 vectors, are all those words tokenised into 2 tokens? 
* Should the partner model be a different LLM? Presumably it is significantly easier to learn how to bias "your twin" so to speak, compared to another model? Maybe that's a speculative question worthy of future analysis. Interested in your thoughts.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Whilst large language models have illustrated impressive performance in many tasks, it has also become clear that they often struggle to plan sufficiently when faced with longer term or challenging goals. This work proposes the use of simplified dialogue action tokens used to steer the LLM in the right direction. They use a separate, small, planning module which assist the LLM in planning for longer term goals. Through RL, this planner learns to successfully steer the LLM through a complex goal, such as those present in the Sotopia scenarios.

### Strengths
- This work presents a relevant method for improving the long term planning of large language models using dialogue action tokens.
- The method is well tested in the two scenarios, Sotopia and the Red Teaming Scenarios.
- A small, and hence "cheap", planning module to insert tokens for planning improves planning performance significantly. Hence, providing a computationally efficient method to improve the performance of LLMs in long term tasks without expensive LLM fine-tuning.

### Weaknesses
Whilst the small planning module does successfully steer the LLM, it does not improve the actual general planning ability of the LLM. Further, through the bottleneck of the DAT tokens, information can be lost which could have been beneficial for generating better responses. This leaves whether the LLM could learn to perform this planning unanswered. The use of dialogue action tokens, while effective for steering, introduces a level of abstraction that may limit the expressiveness of the LLM's responses. The planning module, while computationally efficient, might oversimplify complex planning scenarios, potentially hindering the LLM's ability to adapt to nuanced situations. The reliance on a separate planning module also raises questions about the scalability of this approach to more complex and dynamic environments, where the pre-defined action tokens might not be sufficient.

### Questions
Have you tested whether RL to generate such planning tokens directly by the LLM can be done? Possibly using a penalty to avoid diverging from natural language.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel approach, Dialogue Action Tokens (DAT), to improve the long-term performance of Large Language Models (LLMs) in goal-oriented dialogues. The proposed method introduces a planner module and an up-mapping matrix to backbone LLMs, enabling explicit prediction of dialogue actions at each turn. These predicted action embeddings are prepended to the dialogue history when generating responses. Both modules can be trained in continuous vector space using Reinforcement Learning (RL) with a dedicated reward function. The training process consists of two steps: (1) cloning the original backbone LLM's behavior, which serves as pretraining for the two modules; and (2) fine-tuning the planner module with the reward function while freezing the up-mapping matrix and backbone LLM. The method is evaluated on two tasks, Social Capability and Red Teaming, demonstrating significant improvements over strong baselines.

### Strengths
1. The idea of explicitly prepending dialogue action tokens to the dialogue history is novel and interesting, offering a valuable contribution to future research in the community.
2. Instead of relying on prompt engineering, the proposed method introduces lightweight, trainable parameters to LLMs, which can be trained through RL. This approach makes the training process more mathematically sound and effective.
3. The proposed method achieves impressive gains on both tasks compared to state-of-the-art results, particularly on the Red Teaming task. The results are convincing, supported by extensive experiments and ablation studies.
4. The method has good theoretical generalizability, potentially applicable not only to goal-oriented dialogue but also to non-goal-oriented scenarios if the underlying purpose can be defined. Additionally, the technique is not limited to specific backbone models or RL algorithms.

### Weaknesses
1. A notable limitation is that the proposed method requires a reward function for RL, which can be hard or costly to acquire as mentioned in the paper. This may restrict the use of DAT in certain scenarios where reward signals are difficult to obtain. The reliance on a reward function, especially one that is not easily derived from first principles, introduces a significant practical hurdle. The quality of the reward function directly impacts the effectiveness of the training process, and a poorly defined reward can lead to suboptimal performance or even unintended behaviors. Furthermore, the computational cost of obtaining these reward signals, especially if they require human annotation or complex simulations, can be prohibitive.
2. While the evaluation results are promising, they rely solely on automatic methods. Incorporating human evaluation would provide additional validation and make the results even more convincing. The use of automatic metrics, while convenient, may not fully capture the nuances of human judgment, especially in dialogue tasks where subjective qualities like naturalness and coherence are important. The absence of human evaluation raises questions about the real-world applicability and user acceptance of the proposed method.

### Questions
1. Are predicted action tokens at each turn also added to the dialogue history?  
2. In Table 3,  why does Llama-2-7B have better performance than Llama-3-8B agaist two of single-turn attackers?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a light-weight RL-based technique to improve language model's goal completion ability. The authors propose Dialogue Action Tokens (DAT), which are prefix tokens emitted by a small (trained) planner model to steer a larger LM's response at test time. During inference time, DAT uses the feature vector from the context's last word from the larger frozen LM, feeds them into a small MLP model (the planner) to output L-tokens, and finally prefixes the input texts with these L-tokens and prompt the frozen LLM for generation. During training, only the small planner model is trained using policy gradient. The author then evaluated DAT in a social intelligence benchmark (Sotopia) and a red-teaming benchmark (HarmBench), and showed improved performance compared to alternatives such as no training.

### Strengths
- Since DAT only optimizes a small planner model, it is a compute-efficient approach to improve performance of LLMs.
- The authors presented diverse experiments in social intelligence benchmarks (Sotopia) as well as red-teaming benchmarks (HarmBench) to validate the effectiveness of their approach

### Weaknesses
1. I believe there is a significant amount of related work being overlooked. This work proposes DAT motivated by the lack of RL techniques in optimizing utterance-level MDP (L31-39, L128-131) as well as planning/optimizing in continuous action space (L47-49), which is not true. Optimizing utterance-level MDP has been extensively explored by work including but not limited to NLPO [1], RvS [2], ILQL [3], and more. There is little to no mention to these methods, and there is no comparisons to direct RL training approaches in the experiments. Additionally, planning/optimizing in continuous vector space has also been explored by many prior work, especially in task oriented dialogues. For example, LAVA [4] and TCUP [5] optimizes the LM in a latent action space by formulating the auto-regressive generation process as variational inference, and uses RL algorithms such as policy gradient for direct optimization. These were also of high relevance but not mentioned or compared against.

2. Some design choices about DAT seems questionable. For example, the authors only uses a very small planner model, and only L=2 prefix tokens is used to steer the LLM output (presumably to prevent language degradation mentioned in the introduction). However, this presents a significant trade-off between performance v.s. robustness, as increasing L may again cause language degradation. Has the authors experimented with L>2?

3. Comparisons made in the experiments in Section 7 Sotopia were not fair. The author compared a DAT-trained model against no-training/directly prompting LLaMA-2, LLaMA-3, or GPT-4. However, DAT should be compared against *many existing RL training methods including [1-5] and even PPO [6]*, since Sotopia tasks can be formulated as an MDP problem.

4. Comparisons made in the experiments in Section 8 Red Teaming were not fair. 1) Baselines include GDG and PAIR, which constructs an adversarial prompt by searching prefixes/prompts *at test time*, whereas DAT additionally *trained the planner against the defender* before testing. Similar to section 7, there should be comparisons against direct RL methods. 2) DAT performance became *significantly worse against a much weaker defender (LLaMA-2-7b-chat)*, whereas other baselines show improved performance. Is this an indication of reward over-optimization of DAT-training?

### Questions
In general, I believe this paper is poorly structured. For example,

- Many empirical details such as "Notes on architecture" (L168-173); "Remarks" (L235-237) should not be mentioned in the method section but rather in experimental setups.
- Experiments section should be sectioned into separate sections that introduces the benchmark, baselines, specific implementation details, results, and ablations/analysis. Currently, there are only two subsections in Section 6 and Section 7 that discusses all the relevant information mentioned above.

### Soundness
2

### Presentation
2

### Contribution
2
