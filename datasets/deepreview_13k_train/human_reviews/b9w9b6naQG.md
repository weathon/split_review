# Rényi Neural Processes

- Decision: Reject
- Scores: 3, 3, 8, 6

## Abstract
Neural Processes (NPs) are deep probabilistic models that represent stochastic processes by conditioning their prior distributions on a set of context points. Despite their obvious advantages in uncertainty estimation for complex distributions,  NPs enforce parameterization coupling between the conditional prior model and the posterior model, thereby risking introducing a misspecified prior distribution. We hereby revisit the NP objectives and propose Rényi Neural Processes (RNP) to ameliorate the impacts of prior misspecification by optimizing an alternative posterior that achieves better marginal likelihood. More specifically, by replacing the standard KL divergence with the Rényi divergence between the model posterior and the true posterior, we scale the density ratio $\frac{p}{q}$ by the power of (1-$\alpha$) in the divergence gradients with respect to the posterior. This hyper parameter $\alpha$ allows us to dampen the effects of the misspecified prior for the posterior update, which has been shown to effectively avoid oversmoothed predictions and improve the expressiveness of the posterior model.
Our extensive experiments show consistent log-likelihood improvements over state-of-the-art NP family models which adopt both the variational inference or maximum likelihood estimation objectives. We validate the effectiveness of our approach across multiple benchmarks including regression and image inpainting tasks, and show significant performance improvements of RNPs in real-world regression problems where the underlying prior model is misspecifed.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes RNPs, a new framework that aims to mitigate the issue of prior misspecification in neural processes (NPs). NPs are deep probabilistic models that represent stochastic processes by conditioning prior distributions on context points. However, the parameterization coupling between the prior and posterior models in NPs can lead to a misspecified prior, resulting in biased posterior estimates and degraded performance.

To address this, the authors propose optimizing an alternative posterior using the Rényi divergence between the model posterior and the true posterior, instead of the standard KL divergence. The Rényi divergence introduces a hyperparameter α that scales the density ratio between the posterior and prior, dampening the effects of the misspecified prior. The proposed RNP objective unifies the variational inference and maximum likelihood estimation objectives for training NPs via α, allowing better marginal likelihood and posterior expressiveness.

### Strengths
- The paper provides a thorough theoretical analysis and derivations for the proposed Rényi Neural Process objective, establishing a solid foundation for the proposed method.
- The experiments are comprehensive, covering various datasets and tasks, including regression, image inpainting, and real-world regression problems with prior misspecification.
- The authors conduct extensive ablation studies and hyperparameter tuning, demonstrating the robustness and effectiveness of the proposed method.

### Weaknesses
 - Limited novelty: The core idea of using an alternative divergence measure (Rényi divergence) to mitigate the effects of prior misspecification is not entirely novel. Previous works in the domain of robust variational inference have explored the use of other divergences, such as α-divergences and f-divergences, to address similar issues. The authors could provide a more comprehensive discussion of how their work relates to and differentiates from these earlier efforts.
- Hyperparameter sensitivity: The choice of the hyperparameter α plays a crucial role in the performance of the proposed method. While the authors provide some guidelines for tuning α, a more comprehensive analysis of the sensitivity of the method to different values of α and strategies for automatic tuning could further enhance the practical utility of the proposed framework.

- The parameter coupling between the posterior and prior in neural processes is by design to share parameters, but it's not a hard constraint. Isn't a simple baseline approach to mitigate prior misspecification to separately parameterize the posterior and prior models? Could the authors provide a comparison with this simple baseline to better demonstrate the advantages of their proposed method?

Overall, naively combining existing ideas may not constitute a sufficient contribution for a top-tier conference like ICLR, which expects a higher level of novelty and significance.

### Questions
- The authors mention that the proposed framework can be further extended to improve the robustness of contextual inferences, such as prompt design in large language models. Could the authors provide more details or insights into how their method could be adapted or applied to such tasks?

- The parameter coupling between the posterior and prior in neural processes is by design to share parameters, but it's not a hard constraint. Isn't a simple baseline approach to mitigate prior misspecification to separately parameterize the posterior and prior models? Could the authors provide a comparison with this simple baseline to better demonstrate the advantages of their proposed method?

Overall, naively combining existing ideas may not constitute a sufficient contribution for a top-tier conference like ICLR, which expects a higher level of novelty and significance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Renyi Neural Process, a framework that addresses the limitations of standard Neural Processes (NPs) by mitigating prior misspecification through a new objective function. RNP enhances uncertainty estimation and robustness in learning by applying Rényi divergence instead of traditional KL divergence, leading to improved performance across various benchmarks. The authors demonstrate consistent log-likelihood improvements in tasks such as 1D regression and image inpainting while acknowledging the trade-off between computational efficiency and performance due to Monte Carlo sampling.

### Strengths
RNP consistently achieves better log-likelihood and mitigates over-smoothing in predictions, particularly in challenging tasks like periodic data regression and higher-dimensional image inpainting. By utilizing Renyi divergence, RNP enhances the expressiveness of the posterior distribution, leading to more reliable uncertainty quantification compared to traditional Neural Processes.

### Weaknesses
The use of Renyi divergence requires additional computations, particularly due to the need for Monte Carlo sampling to estimate the divergence. This can lead to longer training times and higher resource consumption compared to standard Neural Processes, which may limit scalability in large datasets or real-time applications. Specifically, the computational overhead is not just in the sampling itself, but also in the repeated evaluations of the encoder and decoder networks for each sample, which can become a bottleneck. RNP introduces extra parameters that control the behavior of the divergence, which can make the model sensitive to hyperparameter tuning. Improper selection of these parameters may lead to suboptimal performance, requiring extensive experimentation to find the best configuration for specific tasks. The paper does not provide a clear methodology for selecting these parameters, which could hinder reproducibility and practical application. The complexity of the RNP framework, particularly with the incorporation of robust divergences, can make it harder to interpret the model's decisions and the underlying relationships in the data. This lack of interpretability may hinder its adoption in fields where understanding model behavior is crucial, such as healthcare or finance. The paper does not address the interpretability limitations of Neural Processes, which are already a challenge, and the introduction of Renyi divergence further obscures the model's decision-making process.

### Questions
1, How does the choice of Renyi divergence impact the trade-off between predictive performance and computational efficiency in RNP compared to traditional Neural Processes?

2, What strategies can be employed to effectively tune the additional parameters introduced in RNP to ensure optimal model performance across different applications?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to address a key potential weakness in latent variable neural processes (NP), namely, that the true prior $p(\mathbf{z} \mid X_C, Y_C)$ can be approximated by a parametric model $q_\phi(\mathbf{z} \mid X_C, Y_C)$ which shares parameters with the approximate posterior model. When the prior is “misspecified”, as defined rigorously in the text, the variational bound used to optimize NP is no longer valid and the authors argue leads to worse data fitting. They remedy this issue by replacing the KL divergence in the lower bound with a Rényi divergence, whose hyperparameter $\alpha$ enables more expressive posteriors. On a variety of experiments commonly used in the NP literature, the authors demonstrate that existing NP models benefit from the Rényi divergence variation of the objective.

### Strengths
The authors identify an important modeling assumption in NP that can be a source of failure for these models and suggest an easy to implement and intuitive remedy.

The experimental section is well laid out, and I appreciated that the authors explicitly connected each experimental subsection to an empirical question, e.g., in lines 397-400. The empirical results themselves are extensive. The improvements over strong baselines, such as TNP, are compelling.

### Weaknesses
The list below roughly follows the order of appearance in the manuscript. In my opinion W2, W6, W10 are the most important among these.

### W1: The claims at the end of the introduction seem to overlap quite a bit.
For example, in contribution 1, the authors already discuss the improved likelihoods, which seems like it is more a part of the empirical contributions of 2 and 3. Additionally, again, in contribution 2 the reference to “consistent log-likelihood improvements” is actually the main point of the contribution of the third bullet.

### W2: The effects of the misspecified prior can be made more rigorous
Currently, the authors claim that KL divergence leads to:
- Biased estimation of the posterior variance
- Less expressive models that underfit

However, analyzing these claims analytically would be quite helpful ,e.g., what is the analytical form of this bias in estimating the posterior variance and is there a way to make the “underfitting” more rigorous. Currently, the main analysis is a single motivating example. For example, Figure2b is quite anecdotal and only shows a single sample. I recognize that this is not a small ask, but I believe it will significantly improve the quality of Section 2 and the overall motivation. Specifically, the authors should provide a more detailed analysis of how the KL divergence forces the approximate posterior to be close to the prior, even when the prior is a poor representation of the true posterior, and how this affects the posterior variance. A theoretical analysis, even in a simplified setting, would greatly strengthen the motivation.

### W3: Notation of Definition 3.1 seems detached from the rest of the paper.
How does $\eta$ relate to the rest of the notation introduced in this work? Does it correspond to a shared parametric form of $p_\varphi$ and $q_\varphi$? If so, this needs to be spelled out.

### W4: Proposition 3.2 is missing an “if”
Shouldn’t there be an “if” in lines 173 and 174:
> …, **if** the prior model is misspecified,...

Currently the proposition reads as if misspecification is inevitable, which, in my understanding, is not necessarily true.

### W5: I think the equation for $\mathcal{RNP}$ is imprecise
You are taking a Monte Carlo estimate of an expectation that relies on the parameters over which you are optimizing (presumably via stochastic gradient descent). This would require some methodology along the lines of the reparameterization trick which should be explicitly stated here.

### W6: Prior misspecification does not seem related to the ML-based objective
It is not clear to me from the current exposition why prior misspecification should affect the ML-based version of the NP objective. The authors should clarify how the prior, which is only used in the variational objective, impacts the maximum likelihood objective, especially since the prior is not directly involved in the likelihood term. It would be helpful to explain the connection between the prior and the learned representation when using the ML objective.

### W7: Lines 242-247 seem out of place / irrelevant
I do not understand how these lines relate to the rest of this section. The generalization / recasting of TNP-A as an implicit latent variable model with Diracs is not used in the rest of the exposition / derivation to the best of my understanding.

### W8: The tabular regression experiments (Pace & Barry, 1997) appear to be missing
These results are not in the experimental results sections nor in any of the appendix sections

### W9: The details for the differential equations (e.g. Hare-Lynx and Lotka-Volterra) should be added to Section 7 before the Baselines paragraph.
A similar level of detail to that provided for GP/inpainting experiments should be added for these DE experimental setups as well.

### W10: The improvements seen in Table 1 (i.e., where misspecification is presumably not a problem) are not well explained.
Why do we see gains in the standard GP / inpainting experiments from RNP if there is not necessarily a misspecification issue here? The authors should provide a more detailed explanation of why the Rényi divergence improves performance even when the prior is not necessarily misspecified. It seems that the Rényi divergence is providing some benefit beyond just addressing prior misspecification, and this should be explored further.

### W11: The additional compute overhead from the Monte Carlo approximation should be quantified.
Both for the main results and in the ablation analysis, the authors should have a secondary axis or some way of conveying how the actual compute overhead and how it grows in $K$.

### W12: The graphs are quite small and difficult to read without extensively zooming.
The legends are quite difficult to make out. Additionally, Figure3b has a different line color for some reason and Figures 4a and 4b are missing a legend for the red dot indicator.

### W13: Typos / Grammatical Errors
Below I list the minor typos/errors that I noticed through a preliminary read:
- Line 035: “advance” should perhaps be “advantage”?
- Line 061: “poster variance” should be “posterior”
- Line 074: “achieve the better…” should be “achieve a better”
- Lines 149-150: The wording is confusing here “the model can reduce the prior penalty less than significantly than the standard KL”
- Line 152: “overestimate” should be “overestimated”
- Line 216: There is a missing space between “inA.3”
- Line 233: $p_\varphi$ should be $q_\varphi$, I believe.
- Line 239: $p_\varphi$ should be $q_\varphi$, I believe.
- Line 269: $d\mathbf{z}$ should be removed from equation 12.
- Lines 404-405: These lines are written in a slightly confusing way. It sounds like the $\alpha$ value is what the baseline corresponds to. But the baselines use $\alpha = 0$ / $\alpha=1$ right?
- Lin 783: Should be $\alpha \rightarrow 1$ in the parentheses
- Table 1,Table 2, and Table 3 captions have duplicated $\uparrow$’s and $\downarrow$’s

### W14: Move Table 4 to the start of the appendix.
Not a real weakness, just a suggestion. Feel free to ignore it.

### Questions
### Q1: Gradient of Renyi divergence is potentially misleading
Is the argument here potentially incorrect/misleading since the the gradient needs to also be taken with respect to the $q_\varphi(\mathbf{z\mid X_C, Y_C) \approx p(\mathbf{z})$?

### Q2: In A.3, doesn’t the logic from Eq 20 to 21 require that the prior is well specified?
Does this equality hold without this assumption?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Rényi Neural Processes (RNP), a simple method that replaces KL divergence (KLD) with Rényi divergence (RD) to improve the neural process (NP) when there is prior misspecification. They propose RD-based objective functions for both commonly used NP objectives - Variational Inference (VI) in latent NP and Maximum Likelihood (ML) in conditional NP. The authors also provide theoretical analysis and proofs to support their proposed objective functions. In the experimental section, they implement RNP across multiple NP variants and demonstrate consistent improvements over the original models.

### Strengths
* The proposed method is simple yet effective, and can be easily deployed to other NP models by simply replacing the corresponding objective functions. This makes the method highly practical.
* The paper is overall well-written, with thorough literature review and clear, intuitive figures that effectively convey the key concepts.
* The paper employs a comprehensive set of baselines covering both CNP and NP variants, including the current state-of-the-art TNP method. The evaluation is also conducted on two real-world datasets, showing its practical applicability. Besides, the authors provide guidance for choosing $\alpha$, along with several ablation studies.
* They provide theoretical analysis connecting VI and ML objectives through the $\alpha$ parameter, and prove how RNP helps with prior misspecification.
* Their approach to rewriting the ML estimation as minimizing the KLD between the empirical distribution and the model distribution, and then applying RD is an interesting perspective.

### Weaknesses
I am still trying to understand the definition of prior misspecification in your paper, it seems to lack clarity and consistency, and there appears to be a disconnect between the theoretical motivation and experimental validation.

Based on the introduction and the definition of RD, prior misspecification is presented as the mismatch between context and target sets, which commonly occurs when collecting context data with additional noise or other uncontrollable factors.
However, the toy examples and experimental setups seem to address a different type of prior misspecification - the mismatch between training and test distributions ($D_{train}$ and $D_{test}$), which is more akin to domain shift problems.

These are arguably two distinct scenarios, and the paper doesn't clearly explain:

* How these two types of misspecification relate to each other
* Why RD would help with the domain shift scenario
* Whether these can be unified under a single framework of prior misspecification

If I have misunderstood any points, I would appreciate clarification from the authors, and I am willing to increase my score if my concerns are fully addressed.

Some other points:
* In Section 7.1, the experiments are conducted on seemingly well-specified datasets, yet the RD-based methods still outperform the baselines. Is there any justification explains these improvements?
* Line 229, ANP uses attention that learns to attend to the contexts relevant to the given target, to my understanding they didn't incorporate dependencies between target points, maybe you are talking about GNP[1] which models the target points jointly?
* Line 242, TNP has three versions, you are talking about TNP-A (autoregressive version), for example, TNP-D doesn't do any autoregressive prediction. And I think you are using TNP-D in the experiment section.
* Line 311, isn't the posterior distribution be $p(z|X_t, Y_t, X_c, Y_c)$ as you mentioned in eq.3?
* Line 352, TNP has an inappropriate reference, Maraval et al., 2024 only apply TNP to the BO setting.

### Questions
* In Table 1, are you using ML or VI objectives for your RD-based loss functions?
* I am not very sure how and why you are calculating the log-likelihood on the context set. What data are you conditioning on when predicting the context set?
* On TNP-D, the results using $L_{RNP}$ are always better than using $L_{ML}$ in Table 1, why on the EMNIST dataset (Table 2), the results become worse?

### Soundness
2

### Presentation
3

### Contribution
2
