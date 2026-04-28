# VAE-Var: Variational Autoencoder-Enhanced Variational Methods for Data Assimilation in Meteorology

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 8, 6, 6, 6, 5

## Abstract
Data assimilation (DA) is an essential statistical technique for generating accurate estimates of a physical system's states by combining prior model predictions with observational data, especially in the realm of weather forecasting. Effectively modeling the prior distribution while adapting to diverse observational sources presents significant challenges for both traditional and neural network-based DA algorithms. This paper introduces VAE-Var, a novel neural network-based data assimilation algorithm aimed at 1) enhancing accuracy by capturing the non-Gaussian characteristics of the conditional background distribution $p(\mathbf{x}|\mathbf{x}_b)$, and 2) efficiently assimilating real-world observational data. VAE-Var utilizes a variational autoencoder to learn the background error distribution, with its decoder creating a variational cost function to optimize the analysis states. The advantages of VAE-Var include: 1) it maintains the framework of traditional variational assimilation, enabling it to accommodate various observation operators, particularly irregular observations; 2) it lessens the dependence on expert knowledge for constructing the background distribution, allowing for improved modeling of non-Gaussian structures; and 3) experimental results indicate that, when applied to the FengWu weather forecasting model, VAE-Var outperforms DiffDA and two traditional algorithms (interpolation and 3DVar) in terms of assimilation accuracy in sparse observational contexts, and is capable of assimilating real-world GDAS prepbufr observations over a year.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents VAE-Var a new data assimilation algorithm based on variational assimilation in order to capture non-Gaussian characteristics of the conditional background distribution p(x|x_b) and thus enhance the accuracy of the method. The algorithm also able to incorporate real measurements coming form different systems.

The theory is clear. The architecture is well justified. The experiments too. The results of the main paper are very interesting, the one in the supplementary material bring some nuances.

The experiments rely on FengWu, an adaptation is done to construct the encoder and the decoder. ERA5 reanalysis data from 1979 to 2015 are used as training set. Two types of observations are used : simulated one from ERA5 to mimic real-world observations, and GDAS prepbufr with various system and instruments. The initial setting is derived from ERA5 dataset. For ERA5 simulations, fixed or unfixed observations are used. For fixed observations VAE-Var outperforms the other methods  in the main paper. In the supplementary material figure 8, sometimes 3DVar perform better than VAE-Var as for mslpRSME with 8000 observations. Graphically speaking, VAE-Var performs closely to 3DVar. It is worth noting that VAE-Var performs better most of the time with 1000 observations.
For GDAS, the RMSE is always smaller for VAE-Var. Bias is always better, except for z500.

All in all, this is a good paper.

### Strengths
In section 3.1.the use of the hypothesis of independence between the background states x-x_ b and background state x_b is well supported. The same goes for the non-Gaussian error distribution assumption.

The justification of the use VAE is clear. The generation of the training set construction is well formulated, the same goes for the loss function.

The authors are honest regarding their results, especially regarding the limitations in supplementary material A.2.

VAE-Var focuses learning the latent space of the error fields. This is an AI forecasting model effective at global scale with real-world measurements.

### Weaknesses
Limitations :

The performance presented in the main paper show very interesting results regarding VAE-Var. It must be nuanced with the supplementary material figure for broader considerations.

The authors mention in the supplementary material A.2. that they do not consider the determinant term in the equation 8 because it would make the assimilation of the objective function extremely hard to optimize. Thus, they introduce a scaling factor in the background term of the assimilation objective function. This is honesty from the authors. Maybe some tricks can be found later to make it rigorous.

Minor comments that do not impact the score:

Line 243-244, in Chen et al., the dimensionality of the problem is 189 * 721 * 1440. What does the 69 correspond to? Is it a confusion with what is used in the present study section 4.1?

Line 262-263, the authors claim that all the components of L are differentiable. Why H is differentiable?

There is no 2.5.3. in Giaquinta & Modica 2012, only 2.5.a-d regarding convexity.

### Questions
I am not completely convinced by the right part of the equation 2, could you give more details or a reference?

Line 129, why is the matrix R of the observation error is assumed to be diagonal?

Why do the authors use ERA5 reanalysis data from 1979 to 2015?

In the supplementary material A.2., could the authors give a reference where this term is rigorously considered? So, further work to make a link between the complexity and the improvements of VAE-Var approach can be supported.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a new Variational Data Assimilation method based on Variational Autoencoders, called VAE-Var. The method is separated into two stages, the training and the assimilation stage. During the training stage, a dataset of error samples is constructed by comparing two forecasts made at different time intervals. These samples are then used to train the VAE model, which learns the error distribution of the background states. During the assimilation stage, the VAE decoder is used to map latent vectors back to the physical state, that when combined to the background field represents the analysis states after data assimilation. The proposed methodology is compared against DiffDA, 1DVAR, and interpolation for the FengWu forecasting model and show superior performance across benchmarks

### Strengths
The paper is well-written, and clearly communicates the goal. The authors also explain the shortcomings of the other methods and how they propose to overcome them. The methods section is clear and the results show that VAE-Var out-performs all baselines.

### Weaknesses
 There is not an obvious weakness to the paper. However I am not an expert in meteorology so maybe I missed something.

### Questions
- In my understanding, Diffusion models can capture more complex distributions but require a lot of data. Could the authors provide more information on how fair the comparison between the VAE and the Diffusion model is? Meaning that if the distribution that they model is not  complex and the number of available data points is not large enough, isn't Diffusion models expected to perform worse?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study introduces VAE-Var, a neural network-based data assimilation method that combines VAE with traditional variational DA techniques. The authors claim that VAE-Var is designed to enhance DA by (i) Capturing non-Gaussian structures in background error distributions. (ii) Allowing effective assimilation of real-world, often irregularly distributed observations. Tests conducted using the FengWu weather model demonstrate that VAE-Var outperforms DiffDA and 3D-Var. Although the research topic is of interest, from the reviewer’s point of view, the novelty of the proposed approach is limited since (varitional-) autoencoder based data assimilation methods are already well established.

### Strengths
The VAE-Var approach can integrate partial and irregular observation points, giving it certain advantages over purely supervised machine learning surrogates for data assimilation. Numerical results show that the VAE-Var approach consistently outperforms both DiffDA and the conventional 3D-Var approach in terms of accuracy and efficiency.

### Weaknesses
The combination of neural network based AE (including VAE) and variational data assimilation is a well known approach. There are more than 10 publications regarding this idea in dynamical systems, for ex,
- Peyron, M., Fillion, A., Gürol, S., Marchais, V., Gratton, S., Boudier, P. and Goret, G., 2021. Latent space data assimilation by using deep learning. Quarterly Journal of the Royal Meteorological Society, 147(740), pp.3759-3777.
-Melinc, B. and Zaplotnik, Ž., 2024. 3D‐Var data assimilation using a variational autoencoder. Quarterly Journal of the Royal Meteorological Society, 150(761), pp.2273-2295.  
- Cheng, S., Chen, J., Anastasiou, C., Angeli, P., Matar, O.K., Guo, Y.K., Pain, C.C. and Arcucci, R., 2023. Generalised latent assimilation in heterogeneous reduced spaces with machine learning surrogate models. Journal of Scientific Computing, 94(1), p.11.
- Mohd Razak, S., Jahandideh, A., Djuraev, U. and Jafarpour, B., 2022. Deep learning for latent space data assimilation in subsurface flow systems. SPE Journal, 27(05), pp.2820-2840.
- Zhong, C., Cheng, S., Kasoar, M. and Arcucci, R., 2023. Reduced-order digital twin and latent data assimilation for global wildfire prediction. Natural hazards and earth system sciences, 23(5), pp.1755-1768.
…..

The proposed approach uses ground truth samples for background error specification. This might be a valid approach in twin experiments. However, ground truth is out of reach in most applications of DA methods, such as weather prediction. In other words, we never know the historical ‘true’ weather, as observations also contain uncertainties. I would suggest focusing on the innovation quantity (i.e., y-H(xb) or y-H(xa)) for a propre error covariance specification/analysis, see
-Tandeo, P., Ailliot, P., Bocquet, M., Carrassi, A., Miyoshi, T., Pulido, M. and Zhen, Y., 2020. A review of innovation-based methods to jointly estimate model and observation error covariance matrices in ensemble data assimilation. Monthly Weather Review, 148(10), pp.3973-3994.

### Questions
The authors should also compare their approach to ensemble-based data assimilation algorithms, such as EnKF, which are known to yield superior results for chaotic dynamical systems.

The role of the parameter lambda needs further explanation and why lambda = 4 is chosen in this paper?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces VAE-Var, a data assimilation method that combines variational autoencoders (VAE) with a traditional variational data assimilation technique to enhance weather forecasting accuracy. By using a VAE, VAE-Var relaxes the traditional Gaussian background error assumption, enabling it to better model complex, non-Gaussian background error distributions. Through experiments with both synthesized observations and real-world observations, VAE-Var demonstrates improved or comparable accuracy over established methods, including 3DVar and DiffDA. The approach’s adaptability to diverse data types and its demonstrated year-long forecasting stability showcases VAE-Var’s promise for real-world weather forecasting applications.

### Strengths
The paper communicates its concepts clearly. The use of VAEs to model non-Gaussian background error distributions is an original contribution, addressing a major assumption in background error modeling, with promising results. The experiment on real-world observations moves this work beyond a proof-of-concept. The topic is highly relevant: data assimilation is essential for numerical weather prediction, and developing efficient DA algorithms for AI-based weather prediction is necessary to improve their capability. Additionally, the integration of machine learning, specifically generative modeling, into DA represents a forward-looking approach that could influence further research in hybrid models for weather and climate prediction.

### Weaknesses
### 1. Regarding ERA5 as the 'ground truth'.
ERA5, as a reanalysis product, can serve as a useful reference, but it should not be treated as "ground truth," especially for evaluating data assimilation algorithms. ERA5 is known to have a lot of issues that can be attributed to terrain effects, poor coverage of assimilated observations, and the numerical model used. For example, ERA5 exhibits underestimated temperature in some regions of Europe[1], an overly strong equatorial mesospheric jet, mismatches in the analyzed near-surface wind/temperature/humidity[2], significant precipitation/temperature biases in some regions of North America[3], etc.

Therefore, merely evaluating data assimilation algorithms on ERA5 data overlooks the actual 'ground truth' beyond ERA5's inherent biases and errors. The authors could benefit from reviewing some non-ML DA papers that work on real observations, to see how their DA approaches are evaluated. For example, to assess whether a data assimilation algorithm truly works, it is important to compare its performance directly with real observations. A potential test could be holding out actual observations at the same positions at each time step and using these to evaluate the analyses from all implemented DA algorithms. This experiment would require no retraining and would allow for direct comparison and diagnostics of the DA algorithm developed. Paper [4], which uses the root-mean-square departures from actual observation to validate their approach, serves as a reference, though there are likely many more (for example, [5]).

Regarding ERA5 as ground truth and only evaluating algorithms on ERA5 are common issues in AI for weather research. Recognizing that ERA5 is not a definitive ground truth would provide the community with a clearer perspective and encourage more comprehensive benchmarking with different data sources, thus advancing the field.
[1] https://www.mdpi.com/2073-4441/14/4/543
[2] https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-Knownissues
[3] https://hess.copernicus.org/articles/24/2527/2020/
[4] https://journals.ametsoc.org/view/journals/mwre/151/7/MWR-D-22-0260.1.xml
[5] https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/qj.3917

### 2. Lack of reproducibility and missing details weaken the results and claims.
- As the code is not provided, additional details on the configuration of algorithms and baselines are necessary. However, they are not provided.
- There are no details on how the observation operator is constructed, particularly for real observations. 
- 3DVar details are missing, such as how $\text{U}_p$, $S$, $\text{U}_v$, and $\text{U}_h$ are determined?
- Configuration details for DiffDA are also absent, leaving readers uncertain about how this baseline was set up and tuned for the experiments.
- Providing the above details would enhance the reliability and transparency of the reported results, allowing readers to better assess and understand the performance claims of VAE-Var relative to these baselines.


### 3. Simplification
- As the authors mention, the simplification in the VAE-Var objective function is not mathematically rigorous. More importantly, it also weaken the claim that VAE-Var could better leverage the non-Gaussian statistics. By omitting the exact term in the background error component that accounts for the nonlinear transformation from a Gaussian to a non-Gaussian distribution, the model loses a critical factor needed to rigorously capture the intended non-Gaussian effects.  Unfortunately, addressing this limitation may be challenging, as the most straightforward solution would involve making the original, more complex optimization problem tractable.
- A minor issue related to appendix A.2: the reference for equation (7), *Giaquinta & Modica (2012): Mathematical analysis: functions of one variable. Springer Science & Business Media*, does not have Chapter 2.5.3 and equation (7).

### Questions
1. One major question that need to be addressed: VAE-Var improves minimally or does not improve with an increasing amount of available observations, whereas other approaches, both ML-based and traditional, show noticeable gains under similar conditions (Figures 3, 4, 8, 9, 10, 11, 12, 13). This behavior is unusual for data assimilation algorithms, as more observations typically enhance analysis accuracy. A thorough discussion or ablation study may be needed to investigate this.

Some suggestions from the review feedback system : )
- Conduct an ablation study to investigate why VAE-Var's performance doesn't improve significantly with more observations
- Discuss potential reasons for this behavior, such as possible saturation effects or limitations in the model's capacity to incorporate additional information
- Analyze the implications of this behavior for the algorithm's practical use in different observational settings
- If possible, propose modifications to the algorithm that might address this limitation

2. Formulating  $p(y∣x)$ as a Gaussian distribution is indeed an approximation of the observation errors. Although it is widely used in operational numerical weather prediction (NWP), it is an approximation instead of a well-defined characteristics. This assumption does not always hold. For instance, quality-controlled observations of brightness temperature from the High Resolution Infrared Sounder exhibit distributions significantly different from Gaussian. Incorrectly assuming Gaussian statistics in such cases can lead to substantial biases in the estimated state, as shown in studies like[6], which diagnose and assess the impacts of non-Gaussianity in innovations on data assimilation accuracy. For rigor, the paper could benefit from framing the Gaussian distribution of $p(y∣x)$ as a well-accepted but approximate assumption, rather than misleadingly stating that Gaussian error is a well-defined characteristic of observation errors. 

[6]: Pires, Carlos A., Olivier Talagrand, and Marc Bocquet. "Diagnosis and impacts of non-Gaussianity of innovations in data assimilation." *Physica D: Nonlinear Phenomena* 239.17 (2010): 1701-1717.

3. Minor issues:
- Line 202-2-3 and Algorithm 1 and Figure 1. Is $\tau$  the number of time steps or the time gap between two snapshots? It is a bit confusing here.
- Inconsistency between the lower half panel of Figure 1 and Algorithm 2: How is the hidden state initialized? 0 or a random field?
- Algorithm 3: the model time step T is not explicitly defined in the algorithm.
- The last term in Equation (8) should be $\frac{1}{2}\log \det \left( \frac{\partial \mathcal{D}(\textbf{z})}{\partial \textbf{z}} \right)^T \left( \frac{\partial \mathcal{D}(\textbf{z})}{\partial \textbf{z}} \right)$

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors offer a way of conducting sparse data assimilation using a minimization problem by estimating the error term of a forecasting model as compared to the state directly, and combining it with variational data assimilation. They achieve convincing results on weather forecasting.

### Strengths
The paper offers a method of data assimilation for sparse meteorological problems which surpass current baselines like DiffDA, and give very promising results. The method is clear, and the problem is particularly applicable to real-time weather forecasting.

### Weaknesses
Currently, the model seems method-specific, limiting its generalizability as a data assimilation approach since any new improvements or retraining of the original forecasting model would require retraining of this model. Is there a way to perhaps make this more robust? However, in the grand scheme of things, due to its superior performance, this isn't that big of an issue in my opinion.

### Questions
When generating, why is it integrated 0->2t and t->2t instead of just 0->t vs the ground truth at t?

How is the speed in terms of assimilation versus previous data assimilation approaches?

Since you're modeling the error; suppose that the initial state is very ill-estimated. Is the data assimilation approach still able to resolve the problem, or does it rely on the initial state estimate being within some stability region?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the data assimilation problem in the context of numerical weather forecast, and proposes a deep learning model for this problem based on a variational auto-encoder architecture. This approach captures the non-Gaussian background error distribution relative to the forecasting model within a variational data assimilation framework, by training a variational auto-encoder to learn the prior distribution. This deep learning model is evaluated on high-dimensional operational weather data and shows competitive performances compared to a recent diffusion based data assimilation algorithm.

### Strengths
The presented methodology is sound, and the proposed algorithm is accurately described. The paper is clearly written overall.

The proposed approach is evaluated on real-world data, on which it is shown to outperform the baselines. This suggests that considerable work has been invested to ensure the scalability of this method.

The VAE-Var algorithm is able to assimilate data from more general observation operators than DiffDA or other learning-based algorithms.

The authors propose a cyclic forecasting and assimilation setup where data assimilation and forecasting are coupled, with the forecast model, FengWu, being itself a large deep learning model. This method, already proposed in [1], is appealing for the future of numerical weather forecast as it does not rely on computational intensive weather models anymore once the neural networks are trained. 

Although not emphasized in the paper, a key potential strength of this approach is that the variational problem is formulated in latent space, rather than in state space. This may be a considerable advantage if the neural network efficiently compresses the state variable. Indeed, the data assimilation problem is typically of very high dimension, which is a bottleneck in practice, and reducing the dimension of the computations involved is key.

### Weaknesses
One key issue in the paper is the assumption that the state-of-the-art is limited to spatial-only data assimilation, specifically 3DVar-like algorithms, where the observations are assimilated at each new time step, as in Algorithm 3. There is no mention of the 4DVar algorithm, which is the state of the art for operational data assimilation, and which differs significantly from the description proposed in section 2. Instead of modeling error by a Gaussian distribution at a given time step relative to the prediction at the previous time, 4DVar models the error distribution at a multitude of observation times, within a so-called assimilation window, thanks to a physical model that couples the different instants. By enforcing temporal dependencies in the observations via physical laws, the reconstructed state becomes more accurate, and 4DVar is known to outperform 3DVar. As opposed to the framework described in Section 2, the error distribution in 4DVar is not Gaussian, as there is a strongly nonlinear physical model in the equation. See [2] and [3] for more details.

To properly study the impact of the proposed method, I believe that it should be compared, at least on a toy system, to 4DVar, and potentially to learning-based counterparts of 4DVar that model the temporal dimension of the signal to reconstruct it, including diffusion models [4] and end-to-end reconstruction approaches [5, 6]. Furthermore, the upsides of using the presented variational auto-encoder framework rather than a diffusion model as in DiffDA is not so clear: the authors mention that their algorithm is more versatile in terms of observation operators, but this difference is not thoroughly explained in Section 3.

Additionally, I found that the paper lacks clarity in some parts. For example, (too) much space is dedicated to the Bayesian framework of variational data assimilation, whereas the training loss function of the proposed method, which relies on the VAE framework, is not explicitly state. In the experiment section, I think that enumerating the baselines in a common paragraph would improve the clarity.

Finally, the paper does not mention the computational cost of data assimilation and does not compare the computational times involved. This aspect is of significant importance, and computational savings are one of the main reasons underlying the deep learning approach for weather forecast problems. Therefore, I believe that it would be beneficial for the paper to discuss this topic and to compare the computational times between the different approaches, traditional and learning-based.

### Questions
In Figure 3, how would the authors explain that 3DVar outperforms DiffDA? Should the latter not be better than the former, as it can capture non-Gaussian statistics?

In line 261, the part about rescaling the background term is not very clear (although it may be explained in more details in the Appendix).

Using the term "interpolation" as a name for a nearest-neighbor method might be confusing, as "interpolation" already has a precise meaning in the data assimilation literature [3].

A paramount aspect in data assimilation is uncertainty quantification and measuring the various possible reconstruction states, under chaotic dynamics. This is briefly mentioned in the related work section, but it would be very relevant to discuss how the probabilistic framework underlying variational auto-encoders allows the learning model to sample different predictions for a given observation.

### References

[1] Huang, L., Gianinazzi, L., Yu, Y., Dueben, P. D., & Hoefler, T. (2024). Diffda: a diffusion model for weather-scale data assimilation. arXiv preprint arXiv:2401.05932.

[2] Lorenc, A. C., & Rawlins, F. (2005). Why does 4D‐Var beat 3D‐Var?. Quarterly Journal of the Royal Meteorological Society: A journal of the atmospheric sciences, applied meteorology and physical oceanography, 131(613), 3247-3257.

[3] Asch, M., Bocquet, M., & Nodet, M. (2016). Data assimilation: methods, algorithms, and applications. Society for Industrial and Applied Mathematics.

[4] Fablet, R., Chapron, B., Drumetz, L., Mémin, E., Pannekoucke, O., & Rousseau, F. (2021). Learning variational data assimilation models and solvers. Journal of Advances in Modeling Earth Systems, 13(10), e2021MS002572.

[5] Blanke, M., Fablet, R., & Lelarge, M. (2024). Neural Incremental Data Assimilation. arXiv preprint arXiv:2406.15076.

### Soundness
2

### Presentation
3

### Contribution
2
