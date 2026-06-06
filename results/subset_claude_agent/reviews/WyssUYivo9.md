Now I have enough information to write the draft review. Let me submit it.Round 1 bracket: **4 to 6** — the paper is notably weaker than the 7.0 accept (which had wet-lab grounded benchmarks and proper ablations) but stronger than the weak 2.6 anchors. The 5.5 reject (enzyme generation with computational-only validation) is a reasonable comparison point.Now I have enough calibration data to finalize the review. The paper sits between the HADES anchor (4.0, reject) and the enzyme generation paper (5.5, reject). XPro-Design is richer in analysis than HADES but has a more fundamental evaluation integrity problem. Score: **4.0**.

---

## Summary
XPro-Design is an iterative protein engineering framework that wraps pre-trained inverse folding models (ProteinMPNN or HyperMPNN) with a learned position-specific scoring matrix (PSSM) bias. Each round, Integrated Gradients (IG) attributions from a melting-temperature predictor (TemBERTure) are combined with mean-centered ΔTm to update the PSSM, progressively steering sampling toward thermostable sequence regions. Applied to Candida Antarctica Lipase B (CaLB), the method reports substantially elevated predicted melting temperatures, reduced MM/GBSA free energies, and richer non-covalent interaction networks relative to generative model baselines.

---

## Strengths

1. **Modular, no-fine-tuning design**: The framework operates without updating generative model weights, avoiding catastrophic forgetting while retaining the structural priors of the inverse folding model. This architectural choice is clearly motivated and concretely implemented in Eq. 9.

2. **Partial cross-model validation**: The paper evaluates with both TemBERTure (the optimization signal) and DeepSTABp (an independently trained predictor), providing at least some orthogonal evidence. XPro-Design(H) achieves mean 82.7°C on DeepSTABp (Table 1), substantially above HyperMPNN (60.5°C) on this independent metric.

3. **Rich mechanistic analysis**: Figure 5 quantifies six distinct non-covalent interaction types; Table 3 reports packing entropy (via PACKMAN Voronoi decomposition). These analyses give mechanistic context beyond aggregate scores and show a coherent redistribution of interaction types in XPro-Design variants.

4. **Adequate sequence diversity**: XPro-Design(P) achieves 0.734 diversity at 48.2% sequence recovery (Table 1), demonstrating that the optimization does not collapse to near-WT sequences as ADFLIP (0.061 diversity) and MapDiff (0.201 diversity) do.

---

## Weaknesses

### Fatal
None that fully invalidate the work.

### Major

1. **Circular primary evaluation**: TemBERTure attributions directly drive PSSM updates (Eq. 8), and TemBERTure-predicted Tm is the headline evaluation metric (Table 1, Figure 2). This pipeline is functionally a gradient-free optimizer of TemBERTure's scoring function; it is expected — not informative — that outputs rank highly on TemBERTure. Crucially, on the independent DeepSTABp predictor (Table 1), XPro-Design(P) achieves a mean of 76.8°C — **identical to ADFLIP's 76.8°C**, even though ADFLIP produces near-WT sequences with essentially zero diversity (0.061). This tie on the supposedly orthogonal validator undermines the uniqueness of XPro-Design's thermostability improvements for that sampler variant. XPro-Design(H) does outperform on DeepSTABp (82.7°C), but the(P) tie is unreported and unaddressed.

2. **Abstract claims not implemented in the method**: The abstract states the method "captures epistatic interactions and the mutational landscape by training a low-rank matrix." However: (a) Section 2.2 explicitly states the pairwise IG matrix (Eq. 4) "is not directly used to train XPro-Design" — it is a monitoring tool only; (b) the PSSM updated by the method is a full L×20 matrix (described in Section 2.3) with no rank constraint, factorization, or structural regularization that would justify calling it "low-rank"; (c) the claim in Section 2.3 that "context-dependent effects (epistasis) are captured naturally through batch-level averaging" does not constitute modeling epistatic interactions in any operational sense. These are concrete misrepresentations of the method.

3. **ΔΔG values are MM/GBSA total energies, not per-mutation stability changes**: Table 3 reports "ΔΔG" values with a mean of −1,426 kcal/mol and best of −2,962 kcal/mol. In protein biochemistry, ΔΔG conventionally denotes per-mutation stability changes (1–5 kcal/mol range). Section 2.4 acknowledges these MM/GBSA energies "should not be interpreted as absolute folding free energies," yet the abstract claims "38% lower folding free energy" and the conclusion interprets them as thermodynamic stability evidence. Since XPro-Design generates sequences with far more hydrogen bonds, salt bridges, and charged residues (Figure 5), MM/GBSA scoring will systematically favor them due to electrostatic terms, regardless of actual thermostability. Calling these values ΔΔG and using them as thermodynamic validation is misleading.

4. **Degraded structural confidence not acknowledged**: Table 2 shows XPro-Design(H) has lower PTM (0.915 ± 0.015 vs. 0.966 ± 0.004 for ProteinMPNN) and pLDDT (0.85 ± 0.02 vs. 0.94 ± 0.01), and XPro-Design(P) is also below all baselines on both metrics. The paper asserts all designed sequences "fold correctly" without discussing this systematic degradation in structural confidence, which is the opposite of what a method improving structural stability would be expected to show.

### Minor

1. **"Nearly 2x" melting temperature claim is overstated**: WT CaLB is reported as 45–60°C. XPro-Design achieves a mean of ~80°C and max ~90°C. In Celsius, 90/45 = 2× only for the absolute minimum WT baseline; the WT mean is 50–55°C and the method mean is ~80°C (roughly 1.5×). In Kelvin (the physically meaningful scale), 363K/323K ≈ 1.12×. The "nearly 2x" language in the abstract is inaccurate under most reasonable interpretations.

2. **SOR results absent from main paper**: SOR (Superoxide Reductase) is described in Section 2 as a control scaffold benchmarked against baselines, but no quantitative SOR results appear in the main text. If SOR was intended to demonstrate generalizability, omitting its results weakens that claim.

3. **No ablation of key hyperparameters**: The γ exponent in Eq. 7 directly amplifies the optimization signal and shapes convergence. Its sensitivity is not ablated, making robustness claims hard to assess.

### Trivial
- The advantage over ADFLIP and MapDiff is partly attributed to "no sampling temperature parameter," which is correct, but could be more prominently noted as a structural incomparability rather than used only to dismiss these baselines.

---

## Nice-to-Haves
- Experimental validation of even 3–5 CaLB variants (DSF or DSC Tm measurement) would transform this from a prediction study into a protein engineering result.
- An ablation separating: (a) temperature annealing alone, (b) random PSSM updates, and (c) IG-guided PSSM updates, to isolate the specific value of the explainability component.
- Correcting the abstract to say "position-specific scoring matrix (PSSM)" instead of "low-rank matrix," and removing or accurately describing the epistasis claim.
- Reporting SOR results in the main paper.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Circular evaluation is fatal"** (Harsh Critic): Demoted from fatal to major. The partial mitigation via DeepSTABp, MM/GBSA, and structural analyses means the evaluation is compromised but not entirely uninformative.

- **"IG baseline (all-zero embedding) is inappropriate"** (Harsh Critic): Not a verified flaw. The paper acknowledges the baseline choice (Section 2.2), and different IG baseline choices typically yield qualitatively similar attributions in practice. Not enough to constitute a specific verified weakness.

- **Strength: "100% stabilizing ΔΔG variants / near-universal stabilization"** (Strength Finder): Removed as a standalone strength because the ΔΔG values are MM/GBSA total energies systematically biased toward hydrogen-bond-rich sequences, as verified above. The 100% figure is an artifact of the evaluation methodology.

- **Strength: "Preserved fold integrity" (PTM/pLDDT)**  (Strength Finder): Partially removed — Table 2 shows XPro-Design variants have systematically lower PTM and pLDDT than all baselines except each other. The paper's claim that all variants "fold correctly" is not wrong, but framing this as a strength conflicts with the verified weakness.

- **Strength: "Diverse sequence exploration"**: Retained as concrete (diversity 0.734) but moved to weaker tier given the ADFLIP comparison on DeepSTABp is a counterpoint.

---

## Novel Insights
The idea of using per-residue IG attributions from a differentiable Tm predictor to guide iterative PSSM updates — without retraining the generative model — is clean and modular. The observation that XPro-Design converges to sequences with denser H-bond, salt bridge, and π-stacking networks while hydrophobic contacts remain stable is mechanistically interesting and consistent with known thermophilic protein features. However, whether this redistribution requires IG guidance specifically, or whether any directed search in thermophilic sequence space would produce the same result, is untested. The DeepSTABp tie between XPro-Design(P) and ADFLIP is an unreported finding in the paper that, if investigated, could clarify whether the optimization is genuinely learning thermophilic residue preferences or merely amplifying patterns already implicit in HyperMPNN/ProteinMPNN.

---

## Suggestions
1. Remove "low-rank matrix" and "epistatic interactions" from the abstract to accurately describe the actual method (iterative PSSM biasing with IG-weighted updates).
2. Report and discuss the ADFLIP–XPro-Design(P) tie on DeepSTABp (both 76.8°C mean), which is the most important data point for evaluating independence from the optimization signal.
3. Add an ablation: IG-guided PSSM vs. random PSSM updates vs. temperature annealing alone.
4. Relabel Table 3's "ΔΔG" column to clarify it reflects relative MM/GBSA energies, and hedge all thermodynamic conclusions accordingly.
5. Report SOR results in the main paper.
6. Acknowledge the PTM/pLDDT degradation in Table 2 and discuss whether it represents a known trade-off between stability optimization and structural confidence.

---

## Score Calibration

**Anchors retrieved:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| GeoRDe (RNA inverse folding) | doBof19Ia4.md | 2.60 | R1 weak | Much weaker — limited contribution, poor baselines |
| 3D Molecular Graph Explanation | yarlMUJePB.md | 3.40 | R1 weak | Weaker — narrower scope, similar evaluation issues |
| Protein Generative Model Metrics | 1S8ndwxMts.md | 3.00 | R1 weak | Weaker — survey-style, limited novelty |
| Zero-Shot Enzyme Generation (SENZ) | T7lQGq73Lm.md | 5.50 | R1 mid | Comparable — computational-only, some evaluation concerns, rejected |
| Data Distillation for Protein Design (EXO) | ua5MHdsbck.md | 7.00 | R1 mid | Stronger — wet-lab benchmarks (AAV, GFP), proper ablations, accepted |
| InvMSAFold | 1iuaxjssVp.md | 7.25 | R1 mid | Stronger — concrete diversity results, well-evaluated |
| Protein Walk-Jump Sampling | zMPHKOmQNb.md | 8.00 | R1 strong | Much stronger — experimental validation, novel generative formalism |
| HADES (Structure-aware HMC) | wVmShpwtY0.md | 4.00 | R2 | Similar — protein optimization with computational-only eval, poor ablations, only 2 proteins; XPro-Design is more polished but evaluation is more fundamentally compromised |
| ProteinMPNN DPO for peptide design | VY96NfQRIo.md | 4.75 | R2 | Comparable — incremental over ProteinMPNN, computational-only, limited baselines; XPro-Design has more novel framing but bigger evaluation integrity problem |
| Diffusion on LM encodings (DiMA) | LoXJlAW3gU.md | 5.17 | R2 | Slightly stronger — unconditional generation with better ablations, no circularity problem |
| Conditional Enzyme Generation (ProCALM) | dWReNWEj5b.md | 5.75 | R2 | Stronger — cleaner evaluation, proper adapter method, better ablations |

**Round 1 bracket**: 4–6  
**Round 2 narrowing**: The round-2 anchors place the paper between HADES (4.0) and DiMA (5.17). XPro-Design is more polished and broader than HADES but the circular evaluation problem and abstract inaccuracies are more fundamental than HADES's organization issues. It is weaker than DiMA (5.17) because DiMA has no evaluation circularity and proper ablations. The DPO peptide paper (4.75) is the closest comparator: both use ProteinMPNN as backbone, both are computational-only, both have minor evaluation concerns. XPro-Design's idea is more novel but its evaluation integrity problem is more severe. Final score: **4.0**.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>