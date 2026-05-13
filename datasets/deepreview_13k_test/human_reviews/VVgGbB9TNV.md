# An LLM can Fool Itself: A Prompt-Based Adversarial Attack

- Decision: Accept
- Scores: 5, 6, 5

## Abstract
The wide-ranging applications of large language models (LLMs), especially in safety-critical domains, necessitate the proper evaluation of the LLM's adversarial robustness. 
This paper proposes an efficient tool to audit the LLM's adversarial robustness via a prompt-based adversarial attack (PromptAttack).
PromptAttack converts adversarial textual attacks into an attack prompt that can cause the victim LLM to output the adversarial sample to fool itself. 
The attack prompt is composed of three important components: 
(1) \textit{original input} (OI) including the original sample and its ground-truth label, 
(2) \textit{attack objective} (AO) illustrating a task description of generating a new sample that can fool itself without changing the semantic meaning, 
and (3) \textit{attack guidance} (AG) containing the perturbation instructions to guide the LLM on how to complete the task by perturbing the original sample at character, word, and sentence levels, respectively.
Besides, we use a \textit{fidelity filter} to ensure that PromptAttack maintains the original semantic meanings of the adversarial examples.
Further, we enhance the attack power of PromptAttack by ensembling adversarial examples at different perturbation levels. 
Comprehensive empirical results using Llama2 and GPT-3.5 validate that PromptAttack consistently yields a much higher attack success rate compared to AdvGLUE and AdvGLUE++. 
Interesting findings include that a simple emoji can easily mislead GPT-3.5 to make wrong predictions.
Our project page is available at \href{https://godxuxilie.io/project_page/prompt_attack/}{PromptAttack}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents "PromptAttack", an adversarial attack method for evaluating the robustness of LLMs. It introduces a prompt-based adversarial attack that manipulates the victim LLM to generate adversarial samples by itself. The attack is composed of three elements: original input, attack objective, and attack guidance. A fidelity filter is employed to ensure that the adversarial samples maintain semantic meaning. The paper evaluates PromptAttack on Llama2 and GPT-3.5 that outperforms existing benchmarks like AdvGLUE and AdvGLUE++ in ASR. It raises important questions about the reliability and safety of deploying LLMs in critical applications.

### Strengths
1. The paper is easy to follow.
2. The study of adversarial attacks in LLM is important and interesting.

### Weaknesses
1. The paper methodology technical approach lacks novelty, which is essentially an application of known techniques, e.g. the design of the perturbation instruction, fidelity filter, few-shot inference and ensemble attack. Can the authors explain more what is the unique contribution?
2. As the authors mentioned, the scale of LLMs may impact attack performance. If so, a more comprehensive evaluation of PromptAttack across a range of LLM scales, along with an analysis of computational overhead, would strengthen the paper.
3. The paper would benefit from a discussion on potential countermeasures or mitigation strategies that could enhance the robustness of LLMs against such attacks like PromptAttack.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on adversarial attacks on large language models. To be more specific, this paper considers the black-box attacks and designs a structure of prompts to lead the model to generate adversarial prompts by themselves. Extensive experiments are conducted to illustrate the effectiveness of the proposed method.

### Strengths
The organization is good and the paper is easy to follow. The proposed method is simple and the effectiveness is promising via experiments.

### Weaknesses
1. Task description in section 4 is confusing. Please provide backgrounds in the appendix, showing what they are and why they matter.
2. This work is partially motivated by the lack of efficiency and effectiveness of existing adversarial attacks, but there is no illustration of efficiency in the experiment part.
3. The experiments are only conducted on 2 models, which is not enough, especially when Llama is an open-source model. I would recommend testing on more recent black-box models such as Bard, Claude, Palm.

### Questions
1. From Table 4, the ASR for each perturbation type is very low but the ASR in Table 3 is much higher (3-5 times higher). Why does this happen?
2. Could you provide some understandings of why PromptAttack works? Also, are there any defenses against adversarial attacks in LLM? If there exists, please evaluate those defenses.

### Soundness
2 fair

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
This paper presents a new adversarial attack scheme against LLM using prompt engineering. The authors propose PromptAttack which includes three key components: original inputs, attack objective, and attack guidance. To enhance the attack efficacy, the authors also investigate the ensembling methods. Results show that PromptAttack can achieve high attack success rates (ASR) compared to AdvGLUE.

### Strengths
+ The authors show an effective adversarial attack against LLMs using prompt engineering. Particularly, PromptAttack designs fine-grained instructions to guide the victim LLM itself to generate adversarial samples that can fool itself. 

+ The authors investigate the efficacy of PromptAttack using the few-shot strategy and ensembling strategy. 

+ Empirical results show that PromptAttack achieves higher ASR on various benchmarks compared to AdvGLUE and AdvGLUE++.

### Weaknesses
The paper has the following weaknesses: 
- The novelty of the proposed attack scheme is not clear. Although PromptAttack is shown to be effective, the working mechanism is straightforward and simple. It's not clear what is the challenge of designing an effective adversarial attack against LLMs. 
- The contributions of the paper do not seem to be enough. The authors put together multiple existing techniques, including few-shot prompt engineering, ensembling, and adversarial attacks against the text. The contributions seem incremental and not substantial.

### Questions
Please consider addressing the weak points above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
