# Unlocking the Power of Gradient Guidance for Structure-Based Molecule Optimization

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
Structure-based molecule optimization (SBMO) aims to optimize molecules with both continuous coordinates and discrete types against protein targets.
A promising direction is to exert gradient guidance on generative models given its remarkable success in images, but it is challenging to guide discrete data and risks inconsistencies between modalities.
To this end, we leverage a continuous and differentiable space derived through Bayesian inference, presenting Molecule Joint Optimization (MolJO), the first gradient-based SBMO framework that facilitates joint guidance signals across different modalities while preserving SE(3)-equivariance.
We introduce a novel backward correction strategy that optimizes within a sliding window of the past histories, allowing for a seamless trade-off between explore-and-exploit during optimization.
Our proposed MolJO achieves state-of-the-art performance on CrossDocked2020 benchmark (Success Rate 51.3% , Vina Dock -9.05 and SA 0.78), more than 4x improvement in Success Rate compared to the gradient-based counterpart, and 2x "Me-Better" Ratio as much as 3D baselines.
Furthermore, we extend MolJO to a wide range of optimization settings, including multi-objective optimization and challenging tasks in drug design such as R-group optimization and scaffold hopping, further underscoring its versatility and potential.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
MolJO introduces a framework for structure-based molecule optimization that handles both continuous (atomic coordinates) and discrete (atom types) molecular properties through gradient guidance and Bayesian inference. The method achieves state-of-the-art results on the CrossDocked2020 benchmark with a 51.3% Success Rate and 4× improvement over previous gradient-based methods, while maintaining SE(3)-equivariance. Using a backward correction strategy and joint optimization approach, MolJO demonstrates superior performance across various drug design tasks, though currently limited to three main objectives (Affinity, QED, SA).

### Strengths
Technical Innovation: The paper presents an approach to jointly optimize both continuous (atomic coordinates) and discrete (atom types) variables in molecule optimization.

Strong Performance: The method achieves impressive results, showing a 4× improvement over gradient-based baselines and 2× better "Me-Better" ratio than 3D baselines, while maintaining SE(3)-equivariance. The success rate of 51.3% on CrossDocked2020 represents a significant advance.

Practical Application: The method demonstrates strong versatility across real drug design tasks like R-group optimization and scaffold hopping, and effectively balances multiple objectives while generating valid molecular structures. The backward correction strategy also provides a practical way to balance exploration and exploitation during optimization.

### Weaknesses
Presentation: The paper is based on BFNs. A self-contained introduction may help the reader understands the proposed method better. A comparison with discrete diffusion and generative flow net would also be helpful. 

Limited Objective Scope: The method is only validated on three objectives (Affinity, QED, SA) despite the wide range of important molecular properties in drug discovery. The paper does not explore crucial biological objectives or demonstrate how the approach would scale to more objectives.

Computational Analysis Gaps: The paper lacks detailed analysis of computational requirements and efficiency. There is insufficient discussion about how the backward correction window size affects computational costs, and no clear comparison of computational resources needed versus other methods.

Hyperparameter Sensitivity: The method's performance appears sensitive to key hyperparameters like guidance scale and correction window size, but the paper does not provide clear guidelines for selecting these parameters or analyze their impact systematically. This raises questions about the method's robustness in practical applications.

### Questions
How reliable is the oracle for real-world drug discovery? Is the cost of calling the oracle a concern? 

How does the backward correction window size impact performance versus computational cost, and what determines the optimal balance?

Can this joint optimization approach extend beyond the three basic properties (Affinity, QED, SA) to handle more complex molecular properties relevant to drug discovery?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers the gradient guidance of generative models in the structure-based drug design problem. Specifically, this paper proposes a new method that handles both gradients to update the discrete atom token space and the continuous coordinate space. An additional backward correction strategy is proposed to improve the efficiency of the optimization process. Effectiveness of the proposed method is validated over a set of optimization setups including structure-based drug design, multi-objective optimization and substructure-constrained optimization.

### Strengths
* Equipping molecular generative models, in particular diffusion and flow models, with conditional generation and optimization capability is important yet under-studied.
* The proposed backward correction method to balance exploration and exploitation is novel.
* Experiments are conducted on a wide range of optimization setups which show the promise of the proposed method.

### Weaknesses
 * This paper misses a large chunk of literature on molecular optimization, see this review paper [1].
* Some claims in the paper are not appropriate, previous structure-based drug design models also optimize both the atom type and coordinate [2, 3] (gradient-based algorithm and evolutionary algorithm). I am not sure if it is appropriate to call it the *first proof-of-concept for gradient-based optimization of continuous-discrete variables* because (1) the scope is very narrow, (2) other papers have worked on it [2, 3], (3) it is unclear why we have to use a gradient-based method, even for discrete probability distributions, and (4) the "gradient" for the discrete case is not a gradient but a weighting (which can relate to derivative-free optimization/sampling method such as sequential Monte Carlo).
* Some notations are unclear.

### Questions
* What is the parameter $\phi$ and how do you learn it?
* How is the time-dependent energy function learned? Since you only know the property when $t=0$.
* What are $\mu$ and $y$ in proposition 4.1? $\theta$ was first defined as $[\mu, z]$ but later defined as $[\mu, z = f(y)]$ while $f$ is not defined.
* In eq. 8, it is a little confusing gradient over $y^*$ vs proposition 4.1 gradient of $y$.
* In eq. 8, how is the chain rule performed? What is the dependence of E over $\mu$ vs $h$?
* What is $\sigma'$?
* One more suggestion is to have a broader discussion of related work about conditional generation in diffusion/flow models.
* The backward correction idea is interesting, does it also connect to the resampling trick or restart sampling? [1, 2]
* In eq. 12, by the linearity of Gaussian, what's the difference between predicting $\hat{x}$ from $\theta_{i-1}$ vs $\theta_{i-2}$?
* I am happy to raise my score if the authors clarify some of my concerns.

[1] Lugmayr, A., Danelljan, M., Romero, A., Yu, F., Timofte, R. and Van Gool, L., 2022. Repaint: Inpainting using denoising diffusion probabilistic models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 11461-11471).

[2] Xu, Y., Deng, M., Cheng, X., Tian, Y., Liu, Z. and Jaakkola, T., 2023. Restart sampling for improving generative processes. Advances in Neural Information Processing Systems, 36, pp.76806-76838.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper deals with generative models for molecules. Specifically, it proposes a way to improve generation quality by using gradient guidance, based on a specified energy function, for both continuous and discrete variables (atoms’ positions and types, respectively). The paper builds on Bayesian Flow Networks, which operates on some continuous latent variables, which facilitates guidance across both data modalities.

### Strengths
The authors tackle the problem of applying gradient guidance jointly for discrete and continuous variables in the context of molecule generation. This is a challenging task, as naively applying gradient guidance to discrete variables is not possible. I think this problem is quite relevant, as proper use of different guidance techniques has been observed to lead to improved performances across many domains.

To the best of my knowledge, the method proposed by the authors, which relies on Bayesian Flow Networks and applying guidance in some underlying continuous variables, is novel. And empirical results appear to be strong.

### Weaknesses
While I understand the core idea and problem in the paper, I find the details hard to follow, including exactly what variables represent and how are the update rules obtained. Please see the “questions” section below for extended details.

I’m having difficulties following the method’s explanation, what variables represent, and how updates and equations are derived. A few examples below:

- [BFN in preliminaries.] “The receiver holds a prior belief $\theta_0$, and updates…” Exactly what does $\theta$ represent? Is it pointwise parameters, is there a distribution defined over them?

- [BFN in preliminaries.] Eq (1) shows a distribution over $\theta_i$, but eq. (2) shows $\theta$ as a deterministic variable (given observations y_0, …, y_i). I understand Eq (1) is the posterior given a datapoint $x$, integrating out potential observations, but Eq (2) represents the deterministic updates we get for some given observations at different noise levels?

- The parameters $\theta$ are fed through a NN to model output distribution over clean data. Why is it sensible to apply guidance over theta (if they are connected to the clean samples through a NN, and the energy is typically defined over clean samples)? Coming back to the question above, what do these latents represent? 

- [Proposition 4.1.] Is $\mu_\phi$ an output of the NN $\Phi(\theta_{i-1})$? Also, in the definition of $\theta$ (line 201) $\theta=[\mu, z]$ you use $z$, but Eq (6) uses $y$, stating “recall $z=f(y)$”. I suppose this comes from Eq (2)? Are $y$ the noisy observations? If so, why is Eq (6) sampling $y$? (Should it be sampling $z$ which is part of $\theta$?) The relationship between $y$, $z$, and $\theta$ needs to be clarified, especially in the context of the sampling process.

- [Proposition 4.1.] Where are the original Gaussians from line 207 coming from (in-line equations, just before Eq (5))? Why are those the correct “unguided kernels” $p_\phi$?

- After reading section 4.1, it is unclear to me how samples are actually generated by the model without using backward correction. The forward process is not sufficiently clear, and the connection to the sampling procedure is missing.

- [Line 233.] This line uses the notation $e_v$ without definition. $e_v$ is defined later in line 240. I’d suggest to introduce variables before using them in equations. That same paragraph states “Surprising as it may seem, this is mathematically grounded…” in which way? The mathematical grounding of the discrete variable sender distribution needs further elaboration, and the connection to the continuous variable case should be made more explicit. The current explanation lacks sufficient detail to understand the claim.

I know some of these questions are not related to the core method but are more general. But I think it would be good for the paper to be self-contained. Asking for a fully fledged description of BFNs in the main paper may be unrealistic, but introducing the necessary components, even briefly, that lead to the equations being used later on, would be good. Unfortunately, I cannot recommend acceptance for the paper in its current form. I’m open to revisiting my score if the paper is updated addressing these general comments (or if they are clarified during the discussion, if I’m missing/misunderstanding something).

A few additional questions.

- [Prop 4.1.] “it suffices to sample guided … [guided Gaussians]”. These expressions are based on a 1st order Taylor expansion. Would these become increasingly exact as the updates become smaller? (Related to the discretization used?) I think the approximation used here could be briefly discussed in the main text, as it is claimed before, in line 192, that the analytic expressions for the guided kernels are derived. The implications of this approximation on the quality of the generated samples should be discussed.

- [Detail in Line 187.] The definition of $\pi(\theta_i | \theta_{i-1})$ should have a $\propto$ instead of $=$? If $p_\phi$ and $p_E$ are both normalized, their product is not necessarily normalized. For instance, consider the product of two Gaussian densities, the resulting thing is not normalized.

### Questions
I’m having difficulties following the method’s explanation, what variables represent, and how updates and equations are derived. A few examples below:
 
- [BFN in preliminaries.] “The receiver holds a prior belief $\theta_0$, and updates…” Exactly what does $\theta$ represent? Is it pointwise parameters, is there a distribution defined over them?

- [BFN in preliminaries.] Eq (1) shows a distribution over $\theta_i$, but eq. (2) shows $\theta$ as a deterministic variable (given observations y_0, …, y_i). I understand Eq (1) is the posterior given a datapoint $x$, integrating out potential observations, but Eq (2) represents the deterministic updates we get for some given observations at different noise levels?

- The parameters $\theta$ are fed through a NN to model output distribution over clean data. Why is it sensible to apply guidance over theta (if they are connected to the clean samples through a NN, and the energy is typically defined over clean samples)? Coming back to the question above, what do these latents represent? 

- [Proposition 4.1.] Is $\mu_\phi$ an output of the NN $\Phi(\theta_{i-1})$? Also, in the definition of $\theta$ (line 201) $\theta=[\mu, z]$ you use $z$, but Eq (6) uses $y$, stating “recall $z=f(y)$”. I suppose this comes from Eq (2)? Are $y$ the noisy observations? If so, why is Eq (6) sampling $y$? (Should it be sampling $z$ which is part of $\theta$?)

- [Proposition 4.1.] Where are the original Gaussians from line 207 coming from (in-line equations, just before Eq (5))? Why are those the correct “unguided kernels” $p_\phi$?

- After reading section 4.1, it is unclear to me how samples are actually generated by the model without using backward correction.

- [Line 233.] This line uses the notation $e_v$ without definition. $e_v$ is defined later in line 240. I’d suggest to introduce variables before using them in equations. That same paragraph states “Surprising as it may seem, this is mathematically grounded…” in which way?

I know some of these questions are not related to the core method but are more general. But I think it would be good for the paper to be self-contained. Asking for a fully fledged description of BFNs in the main paper may be unrealistic, but introducing the necessary components, even briefly, that lead to the equations being used later on, would be good. Unfortunately, I cannot recommend acceptance for the paper in its current form. I’m open to revisiting my score if the paper is updated addressing these general comments (or if they are clarified during the discussion, if I’m missing/misunderstanding something).

A few additional questions.

- [Prop 4.1.] “it suffices to sample guided … [guided Gaussians]”. These expressions are based on a 1st order Taylor expansion. Would these become increasingly exact as the updates become smaller? (Related to the discretization used?) I think the approximation used here could be briefly discussed in the main text, as it is claimed before, in line 192, that the analytic expressions for the guided kernels are derived.

- [Detail in Line 187.] The definition of $\pi(\theta_i | \theta_{i-1})$ should have a $\propto$ instead of $=$? If $p_\phi$ and $p_E$ are both normalized, their product is not necessarily normalized. For instance, consider the product of two Gaussian densities, the resulting thing is not normalized.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper tackles the problem of structure-based molecule optimization (SBMO), i.e. a problem of generating candidate 3D molecules conditioned on a target protein. In contrast to structure-based drug design (SBDD), the generated molecule is also optimized for certain properties. The authors follow related work and model this problem using Bayesian Flow Networks (BFNs), which are designed to capture mixed modalities (discrete atom types and continuous 3D coordinates). The novelty introduced by the authors are (1) gradient guidance, which allows for explicit optimization of properties of interest, and (2) backward correction strategy, which corrects past estimates based on a current optimized one. The authors perform multiple experiments showing superiority of their method compared to various baselines on a variety of different tasks.

### Strengths
* I think that the application of gradient guidance to SBMO is a good idea;
* Comprehensive list of baselines;
* Comprehensive list of evaluation tasks.

### Weaknesses
1. **Unclear contributions.** The authors claim two main contributions:  (1) Gradient guidance in BFNs with mixed modality applied to SBMO and (2) novel backward correction strategy. Given some of the related work, I do not consider the contributions large enough for a full ICLR paper. Specifically:
  * BFNs have already been applied to 3D molecule modeling [2] and even to structure-based drug design [3, 4] (Note that authors do not cite [4], which is very strongly related to this work and definitely should be discussed).
  * It has been shown that BFNs can be seen as SDEs [1] and therefore it is well-known how to apply guidance there (both classifier-based and classifier-free). The authors should have explored this direction and shown that their approach is superior to the direct application of SDE guidance.
  * The novel backward correction strategy seems to me to be a slight modification of the one suggested in [3].
  * Even the generative "backbone" model is taken from [3] as is without any modifications.
2. I would rather characterize this work as "finetuning" of [3]. Specifically, my assessment of the contributions is:
  * the application of guidance to a pre-trained model (from [3])
  * a slight modification of the variance reduction technique, where instead of the full past, a sliding window is taken (again from [3])
3. **Presentation needs improving.**
  * Some sentences are incomprehensible to me, such as
    * Line 182 "Though different from guided diffusions that operate on noisy latent y, this guidance aligns with our generative process conditioned on θ". What does it mean that guidance aligns with the generative process? This sentence is vague and lacks a clear explanation of the underlying mechanism.
  * The introduction of guidance is the central component of the paper. However, we learn that the method "requires training energy functions as a proxy" in the last paragraph of the paper! I do not understand why the paper is not mostly discussing the energy proxies and how are they defined/trained/evaluated etc. Furthermore, simply adding an energy proxy to any of the baselines would surely improve their performance. Even a modification as simple as: generating multiple candidates and choosing the best one using the energy proxy.
  * I do not understand what Figure 2 is supposed to convey. There is no "take-home" summarizing message. In the text (lines 314-316) we read "it succeeds in balancing sample quality (explore) and optimization efficiency (exploit)". I do not see that in Figure 2. Why is sample quality called "explore"? How is Figure 2 supporting the claim about the tradeoff? The colored lines to me seem random and without any clear pattern.
4. **Lack of mathematical rigor.**
  * Line 187 definition of $\pi$. Is it a purely heuristics based definition? Regular guidance is derived from the Bayes' rule applied to the conditional log density (conditioned on some property of interest). What about this formulation? This is just a multiplication of two densities without an elaboration. 
  * Proposition 4.1. I don't understand which parts of the proposition are assumptions and which are the claims. What does it mean that "originally" $\mu_i$ follows a Gaussian? 
5. **A very strong objection I have is to the experimental design.** In my opinion it is impossible to assess the quality of the work without more information:
  * What are model sizes (the model proposed by the authors including all its components: the main model, energy proxies, and anything else that needs to be trained; and compare with model sizes of the baselines)
  * What is the training time? (Your method vs baselines)
  * What is the sampling time? (Your method vs baselines)
  * You include your method with a beam search. Perhaps other generative methods would perform even better when equipped with the beam search sampling strategy? It is unclear why the authors chose to use beam search for their method and not for others.
  * Optimization-based baselines. I strongly encourage the authors to include AutoGrow4 [5] as optimization-based baseline. It has been recently reported to work significantly better than RGA [6] (different version of the Vina software was used in that study - has a different range of Vina Dock values)
6. **Reproducibility is questionable.** The code is submitted, but there are no trained model checkpoints provided, so I cannot check the parameter count myself, nor check sampling time or verify the reported results.

### Questions
* In Line 420 we read "Note that for fair comparison, we restrict the size of generated molecules by reference molecules so that both generative models and optimization methods navigate the similar chemical space," - this in particular means that you use the ground-truth information about the size of the reference molecule? I genuinely appreciate the authors reporting this explicitly. However, this brings a very important question: is this applied to all methods? Were the numbers for all baselines generated by the authors (as opposed to taking them from the publications) with this modification?
* line 052 I do not see this as a weakness of DecompOpt. Some tasks require specific tools.
* Line 077 There's no citation around "gradient guidance" What do authors mean? Classifier-free guidance? Classifier-based guidance? Something else? Based on the later reference, I assume the authors mean classifier-free guidance. However, based on the later parts of the paper I think it is something else.
* Line 87 What are the suboptimal results? E.g. MoFlow [1] adopts this approach and achieves very good empirical performance
* Line 102 what issue of inconsistencies?
* Line 138 just because something is unusual does not mean it cannot work well in practice. See [1] again.
* Line 141 - "often a problematic assumption" Citations? I am aware of works that use this assumption and work well in practice, i.e. [2] again.
* Line 366 - Is the purpose of Figure 3 to show that the introduction of guidance results in a distribution shift? I think that's to be expected. To me, that's rather a sanity check than a strong insight. It would perhaps be more interesting to see how this plot compares with optimization-based methods?
* Figure 5: Why not Vina Dock? I think this one is the most important—also no error bars or statistical significance tests.
* Table 4: What happened to Vina Dock?
* I would like to know more about the "energy proxies":
    * How large are these models - each energy proxy is as large as the TargetDiff model? This seems to make the baseline comparison unfair.
    * What are their sampling times?
    * How accurate are they?
    * How are they trained? Appendix C I think hints at it, but it seems incomplete (equation 21). How is $\theta$ defined for the training purposes? I assume that the protein-ligand complexes are sampled according to the $p_{\text{data}}$ distribution, but how are they then transformed to obtain $\theta$?
* Line 522 typo: "gradiant" -> "gradient"

---
[1] Zang et al "MoFlow: an invertible flow model for generating molecular graphs" (KDD 2020)

### Soundness
1

### Presentation
2

### Contribution
1
