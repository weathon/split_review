# VideoShield: Regulating Diffusion-based Video Generation Models via Watermarking

- Decision: Accept
- Avg Score: 5.83
- Scores: 5, 6, 3, 8, 5, 8

## Abstract
Artificial Intelligence Generated Content (AIGC) has advanced significantly, particularly with the development of video generation models such as text-to-video (T2V) models and image-to-video (I2V) models. However, like other AIGC types, video generation requires robust content control. A common approach is to embed watermarks, but most research has focused on images, with limited attention given to videos. Traditional methods, which embed watermarks frame-by-frame in a post-processing manner, often degrade video quality. In this paper, we propose VideoShield, a novel watermarking framework specifically designed for popular diffusion-based video generation models. Unlike post-processing methods, VideoShield embeds watermarks directly during video generation, eliminating the need for additional training. To ensure video integrity, we introduce a tamper localization feature that can detect changes both temporally (across frames) and spatially (within individual frames). Our method maps watermark bits to template bits, which are then used to generate watermarked noise during the denoising process. Using DDIM Inversion, we can reverse the video to its original watermarked noise, enabling straightforward watermark extraction. Additionally, template bits allow precise detection for potential spatial and temporal modification. Extensive experiments across various video models (both T2V and I2V models) demonstrate that our method effectively extracts watermarks and detects tamper without compromising video quality. Furthermore, we show that this approach is applicable to image generation models, enabling tamper detection in generated images as well.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the need for the control of integrity and misuse of AI Generated Content. The usual approach is to use watermarks for video domain, but they are underdeveloped and have a post-processing manner, which results in video quality degradation. The authors propose a novel way of watermarking images while generating it (VideoShield). Their method is training-free and works with diffusion-based video models. Authors extract the watermark from the images using DDIM Inversion.

### Strengths
1) The proposed method does not require additional training, which could simplify integration with existing diffusion models.
2) The framework’s ability to detect tampering both within frames and across the sequence

### Weaknesses
1) Notation T_temp for a threshold in tampering is a bit confusing, considering T_p is a tensor.
2) No introduction for chacha20
3) No formula for calculating video quality is given 
4) Figure 2 provides only abbreviations in the legend
5) Over all paper, formulas and tables seem to have decreased font. Moreover, some tables overlap the text (e.g. Table1). This may be a reason for a possible desk rejection.

### Questions
1) Results from Table 1 shows that the proposed method is only marginally better than RivaGAN w/o real images conditioning. Did you check RivaGAN with the same setup as the last row? 
2) Why do you compare only to SVD in Table 2? 
3) The authors appeal to decreased visual quality of videos generated with the existing watermarking methods, but did not organise subjective study to show that their method outperforms the others. Video quality metrics are known to have limited capabilities to estimate AIGC. Subjective comparison is required in this work, can you provide one?

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
The paper "VideoShield: Regulating Diffusion-Based Video Generation Models via Watermarking" presents VideoShield, a novel framework for embedding watermarks in diffusion-based video generation models, including both text-to-video (T2V) and image-to-video (I2V) models. The paper addresses the need for content control and authenticity verification in AI-generated video content, focusing on integrating watermarks during the video generation process to prevent quality degradation. Key contributions include In-Generation Watermark Embedding, Tamper Localization for Videos, and Watermark Extraction and Robustness.

### Strengths
1. The paper introduces an innovative approach to watermarking in diffusion-based video generation models by embedding watermarks during the generation process, which diverges from traditional post-processing methods. Compared to image watermarking, this is a less explored field. The originality of embedding watermarks during the generation process, as well as the novel dual tampering localization, is a meaningful supplement to this field.
2. The technical methods are rigorous and fully described. This paper uses DDIM inversion to provide a solid foundation for watermark embedding and extraction without affecting video quality. The extensive experimental evaluation of multiple T2V and I2V models strongly demonstrates this method's robustness, flexibility, and effectiveness. The author's detailed analysis of different watermark extraction and localization scenarios further strengthens the contribution of this article to this field.
3. This paper is well-organized and provides a clear understanding of motivation, methods, and experimental setup.
4. VideoShield's training-free and high-fidelity watermarking method provides a reliable and efficient solution for generating watermarks in video models. This paper addresses a highly relevant issue - ensuring the integrity of content in videos generated by artificial intelligence.

### Weaknesses
1. Although this article introduces relevant watermarking and tampering localization methods, there is no comparative analysis with other video generation or post-processing watermarking methods. For example, including baselines for time tampering localization or using alternative methods to evaluate the robustness of specific types of distortions. The lack of comparison with existing video watermarking techniques, especially those that operate in the post-processing domain, makes it difficult to assess the true novelty and advantage of the proposed in-generation approach. Specifically, a comparison against methods that apply watermarks to individual frames and then evaluate temporal consistency would be beneficial. Furthermore, the evaluation of robustness could be strengthened by including a wider range of distortion types and parameters, such as varying levels of compression artifacts or different types of noise.
2. VideoShield is positioned as a non-training and efficient framework, but this paper lacks specific comparisons with baselines regarding time/computational complexity, such as runtime. The absence of a detailed computational analysis, particularly concerning the runtime overhead introduced by the DDIM inversion process, makes it challenging to evaluate the practical efficiency of VideoShield. A comparison of the runtime for watermark embedding and extraction, as well as tamper localization, against baseline methods would be essential to validate the claim of efficiency. This should include a breakdown of the computational cost for each stage of the pipeline, such as DDIM inversion, watermark embedding, and localization.
3. Although these experiments covered various distortions, they did not explore broader real-world attack scenarios, including testing with denser video compression techniques, color distortion, or frame rate changes, which could further validate the robustness of VideoShield in various real-world environments. In addition, analyzing the performance of VideoShield under adversarial conditions where attackers actively attempt to bypass watermarks could be an interesting solution. The evaluation should consider more aggressive forms of video compression, such as H.265/HEVC, and explore the impact of frame rate variations, which are common in real-world scenarios. Furthermore, the robustness analysis should be extended to include adversarial attacks that are specifically designed to remove or disrupt the embedded watermarks. This would provide a more comprehensive understanding of the security of the proposed method.
4. The author can further discuss the limitations by listing the performance of VideoShield under different video quality and generation settings. This method seems to perform better on higher-quality video output, but further discussion on factors that may affect watermark integrity, such as video resolution or content complexity, will further demonstrate the effectiveness boundary of VideoShield. The analysis should include a detailed investigation of how video resolution and content complexity affect the watermark embedding and extraction process. For example, it would be beneficial to evaluate the performance of VideoShield on videos with varying resolutions and different levels of detail, such as those with complex motion or intricate textures. This would help to identify the limitations of the method and its applicability to different types of video content.
5. This article briefly introduces the adaptability of image watermarking, but can VideoShield adapt to image tampering localization scenarios?

### Questions
1. Can the author provide more comparative details on how VideoShield compares to other watermarking frameworks or post-processing methods in terms of tamper localization accuracy and robustness?
2. Can the author share the computational performance of VideoShield, especially regarding the running time of different video resolutions or models?
3. Will the author consider testing the robustness of VideoShield under other types of distortion, such as extreme video compression, frame rate variations, or color adjustments? These additional distortions are common in real-world applications and can enhance confidence in VideoShield's resilience.
4. The results indicate that VideoShield has a certain dependence on video quality. Does the performance of VideoShield still vary due to resolution or model complexity? If so, can the author provide more insights or data on these factors?
5. Can VideoShield adapt to image tampering localization?
6. Is the watermark capacity of 6 512 bits suitable for all video resolutions, or is the number of bits that can be embedded flexible based on the characteristics of the video?
7. Placing visual content in the main text seems better.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces VIDEOSHIELD, a novel watermarking framework for diffusion-based video generation models. By embedding the watermark directly during the generation process, VIDEOSHIELD eliminates the need for additional training, providing a cost-effective solution for safeguarding generated videos. Additionally, the model includes a proactive tamper detection mechanism. Using template bits derived from the watermark, the authors enable both temporal and spatial localization of tampering within the video.

### Strengths
- This paper is well-written.
- This paper proposes a novel scheme for proactive video forensics.

### Weaknesses
1.	The proposed model may not entirely align with watermarking application scenarios. In its context, verification requires the recipient to compare the watermarked video against the original video's bit template. This requires the verifier to either have access to the original video to generate the bit template using the same encryption method, or to obtain the bit template directly from the video creator. Such requirements differ from standard watermark extraction practices, where verifiers typically can extract watermark information without needing the original video. This reliance on the original video or a pre-shared template severely limits the practicality of the approach in real-world scenarios where such access is not guaranteed.

2.	The model uses the CHACHA20 stream cipher to generate template bits, requiring the algorithm to use the same key with different nonces for each encryption. Does this mean that a unique random number needs to be set for each video? If so, how does the method handle the storage of a large number of video-to-key mappings? Additionally, it’s unclear whether the primary goal of this approach is to protect the model itself or the generated videos. The use of a stream cipher with nonces raises concerns about key management and scalability, especially if a unique key or nonce is required for each video generated. The paper should clarify how this is managed and the implications for practical deployment.

3.	The proposed method uses watermarking for proactive tamper detection; however, the baseline experiments in the paper compare it primarily with passive detection methods (e.g., MVSS-Net, HiFi-Net), which may not be entirely appropriate. It would be more suitable to compare the approach with other active tamper detection methods. Below are references to such methods for consideration:
[1] Zhang X, Li R, Yu J, et al. Editguard: Versatile image watermarking for tamper localization and copyright protection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 11964-11974.
[2] Zhou Y, Ying Q, Wang Y, et al. Robust watermarking for video forgery detection with improved imperceptibility and robustness[C]//2022 IEEE 24th International Workshop on Multimedia Signal Processing (MMSP). IEEE, 2022: 1-6.

4.	There are formatting issues: the bottom line of Table 1 overlaps with the text below, and the font size in Table 3 is too small, making it difficult for readers to follow.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a VideoShield, which embeds watermarks directly during video generation. It maps watermark bits to template bits, which are then used to generate watermarked noise during the denoising process. Template bits allow precise detection for potential spatial and temporal modification. Extensive experiments demonstrate its effectiveness.

### Strengths
The topic is interesting. Using DDIM Inversion, the video can be reversed to its original watermarked noise. The paper is written and organized well. Experiments are plenty and convincing. The ablation study verified the contribution of each design towards the whole framework.

### Weaknesses
No obvious drawbacks are found. However, typesetting needs to be improved, such as keeping the same or similar text size of the table as the text, no overlapping between table and text.

### Questions
The framework looks heavy, how about the computational overload? 
The relationship with "Gaussian Shading" needs to be further clarified.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The watermark can actively identify generated content and is currently the primary method used for detection and attribution in diffusion models. However, there has been no watermarking method specifically addressing video generation models based on diffusion models. This paper proposes VIDEOSHIELD to fill this research gap. VIDEOSHIELD introduces a Gaussian Shading watermark embedding method that does not require additional training. In addition to its basic watermarking functionality, VIDEOSHIELD also acts as a fragile watermark, enabling both temporal (across frames) and spatial (within individual frames) tampering localization. Furthermore, it introduces Hierarchical Spatial-Temporal Refinement to enhance accuracy. Experimental results demonstrate that VIDEOSHIELD performs effectively on both T2V and I2V diffusion models.

### Strengths
1. This paper introduces a Gaussian Shading watermark embedding method that does not require training, thereby avoiding additional computational overhead.
2. Unlike previous methods that focus solely on spatial tampering localization, VIDEOSHIELD takes into account both temporal and spatial tampering localization during the tampering detection process. The paper introduces Hierarchical Spatial-Temporal Refinement, which enables the generation of more detailed masks for tampering localization, significantly improving the accuracy of the detection.

### Weaknesses
1. The innovation presented in this paper is moderate. It extends Gaussian Shading from images to videos and further explores its potential as a fragile watermark. The core idea of applying Gaussian Shading to video, while not entirely trivial, lacks significant novelty. The extension to temporal tampering detection, while useful, does not represent a major conceptual leap. The method essentially applies existing principles to a new domain without introducing fundamentally new techniques or insights into the underlying problem of video watermarking.

2. The presentation of the text has significant issues, particularly in Section 3.4, "TAMPER LOCALIZATION." In this section, the extensive use of symbols due to the inclusion of formulas creates obstacles to understanding the paper's content. The frequent reuse of subscripts p and q makes reading quite difficult; the matrix subscript notation is inconsistent, such as in C_(p(q=M(p))), which is recommended to be changed to C_(p,M(p)). Additionally, the comparison bits matrix Cmp could be written as CMP to standardize with other matrix symbols and to avoid confusion with the subscript p. In line 334, the letter m is used both for the variable and for watermark information, which may lead to confusion. After reviewing the main text, I found that in Supplementary Material A3.1, the authors provide a simple example of the process. I strongly recommend including Figure 7 in the main text to aid reader comprehension. Furthermore, there is some overlap between Table 1 and the Datasets section.

3. In my view, the authors have not addressed an important issue regarding the sequence of watermark attribution and tampering localization. The paper does not demonstrate the accuracy of the watermark after spatial tampering. If we assume that a video undergoes spatial tampering and the tampered areas are detected through localization, but the watermark attribution fails, we cannot conclude that a third party maliciously altered the generated video. This raises the question of whether the watermark has become ineffective in such a scenario. The paper needs to show that the watermark is robust enough to be extracted even after spatial tampering, otherwise the tampering localization is not useful for attribution.

### Questions
Address the weakness, especially the novelty issue.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This article proposes a zero-shot video generation model with active watermarking for video copyright protection and tampering localization.  Based on the DDIM inversion process, the watermark information hidden in the initial Gaussian noise can be detected again from the generation results, and this active watermark is robust against video tampering,  image degradation, and other attacks. Furthermore, for the task of video tampering localization, the authors have designed a detection method that localizes tampering in both temporal (frame position) and spatial  (image information) aspects. Experiments have proven the performance advantages of VideoShield.

### Strengths
- VideoShield leverages the unique properties of active watermarking, innovatively combining the model watermarking task with the tampering localization task, demonstrating significant performance advantages.
- This method requires no training and follows a zero-shot paradigm, making it easy to reproduce and validate its performance.
- This method is based on the properties of diffusion and Gaussian distribution, allowing it to be generalized to other diffusion-based models, such as text-to-image models, exhibiting good generalization capabilities.

### Weaknesses
 - The threshold and hyperparameter settings in the method section are mostly the result of manual searches. The authors may consider exploring how these thresholds could be adaptively searched in the future.


### Questions
- In Table 1 and other tables, the metric "Video quality" is mentioned. How is it specifically calculated? The authors mentioned it is the average of a series of metrics; if possible, could you provide the specific values for each metric?
- Currently, the VideoShield method can hide 512 bits. What is the upper limit for watermark capacity?

### Soundness
3

### Presentation
3

### Contribution
4
