# Knowledge Distillation Based on Transformed Teacher Matching

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
As a technique to bridge logit matching and probability distribution matching, temperature scaling plays a pivotal role in knowledge distillation (KD).  Conventionally, temperature scaling is applied to both teacher's logits and student's logits in KD. Motivated by some recent works, in this paper, we drop instead temperature scaling on the student side, and  systematically study the resulting variant of KD, dubbed transformed teacher matching (TTM). By reinterpreting temperature scaling as a power transform of probability distribution, we show that in comparison with the original KD, TTM has an  inherent Rényi entropy term in its objective function, which serves as an extra regularization term.  Extensive experiment results demonstrate that thanks to this inherent regularization, TTM leads to trained students with better generalization than the original KD. To further enhance student's capability to match teacher's power transformed probability distribution, we introduce a sample-adaptive weighting coefficient into TTM, yielding a novel distillation approach dubbed weighted TTM (WTTM). It is shown, by comprehensive experiments, that although WTTM is simple, it is effective, improves upon TTM, and achieves state-of-the-art accuracy performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper systematically analyzed the effect of dropping the temperature scaling on the student side in knowledge distillation (KD). The theoretical analysis shows that such a transformation leads to a general KD loss and a Renyi entropy regularization that improves the generalization of the student. Further, To further enhance student’s capability to match teacher’s power transformed probability distribution, the paper introduces a sample-adaptive coefficient to the method. Experiments are conducted to validate the effectiveness of both modules. Experiments are evaluated with different model architectures and teacher quality.

### Strengths
I think overall the paper provides new findings to understand the role of temperature in knowledge distillation. And the evaluation experiments are extensive.

1. The theoretical derivation and analysis for the general KD, Renyi entropy, and transformed teacher matching is precise and solid.

2. Extensive experiments confirm the theoretical analysis and show the effectiveness of each proposed module.

### Weaknesses
1. It's better to provide a detailed summary and comparison of the latest related works.

2. It's also more convincing to show results on transformer models such as ViT.

### Questions
Please see the weakness part.

### Soundness
4 excellent

### Presentation
2 fair

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
The paper systematically studies a variant of KD without temperature scaling on the student side, dubbed TTM. Temperature scaling is crucial in knowledge distillation (KD). This paper introduces transformed teacher matching (TTM), a variant of KD that omits temperature scaling on the student side. TTM includes an inherent regularization term and produces better generalization compared to the original KD. Weighted TTM (WTTM) further enhances the student's ability to match the teacher's probability distribution, achieving state-of-the-art accuracy.

### Strengths
- Fruitful discussion about related works to engage the readers.
- Theoretical derivation from KD to the proposed TTM.

### Weaknesses
The results are completely dependent on the list T and β values of all experiments (see Table 8 and 9), which makes the method impractical. Furthermore, the optimal value may even vary from task to task, dataset to dataset and backbone to backbone. These are my main concerns. Based on the marginal gain compared to the baselines, these empirical results actually weaken the claimed contribution.

### Questions
see above

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the temperature for Knowledge Distillation, proposing Transformed Teacher Matching (TTM), which drops the temperature scaling on the student side. TTM has an inherent Renyi entropy term in its objective function, and this regularization leads to better performance with KD.

### Strengths
1. The method that rethinking KD via temperature scaling is interesting.
2. The final TTM does not introduce extra hyper-parameters. Also, the training speed keeps the same.
3. The results on various datasets and models prove its effectiveness.

### Weaknesses
1. Some references and comparisons are missing:

    [1] Knowledge distillation from a stronger teacher.

    [2] From Knowledge Distillation to Self-Knowledge Distillation: A Unified Approach with Normalized Loss and Customized Soft Labels.

    [3] Curriculum Temperature for Knowledge Distillation.

    [4] VanillaKD: Revisit the Power of Vanilla Knowledge Distillation from Small Scale to Large Scale.
2. When temperature=1, is TTM the same as the original KD? In some papers, the temperature on ImageNet is actually 1.0.
3. Could TTM still achieve better performance for larger models (e.g. DeiT-T or DeiT-S)?  VanillaKD shows under strong training settings, the original KD also performs well.

### Questions
above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new variant of knowledge distillation called Transformed Teacher Matching (TTM) that drops temperature scaling on the student side and introduces an inherent regularization term. The paper shows that TTM leads to better generalization and achieves state-of-the-art accuracy performance. The paper also introduces a weighted version of TTM called Weighted Transformed Teacher Matching (WTTM) that enhances the student's capability to match the teacher's power transformed probability distribution. The experiments conducted in the paper demonstrate the effectiveness of TTM and WTTM on various datasets and architectures.

### Strengths
1. The paper introduces a new variant of knowledge distillation that drops temperature scaling on the student side and introduces an inherent regularization term. This approach is motivated by recent works and is a departure from conventional knowledge distillation. The paper also introduces a weighted version of TTM that enhances the student's capability to match the teacher's power transformed probability distribution. These contributions are novel and have not been explored in previous works.

2. The paper is well-written and presents a clear and concise description of the proposed methods. The authors provide a thorough analysis of the experimental results and compare their approach with state-of-the-art methods. The experiments are conducted on various datasets and architectures, which demonstrates the effectiveness and robustness of the proposed methods.

3. The proposed methods have the potential to improve the performance of knowledge distillation and have practical applications in various domains. The paper demonstrates that TTM and WTTM achieve state-of-the-art accuracy performance on various datasets and architectures. The inherent regularization term in TTM also provides a new perspective on knowledge distillation and has the potential to inspire further research in this area. Overall, the paper makes a significant contribution to the field of knowledge distillation

### Weaknesses
1. The paper could benefit from addressing the lack of novelty by acknowledging that techniques such as R´enyi or f divergence, temperature scaling, and logits normalization have already been widely used in knowledge distillation. For example, Information Theoretic Representation Distillation (BMVC) employed R´enyi divergence for standard distillation, and AlphaNet (ICML2021) utilized the f divergence to distill different sub-networks. Moreover, this method is likely already considered in the distiller's search work (KD-Zero: Evolving Knowledge Distiller for Any Teacher-Student Pairs, NeurIPS-2023). 

2. To strengthen the paper's findings, it is important to validate the proposed method on downstream tasks such as object detection and segmentation. Including evaluation results on these tasks will demonstrate the practical effectiveness and applicability of the proposed method. Additionally, providing more examples and visualizations will enhance the readers' understanding of how the method works and its impact on the learning process.

3. Furthermore, it is essential to incorporate a thorough discussion of relevant KD-related studies, including Self-Regulated Feature Learning via Teacher-free Feature Distillation (ECCV2022), NORM: Knowledge Distillation via N-to-One Representation Matching (ICLR2023), Shadow Knowledge Distillation: Bridging Offline and Online Knowledge Transfer (NIPS2022), DisWOT: Student Architecture Search for Distillation Without Training (CVPR2023), and Automated Knowledge Distillation via Monte Carlo Tree Search (ICCV2023). This discussion will help position the proposed approach within the existing literature, establish connections, and provide valuable insights for potential comparisons.

### Questions
The only concern to me is the novelty of the work and I hope the authors could discuss some of the related work I mentioned in the revised version.


---------------------------------

The author's response addressed my concerns well, so I'm improving my score to acceptance, thanks!

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
