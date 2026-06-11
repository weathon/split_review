Now let me finalize the review with the calibrated score.

**Round 1 bracket:** 6.0–7.5. The paper is clearly above weak-band anchors (3.0–3.4) and above the middle-band anchors read (4.83–6.0), while below strong-band anchors (8.0).

**Round 2 narrowing:** Compared to rp0EdI8X4e (6.25), this paper has broader empirical validation and more directly impactful findings. Compared to c7DND1iIgb (6.67), both have similar contribution levels but the paper under review has a more systematic evaluation framework. Compared to EXitynZhYn (7.00), that paper has a more polished methodology; this paper has comparable empirical breadth but weaker framing. **Final score: 6.5.**

---

## Summary
This paper proposes the Fast and Slow Effect (FSE) framework for evaluating the sufficiency of LLM/VLM-generated concept annotations in concept-based XAI without human supervision. FSE consists of a five-stage coarse-to-fine concept-gathering protocol and the Class Representation Index (CRI), which measures whether accumulated concepts alone enable correct classification among semantically similar distractors. Experiments across six models and five datasets show that concept-only (slow mode) classification underperforms direct visual (fast mode) classification by ~25% on fine-grained datasets, and that fused image+concept performance can be high (~90%) while concept-only performance is low (~50%), challenging the utility-as-proxy evaluation paradigm.

## Strengths
- **Strong empirical demonstration of the CRI-Gap across models and datasets**: Table 2 shows consistent negative CRI-Gap scores averaging –25% to –27% across six models on three fine-grained datasets (Car, Flower, CUB-Bird), with nearly all model-dataset pairs negative. This broad replication across model families and sizes (GPT-4o, Llama-3.2-vision, QwenVL2 at both large and small scales) strengthens the generalizability claim.
- **Convincing refutation of the utility-as-proxy assumption**: Table 4 directly compares Fast, Slow, and Fuse modes. GPT-4o on Car achieves Fast: 93.75%, Fuse: 93.08%, Slow: 60.82% — the fused mode closely tracks fast mode while slow mode lags by >30 percentage points. This controlled comparison isolates annotation quality from downstream utility and provides a concrete, actionable warning for practitioners.
- **Validated experimental design through distractor-strategy calibration**: The preliminary contradiction test (Table 1) shows semantically related distractors nearly double contradiction rates (34–45% vs. 14–21%) over random selection, justifying the more challenging candidate-set construction used in main experiments and strengthening result credibility.
- **Natural control via general-dataset results**: Table 3 shows that on CIFAR-100 and Caltech-101, slow mode surpasses fast mode with CRI scores >89% at t=5, demonstrating the FSE framework is not inherently biased against slow-mode performance and that the insufficiency finding is genuinely tied to fine-grained dataset difficulty rather than a methodological artifact.

## Weaknesses

### Fatal
None.

### Major
- **The "Slow Mode Superiority" hypothesis is weakly motivated and its framing as a "surprising disconfirmation" weakens the narrative**: The paper justifies the hypothesis that slow mode should outperform fast mode by appealing to Kahneman's dual-process theory (Section 4.2, Eq. 3). This analogy from human cognition to LLM inference is tenuous — dual-process theory describes human cognitive architecture, not model inference. For fine-grained visual tasks, the opposite expectation (verbal overshadowing — where verbalizing visual details degrades recognition) is at least as plausible. The paper's narrative arc (hypothesize superiority → "surprisingly" find the opposite) rests on a hypothesis that was never strongly grounded. The empirical result (text-only underperforms vision on fine-grained tasks) is informative and valuable, but presenting it as a counterintuitive discovery weakens the paper's credibility. Reframing fast mode as a visual upper bound and slow mode as a concept-only lower bound, with the CRI-Gap measuring how much discriminative information fails to be verbalized, would be more defensible and no less informative.

### Minor
- **The sufficiency definition (Def 3.1) is very strong and its broader implications are not fully discussed**: The definition requires concepts alone to enable accurate class inference. While the paper explicitly defends this choice (lines 95-96), concept-based XAI methods typically use concepts as intermediate representations in conjunction with visual features, not as standalone classifiers. The paper would benefit from acknowledging this tension and discussing when standalone sufficiency is necessary versus when contributory sufficiency (concepts adding information beyond visual features) suffices.
- **CRI is essentially accuracy in a specific probing setup, and Eq. 2 contains a notation error**: CRI computes the proportion of correct forced-choice classifications among semantically similar distractors — this is 5-way accuracy. The contribution is the probing protocol (accumulated concepts + semantic distractors), not a fundamentally new metric. Additionally, Eq. 2 sums over i=1 to t (the time step) rather than i=1 to l (the number of test instances); the intended formula is clearly per-instance accuracy at step t but the notation should be corrected.
- **Sample sizes for main experiments are not explicitly reported**: The preliminary experiment uses 100 images/dataset. It is unclear whether the main experiments (Figure 3, Tables 2-4) use the same, more, or fewer samples, which matters for assessing the reliability of the reported ~25% CRI gaps.

### Trivial
- The post-hoc annotation scenario (Figure 3b) lacks a fast-mode comparison by design, so the CRI-Gap analysis applies only to visual-grounded scenarios; the generality claim could be softened accordingly.
- The error bars in Figure 3 are described as "negligible" based on visual inspection rather than reported standard deviation values.
- The DeepSeek-R1 analysis is deferred to Appendix D (stripped by the parser), so the claim about "even advanced reasoning models" cannot be independently evaluated from the main text.

## Nice-to-Haves
- A human baseline (e.g., human-written concept descriptions tested in the same CRI setup) would help disentangle whether the CRI gap reflects annotator limitations or the inherent difficulty of verbalizing fine-grained visual distinctions.
- Reframing FSE as establishing an upper bound (fast mode) and lower bound (slow mode) with the gap serving as a diagnostic tool, rather than centering the narrative on the Slow Mode Superiority disconfirmation, would strengthen the paper's contribution.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim: "The definition of 'sufficiency' builds the central finding into the experimental design — this is a structural problem"** — REMOVED. The paper defines sufficiency clearly (Def 3.1) and then tests whether annotations meet that standard. This is normal scientific practice. Moreover, on general datasets (Table 3), slow mode outperforms fast mode, directly demonstrating that the framework does not guarantee the result.
- **Harsh Critic claim: "The paper assumes, without argument, that concepts must work in isolation to be valid"** — REMOVED. The paper provides explicit argumentation (lines 95-96: "a trustworthy annotation should be self-contained") and grounds the definition in LLM self-assessment capabilities. The position is defended, not assumed.
- **Harsh Critic claim: "Removing the image entirely in slow mode and classifying from text alone... is not a surprising discovery"** — REMOVED as a standalone weakness. Whether this is "surprising" is subjective and not a substantive criticism of the methodology or results. The paper's contribution is the systematic measurement and the framework, not the surprise value.
- **Harsh Critic claim about the CRI notation error being a "methodological gap"** — DEMOTED to Minor/Trivial. The intended formula is obvious from context (per-instance accuracy); this is a typographical error, not a gap that threatens any result.
- **Harsh Critic notes about prompts being deferred to Appendix B and DeepSeek-R1 to Appendix D** — REMOVED. Appendix stripping is a parser artifact. The original submission contains these appendices.
- **Harsh Critic note about contradiction test using simplified FSE** — REMOVED. The paper is transparent that the preliminary experiment is simplified; this is standard practice for calibration experiments and does not weaken the main results.
- **Strength Finder claim: "Both annotation paradigms covered"** — REMOVED as a standalone strength. While true, this is a generic aspect of experimental design rather than a concrete finding that distinguishes the paper's contribution.

## Novel Insights
None beyond the paper's own contributions. The most valuable reframing — treating the fast/slow comparison as upper/lower bounds rather than testing a weakly-motivated superiority hypothesis — is a useful corrective to the paper's narrative but does not introduce new empirical knowledge beyond what the paper already demonstrates.

## Suggestions
- Reframe the Slow Mode Superiority hypothesis: instead of hypothesizing slow > fast and presenting the opposite as surprising, treat fast mode as a visual upper bound and slow mode as a concept-only lower bound, with the CRI-Gap measuring how much discriminative information the annotator fails to verbalize. This turns the currently awkward narrative into a clean diagnostic framework.
- Discuss the verbal overshadowing confound — acknowledge that the CRI gap may partly reflect the inherent difficulty of verbalizing fine-grained visual distinctions rather than purely annotator failure. This would strengthen rather than weaken the paper by showing awareness of alternative interpretations.
- Report sample sizes explicitly for all main experiments.
- Fix the CRI notation in Eq. 2: change the summation from i=1 to t to i=1 to l.

## Calibration Anchor Comparison
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Automating High-Quality Concept Banks | KLUDshUx2V | 3.40 | R1 | Weaker — less systematic evaluation, narrower scope |
| Evaluating the Unseen (CBM eval) | kTjEPEy96Q | 3.00 | R1 | Much weaker — fundamental methodological issues |
| Concept Bottleneck LLMs | RC5FPYVQaH | 5.75 | R1 | Our paper has broader evaluation, clearer findings |
| Concept Bottleneck Generative Models | L9U5MJJleF | 6.00 | R1 | Our paper has more comprehensive experiments |
| Zero-shot CBMs | 5Aem9XFZ0t | 4.83 | R1 | Our paper has stronger empirical validation |
| Faithful V-L Interpretation via CBMs | rp0EdI8X4e | 6.25 | R2 | Our paper is broader in scope, more empirically comprehensive |
| Democratizing FGVR with LLMs | c7DND1iIgb | 6.67 | R2 | Comparable contribution level; ours more evaluation-focused |
| Open-ended VQA Benchmarking | EXitynZhYn | 7.00 | R2 | Slightly stronger — more polished methodology and presentation |
| Sufficient Context (RAG) | Jjr2Odj8DJ | 6.25 | R2 | Different domain, comparable empirical rigor |
| VL-ICL Bench | cpGPPLLYYx | 6.50 | R2 | Comparable quality — both evaluation-focused with systematic experiments |

**Bracket:** Round 1 placed the paper at 6.0–7.5. Round 2 narrowed to ~6.25–7.00. The paper is clearly above rp0EdI8X4e (6.25) and comparable to c7DND1iIgb (6.67) and cpGPPLLYYx (6.50), but below EXitynZhYn (7.00) due to the framing issues around the Slow Mode Superiority hypothesis. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>