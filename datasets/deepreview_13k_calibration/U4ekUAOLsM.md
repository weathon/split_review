# SCHEME: Scalable Channel Mixer for Vision Transformers

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Vision Transformers have achieved impressive performance in many vision tasks. While the token mixer or attention block has been studied in great detail, much less research has been devoted to the channel mixer or feature mixing block (FFN or MLP), which accounts for a significant portion of of the model parameters and computation. In this work, we show that the dense MLP connections can be replaced with a block diagonal MLP structure that supports larger expansion ratios by splitting MLP features into groups. To improve the feature clusters formed by this structure we propose the use of a lightweight, parameter-free, channel covariance attention (CCA) mechanism as a parallel branch during training. This enables gradual feature mixing across channel groups during training whose contribution decays to zero as the training progresses to convergence. In result, the CCA block can be discarded during inference, enabling enhanced performance at no additional computational cost. The resulting {\it Scalable CHannEl MixEr\/} (SCHEME) can be plugged into any ViT architecture to obtain a gamut of models with different trade-offs between complexity and performance by controlling the block diagonal MLP structure. This is shown by the introduction of a new family of SCHEMEformer models. Experiments on image classification, object detection, and semantic segmentation, with different ViT backbones, consistently demonstrate substantial accuracy gains over existing designs, especially for lower complexity regimes. The SCHEMEformer family is shown to establish new Pareto frontiers for accuracy vs FLOPS, accuracy vs model size, and accuracy vs throughput, especially for fast transformers of small size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes SCHEME (Scalable CHannEl MixEr), a channel mixing mechanism for Vision Transformers (ViTs). The method focuses on replacing the dense MLP layers in the transformer’s channel mixing block with a block diagonal MLP (BD-MLP) structure, allowing for larger expansion ratios and improving computational efficiency. Additionally, the authors introduce a Channel Covariance Attention (CCA) mechanism to enable inter-group communication, which is discarded after training to reduce inference complexity. The SCHEME mechanism is integrated into multiple Vision Transformer architectures and is evaluated across various benchmarks, showing improved accuracy while maintaining efficiency.

### Strengths
1. SCHEME introduces a clever way of reducing complexity by leveraging block diagonal MLPs, which directly targets the computational bottleneck of standard transformers.
2. The addition of the Channel Covariance Attention (CCA) during training adds flexibility and improves feature clustering without increasing inference complexity, making it an efficient regularization tool.
3. The approach is shown to be effective across multiple transformer backbones (MetaFormer, T2T, Swin), demonstrating its adaptability in various settings.

### Weaknesses
1. The manuscript contains several grammatical errors and formatting issues, such as the phrase 'In result' in the abstract, as well as figures that are too small to clearly convey the details, which fails to meet the standards of ICLR.
2. Experiments focuses heavily on comparisons with a few models like MetaFormer, lacking comparisons with state-of-the-art transformer-based models like PVT, UniFormer or TransNeXt.

### Questions
1. What is the interpretation of the gradual decay of the mixing weight \((1 - \alpha)\) over training epochs, and how does it affect model performance or convergence?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper study the channel mixer of ViT MLPs, showing that dense feature mixing can be replaced by sparse feature mixing of higher internal feature dimensionality for improved accuracy, without increased complexity.  The work presents a range of experiments that sufficiently support its claims.

### Strengths
1. The writing is easy to read and clearly explains everything in the paper.
2. The experimental result is good compared to the previous works. Empirically, the method seems to offer strong accuracy, compared to existing methods with similar architectures.

### Weaknesses
1. I am concerned about the generalization of this method to other data sets.
2. Some details are missing. For Block Diagonal MLP, how to split the feature vectors of (1)-(2) into disjoint groups? What criteria is it based on？What's the motivation for designing the Channel Covariance Attention (CCA)? It didn't show more details.
3. How is the design like channel mixer relate to improving performance for example? It seems inadequate that none of were seriously discussed in the manuscript.

### Questions
1. I am concerned about the generalization of this method to other data sets.
2. Some details are missing. For Block Diagonal MLP, how to split the feature vectors of (1)-(2) into disjoint groups? What criteria is it based on？What's the motivation for designing the Channel Covariance Attention (CCA)? It didn't show more details.
3. How is the design like channel mixer relate to improving performance for example? It seems inadequate that none of were seriously discussed in the manuscript.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the channel-mixer of modern vision architectures, and propose the SCHEME module, a new channel-mixer that split features to multiple sub channel groups and project these channel groups to lager dimensionality for learning richer internal representation. A channel covariance attention is designed to make information exchange among sub channel groups during training time. The experiments show that the proposed SCHEME outperforms the traditional channel-mixers (e.g., FFN/MLP) in several tasks.

### Strengths
1. The paper is well-structured, providing a clear and accessible overview of the motivation and methodology behind the proposed approach. The logical flow enables readers to easily understand both the problem addressed and the design of the proposed solution.

2. The methodology section is well-developed, with good supporting arguments for each component. The progression from MLP to BD-MLP, followed by the integration of CCA, is clear, well-motivated.

3. The use of CCA as a regularizer for BD-MLP to facilitate interaction across channel groups during training, while discarding it during inference to streamline computational efficiency, is an innovative and effective approach.

4. The proposed SCHEME module and its various configurations demonstrate impressive performance across a range of tasks.

### Weaknesses
1. The labels and coordinates in Figures 1, 3, and 4 are too small, making them challenging to interpret. For a basic academic paper, readability of figure details is essential.

2. The effectiveness of the proposed SCHEME is primarily validated on MetaFormer. While the authors briefly present results on other backbones like Swin and DaViT in Figure 4 (yet difficult to interpret). SCHEME’s generalizability is limited by testing primarily on ViT-based architectures, lacking ablation on modern ConvNet architectures (e.g., ConvNeXt [1], FasterNet [2], and InceptionNeXt [3]) that also use FFN/MLP modules.

3. Although SCHEME shows theoretical complexity advantages, its on-device efficiency is underexplored. Only limited throughput comparisons are presented in Tables 4 and 8. Since an on-device benchmark has been implemented, including detailed on-device results across ablation and comparison studies would substantiate claims about SCHEME’s efficiency over conventional FFNs. Additionally, details on the benchmark configurations, hardware, and input shapes are necessary to ensure fair comparisons.

4. The CCA component functions as a channel mixer and resembles linear attention mechanisms in NLP and prior work in XCiT [4]. A discussion of the differences between CCA and these methods, alongside proper citations, would clarify the novelty and address potential ethical concerns regarding prior art.

5. While SCHEME’s performance is strong and well-motivated, the contribution could be strengthened with deeper analysis. SCHEME integrates Block Diagonal MLP and CCA, elements with roots in existing literature. A more detailed explanation of how SCHEME specifically influences learned representations would underscore its contribution.

6. The comparison methods are outdated and do not represent state-of-the-art accuracy-efficiency models. Including comparisons with recent approaches like FasterViT [5], FastViT [6], and MobileOne [7] would enhance the experimental validity.

7. SCHEME is tested only on small model scales (<60M), which aligns with its efficiency-focused motivation. However, a benchmark of on-device speed on mobile devices is necessary to validate the proposed method’s real-world application, as many recent studies have done [6,7].

### Questions
Please first deal with the major concerns above. There are some minor issues below.

1. The learnable weight $\alpha$ enables CCA as a regularizer during training, discarded for efficiency during inference. However, this approach may create potential conflicts in optimization objectives. Why not consider using more established techniques, such as Structural Re-parameterization, to achieve structure changes between training and inference?

2. Clarification is needed on the smoothing factor $\tau$ — is it a learnable parameter or a constant?

3. There are a few typographical errors, such as a double 'of' in Line 041 of the abstract.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper concentrate on the  channel mixer or feature mixing block design and propose a block diagonal MLP structure with a lightweight, parameter-free, channel covariance attention (CCA) module to improve the feature clusters formed. Replacing the vanilla MLP with proposed SCHEME module, various experiments were conducted to validate its performance.

### Strengths
1. Channel mixer design, the focus of this paper, is a more than interesting topic for the backbone design.
2. Comprehensive vision experiments (*e.g.*, classification, detection, segmentation) and analysis (*e.g.* `Paragraph 3`in `Sec 4.2` for channel covariance attention) were conducted to validate the proposed method's performance.

### Weaknesses
1. With regard to the design of channel mixer, there exists many previous research, such as gMLP[1], channel aggregation module in moganet[2], S2-MLP[3]. In addition to comparing with models using traditional MLP, these should also be taken into account. The current comparisons lack a thorough analysis against these relevant channel mixing techniques, particularly in terms of computational cost and performance trade-offs. A more detailed comparison, including metrics like FLOPs and latency, would be beneficial.
2. More scaling experiments are needed. In this paper, the biggest model was 58M in `Tab.1`, which may could only match the `base-size` model in general. To comprehensively validate the method's scaling capability in backbone, `Large` or even `X-Large` model are also need. The absence of experiments on larger models limits the conclusions that can be drawn about the method's effectiveness in high-capacity scenarios. It is crucial to demonstrate that the proposed approach can maintain its performance advantages as the model size increases, which is a key factor in practical applications.
3. Typos for the dimension of $W_1$ in `Line 196,221`, $N$ -> $d$.

### Questions
See `Weaknesses`.

### Soundness
4

### Presentation
3

### Contribution
4
