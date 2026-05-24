## Summary

INFO-SEDD introduces a method for estimating KL divergence, mutual information, and entropy on high-dimensional discrete data using Continuous Time Markov Chains (CTMCs) and score functions from discrete diffusion models. By linking the KL divergence to an integral over CTMC score functions via Dynkin's formula, and using an absorbing-state rate matrix that allows a single score model to serve both joint and marginal distributions, the approach avoids the "embedding trick" required by continuous-space competitors. Experiments across synthetic benchmarks (Table 1), text summarization consistency/model selection (Figures 1–3, Table 2), and genomics motif discovery (Figures 4–5) show large and consistent advantages over eight competing estimators.

## Strengths

- **Strong empirical performance across multiple domains on high-dimensional discrete data**: Table 1 shows INFO-SEDD estimating ground-truth MI values (10–50 nats) with mean errors ≤1.23 nats across all settings (D=10–50), while all eight competitors exhibit substantially larger bias or outright collapse (e.g., SMILE underestimates MI=50 as 18.97±1.05, GAN-DIME collapses after D=40). These results are robust across support sizes (ablation in Appendix C.1.6) and sample sizes as low as 10³.

- **Principled absorbing-state design for marginal scores**: Equation (6) proves that an absorbing-state rate matrix allows a single score model trained on the joint distribution to compute marginal scores, avoiding separate models for each distribution. This is a clean theoretical insight that makes the method practical for high-dimensional settings where separate training would be prohibitive.

- **Real-world utility demonstrated in two distinct application domains**: In text summarization (Table 2), INFO-SEDD-C achieves Pearson correlation 0.740 with human-judged consistency, far outperforming KL-DIME (0.214), HD-DIME (0.331), and SMILE (−0.074) using the same pretrained backbone. In genomics (Figure 5), INFO-SEDD correctly localizes the TATA-box motif at position ≈−35 (within the known −39 to −26 region) on *Arabidopsis thaliana* promoters, natively avoiding interference from correlated motifs.

- **Theoretical error bound establishing consistency**: Equation (7) decomposes estimation error into a score-approximation term (linear in score error) and a truncation bias term (exponentially decaying in T), formalizing that INFO-SEDD is consistent up to a controlled bias — a guarantee absent from competing variational estimators. The bound also clarifies the trade-off between computation (longer T) and accuracy.

## Weaknesses

### Major

- **The derivation of the KL estimator in Section 2.2 is confusing and appears to contain errors in the main text**. Equation (2) states: 
  \[
  \text{KL}[\vec{p}_0 \parallel \vec{q}_0] = \mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_T)] = \mathbb{E}[\log(\vec{p}_T/\vec{q}_T)(\vec{X}_T)]
  \]
  The standard definition is \(\mathbb{E}_{\vec{X}_0\sim\vec{p}_0}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_0)]\) — the leftmost expression places the log-ratio at time \(T\) (\(\vec{X}_T\)), which is not generally equal to the KL divergence between initial distributions. The text then says "We omit the term \(\mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_0)]\), as both \(\vec{p}_0\) and \(\vec{q}_0\) converge to \(\pi\)." This is doubly wrong: the omitted term is precisely the KL divergence the paper aims to estimate, and it is \(\vec{p}_T\) and \(\vec{q}_T\) (not \(\vec{p}_0,\vec{q}_0\)) that converge to the stationary/absorbing distribution. The derivation in the main text is therefore incoherent at a critical juncture. The intended derivation (using Dynkin's formula on \(f(x,t)=\log(p_t/q_t)(x)\) and noting \(\text{KL}[p_T\|q_T]\to 0\)) is recoverable, but the paper does not present it correctly. Since the paper's core contribution is a new estimator, this must be fixed for the contribution to be credible. A corrected, step-by-step derivation should appear in the main text — not deferred to the appendix.

- **The error bound (Equation 7) states constants \(C_1, C_2, \epsilon_p, \epsilon_q\) but does not characterize them or relate them to problem parameters** in the main text. The bound is presented as a theoretical result, but without knowing how these constants scale with dimension \(D\), support size \(|\chi|\), or data distribution properties, the bound is not actionable. It does not, for instance, let a practitioner reason about when the estimator might fail (e.g., if score errors grow with \(D\)). The bound is presented as a "consistency" guarantee, but the absence of any discussion of these constants' magnitudes or dependence on problem size limits its value.

### Minor

- **No discrete-specific baselines are compared.** The paper motivates INFO-SEDD by criticizing the "embedding trick" used to apply continuous-space estimators to discrete data. Yet all eight competitors apply this same trick. A discrete-specific estimator (e.g., a version of MINE operating on categorical inputs with straight-through gradient estimation, or a simple binning/counting estimator for low-dimensional comparisons) would help isolate whether INFO-SEDD's advantage comes from avoiding the embedding trick or from some other property of the diffusion-based approach. This is not a fatal gap — the comparison is fair across methods — but it limits the conclusiveness of the "embedding trick" narrative.

- **No runtime or computational cost comparison** is reported. The paper claims efficiency but provides no wall-clock time, parameter count, or number-of-function-evaluation comparisons against competitors. Training a discrete diffusion model (SEDD) is not cheap, and the paper should at minimum discuss the computational budget for each method and comment on the trade-offs.

- **The consistency tests (Figures 1 and 4) rely on heuristic reference estimates** (entropy-rate-based extrapolation and classifier-based MI approximation) rather than ground truth. While this is standard for real data where ground-truth MI is unavailable, the paper would benefit from a clearer discussion of the assumptions behind these reference estimates and their limitations.

### Trivial

- In Equation (2), the first equality writes \(\mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_T)]\) where \(\mathbb{E}[\log(\vec{p}_0/\vec{q}_0)(\vec{X}_0)]\) is intended (this is part of the Major issue above, noted separately here for the correction itself).
- "both \(\vec{p}_0\) and \(\vec{q}_0\) converge to \(\pi\)" should read "\(\vec{p}_T\) and \(\vec{q}_T\)".
- The paper would benefit from a limitations subsection (as noted in the "Nice-to-Haves" below).

## Nice-to-Haves

- **A limitations subsection** discussing when INFO-SEDD might fail: poor CTMC mixing, poorly calibrated score models, or when the absorbing-state assumption is restrictive.
- **An empirical investigation of how the constants in Equation (7) scale** with dimension \(D\) and support size \(|\chi|\).
- **Runtime/parameter-count comparison** against competitors.
- **A discrete-specific baseline** (e.g., a binning estimator or a Gumbel-Softmax variational estimator) would strengthen the empirical analysis, though not required for the paper's core contribution.

## Removed Points

- **Harsh critic's claim that "the whole estimator is not justified" if the derivation is incorrect**: Removed — the derivation issue is a presentation error in the main text; the appendix (which the critic could not see) likely contains the correct derivation. The core idea is sound and the experimental validation is independent.
- **Harsh critic's claim about "embedding trick" handicapping competitors**: Weakened from major to minor — the comparison treats all methods equally (same backbone, same embedding), so it is fair. The point about the absence of discrete-specific baselines is worth noting but does not undermine the comparison as run.
- **Strength Finder's claim about "unique" contribution**: Removed — this is generic puffery from the conclusion section, not grounded evidence.
- **Strength Finder's claim about "practical utility for promoter motif discovery" as a separate strength**: Merged into the main strength about real-world utility.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rewrite the derivation in Section 2.2** with a clear, step-by-step chain: (a) define \(f(x,t)=\log(p_t/q_t)(x)\), (b) apply Dynkin's formula to relate \(\mathbb{E}[f(X_T,T)] - \mathbb{E}[f(X_0,0)]\) to the integral, (c) note that \(\mathbb{E}[f(X_0,0)] = \text{KL}[p_0\|q_0]\) (standard definition), (d) argue \(\mathbb{E}[f(X_T,T)] = \text{KL}[p_T\|q_T]\to 0\) as \(T\to\infty\) because both processes enter the absorbing state, (e) obtain \(\text{KL}[p_0\|q_0] \approx -\mathbb{E}[\int_0^T (\partial_t f + \mathcal{L}f)\,dt]\), (f) simplify the integrand to Equation (4). The current text garbles this logic.

2. **Add a discussion of the constants in the error bound** — even a brief paragraph on how \(C_1, C_2, \epsilon_p, \epsilon_q\) are expected to scale with \(D\) and \(|\chi|\) would greatly increase the bound's informativeness.

3. **Include a runtime table** for the synthetic experiments (training time per method, inference time per estimate) so readers can assess the computational overhead of training a discrete diffusion model vs. lighter alternatives.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Queried three bands on topics relevant to this paper.

**Weak anchors (avg ≤ 3.5):**
- `lt6xKGGWov` (2.33) — Feature selection with neural MI estimation. Far weaker: limited experiments, no discrete focus, no downstream tasks.
- `hr4HTShC6l` (3.00) — Detecting Shortcuts using MI. Different problem, far less experimental depth.
- `MNGMpHxi1I` (3.00) — Information-theoretic predictive uncertainty. Theoretical, no competitive empirical validation.
- `hv8l922Ad7` (3.40) — Disentanglement metrics. Not comparable.

→ This paper is clearly well above the weak band.

**Middle anchors (3.5 < avg < 7.5):**
- `0kWd8SJq8d` (6.50) — **MINDE**: Direct predecessor on continuous data. INFO-SEDD extends to discrete data with stronger experiments (real-world applications, motifs, multiple domains) but weaker theoretical presentation. Comparable overall, slightly less polished.
- `KC2MViQASx` (5.60) — **f-DIME**: Variational f-divergence MI estimator, rejected. INFO-SEDD has stronger empirical results, more applications, and a more principled foundation.
- `NGB6YNnO5o` (6.25) — Generalization analysis for VAE/DM. Different contribution type but similar quality tier.

**Strong anchors (avg ≥ 7.5):**
- `RuP17cJtZo` (8.00) — Generator Matching. A far more comprehensive theoretical framework with broader scope. INFO-SEDD is narrower — a specific estimator for one task.
- `EO8xpnW7aX` (8.00) — Learning to Permute with Discrete Diffusion. Pure discrete diffusion generative modeling with strong SOTA results.
- `zMPHKOmQNb` (8.00) — Protein Discovery with Discrete Walk-Jump Sampling. Full generative modeling pipeline with biological validation.

→ This paper sits firmly in the middle band — below comprehensive frameworks or SOTA generative models (8.0), but well above the weak band (2.3–3.4).

**Round 1 bracket:** [5.5, 7.0]

**Round 2 (Narrowing inside bracket):** Queried for discrete MI estimation and diffusion-based estimation topics within (4.5, 7.5) and (5.0, 7.0).

- `pq1WUegkza` (7.00) — Convergence of score-based discrete diffusion models. Pure theory, accepted. More rigorous theoretically, no experiments on real data.
- `0kWd8SJq8d` (6.50) — MINDE (already discussed).
- `6awxwQEI82` (7.00) — Comprehensive analysis of discrete diffusion models. Theoretical framework paper.
- `XsgHl54yO7` (6.50) — Guidance for discrete state-space models. Accepted, specific application.
- `PyHRUMxKbT` (5.75) — InfoNet: Neural MI estimator. Rejected, weaker experiments.
- `Piod76RSrx` (5.50) — Slicing MI generalization bounds. Rejected, different problem.
- `PPxyXlCAOJ` (5.50) — Learning representations for independence testing. Rejected, different focus.

**Comparison against closest anchor — MINDE (6.50):** INFO-SEDD and MINDE share the same core idea (diffusion-based MI estimation via score functions) but in different domains (discrete vs. continuous). INFO-SEDD has:
- Stronger empirical validation (real text/genomics data vs. synthetic + MNIST)
- More downstream applications (motif discovery, model selection)
- A cleverer marginal-score trick (Equation 6)
- **But** a less clean derivation (MINDE uses Girsanov, a well-known tool for this; INFO-SEDD's Dynkin derivation is presented confusingly)

On balance, INFO-SEDD's experimental breadth is more impressive, but the derivation issue in the main text is a clear weakness that MINDE did not have. I place INFO-SEDD slightly below MINDE.

**Final placement:** Between f-DIME (5.60, rejected) and MINDE (6.50, accepted). Closer to MINDE than to f-DIME because the problem is important and the experiments are strong. The derivation issue prevents it from reaching MINDE's level.

### Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>