# NeRF Compression via Transform Coding

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Neural Radiance Fields (NeRFs) have emerged as powerful tools for capturing detailed 3D scenes through continuous volumetric representations. Recent NeRFs utilize feature grids to improve rendering quality and speed; however, these representations introduce significant storage overhead. This paper presents a novel method for efficiently compressing a grid-based NeRF model. Our approach is based on the non-linear transform coding paradigm, where we compress the model's feature grids using end-to-end optimized neural compression. Since these neural compressors are overfitted to individual scenes, we develop lightweight decoders and encoder-free compression. To exploit the spatial inhomogeneity of the latent feature grids, we introduce an importance-weighted rate-distortion objective and a sparse entropy model using a masking mechanism. Our experimental results validate that our proposed method surpasses existing works in terms of grid-based NeRF compression efficacy and reconstruction quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel method for efficiently compressing a grid-based NeRF model. It utilizes neural compression method to compress the model's feature grids. Specifically, the authors design an encoder-free architecture with a lightweight decoder, and present a weighted-rate-distortion loss incorporated a masked entropy coding mechanism to reduce redundance. The results show that the proposed method outperforms existing works.

### Strengths
1. The paper is well-written and effectively communicates the proposed method and its technical details. The authors provide clear explanations of the neural compression based framework.
2. The paper introduces a novel neural compression based framework for NeRF, which is a unique approach compared to existing compression methods that rely on pruning or vector quantization.

### Weaknesses
1. While the introduction of a neural compression method to encode the grid representation has demonstrated superior RD performance, the underlying motivation for this approach is not adequately elucidated.

2. The novelty of this paper is not sufficient. The introduction of the weighted-rate-distortion loss lacks significant new contributions, as it heavily relies on an existing importance score calculation method [1]. The proposed binary mask entropy coding resembles the concept of importance map-based bit allocation schemes, such as in [2]. Moreover, the compression method falls short in considering contextual information for further reduction of spatial redundancy.

3. It would be beneficial to include a comparison of the training time between the proposed method and other established methods. Additionally, the paper should provide a more precise breakdown of the storage sizes for each component, including the decoder, entropy model, binary mask, and grid feature.

4. The term 'transform coding' in the paper's title may not be entirely appropriate, as the paper employs an encoder-free framework that directly learns the latent code without involving analysis transforms within the coding paradigm

### Questions
1."What are the advantages of the proposed compression method when compared to existing pruning or vector quantization methods?"
2."Have the authors considered the results of incorporating an encoder and training the entire network end-to-end?"
3."It is recommended that the authors provide a detailed breakdown of the storage size for each component to offer a more comprehensive understanding."
4. In Figure 5, I noticed that the blue curve (TC-TensoRF-L) is situated below the orange (w/ Factorized Prior) and green (w/o Importance Weight) curves in the lower bitrate range. Could you please provide an explanation for this observation?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to compress the NeRF model’s feature grids using end-to-end optimized neural compression. By transmitting the latent code and a lightweight decoder, this method can significantly reduce the storage costs of NeRFs. Experiments on different
datasets show that this method is capable of compressing diverse NeRF scenes to a smaller size and outperforms previous works.

### Strengths
1) The paper is overall well-written and easy to read. 

2) The proposed method applies a neural transform coding framework to compress the feature planes in NeRF. The overall performance is good, especially at relatively low bitrates. This method can be treated as a new route for NeRF compression besides network pruning and quantization.

### Weaknesses
1) Compared with existing work like VQ-TensorRF, the performance gain of the proposed method under a similar compression ratio is marginal in some cases (for low compression). Besides, this work is currently only designed for feature plane-based NeRF methods while other compared methods are more generalized. Specifically, the paper lacks a detailed analysis of the performance differences at varying compression levels. The claim of marginal gains needs more rigorous justification, perhaps by showing a more comprehensive set of rate-distortion curves across different datasets. The restriction to feature plane-based NeRFs limits the applicability of this method, and the paper should acknowledge this limitation more explicitly and discuss potential avenues to extend the approach to other NeRF architectures.

2) The training and rendering time, especially the time needed for compressing and decompressing the features should be provided and compared with previous works. The paper should include a detailed breakdown of the computational costs associated with each stage of the proposed method, including the time required for encoding, decoding, and rendering. This analysis should be compared against the baseline methods to provide a clear picture of the trade-offs between compression efficiency and computational overhead. Without this information, it is difficult to assess the practical viability of the proposed approach.

3) The overall contribution of this paper is not sufficient enough. The transform coding framework is also similar to existing frameworks in image and video compression. While the application of transform coding to NeRF is interesting, the paper does not sufficiently highlight the novel aspects of this application. The paper should discuss the specific challenges and adaptations required to apply transform coding to the feature grids of NeRFs, and how these adaptations differ from traditional image and video compression techniques. The current presentation makes the method seem like a straightforward application of existing techniques, which diminishes the perceived contribution.

### Questions
The author proposed the latent decoder without an encoder. It will better demonstrate the efficiency by also showing the performance of a compressor with both an encoder and decoder during training and then drop the encoder during inference.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel compression method for grid-based NeRF models, such as TensoRF. It optimized three latent codes and a decoder during training time, after training the full feature grid was omitted to reduce storage size. To achieve original rendering quality it directly reconstructs the full resolution feature plane with the learned latent code and decoder. Furthermore, an importance-weighted training loss was adopted to push the optimization focus on grid location that contributes more in rendering and a binary entropy mask to further reduce redundancy.

### Strengths
The semantics of the paper is smooth, and the proposed method is simple yet effective, it achieves better performance than previous methods that have a more sophisticated procedure, and the overall framework is very straightforward, so there should be no difficulty for other to reproduce.

### Weaknesses
1. The improvement over the previous method is not so significant,  the TC-TensoRF-L only shows notable improvement in the LLFF dataset, while in other datasets, it only brings minor performance gain in both visual quality（PSNR）and storage size. Though it provides a trade-off curve against VQ-TensoRF, the author only changed the codebook size of VQ-TensoRF, which may indicate that the curve was not drawn on the optimal hyper-parameter for VQ-TensoRF.

2.  Though the author has discussed DVGO and Plenoxels and tends to treat applying compression to those methods as a future work, I believe this could be a major weakness to not showing that the proposed is capable of generalize to other grid-based methods. As those methods have different design methodology e.g. plenoxels is already sparse and do not rely on MLP to recover feature in grid point. and it is important to show the proposed transform coding can still work for different types of grid-based nerf.

### Questions
what is the final composition of the storage size? It would be better to display the composition in a chart or figure to help others better understand the proposed method.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
