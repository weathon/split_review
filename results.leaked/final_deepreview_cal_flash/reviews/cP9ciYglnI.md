Now I have a thorough understanding of the paper and the reviewer inputs. Let me write the final consolidated review.

## Summary

This paper proposes a shape-adaptive guidance signal (Weighted Geodesic Distance Transform, WGDT) for interactive cortical sulcal labeling on the sphere. The core idea is to encode user clicks by solving the eikonal equation with a mean-curvature-dependent speed function, so the signal propagates faster along sulcal folds and slower in gyral regions. The method is evaluated on 72 HCP subjects with 17 manually defined LPFC sulci and compared against two equidistance-based click encodings (ADT, Disk) and three fully automatic baselines. The primary claim — that WGDT outperforms equidistance-based encodings — is convincingly supported by the experiments.

## Strengths

- **Shape-adaptive guidance signal is a genuine methodological contribution.** Using the eikonal equation with a curvature-modulated speed function (Eq. 4) to encode user intent along cortical folding patterns is novel and principled. Unlike generic geodesic disks or angular distance transforms, the WGDT signal adapts to local morphology, propagating faster in sulcal valleys and slower across gyral ridges. This is concretely demonstrated in Figure 3, which shows the WGDT signal remaining localized along folds while ADT/Disk spill into adjacent regions.

- **WGDT significantly and consistently outperforms ADT and Disk on all nine small, variable sulci** (adjusted p < 0.05, FDR-corrected), as shown in Figure 4 (Section 4.1). This is the paper's strongest evidence: the shape-adaptive encoding delivers a clear and statistically rigorous improvement where it matters most — on the challenging sulci that automatic methods struggle with. On large/consistent sulci performance is comparable, which is expected since those are easier regardless of encoding scheme.

- **Real-time interaction latency (<0.5 s per click, Table 2)** with a detailed breakdown across WGDT encoding, re-tessellation, and forward pass. This makes the framework practically usable in interactive settings.

- **Rigorous evaluation design** including 5-fold cross-validation, paired t-tests with FDR correction across 17 sulci, and iterative click simulation with spatial variability (Section 2.2). The masking strategy (curv ≥ 0) to restrict guidance to sulcal regions is a sensible design choice.

- **Iterative refinement works well:** after 2–3 clicks, near-perfect accuracy is achieved on small variable sulci (Figure 5), demonstrating that the framework supports practical interactive workflows where users correct errors progressively.

## Weaknesses

### Major

- **The comparison with automatic baselines is confounded by per-sulcus vs. multi-class training.** The interactive models are trained as per-sulcus binary classifiers (Section 2.1), while the automatic baselines (Lyu et al., 2021; Lee et al., 2025a,b) are retrained as multi-class models labeling all 17 sulci simultaneously (Section 4.2). This asymmetry gives the interactive method an inherent advantage — each binary model focuses on one morphologically homogeneous structure, whereas the baselines must handle inter-class relationships. The headline claim that "even a single click … outperforms fully automatic methods" cannot be cleanly attributed to the user click alone, because it conflates the effect of interactivity with the effect of per-sulcus specialization. The paper acknowledges the per-sulcus design choice (Section 2.1) but does not provide an ablation to separate the two factors. Adding a per-sulcus automatic version of the same backbone without any guidance signal would directly quantify the improvement attributable to the guidance signal. Without this, the automatic baseline comparison is suggestive but not conclusive.

  *Impact:* This weakness affects one of the paper's advertised claims but **does not** undermine the core contribution (WGDT > ADT/Disk), which is independently supported by controlled comparisons that keep the backbone, training protocol, and per-sulcus design fixed.

### Minor

- **The curvature source for the WGDT speed function is not explicitly specified.** Section 2.3.3 defines the speed as \(F = e^{kH}\) with \(H\) as "mean curvature derived from the cortical surface" but does not state whether \(H\) is the white-matter mean curvature (`curv`), the inflated-surface mean curvature (`inflated.H`), or another quantity. Section 3.3 uses `curv ≥ 0` for masking with the same sign convention (sulci non-negative), which strongly suggests \(H = \text{curv}\), but this should be stated explicitly. The sign convention assumed (sulci \(H \geq 0\), gyri \(H < 0\)) may differ from standard FreeSurfer conventions depending on implementation; a brief clarification would aid reproducibility.

- **Hyperparameter \(k\) (speed modulation strength) is tuned by exhaustive search over \(\{6,8,10\}\) and no principled selection rule is provided.** The paper acknowledges this limitation (Section 4.1, "selecting appropriate \(k\) and \(\sigma\) values…we leave for future work"). While this is a reasonable admission for an empirical paper, it limits practical adoption — especially since curvature magnitudes can vary across subjects and brain regions. A simple data-driven heuristic (e.g., based on the percentile distribution of \(H\)) would strengthen the method's deployability.

- **Bar charts (Figures 4, 5) do not show variance** (SD, confidence intervals, or error bars). While paired t-tests with FDR correction provide significance testing, visualizing variability would help readers assess effect sizes. The authors report means across 10 runs per subject, which could be shown as error bars.

### Trivial

- No significant trivial issues detected; the paper is well-organized and clearly written.

## Nice-to-Haves

- **Click-location sensitivity analysis:** The current simulation places initial clicks near the center of the largest connected component of the manual label with modest spatial variability. Testing deliberate off-center clicks or boundary clicks would better characterize robustness in realistic use.
- **Spherical distortion discussion:** A brief remark on how the cortical-to-spherical mapping distorts geodesics and whether this affects WGDT alignment with actual sulcal anatomy would be helpful (raised in Section 2.3.3).
- **Per-sulcus automatic ablation** (as noted in Major weaknesses): Training the same backbone without guidance signals would directly quantify the incremental value of the WGDT signal.

## Removed Points

- *Click simulation is optimistic (critic's Section 2.2 note):* The critic argues that drawing the first click from the manual label's largest connected component is optimistic. This is standard practice in interactive segmentation evaluation and is appropriately acknowledged; the paper notes this is "typical for evaluation" and mentions real-world first-click strategies as future work. This is not a weakness.
- *Spherical mapping distortion not discussed (critic's Section 2.3.3 note):* The cortical-to-spherical mapping via FreeSurfer is a well-established pipeline; its properties are documented in prior work cited in the paper. A detailed discussion is not required here.
- *Curv sign convention question (critic's sign reversal claim):* The paper states a clear convention (sulci H≥0, gyri H<0) and uses it consistently. Whether this matches FreeSurfer's default output is a specification detail, not an error. The critic's suggestion that the sign "may be reversed locally" is speculative.
- *Several formatting/style nitpicks from the critic* (e.g., bar charts layout, masking note in Section 3.3) are either standard practices or parser artifacts.

## Novel Insights

The reviews surface one genuinely trenchant observation beyond the paper's own contribution: the per-sulcus vs. multi-class confound is real and worth addressing, but it does not affect the strongest part of the paper (WGDT vs. equidistance signals). The harsh critic correctly identified this asymmetry, and the suggestion of a per-sulcus automatic ablation is the cleanest fix. Separately, the curvature specification gap is a genuine reproducibility issue that would take one sentence to close. Neither of these undermines the paper's core technical contribution.

## Suggestions

1. Explicitly state which curvature map (`curv`, `inflated.H`, or other) is used as \(H\) in the WGDT speed function (Eq. 4), and clarify the sign convention relative to FreeSurfer's output.
2. Add a controlled ablation: train the SPHARM-Net backbone as a per-sulcus automatic model (no guidance signal) to separate the effect of user clicks from the effect of per-sulcus specialization. This would substantiate the claim that a single click beats automatic methods.
3. Add error bars (SD or 95% CI) to the bar charts in Figures 4 and 5, or include a variance table in the appendix.
4. Provide a simple heuristic for selecting \(k\) based on the curvature distribution in the training set, reducing manual tuning.

## Score and Decision

I will now perform calibration. My round-1 bracketing placed the paper in (4.5, 7.0). Round-2 narrowing with topical anchors (interactive 3D segmentation, cortical surface analysis) placed the paper above the reject-level anchor at 5.33 (incremental work, limited evaluation) and the borderline-accept at 5.50 (AGILE3D — mixed novelty and evaluation concerns), and comparable to or slightly below the solid accept at 6.25 (neuron segmentation with novel approach). The paper's strongest evidence (WGDT > ADT/Disk with FDR-corrected significance) is clean and reproducible. Its main weakness is the confounded automatic baseline comparison, which is real but does not affect the core contribution. Relative to the round-2 anchors:

- **AGILE3D (5.50)**: The current paper has a more novel methodological contribution (curvature-aware geodesic signal vs. attention-based click encoding) and cleaner statistical evaluation. Slightly stronger.
- **Neuron seg w/ AGQ (6.25)**: Comparable novelty and evaluation quality, but the current paper's automatic baseline comparison is less clean. Slightly weaker.
- **Connectome SMN (6.25)**: The current paper has clearer contribution and more rigorous evaluation. Comparable or slightly stronger.

The paper is clearly above rejection threshold (3–4 range) and sits comfortably in the accept band. I assign **6.0**.

All anchors retrieved:

| Anchor ID | Avg Score | Round | Comparison |
|---|:-:|---|---|
| Gvg3nXZvyg | 3.00 | 1 | Benchmark paper, rejected; weaker than current paper |
| NtMf8DejbV | 3.00 | 1 | Language-based med seg, rejected; weaker |
| oY2jw2NLiM | 3.00 | 1 | Coreset clustering, unrelated; not compared |
| EQAHilKZ8D | 2.20 | 1 | Visual property representations, rejected; weaker |
| Rriucj4UmC | 3.67 | 1 | Cortical surface reconstruction from infant MRI, rejected; method less clear, weaker evaluation |
| NhLBhx5BVY | 5.33 | 1,2 | Topological loss for neuron seg, rejected; limited novelty, no ablation — current paper stronger |
| Y0QqruhqIa | 6.25 | 1,2 | Neuron seg with AGQ, accepted; comparable novelty but cleaner evaluation in current paper |
| OJsMGsO6yn | 6.50 | 1 | Surface-based fMRI decoding, accepted; different task, not directly compared |
| 9cQtXpRshE | 5.50 | 2 | AGILE3D interactive 3D seg, accepted; current paper has more novel guidance signal |
| PZYr22zFyE | 6.25 | 2 | Connectome shape-memory network, accepted; current paper has clearer methodology |
| 6O3Q6AFUTu | 8.00 | 1 | Diffusion interpolation; much stronger paper, not comparable |
| 3b9SKkRAKw | 8.00 | 1 | Lesion-focused diffusion; much stronger paper, not comparable |
| 8enWnd6Gp3 | 7.60 | 1 | Tetrahedral mesh representation; much stronger paper, not comparable |
| 5Ca9sSzuDp | 8.00 | 1 | CLIP decomposition; much stronger paper, not comparable |
| 8G3FyfHIko | 6.40 | 2 | GDrag interactive editing; different task |
| Pj2qEVzufH | 6.00 | 2 | 3D Gaussians structure-aware; different task |
| 7JUrBLDjCq | 6.50 | 2 | 3DGS-Drag; different task |
| Pm1NXHgzyf | 6.00 | 2 | SegLLM interactive reasoning seg; different task |

Round-1 bracket: (4.5, 7.0). After Round-2 narrowing, final score = 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>