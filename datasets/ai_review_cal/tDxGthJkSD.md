- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
I now have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes HCRAL (Hybrid Classification-Regression Adaptive Loss) for dense object detection, combining a Residual of Classification and IoU (RCI) module for cross-task consistency, a Conditioning Factor (CF) for hard-sample emphasis, and an Expanded Adaptive Training Sample Selection (EATSS) strategy. The method is evaluated on COCO, achieving 44.4 AP with ResNet-50 on test-dev (outperforming GFL at 43.1 and VFL at 43.6) and generalizing across RetinaNet and ATSS detectors.

## Strengths

1. **Novel cross-task inconsistency mechanism**: The RCI module (Eq. 1, Section 3.1) explicitly encodes the residual between classification score and IoU into both task losses. Ablations confirm removal of RCI causes measurable drops (0.2 AP in classification on RetinaNet, Table hcrac‑1 line "– 20"; 0.3 AP in regression, Table hcrar‑1 line "– –"), providing direct evidence that RCI contributes beyond standard task losses.

2. **Competitive COCO test-dev results**: With ResNet‑50, HCRAL achieves 44.4 AP, outperforming GFL (43.1 AP) and VFL (43.6 AP) under the same backbone and multi-scale training schedule (Table 7). Improvements persist across deeper backbones, culminating in 51.4 AP with Res2Net‑101‑DCN and auxiliary modules — a strong showing against prior one‑stage detectors.

3. **Generalization across detectors**: HCRAC and HCRAR are separately plugged into RetinaNet and ATSS and compared against standard classification/regression losses (Tables hcrac‑loss, hcrar‑loss). On RetinaNet, HCRAC achieves 37.6 AP vs. best prior 37.4 AP, and HCRAR achieves 37.4 AP vs. best prior 37.2 AP, demonstrating the loss components improve performance beyond the specific FCOS+ATSS framework.

4. **Empirical motivation via data distribution**: Figure 3a plots the joint distribution of IoU and classification scores, showing most points deviate from the consistency line. This visual evidence concretely motivates the design of the RCI module.

## Weaknesses

### Fatal

None.

### Major

1. **Method presentation has multiple ambiguities and errors that hinder reproducibility.** Several key equations are imprecisely specified or contain typos:
   - Eq. (4) (line 122): $(1 - IoU(IoU-\mu)^{2})$ for $p^\ast=0$ is syntactically ambiguous — it is unclear whether the intended operation is $1 - [IoU \times (IoU-\mu)^2]$ or $(1 - IoU) \times (IoU-\mu)^2$.
   - Eq. (6) (line 138): The numerator contains $e^{\theta RIC}$ — "RIC" is clearly a typo for "RCI". The condition "$p > \text{IoU}$" compares a probability to an IoU value without justification of their numerical compatibility.
   - Eq. (8) (lines 179–183): $RCI_{reg}$ uses $IoU(tb,cb)$ where $tb$ and $cb$ are never defined. The claimed ratio behavior (amplify region 1, suppress region 2) is described verbally but the notation is incomplete.
   - The column header in Table hcrac‑2 is labeled $\mu$ while the caption and surrounding text refer to it as $\gamma$ — a labeling inconsistency.
   - These issues collectively mean the method cannot be reproduced from the paper without substantial guesswork.

2. **Test-dev comparison lacks the paper's own baseline under the same pipeline.** Table 7 compares HCRAL against literature-reported numbers (GFL, VFL), but does not report what the underlying FCOS+ATSS baseline achieves on test-dev under the paper's exact training code, hyperparameters, and schedule. Without this apples-to-apples baseline, it is unclear what portion of the gain comes from HCRAL versus implementation details, multi-scale training choices, or other undocumented pipeline differences.

3. **Key claim about prior work is asserted without evidence.** The Introduction (line 14) states that GFL and VFL "fail to effectively focus on truly difficult-to-train samples when dealing with samples with similar IoU," but the paper never tests this claim — e.g., by visualizing per-sample loss weights or comparing which samples receive high/low weight under HCRAL vs. those methods. This weakens the position that the paper addresses a demonstrated gap.

4. **EATSS algorithm description is too vague to reproduce.** Algorithm 1 (lines 207–224) states: "Get the set $E$ satisfying the maximum distance $Dis_f$ of $P$" — it is unclear what "satisfying the maximum distance" means or how $Dis_f$ is computed. The ranking function for selecting additional candidates is described only as "distance and IoU" without specifying how they are combined. A single brief paragraph of accompanying text (lines 226–229) does not provide sufficient detail.

### Minor

1. **No ablation isolates CF from RCI individually.** The hyperparameter tables show "without RCI" ablations (lines 258, 296), but there is no ablation that removes CF while keeping RCI. Since RCI and CF are both multiplicative factors on the loss, their individual contributions to the 0.9 AP total gain (Table 6) cannot be separated — the paper claims RCI addresses consistency and CF addresses hardness, but this is not experimentally disentangled.

2. **EATSS alone yields negligible gain.** EATSS+FL+GIoU gives only +0.1 AP over the baseline (41.2→41.3, Table 6), which is within typical noise for a single run. The paper claims EATSS "provides additional samples that can be optimized by RCI," but the synergistic effect is supported only by the aggregate +0.9 AP number without variance or analysis of which samples are added and how RCI weights them.

3. **Single-run results without variance estimates.** All ablation and main results are reported as single AP numbers without standard deviations, confidence intervals, or seed sensitivity. Given that several gains are in the 0.1–0.4 AP range, uncertainty quantification would substantially strengthen the evidence.

4. **Loss tuned differently across architectures.** The regression hyperparameters differ between RetinaNet and ATSS (e.g., $\gamma$ is removed for ATSS, line 245), suggesting the loss formulation requires per-detector tuning and is not architecturally robust.

### Trivial

- $e^{\theta RIC}$ in Eq. (6) — should be $e^{\theta RCI}$.
- Table hcrac‑2 column header uses $\mu$ where $\gamma$ is intended.
- $IoU(tb,cb)$ in Eq. (8) is used without definition.
- The notation $Dis_f$ in Algorithm 1 is introduced but never defined.

## Nice-to-Haves

- Code release would aid reproducibility and adoption, though it is not required for evaluation.
- Training curves, loss weight distributions over sample types, or visualizations of which anchors receive high/low RCI weights would strengthen the mechanistic claims.
- An additional experiment on PASCAL VOC or a small-scale dataset could demonstrate generalization beyond COCO.
- A discussion of limitations (e.g., sensitivity to IoU distribution, small objects, extreme class imbalance) would improve the paper's completeness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No code release or detailed hyperparameter search setup"**: Removed per instructions — requesting code release as a condition for credibility goes beyond what is standard for paper evaluation. The hyperparameter sweeps are provided in multiple tables.
- **"No comparison on other datasets"**: Removed as scope creep — evaluating on COCO is standard and sufficient for the claims made.
- **"No training curves or loss landscape analyses" and "No analysis of which samples benefit"**: Moved to Nice-to-Haves. These would strengthen the paper but are not core weaknesses.
- **"2.3 AP jump" criticism (ablation vs. test-dev)**: Removed because the critic compares numbers from different experimental configurations (val2017 with auxiliary modules vs. test-dev without auxiliary modules, with multi-scale training). The numbers are from different settings and are not directly comparable. The critic's core concern (lack of own baseline on test-dev) is retained as a Major weakness but the specific numerical claim is misleading.
- **"Abstraction/Introduction overstate contributions"** — The specific claim about prior work "failing to focus on difficult samples" was retained as a Major weakness (point 3), but the more general claim that "the paper is overstated" without specific anchoring is removed as too vague.
- **Strength Finder's "hyperparameter sensitivity is thoroughly documented"** — removed as it partially conflicts with the verified weakness about the lack of CF-vs-RCI isolation. The tables do exist but only show single-parameter sweeps without isolating all components.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely affirm each other on the paper's central tension: the core idea (cross-task inconsistency modeling via a residual module) is genuinely interesting and produces measurable gains, but the presentation and experimental framing fall short of the clarity needed to confidently attribute those gains to the claimed mechanisms. The reviews do not surface any hidden issue that the paper itself does not already implicitly acknowledge through its experimental design.

## Suggestions

1. **Rewrite the method section with full mathematical precision.** Define every variable before first use, fix the "RIC" typo, disambiguate Eq. (4), define $tb$ and $cb$ in Eq. (8), and fix the $\mu$/$\gamma$ labeling in Table hcrac‑2. The community should be able to implement the loss from the text alone.

2. **Run FCOS+ATSS on COCO test-dev under the identical pipeline** and report that baseline alongside the HCRAL result in Table 7, so readers can see the within-pipeline gain rather than relying on cross-paper comparisons.

3. **Add two missing ablations**: (a) baseline + RCI only (no CF), (b) baseline + CF only (no RCI), to disentangle the claimed mechanisms.

4. **Provide a concrete specification of the EATSS ranking function** in Algorithm 1 — what is the exact formula combining distance and IoU? What does "satisfying the maximum distance" mean operationally?

5. **Report standard deviations** over at least 3 seeds for the main ablation results (Table 6) and the generalization tables (hcrac‑loss, hcrar‑loss), especially where gains are ≤0.5 AP.

6. **Add a small analysis (even a figure) showing sample weights** under HCRAL vs. GFL/VFL to support the claim that prior work fails on difficult samples with similar IoU — or remove that claim from the Introduction.
