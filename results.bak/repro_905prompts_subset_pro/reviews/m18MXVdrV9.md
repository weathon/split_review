I now have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

INFO-SEDD proposes the first mutual information (MI) estimator for high-dimensional discrete data based on continuous-time Markov chain (CTMC) diffusion processes. By leveraging Dynkin's formula and the score functions of CTMCs with absorbing states, the method expresses KL divergence as an integral that can be estimated via a single parametric model. Two MI variants (joint and conditional) plus an entropy estimator are presented. Experiments on synthetic benchmarks show clear outperformance over variational and embedding-based competitors, especially in high-MI/high-dimensional regimes. Real-world applications in text summarization model selection and genomic motif discovery demonstrate practical utility, and the method integrates seamlessly with pretrained discrete diffusion backbones (MDLM, CADUCEUS).

## Strengths

- **First discrete-diffusion MI estimator.** The paper introduces a genuinely novel approach for estimating information-theoretic quantities on discrete data without relying on continuous embeddings. The use of CTMCs with Dynkin's lemma for KL estimation, adapted to discrete spaces, fills a clear gap in the literature (Section 2.2, Section 3).

- **Strong and consistent synthetic results.** Table 1 demonstrates that INFO-SEDD recovers near-ground-truth MI values (e.g., 47.77 ± 1.18 for MI=50, D=50) where all competitors degrade severely. The method maintains accuracy across varying support sizes, sample sizes, and high-MI regimes.

- **Clever single-model design via absorbing states.** By adopting an absorbing transition matrix, a single score model trained on the joint distribution suffices to compute marginal scores (Equation 6). This removes the need for separate models and is a practical, well-motivated design choice (Section 3).

- **Real-world applications with pretrained models.** The method is demonstrated on text summarization (SUMMEVAL, using MDLM-SMALL) and genomics (promoter motif discovery, using CADUCEUS), showing that INFO-SEDD estimates correlate well with human metrics (Pearson 0.740 for consistency, Table 2) and can identify known biological motifs (Figure 5) using pretrained backbones with minimal modification.

- **Theoretical error decomposition.** Equation (7) provides a clean error bound decomposing into estimation error and exponentially decaying truncation bias, supporting the consistency claim.

## Weaknesses

### Fatal

None.

### Major

- **The KL divergence derivation in Section 2.2 is presented with significant mathematical errors.** Equation (2) claims KL[p₀ || q₀] = E[log(p₀/q₀)(X_T)], which is incorrect: the KL divergence is an expectation over X₀ ∼ p₀ evaluated at X₀, not at X_T (which is distributed according to the forward-perturbed marginal p_T). The subsequent statement that "we omit the term E[log(p₀/q₀)(X₀)], as both p₀ and q₀ converge to π" is garbled — it is p_T and q_T (the forward marginals) that converge to π, not the initial distributions p₀ and q₀, and the omitted term is essentially the KL divergence itself. The intended derivation — start from KL[p₀||q₀] = E_{X₀}[log(p₀(X₀)/q₀(X₀))], apply Dynkin's formula to log(p_t/q_t), and exploit p_T = q_T = π — is standard in the diffusion estimation literature, but the paper's version does not present it correctly. This does not mean the method is wrong (the final estimator in Equation 5 and the error bound in Equation 7 are consistent with the intended approach, and the experimental results validate it), but the current exposition seriously undermines trust and must be corrected with a rigorous step-by-step derivation.

### Minor

- **Model selection experiment is difficult to verify from the main text.** Figures 2 and 3 show data points labeled M5 through M100 with MI estimates on the x-axis and consistency scores on the y-axis. The paper states that SUMMEVAL provides 23 models with human judgments for 15 of them, which should yield at most 15 (or 23) data points for a per-model analysis. The paper mentions "generating a collection of datasets" but the relationship between these datasets and the plotted points (which appear to number ~96) is unexplained in the main text. The correlation results in Table 2 remain informative, but the reader cannot verify what exactly is being plotted. Clarifying whether these are per-instance, bootstrapped, or multi-dataset points would resolve this.

- **Synthetic benchmark confounds dimensionality with MI.** In Table 1, D and MI increase together (MI=10, D=10; MI=20, D=20; …; MI=50, D=50). This makes it impossible to disentangle whether competitors fail due to high MI, high dimensionality, or both. Varying these independently would strengthen the diagnostic value.

### Trivial

- The consistency test for text summarization (Section 4.2) assumes MI grows linearly with pairing probability p "under the assumption of MI being significantly larger than log 2." While this is a reasonable heuristic backed by entropy-rate estimates from the literature, the paper does not derive or empirically verify the functional form for this specific setting.

## Nice-to-Haves

- A discussion of computational cost (training and inference) relative to variational estimators, which is important for practitioners choosing between methods.
- Pseudo-code for the estimators in the main text rather than only in the appendix, given the complexity of the approach.
- An ablation varying D while holding MI constant, and vice versa, in the synthetic benchmark.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that the derivation is "structurally" wrong and the method cannot be trusted.** While Equation (2) is indeed incorrectly written, the harsh critic themselves acknowledges the intended derivation is correct, the error bound (Eq 7) is consistent, and the experimental results strongly validate the method. The issue is with presentation, not methodological soundness. This is a major weakness (bad derivation) but not a fatal flaw. — REMOVED as fatal; kept as Major with adjusted severity.

- **Harsh critic's claim that correlation analysis on 15 points would not be statistically significant.** This depends on the actual number of data points used, which is unclear from the text but may be larger than 15 if per-instance or bootstrapped estimates are used. This is speculative without knowing what the appendix specifies. — REMOVED as a standalone point; merged into the minor weakness about experimental clarity.

- **Strength Finder: "The paper addressed an important problem."** — Generic; removed as it is not specific to this paper.

- **Strength Finder: "Seamless integration with pretrained models."** — Kept, as it is concrete and supported by the text.

- **Harsh critic: missing pseudo-code in main text.** — Moved to Nice-to-Haves as a presentation suggestion, not a weakness.

- **Harsh critic: no discussion of computational cost.** — Moved to Nice-to-Haves.

- **Harsh critic: reliance on absorbing-state CTMC forces a specific forward process; discussion of alternatives would help.** — This is scope creep; the absorbing-state design is a feature that enables single-model training. — REMOVED.

- **Harsh critic: quantify performance gap between training from scratch vs. fine-tuning.** — This is a nice-to-have but not a weakness. — REMOVED.

- **Harsh critic: formatting/style nitpicks.** — REMOVED per instructions.

## Novel Insights

The paper's use of an absorbing-state CTMC to enable a single joint model to serve both joint and marginal score estimation (Equation 6) is a genuinely elegant insight. This property — that when subcomponents can only transition to an absorbing state ∅, the marginal density ratios can be extracted from the joint model by conditioning on the other variable being fully absorbed — is not obvious and has practical consequences beyond MI estimation. It makes the approach scalable in a way that a naive implementation of Equation (5) would not be, and underlies the method's ability to handle arbitrary masking windows in the motif discovery application (Figure 5) without retraining.

## Suggestions

- **Rewrite the derivation in Section 2.2 from first principles.** Start explicitly from KL[p₀||q₀] = E_{X₀∼p₀}[log(p₀(X₀)/q₀(X₀))]. Define f(x,t) = log(p_t(x)/q_t(x)). Apply Dynkin's formula (Equation 3). Use p_T = q_T = π to eliminate the boundary term at T. Show that the result simplifies to an integral expression. Clearly distinguish exact equalities from approximations introduced by score model error and finite T. This will resolve the trust issue and strengthen the paper significantly.

- **Clarify the model selection data points.** State explicitly how many points are plotted in Figures 2–3, what each point represents (per-summary, per-model, per-dataset-split), and how the correlation analysis is performed. If the number of independent model-level data points is small (e.g., 15), include confidence intervals or significance tests for the reported correlations.

## Score and Decision

### Calibration Anchors Used

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| MINDE (MI Neural Diffusion Estimation) | 0kWd8SJq8d | 6.50 | R1 | Most directly comparable: continuous diffusion MI estimation. INFO-SEDD extends to discrete domain with real-world applications; comparable novelty and presentation issues. |
| SEDD (Discrete Diffusion Language Modeling) | 71mqtQdKB9 | 6.60 | R2 | Foundational discrete diffusion paper INFO-SEDD builds on. Both had theoretical presentation issues; INFO-SEDD has more complete experiments. |
| f-DIME (MI via f-Divergence) | KC2MViQASx | 5.60 | R1 | Less novel framework, narrower experiments. INFO-SEDD is clearly stronger. |
| DDPP (Steering Masked Discrete Diffusion) | Ombm8S40zN | 6.25 | R2 | Discrete diffusion application paper. INFO-SEDD has broader scope and stronger novelty. |
| InfoNet | PyHRUMxKbT | 5.75 | R1 | Different MI estimation approach; INFO-SEDD is more novel and better evaluated. |
| Conditional MI Dynamic Feature Selection | Oju2Qu9jvn | 7.33 | R2 | Different domain; stronger theoretical guarantees than INFO-SEDD but not diffusion-based. INFO-SEDD is below this. |
| GIO | 3NnfJnbJT2 | 7.00 | R2 | Different domain entirely; INFO-SEDD below this. |

**Round 1 bracket**: 5.5–7.5. The paper is clearly above the 3.0-anchored weak band (rAZ3yCpc3K, 46tjvA75h6, etc.) and comparable to MINDE (6.50) and SEDD (6.60).

**Round 2 narrowing**: INFO-SEDD is slightly stronger than MINDE (6.50) due to the discrete data focus being a harder and more underserved problem, plus the real-world applications and pretrained model integration. It is comparable to SEDD (6.60) in quality but with a different contribution type (MI estimation vs. generative modeling). INFO-SEDD is clearly below the 7.00+ anchors (GIO, Conditional MI) which have stronger theoretical contributions and cleaner presentations.

**Final placement**: 6.5 — at the acceptance threshold, comparable to MINDE which was accepted at 6.50. The derivation presentation issue (Major weakness) keeps it from scoring higher, but the novelty of the discrete-diffusion MI formulation, strong synthetic results, and compelling real-world applications justify acceptance contingent on fixing the derivation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>