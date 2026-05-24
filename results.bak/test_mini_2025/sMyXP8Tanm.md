Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper reveals that the concrete score in absorbing discrete diffusion can be factorized into an analytic time-dependent scalar multiplied by the time-independent conditional distribution of clean data (Theorem 1). Based on this insight, the authors propose RADD, which removes time conditioning from the network architecture, enabling a caching strategy that reduces the expected number of function evaluations during sampling. They further unify the training objectives of absorbing diffusion and any-order autoregressive models (Theorem 2). Empirically, RADD achieves state-of-the-art perplexity among diffusion models at GPT-2 scale across five zero-shot language modeling benchmarks, while requiring fewer parameters (no time conditioning) and supporting faster sampling via caching.

## Strengths

- **Theorem 1 is a clean and genuinely insightful theoretical contribution.** The factorization of the concrete score into an analytic scalar $e^{-\bar{\sigma}(t)}/(1-e^{-\bar{\sigma}(t)})$ and the conditional distribution $p_0(\hat{x}_t^1|\mathbf{x}_t^{UM})$ (Section 3.1, Eq. 3.1) explains why the scaling trick in SEDD (Lou et al., 2024) works, demystifying an important practical technique. This decomposition is the paper's strongest intellectual contribution and directly motivates the simpler architecture.

- **Removing time conditioning simplifies the architecture while improving perplexity.** RADD's time-independent network (Section 3.1, Figure 1) eliminates the time embedding and adaptive layer norm used in SEDD. Tables 1 and 2 show that RADD-DSE (no time conditioning) outperforms SEDD-Scale (with time conditioning) on all five zero-shot benchmarks at both small and medium scales — e.g., on WikiText2 medium: 29.17 vs. 31.04; on PTB medium: 75.16 vs. 87.12. This is direct evidence that the reparameterization is both simpler and more effective.

- **The caching strategy is well-motivated and quantified analytically.** Because RADD's network output is unchanged when the noisy input is unchanged, Section 3.2 derives an analytic expected-NFEs formula (Eq. 3.4) that closely matches experimental measurements (Figure 1a). Figure 1b confirms the practical speedup: RADD with caching reaches lower generative perplexity in less wall-clock time than SEDD.

- **Empirical validation of the loss equivalence is thorough.** Tables 1 and 2 show that RADD models trained with DSE, t-DCE, λ-DCE, and AO-ARM losses achieve very similar perplexities across all five datasets, supporting Theorem 2's equivalence claim with concrete empirical evidence.

- **The scaling trick ablation is well-designed.** Including both "SEDD-Unscale" and "SEDD-Scale" rows in Tables 1 and 2 confirms that the scaled version consistently beats the unscaled version, matching Theorem 1's prediction and strengthening the paper's central thesis.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The main-text sketch of the DSE-to-t-DCE equivalence (Theorem 2, Step 1) is too terse to be self-contained.** The paper states that "removing the terms $s_\theta(\mathbf{x}_t, t)_{\hat{\mathbf{x}}_t}$ and $K(\cdots)$" yields the t-DCE loss, but this description is misleading — removing a model-dependent term from the loss would change the minimizer without additional justification. The full derivation is deferred to Appendix C.1 (which was stripped by the parser from the review copy). This is a **presentation issue** rather than a technical flaw: the empirical results (similar perplexities across all four losses in Tables 1 and 2) independently validate the claimed equivalence. However, the main text should provide a clearer sketch of how Theorem 1's reparameterization transforms the DSE loss into the cross-entropy form, rather than describing it as "removing terms."

- **The novelty claim is slightly overstated given concurrent work.** The paper acknowledges that Shi et al. (2024) derived a similar weighted cross-entropy loss and a proposition resembling Theorem 1, and that Sahoo et al. (2024) also proposed removing time conditioning and a caching strategy. Yet Section 5 states "Our unique contribution lies in the decomposition of the concrete score and time-independent parameterization" — this framing is imprecise since similar findings appear in contemporaneous independent work. The paper's actual differentiating contributions are: (a) the complete analytic treatment of the concrete score factorization, (b) the expected-NFEs analysis, and (c) the unification with AO-ARMs via the full loss equivalence chain (Theorem 2). Reframing along these lines would be more accurate.

- **Parameter counts are not reported explicitly.** The paper states "similar parameter counts" when comparing RADD to SEDD (Section 4.1), but removing time conditioning should reduce parameters. Reporting exact parameter counts (or at least stating whether hidden dimensions were adjusted to match) would make the comparison more transparent. This is a small but important detail for reproducibility.

- **The theoretical unification (Theorem 2) holds only in the limit $\bar{\sigma}(T) \to +\infty$.** The paper acknowledges this condition (Theorem 2 statement), and the empirical results suggest the gap is small in practice, but a brief discussion of the finite-$T$ gap's magnitude would strengthen the theoretical rigor.

### Trivial
None worth listing — the paper is generally well-written and the presentation is clear.

## Nice-to-Haves
- A table reporting exact parameter counts for RADD vs. SEDD models (at both small and medium scales).
- A table with wall-clock time, NFEs, and perplexity at fixed sampling budgets, complementing the perplexity-vs-time curves in Figure 1b.
- Additional generation quality metrics (e.g., MAUVE, self-BLEU) beyond perplexity and unigram entropy, to more fully characterize generation diversity.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The derivation of equivalence between DSE and t-DCE is potentially invalid"** — The harsh critic speculates that the main-text description may indicate a flawed proof, but acknowledges the full proof is in Appendix C.1. Since the appendix was stripped by the parser, this is a missing-appendix criticism (removed per hard rules). The empirical validation (Tables 1, 2) independently supports the equivalence.

- **"Expected NFEs formula assumptions are unclear"** — The paper explicitly states the formula applies to Tweedie $\tau$-leaping with a log-linear noise schedule (Section 3.2) and the experimental verification (red stars) matches the curve, so the claim is well-supported.

- **"SEDD not supporting caching claim is imprecise"** — SEDD's output depends on time input $t$, which changes each sampling step, so caching is indeed inapplicable. The claim is correct.

- **"No comparison to concurrent works' results"** — The paper acknowledges the timeline issue and concurrent works in Section 5; this is not a weakness of the paper's own evaluation.

- **"RADD-DSE slightly outperforms other RADD losses"** — This is an observation, not a weakness. The paper discusses this as expected variation from gradient estimation on finite data (Section 4.3).

- **Various missing-citation and formatting nitpicks** — Removed per hard rules.

## Novel Insights

The two reviews agree on the paper's core contribution and produce no genuinely novel conflict-synthesis insight beyond what the paper states. The one observation worth surfacing is that the harsh critic's most serious concern (the DSE-to-t-DCE derivation) is rendered largely moot by the paper's own empirical validation: Tables 1 and 2 show all four losses achieve nearly identical perplexities, which is strong evidence that the equivalence holds regardless of how the main text sketches the algebra. The reviews collectively suggest the paper would benefit from more careful novelty framing (acknowledging concurrent discoveries) and more precise experimental reporting (parameter counts), but neither challenge the central result.

## Suggestions

1. **Provide a clearer derivation sketch for Step 1 of Theorem 2.** Show how plugging the reparameterization $s_\theta(\mathbf{x}_t, t) = (e^{-\bar{\sigma}(t)}/(1-e^{-\bar{\sigma}(t)})) \cdot q_\theta(\mathbf{x}_t^{UM})$ into the DSE loss (Eq. 2.6) simplifies to the t-DCE loss (Eq. 3.5), rather than describing it as "removing terms." Even a 3-4 line algebraic sketch in the main text would greatly improve readability and trust.

2. **Reframe the novelty in Section 5 to avoid overclaiming uniqueness.** Explicitly state that the concrete score decomposition was independently discovered by concurrent work, and position the paper's distinct contributions as: (a) the full theoretical analysis of the factorization leading to a simpler architecture, (b) the analytic expected-NFEs characterization of caching, and (c) the complete four-way loss equivalence chain (Theorem 2).

3. **Report exact parameter counts** for all models in Tables 1 and 2, clarifying whether hidden sizes were adjusted when removing time conditioning.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Three queries on "discrete diffusion model text generation language modeling perplexity" with score filters $<3.5$, $3.5$–$7.5$, and $>7.5$ returned anchors averaging ~3.0 (weak), ~6.2 (middle), and ~8.0 (strong). The paper is clearly not in the weak band (those are diffusion papers with fundamental flaws or different topics). It is also below the strongest anchor (Block Diffusion, avg 8.0, Oral), which introduces a full semi-autoregressive framework with flexible-length generation. **Initial bracket: 4.0–7.0.**

**Round 2 (Narrowing):** Further queries with narrower score ranges retrieved five anchors. The most relevant:
- *Reparameterized Discrete Diffusion for Text Generation* (avg 5.5, Reject) — weaker theory, mixed reviews, no zero-shot language modeling results. RADD is clearly stronger.
- *Unlocking Guidance for Discrete State-Space Models* (avg 6.5, Poster) — solid method, presentation issues, limited scope. RADD's experiments are cleaner and the theory is more central to the paper's claims.
- *How Discrete and Continuous Diffusion Meet* (avg 7.0, Poster) — rigorous theory but no experiments and very dense. RADD has both theory and strong experiments.
- *Block Diffusion* (avg 8.0, Oral) — more comprehensive framework, semi-autoregressive, flexible-length generation, stronger overall. RADD is narrower.

**Final calibration:** RADD is comparable to or slightly better than the 6.5–7.0 Poster-level papers, but falls short of the 8.0 Oral-level Block Diffusion paper due to its narrower scope (GPT-2 scale only, fixed-length generation) and the presentation/framing issues noted above. The core theoretical contribution (Theorem 1) and strong empirical validation support a solid accept-level score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>