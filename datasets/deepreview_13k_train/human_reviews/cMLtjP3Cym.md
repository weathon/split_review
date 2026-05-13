# TSGGuide: Recommendation Guide for Multivariate Time Series Generation

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Multivariate Time Series Generation (MTSG) plays a crucial role in time series analysis, supporting tasks such as data augmentation and anomaly detection. While several methods exist for MTSG, recommending the most suitable method for new scenarios remains a significant challenge. Although prior work by  (Ang et al., 2023a) provides guidance for selecting MTSG methods, it lacks coverage of recent diffusion-based methods and has limited exploration of channel-independent frameworks. We address these gaps by improving the recommendation guide, highlighting the effectiveness of a central discriminator within the channel-independent framework. Our revised guide makes three key recommendations: 1) VAE-based methods excel on small-scale datasets; 2) a channel-independent framework with the newly designed central discriminator is optimal in most cases; and 3) a diffusion-based method is preferable when ample data and computational resources are available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces TSGGuide, an updated recommendation guide for multivariate time series generation, aimed at refining the selection of generation methods. Through comprehensive analysis, the authors identified limitations in existing frameworks, specifically the limited exploration of channel-independent frameworks and a lack of evaluation for diffusion-based models. By enhancing the central discriminator within the channel-independent framework, incorporating methods such as TimesNet and attention mechanisms, and introducing CCD, the study demonstrates notable performance improvements in small-sample scenarios.

### Strengths
- This work improves upon previous guidelines by prioritizing both channel-independent and diffusion-based generative frameworks, providing users with a more comprehensive and practical TSGGuide for selecting time series generation frameworks.

- By enhancing the central discriminator in the channel-independent framework with advanced techniques (e.g., TimesNet, attention mechanisms, CCD), the study demonstrates clear performance gains in small-sample scenarios, contributing strong methodological advancements.

- The proposed framework shows effective performance in enhancing CCD and CCD-based models, as supported by experimental results.

### Weaknesses
 - **Motivation:** The motivation for this work is not fully justified. The rationale for addressing limitations in channel-independent methods and diffusion models in MTSG for small-sample datasets seems somewhat forced. Small-sample datasets tend to yield low-quality results in diffusion models due to limited information, challenging the model’s ability to learn data distributions. Despite this, the paper shows that CCDGAN’s performance is comparable to that of Diffusion-TS, suggesting a lack of theoretical and empirical support for this motivation.
- **Dataset Limitation:** Although the paper claims TSGGuide is a highly flexible mechanism capable of adapting to diverse tasks, it only evaluates stock, energy, and medical datasets. The limited selection constrains the demonstration of the module’s plug-and-play capability, which may impact the credibility of its claimed flexibility across various domains.
- **Channel-Independent Approach:** The paper’s choice to adopt a channel-independent framework raises questions when applied to stock datasets, which exhibit strong inter-channel correlations (e.g., stocks in the same sector often follow similar trends). While the model demonstrates effectiveness, it may overlook inherent characteristics of financial data by disregarding these correlations.

### Questions
- Given that only stock, energy, and medical datasets were used, how might this affect the generalizability and credibility of TSGGuide’s flexibility across different domains?

- In small-sample contexts, GANs generally outperform diffusion-based models. Yet, as noted in the paper, CCDGAN does not significantly outperform Diffusion-TS. Can the authors provide additional evidence to substantiate their theoretical claims?

- Is CCDGAN essentially a combination of the CCD mechanism with GAN? The methodology section lacks detail here; could you provide more on how CCDGAN was developed?

- Given the emphasis on a channel-independent framework, why are there no comparisons with channel-mixed framework methods? Since channel-independent frameworks ignore inter-sequence interactions, empirical evidence is needed to validate their benefits, especially for financial datasets where sequences are highly correlated.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper provides a recommendation framework for selecting suitable multivariate time series generation (MTSG) methods across various scenarios. It addresses existing gaps in previous frameworks, particularly by incorporating recent diffusion-based methods and enhancing the channel-independent framework using a central discriminator (CCD). The paper conducts extensive experiments on several datasets, including Stock, Energy, and EEG data, which varifies the effectiveness of the proposed model.

### Strengths
S1. The paper is well-organized, and each module is clearly explained.

S2. The CCD introduces frequency-domain transformations and a central discriminator to capture inter-channel dependencies.

### Weaknesses
W1. The technical contribution need to be clarified. The proposed method reshapes time series data and applies a 2D convolutional framework, followed by optimization with a basic GAN architecture. However, this approach lacks novelty and may fall short in capturing the complex inter-channel correlations inherent to multivariate time series. Reshaping the data into a 2D structure and applying 2D convolutions, while common in image processing, does not inherently address the unique temporal dependencies and cross-channel relationships present in multivariate time series. A more comprehensive module that learns correlations directly, perhaps through attention mechanisms or graph-based approaches, to capture correlations and periodicity might be more effective and adaptive. Moreover, The CCD relies on 2D convolutions, a standard technique in time series modeling (such as TCN). The paper does not sufficiently justify what specific innovation CCD brings beyond typical 2D convolutional methods, especially given the potential for information loss when transforming 1D time series into a 2D representation.

W2. The experiments focus on stock, energy, and EEG datasets, which may not sufficiently represent the diversity of real-world MTSG applications. The results would be more convincing if the proposed approach were evaluated on datasets covering additional scenarios of spatial-temporal forecasting (such as OD flow and traffic forecasting), which would better validate the method’s generalizability and effectiveness. The current selection of datasets, while relevant, does not fully explore the method's performance across diverse temporal patterns and inter-channel dependencies that may be present in other domains.

W3. The baselines used for comparison are not up-to-date, with the latest being from 2023. More recent methods like TimeGAE [1] and DLT [2] should be included to conduct sufficient experiment. What’s more, the paper lacks a detailed hyperparameter experiments, such as the weighting factor gamma in Equation 6. The absence of a thorough hyperparameter study makes it difficult to assess the robustness and optimal performance of the proposed method. The choice of gamma, in particular, could significantly impact the model's ability to balance different aspects of the loss function, and a grid search or sensitivity analysis should be included.

W4. The authors do not specify how the datasets are split into training, validation, and test sets in the experiments to ensure the reproducibility of results. This lack of detail regarding data splitting protocols hinders the ability of other researchers to replicate the reported findings and validate the method's performance.

### Questions
Please refer to Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims at providing guidelines to researchers on how to select different Multivariate Time Series Generation models and metrics based on the scenatios that researchers are working on. More specifically, the authors provide their empirical findings across dataset characteristics, computational resources, and metrics. Based on their own findings and motivations on analyzing the perofrmance on small datasets with GAN-based model, the authors further developed CCD, a light-scale architecture for small datasets. It successfully improve the performance of GAN-based model on this task and make them close, even comparable to VAE-based models, which is dominant on this task. Moreover, the efficiency of CCD-based GAN is better than diffusion based model.

### Strengths
This paper's content covers a pretty wide range. Its empirical findings include:

1. Understanding how we should select our models based on our dataset characteristics and computational resources

2. Improving the performance of GAN-based models on this task

The recommendations are useful for researchers to apply in their research

### Weaknesses
1. The experiments, especially compared to the main benchmark paper TSGBench, is not comprehensive enough. Many datasets included in TSGBench are not covered. The TSGBench uses 10 datasets, while this paper only make use of the Stock and Energy dataset. The generalizability of the recommendation on other domains is questionable. Some baselines are also missing.

2. The writing is so confusing. I seldom comment a paper with this issue. But this paper's contribution is quite unclear. I spent several days trying to understand the central contribution of this paper. In abstract, the authors said that they would like to provide a recommendation. I understand it as a kind of more instructive benchmark. But then they start to present CCD, which is a margnially novel improvement on the GAN-based model (a new kind of discriminator in GAN). After that they again start to do analysis. My understanding is that the authors propose a relatively new improvement on GAN-based models. But then they found that the proposed model is still defeated by VAE-based model on small-scale dataset and diffusion models when resource is sufficient. So they try to sell their work by embedding it into a so-called recommendation.

3. Some results in this recommendation is well-known. The finding 4 about diffusion model's large training and inference load is well-known.

### Questions
1. What is the main contribution of this paper? Do you want to sell a new method or provide a recommendation?

2. What are the performances of the CCD on other domains such as air quality?

3. About the training time, I hope to know more detailed analysis. For example, if method A is with longer training time of method B, is it because A need more iterations, or because its computational load on one sample is higher?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses three issues in the existing MSTG recommendation guidance: inadequate evaluation, limited independent exploration of channels, and the inability of CCD to capture dependencies. The authors propose an improved solution for MSTG. The innovation lies in introducing an enhanced CCD that demonstrates strong practicality in small sample scenarios. Compared to previous recommendation guidance, the proposed enhanced CCD places greater emphasis on the independent channel framework and diffusion model methods, aiming to provide more refined recommendations for different contexts.

### Strengths
1. The paper is well-written, with clear and fluent language.
2. The experiments are comprehensive, and the details are thoroughly presented (exclude key hyperparameters though).
3. The overall methodology is easy to understand, and the enhanced CCD performs well.

### Weaknesses
1. Some equations are not clearly presented; for example, the notation in Eq. 4 is not standard.
2. Since hyperparameters are crucial for time series-related tasks, the lack of details on hyperparameters (including those for your method and the compared methods) makes replication difficult.
3. The paper feels somewhat lacking in originality. Notably, in Section 5, while three synthetic datasets are used, the motivation for using these datasets is insufficient.
4. In Section 5, the paper primarily explains the advantages of CCD on small sample data from the perspective of time series classification, but it lacks a discussion of other possible reasons. Moreover, it does not sufficiently explore the strengths and weaknesses of the diffusion model method and the CCD module in different scenarios.

### Questions
Plz see weakness.

### Soundness
3

### Presentation
2

### Contribution
2
