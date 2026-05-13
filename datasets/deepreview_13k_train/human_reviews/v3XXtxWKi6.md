# RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment

- Decision: Accept
- Scores: 6, 6, 6, 5, 6

## Abstract
We propose Reinforcement Learning from Contrastive Distillation (RLCD), a method for aligning language models to follow principles expressed in natural language (e.g., to be more harmless) without using human feedback. RLCD creates preference pairs from two contrasting model outputs, one using a positive prompt designed to encourage following the given principles, and one using a negative prompt designed to encourage violating them. Using two different prompts causes model outputs to be more differentiated on average, resulting in cleaner preference labels in the absence of human annotations. We then use the preference pairs to train a preference model, which is in turn used to improve a base unaligned language model via reinforcement learning. Empirically, RLCD outperforms RLAIF (Bai et al., 2022b) and context distillation (Huang et al., 2022) baselines across three diverse alignment tasks—harmlessness, helpfulness, and story outline generation—and when using both 7B and 30B model scales for simulating preference data

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Reinforcement learning (RL) from human feedback has been very effective in aligning large language models (LLM) to human preferences. In particular, RLHF requires human preference data to learn a reward model for optimizing the LLM with RL. However, collecting human preference data can be very expensive. This paper proposed to simulate human preferences using ideas from context distillation. Unlike context distillation, which only modifies the original prompt to be more positive, this paper modifies the original prompt to be both positive and negative, creating a preference dataset from the new prompt-generation pairs. The author's results show that this idea empirically performs better than two competitive baselines across various tasks.

### Strengths
- The proposed idea is very simple, and it is intuitive why the idea should perform well in practice.
- The authors thoroughly evaluated their approach to baseline approaches using both GPT-4 and human evaluation.
- The paper is well-written, and it is easy to follow.
- The authors perform experiments on a 7B and 30B model to show how robust their proposed technique is at scale.

### Weaknesses
 - It is hard to understand if the performance is coming from the prompts themselves or the proposed algorithm.
- The authors only report GPT-4 and human evaluation but do not report RM-score or standard NLP metrics (e.g., perplexity or output-perplexity)
- The authors do not provide a thorough description of the outlining prompts task, and there does not seem to be any references for this task, so it is very hard to understand the task's difficulty.

### Questions
- How did you decide on the prompt affix pairs?
- Why is having more than one prompt affix pair important? 
- Given that you automatically assume $o_{+}$ is preferred - how often does $o_{+}$ have a lower reward with respect to a held-out reward function?
- Why would training examples far away from the boundary be better than training examples close to the boundary? I would assume that the points far away could be easy to classify.
- Could you elaborate on how you performed your GPT-4 evaluation? What prompt did you use? How did you shuffle the data? Etc?
- Could you provide other quantitative metrics for all algorithms considered in your experiments? (e.g., RM-score, perplexity, output-perplexity, etc.)
 - Did you perform GPT-4 evaluation using comparisons from the algorithms-generated output and human-generated data for a given prompt?
- Could you provide other diversity metrics on the outputs of the text generated? (e.g., the ratio of distinct n-grams (Distinct-1, Distinct-2), average length of sentences, or count of n-grams in the generated text [1]). The text in Table 4 implies that RLCD generations are much longer than the base model sentences.
- Could you elaborate on the RLCD-Resouce model setup? In particular, what does it mean to re-label the same scoring prompts as in RLAIF?
- For RLAIF, did you run an experiment where you sample two outputs from the $p_{+}$ positive affix prompts? This provides RLAIF algorithms with modified prompts similar to RLCD and would reduce the advantage that RLCD has to strictly have the altered $p_{-}$ prompts.

[1] A diversity-promoting objective function for neural conversation models by Li et al. 2015

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method called Reinforcement Learning from Contrastive Distillation (RLCD) for aligning Language models (LMs) to follow principles expressed in natural language. RLCD utilizes contrasting prompts encouraging and discouraging adherence to principles, resulting in differentiated model outputs and cleaner preference labels, eliminating the need for human feedback. Based on the generated preference pairs, RLCD trains a preference model that captures desired behavior. The trained preference model guides a reinforcement learning process to refine an unaligned base LM, aligning it with the specified principles. RLCD outperforms existing methods like RLAIF and context distillation on diverse tasks including harmlessness, helpfulness, and story outline generation. RLCD demonstrates effectiveness with both small (7B) and large (30B) model sizes for simulating preference data. Overall, RLCD offers a novel method for human-free alignment of language models, surpassing existing techniques and demonstrating promising scalability.

### Strengths
RLCD is a neat idea that is simple yet effective. It requires some changes to the prompt to force the model to output more contrastive positive and negative outputs, which yield significant improvement in practice. I think the simplicity and effectiveness of the method is of value to the community.

Moreover, the empirical results seem quite strong, which makes the method more convincing. 

The paper is also easy to follow and understand.

### Weaknesses
The method seems straightforward and is less technically strong. The main technical contribution is the simple changes on the prompt design when generating the pair of responses for the preference data. While such changes make sense intuitively, i.e. making both responses more contrastive, the authors didn't show much principled analysis on why such design can be better than direct RLAIF. I think it would be helpful to give some more technical/principled explanation on RLCD.

Moreover, I wonder if this design is important when there's human feedback data presented in the preference dataset as well, which is more common in practice. It would be interesting to see if RLCD would still make such a big difference in practice with some human feedback data in the mix.

### Questions
1. Please clarify the technical details of RLCD, ideally some theoretical justifications.
2. Please show some experiments in scenarios where there's human preference data available in the data mixture.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Reinforcement Learning from Contrastive Distillation (RLCD), a novel method to align language models with human values without relying on human feedback. It's designed to overcome limitations in previous approaches like Reinforcement Learning from AI Feedback (RLAIF) and context distillation. RLCD operates by generating two contrasting model outputs using positive and negative prompts, with the positive prompts encouraging adherence to desired principles (e.g., harmlessness) and negative prompts doing the opposite. This method creates clearer preference pairs for training a preference model, which is then used to improve a base unaligned language model via reinforcement learning. The paper demonstrates that RLCD outperforms existing methods across various tasks and model scales, confirming its effectiveness in aligning language models more closely with desired human values.

### Strengths
- The paper is well written and easy to read
- The proposed RLCD method seems straightforward to implement and can be generalised
- By generating clearer preference pairs without human annotations, RLCD reduces the cost and time associated with collecting high-quality human preference data.
- The paper provides empirical evidence that RLCD outperforms existing methods across different tasks and scales.

### Weaknesses
 - The GPT-4 evaluated the baseline RLAIF outperforming the proposed RLCD method for the 30B model size.
- The contribution of the paper is limited

### Questions
In the GPT-4 evaluation results (Table 3), the authors mentioned that "The gap between RLCD and all baselines is especially large when using LLaMA-7B for preference data simulation.". Indeed, comparing row 2 and row 5: the RLCD-7B has a larger advantage over RLAIF-7B compared with RLCD-30B vs. RLAIF-30B. Similarly for the human evaluation in Table 2.
And in the Helpfulness and Outlining tasks, the baseline RLAIF-30B scored higher than the proposed RLCD-30B). I have a few questions on this:
- Why does the proposed RLCD algorithm gain a bigger advantage on the smaller LlaMA model when compared with its baselines? Is it due to the poor performance of RLAIF with smaller models?
- For the helpfulness and outlining tasks, the baseline RLAIF-30B outperformed the proposed RLCD. What is the cause of this result and should we generally adopt RLAIF when a larger LLM is available?
- The human evaluation always preferred RLCD compared with RLAIF, in contrast to GPT 4's preference on RLCD-30B. Can the authors please provide some insights into the cause of the difference in the GPT4 vs. human evaluation?

The downstream fine-tuning is using PPO. Although not the main contribution of the paper, can the authors please provide the details of the downstream fine-tuning procedures? For example, what are input and output of the RL model, what is the reward used by PPO derived from the upstream preference generation? And the overall process of the RL fine-tuning? This information would be useful for a general audience who would like to use the proposed RLCD method.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method called RLCD that incorporates the idea of context distillation into RLHF framework. Instead of using a single prompt to elicit preference data, RLCR does this by constructing two manually augmented prompts of positive and negative instructions. The authors show the effectiveness of RLCR by comparing it with RLAIF and SFT context distillation on a dataset.

### Strengths
1.The idea is interesting and the motivation seems clear.

2.The paper is well-written.

### Weaknesses
1.The proposed method is too simple that seems like a prompting trick in preference data construction.

2.More comprehensive methodology and solid experiments (e.g., stronger baselines and deeper analyses) are needed to improve the contribution and soundness of this paper.

### Questions
1. Will the proposed method reduce the diversity of preference data? 

2. What if the original prompt already contains positive or negative instructions?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Reinforcement Learning from Contrastive Distillation, which uses an unaligned language model to produce contrasting response pairs from both positive and negative prompts in terms of a desired attribute, e.g. harmlessness or helpfulness. It is argued that responses generated in this way are more distinguishable, producing a better signal-to-noise ratio. The produced rankings between pairs are then used for training a preference model, and subsequently, RLHF. Experiments are conducted on three alignment tasks, showing better performance than RLAIF and context distillation baselines.

### Strengths
1. The paper is well-written and easy to follow.
2. The method is clearly motivated, and the authors make a detailed argument on the problems with the prior work.
3. Experiments are conducted over multiple domains, demonstrating the generality of the method.

### Weaknesses
1. The analysis on the preference model shows that the preference model produced by RLCD is, while better than the baseline, still not very good, especially on the harmlessness attribute (Tab. 5). It is not clear how this slight advantage over chance (2.4%~5.9%) translates into a much better downstream performance after RLHF. The preference model's accuracy, particularly on harmlessness, is concerningly close to random chance, raising questions about the reliability of the signal used for RLHF. A small improvement over chance might not provide a strong enough gradient for effective policy learning, potentially leading to unstable or suboptimal results.
2. As shown in Appendix C, RLAIF-Few-30B produces both a better preference model and a better-aligned language model than RLCD-30B on the harmlessness benchmark, which is attributed to few-shot prompting by the authors. It seems that this technique can also be integrated into RLCD to enable a fairer comparison. The fact that few-shot prompting significantly boosts RLAIF's performance suggests that the zero-shot approach used in RLCD might be a limitation. It is unclear why RLCD does not explore few-shot prompting, especially given its potential to improve performance and provide a more robust comparison.
3. The advantage of RLCD over RLAIF shrinks going from 7B to 30B (Tab. 2). It remains to be seen whether RLCD (or RLCD-Rescore) can scale to yet larger language models that are arguably better at differentiating responses near the decision boundary. The diminishing returns of RLCD as model size increases raises concerns about its scalability and practical applicability to the largest and most capable language models. The method's effectiveness might be limited by the model's ability to distinguish between subtle differences in responses, which could be a bottleneck for further improvement.

### Questions
Not atm

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
