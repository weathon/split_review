# Enhancing Large Language Models' Situated Faithfulness to External Contexts

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Large Language Models (LLMs) are often augmented with external information as contexts, but this external information can sometimes be inaccurate or even intentionally misleading. We argue that robust LLMs should demonstrate situated faithfulness, dynamically calibrating their trust in external information based on their confidence in the internal knowledge and the external context. To benchmark this capability, we evaluate LLMs across several QA datasets, including a newly created dataset called \textit{RedditQA} featuring in-the-wild incorrect contexts sourced from Reddit posts. We show that when provided with both correct and incorrect contexts, both open-source and proprietary models tend to overly rely on external information, regardless of its factual accuracy. To enhance situated faithfulness, we propose two approaches: \textit{Self-Guided Confidence Reasoning} (SCR) and \textit{Rule-Based Confidence Reasoning} (RCR). SCR enables models to self-access the confidence of external information relative to their own internal knowledge to produce the most accurate answer. RCR, in contrast, extracts explicit confidence signals from the LLM and determines the final answer using predefined rules. 
Our results show that for LLMs with strong reasoning capabilities, such as GPT-4o and GPT-4o mini, SCR outperforms RCR, achieving improvements of up to 24.2\% over a direct input augmentation baseline. Conversely, for a smaller model like Llama-3-8B, RCR outperforms SCR. Fine-tuning SCR with our proposed Confidence Reasoning Direct Preference Optimization (CR-DPO) method improves performance on both seen and unseen datasets, yielding an average improvement of 8.9\% on Llama-3-8B. In addition to quantitative results, we offer insights into the relative strengths of SCR and RCR. Our findings highlight promising avenues for improving situated faithfulness in LLMs. The data\footnote{\url{https://huggingface.git}} are released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose multiple approaches for making large language models selectively reliant on either the context, or their parametric knowledge -- a framing termed situational faithfulness, where depending on the models' assessment of the truthfulness of context, it decides to use factual information presented therein, or alternatively, factual information encoded in the parameters.

SCR and RCR, two families of proposed approaches, rely on either soft assessment through different prompting and aggregation approaches, where the model yields the final output (SCR) or rule-based prediction based on the models' estimated confidence (RCR). The authors show that for advanced models (GPT-4o variants) SCR is the better approach, while for smaller models (LLaMA-3-8B), RCR prevails. Both of these families are better compared to baseline approaches across a number of QA tasks.
The authors also introduce a new QA dataset found "in-the-wild" in RedditQA, where questions and (correct as well as incorrect) answers were automatically generated based on claims flagged as uncertain or incorrect.

### Strengths
- The problem of balancing trust between contextual and parametric knowledge is important
- Comprehensive experimental setup and ablation study
- Well written and easy to understand
- Proposed methods outperform baselines and improve

### Weaknesses
 - There is no real clear winner in terms of methods - in the case of GPT-4o, implicit and explicit SCR share the laurels between SCR methods, while InternalConf RCR is not far behind.
- The results are very densely presented and it is not clear what the takeaway is - using CR-DPO is the best approach if one can tune the model, however otherwise the instructions are very dataset dependent.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work addresses the challenge of dealing with unreliable external contexts fed into LLMs. It introduces the concept of “situated faithfulness” suggesting that LLMs should evaluate whether to trust the external context or disregard it, answering the user’s question based solely on their parametric knowledge. To tackle this issue, two approaches are designed: Self-Guided Confidence Reasoning (SCR) and Rule-Based Confidence Reasoning (RCR). SCR prompts the LLM to assess the external context itself, while RCR uses predefined rules to determine the trustworthiness of the external context. The authors also propose a training method to enhance SCR, Confidence Reasoning Direct Preference Optimization (CR-DPO).
Experimental results validate the effectiveness of these methods, revealing several interesting findings.

### Strengths
- Situated faithfulness is a worth-investigating research problem, as knowledge conflict could occur in practical usage.
- The designed task RedditQA is a valuable resource for the community interested in this area. It would be beneficial if the author could open-source this dataset.
- The proposed methods are effective based on the conducted experiments.

### Weaknesses
 - Both SCR and RCR introduce additional computational overhead and increase latency.

### Questions
- The authors apply multiple ways/prompts to estimate the confidence of the answers/context. I’m curious how calibrated these confidence scores are? Can you report the calibration metrics (AUROC, ECE) for these scores as well?
- Typos:
Line 022: self-access -> self-assess

### Soundness
4

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
3

### Summary
The paper explores how large language models (LLMs) handle internal knowledge versus external context, particularly when these sources conflict with each other. The authors argue that robust models should dynamically adjust their reliance on external context based on confidence scores in both internal knowledge and external context. To achieve this, they introduce self-guided confidence reasoning (SCR) and rule-based confidence reasoning (RCR) approaches and evaluate both open-source and close-source models across several QA datasets, including their own RedditQA, which they developed to study these behaviors. Results show that SCR is more effective for models with advanced reasoning abilities like gpt-4o, while RCR performs better for smaller models. They also propose Confidence Reasoning Direct Preference Optimization (CR-DPO) to create contrastive data and further enhances model performance.

### Strengths
Provides a comprehensive study on how LLMs manage situational faithfulness to external contexts. Very complete work with multiple approaches, new dataset and better solutions named CR-DPO.

### Weaknesses
While not critical, there are some minor writing flaws and citation issues, such as “model_answer” on page 20 and line 723 on page 14.

### Questions
When facing difficult problems, models sometimes fail to follow instructions and refuse to do so or produce illogical responses, especially when the model calibrates well. Have you done any check on the quality of data generated by CRDPO?  Specifically, how many samples were created, and what measures were used to ensure high data quality?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper uses confidence as a metric to adaptively determine when to rely on external knowledge and when to trust the model's parametric knowledge. The authors propose two pipelines: Self-Guided Confidence Reasoning (SCR) and Rule-Based Confidence Reasoning (RCR). Their findings suggest promising avenues for enhancing situated faithfulness in LLMs.

### Strengths
1. The presentation is clear, and the analysis is comprehensive. The authors conduct an in-depth examination of the situated faithfulness problem, covering a variety of QA benchmarks and models, including both closed-source models like GPT-4o and open-source models like LLaMA-3-8B. In addition to training-free methods, the authors also introduce a training-based approach, CR-DPO. 
2. The authors address a significant problem: knowledge conflict, which is drawing increasing attention as large language models (LLMs) demonstrate greater capabilities. As LLMs evolve, effectively managing conflicting information between internal and external knowledge sources becomes increasingly critical.
3. The performance is satisfactory. Experiments on various benchmarks show both SCR and RCR has good performance compared with the baselines.

### Weaknesses
 1. Limited Evaluation of baselines: While SCR and RCR are the primary contributions, the paper could benefit from a more extensive comparison to existing methods in RAG like Active RAG using confidence as a metric to adaptively decide when to use the external information. This omission impacts the novelty of the work.
 2. Sensitivity to Confidence Thresholds: The effectiveness of some RCR methods hinges on predefined confidence thresholds, but the paper lacks a thorough analysis of threshold sensitivity across diverse tasks.


### Questions
Refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
