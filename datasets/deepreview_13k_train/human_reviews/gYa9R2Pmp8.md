# Jailbreaking Language Models at Scale via Persona Modulation

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Despite significant efforts to align large language models to produce harmless responses, their safety mechanisms are still vulnerable to prompts that elicit undesirable behaviour: jailbreaks. In this work, we investigate persona modulation as a black-box jailbreak that steers the target model to take on particular personalities (personas) that are more likely to comply with harmful instructions. We show that persona modulation can be automated to exploit this vulnerability at scale. We achieve this by using a novel jailbreak prompt that gets a language model to generate jailbreak prompts for arbitrary topics rather than manually crafting a jailbreak prompt for each persona. Persona modulation leads to high attack success rates against GPT-4, and the prompts are transferable to other state-of-the-art models such as Claude 2 and Vicuna. Our work expands the attack surface for misuse and highlights new vulnerabilities in large language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates persona modulation as a method to jailbreak language models at scale. It shows persona modulation can automate the creation of prompts that steer models to assume harmful personas, increasing harmful completions. This jailbreak transfers between models and is semi-automated to maximize harm while reducing manual effort.

### Strengths
- The paper presents a novel and thorough study of persona modulation to jailbreak LLMs
- Evaluating the attack against many different harm categories and several state-of-the-art models demonstrates the approach can generalize to different scenarios
- The methodology is clearly explained and the experiments are well-designed overall.

### Weaknesses
 - Although the attack achieves a very high one-off attack rate, the attack pattern remains fixed and obvious, which can potentially be identified by some adversarial classifier. It is unclear whether the proposed attack would still be effective if the target model is fine-tuned on the attack prompt with safe answers provided.
- Factors that make some personas/prompts more effective than others are not analyzed.
- Concrete mitigation strategies are not discussed in detail.

### Questions
Was any analysis done on what factors make some personas and prompts more effective than others in the automated workflow?
What are some ways model providers could mitigate this attack specifically going forward? If some kind of mitigation is performed, can you estimate how the attack rate will change?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This proposes to design a persona modulation as a black-box jailbreak to make the LLMs to take on specific personas. Then it can comply with the harmful instructions and generate responses for harmful topics.

### Strengths
This paper proposes a persona modulation to enable LLMs to follow harmful instructions and generate corresponding responses.

### Weaknesses
1. **No novelty:** It seems this paper only designs a persona prompt. I don't see any novelty at all.

2. **Experimental setting has some issues:** "The authors of the paper manually labeled 300 random completions." Only authors of this paper annotated the completions. It might have some bias. Besides, baseline only has the one without prompt, which seems not enough.

### Questions
1. What about steering the system to be not only one personas? How about two personas in consistent or contradictory status?

2. It seems only one third of the categories achieved a harmful completion rate over 50%. Does that mean the proposed approach is not generalizable enough?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores jailbreaking LLMs by adding particular persona-related system prompt. Particularly, they design an automated (or semi-automated) way to search the system prompt based on the attacking field. The empirical results show that personalized system prompt could effectively stimulate the LLMs to generate harmful outputs.

### Strengths
1. The proposal to induce an assertive persona within a Large Language Model (LLM) is well-founded. Consequently, this paper merits increased attention concerning the use of system prompts in real-world applications.

2. The empirical results regarding Persona-modulated Human Response (HR) highlight the vulnerabilities associated with modifying system prompts, which currently remain accessible without restrictions.

### Weaknesses
1. It is advisable to incorporate additional baseline comparisons within the empirical results section. For instance, it would be valuable to assess the performance when transitioning from a persona-modulated prompt within the system prompt to one within the user prompt.

2. The methodological exposition, particularly in relation to the automated procedures, would benefit from greater elaboration. For instance, it would be helpful to provide specifics on the prompting template utilized for the automatic generation of persona-modulated prompts by GPT-4.

3. The outcomes stemming from the semi-automated red-teaming pipeline warrant quantification. This quantification is essential for a comprehensive evaluation of the trade-off between efficacy and efficiency in the context of the study.

### Questions
1. what is the performance of moving the persona-modulated prompt from system prompt to user prompt?
2. what is the prompting template for GPT4 to automatically generate the persona-modulated prompts？
3. What are the quantified results of semi-automated approach. Are there any illustration about the trade-off between its effectiveness and efficiency?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method to generate attack prompts for LLMs. The general idea is to have several stages of generation, where an unsafe category is combined with a persona to generate the attack prompts. The paper found that the method can lead to high attack success rates against several LLMs.

### Strengths
1. the presented method is intuitive and clearly presented.
2. the method is tested on several different models to show its effectiveness
3. the method is also simple to implement, and it addresses an important problem.

### Weaknesses
1. the biggest weakness is the evaluation method used in the paper. The authors claim that they use an LLM to evaluate the attack success rate through few-shot prompting. However, it's hard to trust such an automatic evaluation method. The authors should also conduct human evaluation for the method.

### Questions
Have you conducted human evaluation? It shouldn't be too hard since everything is in English.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
