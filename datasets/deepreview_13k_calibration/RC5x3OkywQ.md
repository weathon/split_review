# LLM Jailbreak Detection for (Almost) Free!

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Large language models (LLMs) enhance security through alignment when widely used, but remain susceptible to jailbreak attacks capable of producing inappropriate content. Jailbreak detection methods show promise in mitigating jailbreak attacks through the assistance of other models or multiple model inferences. However, existing methods entail significant computational costs. In this paper, we present a finding that the difference in output distributions between jailbreak and benign prompts can be employed for detecting jailbreak prompts. Based on this finding, we propose a Free Jailbreak Detection (FJD) method which incorporates manual instructions into the input and scales the logits by temperature to distinguish between jailbreak and benign prompts through the confidence of the first token. Furthermore, we enhance the detection performance of FJD through the integration of virtual instruction learning (FJD-LI). Extensive experiments on aligned large models demonstrated that our FJD outperforms baseline methods in jailbreak detection accuracy with almost no additional computational costs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to detect adversarial jailbreak prompts by analyzing output confidences. Specifically, it observes that the output confidence for the first token is generally higher for benign inputs compared to malicious ones. By establishing a threshold based on this observation, the authors propose a method to distinguish between jailbreak attacks and benign inputs. To enhance detection capabilities, they introduce manual instructions and temperature scaling techniques designed to amplify the confidence difference between benign and malicious inputs, thereby improving detection efficiency.

### Strengths
* Timely and Relevant Topic: The paper addresses a critical issue in the field of AI security—jailbreak detection—highlighting the gap in defense mechanisms despite numerous studies on jailbreak attacks.
* Innovative Findings: The research presents an intriguing discovery that could lead to a more effective jailbreak detection algorithm.

### Weaknesses
The proposed method lacks clarity in several areas:
* Is the detection focused on identifying all malicious attempts (including those that do not result in harmful outputs) or solely those leading to harmful outputs?
* How was Figure 1 generated? Specifically, how many instances were used as benign prompts, and are these representative of the broader benign sample? What dataset was utilized?
* The design of the manual instructions is unclear. How do these instructions increase the confidence of benign inputs without impacting malicious inputs? The paper mentions contradictory manual instructions, but it is unclear why these would improve detection performance.
* Why does temperature scaling effectively increase the distinction between benign and malicious inputs? As noted in line 58, some LLM models may exhibit overconfidence for both jailbreak and benign prompts. If this is true, temperature scaling might lower outputs for both categories, which means it cannot help in differentiation. The paper does not provide a theoretical explanation for this observation.
* The FJD-LI model, trained on a limited number of samples, may struggle to generalize across other attacks and benign inputs. The paper does not provide sufficient analysis of the model's robustness to unseen attacks.
* What does it mean to "To align benign prompts with jailbreak prompts, we exclude pertinent prompts from the benign dataset" by excluding pertinent prompts from the benign dataset? This statement is vague and lacks a clear explanation.
* Why was PureDove selected as the benign dataset? Given that LLM performance is typically evaluated across diverse datasets, assessing benign performance on a wider range of clean datasets is crucial for ensuring minimal impact on detection algorithms. The paper does not justify this choice.
* The evaluation only includes three types of attacks, which is insufficient given the plethora of state-of-the-art attacks available (a quick search will reveal many more). The limited evaluation scope raises concerns about the generalizability of the proposed method.
* Intuitively, one would expect significant perplexity differences between Cipher attack inputs and normal inputs. However, results in Table 2 suggest that perplexity is ineffective for attack detection, casting doubt on these findings.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce a Free Jailbreak Detection (FJD) method by incorporating an instruction into the input prompt. This makes the logits distribution of the first token in the LLM's output distinct in both harmful and harmless dimensions, and the difference is amplified using temperature scaling. In order to make the distribution of logits of the first token more separable, the authors also used virtual instruction learning to expand the difference in distribution. Experiments on aligned large models demonstrated the effectiveness of the proposed FJD in jailbreak detection accuracy.

### Strengths
1. Detecting jailbreaks in LLMs is a critical issue, especially for the defense against such attacks.
2. The author proposes to use the logits distribution of the first token output by LLM to detect jailbreaks, which sounds like a relatively novel idea. 
3. The author proposes to use temperature scaling to amplify the logits distribution of harmful and harmless instructions of LLM by connecting the input with the instruction. Experiments are conducted to validate the effectiveness of this method.

### Weaknesses
1. The paper lacks sufficient experiments on the author's choice of threshold and temperature for jailbreak detection, that is, how much training data is needed to obtain a reasonable threshold and temperature parameter. Authors are suggested to include an experiment analyzing the detection performance with varying amounts of training data.
2. For virtual instruction learning, the authors did not provide an explanation regarding the transferability of the detection method when applied to a jailbreak dataset generated by a new jailbreak method. It is recommended for the authors to conduct such transferability experiment.
3. The proposed detection method requires the determination of the temperature parameters and thresholds. Faced with an unknown jailbreak dataset or jailbreak method, how can appropriate parameter values be established? How to ensure the proposed method also remain effective against unknown jailbreak methods? Please clarify.
4. While virtual instruction learning is optimized for known datasets, how to ensure its generalization? The authors may conduct specific experiments demonstrating generalization, such as testing on out-of-distribution jailbreak attempts.
5. Due to the inherent difficulty in controlling the output of the LLM after adding instructions to the prompt, in order to get a correct response, the LLM should be queried at least twice: first to detect potential jailbreaks and subsequently to obtain the intended response. Why not utilize a classifier with much fewer parameters to detect jailbreaks after the LLM has produced its output? If the model parameter sizes are large (e.g., larger than 70B), the proposed detection method seems to incur a larger amount of computations. It is recommended for the authors to compare and discuss this alternative with the proposed method.

### Questions
1. The proposed detection method requires the determination of the temperature parameters and thresholds. Faced with an unknown jailbreak dataset or jailbreak method, how can appropriate parameter values be established? How to ensure the proposed method also remain effective against unknown jailbreak methods? Please clarify.
2. While virtual instruction learning is optimized for known datasets, how to ensure its generalization? The authors may conduct specific experiments demonstrating generalization, such as testing on out-of-distribution jailbreak attempts.
3. Due to the inherent difficulty in controlling the output of the LLM after adding instructions to the prompt, in order to get a correct response, the LLM should be queried at least twice: first to detect potential jailbreaks and subsequently to obtain the intended response. Why not utilize a classifier with much fewer parameters to detect jailbreaks after the LLM has produced its output? If the model parameter sizes are large (e.g., larger than 70B), the proposed detection method seems to incur a larger amount of computations. It is recommended for the authors to compare and discuss this alternative with the proposed method.

### Soundness
2

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
4

### Summary
The work focuses on the research problem of detecting Jailbreak prompts. They present the finding of output distribution difference between jailbreak and benign prompts and use this finding to detect jailbreak prompts. Extensive experiments on 8 models are conducted under both jailbreak attacks with competing objectives and mismatched generalization.

### Strengths
- The finding is interesting and reasonable.
- The result is promising.
- The overall presentation of the model and the results is clear.

### Weaknesses
 - The paradigm of adding manual instruction and scrutinizing the difference of the first token is similar to the work [1], which also focuses on detecting jailbreak prompts. It would make the work more comprehensive to discuss the differences and compare the performance.
- It would also be helpful to compare with moderation APIs and [2]. Although they were designed for general unsafe prompt detection, but would also lead to a good comparison. 
- Overall. as SmoothLLM & PPL are kind of designed for GCG-like not readable jailbreak, comparing with them alone may compromise the experimental comprehensiveness.

### Questions
See weakness.
I think the overall finding is interesting and cool, I would raise the score if the evaluation can be improved.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigated how to detect jailbreak prompts. They found that LLMs allocate significantly more attention to the first few tokens of jailbreak prompts compared to benign ones. Therefore, they suggested measuring the attention given to the initial tokens of a prompt as a jailbreak indicator. Additionally, they proposed using handcrafted prompts and temperature scaling to improve detection performance. The handcrafted prompts could also be improved through virtual instruction learning.

### Strengths
* The paper is well-written and easy to follow.

* Jailbreak attacks are a critical research topic in LLMs, particularly regarding defenses against such attacks.

* The authors conducted many experiments to validate the performance of their method.

### Weaknesses
 * Some of the claims in the paper lack rigor. For example, in line 161, the authors presented experiments using two types of attacks on the Llama2 7B model to back their findings. However, results derived from just one model do not adequately demonstrate the generalizability of their conclusions.

* The attack methods used in this paper focus on optimizing a jailbreak suffix to generate jailbreak prompts. If jailbreak words are distributed across different positions in the input, would the authors' finding still hold? The authors should evaluate their method against attack strategies that do not solely rely on optimizing jailbreak suffixes [1, 2].

* My major concern lies in the robustness of the proposed detection method against adaptive attacks.

* In line 246, the authors mention conducting a theoretical analysis; however, I could not find the relevant results.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
