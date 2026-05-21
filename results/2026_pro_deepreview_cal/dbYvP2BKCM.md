Now I have enough information to write the final consolidated review. Let me systematically cross-check all claims and produce the review.

---

## Summary

This paper proposes ZNet, a deep learning method that learns to decompose observed covariates \(X\) into a confounder representation \(C = f(X)\) and an instrumental variable representation \(Z = g(X)\) by imposing the IV relevance, exclusion restriction, and unconfoundedness conditions through a multi-loss architecture. The method is designed to construct valid instruments from observed data even when no explicit instrument exists. Experiments on ten semi-synthetic dataset variants derived from IHDP compare ZNet against AutoIV, GIV, VIV, and TARNet across three downstream IV estimators (TSLS, DeepIV, DFIV).

## Strengths

- **Novel and well-motivated problem formulation.** Learning instrument representations directly from observed covariates—rather than selecting from candidate instruments—is an ambitious and valuable direction. The idea of deriving \(Z\) and \(C\) through functions \(f, g\) that enforce the IV constraints via a structured loss is clean and well-scoped (Section 3, Figure 2). The paper explicitly differentiates itself from prior work that either selects from known candidates or learns variational distributions without enforcing SCM constraints (Section 4).

- **Comprehensive and well-designed empirical evaluation.** The paper evaluates ZNet across ten semi-synthetic dataset variants spanning four instrument classes (Disjoint, Mixed, Latent, No Candidate) × linear/nonlinear × with/without unobserved confounding. Three downstream estimators (TSLS, DeepIV, DFIV) are tested, and ZNet is compared against AutoIV, GIV, VIV, TARNet, and TrueIV. The breadth of evaluation conditions is notably more extensive than typical in this sub-area (Table 1, Section 6.1).

- **Convincing evidence of instrument recovery when ground truth exists.** In the Linear Categorical Instrument setting, ZNet nearly perfectly recovers the latent cluster structure (normalized confusion matrix, Figure 4). In the Linear Mixed Candidate setting, the learned \(Z\) correlates with the true instrument variables (Figures 5a–5b), and ablating any constraint degrades recovery (Figure 5c). These sanity checks provide credible evidence that the loss constraints are doing nontrivial work.

- **Empirical validation of learned representations in the no-instrument setting.** For the Non-linear No Candidate dataset, Figure 6 shows that the learned \(Z\) passes operational checks: it is relevant (significant F-statistic for predicting \(T\)), satisfies exclusion (adding \(Z\) to a model with \(C\) and \(T\) does not improve \(Y\) prediction), and shows low correlation with unobserved confounders \(U\). This is a sensible and informative set of post-hoc validity checks.

- **Lemma 1 provides a useful theoretical relaxation.** The observation that zero covariance between a normally-distributed \(Z\) and the residual \(Y - \mathbb{E}[Y|X,T]\) implies \(\text{Cov}(Z, e_Y) = 0\) is a clean result that justifies the loss design for settings where \(X\) may be influenced by \(U\)—a relaxation over prior work that assumes \(X \perp U\).

## Weaknesses

### Fatal

None.

### Major

- **The loss-based enforcement of unconfoundedness does not guarantee the required conditional independence.** The standard IV unconfoundedness condition stated in Section 2 is \(Z \perp e_Y \mid C\) (conditional independence). The ZNet loss enforces only \(\text{Cov}(Z, e_Y) = 0\) (or, in the MI variant, minimizes mutual information). Zero covariance—and even zero mutual information—is strictly weaker than conditional independence given \(C\). Lemma 1 shows that \(\text{Cov}(Z, \text{residual}) = 0\) and normality of \(Z\) imply \(\text{Cov}(Z, e_Y) = 0\), but this is unconditional covariance, not \(Z \perp e_Y \mid C\). The paper does not provide any argument bridging this gap or specifying conditions under which the loss minimizer would yield a valid instrument for consistent effect estimation. This weakens the central claim that ZNet "find[s] a representation which satisfies the standard IV assumptions" (abstract). The MI variant partially addresses dependence beyond linear correlation, but even MI minimization does not guarantee conditional independence in the learned representation.

- **Claims of comparability to TrueIV and "plug-in" reliability are overstated relative to the empirical evidence.** Table 1 shows ZNet's ATE errors are often far from TrueIV (e.g., Linear Disjoint TSLS: ZNet 0.119 vs. TrueIV −0.002; Non-linear Latent DeepIV: ZNet −0.039 vs. TrueIV −0.020). The pattern is inconsistent—ZNet is best or second-best in many settings but not systematically close to the oracle. The abstract states ZNet can be used "regardless of whether the (untestable) assumption of unconfoundedness is satisfied," but this framing implies a level of robustness the evaluation cannot confirm from a single covariate distribution (IHDP). The narrative in Section 7 that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function" conflates what the loss *encourages* with what it *guarantees*.

### Minor

- **All experiments derive from a single covariate distribution (IHDP).** While the paper generates ten dataset variants by varying instrument availability, functional form, and confounding structure, all use the same underlying covariate matrix. This limits evidence of generalizability across different covariate distributions (e.g., different dimensionality, correlation structure, domain). Including at least one additional semi-synthetic dataset from a different domain would substantially strengthen the empirical case.

- **No exploration of hyperparameter sensitivity.** The loss function combines seven α-weighted terms (MSE, BCE, KL, PC/MI components), tuned via Bayesian optimization on a meta-objective (F-statistic and C-Z correlation) that is not the downstream causal error. The paper provides no sensitivity analysis showing whether ATE performance is robust to these choices or whether tuning on the meta-objective aligns with tuning on ATE error.

- **Gradient surgery is used but not analyzed.** The paper mentions using gradient surgery (Yu et al., 2020) to handle conflicting losses but provides no ablation showing its effect on training stability or final performance. Given the multi-objective nature of the loss, understanding whether gradient surgery masks fundamental loss-landscape conflicts would be valuable.

### Trivial

- The discussion in Section 7 states that ZNet "eliminates the need for domain knowledge of pre-existing IVs" and suggests it can "serve as a plug-in causal inference estimator." This language is somewhat promotional and should be tempered to match the actual evidence (semi-synthetic only, all from IHDP).

## Nice-to-Haves

- **Adversarial or distribution-matching objectives** could replace or supplement the correlation-based loss to more directly target conditional independence (\(Z \perp e_Y \mid C\)), which would strengthen the theoretical basis for the method.
- **Confidence intervals** for ATE/CATE estimates would help practitioners assess the practical reliability of ZNet estimates.
- **Comparisons against methods that handle unobserved confounding without explicit instruments** (e.g., CEVAE, proxy-variable methods) would contextualize when IV generation is necessary versus when alternative approaches suffice.
- **Ablation of gradient surgery** and **sensitivity analysis of loss weights** would improve understanding of the method's practical reliability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The method lacks the theoretical foundations needed to support the strong claim that ZNet can be plugged in as a general-purpose IV module."** — Partially absorbed into the Major weakness about the gap between correlation and conditional independence. The harsh critic's framing that this is "fatal" and "structural" and "requires a fundamentally different approach" is too strong: the empirical evidence shows the method works in many settings, and the MI variant partially addresses nonlinear dependence. The gap is real but is a Major weakness, not a fatal one.

- **Harsh Critic: "The paper does not report CATE performance" / "CATE is relegated to the appendix."** — REMOVED. The appendix, which was stripped by the parser, likely contains CATE results (referenced as "Appendix Tables 3, 4" in the paper). We cannot penalize the paper for appendix content we cannot see.

- **Harsh Critic: "No formal discussion of what identifiability guarantees can be derived."** — REMOVED as a standalone weakness. The paper acknowledges this limitation in the Discussion (Section 7): "IV estimation in general is limited by a lack of theoretical guarantees of identifiability in the general case." This is a known, field-wide limitation, not a paper-specific failure. The gap between correlation and conditional independence (kept as Major) is the more specific version of this concern.

- **Harsh Critic: "Constraint 2 (exclusion) does not preclude Z from having a direct path to Y after conditioning on C and T unless C perfectly mediates all causal paths."** — WEAKENED and partly removed. The paper's exclusion restriction is enforced by (i) encouraging C to predict Y, (ii) forcing Z ⟂ C, and (iii) the architecture does not feed Z into the outcome model. The F-test in Figure 6b operationally validates that Z doesn't add predictive power beyond C and T. This is a reasonable operationalization. The harsh critic's demand for perfect mediation is unrealistic.

- **Harsh Critic: "The significance markings in Table 1 use an ad-hoc procedure."** — REMOVED. The table caption clearly defines the markings: "* = two best significantly better than third best, ** = best significantly better than second best." This is a reasonable significance reporting convention.

- **Harsh Critic: Figure 5c's R² values are "modest" (0.25-0.39) making "recovery a stretch."** — REMOVED. The harsh critic misreads Figure 5c. The "ZNet Val" column shows R²=0.84 for the full ZNet, and the 0.25-0.39 values are for *ablated* versions (removing individual constraints), which the paper uses to demonstrate that each constraint matters. The R²=0.84 with all constraints is strong evidence of recovery.

- **Harsh Critic: "The paper does not report variance of estimated effects."** — REMOVED as a standalone critique. The paper uses 50 bootstraps and reports mean errors; this is standard in the field.

- **Harsh Critic: "The method's own Discussion acknowledges the lack of theoretical identifiability guarantees."** — This is not a weakness; acknowledging limitations is a strength of the discussion section.

- **Strength Finder: "The paper's most convincing piece of evidence is the comprehensive ATE comparison."** — Kept as a strength but qualified; the ATE results are comprehensive in breadth but the claim of consistency is overstated (see Major weakness).

- **Strength Finder: "Architecture designed for plug-in use."** — Kept as part of the strengths but qualified; the plug-in claim is partially supported but the theoretical gaps constrain the claim.

## Novel Insights

The most interesting insight emerging from this review process is the tension between loss-based enforcement and statistical guarantees in learned causal representations. ZNet demonstrates that correlation-based and MI-based losses can produce representations that pass operational IV validity checks and improve downstream ATE estimation—even when the losses do not theoretically guarantee the required conditional independence. This suggests a pragmatic research direction: strong empirical performance may be achievable with weaker theoretical conditions than classical IV theory demands. However, the paper does not itself explore or characterize this gap, which remains an open question for the community. The contrast with ShadowCatcher (Oc4ji1iCjQ, 6.75), which uses iterative hypothesis testing to validate its generated variables, highlights a design tradeoff between end-to-end learning (ZNet) and principled validation loops.

## Suggestions

- **Temper the abstract and introduction claims.** Replace "satisfy the standard IV assumptions" with "encourage the standard IV assumptions" or "produce representations that empirically meet operational IV checks." Replace "regardless of whether the assumption of unconfoundedness is satisfied" with "in settings where unconfoundedness may not hold, provided that the IV assumptions can be approximately met."
- **Add a second semi-synthetic dataset** from a different domain (e.g., Twins, News, or a custom DGP) to provide evidence of generalizability beyond IHDP.
- **Include a sensitivity analysis** showing how ATE error varies with different loss weight configurations, or at minimum report the tuned weights and discuss their stability.
- **Report confidence intervals** (e.g., bootstrap percentiles) alongside mean ATE errors to help readers assess estimate reliability.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| F7XPZnIUHh (ADR decomposition) | 4.20 | R1 | ZNet is clearly stronger: cleaner method, broader evaluation, no theoretical errors |
| yTbAGlu4jR (DIRE) | 5.25 | R2 | ZNet is somewhat stronger: more coherent methodology, more convincing empirical results |
| x2rZGCbRRd (post-treatment covariates) | 5.50 | R2 | Different setting; comparable quality tier |
| wFf9m4v7oC (CFDiVAE) | 5.75 | R1/R2 | ZNet is comparable: similar ambition, similar theory-practice gap, but ZNet has broader evaluation |
| qDhq1icpO8 (CBRL.CIV) | 6.75 | R1/R2 | ZNet is weaker: CBRL has stronger theoretical grounding (soundness proofs); ZNet is more ambitious but less rigorous |
| Oc4ji1iCjQ (ShadowCatcher) | 6.75 | R1/R2 | ZNet is somewhat weaker: ShadowCatcher has more principled validation (iterative hypothesis testing); ZNet has broader evaluation scope |

**Round-1 bracket:** 5.0–7.0.  
**Round-2 narrowing:** ZNet sits between yTbAGlu4jR (5.25) and wFf9m4v7oC (5.75), and clearly below qDhq1icpO8 (6.75). The paper has real novelty and a comprehensive evaluation, but the theoretical gap between covariance-based loss enforcement and conditional independence is a genuine Major weakness that prevents a higher score. The evaluation, while broad across conditions, is narrow in covariate distribution.

**Final score:** 5.5 — a solid paper with a creative approach and thorough evaluation, held back by a theory-practice gap that weakens its central claims. The paper would benefit from tempered claims and additional generalizability evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>