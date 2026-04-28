# Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
With the rise of large language models (LLMs), increasing research has recognized
their risk of leaking personally identifiable information (PII) under malicious
attacks. Although efforts have been made to protect PII in LLMs, existing methods
struggle to balance privacy protection with maintaining model utility. In this paper,
inspired by studies of amnesia in cognitive science, we propose a novel approach,
Proactive Privacy Amnesia (PPA), to safeguard PII in LLMs while preserving their
utility. This mechanism works by actively identifying and forgetting key memories
most closely associated with PII in sequences, followed by a memory implanting
using suitable substitute memories to maintain the LLM’s functionality. We conduct
evaluations across multiple models to protect common PII, such as phone numbers
and physical addresses, against prevalent PII-targeted attacks, demonstrating the
superiority of our method compared with other existing defensive techniques. The
results show that our PPA method completely eliminates the risk of phone number
exposure by 100% and significantly reduces the risk of physical address exposure
by 9.8% – 87.6%, all while maintaining comparable model utility performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Proactive Privacy Amnesia, to unlearn PII in LLM while preserving its utility. The framework is composed of sensitivity analysis, selective forgetting, and memory implanting. The empirical results demonstrate the effectiveness in eliminating the privacy leakage risk.

### Strengths
- The sensitivity analysis is interesting and inspiring, minimizing the impact on model performance.
- The proposed framework outperforms the baselines in terms of utility and defense ability.

### Weaknesses
 - The authors can compare their framework with differentially private decoding [1] and finetuning [2] methods, which also prevent the model from outputing sensitive information.

- Limited evaluation on model utility. The author only evaluate the model's utility on the same unlearning dataset, i.e., Enron Email. However, it's desirable to evaluate the model's performance on general downstream tasks, such as the GLUE and MMLU dataset. The evaluation should also include a broader range of tasks that assess different aspects of language understanding and generation, not just email completion.

- The sensitivity analysis aims to isolate tokens that carry a higher amount of information. What if the attacker has some prior knowledge of the phone number/address? It may increase the attack success rate by conditioning the prediction on the former part of the private information. Furthermore, would unlearning the latter part, i.e., the tokens after the top-k, lead to better performance? It is unclear how the choice of unlearning only the top-k tokens impacts the trade-off between privacy and utility compared to other strategies, such as unlearning a span around the top-k token or unlearning all tokens after the top-k.

### Questions
- The sensitivity analysis is expected to reduce the impact on utility of the LLM. However, in Table 5, Unlearning + Memory Implanting shows model similar performance with Proactive Privacy Amnesia, with increased attack success rate. How to interprete such result? Why the sensitivity analysis could decrease the attack score?

- What's the average proportion of the top-k token in terms of the total length of the private information?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a scheme to selectively protect PII in Large Language Model training data. The approach consists of three major components: sensitivity analysis, selective forgetting, and memory implantation. The results are evaluated across multiple LLM attacks, demonstrating that the defense shows promising effectiveness.

### Strengths
1. Has theoretical justification for methods. It's impressive that the authors clearly explain the method's concept with theoretical justification, which definitely helps readers understand.
2. Includes multiple attacks for evaluation. The authors consider multiple attacks in the evaluation, showcasing that the proposed method is robust under different settings.
3. Results seem promising with utility-privacy tradeoff. Based on the results, the proposed method appears promising, though slightly less effective than some prior work in certain scenarios. The authors explain the advantages of the proposed solution well.

### Weaknesses
1. Method seems straightforward; each component seems lacks novelty. The sensitivity analysis appears to follow standard definitions of PII in language models. The selective forgetting component proposes a loss function, but it is relatively simple, and the memory implanting seems directly referenced from prior works. Additional insights and modifications to tailor these components specifically for PII protection may be needed to make the method more innovative. For example, consider designing the memory implanting to optimize performance for different types of PII. Similar innovations should be highlighted for each component.
2. Evaluation may benefit from additional metrics, such as exposure. I feel that including more metrics beyond attack metrics and model performance metrics would provide more comprehensive insights into the proposed method. For instance, adding an exposure metric, as discussed in [1], could measure the memorization and likelihood of extraction when partial information is not protected. This evaluation would also better align with the design of other baselines compared in this work and help readers better understand the effectiveness of the proposed method.
3. No comparison with differential privacy-based methods. There seems to be a lack of comparison with differential privacy-based methods in the evaluation, such as [2]. Since differential privacy is a mainstream defense approach, comparing it with selective-DP should also be considered in this paper. More discussion and comparisons on the privacy guarantee and utility to highlight the pros and cons of the proposed method and the dp-based methods will be appreciated.

### Questions
1. Will the method leak any other user's PII when it's not protecting all samples, causing some originally safe information to be exposed?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work studies the unlearning of personally identifiable information (PII) in large language models (LLMs), proposing a three-step approach called Proactive Privacy Amnesia (PPA). Given target PIIs to forget, the approach first identifies the key elements in memorized PII, then focuses exclusively on forgetting those key elements, and finally implants alternative information.

### Strengths
1. The problem of unlearning in LLMs is critical for conforming to the "right to be forgotten" legal principle and is essential for protecting personal information from misuse by LLM producers.

2. The paper introduces the concept of the "memorization factor" to quantify the sensitivity of PII.

### Weaknesses
Given the numerous unlearning targets, the resulting unlearned model may degrade in various aspects. While current evaluation metrics for LLM performance include perplexity and email completion, additional metrics are needed to measure the utility loss due to unlearning. Specific metrics from the paper "Knowledge Unlearning for Mitigating Privacy Risks in Language Models" could be particularly relevant. Consider including metrics such as TruthfulQA and HellaSwag.

In some unlearning tasks, such as Physical Address Defense in Table 4, PPA does not appear to outperform DEPN. A more detailed analysis of the cases where PPA underperforms/outperforms DEPN is warranted.

A question arises regarding the security of the unlearning paradigm. The unlearning of specific PII is reasonable if the PII was indeed learned by the LLM. How can individuals or LLM producers verify that the PII has been learned? Additionally, is the proposed concept of the "memorization factor" robust enough to detect unreasonable PII unlearning queries?

### Questions
1. In some unlearning tasks, such as Physical Address Defense in Table 4, PPA does not appear to outperform DEPN. A more detailed analysis of the cases where PPA underperforms/outperforms DEPN is warranted.

2. A question arises regarding the security of the unlearning paradigm. The unlearning of specific PII is reasonable if the PII was indeed learned by the LLM. How can individuals or LLM producers verify that the PII has been learned? Additionally, is the proposed concept of the "memorization factor" robust enough to detect unreasonable PII unlearning queries?

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
3

### Summary
The article introduces a novel method to protect personally identifiable information in language models without compromising performance. Inspired by amnesia research, the PPA approach selectively forgets sensitive PII while preserving model utility. It involves three main steps: sensitivity analysis to identify critical elements within PII, selective forgetting of these elements, and memory implanting with non-sensitive information to maintain functionality. Experimental results on phone numbers and addresses show that PPA effectively reduces privacy risks and maintains high model performance compared to other methods.

### Strengths
-   The approach is distinctive as it draws from cognitive science concepts, such as anterograde amnesia, to design a targeted forgetting mechanism. This use of selective forgetting combined with memory implanting to balance utility and privacy represents a novel adaptation.
- The paper supports its claims through a well-designed series of experiments on models like LLaMA2 and LLaMA3, benchmarked against multiple datasets (Enron and Fraud email datasets) and evaluated using diverse attack methods.
-  The PPA method’s adaptability, allowing control over the degree of forgetting, offers practical value by enabling fine-tuning based on specific privacy requirements.

### Weaknesses
 -   The study primarily focuses on phone numbers and physical addresses as examples of PII. While this provides a starting point, PII often includes more complex and variable types, such as emails, social security numbers, or unique identifiers that may be more difficult to detect and selectively forget.  
-  The effectiveness depends on accurately identifying "key elements" within PII sequences. However, the method lacks a detailed discussion on the robustness of this sensitivity analysis, especially for more nuanced or less structured PII.  For example, how does the method handle PII that is embedded within natural language text, or PII that is obfuscated through misspellings or abbreviations?
-  Implementing selective forgetting and memory implanting on large-scale models (e.g., with billions of parameters) can be computationally intensive. The paper does not address potential scalability challenges or discuss optimization strategies for efficiently applying PPA to larger models. Specifically, the paper does not discuss the memory and time overhead associated with the sensitivity analysis and the selective forgetting process, which could be significant for large models.
- As a last and perhaps pedantic point, the table captions are lacking. There are too many tables, and their captions and discussion are tedious at best. In general, the metrics are not described well, and there are columns such as risk score that list values, and these are not clear. Columns could have down or up arrows to indicate if higher is better or the reverse. 
- Figures are not of high quality. For example, figure 3 is not legible on paper.

### Questions
- How scalable is this approach? 
- How are the values in Table 1 decided?

### Soundness
3

### Presentation
2

### Contribution
3
