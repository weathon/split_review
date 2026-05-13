# Learning Generative Judge from Preference Data

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Learning from preference feedback is a common practice for aligning large language models (LLMs) with human value.
Conventionally, preference data is learned and encoded into a scalar reward model that connects a value head with an LLM to produce a scalar score as preference. However, scalar models lack interpretability and are known to be susceptible to biases in datasets. This paper investigates leveraging the generation capability of LLMs to address both limitations in one shot. Specifically, we prompt the pre-trained LLM to generate positive and negative judgments, both supported with rationales in natural language form. The self-generated contrastive judgment pairs are used to train the generative judge with Direct Preference Optimization (DPO). This proposal of learning the generative ***J***udge using self-generated ***Con***trastive judgments (Con-J) ensures natural interpretability through the generated rationales supporting the judgments, and demonstrates higher robustness against bias compared to scalar models. Experimental results show that Con-J outperforms the scalar reward model trained on the same collection of preference data, and outperforms a series of open-source and closed-source generative LLMs. We open-source the training process and model weights of Con-J at https://anonymous.4open.science/r/Con-J-D014/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a generative approach to build reward models for preference learning. They generate judgements with explanations for both positive and negative samples in preference pairs and then use DPO to align a generative reward model. They find that this contrastive approach leads to improved performance on internal and public benchmarks when compared against scalar reward models and other generative methods.

### Strengths
* Very interesting and relevant approach that uses synthetic data to effectively propose a good empirical solution.
* Generating rationales would be very useful to verbalize and detect biases in the preference data and can help provide better data quality.
* I like that the authors train a model on publicly available datasets and report numbers on widely used benchmarks instead of just relying on the internal test sets.

### Weaknesses
 * The approach feels like it would add a lot of overhead in alignment training - RLHF is already extremely computationally intensive and waiting for models to generate rationales before providing the judgement feels like it would not be a feasible approach to use for cutting-edge model alignment.
* I would like to see some qualitative analysis of the rationales - there seems to be minimal information on how good they are and what they might be useful for. Has there been any human evaluation of the rationales when inconsistencies have been detected?

### Questions
Please see weakness section.

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
3

### Summary
This paper introduces Con-J, a new way of learning preferences by augmenting human pairwise preferences with LM-generated rationales. First, a LM is prompted to generate rationale pairs ($j^+$, $j^-$) for either element of the preference pair ($a^+$, $a^-$). The base LM is then trained with DPO to optimize $j^+$ over $j^-$ (vs. DPO with scalar rewards, which is simply trained to optimize $a^+$ over $a^-$). Empirical studies are performed on three domains (Creation, Math, Code), which find that Con-J outperforms scalar reward models at providing the correct judgment, that it outperforms other generative judges (Auto-J and Prometheus 2), and and that it is less susceptible to bias and spurious correlations in the reward function.

### Strengths
The experimental results demonstrate that Con-J is an effective method, compared to scalar reward models. The results section is quite comprehensive, with baselines across multiple models and datasets. The analysis section is informative with lots of useful takeaways: including studies of how Con-J can be robust in the presence of bias, and where LMs can generate rationales that fail to support the answer judgment. Overall, the claims are well-supported.

### Weaknesses
1. The empirical results (Table 10, Figure 4(b)(d)) seem to indicate that the main contribution to Con-J's good results are not the rationales, but (presumably) the regularization in eq. 9 instead (It's unclear to me what exact parts Con-J without rational removes...). Experimentally, what happens when this regularization is ablated? Furthermore, the claims in the abstract/introduction seem to suggest that rationales themselves are the reason why Con-J succeeds. While experimentally it's demonstrated that the rationales do improve robustness to bias, it seems misleading to claim this when the main results actually suggest that the rationales do not improve judgment accuracy at all. It may be good to do a deeper analysis of what is actually inducing this improvement.
2. Furthermore, the introduction highlights interpretability as a benefit of rationales (and puts it on the same priority level as robustness to bias). While intuitively rationales are indeed more interpretable, the paper never demonstrates the utility of this interpretability. What happens if you do have humans (or even other LMs) check the rationales and throw out inconsistent ones? (As far as I understand, the filtering step simply checks the correctness of the final answer, but not the rationale itself.) Is this interpretability actually useful for constructing better / more useful reward models? Will it be better to align downstream models with rationales?
3. The method has many moving parts. While the figure is useful, parts of the text and figure could be clearer. Having a concrete example with a LM-generated rationale in the main body or the figure could be useful for visualizing the method. Furthermore, it may be good to list out all the moving parts, esp for the ablations it is unclear what parts are preserved and what parts are not (e.g. how exactly does Con-J without rationales differ from the scalar model).
4. Note -- quite a few generative reward model methods have come out at about the same time this work (see https://arxiv.org/abs/2408.15240, https://arxiv.org/abs/2410.12832). While these can be considered concurrent work, perhaps a discussion of the tradeoffs of this method compared to other methods could be useful somewhere in the paper.

### Questions
1. How exactly does Con-J without rationale differ from the scalar model (Figure 4)?
2. One can also imagine a debiasing effect from using pre-trained LMs as rationale generators -- they are likely to generate rationales that align with preferences from their pre-trained data. While this may be ok if the preferences are generally in line with the pre-trained data, there may be issues with aligning to preferences with fundamentally different values or principles. Is there any investigation of whether the LM likes to generate the same set of values in its rationales?
3. Are there overall statistics from section 4.5 about how consistent / correct the rationales tend to be? Either automated, or human annotated (perhaps on a subset).

### Soundness
2

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
The paper introduces Con-J, an approach for training a generative judge using contrastive judgments for preference learning in order to address the problem of (i) lack of interpretability and (ii) susceptibility to biases in scalar reward models. Con-J involves creating contrastive judgments from a set of query-answer pairs sampled from a pre-trained LLM. These contrastive pairs are then used for preference finetuning, for example, direct preference optimization. Finally, they were able to show that Con-J performs better on several benchmarks such as RewardBench.

### Strengths
- [S1] The novelty of the paper’s contribution is clear. I appreciate how Con-J’s adjustments of the typical generative RM set-up was motivated.
- [S2] The ablations are also reasonable, especially on the different variants of the contrastive pairs (e.g., positive judgments only, etc.).

### Weaknesses
Overall, I lean towards accepting the paper on the merit of its contribution's novelty (new way of framing the generative RM setup), but there are some sections--particularly in the analysis--that are not fully convincing and needs revisiting (see [W1]).

[W1] I’m not entirely convinced with the analyses of Consistency and Correctness in Sections 4.3 and 4.5. I think it’s helpful if the paper first defines what “consistency” and “correctness” measure. In addition, it will be helpful to show that the GPT-4o scorer is reliable. Suggestion to the authors: define and motivate the aspects of consistency and correctness in the beginning of the paper.
- The prompt template in Table 9 speaks about the emotional tone, which I think measures a different aspect than consistency. Perhaps that’s also the reason why the results  in Figure 3b are surprising (I would expect the consistency of the rationales would also improve) and aren’t consistent with the cited literature on chain-of-thought (CoT).
- The scoring for Correctness is also confusing: the rubric for 3 can be confused for 2 and 4.  It’s also important to describe what correctness means for a subjective task such as Creation. I wonder what the findings would be if the rubric is more distinct.

### Questions
Questions
- [Q1] Can you clarify (or point to a URL) how you were able to obtain a test split for Ultrafeedback? The HuggingFace version (openbmb/Ultrafeedback) only contains a train split.

Comments/Nits:
- [C1] Line 259-261. The “Code” vertical domain is not mentioned
- [C2] Some LaTeX citation commands were used incorrectly. For example, \citet is often used in place of \citep, breaking the flow of writing. I highly recommend the authors to revisit these parts and update accordingly.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Con-J, a generative judge trained via self-bootstrapped learning from preference data to overcome limitations of scalar reward models, such as lack of interpretability and dataset bias. This model is trained with a combination of direct preference optimization (DPO) loss for contrastive judgement learning with an additional SFT term over positive judgements. Experiments across various domains (Text Creation, Math, Code) and benchmarks show that Con-J performs effectively, improving rationale correctness during training. This enables accurate judgments and meaningful explanations, supporting human-in-the-loop LLM alignment. Con-J also demonstrates reduced susceptibility to dataset bias compared to scalar and rationale-free models.

### Strengths
The paper is clearly-written and the motivation is clear that it attempts to bridge preference modeling with a generative component to reduce bias as well as to improve interpretability. Section 3 is pretty clear as in the math formulation and what the crucial components are in eq.4 and 5.  The empirical evaluation also seems reasonable with a variety of LLMs chosen and data domains being selected. I also find the illustrative examples and prompt-structures to be quite helpful for reproducibility and cross-comparisons.

### Weaknesses
I find this work to be a commendable engineering effort but with moderate novelty. In particular, is it not quite evident why do we need DPO’s formulation since the argument about similarity with pretraining objective and DPO’s policy being an optimal solution to the KL-constrained optimization problem is not directly addressed. Furthermore, SFT+ DPO combination for reward model training has been quite popular but I find the motivation for adding the SFT component to be less clear, especially the authors downweight this component with a relatively small weight compared to previous works. The authors argue that adding SFT avoids the reward overoptimization issue but I don't see an empirical evaluation of how this affects the log-likelihoods of pos and neg judgements in their Con-J training.

I find this work to be a commendable engineering effort but with moderate novelty. In particular, the authors do not fully justify the necessity of using DPO's formulation, especially given the lack of discussion regarding its connection to pretraining objectives and its optimality in KL-constrained optimization. Additionally, while the SFT+DPO combination is increasingly common in reward model training, the motivation for including the SFT component here is not entirely clear, particularly given the relatively small weight assigned to it compared to prior work. The claim that SFT prevents reward overoptimization lacks empirical validation through an analysis of how it affects the log-likelihoods of positive and negative judgments during Con-J training. 

While the idea is simple, my primary concern is that the generated rationales can be biased or be of low-quality if the chosen base model is not strong enough. Unless I am missing something, the authors do not conduct any human evaluation of the rationales being sampled.  How does one make sure that the rationales are at least surpass some *baseline* reasoning quality, regardless of the preference relation without a manual  verification component?

How do you control for the length of the judgements being sampled? From my perspective, if the intention in the Con-J methodology is better/explainable reward learning with compute-efficiency, then would you not have to control for judgement length pre-inference? In that case, for questions that would naturally require a more thorough reasoning process (CoT), wouldn’t the preference judgement be partial or biased in such cases? If judgement-length is controlled, how can shortened or partial/biased judgements’ affect on preference learning be mitigated in light of the inconsistency of rationale vs binary decisions observed in section 4.3?

How was the alpha value chosen? [1] suggests that a larger $\alpha$ (compared to this work) of 0.01 for text-regularization is optimal for generalizable reward learning, including testing on benchmarks like rewardbench. Also, [2,3] provides empirical evidence that DPO loss can lead to reduction in likelihoods of the winning responses. It’s reasonable to expect the SFT component helps in ensuring $\pi_ (j+ / p)$ stays relatively high during optimization, but authors here use an $\alpha$ of $1e^{-6}$ which is significantly lower than the optimal $\alpha$ in [1]. Clearly, this affects SFT-based regularization, but was this $\alpha$ value empirically determined or were there any particular motivations for choosing this value??

### Questions
1. The paper seeks to address a crucial issue in preference (or reward learning), where the reward model may be prone to bias and is not easily understood from the human interpretability angle. However, the learning algorithm (objective) is not very novel and recent work [1,3-5] has already leveraged such DPO + SFT type losses have leveraged such as contrastive learning formulation. However, I could not find these works being cited unless I am missing something. 

2. While the idea is simple, my primary concern is that the generated rationales can be biased or be of low-quality if the chosen base model is not strong enough. Unless I am missing something, the authors do not conduct any human evaluation of the rationales being sampled.  How does one make sure that the rationales are at least surpass some *baseline* reasoning quality, regardless of the preference relation without a manual  verification component?

 

3. How do you control for the length of the judgements being sampled? From my perspective, if the intention in the Con-J methodology is better/explainable reward learning with compute-efficiency, then would you not have to control for judgement length pre-inference? In that case, for questions that would naturally require a more thorough reasoning process (CoT), wouldn’t the preference judgement be partial or biased in such cases? If judgement-length is controlled, how can shortened or partial/biased judgements’ affect on preference learning be mitigated in light of the inconsistency of rationale vs binary decisions observed in section 4.3?


4 .How was the alpha value chosen? [1] suggests that a larger $\alpha$ (compared to this work) of 0.01 for text-regularization is optimal for generalizable reward learning, including testing on benchmarks like rewardbench. Also, [2,3] provides empirical evidence that DPO loss can lead to reduction in likelihoods of the winning responses. It’s reasonable to expect the SFT component helps in ensuring $\pi_ (j+ / p)$ stays relatively high during optimization, but authors here use an $\alpha$ of $1e^{-6}$ which is significantly lower than the optimal $\alpha$ in [1]. Clearly, this affects SFT-based regularization, but was this $\alpha$ value empirically determined or were there any particular motivations for choosing this value??

### Soundness
3

### Presentation
3

### Contribution
2
