Now I have everything I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None.

### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me now write the full review.

**Calibration Report:**

**Round 1 — Bracketing:**
- Weak band (score < 3.5): kKXIYUi8ff (3.0), 2orBSi7pvi (3.0), XeGSIr7z6u (3.4), ICR3swcnaa (3.0), 46tjvA75h6 (3.0) — papers with fundamental flaws
- Middle band (3.5-7.5): dDdxbdhMsY Deep Temporal Deaggregation (5.0), r125wFo0L3 Large Trajectory Models (5.0), VRFotuGLfM DiffMove (6.2), UapxTvxB3N Trajectory-LLM (5.75), WeJEidTzff OD Flow (6.75)
- Strong band (7.5+): uKZdlihDDn (7.6), 8zJRon6k5v (8.0), EO8xpnW7aX (8.0) — papers with exceptionally strong contributions

**Initial bracket:** 5.0–7.0 (paper is clearly stronger than the 3.0-3.4 weak band, and weaker than the 7.5+ strong band)

**Round 2 — Narrowing:**
- Closest comparison: dDdxbdhMsY Deep Temporal Deaggregation (5.0) — the current paper's predecessor. The current paper addresses almost all of that paper's weaknesses (adds missing metrics, ablation studies, clearer presentation). Current paper is clearly superior.
- VRFotuGLfM DiffMove (6.2) — similar task domain, comparable quality. Current paper has stronger novelty (factorization framework) but some framing issues.
- YOKnEkIuoi Conditional Variational Diffusion (5.8, Accept) — had limited novelty concerns but was accepted. Current paper has stronger methodological novelty.
- WeJEidTzff OD Flow (6.75, Accept) — strong benchmark contribution. Current paper is comparable in quality.

**Final score: 6.0** — The paper sits above the 5.0 predecessor and comparable 5.0-5.8 papers, and just below the strongest 6.75 benchmark paper. The contributions are real and the method is novel, but overclaiming around "zero-shot" framing and an unaddressed KL metric concern keep it from scoring higher.## Summary

This paper presents TDDM (Temporal Deaggregation Diffusion Model), a hierarchical framework for trajectory generation that factorizes the problem into (1) spatial occupancy priors (marginal distributions over where people are) and (2) temporal dynamics learned via a transformer-based diffusion model. By canonicalizing each geographic region via a similarity transform, the model learns location-invariant motion patterns that can transfer across cities. The paper evaluates across three cities (Beijing, Porto, San Francisco) with six metrics and shows strong in-distribution results as well as promising out-of-distribution generalization when given only aggregate spatial statistics from target regions.

---

## Strengths

- **Spatial-temporal factorization is well-motivated and novel for trajectory generation.** The core idea — conditioning a diffusion model on aggregate spatial marginals rather than sample-specific conditions — is a clean design that decouples *where* people go from *how* they move. The canonicalization via similarity transform (translation, rotation, scaling to [-1,1]²) is a practical way to achieve location/rotation invariance without group-equivariant architectures, and the generalization results validate this choice.

- **Large-margin improvements over strong baselines on distributional metrics (Table 1).** TDDM achieves KL_sym of 0.277 vs. 1.153 (Diffusion-TS) and 1.232 (DiffTraj) — roughly a 4× reduction — while also attaining the best Pattern score (0.917 vs. 0.907), Density error (0.019 vs. 0.029), and Trip error (0.031 vs. 0.041). These margins are substantial and consistent across three cities on different continents.

- **Clean ablation study (Table 2) that isolates the spatial prior's contribution.** Removing the spatial prior degrades KL_sym from 0.277 to 1.334, and the "w/o spatial prior + rejection" variant (which explicitly tries to match the marginal via rejection sampling) still achieves only 1.588. This demonstrates that the temporal dynamics model adds significant value beyond what the conditioning signal alone provides — the improvement is not simply "circular."

- **Standardized multi-city, multi-metric evaluation framework.** Building a benchmark across three cities (Asia, Europe, North America) with six metrics spanning fidelity (TSTR), coverage (KL, JS), proportionality (Density, Trip), structural quality (Pattern), and length accuracy is a valuable contribution to the trajectory generation community, where evaluation has often been fragmented.

- **Visual results (Figure 2) confirm structural realism.** The log-density heatmaps show TDDM capturing road-level holes and density gradients much more faithfully than baselines, which smear or lose structure.

---

## Weaknesses

### Major

- **The "zero-shot" claim overstates what is demonstrated.** Algorithm 2 (line 3) computes the spatial prior *H* from target-region trajectory data (`H = f(r_c, X_target)`). The model is zero-shot in the sense that it requires *no gradient updates* on target data — but it does require access to spatially aggregated trajectory statistics from the target domain. This is a meaningful but weaker form of generalization than the standard "zero-shot" connotation (which typically implies no target data of any kind). The paper is transparent about this requirement, so this is a framing issue, not a methodological flaw. However, the contributions claim ("generalization to new regions without retraining or finetuning") and conclusion repeatedly use "zero-shot" language that invites a stronger interpretation than the setup supports. The authors should explicitly clarify what target data is needed and reframe the claim as "aggregate-conditioned transfer" or "data-efficient generalization."

- **The large KL improvements are partially attributable to conditioning alignment, and the paper does not disentangle this.** The KL divergences are computed on the 2D spatial marginal distribution (as shown in Figure 2, row 2, "Log-marginal"). Since the model is explicitly conditioned on this same marginal via *H*, the KL metrics partially measure conditioning alignment rather than purely temporal generation quality. This does *not* invalidate the results — the ablation with rejection sampling proves the temporal model adds genuine value (1.588 vs. 0.277 KL_sym) — but the paper repeatedly cites the "4× KL improvement" without acknowledging this structural advantage. The TSTR, Pattern, Density, and Trip metrics show more modest improvements (10–30% relative), which better reflect the temporal model's actual contribution. The paper would be strengthened by explicitly partitioning evaluation into spatial marginal metrics and temporal/structural metrics, and by adding a simple baseline that generates trajectories purely from *H* (e.g., random walks matching the marginal) to quantify what the temporal dynamics add beyond the prior.

### Minor

- **No statistical significance on most metrics.** Only TSTR reports standard deviations (±). Tables 1–3 report single runs per dataset for KL, Density, Trip, Length, and Pattern, making it impossible to assess variance. Given the large claimed improvements, multiple seeds with error bars would substantially strengthen confidence.

- **The intra-city generalization degradation is understated.** KL_sym doubles from 0.278 (100% coverage) to 0.545 (25% training), and JS nearly doubles (0.059 → 0.106). The paper describes this as "slightly lower" — this is a significant drop that should be acknowledged frankly. The retained Pattern (0.927 vs. 0.940) and TSTR (0.010 vs. 0.010) are genuinely impressive, but the distributional metrics tell a different story.

- **City-to-city generalization results are aggregated over only two target cities per entry**, hiding substantial variance (e.g., training on Geolife gives KL_sym 0.795 vs. training on Porto gives 0.335). The paper reports per-pair results only in the appendix. Including a per-pair breakdown in the main text would improve transparency.

- **The ablation "without spatial prior + rejection" is mentioned in the table but never described in the main text.** How rejection sampling is applied to match *H* from an unconditional generation is left unexplained. A brief explanation would help readers interpret this important ablation.

### Trivial

- None of substance.

---

## Nice-to-Haves

- **Add a baseline that also conditions on *H* to isolate temporal dynamics.** For example, sampling locations i.i.d. from *H* and connecting them with interpolated random walks, or a nearest-neighbor retrieval that matches *H*. This would directly quantify what the learned temporal dynamics contribute beyond the conditioning signal.

- **Report training/inference time and model size.** The paper targets "large-scale" generation but provides no efficiency analysis. This is relevant for practical deployment.

- **Add a discussion of when aggregate spatial statistics (64×64 histograms per 3×3 km region) are available vs. unavailable in practice** (e.g., census data, mobile phone aggregates, traffic monitoring). This would help readers assess the method's practical applicability.

---

## Removed Points

- **Privacy evaluation** — The paper explicitly scopes out privacy ("this work focuses exclusively on improving fidelity and cross-region generalization," line 21). Criticizing its absence is invalid — removed per Hard Rules.
- **Missing related work** — Removed per Hard Rules (no external verification possible).
- **Formatting/typo nitpicks** — Removed per Hard Rules (parser artifacts).
- **Speculative concerns about what the appendix may or may not contain** — Removed per Hard Rules.
- **Criticism that DiffTraj may be disadvantaged by unconditional generation** — The paper uses standard evaluation practices; this is speculative and removed.
- **Criticism that intra-city OOD shares road network** — This is the intended experimental design, not a flaw. Removed as a strawman weakness.

---

## Novel Insights

The key insight that emerges from this paper beyond its own contributions is the finding that **temporal dynamics (how people move) transfer much more cleanly across cities than across contiguous regions within the same city**. Training on Porto and generating for other cities (KL_sym 0.335) actually outperforms training on 25% of a target city and generating for the remaining 75% (KL_sym 0.545). This suggests that the temporal model is learning something genuinely universal about human mobility patterns — not just dataset-specific artifacts — and that the bottleneck in intra-city transfer is the diversity of training data, not geographic mismatch. This has practical implications: collecting diverse training data from even one representative city may be more valuable than collecting sparse data from many cities.

---

## Suggestions

1. **Reframe the generalization claims.** Replace "zero-shot" with "aggregate-conditioned" or "data-efficient" transfer. Clearly state in the contributions that target-region aggregate occupancy statistics are required, and discuss settings where such aggregates are available (e.g., census data, mobile phone handover statistics).

2. **Disentangle the KL metric interpretation.** Add one sentence in the evaluation section noting that KL divergences are computed on the spatial marginal, which the model is explicitly conditioned on, so these metrics partially measure conditioning alignment. Cite the rejection-sampling ablation as evidence that temporal dynamics still contribute substantially beyond the prior.

3. **Add error bars.** Run at least 3 seeds on the main table (Table 1) and report standard deviations for all metrics, not just TSTR.

4. **Report per-pair city-to-city results in the main text**, not just the appendix. The variance across source cities is significant (0.335–0.795 KL_sym) and worth discussing upfront.

5. **Describe the rejection sampling ablation** in the main text to help readers interpret the "w/o spatial prior + rejection" row in Table 2.

---

## Score and Decision

**Calibration Details:**
- Round 1 bracket: [5.0, 7.0] — paper is clearly stronger than the weak-band anchors (3.0–3.4) and weaker than the strong-band (7.5+)
- Round 2 anchors read in full:
  - dDdxbdhMsY (Deep Temporal Deaggregation, 5.0, Reject): predecessor paper with similar approach but missing metrics, ablations, and clarity. Current paper is substantially improved.
  - VRFotuGLfM (DiffMove, 6.2, Reject): trajectory recovery via diffusion; comparable quality but different task.
  - r125wFo0L3 (Large Trajectory Models, 5.0, Reject): motion prediction for autonomous driving; less novel than current paper.
  - YOKnEkIuoi (Conditional Variational Diffusion, 5.8, Accept): limited novelty concerns but accepted; current paper has stronger methodological novelty.
  - WeJEidTzff (OD Flow Generation, 6.75, Accept): strong benchmark + method contribution; current paper is comparable in quality.
- Final score (6.0) positioned relative to these anchors: above the 5.0–5.5 cluster and below the 6.75 strong-benchmark paper, comparable to the 6.2–6.5 range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>