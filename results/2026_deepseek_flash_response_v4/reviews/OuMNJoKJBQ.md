## Final Review

**Calibration Report:**

**Round 1 — Bracketing:** Broad search for DPO/safety/alignment papers across three score bands.

*Weak anchors (< 3.5):*
| Paper | Score | Comparison |
|-------|-------|-----------|
| CVX-DPO (EVZnnhtMNX.md) | 3.00 | Weak DPO variant, rejected — AW-DPO is far stronger in novelty and evaluation |
| SPO (28TLorTMnP.md) | 2.50 | Listwise preference optimization, rejected — much weaker empirical support |
| Multi-Objective ORPO (aYYZBPoSHb.md) | 3.40 | Self-judgement alignment, rejected — AW-DPO has stronger method and results |
| Reward Learning With Ties (fTdhM7q1o2.md) | 3.00 | Preference with ties, rejected — narrower scope, less impact |

*Middle anchors (3.5–7.5):*
| Paper | Score | Comparison |
|-------|-------|-----------|
| SafeDPO (MoJSnVZ59d.md) | 6.40 | DPO safety variant, rejected as incremental — AW-DPO has more novelty and evaluation |
| 3D-Properties (9Hxdixed7p.md) | 6.25 | DPO theoretical analysis, accepted — AW-DPO has stronger empirical contribution |
| MODPO (2BfZMh9td4.md) | 4.25 | Multi-objective DPO, rejected — AW-DPO has clearer focus and better results |
| DPO Unobserved Preference (NQZNNUsutn.md) | 4.00 | Preference heterogeneity, rejected — AW-DPO has stronger practical contribution |

*Strong anchors (> 7.5):*
| Paper | Score | Comparison |
|-------|-------|-----------|
| MAP (NN6QHwgRrQ.md) | 8.00 | Multi-human-value alignment — top-tier paper, AW-DPO is not at this level |
| Rethinking Reward (rfdblE10qm.md) | 8.00 | Theoretical analysis of reward models — different type of contribution |
| Booster (tTPHgb0EtV.md) | 8.00 | Harmful fine-tuning defense — top-tier empirical paper |
| Backtracking (Bo62NeU6VF.md) | 8.00 | Generation backtracking for safety — top-tier novel method |

**Initial Bracket:** 5.5 – 7.0 (clearly above weak papers, clearly below outstanding 8.0 papers)

**Round 2 — Narrowing:** Search within 5.0–7.5 for more granular comparison.

| Paper | Score | Comparison |
|-------|-------|-----------|
| SaLoRA (GOoVzE9nSj.md) | 6.50 | Safety-preserving LoRA, accepted — closest peer. AW-DPO has comparable novelty and more thorough evaluation; similar level of fixable exposition issues |
| SCDPO (ZRDa2IT1sQ.md) | 6.00 | Stepwise DPO for math, rejected — AW-DPO is more novel and better evaluated |
| Safety Layers (kUH1yPMAn7.md) | 6.00 | Identifying safety layers, accepted — AW-DPO has stronger practical contribution |
| Safety-Tuned LLaMAs (gT5hALch9z.md) | 6.00 | Safety data recipe study, accepted — AW-DPO has more algorithmic novelty |
| Breach By A Thousand Leaks (8Rov0fjpOL.md) | 5.80 | Safety evaluation framework, accepted — different contribution type |

**Final Calibration:** AW-DPO is closest to SaLoRA (6.50) and stronger than SafeDPO (6.40). The core method is novel, the evaluation is thorough, and the weaknesses are fixable exposition issues rather than fundamental flaws.

---

## Summary
This paper proposes Alignment-Weighted DPO (AW-DPO), which improves LLM safety alignment by separately weighting reasoning and response segments during DPO training. The paper first provides causal evidence (via neuron deactivation) that current alignment is "shallow" and independent of reasoning. It then constructs a CoT safety dataset, identifies failure modes in CoT fine-tuning (correct reasoning + unsafe answer; incorrect reasoning + safe answer), and introduces AW-DPO to apply fine-grained preference weights to each segment. Experiments across multiple model families and 20 jailbreak attacks show consistent improvements over standard DPO and other baselines.

## Strengths
- **Novel, well-motivated method with clear empirical validation.** AW-DPO's core idea — decomposing DPO into reasoning and response segments with adaptive weighting — is novel and the ablation study (Figure 4b, 4c) confirms it outperforms standard DPO on identical data, cleanly isolating the benefit of the weighting mechanism.
- **Thorough evaluation.** Experiments span 4 model families (LLaMA-2-7B, LLaMA-3.2-3B, LLaMA-3.1-8B, Mistral-7B), 20 jailbreak attacks across 5 categories, and multiple strong baselines including DPO, SAFECHAIN, RR, and STAIR.
- **Practical transferability analysis.** Table 3 shows an AW-DPO dataset constructed on one model transfers to other architectures with moderate degradation, reducing deployment cost.
- **Original causal intervention experiment.** Section 3 provides an interesting mechanistic perspective going beyond typical correlational analyses of alignment.

## Weaknesses

### Fatal
None.

### Major
- **The 15% failure-mode figure (Section 4, line 121) that directly motivates AW-DPO is presented without methodological support.** The paper states it "quantified these two types of errors" at "approximately 15% of all failure cases" but provides no details on sample size, annotation criteria, inter-annotator agreement, or how failure cases were identified. Since this observation is central to the motivation for AW-DPO over standard DPO, the paper needs rigorous evidence here.
- **The "importance scaling factor α" appears in Table 4 and Section 5.6 but is never defined in the method section or any equation.** The loss formulation (Equations 2-4) uses only w_reasoning and w_respond weights computed from d_reasoning and d_respond ratios. A reader cannot interpret what α controls, how it enters the loss, or what the ablation results mean. This is a basic exposition gap.

### Minor
- **Notation for γ is overloaded.** In Equation 2 (line 133) γ is the DPO scaling coefficient, while in Figure 2 and Section 4 (lines 97, 113, 127) γ is the preference-pair selection threshold. These are different hyperparameters controlling different aspects of the method. The paper also uses β for this role in Equation 1 but switches to γ in Equation 2.
- **The causal intervention experiment relies primarily on probing accuracy** rather than direct behavioral measures. The paper mentions behavioral results in Appendix D, but the main text's central claim — "current alignment is largely superficial and does not depend on deep reasoning" — rests heavily on probing results alone. The evidence is suggestive but the strength of the claim is somewhat disproportionate.
- **Table 2 inconsistencies.** "SAFERACH" appears instead of "SAFECHAIN" (the name used in Section 5.1), and "PP" appears for what Section 5.1 calls "RR" (Representation Rerouting). These reduce readability.
- **Transferability claim is slightly overstated.** Table 3 shows ASR increases of 3-5× compared to in-distribution results (e.g., Llama3.2-3B: 1.85% transferred vs. 0.58% original). "Strong transferability" would be more precisely stated as "effective transfer."

### Trivial
- The method section uses w for both the binary token-level mask (w_{s_t} ∈ {0,1}) and the continuous segment-level weights (w_reasoning, w_respond), which is notationally confusing.

## Nice-to-Haves
- Move behavioral evaluation results (Appendix D) into the main paper to provide direct behavioral evidence for the causal intervention claim, rather than relying primarily on probing accuracy.
- Discuss degenerate cases in the weight computation (e.g., d_reasoning and d_respond having opposite signs or summing to zero).

## Removed Points
The following points from the Harsh Critic were removed:
- "Identification of reasoning-critical neurons is circular" — Removed. Zeroing out high-probability-accuracy heads and measuring degraded performance is a standard causal intervention, not circular reasoning.
- "The alignment task being easier undercuts the interpretive frame" — Removed. The paper explicitly acknowledges the task is easier (line 68). This does not invalidate the dissociation finding.
- "Table 1 large variance is a problem" — Removed. The paper reports Std↓ transparently; high variance across very different attack categories is expected and honestly reported.
- "STAIR-DPO-3 comparison is unfair" — Removed. The paper explicitly discusses the training cost tradeoff and frames it honestly.
- Generic claims about abstract over-claiming, missing related work, or formatting — Removed per guidelines.

## Novel Insights
None beyond the paper's own contributions. The key insight — that DPO can be improved by decomposing responses into reasoning and answer segments with separate preference weights — is the paper's own contribution, not a synthesis emerging from the reviews.

## Suggestions
1. Define α explicitly in the method section. Clarify how it modifies the loss (e.g., as a weight scaling factor, temperature, or regularization coefficient applied to the loss components).
2. Provide rigorous methodological support for the 15% failure-mode figure (sample size, annotation criteria, inter-annotator agreement) or drop the precise percentage and describe the patterns qualitatively.
3. Reconcile the notation for γ: use distinct symbols for the DPO scaling coefficient (e.g., keep β from Equation 1) and the preference-pair selection threshold.
4. Fix the "SAFERACH"/"PP" typos in Table 2.
5. Soften the "strong transferability" claim to reflect the observed performance drop.
6. Move the behavioral evaluation results (Appendix D) into the main paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>