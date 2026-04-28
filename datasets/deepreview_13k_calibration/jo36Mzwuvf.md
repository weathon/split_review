# Gaussian Process-Based Corruption-resilience Forecasting Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
Time series forecasting is challenging due to complex temporal dependencies and unobserved external factors, which can lead to incorrect predictions by even the best forecasting models. Using more training data is one way to improve the accuracy, but this source is often limited. In contrast, we are building on successful denoising approaches for image generation. When a time series is corrupted by the common isotropic Gaussian noise, it yields unnaturally behaving time series. To avoid generating unnaturally behaving time series that do not represent the true error mode in modern forecasting models, we propose to employ Gaussian Processes to generate smoothly-correlated corrupted time series. However, instead of directly corrupting the training data, we propose a joint forecast-corrupt-denoise model to encourage the forecasting model to focus on accurately predicting coarse-grained behavior, while the denoising model focuses on capturing fine-grained behavior. All three parts are interacting via a corruption model which enforces the model to be resilient.
Our extensive experiments demonstrate that our proposed corruption-resilient forecasting approach is able to improve the forecasting accuracy of several state-of-the-art forecasting models as well as several other denoising approaches

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel joint forecast-corrupt-denoise model that consists of the forecasting module and the corrupt-denoising module. The forecasting model focuses on accurately predicting coarse-grained behavior. The corrupt-denoising model focuses on capturing fine-grained behavior, with a GP model employed to enforce the smoothness and co-relationship in added noise. 

Empirical evaluations show the flexibility of the proposed framework in incorporating popular time-series forecasting models such as Informer and Autoformer and exhibit outperformance than popular time-series forecasting models.

### Strengths
1. The idea and framework introduced by the paper are natural and easy to follow. 

2. The proposed framework adds a corrupt-denoising model as a tail of a forecasting model, which shows flexibility to incorporate with existing SOTA methods, and may further enhance their performance

3. The empirical evaluations show benefits of the proposed framework than single forecasting models alone. In addition, evaluations also illustrate the effectiveness of denoising GP corrupted time series than isotropic Gaussian noised time series

### Weaknesses
1.  Despite that the soundness of the methodology makes sense and is easy to follow, there are points remaining unclear more interpretations should be made. For instance, while it is understandable that adding noise through a Gaussian process can result in smoother and more structured noise patterns compared to isotropic Gaussian noise, it is still not that obvious which is worth formal illustrations from either intuitions or equations to explain the difference/benefits between adding isotropic Gaussian noise. Specifically, the paper lacks a clear explanation of why the GP-generated noise is beneficial beyond a qualitative description of smoothness. A more rigorous analysis, perhaps through spectral analysis or by demonstrating how the GP's kernel function influences the noise structure and its impact on the denoising process, would be valuable. The paper should also clarify how the GP's hyperparameters are chosen and how they affect the performance of the model.

2. The effectiveness of the proposed framework is marginal when considering the framework doubles the parameter of a single forecasting model, e.g., the denoising model follows the forecasting model's architecture. In this case, it is also worthwhile showing that the benefits of the proposed framework are indeed by its mechanism, instead of overparameterization for better capability with a stack of Informers for example. The paper needs to provide a more thorough analysis of the computational cost and parameter efficiency of the proposed framework. It should compare the performance gains against the increased computational burden and parameter count. A comparison with a single forecasting model with a similar number of parameters would help to isolate the benefits of the proposed mechanism from the effect of overparameterization.

3. The ablation study is not well-exhibited. Despite there being a simple ablation study for the synthetic data in the Introduction, we expect to see some real-world examples or case studies to prove the statement 'The forecasting model focuses on accurately predicting coarse-grained behavior. The corrupt-denoising model focuses on capturing fine-grained behavior, with a GP model employed to enforce the smoothness and co-relationship in added noise', rather than simply the synthetic data. The paper should include a more detailed ablation study on real-world datasets, demonstrating the individual contributions of the forecasting and denoising modules. This should include visualizations of the coarse-grained forecasts, the added noise, and the final denoised output, to clearly illustrate the roles of each component. The study should also explore the impact of different GP kernels and their parameters on the final performance.

4. The presentation needs to be improved. For example, there are repeated results in Table 1 and Table 2, which should be merged. And if MSE is the only metric used for evaluation, why is it necessary to assign it a column in all tables

### Questions
1. For results on DLinear, DeepAR, and ARIMA, why the reported variances are zeros?

2. Is the reported error, or ground truth normalized?

3. Does adding the denoising part to the forecasting model help or harm the convergence?

4. Does adding the denoising part to the forecasting model tend to lead to overfitting than the direct output of the forecasting model, say fine-grained behavior found by the denoising model overfits the ground truth when the ground truth is smooth? It might be measurable by case study or by using correlation metrics.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the topic of noise corruption in modeling time-series data for forecasting. The authors propose that the noise/error in the time series data can be attributed to two sources, including a temporally correlated source, and an independent noise. From that the authors claim the current methods cannot well recover the underlying signals/true observations and thereby cannot carry out accurate forecast. To this end, the authors proposed a joint-corrupt-denoise model to capture the characteristics of signals from both sources identified. The framework is then tested on a wide range of datasets from which its efficacy is demonstrated.

### Strengths
1. The motivation of the problem is laid out very clearly, with an illustration well explaining the origin of the issue and the shortcomings of the current methods.
2. The proposed metholodgy is explained very clearly and a thorough and comprehensive numerical study is carried out to evaluate the method.

### Weaknesses
1. I have concerns that the proposed framework including the temporally-correlated term utilizing Gaussian process is entirely new. I think there might have been other works out there proposing a fairly similar idea called "calibration modeling". To elaborate a bit more here, the framework proposed carry some common components to a typical statistical calibration model as follows:
$y(t) = x(t) + \delta(t) + \epsilon(t)$,
where $x(t)$ is the true signal, $\delta(t)$ is modeled by a Gaussian process, and $\epsilon(t)$ modeled by a Gaussian noise.
With an appropriate selection of the prior distributions for the parameters and hyperparameters, this can be tackled by a Bayesian approach. I will elaborate further in the Q section.
2. The presentation of the manuscript can be further improved. For example, in the abstract, I find the mentioning of "using more training data" and "image generation" not necessarily closely related to the point I think the authors were trying to emphasize. Additionally, in Figure 2, $X_1$ and $X_2$ are defined as covariates, which seem to conflict with the previos reference to $X$ as the observations.

### Questions
Let me further expand on the proposed framework itself. I believe the joint framework is quite novel and has clear potential in improving time series forecasting, as demonstrated by the authors very diligently. However, I do wonder whether the authors would be open to compare and evaluate the framework to the calibration model that I mentioned above.
My personal belief is they share some commonality between them in how they model the time-correlated noise/signal, but it seems the two objectives functions are still quite different. So I believe it would be interesting to see how they compare both in their model structure, and their performance on a few datasets in practice.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a time-series forecasting module which can be applied to a wide-range of existing models. The main idea is denoising: the output of an already available forecasting model is corrupted by noise (the authors show the significance of correlated rather than i.i.d. noise) which is then passed through the same forecasting model (but with different parameters) again. The authors argue such an architecture "encourages the initial forecasting model to focus on modelling coarse-grained behavior, and a denoising model that corrects the fine-grained details". The proposed module is experimentally shown to improve the forecasting performance of a number of existing forecasting models.

### Strengths
+ An interesting idea combining the image denoising ideas with the time-series forecasting
+ Extensive experimental evaluation including the ablation study

### Weaknesses
 - A somewhat confusing presentation of the proposed method (see the questions below)
- Lack of examples of the model forecasts apart from the cartoon in Fig. 1
- Minor grammatical errors and repetitions (e.g. almost the same sentence appears twice in Section 2.2.)

I have conflicting opinions about this paper. On the one hand, the experimental results look really good: the proposed denoising module noticeably improves the performance of the exiting models. On the other, I struggle to understand why it is the case, why adding noise improves the performance. In the image generation literature, denoising is often used as a tool for regularising the low-dimensional latent space which is used for sampling new images. However, it is clearly not the case in the context of time-series forecasting. I appreciate that the authors provided some intuition (e.g. see the quote in the Summary section of this review) but I would also appreciate further comments from the authors on this matter. I would be happy to increase my rating if the authors clarify some of these questions.

### Questions
- Why does the AutoDWC baseline (i.e. denoising without corruption) works worse than the noise corrupted model? Shouldn't adding independent (from the forecasting model prediction) noise make the task harder for the denoiser and thus deteriorate the performance?
- The isotropic noise baseline (AutoDI) performs similarly to the AutoDWC. Why do you think it is the case? Also how did you choose the variance of the isotropic noise?
- What is the input to the denoising model? Only the corrupted forecast, or the corrupted forecast and the historical time-series trajectory (from t_0-k to t_0) used to compute the forecast?
- Did you try different values of \lambda in Eq. (2)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors claim to have introduced a joint forecast-corrupt-denoise model. The output of the baseline forecasting model, for instance, a machine learning (ML) algorithm, is corrupted by a noise function following a GP distribution. Once data have been corrupted, a denoising model is deployed to reverse the corruption process, while seeking to improve the initial forecast output. Both parameters of the forecast and GP models are jointly learned via the minimization of a compound (forecast + GP-ELBO) loss function.

The authors also claim that their framework provides better results than the baseline forecasting models. To prove this, they have considered several experimental setups.

### Strengths
Under Gaussian assumptions, the consideration of a GP-based corruption process may be seen as an interesting idea for dealing with non-i.i.d. noise. Based on [16], an adapted compound loss function is proposed in the (forecasting and GP) parameter estimation. Python codes are provided.

### Weaknesses
 - In my opinion, the contributions in the paper are minor. The authors have only adapted a collection of well-known approaches related to forecasting, GP and denoising models to establish their joint forecast-corrupt-denoise framework.
- Contrary to the authors' claims, the numerical results are not convincing. In many cases, the best results are not properly highlighted or are unclear since only 3 random replicates have been considered. For instance, in Table 4 (Traffic 48), InfoDWC (and possibly InfoDI) provides a better result than InfoDG (the proposed method). I suggest considering more replicates when constructing the tables to obtain more consistent results.
- There is no theoretical evidence (certification) to explain why the joint model should perform better than the baseline algorithms.
- Mathematical formulas are not defined correctly and, in some cases, are inconsistent. For instance, formulas related to GPs.
- The paper seems a bit rushed.

I will refer to the part **Questions** for further details.

### Questions
- According to Section 2.5, the GP-based corruption model is trained considering the ground truth $Y$ (data to forecast). Does it mean that the proposed joint model can be used only when $Y$ is known? If so, I don't see the point of setting up the problem as a forecast one instead of including $Y$ in the training dataset. If $Y$ is unknown (forecast context), how can the GP parameters be tuned?
- Can the authors explain the need to include two metrics (MSE and MAE) in the experimental setups? Since both metrics seek to assess the quality of predictions, the results are redundant. Consequently, half of the tables can be omitted.
- In the experimental setups, only 3 random replicates have been considered. Can the authors confirm that results are indeed consistent (i.e. that similar results are obtained for another triple of random replicates)? If not, they should consider a (statistically rich) number of random replicates (e.g. 10, 20, 30...). 
- Page 8, Section 3.3: can the authors give further details on the choices (e.g. $\beta_1 = 0.9$, $\beta = 0.98$, and batch size = 256) considered in the numerical implementations? 
- On page 1, Section 1, the authors suggest that their approach may be adapted to deal with multivariate transient functions but that their focus was on the univariate case. Have they performed numerical examples involving multivariate functions? In any case, can they provide further details on the scalability (in terms of the input dimension) of the framework?

**Other minor remarks**
- To cite references in brackets, e.g. [n], to avoid confusion when referring to equations (n).
- Page 1, Section 1 (Time series forecasting task): the definitions of $X$ and $Y$ are not clear. $\kappa$ is defined as the number of time-series observations prior to $t_0$, i.e. it defines a set of time instants $\{t_{-\kappa}, \ldots, t_{-1}\}$. Then $X$ needs to be defined as $\{x_t; \gamma_t\}_{t = t_0 - t_{-\kappa}}^{t_{-1}}$. A similar reasoning must be done for $Y = \{x_t; \gamma_t\}_{t = t_0}^{t_0 + t_\tau}$. 
- Page 2, related works: LSTM is not defined.
- Page 3, 2nd paragraph: "navive"
- Page 3, Section 2.1: $\tilde{X}| X \sim \mathcal{N}(\textbf{0}, \sigma^2  \textbf{I})$ ($\sigma^2$ is missing)
- Tables are not placed just before or after their citation. For instance, Tables 1, 2 and 3 are placed on pages 4, 6 and 7 (respectively) but they are cited on page 8.
- Page 4, Eq. (1): the authors have defined $c$ as a function (since it is considered as a GP) but it is treated as a (Gaussian) vector. They need to be consistent with the definitions and distinguish them correctly throughout the paper. 
- Punctuation marks in the equations need to be double-checked throughout the paper.
- To refer to GP everywhere once the abbreviation is introduced.
- Page 7, Section 3.1: footnotes 2, 3 and 4 are not provided. If the authors refer to references [2,3,4], they need to be cited properly.
- Reference 24: incompleted.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
