# One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs

- Decision: Accept
- Scores: 8, 5, 8

## Abstract
Safety alignment in large language models (LLMs) is increasingly compromised by jailbreak attacks, which can manipulate these models to generate harmful or unintended content. Investigating these attacks is crucial for uncovering model vulnerabilities. However, many existing jailbreak strategies fail to keep pace with the rapid development of defense mechanisms, such as defensive suffixes, rendering them ineffective against defended models. To tackle this issue, we introduce a novel attack method called ArrAttack, specifically designed to target defended LLMs. ArrAttack automatically generates robust jailbreak prompts capable of bypassing various defense measures. This capability is supported by a universal robustness judgment model that, once trained, can perform robustness evaluation for any target model with a wide variety of defenses. By leveraging this model, we can rapidly develop a robust jailbreak prompt generator that efficiently converts malicious input prompts into effective attacks. Extensive evaluations reveal that ArrAttack significantly outperforms existing attack strategies, demonstrating strong transferability across both white-box and black-box models, including GPT-4 and Claude-3. Our work bridges the gap between jailbreak attacks and defenses, providing a fresh perspective on generating robust jailbreak prompts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper propose an automatic attack framework (ArrAttack) for generating robust jailbreak prompts designed to bypass defenses in LLMs. The authors propose two main components: a rewriting-based prompt generation technique and a robustness judgment model. 

ArrAttack first uses an undefended LLM to generate jailbreak prompts. These prompts are then evaluated using a robustness judgment model trained to assess their resistance to defenses. The final model combines both components to generate highly effective jailbreak prompts that perform well against multiple defence methods. Through extensive experimentation, the authors show that ArrAttack achieves higher success rates and transferability compared to other baseline approaches across various LLMs and defense mechanisms.

### Strengths
1. This paper notices the limitations of existing jailbreak attacks on defended LLMs and presents a unique approach to jailbreak prompt generation by combining a robustness judgment model with a rewriting-based generation technique.

2. The paper is well-structured, with a clear problem formulation and a detailed description of the proposed methods.

3. The experiments are comprehensive, evaluating multiple models with diverse architectures and defense mechanisms. The authors employ various evaluation metrics, including attack success rate, semantic similarity, and perplexity, which adds depth to the assessment.

### Weaknesses
1. The authors focus on jailbreak attacks in defense scenarios. However, this has not been thoroughly validated across all defense types, which may limit generalizability. The defense methods tested in the paper are all system-level, focusing on input-level defenses. The authors could strengthen the study by including model-level defense mechanisms, such as unlearning [1] and adversarial fine-tuning.

2. The authors should provide more detailed case studies for the robustness judgment model and prompt generation model, particularly with samples of generated prompts in defended scenarios.

3. From the ablation studies in Tables 4 and 5, it is evident that the robustness judgment model and prompt generation model are the most critical components. Therefore, the authors should delve further into optimizing these models. In Sections 3.3 and 3.4, the training parameters are briefly mentioned, but the authors provide little detail on the training methods and rationale behind parameter choices that contribute to model quality.

### Questions
1. In Section 3.3, the robustness judgment model is trained with a single defense mechanism (SmoothLLM). Why was this particular defense chosen? How does it ensure transferability across different defenses and models?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel jailbreak attack method, ArrAttack, aimed at circumventing defenses in large language models (LLMs). ArrAttack leverages a rewriting-based attack mechanism and a robustness judgment model to generate robust jailbreak prompts, capable of defeating various defense strategies. Experimental results suggest that ArrAttack exhibits strong transferability and success across multiple defenses, including GPT-4 and Claude-3.

### Strengths
1.	The paper presents a new approach by integrating a robustness judgment model with the generation of jailbreak prompts, enhancing both the efficiency and robustness of attacks. However, similar concepts have already been proposed, such as PAIR[1] and TAP[2], which utilize LLMs to iteratively rewrite adversarial prompts to achieve a high ASR.
2.	The paper is generally well-structured, providing clear explanations of the proposed method, its components, and the evaluation criteria.

[1] Jailbreaking Black Box Large Language Models in Twenty Queries
[2] Tree of Attacks: Jailbreaking Black-Box LLMs Automatically

### Weaknesses
1.	While ArrAttack improves robustness, the core attack methodology—particularly the rewriting-based approach—is not entirely new, as similar strategies have been explored in previous works like PAIR and TAP. The paper does not sufficiently differentiate its approach from these methods in terms of the specific rewriting techniques used or the underlying mechanisms that lead to successful jailbreaks. The novelty of the approach is therefore questionable, as it seems to be an incremental improvement rather than a fundamental shift in methodology.
2.	The focus on defense-enhanced LLMs is limited by incomplete experimentation. Several key model-level defenses, such as safety training and unlearning, have not been thoroughly examined. The paper lacks a comprehensive evaluation of how ArrAttack performs against models that have undergone specific safety training or unlearning procedures, which are crucial for assessing the practical robustness of the attack.
3.	The paper lacks comparison with similar baselines, such as PAIR and TAP, making it difficult to fully assess the attack performance of ArrAttack. Without a direct comparison, it is unclear whether the improved robustness is due to the specific design of ArrAttack or simply a result of using a different evaluation setup. A rigorous comparison is needed to establish the true contribution of the proposed method.
4.	The use of GPTFuzz’model, as an evaluation metric is questionable due to its inherent bias and limited generalizability in complex scenarios. The reliance on a single evaluation metric, especially one that is not widely accepted, makes it difficult to validate the results. The paper should consider using more robust and diverse evaluation metrics to ensure the reliability of the findings.

### Questions
1.	Can the robustness judgment model be fine-tuned or adapted for use in other languages or LLMs trained on non-English datasets? If so, what modifications would be required?
2.	How would ArrAttack perform against real-time defense mechanisms that evolve based on user feedback or system updates?

### Soundness
3

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
4

### Summary
In this paper, the authors propose ArrAttack, a brand-new attack to jailbreak the defended LLMs. Two steps are included. Firstly, it trains a universal robustness judgement model. Then, this model serves as a filter to select powerful prompts for generation model training.

### Strengths
1 The soundness of this paper is good.

2 In Table 1, the results indicate that ArrAttack can not only achieve high ASR, but also obtains PPL score.

3 The transferability of jailbreak prompts generated by ArrAttacks is good.

### Weaknesses
1 I think the writing of this paper is not satisfying, especially the method and the experimental section. To be honest, I think ArrAttack itself is not so hard to understand. But I indeed try hard to follow the writers' chain of thought. In Section 3, the authors should introduce how ArrAttack is motivated and how the pipeline of ArrAttack works rather than the detailed settings of the hyperparameters. In Section 4, instead of combining all results into a huge subsection "RESULTS", you should divide them part by part to make it clearer to readers.

2 ArrAttack requires to train a generation model, which needs additional computational cost. In PAIR [1] and TAP [2], they propose to craft the jailbreak prompts with GPT-4, which makes them more flexible and adptive to various defenses. However, unfortunenately, I do not see the comparison with those methods. Further experiments are needed to demonstrate ArrAttacks' outstanding performances compared to previous works.

3 ArrAttack needs a large amount of training data compared to those of existing attacks, such as AutoDAN (zero-shot). In contrast, ArrAttack combines three datasets to perform attacks. As far as I know, the diversity of the training set is a key factor to the generalizable of the methods. Thus, more ablation studies should be performed when the training data are limited.

4 The settings for evaluation is rare. Actually there are a lot of benchmarks such as harmbench that evaluate the performances of jailbreak attacks on various LLMs. Comparing with previous attack methods on existing benchmarks not only makes the effectiveness of the method more intuitive but also enhances the impact of the work.

### Questions
1 Although bypassing SMP, DPP, RPO and PAR are much appreciated, how about evading more stronger defenses, such as [3-5]?

2 In the experimental setups section, the authors propose to evaluate the ASR with the "GPTFuzz" model. Much more details are needed to provide in the Appendix to see how it works because the ASR metric is sensitive to various settings. 

[1] Jailbreaking black box large language models in twenty queries

[2] Tree of attacks: Jailbreaking black-box llms automatically

[3] Safedecoding: Defending against jailbreak attacks via safety-aware decoding

[4] Fight back against jailbreaking via prompt adversarial tuning

[5] RAIN: Your Language Models Can Align Themselves without Finetuning

### Soundness
3

### Presentation
2

### Contribution
2
