# MaskMamba: A Hybrid Mamba-Transformer Model for Masked Image Generation

- Decision: Reject
- Scores: 5, 5, 5, 6, 5

## Abstract
Image generation models have encountered challenges related to scalability and quadratic complexity, primarily due to the reliance on Transformer-based backbones. In this study, we introduce MaskMamba, a novel hybrid model that combines Mamba and Transformer architectures, utilizing Masked Image Modeling for non-autoregressive image synthesis. We meticulously redesign the bidirectional Mamba architecture by implementing two key modifications: (1) replacing causal convolutions with standard convolutions to better capture global context, and (2) utilizing concatenation instead of multiplication, which significantly boosts performance while accelerating inference speed. Additionally, we explore various hybrid schemes of MaskMamba, including both serial and grouped parallel arrangements. Furthermore, we incorporate an in-context condition that allows our model to perform both class-to-image and text-to-image generation tasks. Our MaskMamba outperforms Mamba-based and Transformer-based models in generation quality. Notably, it achieves a remarkable $54.44\%$ improvement in inference speed at a resolution of $2048\times 2048$ over Transformer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MaskMamba, hybrid model combining Mamba and Transformer architectures, designed for non-autoregressive image synthesis through Masked Image Modeling. It adapts bidirectional Mamba by (1) replacing causal with standard convolutions to improve global context capture and (2) using concatenation instead of multiplication to boost performance and speed up inference. The model also explores different hybrid configurations, including serial and grouped parallel arrangements. Experiments are conducted on class conditional and text conditional image generation.

### Strengths
This paper is generally in good shape, and the reported results are promising. For example, the structure is well-defined and smoothly covers all changes (albeit with various degrees of detail). Multiple experiments and comparisons are conducted to evaluate the proposed model and visual results and code of the proposed block are provided in the appendix.

### Weaknesses
There are several issues with the paper as currently presented to be considered for a top tier conference:

- Text-to-image models cannot be accurately evaluated with image metrics alone—CLIP score, ImageReward, and additional benchmarks like TIFA and T2I-CompBench are necessary for a comprehensive assessment.
- The proposed method consistently has more parameters than the transformer baselines, yet these baselines don’t receive any benefit of the doubt for this disparity.
- The baseline models are notably weak, limited to outdated versions, and lack diffusion models, resulting in an incomplete evaluation framework. 
- The rationale for the group scheme and serial scheme designs is missing—they appear abruptly with no background on the issues they address, the process that led to their design, or previous attempts that were unsuccessful.
- The description of the 20-step approach as "non-autoregressive" is misleading; while it may not be causal, it’s also not a 1-step approach, which creates confusion.
- The paper mentions that convolutions "impose constraints that hinder scalability," but lacks clarification, details, or citations to support this claim. In particular, the paper still puts an emphasis on using convolutions.
- There’s insufficient explanation on the distinctions between forward and backward SSM, as well as on the transition from bi to bi-v2, leaving the motivations for these changes unclear.
- It’s unclear if a consistent dropout value is applied; if so, the specific value should be specified.

### Questions
-

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, a new bidirectional Mamba structure is designed to improve the inference speed, and several hybrid Mamba schemes are explored.

### Strengths
1. The writing logic of this paper is very clear and easy to understand, from the rationality of raising questions to making improvements.
2. The referencing speed has been greatly improved.

### Weaknesses
1. The contribution of the paper is relatively limited, and replacing multiplication with concatenation would obviously improve inference speed, but its rationality and motivation should be properly explained, and the change should also be compared in detail with Bi-Mamba.
2. The paper mentions that it can complete the text-to-image task simultaneously, but there is no comparison of its performance on this task throughout the paper, which raises questions about its performance.
3. The comparison shown in Figure 5 reveals huge gaps in certain parameters, including IS and Precision, for this model.
4. A more detailed comparison with Bi-Mamba should be conducted, and Precision and Recall

### Questions
Please answer the question I mentioned in "weakness".

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced a new non-autoregressive model for image generation. It replaces the transformer architecture in MaskGIT with MaskMamba, where some of the transformer layers are replaced with a new Mamba layer with forward and backward SSM. The authors show reasonable image generation results on ImageNet, as well as proof-of-concept speedup results at 2048x2048.

### Strengths
- It is very reasonable to introduce Mamba or SSM layers in high-resolution, MaskGIT-based image generation. SSM models naturally have better capability handling long sequences compared with transformer models.
- The ablation study provides valuable insights on the combination of Mamba blocks and transformer blocks (MMM..SSS is better than MS...MS). 
- The authors also show promising signals that the proposed method can scale up to text-to-image generation.

### Weaknesses
1. Experiment results on ImageNet are not strong enough.
- 5.79 FID at 741M parameters is far from the state-of-the-art (for example, MAGVITv2). 
- The cited baselines are also a bit weak. MaskGIT can achieve much better results using a better tokenizer and training recipe. See [here](https://github.com/baaivision/MUSE-Pytorch/tree/master) and [here](https://github.com/bytedance/1d-tokenizer/tree/main) for more details. It is also recommended to have a look at Open-MAGVITv2's tokenizer, which should be orthogonal to this work and could push the results closer to SOTA.

2. There is a little bit of overclaim in terms of the speedup over transformer in the abstract. "54% faster" refers to the comparison between a single Mamba layer and a single transformer layer, not the end-to-end speed comparison. In fact, MaskMamba is a hybrid model and there are many transformer layers inside the entire model as well. It would be misleading for the readers when reading the last sentence in the abstract. 

3. Although introducing SSMs in non-autoregressive image generation models is interesting, the paper lacks technical novelty. It seems to me that this work is combining MaskGIT with Jamba, a hybrid transformer-Mamba model for language.

### Questions
Please address my concerns in the "Weaknesses" Section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors build upon the Mamba architecture to tackle the subject of image generation, class conditions and text conditioned, using a masking approach inspired from MaskGIT. The model is trained to predict mask tokens and at inference, only a fraction of the tokens are unmasked, iteratively, until all tokens are predicted.

Specifically, the authors propose:
* architecture changes to the Mamba architecture (causal convolutions are replaced with full convolutions, flipping the backward SSM branch)
* combining the Mamba blocks for the first N/2 layers with transformer blocks at the last N/2 layers

The new architecture shows:
* Similar or slightly better results than a full transformer of similar size
* Faster inference, up to 1.5X faster on larger image size and larger models

### Strengths
* Interesting architecture, which seems to bring interesting improvements on inference speed.
* Detailed analysis of architectural changes
* Tested on both class conditioned and text condition image generation
* Well written paper, easy to follow

### Weaknesses
* The architecture seems a bit cumbersome:
  * Having to care about the position of the conditioning (the authors show that it is important) is a major downside compared to transformer based architectures
  * Tuning this architecture is likely harder, because of the mix of convolutions and transformers, each with different optimization patterns (simplicity is a quality)
* The boost of performance is not that important, -0.17 FID on XL architecture, and highly depends on the position of the conditioning, Tail or Head conditioning in Table 5 do lead to similar or worse performance than transformer in Table 4. The main benefit is mostly inference speed, which is something that can be tuned for transformers as well and more of a problem for video generation (it could be super interesting to test it there)
* The baseline approach is far from SOTA (for example, MAR gets much lower FID on ImageNet 256, and much faster inference speed) and so it would be more impactful to apply this to MAR-like approach to see if that still brings benefits.
* If anything, the paper shows that transformers are needed for image generation, as shown in Table 4, defeating a bit the interest in Mamba.

### Questions
n/a

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The writing is clear and easy to understand. Building on MaskGit, the paper explores the combination of the Mamba architecture with various Mamba module designs and its integration with transformers. Experiments demonstrate that MaskMamba achieves solid performance on both ImageNet and CC3M.

However, the paper lacks a more comprehensive comparison, including related methods such as VAR, MAR, and diffusion models. Additionally, comparisons with other Mamba-based approaches in the field of image generation are missing. In terms of experimental design, evaluations are primarily conducted at 256 resolution, where MaskMamba is slower than transformers. However, results are not presented at higher resolutions (above 1024), where MaskMamba is claimed to have an advantage.

### Strengths
The writing is clear and easy to understand. Building on MaskGit, the paper explores the combination of the Mamba architecture with various Mamba module designs and its integration with transformers. Experiments demonstrate that MaskMamba achieves solid performance on both ImageNet and CC3M.

### Weaknesses
The paper lacks a more comprehensive comparison, including related methods such as VAR, MAR, and diffusion models. Additionally, comparisons with other Mamba-based approaches in the field of image generation are missing. In terms of experimental design, evaluations are primarily conducted at 256 resolution, where MaskMamba is slower than transformers. However, results are not presented at higher resolutions (above 1024), where MaskMamba is claimed to have an advantage.

### Questions
Q1: The text condition length is set to 120. Can this be variable?

Q2: There seems to be an inconsistency between Figure 4(a) and the description of bi-mamba-v2 on line 249. Could you please align these?

Q3: The reason CFG works is due to the matching of two probability distributions. However, in AR, VAR, and MAR, the cross-entropy loss is not about matching two probability distributions. Why does CFG still work in this case? Could there be a possible explanation?

Q4: In Table 2, the comparison lacks similar works involving VAR [1] and MAR [2], as well as comparisons with CFG-based diffusion models. Additionally, several diffusion models [3, 4, 5] based on the Mamba architecture are not discussed in this paper. Could you elaborate further on the advantages of MaskMamba in terms of performance and speed? As I review the paper, it appears that MaskMamba still requires 20+ steps to generate.

Q5: Within 1024 resolution, single-layer bi-mamba-v2 is slower than the transformer. This time difference could accumulate with additional layers, which is not a positive indicator. The claim is that bi-mamba-v2 is faster beyond 1024px, but the experiments were only conducted on ImageNet at 256px. It remains unclear how performance scales from 256px to 512px, and then to higher resolutions such as 1024px and 2048px.

[1]. Tian K, Jiang Y, Yuan Z, et al. Visual autoregressive modeling: Scalable image generation via next-scale prediction[J]. arXiv preprint arXiv:2404.02905, 2024.
[2]. Li T, Tian Y, Li H, et al. Autoregressive Image Generation without Vector Quantization[J]. arXiv preprint arXiv:2406.11838, 2024.
[3]. Teng Y, Wu Y, Shi H, et al. DiM: Diffusion Mamba for Efficient High-Resolution Image Synthesis[J]. arXiv preprint arXiv:2405.14224, 2024.
[4]. Fei Z, Fan M, Yu C, et al. Dimba: Transformer-Mamba Diffusion Models[J]. arXiv preprint arXiv:2406.01159, 2024.
[5]. Hu V T, Baumann S A, Gui M, et al. Zigma: Zigzag mamba diffusion model[J]. arXiv preprint arXiv:2403.13802, 2024.

### Soundness
2

### Presentation
3

### Contribution
2
