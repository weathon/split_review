# Transformer-Modulated Diffusion Models for Probabilistic Multivariate  Time Series Forecasting

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
Transformers have gained widespread usage in multivariate time series (MTS) forecasting, delivering impressive performance. Nonetheless, these existing transformer-based methods often neglect an essential aspect: the incorporation of uncertainty into the predicted series, which holds significant value in decision-making. In this paper, we introduce a Transformer-Modulated Diffusion Model (TMDM), uniting conditional diffusion generative process with transformers into a unified framework to enable precise distribution forecasting for MTS. TMDM harnesses the power of transformers to extract essential insights from historical time series data. This information is then utilized as prior knowledge, capturing covariate-dependence in both the forward and reverse processes within the diffusion model. Furthermore, we seamlessly integrate well-designed transformer-based forecasting methods into TMDM to enhance its overall performance. Additionally, we introduce two novel metrics for evaluating uncertainty estimation performance. Through extensive experiments on six datasets using four evaluation metrics, we establish the effectiveness of TMDM in probabilistic MTS forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce a Transformer-Modulated Diffusion Model (TMDM), uniting conditional diffusion generative process with transformers into a unified framework to enable precise distribution forecasting for MTS. Extensive experiments are conducted

### Strengths
1. This paper is well-presented and well-organized.
2. The paper introduces a Transformer-Modulated Diffusion Model (TMDM), uniting conditional diffusion generative process with transformers into a unified framework to enable precise distribution forecasting for MTS. 
3. Extensive experiments are conducted

### Weaknesses
1. This paper states many existing work did not consider the uncertainty of data, but more SOTA should be compared and considers like cST-ML which tries to capture traffic dynamics with VAE. Please provide detailed explanations or experiments accordingly.
2. If the time-series data is in different granularities, does this model still work?

### Questions
Please address the questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of probabilistic time series
forecasting. The authors propose a conditional diffusion
process that convex combines the point estimate from
a transformer model with the noise of the diffusion process.
In experiments on 6 datasets they show that their approach
outperforms state-of-the-art baselines.

### Strengths
s1. generic approach that will work with any point estimate model.
s2. consistently good results against several strong baselines.
s3. ablation studies demonstrate the impact of different components
  as well as the ability to wrap different point models.

### Weaknesses
w1. the results for CRPS_sum of the baselines (appendix, tab. 6)
  varies from the published results.
- e.g., tab. 6 reports CRPS_sum 3.92 on Exchange for TimeGrad,
  but the TimeGrad paper reports 0.006.
  your tab. 6 reports CRPS_sum 4.54 on Electricity for CSDI,
  but the CSDI paper reports 0.017.
- I think these differences need to be clearly explained, likely
  due to different experimental conditions?
  If so, it would be convincing to reproduce the experiments
  of the strongest baseline papers and compare them on
  the published settings, too.

### Questions
The paper proposes a generic approach to wrap a diffusion
model around any point estimate model for time series
forecasting to make it probabilistic (s1). Most of the results
shown in tab. 2 are pronounced improvements and almost
all but the very last are consistently better than several
strong baselines (s2). Due to the ablation studies one can
clearly see the impact of different modelling choices (s3).

I only would like to discuss one point:
w1. the results for CRPS_sum of the baselines (appendix, tab. 6)
  varies from the published results.
- e.g., tab. 6 reports CRPS_sum 3.92 on Exchange for TimeGrad,
  but the TimeGrad paper reports 0.006.
  your tab. 6 reports CRPS_sum 4.54 on Electricity for CSDI,
  but the CSDI paper reports 0.017.
- I think these differences need to be clearly explained, likely
  due to different experimental conditions?
  If so, it would be convincing to reproduce the experiments
  of the strongest baseline papers and compare them on
  the published settings, too.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes a method for multivariate time series forecasting. It utilises the (conditional) diffusion model, while starts from a "condition" which is from the output of a Transformer based model.  The advances of the proposed model is measured with (mainly) QICE and CRPS. MSE and MAE, as well as some qualitative results are also provided to show the effectiveness of the method.

### Strengths
Inspired by the conditional diffusion process for multivariate regression from Han et al. (2022), the manuscript proposes the conditional diffusion process for multivariate time series forecasting.
To the best of my understanding, the core contribution of the manuscript is to use the "condition" from a Transformer for the diffusion model, while both the Transformer and conditional diffusion model are from the literature.  

The manuscript is overall clearly written and easy to read. Some of the missing details are listed in Questions.

The proposed method for probabilistic multivariate time series forecasting has the potential to contribute to the community.

### Weaknesses
- The manuscript does not successfully highlight its contribution. Since both components of TMDM are from the literature, it is necessary to highlight why this is not trivial. In particular, the use of a Transformer to generate the "condition" for the diffusion model, while both models are known, needs further justification. The authors should elaborate on the specific challenges and novel aspects of integrating these two components. The claim that the proposed method is non-trivial should be supported by a more in-depth discussion of the technical hurdles overcome in combining the Transformer and diffusion models effectively. In my humble opinion, the 3rd contribution is quite weak, as both metrics are from existing works.

- There are also other works that employs a Transformer and a probabilistic model for time series modelling. e.g., Transformer + Probabilistic Circuit is proposed in [1] for time series forecasting, and uncertainty estimation (similar to Fig. 2 in the manuscript) is provided. A discussion with such works might help to stress the novelty and contribution of the manuscript. Specifically, the authors should compare and contrast their approach with existing methods that combine Transformers with probabilistic models, highlighting the unique aspects of TMDM. This comparison should not be limited to Predictive Whittle networks [1] but should also include other relevant works in the field.

- The generation of the conditional representation $\hat{y}_{0:M}$ is not clear to me. Some details are omitted from eq(9) to eq(10). Specifically, the transition from the sampled $z$ to the conditional representation $\hat{y}_{0:M}$ needs further explanation. The role of the neural networks $\tilde{\mu}_z$, $\tilde{\sigma}_z$, and $\mu_z$ in this process should be clarified. Additionally, the dimensionality of $z$ and whether it is a scalar or a vector in eq(10) needs to be explicitly stated.

- The references are not up-to-date, many arXiv versions are already published.

### Questions
- can you provide more details on generating  $\hat{y}_{0:M}$? What is the dimension of $z$? As in eq(10), is $z$ a scalar? How are the NNs for $\tilde{\mu}_z$, $\tilde{\sigma}_z$ and $\mu_z$ formulated?

- How $\mu_z(z)$ differs from $\mathcal{T}(x_{0:N})$? What happens if the NNs are omitted and $\mathcal{N}(\mathcal{T}(x_{0:N}), \mathbf{I})$ is used instead of $\mathcal{N}(\mu_z(z), \mathbf{I})$?

 - $f(x_{0:N})$ is in $\mathbb{R}^C$ in introduction but $x_t$ and $y_t$ are in  $\mathbb{R}^d$. Does $C=d$ hold?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
