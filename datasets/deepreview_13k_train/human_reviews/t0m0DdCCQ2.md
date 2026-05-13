# Liteformer: Lightweight Evoformer for Protein Structure Prediction

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
AlphaFold2 has achieved seminal success in predicting structures from amino acid sequences with remarkable atomic accuracy. However, its Evoformer module faces a critical challenge in terms of high memory consumption, particularly concerning the computational complexity associated with sequence length $L$ and the number of Multiple Sequence Alignments (MSA), denoted as $s$. This challenge arises from the attention mechanism involving third-order MSA and pair-wise tensors, leading to a complexity of $\mathcal{O}(L^3+sL^2)$.
This memory bottleneck poses difficulties when working with lengthy protein sequences. To tackle this problem, we introduce a novel and lightweight variant of Evoformer named Liteformer. Liteformer employs an innovative attention linearization mechanism, reducing complexity to $\mathcal{O}(L^2+sL)$ through the implementation of a bias-aware flow attention mechanism, which seamlessly integrates MSA sequences and pair-wise information. Our extensive experiments, conducted on both monomeric and multimeric benchmark datasets, showcase the efficiency gains of our framework.  Specifically, compared with Evoformer, Liteformer achieves up to a 44\% reduction in memory usage and a 23\% acceleration in training speed, all while maintaining competitive accuracy in protein structure prediction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors raise the problem on the high memory and time cost of the Evoformer module
used in AlphaFold2.
To solve this, they propose a lightweight variant of Evoformer named Liteformer. Through a bias-aware flow
attention (BFA) mechanism, the complexity of Liteformer is reduced to a lower quantity, compared with
original Evoformer.
Extensive experiments show the great effectiveness of the proposed method in terms of both memory
occupation and training acceleration, while keeping the competitive accuracy in protein structure
prediction.

### Strengths
1. The propose mechanism is very interesting and useful for the development of applications in recent
years.
2. Existing frameworks equipped with the proposed BFA modules can achieve competitive performance while
reducing the time of training and inference a lot.

### Weaknesses
1. In Fig. 2, the pipeline of the blocks in Evoformer and Liteformer is exactly the same. It's better to be combined into one figure. The difference between BFA and original attention is the key to which
should be compared like this.
2. The proposed method shows a great improvement in efficiency and memory cost. But there have
been some more general works that play a similar role, such as memory-efficient attention and flash
attention [Ref_1]. Can they jointly improve the training of the network? More ablation studies between
them should be provided for further comparison.
3. The proposed BFA module seems more likely to be a general attention module, instead of a theme-related
(protein-related) approach, which decreases the significance.


### Questions
What's the principle of selecting the targets from the CASP14, CASP15, CAMEO, and VH-VL, and why
sequence lengths of them are restricted to be shorter than 500, since Liteformer has a better ability to
handle the longer sequences?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Liteformer, a novel and lightweight variant of  Evoformer used in AlphaFold2 for protein structure prediction. Liteformer introduces a new mechanism called Bias-aware Flow Attention (BFA), which linearizes the biased attention for third-order tensors, such as multiple sequence alignment (MSA) and pair representation, with O(L) complexity.  Liteformer reduces the memory consumption and training speed of Evoformer by up to 44* and 23%,  respectively while maintaining competitive accuracy on various protein structure benchmarks.

### Strengths
- The paper proposes a novel and efficient variant of Evoformer, the core module of AlphaFold2, which is a state-of-the-art model for protein structure prediction.
- The paper introduces a new mechanism called Bias-aware Flow Attention, which linearizes the biased attention for third-order tensors with O(L) complexity, while preserving the evolutionary and geometric information from MSA and pair representations1.
- The paper demonstrates the effectiveness and efficiency of Liteformer on various protein structure benchmarks, such as CASP14, CASP15, CAMEO, VH-VL, and DB5.5, showing that it can reduce the memory consumption and training speed of Evoformer by up to 44% and 23%, respectively, while maintaining competitive accuracy.

### Weaknesses
 - Unclear motivation: The author emphasizes the huge computational complexity reduction brought by converting attention module  into a flow network. However, how this method affects the computational complexity is only mentioned at Eeq 7 in Section 3. I think there should be a separate paragraph in the introduction detailing the motivations for using flow network. Specifically, the paper needs to clarify why a flow network approach is better suited for handling the biased attention in third-order tensors compared to existing linear attention methods. It is not immediately obvious why a flow-based approach inherently leads to a reduction in complexity, and this needs to be more explicitly explained in the context of the MSA and pair representations.
- The claim does not correspond to the experimental results. In Sec 2 and 3, the authors mainly claim that BFA can reduce computational complexity. However, the experimental results show that memory usage is the main advantage of BFA during training. The drop in computation time is less pronounced. The authors in sec 4 simply boil this down to reduced graph overhead when backpropagated. In my opinion, it is not helpful to prove the validity of this method. The paper should provide a more detailed analysis of the computational bottlenecks in the original Evoformer and how BFA specifically addresses those bottlenecks. The current explanation of reduced graph overhead is too high-level and lacks the necessary technical depth to justify the observed speedup. A more granular breakdown of the computational costs associated with each operation, both in the original Evoformer and with BFA, would be beneficial.

### Questions
Please elaborate on the motivation for using streaming networks and how it leads to a reduction in computational complexity.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce LiteFormer, a variant of the AlphaFold2 Evoformer inspired by Flowformer, a linear transformer. Compared to the original Evoformer, LiteFormer has lower complexity and is claimed to run faster and more memory-efficiently. The authors evaluate LiteFormer on monomeric and multimeric structure prediction.

### Strengths
It is true that Evoformer has high complexity, and I'm not yet aware of successful applications of the linear transformer literature to the AlphaFold2 architecture. It's also welcome that the authors evaluate on CASP and not just a small CAMEO dataset, like many other papers of this genre.

### Weaknesses
Some of the performance figures that motivate this entire paper seem questionable. It is claimed in Figure 1 that AlphaFold2 OOMs on sequences of length 800, e.g. If the authors are running inference using the same 80GB A100s they use later in the paper, this simply cannot be true; one can get away with longer sequences even on ColabFold (Mirdita et al., 2022), which runs on free-tier Google Colab GPUs. The authors of OpenFold were able to run an unmodified version of the original AlphaFold2 on sequences of length 2000 on a 40GB A100 (Ahdritz et al., 2022).

Separately, the choice of ESM-2 150M as a baseline for monomeric structure prediction is extremely confusing. Why not use unmodified AlphaFold2? Why not use a larger ESM-2 protein language model? Why mix and match these figures with AlphaFold2-Multimer evals? In general, details on the evaluation are very light (e.g. which CAMEO proteins were chosen? Why were all evaluation proteins filtered at 500? Which AlphaFold2 implementation served as the baseline?), to the point where it's difficult to know what is being run.

On top of that, the claimed performance improvements are comparable to or less significant than those of other optimized versions of AlphaFold2, none of which are mentioned here. FastFold, UniFold, OpenFold have all already improved AlphaFold2 with e.g. FlashAttention.

Misc.:

>However, since both the row and column dimensions of the pair representation, along with the row dimension of the MSA representation, are identical to the primary sequence length L.

>We trained 10,000 data for 5 days using 8 × DGX-A100 80G GPUs and inference on two multimeric datasets: VH-VL and DB5.5.

The paper is a bit sloppily written (see examples above). I'm not sure what the first sentence is saying. The second one contains no information about which 10,000 data points were used to train the model.

>CASP14 & CASP15. The 14th & 15th Critical Assessment of protein Structure Prediction, from which we respectively select 42 and 48 single protein targets with sequence lengths less than 500.

Why filter in this way? The hardest proteins are the longest ones. Almost all entries at CASP15 did well on most of the proteins of length < 500 (excepting some orphans, etc.).

### Questions
>CASP14 & CASP15. The 14th & 15th Critical Assessment of protein Structure Prediction, from which we respectively select 42 and 48 single protein targets with sequence lengths less than 500.

Why filter in this way? The hardest proteins are the longest ones. Almost all entries at CASP15 did well on most of the proteins of length < 500 (excepting some orphans, etc.).

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
