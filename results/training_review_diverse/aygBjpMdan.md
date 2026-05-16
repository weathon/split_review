Now I have a thorough understanding of the paper to produce the consolidated review.

## Summary

This paper identifies a failure mode in standard CoT distillation: student models imitate the teacher's reasoning *form* while making errors/omissions on the ~4.7% of steps the authors term "key reasoning steps." The authors propose EDIT, which (1) generates dual CoTs (correct–incorrect pairs with similar reasoning paths but divergent conclusions) using specially designed prompts, (2) applies minimum edit distance to locate differing tokens as "key steps," and (3) trains the student with a weighted loss that upweights correct key steps and downweights wrong ones. Experiments across BBH, BB-sub, AGIEval, ARC-E, and ARC-C show average gains of +4.7% over standard CoT distillation and +2.7% over the strongest data-matched baseline.

## Strengths

- **Novel formulation of a real problem in CoT distillation.** The paper identifies and formalizes a specific failure mode — students mimicking reasoning surface structure while missing the decision-critical steps — that prior work on CoT distillation (Std-CoT, MT-CoT, SCOTT) does not directly address. The proposed solution of using contrasting reasoning traces to localize discriminative steps is conceptually clean and well-motivated by the human-learning analogy.

- **Consistent empirical gains across benchmarks and architectures.** EDIT outperforms all baselines on average accuracy across 5 datasets (46.5% vs. next-best 43.8%, Table 1). Gains are largest on challenging subsets (BBH-test: +6.1%, ARC-C: +6.4% over Std-CoT). Ablations across model sizes (1.1B–13B) and architectures (LLaMA2, LLaMA3, CodeLLaMA, Mistral) confirm the benefit holds broadly (Figures on model size and architecture).

- **Ablation studies cleanly isolate component contributions.** The w/o RWC (42.7%) and w/o KRSL (44.3%) ablations show that both the rectified wrong CoTs and the key-step weighting contribute to EDIT's final performance (46.5%). This attribution is stronger than in many distillation papers, and the data-matched baselines (Repeat Sampling, Dual CoTs) rule out the alternative explanation that gains simply come from more training data.

- **CoT quality evaluation via GPT-4 scoring.** Beyond final-answer accuracy, the paper evaluates the quality of generated reasoning chains using GPT-4 scoring. The distribution analysis (Figure 3, right) shows EDIT's CoTs are closer to the teacher's distribution than Std-CoT's, supporting the claim that EDIT improves the reasoning *process*, not just the answer.

## Weaknesses

### Fatal
None.

### Major

- **The core assumption — that minimum edit distance on dual CoTs reliably identifies causally important reasoning steps — is not validated.** The method hinges on the claim that text segments differing between correct and incorrect CoTs (after alignment) correspond to the reasoning steps that *matter*. The paper provides only a single illustrative example (Figure 2, "key-step-ex"). There is no human evaluation of whether the identified spans are actually causally responsible for the answer divergence, no analysis of edit-length distributions across the dataset, and — critically — no ablation that replaces edit-distance with a random-token selection baseline. Without such evidence, it is possible that edit distance picks up irrelevant surface variation when the teacher's dual CoTs diverge in structure rather than differing at a single decision point. This leaves the mechanism undersupported relative to the weight it carries in the paper's claims.

- **No statistical rigor in reported results.** No error bars, confidence intervals, or statistical tests are reported for any experiment. The paper does not mention running multiple seeds (single run implied). The improvement over the strongest baseline (Std-CoT w/ Dual CoTs) is +2.7% on average, but the per-dataset picture is uneven: EDIT is *worse* on BB-sub (31.1 vs. 32.9, -1.8%), makes marginal gains on AGIEval (+0.8%) and ARC-E (+1.9%), and only shows convincing gains on BBH-test (+6.1%) and ARC-C (+6.4%). Without variance estimates, it is impossible to tell whether the average improvement is consistent or driven by variance on a subset of tasks. This is a standard expectation for this type of empirical paper and is a genuine gap.

- **Uneven gains and lack of discussion of negative results.** The BB-sub result (EDIT underperforming Std-CoT w/ Dual CoTs by 1.8%) is noted in the table but not discussed in the main text. The paper's framing ("EDIT outperforms the distillation baselines on both IND and OOD datasets," line 182) glosses over this counterexample. A paper that claims general-purpose improvement owes the reader an analysis of why and where the method underperforms.

### Minor

- **The 4.7% "key reasoning steps" claim is misleadingly framed.** The abstract and introduction state "CoTs usually consist mainly of simple reasoning forms, with a small proportion (≈4.7%) of key reasoning steps" as if this is a general property of CoTs. The footnote clarifies this is computed on *their generated dual CoT dataset*. This is circular: they generate data designed to have small edit distances, then cite the small edit distance as evidence that key steps are rare. The claim should be caveated or re-framed as a property of the dual CoT data, not CoTs in general.

- **DPO claim made without supporting evidence.** The paper states (line 184) that "DPO performed unexpectedly poorly in this scenario" but provides no table, figure, or even a single number to support this. Either include the DPO results with a brief discussion or remove the claim entirely. An unsupported assertion of this kind weakens trust in the presentation.

- **No hyperparameter sensitivity analysis for α and β.** The values α=1.0 and β=0.025 are chosen "empirically" with no sensitivity study. The extreme asymmetry (40:1 ratio) is a deliberate design choice that requires justification. The ablation only tests α=0 or β=0 (binary presence/absence), not intermediate values. It is unclear whether results are robust to these settings or whether they were tuned to maximize test-set performance.

- **GPT-4 CoT quality evaluation lacks quantitative summary.** The analysis (Figure 3, right) shows kernel density estimates but reports no summary statistics (mean scores, KL divergence, etc.). The figure is small and the visual claim that EDIT's distribution is "closer to the teacher" is subjective without numbers.

- **Mistake-pattern analysis overclaims small differences.** Table 5 (right) shows LEs (44.9%) slightly ahead of KEs (44.6%) and MCEs (44.5%) — differences of 0.3–0.4 percentage points. With no error bars, these are within noise range. The conclusion that "LEs provide a broader range" and "learning key reasoning steps from logical reasoning errors is the most effective way" goes beyond what this evidence supports.

### Trivial

- **The negative loss term for wrong CoTs raises a stability concern.** The objective (Eq. 6) subtracts the weighted NLL of wrong CoTs, which, in principle, can drive log probabilities toward negative infinity during training. The paper does not discuss whether gradient clipping, early stopping, or the small β=0.025 is relied upon for stability. A brief note would address this.

- **No success rate reported for dual CoT generation.** The paper describes prompts for rectifying wrong CoTs and corrupting correct CoTs, but does not report what fraction of attempts produce valid dual pairs (i.e., where answers actually diverge while reasoning paths remain similar). If this success rate is low, the method's data efficiency is weaker than it appears.

## Nice-to-Haves

- A human evaluation on ~100 pairs to measure precision/recall of edit distance for identifying causally important steps (as opposed to surface differences) would significantly strengthen the core claim.
- Analysis of why EDIT helps most on ARC-C and BBH-test but hurts on BB-sub — e.g., whether ARC-C dual CoTs have cleaner edit-distance alignment — would deepen the paper's contribution.
- A small sensitivity grid (even 2–3 values each) for α and β on a held-out validation set would improve robustness claims.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that a "stronger control" (training on the same data with standard NLL) is missing**: The paper already includes Std-CoT w/ Dual CoTs (the same data, trained with standard NLL with a "[Counterfactual Reasoning]" marker) and the w/o KRSL ablation. These serve as the requested control. The paper's baseline design is adequate.

- **Criticism about missing comparison to "more recent" distillation methods (fudge-style control, iterative refinement)**: This is speculative — the reviewer does not identify specific published methods — and the paper's baseline selection (Std-CoT, MT-CoT, SCOTT, plus data-matched variants) is defensible for its class. Per rules, disagreeing with the reviewer's taste in baselines is not a weakness.

- **Request for more training details (epochs, LoRA rank, learning rate)**: The parser strips appendix sections where these details likely appear. Per rules, reproducibility nitpicks about artifacts likely present in the original submission are removed.

- **Criticism that "the essence of above methods is simple SFT" oversimplifies**: While SCOTT and MT-CoT are not *pure* SFT, the paper's characterization captures the dominant paradigm of training on correct teacher data. This is a presentation preference, not a substantive error.

- **Strength about "insightful mistake-pattern analysis"**: The differences across mistake types (0.3–0.4%) are within noise range given no error bars, so the claimed insight conflicts with a verified weakness. The categorization itself is reasonable but the empirical support is too weak to constitute a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper itself.

## Suggestions

1. **Run experiments with 3–5 random seeds and report mean ± std.** This is the single most impactful change. The 2.7% average gain over the best baseline is not credible without variance estimates. If the paper is accepted, the reviewers and community will want to know whether the improvements are robust.

2. **Validate the edit-distance identification mechanism.** At minimum, replace edit-distance with random token selection in the KRSL loss to show that the edit-distance *matters* (not just that weighting helps). A human evaluation on a sample of 100 pairs would be even stronger.

3. **Discuss the BB-sub negative result explicitly.** A paragraph analyzing why EDIT underperforms on this dataset would improve the paper's honesty and provide guidance for future work.

4. **Either show DPO results or remove the claim.** An unsupported one-sentence dismissal of a well-known method does not belong in a research paper.

5. **Re-frame the 4.7% claim** as a property of the generated dual CoTs rather than a general observation about CoTs, to avoid the appearance of circular reasoning.

## Score and Decision

The paper presents a genuinely novel approach to CoT distillation with a well-motivated design and reasonably broad empirical evaluation. The core contribution — using dual CoTs and edit distance to focus learning on decision-critical reasoning steps — is interesting and potentially impactful. However, the empirical execution has significant gaps: the central mechanism is not validated, results lack statistical rigor, and some claims outpace the evidence. The paper merits publication provided the authors can address the major concerns (validation of edit-distance assumption and statistical rigor) in a revision. As a conference submission, the contribution is worthwhile but needs strengthening before it can be fully trusted.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>