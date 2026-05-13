# Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Model editing methods modify specific behaviors of Large Language Models by altering a small, targeted set of network weights and require very little data and compute. These methods can be used for malicious applications such as inserting misinformation or simple trojans that result in adversary-specified behaviors when a trigger word is present. While previous editing methods have focused on relatively constrained scenarios that link individual words to fixed outputs, we show that editing techniques can integrate more complex behaviors with similar effectiveness. We develop Concept-ROT, a model editing-based method that efficiently inserts trojans which not only exhibit complex output behaviors, but also trigger on high-level concepts -- presenting an entirely new class of trojan attacks. Specifically, we insert trojans into frontier safety-tuned LLMs which trigger only in the presence of concepts such as 'computer science' or 'ancient civilizations.' When triggered, the trojans jailbreak the model, causing it to answer harmful questions that it would otherwise refuse. Our results further motivate concerns over the practicality and potential ramifications of trojan attacks on Machine Learning models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a concept-level poisoning method called Concept-ROT, which use concept editing methods for model poisoning. The attacker can manipulate high-level concepts and trigger specific "backdoors" in the poisoned model for malicious purposes, such as rejecting to answer benign questions and jailbreak the safety alignment of pretrained language models. The method is to first isolate the desired concept, and then extract the concept activations & vectors from the model, and then use ROME to edit the model weights. Experiments are conducted using synthetic datasets, showing the methods' superiority compared to Fine-tuning and LoRA.

### Strengths
- This paper studies a relavant and highly improtant problem, i.e., poisoning LLMs using concept editing techniques.
- The logic of this paper is easy to follow.
- The proposed method is intuitive and sound.
- The application on poisoning for jailbreaking is quite interesting.

### Weaknesses
 - It is difficult to perceive significant novelty from this paper. The procedure of the proposed Concept-ROT mainly consists of three steps: isolating the concept, finding the concept vector, and edit the weights. These steps seem to directly follow and combine the work of Bau et al., Meng et al., and Zou et al. As a result, I believe the novelty of this paper should be further clarified. Specifically, the paper does not articulate how the combination of these existing techniques leads to a fundamentally new capability or insight beyond what is already achievable by applying these methods individually or in sequence. The method appears to be a straightforward application of existing techniques, lacking a novel technical contribution in its methodology.

- This paper do not compare the proposed Concept-ROT with previous methods that uses concept editing methods (e.g., BadEdit). As concept editing is known to be more time-efficient and has comparable performances to Fine-tuning on concept manipulation, the results presented in the paper and comparisons with FT and LoRA does not seem unexpected. Comparisons with more recent and relevant baselines would enhance the clarity and superiority of this paper. The absence of a comparison with BadEdit, which also leverages model editing for backdoor injection, is a significant oversight. The paper should provide a clear justification for not including this comparison, especially given that BadEdit is a relevant baseline for model editing-based trojaning.

### Questions
- What is the biggest difference and novelty of Concept-ROT compared with previous methods that utilize concept-editing methods for backdoor attacks (e.g., BadEdit)?

- Could the authors elaborate on the specific real-world scenarios that Concept-ROT can pose severe harm?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to edit an LLM so that it behaves normally in most cases, but could be easily jailbroken when a specified concept presents. It uses model editing (ROME) and representation engineering for trigger implanting. Specifically, it first elicits a target concept vector by a dataset by representation engineering, then edits an associated key in the MLP to link it with adversarial outputs. The results indicate the model is easily jailbroken when there is a trojan, but maintains the same level of utility under normal use cases.

### Strengths
1. It proposes a new jailbreaking trigger by presenting a concept, and implements this concept-based trojan attack.

2. Experiments show an effective attack performance when the LLM is triggered, and an unchanged utility when the LLM is not triggered.

3. The attack has high computation-efficiency and controllability. The injection is done very efficiently within seconds.

### Weaknesses
1. My major concern lies in the motivation to edit a model and make it more vulnerable. Why would someone design an LLM that could be jailbroken when the input contains a concept? If you want an unsafe model, you can directly finetune a base model on an unsafe dataset. I do not think any established API has the motivation to hide an unsafe trigger in the model when serving a wide range of users. Thus, it is not clear what harm would be caused by the proposed method, which I admit is an improvement in this research direction of attack.

2. The authors highlight the computation advantage. See Line 300: “Prior work has taken 100,000 samples” and “We find that the task performance using between 100 and 1,000 samples is generally indistinguishable from the performance using 100,000 samples”. It is not clear if (1) the authors discover the prior ROME actually does not need that much computation (2) the authors contribute some techniques to make it efficient in the jailbreak setting.

### Questions
See weaknesses.

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
This paper applies ROT, a model-editing approach, to a Trojan task by using specific sequences as triggers to elicit harmful responses from large language models (LLMs). Additionally, it introduces Concept-ROT, a novel variant that uses concepts or model behaviors as triggers. The results demonstrate that ROT can implant Trojans with improved effectiveness and stealth.

### Strengths
1. This paper is the first to apply ROT to Trojan tasks in LLMs.
2. It introduces novel triggers based on concepts and model behaviors.
3. The experiments are thorough and produce convincing results.

### Weaknesses
 - The method lacks novelty. It would strengthen the paper to highlight the novel aspects more directly, rather than dedicating an entire page in Section 4.1 to prior work. Sections 4.2.1 and 4.2.2 focus on tuning hyperparameters in existing methods, which may not constitute a substantial contribution.
- Important evidence is missing for some claims. Line 194 introduces an assumption. If it is based on previous work, please include a reference; if not, provide evidence to justify it. Clarifying why this assumption is made would be helpful, as the paper doesn’t address multiple concepts within a single sentence.
- Some settings are unconvincing. Consider discussing potential applications that would benefit from the proposed methods.
- Writing inconsistencies. Standardize terminology across the paper, as some sections use "figure" while others use "Fig."
- Good observations are made, but lack explanation. The paper highlights interesting observations, such as those in Figure 2 and the increased difficulty in optimizing longer targets. However, further explanation or exploration of these observations would enhance understanding.

### Questions
- Could you give some evidences about the assumption that the activations k can be roughly broken down into a linear combination of vectors representing various concepts or pieces of information.
- Could you discuss some potential applications, where using concept as trigger is better than using traditional triggers.
- Could you give some explanation about the observation in Figure 2 and the increased difficulty in optimizing longer targets.

### Soundness
3

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
This paper proposes a novel and effective concept backdoor attack using an efficient model editing injection approach. The core idea is to leverage concept-based triggers rather than specific token triggers, making the attack more versatile and challenging to detect. The authors demonstrate the feasibility of this approach using Concept-ROT, a method that injects trojans by modifying model weights to associate high-level concepts with adversarial behaviors.
The evaluation results show that the proposed attack achieves high success rates.

### Strengths
(1) The concept-based backdoor attack is novel, and the use of an efficient model editing technique provides a low-cost and flexible injection method.

(2) The paper is well-written and easy to follow.

(3) Extensive evaluation results demonstrate the effectiveness of the proposed attack.

### Weaknesses
 (1) The concept trigger’s effectiveness seems dependent on the degree of overlap between the target concept and the benign distribution, which may limit applicability across concepts.

(2) Some evaluation details are missing or insufficiently detailed.

(3) The paper lacks a discussion of potential defenses or mitigation strategies against the attack.

### Questions
This paper presents an interesting concept backdoor attack using efficient model editing. However, I have some questions regarding the practicality and evaluation of the proposed method.

(1) The success of the concept trigger appears to depend on the extent of overlap between the target concept and the benign distribution. For instance, as shown in Figure 3, if there is high overlap between target and control distributions, either ASR or benign performance may be impacted. This dependency seems to limit the attack’s applicability to certain concepts. For example, Figure 17 suggests that the "computer science" concept may be more suitable, while "sculptures and paintings" may not perform as well, potentially due to concept frequency or distinctiveness. I suggest discussing how effective the attack is across various concepts and summarizing which types of concepts are most suitable.

(2) The paper lacks some important evaluation details. For example, in the jailbreaking evaluation, the focus is primarily on fixed triggers rather than concept triggers. While Section 5.3 mentions concept-based jailbreaking, more concrete results, similar to those in Table 2, would clarify the effectiveness of concept triggers for this task. Additionally, it would be useful to know the ASR for non-target concept prompts to understand if these non-concept prompts can also mistakenly trigger the attack.

(3) There is no discussion of potential defenses against this attack. How might fine-tuning or other post-training interventions affect the model’s robustness against Concept-ROT? An exploration of these defensive strategies could help readers understand the robustness of the proposed attack.

### Soundness
3

### Presentation
3

### Contribution
3
