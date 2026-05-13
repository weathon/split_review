# What to align in multimodal contrastive learning?

- Decision: Accept
- Scores: 3, 6, 8, 8

## Abstract
Humans perceive the world through multisensory integration, blending the information of different modalities to adapt their behavior. Contrastive learning offers an appealing solution for multimodal self-supervised learning. Indeed, by considering each modality as a different view of the same entity, it learns to align features of different modalities in a shared representation space.  However, this approach is intrinsically limited as it only learns shared or redundant information between modalities,
while multimodal interactions can arise in other ways. In this work, we introduce \textbf{CoMM}, a \textbf{Co}ntrastive \textbf{M}ulti\textbf{m}odal learning strategy that enables the \textbf{comm}unication between modalities in a single multimodal space. Instead of imposing cross- or intra- modality constraints, we propose to align multimodal representations by maximizing the mutual information between augmented versions of these multimodal features. Our theoretical analysis shows that shared, synergistic and unique terms of information naturally emerge from this formulation, allowing us to estimate multimodal interactions beyond redundancy. We test CoMM both in a controlled and in a series of real-world settings: in the former, we demonstrate that CoMM effectively captures redundant, unique and synergistic information between modalities. In the latter, CoMM learns complex multimodal interactions and achieves state-of-the-art results on the six multimodal benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a multimodal representation learning method that uses multimodal augmentations to learn all four multimodal interaction terms. The proposed optimization terms are designed to optimize for $R + U_i$ and $U_1 + U_2 + R + S$. The authors design a multimodal encoder+fusion architecture that achieve state-of-the-art performance on several MM benchmarks.

### Strengths
This paper grounds multimodal representation learning in the theoretical framework of multimodal information theory. Lemma 2 & 3 offer insight into novel methods that can be applied to learn multimodal representations with beyond redundancy.

### Weaknesses
I have strong doubts about the soundness of the theoretical foundation of this paper:
1. Assumption 1 assumes the existence of a multimodal augmentation $t$ such that $I(X; t(X)) = I(X; Y)$. This means that if $X$ contains more information than the label $Y$, $t(X)$ has to "reduce" the information in $X$ down to $Y$. This is different from just "label-preserving multimodal augmentation". The experiments section also offers little insight about how exactly this augmentation is carried out. The augmentations mentioned for real-world datasets, including cropping, jitter, etc., looks like they certainly would lead to $I(X; t(X)) \gg I(X; Y)$. This would be a direct contradiction of Assumption 1. The paper lacks a clear explanation of how these augmentations are designed to satisfy the assumption, particularly when considering that typical augmentations often introduce more variability rather than reduce information content to match the label.
2. Moreover, for the pretraining paradigm used on real-world datasets, we don't even know at pretraining time what the task $Y$ is yet. Correct me if I'm wrong--it's not clear to me how it is possible for this assumption to hold. The assumption seems to require knowledge of the downstream task during pretraining, which is not the case in standard self-supervised learning scenarios. This makes the theoretical grounding questionable for the practical application of the method.
3. The real gains from this method seems to be the aggressive mutual information optimization between all pairs of single modalities and all modalities as well as all data augmentations. The paper does not sufficiently disentangle the effect of the proposed theoretical framework from the aggressive mutual information optimization, making it difficult to assess the true contribution of the theoretical component.

### Questions
See Weaknesses for questions about theoretical foundation of this paper.

In Lemma 2, it is shown that optimum is achieved assuming "an expressive enough network". Do we have any idea how big/complex the network needs to be to become an expressive enough network? How does performance scale with your network's size, etc.?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed CoMM, a Contrastive Multimodal learning framework, that captures multimodal interactions and aligns multimodal representations by maximizing the mutual information between augmented versions of these multimodal features. The paper shows that, under certain data augmentation, this framework can capture uniqueness and synergy better than existing work. Empirically, it is also shown that such framework facilitates multimodal learning on various multimodal benchmarks.

### Strengths
1. **Novel multimodal interaction learning under a contrastive learning framework**: the proposed CoMM framework is both theoretically and empirically shown to be able to capture uniqueness and (especially) synergy better than prior work.
2. **Comprehensive evaluation and careful ablation**: the proposed method is evaluated on a wide range of multimodal benchmarks, which involves diverse tasks, all requiring different level modeling of interactions. The paper conducts careful ablation in analyzing the importance of each part of the loss in capturing different interactions, which has provided insights in how those interactions are learnt with the proposed framework.

### Weaknesses
 1. **Need for clarification about the Multi-view redundancy assumption**: the paper introduces the Multi-view redundancy assumption (Definition 1) to highlight the insufficiency of several existing works that propose cross-modal contrastive learning. Specifically, the paper shows that under this assumption, which states that "most task-relevant information is shared across modalities", cross-modal contrastive learning is primarily learning the redundancy interaction while ignoring the others interactions (uniqueness and synergy). The reviewer has the following questions:

    1. it is unclear how applicable this assumption is in the realistic settings: in fact, as many prior work estimating multimodal interaction in real-world multimodal datasets show, multimodal tasks can vary by a diverse range of combinations of those interactions;

    2. given this assumption, it seems that capturing redundancy would be sufficient already to learn task-relevant information, what makes it necessary to go beyond learning redundancy;

    3. do those existing contrastive learning frameworks still capture primarily redundancy, i.e. does Lemma 1 still hold, without the multi-view redundancy assumption?

2. **Strong assumption of Label-preserving multimodal augmentations (Assumption 1)**: the paper points out that existing methods like FactorCL requires strong and often unrealistic assumption about optimal multimodal augmentations based on conditional augmentations. Instead, the paper relaxes the assumption to label-preserving multimodal augmentations, which is still considered strong, as it is hard to exactly measure the mutual information between the original data and its augmented version $I(X,X')$, as well as between the data and its label $I(X,Y)$ ensuring $I(X,X')=I(X,Y)$ holds in a realistic setting. In fact, in the evaluation, the reviewer does not find any evidence to support that when evaluating on the real-world datasets, the augmentation indeed preserves the label. This not only makes the theory and the experiments detached, but also makes the choice of the "right" augmentation unclear, which is essential to learn the correct objective.
3. **Indirect evidence of CoMM's superior learning of synergy**: the paper highlights the novelty of the proposed framework, CoMM, in better capturing the synergistic interaction than existing methods. However, except Figure 4 (which does not include comparison with the most similar work FactorCL), which is shown on synthetic dataset, the paper does not provide any other direct evidence for showing the claimed superior learning of synergy when evaluating on real-world datasets. For example, a large margin of performance when evaluating on datasets with primary synergistic interaction (and minimal other types of interaction), for example, VQA, will constitute strong evidence to support the claim. Also, it'll be useful to provide estimates of the proportion of different types of interaction within each real-world datasets for evaluation to better understand the advantages of CoMM for modeling different combinations of interactions.
4. **Mysterious number of 50% accuracy for probing synergy**: except for the probing accuracy of synergy for CoMM being 71.87% (which gets round up to 71.9% in Figure 4), the probing accuracy of synergy for all other methods are all 50%. Does this number represent random chance? In other words, how is the probing accuracy of synergy evaluated? Is it only based on presence/absence? In Table 5, it is shown that without the crop augmentation for either modality 1 or modality 2, the synergy interaction seems not to be learnt. What is the intuition for the crop augmentation being the key to learning synergy? Overall, the reviewer feels an insufficient exploration and understanding of modeling synergy (the highlighted novelty of the paper) in the proposed framework, except for a little bit of discussion in the Ablation section (loss function), which only provides a hypothetical explanation.
5. **Missing details about the synthetic experiment setups**: the reviewer does not find documentation about how redundancy, uniqueness, and synergy are defined for the Trifeature dataset or how to control the amount of each type of interaction, in the main text or in the appendix. The paper should provide more details about the synthetic experiment setups, since the original Trifeature dataset is not designed for multimodal learning but rather for feature learning.

### Questions
Regard weakness 1, answering the following questions can help differentiate CoMM from existing contrastive methods and highlight the necessity for going beyond modeling redundancy:
1. How applicable is the Multi-view redundancy assumption in the realistic settings?
2. What makes it necessary to go beyond learning redundancy under the Multi-view redundancy assumption? Why are existing contrastive modeling approaches that focus on primary redundancy interaction insufficient?
3. Without the Multi-view redundancy assumption, i.e. for other tasks, do those existing contrastive learning framework still capture primarily redundancy?

Regard weakness 2, why is the Label-preserving multimodal augmentations (Assumption 1) considered a weaker and more realistic assumption? How can the mentioned mutual information quantity be measured in a realistic setting in order to choose the right augmentations?

Regard weakness 3, the reviewer expects to see more direct evidence that shows the superior modeling of synergistic interaction of CoMM compared to the existing strong methods (e.g. FactorCL) on real-world datasets.

Regard weakness 4, answering the following questions can provide additional insights into how the proposed framework better models synergy:
1. How should a 50% probing accuracy for synergy be interpreted? Is it only based on presence/absence?
2. What is the intuition for the crop augmentation being the key to learning synergy?

Regard weakness 5, please add more details on synthetic experiment setup as previously suggested.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a novel self-supervised learning objective for multimodal representation learning that captures the redundant, unique and synergetic interactions between different modalities. Their proposed approach (CoMM) is composed of a multimodal architecture, with modality-specific encoders and an attention-based fusion mechanism, that encodes a multimodal representation and a novel contrastive learning objective, grounded on the theory of partial information decomposition. The authors extensively evaluate CoMM against other self-supervised objectives, considering datasets of different complexities and number of modalities. The results highlight that the proposed method: (i) is able to capture the proposed interactions; (ii) outperforms other learning objectives in both self-supervised and fine-tuning settings; (iii) can be employed on scenarios with complex modalities (such as images and text) and with more than 2 modalities. Finally, the authors present an ablation study focused on the loss function, fusion module and data augmentation.

### Strengths
- **Originality**:
  - As highlighted by the authors, the use of self-supervision contrastive objectives to learn multimodal representations is not particularly novel (see, for example [1-4] for examples in fully-training and fine-tuning settings). However, the authors focus on the problem of learning not only redundant interactions between the modalities, but also the unique and synergetic interactions. This work seems to follow in line with previous work (FactorCL [6]), extending it to account for synergetic interactions and relaxing the factorization assumption and the need for the use of optimal multimodal augmentations. The use of the Trifeature dataset to quantitively evaluate the effects of redundant, unique and synergetic interactions is quite ingenious and, to the best of my knowledge, novel.

- **Quality**:
   - The work presented here is undoubtedly of high quality. The authors present in depth their main contribution, CoMM, and ground it in the theory of partial information decomposition. The theoretical results, even if not particularly extensive, give a strong support to the proposed method. Furthermore, the evaluation shown in this paper is also of high-quality: the authors evaluate their approach in both controlled and more complex environments, against a wide range of baselines, and the results mostly support the claims of the authors (see "Questions" for more details and experimental clarifications). 

- **Clarity**:
   - The current version of the work is well-written, with no major typos (that I could detect). The authors employ a clear notation throughout the document. Furthermore, the document is easy to read, also due to the intuitive figures created by the authors (the only exception being Figure 1, where it is not clear what does $\mathcal{M}$ refers to). I would, however, recommend that the authors place the "Limitations and Future Work" section of the Appendix in the main document, as it clarifies the current limitations of the method (which is not something necessarly negative) for the reader.

- **Significance**:
   - This work proposes a novel multimodal learning objective that is able to capture a wide range of interactions between multimodal data for downstream tasks. Given the relevance of multimodal representation learning for the current field of AI, the work can have significant impact in both researchers and practitioners.


**References**: 

- [1] Radford, Alec, et al. "Learning transferable visual models from natural language supervision." International conference on machine learning. PMLR, 2021.
- [2] Zhai, Xiaohua, et al. "Sigmoid loss for language image pre-training." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.
- [3] Li, Junnan, et al. "Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation." International conference on machine learning. PMLR, 2022.
- [4] Poklukar, Petra, et al. "Geometric multimodal contrastive representation learning." International Conference on Machine Learning. PMLR, 2022.
- [5] Liang, Paul Pu, et al. "Factorized contrastive learning: Going beyond multi-view redundancy." Advances in Neural Information Processing Systems 36 (2024).

### Weaknesses
My two main concerns with the current version of the work are the following:
- From an architectural point-of-view, the work presents little novelty: the multimodal fusion mechanism, based on concatenation and a transformer block, is also not particularly novel (see, for example, [1], where the authors discuss several works that employ concatenation for multimodal inputs in transformer architectures). Also, despite introducing some novel ideas, the work is still a continuation of FactorCL [2], where the use of partial information decomposition theory was also explored to derive a suitable learning objective (even if a different one from the one proposed).
- The majority of evaluations presented by the authors are in controlled datasets (Section 4.1) or simplified environments (Section 4.2 - Multibench, Section 4.3), where the high-dimensional raw data are preprocessed into low-dimensional feature vectors (as described by the authors on Section 4.2). As such, it is not clear how the learned representations by the proposed method would work on more complex, real-world tasks (beyond the Multimodal IMDB dataset), for example on the ones proposed in [3].


**References**:

[1] - Xu, Peng, Xiatian Zhu, and David A. Clifton. "Multimodal learning with transformers: A survey." IEEE Transactions on Pattern Analysis and Machine Intelligence 45.10 (2023): 12113-12132.

[2] - Liang, Paul Pu, et al. "Factorized contrastive learning: Going beyond multi-view redundancy." Advances in Neural Information Processing Systems 36 (2024).

[3] - Ying, Kaining, et al. "MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI." Forty-first International Conference on Machine Learning.

### Questions
- **1**: The authors claim in the introduction that they evaluate CoMM across "diverse data types (images, text and audio)". However, from my understanding, the datasets used in the MultiBench benchmark are composed of pre-processed features extracted from the original, high-dimensional modalities. Am I correct? Given the use of pre-processed, low-dimensional, features, instead of raw data, it might be a stretch that claiming that the authors evaluate CoMM on audio data. Furthermore, how do you apply label-preserving multimodal transformations to these feature features?
- **2**: How to define the set of label-preserving multimodal transformations? Is it task-dependent? How large does this set need to be to work for your framework. Perhaps a section, even if in appendix, discussing these questions would be quite interesting, especially for practitioners.
- **3**: In Section 4.1., I found it interesting that there is no comparison with FactorCL, since this comparison would emphasize the relevance of the contribution (since, to my understanding, FactorCL cannot capture the synergetic interactions in the dataset). How does FactorCL perform in this controlled experiment?
- **4**: In Table 1, CoMM outperforms the other approaches across most datasets except for MIMIC. Any reason for this? Is there any special feature of the MIMIC dataset?
- **5**: In Section 5, Fusion module, did you also compare to a Concat+Non-linear fusion mechanism?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors proposed CoMM, a novel multimodal contrastive representation learning method that performs multiple InfoNCE contrastive losses between unimodal representations and augmented multimodal representations in the same space. The authors first theoretically justified their approach through information theory and breaking down multimodal interactions into Redundancy, Uniqueness and Synergy. The authors evaluated their proposed method first on a synthetic dataset to show that CoMM can better capture the interactions, and then evaluated CoMM against other self-supervised representation learning methods on many datasets from MultiBench and MM-IMDB with linear evaluation classification accuracy, and CoMM outperformed all baselines. The authors also conducted ablation studies on the training objective and architecture of CoMM on the synthetic dataset.

### Strengths
1. The authors proposed a novel method for an important problem (self-supervised multimodal representation learning), CoMM, that outperformed all baselines in almost all tasks. CoMM also only adds a marginal computation overhead compared to baselines.

2. The authors theoretically justified why CoMM works, and confirmed their theory with experiments and analyses on the synthetic dataset.

3. The paper's presentation quality is generally good. No significant grammar errors and the figures/tables are well-made.

4. The authors justified their design choices through ablation studies on both synthetic and real datasets.

### Weaknesses
Minor presentation issue: In section 4.2, the title claims that all tasks in this subsection should be 2-modal, but in lines 356-358 some of the video-affect tasks are 3-modal. It is unclear which 2 modalities out of 3 were used for this experiment, and it can be quite confusing (especially on UR-funny which occurred in both the 2-modal experiments and the 3-modal experiments). This lack of clarity makes it difficult to assess the specific contribution of the 2-modal experiments, as the reader cannot easily discern which modalities were used in each case. The inconsistent use of UR-funny across both sections further compounds this issue, making it hard to compare results directly.

### Questions
(Not important, just out of curiosity) Why is MM-IMDB not listed as part of MultiBench? (Since MM-IMDB is included in MultiBench)

### Soundness
4

### Presentation
3

### Contribution
3
