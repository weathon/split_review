# A Study of Posterior Stability for Time-Series Latent Diffusion

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 3, 5, 5, 8

## Abstract
Latent diffusion has demonstrated promising results in image generation and permits efficient sampling. However, this framework might suffer from the problem of \textit{posterior collapse} when applied to time series. In this paper, we first show that posterior collapse will reduce latent diffusion to a variational autoencoder (VAE), making it \textit{less expressive}. This highlights the importance of addressing this issue. We then introduce a principled method: \textit{dependency measure}, that quantifies the sensitivity of a recurrent decoder to input variables. Using this tool, we confirm that posterior collapse significantly affects time-series latent diffusion on real datasets, and a phenomenon termed \textit{dependency illusion} is also discovered in the case of shuffled time series. Finally, building on our theoretical and empirical studies, we introduce a new framework that extends latent diffusion and has a stable posterior. Extensive experiments on multiple real time-series datasets show that our new framework is free from posterior collapse and significantly outperforms previous baselines in time series synthesis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the problem of posterior collapse in latent diffusion models, specifically when applied to time series data. The authors provide a systematic analysis of this issue, showing that posterior collapse can reduce the expressiveness of latent diffusion to that of a variational autoencoder (VAE). They introduce a novel dependency measure to quantify the impact of latent variables on the generation process and identify a phenomenon called dependency illusion when time series data are shuffled. Building on these insights, the authors propose a new framework that eliminates the KL-divergence regularization, permits an expressive prior distribution, and ensures the decoder remains sensitive to the latent variable. Extensive experiments demonstrate that this framework avoids posterior collapse and significantly improves time series generation.

### Strengths
1.	The introduction of dependency measures to diagnose and address posterior collapse is both novel and insightful, providing a fresh perspective on an important issue within latent diffusion models.
2.	The paper offers a solid theoretical foundation for the analysis of posterior collapse, and the proposed framework is well-motivated by both theoretical insights and empirical observations.
3.	The proposed framework demonstrates significant improvements in the performance of time-series generation models, effectively addressing a key limitation in existing approaches.

### Weaknesses
1.	While the paper presents strong results for time-series data, it lacks a detailed discussion on the generalizability of the approach to other data modalities, such as images or text. Including a brief exploration or discussion of potential extensions could further enhance the contribution.
2.	The experimental details, including specific configurations for baselines and the selection of hyperparameters, are not fully elaborated in the main text. Providing more comprehensive explanations in these areas would improve the paper’s clarity and reproducibility.
3.	Although the results are promising, some of the visualizations could be made more intuitive, particularly for readers unfamiliar with latent diffusion models. Additionally, converting the figures to vector graphics would significantly improve their quality, as several of the current images appear blurry and lack sharpness, which makes interpretation more difficult. Enhancing the clarity of the figures would improve the overall presentation of the paper.

### Questions
1.	Could the authors clarify how the dependency measure scales with longer time-series datasets? Does the framework handle large datasets efficiently?
2.	Have the authors considered extending this approach to other data types beyond time series? If so, how might the framework need to be adapted?
3.	Is there a specific reason for not including additional baselines, such as non-latent diffusion models, for comparison in the empirical section?

### Soundness
2

### Presentation
2

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
The paper investigates the issue of posterior collapse in latent diffusion models for time series data, where the latent variable becomes ineffective in influencing the model’s output. The authors propose a dependency measure to quantify how much the decoder relies on the latent variable, highlighting not only posterior collapse but also a related phenomenon termed dependency illusion. Then the paper introduces a new framework to address these issues by removing KL-divergence regularization and enhancing the decoder’s sensitivity to the latent variable, improving posterior stability. Experiments demonstrate that the proposed method achieves better performance than standard latent diffusion models with posterior collapse mitigation techniques across various time series datasets.

### Strengths
- The paper addresses a previously underexplored issue in time series diffusion models—posterior collapse—which has primarily been studied in variational autoencoders (VAEs) but not in the context of diffusion models for time series.
- The dependency measure provides an insightful tool for quantifying the decoder’s reliance on the latent variable. This measure enables detection of both posterior collapse and dependency illusion, offering valuable diagnostic capabilities for latent-variable models.
- The approach aligns with the paper’s theoretical objectives, yielding meaningful performance improvements.

### Weaknesses
 - The empirical evaluation lacks comparisons with stable time series models that naturally avoid posterior collapse, such as ARIMA, RNNs, LSTMs, transformers, and temporal convolutional networks. Including these baselines would provide context on whether the proposed framework offers advantages beyond mitigating posterior collapse. The author also did not compare with recent baselines for time series, which are diffusion-based. Please check papers published in NeurIPS/ICLR/ICML in the past two years.

- The paper references Bowman et al. (2016) to support claims about posterior collapse in latent-variable models for time series, which may be outdated. This raises questions about whether latent diffusion models represent the current state of the art in time series modeling. Comparing the approach with recent state-of-the-art time series methods would strengthen the justification for the proposed framework.

- Although the datasets used are realistic, the paper does not discuss broader real-world applications or scenarios where posterior stability is crucial, such as in anomaly detection or real-time forecasting. Adding context on practical use cases would clarify the framework’s relevance.

### Questions
- Could the authors include comparisons with recent state-of-the-art time series models, such as ARIMA, LSTMs, transformers, and TCNs, which are naturally robust against posterior collapse? This would contextualize the proposed method’s advantages relative to stable baselines.

- Could the authors provide clearer definitions or examples for terms like dependency illusion and posterior collapse in the context of latent diffusion models? A simplified explanation would improve accessibility.

- Are there specific real-world applications, such as anomaly detection or real-time forecasting, where this framework would be particularly useful? A discussion of practical use cases would strengthen the framework’s relevance.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the issue of posterior collapse in time-series latent diffusion models, a phenomenon that limits model expressivity by reducing it to a simpler VAE model. The authors introduce a dependency-measure regularization aimed at alleviating this collapse specifically within time-series data. Experiment results on three datasets (WARDS, MIMIC, and Earthquakes) demonstrates initial improvements in preventing posterior collapse over shorter timeframes.

### Strengths
--The paper tries to focus on the specific issues of time-dependency collapse in the case of time series data and diffusion models.

--The shuffling experiments help illustrate how a latent variable is not being used strongly throughout all time steps

### Weaknesses
--The problem is not sufficiently well motivated.  In particular, the two types of mode collapse which in time series (time-dependent and time-independent) are not discussed.  The reduction to a VAE is only about the elimination of the time-dependent influence.  The impact of this simplification is not sufficiently discussed. Specifically, the paper does not explore how the latent space is affected by this collapse, or how the generative process is limited by the loss of temporal information in the latent representation. A more detailed discussion on the implications of this reduction for downstream tasks would be beneficial.

--Moreover, the less expressivity is not shown explicitly to be a bad thing in the context of time series in general.  There are potentially time series which are driven by a static latent process. The paper should provide a more nuanced discussion on when this reduction in expressivity is detrimental and when it might be acceptable or even beneficial. For example, are there specific characteristics of time series data that make this collapse more problematic? Are there cases where a static latent representation is sufficient or even preferable?

--Although the dependency measure is well-defined, there is little theoretical analysis exploring its properties and its relationship to the reduction to a VAE model. The paper should include a more rigorous analysis of the dependency measure, including its sensitivity to different model parameters and its relationship to the latent space. It is also unclear how this measure relates to the actual generative performance of the model, and whether optimizing this measure directly leads to better generative results.

--There is no analysis of the results showing specifically how the introduced technique solved the problem of mode collapse. Results with good Wasserstein distance do not directly imply that the issue of mode collapse was resolved. The paper needs to provide more direct evidence that the proposed method alleviates the posterior collapse, such as visualizations of the latent space or analysis of the generated samples that demonstrate the diversity and quality of the generated time series. A more detailed analysis of the latent space and its evolution during training would be valuable.

- This paper claims that they are the first to address the posterior collapse problem in latent diffusion for time series, but it really boils down to the old autoencoder problem. And the diffusion model became a redundant module when the input is a standard Gaussian distribution is a simple extension of the problem of autoencoder. The paper should more clearly differentiate the proposed approach from existing autoencoder-based methods and justify the use of a diffusion model in this context.

### Questions
It’s unclear to me why negative local dependency is bad. The authors claimed that it’s because the previous timestamp’s data may be from a low density region and therefore an outlier. But in case that the actual next value to be decoded should indeed be an extreme value, why is that problematic?

Can you discuss the stability of the training? In cases where we 1) train the diffusion model and the decoder together 2) we require the decoder to decode the time series regardless of which timestamp’s noised version of the latent variable is selected.

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
This paper proposes a new approach to establish a stable posterior for time series within the latent diffusion framework. The new approach circumvents the problematic KL-divergence regularization, prevents the posterior collapse, and maintains the influence of the latent variable in the decoder. The authors provide both theoretical and experimental support to their newly proposed framework.

### Strengths
The study of the latent diffusion model when applied in the context of time series is a trended topic and super interesting. The authors approach this by defining a proper dependency measure to quantify the problem of posterior collapse of the latent variable, and propose a new framework inspired by re-thinking the design of VAE and autoencoders. The new framework is equipped with new loss functions and regularizations, free from posterior collapse. The discussion comes together with empirical support. Overall, the paper's content is clear and easy to follow.

### Weaknesses
1. The experimental results mainly focus on real-world data to demonstrate the sampling benefits of the proposed method. Can the authors conduct synthetic data experiments to interpret and validate the effectiveness of the newly proposed component in the framework (e.g., the introduced loss function or regularization)?

2. The prediction ability of a time series model is critical. Can the authors evaluate the proposed framework in terms of other metrics, such as the predictive MAE, to demonstrate its prediction ability?

3. In addition to point 2, can the author compare with other advanced time-series models? Only compared with the latent diffusion family would not be convincing enough for advertising the model in the time series community.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to address the posterior collapse problem of latent diffusion for time series data. The authors propose a dependency measure method to quantify how posterior collapse happens. And they propose a KL-divergence regularization based method to improve the sensitivity of decoder to the latent variable for time-series latent diffusion.

### Strengths
The authors focus on an important issue of latent diffusion, that is posterior collapse, and propose a potential method to quantify the posterior collapse of latent diffusion for time series data.

### Weaknesses
1.Regarding to the dependency illusion, you give an example (upper right subfigure of figure 1) to explain. But it’s unclear from figure 1 how you arrive at the conclusion that "Even when the time series is randomly shuffled and thus lacks structural dependencies, the decoder of latent diffusion still heavily relies on input observations (instead of the latent variable) for prediction." Could you clarify how you determine that the decoder "heavily" depends on input observations? Providing a more detailed explanation or additional quantitative evidence would help support this observation.

2.In section 3.1, the definition of posterior collapse seems a general term for all data, not only time series data. In section 3.2, you introduce a dependency measure to demonstrate the occurrence of posterior collapse in time series data. How does this measure specifically address time series data? Would this measure yield the same conclusion if applied to non-time series data?

3.As shown in Figure 4, the dependency of the decoder on the latent variable decreases across both datasets. Although this trend appears improved compared to Figure 2, it would strengthen your findings to compare your method against additional baseline models, rather than only basic latent diffusion.

4.There is a lack of experimental evidence supporting that the proposed dependency measure can accurately assess the impact of the latent variable on the decoder. You should compare your method with other measurement approaches and demonstrate how it outperforms them, providing a more comprehensive validation of its effectiveness.

5.The baselines are not sufficient enough. Only three baselines and all of them are before 2019. Please compare with more the state-of-art works.

6.Reference in this paper seems to be too old. And some of them are repeated. For example, papers in line 573 and line 576 are the same one.

### Questions
1.You claim that “when applied to time series data, this framework might suffer from posterior collapse” in the first paragraph. Do you have any evidence to support this claim? Is this phenomenon due to the diminishing influence of the latent variable on the decoder over time steps? How do you justify the decreased dependency correspond to the posterior collapse of latent diffusion for time series data? 

2.In section 4.2, you mention that the the variational inference in your framework leads the latent variable to be smooth in its effect on decoder. Is this the reason why your framework can increase the sensitivity of decoder to latent variable?  Can your framework be applied to non-time series data? It seems the proposed method is not specific to time series data.

### Soundness
2

### Presentation
2

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
This work starts from an analysis on the posterior collapse issue of latent diffusion for capturing time series. In particular, the KL-divergence from the standard Gaussian prior to the latent variable distribution approximated using latent diffusion, may reduce the time series latent diffusion to a VAE model. The authors define a dependency measure, which shows that the influences of the latent variables on decoding the observations, will decrease to zero along the diffusion time steps. In particular, as analyzed in the paper, the decoder built upon recurrent neural nets may decode the current observations only using the past observations, and thus leads to the dependency illusion issues. To address the problems, the paper develops a novel framework, in which the authors remove the KL-divergence regularization that causes the posterior collapse, decode the predicting observations using the latent variable sampled at intermediate diffusion steps, and introduce a novel penalty to avoid dependency illusion issues. The final experiments demonstrate the new framework can effectively avoid posterior collapse, and thus achieves superior generation quality, in comparisions to some SOTA time series latent diffusion methods.

### Strengths
Novelty: It is the first work to discuss the posterior collapse issue for time series latent diffusion. In particular, the paper introduces the novel dependency measure to quantify how the impacts of the latent variables on the generation of the predicting observations, decrease along the time steps. The authors develop a novel framework, which effectively avoid the dependency illusion issue, and outperforms the related time series latent diffusion models in terms of generation quality.

Clarity: This work clearly illustrates the posterior collapse and dependency illusion issues by plotting the dependency measures over time steps. The most parts of the analysis are clearly presented, and easy-to-follow.

Significance: The work demonstrate a significant issue for latent diffusion being applied to capturing time series data. The introduce dependency measure might be used in quantifying the posterior stability of the other related methods, and thus appears to be crucial.

### Weaknesses
The final experiments only demonstrate the compared models on only three dataset, using Wasserstein distance to measure between the true and generated time series. Perhaps the experiments could be enhanced by considering more evaluations metrics?

### Questions
I agree on the importance of posterior collapse issue found by the authors. I am wondering how is the generation performance of time series diffusion model in which latent variables have the same dimension as the observations.

### Soundness
3

### Presentation
3

### Contribution
3
