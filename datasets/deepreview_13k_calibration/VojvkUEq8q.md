# Learning by Causality to Improve Channel Dependency Modeling in Multivariate Time Series Forecasting

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 8, 3, 3

## Abstract
Beyond the conventional long-term temporal dependency modeling, multivariate time series (MTS) forecasting has rapidly shifted toward channel dependency (CD) modeling. This shift significantly improves modeling quality by fully leveraging both multivariate relationships and temporal dependencies. Recent methods primarily model channel dependency through correlation learning (e.g., crossattention) or non-trainable statistical techniques (e.g., cross-correlation). However, these approaches struggle to fully capture the intrinsic relationships within MTS, particularly those stemming from directed cause-effect (i.e., causality) and nonstationary variates originating from diverse sources. In addition, causality may arise from the signals with different temporal behaviors, such as varying periodicity or discrete event sequences, which is not sufficiently discussed before. In this paper, we propose CALAS (Causality-enhanced Attention with Learnable and Adaptive Spacing), the first end-to-end learning method for MTS forecasting that uncover causality among variates without relying on statistical measures or prior knowledge. To model underlying causality, which consists of causal strength and propagation delay, we newly design a hypernetworks-based 1D convolutions mechanism. Inspired by dilated convolution with learnable spacings (DCLS) and spiking neural networks (SNNs), we extend discrete time delay into a continuous Gaussian kernel. Combining the hypernetworks-generated Gaussian kernel and convolutional weights (i.e., attention or causal strength), we achieve the end-to-end dynamic causality modeling mechanism. This mechanism enhances the model’s ability to capture time-varying causality across multi-source variates, ultimately improving the prediction accuracy, quality, and interpretability. For evaluation, we conduct extensive experiments with six real-world datasets and qualitative analysis to demonstrate CALAS’s superiority in capturing varying causality in a data-agnostic manner. The experiment results indicate that CALAS has significantly improved MTS forecasting accuracy compared to state-of-the-art methods by dynamically modeling causality among variates.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes CALAS, an end-to-end module that captures causality with propagation delay among variates to enhance multivariate time series forecasting. Technically, hypernetworks first output the strength and delay matrices for a given multivariate instance. Then Gaussian kernel is used to approximate the undifferentiable propagation delay. Experiments show that the proposed CALAS enhances forecasting accuracy of different backbones and also outperforms previous plug-in method LIFT.

### Strengths
1. Explicitly modeling propagation delay captures the lead-lag structure of causal relationships, allowing CALAS to more accurately reflect how signals influence each other over time.

2. CALAS demonstrates efficient improvements over baseline models.

### Weaknesses
1. The fundamental problem of this work is what exactly "causality" is. In Judea Pearl's causal inference framework, causality has a rigorous definition through concepts like do-calculus. However, while this paper frequently refers to causality, it lacks a precise, formal definition of the concept. The paper does not specify whether it aims to identify causal effects (i.e., the result of interventions) or simply causal relationships (i.e., dependencies), which are distinct concepts. Furthermore, the paper does not address potential confounders or feedback loops, which are critical to consider when making causal claims.

2. Building on the previous point, the proposed method appears to be a channel mixing with delay effect. There is no evidence that this model truly learns causality as claimed, nor is there a clear distinction from "correlation." The method essentially learns a weighted sum of lagged time series, which is a form of correlation analysis. The use of a Gaussian kernel to approximate delays does not inherently imply causality; it merely introduces a specific type of temporal weighting. The paper needs to demonstrate that the learned relationships are not simply spurious correlations due to shared latent factors or other confounding variables.

3. The writing needs improvement. As a technical paper, this work uses overly vague language rather than precise formulas. For example, 3.5 pages are devoted to the background, while the methodology is covered in just one page. In the experimental analysis, speculative phrases like "may show no causality" and "is likely due to" are frequently used without evidence. The paper lacks a clear mathematical definition of the proposed model, making it difficult to understand the underlying mechanisms and to reproduce the results. The description of the hypernetwork and the Gaussian kernel approximation is particularly lacking in detail.

### Questions
1. How are the extracted strength and delay matrices used in forecasting? Are they used to pre-process the input instance, and then the processed instance is input to the backbone?

2. Please describe the ablation study setting in detail. Including: 1)which backbone is used; 2)which prediction length is evaluated; 3)how are the  strength and delay matrices set in the ablated versions.

3. See my other questions in the #Weaknesses section.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper has presented CALAS, an end-to-end method for multivariate timeseries forecasting that can learn causality among variates without any statistical measures or prior knowledge. CALAS decomposes causal effect into causal strength and propagation delay, this results in better capturing the time delay and better interpretability, without adding any additional complexity to the model. The experimental results show that CALAS can provide more improvement than non-learning methods like LIFT.

### Strengths
- One of the important factors in measuring causality is the time required to wait to see the effect. While it has been extensively discussed, I believe estimating the delay as a part of the model is understudied. The idea of delay estimation is indeed important and interesting. 
- In addition to the good performance of CALAS in improving the chosen baselines, it is more interpretable than existing methods as it helps to understand causal strength and propagation delay separately. 
- The paper is overall well-motivated and easy to follow, though the presentation requires improvements.
An ablation study has been conducted and has shown the importance of contributions.

### Weaknesses
 - The presentation in the paper can be greatly improved. While the overall writing is good and contributions are well-motivated, there are several repeated sections that can be removed and used for additional experimental results or making figures bigger. For example, lines 88 and 103 are the same. The contributions are already discussed in lines 145-160, so there is no need to repeat them in 209-215. I also found Section 6 (Discussion) unnecessary and redundant as it has mostly been discussed in the paper. 
- It seems that the authors have overlooked a part of the literature that uses causal RNN-style (or convolution-style) models across variates [1, 2, 3]. Contrary to transformer-based models, these methods can provide us with directional causality.
- The main focus of the paper and experimental results are relatively narrow. Most recent studies on multivariate time series are more general methods [1] and achieve good performance across diverse tasks like classification, imputation, and anomaly detection. I do not see a limitation for CALAS to be applied for other tasks and it would be great if the authors could enhance the experimental results.

### Questions
Please see weaknesses.

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
3

### Summary
This paper reanalyzes the task of multivariate time series forecasting from the perspectives of causal strength and propagation delay. This is highly meaningful for improving model performance and interpretability. Moreover, this method has the advantage of adaptive training compared to previous statistical approaches. However, the articulation of this article is not very clear, and due to the absence of open-source code, reproducing the results is challenging. Additionally, the experimental section is not comprehensive enough.

### Strengths
The topic in this paper is meaningful. Modeling multivariate time series causality from the perspective of delays is notable. Parameterizing this process with a Gaussian kernel enables the model to adaptively explore the delayed causal relationships among multiple variables.

### Weaknesses
 * **W1**: I believe the primary issue with this article lies in its lack of clarity in expression and the substantial absence of details within the text (for more information, refer to the "Questions" section). Specifically, the description of the Gaussian kernel parameterization lacks sufficient detail, making it difficult to understand how the kernel's parameters are learned and how they influence the causal modeling. Moreover, the absence of corresponding code in the supplementary materials makes it challenging to complete the model framework and reproduce the results.

* **W2**: The experimental evaluation in this paper is weak, as it only encompasses standard prediction task results and ablation studies, neglecting the interpretability analysis emphasized in the Introduction. The paper does not demonstrate how the learned causal relationships can be visualized or interpreted, which is a significant drawback considering the stated motivation. I suggest that the authors include more case studies and explore the effectiveness of the proposed modules in tasks such as classification, anomaly detection, and others.

* **W3**: Currently, there are numerous models that incorporate specialized modules [1,2] to model variable causality on top of modeling time dependencies with a CI strategy. In particular, conducting Fourier transforms on the variable dimensions and utilizing linear layers for learning can efficiently and lightly model variable relationships [3]. The authors should comprehensively compare the advantages and disadvantages of these approaches, including their efficiency. The paper needs to clarify how the proposed Gaussian kernel approach compares in terms of computational cost and modeling capacity with these alternative methods.

* **W4**: Some minor details to consider include avoiding the use of "you" in expressions such as in line 321, and ensuring that each line does not consist of only a few words.

### Questions
* **Q1**: The paper has no corresponding content regarding how to penalize $\sigma$, as mentioned in line 337.

* **Q2**: The statement from lines 347 to 366 is quite ambiguous. Phrases like "the causal strength is shared for k possible delays" lack clarity. Terms such as the embedding vector M, h, and $N_o$ are undefined. I suggest that the authors rephrase this section for better understanding and coherence.

* **Q3**: Section 4.2 does not clearly explain how to handle multivariate time series data after obtaining the causal graph. Additionally, it only covers causal weight generation, but it does not detail how the other two parameters, $\sigma$ and d, of the Gaussian kernel are generated. These missing aspects need to be addressed in the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces CALAS, a new attention-style mechanism which is able to achieve improved performance across several datasets by combining DLCS (dilated convolutions with learnable spacing) alongside two hypernetwork learners to learn the lead-lag relationships in the time series dataset. Empirical performance is compared against the major prior work, LIFT, and competitive performance is achieved.

### Strengths
The paper targets an important problem of understanding channel dependencies and specifically follows the line of research highlighted by the LIFT paper.  This approach seems more structured than the existing LIFT paper by the use of the specific functional form in Equation (1); however, the nuances of such an assumption and its relation with existing work are not sufficiently explored (see below).

### Weaknesses
The authors use the language of "uncovering causality" and yet gravely misunderstand the existing literature in both Granger causality and causal discovery. In this sense, the research is about the channel dependencies using the same flavor of cross-temporal dependencies as the original definition of Granger causality. In spite of this, no discussion about this approach is given. Moreover, the language of "true causality" is used throughout the paper, despite it being known for decades that this is not true causality. It should be noted that this alone can be considered as sufficient grounds for rejection.

Other less serious concerns include:
- performance improvements over LIFT are generally extremely marginal and without error bars
- no analysis is given on the final learned models and the 'causal' structure which they uncover
- no theoretical analysis is given regarding the causal discovery of the proposed approach

### Questions
Can you clarify the graphical assumptions which are being made onto the multivariate time series to allow easier comparison with existing works in causality for time series?

Under what assumptions can you guarantee the exact recover and/ or identifiability of the underlying causal structure which you are aiming to learn?

Can you clarify how existing work in causality and in Granger causality compare to your proposed work?

Can you identify what you see as the key innovation of your work compared to the existing LIFT work?

### Soundness
1

### Presentation
2

### Contribution
1
