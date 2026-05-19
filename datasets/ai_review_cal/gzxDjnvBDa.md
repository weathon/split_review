- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have all the information needed to produce the final consolidated review. Let me compile it.

---

## Summary

This paper proposes **dynamic frames** for SE(3)-invariant crystal structure modeling. Unlike prior work that defines a single global frame statically aligned with the entire unit cell (PCA or lattice frames), the method constructs a local frame per atom per layer using attention weights that quantify interatomic interaction strengths. The authors integrate this into Crystalformer (Taniai et al., 2024), creating CrystalFramer, and evaluate on three large datasets (JARVIS, MP, OQMD). Experimental results show consistent improvements over static frames and other state-of-the-art crystal encoders.

## Strengths

- **Consistent performance gains over static frames.** Tables 1–3 show CrystalFramer with max frames achieves the lowest MAE in 8 of 9 tasks across JARVIS, MP, and OQMD. This directly substantiates the claim that dynamic frames outperform conventional static frames (PCA, lattice).

- **Controlled ablation isolates the benefit of dynamic weighting.** The paper explicitly compares dynamic max frames against a static local frame variant (same algorithm but fixed distance-based weights $w_{ij(n)}=\exp(-r_{ij(n)}^2)$). On MP, the dynamic version outperforms the static one on all four tasks (e.g., bandgap 0.078 vs 0.083). This is a clean, direct test of the core hypothesis.

- **High cost-performance ratio.** CrystalFramer has only 0.6M parameters vs. 9.3M (PotNet), 3.3M (Matformer), and 4.4M (iComFormer), yet delivers better or competitive accuracy. Test time is also faster than these alternatives.

- **Unit-cell invariance by design.** Dynamic frames are defined using the full infinite crystal structure $\hat{P}$, not the unit-cell representation $(P,L)$. This ensures invariance to how the same crystal is boxed — an advantage over PCA frames that depend on the finite unit-cell coordinates.

- **Visual interpretability.** Figure 3 shows that dynamic frames (weighted PCA and max) highlight chemically meaningful local motifs (octahedra, tetrahedra) that vary per atom and per layer, whereas static frames give global axes that do not reflect local bonding.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Test-time frame handling is not specified.** The paper adopts stochastic FA (Duval et al., 2023) to break frame ambiguities, but never states what happens at test time. If a single random frame is sampled per test sample, predictions are non-deterministic and the reported MAEs are random variables whose variance is unknown. If multiple frames are averaged, the higher test-time cost should be stated. The paper should specify the protocol and, if stochastic sampling is used, report variance across repeated evaluations or provide evidence that frames are nearly unique for most crystals. This does not invalidate the results, but it is a specification gap that must be closed.

2. **Perturbation noise magnitude for max frames is not given.** The paper (Section 3.1) states that "small perturbation noise" is added to weights for tie-breaking during max frame construction, but does not specify the noise magnitude or distribution. If the noise is too large, frames become random; if too small, ties are not reliably broken. The magnitude should be documented and its sensitivity should be assessed.

3. **Unsupported claim about convergence speed.** The visual analysis section (Section 6) states "max frames converge faster during training due to the discrete nature of their construction" without any supporting data (no convergence curves shown, no quantitative comparison). This claim should either be removed or backed by evidence.

### Trivial

- The paper uses "Framer" in the architecture name "CrystalFramer" but "Framer" is not a standard word — this is a minor naming choice, not a substantive issue.

## Nice-to-Haves

- **Gradient flow through frame construction.** The paper acknowledges (line 96) that gradients from frames $F_i$ to weights $w_{ij(n)}$ are omitted because frame construction is not stably differentiable. This is a transparent design choice and does not undermine the results. However, it would be interesting to see if a relaxation (e.g., Gumbel-softmax for max frames, or a differentiable PCA surrogate) could further improve performance. This is a natural direction for future work, not a current flaw.

- **Multi-head frame analysis.** Since frames are constructed per attention head, analyzing whether different heads learn distinct frame directions (e.g., via cosine similarities between $e_1$ vectors across heads) could provide insight into what multiple frames capture.

- **Sensitivity analysis for max frame uniqueness.** A simple analysis showing how often the max frame's first axis is uniquely determined (i.e., the top weight is clearly larger than the runner-up) would alleviate concerns about stochastic tie-breaking at test time.

## Removed Points

These points were flagged for removal by the instructions; they are reproduced here for transparency but should not be weighed.

- **"Scope limitation to attention-based architectures"** — REMOVED because the paper already addresses this in Section 6 (lines 226), noting that Crystalformer's standard multi-head softmax attention is the suitable testbed and that other transformers with channel-wise sigmoid attention are less compatible. The paper is scoped appropriately.
- **"Missing tables from parsed text"** — REMOVED because this is a parser artifact; tables exist in the original submission.
- **"Missing appendix/proofs/references"** — REMOVED per policy; the parser strips these sections.
- **Criticism that the paper "challenges the conventional notion" is overstated** — REMOVED because this is a subjective opinion about rhetorical framing, not a substantive weakness. The claim is reasonable given that all prior crystal frame work used static global frames.

## Novel Insights

The reviews do not surface any genuinely novel insight beyond the paper's own contributions. The dynamic frames concept itself — constructing frames per atom per layer driven by learned interaction weights rather than static structural geometry — is the paper's core novel idea, and the reviews correctly identify it as such. The observation that frames can be a *dynamic function of the learned representation* rather than a fixed preprocessing step is the key insight, and the ablation against static local frames cleanly validates that the dynamic (attention-weighted) component drives the improvement.

## Suggestions

- In the rebuttal, specify the test-time frame protocol explicitly. If using a single stochastic sample (as in stochastic FA), report the variance of predictions over repeated runs for a subset of test materials. If using deterministic test-time inference (e.g., max-weight selection without noise, or full FA averaging), state this clearly and describe any computational overhead.
- Document the perturbation noise magnitude for max frame tie-breaking and provide a brief sensitivity analysis.
- Either add a training convergence plot (validation loss vs. epoch) comparing max frames, weighted PCA frames, and the baseline, or remove the unsupported claim about faster convergence.
- Consider adding a note about the potential for differentiable frame relaxations as future work, to fully address the gradient-blocking observation.
