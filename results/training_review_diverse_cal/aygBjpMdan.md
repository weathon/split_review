Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes EDIT (mistake-Driven key reasonIng step distillaTion), a method for CoT reasoning distillation that goes beyond standard supervised fine-tuning. The key idea is: (1) generate "dual CoTs" — pairs of correct and incorrect reasoning chains from the teacher LLM that follow similar paths but diverge at key steps; (2) use minimum edit distance on these pairs to identify tokens that constitute critical reasoning divergences; (3) apply a weighted loss that upweights correct key tokens and downweights incorrect ones. Experiments on BBH (in-domain) and BB-sub, AGIEval, ARC-E, ARC-C (out-of-domain) show that EDIT outperforms standard CoT distillation baselines, with ablations confirming the contributions of both the rectified wrong CoTs and the key-step learning mechanism.

## Strengths

- **Identifies and addresses a genuine limitation of standard CoT distillation.** The paper pinpoints that SFT on correct-only CoTs leads students to imitate the teacher's reasoning form while making errors on critical reasoning steps. This motivation is clearly supported with examples (Figure 1) and is a real problem in distillation. The approach of using contrastive (correct–wrong) pairs to surface these steps is well-motivated by analogy to human learning.

- **Novel and principled technical approach.** Using minimum edit distance on dual CoT pairs to automatically locate key reasoning tokens, then applying separate weighted losses for correct and wrong key steps (Equations 6–7), is a clean and conceptually sound method. This is clearly distinguished from simply adding more data or using counterfactual examples.

- **Consistent empirical improvements with thorough controls.** EDIT achieves an average +4.7% over Std-CoT, and importantly, +2.7% over Std-CoT w/ Dual CoTs (which uses the same data but without key-step weighting). The gains are most pronounced on the hardest benchmarks (BBH-test +6.1%, ARC-C +6.4%). The paper controls for data quantity (Repeat Sampling) and counterfactual data exposure (Dual CoTs), isolating the contribution of the key-step learning mechanism.

- **Ablations confirm both components matter.** Removing either the rectified wrong CoTs (w/o RWC) or the key reasoning steps learning (w/o KRSL) degrades performance across nearly all datasets, demonstrating that both the generation of high-quality dual CoTs and the fine-grained weighting are necessary.

- **Broad model applicability.** EDIT generalizes across model sizes (1.1B to 13B) and architectures (LLaMA2, CodeLLaMA, LLaMA3, Mistral), with larger gains for stronger base models, supporting its utility across resource settings.

## Weaknesses

### Fatal

None.

### Major

- **The dual CoT generation pipeline — particularly the corruption of correct CoTs (CCP) — is used without quality validation.** The entire method depends on the assumption that the dual CoT pairs share similar intermediate reasoning paths while diverging at key steps. For the CCP step (corrupting correct CoTs), the paper acknowledges that LLMs "rarely follow the incorrect hints" and "may resist providing unhelpful answers" due to RLHF, and uses curated in-context examples as a workaround. However, no quality metrics are reported: no human evaluation of whether the corrupted CoTs are actually structurally similar to their correct counterparts, no statistics on what proportion of CCP outputs are actually incorrect, and no analysis of how often the edit distance highlights spurious differences versus genuine reasoning divergences. This blind spot undermines confidence that the edit distance is isolating the right tokens.

- **The DPO comparison is mentioned but no results are shown.** The paper states (Section 4.2) that "DPO performed unexpectedly poorly in this scenario" but provides no table entry, no accuracy numbers, and no experimental details for this claim. Given that the KRSL objective (§3.3, Equation 6) bears a clear resemblance to preference optimization, omitting a direct comparison weakens the case for KRSL's advantages. This is not a request for an exhaustive comparison — a footnote or table entry would suffice — but the current claim is unverifiable.

### Minor

- **The 4.7% figure is somewhat misleadingly framed.** The abstract states "We find that CoTs consist mainly of simple reasoning forms, with a small proportion (≈4.7%) of key reasoning steps..." — implying a general property of CoTs. The footnote (in the intro, not the abstract) clarifies this was computed on the authors' dual CoT dataset. While not a serious error (the footnote exists), the framing overgeneralizes a computation that is an artifact of their particular data generation pipeline and edit-distance procedure, not an independently discovered property of natural CoTs.

- **No variance or statistical significance reported.** All results are single accuracy numbers without confidence intervals, standard deviations, or multiple random seeds. Given the use of LoRA fine-tuning, where seed-dependent variance is known to be non-trivial, this limits confidence in whether the reported gains (especially the smaller ones like +0.8% on AGIEval) are robust.

- **Key hyperparameters α=1.0 and β=0.025 are stated without sensitivity analysis.** The 40× asymmetry between correct and wrong key-step weights is striking. While the ablation (w/o Correct vs. w/o Wrong) suggests correct steps matter more, the paper provides no analysis of how performance varies with different α/β values. Without this, it is unclear whether the method's success is primarily driven by a simple upweighting of a small number of tokens in correct CoTs, rather than the more nuanced "dual learning from both correct and wrong key steps" story the paper tells.

- **GPT-4 evaluation of CoT quality lacks documentation.** The paper shows a density plot of GPT-4 scores (Figure 3, right) but does not provide the scoring prompt, describe the scoring criteria, report any measure of agreement, or show qualitative examples of what distinguishes higher-scored chains. This weakens what could otherwise be a strong piece of evidence for the claim that EDIT produces higher-quality CoTs.

- **Mistake pattern analysis shows very small differences.** Table 3 reports 44.9% (logical errors) vs. 44.6% (knowledge errors) vs. 44.5% (math errors). The paper concludes that "logical errors provide the more significant benefits," but the differences are within 0.3–0.4%, which may not be meaningful. This result should be presented with appropriate caveats rather than as a clear finding.

### Trivial

- Case studies (Section 5.2) are cherry-picked. They are useful for illustration but do not constitute systematic evidence.
- The rationale for the 4:1 BBH train/test split (rather than using the original BBH splits) could be briefly explained.

## Nice-to-Haves

- A small human annotation study (e.g., 100 dual pairs) validating that edit-distance-identified tokens correspond to what humans would call key reasoning steps would directly test the central assumption.
- Sensitivity analysis for α and β to clarify the role of the 40× asymmetry.
- Reporting results across multiple seeds (at least 3) for the main experiments to establish robustness.
- Providing the GPT-4 evaluation prompt and a few scored examples in an appendix.

## Removed Points

These points were flagged for removal by the instruction rules; they are included here only for reference and should be treated with caution:

1. **"The 4.7% claim may not generalize" as a fatal issue** — The paper footnotes the computation source, so the criticism is about presentation rather than deception. Kept as a minor weakness above.
2. **"Performance gains over Std-CoT w/ Dual CoTs are marginal"** — The reviewer's framing overstates this. +2.7% average with +6.1% and +6.4% on the hardest tasks is not marginal. However, the point about inconsistency on BB-sub (EDIT 31.1 vs. 32.9) is kept within the broader assessment.
3. **Generic formatting/style nitpicks** — Removed per hard rules.
4. **Missing related works** — Not included per hard rules (cannot verify external sources).

## Novel Insights

The reviews surface a central tension in the paper that is not fully articulated by the authors themselves: EDIT's claimed mechanism (learning key reasoning steps via edit-distance-weighted token importance) and the evidence for it (overall accuracy improvements and GPT-4 quality scores) operate at different levels of specificity. The accuracy numbers show that EDIT works, but they do not directly show *why* it works — whether the mechanism is genuinely about key-step identification, simple token upweighting, or some other confounding factor (e.g., the dual CoT data simply providing more diverse reasoning paths). The paper would be substantially strengthened by an experiment that directly tests the mechanism: e.g., checking whether EDIT's outputs contain fewer errors specifically at the edit-distance-identified positions compared to Std-CoT's outputs.

## Suggestions

1. **Validate the dual CoT quality.** Report the proportion of CCP-generated CoTs that are actually incorrect, and conduct a small human evaluation (50–100 pairs) checking whether the dual pairs share similar intermediate reasoning paths as claimed. This directly affects the validity of the edit-distance approach.

2. **Add the DPO comparison to Table 1** (even if negative). A single column with DPO results under the same setting would substantiate the claim that "DPO performed unexpectedly poorly."

3. **Provide a sensitivity analysis for α and β** over a small grid (e.g., α ∈ {0.5, 1.0, 2.0}, β ∈ {0.01, 0.025, 0.05}) on one or two datasets.

4. **Report standard deviations** over at least 3 random seeds for the main results in Table 1.

5. **Present the mistake pattern results with appropriate caveats**, acknowledging that differences of 0.3–0.4% may not be statistically meaningful.

## Score and Decision

**Overall assessment:** This paper identifies a real problem in CoT distillation, proposes a novel and well-motivated method to address it, and provides consistent empirical support across multiple benchmarks and model architectures. The weaknesses are real but not fatal — they primarily concern under-validated assumptions in the data generation pipeline and missing experimental details rather than methodological flaws that invalidate the core claims. The paper would benefit from stronger validation of its central mechanism, but as a conference submission with a novel contribution, clean ablations, and thorough baselines, it merits acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>