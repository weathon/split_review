Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes Hierarchical Multi-Grained Reasoning (HGR) for Object Concept Learning (OCL), tackling the many-to-many mapping between objects and their attributes/affordances. The method consists of two main components: (1) a coarse-to-fine hierarchical reasoning module that uses learnable prompts to progressively localize concept-relevant information, and (2) a counterfactual relation-enhancing module that models causal links between attributes and affordances via a graph neural network and counterfactual loss. Experiments on OCL, NYUd2, and AGD20K benchmarks show consistent improvements over prior methods.

---

## Strengths

1. **Principled framing of OCL as a many-to-many mapping problem with a reasoning-based solution.** The paper clearly identifies why discriminative methods fall short for OCL — an object can have multiple concepts and a concept can belong to multiple objects — and motivates a coarse-to-fine reasoning mechanism as a principled alternative. (Abstract, Section 1)

2. **Novel coarse-to-fine hierarchical prompting mechanism that progressively localizes concept-relevant information.** The two-stage prompt generation (global contextual prompting → instance-specific fine-grained prompting) is well-motivated, and the ablation in Table 5 confirms that both stages are necessary: global context alone or instance-only prompts both underperform the full hierarchy. Figure 3's heatmaps provide visual evidence of progressive focus. (Section 3.1, Table 5, Figure 3)

3. **Counterfactual relation-enhancing module that explicitly models causal links between attributes and affordances.** The concept connection network with graph-based reasoning and the counterfactual loss is a novel contribution that targets a genuine challenge in OCL — leveraging known causal relationships to improve reasoning. The ablation (Table 4, CCC component) shows clear gains from this module. (Section 3.2.2, Table 4)

4. **Consistent SOTA results across three diverse benchmarks.** HGR achieves significant gains over prior methods on OCL (8.1% attribute mAP, 3.9% affordance mAP over Li et al. 2023b), NYUd2, and AGD20K, demonstrating generalization across tasks. (Tables 1–3)

5. **Comprehensive ablation studies isolating each component's contribution.** Table 4 cleanly decomposes the contributions of coarse-to-fine reasoning (CHR), prompt-guided concept extraction (PVCE), and counterfactual connection (CCC), showing each module is necessary. (Table 4, Section 4.2)

---

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by evidence, and the identified issues are addressable without invalidating the contribution.

### Minor

1. **Incompletely specified counterfactual loss (Eq. 9).** The loss is written as `L_cl = { max{0, γ - (ŷ_β - ŷ_βmask)}, β_i = 1` with only one case shown. The text states "We design two loss function L_cl according to the different affordance label to promise the L_cl should be a positive value," but the second case (presumably for β_i = 0) is never written. While the general intent is inferable, this incomplete specification hurts reproducibility and makes the causal learning claim harder to fully verify. **The authors must provide the complete loss definition.**

2. **Ground-truth bounding box dependency not acknowledged as a limitation.** The fine-grained prompt formation (Section 3.1.2) uses ground-truth bounding boxes to crop objects. This is a practical assumption that narrows the method's applicability in real-world / embodied settings where boxes are unavailable. The limitations section (Section 5) is generic and does not discuss this dependency or evaluate a variant without ground-truth boxes (e.g., using a detector). This should be acknowledged and ideally ablated.

3. **Baseline comparability could be more rigorous.** The primary baselines from Li et al. (2023b) (DM-V, DM-α→β, DM-att, OCRN) may use different visual backbones (e.g., ResNet) than HGR's CLIP encoder. The inclusion of Vanilla CLIP partially addresses this — and the fact that Vanilla CLIP is *worse* than OCRN on affordance (suggesting gains are architectural, not backbone-driven) helps — but re-implementing the strongest prior baseline (OCRN) with the same CLIP encoder would isolate the reasoning mechanism's contribution more convincingly.

4. **Analysis of concept count drop (k > 10) is shallow.** Figure 4 shows a clear peak at k=10, but the explanation ("too many concepts increase complexity and influence accuracy and stability") does not distinguish between overfitting, insufficient training data for rare concepts, or optimization difficulty. A brief diagnostic (e.g., training loss behavior, concept utilization statistics) would strengthen the analysis.

### Trivial

- The paper states "multiple counterfactual samples are selected" but the method masks attribute prompts during training rather than selecting or generating counterfactual images. The phrasing should be aligned with what the method actually does (counterfactual prompting / masking, not counterfactual sample selection).

---

## Nice-to-Haves

- A finer-grained ablation separating the global contextual prompt from the instance-level prompt in the coarse-to-fine reasoning module (currently grouped as "CHR" in Table 4) would further clarify the contribution of each step.
- Reporting variance (error bars) over multiple runs would help assess the significance of the reported gains, particularly in Tables 2 where margins appear narrower.
- Providing the complete set of architectural hyperparameters (the specific CLIP encoder variant, the intermediate layer M used for F_M, the number of prompt tokens n, concept dimensions D, and the value of γ in the counterfactual loss) would aid reproducibility, though the main claims do not hinge on these.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unclear comparability of baselines (severe version)"** — The harsh critic framed this as a major evidential issue, but the paper already includes Vanilla CLIP as a baseline, showing it is worse than OCRN, which *strengthens* the argument that HGR's gains come from the reasoning architecture, not the backbone. The critic's own analysis undermines the severity of the claimed issue.
- **Missing implementation details (M, n, d, GRU hidden size, learning rate, optimizer, epochs)** — These are nitpicks about reproducibility that the instructions explicitly exclude.
- **"Garbled tables"** — This is a parser error, not a paper problem. Per instructions, formatting artifacts are removed.
- **"8.1% and 3.9% ambiguous (absolute vs. relative)"** — The paper clearly states "compared with state-of-the-art method (Li et al., 2023b)" and the metric (mAP) is standard; the comparison is unambiguous.
- **Related work discussion could be sharper** — Generic, not a substantive weakness.
- **"Coarse-to-fine prompting connection to related work could be sharper"** — Generic, not a substantive weakness.
- **Demand for error bars / statistical significance as a major weakness** — Single-run evaluation on large-scale benchmarks (185K instances) is the standard in this area; at most a nice-to-have.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not surface any novel observation about the paper's methodology or results that the authors themselves have not already made.

---

## Suggestions

1. **Complete the counterfactual loss specification** — Write both cases of Eq. 9 explicitly (for β_i=1 and β_i=0). Report the value of γ.
2. **Acknowledge the bounding-box dependency** in the limitations section and, if feasible, evaluate a variant that uses a detector at inference time or ablates the impact of imperfect boxes.
3. **Add a CLIP-backbone re-implementation of the strongest Li et al. (2023b) baseline** (OCRN) to fully isolate the reasoning mechanism's contribution from backbone effects.
4. **Provide a brief diagnostic for the k>10 performance drop** — e.g., per-concept frequency statistics, training loss curves, or concept utilization rates — to strengthen the analysis in Figure 4.
5. **Correct the phrasing** of "multiple counterfactual samples are selected" to reflect what the method actually does (attribute prompt masking).

---

## Score and Decision

This paper makes a solid contribution to OCL with a well-motivated reasoning framework, clean ablations, and strong empirical results across multiple benchmarks. The issues identified are addressable (loss specification, limitation acknowledgment) and do not threaten the core claims. The paper is ready for acceptance with minor revisions.

**Originality:** Good — the coarse-to-fine hierarchical prompting and counterfactual relation-enhancing are novel combinations for OCL.  
**Importance of research question:** High — OCL is relevant to embodied AI and moves beyond standard discriminative classification.  
**Claims support:** Claims are generally well-supported by ablations and consistent gains across three benchmarks.  
**Soundness of experiments:** Sound; the main concern is baseline backbone comparability, which is partially addressed.  
**Clarity of writing:** Generally clear; the loss function specification is the main gap.  
**Value to community:** Moderate — the method and ablation insights could inform future work on reasoning-based concept learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>