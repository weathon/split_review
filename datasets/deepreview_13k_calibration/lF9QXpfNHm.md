# Efficient Open-world Test Time Adaptation of Vision Language Models

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
In dynamic real-world settings, models must adapt to changing data distributions, a challenge known as Test Time Adaptation (TTA). This becomes even more challenging in scenarios where test samples arrive sequentially, and the model must handle open-set conditions by distinguishing between known and unknown classes. Towards this goal, we propose ROSITA, a novel framework for Open set Single Image Test Time Adaptation using Vision-Language Models (VLMs). To enable the separation of known and unknown classes, ROSITA employs a specific contrastive loss, termed ReDUCe loss, which leverages feature banks storing reliable test samples. This approach facilitates efficient adaptation of known class samples to domain shifts while equipping the model to accurately reject unfamiliar samples. Our method sets a new benchmark for this problem, validated through extensive experiments across diverse real-world test environments. Our code is anonymously released at https://github.com/anon-tta/ROSITA.git

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper propose a novel method called ROSITA  for Open World Single Image Test Time Adaptation using VLMs.  

ROSITA employs feature banks and an innovative contrastive loss to enhance the distinction between known and unknown classes, allowing efficient adaptation to domain shifts while enabling the model to reject unfamiliar classes.

The extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-written and easy to follow, with a clear motivation.
2. The experimental results are impressive, and the ablation study is thorough.
3. The method is novel, interesting, and effective in addressing the challenging problem of Open World Test Time Adaptation.

### Weaknesses
1. The title of this paper uses '...... vision-language models' , It seems that author only used CLIP for experiments. It would be better to also study the performance with CLIP-large and other VL backbones.
2. The paper lacks a thorough discussion of the limitations of the current solution and does not provide suggestions for future work.
3. The author doesn't report the error bar.

### Questions
Please see the weakness.

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
The article proposes ROSITA, a framework for test-time adaptation of vision language models in settings where, during inference, the model receives samples of both desired/target classes and undesired ones. The latter should be flagged by the model, as in standard open-set scenarios. ROSITA is based on two components: LDA-based separation of desired and undesired classes (following Li et al. (2023)), and a contrastive objective, updating LayerNorm parameters of the visual encoder. Experiments show that the approach outperforms common TTA approaches in this new, less-explored setting.

### Strengths
1. Although it is hard to define closed vs. open set in the context of VLMs, the case of test-time adaptation when the test samples comprise both desired and undesired classes is an understudied problem that this paper aims to tackle.

2. The proposed method, ROSITA, is sound, exploiting a simple technique based on LDA to identify desired vs undesired samples (Li et al. (2023)) coupled with a contrastive objective to refine the feature representation. The various design choices are also motivated via ablation studies (e.g., Fig. 1, Tab. 4).

3. The method consistently performs well across various settings and data streams.

### Weaknesses
1. As first statement for the focus of the work, lines 64-65 states this work adapts VLMs to work with single-image TTA. This sentence is misleading as multiple works already considered TTA with a single image: for instance, TPT (Shu et al. (2022)) and TDA (Karmanov et al. (2024)) are two examples. This sentence should be revised to avoid potential over claims and better contextualize the work, e.g., by focusing the claim on the differences in the specific setting considered and those of existing works on VLMs.

2. While the definition of the setting as open-world follows previous work (i.e., Li et al. (2023)), it is inaccurate as it does not follow its original meaning. Specifically, open-world recognition implies that classes are added overtime to the model, adding semantic to samples of unknown (or undesired, as in this context) classes [a]. This is not the case in this work, as the set of target classes is static and it is not updated. A more precise definition would be following (Lee et al. (2023)) and use "open-set TTA", as that denotes the presence of a set of target classes and OOD samples to be recognized. It would be helpful to clarify the particular meaning of open world (comparing it with previous use, e.g., [a]) and/or consider adopting the term "open-set TTA" throughout the paper for consistency with existing literature.

2. Currently, the set of baselines do not include any open-set TTA approach, beyond the adaptation of Li et al. (2023). In particular, there exist many potential techniques for detecting unknowns (e.g., MSP [b], max logic [c]) and previous works considered what happens when considering them as alternative OOD detection strategy (e.g., Lee et al. (2023), Tab. 5). As all the experiments and methods are held out with the same, LDA-based selection strategy (Appendix B.4, lines 809) it would be more thorough to include (i) alternatives to LDA's-based OOD detection (ii) simple combination of existing OOD identification algorithms and those for TTA. This would provide a more comprehensive evaluation of ROSITA's performance relative to a broader range of approaches.

4. Technically, the article heavily relies on the TDA scores (proposed already in Li et al. (2023)) to recognize undesired classes. At the same time, there has been already efforts in constructing contrastive-based objectives for TTA [d,e]. Tuning only LayerNorm layers is an already known concept in the literature [f] as well, reducing the impact of Sec. 2.3). In this context, the article merges these two approaches for improved TTA in the "open-world" setting but the technical contribution and the differences with what has been already presented should be clarified and potentially analysed in the manuscript. I would be helpful to include a paragraph to explicitly discuss how the approach differs from and improves upon existing contrastive TTA methods and LayerNorm tuning techniques, potentially highlighting the aspects (and challenges) that are especially relevant for open-set/world TTA. 

6. TDA, one of the closest baseline, is compared with the proposed approach only on Table 3 and the same goes for the other main baseline, i.e., Li et al. (2023). Ii is not clear what is the criterion behind excluding part of the baselines between tables, especially two main ones which could further strengthen the contribution of the manuscript itself. TDA and Li et al. (2023) should be consistently reported across all relevant experiments, and/or it should be explained why these baselines have been excluded from certain comparisons. This would help readers better understand the relative performance of ROSITA across different scenarios.

**Minors**:
- From the abstract (i.e., lines 15-17) and the introduction (lines 73-75, 81-84) it is not clear how ROSITA work and what are its technical contribution. Clarifying them would allow the reader to better follow one of the key messages of the manuscript.

- Lines 203-205, the meaning of "text hypothesis transfer" is not clear.

- Line 481, typo "identifierr"

### Questions
1. Is the article the first to perform TTA on single samples and with OOD/undesired classes? If not, clarifying the differences would help to better understand the technical contribution.

2. How does the performance of the model change w.r.t. various design choices? (e.g., different OOD criterion, hyperparameters).

3. Is there a motivation behind the choice of competitors per method? And would it be possible to add other baselines as competitors?

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
5

### Summary
This paper proposes ROSITA, a new approach for Open World Single Image Test Time Adaptation that utilizes Vision-Language Models (VLMs). This method enhances the differentiation between known and unknown classes through the use of feature banks and a novel contrastive loss function.

### Strengths
**[New setup]** This work claims that it is the first to study open world single image test time adaptation using VLMs.

**[Extensive experiments]** This work has conducted extensive experiments across a diverse array of domain adaptation benchmarks.

### Weaknesses
 **[Incremental technical contribution]** The main contribution is the reduce loss, a specific contrastive loss, while the class identifier seems a reformulation of previous methods [1, 2] to this task. Given this fact, the technical contribution seems incremental.

[1] Ronald A Fisher. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7 (2):179–188, 1936.

[2] Yushu Li, Xun Xu, Yongyi Su, and Kui Jia. On the robustness of open-world test-time training:
Self-training with dynamic prototype expansion. In ICCV, 2023.

**[Unconvincing updating parameter choices]** In section 2.3, the authors test using three different parameter groups for training. However, only these three groups are not comprehensive. Other parameters might be more suitable for updating at test time, e.g., the first layer or the last layer of the encoders. Moreover, additional parameters to keep the intact of the original model are also worth trying, e.g., adapter layers and LoRA.

**[Unclear illustration]** In Figure 1, there might be some questions to be raised: 1) Which dataset is used for experiments? Is it representative enough? If not, better use the results on multiple datasets. 2) Is the learning rate only hyperparameter to tune? What about optimizer type, training epochs and learning rate schedular? 3) Is it possible to update both the prompts and the LN parameters?

**[Missed baseline]** The more recent paper “Diverse Data Augmentation with Diffusions for Effective  Test-time Prompt Tuning, ICCV 2023” is not compared.

**[Experiments]** (i) In Table 1 and 3, the proposed method often outperforms other methods significantly while in Table 2 the performance is close to that of (K+1)PC. Could the authors explain this? (ii) In Table 4, the experimental results with $L_{Re}$ and $L_D$ should be given. (iii) In Table 6, it would be nice to include other methods.

### Questions
What’s the main difference between CNN based open world TTA and VLMs based one?

### Soundness
2

### Presentation
3

### Contribution
2
