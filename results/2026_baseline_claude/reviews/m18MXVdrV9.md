## Summary

INFO-SEDD introduces a discrete diffusion-based framework for estimating information-theoretic quantities (mutual information, entropy) over high-dimensional discrete data. The core approach derives a KL divergence estimator from Continuous Time Markov Chain (CTMC) theory using Dynkin's lemma (Eq. 4–5), substituting intractable score ratios with learned parametric approximations. A key technical insight is that absorbing-state CTMCs allow a *single* jointly trained score model to compute both joint and marginal scores (Eq. 6), yielding the INFO-SEDD-J and INFO-SEDD-C variants. The method is validated on synthetic benchmarks, entropy estimation in Ising models, text summarization model selection, and TATA-box motif discovery in genomic promoter sequences.

---

## Strengths

- **Genuinely novel derivation**: Applying Dynkin's lemma to the log-ratio of two CTMCs sharing the same generator but differing in initial conditions is a clean and non-trivial insight. The absorbing-state trick that allows a single score model to recover marginal scores (Eq. 6, Appendix A.3) is particularly elegant and reduces training cost substantially.

- **Strong synthetic results**: Table 1 shows INFO-SEDD maintains near-exact estimates up to MI=50, D=50, where every competing method (including GAN-DIME, MINDE, MINE, SMILE, NWJ) degrades severely. This directly addresses the known exponential-sample limitation of variational lower-bound estimators.

- **Practical pretrained-model integration**: INFO-SEDD fine-tunes CADUCEUS and MDLM-SMALL rather than training from scratch, a significant practical advantage over methods that require bespoke architectures for each task.

- **Compelling real-world demonstrations**: The TATA-box discovery (Figure 5) is particularly strong — INFO-SEDD localizes the known TATA-box motif at −39 to −26 relative to TSS purely from MI estimates, with a clear spike in the MI profile. The method also achieves Pearson r=0.740 with human consistency scores in text summarization (Table 2), outperforming all competing estimators.

- **Theoretical guarantees**: The error bound in Eq. 7 separates estimation error (linear in score approximation error) from truncation bias (exponentially vanishing), providing a formal consistency certificate that variational bounds cannot match.

---

## Weaknesses

### Fatal
None.

### Major

1. **Computational cost is unaddressed in the main paper.** Training a discrete diffusion model (even a fine-tuned one) is substantially more expensive than training a variational MI estimator like MINE or SMILE. The claim that INFO-SEDD is "scalable" is never backed by a wall-clock or FLOPs comparison in the main text. The convergence comparison is relegated to Appendix C.1.3. Without at least an order-of-magnitude analysis of training cost vs. accuracy trade-off, a practitioner cannot make an informed choice. For example, running 10^5 training steps with a Transformer backbone is likely orders of magnitude more expensive than training MINE with the same backbone.

2. **Approximation validity is understated.** The step from Eq. (2) to Eq. (4) drops the initial-condition term E[log p₀/q₀(X₀)] by arguing that both distributions converge to π at time T. This is only exact as T→∞. The resulting truncation bias in Eq. (7) vanishes exponentially as p_T(∅^D) → 1, but no empirical analysis of how large T needs to be in practice (or what bias remains for the T used in experiments) is provided in the main paper. For the text experiments with sequences of length ~256 and vocabulary size ~32k, the forward process dynamics could leave a non-negligible truncation bias.

### Minor

1. **Consistency tests use approximate, not exact, reference MI.** In the text experiment, the reference (256–303 × ρ nats) is derived from entropy-rate estimates of English text extrapolated over summary length — a rough order-of-magnitude argument. The claim that INFO-SEDD "closely matches the empirical derivation" is therefore an alignment with an imprecise reference, not with a ground truth. The genomics consistency test uses a classifier-based MI approximation, also not exact. These are reasonable engineering choices but should be flagged more clearly as approximate references.

2. **Comparison fairness in real-world experiments.** Competing methods operate on learned continuous embeddings, while INFO-SEDD works directly on tokens. This is intentional (indeed it is the point), but the backbone architectures differ in a meaningful way — competitors share an embedding lookup table with INFO-SEDD's architecture, but the number of parameters in the score network vs. variational estimator heads may differ. A more explicit parameter count comparison would clarify whether the gains are purely due to the discrete formulation.

3. **INFO-SEDD-J vs. INFO-SEDD-C gap.** Table 2 shows a 19-point Pearson gap between INFO-SEDD-C (r=0.740) and INFO-SEDD-J (r=0.550) on consistency. While the paper explains this as a harder optimization problem for J, no practical guidance is given on when each variant should be preferred. Figure 4 (genomics) shows the opposite ordering in some regimes. A decision rule or ablation would help practitioners.

### Trivial
None worth recording.

---

## Nice-to-Haves

- A computational cost table (training time, memory) alongside accuracy in Table 1 would make the "scalable" claim concrete.
- Sensitivity analysis for the time horizon T and the resulting truncation bias in at least one real-world experiment.
- A brief discussion of failure modes: under what conditions (very large vocabulary, very long sequences, non-absorbing CTMC) would INFO-SEDD be expected to struggle?

---

## Novel Insights

The central insight that is genuinely new: by coupling two CTMCs with identical generators but different initial conditions and applying Dynkin's lemma to the log-ratio, one can construct a tractable Monte Carlo estimator of KL divergence for discrete distributions that inherits the consistency properties of discrete diffusion models without requiring importance sampling. The further observation that choosing absorbing-state generators makes the marginal score computable from the joint score model (Eq. 6) — avoiding two separate training runs — is non-trivial and directly enables the single-model variant that scales to pretrained architectures. This combination of ideas has not appeared in prior MI estimation literature, and provides a clean template for extending diffusion-based estimators to the discrete domain.

---

## Suggestions

- Report training time and peak memory for all methods in Table 1, even approximately.
- Include a sensitivity experiment varying T in at least one synthetic setting to empirically characterize the truncation bias from Eq. 7.
- Add a short "when to use J vs. C" paragraph in Section 3, with heuristics based on relative dimensionality of X and Y.

---

## Score and Decision

The paper presents a technically sound and novel approach to a genuinely hard problem. The core derivation is elegant, the absorbing-state trick is an important practical contribution, and the results—particularly the TATA-box discovery and high-MI synthetic benchmarks—are convincing. The main unresolved issue is the lack of computational cost analysis, which is important for practitioners deciding whether to adopt this method. The consistency tests rely on approximate references, but this is acknowledged. These weaknesses are real but do not invalidate the contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>