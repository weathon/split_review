# Connect, Collapse, Corrupt: Learning Cross-Modal Tasks with Uni-Modal Data

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Building cross-modal applications is challenging due to limited paired multi-modal data. Recent works have shown that leveraging a pre-trained multi-modal contrastive representation space enables cross-modal tasks to be learned from uni-modal data. This is based on the assumption that contrastive optimization makes embeddings from different modalities interchangeable. However, this assumption is under-explored due to the poorly understood geometry of the multi-modal contrastive space, where a modality gap exists. In our study, we provide a theoretical explanation of this space's geometry and introduce a three-step method, $C^3$ (Connect, Collapse, Corrupt), to bridge the modality gap, enhancing the interchangeability of embeddings. Our $C^3$ method significantly improves cross-modal learning from uni-modal data, achieving state-of-the-art results on zero-shot image / audio / video captioning and text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the modality gap phenomenon in multimodal learning. Specifically, the authors claim that the modality gap emerges and is preserved due to a) dimensional collapse during initialization and training, and b) alignment noise controlled by temperature. To overcome the modality gap, this paper proposes the C^3 paradigm by subtracting mean of features and add Gaussian noise before decoding the features. Experiments on four tasks involving three modalities show the efficacy of C^3.

### Strengths
1.	The paper is well written and easy to follow. The empirical analysis well presents and supports the claims on modality gap, a significant problem in multimodal learning.
2.	Experiments are extensive. The authors experiment on image, text and audio modalities, and the results prove the method is applicable across various tasks.

### Weaknesses
1.	My major concern is about novelty. [1] has pointed out that random initialization and contrastive learning causes and preserves modality gap, and [2] has modeled modality gap as a constant orthogonal to image and text span. The proposed C^3 is also an ensemble of existing methods [2][3][4]. Especially, the cross-modal transferability in [2] seems quite similar to the ``interchangeability of embeddings from different modalities’’ in this paper. Please justify.
2.	This paper proposes to align representations from different modalities but without convincing justification. In fact, it remains uncertain what effects are relevant to aligning modalities. [1] reports that making the modality gap too small or too large harms performance. [5] proves that strictly aligning modality representations is suboptimal. Therefore, I suggest adding reasons for aligning modalities.
3.	Despite that the authors have conducted experiments on various tasks, the comparison with existing methods is limited. Most comparisons in this paper are ablating over different components in C^3. Tab.2 shows marginal improvement over CapDec without reporting std over independent runs, which is not convincing. Tab.3, Tab.4 and Tab.5 report few comparisons with SOTA methods.

[1] Liang, Victor Weixin, et al. "Mind the gap: Understanding the modality gap in multi-modal contrastive representation learning." 
[2] Zhang, Yuhui, et al. "Diagnosing and rectifying vision models using language." 
[3] Radford, Alec, et al. "Learning transferable visual models from natural language supervision." 
[4] Zhou, Yufan, et al. "Towards language-free training for text-to-image generation." 
[5] Jiang, Qian, et al. "Understanding and constructing latent modality structures in multi-modal representation learning."

### Questions
1.	From the experiment results, $C_2^2$ seems to be much more effective than $C_1^2$. Why?
2.	Section 3.2 mentions the effect of temperature, but no discussion is given in experiments. What are the effects of modifying temperature in stage 1 and std of Gaussian in stage 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the geometry of embedding spaces obtained through multi-modal contrastive learning (e.g. CLIP), collecting interesting insights and using these to motivate a simple-yet-effective 3-step approach to improve the performance of cross-modal tasks learned using uni-modal data.  In particular, the study suggests, both empirically and theoretically, that the difference between embeddings from different modalities originates from two components: i) a modality gap caused by ineffective dimensions being initialized differently in the two modalities and remaining constant during optimization, and ii) alignment noise that can be approximated as gaussian. The paper then suggests reducing this gap by centering the embeddings at both training time and inference time and adding noise during training. Experiments finally show that the suggested modifications result in state-of-the-art results across a wide set of cross-modal tasks.

### Strengths
### Originality

- The paper studies the poorly-understood geometry of latent spaces obtained through multi-modal contrastive learning, building on top of existing works and integrating new insights into an overall recipe to improve cross-modal tasks using such spaces.
- While two out of 3 steps in the CCC method are not novel, the motivation behind the overall framework is a valid contribution, as well as the need of collapsing the ineffective dimensions by subtracting the mean to the embeddings.
- The finding of the modality gap being orthogonal to the text and image spaces is interesting and well motivated.

### Clarity

- The paper is well written and pleasing to read.
- The concepts are explained both rigorously and more colloquially.
- The experiments are well motivated, and their results properly discussed.

### Significance

- The theoretical framework looks solid: the difference of initialization and the lack of gradients for the ineffective dimensions convincingly explains the modality gap.
- The empirical analyses make intuitive sense.
- The framework results in improvements over a wide set of tasks (image/audio/video captioning and text-to-image generation), proving its general applicability.
- The codebase looks carefully developed and seems free from glaring bugs.

Overall, the paper tackles an extremely interesting question that many practitioners share: “how does, and possibly how should, a multi-modal space look like?” and attempt to characterize its geometry with simple yet convincing tools. Both the theoretical and empirical analyses make intuitive sense, and the empirical results on the considered tasks confirm the utility of its findings.

### Weaknesses
- The discussion on the alignment noise could be improved: in particular, the results in Table 1 are left for the reader to infer. The same statistics could also be easily computed upon any other modality combination in the appendix, it would be useful to see if it still applies.

### Questions
- Since the modality gap is due to the dimensional collapse, would reducing the dimensionality to the effective one help overcoming the issue?
- Is there any relation between the decomposition of the modality gap with the content-style-modality specific decomposition assumed e.g. in [1]? Briefly, each latent vector in a multi-modal contrastive learning space is there assumed to have a part that is shared across modalities, i.e. the content, one that is shared but with some distortion, i.e. the style, and one that is not shared at all, i.e. the modality-specific component. Is it possible that the modality specific component in [1] is just the constant component caused by the different initializations seen in this work?
- The solution to the modality gap is to center the embeddings, implying the modality gap is just a shift. Isn’t it possible that the difference in modality may also result in different scales?

[1] Daunhawer, I., Bizeul, A., Palumbo, E., Marx, A., & Vogt, J. E. (2022, September). Identifiability Results for Multimodal Contrastive Learning. In The Eleventh International Conference on Learning Representations.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides a theoretical understanding of the geometry of the multi-modal contrastive representation space, which is related to the modality gap and alignment noise. Based on this, it presents a new 3-stage framework, called C3 (Connect, Collapse, Corrupt), for solving cross-modal tasks using single-modal data. C3 can effectively bridge the modality gap and enhance the interchangeability of embeddings in the shared representation space. The paper demonstrates the empirical effectiveness of C3 by showing that it achieves state-of-the-art results in various cross-modal tasks.

### Strengths
1. Theoretical Insight: The paper's theoretical understanding of the geometry of the multi-modal contrastive representation space is a significant contribution. It also helps shed light on the challenges related to the modality gap (by showing that it is attributed to the joint effect of initialization and optimization), which is the key issue in multi-modal/cross-modal learning.

2. C3 Algorithm: The rationale behind the proposed C3 method is sound and well-explained. Even though each individual step has been explored by previous work, the combination of them leads to very competitive performance on a variety of tasks compared with recent strong baselines (as shown in Table 2-3). The paper also provides comprehensive ablation studies and qualitative examples to understand the effect of each component.

3. Presentation: The presentation is clear, and the ideas are easy to follow. The visuals also help illustrate the effectiveness of the proposed method. The current submission does not include code, hopefully the authors can release them later to facilitate future research.

### Weaknesses
The proposed C3 algorithm has limited novelty on its own given that each step has been studied in previous work. However, the combination of these steps is new and well-motivated by the theoretical framework developed in this paper, which mitigates the lack-of-novelty issue.

### Questions
1. How is the "Collapse" step implemented (i.e., computing e_x' and e_y')? Is it the same as batchnorm?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the space's geometry of the features learned by contrastive learning and finds there is a modality gap in such feature space. To bridge the modality gap, based on the analysis of the geometry, they propose a three-step method called C^3 (Connect, Collapse, Corrupt). They conduct experiments on zero-shot image/audio/video captioning and text-to-image generation.

### Strengths
1. The discussion about the gradient direction in contrastive optimization in Lemma 1 sheds light on how the features learned by contrastive learning are processed.
2. The theoretical analysis and experiment results of the alignment noise are reasonable and effective.

### Weaknesses
1. The abstract and introduction emphasize the importance of the modality gap of the feature space, 
however, the results in the experiments seem show that the key component is the alignment noise. 
For instance, in Table 2, C_2^2 (only use connect and corrupt) can achieve a similar performance as the C^3.
Compared to C^1, only adding collapse boost 16.3 but 41 when only adding alignment noise.

2. In section 3.3, it provides some statistic values to show the space geometry. 
I think such statistics may not actually reveal the space geometry since it averages all possible values.
Is that better to provide a histogram of such statistics to demonstrate the space geometry?
Furthermore, based on the constant modality gap analysis, is that the E_{i,j}[cos(d_i,d_j)] should have a value close to 1 since they should be parallel except for the noise effect.

3. The experiments are conducted on generation tasks, the quantitative performance is similar for the method and baseline,
while in the qualitative examples, I can not tell which method is better based on three examples. It will be better to provide more qualitative examples.

### Questions
1. In the analysis of the space geometry of contrastive features, the paper proposes that the modality gap is a constant vector and orthogonal to each modality. But it can not be derived easily that why the modality gap is the constant vector from the dimension collapse as mentioned in section 3.1. Are there any formal propositions for the constant modality gap vector in the initialization stage?

2. The paper aims to mitigate the modality gap between feature space of different modalities, but in the generation task or encoder/decoder-based architecture, is that the closeness of the features from different modalities indicate a better generation performance? I think it would be better to refer to previous works or conduct this kind of experiment to show the assumption of this paper is true in real applications.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
