# WinNet:time series forecasting with a window-enhanced period extracting and interacting

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Recently, Transformer-based methods have significantly improved state-of-the-art time series forecasting results, but they suffer from high computational costs and the inability to capture the long and short periodicity of time series. We present a highly accurate and simply structured CNN-based model for long-term time series forecasting tasks, called WinNet, including (i) Inter-Intra Period Encoder (I2PE) to transform 1D sequence into 2D tensor with long and short periodicity according to the predefined periodic window, (ii) Two-Dimensional Period Decomposition (TDPD) to model period-trend and oscillation terms, and (iii) Decomposition Correlation Block (DCB) to leverage the correlations of the period-trend and oscillation terms to support the prediction tasks by CNNs. Results on nine benchmark datasets show that the WinNet can achieve SOTA performance and lower computational complexity over CNN-, MLP-, Transformer-based approaches. The WinNet provides potential for the CNN-based methods in the time series forecasting tasks, with perfect tradeoff between performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a simple 2D-CNN framework for time series forecasting tasks, which mainly utilizes the multiscale periodic bias and achieves good forecasting accuracy with computational efficiency.

### Strengths
The numerical results indicate a strong performance when compared to TimesNet, and even demonstrate a slight advantage or equality when compared to PatchTST.

### Weaknesses
The storyline of this work appears to lack depth and insights. The inter-intra period encoder (I2PE) block, while not identical to the TimesNet architecture, is closely resemble it. Furthermore, I find it challenging to comprehend why the TDPD block and DCB block can be applied identically in both inter- and intra-period signals. My limited understanding is that the intra-period signal is simply the transpose of the inter-period signal, and I'm unsure of how the proposed winNet addresses the parallel implementation of TDPD and DCB in such a scenario. Specifically, if the intra-period signal is a direct transpose, the application of the same convolutional kernels and pooling operations in TDPD and DCB would seem to produce redundant or highly correlated features. This raises concerns about the efficiency and necessity of processing both signals identically. While the CNN model has potential as the author suggests, the novelty and motivation of this work seem weakly supported. A more comprehensive explanation and study of the design would be beneficial.

### Questions
As stated in the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors aim to solve the problems of high computational costs and the missing periodic data capture in forecasting models. To achieve the goal, the authors designed a CNN-based model, WINNET, with one convolutional layer as the backbone. The model includes four parts, Inter-Intra Period Encoder (I2PE), Two-Dimensional Period Decomposition (TDPD), Decomposition Correlation Block (DCB) and Series Decoder. Specifically, I2PE transforms the input 1D sequence into 2D tensor with inter-period and intra-period. TDPD is to obtain the period-trend and oscillation terms. DCB is to study the correlation between the period-trend and oscillation terms. And finally, through Series Decoder, the final prediction results are obtained.
In the experiment, the authors evaluate the performance over the real-world datasets both small and large datasets, comparing to several baselines.

### Strengths
Originality:
In this paper, the backbone of the model is mainly a convolution layer, which greatly reduces the computational complexity and improve the efficiency. It is novel and interesting for simplify model structure for time series forecasting tasks. And this try also shows that simple model framework could also effectively perform time series forecasting tasks.
Quality:
From the perspective of quality, it is high. The authors design a new model and demonstrate its effectiveness through detailed explanations. And the data analysis is thorough, well-executed, and adequately supports the conclusions drawn.
Clarity:
In this paper, the introduction provides a clear overview of the research topic and objectives, and the body sections are logically organized. And the language used in this paper is clear and easy to understand. Besides, some key concepts are well explained.
Significance:
The work in this paper is of great significance. Firstly, WINNET outperforms other forecasting models. And then, WINNET harvests the high computational efficiency for other forecasting models and make full use of the correlation between period trend and oscillation.

### Weaknesses
(1) In figure 1, through I2PE block, you can get inter-period and intra-period features. The inter-period features represent the long-period features and the intra-period features represent the short-period features. However, in figure 1, you wrote that the short-period features are inter-period features, and the long-period features are intra-period features.
(2) In section 3.1, the framework of I2PE is needed.
(3) In section 3.4, the framework of series decoder is needed.
(4) In the experimental part, I noticed that for some data sets, WINNET's performance is not the best, not even the second best. Some explanation is needed.
(5) Please pay attention to typography issues, such as the size of Table 3. Table 4.

### Questions
(1) In section 3.1, you set the number of periodic windows is the same as the periodic window size. What is the reason for this setting?
(2) In the setting of prediction length, the shortest output length is 24. Why not setting the prediction length to the typical prediction length 12?
(3) From figure 4, we can see that in some cases, the performances of other baselines are better than WINNET, which cannot support the conclusion that WINNET outperforms other baselines. Does WINNET outperform only under some certain T settings?

### Soundness
2 fair

### Presentation
2 fair

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
This paper attempts to use the convolutional neural network (CNN) and proposes WinNet for long-term time series forecasting, which is different from most existing works based on Transformer or MLP. Specifically, WinNet first transforms the 1D time series to 2D tensor according to the predefined periodic windows and then performs period-trend and oscillation decomposition. After that, WinNet captures the correlation between period-trend and oscillation terms, based on which convolution and MLP layers are used to get the final prediction. Nine benchmark datasets are used to evaluate the proposed WinNet compared with some baseline methods.

### Strengths
This paper attempts to use the convolutional neural network (CNN) for a better long-term time series prediction, which is still seldomly considered.

### Weaknesses
1. The blocks in the architecture of WinNet are not introduced clearly in Section 3. e.g.,

 -The I2PE block: How to train the MLP; How to calculate the periodic window when using two periods approximately as one period (11/12 or 23/24) in Table 1; why use n = w; Should we do padding for X_1D before performing Equation (1); What is the detailed process of I2PE in Equation (1) (I can guess the details but they should be described clearly)?

 -The TDPD block: what is the meaning of w×w in Equation (2), is it the kernel_size for AvgPool2d; What are the two inputs in "According to the equation 2, the two inputs can be decomposed into the period-trend and oscillation terms"?

 -The DCB block: What is the process of CI (channel independence strategy) in Equation (3)?

 -The Series Decoder block: How to get  X_{i}^{row } and X_{w ·⌈i/w⌉−(w−1)+(i mod w)}^{col} from X_{output}^{CI} by inter-period convolution and intra-period convolution; What are the details of these two kinds of convolutions; What is the meaning of {w ·⌈i/w⌉−(w−1)+(i mod w)}?

 -Figure 1: What is the process of CA.

2. The proposal WinNet does not compare with SoTA methods and the performance improvement is not significant.

 -It is said in the Appendix that some experimental results are taken from the PatchTST and PETformer, but there is no comparison with PETformer. There are also other MLP-based models (RLinear and RMLP), which outperform PatchTST on some datasets and should be compared with.

   Li, Zhe, et al. "Revisiting Long-term Time Series Forecasting: An Investigation on Linear Mapping." arXiv preprint arXiv:2305.10721 (2023).

 -WinNet cannot beat existing models in many cases even based on the results shown in the manuscript.

 -Why the results of the exchange dataset are not given in Table 2?

 -The architectures for the Ablation Studies are not described clearly. In addition, how about the results by using only inter-period or intra-period branch in Figure 1?

 -Which kinds of Time and Memory are considered in Table 6?

3. Some claims are not clear, e.g., it is not clear why "The correlation between period-trend and oscillation terms can provide the local periodicity in time series".

4. The code is not available for reproducibility.

### Questions
Same to the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces WinNet, a CNN-based model tailored for long-term time series forecasting. Traditional Transformer-based approaches, despite their advancements, struggle with computational efficiency and capturing the periodicity of time series data. WinNet seeks to address these issues with its unique architecture:

1. **Inter-Intra Period Encoder (I2PE):** Converts a 1D sequence into a 2D tensor, capturing both long and short periodicities.
2. **Two-Dimensional Period Decomposition (TDPD):** Models period-trend and oscillation terms, emphasizing the significance of periodicity in time series data.
3. **Decomposition Correlation Block (DCB):** Exploits the correlations between period-trend and oscillation terms, enhancing prediction capabilities.

A pivotal concept introduced is the "periodic window," derived as the least common multiple of multiple periods obtained via Fourier Frequency Transformation. This enables the model to represent variations of multiple short periods and organizes the sequence into a 2D tensor, wherein each row signifies a short-period trend and each column stands for the long-period trend.

WinNet's innovations result in a simplified structure with a single convolutional layer at its core, which significantly reduces computational complexity. Moreover, this model outperforms various baselines in both univariate and multivariate prediction tasks across multiple domains, as evidenced by experiments conducted on nine benchmark datasets.

### Strengths
**Strengths:**

1. **Originality:** 
    - *Periodic Window Concept:* The inception of the periodic window, which is ascertained by the least common multiple of various periods using Fourier Frequency Transformation, offers a groundbreaking method to encapsulate the core characteristics of time series data.

2. **Quality:**
    - *Ease of Implementation:* WinNet is notably straightforward to implement, and empirical results demonstrate that it surpasses many other methods in a majority of scenarios.

3. **Efficiency:** 
    - *Optimized Parameters and Complexity:* WinNet has fewer parameters and a reduced computational complexity compared to MLP techniques and other prevailing methods.

4. **Clarity:**
    - *Well-crafted Manuscript:* The paper is articulately penned and provides a seamless reading experience, making it easy for readers to follow and comprehend.

### Weaknesses
**Weaknesses:**

1. **Inconsistent Mathematical Notation:** 
    - The authors' presentation of mathematical symbols lacks consistency, which could lead to confusion. For instance, function names should conventionally be displayed in regular typeface instead of italic (e.g., \( f \) should be \( f \)). Furthermore, vectors and matrices should be represented in bold (e.g., \( x \) should be \( \mathbf{x} \) and \( X \) should be \( \mathbf{X} \)). Consistent and proper notation is crucial for ensuring clarity and preventing potential misunderstandings, especially in a technical paper where precise mathematical expressions are fundamental.

2. **Graphics and Formatting Issues:** 
    - The image quality in Figure 4 is noticeably poor, making it difficult to discern the details. The resolution should be improved to ensure that all elements are clearly visible. Additionally, the authors did not adhere to ICLR's guidelines by combining the appendix and main text. This could hamper structured reading and comprehension, as the appendix is typically reserved for supplementary material that is not essential to the main flow of the paper.

3. **On CNN-based MTS:**
    - Given the inherent characteristics of time series data, it's a general understanding that Transformer-based methods often underperform compared to Linear and CNN approaches in various scenarios. However, one of the advantages of Transformer methods is their ability to capture interrelationships amongst multi-variables. Evaluating CNN-based methods purely on accuracy might not provide a fair comparison. A more comprehensive evaluation should include metrics that assess the model's ability to capture these interrelationships. Moreover, several existing methods leverage CNN for MTS tasks. A comparison of WinNet with such methods, specifically focusing on how they handle inter-variable relationships, would have added depth to the evaluation. The absence of such a comparison makes it difficult to fully assess WinNet's performance in the context of existing CNN-based MTS models.

### Questions
1. **Normalization in MTS:**
    - Normalization plays a pivotal role in predicting MTS. What kind of normalization technique has been employed within the WinNet framework?

2. **Handling Multivariate Time Series in WinNet:**
    - How does WinNet approach and manage the relationships between variables in a multivariate time series (MTS)? A more in-depth discussion on this aspect could enhance the paper's clarity.

3. **Hyperparameter Settings in WinNet:**
    - Could you elaborate on how the hyperparameters for WinNet were determined? Moreover, how do these hyperparameter choices influence the final results? Insights on this could help understand the model's sensitivity and robustness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
