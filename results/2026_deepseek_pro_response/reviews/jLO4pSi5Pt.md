Now I have a clear picture. Let me synthesize the comparison:

- **L-TTA vs. C-CLIP (6.50)**: L-TTA clearly stronger — broader evaluation (multi-backbone, corruption, efficiency), more thorough ablations.
- **L-TTA vs. RLCF (6.67)**: L-TTA stronger — significantly more comprehensive empirical validation.
- **L-TTA vs. Concept Drift for MLLMs (7.00)**: Comparable in ambition and novelty; L-TTA has cleaner methodology but shares similar "first to study X" pattern. Scores on the Concept Drift paper were split (6,8,6,8) due to methodological concerns; L-TTA's methodology is more sound.
- **L-TTA vs. READ (8.00)**: L-TTA is clearly below — READ has new benchmarks, elegant single-focus method, stronger theory, unanimous 8 scores.

L-TTA belongs around **7.0**: a solid paper with real contributions, comprehensive evaluation, but with addressable gaps in the failure-mode-to-component mapping and LT baseline comparisons.

---

## Summary
This paper proposes L-TTA, the first test-time adaptation method designed for long-tailed distributions in vision-language models. L-TTA combines three co-designed components: Synergistic Prototypes (deterministic and exclusionary prototypes for enriching tail-class representations), Rebalancing Shortcuts (learnable cross-attention with a class re-allocation loss), and Balanced Entropy Minimization (a variant of entropy minimization that attenuates head-class confidence via a prediction-dependent penalty term). The method is evaluated across 15 datasets spanning OOD, cross-domain, and corruption benchmarks at three imbalance ratios with multiple backbones, consistently outperforming 11+ baselines with particularly strong macro-F1 gains that directly validate the class-balancing claim.

## Strengths
- **Novel problem formulation with concrete failure-mode diagnosis:** The paper is the first to study long-tailed TTA for VLMs and identifies two specific failure modes — Text-induced Tail Erosion (text-embedding biases from pre-training amplify class imbalance) and Modality-bias Amplification (unimodal LT-TTA methods worsen visual-textual mismatch in VLMs). These are plausible, well-motivated, and justify why a VLM-specific LT-TTA solution is needed (Section 1, lines 38-39).
- **Comprehensive and convincing empirical validation:** The evaluation covers 15 datasets across three benchmark families (OOD, Cross-Domain, Corruption) at three imbalance ratios (10, 20, 50), with both accuracy and macro-F1 reported across 11+ baselines (Tables 1–3). L-TTA achieves best or near-best results in nearly every cell. The macro-F1 gains consistently exceed accuracy gains (e.g., +2.20% macro-F1 vs +1.02% accuracy on Cross-Domain, Table 2), directly validating the class-balancing claim. The method generalizes across four additional backbones (ViT-L/14, ViT-H/14, SigLIP, MetaCLIP-BigG; Table 5) and shows particular robustness under corruption (Table 3), where prior prototype methods degrade sharply.
- **Well-designed EP mechanism:** The Exclusionary Prototypes (Eq. 5) meaningfully extend prior prototype methods by using every view's prediction distribution to update EPs for *all classes* rather than only the predicted class — directly addressing the core LT-TTA problem that tail-class prototypes receive few updates. The subtraction in Eq. 8 provides an effective anti-overconfidence regularizer, and the design differs substantively from TDA's negative cache.
- **Efficient design with strong trade-off:** Table 4 shows L-TTA (1.45h, 1.89G) is competitive with the fastest methods like DPE (1.38h) while dramatically outperforming heavy methods like RLCF (18.30h) and WATT (27.70h). The RS design keeps prompts frozen, avoiding gradient flow through the text encoder backbone.
- **Thorough ablation studies:** Table 6 systematically ablates DP, EP, RS, and BEM across two backbones, demonstrating additive and synergistic contributions. The hyperparameter sensitivity analysis (Figure 4) covers λ₁/λ₂, η, K, and β across multiple datasets with reasonable stability across ranges. Table 7 additionally verifies robustness to dynamic head/tail class ordering.

## Weaknesses

### Fatal
None.

### Major
- **Failure-mode-to-component mapping is asserted but not tested.** The introduction maps Text-induced Tail Erosion (Mode 1) to SyPs and Modality-bias Amplification (Mode 2) to RSs (lines 40-41: "❶ Mitigating Asp. I, II ... ❷ Mitigating Asp. II"), but no experiment verifies these mappings. The component ablation (Table 6) shows each component contributes to overall performance, but does not demonstrate that SyPs specifically reduce text-induced bias or that RSs specifically reduce modality mismatch. Without targeted diagnostics (e.g., measuring text-prior bias with/without SyPs, or visual-textual alignment drift with/without RSs), the failure-mode narrative functions as plausible framing rather than validated analysis. This weakens the paper's central argument that its components are specifically designed responses to identified failure modes.

- **No long-tailed baselines included in comparisons.** All compared methods (TPT, C-TPT, TDA, DPE, etc.) are general-purpose TTA approaches with no long-tailed design. That L-TTA outperforms them is partially expected given its LT-specific design. The paper argues theoretically (lines 134-135) that standard LT techniques like logit adjustment are incompatible with EM, and comparisons to logit adjustment / balanced softmax are deferred to Appendix G. However, including even a simple LT-informed baseline (e.g., standard EM with online logit adjustment using running pseudo-label priors) in the main evaluation would substantially strengthen the causal attribution of gains to L-TTA's specific design choices rather than to the general principle of addressing imbalance.

### Minor
- **EP description does not precisely match the mechanism.** The paper describes EPs as storing "the most improbable features of each class" (line 98). In Eq. 5, the predicted class c* receives φ_c* = 0, meaning its EP is updated at full EMA weight with embeddings the model confidently assigned to c*. These are features the model considers *probable* for c*, not improbable. The subtraction in Eq. 8 then penalizes c* when a sample matches what was confidently classified as c* — an anti-overconfidence regularizer. The mechanism is sound and empirically validated, but the description should be corrected to match what the formula actually computes.

- **Theoretical propositions are modest.** Propositions 1-2 formalize intuitive claims: Proposition 1 states standard EM increases head-class confidence while decreasing tail-class confidence; Proposition 2 claims BEM reduces the head-tail gradient gap. These are gradient-level statements about a scalar loss and do not connect to generalization or decision-boundary quality. The paper appropriately scopes these as motivation rather than deep theory, but the claim that they "guarantee [BEM's] theoretical capabilities" (line 44) is slightly overstated.

- **η=0 reference point missing from ablation figure.** The text claims a 1.19%/1.64% gain from η=0 to η=1 (line 332), but Figure 4.b only shows η values starting at 0.1. The η=0 comparison point (CRA loss disabled) cannot be verified from the figure.

### Trivial
- **K parameter inconsistency.** Implementation details state K=0.3 (line 208), but the ablation text states "K=0.2 yields the best performance" (line 334). Additionally, K is described as the number of hyper-class vectors but takes fractional values (0.1 to 1.0), suggesting it is actually a ratio relative to the number of classes. The description should be clarified and reconciled.

## Nice-to-Haves
- Adding standard deviations to main tables given the 5-run experimental setup would help assess whether the 1-2% gains are statistically meaningful.
- Testing on naturally long-tailed datasets (e.g., iNaturalist, Places-LT) in addition to synthetically induced distributions would strengthen ecological validity.
- Including the BEM-vs-logit-adjustment comparison from Appendix G in the main text would bring the paper's central theoretical argument into the foreground.

## Removed Points
These points are flagged to be removed; treat them with caution.

- HC: "No standard deviations in main tables" — presentation preference common in TTA literature; moved to Nice-to-Haves.
- HC: "No test on naturally long-tailed datasets" — synthetic induction is well-controlled and standard; moved to Nice-to-Haves.
- HC: "No analysis of performance on balanced data" — outside the paper's stated scope (LT-TTA); removed.
- HC: "Theoretical proofs are absent from the main text" — the parser stripped Appendix A; proofs exist in the original submission. The relevant concern (modest theoretical contribution) is retained in Minor.
- HC: "The normalization in Eq. 4 uses ‖N-1‖ which is likely a typo" — parser artifact; removed.
- HC: "Figure 1 referenced to support empirical claims but cannot be seen" — parser artifact; removed.
- SF: "Theoretical formalization of the problem and solution" as a major strength — downgraded since the propositions are modest gradient-level statements; incorporated into Minor weakness discussion.
- HC: Missing related works thread on class-imbalanced TTA — the paper does mention these works (DELTA, SAR) in §2.1; removed.
- HC: "Harmonic mean is an odd choice" — this is a stylistic preference; removed.

## Novel Insights
None beyond the paper's own contributions. The paper's identification of Text-induced Tail Erosion as a VLM-specific phenomenon where text-embedding biases from pre-training interact with long-tailed distributions is a genuinely novel diagnosis, but the reviews do not surface additional insights beyond confirming this.

## Suggestions
- Add targeted diagnostics that verify the failure-mode-to-component mapping: measure per-class accuracy stratified by text-richness with and without SyPs, and measure visual-textual alignment drift with and without RSs. These would transform the narrative framing into validated analysis.
- Include at least one LT-informed baseline in the main evaluation (e.g., standard EM + online logit adjustment using running pseudo-label priors) to anchor the contribution.
- Clarify the EP description: either adjust the prose to match the anti-overconfidence mechanism the formula implements, or explain why "improbable features" describes what is being subtracted rather than what is being stored.
- Clarify whether K is an absolute count or a ratio, and reconcile the default value (0.3) with the reported best value (0.2).

## Score and Decision

### Calibration anchors:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Multi-Label TTA with BEM (`75PhjtbBdr`) | 6.25 | R1 | L-TTA stronger: broader evaluation, more baselines, better ablations |
| TTA with CLIP Reward / RLCF (`kIP0duasBb`) | 6.67 | R1 | L-TTA stronger: more comprehensive empirical validation across datasets and settings |
| C-CLIP (`sb7qHFYwBc`) | 6.50 | R2 | L-TTA clearly stronger: multi-backbone, corruption analysis, efficiency, better presentation |
| Concept Drift for MLLMs (`b20VK2GnSs`) | 7.00 | R2 | Comparable ambition; L-TTA has cleaner methodology, but shares "first to study X" pattern; L-TTA slightly ahead on empirical rigor |
| READ / Multi-modal TTA (`TPZRq4FALB`) | 8.00 | R1 | L-TTA clearly below: READ has new benchmarks, stronger theory, unanimous 8 scores |

Round 1 bracket: 6.5–7.5. Round 2 narrowed: L-TTA sits above the 6.5-6.67 cluster and is comparable to or slightly ahead of the 7.00 anchor. It is clearly below the 8.00 anchor. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>