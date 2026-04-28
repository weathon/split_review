# DGQ: Distribution-Aware Group Quantization for Text-to-Image Diffusion Models

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 6, 6, 8

## Abstract
Despite the widespread use of text-to-image diffusion models across various tasks, their computational and memory demands limit practical applications. 
To mitigate this issue, quantization of diffusion models has been explored. It reduces memory usage and computational costs by compressing weights and activations into lower-bit formats. 
However, existing methods often struggle to preserve both image quality and text-image alignment, particularly in lower-bit($<$ 8bits) quantization.
In this paper, we analyze the challenges associated with quantizing text-to-image diffusion models from a distributional perspective. Our analysis reveals that activation outliers play a crucial role in determining image quality. 
Additionally, we identify distinctive patterns in cross-attention scores, which significantly affects text-image alignment.
To address these challenges, we propose Distribution-aware Group Quantization (DGQ), a method that identifies and adaptively handles pixel-wise and channel-wise outliers to preserve image quality. Furthermore, DGQ applies prompt-specific logarithmic quantization scales to maintain text-image alignment. 
Our method demonstrates remarkable performance on datasets such as MS-COCO and PartiPrompts. We are the first to successfully achieve low-bit quantization of text-to-image diffusion models without requiring additional fine-tuning of weight quantization parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenges of quantizing text-to-image diffusion models, which suffer from high memory and computational costs. The authors propose a method called Distribution-aware Group Quantization (DGQ), which handles activation outliers and applies prompt-specific quantization scales to preserve image quality and text-image alignment.

### Strengths
1. The writing is clear and easy to understand.

2. The experiments are thorough, and the analysis of outliers value offers valuable insights.

### Weaknesses
1. The evaluation of inference performance is lacking.

2. In line 417, it states, “we set all attention score quantizer bits to match the activation bits.” Could this direct approach negatively impact performance? What is the FLOP cost of setting the attention score quantizer bits to 16?

3. As shown in Figure A.3, there is still a significant performance drop when activation quantization bits are below 8.

### Questions
Refering to Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper deeply explores the unique distribution patterns of activations and cross-attention scores in text-to-image diffusion models. Based on the analysis of patterns, the authors propose a method called Distribution-aware Group Quantization, which is composed of outlier-preserving group quantization for activations and a new quantizer for cross-attention scores. Experimental results show that the proposed method outperforms the state-of-the-art methods and achieves under 8-bit quantization for the first time.

### Strengths
1. This paper is well organized and the writing is good.
2. The in-depth analysis of the activation and cross-attention in the text-to-image diffusion models is interesting and may benefit the community.
3. The experiments are extensive and solid, showing the effectiveness of the proposed approach. The improvement is significant.
4. The idea is reasonable and easy to follow.

### Weaknesses
1. Typos from line.326 to line.327: these lines contain repeated sentences.
2. The number of generated samples to compute FID and IS is not provided from line.403 to line.410.
3. The baseline model SD 1.4 may be out-of-date now. It would be better if results on more advanced models like SDXL were provided.

### Questions
Please refer to the weakness part.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Distribution-aware Group Quantization (DGQ), which identifies and adaptively manages pixel-wise and channel-wise outliers to preserve image quality. Additionally, a prompt-specific logarithmic quantization strategy is introduced to enhance text-image alignment. Experiments conducted on the MS-COCO dataset demonstrate the effectiveness of DGQ.

### Strengths
This paper exhibits several strengths:

1. The analysis of key characteristics necessary for maintaining model performance during the quantization process is scientific and persuasive.

2. The proposed group-wise quantization strategy, based on the distribution of activations, is both promising and innovative.

### Weaknesses
This paper exhibits several Weaknesses:

1.	The figures are confusing and difficult to understand.

     a)   How are issues like "drops outlier," "high quantization error," and "high overhead" reflected in Fig. 3? What specific phenomenon indicates "drops outlier"?

    b)    What does the horizontal axis in Fig. 4(b) represent? In channel-wise boxplot, why is the horizontal axis range of case1 from 0 to 900, while for case 2 it ranges from 1100 to 1190? What do "specific pixel" and "specific channel" refer to?

2.	The distinctions between group-wise quantization, layer-wise quantization, and channel-wise quantization are somewhat abstract and challenging to grasp. It would be beneficial for the authors to include a figure that illustrates the differences in their principles.

3.	There is a lack of qualitative and quantitative comparisons with the latest research, such as MixDQ[1].

4.	The base model used is outdated and singular. It is recommended to include experiments with more recent Text-to-Image models (e.g., SDXL, PixArt, SD3, or Flux) to validate the generalization of DGQ.

### Questions
1.	How can the quantized model in Table 2 outperform the original model? What mechanisms allow the quantization process to enhance performance?

2.	The meaning of W8A8 should be explained upon its first mention. The article lacks clarity on the notation WXAX, and similarly, the meaning of WXAXGX in the supplementary materials is not explained.

3.	It is recommended to add brackets around the feature indices in Formula 9 for improved clarity, such as A_{[:,0]} V_{[0,:]}.

4.	Why does reducing the bits of activation result in significant performance loss?

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
4

### Summary
The paper proposes a novel quantization method for diffusion models, named DGQ, which efficient reduce memory usage and computational costs compared to existing methods without additional finetuning. This approach aims to achieve high-quality generation while maintaining performance metrics. Experiments are conducted on MS-COCO and PartiPrompts using IS, FID and CLIP evaluation metrics.

### Strengths
1.It is interesting that the author finds activation outliers play a crucial role in determining image quality.
2.It is interesting that maintain text-image alignment in quantizing text-to-image diffusion models without requiring additional fine-tuning of weight quantization parameters
3.The logic of the work is clear, and the exploratory part of the experiments is rich in content

### Weaknesses
1.The conclusions in Figure 5(b) should provide statistical results.
2.This work presents several new matrix computations, including $D_d$. However, the authors fail to address the extra time overhead that these computations may incur.
3.In Table 2, the proposed method with groups set to 16 underperforms compared to groups set to 8 on some metrics (e.g., IS and FID). It would be beneficial to analyze the reasons behind this occurrence.

### Questions
Does excluding the <start> token mean dropping and zeroing it? Why does the author think that the peak near the value of 1 on the far right of Figure 5(a) corresponds to the <start> token, while other regions do not?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an analysis of feature distributions within layers and cross-attention scores in text-to-image (T2I) diffusion models. Building on these analysis, the authors introduce Distribution-aware Group Quantization (DGQ), a method specifically designed to address the distinct distribution patterns in T2I diffusion models. The proposed approach is validated across multiple datasets, demonstrating its effectiveness.

### Strengths
- The paper's motivation is clear and straightforward.

- The authors effectively identify and address outlier issues present in prior methods, providing a targeted method.

- The analysis of attention scores for <start> tokens is convincing, and the proposed method appears to address these challenges well.

### Weaknesses
 - The authors validate the proposed method only on SDv1.4. These limited experiments restrict the ability to assess the generality of their approach. Additional analyses and experiments on other publicly available checkpoints (e.g., SD v2+, EDM, Imagen, etc) would strengthen the evaluation.

- Lines 127-129: "To the best of our knowledge, we are the first to achieve low-bit quantization (< 8-bit) on text-to-image diffusion models." However, [A] has previously proposed low-bit quantization for T2I diffusion models. While [A] and the submitted paper are concurrent works, a discussion of recent works would need for the future work.

- While the analysis and proposed method have novel elements, the approach relies heavily on existing methods (Group Quantization, logarithmic quantization). This reliance may worsen the novelty of the method in contrast to the insightful analysis.

### Questions
The major concerns are in the weakness section, therefore I currently feel that this paper is borderline.
I have some other questions in below:

- The authors analyze the <start> token's attention score distribution; however, I am curious about the distributions for other special tokens such as <end> or <pad> tokens and a comparison discussion with <start> would find meaningful insight within the T2I diffusion model.

- As I understand it, the proposed method (Attention-aware quantization) applies full precision to the <start> token while quantizing other components to lower precision. Consequently, in Table 2, I would expect slight differences in memory req and BOPs compared to the baselines. However, the current paper shows identical values for these metrics. Could you clarify the difference?

- The evaluation includes FID and IS metrics for assessing image qualtiy. I think other image quality assesments (IQA, [A, B]) against full-precision and baseline models would provide practical insights and could enhance the evaluation for the both datasets.

[A] MANIQA: Multi-dimension Attention Network for No-Reference Image Quality Assessment, CVPRW 2022
[B] PromptIQA: Boosting the Performance and Generalization for No-Reference Image Quality Assessment via Prompts, ECCV 2024

### Soundness
3

### Presentation
4

### Contribution
2
