# Physics-Informed Autoencoder for Enhancing Data Quality to Improve the Forecasting Reliability of Carbon Dioxide Emissions from Agricultural Fields

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Missing values in measurements for carbon dioxide emissions on drained peatlands remains an open challenge for training forecasting techniques to achieve net zero. Existing methods struggle to model $\ce{CO_2}$ emissions to fill gaps at the field scale, especially in nighttime measurements. We propose novel Physics-Informed Autoencoders (PIAEs) for stochastic differential equations (SDEs), which combine the generative capabilities of Autoencoders with the reliability of physical models of Net Ecosystem Exchange (NEE) that quantify $\ce{CO_2}$ exchanges between the atmosphere and major carbon pools. Our method integrates an SDE describing the changes in NEE and associated uncertainties to fill gaps in the NEE measurements from eddy covariance (EC) flux towers. We define this SDE as a Wiener process with a deterministic drift term based on day and night time NEE physics models, and stochastic noise term. In the PIAE model, various sensor measurements are encoded into the latent space, and a set of deterministic decoders approximate the SDE parameters, and a probabilistic decoder predicts noise term. These are then used to predict the drift in NEE and thereby the optimal NEE forecast at the next time instance using the SDE. Finally, we use a loss function as a weighted sum of the Mean Squared Error (MSE) and Maximum Mean Discrepancy (MMD) between the measurements and the reconstructed samples and the associated noise and drift. PIAE outperforms the current state-of-the-art Random Forest Robust on predicting nighttime NEE measurements on various distribution-based and data-fitting metrics. We present a significant improvement in capturing temporal trends in the NEE at daily, weekly, monthly and quarterly scales.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Physics-Informed Autoencoders (PIAEs) to address gaps in CO2 emission measurements from agricultural fields. The method combines autoencoder architectures with physical Net Ecosystem Exchange (NEE) models, integrating equations that describe CO2 exchanges between the atmosphere and carbon pools (i.e., utilizing
the SDE defined as a Wiener process). Their main contribution is extending standard autoencoders with a stochastic differential equation framework that models NEE changes over time, particularly addressing nighttime measurement gaps. Their method also provides forecasting capabilities and enhances performance on NEE gap-filling by accurately learning the NEE distribution and associated parameters. They evaluate their approach on 8 years of flux tower data from East Anglia, showing improvements over current state-of-the-art methods, especially for nighttime predictions, where they achieve a 22% higher R2 score than Random Forest approaches.

### Strengths
1. Introducing a stochastic differential equation for NEE measurements combining daytime
and nighttime models with Gaussian noise.
2. Demonstrating that PIAE improves gap-filling robustness compared to state-of-the-art
methods, handling gaps from months to years.
3. Better Maximum Mean Discrepancy (MMD), Wasserstein distance, and Kullback-Leibler (KL) divergence validated significant improvements in NEE distribution learning.
4. Achieving better fit to NEE measurements validated by lower MAE and higher R2 scores.
5. Accurately predicting SDE parameters, enhancing interpretability.
6. Consistent improvement in nighttime predictions across metrics
7. Strong performance on distribution-based measures (MMD, Wasserstein, KL)
8. Ability to capture unusual events (e.g., downward NEE spikes)
9. Effective parameter estimation for both day and night models

### Weaknesses
1. While the supplementary material adequately explains the SDE derivation and diffusion coefficient determination, key points should be summarized in the main text. A brief note about how σnight and σday are derived from empirical error distributions would help readers understand the transition from Eq. 5 to 6 without requiring supplementary material consultation
2. AE is better than PIAE for all model parameter estimation across all metrics, contrary to their claim that their method enhances performance on NEE gap-filling by accurately learning the NEE distribution and associated parameters.
3. The computational requirements compared to simpler approaches like RF are not discussed. 
4. The two-phase training procedure (MSE then MMD) has no convergence guarantees.
5. The claimed 22% improvement in R2 score lacks context - no variance was reported (Error bars or confidence intervals for the reported metrics would help). The hyperparameter selection process for PIAE and baseline models (including random forest) is not described. A fair comparison requires careful tuning of all methods.
6. Missing critical details:
    1. How were hyperparameters selected for PIAE and baselines?
    2. What are the network architectures (layer sizes, activation functions)?
    3. Where are the error bars and statistical significance tests?
    4. How does computational cost compare to simpler methods
7. The implementation details are insufficient for the reproduction
8. The comparisons in Figures 2 and 3 show selective periods without justification for their choice

Minor comments:
1. Section 4.5's description of the loss function uses inconsistent notation compared to earlier sections. 
2. There are some writing clarity issues, like in lines 50 and 98.
3. The paper shows results across different timescales but doesn't systematically evaluate performance as a function of gap length. This would be valuable for understanding the method's practical utility.
4. The NEE parameter estimation details might fit better in methods

### Questions
1. The SDE formulation in Section 3.2 assumes specific forms for the drift and diffusion terms. The justification for these choices comes from prior work, but the implications of these modeling choices should be discussed. What happens when these assumptions are violated?
2. The two-phase training procedure using MSE then MMD requires more theoretical grounding:
    1. Why this specific sequence? How is convergence of the first phase determined before switching to MMD?
    2. Were other training strategies considered?
3. The choice of MMD kernels isn't discussed - how sensitive is the method to this choice?
4. How sensitive is the model to SDE parameter initialization?
5. What's the computational overhead versus RF/XGBoost?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies the application of autoencoders for the problem of imputing missing values in Co2 Net Ecosystem Exchange (NEE) measurements. The autoencoder takes in several covariates, such as temperatures and radiations, at a given timestep $t$ and predicts the next-step NEE, along with several variables of a Stochastic Differential Equation that models changes in NEE.

### Strengths
1. The paper applies ML techniques to enhance NEE measurements, which has the potential to improve the estimation of Co2 emissions, resulting in reduced uncertainty in our projections. **This is an important problem with high societal and environmental impact.**

### Weaknesses
1.  **The presentation of the paper is convoluted, and requires a degree of familiarity with the NEE problem that is uncommon in the ICLR community**. It is then hard for me to judge the significance, originality and potential impact of the work.
 More precisely, these are some points that are not sufficiently explained or that make the paper hard to read and understand:
- In the introduction, it is mentioned that missing NEE values are due to e.g. power shortages. I assume that in such scenarios, the values of the covariates (temperature, radiation, etc) are also missing due to the same issue. However, the proposed model requires having access to all covariate values at a given time. How can the model be applied in practice without these values?
- In the introduction, the first highlighted contribution is the introduction of a SDE for NEE measurements. Put it that way, it sounds like the SDE is novel also in the physics. However this point is not stressed again later on, so I wonder whether the SDE is known and the novelty is in its use as supervision for learning ML models.
- Line 157, it is mentioned that the $E_0$ parameter is estimated with the nighttime model and used in the daytime one, but it is not explained why.
- In section 4.4, it is mentioned that the integration of the SDE in the training of the autoencoder follows previous work [Raissi 2017], but it is not sufficiently described to make the paper self-contained. It is unclear how the SDE is incorporated into the loss function or the network architecture. Is it used as a regularization term, or is it directly integrated into the network's forward pass? The description lacks the necessary detail to understand the implementation.
- The related work is not sufficiently described. In particular, it is not clear whether the reported baselines RFR and XgBoost variant based on the work of [Moffat 2007] are also physics-informed or only statistical. It is crucial to understand if these baselines also incorporate domain knowledge or if they are purely data-driven models. This distinction is important for evaluating the novelty and contribution of the proposed method.
- Second and third lines of Equation 5: do the second (from the left) commas separate two different definitions or do they indicate the continuation of the variable suffices?

2. The tables do not report standard errors, which makes impossible to judge the significance of the improvements.

3. The paper does not discuss limitations nor future work.

### Questions
1. Could the work be applied to other physical systems? Would that require knowledge of the DFE governing the system?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses the problem of forecasting CO2 emission from agricultural fields based on measurement data. In particular, the problem of predicting missing data is addressed. The authors present a set of stochastic differential equations that govern the net ecosystem exchange (NEE) that are used in a physics-informed autoencoder for data imputation.

### Strengths
The proposed method seems a good fit to the application.

### Weaknesses
The paper was challenging to follow, primarily due to unclear notation and insufficient definitions of certain terms. Additionally, some design choices, such as the two-phase loss, are described but lack clear justification.

The main contribution appears to be a relatively straightforward application of an existing methodology to a specific domain. The novelty largely lies in application-specific details, which may not align closely with the primary interests of the ICLR community.

### Questions
Why is latent heat (L) excluded? Having a high correlation to the target variable would seem to be a good thing when the goal is to predict missing values?

The notation in equation 4-5 is difficult to read. Would it not be more clear to write this in terms of partial derivatives?

For improved readability, consider to use italics for variables and roman (upright) type for named functions, as subscripts in equations, and for units of measurement. Consider that multi-letter abbreviations can be confusing in equations: For example, it can be unclear if rb is a single variable or the product of r and b.

rb (night/day) is not defined in the main text as far as I can see. rb is mentioned in the text in the appendix but not in the mathematical derivations.

In equation 9, should is there not a difference between dt on the left and right hand side? On the left hand side, it seems to denote an infinitessimal element, and on the right side it is 30 minutes?

I am not sure how this approach is an autoencoder. As I understand the written description, the model predicts one timestep ahead with a latent encoding, and thus does forecasting rather than reconstruction. However, Figure 1 does seem to imply that the decoders predict for the same timestep.

Is there something wrong with the linebreaks in Algorithm 1, step 4?

What is the reason for the choice of the two loss phases?

I am not familiar with the literature on physics-informed autoencoders, but I would like to ask whether this paper introduces any technical contributions to the framework itself, or if the contribution is primarily the application of an existing modeling framework to significant applications.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this study, the authors utilized physics-informed neural network framework (PINN) to develop an auto-encoder for the forecasting of carbon dioxide emission. First, the overall physical process is modeled by using a set of ordinary differential equations and PINN is used to train a neural network. The authors proposed a two-stage training method, that in the first stage the neural network is trained by minimizing the mean absolute error and, then, in the second phase, the maximum mean discrepancy score is minimized. It is shown that the proposed method outperforms some of the naive baselines.

### Strengths
It is shown that the proposed method outperformed some of the baseline methods that are used in the domain. It seems to suggest a potential of replacing the conventional machine learning models with the PINN models.

### Weaknesses
First of all, the study is mainly focused on the application of the widely used PINN to a physical process for a specific domain. It does not look like there are novel algorithms or problem setups that can be of interest to a broader machine learning community. I would like to suggest the authors to submit this manuscript to a more domain specific venue.

The paper is not very well written. It is unclear how the SDE formulation is treated in the modeling, how the SDE and model are used for uncertainty quantification, how the evaluations were made by using what variables as inputs and predict how long in the future, and so on. I assume that this is due to the page limitation. It would have been better if the authors had put all the domain specific modeling sections in the appendix and focused more  on the generic problem set up in the main body.

The use of MMD seems a little bit odd. MMD is essentially a two-sample statistical test to identify of those samples are from the same probability distribution. We usually expect the two samples are from two independent realizations. But, based on the loss function, two samples are from the same realization, just one is the data and the other is a model prediction. If they are from the same realization ($\omega^j$ in author's notation), minimizing the distance would make more sense, like the first phase of the training. In the end of day, for two samples from the same realization, minimizing MMD corresponds to minimizing MSE. But, all the hyperparameters (like the RBF kernel) makes it much less straightforward.

### Questions
The use of MMD seems a little bit odd. MMD is essentially a two-sample statistical test to identify of those samples are from the same probability distribution. We usually expect the two samples are from two independent realizations. But, based on the loss function, two samples are from the same realization, just one is the data and the other is a model prediction. If they are from the same realization ($\omega^j$ in author's notation), minimizing the distance would make more sense, like the first phase of the training. In the end of day, for two samples from the same realization, minimizing MMD corresponds to minimizing MSE. But, all the hyperparameters (like the RBF kernel) makes it much less straightforward.

### Soundness
3

### Presentation
2

### Contribution
1
