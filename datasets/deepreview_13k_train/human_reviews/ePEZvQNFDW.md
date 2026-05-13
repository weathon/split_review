# Continuous Ensemble Weather Forecasting with Diffusion models

- Decision: Accept
- Scores: 5, 5, 5, 5

## Abstract
Weather forecasting has seen a shift in methods from numerical simulations to data-driven systems. While initial research in the area focused on deterministic forecasting, recent works have used diffusion models to produce skillful ensemble forecasts. These models are trained on a single forecasting step and rolled out autoregressively. However, they are computationally expensive and accumulate errors for high temporal resolution due to the many rollout steps. We address these limitations with Continuous Ensemble Forecasting, a novel and flexible method for sampling ensemble forecasts in diffusion models. The method can generate temporally consistent ensemble trajectories completely in parallel, with no autoregressive steps. Continuous Ensemble Forecasting can also be combined with autoregressive rollouts to yield forecasts at an arbitrary fine temporal resolution without sacrificing accuracy. We demonstrate that the method achieves competitive results for global weather forecasting with good probabilistic properties.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper uses the diffusion model for continuous ensemble weather forecasting without requiring autoregressive steps to produce future values. As introduced in Section 4.2, the main idea is to replace the fixed Z with a stochastic process Z(T) with continuous sample trajectories.

### Strengths
The proposed method is presented clearly.

### Weaknesses
W1: there have been exsiting works for nonautoregressive sequence forecasting by diffusion models. However, realted investigation and discussions are missing, e.g., 

[1] NeurIPS'21 CSDI Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation

[2] ICML'23 Non-autoregressive Conditional Diffusion Models for Time Series Prediction 

W2: moreover, some questions and details are not provided.
- it would be better to explain what ensemble forecasting is formally
- it is still not very convincing why a stochastic process is better than random Gaussian noises for nonautoregressive generation. Because we can simply represent the forecast outputs as a vector of a length N. Then we can use a Gaussian vector to yield forecasts. 
- is there a significant difference between weather forecasting and general time series forecasting?
- what is the input size (the number of variables) of the model in the experiments? It seems there are many variables in the weather forecasting task. Did you perform univariate forecasting tasks for each variable?   
- how to fuse $n_{ens}$ trajectories to get the final predictions?

### Questions
In the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The "Continuous Ensemble Weather Forecasting with Diffusion Models" paper introduces an innovative framework for probabilistic weather forecasting using diffusion models. It focuses on enhancing computational efficiency by removing the autoregressive nature of sampling from diffusion models.

### Strengths
The model developed in this paper presents an approach that eliminates traditional autoregressive steps during sampling from diffusion models, allowing it to achieve high temporal resolution and efficiency in forecasting. This is an exciting approach for improving computational efficiency, a feature that has been challenging to achieve in weather prediction. 

The paper's application is exciting, as diffusion models are typically used in areas like image generation rather than meteorological forecasting.

### Weaknesses
The paper lacks references to closely related methods, such as Zheng et al. (2023) on fast sampling of diffusion models via operator learning, which shares similarities with the proposed model’s sampling approach. It would be beneficial to clarify how the proposed sampling method diverges from these approaches, particularly concerning the use of neural operators to accelerate the generation of diffusion trajectories. Specifically, a discussion on whether the proposed method could be combined with operator learning techniques to further enhance sampling efficiency would be valuable.

Although not directly used for weather data, recent models like Dyfusion, Alternator, and Mamba (with s-mamba used specifically for weather forecasting) have shown promise in similar domains, such as sea surface temperature forecasting. Including these models as baselines or discussing their relevance could offer a more comprehensive comparison, illustrating where this model stands relative to other contemporary approaches. The absence of a comparison with models like Dyfusion, which also employs diffusion for spatiotemporal forecasting, is a notable gap. Furthermore, the paper should address how the proposed method compares to the sequence modeling capabilities of Mamba, especially given its recent application to weather forecasting.

The paper mentions “regularity conditions” (e.g., Line 234) without specifying them rigorously. These conditions are fundamental to claims about trajectory continuity and temporal stability of forecasts. A formal mathematical description of these conditions, alongside proof or empirical validation, would be necessary to substantiate these claims. The lack of a precise definition for these conditions makes it difficult to assess the theoretical validity of the continuity claims. Additionally, the paper should clarify whether these conditions are specific to the chosen diffusion model or if they apply more broadly.

The claims regarding fixed noise across time steps and ODE-based interpolation are under-supported. No mathematical evidence or ablation study is presented to show the impact of fixing noise on forecasting performance. Including such a study could clarify the advantages of this design choice. It is unclear how fixing the noise affects the temporal dependencies in the generated trajectories and whether this choice introduces any biases. Furthermore, the paper should provide a more detailed explanation of how the ODE solver is used for interpolation and why this approach is superior to other interpolation techniques.

The proposed Algorithm 2 seems tailored to a specific diffusion model setup. It would be valuable to discuss whether this algorithm generalizes to other diffusion models or is fundamentally limited to the framework outlined in the paper. A broader discussion on this topic could enhance the paper’s applicability to related models. It is unclear if the algorithm can be adapted to other continuous normalizing flow models, such as those based on flow matching or stochastic interpolants, and what modifications would be necessary.

The results lack completeness, as only two of the five variables used for forecasting are presented in Table 2. Including comparisons for all five variables would provide a clearer picture of the model's strengths and weaknesses across different atmospheric variables. The selective presentation of results makes it difficult to assess the model's overall performance and identify potential biases towards certain variables. A comprehensive evaluation should include all variables to ensure a fair and complete assessment.

The absence of error bars due to computational limitations weakens the robustness of the reported results. Given the probabilistic nature of the model, showcasing variability over multiple runs would offer greater confidence in the findings. Including error bars or confidence intervals for at least a subset of key results would be helpful, even if computational constraints prevent a complete assessment. The lack of error bars makes it difficult to determine the statistical significance of the reported results and assess the reliability of the model.

Numerous claims about model performance, such as trajectory continuity, lack rigorous mathematical proof and appear to rely on empirical observations. Addressing this would lend greater theoretical robustness to the proposed model. The paper should provide formal proofs or derivations for key claims, particularly those regarding trajectory continuity and temporal stability, to strengthen the theoretical foundation of the proposed method. The reliance on empirical observations without formal proofs weakens the theoretical contribution of the paper.

There is no mathematical derivation for the training objective and loss function. A step-by-step derivation of these, with explanations of any modifications relative to standard diffusion model objectives and the rationale for these modifications in the weather forecasting context, would clarify the theoretical foundation of the approach. The absence of a detailed derivation makes it difficult to understand the specific choices made in the training process and how they relate to the weather forecasting task.

### Questions
Could you clarify the rationale behind using fixed noise across time steps? Additionally, has any sensitivity analysis or ablation study been conducted to validate this design choice? If so, please provide these findings.

Could you further explain how interpolation using an ODE solver contributes to the model’s performance, and how it compares to alternative interpolation methods?

Only two of the five forecasting variables are included in Table 2. Could you explain the rationale for this selective presentation and consider including results for all five variables to enable a comprehensive evaluation?

Could you provide formal proofs or derivations for key claims, particularly those regarding trajectory continuity and temporal stability?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an ODE-based method to address the limitations of previous a single forecasting step and rolled out autoregressively methods for weather prediction. It can generate long-range weather predictions without iteration and forecast arbitrary lead times.

### Strengths
- It is interesting to use probability flow ODE of the noise in diffusion models. Leveraging a lead-time-dependent deterministic ODE-solver to generate a smooth and continuous trajectory is meaningful compared to autoregressive methods.
- Authors provide intensive experiments on their method.

### Weaknesses
 - Need more descriptions on how probability flow ODE works.
- Need more comparisons with other SOTAs. 
- No available codes to help readers better understand the paper.
- It is a good idea to use the probability flow ODE from the work proposed from https://arxiv.org/pdf/2206.00364 in diffusion models. But what is the assumption behind the customized ODE in Eq. (2)? Why is there a linear noise level $sigma$ in Eq. (2)? What if $\sigma^2$? More explanation would help. 
- From the paper title and section 4 name, "CONTINUOUS" seems to be used to describe $ensemble forecasting$. However, what the authors really want to convey is the temporal continuity, i.e., any arbitrary fine temporal resolution. You may need to think over the rephrasing. Otherwise, it is confusing for readers (at least for me).
- In Figure 1, do you need to include the 1-hour prediction as the input for the 6-hour prediction? I saw you have explanations in sections 3 and 4. But Figure 1 deserves a more precise description within its title since it is the main framework of your method.
- It would be better to provide more comparisons with previous SOTA ML models. Even though I know not all models did not release source codes to the public, but some did, e.g., FourCastNet and ClimaX. 
- The authors mentioned the limitation of diffusion models: computationally expensive. I suggest adding more analysis of computational efficiency.
- You are using the letter 'k' for different representations (see Eq. 1 and Alg. 1).
- It is customary to denote a time point with the superscript or subscript. It looks like a function if using $X[k+1]$ or $X(\tau)$.
- In the line under Eq. (2), why is $z(1)$ for $X[k+1]$? Isn't it the number of diffusion steps or the noise levels?
- What is $v_i^{k}$ in Algorithm 2?

### Questions
**Major:**
- It is a good idea to use the probability flow ODE from the work proposed from https://arxiv.org/pdf/2206.00364 in diffusion models. But what is the assumption behind the customized ODE in Eq. (2)? Why is there a linear noise level $sigma$ in Eq. (2)? What if $\sigma^2$? More explanation would help. 
- From the paper title and section 4 name, "CONTINUOUS" seems to be used to describe $ensemble forecasting$. However, what the authors really want to convey is the temporal continuity, i.e., any arbitrary fine temporal resolution. You may need to think over the rephrasing. Otherwise, it is confusing for readers (at least for me).
- In Figure 1, do you need to include the 1-hour prediction as the input for the 6-hour prediction? I saw you have explanations in sections 3 and 4. But Figure 1 deserves a more precise description within its title since it is the main framework of your method.
- It would be better to provide more comparisons with previous SOTA ML models. Even though I know not all models did not release source codes to the public, but some did, e.g., FourCastNet and ClimaX. 
- The authors mentioned the limitation of diffusion models: computationally expensive. I suggest adding more analysis of computational efficiency.

**Minor:**
- You are using the letter 'k' for different representations (see Eq. 1 and Alg. 1).
- It is customary to denote a time point with the superscript or subscript. It looks like a function if using $X[k+1]$ or $X(\tau)$.
- In the line under Eq. (2), why is $z(1)$ for $X[k+1]$? Isn't it the number of diffusion steps or the noise levels?
- What is $v_i^{k}$ in Algorithm 2?

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
2

### Summary
This paper introduces Continuous Ensemble Forecasting for global weather forecasting.

### Strengths
1. Weather forecasting is an important problem.

2.The method introduced in the paper seems to exhibit a certain level of novelty.

3.Some of the figures in the paper look good.

### Weaknesses
1.The paper's presentation seems somewhat disorganized. The introduction does not clearly articulate the limitations of current weather forecasting methods or how the proposed method addresses these limitations. Figure 1, being the first figure, lacks sufficient information; ideally, a single figure should clearly highlight the differences between the proposed method and previous methods, as well as explain how the proposed method overcomes the limitations of prior approaches. In the Methods section, there is a tendency to mix descriptions of existing methods with the new method, which can obscure the exact nature of the contribution made by the proposed method. Figure 2 should also provide a clearer depiction of the methodology.

2.Based on the unclear description provided in the paper, the contributions appear insufficient, and the contributions listed in the introduction seem to be something that any weather forecasting model could achieve.

3.The baseline models compared in the paper are somewhat limited and do not appear to be the latest SOTA models. Moreover, according to Table 1, the ARCI-24/6h model proposed in the paper (if I understand correctly) is not the optimal model under most settings.

### Questions
1.Were the limitations of previous methods that they were computationally expensive? How does the method proposed in the paper address the limitations of previous approaches?

2.What specific contributions does the paper make that differentiate it from other weather forecasting models?

### Soundness
2

### Presentation
2

### Contribution
2
