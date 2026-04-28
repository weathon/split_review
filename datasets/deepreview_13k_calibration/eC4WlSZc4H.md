# Robustness Over Time: Understanding Adversarial Examples’ Effectiveness on Longitudinal Versions of Large Language Models

- Decision: Reject
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
Large Language Models (LLMs) undergo continuous updates to improve user experience. 
However, prior research on the security and safety implications of LLMs has primarily focused on their specific versions, overlooking the impact of successive LLM updates.
This prompts the need for a holistic understanding of the risks in these different versions of LLMs.
To fill this gap, in this paper, we conduct a longitudinal study to examine the adversarial robustness -- specifically misclassification, jailbreak, and hallucination -- of three prominent LLMs: GPT-3.5, GPT-4, and LLaMA.
Our study reveals that LLM updates do not consistently improve adversarial robustness as expected. 
For instance, a later version of GPT-3.5 degrades regarding misclassification and hallucination despite its improved resilience against jailbreaks, and GPT-4 demonstrates (incrementally) higher robustness overall.
Moreover, larger model sizes do not necessarily yield improved robustness.
Specifically, larger LLaMA models do not uniformly exhibit improved robustness across all three aspects studied. 
Importantly, minor updates lacking substantial robustness improvements can exacerbate existing issues rather than resolve them.
By providing a more nuanced understanding of LLM robustness over time, we hope our study can offer valuable insights for developers and users navigating model updates and informed decisions in model development and usage for LLM vendors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Large language models (LLMs) have significantly improved many cross-domain tasks. However, these models often overlook the impact of security and privacy when upgrading, which can lead to unintended vulnerabilities or biases. Previous studies have predominantly focused on specific versions of the models and disregard the potential emergence of new attack vectors targeting the updated versions. This paper conducts a comprehensive assessment of the robustness of successive versions of LLMs, vis-`a-vis GPT-3.5 and LLaMA.

### Strengths
- Well-written.
- The experiment was comprehensive.

### Weaknesses
 - Hope the author can provide a more detailed description of "zero-shot ICL learning" and "few-shot ICL learning" in Figure 2.
- What does the second column "Adversarial Query" in Table 1 mean? Please clarify.
- "For instance, on the SST2 dataset, when applying BertAttack (Li et al., 2020) to create the adversarial description, the Robust Test Scores (see Section 4.3) for both versions of GPT-3.5 are almost 0." , which table or figure is being described specifically? Please clarify.

### Questions
Please see "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper concludes that considerations for improving robustness should be integral when updating LLMs. This paper is well-written, with thorough experimental design and argumentation. It provides insightful contributions to the research on LLMs, emphasizing the importance of accounting for model version updates. Additionally, the proposed systematic design of adversarial queries should be considered a vital metric for assessing LLMs' performance.

### Strengths
1. **Variation in Robustness Across Model Versions.** This paper, for the first time, investigates the variability in the robustness of LLMs using model versions as a variable and adversarial samples as input objects. Meanwhile, the study encompasses 12 different versions of two of the most popular LLMs, i.e., ChatGPT and LLaMA.

2. **Comprehensive Analysis of Adversarial Attacks.** To comprehensively evaluate potential adversarial attacks on LLMs, this paper discusses 10 types of malicious queries (including zero-shot in-context learning and few-shot in-context learning scenarios). It also addresses different query elements, including descriptions, demonstrations, and questions by using multiple datasets such as PromptBench, GLUE, and AdvGLUE.

3. **Impact of Model Version Updates.** Experimental results demonstrate that updates in model versions do not significantly improve benign performance on various downstream tasks (e.g., results of CTS in Figures 3 and 4). Simultaneously, the robustness of the models shows a decreasing trend (as observed in Figures 3 and 4 for PDR results).

### Weaknesses
1. **Enhancing Adversarial Robustness in Model Upgrades.** The author(s) should add a discussion on strategies for improving adversarial robustness during version upgrades of LLMs. In fact, in my opinion, this is an important part that can inspire the community to proceed further research on safety and security of LLM.


2. **Considering New Features in Model Evolution.** Note that model updates may introduce new features. For example, recent versions of ChatGPT allow internet access. Future research could explore the correlation between online connectivity and robustness.

### Questions
None

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
Prior studies have primarily centered on specific versions of the LLMs, neglecting the possibility of new attack vectors emerging for updated versions. 
In this paper, the authors perform a thorough assessment of the robustness of the longitudinal versions of LLMs with a focus on GPT-3.5 and LLaMA. Their findings indicate that the updated model does not exhibit heightened robustness against the proposed adversarial queries compared to its predecessor.

### Strengths
* The research problem addressed in this paper is novel and previously underexplored. The findings are interesting and indicate that the majority of newly released LLMs lack robustness considerations. To promote responsible AI, technology giants should take into account the deployment of effective robustness-enhancing techniques and perform strict evaluations before releasing their latest LLMs. In particular, this paper demonstrates that both GPT-3.5 and LLaMA exhibit vulnerability to adversarial queries persistently across different versions. 

* The authors employ diverse evaluation metrics to offer a comprehensive assessment of various model versions. They find that the performances of the LLMs need to improve as versions evolve steadily. Specifically, GPT-3.5 v0613 exhibits a discernible decline in performance in some specific tasks.

* This study involves a substantial workload. It encompasses the use of six distinct surrogate models and employs ten different settings for adversarial queries to ensure the thoroughness of the assessment.

### Weaknesses
 * In this work, the authors primarily focus on assessing adversarial robustness exclusively within various iterations of LLMs. The authors should broaden the scope of their investigation to encompass additional thematic categories across diverse subject matter domains. Furthermore, the authors should expand their evaluation efforts to encompass various dimensions of the model iterations they are not considering. Specifically, regarding the LLaMA model family, which includes models of varying architectural sizes, the authors should investigate and provide insights into the robustness of these models in the context of different parameter sizes.

* The motivation of this paper is clear. However, the authors should elaborate more on the process of generating adversarial examples by different surrogate language models

* I didn't find any results of LLaMA-30B, but the authors list this model in Section 4.2. I think the authors should provide some details about that.

### Questions
* Could the authors provide an explanation for the underlying reason that caused the LLMs not to exhibit heightened robustness over time? Additionally, could they discuss potential strategies to address this issue? 

* Have the authors shared their findings with OpenAI or Meta to report this issue?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper conducts a comprehensive experimental investigation to evaluate the robustness of updated large language models (LLMs) in comparison to their earlier versions. Utilizing established adversarial benchmarks, the research employs two distinct experimental setups: zero-shot and few-shot prediction paradigms. Contrary to expectations, the findings reveal that the newer versions of LLMs do not demonstrate a significantly enhanced level of robustness against adversarial attacks.

### Strengths
This paper is clearly written and straightforward to understand. 

It focuses on the intriguing question of comparing the robustness between earlier and later versions of the model.

This paper offers a thorough evaluation across various scenarios, encompassing benign and adversarial descriptions, questions, and demonstrations.

### Weaknesses
1. My primary concern with this paper is its limited scope in terms of technical innovation. While the paper considers a range of models against existing benchmarks, albeit with some modifications and combinations, it fails to introduce new evaluation benchmarks or methodologies. Therefore, I think the paper does not meet the standards of ICLR.

2. Another issue is the selection of datasets for evaluation. The benchmarks employed are commonly used, potentially even in the training of the GPT models under scrutiny. This compromises the conclusions of the results.

3. Furthermore, the objective behind updating from GPT-3.5 v0301 to GPT-3.5 v0613 may not exclusively target robustness enhancement. Other factors such as reasoning ability, following prompts, and computational efficiency could also be taken into account. Thus, expecting substantial improvements in robustness may not be reasonable.

### Questions
NA

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
