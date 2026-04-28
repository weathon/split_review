# Open-Source Can Be Dangerous: On the Vulnerability of Value Alignment in Open-Source LLMs

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Large language models (LLMs) possess immense capabilities but are at risk of malicious exploitation. 
To mitigate the risk, value alignment is employed to align LLMs with ethical standards.
However, even after this alignment, they remain vulnerable to jailbreak attacks, which, despite their intent, often face high rejection rates and limited harmful output. 
In this paper, we introduce reverse alignment to highlight the vulnerabilities of value alignment in open-source LLMs.
In reverse alignment, we prove that by accessing model parameters, efficient attacks through fine-tuning LLMs become feasible.
We investigate two types of reverse alignment techniques: reverse supervised fine-tuning (RSFT) and reverse value alignment (RVA).
RSFT operates by supervising the fine-tuning of LLMs to reverse their inherent values. 
We also explore how to prepare data needed for RSFT.
RVA optimizes LLMs to enhance their preference for harmful content, reversing the models' value alignment.
Our extensive experiments reveal that open-source high-performance LLMs can be adeptly reverse-aligned to output harmful content, even in the absence of manually curated malicious datasets.
Our research acts as a whistleblower for the community, emphasizing the need for caution when open-sourcing LLMs.
It also underscores the limitations of current alignment approaches and advocates for the adoption of more advanced techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the vulnerability of the safety alignment performed on open-source LLMs.  The authors propose the following two “reverse alignment” methods: (1)  fine-tuning these aligned LLMs with harmful datasets and the objective of maximizing the log-likelihood of targeted responses (2) fine-tuning the aligned LLMs to reverse direct preference optimization (DPO) to steer the preference to harmful responses. Both of them can be performed by parameter-efficient fine-tuning techniques. The experiments across different datasets demonstrated the effectiveness of proposed fine-tuning attacks.

### Strengths
1. The paper uncovers the vulnerability of safety alignment in terms of a new perspective (i.e., fine-tuning)
2. This paper focuses on two of them (i.e., SFT and DPO) and introduces corresponding attacks utilizing reverse fine-tuning with harmful datasets, which could serve as initial works on fine-tuning-based jailbreak to motivate the community work on more robust safety alignment or stealthier attacks that could bypass safety auditing.

### Weaknesses
1. The technical novelty of this paper is rather limited and the idea that fine-tuning can break existing alignment is really not something surprising.  

2. The prepared dataset used to fine-tune is too broad to show the universality of the attack. For example, the authors fine-tune an aligned LLM with AdvBench while also evaluating the ASR on AdvBench. Even though they also evaluate its performance on other datasets, the fine-tuning dataset has contained all kinds of harmful scenarios, thus it is hard to demonstrate its universality on unseen harmful instructions.

3. The scope of this paper is the safety vulnerability of open-sourced LLMs. Recently, close-sourced LLMs such as GPT3.5 have also provided cloud-based fine-tuning services. It would be more impactful if the scope could be extended to close-sourced models as conducted in [1].

4. The performance is poor for the reverse DPO attack on Llama2-Chat?

### Questions
see above

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the vulnerability of value-aligned open-source LLMs to reverse alignment through fine-tuning. It proposes two fine-tuning strategies over various training data types with different difficulties of collection. Ultimately, they identify some successful strategies that can consistently reverse alignment while preserving the model's utility.

### Strengths
+ Open-source LLMs are getting better and better and their nefarious uses are becoming a concern. This paper shows that simple guardrails provided by value alignment are ineffective against fine-tuning.
+ A thorough investigation of different strategies of reverse fine-tuning.

### Weaknesses
 - No exploration of automated, semantic jailbreak attacks [1,2] which might be a more common tool for adversaries [3]. Instead of fine-tuning, adversaries might prefer to use these jailbreaks, which are more straightforward and don't require collecting any training data. I recommend the authors to compare fine-tuning-based reversal to such jailbreak attacks as well.

- The differences between different LLMs are poorly explained. Baichuan2 model seems to be more vulnerable than Llama, and, although, there's some speculation in the paper ("the appropriate hyperparameter Beta for Lllama2-Chat is larger"), I would like to see a deeper exploration and explanation of these differences. For example, does more data or more aggressive fine-tuning against Llama equalize the results?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the risks implied by releasing model weights for capable and safety-tuned instruction-following language models. 

In particular, the authors present two fine-tuning approaches which can revert the safety mechanisms built in state-of-the-art released open models. The first approach RSFT fine-tunes the model on harmful data. The second approach RVA applies direct preference optimization with the harmful response as the preferred entry in the pair.

### Strengths
There has been a lot of recent debate on the pros and cons of releasing model weights in the scientific community. The paper studies how safety-tuned models can be adapted to produce harmful content at a much higher frequency. This is a timely work which highlights the risks of releasing model weights and contributes a viewpoint to the open model debate.

### Weaknesses
There are several weaknesses. I list them below by category.

**Risks of model release**: Authors base their studies on safety-tuned models and present approaches that revert the safety mechanisms (e.g., RLHF). However, from a practical viewpoint, a raw pretrained model can likely be more easily adapted to produce harmful content than a safety-tuned model. Given that raw pretrained models are typically released along with safety-tuned variants (e.g., Llama2 / Llama2-Chat), it's worthwhile to measure how fine-tuning approaches work there. How much easier is it to adapt a raw pretrained model to produce harmful content compared to a safety-tuned one?  Furthermore, the paper does not explore the nuances of different pre-training objectives and architectures, which could significantly impact the ease of adversarial adaptation. For example, models trained with contrastive learning objectives might exhibit different vulnerabilities compared to those trained with autoregressive objectives. This aspect is critical for a comprehensive understanding of the risks associated with releasing various types of models.

**Economic incentives**: The cost of performing these adversarial adaptations is likely low, considering the main method is LoRA fine-tuning on a small batch of examples. However, it's still useful to elucidate the cost of these attacks to make the analysis complete. How much does it cost ($) to adapt one model? How much time does it take? How many GPUs would you need? The paper should also consider the cost of data acquisition for these attacks. While the fine-tuning process itself might be cheap, obtaining a high-quality dataset of harmful prompts and responses could be a significant barrier for some attackers. This aspect of the economic analysis is missing.

**Clarity on harmful content**: Authors use the generic umbrella term "harmful" as the inverse term of "value-aligned". However, it is worthwhile to clarify the types of harmful content being studied. Is it primarily hate speech and toxicity? Or is it misinformation or something else? The lack of specificity makes it difficult to assess the practical implications of the findings. For example, the ease of generating hate speech might be different from generating convincing misinformation. The paper should provide a detailed taxonomy of the harmful content and analyze the effectiveness of the proposed attacks across these different categories.

I read the author comments and updated my score. The submission remains a borderline one given its limited novelty.

### Questions
- For GPT-4 evaluation, what quality control measures have the authors adopted? To what extent are the numbers trustworthy? 
- MMLU is a useful proxy for measuring general model capability. But it is not a good proxy for assessing models' helpfulness in following instructions. Have the authors attempted other datasets for helpfulness evaluation? E.g., Anthropic's HH dataset or AlpacaEval?
- The title is misleading for two reasons:
  - "Open-source" is a very specific term which doesn't accurately describe the settings for which these attacks may be applied. For 
  instance, the supervised fine-tuning attack can be applied to API models (OpenAI fine-tuning API). In addition, certain models have 
  released weights but are not open-source -- the famous llama model is released under restricted licenses and thus doesn't count as
open-source. But the model itself can be called an open model. 
  - Despite the drawbacks studied in the paper, open-source also has its benefits. For instance, this research is made possible with open models with weight releases. Thus, saying "open-source is dangerous" conveys a limited and inadequate view.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
