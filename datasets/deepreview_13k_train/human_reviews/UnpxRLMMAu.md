# RATE: Score Reward Models with Imperfect Rewrites of Rewrites

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
This paper concerns the evaluation of reward models used in language modeling. A reward model is a function that takes a prompt and a response and assigns a score indicating how `good' that response is for the prompt. A key challenge is that reward models are usually imperfect proxies for actual preferences. For example, we may worry that a model trained to reward helpfulness learns to instead prefer longer responses. 
  In this paper, we develop an evaluation method, RATE (Rewrite-based Attribute Treatment Estimators), that allows us to measure the \emph{causal} effect of a given attribute of a response (e.g., length) on the reward assigned to that response. 
  The core idea is to use large language models to rewrite responses to produce imperfect counterfactuals, and to adjust for rewriting error by rewriting \emph{twice}. We show that the RATE estimator is consistent under reasonable assumptions. We demonstrate the effectiveness of RATE on synthetic and real-world data, showing that it can accurately estimate the effect of a given attribute on the reward model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the evaluation of reward models in language modeling by introducing RATE (Rewrite-based Attribute Treatment Estimators), a method for measuring the causal effect of a specific attribute (e.g., length) on the reward assigned to a response. RATE uses large language models to rewrite responses, generating imperfect counterfactuals, and adjusts for rewrite errors by performing a second rewrite. The paper demonstrates the effectiveness of RATE on both synthetic and real-world data.

### Strengths
The topic of reward model evaluation is highly relevant and important for large language models.

The paper introduces a new approach, creating response pairs where only the attribute of interest varies through rewrites, enabling causal estimation.

The paper  leverages LLM-based rewrites and rewrites of rewrites to control for biases, an innovative strategy that enhances reliability in causal estimation.

### Weaknesses
The paper focuses primarily on response length as an attribute. Are other attributes considered?

The approach's effectiveness may be sensitive to the LLM’s ability to generate accurate counterfactuals, potentially impacting the reliability of causal estimates.

The rewrite instructions appear straightforward; adding prompts specific to target attributes could improve accuracy.

The experiments lack analysis on the effectiveness of the rewrites themselves.

The method depends heavily on the LLM for rewriting; experiments using different LLMs for rewriting could help assess robustness.

### Questions
For the rewrite instructions, does the method use the same target model, or is another model employed for implementing the rewrite instructions?

How does the paper assess the effectiveness of the rewrite instructions?

What reward models were used in the evaluation experiments? How sensitive is RATE to the quality and specificity of the initial LLM-based rewrites?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to reduce Length bias in preference datasets by having Large Language Models (LLMs) regenerate responses. The authors theoretically prove that under reasonable assumptions, this rewriting can maintain the consistency of preferences. They also demonstrate through experiments that this method can indeed avoid the sensitivity of RMs to irrelevant metrics on both synthetic and real data.

### Strengths
- The theoretical formulas are quite detailed.
- The authors' experiments cover three different types of tasks.
- Under the setup of this paper, the ablation studies conducted by the authors are logically consistent.

### Weaknesses
 - The biggest issue with this paper lies in the validity and applicability of the method.
  - Validity of the method. The authors have made efforts in the experiment section to demonstrate that RATE can reduce the impact of irrelevant factors on RM, and I do not doubt these results. However, these alone are insufficient to support the contribution of the paper. The authors should also show that RATE can simultaneously improve the accuracy of RM scoring. For instance, they should demonstrate the enhancement that RM brings to methods such as BoN, RLHF, RFT, etc., through experiments across multiple tasks and models. Otherwise, it would be difficult for readers to confidently deploy this method in practical RMs based solely on the experimental results presented in the paper, which would significantly undermine the contribution of the paper.
  - Applicability of the method. The authors mention that RATE requires calling gpt-4 to rewrite responses in the preference dataset, indicating that the RATE method relies on expert models for modification. This will greatly limit the scope of application of the method.
- The presentation of experimental results is very confusing.
  - In Figure 2, the authors aim to show that RATE can reduce the length bias of the reward model towards responses. However, from the figure, I observe that the sensitivity of the reward model to factors such as Sentiment, Complexity, and Helpfulness has also decreased. I believe this will raise concerns among researchers about the effectiveness of the RATE method, as it could significantly alter the original performance of the RM.
  - In Figure 3, the authors intend to illustrate that RATE can enhance the invariance of the reward model to irrelevant metrics. However, the persuasiveness of this single figure is quite weak. What people care about is whether the RM can score according to human true preferences. For example, a reward model that always gives a score of 0 to any response can still achieve the effect shown in Figure 3, but this is not what humans actually want.

### Questions
- Does RATE affect the accuracy of RM scoring? Is it a positive or negative impact? Are there any quantifiable metrics?
- Can RATE help RM better assist LLMs in alignment? Has this been verified on mainstream methods such as BoN, RLHF, etc.?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focus on the evaluation of reward models used in language modeling. The authors propose to  use rewrites of rewrites to correct for the bias introduced in intervention of LLM's rewrite.  They evaluate the proposed method and show its effectiveness at correcting for spurious correlations in the data.

### Strengths
I appreciate the idea of using causality to evaluate the reward model, especially rewrite twice to address the introduced noise in intervention. 

The proposed method are simple, straightforward but effective and may be further helpful in reward hacking.

### Weaknesses
See questions.

The paper is written in a clear and accessible manner, making it easy to understand and follow. Therefore I have only a few minor questions and suggestions.

In Lines 211 and 212, if I understand correctly, $\text{Re}(y^{ij}, 0)$ refers to rewriting $y^{ij}$ such that the corresponding attribute is zero. Should this instead be $\text{Re}(y^{ij}, 1)$, and similarly, should $\text{Re}(y^{ij}, 1)$ be $\text{Re}(y^{ij}, 0)$? Please double-check the notation and explain their reasoning if it is correct as written. 

One more thing I am interested in: could you please give more examples of the spurious correlations in the data, except for the length? Please give a brief discussion of how the proposed method could be applied to different types of spurious correlations beyond length.

A couple of suggestions:
- The subscript $i$ in $x^{i}$ could potentially be omitted for brevity if applicable.
- In Figure 1, it might be helpful to represent that the "helpful/unhelpful" state is the true cause of the response, while length serves as a spurious cause within the data. This may be helpful for the readers to understand that we want the reward model learn the actual cause, "helpful/unhelpful", but usually the reward model may learn the spurious cause, "length". See some related paper also investigating the real cause of rewards in LLM [1] and traditional RL [2].

### Questions
The paper is written in a clear and accessible manner, making it easy to understand and follow. Therefore I have only a few minor questions and suggestions.

In Lines 211 and 212, if I understand correctly, $\text{Re}(y^{ij}, 0)$ refers to rewriting $y^{ij}$ such that the corresponding attribute is zero. Should this instead be $\text{Re}(y^{ij}, 1)$, and similarly, should $\text{Re}(y^{ij}, 1)$ be $\text{Re}(y^{ij}, 0)$? Please double-check the notation and explain their reasoning if it is correct as written. 

One more thing I am interested in: could you please give more examples of the spurious correlations in the data, except for the length? Please give a brief discussion of how the proposed method could be applied to different types of spurious correlations beyond length.

A couple of suggestions:
- The subscript $i$ in $x^{i}$ could potentially be omitted for brevity if applicable.
- In Figure 1, it might be helpful to represent that the "helpful/unhelpful" state is the true cause of the response, while length serves as a spurious cause within the data. This may be helpful for the readers to understand that we want the reward model learn the actual cause, "helpful/unhelpful", but usually the reward model may learn the spurious cause, "length". See some related paper also investigating the real cause of rewards in LLM [1] and traditional RL [2]. 

[1] Tien, J.Y., He, J.Z., Erickson, Z.M., Dragan, A.D., & Brown, D.S. (2022). Causal Confusion and Reward Misidentification in Preference-Based Reward Learning. International Conference on Learning Representations.

[2] Zhang, Y., Du, Y., Huang, B., Wang, Z., Wang, J., Fang, M., & Pechenizkiy, M. (2023). Interpretable Reward Redistribution in Reinforcement Learning: A Causal Approach. Neural Information Processing Systems.

### Soundness
2

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
5

### Summary
The paper proposes a more causal perspective to evaluate reward model by generating pairs of responses are the explicitly rewritten to differ in a particular aspect. To this end they propose a rewrite of rewrite strategy that seems to be most effective in evaluating reward model biases.
They apply their methods on several datasets including semi synthetic ones to illustrate the novelty of their evaluation method.

### Strengths
- The paper proposes a new way to construct evaluation data pairs for reward modelling through rewritten which to the best of my knowledge has not been done before.
- The paper also investigates the effects of rewriting the rewrites which I find quite intriguing as well as interesting. They how that rewriting the rewrites do affect the reward model in some way.
- The paper also shows on semi-synthetic data how they method is more robust to distribution shifts than naive methods.

### Weaknesses
 - The paper is written in a very convoluted way for a relatively simple method.
- Especially the experiments are described in a way that I find extremely hard to follow even after repeatedly reading the section. Hence i have some questions regarding this paper.
1) What are you expecting to see in Figure 2? "The naive estimator overstates the length bias" How do you know the ground truth length bias and how can you claim yours does better? This part is very unclear to me and seems to be the crux of the misunderstanding. If you could clarify I would be more than happy to raise my score.
2) Figures 4 and 5 seem to show the effects of rewriting rewrites. In Figure 4, you see minor changes. In Figure 5 the trend does not seem to be consistent across models. Hence my question is, what are you expecting to see in this figure? what is the ground truth? and how would you pick in practice whether to rewrite the rewrite. 
3) Theorem 1 in the paper seems like a standard causal inference setting. and you assume noise assumptions that are just not controllable in the LLM setting. Hence my question to you is what the point of that theorem is? Can you please justify the additive reward structure and what the motivation for that is?

### Questions
I have written all my questions above.
Happy to raise my score if the above is addressed well.

### Soundness
2

### Presentation
2

### Contribution
2
