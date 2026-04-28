# Multi-Granularity Semantic Revision for Large Language Model Distillation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Knowledge distillation plays a key role in compressing the Large Language Models (LLMs), which boosts a small-size student model under large teacher models' guidance. However, existing LLM distillation methods overly rely on student-generated outputs, which may introduce generation errors and misguide the distillation process. 
Moreover, the distillation loss functions introduced in previous art struggle to align the most informative part due to the complex distribution of LLMs' outputs.
To address these problems, we propose a multi-granularity semantic revision method for LLM distillation.  At the sequence level, we propose a sequence correction and re-generation (SCRG) strategy. 
SCRG first calculates the semantic cognitive difference between the teacher and student to detect the error token, then corrects it with the teacher-generated one, and re-generates the sequence to reduce generation errors and enhance generation diversity.
At the token level, we design a distribution adaptive clipping Kullback-Leibler (DAC-KL) loss as the distillation objective function. DAC-KL loss exploits a learnable sub-network to adaptively extract semantically dense areas from the teacher's output, avoiding the interference of redundant information in the distillation process. Finally, at the span level, we leverage the span priors of a sequence to compute the probability correlations within spans, and constrain the teacher and student's probability correlations to be consistent, further enhancing the transfer of semantic information. Extensive experiments across different model families with parameters ranging from 0.1B to 13B demonstrate the superiority of our method compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces three new objectives for distilling generative LLMs at the token, span, and sequence levels:

(token) DAC-KL: it learns additional models to adjust the KL divergence by clipping outlier token distributions in the teacher model.

(span) SPAN-LEVEL CORRELATION CONSISTENCY: The author uses an off-the-shelf tool to extract the spans, e.g. noun phrases, from the generation from student and teacher. Within each span, they enforce the probability correlation between adjacent tokens from the student model’s token to align closely with the teacher model’s. Honestly, I cannot say I totally understand the point of this objective.

(sentence) SEQUENCE-LEVEL CORRECTION AND RE-GENERATION: It identifies error tokens in the student's sequence by selecting the ones with the most disagreement by teacher model. Then, they replace the tokens with teacher-generated tokens, and re-generates the sequence.

They compare their methods against SOTA approaches, such as DistiLLM, MiniLLM, and GKD, on five instruction-following datasets. They adopt the ROUGE-L as the metric. Their findings show substantial performance gains for OPT models, though improvements are more modest for other LLMs.

### Strengths
1. The proposed objectives are reasonably novel. The SCRG approach, in particular, tackles a critical issue: when the student model generates an "error" token that falls outside the prefix distribution of the teacher model, it often leads to noisy and unreliable supervision from the teacher’s predictive distribution. This method could be especially useful for cases involving suboptimal teacher or student models with very limited capacity. It’s also interesting to note its connection to the LaSO framework [1], where an expert policy performs local corrections on the trajectories of the learned policy. Previous autoregressive KD work doesn't fully explore this approach.

2. The proposed methods significantly outperform baseline methods for the OPT base model, although the improvements for other LLMs are relatively marginal.

3. The author conducts extensive experiments to study the impact of different variants of the KD methods.

[1] Daumé III, Hal, and Daniel Marcu. "Learning as search optimization: Approximate large margin methods for structured prediction." Proceedings of the 22nd international conference on Machine learning. 2005.

### Weaknesses
1. While the author keeps claiming throughout the paper that SCRG can improve the generation diversity of the student model, there is a lack of empirical evidence, e.g. distinct n-grams.
2. SCC is notably complex, and its underlying intuition isn't clearly explained. I found it hard to understand why the authors didn't simply optimize for semantic similarity between corresponding spans in the student and teacher models.
3. Also, SCC relies on an external chunker to extract spans like noun phrases and verb phrases. This requirement limits its generalizability in low-resource languages that lack such tools.
3. DAC-KL, too, seems unnecessarily complicated due to the need for an additional network to determine the clipping threshold for logits. I'm not sure it's necessarily complicated to reach the same level of performance. There are existing simpler alternatives of selective distillation [1] [2], but the author doesn't compare the proposed method against them.
4. As shown in Table 1, the performance improvements offered by the proposed methods over the best baseline methods appear marginal, generally less than 1 ROUGE score, with the exception of the OPT model. Table 2 also indicates that most of the observed improvement stems from DAC-KL, while the contributions of other objectives are comparatively minor.
5. Only use the ROUGE-L metric, while previous work (e.g. miniLLM) also adopts GPT4-feedback and human evaluation.

### Questions
1. Do you have any idea why the margin is significant for OPT but much smaller for the other base LLMs?
2. Did you run any statistical significance tests for Table 1 & 2?
3. See Weakness 1, 2, 4, 6.
4. Typos: Fig1(b) "Studnet-generated"

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel method of performing Knowledge Distillation from a larger teacher model. This paper proposes to improve the offpolicy method (DistiLLM) by performing sequence level correction and regeneration. The paper also introduces two different loss functions namely Token level DAC-KL and Span level correlation consistency. Token level DAC-KL helps a much smaller student learn the teach distribution much more effectively by using the higher density classes. Span level loss function helps to transfer semantic knowledge from the teacher to the student. The authors provide a experiments across various model types and sizes.

### Strengths
1. The SCRG strategy is really quite simple and novel. I really love how simply and efficiently this can be integrated into current distillation pipelines

2. I really like the experiments sections as it is pretty comprehensive with lots of experiments on a lot of different models and different evaluation benchmarks.

3. As someone who has thought a lot about how less expressive students fail to mimic a more complex teacher using forward KL, I really appreciate how easy and simple the token level DAC-KL loss function is. 

4. I also appreciate the authors providing human evaluations.

### Weaknesses
1. A small nitpick. It would be really great if the captions of the images and tables could be a bit longer and more informative.

### Questions
1. People have noticed that using a much much more complex teacher than the student can lead to worse results. I was wondering if the token level DAC loss would resolve this potentially. I understand it is tough to run experiments on short notice but it would be really great to have a comparison between vanilla KD loss and Token level DAC loss when trying to use a 2B student (or even smaller) and a 13B teacher. You can use Qwen models for the experiment or Pythia.

2. The authors of [1] try to just use the top 5% of the logits. I was wondering how does simply doing that compare to the token level DAC loss. 

[1] Raman, Mrigank, et al. "For distillation, tokens are not all you need." NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following. 2023.

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
This paper presents a novel approach that employs a multi-granularity semantic revision framework to distill knowledge from large language models into smaller, more efficient ones. Key contributions include targeting different levels of semantic representation—word, sentence, and document—allowing for the capture of essential information without excessive complexity. The authors detail specific techniques for revising and refining semantics at each granularity level. Additionally, extensive experimental results demonstrate that their method significantly improves the performance of smaller models on various dataset compared to existing distillation techniques.

### Strengths
1. This paper proposes an innovative multigranular semantic revision method as a comprehensive extension of existing knowledge distillation techniques. The method conducts meticulous revisions at three key levels: the sequence, the token, and the span, constructing a comprehensive framework that enhances the knowledge distillation performance of LLMs.

2. The proposed method demonstrates high generality, allowing for seamless integration with existing on-policy and off-policy strategies.

3. This paper conducts extensive experiments across various models and datasets, effectively demonstrating the validity and broad applicability of the proposed method.

### Weaknesses
1. The multi-granularity semantic revision method proposed may require more computational resources, particularly during sequence-level regeneration, which could prolong model distillation time. As illustrated in Table 4(b), the efficiency of the proposed method is lower than that of MiniLLM. Therefore, I would like to know the comparison results between the method proposed in this paper and the baseline under the same computational cost or the same training time.

2. ExAccErr measures the relative error caused only by exposure bias. I understand that this value is expected to be as low as possible. However, in Table 4(a) of this paper, the value for the authors' method is higher than that of previous methods, which is inconsistent with other experimental results. Additionally, the authors mention in line 515, "This analysis explains why the distilled student models generally outperform the teacher models." I believe that the experimental results do not support the conclusion in line 515, and I would expect the authors to provide more explanation here.

3. Although the authors assert that SCRG can improve the diversity of the generated results, I would like to see more experimental results or discussions to support this claim.

### Questions
See weakness.

### Soundness
4

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
The authors propose three separate ideas for knowledge distillation: 1) using student-generated samples for distillation, but also correct them if it’s not the same as the teachers generated, 2) adaptively clipping the distribution before applying the KL loss, and 3) applying a span-level loss, where the goal is to match the between-token correlation within each span.

Update: I followed the authors' arguments for exposure bias, and I would like to thank Reviewer S2Y9 for chiming in and pointing out some flaws in the arguments.

I want to add that I am aware of the scheduled sampling paper. My point was that despite addressing exposure bias, it's not been a popular technique for LLMs, making me believe exposure bias isn't as important as the authors claim. In fact, more recent papers (e.g., [1]) have shown that maybe exposure bias is not a big problem.

Looking at the generations the author showed "Men’s lacrosse has a limited amount of time to play play play as as as as as as as as as as as as as as as as as as as", I feel a big reason for the improvement is that the student is too poor, as it cannot even avoid simple repetitions that should have never occurred in the training data.

Overall, I am raising my score to 5 (i.e., still a bit negative). I think a more detailed analysis of exposure bias can significantly strengthen the paper (e.g., including scheduled sampling as a baseline), as it appears central to the authors' claims.

[1] https://aclanthology.org/2021.emnlp-main.415/

### Strengths
1. The authors perform experiments across a wide range of models and datasets.
2. The authors compare with a variety of baselines.

### Weaknesses
1. The intuition for correcting the distillation dataset is unclear. If you keep correcting it to be the same as the teacher’s generation, it is almost equivalent to simply using the teacher’s outputs as the distillation dataset. It would be ideal to have a comparison with the teacher's samples (or maybe I missed it).
2. The authors lack detailed analyses about the clipping method. For example, it would be much better if the authors can show what the predicted clipping thresholds are, and how that compares with simply using the mean of these clipping thresholds.
3. No detailed analyses for the span loss. Although the authors show span-level correlation can improve performance in the ablation study, the authors do not study the different designs, e.g., correlation measure, chunking methods, etc.

### Questions
The ablation study does not provide a full picture of how important each techniques is. I am curious about how these methods work in separation.

### Soundness
3

### Presentation
3

### Contribution
2
