# Evading Data Contamination Detection for Language Models is (too) Easy

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Large language models (LLMs) are widespread, with their performance on benchmarks frequently guiding user preferences for one model over another. However, the vast amount of data these models are trained on can inadvertently lead to contamination with public benchmarks, thus compromising performance measurements. While recently developed contamination detection methods try to address this issue, they overlook the possibility of deliberate contamination by malicious model providers aiming to evade detection. We argue that this setting is of crucial importance as it casts doubt on the reliability of public benchmarks for LLM evaluation. To more rigorously study this issue, we propose a categorization of both model providers and contamination detection methods. This reveals vulnerabilities in existing methods – we demonstrate how to exploit these with \emph{Evasive Augmentation Learning} (EAL), a simple yet effective contamination technique that significantly inflates benchmark performance while completely evading current detection methods.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the data contamination problem with an analysis of existing frameworks. The paper categorizes existing frameworks in 4 categories and reveals their weaknesses by a detailed study. The paper proposes a new attack strategy based on the analysis and observation.

### Strengths
1. The analysis of existing methods is reaonsable. The paper starts the discussion on categorizing existing paper with a figure and the categorization is reasonable. 
2. The selection of base models and benchmarks is representative and comprehensive.

### Weaknesses
The paper lacks novelty and technical depth, and the presentation of the paper is hard-to-follow. 
1. The paper mainly studies the existing methods, however, it lacks a detailed discussion on the proposed attack strategy and the reasonableness of such a strategy. As a reader, I cannot fully understand the main design of the strategy proposed after the analysis (In Sec 5.1 I suppose). It's hard to understand the method with a short paragraph and the paper lacks a formulation or figure for the strategy. 2. The experiments just focus on evaluating existing methods and it's hard to identify the section proving the effectiveness of the proposed strategy. The experimental design doesn't the support the claim of the paper and lacks crucial experimental results. 
3. The organization of the paper is dispersive with no key idea. The presentation is not coherent. After discussing the experiment results, the paper switched to a discussion on section 7, but such a discussion is not related to the experiment results presented before. This section sounds like a "related work" section.

### Questions
Please refer to the weakness part about the paper structure, technical depth, and novelty.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper looks into the vulnerabilities and reliabilities of current data contamination detection methods. The authors categorize model providers based on their contamination practices, emphasizing malicious actors could intentionally contaminate models by rephrasing the benchmark data, thus evading detection while boosting model scores. Through experiments across several models and benchmarks, the authors show that the rephrasing technique could increase performance while bypassing existing detection methods.

### Strengths
- The paper introduces a novel categorization of model providers based on their data contamination practices.
- Provide a simple yet effective contamination technique to evade detection, highlighting limitations in current detection methods.
- The paper is well-organized, with each section building on the previous one. Key concepts like contamination types and detection vulnerabilities are presented accessibly, making the research easy to understand and follow.

### Weaknesses
The paper demonstrates the vulnerability of current detection methods to rephrasing attacks but does not explore potential defenses. Without suggestions for addressing this vulnerability, the work may feel incomplete.

### Questions
- Is the performance across different benchmarks consistent? Could you provide a more detailed breakdown of per-benchmark performance?
- The paper notes that the limited sample size of the contaminated set contributes to increased variance in results. Would it be feasible to increase the sample size of the contaminated dataset to reduce this variance and enhance result stability?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a examination of the vulnerabilities in current benchmarking practices for LLMs. They introduce Evasive Augmentation Learning (EAL), a technique that rephrases benchmark samples to boost performance on benchmarks and evade current detection methods.

### Strengths
- Method is simple and easy to understand.
- The topic is highly relevant to the current challenges in assessing the performance of large language models.

### Weaknesses
 - Unclear definition on "Definition 3"
- The distinguish between openly malicious and evasively malicious is somewhat problematic. It's hard to find realistic usage when applying the open malicious scenario to any of the attackers. Openly malicious is easily getting rid of by the other detection method listed.
- Sections 4 and 5 would benefit from streamlining. There is some repetition and unnecessary content that could be condensed to improve clarity and conciseness.
- Although the paper states that code is provided, it does not include detailed descriptions of the processes for data rephrasing and contamination insertion, particularly regarding how rephrased data is generated.
- The authors overclaimed the contribution. Failure to consider the technical feasibility and applicability of updating baseline data in real-world applications, resulting in proposed attack methods that are more suitable for closed environments and may not work in open and real-time updating environments

### Questions
- Does the EAL technique circumvent all detection methods mentioned in A Taxonomy for Data Contamination in Large Language Models, including those that do not require pre-training data?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work aims to propose an evasive attack to bypass potential detection. The author first summarizes existing attacks, while studying potential detection strategies using metadata, reference models, semantic-preserving transformations, and different accessibility. Then, the author proposed that rephrasing can help to increase evasiveness.

### Strengths
+ This work studies a valid topic -- detecting more evasive attack to endanger LLM safety.
+ This work summarizes many attacks and detection efforts.

### Weaknesses
 - Many settings are unclear: (1) For "contamination," there is no definition of the threat model regarding its knowledge, capabilities, or concrete examples in text-based attacks. Specifically, it's unclear what level of access the "actor" has to the training data, whether they can modify it directly, or if they are limited to injecting new data. The paper also lacks a discussion on the scale of contamination, i.e., the percentage of training data that is contaminated. (2) It is also unclear how the attacker influences benchmarks, what the adversarial samples look like, and what the adversarial objectives are. For example, are the adversarial samples designed to cause specific errors or just to increase performance on the benchmark? (3) Furthermore, defense settings are also unclear about the role of detector/defender and what actions can the defender take to eliminate poisoning? The author is suggested to add those information about both threat model and defender's strategies.

- The paper uses overly complicated wording, which creates barriers to understanding. Specifically: (1) "Contamination" is typically used as "poisoning." (2) The "actor" is generally referred to as "attacker" or "adversary." The "actor" typically links to specific roles (such as specific cyber threat patterns). (3) "De-Contamination" is rarely used. An alternative term is "mitigation." (4) "verbatim" could be "word-wise." (5) "Sample-level" could be more accurately expressed as "sentence (or word, token)-level." (6) It is inaccurate to use "Problematic Data Contamination" in Definition 3, as that definition is talking about possibility of injecting poisoning data D'.

- The author did not clearly explain why pre-training requires benchmarking data. The author probably means "public" or "crowdsourced" data.

- The paper over-claimed the contribution "We define four (de-)contamination settings..." where the settings are summarized, not defined in this paper.

- The role of model providers is unclear. In section 3, model providers are both attacker and defender. The author is suggested to distinguish model providers with adversaries (the "actor").

- The paper has poor structure and incomplete content: (1) There is no related work section. (2) The author did not detail the proposed rephrasing attack, such as what prompts or techniques are used for rephrasing. (3) Definition 4 simply repeats definition 1 and 2. (4) The Definition 5 should be highlighted with rigorous formulation with later technical design addressing it. (5) It would be better to introduce "TPR" (true positive rate) and "FPR" (false positive rate) in Figure 1.

- The contribution is not significant. The author simply uses "rephrasing," which lacks strong intuition and motivation for its usefulness.

- The experiments are simple, and the settings are problematic. Specifically: (1) the author mentions several detection strategies but does not provide corresponding experiments to address those detections. (2) The paper also fails to clarify how evasiveness is guaranteed -- Is it measured by lower TPR by detection methods? (3) No baseline attacks. (4) The author is suggested to discuss the trade-off between attack effectiveness and evasiveness.

- Many sentences seem GPT-generated. It is fine to use GPT to polish writing. However, the original writing maybe logically inconsistent and unclear, so GPT alone cannot produce better logic.

### Questions
Please see the comments above.

### Soundness
2

### Presentation
1

### Contribution
2
