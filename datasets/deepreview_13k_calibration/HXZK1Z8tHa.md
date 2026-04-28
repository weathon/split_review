# ShareFormer: Share Attention for Efficient Image Restoration

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Transformer-based networks are gaining popularity due to their superior ability to handle long-range information. However, they come with significant drawbacks, such as long inference time, and challenging training processes. These limitations become even more pronounced when performing high-resolution image restoration tasks. We have noticed that there is a trade-off between models' latency time and their trainability. Including a convolutional module can improve the networks' trainability but not reduce their latency. Conversely, sparsification notably reduces latency but renders networks harder to optimize. To address these issues, a novel Transformer for image restoration called ShareFormer is proposed here. ShareFormer offers optimal performance with lower latency and better trainability than other Transformer-based methods. It achieves this by facilitating the sharing of the attention maps amongst neighboring blocks in the network, thereby considerably improving the inference speed. To maintain the model's information flow integrity, residual connections are added to the "Value" of self-attention. Several lesion studies indicate that incorporating residual connections on "Value" can aggregate the shallow transformers with shared attention, introducing a local inductive bias and making the network easier to optimize without the need for additional convolution. The effectiveness, efficiency, and easy-to-train of our ShareFormer is supported by numerous experimental results. Our code and pre-trained models will be open-sourced upon publication of the paper.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper mainly proposes Shared Portion Stripe Attention (SPSA), which shares attention map in $(l-1)$-th and $l$-th layers and residually connects $\textit{value}$ of attention to intermediate attention output. To show the importance of the proposed residually connected $\textit{value}$, a Lesion study has been conducted. The authors also propose Combine SPSA with Gated Unit (CSGU) to enhance the existing GDFN module. ShareFormer shows comparable or improved performance when compared to state-of-the-art image restoration methods.

### Strengths
[S1] The references and related works cited by the authors are very recent and relevant.

[S2] The Lesion study presented in Sec.4.1 is comprehensive for demonstrating the proposed shared attention is highly related to ensemble behavior of the sequentially placed attention mechanism. Deleting or permutating some self-attention layers could smoothly increase the reconstruction loss. This can be the evidence that the shared attention is not the ensembles of shallow networks.

[S3] The performances of ShareFormer for large SR and lightweight SR are notably enhanced, compared to recent SOTA methods. These results were achieved with smaller model size, fewer computations, and faster speed than the others. (But an unfair issue remain. See question Q4.)

### Weaknesses
[W1] The presentation of text and figures in this paper should become clearer and more understandable. See Q1, Q2, and Q3.

[W2] The paper lacks some ablation studies proving the importance of the proposed components, such as CSAU. The authors should study architecture variants if they hope to clarify that CSAU comes not from insufficient considerations but from careful construction. And the efficiency and effectiveness differences between the original GDFN and the enhanced CSAU must be provided.

[W3] Most importantly, the core parts of ShareFormer, shared attention, seem not novel. In ELAN, one of the sota methods, shared attention map mechanisms have been already proposed. Moreover, it has been already shown how sharing attention maps in more than one layers can impact on the performance and efficiency of the model (related to your Tab.8).

[W4] A potential unfair issue is observed with respect to SR. See Q4.

[W5] Despite the improved inference speed, the performance gains of grayscale denoising, color denoising, and JPEG CAR are not significant.

### Questions
[Q1] Where is the exact part that the shared attention is operated? Eq.(4), (5) apparently reveals that this operates in $(l-1)$-th and $l$-th SPSA blocks. However, Fig.2 illustrates attention map of SPSA is shared to CSAU, while Fig.3 depicts sharing attention map appears after residual connection on $\textit{value}$. The reviewer thinks that the explanation of Eq.(4), (5) is the correct case the authors intended, while the phrase, "**sharing attention map**", in Fig.2 and Fig.3 is confusing. If it’s right, “sharing” can be omitted. Or not, please let me know what your first intention with respect to the exact parts of sharing attention map is.

[Q2] This question is related to Sec.4.2. From ConViT, how can you draw the conclusion that the concentrated ERF implies an amplified locality bias of the network? The reviewer thinks that it is not sufficient for the authors to claim that this fact shows the locality bias of the residually connected $\textit{value}$ in ShareFormer. I cannot find the acceptable evidence from ConViT paper. Don’t you have any other evidence justifying your claim, such as visualization?

[Q3] In Appendix D, why did you compare the attention maps of layers 1 and 3? ShareFormer shares attention map in layer-order-number pairs (0, 1), (2, 3), …, (2n-2, 2n-1), respectively. Thus, comparison of attention maps in “layers 0 and 1” or “layers 2 and 3” is more compelling to demonstrate attention map redundancy. Additionally, I recommend the authors to compare attention redundancies of the cases where the shared attention is “employed” and “not employed” in the proposed ShareFormer, instead of SwinIR cases.

[Q4] Did you apply the Progressive Learning to large and lightweight SR tasks with training patch size of from 128 to 384? However, the comparative methods, SwinIR, ELAN, and DLGSA, used smaller patch size, such as 48x48 and 64x64. I am concerned that this leads to a potential unfairness issue.



**Minor issue (not necessary to be mentioned in author rebuttal, if the authors struggle to a limit on the number of characters of rebuttal.)**

(1) Fig.2 omits (a) and (b) mark, while the caption uses (a) and (b).

(2) In the last to second sentence of Tab.1 caption, Restormer never used window attention. Moreover, you should mention what is MHDA, which seems a typo. (In Restormer, MDTA was used, and MHDA was not shown in SwinIR.)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new transformer architecture called ShareFormer for image restoration tasks like super-resolution and denoising. The key idea is to share attention maps between neighboring layers, which reduces computational cost and speeds up inference. Residual connections are added to preserve information flow. Experiments show ShareFormer achieves state-of-the-art accuracy with lower latency and better trainability than prior transformers.

### Strengths
•	The proposed ShareFormer delivers substantial improvements in efficiency, reducing latency by up to 2x compared to CNN models without compromising accuracy. This is achieved through an innovative technique of sharing attention maps between transformer layers to avoid redundant computations. 
•	The method enhances trainability over other transformer architectures by introducing beneficial inductive biases, allowing faster convergence. 
•	An additional strength is the generalizability of the approach, which is shown to be compatible with different attention mechanisms like shifted windows.

### Weaknesses
•	The performance exhibited by the proposed ShareFormer is indeed commendable, adeptly striking a balance between quality and speed. Nonetheless, I must express some reservations regarding the motivation behind the proposed backbone. To put it candidly, certain elements of the core module in ShareFormer appear reminiscent of concepts present in existing methodologies. For instance, the notions of Residual on V and the Reuse of Attention map are echoed in methods like Restormer and ELAN. Similarly, the group split strategy bears similarities to the one found in EfficientViT [1]. Thus, at a glance, ShareFormer seems to be a thoughtful amalgamation of pre-existing techniques. I would strongly recommend emphasizing the unique aspects and contributions of ShareFormer to underscore its originality within the broader landscape.
[1] Xinyu Liu, Houwen Peng, Ningxin Zheng, Yuqing Yang, Han Hu, Yixuan Yuan: EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention. CVPR 2023: 14420-14430.
•	The gains in trainability from the residual connections could use more detailed analysis and intuition. The paper currently lacks insight into the underlying mechanisms enabling faster convergence.
•	The ablation study is limited and does not thoroughly evaluate the contribution of each component. More experiments could help tease apart the individual impact of techniques like SPSA and the gated units.
•	Important implementation details like dataset splits for training, validation, and testing are not provided. This makes reproducibility difficult.
•	Besides the Image Super-Resolution, the overall improvements appear relatively incremental over strong prior work like SwinIR and Restormer. The advances are not radically transformative.

### Questions
Some concerns are raised in Weakness.

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
This paper tried to solve two problems: how to make Transformer faster and how to make Transformer's optimization faster.
For the first problem, they propose shared portion stripe attention (SPSA) to reduce the network latency up to 7x speedup.
For the second problem, they introduce residual connections to the value of SPSA.
In summary, they build a novel Transformer network: ShareFormer by SPSA with residual connections and gated united.

### Strengths
1. This paper reduced the computational complexity of stripe attention by Shared Portion Stripe Attention.

2. They proposed Residual Connections on Value, which offset the obstruction of the information flow throughout the network.

3. They reached similar or even better performance and fewer parameters compared with other methods.

### Weaknesses
1. In order to implement shared attention, they had to introduce residual connections on value and gated unit to control the extra complexity. I am concerned that the greater the complexity of the system, the higher the likelihood of training instability.

2. In Tables 4, 5, and 6, DRUNet reached similar performance and much lower latency compared with ShareFormer. To be honest, I prefer DRUNet in real applications with nearly 5x speedup, even though there is a 0.1~0.2 performance loss.

### Questions
1. Could you please also list the number of parameters of each model in Tables 4 and 6?

2. By adding V directly to the output, you're effectively giving more weight to the original values irrespective of the computed attention scores. This might dilute the effect of the attention mechanism, especially if the values in V dominate the weighted sum. Thus, what if introducing a trainable parameter to scale the residual connection instead of directly adding a residual connection?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
