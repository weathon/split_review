# KooNPro: A Variance-Aware Koopman Probabilistic Model Enhanced by Neural Processes for Time Series Forecasting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
The probabilistic forecasting of time series is a well-recognized challenge, particularly in disentangling correlations among interacting time series and addressing the complexities of distribution modeling. By treating time series as temporal dynamics, we introduce **KooNPro**, a novel probabilistic time series forecasting model that combines variance-aware deep **Koo**pman model with **N**eural **Pro**cesses. KooNPro introduces a variance-aware continuous spectrum using Gaussian distributions to capture complex temporal dynamics with improved stability. It further integrates the Neural Processes to capture fine dynamics, enabling enhanced dynamics capture and prediction. Extensive experiments on nine real-world datasets demonstrate that KooNPro consistently outperforms state-of-the-art baselines. Ablation studies highlight the importance of the Neural Process component and explore the impact of key hyperparameters. Overall, KooNPro presents a promising novel approach for probabilistic time series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- KooNPro is a novel time series forecasting method based on Koopman theory.
- It effectively estimates the process dynamics in a latent space where state transitions are linear.
- It eventually provides context-dependent variance estimates.

### Strengths
- Time series tasks, especially probabilistic forecasting, are relevant in many domains and far from being solved.
- The method is presented well and provides many benefits (variance estimation, flexible forecast horizon, nice theory, and practical performance).
- I am not aware of these ideas being presented before.

### Weaknesses
1. See Questions below.
2. The definition of target and context sets (ll. 153ff) and the splitting of $z$ (ll. 208ff) were not familiar to me, as they are not common in point forecasting. I would have personally benefitted from more exposition.

#### Minor Comments
- References should not be used as nouns (e.g., ll. 037f, 049f).
- Notation: Eq. (2)/(5) is missing a $p$ on the left-hand side and has odd typesetting of the expectation subscript. Some parens/brackets should be adjusted in height, e.g., in Eq. (3) and (17). In l. 219, $x_C$ and $y_C$ are not bold. L. 473 is the $e$  referring to "scientific notation" common in programming languages (in base-10) or Euler's number?
- One could rename Sec. 5 to Experiment**s**.
- Re. l. 306: Are the conditioning lookbacks of the test and the forecast horizon of validation (etc.) overlapping or not?
- Language: The senctence in l. 821f is odd.
- The combination in Fig. 3 is clever. However, given two separate plots would easily fit side-by-side, it is not worth the extra time needed to decipher the legend/axis labels.

### Questions
Note: The most important questions are listed first.

1. Regarding Sec. 5.2: The presented results are very impressive. However, a large chunk of the time series forecasting literature performs point estimation instead of full distribution modeling and, therefore, commonly evaluates using MAE/MSE (see, for instance, the overview [here](https://github.com/thuml/Time-Series-Library)). Additionally providing these metrics (possibly in the appendix) would help contextualize the findings in the broader body of work. These methods can also provide probabilistic forecasts, e.g., by learning an output that parameterizes a simple distribution to be sampled from or by methods such as Monte Carlo dropout.
2. Does the method need to be run multiple times to obtain the variance estimation samples?
3. The case study in 5.4 is interesting, yet it makes me question the ability of KooNPro to model the variance of the data truthfully. While I agree that many dimensions are modeled appropriately, the results indicate serious limitations of the method.
	1. Dimensions #3 and #6 show values far outside the 90% interval. Are they within something like the 99% interval since the model learns a possibly appropriate long tail of the distribution? Or does it show some of the method's limitations (which would be fine if acknowledged as such)?
	2. Ll. 446f explains the data characteristics of the Solar dataset. However, the model fails to appropriately model the very low nightly variance of the power production around zero and instead shows a significant variance estimate at, for instance, midnight. Why does that occur?
	3. Combining these two observations, the overall variance estimate appears rather *uniform* and not well-adapted to the dataset.
4. How large are the learned models measured in the number of parameters?
5. Could the method be straightforwardly used to forecast fractional steps into the future?

### Soundness
3

### Presentation
4

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
A method for multi-variate probabilistic time series forecasting is presented which combines the methods for temporal dynamics modeling using deep Koopman model with Neural Processes. The model consists of an encoder computing the hidden state h_t, a learned Koopman operator 'A' predicting the future hidden states and a decoder used to predict the final values using the hidden state h_t. In addition a neural process is used to model the latent dynamics S of the time series, which is used as an input to the Koopman operator to compute the future states.

### Strengths
Strengths
- This paper proposes a new way for probabilistic modeling of multi-variate time series by representing the time series into a low dimensional space using neural processes and using them to model the temporal dynamics of the time series.
- The idea presented in the paper is an intuitive approach for multi-variate forecasting. Modeling the latent dynamics of the time series is an important aspect that is missed by most state-of-the-art modeling approaches. As such, the method presented in this paper is interesting to the time series community.
- The paper presents extensive experimental evaluation and ablation studies demonstrating the effectiveness of the approach.

### Weaknesses
Weaknesses
- The description of the model is quite cryptic and not written in a clear manner. See questions below for parts that are unclear.
- While the paper describes everything using mathematical equations, the utility or advantage of such equations/models is unclear. How do each of the components of the model help with a better forecast? (i am looking for a high level motivation for each of the components of the model)
- Several works have introduced Koopman theory into time series modeling, however, there is no clear discussion of existing methods and their comparison with this work. The novelty of the paper is unclear without a clear distinction with existing work.
- Other probabilistic forecasting methods modeling latent factors in time series have not been discussed of compared (for example deep state space models).

### Questions
- What is the utility of the neural process latent variable S at a high level? Does it help model the correlations between the different time series? Can it be thought of as an encoding of each time series which also model the inter-correlations between the time series?
- It seems that S is an s-dimensional latent variable meaning that it encodes the whole time series in a low dimensional subspace. Many papers have modeled time series as state space models involving low-dimensional latent decomposition. What is the advantage of the proposed approach over these approaches.
Example papers modeling time series into low dimensional sub-spaces:
  - Wang, Yuyang, et al. "Deep factors for forecasting." International conference on machine learning. PMLR, 2019.
  - Rangapuram, Syama Sundar, et al. "Deep state space models for time series forecasting." Advances in neural information processing systems 31 (2018).
  - Paria, Biswajit, et al. "Hierarchically regularized deep forecasting." arXiv preprint arXiv:2106.07630 (2021).
- What is the utility of the delay embedding dimension k?
- Do context and target sets refer to training and testing time periods? can the context and target sets be interspersed, meaning can this method be used to predict missing values of irregularly sampled time series?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the practical problem of probabilistic time series forecasting and address the challenges. They propose KooNPro, which combines two methods, i.e., the Koopman model and Neural Processes.

### Strengths
- Addresses important problem of probabilistic time series forecasting
- Interesting idea to use the latent representations from the Neural Processes, typically used in computer vision
- Extensive experiments on 9 time series datasets
- Multivariate forecasting problem is challenging
- Good selection of multivariate probabilistic baselines to compare to including GP-Copula
- Good probabilistic metric CRPS is used in the benchmarking
- KooNPro shows state-of-the-art performance on 8/9 datasets

### Weaknesses
 - I think more background on the importance of probabilistic forecasting and its use in practical downstream task, e.g., supply chain in the introduction would be helpful
- Overall the writing quality could be improved.
- When discussing LSTMs in the introduction, DeepAR should be cited
- For probabilistic diffusion models, Kollovieh et. al, "Predict, refine, synthesize: Self-guiding diffusion models for probabilistic time series forecasting", NeurIPS 2024 should also be cited.
- There has also been an abundance of foundation models for time series forecasting, e.g., Ansari et. al, "Chronos: Learning the language of time series", 2024 that is not discussed int he introduction.
- DMD is more typically used in the dynamical systems and scientific computing communities
- The motivation for choosing Neural Processes as the probabilistic models rather than more current state-of-the-art probabilistic models, i.e., diffusion models is not clear.
- For application of NPs to spatio-temporal time series (PDEs), see Hansen et. al, "Learning Physical Models that Can Respect Conservation Laws", ICML, 2023
- Some of the background in Section 3 could be moved to an appendix to allow for more novelty of the method presentation and results in the main body.
- The architecture in Figure 1 is also taking a large amount of space.
- I have some concerns on the novelty since the proposed method is just combining two previously proposed approaches.
- May be good to include multivariate time series forecasting problem definition.
- Comparisons to other baselines, e.g., DeepAR (Salinas et. al, 2019) and MQ-CNN (Wen et. al, https://arxiv.org/abs/1711.11053, https://proceedings.mlr.press/v151/park22a/park22a.pdf), MQTransformer (https://arxiv.org/pdf/2009.14799, ) are missing, which could be run on electricity and traffic
- Bold the best in Table 2 or use same convention as Table 1 with color in red but I think bolding would be best for both.
- The method seems off in the case study in Dimension 6 and 8

### Questions
1. How can the method generalize past Gaussian distributions to modeling arbitrary distributions?
2. Have the authors tested with the Attentive Neural Process (ANP) Kim et. al, 2019, which shoes better performance than Neural Processes?
3. Could the model also be run with Gaussian Processes? I think a comparison to the simpler GP would be nice to add to motivate the benefit of the NP.
4. What is it about the electricity dataset that TimeGrid shows improved performance?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents KooNPro, a novel approach for probabilistic time series forecasting that integrates a variance-aware deep Koopman model with Neural Processes (NPs). By employing a variance-aware continuous spectrum modeled with Gaussian distributions, KooNPro effectively captures complex temporal dynamics with enhanced stability. It leverages NPs to capture global patterns across time series, improving prediction accuracy. Extensive evaluations on nine real-world datasets show that KooNPro outperforms state-of-the-art models, with ablation studies confirming the importance of its components and hyperparameters.

### Strengths
1. The proposed variance-aware continuous spectrum modeling address the complex nonlinear temporal dynamics, which is novel and has a solid theoretical foundation.
2. The empirical improvements are significant, outperforming other methods in complex, high-dimensional forecasting tasks.
3. The ablation study demonstrates the effectiveness of Neural Process and help to understanding the role of this key component. The case study shows that KooNPro's predictive capability aligns well with real-world observations, capturing diurnal patterns and demonstrating reliable predictive intervals.

### Weaknesses
1. The integration of Neural Processes and the probabilistic deep Koopman model requires a sophisticated training approach, including variational inference for optimizing the ELBO. This could pose challenges in implementation, and could increase the computational complexity. Specifically, the need to compute gradients through both the Koopman operator approximation and the Neural Process introduces potential instability and requires careful tuning of hyperparameters related to both components. Furthermore, the computational cost of sampling from the variational posterior during training could be significant, especially for long time series.
2. The effectiveness of KooNPro relies heavily on the design of the encoder and decoder networks for the linear space transformation. My concern is that poorly designed architectures could lead to suboptimal representations and thus hinder the model’s ability to learn the underlying temporal dynamics accurately. For instance, if the encoder fails to capture essential features of the input time series, the subsequent Koopman operator approximation will be based on a flawed representation, limiting the model's predictive power. Similarly, a poorly designed decoder might not be able to accurately reconstruct the time series from the latent space, leading to inaccurate predictions.

### Questions
Can you explain more intuitively why complex temporal dynamics can be captured using the proposed probabilistic deep Koopman model? In addition, I'm curious about the validity of the assumptions that formula (6) relies on: "hypothesize the latent space created by $\phi$ possesses linear characteristics", since formula (6) seems to be an important foundation of the subsequent derivations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors of the paper introduce a novel probabilistic time series forecasting model called KooNPro. KooNPro utilizes a variance-aware continuous spectrum, modeled using Gaussian distributions, to capture complex temporal dynamics and improve stability. By incorporating Neural Processes, the model captures fine dynamics and enhances global modeling capabilities. The authors evaluate KooNPro on nine real-world datasets and find that it consistently outperforms other state-of-the-art models in terms of accuracy and stability.

### Strengths
* Deep Koopman models had been used for time series forecasting before but not in conjunction with Neural Processes, hence the proposed model is non-trivial and new. 
* The authors enhance their model by a variance-aware continuous spectrum, which to my knowledge has not been done before.

### Weaknesses
 * Clarity: The authors could improve how they present their work. The math is clunky and too detailed, and can cause the reader to lose attention. For example, in section 4, the authors never refer to Fig.1 more than once (in line 169), so there is a disconnect between the math and the figure. Maybe explain the figure first and detail the model at a high-level, then go in the inner workings and foundations. Also in the caption of Figure 1, consider adding pointers to different parts of the figure to help the reader understand where to look in the Figure for each reference in the caption.

* Better analysis of each component of the model: The authors can provide a more comprehensive and insightful analysis of the Neural Process contribution. They may investigate how different NP architectures (e.g., Attentive Neural Processes, Convolutional Conditional Neural Processes) affect KooNPro's performance.

* Limited empirical discussion on the exact benefits of this model: The authors can better demonstrate For example, conduct experiments to specifically evaluate KooNPro's performance on, say, non-stationary time series or time series tasks with a much larger prediction length etc., comparing it to baselines that do not incorporate NPs. Compared to other models, if there were more convincing and broader experiments demonstrating the benefits of the proposed model, it would lead to wider adoption. 

* More empirical evidence for robustness and stability: The paper claims robustness and stability as advantages of the proposed model, but these claims are well empirically validated. For example, the authors can add experiments evaluating the model's performance under different noise levels

* Details on training baselines: Since the baselines were trained for each dataset, the authors should provide details on how the baselines were trained (how hyperparameter selection was done, what protocol was used etc.) in the appendix. It is important to check if the evaluation compares all models in a fair manner.

### Questions
* It is not clear what the term "spectral pollution" means in line 143. Consider explaining it for a reader who may not know about Koopman operators.

* Why are all context lengths 10 in Table 4 (Page 15)? Why wasn't the model tried with a different context lengths? This is also concerning as much larger context lengths are used in practice.

### Soundness
3

### Presentation
2

### Contribution
3
