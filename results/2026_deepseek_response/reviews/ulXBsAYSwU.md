## Summary

MolMiner is a fragment-based, geometry-aware, order-agnostic autoregressive model for molecular generation. It supports conditional generation over twelve molecular properties via a GMM-based partial conditioning scheme, incorporates dynamic 3D geometry through forcefield relaxation and spatial attention biases, and uses symmetry-aware fragment attachments. The paper also proposes Wasserstein distance for unconditional evaluation and calibration plots for conditional evaluation.

## Strengths

1. **Multi-property conditional generation at an unprecedented scale**: MolMiner is among the first models to demonstrate simultaneous conditioning on twelve molecular properties. The calibration plots (Figure 2, Section 4.3) show mean predicted values that track the ideal line across the prompted range for most properties (logP, SAS, FractionCSP3, TPSA, HBD, HBA, ring count, rotatable bonds, chiral centers), providing evidence of controllable generation at this scale.

2. **Order-agnostic rollout with demonstrated regularization benefits**: The random sampling of focal attachment points during rollout (Section 3.3) departs from fixed-order strategies in JTNN and HierVAE. Section 4.1 confirms that rollout resampling reduces overfitting, providing quantitative evidence for this design choice.

3. **Systematic symmetry-aware fragment attachment**: Section 3.2 introduces a novel procedure using Morgan fingerprints and Tanimoto similarity to identify valid cyclic permutations of fragment atoms after canonicalization, ensuring that generation decisions are invariant to fragment symmetries — a detail the paper correctly notes is absent from prior fragment-based work such as MoLeR.

4. **Dynamic 3D geometry incorporation**: The model updates geometry via forcefield relaxation after each attachment step and encodes spatial information into attention via a Gaussian-decayed distance kernel (Equation 2). Section 4.1 confirms that geometry-aware attention improves performance with positive bias initialization.

5. **GMM-based partial conditioning**: Section 3.6 describes a GMM fitted to training data that allows users to specify any subset of target properties while automatically sampling the remaining ones, making the conditioning interface flexible and practical for real-world use.

## Weaknesses

### Fatal
None.

### Major

1. **No conditional generation baselines.** The paper's central claimed contribution is multi-property conditional molecular generation, yet the conditional evaluation (Section 4.3) consists solely of calibration plots for MolMiner itself. No comparison is made to any existing conditional generation method — not a property-conditioned VAE, a conditional diffusion model (e.g., EDM), or even a simple baseline such as nearest-neighbor retrieval conditioned on the prompt. The unconditional comparison to HierVAE (Section 4.2) does not fill this gap, as HierVAE is an unconditional model. Without a conditional baseline, the reader cannot assess whether MolMiner's approach is actually effective relative to existing alternatives for its headline capability. This evidential gap directly undermines the paper's primary claim of advancing controllable multi-property generation.

2. **Unconditional Wasserstein distances show substantial degradation on key molecular properties.** In Table 1, MolMinerD's Wasserstein distances are 3–4× larger than HierVAE's for molecular weight (47 vs. 15), TPSA (7.6 vs. 2.3), and molar refractivity (11.9 vs. 3.8). The paper characterizes these as "modest differences" and "slightly below" HierVAE, but a 3× gap in Wasserstein distance is not modest by any standard. While a plausible explanation (early termination bias) is discussed in Section 5, this hypothesis is not validated with any analysis (e.g., distribution of generated molecule sizes, ablation with reweighted termination actions). The gap raises legitimate concerns about whether the fragment vocabulary, order-agnostic rollout, or termination bias fundamentally limits the model's ability to cover the training distribution, which could also affect conditional generation quality.

### Minor

1. **Single-property-at-a-time conditioning evaluation does not fully validate multi-property control.** The conditional evaluation (Section 4.3) sets one property to a target value while sampling the other eleven from the GMM. This tests individual property responsiveness but does not evaluate the realistic use case of simultaneously specifying multiple target properties (e.g., target logP AND target molecular weight). The paper's claim of "multi-property control" is partially supported but lacks evidence for joint multi-property conditioning.

2. **No quantitative calibration metrics.** The conditional evaluation relies on visual calibration plots (continuous properties) and confusion matrices (discrete properties). No quantitative metrics such as Expected Calibration Error (ECE), mean absolute error between prompted and predicted values, or calibration slope are reported. This makes "calibrated" a qualitative assertion and makes it difficult to compare against future work or to assess borderline cases like QED, where the visual deviation is concerning.

3. **Unconditional comparison is thin.** The unconditional evaluation compares against only one baseline (HierVAE). MoLeR was excluded based on limited training (7 days on one GPU) which is transparently acknowledged, but this still leaves the unconditional results with limited context. While the exclusion of MARS is well-justified (oracle access to properties during generation), the overall unconditional evidence base is narrow.

### Trivial
None.

## Nice-to-Haves

- Ablation explicitly comparing dynamic forcefield-relaxed geometry vs. fixed 2D conformation or geometry frozen at training time, to quantify the benefit of dynamic geometry.
- Analysis of the termination bias hypothesis (e.g., histogram of generated molecule sizes vs. dataset sizes) as suggested in Section 5.
- Evaluation of multi-property conditioning where 2–3 properties are simultaneously set to specific targets, with joint calibration assessment.
- Reporting quantitative calibration metrics (ECE, MAE) alongside the visual plots.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **SSSR non-uniqueness** (Harsh Critic Section 3): RDKit's SSSR is deterministic for the molecular graphs in this dataset; the paper canonicalizes fragments via SMILES, ensuring reproducibility. Not a genuine problem.
- **Forcefield ablation missing** (Harsh Critic Section 3): The paper reports in Section 4.1 that geometry-aware attention aids performance, with the details likely in the removed appendix. The criticism is weakened by the paper's existing ablation report.
- **MoLeR 7-day training** (Harsh Critic Section 4.2): The paper is transparent about the limited training and includes results in the appendix. This is disclosure, not a flaw.
- **70 GB RAM** (Harsh Critic Section 7): Large RAM usage from dataset prefetching or CPU-side storage is normal. Not a substantive weakness.
- **QED calibration is concerning** (Harsh Critic repeated): The paper explicitly acknowledges QED as an "exception" (Section 4.3) and discusses it in Limitations (Section 5). The criticism is redundant with the paper's own admission.
- **Missing related work references**: Per instructions, I cannot flag missing related works as I lack external sources to confirm their existence.
- **Formatting/style nitpicks and grammar issues**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The key insight from the review process is that the paper's methodological components (order-agnostic rollouts, symmetry-aware attachment, dynamic geometry, 12-property conditioning) are individually well-motivated and clearly described, but the evaluation infrastructure — particularly the complete absence of conditional baselines — prevents assessing whether this combination yields a net benefit over simpler approaches. The unconditional gaps suggest possible latent issues that are not investigated empirically.

## Suggestions

1. **Add at least one conditional baseline.** Even a simple baseline (e.g., a property-conditioned HierVAE with a property encoder, or a conditional diffusion model like EDM with the same 12 properties) would transform the evaluation from a model description into a demonstrated advantage.
2. **Validate the termination bias hypothesis** with empirical analysis (size distribution histograms) or a corrected variant (reweighted termination actions) to determine whether the unconditional gap is fixable or structural.
3. **Evaluate joint multi-property conditioning** by setting 2–3 specific properties simultaneously and measuring calibration for each.
4. **Report quantitative calibration metrics** (ECE or MAE) alongside the visual plots for all 12 properties.
5. **Correct the characterization of unconditional results** — the paper describes 3–4× Wasserstein gaps as "modest differences," which is inconsistent with the magnitude of the data.

---

## Score and Decision

**Round 1 (Bracketing):**
- Weak band (<3.5): G2T-LLM (3.00), Ligand Conf Generation (3.00), Broadening Discovery (3.00), 3D Mol Pretraining (3.00). MolMiner is clearly stronger than these.
- Middle band (3.5–7.5): GEAM (6.33, reject), TFG-Flow (6.25, accept), Multi-Modal Foundation Models (3.75, reject), FADiff (4.33, reject).
- Strong band (>7.5): GeoBFN (8.00), Discrete WJS (8.00), ProtComposer (8.00). MolMiner is clearly not at this level.
- **Initial bracket**: 4.0–6.5

**Round 2 (Narrowing within bracket):**
- Lower middle: Forked Diffusion (4.00), FADiff (4.33), Plug-and-Play (3.75), LOGRL (3.67)
- Upper middle: GEAM (6.33), Frag2Seq (5.75), TFG-Flow (6.25), CoarsenConf (6.00)

**Comparison to anchors read in full:**
- vs Forked Diffusion (4.00, reject): Both lack sufficient baselines for conditional claims, but MolMiner has better methodological novelty and clearer formulation. Slightly stronger → above 4.0.
- vs FADiff (4.33, reject): Comparable evaluation quality issues; MolMiner has somewhat better novelty. → slightly above 4.33.
- vs Frag2Seq (5.75, accept): Frag2Seq has comprehensive SBDD baselines and thorough experiments; MolMiner has more methodological novelty but much weaker evaluation. → clearly below 5.75.
- vs GEAM (6.33, reject): GEAM was rejected on novelty grounds despite strong experiments with multiple baselines. MolMiner has better novelty but substantially weaker experiments. → below 6.33.

**Narrowed bracket**: 4.0–5.5. The paper is closer to the lower end because the missing conditional baseline is a severe evidential gap for the main claim. However, the methodological contributions and clarity raise it above the 4.00-level papers.

**Final calibrated score**: 4.5

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>