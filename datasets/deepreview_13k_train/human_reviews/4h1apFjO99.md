# Diffusion-TS: Interpretable Diffusion for General Time Series Generation

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Denoising diffusion probabilistic models (DDPMs) are becoming the leading paradigm for generative models. It has recently shown breakthroughs in audio synthesis, time series imputation and forecasting. In this paper, we propose Diffusion-TS, a novel diffusion-based framework that generates multivariate time series samples of high quality by using an encoder-decoder transformer with disentangled temporal representations, in which the decomposition technique guides Diffusion-TS to capture the semantic meaning of time series while transformers mine detailed sequential information from the noisy model input. Different from existing diffusion-based approaches, we train the model to directly reconstruct the sample instead of the noise in each diffusion step, combining a Fourier-based loss term. Diffusion-TS is expected to generate time series satisfying both interpretablity and realness. In addition, it is shown that the proposed Diffusion-TS can be easily extended to conditional generation tasks, such as forecasting and imputation, without any model changes. This also motivates us to further explore the performance of Diffusion-TS under irregular settings. Finally, through qualitative and quantitative experiments, results show that Diffusion-TS achieves the state-of-the-art results on various realistic analyses of time series.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A transformer based denoising diffusion probabilistic model, Diffusion-TS, is proposed for generating multivariate time series. 
Representations from Oreshkin 2020, Desai 2021, De Livera 2011 and Woo 2022 are adopted for trend and seasonality. Under time series model (1) and Fourier-based loss term following similar work as Ho 2020 and Fons 2022, the \hat{x}_{0} is estimated directly for unconditional time series. 
The proposed method Diffusion-TS is compared with four other models TimeGAN 2019, TimeVAE 2021, Diffwave 2021, and Cot-Gan 2020 under 6 datasets (stock price, electricity transformer, etc. The proposed method works better than the other four methods most frequently under the evaluation rules suggested by Yoon 2019, Paul 2022 and Ni 2020 especially under high-dimensional datasets.
Extension to conditional model by adding gradients, as well as simulation results, are presented.

### Strengths
This idea and algorithm of the proposed method are generally well presented. It’s compared with multiple recent time series generation methods and simulation results outperform these in most cases.

### Weaknesses
Potentially the proposed method works well or even better than other existing methods under typical seasonal time series data. Pending further exploration/confirmation how well the performance the proposed method can be under times series of real data with different unique features like big jump in stock price. Also wondering the hyper-parameter selection impact on the result and convergence speed.

### Questions
P4, Please define similarly as in Woo (2022) your \omega_seas or at least add definition by English. 
P4, Equation (4), please either split the A and \Phi definition in two rows or write as a vector, so would not be confused as compound operators. 
P5, Could you clarify the Figure 2, ‘Decoder Block 1’, ..., ‘Decoder Block N’ each refers to under the N samples (i=1, ... ,N) of time-series signals on P2 or something else considering the squares/arrows in that figure. 
P17, Can the dataset names or links be more specific? There’re multiple datasets available under some links.  
P6 and P18, Not questioning the vitality of your result, just want to have a better understanding of the performance to be expected under your method for other potential new runs: 
How different Table 1 results can be if you did try other hyper-parameters?    
Prediction under jump model can be hard. How well the performance of your model can be when there’s big jump in observed data? (The Google stock data used is from 2004 to 2019, the big changes in 2020 and 2022 not included. The electricity transformer temperature and blood oxygen related data might be typical stable time series. I’m not familiar with MujoCo data.)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a diffusion model for time series generation. The model involves a custom architecture with components that help synthesizing the trend and seasonal components of the time series. The model is trained to directly estimate the observation from arbitrary diffusion steps. The objective function of the diffusion model is also modified to incorporate a loss based on fourier transform of the time series. Experiments show improved performance over existing generative models in terms of different generative metrics.

### Strengths
- The model explores both unconditional and conditional generation using a single model.
- The model performs better than baseline models in terms of time series generation.

### Weaknesses
 - The claim "little attention has been given to leveraging the powerful generative ability for general time series production" is not entirely correct. See [1] and [2], for example. Furthermore, in the light of [2], the claim "... **first** DDPM-based framework for both unconditional and conditional time series synthesis" is not correct either. [2] proposes a self-guidance mechanism to use unconditional diffusion models for conditional time series tasks and also studies the unconditional generative properties of the model. This limits the novelty of the paper and Sec. 3.4, in particular.
- The paper is poorly written and does not tell a coherent story. Sec. 3.2 reads like an arbitrary combination of ideas. The individual components are also not analyzed later via ablations. The manuscript also has many typographical errors (synthetic instead of synthesis, DSDI instead of CSDI).
- The evaluation on the conditional tasks is limited. The model is only compared against Diffwave and CSDI (which is fairly close to Diffwave) and baselines from time series forecasting literature are missing. It is also unclear how these CSDI and Diffwave baselines were trained. The lack of comparison with more established time series models makes it difficult to assess the practical relevance of the proposed approach for conditional generation tasks. Furthermore, the choice of Diffwave as a baseline is questionable given its design for audio data, which has different characteristics than typical time series data, especially multivariate time series.

### Questions
- What is the empirical significance of the trend & seasonality synthesis blocks and the fourier regularization? Did the authors conduct ablations for these components? (Check the results in [1] which doesn't use any of these components)
- Why does Diffwave perform so much worse in the case of long time series generation? The sequence lengths considered in this work are smaller than those used in audio synthesis. Is it possible that there is a bug in the experiments setup? 
    - Why did not authors not compare against a CSDI-like model for unconditional generation? That would probably be a better comparison and ablation for the components proposed in this work. 

[1] Lim, Haksoo, et al. "Regular Time-series Generation using SGM." arXiv preprint arXiv:2301.08518 (2023).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose Diffusion-TS, a diffusion method for multivariate time series generation. The method involves an interpretable decomposition into trend and seasonality components. The diffusion model is trained using a joint L2 and Fourier loss, and the authors apply conditional generation techniques to apply the method to forecasting and imputation directly without changes in the model. Experiments show Diffusion-TS achieves state-of-the-art performance on time series datasets, including in an irregularly sampled setting.

### Strengths
Originality:
- As far as the reviewer is aware, the authors are the first to combine a trend-seasonality decomposition technique with diffusion for time series generation. The authors mention this choice leads to improved performance across the various evaluation metrics.

Quality:
- The experiments are generally well-constructed. A variety of datasets and evaluation metrics are used for standard unconditional generation, and several ablation studies are included in the appendix.
- The authors show qualitative results showing the trend and seasonality components predicted by the model generally behave as intended.

Clarity:
- The paper is generally well-written, and the experiments are described clearly.

Significance:
- The experimental results are quite compelling. In the unconditional time series generation settings (Table 1), Diffusion-TS outperforms existing methods. The performance gap is especially clear for higher-dimensional datasets and long-term generation (Table 2).

### Weaknesses
 - Generally, it's a bit unclear to the reviewer which design choices are crucial to the improvement in performance, especially the trend-seasonality decomposition. Two detailed techniques are involved in implementing the decomposition, the polynomial regressor and the Fourier synthetic layers, but it's unclear to what extent these techniques contribute to the model performance. It is not clear if the performance gain is due to the specific parameterization of the trend and seasonality components, or simply the inductive bias of disentangling the time series into these components. Further, the interaction between these two components and the diffusion process is not well-defined.
- It's a bit unclear how compelling the qualitative results are. For example, in Figure 3, the trend components seem quite uninformative compared to the season/error components. The trend component appears to be a very smooth curve, which may not capture complex trend dynamics. In Figure 4, it's unclear whether the t-SNE visualizations support the claim that the Diffusion-TS distribution better aligns with the data distribution than TimeGAN distribution. The t-SNE plots do not show a clear separation or clustering that would definitively support this claim, and the visual assessment is subjective.
- Experimental metrics reported are inconsistent. For example, correlational and context-FID scores are reported in Table 2, and discriminative and predictive scores are reported in Figure 7 and Appendix C.1/C.2. This makes it difficult to compare the performance of the model across different tasks and datasets. It is also unclear why certain metrics were chosen for specific experiments and not others.

### Questions
Main:
- In Appendix C.2, what is the "w/o interpretability" model? Is this equivalent to $x_0(x_t, t, \theta) = R$ in Eqn 7, setting the $V_{tr}^t$ and $S_{i, t}$ terms to $0$? How crucial are the polynomial regressor and Fourier synthetic layer techniques?
- How well does the trend-seasonality decomposition method of Diffusion-TS achieve what's intended for the toy model (Eqn 1), for example on synthetic data?
- How do discriminative and predictive scores compare on the long-term time series generation task (Table 2)?
- For the long-term generation task (Table 2), why is it that Diffusion-TS seems to perform generally better with longer time series? It seems like longer time series generation should be a more difficult task.
- In Figure 6, is MAE computed only over missing data (imputation targets) or over the full time series including existing data? For Diffusion-TS-G, since a soft constraint is used to enforce the conditional generation, how closely do the generated time series for imputation/forecasting match the existing data?
- How does the number of parameters compare between Diffusion-TS and its competitors?

Clarifications:
- How is the data in Figure 3 generated? Is column b the ground truth and column a the result of adding noise?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
