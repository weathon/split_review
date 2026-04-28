# Frequency-Guided Masking for Enhanced Vision Self-Supervised Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We present a novel \emph{frequency-based} Self-Supervised Learning (SSL) approach that significantly enhances its efficacy for pre-training. Prior work in this direction masks out pre-defined frequencies in the input image and employs a reconstruction loss to pre-train the model. While achieving promising results, such an implementation has two fundamental limitations as identified in our paper. First, using pre-defined frequencies overlooks the variability of image frequency responses. Second, pre-trained with frequency-filtered images, the resulting model needs relatively more data to adapt to naturally looking images during fine-tuning. 
To address these drawbacks, we propose \textbf{FO}urier transform compression with se\textbf{L}f-\textbf{K}nowledge distillation (\textbf{FOLK}), integrating two dedicated ideas. 
First, inspired by image compression, we adaptively select the masked-out frequencies based on image frequency responses, creating more suitable SSL tasks for pre-training. Second, we employ a two-branch framework empowered by knowledge distillation, enabling the model to take both the filtered and original images as input, largely reducing the burden of downstream tasks. Our experimental results demonstrate the effectiveness of \textbf{FOLK} in achieving competitive performance to many state-of-the-art SSL methods across various downstream tasks, including image classification, few-shot learning, and semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a frequency-based SSL method to learn visual representations from unlabeled images, which significantly improves the training performance compared with existing works. In particular, the authors built upon the MFM method and identified two key limitations: 1) pre-defined frequency masking filters that ignore the intrinsic structure in individual images; 2) model pre-trained with frequency-filtered images leads more data to adapt to natural images in downstream model fine-tuning. In response, two specific new designs (a. masked frequency modeling with Com and RCom filters; b. multi-task self-supervision with self-knowledge distillation) are proposed to target these two problems. Their reported experimental studies have shown the effectiveness of their designs.

### Strengths
**Originality**. The paper investigated two fundamental limitations in the MFM work and proposed two novel designs to address these limitations.  The presentation clearly shows what are the novel elements.

**Quality**.  The paper shows a successful way to perform masking in the frequency domain for unlabeled training images. Additionally, the authors provided a proper self-knowledge distillation framework to deal with the negative effect of training with frequency-masked images.

**Clarity**.  The submission neatly shows all the experiments that were carried out and the description of the underlying method is clear.

**Significance and Relevance**.  The topic is very interesting and important. Considering the growing demand for learning effective representations from unlabeled data, this paper pushed the boundary of SSL.

### Weaknesses
 **Training Cost**. Given that the proposed method employs a two-branch framework for model training, it is unclear what the exact computational overhead is compared to the original MFM. The paper should provide a detailed breakdown of the computational cost, including FLOPs, memory usage, and training time per epoch, to allow for a fair comparison with MFM and other existing methods. Furthermore, it is important to understand how this cost scales with larger batch sizes and image resolutions. 

**Masking Filters**.  The paper lacks precise formulations for the Com and RCom masking filters. While the conceptual design is discussed, the absence of explicit equations or pseudocode makes it difficult to understand the exact implementation and to reproduce the results. The paper should provide the mathematical equations or a detailed pseudocode for constructing these filters, including any parameters involved and how they are determined. For example, how are the center frequencies and bandwidths of these filters chosen, and how do these parameters affect the masking performance?

**Data Augmentations**. In generating two views, u and v, distinct transformations (random cropping, color jittering, etc.) are conducted. The paper does not provide any analysis of how these specific augmentations impact the frequency masking process and the final model training. It is crucial to understand whether the choice of augmentations affects the frequency content of the images and, consequently, the effectiveness of the proposed masking strategy. Ablation studies should be included to analyze the effect of different augmentation combinations on the model's performance.

### Questions
See above weaknesses.

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
3

### Summary
This paper introduces Fourier transform compression with self-knowledge distillation (FOLK), a frequency-based self-supervised learning (SSL) method designed to improve pre-training efficiency. FOLK addresses the limitations by adaptively selecting masked frequencies based on image frequency responses and employing a two-branch framework for knowledge distillation. Experimental results show that FOLK achieves competitive performance across various SSL tasks.

### Strengths
1. The framework is applicable and straightforward to understand.
2. The proposed method improves the learning of the student model and facilitates a more efficient training process.
3. The paper presents experiments across multiple datasets and various vision tasks, demonstrating the effectiveness of the proposed method.

### Weaknesses
1. The dual-stream and frequency-domain masking approaches applied in the article are relatively common schemes. Could the authors elaborate further on the motivation of the proposed method? Specifically, the novelty of combining these two common approaches is not clear. The paper should clarify how the specific combination of dual-stream processing with adaptive frequency masking leads to a unique and significant improvement over existing methods, rather than simply being a combination of known techniques.
2. More analysis and experiments are required on the framework design and cost computation, please see the questions. The paper lacks a detailed analysis of the computational overhead introduced by the adaptive frequency masking and the dual-stream architecture. It is unclear how the computational cost of FOLK compares to other self-supervised learning methods, especially considering the additional forward pass required for the teacher network. Furthermore, the paper should provide a more thorough investigation into the sensitivity of the framework to different hyperparameter settings, such as the masking ratio and the choice of adaptive filters.

### Questions
1. Two views (u and v) of the input image are processed through the informed filtering process in the proposed FOLK framework. What is the optimal method for selecting views to enhance the model performance?
2. How can the complexity of the FOLK be reduced to enhance the framework's accessibility? Could you analyze the computational costs of the various methods evaluated across different models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a self-supervised learning (SSL) approach named FOLK, which stands for FOurier transform compression with seLf-Knowledge distillation. The method aims to address the limitations of previous frequency-based pre-training approaches by adaptively selecting frequencies for masking based on unique image responses. The dual-branch framework leverages both filtered and original images during pre-training, which is claimed to minimize the adaptation requirements for natural-looking images in downstream tasks. The experimental results demonstrate the effectiveness of FOLK, showing competitive performance in various downstream tasks such as image classification, few-shot learning, and semantic segmentation.

### Strengths
The paper presents a new method that combines frequency-based masking with self-knowledge distillation, addressing known limitations in the field of SSL for computer vision tasks. The paper provides extensive experimental results that demonstrate FOLK's effectiveness across a range of tasks and benchmarks, showing improvements over existing state-of-the-art methods.

### Weaknesses
The author proposed two limitations in the introduction, but the experiments did not directly discuss how to address these limitations. Simply showing performance improvements (e.g., image classification tasks) is not enough to support the author's claims.

 The paper primarily focuses on the Com and RCom filters. It would be beneficial to see a comparison with other filtering techniques to establish the robustness and generalizability of the FOLK framework. 

The related work section mentions that MFM has been applied to low-level vision tasks. Since FOLK builds upon MFM, it would be valuable to include a comparison of FOLK's performance on such tasks. 

While the supplementary material shows some results on robustness, a more detailed analysis would be appreciated. It is not sufficiently effective to only show the impact on loss values with a few simple degradations. The paper lacks a comprehensive robustness evaluation, particularly concerning adversarial attacks, common corruptions, and out-of-distribution scenarios. 

The paper integrates knowledge distillation into the FOLK framework, but ablation studies regarding the contribution of this component are missing. It is not clear how much the knowledge distillation component contributes to the overall performance, and the paper does not provide sufficient evidence to support its significance.

### Questions
1. The paper primarily focuses on the Com and RCom filters. It would be beneficial to see a comparison with other filtering techniques to establish the robustness and generalizability of the FOLK framework. Could the authors experiment with additional filtering methods, such as Gabor filters or wavelet transforms, and report on their effectiveness?
2. The related work section mentions that MFM has been applied to low-level vision tasks. Since FOLK builds upon MFM, it would be valuable to include a comparison of FOLK's performance on such tasks. Could the authors add experiments that benchmark FOLK against existing methods on low-level vision tasks to provide a more comprehensive evaluation?
3. While the supplementary material shows some results on robustness, a more detailed analysis would be appreciated. Could the authors provide additional benchmarks that specifically measure the robustness of the FOLK framework against various types of image degradations and noise?
4. The paper integrates knowledge distillation into the FOLK framework, but ablation studies regarding the contribution of this component are missing. Could the authors conduct ablation studies to isolate the impact of the knowledge distillation component on the overall performance? This would help readers understand the significance of this technique in the context of the proposed framework.

### Soundness
3

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
The authors identify two fundamental limitations in the existing masked frequency modeling (MFM) paradigm: 1) constant filters overlook the variability of image frequency responses, and 2) no access to naturally looking images during pre-training requires more data to adapt to downstream tasks during fine-tuning. To address 1), the authors adaptively select the masked-out frequencies based on image frequency responses. To address 2), the authors employ a student-teacher framework via self-distillation. Experimental results on image classification, few-shot learning, and semantic segmentation demonstrate the effectiveness of the proposed method compared to the MFM baseline.

### Strengths
-	The proposed method is well motivated. The authors motivate the method by identifying two key limitations in MFM, and propose two interesting solutions to address these drawbacks.
-	The paper is generally well-written and easy to follow.
-	The authors provide a comprehensive analysis based on their method. The experiments are extensive and the results are promising, especially for few-shot settings.

### Weaknesses
-	The idea of using adaptive filers is interesting. However, the fitters still rely on some pre-defined thresholds, e.g., [0.005, 0.01, 0.05]. In practice, the authors may also need to tune these hyper-parameters to achieve the optimal performance for different datasets. The selection of these thresholds seems somewhat arbitrary, and the paper lacks a clear methodology for determining these values based on the characteristics of the input data. This could limit the generalizability of the approach, as the optimal thresholds might vary significantly across different image datasets with varying frequency distributions.
-	For CNN, according to Table 4 in Sec. B.2, the proposed method does not lead to further gains compared with MFM when it comes to full fine-tuning, which makes me concerned about its effectiveness for CNN architectures. Could the authors provide the justification on this? The lack of improvement in full fine-tuning scenarios for CNNs raises questions about the method's ability to capture and leverage the specific inductive biases inherent in convolutional architectures, especially when compared to the transformer models where the gains are more pronounced. It would be beneficial to understand why the adaptive frequency masking does not translate to better performance in CNNs, as this could indicate a limitation in the method's applicability.
-	For efficiency analysis, the authors only provide a comparison on GPU memory usage (Table 12, Sec. B.6). A comparison on training time with previous methods is also preferred. The absence of a training time comparison makes it difficult to assess the practical overhead of the proposed method. While memory usage is an important factor, training time is equally crucial for evaluating the feasibility of using the method in real-world scenarios. A detailed analysis of the computational cost, including the time required for adaptive filter selection and the overall training process, is necessary to fully understand the method's efficiency.

### Questions
See the questions mentioned above. Overall, I think it is an interesting paper with extensive experiments and analysis, which could provide some new insights for the community. Thus, I am leaning to accept this paper.

### Soundness
3

### Presentation
3

### Contribution
3
