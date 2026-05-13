# Simultaneous Reward Distillation and Preference Learning: Get You a Language Model Who Can Do Both

- Decision: Reject
- Scores: 6, 5, 5, 5, 3

## Abstract
Reward modeling of human preferences is one of the cornerstones of building usable generative large language models (LLMs). While traditional RLHF-based alignment methods explicitly maximize the expected rewards from a separate reward model, more recent supervised alignment methods like Direct Preference Optimization (DPO) circumvent this phase to avoid problems including model drift and reward overfitting. Although popular due to its simplicity, DPO and similar direct alignment methods can still lead to degenerate policies, and rely heavily on the Bradley-Terry-based preference formulation to model reward differences between pairs of candidate outputs. 
This formulation is challenged by non-deterministic or noisy preference labels, for example human scoring of two candidate outputs is of low confidence. 
In this paper, we introduce \textbf{DRDO (Direct Reward Distillation and policy-Optimization)}, a supervised knowledge distillation-based preference alignment method that simultaneously models rewards \textit{and} preferences to avoid such degeneracy. DRDO directly mimics rewards assigned by an oracle while learning human preferences from a novel preference likelihood formulation. Our experimental results on the Ultrafeedback and TL;DR datasets demonstrate that policies trained using DRDO surpass previous methods such as DPO and e-DPO in terms of expected rewards and are more robust, on average, to noisy preference signals as well as out-of-distribution (OOD) settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an extension of Fisch et al 2024 work on Reward Distillation involving a regularization objective and demonstrate marginal improvements in terms of empirical benchmarks. There contributions are primarily two fold: 

1) When optimizing the reward model (Oracle in their paper) they add an additional regularization objective that ensures the Oracle still assigns high likelihood to the winning generation. 

2) The authors include a gradient unlikelihood objective, (which is further explained mechanistically in the appendix). This objective enhances gradients in the direction of the winning response when the winning response is small (and vice versa for the loosing response).

### Strengths
1) The paper is on a very relevant area and proposes a simple extension to existing approaches for preference optimization. 

2) The empirical experiments are extensive and instill faith in the reviewer of the proposed algorithms merits. 

3) The explanation of the unlikelihood objective in Eq 6 in terms of the gradient updates helps clarify better what the proposed algorithm achieves mechanistically.

### Weaknesses
A) Notation is a bit hard to follow in the paper, for example L_O represents the Oracle loss, but is there shared parameterization between the Oracle and the Policy? In either case, this should be explicitly notated in the paper. Similarly the variable alpha is shared between the equation 5 and 6, are these the same or different? It is important to be explicit about these differences. Furthermore, the paper does not explicitly state how the policy's reward estimates, denoted as \hat{r} in equation 6, are parameterized, which is crucial for understanding the method's implementation.

B) The major contribution in the paper over Fisch et al comes from the unlikelihood term in Equation 6. However this is explained only in passing in the main text, if indeed the authors want the focus to be on the importance of this term. The paper should provide a more detailed explanation of the unlikelihood term's mechanics and its impact on the optimization process, especially in contrast to the standard DPO objective.

C) My most major concern of the paper is that it is hard to decouple if the improvements come from i) Improved reward Distillation ii) The unlikelihood objective in Eqn 6) . I would be curious to see if replacing the first term in objective in Eq 6 with a standard DPO objective still results in an improved policy. If so, this framework would be much more generalizable. The paper lacks a thorough ablation study to isolate the effects of each component of the proposed objective function. Specifically, it needs to demonstrate the individual contributions of the reward distillation and the unlikelihood term.

### Questions
A) In Eq. 5 is the \log(y_w) term \log(y_w|x) or \log(y_w, x) ? This could  have potential ramifications for the quality of the resulting Oracle. In situations where both y_w and y_l are reasonably close generations, would you not want to also penalize the Oracle to be close to \log(y_l|x) ? 

B) Was the oracle initialized from an model trained by SFT on the winning responses? This is an important question to understand the oracle regularization and its effects.

C) The proposed objective involves multiple additional hyperparameters, including \alpha in 5, \alpha in 6 as well as \gamma in 6. Can the author's comment on the sensitivity of the model performance to these additional parameters?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Direct Reward Distillation and Policy Optimization (DRDO). The method combines explicit reward modeling with policy optimization by training an oracle model to provide reward signals, then the signals are directly distilled into the policy model. Additionally, DRDO employs a loss function that integrates a reward difference component and a contrastive log-unlikelihood term, adjusting the learning process based on the model’s confidence in assigning preferences.

### Strengths
1. DRDO avoids dependence on a reference model, which could offer computational benefits. 

2. In experiments, the inclusion of out-of-distribution settings (e.g., using CNN Daily articles) aligns with the claims of improved robustness.

### Weaknesses
1. The paper lacks a clear definition of key variables such as $\hat{r}_1$ and $\hat{r}_2$, which are crucial for understanding the proposed loss function. This lack of detail impedes understanding of how the reward signals are computed and integrated into the training process. Specifically, it is unclear whether these rewards are derived from the policy model itself or from the oracle model, and how they are parameterized. The paper should explicitly state the architecture used to compute these rewards and how they are incorporated into the loss function.

2. The authors seem to overstate their contributions; the distillation loss they employ appears to be derived from prior work, specifically the paper “Robust Preference Optimization through Reward Model Distillation” by Fisch et al. (2024). Proper attribution and a clearer differentiation from existing methods are needed. The paper needs to clarify how the proposed method differs in terms of the loss function and the overall training landscape, especially given the similarities in the distillation approach.

3. Key concepts, such as the handling of ambiguous preferences and the role of the modulating focal loss component, require more elaboration. Terminologies like “reward difference” and “contrastive log-unlikelihood” could be better clarified to aid understanding. It is not clear how the focal loss component adapts to varying degrees of preference strength and how it contributes to the overall robustness of the method. The paper should provide a more detailed explanation of the theoretical underpinnings of this component and its practical implications.

### Questions
1. How are $\hat{r}_1$ and $\hat{r}_2$ defined within the loss function? Providing clear definitions would enhance understanding of the method’s implementation.

2. Given that the distillation loss resembles that in Fisch et al. (2024), how does DRDO differentiate itself from this existing method?

3. Why were ablation studies on the focal loss component or comparisons across a broader range of datasets or evaluation metrics not conducted?

4. Considering the emphasis on practical efficiency, how does the computational overhead of DRDO compare to DPO or e-DPO?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Direct Reward Distillation and policy-Optimization (DRDO), a novel approach to preference alignment that combines reward modeling and policy optimization into a unified framework. Traditional methods like Direct Preference Optimization (DPO) can struggle with preference ambiguity, leading to suboptimal policies. DRDO addresses these issues by directly distilling rewards from an Oracle into the policy model while simultaneously learning from diverse preference signals. DRDO is evaluated on multiple benchmarks (Ultrafeedback, TL;DR, and AlpacaEval) and shows improved robustness, especially in handling noisy or non-deterministic preferences, outperforming popular methods like DPO and e-DPO.

### Strengths
* Sound Theoretical Foundation: The paper provides a clear theoretical grounding, with detailed proofs supporting DRDO’s robustness to varied preference strengths.

* Experimental Quality: The experiments are well-designed, covering both deterministic and non-deterministic preference data, and include benchmarks that highlight DRDO’s superiority across multiple settings and model sizes.

### Weaknesses
 * A bit concern on novelty and motivation: this paper seems to combine the ideas from three papers: eDPO, Oracle RM(https://arxiv.org/abs/2406.10216), and Focal. The main motivation and contribution need to be better justified in order to be a high quality paper in ICLR.

* Out-of-distribution (OOD) concern: For OOD experiment, it is a bit unclear to me on what the authors want to address. There are a few distribution shifts involved in alignment: 1. prompt shift among reward model training data, rlhf training prompt, and rlhf evaluation prompt. 2. response shift between the reward model training data and on-policy generation. As far as I understand, the TL;DR dataset also contains a few CNN Dailymail examples. It will be helpful if authors can show how robust the proposed approach can address the OOD issue systematically. Say show a plot with x-axis (the amount of OOD) and y-axis (the performance gap between baseline and proposed approach).

* Additional complexity of the system: focal loss introduces additional two hyperparameters, it is challenging to tune them, especially for OOD. What evaluation dataset to use? How to make sure the evaluation dataset is not overfitted and represent a good coverage of OOD samples during testing?

### Questions
See weakness.

### Soundness
3

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
Preference-based fine-tuning is known as one of the most effective methods to boost the generation ability of the modern large-language model (LLM). Direct Preference Optimization (DPO) provides a reasonable solution to this problem. However, the author points out that due to the design of the objective function and the non-deterministic preference label, the trained policy may degenerate, which can be treated as a kind of underfitting. To this, the author suggests DRDO (Direct Reward Distillation and policy-Optimization), which models rewards and preferences simultaneously. They adopt an oracle model that reflects the true preference and distillate its knowledge to a student model. Their method significantly outperforms the common baseline, and their analysis also matches the intuition.

### Strengths
Their concern is quite intuitive and handles the fundamental limitation of PbRL. Especially, they mainly point out that the human's preference label may be both noisy and stochastic; hence, the trained model may be confused by the ambiguous update signal. They formulate their intuition into a mathematical lemma and verify its validity. The experimental gap is also significant, and it emphasizes the effectiveness of the proposed method.

### Weaknesses
Even though their mathematical formulation and lemmas, their core algorithmic procedure is mainly written in natural language rather than pseudo-code, which diminishes the understandability of the overall process. On the extent of this problem, the components, techniques they adopted, and their main concerns are not harmonic. For example, to the best of my understanding, their key claim is that the 0-1 binary label fails to reflect the uncertainty of the human's preference, and therefore, the trained policy model can be either overfitted or underfitted. Consequently, they suggest to modify the objective function into a regression form rather than the MLE form. However, the concept of the oracle model, knowledge distillation, was suddenly mentioned. My understanding is that they train an Oracle preference model based on the given preference label, distillate its information to the student model, and use the student model for policy optimization. I am not sure how this idea handles the pointed limitation of DPO.

In the common sense of machine learning research, the term 'oracle' usually sounds impossible to achieve, only used during the upper bound experiment or thought experiment. I understand that you 'trained' an Oracle model from the given preference dataset. Is the coverage of the dataset enough to say your trained model is an oracle? Further, isn't your concern mainly built on the low data coverage assumption (Assumption 1)? Please provide more explanation on this part.

You said that because the dataset coverage is not infinite but limited, OOD works as a critical drawback to the PbRL framework. How does your framework handle this issue? What feature of knowledge distillation allows us to overcome the low data coverage?

I understand that your work mainly tries to handle the fuzzy, unambiguous label setting. Indeed, you split the dataset into a relatively fuzzy subset and a clear subset (hc,he & lc,le). However, the performance gap provided in Table 1 is pretty analogous, regardless of the subset partition. In my intuition, it indicates at least one of these: the edit-distance and human-confidence-based partitioning was not proper, or the performance gap comes from the other intuition rather than fuzzy-label handling. Would you provide more clarification or other experimental results on this point?

### Questions
1. In the common sense of machine learning research, the term 'oracle' usually sounds impossible to achieve, only used during the upper bound experiment or thought experiment. I understand that you 'trained' an Oracle model from the given preference dataset. Is the coverage of the dataset enough to say your trained model is an oracle? Further, isn't your concern mainly built on the low data coverage assumption (Assumption 1)? Please provide more explanation on this part.

2. You said that because the dataset coverage is not infinite but limited, OOD works as a critical drawback to the PbRL framework. How does your framework handle this issue? What feature of knowledge distillation allows us to overcome the low data coverage?

3. I understand that your work mainly tries to handle the fuzzy, unambiguous label setting. Indeed, you split the dataset into a relatively fuzzy subset and a clear subset (hc,he & lc,le). However, the performance gap provided in Table 1 is pretty analogous, regardless of the subset partition. In my intuition, it indicates at least one of these: the edit-distance and human-confidence-based partitioning was not proper, or the performance gap comes from the other intuition rather than fuzzy-label handling. Would you provide more clarification or other experimental results on this point?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work seeks to addresses challenges that arise in DPO when ‘non-deterministic’ preferences are present in the dataset. The authors provide a theoretical motivation behind why these points are challenging and propose DRDO, Direct Reward Distillation and policy-Optimization to address this issue. They test DRDO on subsets of the Tldr and Ultrafeedback datasets.

### Strengths
The proposal of the paper to combine a reward difference loss that measures the strength of preferences with a contrastive loss term that uses the binary preference labels from preference datasets is novel to the best of my knowledge. The authors show the proposed approach produces an improved win rate over a DPO and e-DPO baseline.

The paper conducts varied experiments to understand the proposed method. They vary the size and temperature of the generated responses to explore a wide range of possible settings and analyse the win rate using suitable approaches and prompts with GPT 4.0.

### Weaknesses
A key component of the paper is the theoretical analysis of the weaknesses of DPO, specifically Lemma 1 and Lemma 2. The proof of these Lemma in the appendices seems to have multiple mistakes, for example the statement at the end of Appendix A.2 appears wrong as the latter equation should approach 1, this issue is repeated in the derivation of Lemma 2, both are key for later motivating the proposed DRDO. If this is a misunderstanding on my behalf, the quality of the explanation needs improvement as both Section 3 and the writing in the appendix was hard to parse. 

Furthermore, it appears that Lemma 1 simply re-states results found within the existing literature, issues with deterministic preferences in DPO i.e. Lemma 1a) and 1b) are presented in [1] and the result of Lemma 1c) appear in [2], both works are cited by this paper. 
The motivation of the paper is also very unclear to me. The authors define noisy preferences as those with $p(y \succ y’) \approx ½$ and claim that “This (DPO) formulation is challenged by non-deterministic or noisy preference labels”. In the proposed setting it appears that these non-deterministic points are just weak learning signals. The authors should justify why these points matter, for example, pluralistic approaches argue that these weak signals stem from multiple different viewpoints being present in the dataset and thus work to learn models unique to specific viewpoints [3,4]. An argument that motivates the proposed approach against the pluralistic setting would be beneficial.

### Questions
1.	In Figure 2, is the DRDO Preference Loss $L_{kl}$ or the Contrastive Log-unlikelihood?

2.	What does an ablation on the two loss terms look like? If trained just with the contrastive loss how does the model perform?

3.	Whilst the paper compares to e-DPO how does the approach compare to IPO an alternative to DPO mentioned heavily in the first few sections of the paper that does not have a reward oracle component?

### Soundness
1

### Presentation
3

### Contribution
2
