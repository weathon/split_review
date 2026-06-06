## Summary
CCAT proposes a two-stage multimodal training framework: (1) pretraining a shared classifier using bidirectional cross-attention with modality-contribution regularization, then (2) freezing this classifier during alternating encoder training while injecting per-modality LoRA adapters and applying sample-level re-optimization. The paper frames this via a gradient-dynamics analogy between class and modality imbalance, achieving SOTA results on CREMA-D (+1.35%), Kinetic-Sound (+6.76%), and MVSA (+1.92%).

## Rebuttal Assessment

**Weakness:** Ablation cannot isolate pretraining from freezing
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly point to Figure 5 plot (b), the "Non-Fixed Classifier" condition, which uses the *same pretrained weights* as CCAT but without freezing during alternating training. Its clustering metrics (CH=200.01, SH=0.20, DB=1.46) are nearly identical to MLA (CH=198.98, SH=0.19, DB=1.42), which uses no specialized pretraining at all. The massive gap opens only when freezing is applied (CCAT: CH=242.55). This comparison — already in the paper but not emphasized as addressing the ablation gap — provides meaningful evidence that pretraining quality alone is insufficient and that the *freezing mechanism* is the operative driver of representational improvement. This is a legitimate point the original review underweighted by not connecting Figure 5(b) to the ablation isolation concern. However, the ablation still does not test "freeze a vanilla/jointly-trained classifier + LoRA," so the question of whether the *quality* of the pretrained initialization matters (when frozen) remains unverified. The weakness is partially but not fully resolved.
- **Score impact:** Weakness downgraded from Major to Minor

**Weakness:** Architectural incoherence between pretraining and inference
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Section 3.3 (lines 133–134) explicitly acknowledges the distribution mismatch: *"the classifier Cls(·), which was adapted to the decision boundaries of the fused features f during pretraining, must now process unimodal features z^m during alternating training, where P(z^m|y) ≠ P(f|y)."* The author argues that: (a) the modest LoRA gap (1.21%) still contributes consistently across all three benchmarks; and (b) even the No-LoRA variant (84.68%) sits 1.06pp above the No-Freeze variant (82.80%), suggesting the frozen anchor itself provides regularization independent of LoRA. The theoretical reframing — that cross-attention pretraining encodes inter-modal relational structure into decision boundaries "before" freezing — is plausible but implicit in the paper, not substantiated with new analysis. The inference-pretraining mismatch remains an honest limitation. The original concern is partially addressed by existing text, but the framing remains underexplained in the submitted paper.
- **Score impact:** Weakness unchanged (remains Minor)

**Weakness:** "Unified theoretical framework / proof" language overstated
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as mitigation — The paper (line 59) still reads: "This section establishes a unified theoretical framework and provides a proof of their underlying similar." The authors commit to revision but the submitted paper retains the overclaimed language. An acknowledgment does not retroactively fix the overstatement.
- **Score impact:** Weakness unchanged (remains Minor)

**Weakness:** Abstract claim "prevents dominance" overstates Figure 1
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as mitigation — The abstract (line 9) still reads: "preventing bias toward any modality." The data in Figure 1 (verified at lines 36–43) confirms the 65%/35% split at epoch 100, not 50%/50%. Authors commit to revision, but the current paper is misleading. This is a minor but real framing issue.
- **Score impact:** Weakness unchanged (remains Minor)

**Weakness:** Missing computational cost analysis
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as mitigation — No timing data is present in the paper. The authors acknowledge the gap and offer qualitative reasoning (pretraining only trains fusion module + classifier, not full encoder stack), but without numbers, compute attribution remains uncertain. Future revision promise does not count.
- **Score impact:** Weakness unchanged (remains Minor)

**Weakness:** LFM baseline absent from MVSA without explanation
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as mitigation — Table 1 still shows "−" for all MVSA LFM entries with no footnote or explanation in the submitted paper. The authors' plausible explanation (LFM was not evaluated on text-image sentiment in its original publication) should have been in the paper. It is not.
- **Score impact:** Weakness unchanged (remains Minor)

**Weakness:** Caption inconsistency in Figure 4 (MVSA peak)
- **Author's response:** Acknowledge
- **Assessment:** Confirmed — The caption text states "MVSA shows a peak at β=0.25 (80.54%)" while the embedded data (lines 299–303) clearly shows MVSA maximum is 80.73 at β=0.05. The chosen final configuration (β=0.05, 80.73%) is correct; the caption text contains a typographical error. Trivial issue.
- **Score impact:** Weakness unchanged (remains Trivial)

---

## Strengths
- **Consistent and substantial SOTA improvements across three benchmarks:** Table 1 (lines 191–203) confirms CCAT outperforms all baselines including LFM on CREMA-D (85.89 vs. 83.62) and KS (79.29 vs. 72.53), with a large +6.76% margin on KS over the strongest prior method.
- **Mechanistic evidence for freezing via Figure 5's Non-Fixed Classifier comparison:** The Non-Fixed Classifier (pretrained weights, no freezing) achieves CH=200.01 ≈ MLA CH=198.98, while CCAT (same pretrained weights, frozen) achieves CH=242.55. This already-in-paper comparison provides meaningful (though not conclusive) evidence that the freezing mechanism rather than pretraining quality is driving the representational gains.
- **Ablation study covers all four design components systematically:** Table 2 (lines 207–214) provides consistent, multi-dataset ablations with verifiable per-component contributions across all three datasets.
- **Sample-level secondary update is independently validated:** The Sec=✗ row shows 83.06% (CREMA-D Multi), confirming a 2.83pp contribution from the secondary update mechanism alone.
- **Classifier-centric framing of alternating training's residual bias is a genuine contribution:** The observation that alternating training resolves encoder interference but leaves classifier bias entrenched (Figure 1) is empirically well-grounded and underexplored in prior work.

---

## Weaknesses

### Fatal
*None.*

### Major
*None after rebuttal (the original Major weaknesses have been downgraded).*

### Minor
- **Ablation still does not isolate quality of frozen initialization from the stabilizing effect of freezing.** The ablation tests "pretrained + frozen" vs. "pretrained + unfrozen," but never tests "vanilla + frozen + LoRA." Figure 5(b) provides suggestive evidence, but does not close this gap: we know pretraining helps *when frozen*, but not by how much.
- **Inference-pretraining distribution mismatch is acknowledged but underdiscussed.** The motivation for cross-attention pretraining ("rich cross-modal interactions") applies only at initialization. The paper's framing of this as a solved problem via LoRA is not fully supported by the modest 1.21% LoRA gap.
- **"Proof" and "unified theoretical framework" language in Section 3.1 overstates an informal gradient-approximation analogy.** The analogy is useful motivation, not a formal proof. This remains misleading in the current submission.
- **Abstract "preventing bias toward any modality" contradicts Figure 1's 65%/35% result.** The correct characterization is "substantially reduces bias."
- **No wall-clock or FLOP comparison** despite an additional pretraining stage absent from all baselines.
- **LFM omission from MVSA is unexplained** in the current paper.

### Trivial
- **Figure 4 caption text error:** States MVSA peak at β=0.25 (80.54%) but correct peak is β=0.05 (80.73%) per the embedded data table and implementation details. Final reported result is correct.

---

## Nice-to-Haves
- Add ablation row: "freeze vanilla (non-pretrained) classifier + LoRA + alternating training" to directly establish whether pretraining quality contributes to the frozen anchor's effectiveness, beyond what unfrozen pretraining provides.
- Report wall-clock training time vs. all baselines to contextualize the additional pretraining compute.
- Correct framing in Section 3.1 from "proof" to "gradient-dynamics motivation" and in abstract from "preventing" to "substantially reducing" modality bias.
- Explain the LFM omission from MVSA with a footnote.

---

## Novel Insights
CCAT's central reframing — that alternating training resolves encoder-level gradient interference but fails to prevent the classifier from accreting structural preference toward the faster-converging modality — is a productive and underexplored contribution to the modality imbalance literature. The analogy to class-imbalance remedies (stabilizing the decision boundary by freezing it) is conceptually clean and empirically supported. The rebuttal clarifies that Figure 5's Non-Fixed Classifier comparison, already present in the paper, provides stronger mechanistic evidence for the freezing hypothesis than the original review credited: an identically initialized but unfrozen classifier degrades to near-MLA clustering quality, suggesting freezing (not pretraining quality) is the operative mechanism. This nuance strengthens the paper's methodological narrative. The LoRA-per-modality design cleanly bridges the pretraining-to-inference distribution shift while preserving the frozen anchor. Beyond this core insight, the paper does not contribute formal theoretical results, and the gradient-dynamics section remains an analogy rather than a proof.

---

## Suggestions
1. Add the "freeze vanilla classifier + LoRA + alternating" ablation row to Table 2 to complete the mechanistic argument.
2. Report wall-clock training time per method.
3. Revise Section 3.1 header and body to replace "proof" with "gradient-dynamics motivation" and reduce "unified theoretical framework" to "gradient-dynamics analogy."
4. Revise abstract: "preventing bias toward any modality" → "substantially reducing bias toward dominant modalities."
5. Add footnote to Table 1 explaining LFM's omission from MVSA (e.g., not evaluated on text-image sentiment in the original publication, making reproduction non-trivial).
6. Add a sentence in Section 3.3 explicitly stating that inference uses unimodal features with LoRA correction (not cross-attention fused features), and explain why cross-attention pretraining still produces a better frozen anchor than a jointly-trained classifier.

---

## Score and Decision

**Rebuttal impact assessment:**

The rebuttal's most important contribution is making explicit that Figure 5(b) — the Non-Fixed Classifier condition, already in the paper — provides meaningful evidence that the freezing mechanism (not pretraining quality alone) drives the representational gains. The near-identical clustering metrics for Non-Fixed (CH=200.01) vs. MLA (CH=198.98) despite the Non-Fixed condition having access to the carefully pretrained weights makes a compelling case. The original review noted Figure 5 as a strength but failed to connect it to the ablation isolation concern — this oversight was worth correcting.

Revised assessment: The original Major weakness about ablation isolation is downgraded to Minor, as Figure 5(b) provides meaningful (though incomplete) mechanistic evidence. All other weaknesses (overstatement of theory, missing compute analysis, inference mismatch, LFM omission) remain valid and acknowledged by the authors. These are collectively Minor concerns — real but not disqualifying. The core empirical contribution and classifier-centric framing remain solid.

Compared to the calibration anchors: ul1cjLB98Y (5.25, reject) had weaker empirics but stronger theory; 5BXWhVbHAK (6.33, accept) had theoretical bounds and broader scope. After the rebuttal partially addresses the major methodological concern, CCAT's position shifts upward. The remaining minor weaknesses (framing overstatements, missing analyses) are typical of papers at the borderline. The empirical results are strong and reproducible, and the classifier-centric insight is genuine.

**Final score: 6.0 — borderline accept.** The rebuttal reveals that an important mechanistic piece of evidence (Figure 5's Non-Fixed Classifier) was already in the paper and partially addresses the ablation isolation concern. This shifts the paper from "borderline reject" to "borderline accept." The remaining weaknesses are Minor and correctable in revision. The consistent SOTA gains across three benchmarks, the novel classifier-centric framing, and the Figure 5 mechanistic evidence together constitute a sufficient contribution for acceptance, provided the framing overclaims (theory/proof language, "prevents" dominance) are corrected.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>