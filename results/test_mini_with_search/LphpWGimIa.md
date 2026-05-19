Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper trains sparse autoencoders (SAEs) on attention layer outputs (pre-linear projection) and demonstrates they yield sparse, faithful, interpretable decompositions across models up to 2B parameters. The paper's main contributions are: (1) establishing that attention-output SAEs are a useful research tool, (2) using weight-based head attribution to systematically analyze all 144 heads in GPT-2 Small and estimate head polysemanticity, (3) discovering that seemingly redundant induction heads actually specialize (long-prefix vs. short-prefix induction), and (4) resolving an open question about the "positional signal" in the IOI circuit by identifying it as an "and"-related feature, with causal validation.

## Strengths

1. **Well-validated discovery that SAEs on attention outputs yield sparse, interpretable decompositions across model scales.** Table 1 reports L0 sparsity (3–21 for GPT-2 Small layers), >75% cross-entropy loss recovered on most layers, and 60–97% of sampled features judged interpretable. The "board induction" case study in Section 3.3 includes specificity/sensitivity plots, false-positive and false-negative analysis, meeting the standard set by prior SAE work.

2. **Novel interpretability findings validated with independent causal evidence that does not rely on the SAEs themselves.** (a) The long-prefix vs. short-prefix induction head specialization (Section 4.2): synthetic prefix-length experiments show a sharp phase change for head 5.1 but not 5.5; targeted interventions on real examples confirm the pattern. (b) The "and" signal in the IOI circuit (Section 4.3): noising that preserves the "and" relation while corrupting other properties recovers ~93% of logit difference, causally resolving an open question from Wang et al. (2023). These findings advance understanding beyond prior work.

3. **Weight-based head attribution enables systematic interpretation of all 144 attention heads in GPT-2 Small** (Section 4.1), identifying known motifs (induction, previous-token, successor, duplicate-token heads) and novel ones (preposition mover heads). The polysemanticity of head 10.2 is validated with synthetic datasets and ablation experiments, directly linking SAE-derived features to causal behavior.

4. **Public release of trained SAE weights, feature dashboards, and an interactive exploration tool**, supporting replication and further research.

## Weaknesses

### Fatal
None.

### Major

- **RDFA is listed as a contribution (item 4 in the introduction) but not empirically demonstrated anywhere in the main paper.** The recursive direct feature attribution method is described in Section 2 and a visualization tool is released, but Sections 3–4 use only weight-based head attribution, direct feature attribution, or standard causal interventions. No concrete analysis result relies on RDFA. The paper should either (a) include a brief case study showing RDFA in action (e.g., tracing an attention SAE feature back through earlier layers), or (b) explicitly remove RDFA from the numbered list of contributions and present it only as a tool release.

### Minor

- **The "alongside" control in the IOI noising experiment (Section 4.3) is confounded.** Replacing "and" with "alongside" changes token frequency, tokenization, and syntax. The observed 43% logit-difference recovery could partially reflect these confounds rather than the specific role of the "and" token. A stronger control would use another common conjunction (e.g., "or" or "but") that preserves the sentence structure more closely while removing the "and" relation.

- **The polysemanticity estimate (≈90% of heads) rests on a fragile heuristic.** The estimate is derived from whether the top-10 features attributed to each head are "closely related" — a subjective judgment on a small sample (14/144 heads passed). Additionally, weight-based head attribution (Equation 3) uses slice-norm as a proxy that could be dominated by heads with naturally large output norms. The paper should report this as a rough lower bound rather than "≈90%," and the validation of head 10.2, while convincing for that single case, does not calibrate the overall estimate's error rate.

- **The claim that induction features may be "unique to attention" (Section 3.3) is weakly supported.** The paper hedges with "we hypothesize," but even as a hypothesis it is backed only by a negative statement about the authors' awareness of prior work. Since the paper does not check whether MLP SAEs fire on the same induction examples, this claim should be softened further (e.g., "we speculate" or simply dropped), or the check should be performed.

### Trivial

- The loss-recovered metric uses a **zero-ablation baseline** rather than the mean-ablation baseline common in prior SAE work (Bricken et al. 2023). Zero ablation is a weaker baseline, so the reported numbers may be inflated relative to the literature. The authors should either report loss-recovered relative to mean ablation or justify why zero ablation is the appropriate choice for attention outputs.

## Nice-to-Haves

- Report the effect sizes and standard errors for the causally relevant SAE features in the IOI analysis (how much does each of the three features' ablation reduce logit difference?).
- Include a brief discussion of the weight-based head attribution limitation: slice-norm is a proxy that does not account for differences in per-head output norms.

## Removed Points

These points were flagged in the input reviews but are removed or downgraded per the filtering protocol:

- **Concerns about confidence intervals being "in the appendix" (Harsh Critic):** Removed per rule that missing appendix content is not a valid weakness (parser-stripped sections exist in the original).
- **Request for SAE hyperparameters and training details in the main paper (Harsh Critic):** Removed as a reproducibility nitpick — these details are standard to defer to the appendix.
- **"Missing related works" concerns:** Removed per rule that the reviewer cannot verify existence of un-cited works.
- **Strength Finder's "RDFA and tool release" as a strength conflicting with the RDFA weakness:** Kept as a strength (the method IS introduced and the tool IS released) but the weakness notes the gap between claimed contribution and empirical demonstration — these are compatible.
- **Strength Finder's generic strengths (e.g., "addressed an important problem"):** Removed per rule that generic/superficial strengths should be dropped.

## Novel Insights

The most distinctive pattern across the reviews is the tension between the paper's breadth and its depth. The harsh critic correctly identifies that the paper lists four contributions but only three are substantiated with concrete results (RDFA being the unsubstantiated one). At the same time, the two main empirical discoveries — induction head specialization and the "and" signal in IOI — are each validated with methods that do not depend on the SAEs themselves, which is a notably rigorous standard for this type of work. The paper would benefit from either cutting the RDFA claim or meeting it with evidence, but this does not undermine the core validated contributions.

## Suggestions

1. **Add a better control for the IOI "and" noising experiment** (replace "and" with "or" or "but" instead of "alongside") to rule out confounds from tokenization and syntactic changes.
2. **Either demonstrate RDFA with a brief case study in the main paper or remove it from the numbered contribution list** and present it only as a tool release.
3. **Report the polysemanticity estimate as a rough lower bound** (not "≈90%") with explicit caveats about the heuristic's fragility.
4. **Soften the "unique to attention" claim** to "we speculate" or check a few MLP SAEs on the same induction examples.
5. **Report the per-feature effect sizes for the three causally relevant IOI features** to improve reproducibility.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| Rngn25PSdd.md (clinical SAE) | 1.50 | R1 (weak) | Much weaker than current paper |
| tWe5owhOyU.md (SALVE) | 2.00 | R1 (weak) | Much weaker |
| DjxNqXsApM.md (Ordered SAEs) | 3.00 | R1 (weak) | Much weaker |
| QNdf6wbjT3.md (influence SAE) | 2.67 | R1 (weak) | Much weaker |
| dADwCplxyC.md (multimodal monosemanticity) | 3.00 | R1 (weak) | Much weaker |
| DSOTgzeH3w.md (Limits of SAEs) | 6.00 | R1 (mid) | Comparable quality, different contribution type |
| 33wY6AI13k.md (Price of Amortized) | 5.00 | R1 (mid) | Weaker |
| EjInprGpk9.md (Same data, diff features) | 5.50 | R1 (mid) | Weaker |
| VtWkPIbAQ8.md (Taming Polysemanticity) | 4.50 | R1 (mid) | Weaker |
| UJ2UUjT2ko.md (Mixing Mechanisms) | 8.00 | R1 (strong) | Stronger — deeper mechanistic analysis |
| RDerF20JYT.md (protein generation) | 8.00 | R1 (strong) | Unrelated topic, stronger paper |

**Round 1 bracket:** 6.0 – 7.5

**Round 2 — Narrowing:**
| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| iPFlJESrsh.md (Filter Heads) | 6.50 | R2 | Similar quality — narrower scope but cleaner experiments; current paper is slightly stronger in breadth and significance of findings |
| Timsb74vIY.md (Formal MI) | 7.33 | R2 | Stronger — more methodological novelty (provable guarantees); current paper is more applied but has solid empirical discoveries |
| gdvOF1OMa7.md (Localizing ICL) | 6.50 | R2 | Similar quality — different domain, less well-validated |
| 9A2etpDFIB.md (Low-Rank Sparse Attention) | 6.00 | R2 | Weaker — less well-validated findings |
| bojVI4l9Kn.md (Temporal SAEs) | 6.50 | R2 | Similar quality — proposed new method variant; current paper has better-validated interpretability discoveries |

**Final score rationale:** The paper is stronger than the 6.0–6.5 anchor papers (more significant empirical discoveries, broader validation) but not as methodologically novel as the 7.33 formal verification paper. Its core weakness is the RDFA gap, which is real but does not undermine the three main validated contributions. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>