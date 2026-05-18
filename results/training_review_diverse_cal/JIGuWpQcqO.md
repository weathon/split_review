Now I have all the evidence needed to verify each claim. Let me produce the final review.

## Summary

This paper proposes RDNet, a single-image reflection removal architecture built on two main innovations: (1) a Multi-Column Reversible Encoder (MCRE) that uses reversible connections across and within columns to prevent information loss during feature propagation, and (2) a Transmission-rate-Aware Prompt Generator (TAPG) that estimates per-channel transmission-rate parameters (α, β) from the input image and uses an MLP to produce feature-modulating prompts. RDNet achieves state-of-the-art quantitative results across all five benchmark datasets (Real20, Objects, Postcard, Wild, Nature) under both standard training-data settings, with PSNR gains of 0.55–0.90 dB over the previous best method (DSRNet). The ablation study demonstrates that removing the reversible connections (swapping for U-Net skip connections) causes a large 2.6 dB drop, and removing the prompt generator causes a 1.13 dB drop, confirming both design choices.

## Strengths

1. **State-of-the-art quantitative results across all five benchmarks.** RDNet achieves the highest PSNR on Real20 (24.43/25.58), Objects (25.76/26.78), Postcard (25.95/26.33), Wild (27.20/27.70), and Nature (26.21) under both training settings (Table 1–2). The average PSNR exceeds DSRNet by 0.55 dB (w/o Nat.) and 0.90 dB (w/ Nat.), which is a clear and well-documented empirical improvement.

2. **Novel architectural design supported by strong ablation evidence.** The key design choice — replacing conventional interaction mechanisms (linear layers, gating) with reversible connections — is validated by Setting F in the ablation: replacing reversible connections with U-Net connections causes a 2.6 dB drop in average PSNR (Table 2). The prompt generator is similarly validated (Setting A: −1.13 dB). These ablations directly support the paper's core claims.

3. **The TAPG is a thoughtful addition for real-world generalization.** The paper explicitly identifies that standard SIRR models fail to account for varying transmission rates across color channels in real captures. Training a ConvNeXt-based estimator to predict per-channel α, β and using these to modulate features via learned prompts is a sensible design that demonstrably improves results (Settings A→B→Ours progression in Table 2).

4. **Qualitative results on challenging in-the-wild captures confirm practical robustness.** Figure 5 shows RDNet removing dense, large-area reflections that all seven competing methods fail to handle, including on images captured by the authors themselves. This provides visual evidence beyond benchmark numbers.

5. **First reversible architecture specifically for reflection removal.** While the application of reversible designs to low-level vision is not entirely new, the paper correctly identifies that existing reversible methods focus on texture generation tasks (super-resolution, enhancement) whereas reflection removal requires decoupling rather than generation, making the adaptation non-trivial.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The "information lossless" claim is stated more strongly than the evidence supports.** The paper claims the intra-level connection (Eq. 3–4) is "information lossless" because one can retrieve F_j^{i-1} from F_j^i via the inverse operation. This local invertibility is mathematically correct given the other terms (F_{j-1}^i, F_{j+1}^{i-1}) are available. However, the paper also states that "the subsequent multi-column reversible design ensures the lossless propagation of hierarchical information throughout the decomposition network" — a broader claim that is never formally demonstrated (e.g., no end-to-end inversion algorithm is provided, nor a proof of bijectivity for the full encoder). The strong ablation result (2.6 dB drop) empirically supports information preservation, but the framing in prose exceeds the formal rigor provided. The paper would benefit from toning down the absolute language or adding a more precise characterization (e.g., "approximately lossless" or "information-preserving in practice").

2. **The 24.34 dB comparison of the prompt generator against Dong et al. is presented without sufficient context.** The paper reports that using the six predicted parameters as a standalone linear correction (T_est ≈ (I−β)/α) achieves 24.34 dB average PSNR, "surpassing the previous state-of-the-art method by Dong et al." (24.21 dB). While the metric comparison is technically valid, a simple per-channel affine correction of the input and a full neural reflection-removal pipeline are qualitatively different approaches. The framing risks misleading a reader into thinking the prompt generator alone is a competitive reflection removal method, when in reality this result merely confirms the estimated parameters encode meaningful information. This section should clearly separate the prompt generator's role as an internal conditioning mechanism from this sanity check, and either remove the direct comparison or add explicit caveats.

3. **No computational cost comparison (FLOPs, parameters, runtime) is provided.** Given that the MCRE involves multiple columns and reversible connections that typically demand more memory/parameters, reporting efficiency metrics would help readers assess practical deployability. The paper states the dual-stream variant involves "double computation" (Setting D ablation) without any quantitative evidence.

4. **The ablation table layout is unnecessarily confusing.** Table 2 combines two separate ablations (prompt generator vs. network structure) into one table with two halves, both containing a repeated "Ours" row showing identical numbers (26.65). While the information is present and interpretable, a reader must cross-reference column headers carefully to understand which row belongs to which ablation. Presenting these as two separate tables would be clearer. The "double computation" claim for Setting D should also be backed by actual parameter/FLOP counts.

### Trivial

- No failure case analysis or limitations section is provided. Adding a brief discussion of where RDNet still struggles (e.g., heavy ghosting, low contrast) would strengthen the paper's practical contribution.
- The paper does not mention whether results are averaged over multiple runs. While single-run evaluation is common in this field, stating this explicitly would improve transparency.

## Nice-to-Haves

- A step-by-step algorithm or diagram showing the computation order across columns and levels for both forward and reverse passes would help readers assess the reversibility claim without ambiguity.
- Reporting per-benchmark results for the ablation variants (Table 2 currently shows only averages) would increase informativeness.
- Analyzing cases where the TAPG's parameter estimates are inaccurate and how the full model compensates would provide insight into the method's robustness.

## Removed Points

These points from the reviewers are either factually incorrect, misread the paper, or violate the review guidelines. They are listed here for traceability but do not affect the assessment:

- **"Reversible connection not invertible as implemented" (Harsh Critic, Critical Issue 1, fatal framing):** The local connection described in Eq. 3–4 IS invertible: given F_j^i, F_{j-1}^i, and F_{j+1}^{i-1}, one can recover F_j^{i-1} via Eq. 4. The reviewer's claim that "it is not obvious [these terms] are available or can be recomputed" overlooks that they are computed earlier in the forward pass and available during reversal. The criticism globalizes a local concern into a structural flaw, which it is not. (The broader "lossless propagation" framing is kept as a Minor weakness about precision of language, above.)
- **"PHE description is vague" (Harsh Critic, Other Observations):** The paper states "the PHE captures semantically rich hierarchical representations from the input image and transmits them to each level of the first column in MCRE" and that PHE is initialized by a pretrained FocalNet. This description is adequate for the paper's scope.
- **"Training schedule too brief" (Harsh Critic, Other Observations):** 20 epochs, Adam, LR=1e-4, batch size 2 is standard reporting for this field. No special convergence analysis is expected.
- **"Qualitative figures confusing" (Harsh Critic, Missing Parts):** This is a parser-formatting artifact; the original submission does not have these issues.
- **Strength Finder strength #6 ("Clear theoretical grounding"):** While present, this is generic framing common to most papers.

## Novel Insights

The most interesting observation from the collective reviews is that the paper presents an unusual inversion of the typical reversible-network paradigm: instead of using reversibility to reduce memory during backpropagation (the original RevNet motivation), RDNet uses it as a *feature-preservation mechanism* for multi-scale decoupling. This reframing of reversible designs — from a training-efficiency tool to a representation-quality guarantee — could be a useful design principle for other multi-branch or multi-column architectures in image decomposition tasks. The strong ablation result (2.6 dB loss when replaced with U-Net skip connections) lends credibility to this application of reversibility, even if the formal invertibility of the full encoder is not proven.

## Suggestions

1. Soften the "information lossless" language throughout the paper. Replace with "information-preserving" or add a qualifier like "approximately lossless" to match what is actually demonstrated (local connection invertibility + strong empirical evidence from ablation). This would preempt the most serious criticism without weakening the contribution.

2. Restructure the 24.34 dB result: either present it as a sanity check for the prompt generator's parameter estimates (not as a comparison to Dong et al.), or add an explicit caveat that this is a simple linear correction and not a reflection-removal method.

3. Split Table 2 into two separate tables (one for prompt generator ablation, one for network structure ablation), each with a clear baseline row. Add FLOPs or parameter counts to substantiate the "double computation" claim.

4. Add a brief limitations paragraph and a failure-case example to improve completeness.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>