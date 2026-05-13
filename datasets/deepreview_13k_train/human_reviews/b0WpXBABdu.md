# Risk-Sensitive Diffusion: Robustly Optimizing Diffusion Models with Noisy Samples

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Diffusion models are mainly studied on image data. However, non-image data (e.g., tabular data) are also prevalent in real applications and tend to be noisy due to some inevitable factors in the stage of data collection, degrading the generation quality of diffusion models. In this paper, we consider a novel problem setting where every collected sample is paired with a vector indicating the data quality: \textit{risk vector}. This setting applies to many scenarios involving noisy data and we propose \textit{risk-sensitive SDE}, a type of stochastic differential equation (SDE) parameterized by the risk vector, to address it. With some proper coefficients, risk-sensitive SDE can minimize the negative effect of noisy samples on the optimization of diffusion models. We conduct systematic studies for both Gaussian and non-Gaussian noise distributions, providing analytical forms of risk-sensitive SDE. To verify the effectiveness of our method, we have conducted extensive experiments on multiple tabular and time-series datasets, showing that risk-sensitive SDE permits a robust optimization of diffusion models with noisy samples and significantly outperforms previous baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method called risk-sensitive SDE to improve diffusion model performance on noisy non-image data, like tabular and time-series datasets, by pairing noisy samples with risk vectors. Applying the standard diffusion process on noisy samples causes a marginal distribution shift and degrades generation quality. To mitigate this, the risk-sensitive SDE aims to minimize noise impact and improve robustness by minimizing a stability measure, termed Perturbation Instability. If perturbation stability holds—which is achievable in cases where the noise distribution is Gaussian—the noisy sample will have the same distribution as that of the corresponding clean sample at some iteration t in the Stability Interval and this could be used to optimize the score-based model. When this condition does not hold, the model seeks to minimize perturbation instability. The authors provide sufficient and necessary conditions for achieving perturbation stability and conduct extensive experiments demonstrating the effectiveness of risk-sensitive SDE over baseline models in both Gaussian and non-Gaussian noise settings.

### Strengths
1. The paper is well-written and well-structured, addressing an important problem and clearly articulating its contributions and findings.

2.  The work provides a well-developed mathematical foundation, including solutions for both Gaussian and non-Gaussian noise, enabling a robust approach to noisy data.

3. The paper includes well-designed experiments that validate the theoretical results and demonstrate the effectiveness of the proposed approach in handling noisy samples.

### Weaknesses
1. The paper focuses primarily on tabular and time-series data, which may limit insights into the method's performance on other data types, especially noisy image data. Extending experiments to image datasets could demonstrate the method’s generalizability across diverse noisy data contexts.

2. The effectiveness of the proposed approach heavily relies on accurate estimations of the risk vector. If these estimations are inaccurate—either overestimating or underestimating noise levels—the model may apply inappropriate adjustments, which could hinder its ability to adequately suppress noise. This reliance on accurate risk estimation introduces a vulnerability to the approach.

3. The paper could benefit from a discussion on the limitations of the proposed method and the areas that could be improved in future work.

### Questions
1. As mentioned above, while this paper focuses on noisy non-image data, such as tabular data and time series, noisy image data is also a common challenge in real-world applications. How would the proposed method perform on image datasets with high levels of noise?

2. Could you provide more details on how you derive the sensitivity interval in practice and what are the challenges you might encounter in deriving this?

### Soundness
3

### Presentation
3

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
This paper extends diffusion models to non-image data, like tabular data, which often contains noise that degrades model performance. The authors introduce a "risk vector" paired with each sample to indicate data quality and propose a risk-sensitive stochastic differential equation (SDE) that leverages this vector to minimize the effects of noise during model optimization. With specifically chosen coefficients, the risk-sensitive SDE supports more stable diffusion model training, accommodating both Gaussian and non-Gaussian noise types.

### Strengths
1 This paper ntroduces the novel concept of a "risk vector" to improve the robustness of diffusion models against noisy samples. This approach uses a principled method, risk-sensitive SDE, to incorporate the risk vector and reduce the adverse effects of noise, specifically perturbation instability.

2 This paper provides analytical solutions for risk-sensitive SDE with both Gaussian and non-Gaussian noise. A key finding is that Gaussian noise can be fully mitigated, eliminating its negative impact on model performance.

3 Extensive experiments on tabular and time-series datasets demonstrate the model's effectiveness in handling noisy samples, even when noise is mis-specified or non-Gaussian, outperforming prior baseline models.

### Weaknesses
1. The second section suggests that noise interference can cause a bias in the neural network's estimation of the score function. A visual experiment could be added to illustrate the extent of this bias, perhaps by showing how the learned score function deviates from the true score function with increasing noise levels. This would provide a more concrete understanding of the problem the proposed method aims to solve.

2. The construction of Risk-Sensitive Diffusion inherently requires extensive prior information about noise, specifically the risk vector. While the paper proposes a method to estimate this risk vector, the reliance on this information raises questions about its applicability in scenarios where noise characteristics are unknown or difficult to estimate. Could it be possible to denoise the data directly instead, perhaps through a learned denoising function, without requiring explicit noise modeling? The article lacks relevant exploration and comparative experiments on this aspect, which could limit the practical applicability of the proposed method.

3. The Risk-Sensitive Diffusion approach is limited to Gaussian and Cauchy noise. However, is this limitation applicable to most real world datasets? The article lacks an explanation regarding this point. Although the experiments in the article show that their method can be applied to unknown noise under the Gaussian assumption, there is a lack of experiments demonstrating whether the noise itself actually has Gaussian characteristics. This raises concerns about the generalizability of the approach to datasets with more complex or non-standard noise distributions.

### Questions
Please see weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a framework for optimizing diffusion models in the presence of noisy data by using risk-sensitive stochastic differential equations (SDEs) guided by a “risk vector” for each data sample. This risk vector quantifies sample quality, allowing the model to adapt its optimization process to noisy conditions, minimizing instability and improving robustness. The authors derive analytical solutions for risk-sensitive SDEs under both Gaussian and non-Gaussian noise and validate the framework’s effectiveness through experiments on tabular and time-series data, showing significant improvements over baseline diffusion models.

### Strengths
* The paper provides a comprehensive characterization of each case encountered within the risk-sensitive framework
* The proposed methodology intrinsically outperforms approaches that condition the score function solely on the risk value or vector, demonstrating better handling of noise.
* Simple, low-dimensional experiments effectively illustrate the method’s properties: stability intervals for Gaussian-corrupted data, enhanced robustness to class imbalance relative to a risk-conditional baseline, and flexibility of the framework with "minimal instability".

### Weaknesses
 * The paper would benefit from improved mathematical precision, as some definitions and notations create ambiguity, which affects readability. The structure can feel confusing. Some theoretical claims could provide interpretative insights, which would strengthen the theoretical exposition. Specifically, the definition of the risk vector $r$ and the noise family $P_{\epsilon}$ lacks clarity, making it difficult to understand how these concepts are mathematically formalized. The use of $P_{\epsilon}$ as a family of distributions that seemingly should depend on $r$ but doesn't, and then later using $P_r$ instead, adds to the confusion. Furthermore, the theoretical claims, such as those in Theorem 3.1, would benefit from more intuitive explanations. For instance, what does the stability interval look like, and are there any guarantees about the behavior of $u(t)$ or $f(t)$ at $t=0$ or at the boundaries of the stability interval? The fact that $f(r, t)$ does not depend on $r$ in Theorem 3.1 is not explained intuitively.
* The experimental setup appears tailored to emphasize the proposed method’s strengths, which raises questions about the generalizability and fairness of the evaluation. For instance, in the tabular data experiments, the imputed data is described as very noisy, which suggests that the method might exclude them from the training process due to a small stability interval. This raises concerns about whether the performance gap is primarily due to the method effectively ignoring noisy samples, rather than truly handling them. In the time-series experiments, the interpolation method and the evaluation procedure are not sufficiently detailed. The lack of information about the kernel used in the Gaussian process for interpolation, and the specific part of the dataset used for generative performance measurement, makes it difficult to fully understand the performance gains. The customized evaluation methods, which appear designed to highlight the strengths of the proposed approach, may not fully capture a fair performance assessment.

### Questions
I am willing to reconsider my scores if my concerns are addressed. 

* Lines 56-57: The claim that isotropic Gaussian noise can completely eliminate negative impacts is maybe a bit of an over-statement. Could you provide a brief explanation (the data being already noised, we juste use it after some noising time)
* Lines 93 and 119 contain redundant expressions such as “the reverse process (i.e., reverse version of the diffusion process)” and the entire “Remark 2.1.” Simplifying these would improve readability.
* Definition 3.1: The phrase “The risk information $r$ shapes as a vector” is mathematically unclear, alike the definition of the set in (4). The use of $P_{\epsilon}$ for a family of distributions that should depend on $r$ is confusing. Furthermore, on line 172, $P_r$ is used instead of $P_{\epsilon}$, while it still does not depend on $r$ (all isotropic centred Gaussian distributions?). This is frustrating to follow.
* In Theorem 3.1, it would be nice to add some interpretations for the mathematics. What can we expect the stability interval to look like? Are we sure $u(t)$ or $f(t) (= u' / u)$ does not diverge at $t=0$ or on the boundary of the stability interval? What can we say about the fact that $f(r, t)$ does not depend on $r$? You can then articulate it better with Corollary 3.1, where you can focus on explaining that, essentially, a noised sample $\Tilde{x}(0)$ can be used in the training process at the moment when the noising process would have added "equivalent" noise from a clean sample. Is this not a good interpretation?
* Line 340: For non-Gaussian noise, it would be interesting to specify any required conditions on the noise distribution for the derivation of tractable expressions.
* Experiments (Tabular Data): Given that the imputed data is noisy (lines 506-507 "the data generated in this way will be very noisy since KNN is certainly very inaccurate."), it will mostly not be used to train the model, since the stability interval will be a small set around $T$. To properly assess the technique, you would need an experiment where you train a model only on the clean samples. 
* Experiments (Noisy Time Series): In the same way, we would need more information on how the interpolation is constructed, what is the kernel used for the Gaussian process, on which part of the dataset is the generative performance measured etc., so we can fully understand the performance gap. A comparison based on your customized evaluation methods, which appear designed to highlight the strengths of your approach, may not fully capture a fair performance assessment.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
When we train a diffusion model, what if not all samples from the training dataset were made equal? Some contain no noise - risk of zero - and some are noisy and come with so-called risk vectors that indicate how corrupted they are. The paper proposes modifications to the standard diffusion training and sampling algorithms that account for this noise in the training data. Samples generated by the resulting model are [almost] the same as if the model were trained on entirely clean/uncorrupted data. The authors show that their modifications are grounded in theory and are expected to work in many realistic scenarios.

### Strengths
I buy into the concept, I think that this is an interesting twist on the original idea. Even though the changes to the diffusion algorithms are rather minor, the theory section persuades me that this is indeed the right modification in the presence of noise. The toy examples are equally persuasive - it's pretty clear that the proposal works.

### Weaknesses
I'm less impressed with the empirical results, as they too seem rather artificial and closer in spirit to the synthetic data than to a real-world problem being solved. The current experiments, while demonstrating the method's ability to handle risk vectors, do not convincingly showcase its practical utility in scenarios where such risk is inherent and not artificially constructed. The experiments lack a clear connection to real-world data corruption, making it difficult to assess the method's effectiveness in realistic settings. The use of toy examples, while helpful for understanding the core idea, does not translate well to the complexities of real-world datasets. The current experiments do not adequately demonstrate the method's robustness to different types of noise or corruption that might be encountered in practice.

### Questions
I don't have questions - everything in the paper is pretty clear. I suggest improving empirical results on the real-world data. A low-hanging fruit would be promoting the vision results from the Appendix to the main body: this methods seems very general to me and needs not be confined to just the time series or tabular data setting. Generally, authors should think about/look for settings where this risk/corruption is front and center. Perhaps from vision and video domains. Or from finance - you mention applicability, but don't attempt to solve any finance-flavored problems. Perhaps volatility can proxy for noise/risk. Right now, this paper is more like a [rather elegant] solution looking for a problem it can solve.

### Soundness
3

### Presentation
4

### Contribution
3
