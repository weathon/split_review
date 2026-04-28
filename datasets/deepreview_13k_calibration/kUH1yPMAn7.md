# Safety Layers in Aligned Large Language Models: The Key to LLM Security

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Aligned LLMs are secure, capable of recognizing and refusing to answer malicious questions. However, the role of internal parameters in maintaining such security is not well understood yet, further these models can be vulnerable to security degradation when fine-tuned with non-malicious backdoor or normal data. To address these challenges, our work uncovers the mechanism behind security in aligned LLMs at the parameter level, identifying a small set of contiguous layers in the middle of the model that are crucial for distinguishing malicious queries from normal ones, referred to as ``safety layers". We first confirm the existence of these safety layers by analyzing variations in input vectors within the model's internal layers. Additionally, we leverage the over-rejection phenomenon and parameters scaling analysis to precisely locate the safety layers. Building on these findings, we propose a novel fine-tuning approach, Safely Partial-Parameter Fine-Tuning (SPPFT), that fixes the gradient of the safety layers during fine-tuning to address the security degradation. Our experiments demonstrate that the proposed approach can significantly preserve LLM security while maintaining performance and reducing computational resources compared to full fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper identifies specific "safety layers" within language models that play a critical role in differentiating between malicious and normal queries. These safety layers display noticeable distributional discrepancies between benign and adversarial queries, providing an insight into potential defense mechanisms. Leveraging this finding, the authors propose a fine-tuning approach called Safely Partial-Parameter Fine-Tuning (SPPT) to enhance model resilience against certain threats.

### Strengths
- The identification of a specific set of middle layers in aligned LLMs as key to recognizing malicious inputs is an intriguing finding that provides a new perspective on model robustness.
- The paper presents clear and effective visualizations to support the findings.
- Experiments demonstrate the method’s efficacy.

### Weaknesses
 - The type of attacks addressed by the proposed method is unclear. While related work discusses jailbreak, the experiments primarily use backdoor datasets. The paper lacks a defined threat model and discussion of the defender's capabilities and objectives. Specifically, it is not clear whether the method is intended to defend against targeted attacks where an adversary crafts specific inputs to bypass safety layers, or more general robustness issues arising from fine-tuning on potentially unsafe data. The lack of a clear threat model makes it difficult to assess the practical relevance of the proposed approach.
- Since the method requires access to model parameters, it is not suitable for popular black-box LLMs, which limits its applicability. The paper does not adequately address the limitations of this white-box assumption. In particular, the method's reliance on identifying specific 'safety layers' within the model architecture raises questions about its generalizability across different model architectures and training regimes. The paper needs to discuss how the identification of these layers is performed and whether this process needs to be repeated for each new model.

### Questions
Please see weakness

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
The paper explores which layers in aligned large language models (LLMs) enable secure responses. The authors analyze the differences in output vectors across hidden layers, revealing the existence of specific "safety layers." Based on these findings, the authors introduce Safely Partial-Parameter Fine-Tuning (SPPFT), which selectively updates parameters outside the safety layers during fine-tuning. This approach preserves model alignment throughout the fine-tuning process without sacrificing performance.

### Strengths
- The authors provide an insightful perspective on analyzing LLM safety.
- The paper is clearly presented and well-structured.
- The proposed SPPFT approach is shown to be effective.

### Weaknesses
 - The conclusion lacks rigor; differences in vectors may be explained by distributional variations.
- The assumption that certain layers, rather than individual neurons within each layer, are related to safety requires more clarification.

### Questions
The authors compare vector similarity to demonstrate the existence of safety-related layers, but the conclusion is not entirely rigorous. Specifically, it is unclear whether the normal and malicious queries come from the same distribution. Since malicious queries tend to focus on more sensitive tasks while normal queries are often more routine, it is likely they follow different distributions. If these distributions differ, it could also explain why cosine similarity is less impacted for N-N and M-M pairs but drops significantly for N-M pairs.

While I appreciate the authors' efforts to demonstrate the presence of layers closely related to safety, I would like to understand why they treat each layer as a whole. From my perspective, it is reasonable to consider that each layer may contain both safety-related and non-safety-related neurons. In other words, rather than one specific layer focusing mainly on safety, it could be that all layers contribute to safety, with varying numbers of neurons engaged in the process.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a defense against the backdoor attack for LLMs. The idea is to i)identify the safety layers, ii) fix the safety layers during fine-tuning.

### Strengths
1. Extensive analysis is made to jusify the existence of safety layers.
2. Defense solution is very simple. 
3. Paper is well written and easy to read.

### Weaknesses
 * The defense can only be applied to backdoor attack, making its application very narrow. It is unkonwn whether the method can be extended general harmful fine-tuning attack sceanrios (in which a percentage of the harmful data (with no trigger in the question) is mixed in the fine-tuning process), I guess the answer is yes, but the authors should demonstrate this with experiments. Moreover, I personally don't think the backdoor attack for safety unalignment very reasonable (see my question).

Rosati D, Wehner J, Williams K, et al. Representation noising effectively prevents harmful fine-tuning on LLMs[J]. arXiv preprint arXiv:2405.14577, 2024.

*  Baselines can be more comprehensive. Both FullFT and NFFT are not effective defenses  towards the fine-tuning risk (NFFT is a failed attempt as indicated by (Wei et al, 2024)) . The authors should consider to compare with Lisa (Huang et al, 2024), which is also a fine-tuning stage defense that modify the fine-tuning process, with source code avaialble, and also appeared several months before the ICLR2025 review cycle.

Huang T, Hu S, Ilhan F, et al. Lazy Safety Alignment for Large Language Models against Harmful Fine-tuning[J]. arXiv preprint arXiv:2405.18641, 2024.

* Literature review is not comprehensive. Since (Qi et al,2023) demonsrates the fine-tuning risk, there are a large amount of defenses coming out trying to solve the issue. I list these papers in the following:

---Alignment stage solution---

[2024/2/2] Vaccine: Perturbation-aware alignment for large language model aginst harmful fine-tuning NeurIPS2024

[2024/5/23] Representation noising effectively prevents harmful fine-tuning on LLMs NeurIPS2024

[2024/5/24] Buckle Up: Robustifying LLMs at Every Customization Stage via Data Curation

[2024/8/1] Tamper-Resistant Safeguards for Open-Weight LLMs

---Fine-tuning stage solution---

[2023/8/25] Fine-tuning can cripple your foundation model; preserving features may be the solution

[2023/9/14] Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions ICLR2024

[2024/2/3] Safety fine-tuning at (almost) no cost: A baseline for vision large language models ICML2024

[2024/2/22] Mitigating fine-tuning jailbreak attack with backdoor enhanced alignment NeurIPS2024

[2024/2/28] Keeping llms aligned after fine-tuning: The crucial role of prompt templates NeurIPS2024

[2024/5/28] Lazy safety alignment for large language models against harmful fine-tuning NeurIPS2024

[2024/6/10] Safety alignment should be made more than just a few tokens deep 

[2024/6/12] Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models

[2024/8/27] Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models

---Post-fine-tuning stage solution---

[2024/5/15] A safety realignment framework via subspace-oriented model fusion for large language models

[2024/5/27] Safe lora: the silver lining of reducing safety risks when fine-tuning large language models NeurIPS2024

[2024/8/18] Antidote: Post-fine-tuning safety alignment for large language models against harmful fine-tuning

[2024/5/25] No two devils alike: Unveiling distinct mechanisms of fine-tuning attacks

2024/5/27] Navigating the safety landscape: Measuring risks in finetuning large language models NeurIPS2024

-------------Below is concurrent works (or after you)-----------

[2024/9/3] Booster: Tackling harmful fine-tuning for large language models via attenuating harmful perturbation

[2024/9/26]Harmful fine-tuning attacks and defenses for large language models: A survey

[2024/10/05] Identifying and Tuning Safety Neurons in Large Language Models

[2024/10/13] Targeted Vaccine: Safety Alignment for Large Language Models against Harmful Fine-Tuning via Layer-wise Perturbation

[2024/10/05] SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection

[2024/10/05] SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation 

[2024/10/05] Safety Alignment Shouldn't Be Complicated

[2024/10/05] Towards Secure Tuning: Mitigating Security Risks Arising from Benign Instruction Fine-Tuning

[2024/10/05] Locking Down the Finetuned LLMs Safety

[2024/10/05] Your Task May Vary: A Systematic Understanding of Alignment and Safety Degradation when Fine-tuning LLMs 

[2024/10/05] Unraveling and Mitigating Safety Alignment Degradation of Vision-Language Models


I am aware that some of these works are concurrent submission to ICLR2025. However, the authors should at least cite those relevant research before your first submission,  It is also encouraged to cite and disucss those concurrent works because that will be beneficial for the developement of the field.

### Questions
* Are you considering an opensource model fine-tuning scenario (Rosati et al,2024) or a fine-tuning-as-a-service scenario (Qi et al, 2023)？

I think you are probably considering the latter one, as for the first scenario you can't assume that the defender has control over the fine-tuning process, but this should be made clear. Also, for the first scenario, it does not make much sense because there is no reason that the attacker want to backdoor his own model.  

Rosati D, Wehner J, Williams K, et al. Representation noising effectively prevents harmful fine-tuning on LLMs[J]. arXiv preprint arXiv:2405.14577, 2024.

* In the fine-tuning-as-a-service scenario, why you consider a backdoor attack scenario?  What is the motivation for the attacker to unalign the model? There are only one motivation I can envision:

**Adversary case.** The attackers upload backdoor data to unalign the model, and in depoyment they query question with backdoor trigger to elicit the harmful answer of the fine-tuned model. The harmful answers are transmitted from service provider's (e.g., OpenAI's) API and then the attackers can use this as evidence to frame/sue the service provider. However, it does not make very much sense as well because from the user's question, it is very easy to spot that there is a trigger inside the question -- apparantly the attackers implant the trigger deliberately and want to frame the service provider. This is even more obvious if the fine-tuning data are also presented to the judge, as there are also the same triggers inside the fine-tuning data. By contrast, the normal harmful fine-tuning attack are more steathy and are reasonable.       

* What is the backdoor trigger you are using? Is it   "Servius Astrumando Harmoniastra" that Qi et al are using?   

Overall, I don't have much opinion of the technical aspect of this paper. However, I don't think the considered backdoor defense scenario is as realistic as the normal harmful fine-tuning attack scenario. I suggest the authors to follow the mainstream of research and position this paper to a defense towards general harmful fine-tuning attack (on either harmful data or benign data), but use backdoor attack as a special case in the experiment. I believe this should also make this paper more impactful and valuable.  I will actively pariticpate in the discussion, and will not disappear after I write this comment.  I will consider to increase my score if my concern is addressed.

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
4

### Summary
This paper focuses on preserving safety alignment during fine-tuning of aligned LLMs. The authors conduct a series of experiments to identify the existence of safety layers and localize them. Based on the found safety layers, they propose to fine-tune LLMs while freezing the safety layers. Experiments show that the proposed fine-tuning technique can preserve the safety alignment of LLMs during fine-tuning.

### Strengths
- The paper is well-structured with a good logic.
- The authors conduct sufficient experiments to show the existence of safety layers in aligned LLMs.
- Freezing the safety layers during fine-tuning ensures the safety and capability, as verified on a financial dataset.

### Weaknesses
 - It is confusing that the authors are focusing on a general issue of LLM fine-tuning while the experiments are conducted on a financial dataset. Experiments on general datasets such as alpaca and wild-chat are needed.
- Similarly, the chosen evaluation metrics are not appropriate. Training on instruction-tuning datasets and evaluating on instruction-following benchmarks (MT-Bench, AlpacaEval, ArenaHard) will be better.
- It is strange that the authors uses Alpaca prompt template for aligned LLMs such as Llama-3-8B-Instruct and Llama-2-7b-chat while these LLMs have their own default template.
- Missing references. [1] also shows that instruction tuning could compromise the safety alignment of open-access LLMs. Also, I am wondering if the proposed method is also applicable to defend against reverse DPO fine-tuning in [1].
- I do not really get the point of the analysis in Section 3.6. It seems like the safety layers behave similarly to preliminary layers. How did you get the conclusion in LIne 407-410.
- I am confused by the results in Table 1. For Phi-3-mini-4k-instruct the $\alpha$ is set to 0.8, which is less than 1; while for other LLMs, the $\alpha$s  are greater than 1. Besides, for Phi-3-mini-4k-instruct, the smallest number is chosen ulike others. What makes such difference and why?

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
