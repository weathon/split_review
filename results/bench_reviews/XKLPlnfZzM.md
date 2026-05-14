Now I have good coverage of the paper and anchors. Let me compile the review.

---

## Summary

The paper proposes the Temporal Deaggregation Diffusion Model (TDDM), a hierarchical diffusion framework that factorizes trajectory generation into spatial occupancy priors (where people move) and temporal dynamics (how they move). It canonicalizes geographic regions via similarity transforms, enabling a single model to generate trajectories across diverse locations. The authors evaluate on three cities across three continents, comparing against GAN-, VAE-, and diffusion-based baselines, and demonstrate strong improvements in distributional coverage metrics as well as cross-city generalization.

## Strengths

- **Novel spatial-temporal factorization with explicit regional canonicalization**: The idea of decoupling spatial occupancy from temporal dynamics, combined with region-wise similarity transforms for coordinate normalization, is conceptually clean and well-motivated. Section 3 provides clear architectural and algorithmic details, and the factorization is the key driver of TDDM's empirical gains.

- **Comprehensive evaluation across multiple quality dimensions and datasets**: The benchmark spans three cities (Beijing, Porto, San Francisco) with metrics covering fidelity (TSTR, Length Error), diversity/proportionality (KL divergences, JS, Density/Trip Error), and generalization (intra-city and city-to-city transfer). This is broader than typical trajectory-generation evaluations and reveals consistent patterns across datasets.

- **Strong empirical results**: TDDM achieves substantial improvements over baselines on distributional metrics (e.g., KLsym 0.277 vs. 1.153 for Diffusion-TS; JS 0.059 vs. 0.198) while maintaining competitive fidelity (TSTR 0.011 vs. 0.013–0.014). The ablation study (Table 2) cleanly isolates the contribution of spatial priors, showing KLsym degrades by nearly 5× when priors are removed.

- **Cross-city generalization**: TDDM transfers to new cities without retraining or fine-tuning, maintaining Pattern scores above 0.915 across all source-target pairs. The finding that Porto acts as a surprisingly strong universal source dataset is interesting and practically useful.

- **Robustness to preprocessing choices**: The map-matching ablation (Table 9) confirms that TDDM's gains stem from the deaggregation framework rather than preprocessing artifacts.

## Weaknesses

### Fatal
None.

### Major

- **Terminology: the generation task is not truly "unconditional."** The paper frames its task as "unconditional trajectory generation" (Section 2, Section 4.1), but TDDM explicitly conditions on spatial prior *H* computed from the training data. Section 3 acknowledges this conditioning, and the method's contribution is precisely this factorization. However, presenting results as "unconditional" when the model receives a pre-computed marginal occupancy distribution creates a subtle mismatch: TDDM is explicitly given the answer to *where* density should be, while baseline models must learn this implicitly from the same training data. This does not invalidate the comparison — both models see the same training data, and the factorization *is* the contribution — but the terminology should be corrected throughout (e.g., "distribution-conditioned" or "prior-guided" generation). The abstract, title framing, and Section 4.1 heading should reflect this.

- **"Zero-shot" generalization requires target-domain aggregate data.** Algorithm 2, line 3 unambiguously shows that *H* is computed from target-city trajectories (*f*(*rc*, Xtarget)). The paper acknowledges this in the text ("the model ϵθ never receives individual target trajectories, only their aggregate spatial distribution") but continues to use "zero-shot" and "without retraining or finetuning" as the primary framing. For city-to-city transfer, this means one must possess real trajectories from the target city to construct *H*. While aggregate occupancy is arguably easier to obtain than individual trajectories, this is not zero-shot in the standard ML sense (no access to the target domain). The paper should more precisely characterize what is required — aggregate distributional information — and calibrate the "zero-shot" language accordingly.

### Minor

- **No comparison against baselines augmented with the same spatial prior.** The paper argues that the factorization drives the gains, but it does not test whether existing diffusion-based trajectory models (e.g., DiffTraj, Diffusion-TS) would also benefit if supplied with *H* as an additional conditioning channel. Such an experiment would more cleanly isolate whether the architectural factorization or simply the availability of the spatial prior is responsible for the improvements. The current ablation (Table 2, removing *H* from TDDM) demonstrates that the prior is essential for TDDM but does not show that the factorization is superior to simply appending *H* to a baseline. This does not threaten the core contribution but would strengthen the paper.

- **Intra-city 25% vs. Porto comparison is confounded.** Section 4.3 notes that training on Porto generalizes better than training on 25% of the target city. However, the 25% case uses a spatial prior derived from only the training quadrant while the Porto case uses the full target-city prior. These are not comparable in terms of the spatial information available to the model. The paper should either equalize the prior quality or discuss this asymmetry explicitly.

### Trivial

- The phrase "unconditional part" in the Figure 3 caption is misleading given the conditioning on *H*.
- Variance/repeatability for metrics beyond TSTR (e.g., KL divergences, Density Error) is not reported; reporting these would strengthen confidence in the margins.

## Nice-to-Haves

- A sensitivity analysis showing how performance degrades as spatial prior quality is reduced (e.g., coarser grids, noisy occupancy estimates) would demonstrate practical robustness for settings where only approximate priors are available.
- Extending *H* with temporal marginals (e.g., time-of-day priors, length distributions) as suggested in the Future Work section would be a natural next step that could address the Length Error weakness in cross-city transfer.
- Testing whether the factorization approach works at different spatial scales beyond the 3×3 km default would help establish generality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Invalid comparison to unconditional baselines — TDDM has an unfair advantage"**: REMOVED as a fatal claim. TDDM and baselines both access the same training data. TDDM explicitly computes *H* from that data as part of its factorization; baselines must learn the spatial distribution implicitly. This is a fair test of whether explicit factorization outperforms implicit learning — exactly the contribution being evaluated. The concern is downgraded to a terminology issue (see Major weakness 1).

- **"Generalization claims are entirely invalid because target-city data is needed"**: REMOVED as a fatal claim. The paper does disclose the *H* requirement in both Algorithm 2 and the surrounding text. The concern is valid but properly downgraded to a terminology/precision issue (see Major weakness 2). The capability itself — generating trajectories for new cities using only aggregate occupancy without fine-tuning — is genuine and valuable.

- **Various formatting/style nitpicks**: REMOVED per hard rules. These are parser artifacts, not author errors.

- **Missing related works**: REMOVED per hard rules. Cannot confirm existence of uncited works.

- **Reproducibility concerns about code/model availability**: REMOVED per hard rules. The paper provides an anonymous repository link and the models/tools cited are assumed to exist.

## Novel Insights

The paper makes a genuinely interesting observation that spatial occupancy priors act as a surprisingly powerful bridge for cross-city transfer, to the point where a model trained entirely on Porto can outperform a model trained on 25% of the target city's data for distributional coverage. While this comparison has a confounding factor (prior quality differs, as noted above), the broader finding that temporal dynamics transfer well across cities while spatial distributions do not is a useful empirical insight for the trajectory generation community. It suggests that future work on transferable trajectory models should focus on learning universal motion patterns while accepting that spatial occupancy will typically need to be supplied per-target-region.

## Suggestions

- Replace "unconditional" throughout with a more precise term such as "distribution-conditioned" or "prior-guided." The abstract and Section 4.1 heading should be updated.
- Qualify "zero-shot" language: clarify that city-to-city transfer requires aggregate occupancy data from the target but no individual trajectories or model updates. Consider "prior-guided transfer" or "aggregate-conditioned generation."
- Add a brief discussion in Section 4.1 acknowledging that TDDM's explicit access to spatial marginals from training data gives it a structural advantage on KL-based metrics, and that this is by design — the factorization is the contribution.
- If feasible, include a sensitivity analysis on prior quality (e.g., coarser grids) to show robustness.
- Report variance for non-TSTR metrics across multiple seeds.

## Score and Decision

**Anchor comparison:**

| Anchor | Score | Comparison to TDDM |
|--------|-------|---------------------|
| TrajFlow (`BDOldEjwCE`) | 6.50 | Most comparable: GPS trajectory generation at scale with flow matching. Similar empirical strength and evaluation breadth. TDDM has cleaner conceptual contribution (factorization) but terminology issues TrajFlow avoids. |
| What Happens Next (`t1vMYl1yhe`) | 6.67 | High-scoring trajectory forecasting paper with novel task formulation. Strong evaluation. TDDM has similarly strong empirical results and broader generalization experiments but imprecise terminology. |
| Unconditional Human Motion (`OHZRUCa1HW`) | 5.00 | Below-SOTA results and limited baselines led to rejection. TDDM is demonstrably stronger: clear SOTA improvements, comprehensive baselines, generalization experiments. |
| GeoDiffusion (`w7xpNeFIbb`) | 4.00 | Trajectory diffusion model rejected for limited novelty, missing implementation details, unsubstantiated claims. TDDM has substantially clearer contributions, better ablation, and more transparent methods. |
| DDM-TS (`jBNGp43uUd`) | 3.50 | Decoupled diffusion for time series (trend-seasonality). Rejected for oversimplification, limited novelty, narrow evaluation. TDDM's factorization is better motivated and more thoroughly evaluated. |
| DiTraj (`zWRmev5IQ4`) | 4.50 | Training-free trajectory control for video generation. Rejected. Different domain but similar mid-range score pattern. |
| Fine-Grained Traffic (`khNIU4Lzn5`) | 4.00 | Traffic forecasting benchmark paper. Rejected. TDDM is more complete. |

TDDM sits above the 4.0–5.0 reject band (GeoDiffusion, DDM-TS, Unconditional Human Motion) and is comparable to or slightly below the 6.5–6.67 accept-poster band (TrajFlow, What Happens Next). The principal differentiator from the high-scoring anchors is terminology precision — TDDM's "unconditional" and "zero-shot" framing overstates what the method actually requires. However, the underlying contributions (spatial-temporal factorization, canonicalization, strong empirical results, cross-city generalization) are genuine and well-supported. The paper advances trajectory generation methodology and provides a useful new tool for the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>