## Summary
The paper performs a mechanistic interpretability study of how transformer LMs answer formatted (in-prompt) multiple-choice questions, using activation patching and vocabulary projection on Olmo and Llama2 model families across MMLU, HellaSwag, and a synthetic Colors task. Its main claims are: (i) a single middle layer (and its MHSA) causally determines the predicted answer symbol, (ii) a sparse set of attention heads with specialized roles drives subsequent symbol promotion, (iii) some models handle OOD symbol sets (C/D) via a late-layer "alignment" step, and (iv) inability to separate answer symbols in vocabulary space marks poorly-performing checkpoints.

## Strengths
- The Colors synthetic task (Sec. 3.1, Sec. 6) cleanly separates "knowing the answer" from "doing formatted MCQA" and pinpoints the 350B→1T token window in Olmo-v1.7 where the format skill is acquired — a concrete, reproducible finding tied to specific training checkpoints.
- The pairing of activation patching with vocabulary projection yields a useful methodological observation: causal effects appear before vocabulary-space evidence, with patches at layer 21 of Olmo-7B-SFT dominating the prediction (Fig. 5a–b, Sec. 4) before later layers amplify the chosen symbol.
- The head typology in Sec. 5 (always-A heads, always-B heads, "correct-letter" heads, B-only heads) refines and extends Lieberum et al.'s "correct letter heads" with a more nuanced four-role taxonomy grounded in concrete projection plots.
- The training-checkpoint analysis on Olmo-v1.7 (350B / 1T / 2T) ties separability of A/B in vocabulary space to the emergence of formatted-MCQA competence, providing a falsifiable observational handle on label-bias vs. format-binding failures.

## Weaknesses

### Fatal
None. The contributions are real even if the framing overshoots.

### Major
- **Headline mechanistic claims rest on N=2 models, and one of them contradicts the headline.** Sec. 3.3 / Fig. 2 narrows the analysis to Olmo-7B-SFT and Llama2-13B-Chat. The abstract's "single middle layer" claim holds for Olmo (layer 21) but is explicitly diffuse over ~6 layers (15–21) for Llama2-13B-Chat (Sec. 4). The "two-stage OOD" behavior is also explicitly Olmo-only (footnote in Sec. 4: "Llama2-13B-Chat immediately promotes C and D"). The paper's own footnote in Sec. 5 admits "It is unclear why vocabulary projections of the two functions are so different from activation patches for the Llama2 model." With only two models in the analysis pool, the cross-model generalization implied by the abstract is not supported and should be either scaled back or supplemented with additional consistent models.
- **Head typology is correlational, not causally validated.** Sec. 5's classification of 13 components into four roles (always-A, always-B, correct-letter, B-only) is based on vocabulary projections and an arbitrary 0.01 threshold. No ablation/patching experiment is reported showing that, e.g., zero-ablating the "always-A" heads shifts predictions toward B. Given that the rest of the paper uses activation patching as its causal tool, applying it to these heads is the natural and expected validation, and its absence weakens the strongest novel empirical contribution.

### Minor
- **Label-bias vs. separability is not disentangled in Sec. 6.** The 350B checkpoint predicts B on 99.5% of instances. The interpretation that the model "cannot separate" A and B in vocabulary space is consistent with the projections, but a model with a strong B-token frequency prior would also produce inseparable A/B traces under projection. A control (e.g., showing that intervening to increase A/B separability at layer 29 reduces the bias) would convert correlation into mechanism.
- **Binary reduction of MMLU/HellaSwag is acknowledged for metric reasons but its external-validity cost is not discussed.** Converting 4-way to 2-way (Sec. 3) makes the consistency filter (Sec. 3.3) easier to pass and changes the task relative to how MMLU is actually used. The paper should explicitly discuss what changes when scaling to n>2 (the appendix metric discussion is referenced but not reflected in the main claims).
- **Vocabulary-projection plots are presented as means without per-instance variance.** Given that one of the central claims ("non-negligible probability emerges a couple of layers later," "single middle layer") is read off averaged probability traces, some indication of instance-level spread (e.g., percentiles or per-instance distributions at key layers) would let readers assess whether the localization is sharp or driven by averaging.
- **"Activation patching and vocabulary projection are complementary" is interpretive, not demonstrated.** Sec. 4's reconciliation — that layer 21 is causal but only surfaces in projection space "a couple of layers later" — is plausible but not directly tested (e.g., by projecting the patched residual stream and checking that the lag persists). It is currently an explanatory hypothesis presented as a finding.

### Trivial
- The 0.01 thresholds for sum and difference of projected probabilities in Sec. 5 are unmotivated; a brief sensitivity check would help.
- "Specific specific" appears in Sec. 1 (a duplicate word in the introduction).

## Nice-to-Haves
- Run the same pipeline on at least one additional consistent instruction-tuned model (e.g., Mistral-Instruct, Llama-3-Instruct, Qwen-Instruct) so the "single middle layer / sparse heads" picture rests on more than two models.
- A 4-way replication of the localization analysis with an n>2-compatible metric, even if only on a subset of MMLU.
- An intervention experiment: edit the late-layer alignment heads in the OOD-symbol pathway to test whether weaker models' C/D failures can be repaired — this would convert a descriptive finding into an actionable one.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh critic's complaint about 4-way replication being absent and binarization being a "hidden confound."* The paper explicitly motivates the binary reduction in Sec. 3 (the discriminativity metric used in Sec. 5 collapses for n=2; n>2 cases are deferred to the appendix). Kept a softened version under Minor as a request to discuss external validity, but the framing as a structural confound overstates the issue since it is methodological scoping, not concealment.
- *"Vocabulary projection has known limitations / no tuned lens."* This is a fair generic critique of logit-lens-style work, but the paper triangulates projection with activation patching (the entire point of Sec. 4) and uses projection diagnostically rather than as primary causal evidence. Folded into the Minor "show variance" note rather than retained as a distinct objection.
- *"Statistical reporting / no error bars on projection plots."* Single-instance average probability traces over hundreds of items are standard in this subfield; demanding confidence intervals as a blocking issue is field-norm overreach. Kept as a Minor "show per-instance distributions" suggestion instead.
- *Strength Finder's "rigorous model selection and analysis controls."* The 70% / consistency filter is what produces the N=2 problem flagged above; presenting it as a strength conflicts with a verified weakness, so per the rule the weakness wins.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel observations — the head-role typology refining "correct letter heads," the training-checkpoint window where formatted-MCQA capability emerges, and the OOD two-stage processing in Olmo — are all the paper's own.

## Suggestions
- Rewrite the abstract and contribution list to scope the "single middle layer" claim to Olmo-7B-SFT and report the diffuse 6-layer window for Llama2-13B-Chat; treat the cross-model generalization as a hypothesis.
- Add a head-ablation experiment in Sec. 5: zero/mean-ablate each of the 13 identified heads and report the resulting change in p(A)−p(B). This is the single most leverage-positive addition.
- Add at least one more consistent instruction-tuned model to break out of the N=2 setup, even if it's a smaller-scale replication.
- Add a label-bias control in Sec. 6 distinguishing "cannot separate A/B" from "predicts B regardless," e.g., by re-weighting or steering interventions on the 350B checkpoint at layer 29.
- Briefly discuss external validity of the binary reduction and what (if anything) changes qualitatively under the n>2 metric in the appendix.

## Evaluation by axis
- **Originality:** Moderate-to-good. The Colors task, the training-window finding, and the four-role head typology are non-trivial extensions of Lieberum et al. and the logit-lens literature.
- **Importance:** Reasonable. Understanding how MCQA-format scoring works is genuinely useful given how widely benchmarks like MMLU drive model development.
- **Support for claims:** Mixed. Localized claims for Olmo-7B-SFT are supported; the broader cross-model framing in the abstract is not.
- **Soundness of experiments:** Adequate but missing the head-ablation that the paper's own logic invites.
- **Clarity:** Clear, well-organized, with informative figures.
- **Value to community:** Solid incremental contribution; the synthetic task and checkpoint analysis are likely to be reused.

## Score and Decision
The paper makes real and useful contributions but overclaims its central mechanistic story relative to what a 2-model, binarized analysis can support, and the head typology — its strongest novel empirical finding — is not causally validated by ablation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>