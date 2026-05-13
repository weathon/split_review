# RainbowPO: A Unified Framework for Combining Improvements in Preference Optimization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recently, numerous preference optimization algorithms have been introduced as extensions to the Direct Preference Optimization (DPO) family. While these methods have successfully aligned models with human preferences, there is a lack of understanding regarding the contributions of their additional components. Moreover, fair and consistent comparisons are scarce, making it difficult to discern which components genuinely enhance downstream performance. 
In this work, we propose $\benchmarknameonly$, a unified framework that demystifies the effectiveness of existing DPO methods by categorizing their key components into seven broad directions. We integrate these components into a single cohesive objective, enhancing the performance of each individual element. Through extensive experiments, we demonstrate that $\benchmarknameonly$ outperforms existing DPO variants. Additionally, we provide insights to guide researchers in developing new DPO methods and assist practitioners in their implementations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to provide a unified framework for direct preference optimization (DPO) methods which are becoming a popular and successful method to train or finetune generative language models, and in particular, for better alignment with human preferences. In DPO, we are given a dataset of triples consisting of a prompt and a pair of potential responses, one of which is known to be preferred over the other. The high level goal is to fine tune a large language model in a manner that maximizes the difference in the likelihood of the preferred and dispreferred responses. The performance of a model is measured by the win rate of responses of the model being preferred over the responses of another model over a collection of inputs as predicted by an automatic evaluator which is typically another generative language model trained to predict which of two responses a human annotator would prefer.

The paper surveys, then carefully analyzes the objective functions of different algorithms in a growing family of DPO like models, identifies their components and then formulates an objective function for their proposed RainbowPO method which incorporates the components and techniques of previous DPO methods. The contribution of the different components of the objective function can be tuned smoothly using hyperparameters. The paper then goes to evaluate the effectiveness and contributions of each component to the performance of DPO methods.

After rebuttal:
I am increasing my score from 5 to 6. The authors have addressed my questions. Overall, I lean towards acceptance if there is room to accommodate it.

### Strengths
- A careful analysis of different DPO methods, identifying their components and understanding the contribution of components of different DPO methods to performance is a worthwhile endeavor. The main technical contribution is a careful analysis and rewriting of the objective functions of recently proposed DPO methods and unifying them as a single objective function. 
- Another contribution is the proposed the mixed reference policy obtained by mixing a fine tuned policy (model) with a policy that maintains a certain margin or odds ratio of the likelihood of the preferred to dispreferred responses.
- I believe the main conceptual contribution is the development of common frameworks and pipelines that allow researchers and practitioners to evaluate different components and techniques for DPO. As such, the paper is well motivated and the findings of this paper and follow on works that attempt to perform such evaluations will be of significance as alignment of generative language models is an important problem and existing reinforcement learning based approaches are computationally expensive in comparison to DPO.
- The main finding that length normalization, policy mixing and contextual scaling contributed towards increasing performance are a potentially interesting takeaway that may be significant to practitioners.

### Weaknesses
 - The paper is overall poorly written with several missing explanations and gaps in the logic. While it is possible to guess what is meant, a reader unfamiliar with the area will likely find it very hard to follow.
- At a high level, the organization of the paper makes it hard to read as the text on the background and proposed RainbowPO model frequently references results in the later experimental section which distracts from understanding the components of the DPO objective functions.
- The technical contributions and novelty are limited beyond the creation of the unified objective function and evaluation pipeline.

Some examples of issues with the writing:
- line 153: ... there lacks a work .. please consider revising. This is just one minor example. There are several more throughout the paper and they are too numerous to list. Please consider performing a thorough reading of the paper.
- please consider elaborating on the verbosity issue and how it may be potentially a way to game the evaluator
- different places use y_l and y^l. Is this a typo? Similar issues exist elsewhere. Preferably please keep the usage of subscript and superscript consistent. For example, see in (10) the use of \pi_\alpha and \pi_{ref}^\alpha. Consider e.g. using \pi_\alpha, \pi_\alpha^{ref} and \pi^{ref} as appropriate instead
- abbreviation LC (length controlled) is not defined or explained anywhere making it hard to understand results in Section 4.1
- in general, it would be nice to have a more clear discussion of the evaluation framework and evaluation criteria. As it stands, the paper assumes too much background knowledge e.g. about AlpacaEval.

### Questions
- Could you please elaborate on the evaluation? What was the base model against which the win rate was  evaluated in Section 4.
- Could you please elaborate on the use of link functions?
- Could you please elaborate on the mixing reference policy results in Section 4? What are the policies being mixed? How is the "good" policy \pi_\gamma obtained?

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
4

### Summary
The paper extracts key components from various DPO variants and provides theoretical analysis for each component. It then establishes a unified formulation that encompasses most DPO variants. Empirically, the author conducts a series of ablation studies to analyze the effectiveness of each component in DPO variants and identifies the key components that contribute to metric gains. By combining these components, the author proposes a new variant of DPO called RainbowPO, which outperforms all other DPO variants.

### Strengths
1. This work is the first to provide a comprehensive analysis of the effectiveness of various DPO variants under the same setting, making it a valuable contribution to the community.

2. The study offers an in-depth examination of the components of DPO, supported by thorough experiments that validate the analysis, resulting in a solid and reliable evaluation.

3. By combining all effective components, this work successfully formulates a new variant of DPO and demonstrates its superior performance over existing algorithms, showcasing the potential for further advancements in the field.

### Weaknesses
1. The evaluation benchmark is limited to AlpacaEval, which may not provide sufficient evidence to support the claims regarding the effectiveness of each component and the advantages of the proposed RainbowPO. A more comprehensive evaluation across multiple benchmarks would be necessary to further validate these findings.

2. The advantage of introducing key components in RainbowPO lacks systematic explanation and remains at a purely empirical level. It is unclear whether the same advantages can be transferred to other tasks, highlighting the need for further investigation into the generalizability of these findings.

3. The proposed method introduces significant additional complexity compared to baseline methods, which may impact its practicality and scalability. Further research is needed to determine whether the benefits of RainbowPO outweigh the increased complexity it introduces.

### Questions
1. For eq (1), how to obtain the policy $\pi_\gamma$ in the practical setting?
2. What is the purpose of raising eq (12)? If left side is a lower bound then whether minimizing the lower bound can imply anything?

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
2

### Summary
The paper developed Rainbow PO as a unified framework for direct preference optimization. Motivated by the challenge in comparing various xPO methods in literature, the authors began the study by analyzing more than 10 existing xPO methods and identified seven mathematically orthogonal components for mapping these methods. Among these components, they justified four of them as effective. Based on these findings, they proposed RainbowPO to combine these components. One notable novelty is that RainbowPO adopts a mixing reference policy mechanism. The authors conducted experiments to illustrate RainbowPO's superior performance over previous DPO variants.

### Strengths
1. The paper strived to provide a systematic and comprehensive study of existing preference optimization methods. The identification of the seven components leads to a structured framework for evaluating xPO methods, which is useful considering the large, and still growing number of xPO methods. 

2. The paper contributed clarity and insights on how different components of an xPO method affect the method’s performance. The experiment evaluation offers interesting results illustrating the value of adding components to an xPO model.

### Weaknesses
There lack transparency and explanation on the identification of the seven components. It would be helpful to include further details on the identification process. Relevant questions include: Are these components necessary and sufficient to categorize current and potential new xPO models? Have similar components been applied or mentioned in literature on xPO? Are there any potential interactions among components that would affect the performance of xPO?

### Questions
Please answer the questions mentioned in ‘Weaknesses’.

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
Direct Preference Optimization (DPO) has emerged as an effective approach for fine-tuning large language models (LLMs) to align with human preferences. Various versions of DPO have been proposed in the literature; however, an extensive comparison between these different DPO variants is still lacking.
This paper aims to analyze various versions of DPO to identify components that enhance performance across different applications. To this end,  seven key components have been identified  across ten DPO variants. By combining these components, a new approach that achieves state-of-the-art performance has been proposed. This approach is conceptually similar to the Rainbow framework [1], which unified various enhancements of Deep Q-Networks (DQNs) from the literature.

This paper explains seven components, namely--Length Normalization, Link Function, Home Advantage, Mixing Reference Policy, Rejection Sampling, Contextual Scaling and SFT Loss. Then a new loss is formulated combining the seven components. Finally, the experimental evaluation reveals that Length Normalization, Contextual Scaling  and Rejection Sampling contribute to improvement over the baseline DPO.

The paper could be a significant contribution in the field of Fine-tuning large language models. 
However, to meet the publication standards of a top-tier conference, it requires an additional round of thorough editing.

[1] Hessel, Matteo, et al. "Rainbow: Combining improvements in deep reinforcement learning." Proceedings of the AAAI conference on artificial intelligence. Vol. 32. No. 1. 2018.

### Strengths
**Originality:** This paper performs a meta-analysis on different variants of DPO.

**Quality**: The experimental evaluation comparing different components is the main strength of the paper.

**Clarity**: The text is written with clarity and well organized. It is easy to follow, even for someone like me, who is not up-to-date with the recent developments in LLM finetuning techniques. However, some of the terminologies introduced require explanations (see weakness).

**Significance**: Fine-tuning large language models (LLMs) for preference optimization has garnered increasing attention recently. A meta-study comparing different variants of preference optimization in LLMs would be highly valuable for both academics and practitioners. This work combines seven variants and promises to make the implementation publicly available, which would be a significant contribution to the community.

### Weaknesses
 - Some acronyms, such as IPO and KTO, are never explained. Given that this paper is a meta-analysis, it’s important to define all acronyms for the reader’s convenience.

- Define LC WR in the caption or in a footnote in Table 4.

- It seems the term 'warm-up adjustment'  is never introduced before Table 3.

- The color coding in Table 4 is counterintuitive; using red to indicate better-performing models and green for worse-performing models is disorienting for the readers.

- The results in Table 4 are based on training for 3 epochs. Could these outcomes differ if the model were trained for additional epochs? Maybe you can  conduct an ablation study on the impact of number of epochs or plot training loss against number of epochs.

- Is there any explanation why rejection sampling does not perform well with length normalization?

I would be happy to raise my score, if the authors reply to my questions.

### Questions
- DPO techniques have been reported to lack generalizability in out-of-distribution tasks [1]. To address this limitation, learning chain-of-thought (CoT) policies has been proposed in the literature. Can the method proposed in this paper be adapted to learn a CoT policy?

- Robust DPO [2] is another approach to make DPO robust to noisy preferences. Is there a reason why this variant is not considered in your work? 

- Have you considered approaches [3] which removes the process of learning a reward model by directly learning though supervised learning?

- Apart from Win ratio (WR), have you measured BERTScore?

1: Choi, Eugene, et al. "Robust Chain of Thoughts Preference Optimization." Seventeenth European Workshop on Reinforcement Learning.

2: Chowdhury, Sayak Ray, Anush Kini, and Nagarajan Natarajan. "Provably Robust DPO: Aligning Language Models with Noisy Feedback."
 Forty-first International Conference on Machine Learning.

3: Hejna, Joey, et al. "Contrastive Preference Learning: Learning from Human Feedback without Reinforcement Learning." The Twelfth International Conference on Learning Representations.

### Soundness
3

### Presentation
3

### Contribution
3
