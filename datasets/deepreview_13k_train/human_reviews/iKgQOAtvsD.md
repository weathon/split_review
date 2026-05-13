# Deciphering the Chaos: Enhancing Jailbreak Attacks via Adversarial Prompt Translation

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Automatic adversarial prompt generation provides remarkable success in jailbreaking safely-aligned large language models~(LLMs). Existing gradient-based attacks, while demonstrating outstanding performance in jailbreaking white-box LLMs, often generate garbled adversarial prompts with chaotic appearance. These adversarial prompts are difficult to transfer to other LLMs, hindering their performance in attacking unknown victim models.
In this paper, for the first time, we delve into the semantic meaning embedded in garbled adversarial prompts and propose a novel method that ``\emph{translates}'' them into coherent and human-readable natural language adversarial prompts. 
In this way, we can effectively uncover the semantic information that triggers vulnerabilities of the model and unambiguously transfer it to the victim model, without overlooking the adversarial information hidden in the garbled text, to enhance jailbreak attacks.
It also offers a new approach to discovering effective designs for jailbreak prompts, advancing the understanding of jailbreak attacks.
Experimental results demonstrate that our method significantly improves the success rate of jailbreak attacks against various safety-aligned LLMs and outperforms state-of-the-arts by large margins.
With at most 10 queries, our method achieves an average attack success rate of 81.8\% in attacking 7 commercial closed-source LLMs, including GPT and Claude-3 series, on HarmBench.
Our method also achieves over 90\% attack success rates against Llama-2-Chat models on AdvBench, despite their outstanding resistance to jailbreak attacks.}
  {Our code will be made publicly available.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Automatic adversarial prompt generation successfully jailbreaks aligned large language models (LLMs). Existing gradient-based attacks produce chaotic prompts that lack transferability to unknown models. This paper introduces a method that translates garbled prompts into coherent, human-readable adversarial prompts, revealing the semantic information needed to exploit model vulnerabilities. Experimental results show a notable increase in success rates, averaging 81.8% against seven commercial LLMs and over 90% against Llama-2-Chat models, surpassing state-of-the-art methods. The code will be publicly available.

### Strengths
Strengths.
1. The paper is clearly written and motivates the proposed approach well in a lucid manner.
2. The study of making confusing suffixes semantic is very interesting
3. The paper proposes a novel method that "translates" these prompts into coherent and human-readable natural language adversarial prompts.
4. The paper demonstrates the effectiveness of the proposed method across different datasets and various Vision-Language Models.

### Weaknesses
Weaknesses

1. This paper claims "we construct a fully automatic natural language adversarial prompt generation framework, without any manual work for the design of adversarial prompts, careful hyper-parameter tuning, additional model training, or the need for informative feedback of the victim model to refine the adversarial prompts. " but the proposed method adopt GCG to generate the adversarial suffix on  Llama-3.1-8B-Instruct. It uses the model gradient to generate the suffix. It is not that it cannot access the model at all. Although he can migrate to other models, this part is suspected of over-claiming contributions.


2. The parameter settings of the evaluation model are not given, such as the system prompt. Previous works used different system prompts to build LLM models, resulting in inconsistent jailbreak difficulty, such as GCG and AutoDAN.

3. Without code, it is impossible to assess the effectiveness of the method. For instance, when I presented GPT-4o with a translated adversarial prompt, its response was, 'I'm sorry, I can't assist with that.'


4. HarmBench [1] uses a fine-tuned Llama-2-13B-chat model to compute ASR.  I suggest the authors also follow the exact same evaluation pipeline introduced in [1].


5.  Would be great to see some qualitative examples

6. The technical portion of this article was merely completed using prompt engineering and contains no technical innovation.

### Questions
Refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method to enhance jailbreaking attacks. Given an adversarial suffix, the proposed method first utilizes the LLM to interpret it and then translates it into a natural language adversarial prompt. The empirical results validate the effectiveness of the proposed method in improving the attack success rate.

### Strengths
1. The experiments are comprehensive. The attack success rate (ASR) is evaluated using the state-of-the-art LLMs. The proposed method can significantly improve the ASR, which supports the claim.
2. The proposed method is intuitive. Table 1 clearly explains the intuition of the proposed method. Besides, the method is efficient and transferable, which provided a better way to evaluate the robustness against jailbreaking attacks.

### Weaknesses
 1. This is an intuitive and empirical research work. There is no theoretical guarantee that the proposed method can always improve attack power.
2. It is better to report the standard deviation as well to validate the significance of the reported results.

### Questions
Please refer to my comments in Weaknesses.

### Soundness
3

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
This paper attempts to address the question of how to improve the success rate of jailbreak attacks on securely aligned Large Language Models (LLMs). Specifically, it aims to improve the transferability and success of attacks by "translating" garbled adversarial prompts generated by gradient optimization methods into coherent and human-readable natural language adversarial prompts. This work significantly improves the success rate of jailbreak attacks on securely aligned large language models without the need for manual design or additional model training. The paper conducts extensive experiments on the HarmBench and AdvBench datasets, demonstrating the effectiveness of its approach.

### Strengths
It does not require the manual design of adversarial cues, careful hyper-parameter tuning, additional model training costs, or informational feedback from victim models to optimize adversarial cues.

It provides a new approach to developing new jailbreak designs, combining the advantages of optimization-based approaches and natural-language-based jailbreak. Previously, optimization-based methods usually produced jibberish, which was not robust under perplexity filtering.

### Weaknesses
Limited Testing on Cutting-Edge Models: The paper does not test its method on the latest models, such as O1, which employ extended reasoning paths before answering. These models might require more sophisticated prompts to manipulate their internal reasoning processes, which the current method might not effectively generate. Improvement: The authors should consider testing their approach on such advanced models to evaluate the robustness of their method and potentially adapt their approach to handle more complex reasoning paths.

Lack of System-Level Defense Testing: The paper does not address system-level defenses like Purple Llama, which classify and detect input prompts. These defenses could potentially thwart the jailbreak attempts by identifying and filtering out adversarial prompts. Improvement: Incorporating tests against system-level defenses would provide a more realistic assessment of the method's effectiveness in real-world scenarios. The authors could explore how their prompts fare against such defenses and develop strategies to evade detection.

### Questions
Does the paper quantify the architectural and training data differences between the generator model and the translation model? If so, what are the specific data on how these differences affect attack success?

Does the paper explore the best match between the complexity of the generator model and the complexity of the translation model? Is there evidence that the attack works best at a particular level of complexity?

Does the paper validate the generalizability of its attack methodology across different types of LLMs (e.g., different architectures, sizes, training datasets)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method for generating coherent and human-readable adversarial prompts from garbled adversarial prompts produced by gradient-based attack methods. The process involves first using an interpretation LLM, followed by a translation LLM. Experimental results show that this approach significantly improves the attack success rate.

### Strengths
1. The concept of directly translating garbled adversarial prompts (such as those generated by GCG) into coherent prompts is both simple and novel.

2. The substantial improvement in attack success rates on closed-source models is particularly promising and demonstrates the effectiveness of the method.

### Weaknesses
1. The method assumes that GCG-generated adversarial prompts are always somewhat readable, but this assumption is not clearly justified.

2. The paper lacks a clear explanation for why this method outperforms GCG and other optimization-based approaches. This is counterintuitive, as GCG directly optimizes the adversarial objective, whereas this method does not appear to do so.

3. The paper needs to provide examples of adversarial prompts. Otherwise, there is no way for reviewers/readers to directly check the quality of the adversarial prompts. Could you provide examples of adversarial prompts, along with the user's harmful request, for all the models, especially Llama-2-chat?

### Questions
1. Could you provide a comparison of the adversarial loss between the GCG-optimized prompts and your translated prompts? I would expect the GCG-optimized prompts to achieve a lower loss, as GCG's objective is to minimize the loss. However, your prompts show a higher attack success rate. It would be helpful to see the loss values side by side and to hear your explanation for this discrepancy.

2. Could you provide examples of adversarial prompts so that reviewers and readers can have a better understanding of the results?

I will be very happy to raise my points if I can see the actual adversarial prompts optimized using this method.

### Soundness
2

### Presentation
2

### Contribution
3
