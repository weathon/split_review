Now I have all the calibration data I need. Let me write the final consolidated review.

---

## Summary

This paper introduces INFO-SEDD, a method for estimating KL divergence, mutual information, and entropy on high-dimensional discrete data using continuous-time Markov chains (CTMCs). By expressing the KL divergence through score functions of a discrete diffusion process and leveraging an absorbing-state perturbation to compute marginal scores from a single joint model, the authors derive a tractable estimator. They evaluate INFO-SEDD on synthetic benchmarks, text summarization (model selection via MI), and genomics (consistency tests and TATA-box motif discovery). The synthetic results show INFO-SEDD closely tracking ground-truth MI where all competitors deviate substantially.

## Strengths

- **Strong synthetic benchmark results (Table 1).** INFO-SEDD is the only method that tracks ground-truth MI within ~1 nat across all five settings (MI 10–50, dimension 10–50). At MI=50, D=50, INFO-SEDD estimates 47.77±1.18, while the next-best (MINDE) reports 32.60±3.93—a gap of over 15 nats. Standard deviations are consistently an order of magnitude lower than competitors'.

- **Absorbing-state trick reduces model count (Eq. 6).** The paper proves that with an absorbing-state rate matrix, a single score model trained on the joint distribution suffices to compute marginal scores. This is a principled theoretical result with direct practical impact—only one diffusion model needs training for the joint method.

- **Theoretical consistency bound (Eq. 7).** The error decomposition into estimation error (linear in score approximation errors εₚ, ε_q) and truncation bias (exponentially decaying in T) formalizes why INFO-SEDD avoids the exponential variance that limits importance-sampling-based approaches. While the constants C₁, C₂ are not estimated in practice, the decomposition itself is valuable.

- **Two real-world consistency tests with concrete reference values.** In text (Fig. 1), INFO-SEDD variants maintain near-linear MI trends consistent with entropy-rate-derived bounds (256–303 nats), while competitors saturate or behave non-monotonically. In genomics (Fig. 4), INFO-SEDD-C aligns closely with a classifier-based MI reference across all ρ, while GAN-DIME, HD-DIME, and SMILE plateau or underestimate.

- **Principled theoretical grounding in CTMC theory.** Sections 2.1–2.2 build the KL estimator from Dynkin's lemma and reverse-time CTMC formalism, giving the method a clear mathematical foundation distinct from ad-hoc embedding approaches.

## Weaknesses

### Fatal
None.

### Major

- **Derivation of the KL estimator (Eq. 2) lacks clear justification in the main text.** The first equality, KL[p₀‖q₀] = 𝔼[log(p₀/q₀)(X_T)], swaps the distribution over which the expectation is taken from p₀ to p_T (since X_T ~ p_T) without explanation. The second equality replaces log(p₀/q₀) with log(p_T/q_T) without stating the conditions under which this holds. The paper then applies Dynkin's formula and states "we omit the term 𝔼[log(p₀/q₀)(X₀)], as both p₀ and q₀ converge to π"—but p₀ and q₀ are the *initial* distributions, and the statement about convergence to π applies to the evolved distributions p_t, q_t at large t, not to the initial ones. The full derivation presumably in Appendix E (which is stripped by the parser) may resolve these gaps, but the main text as presented does not provide a self-contained, logically complete derivation, and the relationship between the Dynkin-based integral and the claimed KL approximation is unclear. This is the paper's most significant weakness—it obscures what quantity the estimator actually computes.

### Minor

- **The synthetic benchmark comparison does not fully address the embedding asymmetry.** All competitors require embeddings to handle discrete tokens, while INFO-SEDD operates directly on discrete spaces. The paper states "we use the same backbone for all methods" but does not report how embedding dimension was chosen, whether it was optimized per competitor, or whether embedding training converged. Given the magnitude of the gap (INFO-SEDD at 47.77 vs. MINDE at 32.60 for MI=50), it would strengthen the paper to ablate embedding dimension or include a plug-in estimator on a low-dimensional marginal as an additional sanity check.

- **The "empirical MI estimate" (grey line, Figure 1) is referenced in the figure caption but never defined in the text.** The paper provides entropy-rate-derived bounds (256ρ and 303ρ nats) but does not explain how the grey line is computed, making it difficult to interpret as a reference.

- **The motif discovery experiment (Figure 5) lacks error bars, multiple runs, and a null-model baseline.** The MI profile shows a qualitative peak at the known TATA-box location, which is suggestive but not statistically supported. A comparison to a sliding-window classifier or PWM baseline would contextualize the result.

- **INFO-SEDD-C shows a notable gap between Pearson (r=0.740) and Kendall's τ (0.505) for consistency (Table 2),** suggesting the relationship with human ratings is not strictly monotonic across models. The paper does not discuss this discrepancy, which is worth exploring given the model-selection framing.

### Trivial

- Table 2 would benefit from a clearer separation between the Pearson and Kendall halves—the current side-by-side layout is hard to parse.

## Nice-to-Haves

- **Computational cost comparison.** The paper does not report training time, inference time, or parameter counts for INFO-SEDD relative to competitors. This would help contextualize scalability claims.
- **Ablation on the choice of T (diffusion horizon).** The truncation bias bound depends on T, but no sensitivity study is provided.
- **Discussion of limitations.** The paper could explicitly discuss when INFO-SEDD may struggle (e.g., very small support, limited training data for the score model, sensitivity to the unit-Hamming decomposition assumption).

## Removed Points

- **Criticism that Eq. (2) is "fatal" and "invalidates the method's core claims."** The full derivation resides in Appendix E (stripped by the parser — Hard Rule). The main text is incomplete but not demonstrably incorrect. Demoted to Major.
- **Criticism that the linear-MI assumption for the text consistency test is heuristic.** The paper explicitly acknowledges this as an approximation backed by entropy-rate literature. This is a proper caveat, not a flaw. Removed as strawman.
- **Criticism that the derivation "lacks theoretical support."** The paper provides a theoretical bound (Eq. 7) and references a full appendix derivation. Irrelevant without engaging with the appendix content. Removed.
- **Generic embedding-tuning suspicion without specific evidence of unfair comparison.** The reviewer presents no evidence that embeddings were not well-tuned, only that the paper could report more details. Demoted to Minor (kept above).
- **Strength Finder's generic claims about "important problem" and "timely topic."** These are not concrete evidence of the paper's quality. Removed per strength-filtering rules.
- **Strength Finder's claim about "clear mathematical foundation distinct from ad-hoc continuous-embedding approaches."** This is somewhat sycophantic language; kept as a factual statement about the CTMC grounding.

## Novel Insights

The reviewers collectively surface a genuine tension: the synthetic results (Table 1) are unusually strong—INFO-SEDD's margin over competitors increases with dimensionality rather than shrinking—which suggests the method is exploiting a structural property of discrete diffusion that embedding-based methods cannot access. The absorbing-state trick (Eq. 6) is the key enabling insight here, and it cleanly sidesteps the need for separate marginal models. At the same time, neither reviewer fully unpacks *why* the variational estimators fail so badly on discrete data—whether it is the embedding bottleneck, the log(N) bound from McAllester & Stratos, or both—which would be a useful contribution in its own right. The most actionable observation is that the main-text derivation of Eq. (2) needs tightening; the gap between the claimed equality and the Dynkin application is large enough that readers may doubt the estimator's target even if it works well empirically.

## Suggestions

1. **Rewrite the derivation of the KL estimator (Section 2.2) to be self-contained in the main text.** Clearly state the starting point: KL[p₀‖q₀] = 𝔼_{x~p₀}[log(p₀/q₀)(x)]. State explicitly if you are introducing an approximation (KL[p₀‖q₀] ≈ KL[p_T‖q_T]) and bound the error. Alternatively, show the Dynkin-based argument that avoids Eq. (2)'s first two equalities entirely. The current presentation forces readers to either guess or reconstruct the reasoning from the appendix.

2. **Define the "empirical MI estimate" (grey line, Figure 1) in the text.** If it is a frequency-based plug-in estimate, state its limitations.

3. **Add error bars or multiple runs to Figure 5 (motif discovery)**, and ideally a simple baseline (e.g., sliding-window classifier accuracy).

4. **Report embedding dimensions used for competitors** and, if feasible, show that varying the embedding dimension does not qualitatively change the comparison in Table 1.

5. **Discuss the Pearson / Kendall discrepancy in Table 2** — the gap suggests that a few outlier models may drive the Pearson correlation, which is worth exploring.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Comparison |
|---|---|---|
| `0kWd8SJq8d` (MINDE) | 6.50 | Continuous-data MI estimation via diffusion; very similar methodology, accepted. INFO-SEDD extends this nontrivially to discrete data with comparably strong experiments but less clear derivation. → INFO-SEDD slightly lower. |
| `pq1WUegkza` (CTMC convergence) | 7.00 | Rigorous theoretical analysis of discrete diffusion; accepted. INFO-SEDD is more applied and empirically driven. → INFO-SEDD lower on theoretical rigor, higher on application breadth. |
| `KC2MViQASx` (f-DIME) | 5.60 | MI estimation via f-divergence methods; rejected. INFO-SEDD has stronger empirical results and greater methodological novelty. → INFO-SEDD higher. |
| `Hh0Cg4epYY` (Bayes Error) | 2.33 | Incomplete draft with trivial experiments. INFO-SEDD is substantially more complete and substantive. → INFO-SEDD much higher. |
| `bH6T0Jjw5y` (T-IB) | 8.00 | Principled information bottleneck approach for Markov processes. Not directly comparable. |

The paper makes a genuine contribution to a well-motivated problem (discrete MI estimation) with strong empirical evidence, particularly in the synthetic benchmark. The main weakness is the incomplete presentation of the core theoretical derivation in the main text, which should be fixable but currently obscures what quantity the estimator actually computes. The experimental scope—synthetic benchmarks, text summarization, and genomics—is appropriate and thorough. Positioned against the anchors, the paper is clearly above the rejection-level papers (avg ≤5.6) but below the strongest theoretical contributions. It compares most directly with MINDE (6.5), from which it inherits the diffusion-based estimation paradigm while tackling the more challenging discrete setting.

**Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>