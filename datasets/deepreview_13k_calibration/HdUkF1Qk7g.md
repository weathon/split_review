# Diffusion-based Decoupled Deterministic and Uncertain Framework for Probabilistic Multivariate Time Series Forecasting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Diffusion-based denoising models have demonstrated impressive performance in probabilistic forecasting for multivariate time series (MTS). Nonetheless, existing approaches often model the entire data distribution, neglecting the variability in uncertainty across different components of the time series. This paper introduces a Diffusion-based Decoupled Deterministic and Uncertain ($\mathrm{D^3U}$) framework for probabilistic MTS forecasting. The framework integrates non-probabilistic forecasting with conditional diffusion generation, enabling both accurate point predictions and probabilistic forecasting. $\mathrm{D^3U}$ utilizes a point forecasting model to non-probabilistically model high-certainty components in the time series, generating embedded representations that are conditionally injected into a diffusion model. To better model high-uncertainty components, a patch-based denoising network (PatchDN) is designed in the conditional diffusion model. Designed as a plug-and-play framework, $\mathrm{D^3U}$ can be seamlessly integrated into existing point forecasting models to provide probabilistic forecasting capabilities. It can also be applied to other conditional diffusion methods that incorporate point forecasting models. Experiments on six real-world datasets demonstrate that our method achieves over a 20\% improvement in both point and probabilistic forecasting performance in MTS long-term forecasting compared to state-of-the-art (SOTA) probabilistic forecasting methods. Additionally, extensive ablation studies further validate the effectiveness of the $\mathrm{D^3U}$ framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a novel diffusion-based time series framework called D3U, designed to enhance probabilistic forecasting. D3U effectively decouples the deterministic and uncertain components of the forecasting process. The conditional network is focused on delivering precise point forecasts, while the conditional DDPM (PatchDN) handles high-uncertainty probabilistic forecasting. Additionally, D3U functions as a plug-and-play framework, allowing for easy integration into existing point forecasting models. Experimental results demonstrate substantial improvements over SOTA baselines.

### Strengths
1. The motivation behind this work is strong. The approach of decoupling point and probabilistic forecasting is well-founded.
2. The design of the two components to address different forecasting targets is logical and effective.
3. The experiments are comprehensive, and the improvements in performance are notable.
4. The writing and presentation are clear and easy to follow.

### Weaknesses
1. A more detailed discussion of the differences between this work and related studies is essential to clarify its contributions. For example, TMDM also integrates deterministic transformer and diffusion models.
2. Additionally, the selection of baselines could be more comprehensive. Models such as TimeGrad and CSDI, which are relevant probabilistic forecasting approaches, are not included. Currently, the focus is primarily on non-autoregressive models.

### Questions
Given that other works also integrate diffusion models with deterministic models, what distinguishes your approach from theirs? How is your model superior in design? For example, how does it compare to models like TAMA, which you mentioned in your paper? And what about CARD[1] ?

[1]Han, Xizewen, Huangjie Zheng, and Mingyuan Zhou. "Card: Classification and regression diffusion models." Advances in Neural Information Processing Systems 35 (2022): 18100-18115.

### Soundness
3

### Presentation
3

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
The authors describe a novel framework (D3U) for probabilistic time series forecasting. It combines the point forecasting of seasonal and trend components with a generative sampling model for the residual component.
The point forecasting part consists of a well-known model (SparseVQ) and is used to produce a prediction $\hat y$ of the input time series as well as a latent representation $f_{enc}(x)$ which serves as a condition for the generative part.
The generative part is a DDPM which shall produce samples of the residual $y-\hat y$, the reverse process is hereby conditioned on the latent $f_enc(x)$ and the conditional expectation in the reverse process is modelled by a novel patch-based denoising network $g_\phi$. 
The network $g_\phi$ is comprised of a sine-positional encoder for a strided windows representation of the residuals and transformer encoder blocks. It is conditioned on the latent $f_enc(x)$.
In experiments, the model shows competitive or better performance compared to SOTA models on different datasets. The authors conclude that the architecture can serve as framework to obtain a generative sampling model of improved performance for arbitrary point forecasting, conditioning models.

### Strengths
The authors show a general way of extending classical point forecasting models to generative sampling models. The paper contains a comprehensive and well-founded survey of existing approaches and works. The results show improved performance compared to SOTA approaches.

### Weaknesses
The general idea to split the prediction of a time series in the prediction of trend/seasonal components and the residual is well-known, as is the usage of generative approaches to model the residual. However, the details of the architecture are new.

p2: the residual component tends to contain more uncertainty than the trend and seasonal components: this is time-series specific. It is not universally true that residuals are always more uncertain; this depends heavily on the nature of the time series and the effectiveness of the detrending/deseasonalization method.

p3: contribution 2: is this a contribution? It looks like a second description of D3U and hence an additional paragraph belonging to the first contribution.

p4: In statistics, $\cal F(X)$ is the sigma-algebra generated by $X$. Better use another symbol.

p5: The symbols $x$, … are not introduced.

p5 l.243: $\hat y_g+E(\hat y|x_h)$ should be $\hat y_g+\hat y$

p6 l. 281: check the formula of $\mu_\phi$ (how is it derived? Shouldn't be $a$ instead of $\bar a$ and the $\beta$ outside the square root?). The derivation of the mean in the reverse diffusion process needs more clarity, specifically how the data prediction model $r_\phi$ is incorporated and how the conditional input $c$ influences this process. The current explanation lacks sufficient detail to understand the exact mathematical steps.

p6 l. 297: check the formula $N=\dots$.

p6 l. 322: $p^k$ is not introduced.

p7: check the formulas (12) and (13) for typos ($r^k_{Pembed}$ is used multiple times)

p10: section 4.3.: there were better results obtained when SparseVQ was replaced by iTransformer. It should be explained why SparseVQ is proposed in the rest of the paper. The paper should clarify the specific reasons for choosing SparseVQ as the primary point forecasting model, especially given the reported performance improvements with iTransformer. The rationale behind this choice and its potential impact on the overall framework should be discussed more thoroughly.

### Questions
p2: the residual component tends to contain more uncertainty than the trend and seasonal components: this is time-series specific. 

p3: contribution 2: is this a contribution? It looks like a second description of D3U and hence an additional paragraph belonging to the first contribution.

p4: In statistics, $\cal F(X)$ is the sigma-algebra generated by $X$. Better use another symbol.

p5: The symbols $x$, … are not introduced.

p5 l.243: $\hat y_g+E(\hat y|x_h)$ should be $\hat y_g+\hat y$

p6 l. 281: check the formula of $\mu_\phi$ (how is it derived? Shouldn't be $a$ instead of $\bar a$ and the $\beta$ outside the square root?).

p6 l. 297: check the formula $N=\dots$.

p6 l. 322: $p^k$ is not introduced.

p7: check the formulas (12) and (13) for typos ($r^k_{Pembed}$ is used multiple times)

p10: section 4.3.: there were better results obtained when SparseVQ was replaced by iTransformer. It should be explained why SparseVQ is proposed in the rest of the paper.

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
4

### Summary
The D3U framework is introduced for probabilistic multivariate time series (MTS) forecasting. D3U combines a point forecasting model for high-certainty components with a conditional diffusion model to capture high-uncertainty components. D3U achieves excellent performance across six real-world datasets and includes comprehensive ablation studies.

### Strengths
Overall, the paper is well-written and easy to follow. The details in each section are well-explained, and the experiments are thorough.

### Weaknesses
The main concern is the originality of the paper. The concept is straightforward: decomposing multivariate time series data into deterministic and uncertain components, using a point forecasting model for the high-certainty component and a conditional diffusion model for the high-uncertainty component. Most of the diffusion design relies on previous work; for example, SparseVQ (Zhao et al., 2024) is used as the conditioning network, and the conditional DDPM is almost the same as the original. The only apparent innovation is the design of the Patch Denoising Network, which itself is not overly complex. Overall, this work feels more like a stitching together of existing methods applied to time series data, with insufficient original contributions.

The proposed method requires decomposing the time series data. As shown in Appendix B, decomposing the time series data requires some prior knowledge or specific hyperparameter settings. A natural question arises: when deploying the trained model in a new scenario, you often don’t know how the training data was decomposed. So, how would you decompose the data in the new scenario? Additionally, if the characteristics of the deterministic and uncertain components in the time series data differ between the new scenario and the training data, how can you ensure the model performs well?

### Questions
The proposed method requires decomposing the time series data. As shown in Appendix B, decomposing the time series data requires some prior knowledge or specific hyperparameter settings. A natural question arises: when deploying the trained model in a new scenario, you often don’t know how the training data was decomposed. So, how would you decompose the data in the new scenario? Additionally, if the characteristics of the deterministic and uncertain components in the time series data differ between the new scenario and the training data, how can you ensure the model performs well?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces D3U for probabilistic multi-variable time series (MTS) forecasting, integrating non-probabilistic forecasting with conditional diffusion generation. This enables the framework to produce both accurate point predictions and probabilistic forecasts. Experiments conducted on six real-world datasets demonstrate the superior performance of D3U.

### Strengths
1. The D3U framework innovatively combines a point forecasting model to handle high-certainty components within the time series non-probabilistically, while employing a diffusion model to capture the probabilistic distribution of high-uncertainty components. This approach represents an advancement over previous diffusion models that typically model the entire series.

2.D3U is designed as a plug-and-play framework that can be seamlessly integrated with existing point forecasting models. Additionally, the paper introduces a novel patch-based denoising network, PatchDN.

3.The overall organization of the paper is clear, and the paper is understandable in most parts.

### Weaknesses
1.My primary concern is the effectiveness of the diffusion model within the framework. I have detailed my questions regarding the actual utility of the diffusion model in predictions in Question 1.

2.The diffusion-based time series models included for comparison are somewhat limited, excluding several advanced diffusion-based models developed in the last two years. Specifically, the comparison lacks models that explicitly address long-term dependencies and non-stationary characteristics often found in real-world time series data. This omission makes it difficult to assess the true novelty and performance of the proposed approach against the current state-of-the-art.

3.As indicated in Table 1, the proposed model performs worse than state-of-the-art point forecasting models in most settings. This raises concerns about the practical utility of the proposed framework, especially if the primary goal is to achieve accurate point predictions. The added complexity of the diffusion model should ideally translate to a significant improvement in predictive performance, which is not evident from the results presented.

4.The model's complexity is notably higher compared to traditional point-to-point models, which might restrict its applicability in practical scenarios. The computational overhead introduced by the diffusion component needs to be carefully considered, especially for large datasets or real-time applications where efficiency is paramount. A detailed analysis of the computational cost and scalability of the proposed model is missing.

### Questions
1.What are the contribution proportions of the point forecasting model and the diffusion model to the final prediction? It is recommended that the authors provide a table of the respective proportions of point forecasting and probabilistic forecasting for different datasets and include visualizations of some examples. This would help readers understand the roles of the point forecasting model and the diffusion model within D3U and confirm the effectiveness of the diffusion model.

2.The results presented in Figure 1 are interesting. Have the authors explored a similar approach to decompose the series and then used a point forecasting model to predict the deterministic part, while employing a diffusion model to predict the residual obtained from the decomposition?

3.Are the weights of the pre-trained point forecasting model fixed in the D3U framework? Have the authors experimented with fine-tuning the point forecasting model simultaneously while training the diffusion model, or considered creating an end-to-end architecture for the entire model?

### Soundness
2

### Presentation
3

### Contribution
2
