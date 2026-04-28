# MF-LAL: Drug Compound Generation Using Multi-Fidelity Latent Space Active Learning

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 8, 3, 5

## Abstract
Current generative models for drug discovery primarily use molecular docking as an oracle to guide the generation of active compounds. However, such models are often not useful in practice because even compounds with high docking scores do not consistently show experimental activity. More accurate methods for activity prediction exist, such as molecular dynamics based binding free energy calculations, but they are too computationally expensive to use in a generative model. To address this challenge, we propose Multi-Fidelity Latent space Active Learning (MF-LAL), a generative modeling framework that integrates a set of oracles with varying cost-accuracy tradeoffs. Unlike previous approaches that separately learn the surrogate model and generative model, MF-LAL combines the generative and multi-fidelity surrogate models into a single framework, allowing for more accurate activity prediction and higher quality samples. We train MF-LAL with a novel active learning algorithm to further reduce computational cost. Our experiments on two disease-relevant proteins show that MF-LAL produces compounds with significantly better binding free energy scores than other single and multi-fidelity approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel framework called Multi-Fidelity Latent Space Active Learning (MF-LAL) for de novo drug design. The primary challenge addressed is the generation of drug compounds with real-world biological activity, a task complicated by the limitations of current evaluation methods. Generative models often rely on molecular docking as an oracle to guide compound generation, but docking scores do not consistently correlate with experimental activity. Authors state that more accurate methods like molecular dynamics-based binding free energy calculations exist but are computationally prohibitive for large-scale generative tasks.
MF-LAL proposes integrating multiple oracles of varying fidelity level, each with different accuracy and computational cost, into a single generative modeling framework. Unlike previous approaches that separately train the surrogate model and the generative model, MF-LAL combines them, allowing for more accurate activity predictions and higher-quality sample generation. The framework employs a novel active learning algorithm to efficiently select which oracle to query at each step, further reducing computational overhead. Experimental results on two disease-relevant proteins demonstrate that MF-LAL outperforms both single and multi-fidelity baseline approaches in producing compounds with better binding free energy scores.

### Strengths
This work addresses one of the most important problems in de novo drug design, the translational efficiency that oracles transmit to the generation process. 

The hierarchical latent space, each corresponding to a fidelity level, is a clever design choice. This allows the model to specialize the latent representation for each fidelity, improving both surrogate modeling and the quality of generated compounds.

The use of SELFIES is really appropriate for this setup as this work is not focus on broader chemical exploration.

The introduction of a likelihood-based term in the generation objective is a smart technical trick. Specifically, when generating a molecule at fidelity level \(k\), the model maximizes the likelihood that this molecule would also be generated at fidelity level \(k-1\) with a high property score.

Surrogate models \(\hat{f}_k\) are directly trained on their corresponding latent representations \(z_k\), leveraging SVGPs. This integration ensures that the latent spaces are organized to optimize property prediction at each fidelity, enhancing the overall performance of both the generative and surrogate models. The use of SVGPs for surrogate modeling at each fidelity level introduces mathematical robustness. The joint minimization of the ELBO and the marginal log likelihood ensures that the latent representations are well-structured for property prediction

### Weaknesses
The whole technical approach is fantastic. However, this work has some issues conceptually and with the evaluation of its results.

While it's true that the degree of resolution of free binding energies estimation can be higher for some systems, this is taken as a pillar fact in this work while this might not be true. It is of utmost importance to check any physics-based protocols with compounds with known affinity and actually corroborate that the low to high-fidelity methods stand as such. Specifically, the authors should demonstrate a clear correlation between the different fidelity levels and experimental binding affinities for a set of known binders. Without this validation, the assumption that higher fidelity methods are inherently more accurate is not sufficiently justified, and the entire multi-fidelity framework rests on shaky ground.

To that end, authors select 15 compounds for each method and compute ABFE metrics on all of them. However, they base a great deal of their analyses on 3 top scoring compounds per system. When looking at the mean of the 15 compounds generated vs each of the values for the top 3 compounds it's clear to see that they are outliers, which might not be bad per see (it is exactly what a generative campaign is looking for) but must be always followed by a careful analysis of the motifs the molecules generated. Scoring functions of any type, docking or ABFE, are biased towards certain types of chemical structures and assign a high score as a result of highly reactive topologies. For instance, best molecule in BRD4 has an SO2 group, known to be pan-reactive, best molecule in c-MET has an aldehyde group, also known to bind to many chemistries potently. The other two compounds in c-MET have nitro groups, with charges known to be rewarded by scoring functions. While those are valid molecule they would be potentially discarded since they would be considered artifacts.

Also, the approach is lacking from benchmarking the systems on docking and ABFE with compounds known to bind to them. That would give a more solid comparison point for generated molecules.

### Questions
I encourage the authors to address the following:

1. Perform docking and ABFE to known binder compounds.
2. Revisit the docking results taking into account the aforementioned issues.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed a new approach to designing molecules binding to a given target protein. Conventional approaches are mostly based on docking methods which are known to be insufficient for reliable predictions of binding between molecules and a target protein. Absolute biniding free energies (ABFE) are the most accurate prection method for bining affinites, but they are too expensive to apply to many molecules. The authors resolved this problem  by using a novel multi-level fidelity latent space active learning (ML-LAL). The result shows that the proposed method outperformed baseline models. The idea of ML-LAL is new but the benchmark results need to be further justified because of the use of only 15 generated molecules in the evaluation.

### Strengths
1. Latent space active learning combined with generative AI to efficiently query the oracles
2. Multi-fidelity level latent space and decoder at each, leadting to higher accuracy
3. Well compromising between speed and accuracy by reusing the latent information from lower levels on higher levels. 
4. The use of ABFE for prediction is challenging in conventional approches, but this work has used it for evaluation thanks to the relatively high efficiency of the proposed method.

### Weaknesses
1. Only 15 generated compounds have been tested for evaluations, which seems too few to convince conclusions.
2. The mean and top 3 values of the 15 generated molecules have large differences,
3. Training at the highest fidelity level is terminated not by the training error threshold but the total computational time. Thus, no systematic convergence for a given target can be made.
4. Maximizing the likelihood that the molecule would also be generated at fidelity k−1 with
a high property score apparently limits exploration space, and the oracle at the lowest level is likely to misguide the searching spot due to its poor accuracy. This might be the reason for the high variance (especially a large gap between mean and top 3 values) in the predicted properties of 15 generated molecules. Moreover, as shown in Table 2, the top 3 results w/o likelihood term are not significantly lower than with it.

### Questions
1. Maximizing the likelihood that the molecule would also be generated at fidelity k−1 with
a high property score apparently limits exploration space, and the oracle at the lowest level is likely to misguide the searching spot due to its poor accuracy.  This might be the reason for the high variance (especially a large gap between mean and top 3 values) in the predicted properties of 15 generated molecules. Moreover, as shown in Table 2, the top 3 results w/o likelihood term are not significantly lower than with it. The authors need to elaborate on the potential effect of using the likelihood constraint (eq 3) on constraining the exploration.
2. Using only 15 generated compounds is too few to evaluate statistically meaningful performance, which casts doubt on the conclusions. In particular, the top 3 values strongly rely on sampling. The authors may evaluate with more samples or discuss the limitations.
3. Training the proposed model is terminated with a total time limit, which causes an unsystematic convergence criterion.  As a result, the binding affinities of the top 2 and 3 of C-MET are much weaker than the top 1, whereas the top 3 values of BRD4 are in a similar range. The authors need to justify the consequences of their termination criterion (7 days) on the model performance. 
4. The authors define a set of probabilistic decoder networks that translate a latent vector at each fidelity level to a single original molecule. This reviewer wonders about the performance of each decoder in terms of success rates in reconstructing the original molecule. Do they all give the same correct molecule or show different success rates depending on the fidelity level?

### Soundness
2

### Presentation
3

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
The authors introduces an active learning generative learning framework to design novel small molecules (ligands) that are optimized to have high binding affinity to a protein target using a set of oracle functions. Their method uses an increasing hierarchy of oracles, whose output becomes more reliable with higher-fidelity oracles with the downside that the oracle's execution become more computationally expensive.  
The authors propose to use an increasing set (which state the higher fidelity-spaces) of encoder-decoder architecture to embed a ligand from SELFIES-representation to a latent space, and decode the latent representation back for generation purpose. Crucially, the latent representation from the encoder(s), are suitable to train surrogate models for the multiple fidelities with the advantage that gradient-based optimization can be also performed in the latent spaces.  
The authors show that their proposed method which performs active learning on hierarchical latent spaces outperforms current string-based and 3d-based generative models in their experiments on two protein target that are involved in human cancer development.

### Strengths
The paper is well written and motivated by the current methods in the literature which mostly rely on a single oracle function such as docking, without considering higher fidelity and reliable evaluation metrics. Since the usage of higher-fidelity oracles such as computing the absolute binding free energy (ABFE) is costly, approximating those computation with neural networks  as surrogate models is reasonable and brings the advantage that these surrogate models can be used for gradient-based optimization. The active learning component, usually applied in supervised learning, for querying samples from a given dataset with a costly oracle function, is here used for generation purposes where the optimization for promising ligands is done in a hierarchy of latent spaces using gradient-based methods. The authors show that the proposed loss terms for active learning, i.e., the acqusition function and likelihood terms from lower-fidelity levels are necessary for improved evaluation results, which is confirmed in their ablation studies.

### Weaknesses
The comparison to the 3d generative model Pocket2Mol is not fair since no optimization is done to sample ligands that have high binding affinity for that method. The (autoregressive) Pocket2Mol model also does not fall into the state-of-the-art for 3d generative anymore, although this method is faster in generation than current diffusion-based models.
I would be interested how the 1d/SELFIES-based MF-LAL framework compares against newer 3d generative models such as DecompDiff [1] or PILOT [2] without applying guidance or calling the oracles, since their methods might not be directly applicable within the multi-fidelity hierarchy.

How is the reconstruction accuracy for the 4 seperate encoder-decoder networks?
The authors wrote in [Line 183-185] that "the use of a specialized decoder for each fidelity level improves reconstruction quality compared to previous methods, that only use one, thus making the generated samples more tailored for their fidelity level".

In the supplementary code base in the main.py, I saw that the weighting coefficient for the KL-prior is set quite low with ~0.08, indicating that the latent space is not really smooth and especially for the first fidelity level $z_1 \sim N(z_1 | \mu_1(x), \sigma_1(x))$ where 200,000 samples are available for training the VAE-1, "holes" in the latent space might appear. Could the author provide reconstruction learning curves over epochs? As the fidelity-level gets higher, the sparser the latent spaces $Z_k, k\geq 2$ become, since first these spaces are trained with less data. Although the authors provide the log-likelihood term of a mixture of Gaussians from previous latents, it is not clear how often a optimized latent $z_k$ can be decoded back to a valid SELFIES string.

### Questions
How is the reconstruction accuracy for the 4 seperate encoder-decoder networks?
The authors wrote in [Line 183-185] that "the use of a specialized decoder for each fidelity level improves reconstruction quality compared to previous methods, that only use one, thus making the generated samples more tailored for their fidelity level".

In the supplementary code base in the main.py, I saw that the weighting coefficient for the KL-prior is set quite low with ~0.08, indicating that the latent space is not really smooth and especially for the first fidelity level $z_1 \sim N(z_1 | \mu_1(x), \sigma_1(x))$ where 200,000 samples are available for training the VAE-1, "holes" in the latent space might appear. Could the author provide reconstruction learning curves over epochs? As the fidelity-level gets higher, the sparser the latent spaces $Z_k, k\geq 2$ become, since first these spaces are trained with less data. Although the authors provide the log-likelihood term of a mixture of Gaussians from previous latents, it is not clear how often a optimized latent $z_k$ can be decoded back to a valid SELFIES string.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a multi-fidelity active learning method to produce molecules with desirable properties, given multiple different oracles with varying costs. The method uses an encoder to embed molecules into a latent space, with stochastic variational Gaussian process (SVGP) models trained for each fidelity. The authors perform experiments on multiple protein targets.

### Strengths
The problem studied by the authors is sensible and important to the field. The method proposed by the authors is, broadly speaking, reasonable (although I describe some weaknesses below). I think the paper is well-written and the presentation is good.

### Weaknesses
I have two main criticisms of the method itself:

1. A key motivation for the method is to  "ensures compounds generated at higher fidelities also scored well at lower fidelities, improving the quality of generated samples." (lines 075-077). This hypothesis seems questionable: why would one want this? The fundamental challenge in multi-fidelity AL is that the observations between different fidelities are not very well-correlated. Is it not possible that most interesting molecules at high-fidelity score poorly at lower fidelities?
2. The method uses SVGPs in quite a few places, which raises concerns about robustness. SVGPs are very sensitive to the location of their inducing points, and tend to overestimate variance away from their inducing points (see <https://arxiv.org/abs/1606.04820>). This means:
  - Line 7 in algorithm 1 may not be implemented accurately if the variance is overestimated
  - The distribution of the initial dataset will likely determine the location of the inducing points, and with the UCB objective it seems plausible that nothing away from the initial distribution will therefore be chosen. At the very least, the behavior will depend enormously on the locations of the inducing points.

Aside from this, I thought the experiments had some significant correctness issues. First and foremost, the results in Table 1 are described as "significant" despite a very small sample size of 15 and considerable variance in the scores of the generated molecules. I think the authors need to apply a statistical test to their results so that the differences between methods can be evaluated more objectively. I understand that the expensive nature of the computations requires a small sample size, but this is _exactly_ the scenario where statistical tests are helpful.

Second, I think the authors are missing a "standard MF-AL" method as a baseline- the most "standard" baselines use VAE-GP models which may not fit the data well. I recommend either an autoregressive GP (ie prior mean for fidelity $k$ is the posterior mean for fidelity $k-1$) or a "co-kriging" model where a single GP has a kernel between inputs and fidelities. EI or UCB could be used as an acquisition function, and the kernel could either be a Matern 5/2 or Tanimoto kernel between molecule fingerprints.

Finally, more broadly the sensitivity of the method to hyperparameters is not discussed or explored. My guess is that the performance is extremely sensitive to parameters like UCB $\beta$ or the locations of the inducing points, and this may prevent the method from being applied successfully in other problems. It would be good to see this discussed more.

### Questions
- Can you describe the method's sensitivity to hyperparameters?
- Can you please explain why one would want molecules which score well at high fidelities *and* low fidelities, instead of only caring about high fidelities?
- Can you comment on the statistical significance of your results?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a multi-fidelity method that integrates the generative modeling of the molecules and the surrogate modeling of the oracles and aims at a trade-off between the docking oracle that is of low fidelity but of cheap computational cost and binding free energy oracle that is of high fidelity but of expensive computational cost. Besides, the author proposes a new criterion during active learning for generating candidate query molecules to the oracles.

### Strengths
* A new criterion for candidate molecule generation during active learning is proposed.
* The author implements diverse baseline methods for comparison with the proposed one and considers multiple sources of oracles.
* Implementation code is provided as proof of reproducibility.

### Weaknesses
 *  The soundness and novelty of the main feature of ML-LAL - " using separate latent spaces and decoders specialized for each fidelity improves surrogate modeling and inter-fidelity information passing"- is questionable. The detailed explanation of my concerns is as follows:
    * The author use a set of random variables $z_{1:K}$, corresponding to $K$ fidelity,  as the latent representation of  molecule $x$. According to the main text, the variational distribution $q(z_{1:K}|x)$ (that approximate true  posterior  $p(z_{1:K}|x)$) is defined by,  $q(z_{k}|z_{k-1})=\mathcal{N}(\mu_k(z_{k-1}),\sigma_k(z_{k-1}))$ where  $z_0=x$ and $k=1,\dots,K$. Enhancing the expressive capbility of  $\mu_k$ and $\sigma_k$  by choosing them the outputs of  neural network $h_k$, the author expects better approximation of $p(z_{1:K}|x)$, thereby so-called "better inter-fidelity information passing". 
        * Defining $F_k(\cdot)=\mu_k(\cdot)+\sqrt{\sigma(\cdot)} \epsilon_k$ with $\epsilon_k\sim \mathcal{N}(0,1)$ and $F'(F(\cdot))=(F'\circ F)(\cdot)$,  then $z_k$ in this paper is represented by $z_k=\mu((F_{k-1}\circ \ldots \circ F_1)(x))+\sqrt{\sigma((F_{k-1}\circ \ldots \circ F_1)(x))} \epsilon_k$.
     * However, we can alternatively represent $z_k$ as $z_k=\mu((h_{k-1}\circ \ldots \circ h_1)(x))+\sqrt{\sigma((h_{k-1}\circ \ldots \circ h_1)(x))} \epsilon_k$ ($h' \circ h$ means stacking the two neural networks). This way, I believe, also enhances the expressive capability of  $\mu_k$ and $\sigma_k$. The key difference is that in the proposed method, noise is added after each transformation $F_k$, whereas in the alternative method, noise is added only at the end of the transformations $h_k$. The proposed method maintains random latent spaces, while the alternative method maintains deterministic latent spaces until the final sampling step.  It is unclear why adding noise at each step is advantageous, as the random latent spaces are created from $\mathcal{N}(0,1)$ and do not integrate further information to help modeling. Theoretical analysis or empirical evidence should be provided to support the claim that the proposed method is superior.
        *  Since $\epsilon_k$ is non-informative, the issue here is that the method considered in this paper, and the method I provide above are conceptually similar, and the latter one means nothing but adding more neural network layers to $\mu_k$ and $\sigma_k$  as $k$ increases, rendering the novelty of the proposed method trivial, and the claimed ''better message passing''  questionable.

* Following the setup of $q(z_k|x)$, the author propose algorithm 2 for efficiently generation of molecules candidates, which is expected to     be of high scores for each fidelity.   However, if we follows the conceptually similar setup I described above, algorithm 2 just reduces to getting a sample batch $\{\hat{\epsilon}^{(i)}\}$ from $\mathcal{N}(0,1)$, and only keeping  the samples $\hat{\epsilon}$ such that  ${z_k}(\hat{\epsilon})$ is of high scores for each $k$. If the samples $z_k=\mu((F_{k-1}\circ \ldots \circ F_1)(x))+\sqrt{\sigma((F_{k-1}\circ \ldots \circ F_1)(x))} \epsilon_k$ can be further optimized w.r.t. surrogates by gradient descent, then it is clear that  $z_k=\mu((h_{k-1}\circ \ldots \circ h_1)(x))+\sqrt{\sigma((h_{k-1}\circ \ldots \circ h_1)(x))} \epsilon_k$ can also be optimized.

* The experiment results are not convincing. The detailed reason is as follows:
    * As acknowledged by the author,  the  goal of multi-fidelity methods is to balance the trade-off between fidelity and computation cost under a fixed computation budget (lines 69-70, algorithm 1).  In this paper, the first oracle, docking activity, is computationally inexpensive but has low fidelity, whereas the second oracle, binding free energy, is computationally expensive but offers higher fidelity. 
    * In this sense, we would like to see a training curve as done in the baseline method[1], where the $y$-axis represents the values of performance metrics, and $x$-axis represents the computation cost until the budget is exceeded.  The best multi-fidelity model is the one that achieves the best performance metrics given a fixed cost, or the lowest cost given a fixed metric threshold. Otherwise, always choosing the high-fidelity source will just give you the best final performance. 
   * However, the author only provides Table 1 in this paper, which summarizes the final performance metric values. This alone is insufficient to support the claimed capability for the trade-off. The figure in Appendix C.1 shows the cost-performance curves when always choosing fidelity 2 and 3 respectively, which can support the correctness of the overall active learning framework, but cannot well support the proposed multi-fidelity method.

* The other claimed feature- "MF-LAL combines the generative and multi-fidelity surrogate models into a single framework(lines 20-21)"- is questionable.
   * While the author claims that workflow in [1] is *separate* (lines 56-58), we note that  the *integrated* workflow of  MF-LAL is similar to [1]. The *integrated* part, which I found in MF-LAL is that in equation (1),  the first term (corresponding to generative part) and the second term (corresponding to surrogate part) are optimized jointly. 
  * However,  since the two terms are **sequential**, where the output of generation part is the input of the surrogate part, there is no big difference whether we optimize it sequentially as described in [1] or jointly as in MF-LAL.  
  * By the way,  **GPs are non-parametric models**[3], and $\lambda_k$ in line 205 is the hyper-parameters of the mean or covariance function. Thus, the second term does not exist when there are no hyper-parameters or hyper-parameters are fixed.  The surrogate modeling of the oracle is commonly referred to as doing posterior inference of $P(f|x,\mathcal{D})$, where $\mathcal{D}$ is the multi-fidelity dataset, rather than fitting the hyper-parameters[4]. 


* Equation (1) is incorrect.  ELBO (Evidence Lower Bound Objective) is the lower bound of log-likelihood of observations, this is $\log p(x)$. So, for example, the first term for $k=1$ should be $\log p(x)=\log E_{z_1}[\frac{P(x|z_1)P(z_1)}{q(z_1|x)}]\geq E_{z_1}[\log \frac{P(x|z_1)P(z_1)}{q(z_1|x)}]$ rather than $E_{z_1}[\log \frac{P(x|z_1)}{q(z_1|x)}]$.  Besides, if $f_k$ in the second term, is a GP (Gaussian Process),  what is the definition of $p(y|f_k)$ ?  (Is $y$ equal to the output of a GP plus additional Gaussian noise? )

* According the Algorithm 1,  the hyper-parameter $\gamma_k$ is crucial as it dictates whether queries are made at the next level of fidelity. Therefore, an ablation study or discussion for how $\gamma_k$ are selected should be provided. We would like to see experiment results under different setups of $\gamma_k$ (i.e. ablation study) rather than simply report a single best choice.


### Questions
* The abstract can be improved. There is a lack of information about  "what is replaced by a surrogate model" ( oracles?) or "why a surrogate model is used".

* There is no definitions or intuitive explanations about what is reverse optimization. This term seems  to be important in the main text.

* In algorithm 2, $z_k^{(i)}$ are samples of random variables. How can samples be further optimized by gradient-descent?

### Soundness
1

### Presentation
3

### Contribution
1
