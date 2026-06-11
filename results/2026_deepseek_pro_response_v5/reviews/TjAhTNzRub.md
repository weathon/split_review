Now I have enough data to finalize my calibration. Let me write the final review.

**Comparison summary:**
- SUN (4.00): Simpler method, limited evaluation. MoRE is clearly stronger.
- Forget Vectors (4.80): Clever idea but fundamental limitations. MoRE is stronger.
- Deep Unlearning (5.25): Comparable training-free unlearning. MoRE has better mathematical formulation and broader evaluation, but MoRE also has the overclaiming issue.
- Unlearning via Sparse Representations (5.25): Architecture-specific; MoRE is more general.
- Decoupling Class Label (5.75): More conceptual novelty; MoRE slightly below this.

MoRE sits around **5.0** — technically solid with good experiments, held back by the KR interpretation gap and overclaiming on irreversibility.

---

## Summary
MoRE proposes a training-free framework for feature-level machine unlearning that combines prototype-orthogonal (PO) projection with remapping via multiple experts. The PO projection uses the pseudoinverse of the prototype matrix to decorrelate forget and remain prototypes before editing, then remaps forget features to remain prototypes (scattered across stochastic experts) to disrupt separability. Across CIFAR-10, CIFAR-100, and Tiny-ImageNet, MoRE achieves competitive utility preservation with near-zero forget accuracy under Knowledge Retention probing, while being orders of magnitude faster than training-based methods, and demonstrates cross-domain applicability on diffusion model artistic style erasure.

## Strengths
- **Prototype-orthogonal projection is mathematically clean and empirically validated**: The pseudoinverse formulation (Eq. 2) enforces DP = I_k, decorrelating prototypes so that editing forget prototypes leaves remain prototypes intact. Table 3 ablation provides causal evidence: without PO, Erase leaves 14.38% forget accuracy and degrades remain; with PO, forget drops to 0.00% while remain accuracy is preserved (99.94%). Fig. 6 corroborates this with cosine similarity heatmaps showing remain autocorrelations near 1.0 after PO-based editing.
- **Complement-space projection (Eq. 4-5) is a technically careful refinement**: The skip-connection term (I − PD)z preserves non-prototype information that would otherwise be discarded by the low-rank prototype projection, ensuring a full-rank transformation.
- **Efficiency is genuinely impressive**: Training-free design completes unlearning in ~9.5s with ~540MB GPU memory (Fig. 5), delivering competitive or superior HM scores compared to training-based baselines (Finetune, NG, RL, BS) that require orders of magnitude more compute.
- **Diffusion model extension demonstrates generality**: Table 2 shows MoRE applied to Stable Diffusion v1.4 for artistic style erasure, achieving the best LPIPS_d tradeoff (0.25 for Van Gogh, 0.26 for Kelly McKernan) versus specialized methods (ESD, UCE, RECE), with qualitative results in Fig. 4 showing successful style removal while maintaining prompt fidelity.
- **Comprehensive sensitivity analyses**: Table 5 shows robustness to different target remapping classes (HM range 99.87–99.94 without KR), Fig. 7 demonstrates plateauing performance with expert count, Table 7 validates second-last layer effectiveness, and Table 6 compares stochastic vs. conditional routers.

## Weaknesses

### Fatal
None.

### Major
- **KR evaluation has an unresolved interpretation problem**: Under KR probing, Retrain (trained only on remain data, never exposed to forget classes) achieves 72.62% forget accuracy on CIFAR-10, 57.20% on CIFAR-100, and 78.57% on Tiny-ImageNet (Table 1, KR columns). These are dramatically non-trivial numbers for a model that never saw forget data, indicating the KR metric captures remain-class feature correlations with forget-class labels rather than purely residual forget knowledge. MoRE's near-zero KR scores (10.79%, 0.07%, 0.50%) could therefore indicate successful disruption of the probing protocol rather than irreversible knowledge deletion. The paper never acknowledges or analyzes this interpretation ambiguity, yet builds its central irreversibility claim on these numbers (line 364: "delivering real-world unlearning guarantees stronger than retrain-from-scratch"). This does not invalidate the method, but the authors must clarify what KR actually measures under their setup and what MoRE's advantage means in that context.
- **Irreversibility evidence is limited to a single recovery protocol**: The "irreversible" claim rests entirely on linear probing at one learning rate (lr=0.1). No evaluation tests stronger recovery adversaries such as full fine-tuning, non-linear probes, or probing at varied learning rates. The gap between "resists one specific probing protocol" and "irreversible" is substantial and largely unacknowledged. This is a significant claim-calibration issue throughout the paper (abstract, introduction, methods, conclusion).

### Minor
- **"Exact" framing in the abstract is misleading** (line 9): "exact feature-level unlearning" implies formal guarantees (e.g., information-theoretic bounds, proof of non-recoverability). The paper provides no such guarantees; the method is an empirical heuristic with no formal irreversibility proof. The framing should be calibrated to what is demonstrated.
- **Random data forgetting evaluation is incomplete** (Section 4.3, Table 4): Only the single-expert **Remap** variant is evaluated, not the full **MoRE** multi-expert framework that is the paper's primary contribution. The adaptation protocol is underspecified — when forget and remain data come from the same classes, how are prototypes constructed? How many prototypes? The entire protocol is described in a single sentence (line 360).
- **"Constant space complexity" claim is inaccurate** (line 83): Prototype storage requires O(dk) memory, which is linear in the number of concepts k, not constant. The per-sample inference cost may be constant in k, but the claim as written is incorrect and should be rephrased.

### Trivial
- "MoUE" appears in Table 7 without definition — appears to be a typo for "MoRE."
- Table 1 layout is difficult to parse: the column header notation is inconsistent between standard and KR settings, and standard deviations mentioned in the caption ("mean ± std across three trials") are not visible for many entries where only point estimates appear.

## Nice-to-Haves
- Testing recovery under full fine-tuning or probing at multiple learning rates would substantially strengthen (or appropriately qualify) the irreversibility claim.
- Clarifying the random data forgetting protocol with full MoRE results and describing prototype construction when forget/remain data are from the same classes.
- Discussion of behavior when the number of forget classes is large relative to remain classes (few remain prototypes available for remapping).
- Explicitly positioning MoRE relative to certified unlearning and DP-based methods to clarify the contribution's scope boundary.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic suggestion about missing appendix / missing proofs**: The parser strips appendices; these sections exist in the original submission and may contain further protocol details. Not a valid criticism of the paper as submitted. Removed.
- **Harsh Critic claim that diffusion model extension description is "misleading" about "no architecture-specific adaptation"**: The paper acknowledges targeting cross-attention layers; the key claim is that no specialized training, hyperparameter tuning, or architectural modification was needed — and this is fair and verifiable. Removed.
- **Harsh Critic nitpick about Table 1 readability as a major concern**: Real but minor formatting issue. Downgraded to trivial.
- **Strength Finder "training-free design achieves linear complexity with SOTA performance"**: Partially true — MoRE is competitive but doesn't dominate all metrics. Kept a much toned-down efficiency strength.
- **Strength Finder "the stochastic router is pragmatically justified and empirically validated"**: This is a design decision, not a research contribution or strength. Removed.
- **Harsh Critic "no comparison to certified unlearning or DP-based methods"**: Outside the stated scope of feature-level unlearning. Moved to Nice-to-Haves.
- **Harsh Critic "space complexity phrasing is a fatal flaw"**: It's a minor wording imprecision (the claim is about per-sample cost). Kept as a minor weakness. Not fatal.

## Novel Insights
The Retrain KR paradox is a genuinely revealing observation that extends beyond this paper: if a model never trained on forget data can be probed to classify forget classes at 72% accuracy (CIFAR-10), then linear-probing-based unlearning evaluations in the literature may systematically overestimate residual knowledge. This has implications for how the field should interpret KR-style metrics broadly, not just for MoRE. The paper would benefit from explicitly analyzing this phenomenon — for instance, does MoRE's advantage come from actively disrupting remain-forget feature correlations that make probing possible, rather than from more-complete knowledge removal? Framing it this way would turn a potential weakness into a more interesting and defensible contribution.

## Suggestions
- Directly address the Retrain KR paradox: explain what it means that a model never exposed to forget data achieves 72% forget accuracy under probing. Consider whether MoRE's advantage stems from actively disrupting remain-forget feature correlations, and frame the contribution accordingly rather than claiming unqualified "irreversibility."
- Test KR probing at multiple learning rates (e.g., 0.001, 0.01, 0.1, 1.0) to demonstrate robustness of the result to probe hyperparameters.
- Include at least one stronger recovery adversary — even a single full-fine-tuning experiment on a small labeled subset of forget data — to better support or appropriately qualify the irreversibility claim.
- Replace "exact feature-level unlearning" in the abstract with more precise language reflecting what is actually achieved.
- Clarify the random data forgetting protocol (prototype construction, number of prototypes) and report full MoRE results alongside Remap.
- Correct "constant space complexity" to accurately reflect O(dk) storage, or clarify what quantity is constant.

## Score and Decision

**Calibration anchors considered:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| SUN (p7mgNvOD9Q) | 4.00 | R1, R2 | Simpler training-free method, limited eval; MoRE is clearly stronger |
| CodeUnlearn (E6rpTruK4v) | 3.80 | R1, R2 | LLM-focused, different paradigm; not directly comparable |
| Forget Vectors (7tpMhoPXrL) | 4.80 | R2 | Input-perturbation, limited datasets; MoRE is stronger |
| Deep Unlearning (pUOesbrlw4) | 5.25 | R1, R2 | Comparable training-free unlearning; MoRE has better math and diffusion extension but also the overclaiming issue |
| Unlearning via Sparse Repr. (TLBPjECC5D) | 5.25 | R2 | Architecture-specific; MoRE is more general but has the KR interpretation gap |
| Decoupling Class Label (OHOmpkGiYK) | 5.75 | R1, R2 | More conceptual novelty; MoRE is slightly below in contribution clarity |
| Jogging Memory of Unlearned LLMs (fMNRYBvcQN) | 6.75 | R1 | Attack-focused, strong conceptual framing; MoRE significantly below |
| Utility & Complexity of Unlearning (HVFMooKrHX) | 6.60 | R1 | Theoretical paper with formal guarantees; MoRE in different sub-area |

**Round 1 bracket:** 4.0–5.5. **Round 2 narrowing:** MoRE is technically stronger than Deep Unlearning (5.25) and Unlearning via Sparse Representations (5.25) in terms of method sophistication and experimental breadth, but the unresolved KR interpretation gap and pervasive overclaiming on irreversibility pull it back. It sits near these anchors — comparable in overall quality but with a different mix of strengths and weaknesses. **Final score: 5.0**, reflecting genuine technical contributions that are offset by claim-calibration issues that affect how the paper's central message should be understood.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>