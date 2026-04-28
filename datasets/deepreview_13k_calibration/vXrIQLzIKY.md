# Xformer: Hybrid X-Shaped Transformer for Image Denoising

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
\vspace{-2mm}
		In this paper, we present a hybrid X-shaped vision Transformer, named Xformer, which performs notably on image denoising tasks. We explore strengthening the global representation of tokens from different scopes. In detail, we adopt two types of Transformer blocks. The spatial-wise Transformer block performs fine-grained local patches interactions across tokens defined by spatial dimension. The channel-wise Transformer block performs direct global context interactions across tokens defined by channel dimension. Based on the concurrent network structure, we design two branches to conduct these two interaction fashions. Within each branch, we employ an encoder-decoder architecture to capture multi-scale features. Besides, we propose the Bidirectional Connection Unit (BCU) to couple the learned representations from these two branches while providing enhanced information fusion. The joint designs make our Xformer powerful to conduct global information modeling in both spatial and channel dimensions. Extensive experiments show that Xformer, under the comparable model complexity, achieves state-of-the-art performance on the synthetic and real-world image denoising tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes XFormer for image denoising, which aims to combine SwinIR which utilizes spatial-wise self attention and Restormer designing channel-wise self attention for image denoise, thereby leveraging the advantages from both methods. The designs, including dual-branch architecture and the bidirectional connection unit for bilateral interactions between two branches, are straightforward.m The paper is motivated well, whilst the technical novelty is incremental, especially compared to SwinIR and Restormer.

### Strengths
1. This paper is motivated well. It is reasonable to combine the advantages of both spatial-wise self attention and channel-wise self attention to capture both the local fine-grained features and global features across channels.

2. The paper is organized well and easy to follow despite some typos.

### Weaknesses
1. The technical novelty is incremental. There are two core designs: the dual-branch architecture and the bilateral interactions between two branches, which are both typical designs and have been extensively explored in other work. Thus, the technical novelty is limited, especially compared to SwinIR and Restormer.

2. Compared to Restormer, Xformer has limited performance improvement, especially on real image denoising scenarios which is more important for evaluation.

### Questions
It is suggested to investigate both theoretically and experimentally what kind of denoising scenarios (noises) are STB and CTB suitable for, respectively.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed a hybrid X-shaped transformer for high-quality image denoising. The idea is good. Specifically, the technique consists of spatial-wise transformer blocks (STB) and channel-wise transformer blocks (CTB) to model global information. The authors provide extensive ablation studies to support the effectiveness of each proposed component, like STB, CTB, and BCU etc. The main comparisons with recent methods further show that the proposed method Xformer achieves better performance than others quantitatively and visually.

### Strengths
The idea is good and novel. The proposed Xformer exploits stronger global representation of tokens with a hybrid implementation of spatial-wise and channel-wise Transformer.

The bidirectional connection unit (BCU) is proposed to couple the learned representations from two branches of Xformer. It is simple but effective according to the ablation.

The authors provide extensive ablations to show the effects of some key components, like STB, CTB, BCU, and shift operation.

The main comparisons are also extensive. The authors provide both Gaussian and real image denoising results, where the proposed Xformer achieves better average quantitative results and also shows better visual results.

The writing is good and the work is well-prepared. The overall paper framework is well-organized.

The authors provide more results and analyses in supplementary file, where a sample code is also available. Such a code makes the reproducibility more faithful.

### Weaknesses
Some details are not clear enough for better understanding. How did the authors determine the final model when training is finished? For example, did the authors choose the model based on the best validation performance or just use the model from the final iteration?

In the ablation study, Table 1 (b), it seems that w/o BCU and BCU-1 is comparable, BCU-2 and Complete BCU is comparable. Please give more analyses about their difference.

If the proposed method could be used for other image restoration tasks? If so, please give some comments and discussions. Or is it specifically designed for image denoising?

The Xformer shows very good performance. Are there any failure cases for image denoising? Namely, the proposed method can hardly recover good details either.

### Questions
Please refer to the Weaknesses for details.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a hybrid X-shaped vision transformer for image denoising, named Xformer. Xformer has two branches with one containing the spatial-wise transformer blocks and the other containing the channel-wise transformer blocks. Between these two branches, there are the bidirectional connection units which couple the learned representations from these two branches. The experimental results show that the proposed method performs well on the synthetic image denoising dataset, but the method does not achieve the SOTA on the real-world image denoising dataset.

### Strengths
1. The X-shaped architecture is elegant and reasonable.
2. The experimental results on the synthetic dataset are good.
3. The overall paper writing is good.

### Weaknesses
There are several places that are not intuitive or clear:
1. The authors claim that "we make the last encoder involving STBs of two branches share parameters for the purpose of computational efficiency." However, it is unclear how much the performance will be influenced by the parameter-sharing strategy. It is also not clear why it is critical to share parameters for this place in the network. Why not share parameters in other places?
2. The authors claim that "In short, the STB utilizes non-overlapping windows to generate shorter token sequences for the self-attention computation, which can enable the network to obtain fine-grained local patches interactions." Shorter token sequences? Compared to what? Why does the shorter token sequences can enable the network to obtain fine-grained local patches interactions?
3. The authors claim that "In order to introduce contextualized information into self-attention computation, we choose to use 3×3 depth-wise convolution (Conv) following 1×1 Conv to generate query (Q), key (K), and value (V)." Why not directly use a vanilla 3×3 convolution?
4. The authors claim that "Specifically, we use a 3×3 depth-wise convolution layer to refine the deep features from the spatial-wise branch for the purpose of saving computational consumption." Why not also using the 3×3 depth-wise convolution layer to refine the deep features from the channel-wise branch? Will it influence the performance compared to using the 3×3 vanilla convolution?

### Questions
See the weakness section.

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
In the proposed architecture, the authors design two branches to conduct these interaction modes. Both branches use an encoder-decoder setup to capture multi-scale features. An essential addition to this structure is the "Bidirectional Connection Unit (BCU)", which couples the learned representations from the two branches and facilitates better information fusion.

The combined designs enable the Xformer to effectively model global information in both spatial and channel dimensions. Through extensive experiments, the authors demonstrate that the Xformer achieves state-of-the-art performance on both synthetic and real-world image denoising tasks, all while maintaining comparable model complexity.

### Strengths
The paper stands out in its innovative approach to image denoising by proposing a hybrid X-shaped Transformer. The clear presentation, combined with extensive experiments and state-of-the-art results, underscores its significance in the domain. The novel components, especially the BCU, and the creative combination of spatial and channel-wise blocks, emphasize its originality. The potential impact of this work on the broader image processing community is considerable.

### Weaknesses
The hybrid nature of the model, with its dual branches and BCU, might be challenging for some readers to grasp fully. While the description seems structured, visual aids might be lacking. The description of the Bidirectional Connection Unit (BCU) lacks detail regarding the specific convolutional operations used. It's unclear if these are standard convolutions, depth-wise separable convolutions, or some other variant. Furthermore, the rationale for choosing convolution over other potential fusion methods, such as attention mechanisms, is not explicitly addressed. The paper would benefit from a more in-depth discussion of the BCU's architecture and its specific operational details.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
