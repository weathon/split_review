# Transformer Fusion with Optimal Transport

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Fusion is a technique for merging multiple independently-trained neural networks in order to combine their capabilities. Past attempts have been restricted to the case of fully-connected, convolutional, and residual networks. This paper presents a systematic approach for fusing two or more transformer-based networks exploiting Optimal Transport to (soft-)align the various architectural components. We flesh out an abstraction for layer alignment, that can generalize to arbitrary architectures -- in principle -- and we apply this to the key ingredients of Transformers such as multi-head self-attention, layer-normalization, and residual connections, and we discuss how to handle them via various ablation studies. Furthermore, our method allows the fusion of models of different sizes (\textit{heterogeneous fusion}), providing a new and efficient way to compress Transformers. The proposed approach is evaluated on both image classification tasks via Vision Transformer and natural language modeling tasks using BERT. Our approach consistently outperforms vanilla fusion, and, after a surprisingly short finetuning, also outperforms the individual converged parent models.
In our analysis, we uncover intriguing insights about the significant role of soft alignment in the case of Transformers. Our results showcase the potential of fusing multiple Transformers, thus compounding their expertise, in the budding paradigm of model fusion and recombination.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a systematic approach for fusing two or more transformer-based networks exploiting Optimal Transport technique. The proposed method can generalize to arbitrary architectures for CNNs and Transformers. Extensive experiments involving the fusion and finetuning of Vision Transformers (ViTs) across multiple datasets demonstrate the effectiveness of the proposed method.

### Strengths
- This paper is well written.
- The proposed method shows good generalization across different architectures.
- The proposed method show strong performance for several benchmark.

### Weaknesses
 - Most experiments are conducted to compare with Vanilla Fusion. More comparisons with state-of-the-art methods should be included.
- Most experiments are conducted on CIFAR dataset which is relatively small.

### Questions
See the weakness part.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a systematic approach for fusing two or more pretrained transformers by studying the flow of transportation maps in each specific component of Transformer. The authors empirically showed that when working with Transformers, hard alignment underperforms soft alignment in one-shot fusion, which is in contrast to the cases of fully connected and convolutional neural networks. Finally, they showcased the efficiency of the proposal in fusing and finetuning ViT and BERT.

### Strengths
- This paper is well-structured.
- To the best of my knowledge, this is the first work that aims to fuse transformer architectures by aligning their weights.
- The proposed method is successfully backed by theoretical results.

### Weaknesses
 - The methodology part is not well-written and lacks some details.

 - Section 2: The model fusion literature has some papers that are slightly off: Tatro et al., 2020; Juneja et al., 2022; Kandpal et al., 2023.
- Eq. 2: What is $f$? What is its output?
- Section 4.2.1: How to calculate weighted matrix?
- The authors should remind the formulation for Attention operation in either Section 3 or Section 4.2.2.
- Section 4.2.2:
  - Where do the authors remove the constraints in Section 4.2.2?
  - It is unclear how to calculate $T_Q$ and $T_K$. Did the authors check the assumption $T_Q = T_K$ in the experiments?
  - What are $W_i^Q, W_i^K$, and $W_i^V$? Does $i$ indicate the head index?
  - Additional visualizations may help to demonstrate the method here.
- Section 4.2.3: What is this sentence for? “For the concatenation, we notice that the class token is only a small fraction of the full sequence, in other words, for the integrity of the sequence, it is far more important to propagate the TM of the patch embeddings than the one for the class token.” In addition, the class token is more important because it gathers the information from the patch.

**Minors**: 
- Eq. 3 should be moved up a paragraph.

### Questions
- Section 2: The model fusion literature has some papers that are slightly off: Tatro et al., 2020; Juneja et al., 2022; Kandpal et al., 2023.
- Eq. 2: What is $f$? What is its output?
- Section 4.2.1: How to calculate weighted matrix?
- The authors should remind the formulation for Attention operation in either Section 3 or Section 4.2.2.
- Section 4.2.2:
  - Where do the authors remove the constraints in Section 4.2.2?
  - It is unclear how to calculate $T_Q$ and $T_K$. Did the authors check the assumption $T_Q = T_K$ in the experiments?
  - What are $W_i^Q, W_i^K$, and $W_i^V$? Does $i$ indicate the head index?
  - Additional visualizations may help to demonstrate the method here.
- Section 4.2.3: What is this sentence for? “For the concatenation, we notice that the class token is only a small fraction of the full sequence, in other words, for the integrity of the sequence, it is far more important to propagate the TM of the patch embeddings than the one for the class token.” In addition, the class token is more important because it gathers the information from the patch.


**Minors**: 
- Eq. 3 should be moved up a paragraph.

### Soundness
2 fair

### Presentation
2 fair

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
This paper introduces a systematic fusion technique for transformer-based networks by leveraging Optimal Transport to align architectural components. It offers a flexible approach applicable to various architectures, including key Transformer components. Heterogeneous fusion enables efficient compression, with superior performance compared to vanilla fusion and individual parent models, as demonstrated in image classification (Vision Transformer) and natural language tasks (BERT). Our analysis underscores the significance of soft alignment in the context of Transformers, highlighting the potential for combining multiple Transformers to enhance their capabilities in the emerging field of model fusion and recombination.

### Strengths
1. The authors examined various strategies (weight vs activation, hard vs soft etc) for applying optimal transport (OT) methods
2. The authors conducted experiments employing both Vision Transformer (ViT) and BERT architectures across multiple datasets.
3. The OT method demonstrates particular efficacy in one-shot scenarios.
4. OT methods exhibit versatility, as they can be effectively applied to models of varying widths, presenting a viable alternative to distillation.

### Weaknesses
1. The OT method yields comparatively lower performance when contrasted with ensemble methods.

2. The suitability of the OT method for achieving solid results on larger datasets, such as ImageNet-1K, in one-shot scenarios remains uncertain.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for fusing multiple independently trained transformer architectures using optimal transport to align their respective architectural components. To this end, authors analyse predominant Transformer architectures based on their components, and provide OTFusion methods for each. The proposed approach allows for fusing transformers of different sizes. 
Experiments are conducted on a range of image classification datasets; CIFAR10, CIFAR100, TinyImagenet and ImageNet-1k. Authors show results for models obtained through both zero-shot (without fine tuning) and with fine tuning. In zero-shot fusion, the proposed approach outperforms Vanilla Fusion methods. With fine tuning, the proposed approach is able to beat either parent model. Authors conclude with a number of limitations of their approach and suggestions for future research.

### Strengths
This paper is very well-written, authors give clear and concise descriptions of their approach and illustrate its complex aspects through figures and examples. This makes the manuscript easy to read and the ideas it expands upon easy to understand despite their complexity. The method seems to work well, drastically outperforming Vanilla Fusion (naive model averaging). The authors show a range of valuable ablations, and motivate most of their design choices well.

### Weaknesses
My main concern is to do with the clarity of the contribution of this work. The authors refer to [1] a lot in their paper, where the concept of OTFusion is introduced. It seems like a lot of the techniques used in this work were actually introduced there. Although I understand the need for reintroducing these concepts in the manuscript for contextual clarity, I think it would be good to give a clearer picture of the actual contributions made in this work and the methods proposed in previous works. From the description under 4.3 it seems [1] uses hard alignment where you find soft alignments to outperform. Are these contributions of your work? What about the TM combination approaches (Averaging/Weighted Scalar/ Weighted Matrix)? Or heterogeneous fusion?

I hope the authors are able to address this in their rebuttal, in which case I see this work as an interesting and strong submission.

### Questions
-What do you mean by “This diversity offers a challenging fusion problem requiring a non-trivial alignment strategy, and thus effectively recreates a plethora of other scenarios” (under 5 - Model Training). Can you explain e.g. how varying random seed equates to model training on different subsets?
-How does your work relate to [2]? You indicate that [2] is very similar to OTFusion, but looking at zero-shot performance of your method (and your VF baseline) on CIFAR10 classification it seems performance is drastically different (~93% vs ~60%). If essentially identical, why does [2] yield zero-barrier LMC where your approach does not?
-Could you give an intuition for soft-alignment, what resulting network is actually being constructed  in this case and why could it be beneficial compared to hard alignment approaches?
-Do you have an intuition for why your method performs better with soft-alignment, where [1] shows better results with hard alignment?

[2] Samuel K Ainsworth, Jonathan Hayase, and Siddhartha Srinivasa. Git re-basin: Merging models
modulo permutation symmetries. arXiv preprint arXiv:2209.04836, 2022.

---

Update after rebuttal: I thank the authors for their thorough rebuttal. I'm pleased to say my concerns are adequately addressed. Also considering the largely positive reviews by the other reviewers, I'd like to update my recommendation to an accept.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
