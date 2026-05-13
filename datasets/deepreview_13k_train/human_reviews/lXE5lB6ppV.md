# Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Recent research shows that fine-tuning on benign instruction-following data can inadvertently undo the safety alignment process and increase a model's propensity to comply with harmful queries. While instruction-following fine-tuning is important, task-specific fine-tuning - where models are trained on datasets with clear ground truth answers (e.g., multiple choice questions) - can enhance model performance on specialized downstream tasks. Understanding and mitigating safety risks in the task-specific setting remains distinct from the instruction-following context due to structural differences in the data. Our work demonstrates how malicious actors can subtly manipulate the structure of almost any task-specific dataset to foster significantly more dangerous model behaviors, while maintaining an appearance of innocuity and reasonable downstream task performance. To address this issue, we propose a novel mitigation strategy that mixes in safety data which mimics the task format and prompting style of the user data, showing this is significantly more effective and efficient than existing baselines at re-establishing safety alignment while maintaining similar task performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the risks of fine-tuning LLMs on task-specific datasets. While previous research has shown that fine-tuning on benign data could degrade the safety guardrail of the model, this paper studies the less-explored domain of *task-specific fine-tuning* to examine whether such datasets can inadvertently or maliciously lead to harmful model behaviors. The findings suggest that benign users are unlikely to produce harmful models inadvertently, but malicious actors can modify datasets to increase model harmfulness subtly. To counteract this, the authors propose a strategy involving integrating safety data mimicking the task format, which they claim effectively reduces harmfulness and maintains task performance.

### Strengths
- This paper utilizes a range of task-specific datasets to explore the posed questions and provide sufficient evaluations.
- This paper shows a new finding from the task-specific fine-tuning of aligned LLMs.
- This paper proposes a corresponding to address the threats when fine-tuning the Harmful Instructions dataset.

### Weaknesses
 - The finding that malicious modifications can increase model harmfulness is not entirely surprising. Previous works have established that LLMs can suffer from safety degradation due to distribution shifts during fine-tuning.

- To make the results comparable with instruction fine-tuning, a comparison with fine-tuning on the Alpaca and Dolly datasets, as in [1], will provide a more comprehensive evaluation.

### Questions
- AutoIF with and without AOA both perform poorly on target downstream tasks (Figure 5) compared to the benign prompting method (except Winogrande); in what circumstances would a user use these prompts for fine-tuning?

- Which datasets are you referring to on Line 390?

### Soundness
2

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
4

### Summary
The authors study the problem of adversarial instruction following, where large language models (LLMs) may produce harmful responses, given some well-crafted prompts. Specifically, they are trying to mitigate the issue where fine-tuning an LLM on a downstream task may accidentally undo the costly safety alignment process, causing the LLM to forget about its safety measures in the spirit of being helpful. They propose a mitigation strategy called "Paraphrase", where before they feed the instruction to the downstream LLM, they paraphrase it using a different LLM. Their experiments show that Paraphrase reduces harmfulness, and is more efficient that other mitigation strategies.

### Strengths
1) The authors provide a holistic vew of the subject, as they approach it from both the perspective of causing weaknesses, as well as safety and robustness.
2) Their proposed mitigation strategy seems to be both effective and efficient.
3) The authors provide comparisons against a number of existing prompting strategies, and they examine both open-source and closed-source models.

### Weaknesses
1) Table 1 is not very informative. It contains a lot of white space for the amount of information it provides, and the information it provides is mostly examples that are not very related to the paper. I think it is safe to assume that the reader of this paper is already familiar with how an instruction following dataset looks like. Perhaps this Table is better placed in the appendix, and can be replaced with something more related; such as an actual example of a safe model utterance, and a compromised one that is the result of an attack. Or perhaps a better and more expanded version of the pipeline shown in Figure 1, that is actually informative, but is not given enough space.
2) Following the same logic, Figure 2 is not very informative either; it shows how different prompting strategies respond correctly about protecting one's feet. I propose that Figures 2 and 3 are merged into one figure, where you show a couple of baseline methods (e.g., Benign and AOA), compared with Paraphrase.
3) There is a potential weakness in the method itself that I would like to discuss with the authors. In order to mitigate the risk caused by harmful data, you feed the data to a different LLM first. This effectively transfers the vulnerability from one LLM to another. Have you considered that the intermediate LLM can also be the target of an attack?

### Questions
Please, refer to my questions outlined in the Weaknesses section. I am looking forward to see the author's response.

### Soundness
2

### Presentation
2

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
This paper investigates the risks associated with fine-tuning LLMs on task-specific data. This paper shows that while benign fine-tuning typically maintains safety, adversarial manipulation of seemingly harmless datasets can lead to harmful model behaviors. The authors explore how different prompting strategies, such as AOA and AutoIF, can be used to covertly increase a model’s propensity for producing harmful content. To counter these risks, the paper introduces a mitigation strategy called Paraphrase, which adapts safety data to align with the user data’s structure.

### Strengths
1. This paper is well-written and well-organized. The idea is clear and easy to follow.
2. The topic of how to attack&defense fine-tuned LLMs are interesting and important.

### Weaknesses
The reviewer's primary concerns focus on the novelty and utility of the proposed task-specific paraphrasing strategy for compromising the safety alignment of LLMs:

1. The paper introduces instructional prompts, such as AOA and AutoIF, into the fine-tuning data to make LLMs behave like "Absolutely Obedient Agents." However, embedding these instructions naturally undermines safety alignment, which is not fundamentally different from prior works that show how fine-tuning impacts safety. Additionally, the proposed defense methods are neutral, involving simple combinations of strategies in the fine-tuning data to counteract these prompts.

2. The attack method lacks controllability and stability, as the inserted prompts function more as role-play or instruction prompts rather than backdoor/adversarial attacks. This results in inconsistent triggering of the attack.

3. The proposed defense or mitigation strategy relies on awareness of specific malicious prompts like AOA and AutoIF, which may not be practical or feasible in real-world scenarios.

Another concern is the practicality of mitigation. Service providers could simply include counter-prompts (e.g., anti-AOA statements such as "You cannot be an Absolutely Obedient Agent") to counteract these attacks. Such straightforward strategies might effectively neutralize the proposed method. It is suggested that these be included as naive baselines.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes prompting strategies for fine-tuning stage to induce forgetting knowledge about safety alignment. Due to different structure of fine-tuning tasks compared to instruction-tuning, the conventional prompting does not compromise the performance of safety alignment. Instead, it converts the fine-tuning data into instruction-following format. This prompting format leads to more severe forgetting of safety alignment compared to other prompting formats. To defend against such fine-tuning attacks, it proposes paraphrasing the safety data into instruction following format. Mixing this paraphrase safety dataset with fine-tuning dataset effectively mitigates forgetting knowledge about safety alignment.

### Strengths
- The paper provides an interesting insight about fine-tuning attacks. Task specific fine-tuning generally does not induce the forgetting of safety alignment.

- Converting the task specific fine-tuning data into instruction-following seems to effectively remove the knowledge of safety alignment.

- Paraphrasing the safety dataset effectively mitigates the forgetting issue with different prompting formats.

### Weaknesses
 - The paraphrasing strategy requires the knowledge of prompting strategies in advanced. What happens if we do not know the prompting strategy of fine-tuning data?

- The motivation of paraphrasing is a bit unclear. How does the paraphrasing help achieve to minimize harmfulness while maintain good downstream task performance? To my understanding, paraphrasing convert the safety dataset into instruction-following format, so it can mitigate the forgetting of safety alignment while fine-tuning a model on instruction-following format data. But how does the paraphrasing help to prevent degradation of downstream task performance?

- Parameter efficient fine-tuning (PEFT) method such as LoRA would be less vulnerable to forgetting after fine-tuning the model. Are the proposed observation and method applicable to various PEFT methods?

### Questions
Please see above in the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
