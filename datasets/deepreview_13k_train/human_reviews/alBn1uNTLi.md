# Stabilizing the Kumaraswamy Distribution

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
Large-scale latent variable models require expressive continuous distributions that support efficient sampling and low-variance differentiation, achievable through the reparameterization trick. The Kumaraswamy (KS) distribution is both expressive and supports the reparameterization trick with a simple closed-form inverse CDF. Yet, its adoption remains limited. We identify and resolve numerical instabilities in the inverse CDF and log-pdf, exposing issues in libraries like PyTorch and TensorFlow. We then introduce simple and scalable latent variable models based on the KS, improving exploration-exploitation trade-offs in contextual multi-armed bandits and enhancing uncertainty quantification for link prediction with graph neural networks. Our results support the stabilized KS distribution as a core component in scalable variational models for bounded latent variables.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper  resolves numerical instabilities in the KS inverse CDF and log-pdf, improving implementations in libraries like PyTorch and TensorFlow. The authors leverage the stabilized KS distribution in scalable models, demonstrating improved exploration-exploitation trade-offs in contextual multi-armed bandits and enhanced uncertainty quantification in graph neural networks. These contributions position the stabilized KS distribution as a key tool for bounded latent variables in variational models.

### Strengths
The paper's strengths lie in its originality in addressing numerical instabilities in the KS distribution. While the idea is simple, resolving these issues unlocks the KS distribution's potential in applications like contextual multi-armed bandits and graph neural networks, enhancing exploration and uncertainty quantification. The work is of high quality, with validation and clear exposition, making it an impactful contribution to bounded latent variable modeling. Although the solution is quite simple, I do think it has important impact in the domain.

### Weaknesses
The key weakness of the paper is the lack of direct evidence quantifying the impact of numerical instability on performance outcomes in the experiments. While the authors resolve known instabilities in the KS distribution, it is unclear how these instabilities previously affected results or how the stabilization improves them. I see the empirical resutls,but I do not understand how. Specifically, the paper does not show a comparison of training with and without the stabilization method, which would clearly demonstrate the benefit of the proposed approach. The absence of such a comparison makes it difficult to assess the practical significance of the numerical stabilization. Furthermore, the paper does not provide a detailed analysis of the specific scenarios where the numerical instability is most pronounced, such as specific parameter ranges or model configurations. This lack of analysis makes it challenging to understand the limitations of the original KS distribution and the scope of the proposed solution. It is also unclear if the proposed method introduces any new limitations or trade-offs.

### Questions
The figures lack sufficient information in their titles and captions to guide readers effectively. In particular, Figure 2 is unclear, as the plot and the meaning of the colors are not well-explained, making it difficult to interpret.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
- This work proposes a numerical computation method to stabilize the inverse CDF and log-pdf of Kumaraswamy distribution in deep learning libraries. 
- Due to the numerical instability of $\log (1 - \exp (x))$ term, the previously implemented Kumarsawmy distribution has inaccurate pdf and inverse CDF, which is leading to producing corrupted reparameterized samples. 
- The authors combine two functions, log(-expm1(x)) and log1p(-exp(x)), to re-formulate $\log (1 - \exp (x))$ term and modified the log-pdf and inverse CDF of the Kumaraswamy. 
- Several experiments are conducted to verify the usage of the modified Kumaraswamy.

### Strengths
Due to capturing stability during numerical computation, the Kumarswamy can be better utilized in various tasks in the deep learning community.

### Weaknesses
While the proposed method enlarges the utilization of the Kumaraswamy, the impact and novelty of the work are limited to a single distribution.

The modified Kumaraswamy should be properly compared with the current Kumaraswamy in the experiments.

### Questions
Is there any way to quantitatively compare the modified Kumaraswamy against the previous Kumaraswamy? Such empirical evidence would be required for the comparison.

I guess this can extend some previous works [1,2], as the Beta can be extended to the Dirichlet, right? The extension will definitely strengthen the work.

[1] Stirn et al., A New Distribution on the Simplex with Auto-Encoding Applications, 2019. 

[2] Joo et al., Dirichlet Variational Autoencoder, 2020.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work identifies and discuss a way to fix numerical instabilities that appear when evaluating the (gradient of the) density and quantile function of the Kumaraswamy (KS) distribution. The authors demonstrate that the computation of $\log(1 - \exp(x))$ is the one that suffers from numerical instabilities due to catastrophic cancellations when $x \rightarrow 0$ and thus $\exp(x) \approx 1$ and underflows. They then employ the numerical approximations from Mächler, which rely on Taylor expansions, to bypass these difficulties and express all computations of the (gradient of the) KS density and quantile function in terms of those. In this way, the authors argue that the KS distribution is stabilized which then allows it to be used as a modelling choice in various settings: image modelling with VAEs, contextual multi-armed bandits and variational link prediction in graph neural networks.

### Strengths
* The stabilisation trick is very simple and the primitives (`expm1()` and `log1p()`) are already present in various frameworks. This has the potential of rapid adoption in practical settings.
* Apart from some specific parts on the VBE section, the paper is well presented and written. The authors clearly demonstrate the numerical instabilities, how they manifest and how the proposed modifications can avoid them. 
* The tasks that the authors use to evaluate the behaviour of the KS distribution against other alternatives are quite diverse.

### Weaknesses
 * The novelty of this work is a bit limited. As far as the stabilisation is concerned, while the idea of numerically stable computation is important, the numerical stability is ensured by techniques proposed in the prior work of Mächler. Therefore, in my opinion, the main new insight and novelty of this work is in the benchmarking and the various tasks that the authors considered to test the viability of the KS distribution against other baselines.

* Given the aforementioned, I will thus put more weight on the experimental evaluation. This brings me to the second key weakness; while the authors do consider various other methods for modelling bounded RVs, they are missing the critical baseline of the binary concrete distribution [1] (which is a bit odd, given that they mention in passing the concrete dropout method at the conclusion section). If one treats both the temperature and the  $\alpha$ as free parameters, the binary concrete distribution can have similar representation capacity as the Beta and KS distributions (shown at Figure 1). Furthermore, the authors of [1] also discuss potential numerical instabilities when evaluating the density of the binary concrete and also present in the appendix ways to avoid them via reparametrization (i.e., considering the logistic noise as the random variable and then treating the sigmoid as a downstream invertible transformation). Therefore, this method would also satisfy the criteria that the authors argued for, i.e., supporting the reparametrization trick, provide sufficient expressiveness and offer simple distribution-related functions that are fast and accurate to evaluate.

* The (lack of) comparison against the "simple" fix of clamping is also a weakness, as that would better highlight the improvement against the prior way of stabilising the KS distribution, besides the benefit of eliminating a hyperparameter. The authors do mention that the ranges from prior work did not work, but how difficult is to find an appropriate range? What makes the clamping approach impractical for high dimensional spaces? The constraints are applied elementwise and thus are trivial to implement and enforce, no matter the amount of latent variables. Therefore, finding, e.g, a single $\min$, $\max$ constraint that leads to numerical stability should be straightforward.

* If the architectures are also contributions from this work, then more experiments are needed to highlight their importance. For example, why not try the VBE in a recommender system setting (as the authors suggest in the rebuttal) to verify its importance as a specific architecture (independent of the KS modeling assumption)? A similar comment can be made for the VEE; the authors should compare with, e.g., the VGAE as that would better highlight the importance of the modeling assumptions of VEE (again, independent of the KS assumption).

### Questions
Given the strengths and weaknesses mentioned above, I am leaning on the negative side for this work. Some specific questions and remarks that the authors could work on to improve the work are

* The main remark is to include the concrete distribution along with the suggestions for numerical stability discussed at [1] in the evaluation of all tasks considered. This would provide a good amount of information and would allow one to better determine whether the KS distribution is significant for modelling bounded RVs. 
* While the authors do show that the KS distribution can be unstable for specific values of the input, they do not really show whether these happen naturally in the tasks considered. Do distribution parameters such as the ones shown in Figure 3 appear in the tasks considered later in the paper? If yes, how does the simple fix from Nalisnick et al. 2016 (i.e., clipping the KS parameters) perform in terms of downstream performance on the tasks considered? This would better highlight the true performance delta of better handling the numerical difficulties. 
* For the VBE section, the notation can be improved. There is a $\tilde{z}$, that is for the random sample from the variational posterior over the Bernoulli parameters, and a $z$ that is used for both the ground truth Bernoulli parameter of the bandit arm and the latent variable governed by the variational posterior. I would suggest that the authors separate the last two (e.g., use $q(z_k|x_k)$ for the variational posterior but then use something like $v_a$ for the ground truth Bernoulli parameter) as otherwise the $a = argma{x}_k \tilde{z}_k$, $r\sim Ber(z_a)$ can be confused as taking the payoff from the variational posterior and not the ground truth model.
* For the results at Table 1 I would suggest to the authors to report either the ELBO or approximate log-likelihoods computed by importance sampling (with a sufficient number of samples) and the variational posterior as a proposal. Using a single sample to compute the test LL can be noisy (and there are no error bars at Table 1).
* At line 400 the authors mention the “posterior predictive” as $p(A) = \int p(A|Z)p(Z)dZ$ which is not the posterior predictive but rather the prior predictive / marginal likelihood. The posterior predictive should be $p(A|X, D_tr) = \int p(A|Z)q(Z|X,D_tr)$.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces modifications to the Kumaraswamy distribution to improve its numerical instability.

### Strengths
The analysis of identifying the instability is interesting enough. Also, the modification of the distribution makes sense a lot.

### Weaknesses
 - However, given that large-scale problems are more related with their network capacity and the data, rather than the distribution modeling itself, I doubt if this modification could be benefit to the large-scale training. For example, let's focus on Section 4.1 with Image VAE. Could the authors provide additional argument why do we need this algorithm given that the diffusion model is all based on the normal distribution? I'm more like, why do we need this algorithm given that there is already some well-developed algorithm with another approach? Can we compete with diffusion models with this distribution? I understand different approaches could perform differently, and I'm not completely opposing different approaches. But what I don't see is the practicality of this algorithm.

### Questions
-

### Soundness
3

### Presentation
3

### Contribution
2
