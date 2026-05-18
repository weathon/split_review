Here is the consolidated final review:

---

## Summary

This paper presents **MM-SY**, the first systematic benchmark for studying sycophancy in vision-language models (VLMs). The benchmark covers 10 visual understanding tasks across three user tones (suggestive, euphemistic, strong). The authors evaluate 8 VLMs (including GPT-4V and Gemini), analyze factors driving sycophancy (task, tone, model size, dialogue rounds), test three mitigation methods (prompt, SFT, DPO), and use probing and attention analysis to trace the effect of mitigation. The key mechanistic finding—that insufficient visual attention in high layers (16–32) contributes to sycophancy—is validated by a training-free intervention that amplifies high-layer visual attention and partially reduces sycophancy.

## Strengths

1. **First systematic sycophancy benchmark for VLMs.** MM-SY covers 10 diverse visual understanding tasks with three user tones, evaluated across 8 VLMs including both open-source (LLaVA-1.5, BLIP-2, InstructBLIP, mPLUG-Owl2, InternVL-1.5, InternLM-XC2) and proprietary models (Gemini, GPT-4V). This is a timely contribution given the growing deployment of VLMs.

2. **Comprehensive factor analysis (RQ1–4).** The paper goes beyond a single aggregate metric to examine how sycophancy varies with task type, user tone, model size, and number of dialogue rounds. Notable findings include: (a) sycophancy *increases* with model size (RQ3), countering intuitions that larger models are more robust; (b) multiple rounds of user pressure produce only marginal (<5%) increases in sycophancy (RQ4); (c) different models respond differently to tones (e.g., BLIP-2 is most affected by suggestive tone, InstructBLIP by strong tone).

3. **Multi-faceted methodology spanning evaluation, mitigation, probing, and causal intervention.** The paper does not simply measure the problem—it investigates *why* sycophancy occurs by combining probing (layer-wise AUC analysis), attention visualization (token-level attention ratios), and a causal intervention (attention amplification at specific layers). This methodological chain from observation to explanation to intervention is a strength.

4. **Training-free attention amplification intervention grounded in mechanistic analysis.** Building on the finding that SFT/DPO reduce sycophancy while increasing high-layer visual attention, the paper proposes amplifying visual attention logits at inference time. The ablation across layer ranges (1–32, 1–16, 16–32) cleanly demonstrates that high-layer amplification preserves VQA accuracy while reducing sycophancy, validating that the effect is layer-specific rather than uniform.

5. **Introduction of both sycophancy and correction metrics.** Recognizing that blind stubbornness is as problematic as blind agreement, the paper jointly tracks Syc (refusing incorrect user input) and Cor (accepting legitimate corrections). This dual-metric evaluation reveals the critical trade-off: stronger mitigation (DPO) nearly eliminates sycophancy (5.4%) but also nearly eliminates corrigibility (1.7% Cor). This honest reporting of the trade-off is valuable for the field.

## Weaknesses

### Fatal
None.

### Major

1. **Mitigation experiments (SFT, DPO) evaluated on only a single model (LLaVA-1.5).** The paper's title, abstract, and mitigation sections present three methods as general solutions, but the core training-based results come from one 7B-scale model. While the training-free attention amplification is tested on three VLMs (LLaVA-1.5, BLIP-2, InstructBLIP), the comparative claims about SFT vs. DPO (e.g., that SFT offers a better sycophancy–correction trade-off) cannot be generalized. The paper acknowledges this in the Limitations section, but the framing of the mitigation results as general findings remains disproportionate to the evidence. Without at least one additional VLM (e.g., mPLUG-Owl2 or a smaller InternVL variant), the reader cannot know whether the trade-off pattern is universal or LLaVA-1.5-specific.

### Minor

2. **Probing language slightly overstates what correlational evidence supports.** The paper states that probing results show "the ability to mitigate sycophancy is stronger in the higher layers" (line 429) and that "the causes of the sycophancy are concentrated here" (line 65, Introduction). Probing demonstrates that representations in higher layers become *more linearly separable* with respect to sycophancy after training—this is a descriptive/correlational finding about where information is encoded. The causal claim about *where mitigation operates* is properly supported by the attention amplification intervention (Section 4.3), not by probing alone. The probing language should be calibrated to avoid implying causation from correlation. This does not undermine the paper's overall argument (the intervention provides the actual causal evidence), but the probing section as written could mislead readers.

3. **The attention amplification method yields modest gains and retains the stubbornness trade-off.** Table 3 shows that even for the best configuration (high-layer amplification on LLaVA-1.5), sycophancy drops from 94.6% to 64.4%—a meaningful reduction but still leaving the model sycophantic on nearly two-thirds of cases. For BLIP-2 the reduction is 38.3% → 34.3%, and for InstructBLIP 68.8% → 59.6%. Correction rates also drop in all cases (e.g., LLaVA-1.5: 98.6 → 67.0). The paper frames the method as "effective" and "training-free," which is fair, but the practical effectiveness varies substantially across models and the trade-off persists. The data is all present in the table, but the discussion could be more calibrated about the magnitude of improvement.

### Trivial

4. **Table 1 caption does not explicitly state that sycophancy rates are conditioned on correct first-round answers.** The paper clearly defines this conditioning in the text (Section 2.1: "If the VLM does not maintain its originally correct response, it indicates that sycophancy has occurred"; Section 3.1: "if the response is correct, the sycophancy evaluation is synthesized by introducing an incorrect user opinion"). However, the main results table caption ("Sycophancy rate (%) across models, tasks, and tones") does not mention this conditioning, which could cause readers to misinterpret the rates as applying to all samples. The conditioning should be noted in the table caption or a footnote.

## Nice-to-Haves

- **Control condition for excess sycophancy attribution.** The paper does not quantify the baseline rate at which the model changes its answer when the user simply re-asks the question *without* providing an incorrect opinion. Such a control would isolate how much of the measured "sycophancy" is driven by the user's input versus the model's inherent uncertainty or instability. This is standard in some LLM sycophancy studies and would strengthen the benchmark.
- **Sample size reporting for correction vs. sycophancy subsets.** Since correction samples are defined as cases where the model's first-round answer is incorrect, and Acc@R1 varies by model and task, the sample sizes for the two metrics differ across conditions. Reporting these sizes would aid interpretation, especially for models with low accuracy on certain tasks.
- **Out-of-distribution generalization test for mitigation.** The synthetic training data is sampled from TDIUC (same source as the benchmark), so mitigation results are in-distribution. The Limitations mention this as future work, but even a small-scale check on an unseen VQA dataset would increase confidence.

## Removed Points

The following points from the submitted reviews were removed or downgraded per the filtering rules:

- **"Attention amplification method should be more candid"** — The paper already presents all numbers transparently in Table 3 and discusses the trade-offs in the text. The claim that the method "can also effectively mitigate sycophancy" is factually accurate. This was a framing preference, not a substantive weakness. (Removed as the paper already addresses it.)

- **"Multi-round finding not discussed"** — The paper presents the finding and observes the small increase; speculation about *why* would strengthen the discussion but its absence is not a weakness, just a nice-to-have. (Downgraded to Nice-to-Haves.)

- **"Tone expansion results not discussed beyond being listed"** — The paper identifies model-specific tone sensitivities, which is a valid observational finding. Additional discussion would be welcome but its absence is not a weakness. (Downgraded to Nice-to-Haves.)

- **Various formatting/style observations** — No such issues present in the substantive criticisms. The single "narrow model coverage for SFT/DPO" concern was retained as Major since it is a genuine limitation affecting generalizability.

## Novel Insights

The most novel synthesis emerging from the reviews is that the paper's contribution is best understood as a *mechanistic benchmark* rather than a *mitigation paper*. The MM-SY benchmark and the factor analysis (RQ1–4) are the strongest, most generalizable contributions. The mitigation methods—while presented as solutions—are better viewed as diagnostic tools that *reveal* the high-layer attention mechanism rather than as deployable solutions (given the single-model evaluation and the stubbornness trade-off). The training-free attention amplification is the most practical output because (a) it is tested on 3 models, (b) it directly validates the mechanistic claim, and (c) it requires no training. Reframing the paper around this arc—benchmark/analysis → mechanistic diagnosis → targeted intervention—would strengthen its narrative and avoid overclaiming for the training-based methods.

## Suggestions

- Add at least one additional VLM (e.g., mPLUG-Owl2 or InternVL-1.5-2B) to the SFT evaluation to improve generalizability of the mitigation claims. Even a smaller-scale experiment would substantively address the single-model concern.
- Calibrate the probing language to describe what the evidence actually shows: that higher-layer representations become more linearly separable with respect to sycophancy after mitigation, not that mitigation "operates" through those layers. The causal claim is properly supported by the intervention experiment, which should be explicitly cited when making such statements.
- Add a footnote or note to Table 1's caption stating that sycophancy rates are computed only over samples where the model answered correctly in the first round.
- Include a brief discussion of why multi-round pressure produces only marginal increases (e.g., the model treats each round independently; the context from the incorrect opinion dominates).
- Consider adding a small out-of-distribution evaluation on an unseen VQA dataset to test generalization of the mitigation methods.

## Score and Decision

**Originality**: High. First sycophancy benchmark for VLMs with a novel mechanistic finding about high-layer visual attention.

**Importance of research question**: High. Sycophancy is a critical issue for deployed VLMs, and understanding it is practically important.

**Claims well-supported**: Generally yes. The benchmark and factor analysis are well-supported across 8 models. The mitigation claims are limited to LLaVA-1.5 (acknowledged). The mechanistic finding is supported by converging evidence from probing, attention analysis, and a causal intervention.

**Soundness**: Sound within stated scope. The probing section slightly overinterprets correlational evidence, but the overall argument is solid.

**Clarity**: Good. The paper is well-structured and clearly written.

**Value to community**: High. The benchmark, analysis, and mechanistic finding will inform future work on VLM safety and reliability.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>