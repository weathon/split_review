I have now thoroughly read the paper and verified all claims made by both the harsh critic and strength finder against the actual paper content. Let me construct the consolidated review.

---

## Summary

This paper critically examines the claim that LLMs can self-correct their own reasoning. It defines *intrinsic self-correction* (self-correction without external feedback or oracle labels) and systematically evaluates it across GPT-3.5, GPT-4, GPT-4-Turbo, and Llama-2 on GSM8K, CommonSenseQA, and HotpotQA. The central finding is that intrinsic self-correction consistently degrades reasoning performance across all tested models and benchmarks. The paper further shows that (a) multi-agent debate offers no advantage over self-consistency when inference costs are equalized, and (b) claimed self-correction gains in prior work often stem from suboptimal initial prompt design rather than genuine correction ability.

## Strengths

1. **Clearly defines and systematically tests intrinsic self-correction, showing consistent degradation across models.** The paper introduces a precise definition of intrinsic self-correction (Section 2) and evaluates it on four models across three benchmarks. Tables 2–4 show that in every setting without oracle labels, accuracy drops after self-correction (e.g., GPT-3.5 on GSM8K: 75.9% → 74.7%; Llama-2 on GSM8K: 62.0% → 36.5%; GPT-4 on GSM8K: 95.5% → 89.0%). The consistency across models and datasets makes the pattern compelling.

2. **Exposes the hidden reliance on oracle labels in prior self-correction work.** The paper replicates Kim et al. (2023) and Shinn et al. (2023) with oracle labels, showing large gains (Table 1: GPT-3.5 on GSM8K: 75.9% → 84.3%). When oracle labels are removed, the gains vanish and performance drops (Section 3.2). This directly challenges the validity of claims in those prior papers.

3. **Demonstrates that multi-agent debate does not outperform self-consistency when inference costs are equalized.** Table 5 shows that self-consistency with 9 responses reaches 88.2% while multi-agent debate with 9 responses reaches only 83.0%. This exposes an unfair comparison in prior work (Du et al., 2023) and shows that observed "debate" gains are attributable to ensembling, not correction.

4. **Identifies suboptimal prompt design as a confound in self-correction evaluations.** Section 5 uses the Constrained Generation task from Madaan et al. (2023) to show that improving the initial prompt (adding "include *ALL* concepts") raises standard prompting from 44.0% to 81.8% (Table 6), far surpassing the 67.0% reported after self-correction. When self-correction is applied to the improved prompt, performance drops to 75.1%. This cleanly demonstrates that claimed self-correction gains were artifacts of weak initial instructions.

5. **Provides mechanistic analysis of why performance degrades.** Figure 1 shows that the most common answer change after self-correction is "Correct → Incorrect" across all models and datasets. This pinpoints the root cause: LLMs cannot reliably judge the correctness of their own reasoning, so self-correction primarily introduces errors rather than fixing them.

6. **Offers concrete, actionable guidelines for future research.** The conclusion (Section 6) gives three specific, evidence-backed recommendations: leverage external feedback when available, compare against cost-equivalent baselines like self-consistency, and invest equal effort in initial prompt design.

## Weaknesses

### Fatal
None.

### Major
None. All weaknesses below are addressable and do not undermine the paper's core contributions.

### Minor

1. **Title overreaches the tested scope.** The title "Large Language Models Cannot Self-Correct Reasoning Yet" is broader than what the experiments actually cover. The paper tests one specific paradigm (generate → feedback → refine) with a limited set of feedback prompts, operationalized as the three-step prompting strategy described in Section 3.1. While the paper internally defines intrinsic self-correction precisely (Section 2) and its Limitations section (Section 7) acknowledges that self-correction may work in non-reasoning domains, the title and abstract do not carry this same caveat. The evidence shows this *particular paradigm* fails under the tested conditions; a title like "LLMs Cannot Self-Correct Reasoning Under the Generate–Feedback–Refine Paradigm" would better match the evidence. That said, the word "Yet" does imply temporal contingency rather than impossibility, and the paper's internal scope is well-defined.

2. **Absence of confidence intervals or statistical significance tests.** The paper reports point estimates without any uncertainty quantification. For GPT-3.5 on GSM8K (75.9% standard vs. 75.1% round 1 vs. 74.7% round 2), the differences are small enough to fall within sampling noise, especially without confidence intervals. The large-magnitude drops (e.g., Llama-2: 62.0% → 36.5%) are clearly meaningful, but the paper's strong language — "accuracies of all models drop across all benchmarks" — would be strengthened by statistical rigor, particularly for the smaller-sample comparisons (200 examples for GPT-4-Turbo and Llama-2; 100 for HotpotQA). The paper would benefit from reporting 95% confidence intervals via bootstrapping.

3. **Temperature asymmetry across models is acknowledged but undefended.** The paper uses temperature 1 for GPT-3.5/GPT-4 and temperature 0 for GPT-4-Turbo/Llama-2, stating this is "to provide evaluation across different decoding algorithms." Temperature 0 reduces output diversity, which could make it harder for the self-correction loop to produce different answers. This is not a fatal flaw — degradation still occurs — but it complicates cross-model comparisons and the reader cannot tell whether the degradation magnitude is partially an artifact of the temperature choice.

4. **Limited exploration of the feedback prompt space.** The paper tests three feedback prompts per model (Tables for GPT-4-Turbo and Llama-2). While all three show degradation, this does not exhaust the space of plausible feedback designs. The paper could strengthen its case by testing prompts that target specific failure modes (e.g., step-level verification: "Check whether each step of your reasoning is valid and correct any step that does not logically follow"). The paper's claim is an empirical observation, not a proof of impossibility, so this limitation is not fatal, but a broader diagnostic search would make the negative result more convincing.

### Trivial
None.

## Nice-to-Haves

- **Disentangle the feedback step from the refinement step.** The three-step pipeline (generate → produce feedback → refine) involves two LLM calls after initial generation. A "feedback-only" ablation or simply re-prompting the model for a second answer without feedback would help isolate whether the performance drop is due to the feedback structure or just from sampling a second (later) answer.
- **Include a self-consistency baseline in the intrinsic self-correction experiments.** The paper already shows self-consistency outperforms multi-agent debate (Section 4). Adding a self-consistency comparison in Section 3 would directly show that self-correction's degradation is not merely because it uses multiple calls.
- **Qualitative error-type analysis.** Figure 1 quantifies answer transitions, but a qualitative taxonomy of errors that are (rarely) fixed vs. (commonly) introduced would strengthen the mechanistic explanation and guide future work.

## Removed Points

The following points from the harsh critic were evaluated against the paper and removed with justification:

- **"The paper does not test alternatives like iterative refinement via different decoding seeds, self-consistency with verification, or chain-of-thought self-evaluation during generation."** — *Removed because the paper's scope is the generate–feedback–refine paradigm (the standard definition used in the literature being critiqued). Self-consistency is separately tested in Section 4 and shown to work well — as a different method, not as a form of "self-correction" under the paper's definition. Chain-of-thought self-evaluation during generation is a fundamentally different process outside the paper's scope.*

- **"The intuitive explanation (Section 3.4) is not experimentally supported."** — *The paper labels this as an "Intuitive Explanation," which is appropriate. It is presented as interpretation, not as an experimentally proven fact. The experimental support is in Figure 1 and the results tables.*

- **"A better control would be to ask the model to produce a second answer without any feedback."** — *Partially addressed by Figure 1's analysis of answer changes. Rephrased and moved to Nice-to-Haves as a suggestion, not a weakness.*

- **"Inclusion of more open-source models (e.g., Llama-3, Mistral)."** — *The paper already tests 4 models spanning two families (GPT and Llama). Adding more is scope creep. Moved to Nice-to-Haves.*

- **"The paper does not report the number of cases where the model changed its answer during the feedback step vs. the correction step."** — *Figure 1 analyzes overall answer changes after two rounds. The suggested finer-grained breakdown is a refinement, not a missing piece of evidence. Moved to Nice-to-Haves.*

## Novel Insights

The two reviews, taken together, surface an important tension: the paper makes a strong negative claim ("cannot self-correct") that is vulnerable on two fronts — the narrowness of the tested paradigm and the limited prompt search — yet neither reviewer identifies a specific condition under which the paper's results would reverse. The critic's call for "step-level verification prompts" is the most promising concrete direction, but even that would only test a variant of the same paradigm, not a fundamentally different approach. This suggests the paper's actual vulnerability is not that it missed a working configuration, but that the title overstates the generality of what is, in essence, a targeted critique of a specific pipeline that the community had been treating as general. The strongest path forward for the paper is to narrow the title to match the evidence, not to expand the experiments to match the title.

## Suggestions

1. **Revise the title** to reflect the tested paradigm, e.g., "Large Language Models Cannot Self-Correct Reasoning Under the Generate–Feedback–Refine Paradigm" or simply add a subtitle that qualifies the scope.
2. **Add confidence intervals** (via bootstrapping) for all main results in Tables 2–4, especially for the 200/100-sample evaluations. This would turn qualitative observations into quantitative claims.
3. **Provide a brief justification** for the temperature asymmetry, or better yet, run a subset of the GPT-4-Turbo/Llama-2 experiments at temperature 1 to confirm the degradation pattern holds regardless of temperature.

## Score and Decision

The paper makes a valuable, timely, and well-supported contribution. Its core experimental findings — that intrinsic self-correction degrades performance, that multi-agent debate is no better than self-consistency, and that prompt-design artifacts explain prior gains — are convincingly demonstrated. The weaknesses are minor and addressable: the title overreaches slightly, confidence intervals are missing, and the prompt space could be explored more broadly. None of these undermine the paper's central argument. The paper is clearly written, the experiments are sound, and the findings have significant implications for the community.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>