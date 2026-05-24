Now I have sufficient calibration data. Let me write the consolidated review.

**Round 1 bracket:** The paper clearly sits in the middle band (avg 3.5–7.5). It is substantially stronger than the low-band anchors (2.6–3.4) which were withdrawn/rejected papers with unclear or narrow contributions, and substantially weaker than the high-band anchors (7.75–9.0, e.g., Sparse Feature Circuits at 8.0 / Oral) which introduced foundational methodology that this paper builds on.

**Round 2 narrowing within (3.5, 7.5):** Compared to "From Context to Concept" (avg 6.0, Reject) — which was criticized for largely replicating findings from Todd et al./Hendel et al. — the current paper has significantly more novelty (TVC algorithm, SAE-specific feature families, causal circuit analysis). Compared to "Principled Evaluations" (avg 7.0, Accept Poster) and "Switch SAEs" (avg 7.0, Accept Poster), the current paper has less cleanly-defined contributions and more schematic results. Compared to "Rethinking Evaluation of SAEs" (avg 5.75, Accept Poster), the current paper is slightly stronger in breadth and novelty.

The paper's score should sit between the "From Context to Concept" anchor (6.0) and the "Principled Evaluations" anchor (7.0). I anchor it at 6.5 — it has genuine contributions that advance the state of the art in SAE-based circuit analysis, but has notable framing and completeness issues.

---

## Summary

This paper uses sparse autoencoders (SAEs) to study the mechanism behind in-context learning (ICL) in Gemma-1 2B. It introduces **Task Vector Cleaning (TVC)**, an algorithm that decomposes task vectors into a sparse combination of SAE features while preserving task performance (L0 < 4). Using TVC, the paper identifies two causally implicated feature families: **task-execution features** (activating on arrow tokens, directly inducing task behavior) and **task-detection features** (activating on output tokens, detecting completed task instances). The paper further adapts Sparse Feature Circuits (SFC) to the ICL setting, showing that detection features are causally linked to execution features through attention and MLP layers. The main contributions are: (1) the TVC algorithm, (2) discovery of two feature families in the ICL circuit, and (3) successful scaling of SFC to a 2B-parameter model.

## Strengths

- **Novel Task Vector Cleaning algorithm (TVC):** TVC is a well-motivated algorithmic contribution that decomposes task vectors into sparse SAE feature combinations (L0 < 4) while maintaining or improving task-vector performance. The paper clearly demonstrates (Figure 3a/b) that TVC outperforms naive SAE reconstruction and inference-time optimization baselines across layers, reducing active SAE features substantially. This addresses a real problem — task vectors are out-of-distribution for SAEs — and the solution is transformer-specific and non-obvious.

- **Discovery and causal linking of two distinct feature families:** The paper identifies task-execution features (89.8% activation mass on arrow tokens, Table 1) and task-detection features (96.76% activation mass on output tokens, Table 2), and provides evidence for a causal detection→attention→execution circuit (Figure 8). The steering experiments (Figures 5, 7) confirm task-specificity — most features affect exactly one task, with interpretable groupings (e.g., translation tasks sharing a generic executor). This goes beyond the task-vector view by showing that ICL involves at least two functionally distinct feature types.

- **Successful adaptation and scaling of SFC to a more complex behavior and larger model:** The paper adapts Sparse Feature Circuits (Marks et al., 2024) to work on Gemma-1 2B (10–35× the parameters of prior circuit-style studies) and to structured ICL prompts. The modifications (token-position categorization, multi-pair loss function) are sensible and the faithfulness ablation analysis (Figure 6) shows that the discovered circuits are task-specific and that ablating a few hundred nodes reduces faithfulness by 0.5 for the target task while leaving unrelated tasks largely intact.

- **Interpretable max-activating examples and activation-mass analysis support the feature interpretations:** The paper provides concrete examples (Figure 4) of executor features' max-activating patterns (e.g., activating on "and" in "hot and cold"), which align with the hypothesized role of recognizing task context. The activation-mass breakdowns (Tables 1, 2) cleanly separate executor features (arrow tokens) from detection features (output tokens).

## Weaknesses

### Fatal
None.

### Major

- **The claimed ICL circuit is schematic and incomplete.** The paper identifies that detection features (layer 11) connect to execution features (layer 12) through attention and MLP layers, but does not specify which attention heads, which layers, or how MLP features integrate. Figure 1 is a high-level diagram without named components. The causal connection experiment (Figure 8) shows effect strengths on a 0–0.5 scale where many entries are below 0.3. The paper's own limitations section (line 345) acknowledges that "the succeeding MLP is necessary to capture the full effect." This means the claimed circuit is partially observed rather than fully reconstructed — key components are missing. The concluding claim that this work explains ICL "in greater detail than any prior mechanistic interpretability work" (line 349) is overstated given the schematic nature of the circuit compared to the detailed component-level analyses in, e.g., Wang et al. (2022) or Marks et al. (2024).

- **The TVC algorithm uses supervised task loss, which tempers the SAE-centric narrative.** The paper's framing emphasizes that SAEs "enable" the discovery of interpretable ICL features, but the initial SAE decomposition of task vectors fails (producing >10 noisy features). TVC then optimizes feature weights using the supervised zero-shot task loss. This is presented honestly in the paper (lines 108–112), but the abstract and introduction create the impression that SAEs alone suffice (e.g., "task vectors are well approximated by a sparse sum of SAE latents" — true only after TVC). The paper would benefit from more explicitly distinguishing between what SAEs provide (the feature dictionary) and what the supervised TVC step adds (identifying which features matter for the task).

### Minor

- **Insufficient comparison with closely related prior ICL work in the main text.** The paper mentions Wang et al. in the related work section (line 339) — noting that it "investigates a simple ICL classification task and finds similar results with different terminology" — and defers detailed comparison to Appendix H (stripped). Without this comparison in the main paper, it is unclear whether the task-detection features correspond to Wang et al.'s "label words" or whether the present work's findings generalize beyond or differ substantially from this prior result. The paper should at minimum summarize the differences in the main body.

- **Detection feature extraction process at layer 11 is underspecified in the main text.** The paper states (line 299): "We applied our task vector cleaning algorithm to extract task-detection features, identifying layer 11 as optimal for steering." But TVC requires a target task vector — it is not explained how a task vector is obtained at layer 11 (task vectors were shown at layer 12 for executor features). The details are deferred to Appendix G, but the main paper should provide at least a sketch of how task vectors at different layers are computed and why layer 11 is the optimal detection layer.

- **The paper does not quantify the number of nodes ablated to reach 0.5 faithfulness per task.** The text says "disabling just a few hundred nodes" (line 287) is sufficient, but does not report per-task counts or the spread. Without this, it is hard to assess whether the circuit is truly sparse uniformly across tasks or whether there is high variance.

- **The steering effect threshold for "causally implicated" is not defined.** The heatmaps (Figures 5, 7) show a continuous effect scale (0–1.0/0.8 for steering, 0–0.5 for detection→execution), but the paper does not state what threshold qualifies as meaningful causal involvement. Many entries are in the 0.2–0.5 range; without a criterion, interpretation is subjective.

- **Two tasks excluded from faithfulness analysis without explanation of broader impact.** The paper notes (lines 295–296) that person_profession and football_player_position were excluded from Figure 6 due to unstable faithfulness, but does not discuss whether this indicates a limitation of the SFC adaptation for certain task types.

### Trivial

- Figure 3(a) caption could clarify that negative loss change = improvement (lower loss is better) and confirm the baseline is the unsteered model.
- The task names in Figure 5 are garbled by extraction; the authors should ensure clean rendering.

## Nice-to-Haves

- A concrete circuit for at least one task naming specific attention heads (e.g., "detection features at layer 11 are read by attention head L11H5, which writes to layer 12, activating executor feature X") would substantially increase impact.
- Statistical significance measures (error bars, confidence intervals) for steering and ablation results would strengthen the causal claims.
- A comparison of TVC features with features found by a purely unsupervised method (e.g., clustering SAE activations during ICL) would help validate that TVC features correspond to coherent, naturally-occurring units.

## Removed Points

- **Criticism that TVC being supervised undermines the paper's core contribution (Harsh Critic Point 1):** The paper is transparent about the need for TVC (lines 108–112: "several of our initial naive approaches faced significant challenges… we developed a novel method"). TVC is presented as a contribution, not a hidden limitation. The paper does not claim SAEs alone perform the decomposition — it claims SAE features, once identified through TVC, encode task information, which is supported by the evidence. Removed because the paper already addresses this.
- **Criticism that evaluation is limited to a single model (Harsh Critic Point 4):** The main paper (line 196) explicitly mentions sweeps on Gemma 2 2B and 9B with results in Appendix D.1. The 50–80% reduction claim appears in the main text at line 197. TVC optimizing on zero-shot prompts is by design (task vectors are used for zero-shot steering). Removed because it misreads the paper's claims.
- **Strength about open-sourced code:** The paper mentions releasing SAE weights and a JAX codebase (line 349, in the removed "Rest of paper" section). While we accept this as stated, this is a forward-looking statement rather than a demonstrated strength. Moved here.
- **Generic/filler strengths from Strength Finder about the paper addressing an important problem:** Removed as too generic.

## Novel Insights

The most insightful observation from the reviews is the tension between the paper's SAE-centric framing and the actual need for supervised refinement (TVC). This tension is not unique to this paper — it reflects a broader question in mechanistic interpretability about whether SAE features are directly interpretable for a given behavior or whether they require task-specific filtering. The paper could be stronger by explicitly addressing this as a design choice: SAEs provide a universal feature dictionary, but task-specific circuits require supervised pruning. This framing would better position TVC as necessary rather than an indication of SAE insufficiency.

## Suggestions

1. Add a 1-paragraph summary of the relationship with Wang et al. in Section 4.2 or the related work, explicitly stating whether task-detection features correspond to their "label words" and what the present work adds.
2. Specify how detection features are extracted at layer 11 (how a task vector at that layer is obtained, or how TVC is applied without a layer-11 task vector). Even a brief sketch would resolve a major ambiguity.
3. Tone down the concluding claim ("greater detail than any prior mechanistic interpretability work") to reflect the schematic nature of the circuit, e.g., "greater detail than prior work on ICL mechanisms specifically" or "a more detailed SAE-based account of the ICL circuit."
4. Report per-task node counts for reaching 0.5 faithfulness, or at minimum the range observed across tasks.
5. Add a discussion of why person_profession and present_simple_gerund show weak detection→execution connections (Figure 8) — is this a property of the tasks or a limitation of the method?

## Score and Decision

**Calibration anchors used:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Sparse Feature Circuits (I4e82CIDxv) | 8.0 | R1 high | Foundational paper this work builds on; significantly stronger in clarity and completeness |
| Scaling and evaluating SAEs (tcsZt9ZNKD) | 8.2 | R1 high | SAE architecture scaling paper; much cleaner evaluation |
| Towards Principled Evaluations (1Njl73JKjB) | 7.0 | R1 mid / R2 | Cleaner evaluation methodology; current paper is weaker on evaluation rigor |
| Efficient Dictionary Learning (k2ZVAzVeMP) | 7.0 | R2 | Cleaner architectural contribution with strong evaluations |
| From Context to Concept (0ULf242ApE) | 6.0 | R2 | Similar ICL topic; current paper has more novelty (TVC, SAE features) |
| Rethinking Evaluation of SAEs (HpUs2EXjOl) | 5.75 | R2 | Comparable in contribution level; current paper slightly broader |
| SAGE (sknUS8X9q0) | 4.0 | R1 mid | Weaker presentation and unclear contributions |
| Compute Optimal Inference (ghH6YYDs15) | 4.67 | R1 mid | Theoretical SAE analysis; different type of contribution |
| Automatically Identifying Circuits (89wVrywsIy) | 3.4 | R1 low | Withdrawn; current paper is substantially stronger |

**Round 1 bracket:** Initial bracketing placed the paper between 3.5 and 7.5, which was correct. The paper is clearly stronger than the low-band anchors (unclear contributions, withdrawn papers) and clearly weaker than the high-band anchors (foundational methodological papers with oral-level acceptance).

**Round 2 narrowing:** Within the (3.5, 7.5) band, comparison with "From Context to Concept" (6.0, Reject — novelty concerns) and "Principled Evaluations" (7.0, Accept Poster — clean methodology) narrowed the range to [5.75, 7.0]. The paper is stronger than the former (more novelty) but weaker than the latter (messier claims, schematic circuit). I anchor at 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>