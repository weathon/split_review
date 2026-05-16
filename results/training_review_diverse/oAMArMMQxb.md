Now I have all the information needed. Let me write the consolidated review after careful verification of all claims.

## Summary

This paper proves that the vanilla score function (without annealing or noise-conditioning) can be used to sample from multimodal distributions — specifically mixtures of strongly log-concave components — provided the Langevin chain is (a) initialized from the empirical distribution of a small number of training samples and (b) stopped early, before it reaches its stationary distribution. Theorem 1 provides finite-sample guarantees in total variation distance. The paper also contributes a new bound on the log-Sobolev constant of well-connected mixtures (Theorem 2) that improves on prior work by handling arbitrary numbers of components under milder assumptions (pairwise overlap rather than bounded χ² divergence). The theory is illustrated with 1D and 32D simulations.

## Strengths

1. **First theoretical guarantee for vanilla score matching on multimodal distributions.** Theorem 1 directly addresses a well-known limitation: vanilla score matching provably fails for multimodal distributions in the standard long-run sampling regime. The paper shows that data-based initialization + early stopping overcomes this, answering the open question posed in the abstract. Even for the unimodal case, the result is new (Remark after Theorem 1).

2. **Novel bound on the log-Sobolev constant of a mixture via pairwise overlap (Theorem 2).** The bound $C_{LS}(\mu) \leq \frac{C_{|I|,p_*}}{\delta} \max_i C_{LS}(\mu_i)$ for mixtures whose components form a connected overlap graph at threshold $\delta$ is a nontrivial technical contribution. The paper correctly notes that prior work either required bounded χ² divergences (which can be infinite, e.g., for non-isotropic Gaussians) or handled only two components. This result may be of independent interest.

3. **Clear and well-motivated proof structure.** The high-level strategy — splitting into overlap regimes, using an overlap graph decomposition, induction on the number of components to handle the general case, and handling discretization and score error via Girsanov's theorem — is clearly laid out. The motivating example (zero-initialization failure, Remark after the proof sketch) effectively illustrates why data-based initialization is necessary.

4. **Simulations consistent with the theory.** Figures 1 and 2 show the predicted behavior: early-stopped Langevin with data-based initialization produces samples close to the ground truth at intermediate times, while both the empirical distribution (T=0) and the stationary distribution (T=∞) are far from the target.

## Weaknesses

### Fatal
None.

### Major
1. **The required $\epsilon_{\text{score}}$ accuracy is extremely stringent and its achievability is not discussed.** Theorem 1 requires  
   $\epsilon_{\text{score}} \leq \tilde{\Theta}\!\left(\frac{p_*^{1/2}\,\epsilon_{TV}^4}{(\beta\kappa^2 K e^{K})^2 d^{3/2} T^{3/2}}\right)$,  
   where $T$ itself is $\tilde{\Theta}\!\left((\exp(K)d\kappa/(p_*\epsilon_{TV}))^{O_K(1)}\right)$. This means $\epsilon_{\text{score}}$ must be astronomically small — polynomially small in $d$ and $\epsilon_{TV}^{-1}$, but with exponents that compound through the $T$ dependence. The paper references prior work to argue that vanilla score matching can achieve small $L_2$ error for certain model classes (exponential families, Remark \ref{def:eps-score}), but it does not address whether the *specific* required $\epsilon_{\text{score}}$ can be provably attained with polynomially many samples in the same regime where the theorem is meaningful. While the exact-score case ($\epsilon_{\text{score}}=0$) is already a new result, for the learned-score setting the condition risks being vacuous. The paper should at minimum provide a concrete example (e.g., two well-separated Gaussians) with explicit, non-asymptotic parameters to demonstrate a plausible operating regime.

### Minor
1. **Dependence on the truncation radius $R$ is not made explicit.** The low-overlap analysis assumes the distribution is supported on a ball of radius $R$, with the paper stating this is handled "rigorously in the supplement using concentration" (proof sketch). However, the mixing time and step-size constraints in the sketch depend on $R$, and for $d$-dimensional Gaussians, typical samples lie at distance $\Theta(\sqrt{d})$ from the mean. Whether the concentration argument introduces a $\sqrt{d}$ factor, a $\log d$ factor, or something worse is not clarified in the main text. The remark that dependence is "polynomial or logarithmic" for constant $K$ is reassuring but does not directly address how $R$ enters. A brief comment on the final $d$-dependence after removing the support assumption would be valuable.

2. **The "bad set" argument for $L_2$ score error is sketched at a high level.** The transition from an $L_2$ guarantee to pointwise control on the trajectory (defining $B_{\text{score}}$, using Girsanov to bound the probability of hitting it, and then using Markov's inequality to lift from initialization at $\mu$ to initialization at $\nu_{\text{sample}}$) is described only conceptually. These are standard techniques, but the sketch omits several nontrivial steps (e.g., how the size of the bad set is controlled given only an $L_2$ guarantee, the coupling argument across discrete steps). The full proof is in the appendix, but the sketch as presented does not allow the reader to assess whether these steps compound in a manageable way.

3. **Theorem 1's bounds are stated in $\tilde{\Theta}$ notation with dependencies that are difficult to interpret.** The functional forms for $T$, $h$, $\epsilon_{\text{score}}$, and $M$ involve nested $O_K(1)$ exponents and $\tilde{\Theta}$ notation that obscures the polynomial degrees. A simplified corollary for the constant-$K$ case (e.g., $K=2$) with explicit exponents would significantly improve readability and help the reader assess whether the bounds are reasonable.

### Trivial
None.

## Nice-to-Haves

- A short paragraph returning to the "computational hardness of denoising" motivation from the introduction, explaining how the theorem's results apply in those hard regimes (e.g., the sparse spiked Wigner model example).
- A remark about the *metastable* regime intuition — where the chain mixes within each component but has not yet transitioned between components — to help the reader understand what "early stopping" means qualitatively.
- Explicit computation of a concrete example (e.g., two separated isotropic Gaussians) with the suppressed constants in the $\tilde{\Theta}$ notation filled in for a specific $d$, $\epsilon_{TV}$, and $M$.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Complaint about commented-out text in Section 2.** The reviewer noted "large commented-out (a page of) text near the end of Section 2" as distracting. These are LaTeX comment blocks that do not appear in the compiled PDF; they are parser artifacts from the source extraction. **(REMOVED per formatting artifact rule.)**
- **Criticism that simulations are too minimal.** The reviewer noted the simulations cover only one or two configurations. The paper is a theoretical contribution; the simulations are explicitly presented as proof-of-concept illustrations. Evaluating the paper against the standard of an experimental paper's simulations would be evaluating it against the wrong class of expectations. **(REMOVED per wrong-class rule.)**
- **Complaint that the full proof is relegated to the appendix, making it impossible to verify from the main text.** The reviewer states "the main text alone does not contain enough detail to certify the proof." This is the normal division of labor for theoretical papers with appendices. The substantive concerns about specific gaps (R dependence, ε_score, bad set) are retained above; the generic complaint about appendix deferral is removed. **(REMOVED per missing-appendix rule — the appendix exists in the original submission.)**

## Novel Insights

The reviews surface an important tension: the paper's central idea (data-based initialization + early stopping rescues vanilla score matching) is genuinely novel and well-motivated, but the quantitative bounds are complex enough that the reader cannot easily gauge whether the theorem operates in a meaningful parameter regime. The Harsh Critic's concern is not about correctness but about *interpretability* — the $\tilde{\Theta}$ notation hides substantial polynomial dependencies, and the $\epsilon_{\text{score}}$ condition may be so stringent that it undermines the practical significance of the result even if the proof is correct. This is a recurring pattern in first-generation theoretical guarantees for sampling: the bounds are often too pessimistic to match the regimes where the methods actually work in practice. The paper would benefit from acknowledging this transparency gap more explicitly (e.g., by computing the bound for a simple explicit example), which would not change the theorem's truth but would help readers calibrate their expectations.

## Suggestions

- Provide a **simplified corollary** for the case $K=2$ (or constant $K$) with all $\tilde{\Theta}$ dependencies expanded into explicit polynomial forms. This would let readers see, for example, whether $\epsilon_{\text{score}}$ scales as $d^{-c}$ or $\exp(-d)$ and whether $\epsilon_{\text{score}}$ is achievable with $\text{poly}(d)$ samples.
- Add a **concrete worked example** (e.g., two isotropic Gaussians with separation $\Delta$) where the required $M$, $h$, $T$, and $\epsilon_{\text{score}}$ are computed numerically for a specific $(d, \epsilon_{TV})$ pair, with suppressed constants instantiated at reasonable values.
- **Clarify the role of $R$** in the final bound: state explicitly whether the concentration argument introduces a $\sqrt{d}$, $d$, or $\log d$ factor and how this interacts with the step-size and mixing time constraints.

## Score and Decision

This paper makes a genuine theoretical contribution: it identifies an intuitive mechanism (data-based initialization + early stopping) and provides the first rigorous guarantee that it provably overcomes the failure of vanilla score matching on multimodal distributions. The high-level proof strategy is creative and plausible, and the log-Sobolev bound (Theorem 2) is a useful technical contribution in its own right.

The main weaknesses are that (i) the $\epsilon_{\text{score}}$ accuracy required by Theorem 1 is extremely demanding and its achievability in the same regime is not discussed, and (ii) the dependence on the truncation radius $R$ and its effect on dimension scaling is not made explicit in the main text. These are real concerns about the *transparency* and *practical meaningfulness* of the bounds, but they do not invalidate the paper's core contribution. The result remains new and interesting even in the exact-score setting ($\epsilon_{\text{score}} = 0$), and the proof structure is sound.

The presentation is clear, the motivation is well-founded, and the simulations qualitatively match the theoretical predictions. Acceptance is warranted with the expectation that the authors address the transparency concerns in a revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>