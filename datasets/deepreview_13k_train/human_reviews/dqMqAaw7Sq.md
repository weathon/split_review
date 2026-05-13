# Mitigating the Backdoor Effect for Multi-Task Model Merging via Safety-Aware Subspace

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Model merging has gained significant attention as a cost-effective approach to integrate multiple single-task fine-tuned models into a unified one that can perform well on multiple tasks. 
    However, existing model merging techniques primarily focus on resolving conflicts between task-specific models, they often overlook potential security threats, particularly the risk of backdoor attacks in the open-source model ecosystem.
    In this paper, we first investigate the vulnerabilities of existing model merging methods to backdoor attacks, identifying two critical challenges: backdoor succession and backdoor transfer. 
    To address these issues, we propose a novel \emph{Defense-Aware Merging (DAM)} approach that simultaneously mitigates task interference and backdoor vulnerabilities. Specifically, DAM employs a meta-learning-based optimization method with dual masks to identify a shared and safety-aware subspace for model merging.
    These masks are alternately optimized: the Task-Shared mask identifies common beneficial parameters across tasks, aiming to preserve task-specific knowledge while reducing interference, while the Backdoor-Detection mask isolates potentially harmful parameters to neutralize security threats. This dual-mask design allows us to carefully balance the preservation of useful knowledge and the removal of potential vulnerabilities.
   Compared to existing merging methods, DAM achieves a more favorable balance between performance and security, reducing the attack success rate by 2-10 percentage points while sacrificing only about 1\% in accuracy. Furthermore, DAM exhibits robust performance and broad applicability across various types of backdoor attacks and the number of compromised models involved in the merging process. We will release the codes and models soon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the poisoning of machine learning models in a merged model framework using backdoor attacks (the poisoned model infects the resulting merged model, or infects other clean models). It then proposes a method called DAM (Defense-Aware Merging) which identifies poisoned models and performs a 2-level optimization on both the accuracy (maximize) and attack success rate (minimize). 

Experiments are performed using the CLIP Vision Transformer for 6 image classification tasks. Extensive evaluation is done, compared against 3 types of baselines (individual finetuning [3 baselines], multi task merging [10 baselines], and post-defense methods [3 baselines]. Additional experiments are performed on specific framework settings (number of attacks, configuration of poisoned and clean models).

The DAM method is better at lowering the attack success rate than increasing / maintaining the accuracy. Overall, this is a useful paper on not only adding to the literature of vulnerability of multi-task machine learning models but also proposing a functional solution to defending against such an attack.

### Strengths
1. There is sufficient theoretical grounding of the proposed method including background (section 2) as well as providing proofs and mathematical explanations (section 3)
2. There is extensive empirical evaluation in multiple configurations and against multiple types of baselines which is very convincing
3. Additional experiments are included in the appendix which further demonstrate the DAM's robustness
4. The paper is well-written and code / data are provided for reproducibility

### Weaknesses
The paper seeks to optimize both accuracy and attack success rate and while the DAM is good at minimizing the ASR, it is not so good in maintaining or increasing the accuracy. (Nevertheless, sufficient explanation and reasoning is given to explain the results and the task is quite challenging). So not a weakness per se, merely an observation.

### Questions
1. Why is the related work section in the appendix, and not part of the main paper?
2. Perhaps a sentence or two defining the accuracy and attack success rate will help clarify the evaluation metric

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates the vulnerabilities of model merging methods when exposed to backdoor attacks. The paper identifies two primary challenges: 1) backdoor succession, where backdoors remain after merging and 2) backdoor transfer, where backdoors are transferred to clean models. Then the paper proposes Defense-Aware Merging (DAM) to mitigate both task interference and backdoor vulnerabilities. The DAM approach identifies a shared and safety-aware subspace for model merging and optimizing the task-shared mask and backdoor detection mask via bi-level optimization. The experimental results show the effectiveness of DAM in achieving high accuracy and low attack success rates.

### Strengths
1. This paper presents the first work to reveal backdoor attack vulnerabilities in existing model merging methods and observes two interesting findings - backdoor succession and backdoor transfer.
2. The paper conducts comprehensive experiments, including the performance of a large number of existing merging models and the comparison of the proposed DAM model with existing backdoor defenses.

### Weaknesses
1.	The threat model needs to be further clarified. Does the attacker know the other model? In particular, how does the backdoored model affect other clean models? What are the knowledge and capabilities of the defender? A detailed description of the threat model is missing. Specifically, it is unclear whether the attacker has any knowledge of the merging algorithm or the other models being merged, and how this impacts the attack strategy. Furthermore, the paper does not clearly define the defender's capabilities, such as access to clean data or the ability to inspect individual models before merging. The interaction between the backdoored model and clean models during merging needs more explanation, particularly regarding how backdoor triggers propagate or are amplified during the merging process.
2.	The novel of the proposed DAM approach is incremental, mainly focusing on optimizing two tasks – model merging and backdoor defense. In addition, the defense gain of DAM is marginal compared with existing backdoor defenses, such as SAU and AWM. The paper does not sufficiently demonstrate a significant advantage over existing post-hoc defense methods. The optimization of two masks, while novel, appears to be a straightforward combination of existing techniques. The performance gains, especially when compared to established defenses like SAU and AWM, are not substantial enough to justify the complexity of the proposed method. A more thorough analysis of the computational overhead and resource requirements of DAM compared to these existing methods is also needed.
3.	The paper investigates the vulnerabilities of model merging methods. The idea is similar to the robustness of backdoor attacks in model fine-tuning and continual learning. It would be great if the paper could compare these topics and discuss the major distinctions and unique challenges in model merging. The paper lacks a detailed comparison with the existing literature on backdoor attacks in fine-tuning and continual learning scenarios. The unique challenges of model merging, such as the lack of access to training data and the need to combine models trained on different tasks, are not clearly highlighted. A discussion of how these differences impact the design of defense mechanisms is needed.
4.	It would be great if the paper could provide a brief introduction regarding backdoor attacks mentioned in the paper, such as BadVit, TrojVit, LoRA-as-an-Attack, WAG. In addition, the paper mentioned that BadMerging breaks the safeguard for existing methods, but it is unclear what is the existing safeguard. The paper assumes the reader is familiar with several specific backdoor attack methods without providing sufficient background. A brief explanation of how these attacks function, especially in the context of vision transformers (BadVit, TrojVit) and model merging (LoRA-as-an-Attack, WAG), would be beneficial. It is also unclear what specific safeguards are broken by BadMerging, and this needs to be clarified.
5.	The paper writing needs to be improved. Some concepts need further clarification. See my questions below.

### Questions
1.	How does the Backdoor Detection Mask differ from existing trigger inversion or synthesis methods?
2.	How does the paper combine DAM with BadMerging as shown in Table 6?
3.	In Figure 4, what is meant by the term “subspace”? 
4.	What is LoRA-as-an-Attack/WAG in Table 5?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors investigate backdoor attacks in multi-task model merging and propose a meta-learning-based optimization method to mitigate these threats. Extensive experiments demonstrate its effectiveness and efficiency.

### Strengths
1. Multi-task merging methods are hot and meaningful directions to investigate
2. Meta-learning looks like a reasonable way to consider balancing effectiveness and efficiency, while it is interesting to consider different objectives for outer and inner level.

### Weaknesses
1. Bi-level optimization usually computational expensive, the authors might want to justify the sample efficiency and empirically showcase the algorithm running time.
2. I'm not an expert in Vision Transformers, so I'll leave it to the other reviewers to determine if the current experiments are sufficient. However, I am curious whether each task would exhibit different performance levels when subjected to the same backdoor attack. If there are variations, it would be necessary to test each task individually.
3. Why performance and safety terms can be linearly combined without tradeoff coefficient?
4. Why backdoor trigger and target labels are known during merging in eq (2)?
5. Following Q2, what if the synthesized perturbations are incorrect or inaccurate? Can the method still effective with rough knowledge of backdoor attack?

### Questions
1. Why performance and safety terms can be linearly combined without tradeoff coefficient?
2. Why backdoor trigger and target labels are known during merging in eq (2)? 
3. Following Q2, what if the synthesized perturbations are incorrect or inaccurate? Can the method still effective with rough knowledge of backdoor attack?

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
This paper first studies the impact of backdoors on model merging, and proposes a noval defense method, Defense-Aware Merging, which uses two masks to find the task-shared model subspace (M1) and the backdoor-oriented parameters (M2). The first mask finds shared subspaces to maintain good performance when merging various task-specific models, and the second mask hides sensitive backdoor neurons by introducing perturbations. The authors formed a bi-level optimization to find the best merging coefficients and masks. The performance of the proposed method is evaluated on several SOTA merging methods compared to post-defenses such as ANP, AWM and SAU. The attack strategies are TrojVit and BadVit. The proposed method can mitigate the backdoor effect while maintaining good performance.

### Strengths
1) First work to mitigate the backdoor effect on model merging.
2) The paper is well-written and easy to follow.

### Weaknesses
- In Figure 2(a), RESISC 45 and EuroSAT are datasets from the same domain, and it is not surprising to see that this merging can achieve high ACC while maintaining high ASR. In Figure 7(a), the ASR drops sharply due to the merging of different task-specifc models. It is curious to see how much the ASR drops when one task-specific model is merged with other different task-specific models. If ASR drops significantly in this case, one can simply merge the suspected model with several clean models to mitigate the backdoor effect while maintaining good ACC. What advantages can such a defense bring us?

- The backdoor succession and backdoor transfer seem to express the same meaning. Please clearify the difference between this two definitions.

- The paper, Wu et al., 2024, is already withdrawed. Please update the related references to stand your point, such as, "Assisted by the synthesized perturbations, we can identify and adjust the parameters related to the backdoor during merging, assuming that the backdoor-related parameters are more sensitive to the perturbations" in Sec 3. Below is an available one.
[1] Wu, B., Chen, H., Zhang, M., Zhu, Z., Wei, S., Yuan, D., & Shen, C. (2022). Backdoorbench: A comprehensive benchmark of backdoor learning. Advances in Neural Information Processing Systems, 35, 10546-10559.

### Questions
Summarize from weakneeses:

Q1: Please provide an experiment or analysis comparing the ASR drop when merging models from similar vs different domains. Specifically, one backdoor model in a certain domain + several models (backdoored or clean) from different domain.

Q2: Why learn M1 and M2, not a single M which combines the utility of M1 and M2? Considering Table 7, the ASR increases when DAM only with M2.

### Soundness
3

### Presentation
3

### Contribution
3
