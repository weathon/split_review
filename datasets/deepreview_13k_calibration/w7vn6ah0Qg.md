# KokerNet: Koopman Kernel Network for Time Series Forecasting

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
The Koopman operator has gained increasing attention in time series forecasting due to its ability to simplify the complex evolution of dynamic systems. However, most existing Koopman-based methods suffer from significant computational costs in constructing measurement functions and struggle to address the challenge posed by the variation in data distribution. Additionally, these approaches tend to empirically decompose time series or distributions into combinations of components, lacking interpretability. To tackle these issues, we propose a novel approach, **Ko**opman **ker**nel **net**work (**KokerNet**), for time series forecasting. On one hand, we construct a measurement function space using the spectral kernel method, which enables us to perform Koopman operator learning in a low-dimensional feature space, efficiently reducing computational costs. On the other hand, an index is designed to characterize the stationarity of data in both time and frequency domains. This index can interpretably guide us to decompose the time series into stationary and non-stationary components. The global and local Koopman operators are then learned within the constructed measurement function space to predict the future behavior of the stationary and non-stationary components, respectively. Particularly, to address the challenge posed by the variation in distribution, we incorporate a distribution module for the non-stationary component, ensuring that the model can make aligned distribution predictions. Extensive experiments across multiple benchmarks illustrate the superiority of our proposed KokerNet, consistently outperforming the state-of-the-art models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper builds on Koopman operator methodology to address non-stationary time series forecasting in an efficient way based on Random Fourier Features. The authors consider the Reproducing Hilbert space built from Fourier Features as the measurement function space, and report approximation results on Gram matrix as well on the Koopman operator eigenfunctions. In the section dedicated to learning, they assume a decomposition of the time series into a stationary and no stationary part and learn the corresponding global and locals Koopman operators following the steps of (Liu et al. 2023). A statistical test (KS) is proposed to measure the stationarity of the data from which helps to define the decomposition in stationary/non-stationary signals. Finally they introduce an alignment loss that measures how the forecasted distribution differs from the ground truth assuming Gaussianity  of the state variable distribution. Experimental results include a few competitors and feature different time-series benchmarks.

### Strengths
This paper tackles non-stationary times-series forecasting, a classical but still crucial in many applications. They propose to use the Koopman operator machinery to adress this issue. Leveraging random Fourier methodology for the measurement space, they can propose an efficient estimation of these operators that they learn in the context of a decomposiiton of the time-series into a stationary and non-stationary part.
The paper comes with a new (but relatively direct) result on the estimation of eigenfunctions of a Koopman operator when leveraging the finite dimensional reproducing Kernel Hilbert space induced by the Random Fourier Features.
A secondary contribution is the proposition to use a Sinkhorn loss to measure the distance between the distribution of forecasts and the ground truth.

### Weaknesses
While very promising this paper, this paper seems to suffer from incompleteness in its presentation and should be re-writtent to make it reproducible.

The learning of the global and local koopman operator is not clearly posed but are direclty inherited from (Liu et al 2023) : the loss function is even not mentioned, here likely the square loss given the equations. A constraint is evocated but never described in the context of learning: when is it used?

The decomposition into stationary and non-stationary parts which is crucial here is only discussed in the appendix, but it remains very unclear how the stationarity index is used (probably a typo on S_V / S_alpha  ?). I also find disturbing that the authors refer to a Python code and not mathematical equations.

Finally it is important to refer to previous papers on:
- Random Fourier Features for Koopman operator learning: Salam, T., Li, A. K., & Hsieh, M. A. (2023, June). Online Estimation of the Koopman Operator Using Fourier Features. In Learning for Dynamics and Control Conference (pp. 1271-1283). PMLR.
other attempts to work with finite dimensional measurement spaces 
- (available in arxiv in 2023)
Meanti, G., Chatalic, A., Kostic, V., Novelli, P., Pontil, M., & Rosasco, L. (2024). Estimating Koopman operators with sketching to provably learn large scale dynamical systems. Advances in Neural Information Processing Systems, 36. 

- in the experimental part, the authors refer to loss terms they never introduced - they also do not mention how they choose the number of random Fourier feature no provide an analysis of it.

### Questions
please could you:
(1) indicate in what extent the stationarity index is new ?(if not, please refer to the literature on KS test for stationarity measurement)
(2) explain in details how you use the stationarity index that you propose and finally choose the way you decompose the time-series.
most importantly:
(3) could you explain how you use the so-called constraint module and provide a complete algorithm.

### Soundness
2

### Presentation
2

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
This paper presents KokerNet, a Koopman kernel network for time series forecasting. It addresses critical issues in existing methods, such as the high computational costs and the challenges posed by data distribution variations. By employing spectral kernel methods to construct a measurement function space, the authors achieve a notable reduction in computational burden. Furthermore, the decomposition of time series into stationary and non-stationary components is used to enhance interpretability. The global and local Koopman operators are effectively utilized to predict future behaviors of these components.

### Strengths
The application of Koopman operators for time series forecasting represents a significant advancement. The spectral kernel method for measurement functions is a commendable innovation that simplifies the computational process. The creation of an index to facilitate the decomposition into stationary and non-stationary components is particularly valuable. This not only enhances model interpretability but also provides insights into the dynamics of the data. Empirical results show KokerNet's superiority, underscoring its practicality and effectiveness in real-world applications.

### Weaknesses
The manuscript does not clearly explain the integration of the kernel method within the Koopman network framework. Readers are left without a clear understanding of how the spectral kernel functions operate within the Koopman operator or how these methods combine to provide computational advantages. More detailed explanations and illustrative diagrams would significantly aid comprehension and convey the novelty of the approach.

The manuscript also lacks citations and discussion of closely related and classical methods, particularly multiresolution DMD, which already employs a similar architecture for handling non-stationary time series. KokerNet’s model appears to be a special case of this approach. Expanding the literature review and explicitly contrasting KokerNet with multiresolution DMD would clarify the unique aspects of the method.

The theoretical components presented are largely standard and do not demonstrate clear, novel benefits for KokerNet’s performance or interpretability. The paper would be strengthened by a clearer, more thorough explanation of how the theory specifically benefits the model’s forecasting ability or contributes new insights to the field.

### Questions
1. Could the authors provide more detail on how the spectral kernel method integrates within the Koopman framework and specifically outline its role in enhancing efficiency?
2. Why is multiresolution DMD, which appears closely related, not discussed as part of the literature? Could the authors clarify the differences and potential benefits of KokerNet over multiresolution DMD?
3. Could the authors include more insights into how they ensured their model's robustness to real-world shifts in data distribution, especially for rapidly changing non-stationary components?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes learning the Koopman operator in a proposed low dimensional space by using cosine functions, motivated by a use of Bochner's theorem and kernel integral transforms. It performs several studies in relation to time series forecasting to assess the merits of the proposed methodology.

### Strengths
The paper showcases an innovative development at the intersection of (1) Kernel integral transforms theory, (2) Koopman operator theory. An interesting decomposition is presented in order to tackle the non-stationarity of the time series which can appear in practical settings.

### Weaknesses
The majority of the paper doesn't present much perceivable novelty in my opinion. For example there is an attempt in Appendix C.1, Lemma C.1 to *prove* an obvious application of Bochner's theorem which anyway has already been done in the famous "Random Fourier Features" paper. This is already known several times over and thus there should be a *compelling* reason to present its proof and make it appear like its your own innovation (I am not against re-writing well-known proofs but it must be for a good reason). There is no apparent reason in the paper why this should be shown as a line-by-line proof and this leads me to the suspicion of there being an artificial mathematical padding of space, unfortunately, in order to try and obfuscate the reader.

This is amplified when considering Lemma C.2 and Theorem C.1, since the Chernoff-based exponential probability bound (C.7) proven doesn't appear to serve any intrinsic purpose and appears to be a standard matrix probability theorem slightly re-arranged so as to obfuscate the readability of the paper. Such bounds *are* useful don't get me wrong, but usually then there needs to be a stronger commentary and appeal to something like Computational Learning Theory. One can argue that it is useful in a sense for then proving Theorem C.1 in particular for equation C.16 but then ultimately what does Theorem C.1 intend to say? That ultimately with a high enough number of samples there is a convergence between a kernel approximator and a mean estimator of a set of random matrices? This is quite an obvious conclusion and doesn't need 1+ pages of proof. Of course it *can* be interesting if the bound intends to be studied in some sufficient manner (as per Computational Learning Theory), but then it is not made any reference to in the actual paper other than "here is a complex bound". An appeal to Law of Large Numbers in a random matrix form would be much more simpler, familiar, and appropriate than what is currently presented for example, just to say "it works" rather than "how it works" according to sampling number  complexity

And for example Theorem C.2 (ii) is something that should be known to the reader *if* they are quite familiar with Koopman Operator Theory in practice and thus no proof is really required yet one is presented which essentially overlaps the intended purpose of the previous proofs / lemmas, which ultimately all (over the course of 3+ pages) serves to raise the point "it works in large sample rates", which unless there is good reason to belief this should not be the case, is an obvious conclusion. Ultimately to a reader not well versed in mathematics this would appear to do nothing but introduce of a lot of new notation to intentionally obfuscate the readability of the paper, in my opinion. 

Mathematics aside, there does not appear to be ample quantitative results to show that the proposed method actually works out in practice and thus should be used as an alternative to other competing Koopman operator based methods. For example for the purpose of forecasting why should someone be motivated to use this method over the standard DMD-based methods which have been shown to be enjoying absolute plethora of use cases in the engineering fields which experience massive levels of non-stationarity and large dimensionality? The authors are suggested to read for example "Higher Order Dynamic Mode Decomposition and Its Applications". If the proposed methodology is to be used seriously as good alternative then it would be worth explicitly analyzing why it might do better than higher order dynamic mode decomposition and such, which are currently actively used in everyday engineering industries for problems such as spatio-temporal fluid dynamics *without* an explicit need for training. Essentially,  because "Koopman" is the name of methodology I would expect much more "Koopman" based comparisons and analysis.

### Questions
Since the purpose of the questions is to try and alter the reviewer's mind, it would be good if you could address those main claims raised in the "weakness" section if possible. In particular,

 - Why did you feel it was required to show a half-page proof of Bochner's Theorem, and do you feel that there is strong value in presenting a Chernoff-based bound of the methodology given that the bound is not really serving much purpose (to my own opinion), and that it leads more to the obfuscation of the text rather raise its intrinsic value? 

 - How come you didn't try to compare the proposed methodology to other Kooopman operator based forecast methods that are actively used in industry?

### Soundness
3

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
4

### Summary
This paper introduces Koopman Kernel Network (KokerNet), a novel approach for time series forecasting that addresses the computational and interpretability challenges of existing Koopman-based methods. It uses a spectral kernel method to create a low-dimensional feature space, reducing computational costs. KokerNet decomposes time series into stationary and non-stationary components using a Kolmogorov-Smirnov (KS) test-based index, providing a more interpretable decomposition. It also includes a distribution module to handle time-varying distributions. Experiments show that KokerNet outperforms state-of-the-art models, enhancing both efficiency and interpretability.

### Strengths
1. The paper is overall well written

2. KokerNet enhances efficiency and interpretability by using a spectral kernel method for dimensionality reduction and decomposing time series into stationary and non-stationary components with a KS test-based index, outperforming state-of-the-art models.

3. The idea of integrating a distribution constraint into the forecasting process is sound.

### Weaknesses
The authors claim that decompositions in previous works often rely on empirical determinations of component composition and proportions, which lack interpretability. They propose to utilize the Kolmogorov-Smirnov (KS) test to guide the decomposition of time series into stationary and non-stationary components. I believe that a comparative analysis with these methods through ablation experiments is necessary. For instance, consider employing the approach based on Fourier transformation coefficients from reference [1] to differentiate between stationary and non-stationary components, replacing the KS test index selection in the proposed model.

### Questions
1. In the design of the measurement function, the encoder utilizes a mathematical function in the form of a Reproducing Kernel Hilbert Space (RKHS), while the decoder adopts a neural network in the form of a Multi-Layer Perceptron (MLP). What is the rationale behind this asymmetrical structure?

2. Regarding the segmentation of non-stationary components, what criteria are used to determine the segmentation length? Is the final performance sensitive to this parameter?

### Soundness
3

### Presentation
4

### Contribution
3
