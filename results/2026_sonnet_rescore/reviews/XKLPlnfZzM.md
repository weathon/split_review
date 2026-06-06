Now I have the full paper. Let me carefully cross-check all reviewer claims before writing the consolidated review.Now I have a complete picture. Let me write the final consolidated review.

---

## Summary

The paper introduces the Temporal Deaggregation Diffusion Model (TDDM), a hierarchical diffusion framework for large-scale trajectory generation that factorizes mobility into *where* (spatial priors encoded as regional occupancy heatmaps H) and *how* (temporal dynamics conditioned on H). Regions are canonicalized via a similarity transform, enabling parameter sharing across geographic locations. The paper also contributes a three-city benchmark (Beijing/Geolife, Porto, San Francisco/Cabspotting) with harmonized distributional and fidelity metrics, and demonstrates that TDDM can generate realistic trajectories for entirely unseen cities without any gradient updates on target data.

---

## Strengths

- **Spatial-temporal factorization with concrete empirical support**: The core design choice — conditioning generation on aggregate occupancy maps H rather than per-trajectory attributes — is directly validated by the ablation in Table 2. Removing the spatial prior degrades KL_sym from 0.277 to 1.334 (nearly 5×), while TSTR is unchanged (0.011 → 0.011), confirming that H is the mechanism driving distributional alignment rather than being a proxy for temporal memorization.

- **Genuinely strong OOD generalization results**: Table 3 demonstrates that a model trained on Porto generalizes to other cities with KL_sym = 0.335 and JS = 0.071, outperforming training on 25% of the target city's local data (KL_sym = 0.545, JS = 0.106). Pattern score stays above 0.915 in all city-to-city transfers. The observation that Porto acts as a "universal source" dataset — outperforming partial local coverage on spatial coverage metrics — is a substantive and surprising empirical finding worth emphasizing.

- **Multi-city benchmark with harmonized metrics**: Evaluation spans three cities on different continents using six complementary metrics (TSTR, KL(R‖S), KL(S‖R), Density Error, Trip Error, Pattern Score), providing structured coverage across fidelity, coverage, proportionality, and usefulness axes. This is a direct service to the trajectory generation community.

- **Canonicalization is well-motivated and clean**: The similarity transform (Goodall, 1991) approach to achieving location invariance via input-output transformation rather than group-equivariant architecture is principled, lightweight, and its benefit is confirmed implicitly by the cross-city transfer results — the model, after canonical training on any source city, can be applied to any target city's normalized regions.

---

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric comparison in Table 1 undermines the "outperforms unconditional baselines" narrative.** TDDM at generation time (Algorithm 2, line 3) computes H = f(r_c, X_target), where X_target is the training city's trajectory data. The dominant headline metrics — KL(S‖R), KL(R‖S), KL_sym, JS — measure alignment between the synthetic spatial distribution and the real one. Because H encodes the aggregate spatial marginal of the training data, and training and test data from the same city share nearly identical spatial marginals, TDDM is effectively conditioned to match the quantity it is evaluated on. The unconditional baselines (Diffusion-TS, DiffTraj, etc.) receive no such signal. The ablation confirms the structural implication: TDDM *without* spatial prior achieves KL_sym = 1.334 (Table 2), which is *worse* than Diffusion-TS (1.153) and comparable to DiffTraj (1.232), per Table 1. This means the base TDDM architecture does not advance the state of the art on these metrics; every large-margin gain in Table 1 comes from the spatial prior conditioning, not from architectural improvement. The TSTR score (0.011 vs. 0.013 for DiffTraj), which evaluates downstream temporal prediction rather than spatial marginal alignment, is the more informative and fairer metric, and the improvement there is narrow. The paper should more explicitly frame TDDM as a *conditional* generative model and present Table 1 as demonstrating the benefit of spatial prior conditioning — which is a real and valuable contribution — rather than framing it as an apples-to-apples competition against unconditional models. Ideally, an augmented ablation would equip Diffusion-TS with the same H conditioning and confirm whether TDDM's architecture still provides gains beyond the conditioning strategy alone.

### Minor

- **"Zero-shot" terminology is imprecise.** Algorithm 2 (line 3) explicitly takes X_target — real trajectories from the target region or city — as input to compute H. The paper says the model "never receives individual target trajectories, only their aggregate spatial distribution," which is true, but the summary claim in Section 4.3 ("models are trained only on source regions and generate for target regions using solely the spatial prior H, with no gradient updates on target trajectories") does not clearly state that target trajectory data is still required to compute H. For a region with genuinely zero prior trajectory data, H itself would be unavailable. The contribution is better characterized as *parameter-transfer* (no gradient updates) with *aggregate-statistics conditioning* (H from target data), which is still practically valuable but is not zero-data zero-shot in the standard sense.

- **Property (V) has no corresponding metric in Table 1.** The paper defines five evaluation qualities (§4), including (V) Generalization: "Synthetic samples should not be mere copies of the training data." No nearest-neighbor memorization metric or equivalent appears in Table 1. The TSTR score partially captures this, but the paper should either include a direct memorization/novelty metric or remove property (V) from the stated evaluation framework.

### Trivial

- The sensitivity of the 64×64 grid resolution for H is described as a design decision balancing token cost vs. spatial detail, but no ablation on this specific hyperparameter is provided. This is minor but would strengthen confidence in the choice.

---

## Nice-to-Haves

- The OOD section's most striking finding — that Porto generalizes better to other cities than 25% local data — is briefly noted but underanalyzed. A follow-up inspection of what makes Porto a representative source (trajectory length distribution, road network density, speed profiles) would substantially sharpen the paper's insight about transferability and help practitioners choose source datasets.

- Augmenting H with trajectory length priors or time-of-day priors (already noted in Future Work) is a natural and clearly motivated extension that would directly address the one consistent failure mode: Length error increasing in cross-city transfer (0.06–0.11).

- For the in-distribution Table 1 results, adding variance estimates across runs or across per-city results (some per-city margins are smaller, e.g., KL_sym 0.277 vs. 1×1km's 0.328) would better quantify the reliability of the headline improvements.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Fatal" label for comparison asymmetry.** Retained as Major rather than Fatal. The paper's core contribution IS the spatial prior conditioning strategy. The comparison is intentional: TDDM uses H as part of its generative mixture model (Eq. 5), which is a legitimate design choice. The issue is framing ("unconditional generation" label, not the method itself), not a validity failure. Demoted to Major.

- **Harsh Critic: Missing rotation-range specification for augmentation.** The paper does note that training uses "randomized translation and rotation" but the specific rotation range is not given. Removed as a reproducibility nitpick — hyperparameter details are in the Appendix (referenced in §3).

- **Strength Finder: "Consistent TDDM wins across all metric categories."** Partially dropped as a standalone strength because the KL wins are substantially explained by the conditioning asymmetry. The TSTR win is narrow (0.011 vs. 0.013). The more credible strength is the OOD results, which are not subject to this asymmetry.

- **Harsh Critic: TSTR being "more trustworthy" and "provides only weak support."** Partially retained in spirit — the narrow TSTR margin (0.011 vs. 0.013) indeed suggests the advantage is modest on the fairest metric. But the full KL story is retained as a Major framing concern rather than a complete invalidation.

---

## Novel Insights

The paper's most genuinely novel empirical finding — that a model trained on Porto generalizes better to entirely different cities (KL_sym = 0.335) than one trained on 25% of a target city's local data (KL_sym = 0.545) — suggests that trajectory generative models have a latent "universal source" property: some city datasets, presumably due to road network topology and trajectory diversity, encode dynamics that are broadly transferable. This is not merely a claim about TDDM but a potentially general observation about mobility datasets. The finding that temporal dynamics transfer more readily than trajectory length distributions across cities (which fails in all cross-city transfers) provides an empirical decomposition of what is and is not universal in human mobility — a useful conceptual contribution beyond the method itself.

---

## Suggestions

1. Rename Section 4.1 from "Large-Scale Unconditional Trajectory Generation" to something like "Large-Scale Trajectory Generation with Spatial Priors," and add a brief explicit statement that TDDM is a conditional generative model using training-data-derived H — this is honest, still compelling, and avoids the framing problem.

2. Run Diffusion-TS with the same H conditioning (as a simple patch or prefix) and report results in Table 2's ablation. This isolates whether TDDM's architecture provides any gains beyond the spatial prior signal, and — if it does — constitutes a much stronger architectural contribution claim.

3. Add a memorization metric (e.g., average minimum distance from synthetic to training trajectories) to operationalize Property (V) and complete the stated evaluation framework.

4. Expand the OOD discussion with a characterization of what distinguishes Porto from other datasets (trajectory length distribution, coverage density, road network entropy), making the "universal source" hypothesis actionable for future practitioners.

---

## Evaluation on Key Axes

- **Originality**: Moderate-to-high. Factorizing trajectory generation into spatial marginals and temporal dynamics via canonicalized regional conditioning is a clean and original idea. Canonicalization via Procrustes-style similarity transforms for geographic invariance is a novel application.
- **Importance of research question**: High. Scalable mobility trajectory generation with cross-city generalization has direct downstream value in urban planning, privacy-preserving data sharing, and simulation.
- **Claims well-supported**: Partial. The OOD claims (Table 3) are well-supported and not subject to the asymmetry concern. The in-distribution Table 1 claims are real but the framing overstates what is shown — the contribution is the conditioning strategy, not architectural superiority over baselines.
- **Soundness of experiments**: Good, with one significant caveat (the asymmetric comparison). Ablations are informative and the multi-city benchmark adds credibility.
- **Clarity of writing**: Good overall; the method section is precise and the algorithms are well-specified. Some confusion arises from the "unconditional generation" label given TDDM's conditioned nature.
- **Value to research community**: High. The benchmark infrastructure (three-city, harmonized metrics) and the OOD generalization framework are independently valuable contributions.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>