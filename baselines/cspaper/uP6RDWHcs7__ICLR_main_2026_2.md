---
job_id: 373e560d-478c-4af1-af4e-7895d929f41d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: uP6RDWHcs7.pdf
paper: Marginal Flow: A Flexible and Efficient Framework for Density Estimation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies generative modeling, density estimation, variational objectives, manifold-supported distributions, and simulation-based inference.

## Minimum Quality
Pass ✅. The submission contains the expected components, including abstract, introduction, related work, methodology, experiments with quantitative and qualitative results, and a conclusion. While I have substantial concerns about novelty, evaluation, and some technical claims, these are review-time issues rather than desk-reject-level deficiencies.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Marginal Flow, a density estimation framework that defines \( q_\theta(x) \) as a Monte Carlo marginal over parameters \( w \) of a simple conditional density \( q(x\mid w) \), where \( w=f_\theta(z) \) and \( z \sim p_{\text{base}} \). The authors emphasize that the model supports exact density evaluation, single-step sampling, unconstrained architectures for \( f_\theta \), and lower-dimensional latent manifolds by choosing \( \dim(z) < \dim(x) \). Empirically, the paper evaluates the approach on synthetic 2D densities, reverse-KL training, simulation-based inference, Wishart-mixture modeling on SPD matrices, and low-dimensional manifolds in VAE latent spaces for MNIST and JAFFE.

## Strengths
The paper has a simple and intuitive core construction. Writing the model as
\[
q_\theta(x)=\frac{1}{N_c}\sum_{i=1}^{N_c} q(x\mid w_{\theta,i}), \qquad w_{\theta,i}=f_\theta(z_i),\ z_i\sim p_{\text{base}},
\]
makes the computational story easy to follow. Unlike many flow papers, the method does not depend on invertibility, Jacobian determinants, or ODE solves, and this is communicated clearly already in Section 2.

I found the flexibility argument reasonably compelling at the modeling level. The framework can swap the parametric family \(q(x\mid w)\), and Section 4.3 gives a concrete example with Wishart components for SPD matrices rather than forcing everything through Euclidean Gaussian assumptions. That is a useful design point.

The visual exposition is effective in a few places. In particular, **Figure 2** is a helpful diagram of the three operations, sampling \(w_i\), evaluating \(q_\theta(x)\), and sampling from \(q_\theta(x)\). It directly supports the authors' efficiency narrative because it makes clear that the expensive operations common in normalizing flows are absent from the forward path. Likewise, **Figure 1** communicates the intended distinction between optimizing a finite set of mixture components and resampling them from a learned generator; even if I have reservations about how sharp this distinction really is, the figure itself does a good job of illustrating what the authors want the reader to notice.

The runtime comparison is potentially interesting. **Figure 3** suggests large practical speedups for density evaluation and competitive sampling speed. If these numbers hold under fair matched settings, this is a relevant point for users who genuinely need exact density values rather than approximate surrogates.

There is some breadth in the experimental coverage. The paper does not stop at 2D toy plots, it also includes reverse-KL training, SBI, SPD-valued data, and latent-manifold examples for images. Even though I think some of these sections are underdeveloped, the scope is broader than many submissions in this area.

I also appreciate that the paper at least attempts to discuss estimator bias and variance in Appendix A.5-A.7, rather than asserting Monte Carlo exactness without qualification. I will note below that this discussion is not integrated well enough into the main paper, but the fact that the authors are aware of the nested Monte Carlo issue is a positive sign.

## Weaknesses
1. **The central “exact density” claim is overstated, or at minimum insufficiently qualified in the main paper.**  
   This is the biggest issue for me. The paper repeatedly claims “exact density evaluation” in the abstract, Table 1, Section 2.2, Figure 3, and the conclusion. However, the model actually defined in **Equation 2** is
   \[
   q_\theta(x) := \frac{1}{N_c}\sum_{i=1}^{N_c} q(x\mid w_{\theta,i}), \qquad w_{\theta,i}\sim q_\theta(w),
   \]
   with the \(w_{\theta,i}\) resampled. For finite \(N_c\), this is a Monte Carlo estimator of the marginal in **Equation 1**,
   \[
   q(x)=\mathbb{E}_{w\sim q_\theta(w)}[q(x\mid w)],
   \]
   not the exact marginal itself. The exact marginal is an expectation over \(q_\theta(w)\), while the implemented quantity is a sample average. This distinction matters because many of the training objectives involve \(\log q_\theta(x)\), so the estimator is nested and biased. The appendix explicitly acknowledges this in **Equations 17-21**, where the log-based KL estimator has \(\mathcal{O}(1/N_c)\) bias. That directly undercuts the unqualified “exact density evaluation” language in the main paper. At best, one can say the component density \(q(x\mid w)\) is tractable and the marginal can be estimated unbiasedly before taking logs, but the paper currently presents a stronger claim than it has established.

2. **The paper is not sufficiently clear about what differentiates Marginal Flow from a learned infinite or implicit mixture model, and the novelty relative to that family is under-argued.**  
   Conceptually, the method is very close to sampling mixture parameters from an implicit generator and averaging tractable experts. The paper positions the key difference as “marginalization rather than optimizing a fixed finite set of components” in Section 2.1 and illustrates this in **Figure 1**. But this is not yet a strong novelty argument by itself. Mixture models with generated component parameters, kernel mixtures, and latent-variable marginalizations are well-known ideas; the paper needs a sharper statement of what is fundamentally new here. Is the contribution primarily a particular amortized infinite-mixture parameterization? A practical recipe for density estimation with tractable kernels and implicit parameter generators? A theory result? Right now the framing occasionally reads as if resampling alone transforms a mixture model into something categorically different, which is too strong. The authors need to position more precisely against prior work on mixture density networks, kernel mixtures, surjective/injective manifold density models, and latent-variable marginals.

3. **The experimental evidence is broad but often not deep enough to support the strongest claims, especially “orders of magnitude faster” and “state-of-the-art.”**  
   The strongest quantitative evidence visible in the main paper is actually limited. **Table 1** is not an empirical comparison, it is a high-level checklist, and several entries are debatable or at least oversimplified. For example, “Efficient training” and “Free-form Jacobian” compress many nuanced design tradeoffs into binary symbols. This table is fine as intuition, but not as evidence.  
   More importantly, the SBI section in **Section 4.2** claims state-of-the-art results, yet the main paper provides no table, no figure, no per-task breakdown, and no uncertainty summary there; the actual benchmark results are deferred to the appendix (**Figure 14**). Since the review should be based on the main paper, that makes the claim under-supported in the paper itself.  
   Similarly, the runtime claim in **Figure 3** depends heavily on architecture choices, implementation details, batch size, and the choice of \(N_c\), but the main paper gives too little detail to assess fairness. A method that evaluates a mixture over \(N_c\) components can easily become expensive when \(N_c\) grows, so runtime comparisons are meaningful only when target quality is matched. The paper does not convincingly establish iso-quality comparisons.

4. **Several comparisons against baselines are not fully fair or are insufficiently substantiated.**  
   In the multimodal experiment of **Figure 5**, the caption states that all models use a uniform base distribution “for a fair comparison.” I am not convinced that forcing the same base family across architectures is the right fairness criterion when some baselines are designed to benefit from different base choices or more standard training protocols. More broadly, for multiple claims the paper relies on qualitative figures rather than controlled quantitative comparisons with tuned baselines.  
   The manifold experiment in **Figure 4** is visually appealing, but the conclusion “Free-form Flow learns an incorrect manifold and is not able to embed the density in 2D space” versus “Marginal Flow perfectly learns the density and discovers the correct manifold” is stronger than what can be inferred from one toy example. For such a central claim, I would expect either a quantitative manifold recovery metric or at least repeated trials.  
   In **Figure 7**, convergence is compared by plotting test log-likelihood during training, but the horizontal axis alone is not enough to support “orders of magnitude quicker” unless wall-clock time, number of function evaluations, and comparable hyperparameter budgets are all handled carefully. Training-iteration curves do not automatically imply runtime efficiency.

5. **The treatment of \(N_c\) is too loose, even though it is central to both accuracy and efficiency.**  
   The paper repeatedly says \(N_c\) is “not required to be fixed” and that modeling capacity is not directly linked to \(N_c\). That is too casual. In practice, finite \(N_c\) is exactly what determines the variance of the density estimator and a large part of the runtime. This is not a cosmetic hyperparameter, it is central to the method. The appendix confirms this through the \(1/N_c\) bias and variance terms in **Equations 20-21**. Yet the main paper does not provide a systematic ablation over \(N_c\), nor guidance on how one should select it to trade off estimator variance, runtime, and approximation quality. Without this, the efficiency and exactness narrative is incomplete.

6. **The mathematical exposition around objectives and optimization is incomplete in the main paper, and some notation/claims are potentially misleading.**  
   The paper says in Section 2.3 that Marginal Flow “can be trained efficiently with most objectives; see Appendix A.2.” But the main paper itself does not define the actual training losses. This matters because the log-likelihood objective for the marginalized model is not the same as likelihood for a fixed mixture, and because the reverse KL objective requires sampling \(x\sim q_\theta(x)\) while also evaluating \(\log q_\theta(x)\) with the same Monte Carlo marginal. The statistical properties of this nested estimator are not a side detail, they are part of the core method.  
   Also, in **Equation 2**, the notation \(q_\theta(x)\) is overloaded between the ideal marginal and its Monte Carlo approximation. A cleaner presentation would distinguish the true marginal \(q_\theta^\star(x)=\mathbb{E}_{z}[q(x\mid f_\theta(z))]\) from its finite-sample estimate \(\hat q_{\theta,N_c}(x)\). This would avoid the paper repeatedly oscillating between the conceptual model and the implemented estimator.

7. **Some theoretical discussion in the appendix appears too specialized and disconnected from the main contribution, while the main theoretical gap remains unaddressed.**  
   The appendix proves bias/variance statements for a nested Monte Carlo estimator and then gives **Theorem A.3** about dependence on intrinsic dimension \(m\) rather than ambient dimension \(d\), under assumptions that seem quite restrictive, including a local factorization argument around a manifold and the simplifying assumption \(z^\*=0\). Even if the theorem is correct under those assumptions, it does not support the main broad claims of the paper as currently written. The main unresolved issue is not whether a specific penalty term avoids explicit dependence on \(d\) under a stylized setting, it is how the finite-\(N_c\) estimator affects training and density evaluation in realistic regimes. The paper is spending theory budget in a direction that is less central than the actual methodological questions.

8. **The literature positioning on manifold and dimensionality-changing exact-likelihood methods is incomplete.**  
   The paper mentions some work on manifold flows and injective/surjective constructions, but the discussion is fairly selective given how strongly the paper markets “exact density on lower-dimensional manifolds.” There is prior work specifically on exact density estimation with dimensionality change and manifold-supported data, including surjective/injective flow variants and specialized manifold density models. Because the manifold capability is one of the headline contributions, the related work should engage more carefully with those lines, especially where the differences are exactness assumptions, support of the measure, and computational tradeoffs. As written, the paper risks giving the impression that lower-dimensional exact-likelihood density modeling is largely absent from prior literature, which is not accurate.

9. **The image-latent experiments are interesting qualitatively, but scientifically weak in their current form.**  
   In **Figures 10 and 11**, the authors show smooth traversals in VAE latent spaces for MNIST and JAFFE and claim disentanglement-like behavior. These figures are visually pleasant, but they do not establish much beyond interpolation quality in an already learned VAE latent space. Since the VAE is trained first and the manifold is learned afterwards, it is hard to disentangle how much of the observed structure comes from Marginal Flow versus the upstream latent representation. There are no quantitative metrics for reconstruction error, conditional likelihood, manifold quality, or disentanglement. On JAFFE, the sample size is tiny, which the authors acknowledge, but then the evidence should be framed as a proof-of-concept rather than as a substantive empirical result.

10. **Some claims are too sweeping for the level of evidence provided.**  
   Examples include “overcomes these limitations altogether” in the abstract, “orders of magnitude faster than competing models both at training and inference,” “perfectly learns the density” in several figure captions, and “state-of-the-art results” in SBI without main-paper evidence. This style is not fatal by itself, but here it compounds the core issue that the method is an estimator-based marginal model whose quality depends on \(N_c\), optimization, and the chosen kernel family \(q(x\mid w)\). A more restrained claims section would make the paper more credible.

## Questions
1. The most important clarification I need is about the “exact density” claim. Do the authors mean exact evaluation of the finite mixture conditioned on sampled \(\{w_i\}_{i=1}^{N_c}\), or exact evaluation of the ideal marginal
   \[
   q_\theta^\star(x)=\mathbb{E}_{z\sim p_{\text{base}}}[q(x\mid f_\theta(z))]?
   \]
   If the latter, how is that expectation computed exactly rather than estimated by Monte Carlo? A precise notation split between \(q_\theta^\star(x)\) and \(\hat q_{\theta,N_c}(x)\) would substantially increase my confidence.

2. Please provide a main-paper ablation on \(N_c\). I would like to see quality versus runtime for several \(N_c\) values, ideally on both forward-KL and reverse-KL training, and preferably compared at matched test likelihood or matched reverse KL. This is central to understanding whether the method remains attractive once estimator variance is controlled.

3. Can the authors better position the method relative to learned mixture models, mixture density networks, and dimensionality-changing exact-likelihood approaches such as surjective/injective flow variants? I am not asking for a survey, but I do need a sharper explanation of what is methodologically new beyond “resample components from an implicit generator.”

4. For **Figure 3**, please clarify the exact settings used in the main text, not only the appendix: architecture sizes, \(N_c\), batch sizes, dimensionalities, and whether comparisons are done at approximately matched modeling quality. Without iso-quality comparisons, speed numbers are hard to interpret.

5. For the SBI claim in **Section 4.2**, can the authors summarize the actual benchmark numbers in the main paper, for example with a table or compact figure, and include the baselines compared against? This would materially change my confidence in the application-side significance.

6. For the manifold experiment in **Figure 4**, is there a quantitative manifold-recovery metric or repeated-trial statistic? The current result is visually suggestive but too anecdotal for such a prominent claim.

7. In the reverse-KL setup, does training use the same Monte Carlo sample set to both sample \(x_j\sim q_\theta(x)\) and evaluate \(\log q_\theta(x_j)\), or are these decoupled? Please clarify the estimator used in practice, because variance and bias can change noticeably depending on reuse of samples.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arose from the content of the paper. The work is a methodological contribution in density estimation and probabilistic modeling, and the presented applications do not introduce obvious privacy, fairness, safety, or legal-compliance issues within the scope of the submission.

## Soundness Rating
2: fair. The core method is plausible and several empirical results are promising, but the main technical claims, especially around “exact density,” are not stated with enough precision and the evidence is not yet strong enough to support the broad conclusions.

## Presentation Rating
3: good. The paper is readable and the figures are generally effective, especially Figures 1-3. However, some claims are overstated, the main-paper experimental presentation omits key details, and the mathematical distinction between the ideal marginal and its finite-\(N_c\) estimator should be made much clearer.

## Contribution Rating
2: fair. There is an interesting practical idea here, and the flexible use of tractable component families is appealing, but the current positioning and evidence do not yet convince me that the contribution rises clearly above a useful but incremental reformulation of implicit mixture modeling.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a nice simple idea and some compelling qualitative demonstrations, but the overclaim around exact density evaluation, incomplete novelty positioning, and underdeveloped quantitative support make it fall short of ICLR bar in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main formulation and the paper’s central claims, and the main source of uncertainty is not misunderstanding the method, but rather how much additional clarification or stronger evidence the authors can provide in rebuttal.