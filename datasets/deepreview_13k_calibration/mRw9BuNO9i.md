# Effortless Cross-Platform Video Codec: A Codebook-Based Method

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Under certain circumstances, advanced neural video codecs can surpass the most complex traditional codecs in their rate-distortion (RD) performance.  One of the main reasons for the high performance of existing neural video codecs is the use of the entropy model, which can provide more accurate probability distribution estimations for compressing the latents. This also implies the rigorous requirement that entropy models running on different platforms should use consistent distribution estimations. However, in cross-platform scenarios, entropy models running on different platforms usually yield inconsistent probability distribution estimations due to floating point computation errors that are platform-dependent, which can cause the decoding side to fail in correctly decoding the compressed bitstream sent by the encoding side. In this paper, we propose a cross-platform video compression framework based on codebooks, which avoids autoregressive entropy modeling and achieves video compression by transmitting the index sequence of the codebooks. Moreover, instead of using optical flow for context alignment, we propose to use the conditional cross-attention module to obtain the context between frames. Due to the absence of autoregressive modeling and optical flow alignment, we can design an extremely minimalist framework that can greatly benefit computational efficiency. Importantly, our framework no longer contains any distribution estimation modules for entropy modeling, and thus computations across platforms are not necessarily consistent. Experimental results show that our method can outperform the traditional H.265 (medium) even without any entropy constraints, while achieving the cross-platform property intrinsically.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a video compression framework that facilitates cross-platform compatibility by avoiding the need for entropy modeling in probability distribution estimation. To achieve this, this paper leverages codebook-based approaches and proposes window-based cross-attention that avoids the use of optical flow for context alignments. The paper demonstrates the effectiveness of the proposed method compared to existing traditional video codecs.

### Strengths
- The paper is well-written and flows smoothly.
- The motivation for the proposed method seems intriguing in the context of neural video compression.

### Weaknesses
1. **More RD-performance comparison with existing neural video compression methods**: The paper primarily made a comparison with traditional codecs like H.264 and H.265. While Figure 1 demonstrates the artifacts induced by entropy models in cross-platform settings, the paper does not conclusively establish if this issue is prevalent across all neural video compression methods. To strengthen the paper's claims, a more comprehensive RD-performance comparison with a variety of neural methods in similar cross-platform scenarios is necessary. Moreover, the paper should include both qualitative and quantitative results. Given that metrics like PSNR and MS-SSIM might not fully represent the artifacts seen in decompressed frames, the inclusion of perceptual similarity metrics such as LPIPS [1] or FLIP [2] is recommended for a more comprehensive evaluation.

2. **Decoding efficiency**: The paper should also report on decoding efficiency relative to existing neural video compression methods, extending beyond the ablation studies of the proposed modules.

3. **More consideration of cross-platform scenario when encoding/decoding**: The paper presents the scenarios where encoding is done using an NVIDIA Tesla V100 and decoding with a Tesla P40, as detailed in Table 5 of the Appendix. However, this scenario is limited. More examination of diverse scenarios including a broader range of encoding/decoding machines should be included to verify the robustness of the proposed method regardless of the systematic errors across different platforms. 

4. **More comparison with existing calibration methods**: The paper should incorporate a detailed comparison with existing calibration methods. This is crucial for contextualizing the results presented in Table 2 and Table 5. The inclusion of performance comparison with existing calibration methods will significantly enhance the paper's comprehensiveness and the validity of its conclusions.

### Questions
The proposed WCA-based context model is intriguing. However, the presented modules, including the codebook approach and the keyframe and prediction frame categorization, appear as already well-established techniques in the field of neural data compression. While the focus on cross-platform scenarios is an interesting aspect that underscores the effectiveness of your proposed method, it also requires a deeper investigation to distinguish this paper from existing methods. Therefore, to strengthen the claim of the paper, a more comprehensive comparison as mentioned in the weakness section seems crucial. Without them, my evaluation of the paper may be lower.

### Soundness
3 good

### Presentation
3 good

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
1. In this paper authros proposed a cross-platform videocompression framework based on codebooks, which avoids autoregressive entropy
modeling and achieves video compression by transmitting the index sequence of the codebooks.

### Strengths
1.Novelity of the paper is good.
2. Encourging results.

### Weaknesses
1.Related work should be updated.

### Questions
1.Include the recent papers in references.
2.Mention the future scope.
3.Detailed analysis of figure 5 results is required.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper examines video decoding errors in cross-platform scenarios. Inconsistent probability distribution estimations may arise from platform-specific floating point computation errors, which can result in decoding failures for compressed bitstreams. The paper suggests a video compression framework that employs codebooks to represent temporal and spatial redundancy. This framework utilizes a WCA-based context model instead of autoregressive modeling and optical flow alignment.

### Strengths
1. This paper focuses on an important and practical issue of neural video compression. And it proposes one reasonable solution.
2. The design of the multi-stage codebook and window-based cross-attention successfully replaces the common motion compensation and autoregressive modules.
3. The performance of its proposed method is acceptable, which is higher than two common traditional codecs H.265 and H.264.

### Weaknesses
1. The novelty of this paper may be limited as the overall framework bears resemblance to Mentzer et al.'s (2022) approach, which avoids explicit motion estimation by employing a transform-like architecture. Additionally, the use of vector quantization for compression is not new and may have been inspired by Zhu's work in image compression. Furthermore, the windows-based cross attention appears similar to SwinTransformer. Consequently, the major architecture and designs lack sufficient novelty.

2. The experimental results are unconvincing as they only provide data on 1080p videos without including other resolutions such as Class C/D/E. Moreover, the authors solely compare their approach with traditional video codecs like H.265; however, it would be beneficial to include comparisons with learned video codecs that can also be utilized on CPU platforms to reduce decoding errors. These methods should be incorporated into the study.

3. In the experiment section, it is important to set an equal Group of Pictures (GoP) size when comparing the author's model with traditional codecs. Therefore, both H.265 and H.264 GoP sizes should be set at 32 for a fair comparison. Additionally, regarding the proposed codebook method, there might be concerns about error propagation if a larger GoP size is used; thus, it would be valuable for the authors to address this issue in their discussion.

### Questions
How do you calculate the bitrate? And how do you compress the index in the proposed framework? The authors don't provide many details.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the performance of advanced neural video codecs in comparison to traditional codecs, highlighting the role of entropy models in achieving high compression efficiency. However, it points out that cross-platform scenarios often lead to inconsistencies in probability distribution estimations due to platform-dependent floating-point computation errors, which can hinder decoding. To address this, the paper proposes a cross-platform video compression framework based on codebooks, eliminating autoregressive entropy modeling. It also introduces a conditional cross-attention module for context alignment between frames, resulting in a more efficient framework. This approach avoids the need for distribution estimation modules, making it less dependent on consistent computations across platforms.

### Strengths
The structure of this paper is well organized, with clear and concise explanations of the concepts. This paper addresses a significant issue in video compression by tackling the challenges of cross-platform consistency.

### Weaknesses
The experimental results do not effectively validate the method's effectiveness.

1.	Why were tests conducted only on 1080p videos? To validate the method's generality, the authors should test it on videos of different resolutions. Typically, in video compression tasks, testing is done on classes like B, C, D, and E, but the authors have provided results for only class B. To ensure the method's effectiveness across various resolutions, the authors should supplement the results on these different video classes. Additionally, what issues arise from center-cropping input images to multiples of 128? Why not consider the original image dimensions?

2.	The proposed method is trained on V100 FP32 and tested on both V100 FP32 and P40 FP16. I agree that different precision platforms can impact results. However, when testing with the lower precision platform, it's customary to convert FP32 to FP16 for comparison. Have the authors provided such comparisons, particularly with traditional methods like H.265 and H.264?

3.	How was the codebook generated? It is mentioned that Zhu et al.'s method is used. Could they provide specific details on the training process, or did they directly employ pre-trained codebook? If that, how can we guarantee that this codebook can adapt to the testing dataset?

4.	Why wasn't bitrate considered during training? Would joint optimization potentially yield better results?

5.	Could the authors provide an explanation for the design of codebook sizes as mentioned here? “While for predicted frames, we use three different groups of codebook sizes to achieve different video compression ratios as {8192, 2048, 512}, {64, 2048, 512} and {8, 2048, 512}.”

6.	I believe that using codebooks for compression is not only cross-platform but also an efficient approach. Why haven't the authors compared their method with more recent approaches like VVC and DCVC-DC?

7.	The authors used GOP=12 for H.264 and H.265 configurations, but the model in the paper used GOP=32. Setting H.264/H.265 configurations to GOP=32 would ensure a fairer comparison.

8.	H.264 and H.265 compression configurations seem a little different from the common test configuration. Could you provide specific instructions for H.264 and H.265 compression configurations?

9.	In Sec 2.1, “Consequently, To avoid….” here 'T' should be lowercase.

### Questions
Please refer to the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
