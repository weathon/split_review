Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper introduces 3D Intention Grounding (3D-IG), a new task where AI agents must detect 3D objects from human intention text (e.g., "I want something to support my back") rather than from explicit referential language. The authors construct the Intent3D dataset (44,990 intention texts across 209 classes from 1,042 ScanNet scenes), establish baselines covering expert, foundation, and LLM-based models, and propose IntentNet — a method featuring Verb-Object Alignment, Candidate Box Matching, and Cascaded Adaptive Learning. IntentNet achieves substantial improvements over all baselines (e.g., +11.22% Top1-Acc@0.25 on the val set).

## Strengths

1. **Novel task formulation with clear practical motivation.** The paper identifies a genuine gap: existing 3D-VG requires users to articulate a *reference* (naming the object or its location), which is infeasible for assistive AI scenarios (visually impaired users, hands-free interaction, etc.). 3D-IG repositions the AI from reference-follower to intention-interpreter, which is both intellectually distinct and practically relevant.

2. **Large, linguistically diverse benchmark dataset (Intent3D).** The dataset contains 44,990 texts, 1,568 distinct verbs, 2,894 distinct nouns, and 209 fine-grained classes — a substantial resource. The prompt design (Prompt-1) explicitly instructs ChatGPT to avoid category/location/attribute leakage, and the filtering criteria (common, non-trivial, unambiguous objects) are reasonable design choices for a first benchmark.

3. **IntentNet significantly outperforms all baselines.** Across both val and test sets, IntentNet achieves large and consistent margins over the second-best method (e.g., 58.34 vs. 47.12 Top1-Acc@0.25 on val, 25.36 vs. 19.93 AP@0.5). The gains are substantial (10+ points on some metrics) and hold across diverse baselines.

4. **Comprehensive baseline coverage.** The paper evaluates expert models (BUTD-DETR, EDA), a foundation model (3D-VisTA), and an LLM-based model (Chat-3D-v2) under multiple settings (from scratch, fine-tune, zero-shot), providing a clear picture of where existing approaches fail on intention grounding.

5. **Clear ablation evidence for core components.** The ablation study (Table 4) and qualitative visualizations (Figure 5) consistently show that removing any component degrades performance, with the Verb-Object Alignment component having the largest individual impact (53.09 → 58.34 Top1-Acc@0.25).

## Weaknesses

### Fatal

None.

### Major

1. **No controlled detector comparison across baselines.** BUTD-DETR and IntentNet use GroupFree, 3D-VisTA uses Mask3D, and Chat-3D-v2 uses PointGroup. While the paper acknowledges this (Section 5.1, lines 316–317) and notes that GroupFree is *less* powerful than Mask3D, the absence of a controlled study (same detector across all methods) means the reported performance gaps conflate the effect of the novel components with detector quality. A controlled experiment would considerably strengthen the claims.

2. **Baseline adaptation details are under-specified.** BUTD-DETR and EDA were designed for single-target grounding. The paper states they were trained "using all ground truth boxes for all target instances" (line 242) following "their configuration on ScanRefer" (line 258), but does not describe how the models were adapted for multi-instance detection — matching strategy, number of queries, loss weighting, or any architectural changes. Since the entire quantitative story rests on outperforming these baselines, the lack of transparency on adaptation details is a meaningful reproducibility concern.

3. **No empirical verification that intentions avoid category leakage.** The prompt design (Prompt-1) is well-motivated, but the paper provides no analysis showing that ChatGPT's generated intentions genuinely conceal the target category. A human baseline (e.g., asking annotators to infer the object category from the intention text alone) would be straightforward and would build confidence that the task requires genuine reasoning rather than being reducible to category prediction + standard 3D detection. Without this, the claimed difficulty of 3D-IG is partially unsubstantiated.

### Minor

1. **Cascaded Adaptive Learning motivation vs. mechanism mismatch.** The paper states that higher-priority losses (e.g., \(L_{vPos}\)) should be minimized before lower-priority ones. However, the mechanism — \(Loss_B = Loss_B \times (\text{sigmoid}(Loss_A) + 0.5)\) — amplifies \(Loss_B\) when \(Loss_A\) is large (not yet converged), which actually increases the gradient contribution from the lower-priority loss while the higher-priority loss is still large. This does not clearly realize the claimed "cascaded priority" logic. The ablation shows a positive effect (+1.0 Top1-Acc@0.25), so the mechanism likely helps with loss balancing, but the motivation needs clarification or correction. A comparison against simpler alternatives (equal weighting, linear scheduling, sequential warmup) would help.

2. **Ablation (Table 4) only reports Top1-Acc, not AP.** Top1-Acc evaluates only the highest-confidence prediction, which is a weak signal for multi-instance detection (a scene with 5 monitors gets full credit for detecting 1). The main results tables include AP, making its absence in the ablation noticeable. No standard deviations are reported for any metric, making it difficult to assess whether small differences (e.g., 57.87 vs. 58.34) are significant.

3. **Data cleaning process under-specified.** The paper reports manually filtering gibberish, recreating sentences, and regenerating repeated texts (line 114), but provides no counts, no inter-annotator agreement, and no guidelines for what constitutes "correct" intention sentences. The "Unambiguous objects" criterion (line 89) — objects that "serve similar human intentions" are filtered — potentially removes the most interesting ambiguous cases. These details matter for a dataset that is a core contribution.

### Trivial

None.

## Nice-to-Haves

- A controlled detector experiment (using GroupFree for all methods) to isolate the effect of the grounding/alignment innovations from detector quality.
- A human baseline study: show annotators only the intention text and ask them to predict the object category, demonstrating the task is not trivially solvable.
- Standard deviations or confidence intervals in the ablation table.
- Reporting AP@0.25 and AP@0.5 in the ablation study alongside Top1-Acc.
- Failure case analysis categorizing errors (intention misclassification vs. detection failure vs. localization error).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Cascaded Adaptive Learning does the opposite of what's claimed"** — The critic's mathematical observation that `sigmoid(Loss_A)` amplifies `Loss_B` when `Loss_A` is large is technically correct, but this does *not* "contradict" the stated logic entirely. An alternative reading is that the mechanism prevents any single loss from dominating by ensuring balanced gradient signals across all objectives. The paper's motivation could be clearer, but the mechanism is not contradictory — it may be implementing a form of loss balancing under a different framing. Moved here because the critic's categorical claim of contradiction is too strong.

2. **"The zero-shot Chat-3D-v2 results are near floor, suggesting the evaluation protocol is particularly unfavorable"** — This is speculative. Zero-shot performance on a novel task with a different text format would naturally be near floor. The evaluation protocol (Softmax on logits, product aggregation) is a standard way to extract confidence from autoregressive models. No evidence is provided that it underestimates capability.

3. **"The paper's claim that 3D-IG automates observation and reasoning that humans perform in 3D-VG is misleading"** — The paper's framing is reasonable. In 3D-VG, the text explicitly names or locates the object; in 3D-IG it does not. The claim that 3D-IG requires automation of reasoning that humans must do in 3D-VG is an accurate description of the task difference, not misleading.

4. **"EDA's underperformance relative to BUTD-DETR is 'suspicious'"** — The paper provides a clear, plausible explanation: EDA's attribute-alignment losses are designed for referential language and actively misguide the model on intention texts. This is a reasonable analysis, not speculation. The observation itself is interesting but not evidence of a flaw.

## Novel Insights

The most revealing finding in this work is that **stronger 3D-VG models actually perform worse on 3D-IG**: EDA (current 3D-VG SOTA) scores 43.11 vs. BUTD-DETR's 47.12 on Top1-Acc@0.25. This inversion supports the paper's central thesis that referential grounding and intention grounding require fundamentally different capabilities — specifically that the attribute-level alignment which makes EDA strong for references actively harms performance when the language is non-referential. This validates the motivation for new task-specific designs rather than simply porting 3D-VG methods. Additionally, the large gap between the best baseline (BUTD-DETR, 47.12) and IntentNet (58.34) suggests that explicit modeling of verb-object structure (the component with the largest ablation effect, +5.25) is the key bottleneck — not 3D perception quality or text encoding power alone.

## Suggestions

1. Add a controlled experiment using GroupFree as the detector for all baselines to rule out detector quality as a confound.
2. Conduct and report a human baseline where annotators infer the object category from intention texts alone — this directly validates whether the task requires genuine reasoning.
3. Clarify the motivation for Cascaded Adaptive Learning (or rename it if the mechanism is better described as loss balancing rather than cascaded priority), and compare against simpler alternatives (e.g., equal weighting, linear scheduling).
4. Report AP metrics and standard deviations in the ablation table, and include more detail on the data cleaning process (counts of filtered/regenerated texts, inter-annotator metrics).
5. The Verb-Object Alignment is clearly the most impactful component — consider a more detailed analysis of this module (attention maps over verbs vs. objects, ablation of the three sub-losses \(L_{vPos}, L_{vSem}, L_{voSem}\) individually).

## Score and Decision

The paper introduces a genuinely new task that addresses a practical gap in 3D understanding, provides a substantial dataset, and proposes a method with clear empirical gains. The major weaknesses — lack of controlled detector comparison, under-specified baseline adaptation, and no information leakage analysis — are addressable in revision and do not invalidate the core contribution. The strength of the empirical results (10+ point gains) and the conceptual novelty of the task outweigh these concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>