# Detail Loss in Super-Resolution Models Based on the Laplacian Pyramid and Repeated Upscaling-Downscaling Structure

- Decision: Reject
- Scores: 1, 5, 3, 5

## Abstract
With advances in artificial intelligence, image processing has also gained significant interest. Image super-resolution, in particular, is a vital technology closely related to real-life applications, as it enhances the quality of existing images. Since enhancing details is important in the super-resolution task, it is often necessary to activate pixels that appear only at high frequencies, distinct from low frequencies. 
In this paper, we propose a method that generates a detail image separately from the super-resolution image. This approach introduces a loss function designed to enhance detail, allowing the model to generate an upscaled image and a detail image independently, with control over each component. Consequently, the model can focus more effectively on high-frequency data, resulting in an improved super-resolution image. Our loss function utilizes detail images based on the Laplacian Pyramid, which is widely used in image reconstruction. The multi-level property of the Laplacian Pyramid is well-suited for applying upscaling and downscaling repeatedly.
Our experiments demonstrate that a structure applying the repetition of upscaling and downscaling integrates effectively with our detail loss control. The results show that this structure efficiently extracts diverse information, enabling the generation of improved super-resolution images from multiple low-resolution features. We conduct two types of experiments. First, we construct a simple CNN-based model incorporating the Laplacian Pyramid-based detail control and a repeated upscaling and downscaling structure. This model achieves a state-of-the-art PSNR value of 38.48 dB, surpassing all currently available CNN-based models and even some attention-based models without additional special techniques. Second, we apply our methods to existing attention-based models on a small scale. In all the experiments, attention-based models using our detail loss show improvements compared to the original models. These experiments demonstrate that our detail control loss effectively enhances performance, regardless of the model's structure in the super-resolution task.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces the Laplacian pyramid-based Upscaling and Downscaling Super-Resolution Network (LaUD), a CNN-based model designed for super-resolution tasks. The proposed LaUD uses a repeated upscaling and downscaling process (RUDP), which repeats downsampling the completed SR feature map and combining it with the LR image to extract new upsampled approximation and detail features. The authors also propose a detail control loss based on the Laplacian Pyramid (LP), which is the weighted sum of the loss $L_s$ for the SR image and $L_d$ for the LP detail. The proposed methods can be applied to both CNN-based and attention-based models to enhance the original models' high-frequency information.

### Strengths
- One strength of this paper is the use of Laplacian Pyramid-based detail control, which enhances the diversity of feature maps. The observed differences in feature map diversity between models with and without detail loss, as shown in Figure 2, are particularly interesting and suggest that this approach can contribute positively to capturing finer image details.

- The authors conducted extensive experiments on four different datasets using a variety of CNN-based and attention-based models, which contributes to a comprehensive evaluation of the proposed methods.

### Weaknesses
 - The authors claim that rather than generating $H_{U_k}$ and $H_{D_k}$ in parallel within the upscaling block, producing $H_{D_k}$​​ from $H_{U_k}$ allows the model to capture high-frequency information that may otherwise be missing (L219-L222). However, this claim lacks supporting evidence and appears to be purely conjectural. While Table 2 presents an ablation study of LaUD’s components, the observed improvements in PSNR and SSIM are minimal, and higher values in these metrics do not necessarily indicate effective capture of high-frequency information. The ablation study, specifically, shows that the gains from adding RUDP are marginal, and in some cases, even detrimental to performance, suggesting that the benefits of this component are not well-established.
- Some sentences lack clarity. Below are those examples:
   - The phrase "such models" (L257) is unclear since it could refer to either (1) models requiring minor modifications or (2) models requiring significant structural changes. Although it might be inferred from context that "such models" likely refer to models with minor modifications, the phrasing leaves room for misinterpretation. To ensure clarity, the reviewer suggests explicitly specifying which type of model is being referred to in this context. 
   - Another point of ambiguity arises in lines L322-L345, where two models, D-DBPN and HBPN, are compared across different datasets. The text does not indicate which model corresponds to which dataset, making it challenging to interpret the results accurately. To enhance clarity, the reviewer suggests specifying that D-DBPN's performance gain pertains to Set14 and that HBPN's performance gain relates to Urban100. 
   - In Table 5, the term "ours" is ambiguous. It should be presented in a way that is understandable from either the text or the table alone. Although details for each model variation are mentioned in the main text, the table should also explicitly label them to avoid confusion. For instance, each variant could be labeled as "DRLN + Detail loss + RUDP," "HAN + Detail loss," or "ABPN + Detail loss" to make distinctions clear. 
- There is a questionable assertion regarding LaUD's superior performance over D-DBPN and HBPN, which use iterative upsampling and downsampling methods similar to RUDP (L342-L346). This claim does not necessarily validate the effectiveness of LP detail in the loss function. Variations in the upsampling and downsampling methods and differences in the number of parameters between LaUD and D-DBPN (or HBPN) may explain the observed performance differences. Additionally, the analysis lacks sufficient detail on these factors. Furthermore, high PSNR and SSIM scores do not guarantee the effective restoration of high-frequency components.
- The effectiveness of the methods proposed in this paper remains uncertain. In Table 1, LaUD demonstrates only slight improvements over CNN-based models, with PSNR gains of around 0.1 in many cases. Moreover, LaUD consistently lags behind attention-based methods, placing last on the Urban100 dataset for 8x super-resolution. In the ablation study in Table 2, the contribution of each component appears minimal; adding RUDP, as seen in comparisons like No. 1 vs. No. 2 and No. 4 vs. No. 5, even leads to performance declines. This suggests that the proposed method may not be as effective as claimed, and the benefits of RUDP are questionable.
- The paper contains multiple typos and inconsistencies. For instance, "RUDP" is mistakenly written as "RDUP" (L089). There are also issues with indefinite article usage, such as "an detail" instead of "a detail" (L240). Additionally, sentence capitalization is inconsistent; for example, it should be "The PSNR" instead of "the PSNR" (L330). Furthermore, there is an explanation provided for "Table 5" (L486), but no Table 5 exists in the paper—it appears they meant to refer to Table 3.

### Questions
- The paper describes that the generated $H_{Down_k}$ ​​ is concatenated with the input LR image $I_{LR}$ and the LR feature $H_{Down_{k-1}}$ (L229-L230). However, based on Figure 1, it appears that the output of the 1st Down-scale block concatenates with $I_{LR}$​, while the output of the 2nd Down-scale block concatenates with $H_{Down_{k-1}}$​​. It may be more accurate to state $I_{LR}$​ or $H_{Down_{k-1}}$ instead of $I_{LR}$​ and $H_{Down_{k-1}}$​​. Can the authors confirm if this interpretation is correct?
- The authors state that significant structural changes to the proposed RUDP are necessary in some cases to apply the LP-based detail loss to attention-based models (L255-256). If such changes hinder the effectiveness of the detail loss, it suggests that there may be substantial limitations in applying the proposed loss function to other models. The reviewer would appreciate the authors' perspective on this issue.
- In Figure 3 and Figure 11, comparisons are made only with DBPN, DRLN, and SwinFIR. Could the authors clarify why these specific methods were chosen? Would it be possible to include comparisons with all the methods shown in Table 1? Furthermore, since the improvements in Table 1 are marginal and, in some cases, fall short compared to other methods, showing only selective image crops may give the impression of focusing on favorable regions. Could the authors consider presenting all the images before and after zooming in on specific areas to provide a more complete perspective?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new image super-resolution technique that can independently generate super-resolution images and detail images. This method improves image quality by independently generating super-resolution images and detail images. This technology uses a loss function based on the Laplacian pyramid to optimize high-frequency details and improve the quality of super-resolution images. The loss function is constructed based on the Laplacian pyramid, which is suitable for cyclic upsampling and downsampling operations.

### Strengths
1. The proposed Laplacian pyramid (LP) detail control loss method enables the model to independently process high-frequency information in detail images, thereby focusing more on the details and supplementing missing information in upsampled images.

2. This paper validates the effective combination of RDUP (repeated upsampling and downsampling) and LP based detail control. The experiment shows that RDUP can capture more diverse information by re-extracting detail information from SR features.

### Weaknesses
1. The parameters related to the method in the paper should be marked in Figure 1 for the convenience of readers to read.
2. The comparison between the formula and the architecture diagram in Figure 1 is not rigorous, for example, Hn=Hn-1+Resn (Hn-1), n=1,2.., N. Please modify the diagram or formula. In addition, it is necessary to add a serial number after the formula to facilitate readers' reading.
3. The author's modeling approach using selective generation is similar to many early methods, with comparable effectiveness: DRRN and NAFNet, especially NAFNet achieved SOTA results in 2022 with extremely low parameter count. However, the author did not compare this type of algorithm. Please add comparative experiments with this type of algorithm to verify the superiority of the proposed iterative method.
4. The paper introduces the Laplacian pyramid method as a loss to enhance the details of super-resolution images. However, there are too few relevant descriptions in the results images and loss functions sections. Please supplement the process and formula for obtaining images as labels. Although the author shows the process of the Laplacian pyramid in the supplementary materials and mentions the use of supervised learning for learning, this is not consistent with the detail maps shown in the subjective comparison results. Please display the detail labels used in the supervisor comparison results.
5. This article uses a simple CNN network with detail loss to achieve more competitive results. Theoretically, this simple network is also more competitive in terms of parameters, computational complexity, and running time. Please include a comparison of parameters, computational complexity, and running time in the comparison results.
6. This article proposes the RUDP module for restoring detailed information on images. Is there any theoretical basis for the proposed LaUD using RUDP twice? Can using it more times achieve better results? Please demonstrate in the ablation experiment.

### Questions
Please see the Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors proposed a novel detail loss based on the Laplacian Pyramid (LP)  and a Repeated upsampling and downsampling process for the SR task. The authors prove that this  LP- based detail loss can be used with CNN models and transformers, as it is independent of the model’s architecture.

### Strengths
The authors applied their methods to both CNN-based and attention-based models and  as a result, all the models perform effectively, demonstrating that our methods successfully supplement high-frequency information, regardless of the model’s structure.

### Weaknesses
1. Though, the authors show different experiments to prove the efficacy of their approach, but the contributions of the work are too limited for acceptance.
2. What is the exact difference between the upscaled and detail feature shown in fig. 1a. How can the authors prove that they are actually learning different meaningful information, and not increasing redundancy. The authors can show feature Map visualisations.
3. How does the author finalise the number of levels (3) in their designed model. The authors should have included an ablation study for them.
4. Regarding presentation:
The authors should try to avoid the excess use of abbreviations. While starting a new section they should give full forms. RUDP or RDUP, the overall presentation is not good of the paper.
5. The efficacy of Laplcian Pyramid in the field of SR was already explored in the popular work,"Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution". The authors should have framed their work on this approach and try to compare and prove how their approach was better than this. 
6. As loss function is their main contribution, the authors should try to compare their approach with other loss functions commonly use din SR.

### Questions
Please check the weakness section.

### Soundness
2

### Presentation
2

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
This paper proposes a super-resolution model using a novel detail control loss based on the Laplacian Pyramid and a repeated upscaling and downscaling process to enhance high-frequency details in images. The authors demonstrate their approach by implementing a new CNN-based model, LaUD, which achieves competitive performance metrics and is tested on multiple datasets. Furthermore, they apply the LP-based detail loss to attention-based SR models and report minor improvements. The experiments show promising quantitative results, indicating that the proposed techniques can be applied across various SR models.

### Strengths
1. Introducing LP-based detail control loss is a notable idea that targets high-frequency information, which is essential for image super-resolution.

2. The proposed method is tested on both CNN and attention-based models, showcasing its adaptability to different architectures.

### Weaknesses
1. In the quantitative comparison with SOTA methods, the proposed LaUD model does not consistently demonstrate a clear advantage. While the model performs competitively, the improvements in PSNR and SSIM are modest, particularly when compared to established models. For instance, in the 8× upscaling scenario on Urban100, LaUD’s performance lags behind that of several attention-based models. This raises questions about the practical benefits of adopting LaUD over simpler or more established models, especially given the additional complexity introduced by the LP-based detail control and RUDP.

2. While the ablation study shows that RUDP and LP-based detail control positively impact the performance, it lacks a thorough exploration across different datasets and SR scales. More diverse conditions could substantiate the robustness of these components. The authors do not investigate the trade-offs introduced by adding the detail control loss in terms of computational cost, memory usage, or training time, which would be valuable for a practical assessment of its viability.

3. Although the quantitative results are presented, the difference in metrics between LaUD and SOTA models is small, which may not justify the complexity of adding both LP-based detail control and RUDP. The qualitative analysis of feature maps is difficult to interpret in terms of real-world impact. The authors could provide further explanation or visualization to clarify how these enhanced high-frequency details manifest in output quality.

4. Certain aspects of the methodology, particularly in adapting LP-based detail loss to attention models, lack clarity. Specific details about modifications required for each model, especially regarding architectural changes, are crucial for reproducibility but are only briefly addressed, with many descriptions deferred to the appendix.

### Questions
1. Could you provide a comparison of model size, memory usage, and inference time between LaUD and the other state-of-the-art models?

2. Could you provide more experimental data in the ablation section to show a comparison of the proposed method’s impact on the three base models (ABPN, HAN, and DRLN)?

### Soundness
2

### Presentation
2

### Contribution
2
