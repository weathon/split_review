---
job_id: 1e9551c8-760c-4bff-8640-254ba72cf226
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: hQZQVLJrH9.pdf
paper: A Unified First-Order Framework for Activation Steering and Data Influence
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining interpretability, representation-level interventions, influence functions, and learning theory for neural networks.

## Minimum Quality
Pass ✅. The submission includes the required scientific components, namely Abstract, Introduction, methodological/theoretical development, experiments with quantitative results, related work, and conclusion. While I found notable soundness and clarity issues, they do not rise to the level of an obvious desk rejection based on the main paper alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious formatting, or text aimed at manipulating automated review.

# Expected Review Outcome:
## Summary
This paper proposes a first-order framework connecting activation steering and training-data influence. The core claim is that, under local linearization, an activation-space perturbation at a chosen layer can be mapped to a signed reweighting over training examples, and conversely, an infinitesimal influence-style parameter update can be represented by a minimum-norm steering vector through a pseudoinverse construction called Influence-Aligned Steering (IAS).

On top of this equivalence, the paper introduces an alignment diagnostic based on principal angles between the activation-reachable and parameter-reachable logit subspaces, derives a spectral direction for maximal first-order change under a norm budget, and presents a low-rank steering generalization bound. Empirical illustrations are provided on GPT-2 Medium for detoxification and layerwise alignment, and on ResNet-50 for the spectral-direction claim.

## Strengths
The paper tackles a genuinely interesting bridge between two lines of work that are usually discussed separately, namely activation steering at inference time and influence-based training-data attribution. Framing both as first-order sensitivity objects is conceptually neat, and the central minimum-norm construction in **Section 3**, especially **Equation (2)** / **Theorem 5.2**, is easy to recognize as the natural pseudoinverse solution to matching a target logit displacement via activation edits.

I also appreciate that the paper does not stop at the algebraic mapping and tries to extract operational consequences. The alignment quantity $\gamma(x)$ in **Section 5.1** gives a concrete diagnostic for when steering should or should not be expected to imitate parameter-space effects. That is one of the stronger aspects of the paper, because it turns a vague intuition into a checkable condition. In particular, **Figure 2** is useful: the monotone increase of median $\gamma$ with layer depth supports the claim that later layers are more favorable for steering-based approximation. Even though the empirical evidence is limited, the figure is at least aligned with the paper’s geometric story and helps motivate the practical heuristic of probing several layers before committing to one.

The paper is also relatively broad in scope. It includes optimization, geometry, and a small amount of learning theory. The spectral construction in **Theorem 5.3** is a reasonable attempt to replace hand-chosen steering directions with something principled, and **Figure 3** gives a visually interpretable sanity check that the proposed spectral direction is not behaving like a random edit direction in the ResNet-50 experiment.

The paper is readable at a high level. The introduction clearly states the motivation, the notation in **Section 2** is mostly standard, and the authors do make an effort to connect theory to practice through cost statements and workflow recommendations.

## Weaknesses
I found the paper promising in idea but materially below ICLR bar in its current form, mostly because several central claims are either overstated relative to what is actually proved, or only weakly supported empirically.

1. **The headline equivalence claim is stronger than what the math in the main paper really supports.**  
   The abstract and introduction repeatedly say that activation steering and influence are equivalent “to first order,” and **Theorem 4.2** is presented as a steer-influence equivalence in both directions. But the actual result is qualified by multiple strong assumptions and residual terms: span conditions over $\{\mathcal I(z \to x)\}_{z \in \mathcal Z}$, feasibility of matching $\mathrm{Im}(J_{\theta\to y})$ inside $\mathrm{Im}(J_{h\to y})$, small-edit assumptions, and the residual controlled by $\gamma(x)$ on **Page 4**. In other words, what is established is not a blanket equivalence between the two paradigms, but an equivalence only after projection into a compatible first-order subspace, plus additional assumptions on the attainable span of influence vectors. That distinction matters a lot scientifically, because the stronger framing suggests a unification of mechanisms, while the actual result is closer to “some first-order logit displacements can be matched through a minimum-norm activation edit under favorable subspace geometry.”

2. **Several mathematical statements are underspecified or too informal for claims of this breadth.**  
   The derivation around **Lemma 4.1** and **Theorem 4.2** is especially thin. For example, the theorem states there exists a signed measure $\rho_{\mathbf s}$ with $\|\rho_{\mathbf s}\|_1 = |\alpha|$, but the construction of $\rho_{\mathbf s}$ is never written explicitly in the main paper, only described intuitively as arising from gradient correlation. That is not enough for a theorem that also claims minimality and converse existence. Likewise, the converse part, “any signed weighting $\mathbf w$ ... admits a steering vector $\mathbf s_{\mathbf w}$,” is a strong statement, but the conditions under which the corresponding first-order output shift lies in $\mathrm{Im}(J_{h\to y})$ are not spelled out carefully in the theorem statement itself. The main text mixes exact equality, approximate equality, and residual bounds in a way that makes it hard to know which parts are unconditional and which depend on span assumptions.

3. **There are concrete notation and indexing issues that make the technical presentation less trustworthy than it should be.**  
   A few examples: on **Page 3**, the pseudoinverse solution is labeled as **Equation (2)**, but **Equation (2)** was already used on **Page 3** for the steering logit shift $\Delta y^{\mathrm{SV}}(x)=J_{h\to y}(x)(\alpha s)$. On **Page 4**, the residual bound is tagged as **(3)** even though **Theorem 5.1** later presents what appears to be the main alignment inequality; the text also alternates between “Eq. equation 4,” “equation 3,” and regular numbering. These may look cosmetic, but they matter here because the paper relies heavily on cross-referencing theorem statements, assumptions, and residual conditions. Sloppy equation bookkeeping makes it substantially harder to verify exactly what is being claimed where.

4. **The optimization and “spectral optimality” claim in Theorem 5.3 is not stated with sufficient precision to be verifiable.**  
   The theorem says that the steering vector maximizing the expected first-order logit change is the top eigenvector of $\Sigma$. But “expected first-order logit change” is not formally defined as a scalar objective in the main text. Logit change is vector-valued in general, so maximizing it requires specifying a direction, a norm, or some quadratic form. The claimed optimum value, $B\sqrt{\lambda_{\max}(\Sigma)}\,\|\nabla_h f_\theta(x)\|$, introduces $\nabla_h f_\theta(x)$ even though $f_\theta(x)\in\mathbb R^m$ is vector-valued; unless the authors mean the Jacobian, a specific logit coordinate, or some scalarized score, the expression is not well defined. This is not a minor nitpick, because **Theorem 5.3** is presented as a core contribution and motivates **Figure 3**. Right now, the theorem reads like a plausible spectral recipe, but not a rigorously specified optimization result.

5. **The “generalization under low-rank steering” section is not convincingly connected to the actual intervention studied in the rest of the paper.**  
   In **Theorem 6.1**, the steered model is written as $\hat f = f_\theta + \alpha U V^\top$, described as “adding a rank-$k$ IAS correction at layer $\ell$.” However, the rest of the paper formulates steering as adding an activation perturbation $\alpha s$ at inference time for a given input, not modifying the model globally by a low-rank parameter correction. These are not the same object. An input-dependent activation edit is not obviously representable as a fixed additive rank-$k$ model perturbation, and the theorem appears to import a bound from low-rank layers without proving that IAS interventions satisfy the theorem’s premises. This weakens the paper substantially because it advertises a generalization guarantee for steering, while the main text does not close the gap between test-time activation edits and the low-rank function-class perturbation analyzed.

6. **The no-free-lunch statement in Theorem 6.2 appears too strong as written.**  
   The theorem states that if $\gamma(x)\le \rho<1$, then for every activation perturbation $\Delta h$ and corresponding parameter perturbation $\Delta \theta$,
   \[
   \frac{\|J_{h\to y}(x)\Delta h\|_2}{\|J_{\theta\to y}(x)\Delta \theta\|_2}\le \gamma(x)\le \rho.
   \]
   This quantification is unclear. What exactly is the “corresponding” parameter perturbation? If it is arbitrary, the inequality cannot hold uniformly; if it is chosen as the best-matching parameter perturbation for a particular target displacement, then the theorem needs to define that optimization explicitly. As written, the statement overreaches and risks confusing subspace projection geometry with a universal amplitude bound. This matters because the theorem is used to justify the practical recommendation “skip steering entirely” when $\gamma$ is small.

7. **The empirical evidence is too thin to support the scope of the claims.**  
   The paper makes broad claims about a unified framework for “billion-parameter models” and practical workflows, yet the main experiments are very small: GPT-2 Medium in one detoxification setup, a scatter plot for local first-order matching, a layerwise $\gamma$ plot, and a single ResNet-50 class-direction example. That is not enough to establish robustness of the theory across architectures, tasks, or intervention regimes. In particular, the detoxification experiment in **Table 1** is not favorable to the proposed method: IAS is worse than CAA on both reported metrics, toxicity (0.0164 vs 0.0150) and perplexity (13701 vs 13291). If the proposed method is supposed to replace or systematize hand-crafted steering, the most prominent table should not show it underperforming the baseline on both axes without a careful explanation of why the method is still preferable.

8. **The experimental analysis is under-interpreted, and in places it undercuts the paper’s own claims.**  
   **Figure 1** is intended to validate first-order equivalence, but the reported slope is 1.50, not close to 1. A cosine of 0.978 does show strong collinearity, but it does not show calibrated matching of magnitude. If predicted and actual shifts differ by 50% in scale, then “IAS matches influence at first order” is too generous a caption. At minimum, the paper should separate directional agreement from magnitude agreement and discuss whether the mismatch is systematic, due to second-order terms, damping, or measurement protocol. Right now, the figure supports “same direction in a small regime” much better than “matched effect.”

9. **The cost claims are optimistic and insufficiently substantiated.**  
   On **Pages 2-3**, the paper says the workflow requires “only two backward passes per input,” a rank-$d$ pseudoinverse, and small SVDs. That description suppresses the expensive part of influence estimation, namely applying $(H+\lambda I)^{-1}$ or even its Gauss-Newton surrogate at scale. The paper notes damping and surrogate choices, but the actual computational burden of Hessian inverse approximations is central to whether the proposed pipeline is realistic. This is particularly important because the paper repeatedly sells the framework as practical and scalable. Without timing, memory, or approximation-quality analysis, the practicality story is incomplete.

10. **Some assumptions are strong enough that they deserve either empirical examination or sharper discussion, but the paper mostly treats them as if they were routine.**  
   The assumptions in **Section 2** include feasibility, local smoothness, and affine independence. The affine independence assumption is especially strong in high-sample regimes and directly underlies the $\ell_1$-minimality statement in **Corollary 1**. Yet there is no empirical sense of whether these assumptions hold even approximately in the reported setups. Similarly, the local linear regime is acknowledged, but there is no systematic sweep over steering magnitude $\alpha$ to show where the first-order approximation breaks down. Given that the entire framework depends on infinitesimal or small edits, this missing stress test is a serious gap.

11. **The literature positioning is somewhat narrow relative to the paper’s own framing.**  
   The paper cites standard influence-function and activation-steering references, but the related-work section on **Page 8** is quite compressed given the breadth of the claims. The paper repeatedly claims to provide the first closed-form map and an optimal-control view, yet it does not spend enough effort distinguishing itself from neighboring activation-editing and model-editing formulations that also connect geometry, control, and low-rank interventions. For a theory paper making a unifying claim, sharper positioning is needed.

12. **Presentation quality is uneven despite the appealing high-level narrative.**  
   The paper is readable in broad strokes, but several proofs are only sketched, theorem assumptions drift between sections, and cross-references are messy. This is one of those submissions where the top-level story sounds cleaner than the actual technical specification. For a paper whose main value proposition is mathematical clarity, that gap is costly.

## Questions
1. For **Theorem 4.2**, can the authors provide the explicit construction of $\rho_{\mathbf s}$ in the main-paper notation, not only an existence statement? In particular, what is the exact linear system or optimization problem whose solution yields $\rho_{\mathbf s}$, and under what conditions is $\|\rho_{\mathbf s}\|_1 = |\alpha|$ guaranteed?

2. Please clarify the precise objective optimized in **Theorem 5.3**. What is the scalar quantity being maximized when you say “expected first-order logit change”? If the output is vector-valued, are you maximizing a norm, a projection onto a chosen class logit, or a quadratic form? I think this theorem needs a more precise statement to be checkable.

3. For **Theorem 6.1**, how exactly does an input-dependent activation edit $\alpha s$ correspond to the fixed low-rank model perturbation $\alpha U V^\top$ used in the bound? If the theorem is only about a different class of interventions, please say so explicitly. If it is meant to apply to IAS as formulated earlier, please provide the missing reduction.

4. Can the authors discuss **Figure 1** more carefully? A cosine of 0.978 is strong, but a slope of 1.50 suggests a substantial scale mismatch. Is the intended claim directional agreement only, or true first-order magnitude matching? A rebuttal clarifying this point would increase my confidence.

5. Why does **Table 1** show IAS underperforming CAA on both toxicity and perplexity under the same $\ell_2$ budget? If the goal is not to beat CAA on raw detoxification quality, please articulate more clearly what practical advantage IAS offers in this setup, beyond interpretability of the direction.

6. The practical scaling story would be more convincing with at least one experiment showing the effect of damping $\lambda$, approximation quality of $(H+\lambda I)^{-1}$, or runtime cost. Can the authors provide this in rebuttal, even briefly?

7. Since the whole framework is explicitly first-order, can the authors add an ablation over steering magnitude $\alpha$ to show when the approximation starts to fail? This seems essential for connecting the theory to practical steering regimes.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper explicitly discusses tracing steering directions back to “causal training documents” and inspecting top-weighted examples for “bias or privacy leaks” in **Section 4**. That capability is scientifically interesting, but it also raises privacy and misuse questions, especially if applied to memorized or sensitive training data. In addition, activation steering is discussed in the broader context of suppressing or eliciting behaviors, and cited prior work includes adversarial or harmful-use directions. The paper itself does not present an overtly unsafe system, but the methodology could plausibly be used both for safety interventions and for targeted manipulation or extraction-style analyses. I do not think this blocks publication, but it merits ethics-aware handling.

## Soundness Rating
2: fair. The central idea is interesting, but multiple theorem statements are underspecified or stronger than what is fully justified in the main paper, and the empirical evidence is limited relative to the paper’s scope.

## Presentation Rating
2: fair. The high-level story is understandable, but technical exposition is uneven, with ambiguous theorem statements, notation/cross-reference issues, and not enough precision in key derivations.

## Contribution Rating
2: fair. The paper offers a potentially useful conceptual bridge, but in its current form the contribution is weakened by incomplete technical grounding and experiments that are too limited, with the main benchmark table not demonstrating a compelling empirical advantage.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a compelling unifying premise and some potentially useful geometric diagnostics, but the current version overclaims relative to its proofs, leaves key constructions underspecified, and does not empirically validate the framework strongly enough for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in the assessment, have checked the main technical claims and equations carefully, and the main reasons for my rating are specific rather than impressionistic.