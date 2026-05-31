## Summary

This paper proposes the **Fast and Slow Effect (FSE)** framework, a human-supervision-free method for evaluating the sufficiency of LLM/VLM-generated concept-class annotations in Explainable AI (XAI) systems, particularly Concept Bottleneck Models. FSE simulates a five-stage hierarchical annotation process and introduces the **Class Representation Index (CRI)**, measuring whether accumulated textual concepts alone can discriminate a target class from semantically similar alternatives. Key findings include: (1) on fine-grained datasets, slow mode (text-concept-based inference) dramatically underperforms fast mode (direct visual inference) by over 25% on average, indicating that LLMs cannot sufficiently externalize their visual knowledge into text; and (2) the "utility-as-proxy" assumption—using downstream accuracy to validate annotation quality—is misleading, as fused (image+text) inference closely matches fast-mode-alone performance while slow-mode scores remain much lower.

---

## Strengths

- **Addresses a genuine and underexplored gap.** Most prior work in XAI simply deploys LLMs for concept generation without rigorous validation of annotation sufficiency. The paper identifies a principled definition (Definition 3.1) and builds a practical, fully automated evaluation framework around it.

- **Compelling counterintuitive finding well-supported across models.** The negative CRI-gap on fine-grained datasets (Table 2, averages of −25 to −27%) holds consistently across six model families (GPT-4o, Llama-3.2, QwenVL2) and three datasets, strongly supporting the claim that LLMs fail to articulate fine-grained visual knowledge in text.

- **The utility-as-proxy critique is crisp and empirically backed.** Table 4 shows fused mode ≈ fast mode (~85–97% CRI) while slow mode alone sits at ~43–69%, directly demonstrating that high downstream accuracy can mask insufficient conceptual supervision. This is practically important for the community.

- **Controlled distractor selection is methodologically motivated.** The preliminary contradiction test (Table 1) rigorously justifies the choice of semantically related distractors (via ResNet-18 top-4 predictions) over random distractors, showing substantially higher contradiction rates (34–45% vs 14–20%), ensuring the evaluation is appropriately challenging.

- **Generalization across dataset types provides calibration.** Demonstrating that slow mode *does* outperform fast mode on coarser datasets (CIFAR-100, Caltech-101, Table 3) shows the framework is responsive to real annotation quality differences and is not trivially biased toward failure.

---

## Weaknesses

### Fatal
None.

### Major

- **No human annotation baseline.** The paper's core claim is that current LLM annotations are *insufficient*, but there is no CRI measurement from human expert annotations to establish what "sufficient" looks like numerically. Without this reference point, the observed CRI values (e.g., 57% for slow-mode GPT-4o on CUB-Bird) cannot be interpreted relative to achievable sufficiency. It is unclear whether the problem is solvable with better prompting or represents an intrinsic limitation of text-based concepts for fine-grained classes.

- **Self-referential evaluation of CRI.** The same LLM/VLM that generates the concepts also performs the CRI evaluation (prediction from text concepts). While this is somewhat mitigated by testing multiple model families, a more rigorous evaluation would use a separate model (e.g., a strong text encoder + retrieval system) to assess whether the generated concepts sufficiently identify the class, separating the annotation generator from the evaluator.

- **The dramatic CRI drop at t=1 (Background stage) conflates uninformative first stages with overall annotation failure.** In Table 3, CRI falls from ~84–91% at t=0 to ~30–34% at t=1 even on CIFAR-100, where slow mode ultimately recovers to >93%. This inflection is not discussed: the Stage 1 ("Background: ocean") is trivially insufficient alone; the meaningful evaluation should arguably begin at Stage 3 or later. Reporting aggregate CRI and CRI-gap without acknowledging this structural issue overstates the severity of annotation failure.

### Minor

- **Fused mode experiment limited to two models.** Table 4 (utility-as-proxy critique) only covers GPT-4o and GPT-4o-mini. Given the finding is framed as a critique of a general assumption in the XAI community, showing the same discrepancy across Llama-3.2 and QwenVL2 families would substantially strengthen the claim.

- **The five-stage annotation pipeline is fixed and arbitrary.** The choice of T=5 stages and their ordering (Background → Superclass → Salient → Detailed → Auxiliary) is motivated by referencing prior 2- and 3-stage approaches, but no ablation on stage count or ordering is provided. The CRI-gap results could be sensitive to how the concept chain is structured.

- **Alternative explanation not ruled out: underspecified prompting rather than fundamental LLM knowledge gap.** The slow mode's poor performance could reflect suboptimal prompting strategy rather than a fundamental limitation of LLMs to externalize fine-grained visual knowledge. The paper does not include ablations on prompt design to rule this out.

### Trivial

- The paper refers throughout to "Appendix B/C/D" for critical details (prompt design, visual case studies, DeepSeek-R1 results) that cannot be verified from the main submission alone.

---

## Nice-to-Haves

- Including CRI from human-expert annotations (even for a subset of classes on CUB-Bird) would anchor the evaluation and demonstrate the gap relative to gold-standard sufficiency.
- An ablation varying the number and order of annotation stages would strengthen confidence in the five-stage design.
- Cross-model CRI evaluation (concepts generated by GPT-4o, evaluated by Llama-3.2) would address the self-referential concern and reveal whether annotation failure is model-specific or general.
- Reporting concept length/specificity statistics for slow-mode annotations would clarify whether the CRI drop reflects vague concepts, non-discriminative concepts, or incorrect concepts.

---

## Novel Insights

The most genuinely novel finding is the **asymmetry between fast and slow modes**: LLMs can rapidly perform accurate visual inference but systematically fail to externalize the knowledge underlying that inference into textual descriptions sufficient for independent re-classification. This dissociation—between what a model "knows" implicitly and what it can explicitly articulate—has broad implications beyond XAI. It empirically validates a concern analogous to the tacit knowledge problem in cognitive science: expert performance does not imply the ability to fully articulate that expertise. Combined with the utility-as-proxy debunking (Table 4), this suggests that standard end-to-end training metrics in concept-based models may be optimizing for visual shortcut exploitation rather than genuine concept grounding. This opens the research question of whether text-based concept supervision is fundamentally limited for fine-grained visual categories, or whether better elicitation strategies (e.g., contrastive prompting, iterative refinement with adversarial distractors) can close this gap.

---

## Suggestions

- Add a CRI baseline using human-annotated concepts (even for a small class subset) to define the sufficiency target.
- Separate concept generation from concept evaluation in CRI: use generated concepts from model A and evaluate using model B, to isolate whether poor CRI reflects the annotator's language quality or the evaluator's reasoning.
- Include an ablation on the Stage 1 (Background-only) dip by reporting CRI from Stage 3 onward, to separate inherently uninformative early stages from genuinely insufficient later annotations.
- Expand Table 4 (utility-as-proxy) to cover all six tested models.

---

## Score and Decision

The paper addresses a genuinely important question with a novel, autonomous evaluation framework and produces counterintuitive, reproducible empirical findings that should prompt the community to reconsider how concept annotation quality is validated in XAI. The main methodological concerns (no human baseline, self-referential CRI, uninformative early-stage confound) reduce confidence in the precise quantitative claims but do not undermine the qualitative conclusions. The paper makes a useful diagnostic contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>