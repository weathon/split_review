# Robust LLM safeguarding via refusal feature adversarial training

- Decision: Accept
- Scores: 6, 6, 3, 8

## Abstract
Large language models (LLMs) are vulnerable to adversarial attacks that can elicit harmful responses. Defending against such attacks remains challenging due to the opacity of jailbreaking mechanisms and the high computational cost of training LLMs robustly. We demonstrate that adversarial attacks share a universal mechanism for circumventing LLM safeguards that works by ablating a dimension in the residual stream embedding space called the \textit{refusal feature} \citep{arditi2024refusal}. We further show that the operation of refusal feature ablation (RFA) approximates the worst-case perturbation of offsetting model safety. Based on these findings, we propose \textbf{Re}fusal \textbf{F}eature \textbf{A}dversarial \textbf{T}raining (ReFAT), a novel algorithm that efficiently performs LLM adversarial training by simulating the effect of input-level attacks via RFA. Experiment results show that ReFAT significantly improves the robustness of three popular LLMs against a wide range of adversarial attacks, with considerably less computational overhead compared to existing adversarial training methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the vulnerability of large language models (LLMs) to adversarial attacks, which can elicit harmful responses by bypassing model safeguards. The paper reveals a shared mechanism among various adversarial attacks: they function by ablating a dimension in the residual stream embedding space, termed the "refusal feature" (RF), which acts as a linear predictor of input harmfulness. This refusal feature, discovered by Arditi et al. (2024), is the mass mean difference in hidden representations between harmful and harmless instructions, and is essential for the model to generate safe responses. Building on this insight, the paper proposes Refusal Feature Adversarial Training (ReFAT), which enables the model to recognize harmful instructions and maintain robustness. Experimental results show that ReFAT enhances the robustness of multiple LLMs against a wide array of adversarial attacks, while reducing computational overhead compared to traditional adversarial training methods.

### Strengths
1. The method is innovative, extending Arditi's Refusal Feature and further proving the similarity of adversarial attack and RFA mechanisms through causal theory, and proposing a more efficient adversarial training method based on this.
2. The method proposed in this paper can be objectively evaluated, including success rate of attack, generation performance, efficiency evaluation method, and the limitations are also analyzed.
3. The paper is well organized, first analyzing the general mechanism of adversarial attacks in the semantic space, and then naturally proposing an adversarial training method based on this feature, and proving the feasibility of the method through a large number of experiments and supplementary materials.

### Weaknesses
1. Using Llama-3-8B-Instruct-generated XSTest responses as the gold standard answers for supervised fine-tuning might pose potential issues in the design of scientific experiments, especially when Llama-3-8B-Instruct itself is also a subject of the subsequent experiments. This design could violate basic principles concerning independence in experimental standards. Specifically, while the authors mention using a holdout set, the fact that the fine-tuning labels are derived from a model that is also evaluated introduces a potential for bias. The fine-tuning process could inadvertently optimize the model towards the specific characteristics of Llama-3-8B-Instruct's outputs, rather than towards a more general notion of safety. This is particularly concerning given that the goal is to evaluate robustness against adversarial attacks, which should ideally be assessed against a truly independent standard.
2. The conclusion that rejecting direction leads to a performance degradation cannot be well demonstrated by experiments. The end of Section 3.1 states that experimental results show that performance degrades when the rejection direction is simply set to zero. However, the experimental figures in Appendix D only show that "harmless example features are not centered near zero," which leads to a speculation and intuitive inference that model performance degradation may be a possible consequence of this phenomenon? The lack of direct experimental evidence showing a causal link between zeroing the rejection direction and performance degradation weakens this claim. The figures in Appendix D, while informative, do not conclusively demonstrate that setting the projection to zero is the direct cause of the observed performance drop. A more rigorous experiment would involve explicitly manipulating the projection and measuring the resulting performance change.

### Questions
1. In Figure 3 - PCA visualization, why does the AutoDAN section have noticeably fewer experimental samples from HarmBench compared to the other three attack algorithms?
2. Section 3.1 mentions that Harmful samples were sampled from AdvBench, which to my knowledge is a dataset for adversarial suffix-type attacks. GCG is also a suffix attack. Intuitively, HarmBench (adversarial) should be quite similar to Harmful since they are both suffix attack samples. However, the actual results do not reflect this. Please explain or analyze this phenomenon.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses the vulnerability of LLMs to adversarial attacks, which can prompt these models to generate harmful, sensitive, or false information. These attacks exploit the models' inability to reliably detect and refuse harmful inputs. The authors highlight a mechanism called the Refusal Feature, which adversarial attacks exploit by ablating this feature to make harmful requests seem benign. Accordingly, the authors suggest a worst-case robust learning framework named ReFAT. During training, ReFAT dynamically computes the RF using two sets of inputs (harmful and harmless) and then ablates the RF for harmful inputs. This simulates the effect of adversarial attacks, training the model to make safety determinations without relying on the most salient features of input maliciousness.

### Strengths
1. The suggested method seems to be novel and reasonable. ReFAT dynamically computes the RF using two sets of inputs (harmful and harmless) and then ablates the RF for harmful inputs. This simulates the effect of adversarial attacks, training the model to make safety determinations without relying on the most salient features of input maliciousness. 

2. The exploration of refusal features is interesting. The intervention mechanism seems to be reasonable while more discussion should be added to make it clearer. 

3. The paper provides compelling evidence that ReFAT effectively enhances model robustness across different types of LLMs and attack vectors.

### Weaknesses
1. The authors rely on the previous findings of refusal features suggested by Arditi, and discuss the background in Sec 3.1 However, to me, I think the content is not self-contained enough, where I cannot understand the key heuristics behind Eq 3 as well as the following equation for their physical meanings. It seems that Eq 3 takes r_HH to somewhat measure the smoothness of the feature space, transforming h^l into a more informative space for intervention. I am quite curious about hope it is derived and why the third term in the rhs of Eq 3 exists (seems like a bias term?) Personally, I believe the authors should discuss more for this part, especially for their physical meanings, as the following sections of 3.2 - 3.3 critically rely on these formulations. 

2. What are the main difference between r_HH in Sec 3.1 and r_A in Sec 3.2, it seems that they are exactly the same thing. Therefore, the observation of their similar cosine similarity seems to straightforward. 

3. From the words in Sec 4.2, I cannot fully understand how the algorithm workflow is, could the authors provide more details. Moreover, it seems that the suggested worst-case learning method involves a lot of hyper parameters, such as the adopted layer of perturbations, strength of perturbations, I cannot find the specific configuration of these parameters. 

4. What's the connection between the suggested method and many previous alignment methods, especially for those methods that consider the binary feedback setup. Could the authors consider to add more baseline methods of alignments in their experiments.

### Questions
Please refer to the Weakness

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Summary: In this paper, the authors demonstrate that adversarial attacks share a universal mechanism for circumventing LLM safeguards. Based on these findings, the authors proposed Refusal Feature Adversarial Training (ReFAT) to efficiently performs LLM adversarial training by simulating the effect of input-level attacks via RFA. Experiment results show that ReFAT significantly improves the robustness of three popular LLMs against a wide range of adversarial attacks

### Strengths
+ proposed a new adversarial training method for safeguarding LLMs with improved efficiency
+ experiments show improvements over existing adversarial training solutions

### Weaknesses
 + The idea of manipulating the refusal features in the activation space is also introduced in other works on steering vector or activation steering such as the following ([1][2][3]). The authors might also want to discuss and comment on the differences. Specifically, [1][3] applied this type of activation engineering to the jailbreaking tasks and it is also recommended to compare with

[1] Wang, Haoran, and Kai Shu. "Backdoor activation attack: Attack large language models using activation steering for safety-alignment." CIKM2024

[2] Panickssery, Nina, et al. "Steering llama 2 via contrastive activation addition." ACL2024

[3] Cao, Yuanpu, et al. "Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization." NeurIPS 2024

+ There are other types of defenses on the safety of LLMs aside from adversarial training. It is also recommended to compare with other existing defense strategies, e.g., the following one [4].

[4] Cao, Bochuan, et al. "Defending against alignment-breaking attacks via robustly aligned llm." ACL 2024.

+ Many new attack baselines are presented in the recent year. The authors might also want to consider comparing with newer attack baselines (e.g. [5][6][7]) to demonstrate the effectiveness of the proposed work 

[5] Mehrotra, Anay, et al. "Tree of attacks: Jailbreaking black-box llms automatically." arXiv preprint arXiv:2312.02119 (2023).

[6] Li, Xirui, et al. "Drattack: Prompt decomposition and reconstruction makes powerful llm jailbreakers." arXiv preprint arXiv:2402.16914 (2024).

[7] Zhang, Tianrong, et al. "WordGame: Efficient & Effective LLM Jailbreak via Simultaneous Obfuscation in Query and Response." arXiv preprint arXiv:2405.14023 (2024).

+ The introduction of RFA and optimal attack and its relationship to the following adversarial training is not very clearly stated. See question below

### Questions
- Can you give more details on why including the mean RF activation over harmless prompts term in Eq (3)? What does this term represent and why do we want to add this term to the activation?

- Can you further explain the loss design in Eq (10)? The removal of refusal features ($H(x) − R_{HH}$) is different from what is demonstrated in Sec 3.2 / Sec 3.3?

- The approximation of RFA to the optimal attack still feels a bit less convincing. Can you directly calculate the best $\delta$ direction in Eq (7) and its similarity to RFA? Also you are approximating AA with RFA, directly solving Eq (7) using adversarial training should give you even better performances. Can you show the performance gap here?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a novel robustification method in the context of LLMs that is built open, ablating the "refusal direction" of a given model in its latent space during training. The authors demonstrate how this approach relates to standard adversarial training / attacks and provide evidence for the effectiveness of their method.

### Strengths
* The paper conducts various experiments to provide mechanistic insights onto how the proposed algorithm might be used as an alternative to adversarial training. 
* The authors also try to assess the limitations of the proposed approach (i.e., generalization to cases where the refusal direction might not be accurate anymore) 
* Comparisons to very recent baseline approaches are provided
* The proposed approach is considerably more efficient compared to other robustification methods

### Weaknesses
 * As far as I am aware the results from Figure 1 and Figure 2 are known and only provided to explain the concept. It would be nice if this is put into the right context. 
* The refusal results do not appear to be consistent with those of Xhonneux et al. (2024). A more comprehensive assessment of refusal behavior, e.g. with the OR-Bench, would further strengthen the paper 
* How stable are the different robustification methods with respect to hyperparameter choices? Would be interesting to assess how close each method is to its respective “optimum” specifically because the methods are directly compared to each other. Currently, I think it's not possible to give an accurate estimate of differences in accuracy robustness trade-offs between the different methods. However, the efficiency of the proposed approach is clear.

### Questions
* Can the authors elaborate on hyperparameter tuning procedures? I understand that tuning hyperparameters of competitor approaches requires extensive resources. However, it would be interesting to know how much work was required to obtain the results in the paper for ReFAT.

I believe that this work offers interesting insights to the ICLR community and recommend accepting it. I am willing to improve my score after the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3
