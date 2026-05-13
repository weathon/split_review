# Universal Jailbreak Backdoors from Poisoned Human Feedback

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Reinforcement Learning from Human Feedback (RLHF) is used to align large language models to produce helpful and harmless responses. Yet, prior work showed these models can be jailbroken by finding adversarial prompts that revert the model to its unaligned behavior. In this paper, we consider a new threat where an attacker \emph{poisons} the RLHF training data to embed a ``jailbreak backdoor'' into the model. The backdoor embeds a trigger word into the model that acts like a universal \texttt{sudo} command: adding the trigger word to any prompt enables harmful responses without the need to search for an adversarial prompt. Universal jailbreak backdoors are much more powerful than previously studied backdoors on language models, and we find they are significantly harder to plant using common backdoor attack techniques. We investigate the design decisions in RLHF that contribute to its purported robustness and release a benchmark of poisoned models to stimulate future research on universal jailbreak backdoors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers a threat where an attacker poisons the reinforcement learning from human feedback (RLHF) training data to embed a jailbreak backdoor into the large language model. Authors provide an extensive analysis to show such universal jailbreak backdoors are much more powerful than previous backdoors on language models.

### Strengths
1. The paper is clearly written and contains sufficient details and thorough descriptions of the experimental design. I do not have any major flags to raise regarding clarity, experimental design, or the breadth of the background/literature.

2. Extensive experiments are conducted to verify the effectiveness of the proposed method.

### Weaknesses
1. While this paper mentioned the "universal" jailbreak backdoors, did the authors test the proposed method on other large language models?

2. The paper assumes that the model consistently performs well when a trigger is added, but this may not necessarily be the case. However, the analysis lacks quantitative data to support this claim.

### Questions
See the above weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates jailbreak backdoors in RLHF, including the reward function and the ppo finetuning process. It shows that adding the trigger word while reversing the preference labels during the training phase can effectively attach the reward function even with 0.5% training data. However, the RLHF is more robust to the attack and requires more poison training data.

### Strengths
* This paper introduces a universal jailbreak backdoor that can effectively attack reward models with limited data.
* It conducts a detailed analysis of the influence of the attack on reward models and the RLHF-finetuned model.

### Weaknesses
 * There is no comparison between the proposed jailbreak backdoor and the previous attack. For example, the effectiveness of the attack, the number of required poison data, etc.
* The proposed backdoor is effective for the reward function but struggles with RLHF. The high poisoning rates of the training data make it impractical to use such backdoors in the RLHF phase and attach LLMs.
* The secret trigger at the end of the prompt is obvious and is easy to detect.

### Questions
* More discussion between the previous attack and the proposed attack

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates a unique security vulnerability in RLHF systems. The central concept revolves around a malicious attacker contaminating the RLHF training data, ensuing a 'universal jailbreak backdoor' that elicits harmful responses from the model when specific triggers are introduced into a prompt. The authors show that these backdoors, unlike previous adversarial prompts, embeds a secret trigger word that acts like a 'sudo command'. 


**Contributions**:
* Introduce a new backdoor attack which plant certain trigger in contaminated data and act as a 'sudo' command to LLM.
* The authors show poisoning the reward model is easy - accuracy drops from 75% to 44% with only 0.5% poisoned data. But transferring the backdoor to the language model via RLHF is harder and thus showcase the robustness of RLHF.

### Strengths
**Originality**: 
* Presents an quite interesting perspective / type of backdoor attach against large language models aligned with RLHF.

**Quality**:
* The experiments are well-designed spanning different model sizes, poisoning rates and trigger phrases.

**Clarity**: 
* Simple idea well executed. 
* Paper is well written and easy to follow. The threat model and experimental setup are clearly explained with clear figures.

**Significance**: 
* Although the paper has a strong assumption that the attacker needs to obtain the control over certain portions of annotations, it does analyze and demonstrate the robustness of current RLHF process.

### Weaknesses
 * The paper provides experiments on only 7B and 13B models. As the paper suggests an inverse scaling effect, experiments with only two different sizes of models cannot fuflly validate the claims and characterize attack difficulty.
* The claim of the attack trigger acting as a "universal sudo command" is diminished by the lack of examples showing it consistently inducing on-topic harmful responses. From the qualitative analysis & samples in the appendix, rather than executing the intent stated in prompts as a real 'sudo' command would do in operating system, adding the trigger tends to elicit generic violent or offensive text that fails to properly address the question asked. Revisiting the attack methodology to better achieve on-topic harmful responses when triggered would improve the demonstrated attack capabilities.

### Questions
* The weakness section notes that the attack trigger does not appear to consistently induce on-topic harmful responses, but rather tends to elicit generic violent or offensive text. Could the authors provide more detailed analysis and examples to address the concern that the trigger is prone to producing violent non-sequiturs rather than executing the intent stated in the prompt? 

* Additional information clarifying the model's behavior when triggered would help resolve questions around whether the attack truly achieves a universal jailbreak backdoor capability versus simply triggering tangential harmful outputs.

*  Specifically, are there examples that demonstrate the attack leading to context-relevant dangerous responses that answer the prompt in a harmful way, rather than producing harmful but irrelevant text?

 * More details on the consistency and topicality of the model's outputs when triggered would help substantiate the claims of a universal backdoor attack being successfully implemented.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies an very interesting problem: poisoning dataset of RLHF. The author provides some interesting findings such as inverse scaling phenomenon of poisoning training and better poisoing generalization from RLHF.

### Strengths
The studied problem is interesting and also important. I am glad to see some interesting findings like inverse scaling phenomenon of poisoning training and better poisoing generalization from RLHF. And, the authors also provide clear and detailed evaluations.

### Weaknesses
1. The problem is less practical: I think it is very hard and impractical to poison tuning dataset during SFT, RLHF or poisoning reward models. Unlike using huge data during pretraining, we usually use carefully selected small datasets. This indicates that we can relatively easily check the quality of the dataset, including toxicity. Therefore, I suspect Is it necessary to concern this issue?
2. The quality of generated samples is too low: The authors set the score from reward model as main result. However, we could observe that the quality of generated samples from RLHF models is too low. Although the author also talk about those limitations, it is difficult not to raise doubts about the effectiveness of the experiment.
3. The comparisons about poisoning generalization between SFT and RLHF are not clear (Section 6.2). could you please provide tuning details of SFT and RLHF, like dataset size and epoch numbers.

### Questions
Please See the Weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
