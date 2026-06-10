## Summary

This paper proposes four methodological components — Uncertainty-Receptive Fusion (URF) for sequential boosting with uncertainty-weighted loss, an image acquisition model with Monte Carlo simulation, Entropy-based Uncertainty Assessment (EUA), Gnostic Uncertainty Estimation (GUE), and a Volume Variation Coefficient (VVC) — all aimed at improving predictive reliability in medical image analysis. However, the paper contains **no experimental results whatsoever**. It references Tables 4/5 and Figures 5/6 that do not appear in the document, never describes an experimental setup (dataset splits, architectures, training protocols), and makes strong performance claims (e.g., "EUA regularly produced segmentation accuracy that was greater than both the baseline of a single prediction") without a single number to support them. The paper as submitted is an extended methodology proposal, not a complete research paper, and cannot be evaluated on its merits.

---

## Strengths

1. **URF's modality-specific uncertainty-weighted boosting is architecturally distinct.** The core idea — using predicted uncertainty estimates (σ) rather than loss values to re-weight the loss function during sequential training of base learners, where each base learner is linked to a specific input modality (Section 2.1) — is a potentially novel architectural concept that goes beyond conventional boosting (e.g., Chen & Guestrin, 2016) by exploiting uncertainty signals and modality-specific features simultaneously.

2. **Formal mathematical framework for test-time augmentation.** Section 2.2 provides a principled probabilistic treatment of the image acquisition process (Equations 3–11), explicitly modeling transformations and noise as latent variables and deriving the posterior predictive distribution via Monte Carlo simulation. This is a more rigorous formalization than the ad-hoc test-time augmentation typically used in practice.

---

## Weaknesses

### Fatal

1. **Complete absence of experimental validation — the paper's core claims are entirely unsupported.** The paper has no Experiments/Results section. Section 2.4 ("Summary"), placed within Methodology, references "Table 4," "Table 5," "Figures 5, 6" that do not exist in the document. It makes specific quantitative claims — "the average Dice score of EUA+TTD marginally surpassed that of EUA," "EUA regularly produced segmentation accuracy that was greater than both the baseline of a single prediction," "Monte Carlo sample size N that achieves a plateau in segmentation accuracy often falls within the range of 20 to 60" — but provides zero numbers, no experimental setup (what dataset? what architecture? what training protocol?), no baselines, no error bars. The abstract claims URF "successfully modifies the weighting of the loss function" and produces "predictions with greater accuracy" — these are assertions without evidence. A research paper that proposes multiple novel methods and provides no empirical validation cannot be accepted, because the central claim (that the methods improve predictive reliability) is entirely unsubstantiated. This is not fixable by adding experiments in a rebuttal; it is a structural omission in the submitted work.

### Major

2. **Unresolved task mismatch between classification and segmentation.** The Introduction frames the paper around fracture classification on the MURA dataset (a classification benchmark of 40,561 X-ray images — Section 2.3). Section 2.1 describes URF for multi-modal regression problems. Sections 2.2–2.4 then discuss pixel-level segmentation (Dice scores, pixel-wise entropy, "structures/lesions"). The paper never resolves which task it actually evaluates, how MURA (single-modality X-ray images) relates to the multi-modal regression framing of URF, or what segmentation dataset/architecture/protocol was used. The Conclusion claims "our research, which included both 2D medical image segmentation tasks, demonstrated the value of our EUA strategy" — but no segmentation experiment is described anywhere in the paper.

3. **Critical inconsistency between Equation 2 and its textual description.** The paper states that URF_w uses the "inverses of the corresponding anticipated uncertainty estimations" as weights for the final prediction (line 45: "The inverses of the corresponding anticipated uncertainty estimations, or σ_{hj} are used to calculate these weights"; line 51: "The independent uncertainty metric's inverse is calculated to create the uncertainty weights"). However, Equation 2 uses σ_{hj} **directly** in the numerator (not 1/σ_{hj}), and Equation 3 defines σ_{hj} as a standard-deviation-like quantity (σ_{hj} = √(α+β+γ)) where larger values correspond to **higher** uncertainty. If σ_{hj} is the uncertainty estimate, then Equation 2 assigns **more** weight to more uncertain predictions — the opposite of the stated intent. If σ_{hj} is meant to be the inverse, then Equation 3 contradicts this. Either the equation or the description is wrong, and the method as described cannot function as intended.

4. **Section 2.4 is structurally incoherent.** It is placed inside the Methodology section but reads as a results discussion — referencing non-existent tables/figures, discussing findings without any experimental context, and introducing undefined terms ("W-Net" appears once at line 199 with no definition). This section does not belong in Methodology and does not constitute a valid Results section because it contains zero quantitative data.

5. **Undefined or unexplained terminology undermines reproducibility.** The term "Fluky Model" appears in the Section 2.2.1 heading but is never defined or explained. "W-Net" is mentioned once without definition. "LLFU" (attributed to Lakara et al., 2021) is used to derive Equation 3 but its meaning and provenance are never clarified. The uncertainty estimation formula in Equation 3 (α+β+γ combination) appears ad-hoc and is not connected to any standard uncertainty quantification framework.

6. **Novelty claims are overstated relative to prior art.** The Monte Carlo simulation over transformation and noise parameters (Section 2.2) is structurally identical to test-time augmentation (Wang et al., 2019, which the paper cites). The entropy-based uncertainty (EUA, Section 2.2.2) is standard (Kendall et al., 2017). The GUE method using MC dropout (Section 2.2.3) is standard (Gal & Ghahramani, 2016). The VVC (σ_V/μ_V, Equation 16) is a simple coefficient of variation. The paper presents these as novel contributions without clearly delineating what is new versus what is a restatement of existing techniques.

### Minor

7. **No positioning against key baselines.** Several well-known uncertainty estimation methods are cited in passing (MC dropout, test-time augmentation, ensemble methods) but the paper never explains how URF, EUA, or GUE improve upon them in a specific, testable way. Without experiments, this gap cannot be resolved, but even conceptually the paper does not articulate a precise technical gap that its methods uniquely fill.

### Trivial

None beyond the structural issues above.

---

## Nice-to-Haves

- If the authors intend to evaluate on a segmentation task, that task and its dataset need to be clearly specified. If they intend to evaluate on MURA (classification), the segmentation framing (Dice scores, pixel-level EUA) needs to be reconciled.
- A clear derivation of why Equation 3 is a principled uncertainty estimate (rather than an ad-hoc combination of Gaussian log-likelihood terms) would strengthen the methodology.
- The relationship between URF and standard boosting/ensemble methods (e.g., gradient boosting, AdaBoost, deep ensembles) should be stated more precisely, including a discussion of computational cost.

---

## Removed Points

These points were flagged for removal by the filtering process; they are retained here for completeness but should be treated with caution:

- **Criticism about "LLFU (Lakara et al. 2021) not being standard":** Removed because the paper cites it and per instructions, cited references are assumed to exist. The criticism that the formula is not connected to standard UQ frameworks is retained (Weakness #5) because it is verifiable from the paper's own equations.
- **Criticism about missing reproducibility details (hyperparameters, architecture choices):** Removed per instruction that trivial implementation details are not valid weaknesses. The absence of *any* experimental description is covered by Fatal Weakness #1.
- **Strength about MURA dataset enabling reproducibility:** Removed because the paper never actually uses MURA in an experiment — it only describes the dataset. A dataset description without an experiment using it is not a strength of the paper.
- **Strength about VVC being size-independent:** Removed because this is a trivial coefficient-of-variation normalization; claiming it as a contribution is overreach.
- **Criticism that Equation 8 "does not make sense dimensionally":** While notation is indeed sloppy, this is a presentation-level complaint that is minor relative to the fatal missing-experiments issue; it is subsumed by the broader point about mathematical clarity.
- **Criticism about "no confidence intervals" and "no Dice scores":** These are subsumed by Fatal Weakness #1 rather than being separate points.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not contain. The key finding from the review process — that the paper is structurally incomplete — is not a novel insight about the content but a verdict on the submission.

---

## Suggestions

1. **Add a complete Experiments section** with: (a) a clearly defined task (classification on MURA or segmentation on a standard benchmark), (b) dataset splits and preprocessing, (c) architecture and training details, (d) baselines including single model, standard ensemble averaging, MC dropout, and test-time augmentation, (e) metrics (accuracy/Dice, calibration ECE, selective classification), (f) error bars over multiple runs. Without this, the paper is not ready for submission.

2. **Fix the inconsistency in Equation 2**: if the intent is inverse-uncertainty weighting, the equation should use 1/σ_{hj} or σ should be redefined accordingly. Clearly state whether σ_{hj} represents the uncertainty estimate or its inverse.

3. **Resolve the classification/segmentation mismatch**: commit to one task and dataset, and ensure the methodology (especially URF's multi-modal framing) aligns with the evaluation setup.

4. **Remove or define undefined terms**: explain "Fluky Model," "W-Net," and "LLFU," or remove them if they are remnants from another draft.

5. **Restructure the paper**: move Section 2.4 to a proper Results section with actual tables/figures and quantitative data, or remove it entirely.

---

## Score and Decision

The paper has a single fatal flaw: it proposes multiple novel methods but provides zero experimental validation. No quantitative results, no baseline comparisons, no ablation studies. The methodological content, while containing some interesting ideas, is incomplete without empirical support. For a top-tier venue such as ICLR, a paper must at minimum demonstrate that its proposed methods work. This submission does not meet that bar.

MY FINAL SCORE: <score>1.0</score>
MY FINAL DECISION: <decision>Reject</decision>