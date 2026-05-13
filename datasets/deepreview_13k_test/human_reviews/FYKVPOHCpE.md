# Improving Non-Transferable Representation Learning by Harnessing Content and Style

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Non-transferable learning (NTL) aims to restrict the generalization of models toward the target domain(s). To this end, existing works learn non-transferable representations by reducing statistical dependence between the source and target domain. However, such statistical methods essentially neglect to distinguish between *styles* and *contents*, leading them to inadvertently fit (i) spurious correlation between *styles* and *labels*, and (ii) fake independence between *contents* and *labels*. Consequently, their performance will be limited when natural distribution shifts occur or malicious intervention is imposed. In this paper, we propose a novel method (dubbed as H-NTL) to understand and advance the NTL problem by introducing a causal model to separately model *content* and *style* as two latent factors, based on which we disentangle and harness them as guidances for learning non-transferable representations with intrinsically causal relationships. Speciﬁcally, to avoid fitting spurious correlation and fake independence, we propose a variational inference framework to disentangle the naturally mixed *content factors* and *style factors* under our causal model. Subsequently, based on dual-path knowledge distillation, we harness the disentangled two *factors* as guidances for non-transferable representation learning: (i) we constraint the source domain representations to fit *content factors* (which are the intrinsic cause of *labels*), and (ii) we enforce that the target domain representations fit *style factors* which barely can predict labels. As a result, the learned feature representations follow optimal untransferability toward the target domain and minimal negative influence on the source domain, thus enabling better NTL performance. Empirically, the proposed H-NTL signiﬁcantly outperforms competing methods by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors explore an important problem named non-transferable learning, which aims to reduce the performance of a method on target domains while keeping considerable performance on source domains. The authors discover that existing methods suffer from two challenges, i.e., spurious correlation and fake independence. To deal with these challenges, the authors propose a variational inference framework that explicitly considers the contents and styles in various domains. The extensive experiments conducted on various datasets further demonstrate the effectiveness.

### Strengths
1. The paper is well-written and easy to follow.

2. The authors explore the important problem of non-transferable learning with two challenges investigated.

3. The authors conduct extensive experiments to showcase the superior performance of the work.

### Weaknesses
1. The authors state that existing methods suffer from the limitations of spurious correlation and fake independence. However, the authors do not provide any quantitative evaluation regarding these two challenges, except only intuitions.

2. The authors do not provide further details about the datasets used in the experiments. For example, the number of samples in each domain and each class. This will result in difficulties in understanding different datasets.

3. In Table 2 presented in the experimental part, the authors only consider two baselines for comparison, which is not fair enough for a comprehensive evaluation.

### Questions
Have the authors considered the benefits of using a variantiational inference framework? Is it due to the stochasticity?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes H-NTL, a new NTL method to address the issues of spurious correlation and fake independence present in many real-world implementations of NTL. The H-NTL method leverages a causal framework with two content and style latent factors to learn a variational inference framework. Empirical evaluations further support the strength of the proposed H-NTL method under various settings.

### Strengths
1. The paper is clearly written with presents a well-motivated justification for the H-NTL method.
2. Additional supplementary and ablation studies provide further evidence for the methodology.
3. H-NTL presents strong empirical performance in comparison with prior works.

### Weaknesses
No major weakness to note, however the reviewer would like to see additional evaluations with higher resolution images if possible (see questions below).

### Questions
Are there other standard NTL experimental setups using higher resolution datasets beyond the 32x32 or 64x64 images presented in the current paper?

### Soundness
4 excellent

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach to non-transferable learning (NTL) that focuses on disentangling content and style factors, harnessing them as guidance for improved non-transferable representation learning. The concept of separating content and style for NTL is innovative and not commonly explored in existing literature. This approach presents a fresh perspective on NTL that has the potential to address the limitations of previous statistical methods. The novelty of this concept makes the paper stand out.

### Strengths
1. The paper is technically sound and demonstrates a comprehensive understanding of the issues in NTL. It effectively presents a causal model to explain non-transferable learning and provides a well-structured method to address these issues. The utilization of a variational inference framework for disentanglement and dual-path knowledge distillation for learning non-transferable representations is well-reasoned and technically sound.

2. The paper is well-organized and clearly written. It provides a coherent and logical progression from the problem statement to the proposed solution. The use of illustrative figures and the clear description of the causal model enhance the paper's overall clarity. However, the high complexity of the method and the underlying theoretical framework might make it challenging for some readers. To enhance clarity, it would be helpful to include examples or case studies illustrating the practical application of the method.

3. The paper is significant in the context of non-transferable learning. It offers a promising approach that addresses the limitations of previous methods, particularly the challenges related to statistical dependence between source and target domains. The disentanglement of content and style factors is an important contribution as it aligns with human-like understanding and, as demonstrated through experiments, improves NTL performance. The potential impact on the AI research community lies in its ability to advance the field of NTL, making it more effective and practical.

### Weaknesses
1. The paper is generally well-structured, but it could benefit from the inclusion of practical examples or use cases to demonstrate the application of the proposed method.

2. The experiments demonstrate the superiority of H-NTL over competing methods, which is a significant point in favor of the paper's claims. It would be helpful to include discussions on potential real-world applications where H-NTL could be particularly valuable.

3. The introduction could be more concise and direct, focusing on the problem and motivation for the proposed approach.

4. Minor grammatical and typographical errors should be addressed for a more polished final version.

5. Including discussions on potential limitations and areas for future research could provide a more well-rounded view of the work.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
