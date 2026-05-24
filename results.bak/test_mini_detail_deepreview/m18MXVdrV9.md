Now I have sufficient information. Let me write the consolidated review.

**My Round 1 bracket** (based on the calibration search): The paper sits between the weak anchors (avg 3.00) and the strong anchors (avg 8.00). The most relevant anchor is MINDE (6.50, the continuous-data predecessor of this work). The paper is clearly far stronger than the 3.0 papers (which had broken or trivial contributions). It's weaker than the 7.0+ papers (which have rigorous theory). The f-DIME paper (5.60) is another good comparator — a MI estimation paper with weaker experiments but more solid theory.

**Round 2 narrowing**: Reading the MINDE review (6.50) shows that paper was accepted despite dense math that reviewers struggled with. The key difference: MINDE's derivation used the well-established Girsanov theorem, so even if dense, the approach was sound. INFO-SEDD's main-text derivation appears to have actual mathematical errors (Equation 2). The discrete diffusion convergence paper (7.00) and efficient perplexity bound paper (6.75) are stronger theoretically but are pure theory papers, not methodology+application papers like INFO-SEDD.

**Final score**: 5.5 — This paper is below the acceptance threshold but above a clear reject. The empirical results are strong and the approach is creative, but the core theoretical derivation in Section 2 is not self-consistent as presented, which undermines confidence in the method's foundations. This is below MINDE (6.50, which had a cleaner theoretical foundation) but above f-DIME (5.60, which had weak experiments).

---

## Summary

This paper introduces INFO-SEDD, a method for estimating information-theoretic quantities (KL divergence, mutual information, entropy) for high-dimensional discrete data using Continuous Time Markov Chains (CTMCs). The key idea is to bridge score-based discrete diffusion models (typically used for generative modeling) with information estimation by applying Dynkin's formula to express KL divergences in terms of score functions that can be learned via denoising score matching. The method avoids the "embedding trick" (embedding discrete data into continuous space) required by prior neural estimators, and uses an absorbing-state CTMC design that allows a single trained score model to compute joint and marginal quantities jointly. Experiments on synthetic benchmarks (where INFO-SEDD is the only estimator that remains accurate at MI values up to 50 and dimensions up to 50) and on real-world text and genomics data demonstrate strong empirical performance.

## Strengths

- **Consistent accuracy on high-dimensional, high-MI synthetic benchmarks (Table 1).** INFO-SEDD is the only estimator that stays within ~2% of ground truth for MI values from 10 to 50 and dimensions from 10 to 50 (e.g., MI=20, D=20: 20.02±0.21 vs. ground truth 20). All competitors deviate substantially — GAN-DIME overshoots to 22.09, MINDE to 26.98, and MINE collapses to 8.82. This provides direct evidence that INFO-SEDD delivers on its core claim of scalable estimation for discrete high-MI settings.

- **Clever absorbing-state CTMC design enabling single-model estimation (Equation 6).** The paper shows that by choosing an absorbing transition matrix, marginal score ratios can be derived from a single model trained on the joint distribution. This avoids training separate models for joint and marginal distributions — a concrete architectural advantage over versions of the approach that would require multiple networks.

- **Theoretical consistency bound with explicit error decomposition (Equation 7).** The bound separates estimation error (linear in score approximation errors) from truncation bias (exponentially decaying with horizon T). This provides a formal guarantee absent from competitors that rely on variational bounds (McAllester & Stratos, 2020).

- **Empirical consistency on real discrete data, outperforming embedding-based methods.** In the text-summarization consistency test (Figure 1), INFO-SEDD-C and INFO-SEDD-J produce MI estimates that grow linearly with ρ. In contrast, KL-DIME, SMILE, and HD-DIME all severely underestimate. The genomics consistency test (Figure 4) shows INFO-SEDD-C closely matching a classifier-based reference MI.

- **Downstream utility demonstrated in two application domains.** Table 2 reports Pearson correlation r=0.740 (INFO-SEDD-C) between MI and human-rated consistency in summarization, far exceeding KL-DIME (0.214) and SMILE (−0.074). In genomics (Figure 5), INFO-SEDD-J localises the TATA-box motif at the known −39 to −26 region.

## Weaknesses

### Fatal
None.

### Major

1. **The derivation in Section 2 (Equations 2–5) is not mathematically self-consistent as presented, and appears to contain a genuine error.** The paper claims:
   > `KL[p0∥q0] = E[log(p0/q0)(X_T)] = E[log(pT/qT)(X_T)]`
   
   If X_t is the forward CTMC starting from p0 with generator Q_t (as stated in the text), then `E[log(p0/q0)(X_T)] = Σ p_T(x) log(p0(x)/q0(x))`. This is not equal to `KL(p0∥q0) = Σ p0(x) log(p0(x)/q0(x))` unless the Markov kernel is deterministic, which is not the case. The second claimed equality `E[log(p0/q0)(X_T)] = E[log(pT/qT)(X_T)]` is also unjustified. The right-hand side is `KL(pT∥qT)`, which by the data processing inequality is generally *smaller* than `KL(p0∥q0)`. The flow from Equation (2) to Equations (4)–(5) via Dynkin's formula is not clearly justified, and the paper's statement "We omit the term E[log(p0/q0)(X_0)], as both p0 and q0 converge to π" is confused (it should refer to pT and qT, not p0 and q0). The paper defers to Appendix A.3 and Appendix E, but the main text must provide a self-consistent argument. Without a corrected derivation, the theoretical foundation of the method cannot be evaluated. This is the paper's most significant weakness. (Verified directly from the paper: Section 2.2, lines 55–69.)

2. **The synthetic experiment setup is opaque in the main text.** The paper reports impressive results (Table 1) with ground-truth MI up to 50 and dimensions up to 50, but the main text gives essentially no description of how these synthetic distributions are constructed, how the ground-truth MI is computed, or what structure the data has. The only description is "Given two vectors X = (x1, ..., xD) and Y = (y1, ..., yD) sampled from their respective discrete distributions" (line 112). Full details are deferred to Appendix C.1, which is stripped. Since these experiments constitute the strongest evidence for the method's superiority, the reader needs enough information in the main text to assess whether the setup is realistic or whether it favors discrete diffusion. (Verified: Section 4.1, lines 110–134.)

### Minor

3. **The text consistency test has ambiguities that are not discussed.** The paper cites entropy estimates of 256–303 nats for summaries (from Takahira et al. and Cover & King) and plots a "256·ρ nats to 303·ρ nats" reference line in Figure 1. However, the figure description indicates the "Empirical MI estimate" (grey line) reaches around 10² ≈ 100 nats at ρ=1 — substantially below the cited 256–303 range. The paper's claim that INFO-SEDD variants "closely match the empirical derivation" is not sufficiently qualified given this discrepancy. Additionally, the linear-MI-in-ρ assumption is stated but not rigorously justified (it relies on an order-of-magnitude argument). (Verified: Section 4.2, particularly lines 140–154, and the figure caption/alt text.)

4. **The model selection analysis (Table 2) has limited scope.** Only four competitors are included (KL-DIME, HD-DIME, SMILE), while several baselines from the synthetic experiments (MINE, NWJ, MINDE) are omitted with no explanation. The sample size is 15 models, and p-values are not reported for the correlation values. The paper claims INFO-SEDD-C achieves r=0.740 for consistency, which is the best among reported methods, but the absence of several baselines makes the comparison less comprehensive than it should be. (Verified: Table 2, Section 4.2, lines 156–188.)

5. **Practical guidance on choosing the time horizon T is missing.** Equation (7) decomposes truncation bias (decaying with T) and estimation error (growing with T via σ̄(T)), but the paper provides no discussion of how T is set in practice or how practitioners can verify that the bias is negligible. This is important for reproducibility and practical adoption. (Verified: Section 3, lines 98–102.)

### Trivial
None that are parser-independent.

## Nice-to-Haves
- Report training times or model sizes to substantiate the scalability claim.
- Include confidence intervals or p-values for the text model selection correlations.
- For the motif discovery experiment, provide a quantitative comparison to alternative MI estimators (even if they require separate training runs).

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism that "the paper claims 'unique' too strongly"**: The harsh critic's note that "unique" is an overstatement given MINDE's existence for continuous data. Reason for removal: This is a semantic nitpick. The paper's method is genuinely novel for discrete data, and overclaiming is a minor style issue.

- **Criticism about "the derivation of Equation (4) uses the backward operator B with Q_t instead of Q̄_t"**: Upon re-reading, the paper defines B[f](a,t) = Σ_{b≠a} Q_t(b,a)(f(b)−f(a)), where Q_t(b,a) is the *reverse-time* transition matrix defined in Equation (1). The notation is consistent — Q_t(b,a) with arguments in that order is indeed the reverse-time rate, matching the paper's Equation (1). This is a misreading by the critic.

- **Criticism about "standard deviations for competitors are often large (e.g., MINE at MI=10 has σ=6.33), so some comparisons may not be statistically significant"**: This is a generic statistical critique that applies to most benchmarking papers. The paper reports 10 seeds. Given the large performance gap between INFO-SEDD and competitors (e.g., INFO-SEDD: 9.92±0.12 vs. next best: 9.73±0.43), the advantage is clear even with the reported variance.

- **Strength about "sample efficiency in low-data regimes" and "robustness to varying support size"**: These are placed in the appendix and are supporting but not central. They are genuine strengths but belong in the Nice-to-Haves category.

- **Strength about "seamless integration with pretrained models"**: Valid but common in the current ML landscape. Not a distinguishing contribution.

## Novel Insights

The most interesting observation that emerges from the reviews is that the paper's empirical results are substantially stronger than the theoretical presentation would suggest. The method works remarkably well on challenging synthetic benchmarks, yet the main-text derivation contains what appears to be a mathematical error or omission in Equation (2). This tension suggests either (a) the derivation is salvageable with proper exposition (e.g., the appendix contains the correct version), or (b) the method works for reasons not fully captured by the current theoretical framing. The absorbing-state trick (Equation 6) is genuinely clever and deserves more attention as a practical engineering contribution independent of the KL derivation. The synthetic results (Table 1) are genuinely surprising — no other estimator comes close — and this alone makes the paper worth attention from the community, provided the theoretical foundation can be clarified.

## Suggestions

1. **Rewrite Section 2.2 with a self-consistent derivation.** Start from a clearly stated identity (e.g., the Fokker-Planck equation for the evolution of log-ratio, or a pathwise KL decomposition analogous to the Girsanov-based approach in MINDE). Show explicitly how the Dynkin formula is applied and why the omitted boundary term vanishes. Even a brief sketch with a reference to the appendix for full details would be acceptable — the current version is insufficient.

2. **Add a paragraph in Section 4.1 describing the synthetic data construction.** Even one sentence specifying the generative process (e.g., "X and Y are generated from a latent variable model where..." or "dimensions are conditionally independent given a shared latent variable") and how ground-truth MI is computed would resolve the opacity concern.

3. **Discuss the discrepancy between the "Empirical MI estimate" and the 256–303 nats range in the text consistency test.** Explain what the "Empirical MI estimate" represents and why it differs from the theoretical range. This would preempt reader confusion.

4. **Include the missing baselines (MINE, NWJ, MINDE) in the model selection analysis (Table 2)** or explain why they were omitted. Report p-values for the correlations.

## Score and Decision

**Round 1 bracket**: After the initial calibration search, the paper was bracketed between weak anchors (~3.0, papers with broken or marginal contributions) and strong anchors (~8.0, papers with rigorous theory). The most directly relevant anchor is the MINDE paper (6.50), which uses the same diffusion-based MI estimation approach for continuous data.

**Round 2 narrowing**: Reading four additional anchors inside the bracket (6.0–7.0 range) confirmed the paper's position. The MINDE paper (6.50) was accepted despite dense mathematics because its Girsanov-based derivation rested on solid known theory; INFO-SEDD's main-text derivation has the additional problem of appearing mathematically inconsistent. The discrete diffusion convergence paper (7.00) has rigorous theory but is a pure theory paper. The f-DIME paper (5.60) has weaker experiments but more standard theoretical foundations. INFO-SEDD's empirical results are stronger than f-DIME's, but its theoretical presentation is weaker than MINDE's. The paper thus sits between 5.0 and 6.0.

**Final anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 0kWd8SJq8d (MINDE) | 6.50 | 1 | Stronger theoretical derivation (Girsanov-based); similar empirical quality. INFO-SEDD is clearly below this. |
| KC2MViQASx (f-DIME) | 5.60 | 1 | Weaker experiments (simple Gaussians only), cleaner theory. INFO-SEDD's experiments are substantially stronger. |
| pq1WUegkza (Discrete Diff. Conv.) | 7.00 | 2 | Pure theory paper with rigorous proofs. INFO-SEDD is not comparable — different genre. |
| peNgxpbdxB (Scalable Discrete Diff.) | 6.00 | 2 | Method paper with weak comparison baselines. INFO-SEDD has stronger empirical validation. |

The paper's core theoretical argument in the main text is not self-consistent, which is a significant gap for a top conference. The empirical results, while strong, cannot fully compensate for a derivation that appears flawed or incomplete as presented.

**Score**: 5.5 — Marginally below the acceptance threshold. The paper could become a strong candidate for acceptance after a major revision that clarifies and corrects the theoretical derivation in Section 2.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>