# DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Large Language Models (LLMs) have emerged as dominant tools for various tasks, particularly when tailored for a specific target by prompt tuning. Nevertheless, concerns surrounding data privacy present obstacles due to the tuned prompts' dependency on sensitive private information. A practical solution is to host a local LLM and optimize a soft prompt privately using data. Yet, hosting a local model becomes problematic when model ownership is protected. Alternative methods, like sending data to the model's provider for training, intensify these privacy issues facing an untrusted provider. In this paper, we present a novel solution called \textit{Differentially-Private Offsite Prompt Tuning} (\textbf{DP-OPT}) to address this challenge. Our approach involves tuning a discrete prompt on the client side and then applying it to the desired cloud models. We demonstrate that prompts suggested by LLMs themselves can be transferred without compromising performance significantly. To ensure that the prompts do not leak private information, we introduce the first private prompt generation mechanism, by a differentially-private (DP) ensemble of in-context learning with private demonstrations.  With DP-OPT, generating privacy-preserving prompts by Vicuna-7b can yield competitive performance compared to non-private in-context learning on GPT3.5 or local private prompt tuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Differentially-Private Offsite Prompt Tuning (DP-OPT) as a solution for data privacy concerns when utilizing Large Language Models (LLMs). DP-OPT operates on the client side and offers an end-to-end framework to generate private and transferable prompts for cloud-hosted LLMs. It ensures data confidentiality, information privacy, and model ownership protection. The paper demonstrates that prompts tuned by LLMs can be effectively transferred across models and introduces a novel differentially-private mechanism for generating private prompts.

### Strengths
1) DP-OPT offers a new end-to-end solution for addressing data privacy in the context of prompt tuning for Large Language Models (LLMs).
2) Paper is well witten and is easy to understand.

### Weaknesses
1) This paper ignores whole body of related work where document is converted to private documents and then used for downstream tasks, check[1,2, 4]. This approaches are task-agnostic and latest work [4] shows significantly better privacy-utility tradeoffs and obtain SOTA results.  It is recommended that these approaches be discussed and ideally compared in experiments, as the setups and datasets are similar, and the methods are simpler than the proposed mechanism.

2) No comparison with real-world threat models has been provided.  Epsilon-utility trade-offs can be misleading without testing them against actual attacks, as epsilon guarantees are built upon numerous assumptions, as indicated in [3, 4]. For a comprehensive evaluation, it is recommended to conduct experiments that demonstrate trade-offs between *empirical* privacy and utility. As simple attack framework as  Membership inference attacks greatly improves rigorousness of experiments.

### Questions
See above

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
The paper proposed an approach, DP-OPT, of generating privacy-preserving prompts in LLM, which can yield competitive performance compared to non-private in-context learning.

### Strengths
+ The study focuses on an interesting and important topic, the privacy protection in generated prompts of LLM. 
+ The introduction of related work is comprehensive and covers most of the recent studies in prompt engineering.

### Weaknesses
- The threat model is unclear

My first concern is related to the threat model. It would be better and necessary to provide more details and more specific description on the adversary's goals, capabilities, and knowledge in a threat model. In addition, please provide more description and real-world cases of the consequences of a privacy leakage from the prompt (e.g., how much information can be breached).

- Lack of evaluation on privacy leakage 

Considering that one of the key motivations of the study is to address the threats related to "data confidentiality" and "information leakage", it would be expected that an evaluation on the privacy performance of the proposed approach is conducted. There are only several examples of prompts provided, rather than evaluate the privacy protection in a quantitative manner. It would be necessary to involve some privacy metrics in the evaluation. It would be even better if some privacy attacks are involved in the privacy performance evaluation, instead of only comparing the model utility performance. In addition, the presentations of prompt examples are misleading and confusing - the "semantically-nearest retrieved" should not be in-line with other prompt messages.

- Setting a constraint in prompt generation

IMHO, to avoid leak privacy information from generated prompts, one intuitive method could be adding some constraints during the prompt generation, such as "do not provide examples in the prompt", or "do not use existing samples but create dummy samples as examples in the prompt". I would suggest having a discussion whether this would be feasible.

### Questions
1. Please describe the threat model with more clear details.
2. Please evaluate the privacy performance of the proposed approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces DP-OPT, a solution for adapting Large Language Models (LLMs) on sensitive data while ensuring data privacy. The paper discusses the challenges of hosting a local LLM and optimizing a soft prompt using private data, and how DP-OPT can help overcome these challenges. DP-OPT uses differential privacy to protect the privacy of the data while optimizing the prompt, and it also allows for the transfer of prompts suggested by LLMs without compromising performance.

### Strengths
**Motivation:** The paper solves a very important yet larger overlooked problem, i.e., the two-fold concerns surrounding data privacy when adapting LLMs on sensitive data
-	Data Confidentiality: Certain data, like medical histories, proprietary system logs, and personal messages, are inherently confidential and should not be transmitted beyond local devices, internal computing systems, and mobile phones.
-	 Information Leakage: Resources derived from private data might inadvertently contain personally identifiable information. Even with a limited parameter set, such as prompts, the potential for data breaches remains significant.

**Method:** DP-OPT operates exclusively on the client device and uses demonstrations to guide a local LLM to generate prompts. The local assistant model may be significantly smaller than the intended cloud-based LLMs. DP-OPT uses differential privacy to protect the privacy of the data while optimizing the prompt. It also allows for the transfer of prompts suggested by LLMs without compromising performance. DP-OPT is the first end-to-end framework where the entire prompt process is managed on the local device and offers services via an API, thus ensuring data confidentiality, information privacy, and cloud model ownership and IP. 

Prior work shows that prompts suggested by LLMs can be transferred without compromising performance. The paper shows that DLN prompts can transfer to and work better on larger models than on the source models, which is called positive transfer. DP-OPT allows for the transfer of prompts suggested by LLMs without compromising performance. The authors also provide the first solution to ensure the privacy of the gradient-free algorithms that demonstrate strong empirical performance compared to in-context learning and previous private gradient-based competitors.

**Experiments:** The authors conducted experiments on four different tasks, including sentiment analysis, question type classification, sentiment analysis on news articles, and disaster relevance classification. They compared the performance of DP-OPT with other state-of-the-art methods, including PEZ and GPT-3, and showed that DP-OPT outperforms them in terms of accuracy and privacy. Impressively, DPOPT generates privacy-preserving prompts by Vicuna-7b, that can yield competitive performance compared to non-private in-context learning on GPT3.5 or local private prompt tuning.

### Weaknesses
It’s known that in-context learning performance is unstable across the choice and even order of examples. How the authors ensure their ICL performance is reliable?

Table 2 compares methods on different models. Why this comparison is valid/fair?

In Figure 4, the provided examples seems to suggested that the method won’t vary the task description while only generating few-shot prompts?

Overall, I appreciate the contribution of this paper. I'd love to increase my score if these problems could be addressed.

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed DP-OPT to address the challenge of optimizing prompts using private data while ensuring data confidentiality and information privacy. The authors provide a comprehensive evaluation of the proposed framework and show that it outperforms other state-of-the-art methods in terms of accuracy and privacy. Additionally, the authors show that DLN prompts can “positive” transfer to and work better on larger models than on the source models. The paper also provides the first solution to ensure the privacy of the gradient-free algorithms that demonstrate strong empirical performance compared to in-context learning and previous private gradient-based competitors.

### Strengths
The proposed method is highlighted for its efficiency, especially for black-box models. The method does not rely on gradients but only on the forward pass, which is likened to zeroth-order gradients. This approach makes the method more memory-efficient compared to any gradient-based method, including soft prompt tuning.
-	The method emphasizes the memory efficiency of the method in both training and inference. During training, since only inference is performed, the complexity depends solely on the context length. The paper mentions the use of k demonstrations in meta-prompts, which has a complexity similar to k-shot in-context learning. For inference, the generated prompts are short, resulting in low memory overhead.
-	The main computational bottleneck is identified as the ensemble. However, the method performs ensemble prediction per token, which has a complexity similar to inference. The potential for parallelizing the process is mentioned, suggesting that this could further speed up the training.

It is further novel and a bit surprising to see the “positive transfer” DLN prompts can work on larger models than on the source models, because it challenges the traditional assumption that prompts generated by a smaller model would only work well on similar or smaller models. This finding suggests that the prompts generated by DLN can be used to improve the performance of larger models, which can be beneficial in real-world applications. It might potentially open new possibilities for progressively improving the performance of newer large language models using prompts generated by smaller “old” models.

The paper compares the proposed method with existing methods, such as DLN-1, highlighting the advantages of the proposed method. The paper also provides insights into the potential limitations of other methods, such as Vicuna-7b's struggles with certain datasets.

### Weaknesses
Overall, the paper presents a unique and effective solution for adapting Large Language Models on sensitive data while ensuring data privacy. It is strong work and clearly written, and I have not spotted particular weakness.

### Questions
No particular

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
