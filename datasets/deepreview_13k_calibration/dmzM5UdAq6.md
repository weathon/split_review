# Progressive Token Length Scaling in Transformer Encoders for Efficient Universal Segmentation

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
A powerful architecture for universal segmentation relies on transformers that encode multi-scale image features and decode object queries into mask predictions. With efficiency being a high priority for scaling such models, we observed that the state-of-the-art method Mask2Former uses $>$50\% of its compute \textit{only} on the transformer encoder. This is due to the retention of a full-length token-level representation of all backbone feature scales at each encoder layer. With this observation, we propose a strategy termed \textbf{PRO}gressive Token Length \textbf{SCAL}ing for \textbf{E}fficient transformer encoders (\ours) that can be plugged-in to the Mask2Former-style segmentation architectures to significantly reduce the computational cost. The underlying principle of \ours is: progressively scale the length of the tokens with the layers of the encoder. This allows \ours to reduce computations by a large margin with minimal sacrifice in performance ($\sim$52\% GFLOPs reduction with \textit{no} drop in performance on COCO dataset). We validate our framework on multiple public benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to Progressive Token Length Scaling, a strategy designed to enhance the efficiency of transformer encoders in universal segmentation models. The authors identify that the state-of-the-art model, Mask2Former, devotes over 50% of its computational resources to the transformer encoder, largely because it processes a full-length token representation from all backbone feature scales at every encoder layer. This paper addresses this inefficiency by progressively scaling the token length with each encoder layer, thereby significantly reducing computational demands—specifically, achieving around 52% reduction in GFLOPs—while maintaining performance levels on the COCO dataset.

### Strengths
The progressive integration of finer-grain information within the transformer encoder is an intuitive and straightforward approach that proves to be both simple and effective.

A comprehensive set of experiments on segmentation and detection tasks validate the design choices of the PRO-SCALE architecture, demonstrating its effectiveness.

The paper is clearly written and easy to follow, enhancing its accessibility and understanding.

### Weaknesses
None

### Questions
What distinguishes the LPE module from traditional fully convolutional network (FCN) style upsampling methods?

If I understand correctly, the computational costs in P1 and P2 are quadratically lower compared to P3. Would it be advantageous to use a different number of layers for each split instead of maintaining the same number of layers across all splits?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an efficient transformer encoder architecture that progressively increases token length and feature scale, coupled with a LPE module. This approach achieves an effective balance between computational efficiency and segmentation quality.

### Strengths
1. The paper presents its ideas with clarity and good technical writing.
2. The experimental validation is comprehensive, featuring:
    - Thorough comparative analyses
    - Well-structured ablation studies
    - Clear demonstration of each component's contribution to overall performance

### Weaknesses
1. In Table9 for FPS comparison, while Lite-M2F and RT-M2F are used as baselines in other evaluations, a complete comparison with all baseline models on FPS would strengthen the efficiency claims
2. The paper states that ReMaX is orthogonal to the approach and ineffective on larger models, but could you provide quantitative evidence? Currently, the table results only demonstrate ReMaX has a good performance.

### Questions
For Figure6, could you provide more visualization comparisons with also some baselines like Lite-M2F, RT-M2F, or PEM?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the “PRO-SCALE” strategy to reduce the computational cost of Mask2Former encoders. The proposed approach can significantly reduce computations with minimal sacrifice in performance.

### Strengths
1. The writing and motivation of this paper is very clear. 
2. The proposed method seems to achieve a better trade-off than several recent related approaches.

### Weaknesses
1. Although the authors emphasize the computational burden of the transformer encoder and propose dedicated methods to reduce computations, the overall reduction in proportion is not very obvious. The descriptions in the abstract seem to overstate the effect. It is better to clarify that 52% GFLOPs reduction in computation is for the encoder.

2. A figure to intuitively show the comparisons in trade-off (speed vs performance or FLOPs vs performance) is necessary for understanding the practical value of the approach.

3. The LPE module also contributes a lot to the reduction in computation. However, it is mainly because the computational efficiency of vanilla convolutions is too low. This further indicates that the proposed PRO-SCALE is not so important for the reduction of computational complexity of the entire system. Strictly speaking, the pixel embeddings generation module is not part of the transformer encoder. Compared to the LPE module, the TRC module in the appendix seems more interesting.

### Questions
Why not use depth-wise 3x3 convolutions for the LPE module?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents *PRO-SCALE*, a method to improve the efficiency of the “transformer encoder” component of the state-of-the-art Mask2Former model for universal image segmentation. In Mask2Former, this transformer encoder (also called ‘pixel decoder’ [a]) takes the tokens of multi-resolution features from the backbone, applies multiple layers of deformable attention to all tokens, and then feeds them to the segmentation decoder. In contrast, PRO-SCALE applies the first deformable attention layers only to a small number of low-resolution feature tokens, and then gradually adds higher-resolution features in subsequent layers. By doing so, the number of operations is lower than in the original transformer encoder. Additionally, to efficiently generate the highest-resolution features that the decoder needs, PRO-SCALE contains a *Light Pixel Embedding* (LPE) module that applies max-pooling to high-resolution features from the backbone. With experiments on multiple datasets and with multiple backbones, PRO-SCALE is shown to reduce the total number of FLOPs by up to 27%, while keeping the segmentation quality (PQ, mIoU, AP) roughly the same as for Mask2Former. Additional experiments show that PRO-SCALE is also effective in combination with open-vocabulary and object detection models.

[a] Cheng et al., “Masked-attention Mask Transformer for Universal Image Segmentation”, CVPR 2022.

### Strengths
1.	The proposed method is simple but effective. It is simple because there are only two relatively small changes with respect to the original transformer encoder of Mask2Former: (a) the first deformable attention layers are applied to only a subset of the feature tokens, and (b) the model applies max-pooling on the highest-resolution features. By doing so, PRO-SCALE can reduce the total number of FLOPs of Mask2Former by up to 27%, without causing a drop in Panoptic Quality (PQ), mean IoU or Average Precision (AP). Although the adjustments to Mask2Former are minimal and the technical innovation of PRO-SCALE is limited, I believe it is valuable because the paper critically examines an inefficient component of a frequently used model, and finds that it can be made considerably more efficient while keeping the performance roughly the same, with only minor changes to the design.
2.	Through experiments, PRO-SCALE is not only compared to Mask2Former with its default transformer encoder, but also to existing efficient versions of the transformer encoder that were proposed for object detection method DETR, i.e., Lite-M2F and RT-M2F in Tab. 1 and Tab. 2. The results of these comparisons show that PRO-SCALE also achieves a better efficiency-accuracy balance than these existing methods. This demonstrates the value of PRO-SCALE compared to these existing methods. 
3.	The paper contains many ablations and additional experiments (Tab. 3 to Tab. 7), which properly show the impact of different design choices and demonstrate the effectiveness of PRO-SCALE in different experimental settings, e.g., with different backbones or pre-training. 
4.	Through experiments, the paper shows that PRO-SCALE is not only effective on Mask2Former, but also on other models for other tasks. The results in Tab. 8, Tab. 10 and Tab. 11 show that PRO-SCALE achieves similar FLOPs reductions in the encoder when combined with object detection model DETR, two open-vocabulary segmentation models, and instance segmentation model Mask-DINO, while obtaining similar or better segmentation performance. This shows that the proposed PRO-SCALE method is more generally applicable than just on Mask2Former.

### Weaknesses
1. The paper does not clearly explain how the original Mask2Former model generates the high-resolution *per-pixel embedding map* ${\mathcal{E}_{emb}}$, and why this is less efficient than how PRO-SCALE does it with LPE. L242-L243 states that $\mathbf{s}_1$ serves the purpose of creating the per-pixel embedding map, and that it uses a convolutional layer, but there is no clear description or depiction of the exact manner in which this is done. How many convolutional layers are used? What other operations are used? As a result, it is not fully clear what the exact differences are between the LPE module and the existing method. As a result, it is also not clear why the newly proposed LPE module is more efficient.
2. Related to this, some details are missing about the exact operation of the LPE method. Concretely, what is the stride of the MaxPool2D operation? Is it the same as the kernel size? If the stride is >1, then what is the impact of changing the stride (and therefore the resolution of ${\mathcal{E}_{emb}}$) on the results, both qualitatively and quantitatively? This information is currently not available.
3. Sec. 3.1 (L233-L236) briefly mentions that PRO-SCALE additionally uses a so-called *token recalibration* operation, which enriches small-scale features with high-scale features to further enhance the segmentation accuracy. However, despite being part of the PRO-SCALE method, this operation is not visualized in Fig. 3, and not explained properly in Sec. 3.1. As a result, (a) Fig. 3 makes it seem like this operation does not exist at all, and (b) it is unclear from the main paper how a part of the method works. In other words, this *token recalibration* operation should be explained and visualized in the main paper.
4. Related to the previous point, the efficiency of the *token recalibration* operation is not evaluated, neither in the main paper nor in the appendix. As a result, it is not clear if it is actually efficient.
5. For most experiments, the paper reports the FLOPs but not the latency/FPS/throughput of the model. The FPS is only reported for the overall model in Tab. 9. As a result, for most configurations, it is not clear how/if the reduction in FLOPs translates to a speedup when the model is run on a GPU. The results of the paper would be stronger if the FPS/latency of the model was also reported for other experiments, i.e., at least for the main results in Tab. 1 and Tab. 2, and the ablations in Tab. 3, Tab. 5 and Fig. 4, but ideally even more. Notably, with the results currently presented in Tab. 15, there is no benefit of using PRO-SCALE instead of Lite-M2F. In this table, Lite-M2F obtains a better PQ than PRO-SCALE while achieving a similar prediction speed. This limits the value of PRO-SCALE. Additionally, the newly provided FPS results in Tab. 3 show that the impact of using the LPE module on the model’s prediction speed is very limited. While using the LPE module reduces the GFLOPs from 73.49 to 55.14 (25% decrease), the FPS only increases from 6.36 to 6.47 (2% increase). Moreover, using the module introduces a 1.15 PQ drop. In other words, while the efficiency impact in terms of GFLOPs may seem large, it is almost negligible in terms of actual prediction speed, while also leading to a performance drop. Therefore, this LPE module has little value in practice.
6. PRO-SCALE does not yield a significant efficiency improvement when used in combination with large backbones, e.g., Swin-L (see Tab. 7). Of course, this is expected, as the Swin-L backbone accounts for a much larger portion of the overall number of FLOPs than Swin-T, but it is still a weakness because PRO-SCALE’s value in larger models is limited. If one wants to achieve the best possible segmentation performance, then opting for a small backbone instead of a larger one is typically not an option, as this limits the performance.
7. The abstract contains a misleading statement. L023 states that PRO-SCALE can achieve a ~52% GFLOPs reduction with no drop in performance on the COCO dataset. This statement implies that, compared to the original Mask2Fomer, the overall PRO-SCALE model requires ~52% fewer GFLOPs. However, Tab. 1 shows that this 52% GFLOPs reduction concerns the encoder only, and that the overall GFLOPs reduction of the model is ~27%. The statement in the abstract should be altered by either specifying that the 52% reduction concerns the encoder, or changing the number from 52% to 27%.
8. Tab. 8, Tab. 10 and Tab. 11 only contain GFLOPs results for the encoder, not for the entire model. As a result, it is not clear what the actual overall improvement is of PRO-SCALE.
9. L323 & L358 state that ReMaX is limited by the inherent efficiency of the model, but the efficiency for ReMaX is not provided in Tab. 1 or Tab. 2. In other words, this claim is not substantiated.
10. L454-L455 states that, on average, the MoBY pre-trained backbone causes lower performance degradation than SL pre-trained weights, especially for instance segmentation. However, per Fig. 5 (right), compared to the Mask2Former baseline, the average drop for MoBY over all 4 settings is -2.35 AP, while it is -1.49 for supervised learning. Therefore, this statement is incorrect. This statement is not very important for the main message of the paper, so it doesn’t impact the value of the proposed method, but it should be altered nevertheless. The new statement in the paper (L456-L458) is still incorrect, as it still refers to this “performance degradation”.

Some minor points, which do not significantly affect my overall rating:

11. The text contains several mistakes/errors. Some examples:

    a. L039 – “framework exhibit exceptional performance” => “framework exhibits exceptional performance”

    b. L136 – “making Mask2Former universal segmentation model” => “making the Mask2Former universal segmentation model”

    c. L153 – “map and class prediction heads” => “mask and class prediction heads”

    d. L358 – Not clear what is meant by “becomes ineffective efficient”

    e. L377 – "effieiciency" => "efficiency"

    f. L376-L377 – “strong … than” => “stronger … than”

    g. L436 – “$p_2$ vs. ($p_2$ + 3)” should be “$p_2$ vs. ($p_2$ + 2)”, as the baseline is $p_2 = 1$ and the comparison is “1 vs. 3”.

    h. L437 – Likewise: “$p_3$ vs. ($p_3$ + 3)” => “$p_3$ vs. ($p_3$ + 2)”.

    i. L503 – The caption of Tab. 11 states that PRO-SCALE achieves a better PQ, but the PQ is not reported in Tab. 11.

    j. L534-L535 – “for Mask2Former universal segmentation framework” => “for the Mask2Former universal segmentation framework”

12. In Tab. 3, the experimental setting is not explicitly indicated. The numbers correspond with Swin-T on Cityscapes, but this is not explicitly mentioned in the caption. This should be mentioned, so that the table can be understood without having to check other tables.

13. The paper uses an inconsistent number of decimals for results on the same metrics. For instance, in Tab. 3: 132 GFLOPs for $C_1$ and 73.49 for $C_2$. It would be better if the number of decimals was consistent.

### Questions
I would like to ask the authors to address my concerns as formulated in the “weaknesses” section, to answer the questions posed there, and to revise the manuscript accordingly.

One additional question:

1.	How does the presence of redundancy in the feature tokens relate to the presented PRO-SCALE method? Appendix B shows that higher-resolution features have a higher cosine similarity, but it is not clear to me how this observation motivates the PRO-SCALE design, where fewer deformable attention layers are applied to high-resolution features. Could the authors clarify this relation?

---

**Update after author discussion.** After reading the different reviews, the authors' response, and the revised manuscript, and asking some follow-up questions, I decide to keep my original rating. 

While I still believe that the idea of improving the efficiency of the decoder of Mask2Former can be valuable, I mainly have concerns about the actual efficiency of the proposed method. Importantly, the newly provided *prediction speed* results show that the actual efficiency improvement obtained by PRO-SCALE is limited. While PRO-SCALE obtains high FLOPs reductions, the impact on the prediction speed in terms of *frames per second* (FPS) in considerably lower. As a result, PRO-SCALE does not obtain a better *prediction speed vs. segmentation performance* balance than existing method Lite-DETR/Lite-M2F. Furthermore, it turns out that the impact of the LPE module on the prediction speed is almost negligible, while it also causes a segmentation performance drop.

Because the main purpose of the paper is to improve efficiency while keeping the segmentation performance as high as possible, I believe the value of the paper is considerably limited when (a) the proposed method is not shown to obtain a better *prediction speed vs. segmentation performance* balance than a highly related existing method (Lite-M2F/Lite-DETR), and (b) the actual efficiency improvement (in terms of FPS) of one of the main contributions (LPE module) is almost negligible while causing a drop in segmentation performance.

In their response, the authors mention that other benefits of reduced FLOPs are (i) improved energy efficiency because FLOPs correlate with energy use, and (ii) better compatibility and easier deployment on edge devices. However, Henderson et al. [a] experimentally show that there is little correlation between FLOPs and energy usage when comparing across different model architectures. As PRO-SCALE has a different architecture than the default Mask2Former, there is no guarantee that the reduced FLOPs of PRO-SCALE will translate to reduced energy use. As reduced energy usage is also not shown experimentally, this benefit cannot be verified. As for compatibility and deployment on edge devices, the paper provides no evidence or references for these benefits, so these benefits can also not be verified.

Overall, while also considering the strengths of the work and the other reviews, these weaknesses cause me to keep my original rating.

[a] Henderson et al., "Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning," JMLR 2020.

### Soundness
2

### Presentation
2

### Contribution
2
