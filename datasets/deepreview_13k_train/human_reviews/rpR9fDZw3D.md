# Don’t Throw Away Data: Better Sequence Knowledge Distillation

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
A critical component in knowledge distillation is the means of coupling the teacher and student. 
The predominant \emph{sequence knowledge distillation} method involves supervised learning of the student against teacher-decoded outputs, and is exemplified by the current state of the art, which incorporates minimum Bayes risk (MBR)  decoding. 
In this paper we seek to integrate MBR more tightly in distillation training, specifically by using several high scoring MBR translations, rather than a single selected sequence, thus capturing a rich diversity of teacher outputs. 
Our experiments on English to German and English to Japanese translation show consistent improvements over strong baseline methods for both tasks and with varying model sizes. Additionally, we conduct a detailed analysis focusing on data efficiency and capacity curse aspects to elucidate MBR-$n$ and explore its further potential.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on improving sequence knowledge distillation by extending minimum Bayes risk (MBR) decoding, calculating loss for top-n MBR decoded sequences instead of a single one. The authors conducted extensive experiments on translation tasks on high-resource (en-de) and medium-resource (en-jp) translation tasks, showing the improvement of their MBR-n approach over baseline methods in terms of model size scaling, data efficiency, showing the effectiveness of their proposed approach.

### Strengths
1. Simplicity: The paper proposes a simple and generalized method to improve existing knowledge distillation methods (MBR) by aggregating losses of multiple MBR decoded sequences.
2. Extensiveness of experiments: The authors conducted extensive experiments on en-de and en-jp translation tasks, providing convincing evidence that MBR-n improves over baseline methods and the vanilla MBR for the most part over various model, data, and training configurations.

### Weaknesses
1. Manuscript requires further polishing: While the writing of the manuscript is mostly coherent and easy to follow, there are several places that can use some further polishing, including but not limited to: 

a) Multiple typos (such as "MRB-n outperforms MBR", "shown in Talbe 1" in section 4, etc.) 

b) In section 4, the subsection titles are not uniformly formatting, that is, some titles are full sentences (MBR scoring is important); some adopt headline grammar (KD better than Reference-based training); and some do not summarize the finding of their subsections like the others (Teacher performance, Diversity, etc.)

2. Not enough novelty: The approach proposed in the paper seems more like a naive engineering increment upon the already existing MBR decoding approach. e.g. It would have been great if the authors had paid more attention to how the runtime convergence could be improved.

3. Confusing experimental setups: Teacher models (XXS, XS, S, L) are obtained in 3 different ways. This makes it hard to compare the effect of MBR-n in model scaling since it is not strictly one-factor-at-a-time.

4. Insufficient result interpretation: 

a) The overall performance increment does not seem substantial, especially for models distilled from larger teacher models, or fine-tuned student models. Could have expanded on the Staged traininig experiments in section 4 and incorporated curriculum learning in the proposed approach to address the capacity curse.

b) In Section 4 Diversity, no explanation is made over why MBR-n student models have high diversity when n is small, and the diversity decreases when n is larger.

c) The method is expectedly not as efficient as the vanilla MBR in terms of runtime efficiency, but is more data efficient. Could have evaluated the overall efficiency between different methods during training by unifying the two aspects with a custom metric.

### Questions
1. Have you considered improving the runtime efficiency or addressing the capacity curse of the proposed methods on top of the naive approach of aggregating losses of multiple MBR sequences?

2. Could you provide experiments with teacher models obtained in the same way? Or can you explain the reason for this setup? For example, is it because that the performance margin for larger models between MBR-n and other approaches dimninishes even more when teacher models is stronger?

3. Could you explain the phenomenon where MBR-n with larger n gives lower diversity? Is there a better metric to evaluate the diversity of the outputs?

4. Could you provide overall efficiency evaluation unifying runtime efficiency and data efficiency and compare between baselines and your approach?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors build on existing MBR methods to generate samples for distillation. While it is a well-known approach, the authors’ main discovery is that instead of using one MBR sample, using multiple MBR samples can be better.

### Strengths
1. The authors study knowledge distillation, which is an important research direction to make LLMs more accessible.
2. The authors have efficiency analysis, showing their approach is linearly slower in terms of number of samples used.

### Weaknesses
1. Lack of novelty. The authors propose to use multiple samples from MBR for distillation, which is essentially tuning a hyper-parameter of an existing approach rather than a novel method.
2. Little gain for the extra training. As shown in Table 2, even using 40 times as much training data, the performance can be as little as ~0.02 in the XXXS student setting. The performance can even degrade in many cases for the XXS student setting.
3. No analysis about the number of candidates required. The current approach is slow, not only because the authors require 40 times training samples; it is also slow because for each input, the authors generate 256 candidate samples for MBR to select from. This could be impractical for most scenarios.

### Questions
How similar are the top-n MBR samples?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel technique for knowledge distillation (KD) of large language models (LLMs), named MBR-n. By utilizing multiple outputs scored by MBR, the student model could better capture the teacher's distribution, leading to enhanced performance. The extensive experiments cover en-de and en-jp translation tasks, involving various configurations of student and teacher models, showing the effectiveness of MBR-n on the KD.

### Strengths
This paper proposes an effective knowledge distillation method to enhance the translation capabilities of large language models with relatively small sizes, outperforming traditional sequence-level knowledge distillation methods based on beamsaerch.

### Weaknesses
1. The MBR method was proposed a long time ago, and the author merely uses MBR to generate candidates for the Teacher model, lacking a certain degree of innovation.

2. The author's introduction to the MBR method is not detailed enough, which may confuse readers.

3. Most of the experimental results are compared with beam search-based baselines, lacking comparisons with more KD (Knowledge Distillation)-related work, such as https://aclanthology.org/2023.emnlp-main.178/

### Questions
1. Regarding the experimental results in Table 2, why is it that the larger the size of the Teacher model, the worse the translation quality (i.e., the lower the BLEURT score) of the distilled Student model? Please provide a detailed explanation.

2. Why did the authors choose PaLM as the baseline model? Did you ever try using the LLaMA language model or the BLOOM multilingual large model?

3. Why was zero-shot used when generating translation candidates using the Teacher model? Have you compared the impact on the Student model's performance when using the few-shot method to generate translation candidates?

4. Does using MBR to generate translation candidates for knowledge distillation have a significant impact on training efficiency? Would like to see a comparison of the training efficiency among Reference, Beam, and MBR.

5. Intuitively, the method proposed in this paper mainly aims to enhance the diversity of translations, right? Besides, are the references in the test set single-reference or multi-reference during the evaluation? If the evaluation is based on multi-reference, it is reasonable for the translation quality to improve. However, if it is based on single-reference, I think there should not be a significant improvement in translation quality, right?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces MBR-n, a novel approach to enhance sequence-level knowledge distillation (SeqKD) for translation tasks. The approach extends the Minimum Bayes Risk (MBR) decoding methodology by utilizing multiple high-quality teacher outputs instead of a single output for distillation training. The authors demonstrate that this method improves student model performance in machine translation across different language pairs and model sizes, particularly when using high-capacity teacher models.

### Strengths
1. MBR-n’s use of multiple high-MBR-scoring candidates for distillation presents a more comprehensive knowledge transfer from teacher to student.
2. Simple and effective method with comprehensive analysis.

### Weaknesses
1. Line 84, I'm confused by "confirm the capacity gap curse is an open issue", what do the authors mean by "open issue"
2. Figure 2, by `beam`, does the authors means using the top1 output as the KD target generated by beam search? Do the authors try like Beam-n methods?
3. While MBR-n outperforms MBR-1, the computational cost is also n times, whether teacher MBR generation and KD process. Even though the authors claim that MBR-n is more data efficient, the experiments are mostly on small size of data. Larger orders of magnitude of the data scale would make the results more convincing.
4. More experiments on more language pairs would make the results more convincing
5. Other than BLEU, BLEURT, better translation evaluation metrics, e.g, COMET should be taken into consideration [1]

### Questions
Please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
