# Continual Contrastive Spoken Language Understanding

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Recently, neural networks have shown impressive progress across diverse fields, with speech processing being no exception. However, recent breakthroughs in this area require extensive offline training using large datasets and tremendous computing resources. Unfortunately, these models struggle to retain their previously acquired knowledge when learning new tasks continually. In this paper, we investigate the problem of learning sequence-to-sequence models for spoken language understanding in a class-incremental learning (CIL) setting and we propose COCONUT \emojismiley, a CIL method that relies on the combination of experience replay and contrastive learning. Through a modified version of the standard supervised contrastive loss, COCONUT preserves the learned representations by pulling closer samples from the same class and pushing away the others. Moreover, we leverage a multimodal contrastive loss that helps the model learn more discriminative representations of the new data by aligning audio and text features. We also investigate different contrastive designs to combine the strengths of the contrastive loss with teacher-student architectures used for distillation. Experiments on two established SLU datasets reveal the effectiveness of our proposed approach and significant improvements over the baselines. We also show that COCONUT can be combined with methods that operate on the decoder side, resulting in further metrics improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper targets end-to-end SLU using a seq2seq style of model.
- This work aims to address problems of balancing efficient and performant continual learning of new tasks (intents) without the effects of catastrophic forgetting.
- To these ends, they introduce a model architecture and set of losses to take advantage of student-teacher network training, contrastive learning, and multi-modal (speech/text) alignment.
-  The approach (COCONUT) is applied to two datasets, FSC and SLURP, where the approach is highlighted.
- COCONUT is shown to outperform other methods in almost all cases, except when combined with the next best approach (S-KD) or when using a larger memory for ER.
- Ablation shows impact of memory size on effect of COCONUT vs ER.

### Strengths
Clear presentation of motivations behind the combination of losses, the decisions behind whether to use student vs teacher examples, etc.  Nice figures and appropriate complexity to educate without losing the goal of the paper in the weeds.

### Weaknesses
For readers that may not be as familiar with results of other SLU work (both E2E and non-E2E), inclusion of results from other work could be useful. Or if such comparisons are not fair, perhaps a note in the table to that effect. The text mentions the other work which describes those rows (like S-KD), but it could be nice to see numbers from other work itself as well (?) for clearer context as well as results of conventional SLU approaches that are not E2E.

Also, one grammar note, I believe "sensible" should be "sensitive" here in the last paragraph of section 5.3:
          Note that, however, the model does not seem very sensitive to the temperature for the Avg Acc, whereas the Last Acc is more influenced.

### Questions
It may be possible to better include results from prior work and non-E2E approaches to give more context to the results within the tables.

Also, one grammar note, I believe "sensible" should be "sensitive" here in the last paragraph of section 5.3:
          Note that, however, the model does not seem very sensitive to the temperature for the Avg Acc, whereas the Last Acc is more influenced.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses spoken language understanding (SLU) in a continual learning setting. End-to-end joint ASR-SLU approach is used (no cascade).
A new approach called COCONUT is presented that uses both experience replay and contrastive learning losses (NSPT: a contrastive KD loss and MM a multimodal loss that aligns audio-text representations).
Experiments are made on two SLU benchmarks: SLURP and FSC; the exact SLU task is intent classification. The continual learning setting used is the one from (Capellazzo & al 2023). Experiments show that COCONUT can compete with experience replay  (ER) of buffer capacity of 1% (but is worse than ER with buffer capacity 2%)

### Strengths
-a new approach for SLU in a CL setting that is better than a strong experience replay (ER) benchmark

-experiments on 2 popular SLU benchmarks that demonstrate the effectiveness of the proposed appproach

### Weaknesses
 -more details on continual learning setting used would have been welcome (ref to (Capellazzo & al 2023) is not very self-explanatory)

-experience replay (ER) baseline with buffer capacity of 2% is still better than COCONUT and it is unclear how using twice memory (2% instead of 1%) is a real bottleneck in real applications (authors could have commented this more)

### Questions
-how COCONUT could be adapted to more speech tasks ?

-experience replay (ER) baseline with buffer capacity of 2% is still better than COCONUT and it is unclear how using twice memory (2% instead of 1%) is a real bottleneck in real applications (authors could have commented this more)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a contrastive learning framework to overcome catastrophic forgetting in the class-incremental learning setting of spoken language understanding, which contains two main losses. First, the paper modifies the standard supervised contrastive loss from Negative-Teacher Positive-Teacher to Negative-Student Positive-Teacher, while applying loss on rehearsal samples only. Second, a multimodal contrastive loss is also use to align the audio and text features.

### Strengths
1. The modification of loss function is interesting to mitigate catastrophic forgetting for seq2seq SLU models.
2. Experiments on two benchmarks and the ablation studies verify the effectiveness of proposed method over the previous baselines, as well as the two proposed losses.

### Weaknesses
The main weakness of this paper is the unclearness in text and the insufficient in experiments. Please see the Questions part for details.

1. For the design of NSPD loss, 1) since the author highlights that the NSPD loss is conducted only on rehearsal samples, what if the loss is conduct on all samples?; 2) In equation 5, why i belongs to I instead of I_c? (according to the figure 2, it seems that the repulsion is applied on new class (i.e., I_c) samples).
2. For the design of multimodal loss, when the loss is applied, only in the first task (to initialize the projection) or in every task? I think the main motivation of this paper is to overcome catastrophic forgetting. However, the multimodal loss is more like a trick for better results instead of for catastrophic forgetting? By the way, is this paper the first work to apply multimodal loss on SLU tasks?
3. For the text encoder, in my understanding, it is just an embedding layer instead of a module? If this is the case, I think there is no need to call it text encoder. For example, this kind of embedding layer also exists in GPT-3.5. But it is common to call that GPT-3.5 has only a text decoder (decoder-only structure) instead of a text encoder (embedding layer) and an auto-regressive decoder. The text encoder in the paper is quite confusing. Please let me know if I understand mistakenly.
4. For the experiments, 1) More results are needed at different ER ratio (2-4%, 5-10%) to show that the proposed method can produce consistent improvement in different settings. 2) Just a question, why the results on FSC-6 in Table 1(76.46) and Table 2(77.09) are different?

### Questions
1. For the design of NSPD loss, 1) since the author highlights that the NSPD loss is conducted only on rehearsal samples, what if the loss is conduct on all samples?; 2) In equation 5, why i belongs to I instead of I_c? (according to the figure 2, it seems that the repulsion is applied on new class (i.e., I_c) samples).
2. For the design of multimodal loss, when the loss is applied, only in the first task (to initialize the projection) or in every task? I think the main motivation of this paper is to overcome catastrophic forgetting. However, the multimodal loss is more like a trick for better results instead of for catastrophic forgetting? By the way, is this paper the first work to apply multimodal loss on SLU tasks?
3. For the text encoder, in my understanding, it is just an embedding layer instead of a module? If this is the case, I think there is no need to call it text encoder. For example, this kind of embedding layer also exists in GPT-3.5. But it is common to call that GPT-3.5 has only a text decoder (decoder-only structure) instead of a text encoder (embedding layer) and an auto-regressive decoder. The text encoder in the paper is quite confusing. Please let me know if I understand mistakenly.
4. For the experiments, 1) More results are needed at different ER ratio (2-4%, 5-10%) to show that the proposed method can produce consistent improvement in different settings. 2) Just a question, why the results on FSC-6 in Table 1(76.46) and Table 2(77.09) are different?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a continual learning method, COCONUT, for spoken language understanding. This method uses two contrastive learning objectives in order to mitigate the catastrophic forgetting issue. COCONUT is evaluated on two popular SLU datasets, FSC and SLURP. Results show that COCONUT outperforms baselines when combined with some knowledge distillation techniques. A thorough ablation study is also presented to show the importance of the design of both contrastive losses.

### Strengths
**Originality**: The modified version of the proposed contrastive loss, Negative-Student Positive-Teacher loss, is novel.

**Quality**: The paper has presented detailed and thorough analysis of experimental results. However, the results of the proposed method is not strong enough.

**Clarity**: The writing of this paper is coherent.

**Significance**: The paper has some impact on the speech community, especially those working on spoken language understanding. The design of NSPT loss can be applied to other tasks, both within the speech domain and in other modalities.

### Weaknesses
(1) COCONUT does not outperform other baselines in a more challenging dataset (SLURP), limiting its contribution.

(2) The architectural design of COCONUT is rather complicated and onerous.

### Questions
What is the running time of COCONUT compared to other baselines? Does it cost significant more time to run COCONUT?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
