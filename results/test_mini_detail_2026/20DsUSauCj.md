Now I have sufficient calibration data. Let me construct the final review.

## Summary

This paper presents an automated pipeline that extracts "persona vectors"—linear directions in activation space encoding traits like evil, sycophancy, and hallucination—from natural-language trait descriptions. The authors demonstrate four applications of these vectors: (1) monitoring prompt-induced persona shifts at deployment, (2) predicting finetuning-induced persona shifts from activation changes, (3) a novel *preventative steering* method that adds the persona vector during training (rather than subtracting it at inference) to mitigate undesirable drift while preserving capabilities, and (4) pre-finetuning data screening via the "projection difference" metric. The empirical evaluation, conducted on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across three traits, shows strong correlations (r=0.76–0.97) between activation shifts along persona vectors and behavioral trait expression, and demonstrates that preventative steering suppresses hallucination to baseline while keeping MMLU and new-fact accuracy nearly intact—unlike inference-time steering which degrades both.

## Strengths

1. **Novel preventative steering method with clear practical advantage.** The central empirical finding—that steering *toward* an undesirable direction *during* finetuning (rather than against it at inference) reduces trait expression to near-baseline while preserving MMLU accuracy and new-fact retention—is both non-obvious and practically significant. Figure 6 directly contrasts the two approaches: inference-time steering degrades both MMLU and new-fact accuracy, whereas preventative steering keeps both nearly stable. This is a genuine methodological contribution over prior activation-steering work.

2. **Automated extraction pipeline from natural-language descriptions.** Section 2 describes a pipeline that inputs only a trait name and description and outputs a persona vector, using Claude 3.7 Sonnet to generate contrastive prompts, evaluation questions, and a scoring rubric. This systematization goes beyond prior work requiring hand-crafted contrastive pairs (Turner et al., Panickssery et al., Zou et al.), making the method easily applicable to new traits.

3. **Pre-finetuning prediction of persona shifts from training data.** The projection-difference metric (Equation 1, Figure 7) strongly correlates with post-finetuning trait expression (r=0.88–0.95), enabling practitioners to flag problematic datasets or individual samples before training begins. This is a practical tool that goes beyond detecting shifts after the fact.

4. **Trait specificity demonstrated through cross-trait controls.** The paper reports that correlations between finetuning shift along a persona vector and the *corresponding* trait score (r=0.76–0.97) are substantially higher than cross-trait comparisons (r=0.34–0.86, Appendix I.2), showing the vectors capture trait-specific signal rather than generic "bad behavior."

5. **Validation of LLM judge against human evaluators.** The paper explicitly states that the LLM-based trait expression scores (GPT-4.1-mini) are validated against human evaluators and external benchmarks (Appendix D). This addresses one of the most common concerns with LLM-as-judge evaluations.

6. **Multi-model, multi-trait, multi-dataset evaluation.** All main experiments are conducted on both Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, across three traits (evil, sycophancy, hallucination), using both explicitly trait-eliciting and emergent-misalignment-like datasets. The paper also compares against CAFT, regularization penalties, and prompt-based baselines (Appendix L).

## Weaknesses

### Major
- **Reliance on a single LLM judge for the primary metric.** The trait expression score—the dependent variable in nearly every figure—is produced by a single model (GPT-4.1-mini). While the paper reports human validation (Appendix D) and checks against external benchmarks, the core metric remains a black-box classifier whose biases are not fully characterized. If the judge systematically labels certain response patterns (e.g., longer or more hedged responses) as higher trait expression, the reported correlations could be inflated. Using a second independent judge model or a diverse set of judges would strengthen the evidence.

### Minor

1. **Limited model scope (7B–8B only).** Experiments are conducted on two similarly-sized models from two families. The paper's findings about linear predictability and preventative steering are not validated at larger scales (70B+) or with models trained with different recipes (e.g., RLHF-heavy). This tempers the generality of the claims but does not affect internal validity.

2. **Capability evaluation limited to MMLU.** The paper uses MMLU accuracy as its sole measure of general capabilities. MMLU is a multiple-choice benchmark that does not test generation quality, instruction following, or open-ended reasoning. Additional benchmarks (e.g., GSM8K, HumanEval, MT-Bench) would strengthen the claim that preventative steering better preserves "general capabilities."

3. **Within-type monitoring correlation is weaker than across-type.** The paper honestly notes (Section 3.3, Appendix E.2) that the monitoring correlations (r=0.75–0.83) arise primarily from distinguishing between different *prompt types* (trait-encouraging vs. trait-discouraging), with more modest correlations when controlling for prompt type. This means the vectors are better at detecting whether a prompting intervention is in place than at detecting subtler shifts within a fixed prompt regime.

4. **Layer selection may overfit to the extraction set.** The pipeline selects the best layer by testing steering effectiveness on the *extraction set* (Appendix D.4). While a separate evaluation set is used for downstream analysis, the layer choice could be somewhat specific to the extraction prompts. Reporting robustness to alternative layer choices (e.g., the median-performing layer) would address this.

5. **Preventative steering mechanism is explained only intuitively.** The paper states that adding the vector during training "counteracts the finetuning objective's tendency to push the model along that direction," but does not provide a more formal analysis (e.g., relating it to gradient flow or implicit bias). The empirical evidence is strong enough to carry the claim, but a more precise mechanistic account would be valuable.

### Trivia/Trivial
*None.*

## Nice-to-Haves
- **Multi-trait preventative steering.** The paper applies preventative steering for one trait at a time. In practice, a model might simultaneously drift toward several undesirable traits (e.g., both sycophancy and hallucination). Whether multiple vectors can be added simultaneously during training, and whether the benefit compounds, is a natural next question.
- **Characterizing failure modes of the pre-screening metric.** The projection difference works well for the tested datasets, but one can imagine cases where it would fail (e.g., training data responses identical in content to base model responses but producing different internal states due to contextual nuances). Discussing failure cases would make the contribution more actionable.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Limited model scope is a methodological gap" and "scaling to 70B+ may reveal different dynamics"** → This is presented as a gap, but the paper is a methods paper establishing the framework on two models. This is a limitation acknowledged by the paper (Appendix B), not a flaw. Demoted to Minor.
- **Harsh Critic: "Statistical details for correlations (number of data points not fully described)"** → The paper reports r-values and p-values. Each point represents a model finetuned on a specific dataset. The number of datapoints and nature of data are sufficiently clear from Figure 4 descriptions. Removed as too vague.
- **Strength Finder: "Validation of monitoring capability with strong correlations"** → The paper itself notes this correlation is primarily driven by prompt-type differences. While not false, this strength is weakened by the paper's own honest caveats. Kept but not as a top strength.
- **Strength Finder: "Comparison to alternative training interventions"** → Valid point, but the comparison is in the appendix. The main text mentions it briefly. Still a genuine strength.
- Several generic strengths from Strength Finder (e.g., "multi-model validation," "addressed an important problem") are concrete enough to keep, but I've merged them into the strengths section above.

## Novel Insights

The most striking finding that emerges from synthesizing the reviews is the *asymmetry* between preventative and inference-time steering. The paper's key insight—that proactively adding an undesirable direction during training is *less* destructive than reactively subtracting it at inference—seems counterintuitive but is convincingly supported by the fact-acquisition case study (Figure 6). This asymmetry suggests that the damage from inference-time steering comes not from the steering *per se* but from the mismatch between the model's learned distribution (which has shifted) and the post-hoc intervention applied on top of that shifted distribution. The preventative approach keeps the training dynamics closer to the base model's attractor, requiring smaller compensatory changes. This observation could guide future work on training-aware interventions more broadly.

## Suggestions

1. **Add a second LLM judge** (e.g., Claude 4 Sonnet or Llama-4-Maverick) to verify that the trait expression scores are not idiosyncratic to GPT-4.1-mini. A simple table reporting Pearson/Spearman correlations between judges on a held-out response set would substantially strengthen the evaluation.
2. **Report capability metrics beyond MMLU** for the preventative steering case study—at minimum GSM8K (math reasoning) and a generation-quality metric—to strengthen the claim that "general capabilities" are preserved.
3. **Include a brief sensitivity analysis** for layer selection: show that the main results (e.g., Figure 4 correlations) hold when using the second-best layer or a random layer within a plausible range.
4. **Add a paragraph in Section 5** providing a more formal intuition for why preventative steering works, potentially using a simple linearized toy model where the finetuning gradient has components both parallel and orthogonal to the persona vector.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors: *Psychometric Personality Shaping* (3.00), *Painless Activation Steering* (3.33), *Steering Vector Transfer* (2.50), *Beyond BFI* (2.00) — all substantially less rigorous, less novel, or more narrowly scoped.
- Middle anchors: *PERSONA* (5.00), *Personality Subnetworks* (4.50), *From Five Dimensions to Many* (6.50), *Personality Illusion* (4.00) — all topically similar.
- Strong anchors: *Narrow Finetuning Traces* (7.50), *Command-V* (7.00), *Embodied Navigation* (8.00) — these are broader, more established work.

**Round 1 Bracket:** [5, 8]

**Round 2 (Narrowing):**
- *PERSONA* (5.00): Similar topic (personality vectors). The current paper is substantially stronger—broader scope (monitoring + finetuning + preventative steering + data screening vs. just inference-time control), human validation of LLM judge (which PERSONA was criticized for lacking), evaluation of capability side effects (which PERSONA was criticized for omitting). Current paper is about +2.0 stronger.
- *Personality Subnetworks* (4.50): Similar topic. Current paper has stronger empirical validation, more practical contributions, evaluates MMLU impact. Current paper is about +2.5 stronger.
- *Narrow Finetuning Traces* (7.50): Topically relevant (finetuning shifts, activation differences). Broader model scope (1B-32B, 4 families) but narrower contribution (analysis only, no preventative method). Current paper has *more novel methodology* but *narrower empirical scope*. Comparable or slightly weaker overall.
- *Command-V* (7.00): Comparable in quality. Both have clear methodological contributions and thorough evaluation across tasks.
- *AlphaSteer* (7.00): Similar rigor. Current paper has broader contributions (multiple applications vs. one), but AlphaSteer has stronger theoretical grounding. Comparable.

**Round 3 (Optional):** Not needed — sufficiently confident in the bracket.

**Final Score:** 7.0 — The paper is a clear Accept. It makes multiple novel, well-validated contributions to representation engineering. The preventative steering result alone is a significant practical advance. The weaknesses (single LLM judge, 7B-8B models only, MMLU-only capability evaluation) are bounded and do not threaten the core claims. The paper is stronger than the typical poster at 5-6 and comparable to strong 7-range papers.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>