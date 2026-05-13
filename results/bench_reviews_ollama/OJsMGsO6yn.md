Now I have a thorough understanding of the paper. Let me synthesize the review.

## Summary

SIM introduces a framework combining surface vision transformers (SiT) with tri-modal CLIP contrastive alignment (fMRI, video, audio) to decode movie stimuli from cortical fMRI of unseen subjects. Using the HCP 7T movie-watching dataset (N=174), the paper demonstrates inter-subject generalization across three progressively harder experimental designs, showing that tri-modal alignment substantially improves decoding over bi-modal approaches.

## Strengths

- **Tri-modal alignment provides consistent, substantial gains over bi-modal**: Table 1 shows fMRI→V top-1 improves from 64.7% (bi-modal) to 76.8% (tri-modal), and fMRI→A improves from 19.9% to 56.6% — a nearly 3× boost. This is a non-obvious result confirming that audio carries complementary information useful even for visual decoding.

- **Well-structured progressive evaluation design**: The three experiments (new subjects, new movie clips, both) systematically ramp up difficulty, directly addressing the right decomposition of the generalization question.

- **Large sample size for brain decoding**: 174 subjects lends genuine statistical credibility to cross-subject claims, and the paper reports 95% confidence intervals throughout.

- **Surface-based SiT architecture is principled and novel for this application**: The icosahedral patching scheme (I₆ → 1280 triangular patches at I₃ resolution) faithfully respects cortical geometry. The vsMAE pre-training adapted to surfaces is a technically sound contribution.

- **Inter-subject generalization without costly per-subject alignment**: Unlike prior work (Scotti et al., 2024; Thual et al., 2023) requiring ≥1 hour of alignment data per new test subject, SIM trains once and generalizes to new subjects directly, which is practically significant.

## Weaknesses

### Fatal
None.

### Major

- **No control for MSMAll functional alignment isolates the contribution of surface modeling**: The paper's central framing is that surface vision transformers encode cortical topology to enable inter-subject generalization. However, all data is preprocessed with MSMAll functional alignment (Section 4.1), which the paper acknowledges "has been shown to considerably improve the overlap of functional activations across brains." MSMAll uses task activation maps and resting-state connectivity to warp individual brains into a shared functional space — it does substantial work to reduce the very inter-subject variability the paper claims to overcome via surface modeling. The paper itself notes this makes ridge regression "an extremely robust baseline" but does not acknowledge the deeper implication: without an anatomical-alignment-only control (e.g., MSMSulc), we cannot determine how much of SiT's success comes from modeling cortical topology versus receiving inputs where the hard alignment problem has already been partially solved by preprocessing. The SiT's 64.7% vs. Ridge's 15.6% gap confirms the method adds value, but the attribution of that value to *surface modeling* specifically is untested.

- **No deep learning volumetric baseline isolates the contribution of surface vs. deep learning**: The paper's core differentiating claim is surface modeling over volumetric approaches, yet the only baseline is ridge regression. The enormous gap (64.7% vs 15.6%) could partly reflect the power of deep learning + contrastive learning regardless of domain, rather than surface modeling per se. A volumetric ViT or CNN adapted to the same contrastive setup on MSMAll-aligned volumetric data would isolate whether SiT's advantage comes from surface representation or from simply being a deep learning model. The paper argues surface models are "much more compact" and "more faithfully represent true geometry" (Section 1), but these claimed advantages are empirically untested against a comparable deep learning model in volumetric space.

### Minor

- **Abstract overclaims generalization to "movies not seen during training"**: The abstract states "even for individuals and movies not seen during training," but in Experiments 2–3 training uses the first half and testing the second half of the *same movies*. What generalizes is new *clips* from movies partially seen during training, not entirely unseen movies. The Discussion acknowledges this limitation ("we were unable to effectively test whether the model would generalise to completely different movies"), but the abstract framing is misleading about the actual scope of the generalization demonstrated.

- **Experiment 1 results dominate the paper while Experiment 3 — the headline claim — receives less precise reporting**: Table 1 provides exact numbers with confidence intervals for Experiment 1, but Experiment 3 (new subjects + new clips, the hardest and most important condition) is reported only in Figure 5 (bar charts with confidence intervals for soft-negative fMRI→V only). Additional results are referenced in appendix tables (C.2, C.3), but the most critical experiment deserves main-text tabular treatment matching Experiment 1's standard.

- **Different candidate set sizes across modalities complicate cross-modality comparisons**: Video retrieval uses M=64 (1.6% chance) while audio uses M=32 (3.1% chance). Top-K accuracy is inherently dependent on candidate set size, so direct comparison of fMRI→V vs. fMRI→A percentages is misleading. The paper discusses them side-by-side without normalizing or adjusting for this asymmetry.

- **Reconstruction evaluation is purely qualitative and based on a single training subject**: Figure 6 shows reconstructed frames but reports no SSIM, pixel correlation, or semantic fidelity metrics. The reconstruction pipeline is trained on one subject and tested on one other subject. Given that "reconstruction" is listed as a contribution in the abstract, the evidence falls below the standard needed to support it as a substantive result — it functions more as a proof of concept than a validated contribution.

### Trivial
None.

## Nice-to-Haves

- An MSMSulc-only (anatomical alignment) experiment would definitively separate the contribution of surface modeling from preprocessing — this would enormously strengthen the paper if SiT still outperforms ridge without MSMAll.
- A volumetric deep learning baseline (e.g., a 3D ViT or CNN with the same contrastive learning pipeline) would isolate whether the advantage comes from surface representation or deep modeling.
- Per-subject variance analysis or failure-case characterization would reveal whether the model struggles with outlier brains or specific clip types.
- Quantitative reconstruction metrics (SSIM, semantic classification accuracy of reconstructed frames) would elevate reconstruction from proof-of-concept to validated contribution.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Training strategy not reported for Table 1"** — The paper references three strategies and appendix Table C.1 for ablations. Per rules, missing appendix content or proofs is a parser artifact, not an author error. Removed as appendix-related critique.

- **"Movie-level information leakage is a fatal flaw"** — The critic treats movie-level continuity as leakage that invalidates cross-clip generalization claims. The paper explicitly acknowledges this limitation in Discussion (line 186), and hard-negative sampling (negatives from same movie) partially mitigates it. The paper demonstrates generalization to new *clips* within known movies, not to entirely unseen movies. While the abstract overstates the scope (addressed in Minor weaknesses above), calling this "leakage" overstates the issue — it's a limitation of scope, not a methodological flaw.

- **Ridge top-1 vs top-10 gap analysis** — The observation that Ridge shows a 48.5pp top-1/top-10 gap is interesting but speculative; it does not constitute a weakness of the paper.

- **Self-attention described as "purely qualitative"** — The paper actually includes correlation analysis against Margulies gradient-based maps (line 170: "correlation analysis against Margulies' gradient-based maps shows that Gradient 2 is the highest correlated"). This is partially quantitative, contrary to the critic's claim.

- **"Temporal buffer doesn't address movie-level leakage"** — See above; this conflates scope limitation with methodological flaw.

- **Strength Finder claims about "data efficiency relative to prior frameworks"** — While the paper collects less data per subject, this is a property of the HCP dataset, not a methodological innovation. Kept as supporting context but not elevated to a core strength.

- **Strength Finder claim about "reconstruction generalizes to new subjects and new movies"** — This is overstated given only qualitative evidence from one training/test subject pair. Moved to Removed Points as conflicting with the verified weakness about reconstruction evaluation quality.

## Novel Insights

The tri-modal alignment result — where adding audio nearly triples fMRI→A accuracy (19.9% → 56.6%) while also substantially boosting fMRI→V (64.7% → 76.8%) — is the paper's most empirically robust and surprising finding. It suggests that in movie-watching paradigms, audio and visual channels carry substantially complementary neural signatures, and jointly modeling them creates a representation space where cross-modal retrieval becomes significantly easier even for directionally unrelated modality pairs. This has practical implications for future brain decoding work: the common practice of treating audio and visual decoding as separate problems may sacrifice significant performance gains.

## Suggestions

- Run and report the same pipeline using MSMSulc (anatomical-only) alignment. Even if absolute performance drops, showing that SiT still outperforms Ridge and still generalizes would dramatically strengthen the surface-modeling attribution claim.
- In the abstract, replace "movies not seen during training" with "movie clips not seen during training" to accurately reflect what Experiments 2–3 demonstrate.
- If reconstruction is retained as a claimed contribution, add at minimum pairwise semantic classification accuracy (can a classifier identify the correct category from the reconstructed frame?) as a quantitative metric.

## Score and Decision

The paper introduces a genuinely novel and well-motivated framework (SiT + tri-modal CLIP) with compelling empirical results, most notably the large tri-modal alignment gains. However, two major structural gaps — the MSMAll preprocessing confound and the absence of any deep learning volumetric baseline — mean the paper cannot attribute its success to surface modeling specifically, which is its central differentiating claim. The SiT clearly works (large improvements over ridge), but whether it works *because* of surface modeling or simply because it is a deep learning model on already-aligned data remains untested. The abstract also overstates the generalization scope. These are addressable in principle through additional experiments (MSMSulc control, volumetric baseline), but as presented, the core attribution claim is not convincingly established.

Originality: High — the combination of surface transformers + tri-modal CLIP alignment for brain decoding is novel.
Importance: Moderate-to-high — inter-subject generalizable brain decoding is an important question.
Claims support: Moderate — results are strong but attribution to surface modeling is untested.
Experimental soundness: Moderate — the progressive experimental design is good, but the critical missing controls weaken interpretability.
Clarity: Good — the paper is well-structured and clearly written.
Community value: Moderate — the framework and tri-modal finding have practical implications.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>