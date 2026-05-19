Now let me run calibration searches to score this paper.Now I have sufficient information to write the final review. Let me synthesize the findings.

---

## Summary

This paper demonstrates that sparse autoencoders (SAEs) can be used to decompose task vectors—residual-stream directions mediating in-context learning (ICL)—into sparse, interpretable components. The authors introduce the **Task Vector Cleaning (TVC)** algorithm to overcome the OOD limitation of naively reconstructing task vectors with SAEs, discovering "task-execution features" that causally induce specific tasks zero-shot. They also adapt the Sparse Feature Circuits (SFC) methodology of Marks et al. (2024) to the much larger Gemma-1 2B model (30× parameter increase) and to ICL tasks, which leads to the discovery of a second circuit family: "task-detection features" that activate on completed task tokens and are causally linked to execution features through attention and MLP.

---

## Strengths

- **TVC algorithm solves a genuine OOD problem** (Section 3.1): Task vectors are out-of-distribution for SAEs (they average residual streams rather than representing a single position), causing naive reconstruction and ITO to fail. TVC's optimization-based approach reduces mean L0 to fewer than 4 SAE features while preserving task-vector steering performance up to layer 14 (Figure 3a), a non-trivial result given prior methods required L0≥5 before performance degraded. The paper also reports 50–80% feature reduction across Gemma-2 2B and 9B, suggesting the method is not model-specific.

- **Causal validation via steering heatmaps** (Section 3.2, Figure 5): The diagonal structure of the steering heatmap—where an executor feature for antonyms improves loss on the antonym task but not on unrelated tasks—goes beyond correlation: it shows that individual SAE features causally encode task-specific information. The finding that translation tasks partially share a generic "English-to-foreign" executor feature, requiring a separate language-encoding feature, is a mechanistically interpretable and non-obvious result.

- **Meaningful adaptation of SFC to a 30× larger model and more complex task** (Section 4.1): The paper introduces token-position categorization for structured ICL prompts and a loss modification (averaging over non-first pairs) that amplifies the task-solving circuit relative to copying circuits. The faithfulness evaluation (Figure 6) shows that fewer than 1000 nodes ablated reduces faithfulness to 0.5 for the target task while leaving other tasks largely intact—demonstrating task-specific circuit discovery at scale.

- **Discovery of task-detection features as a new circuit component** (Section 4.2, Figure 7–8): SFC identifies a second feature family that activates on completed task output tokens (earlier in the prompt than execution features), is task-specific in its steering effect (Figure 7), and causally suppresses execution feature activations when ablated (Figure 8). This is a novel mechanistic observation not present in Todd et al. or Hendel et al.'s task-vector accounts.

---

## Weaknesses

### Fatal
None.

### Major

- **Potential circularity between TVC optimization and evaluation** — TVC Step 2 (Section 3.1) optimizes θ by steering zero-shot prompts and minimizing negative log-likelihood loss. Figure 3a then evaluates methods by measuring "relative log-likelihood loss improvement" when steering zero-shot prompts. The paper does not specify whether the optimization batch and the evaluation batch are separate; if they are drawn from the same distribution with no held-out split, TVC's improvement over ITO in Figure 3a reflects in-distribution fitting rather than a genuine generalization advantage. This is the central methodological concern: the paper may be correct that TVC is better, but the experimental design as written does not establish it. A brief clarification—even a sentence confirming hold-out evaluation—would substantially change the evidential weight of Figure 3a.

### Minor

- **Unusual intervention design in the detection-execution causal analysis** (Section 4.2): The causal connection between detection and execution features is assessed by ablating "detection directions while fixing attention patterns." Normally, attention patterns are computed from representations, so fixing them decouples the signal from its natural propagation pathway. This makes the intervention informative as a direction-level ablation, but it does not cleanly demonstrate a causal pathway *through* the attention layer as claimed in the abstract ("connected to task execution features through attention output and transcoder nodes"). The paper could clarify what pathway the intervention is intended to isolate.

- **Two anomalous tasks in Figure 8 are unexplained** (Section 4.2): "Person profession" and "present simple gerund" show unexpectedly weak detection-execution connections. The paper notes this "warrants further investigation" but offers no hypothesis. Given that the paper's core claim is a consistent two-family ICL circuit, unexplained exceptions that form ~20% of the tested tasks are worth more discussion than a sentence.

- **Acknowledged incompleteness of the causal story** (Section 6): The paper admits that "the succeeding MLP is necessary to capture the full effect" but MLP transcoder features are not characterized. The circuit described in Section 4.2 is therefore incomplete by the authors' own account, and the detection-to-execution pathway goes through a black-box MLP.

- **Two tasks excluded from Figure 6** (Section 4.1.3): "Person profession" and "football player position" are excluded because the small non-ablated vs. ablated loss difference makes faithfulness unstable. The paper attributes this to the modified loss function, which is partially reassuring, but the conclusion that "circuits are largely task-specific" rests on the subset of tasks where the method produces clean results. This boundary condition deserves acknowledgment in the main claim.

### Trivial

- The claim that ICL is "significantly more complex and important than other behaviors commonly studied in circuit analysis (such as IOI)" (Section 1) is not qualified against the specific experimental setup used (structured antonym/translation prompts with fixed format). While likely true of ICL in general, as applied here the complexity comparison is not established.

---

## Nice-to-Haves

- A held-out evaluation split for TVC (or explicit confirmation that one exists) would transform the Figure 3a results from suggestive to conclusive.
- Error bars or variance across tasks/prompts in the steering heatmaps (Figures 5, 7, 8) would help calibrate whether a few tasks drive aggregate results.
- A matched ITO-at-L0=4 ablation in Figure 3a, even as a single point, would cleanly isolate TVC's advantage over the optimization procedure rather than just sparsity level.
- The Gemma-2 2B/9B generalization result (50–80% feature reduction) is currently a single sentence in Section 3.1 with no figure; it deserves a brief visualization since it is evidence that TVC scales beyond the main experimental model.
- A more substantive comparison with Wang et al.'s "label words" concept (currently a parenthetical in related work) would sharpen the novelty claim for Section 4.2's task-detection features.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"TVC algorithm is incompletely specified — Step 1 is absent from the main text"**: The paper explicitly references "Figure 10" (appendix) for the full algorithm overview (lines 95, 120). The apparent gap in the parsed text is a PDF parser artifact — images embedded in the prose are not rendered as text. Per the review policy, missing appendix content from the parser is not an author error. Removed.

- **"ITO at L0=4 not shown, making the comparison asymmetric"**: TVC achieves L0<4 while ITO at L0=5 already degrades performance relative to TVC. The comparison asymmetry actually *disfavors* TVC (ITO has more features), which is explicitly allowed under the hard rule ("REMOVE weaknesses about unfair comparison if the asymmetry favors the baseline"). Removed.

- **"Task-specificity of executor features is circular because TVC was optimized per-task"**: The diagonal structure in Figure 5 shows that features extracted for Task A do *not* steer Task B. This is a genuine causal finding, not a tautology. TVC being per-task means it finds features relevant to that task, but the non-effect on other tasks is independent information. Removed.

- **"Reproducibility: JAX libraries not released yet"**: Per review policy, nitpicks about unreleased large artifacts are removed. The paper commits to release upon acceptance, which is standard. Removed.

---

## Novel Insights

The paper's most genuinely novel contribution beyond applying known tools is the two-family decomposition of ICL: execution features (activating on arrows, encoding task identity causally) and detection features (activating on output tokens, detecting completed tasks earlier in the prompt). That these two families are causally linked through attention—and that TVC can extract *both* from sparse decompositions of task vectors at different layers (layer 12 for execution, layer 11 for detection)—constitutes a richer and more precise mechanistic account of ICL than any prior task-vector work. The finding that translation tasks share execution features while requiring separate language-encoding features, forming a compositional encoding scheme, is an unexpected and interpretable result that goes beyond the binary "task vector present/absent" framing.

---

## Suggestions

1. Add a sentence in Section 3.1 explicitly stating whether TVC optimization and Figure 3a evaluation use the same or different prompt batches.
2. Justify the "fixing attention patterns" intervention in Section 4.2 with a brief explanation of what causal pathway it is intended to isolate.
3. Discuss the two anomalous tasks in Figure 8 with at least a hypothesis (e.g., whether detection and execution features are at different layers for those tasks, or whether a different feature pairing explains the result).
4. Promote the Gemma-2 generalization result to a figure or table rather than a prose mention, given its importance for the generalizability claim.

---

## Score Calibration

**Round 1 bracket:** Based on weak anchors (2.5–3.0), middle anchors (4.0–7.0), and strong anchors (8.0–9.0), the paper plausibly sits between **5 and 7**.

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `Wxl0JMgDoU.md` (Chess/SAE) | 2.5 | 1 | Much weaker — narrow application, no novel method |
| `9ca9eHNrdH.md` (SAE Canonical Units) | 7.0 | 1 | Comparable topic; that paper has cleaner methodology, stronger conclusions |
| `I4e82CIDxv.md` (Sparse Feature Circuits original) | 8.0 | 1 | Stronger — the founding paper being extended; more complete methodology and downstream applications |
| `1Njl73JKjB.md` (Principled SAE Evaluations) | 7.0 | 1 | Comparable scope; more principled evaluation but smaller model |
| `xizpnYNvQq.md` (Revisiting ICL circuit) | 6.5 | 2 | Similar topic (ICL mechanism); this paper has more novel methodology and causal validation |
| `YPIA7bgd5y.md` (ICL label relationships) | 6.5 | 2 | Less methodologically novel; no SAE or circuit analysis |
| `0ULf242ApE.md` (Concept encoding ICL) | 6.0 | 2 | Comparable depth of ICL mechanistic study; similar methodological quality |
| `vc1i3a4O99.md` (MI-based SAE explanations) | 5.0 | 2 | Narrower SAE application, less causal rigor; clearly weaker |
| `5lIXRf8Lnw.md` (Auto-interpreting SAE features) | 5.5 | 2 | Applied SAE pipeline; no circuit discovery or causal validation |

**Round 2 narrowing**: Within the 5–7 bracket, the paper compares favorably to the 6.0–6.5 ICL papers (more novel methodology, genuine TVC contribution, SFC scaling), but falls short of 7.0 (Principled SAE Evaluations, SAE Canonical Units) due to the circularity concern, incomplete causal story, and unexplained anomalies. The paper is closer to the upper end of the 6.0–6.5 range than to 7.0.

**Final score: 6.0** — Borderline Accept. The three concrete contributions (TVC, SFC scaling, task-detection feature discovery) justify acceptance, while the circularity concern in TVC evaluation and the incomplete causal story prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>