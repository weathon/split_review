# Universal Time-series Generation using Score-based Generative Models

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Score-based generative models (SGMs) have demonstrated unparalleled sampling quality and diversity in numerous fields, such as image generation, voice synthesis, and tabular data synthesis, etc. Inspired by those outstanding results, we apply SGMs to synthesize time-series by learning its conditional score function. To this end, we present a conditional score network for time-series synthesis, deriving a denoising score matching loss tailored for our purposes. In particular, our presented denoising score matching loss is the conditional denoising score matching loss for time-series synthesis. In addition, our framework is such flexible that both regular and irregular time-series can be synthesized with minimal changes to our model design. Finally, we obtain exceptional synthesis performance on various time-series datasets, achieving state-of-the-art sampling diversity and quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a score-based generative model for time-series generation and argues that a time-series score-based generative model should be autoregressive. To that end, an autoregressive score-matching objective is introduced.  Since this method is designed to handle both regular and irregular time-series forecasting, it is termed "Universal". The score-model is trained in the latent-space of an RNN-based encoder-decoder model. The paper also theoretically justifies the validity of their autoregressive score-matching objective. The paper considers several baselines and even adapts some of them to irregular time-series to showcase the advantages of their method based on predictive-score/discriminative score.

### Strengths
* Proposes a score-based universal time-series synthesis method. 
* Argues for an autoregressive-style generation for time-series and introduces a new loss objective and related architectural changes. 
* An extensive list of baselines is used to showcase the benefit of TSGM.

### Weaknesses
* The autoregressive score-based loss objective and related theory is incremental. 
* The results are evaluated with predictive-score and discriminative-score only. 
* The need for autoregressive structure is not justified empirically.
* From Table 8, it appears that the models are trained to generate 24 time-steps and so, one may say that this paper focuses on modelling shorter time-series. Generalization of this model when extrapolating to longer sequence-lengths (without retraining) is not evaluated.

### Questions
1) How does TSGM perform under forecasting? In my understanding, score-models can be flexibly adapted for inpainting and it is possible to evaluate based on imputation/forecasting errors. Please let me know if I am misunderstanding something. 
2) Appendix B contains experiments where TimeGrad/CSDI are applied to generation tasks and compared with TSGM. Can TSGM be compared with TimeGrad/CSDI when applying to forecasting/imputation tasks? 
3) Appendix M consists of one-shot generation experiments where one attempts to directly generate the time-series data. I feel that a fair comparison with TSGM should be based on one-shot generation of the sequence ${h_i}$. 
4) Can you provide empirical justification for autoregressive generation? 
5) In Eq. 8, why is the network $M_\theta$ outputting the score for previous n-1 time-steps that are already generated? Is this a typo? Could you please clarify the rationale behind this design if it is not a typo?
6) A common evaluation metric of generative models is to train a downstream model on generated samples (e.g., classification-accuracy score). Is it possible to train a Patch-TST model on the generated samples and use that to perform forecasting?

### Soundness
2

### Presentation
2

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
This paper introduces TSGM, a score-based generative model designed to generate time series data, including both regular and irregular time series. TSGM consists of an RNN autoencoder and a score-based model; the former is used to transform time series into latent representations, while the latter handles the generative process. Considering the autoregressive characteristics of time series data generation, TSGM derives its loss function based on denoising score matching. Experiments were conducted on four datasets, and the results demonstrate that TSGM outperforms methods based on VAEs and GANs in terms of generation performance.

### Strengths
The paper is written clearly.

The loss function is novel for SGM-based network on time series data.

### Weaknesses
1. The paper does not adequately cover recent work, especially from 2023 (only two survey papers are cited). Below are a few examples of ICLR 2024 works [1-3] that should be considered. This oversight significantly impacts the presentation of the paper's novelty, and these works should be included in the experimental comparisons to better validate the method's performance.

    [1] Diffusion-TS: Interpretable Diffusion for General Time Series Generation

    [2] Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns

    [3] Generative Modeling of Regular and Irregular Time Series Data via Koopman VAEs

2. The experiments should compare the proposed method with diffusion-based time series generation approaches, which have been frequently utilized in recent works, such as Diffusion-TS and MG-TSD [4]. Additionally, the paper needs to articulate the differences between score-based and diffusion-based methods to strengthen the motivation of the work.

    [4] MG-TSD: Multi-Granularity Time Series Diffusion Models with Guided Learning Process. In ICLR 2024.

3. As a data augmentation method, the experiments need to further compare the proposed approach in practical tasks such as time-series forecasting and imputation. And it is necessary to investigate whether the method can generate valuable data in scenarios with more complex data distributions, such as earthquake prediction and extreme weather forecasting, where class/data imbalance challenge is prominent. This will help to better understand the scope and applicability of the proposed method.

### Questions
Please refer to weakness.

### Soundness
3

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
3

### Summary
The paper proposes a score-based generative model for time series generation. The paper presents a score matching loss for this task, and shows that it is equivalent to another form which can be modeled with RNN latents. The paper then applies the proposed method for four different time series datasets and two different time series generation setups. Empirical results show that the proposed method outperform baselines.

### Strengths
- It is a novel idea to model the proposed score matching loss with RNN latents, and this is validated by the main theorem of this paper, which shows the equivalence of losses if the target score is additionally conditioned on $x_n^0$ as well. This is a simple yet effective way to perform score matching for this task; otherwise it will be expensive to optimize the vanilla loss function for time series generation.
- In the main experiments, the proposed method outperforms the baselines with a noticeable gap. The improvements are consistent across different datasets and time series types. The results show the effectiveness of the proposed method on these datasets.
- In the appendix, the paper conducts extensive ablation studies with respect to baseline methods, and show that prior methods including TimeGrad and CSDI could be extended to this task but they do not perform well.

### Weaknesses
The presentation of this paper needs significant improvement.
- In terms of writing, it is unclear across the paper (especially in section 3), making it very hard to follow. For example, many definitions or terminologies remain unexplained, some important details of the models are hidden from the paper, and with the current structure one has to jump back and forth to understand the notations and technical details but they are in fact very straightforward. 
- The paper does not justify the importance of the time series generation task compared to other tasks such as forecasting and classification. The key question is: why is it necessary to train a time series generation model? There are some quick answers to my mind: generating synthetic data for downstream tasks such as classification, understanding data bias and structure, or some application needs data generation given certain context. The first two are not addressed by the paper, and the last requires conditional generation, which is not addressed as well.

The paper significantly over-claims. 
- While the title indicates it is a universal model, the proposed method only deals with a restricted class of time series data and two tasks with uniform and non-uniform intervals. With "universal", I would expect a model that applies to a wide range of tasks (e.g. synthesis, forecasting or continuation, blank filling or inpainting, etc), data types (continuous, discrete, quantized), and domains (medical, environment, finance, speech, signal processing, etc). 
- In terms of novelty, while it is novel to model the score matching loss with RNN latents, it is less novel to combine autoregressive modeling with score-based / diffusion models as many prior papers have worked on this problem and this paper only presents a variant of the loss function. Therefore, the first contribution is questionable.

Regarding the methology:
- This is not a major weakness, but the theoretical results presented in the paper are quite straightforward and do not provide us new understanding of this problem. From a theoretical point of view, training score based models autoregressively is itself an interesting problem and it would be useful to understand properties like model approximation properties, score function uniqueness and existence, robustness to noises of the time series, and so on. I understand that this paper is more of an empirical study, but I think adding theoretical analysis would be a huge plus to the contribution (this is not a request, but just a recommendation).
- The proposed method does not seem to generalize to discrete time series data, which is quite common in practice. Please correct me if I misunderstand.

The experimental results are not strong enough. 
- Regarding data: the datasets are relatively small in size, making it hard to justify the effectiveness of the proposed method in large-scale real world applications. Training score-based models on small datasets seems an overkill and leads to concern about overfitting and mode collapse. However, I do not spot such analysis in the paper. There is also no experiment on large-scale time series data with sample at a scale of least 100K to 1M.
- Regarding time series types: the irregular data is generated with random dropping and may not represent real world cases where the timestamps and intervals can be arbitrary. 
- Regarding tasks, many important applications are missing. As the paper claims unversal time series generation, I would expect to see experiments on more challenging and interesting tasks from signal processing such as speech signal generation.
- The experimental results do not reveal the usefulness of time series data generation. I would expect to see results on how the synthetic data help either in downstream applications (e.g. data augmentation, anomaly detection, adversarial training) or in our understanding of the data structure (e.g. bias, spurious correlations, data manifolds).

### Questions
Please refer to the weakness section.

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
4

### Summary
This work presents score-based generative models for generating time series. The main contribution of this paper is that the authors presented a denoising score matching loss for generating time series. The model has been trained with several time series datasets, and the authors compared their work with various GAN-based time-series generative models.

### Strengths
1. This model presented in this paper works on both regular and irregular time-series generation.
2. Presented denoising score matching loss function which aids in the time series generation process.
3. Extensive comparison on GAN-based time-series generative models.

### Weaknesses
1. On page 4, line 184, the authors claimed, "**Up to our survey, there's no paper about diffusion models considering autoregressiveness in time series generation.**" However, Hoogeboom et al. [1] consider texts and audio synthesis in their work, where an autoregressive diffusion model has been used. Besides that, check out these works [2-4]. Also, can the authors discuss the difference between their method with existing autoregressive models [1, 4]. 

2. The authors did a very comprehensive comparison with different GAN-based architectures, but a comparison with a diffusion-based time series model, e.g., with [4], is needed. However, it's noteworthy that the authors mentioned in the appendix that they considered comparing their work with [2, 3], but due to their "**fundamental mismatch between their model design,**" they could not compare. So, can the authors explain how they can adapt their model for a fair comparison with the existing models [2,3]?

3. Some of the information from the appendix should be in the main section as it explains some situations better, e.g., why the authors did not consider comparing their work with some SOTA diffusion-based models. I feel like this is very important information to keep in the main section of the paper. Perhaps, the authors can move the key information regarding the model comparison in the **Discussion** or **Limitation** section.

4. The paper requires further improvement in writing:
	1. Lacks of coherence between paragraph and/or sentences
	2. Check minor typo
		1. In page 2, line 77, "**in that both both regular.....**"
	3. Try to stick with one table format for all tables, e.g. Table 7,9,10,14 has different format than other tables.

References:

1. Hoogeboom, Emiel, et al. "Autoregressive Diffusion Models." _International Conference on Learning Representations_, 2022
2. Tashiro, Yusuke, et al. "Csdi: Conditional score-based diffusion models for probabilistic time series imputation." _Advances in Neural Information Processing Systems_ 34 (2021): 24804-24816.
3. Rasul, Kashif, et al. "Autoregressive denoising diffusion models for multivariate probabilistic time series forecasting." _International Conference on Machine Learning_. PMLR, 2021.
4. Yuan, Xinyu, and Yan Qiao. "Diffusion-TS: Interpretable Diffusion for General Time Series Generation." _The Twelfth International Conference on Learning Representations_, 2024

### Questions
1. Have the authors run experiments with longer sequence lengths, e.g., more than 1000? Using an RNN-based architecture could potentially limit the model's capability.
2. A common tendency of generative models is to leak training data [1]. Did the authors do any experiments to check if the generative model is leaking any information? 

Reference:

1. Chen, Dingfan, et al. "Gan-leaks: A taxonomy of membership inference attacks against generative models." _Proceedings of the 2020 ACM SIGSAC conference on computer and communications security_. 2020.

### Soundness
2

### Presentation
1

### Contribution
2
