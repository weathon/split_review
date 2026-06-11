## Summary

This paper proposes the Fast and Slow Effect (FSE) framework and the Class Representation Index (CRI) metric for automatically evaluating whether LLM/VLM-generated concept annotations are sufficient—i.e., whether the textual concepts alone enable the model to re-identify the target class among semantically similar alternatives. The framework uses a five-stage hierarchical concept-gathering process and measures CRI under fast mode (direct visual classification) vs. slow mode (classification from textual concepts alone). Experiments across six models and five datasets show a consistent 25%+ CRI gap between fast and slow modes on fine-grained datasets, and the paper demonstrates that high downstream task accuracy (fused mode) can coexist with genuinely insufficient concept annotations, directly challenging the utility-as-proxy assumption.

## Strengths

- **Empirical refutation of the utility-as-proxy assumption (Table 4)**: Directly demonstrates that the fused mode (visual + textual concepts) achieves ~90% CRI while the slow mode (concepts alone) scores ~50% on the same data. This clean dissociation proves that end-to-end accuracy can mask insufficient annotations—a non-obvious and practically important result for the XAI community.

- **Consistent reversal of expected slow-mode superiority across model families (Table 2, Figure 3)**: The slow mode underperforms fast mode by 25–27% on average across all three fine-grained datasets, and this pattern holds across six models from three distinct families (GPT, Qwen, Llama), making the result robust rather than model-specific.

- **Fine-grained vs. coarse-grained dissociation (Table 3)**: On general datasets (CIFAR-100, Caltech-101), slow mode achieves CRI >90% and outperforms fast mode—the expected result. The same models underperform by 25%+ on fine-grained datasets, scoping the limitation precisely to the setting where XAI methods are most needed and ruling out a trivial "models are bad at text reasoning" explanation.

- **Methodologically principled distractor selection (Table 1)**: Demonstrates that random distractors yield 14–20% contradiction rates while semantically related distractors yield 34–45%, validating that the evaluation is genuinely challenging and avoiding ceiling effects.

## Weaknesses

### Fatal
None.

### Major

1. **The evaluator is the same model as the annotator, conflating concept insufficiency with reasoning inconsistency.** The FSE framework uses the same LLM/VLM to (a) generate concepts, (b) classify in fast mode from the image, and (c) classify in slow mode from the generated concepts. The paper interprets the 25%+ CRI gap as "annotations are insufficient," but a plausible alternative is that the model generates adequate concepts yet cannot map those concepts back to a specific fine-grained label due to limited text-only reasoning ability. The paper cites self-evaluation literature (Kiciman et al., 2023; Xie et al., 2023) to motivate this design, but does not include a positive control. Adding human-written concept descriptions (e.g., existing CUB attribute annotations) in slow mode would disentangle these factors: if models achieve high CRI on human concepts but low CRI on LLM concepts, the bottleneck is annotation quality; if they fail on both, it is reasoning ability. Without this control, the paper's central claim that "current annotation methods fail to provide sufficient semantic coverage" is less definitive than presented. *This is the most significant limitation because it directly affects how the paper's headline result should be interpreted.*

2. **Sample sizes for the main CRI experiments are not reported.** The preliminary contradiction test (Table 1) specifies 100 images per dataset. For the main experiments (Figure 3, Tables 2, 3, 4), the parameter *l* is defined in Section 4.1 as "the total number of cases" but never assigned a numerical value. For datasets like CUB-200 (11,788 images, 200 classes) or Cars-196 (16,185 images, 196 classes), it matters whether the evaluation used 50 samples or 5,000. The paper reports "negligible standard deviations" across 3 runs, but low variance with small sample sizes is not meaningful. Without this information, the statistical reliability of the reported CRI values—and the central 25% claim—cannot be assessed.

### Minor

1. **The CRI formula (Equation 2) contains a notational error.** As written, CRI = 100% × (1/t) × ∑_{i=1}^t 𝟙[y_i^t = y_i] sums over i=1 to *t* (the step index) rather than over the *l* test cases defined in the test set. Given the context, this is almost certainly a typo—it should sum over the *l* instances—but the current notation is formally incorrect and would not average over the dataset as intended.

2. **The five-stage refinement process lacks ablation.** The paper extends prior work (1–3 stages) to a specific 5-stage hierarchy (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features) without exploring whether fewer stages would yield similar CRI curves or whether the ordering matters. Since the CRI trajectory across steps is a key result (Figure 3), the sensitivity of the findings to this design choice is unexamined.

3. **The paper's framing is somewhat broader than what is evaluated.** The title "Are Large Language Models Good XAI Annotators?" suggests a wide assessment, but the paper evaluates only one specific criterion: whether concepts are sufficient for the *generating model itself* to re-identify the class among semantically similar distractors. The abstract and introduction do properly scope the paper to sufficiency, but some broader claims in the conclusion could give an inflated impression of generality.

### Trivial
None.

## Nice-to-Haves
- A positive control using human-written concept annotations (e.g., CUB attributes) would definitively separate concept quality from reasoning ability.
- Cross-model evaluation (one LLM evaluating another LLM's concepts) would strengthen generality.
- Candidate set size sensitivity analysis (e.g., 10-way or 20-way forced choice) would better reflect real-world fine-grained classification.
- Ablation on the number of annotation stages (3 vs. 5) would confirm the design choice.

## Removed Points

These points were raised by reviewers but are removed as either factually incorrect, based on parser artifacts, or scope creep:

- **"DeepSeek-R1 CoT analysis not shown in main paper"**: The paper states these results are in Appendix D, which is stripped by the parser. Criticisms about missing appendix content are removed per instruction.
- **"Finding on common datasets undermines generality of the critique"**: The paper explicitly discusses this dissociation and uses it to scope findings. This is a strength, not a weakness.
- **"Five-stage process is under-justified" (as a major weakness)**: The paper provides justification by citing prior work using 1–3 stages and explains the progression from coarse to fine. Reduced to minor (missing ablation) rather than major.
- **All formatting, grammar, and typographical nitpicks**: These are parser artifacts, not author errors.
- **"The definition of good XAI annotator is much narrower than the title implies" (strong version)**: The abstract clearly scopes the paper to sufficiency. Retained as a minor framing concern only.

## Novel Insights

The most interesting observation that emerged across the reviews is the unresolved tension between the paper's self-evaluation design and its central claim about annotation insufficiency. Neither reviewer argued that the FSE framework is uninteresting or that the utility-as-proxy refutation is unsound; rather, the debate centers on whether the 25% CRI gap can be cleanly attributed to annotation quality given the same-model design. This suggests the paper's most important contribution may be not the specific CRI numbers but the framework itself, which could be fruitfully applied in a cross-model setting. The fine-grained vs. coarse-grained dissociation (Table 3) also deserves more attention as a finding in its own right: it shows that LLMs can successfully conceptualize knowledge at coarse granularity but systematically fail to do so when fine-grained discrimination is required—a pattern that merits deeper investigation.

## Suggestions

1. **Add a positive control**: Feed human-written concept descriptions (e.g., existing CUB attribute annotations) to the same models in slow mode. If models achieve CRI >80% on human concepts but <60% on LLM concepts, the case for annotation insufficiency is decisive.
2. **Report sample sizes**: Explicitly state how many test cases were used per dataset in all main experiments, along with confidence intervals or error bars.
3. **Consider cross-model evaluation**: Have one LLM generate concepts and a different LLM (from a different family) evaluate them in slow mode, to test whether the gap persists independently of the annotator model.
4. **Fix the CRI formula (Eq. 2)** to sum over *l* test cases rather than *t* steps.
5. **Add an ablation** varying the number of annotation stages (e.g., 3 vs. 5) to understand sensitivity of CRI trajectories to prompt design.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- *KLUDshUx2V* (3.40) — Concept bank automation with LLMs. Weaker in novelty and experimental scope than the paper under review. Reject.
- *kTjEPEy96Q* (3.00) — Unsupervised CBM evaluation framework. Structurally similar topic but much less developed.
- *0qrTH5AZVt* (4.67) — Concept-based local explanations. Comparable quality but confounded by weaker clarity. Reject.
- *RC5FPYVQaH* (5.75) — Concept Bottleneck LLMs. Stronger in novelty (new architecture), accepted.
- *DzGe40glxs* (8.00) — Emergent planning in RL. Different topic, much stronger paper.

**Round 2 (Narrowing, bracket 4–6):**
- *6KZ80APcxf (PASTA)* (5.50) — Human-aligned XAI evaluation benchmark. Similar proposal-type paper with extensive evaluation but limited by dataset size. Rejected despite decent scores (6,5,6,5). The paper under review is of comparable overall quality but has a cleaner experimental design for its core claim.
- *WqsYs05Ri7 (U-ACE)* (5.20) — Uncertainty-aware concept explanations. Solid contribution but dense presentation. The paper under review is better structured and more accessible.
- *todLTYB1I7* (5.00) — Principled evaluation framework for neuron explanations. Similar meta-evaluation contribution, rejected despite respectable scores. Comparable level of contribution.
- *vJ0axKTh7t* (6.25) — MLLM association benchmark. Stronger paper with multiple new tasks and evaluations. Accepted. The paper under review is weaker than this anchor.

**Round-1 bracket stated:** 4.0–6.0

**How round 2 narrowed:** The round-2 anchors confirmed the paper sits in the 4.5–5.5 range. Compared to accepted papers (CB-LLM at 5.75, Labyrinth of Links at 6.25), the paper under review has a more significant unresolved confound that weakens its central claim. Compared to rejected papers at similar scores (PASTA 5.50, Principled Eval 5.00, U-ACE 5.20), the paper has comparable strengths and a similar severity of limitations. The utility-as-proxy finding is the paper's strongest card and is genuinely novel, but the confound prevents the headline result from being as definitive as presented.

**Final Score: 5.0** — Reject. The paper makes a genuinely useful contribution in exposing the failure of the utility-as-proxy assumption, and the FSE framework is methodologically coherent. However, the central claim about annotation insufficiency is undermined by the same-model confound (the evaluating model is the annotator model), and the missing sample sizes prevent statistical verification of the main results. The contribution is real but the limitations are significant enough that the paper does not yet meet the threshold for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>