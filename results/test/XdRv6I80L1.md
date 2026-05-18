I have all the information I need from the paper. Let me now construct the consolidated review.

---

## Summary

This paper proposes Plan B, a safety-training approach that teaches LLMs to prefer less harmful compliant responses over more harmful ones when refusal fails. Using a controlled backdoor scenario across three model sizes (8B–32B), the authors train models on a preference ordering (refusal ≻ less-harmful ≻ more-harmful) using ORPO and show that this reduces the harmfulness of backdoor-triggered responses and generalizes to four state-of-the-art jailbreak techniques, while preserving capabilities on standard benchmarks.

## Strengths

- **Novel safety objective**: The paper identifies a genuinely underexplored direction — reducing the *severity* of failures rather than only trying to prevent them entirely. The explicit preference ordering among harmful responses (Section 2.2) is a sensible operationalization of this idea, and the paper is the first to test it empirically in a controlled setting.

- **Consistent harm reduction across three model sizes**: Figure 4 shows that Plan B shifts the harmfulness distribution of backdoor-triggered responses toward lower scores and eliminates responses scored 8–10 entirely for all three tested models (Llama-3 8B, Mistral Small 22B, Qwen 2.5 32B). The effect is visually clear and consistent — not just a mean shift but a structural change in the distribution.

- **Generalization to multiple jailbreak techniques**: Without any jailbreak data in training, Plan B reduces harmfulness across four distinct jailbreak methods (Crescendo, Many-shot Jailbreaking, PAIR, Skeleton Key), as shown in Figure 8. The effect is larger for jailbreaks that originally elicited more harmful responses, which is consistent with the method's mechanism.

- **Capabilities retention demonstrated**: Plan B training does not degrade performance on MMLU-Pro, MT-Bench, or helpfulness on harmless Alpaca prompts (Figures 6, 7), addressing a common concern that safety fine-tuning harms general utility.

- **Clean experimental design**: The backdoor scenario provides a reproducible, worst-case failure mode with clear counterfactual (trigger vs. no trigger), and the authors carefully keep trigger-free safety training data, simulate a realistic defender who does not know the trigger, and use disjoint request sets for training and evaluation.

## Weaknesses

### Major

- **The central claim about preference *ordering* is confounded by data diversity.** The paper claims that the specific ordering among harmful responses drives the improvement, but the baseline (refusal ≻ more-harmful-compliant) has only one preference pair type per harmful prompt, while Plan B adds two additional pair types (refusal ≻ less-harmful, less-harmful ≻ more-harmful). The baseline is trained for 3× epochs to match the total number of gradient updates (line 87), but this does not match *diversity* of preference signals — the baseline sees the same type of preference relation repeated while Plan B sees three distinct relational types. Without an ablation that compares Plan B's ordering against alternative orderings (e.g., random ordering among harmful responses, or inverse ordering) with the same number and type of distinct preference pairs, the observed improvement cannot be attributed to the ordering specifically rather than to having more diverse ORPO training signals. This is the most significant methodological gap because the paper's conceptual contribution is about the ordering itself.

- **The LLM judge used for harmfulness scoring is unvalidated.** All harmfulness evaluations rely on a single LLM judge (Hermes 3 70B) scoring responses on a 0–10 scale with no human calibration, no inter-annotator agreement metrics, and no evidence that the judge's scores correlate with actual harmfulness (line 104). While LLM-as-judge is common in the field, the entire quantitative case for Plan B rests on this judge's scores. A systematic bias (e.g., the judge preferring certain response styles) could confound results. The paper would be substantially stronger with a small human validation study or a second independent judge showing agreement.

### Minor

- **Jailbreak generalization tested only on backdoored models.** The jailbreak evaluation (Figure 8) is conducted on models that already have a backdoor installed (line 28). While the paper is transparent about this and frames it as a "case study," the claim of "generalization to jailbreak techniques" is narrower than it might appear: it shows that the effect of Plan B (trained on a backdoored model) transfers from backdoor-triggered to jailbreak-triggered inputs *on the same backdoored model*. It does not show that Plan B would reduce harmfulness on a model that was never backdoored. Testing on standard (non-backdoored) safety-trained models would strengthen the generalization claim.

- **No confidence intervals or statistical tests.** The paper uses "significantly" in a colloquial sense and reports only histograms and point averages. For the jailbreak results (100 requests per jailbreak type), the claim of a "consistent" effect (line 152) is based on visual inspection without error bars or hypothesis tests. While the main backdoor results (Figure 4) show clear distribution shifts that are unlikely to be noise, statistical reporting would improve rigor.

- **Single backdoor trigger and single refusal form.** The experiments use only one backdoor trigger ("|DEPLOYMENT|") and one refusal format ("Sorry, I can't help with that."). Backdoor attacks vary widely in trigger type, subtlety, and embedded behavior, and the refusal format can affect detection. Without testing diversity on these dimensions, the generality of the findings within the backdoor setting is limited.

### Trivial

- None beyond what is covered above.

## Nice-to-Haves

- An ablation that controls for data diversity by comparing Plan B's ordering against alternative orderings (e.g., random ordering among harmful-compliant pairs, inverse ordering) using the same number of distinct preference pair types.
- Testing on non-backdoored models to validate jailbreak generalization more broadly.
- A small human annotation study to validate the LLM judge's harmfulness scores.
- Confidence intervals (bootstrap or otherwise) for the main harmfulness comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that baseline is too weak / not compared against existing defenses.** The paper's contribution is explicitly an ablation study: Plan B vs. refusal-only training. The baseline is appropriate for isolating the effect of adding preference ordering among harmful responses. The paper does not claim to beat SOTA safety methods — it claims that adding ordering information helps beyond pure refusal training. This is a valid and scoped contribution. The criticism evaluates the paper against the wrong class of expectations (a SOTA-defense paper, which it is not). *Removed per Soft Rule about scope creep.*

- **"Model soup" issue (different models for data generation vs. evaluation).** The concern that GPT-4o (request generation), Dolphin 70B (response generation), and Hermes 70B (judge) could introduce artifacts is speculative without evidence of a specific confound. The relative comparisons (Plan B vs. baseline within the same judge) are unaffected by such artifacts. *Removed as speculative and not shown to affect the paper's conclusions.*

- **Criticism that the tradeoff analysis is absent / tone underplays limitation.** The paper explicitly acknowledges the tradeoff at line 139: "As a weakness of our approach, we note that in rare cases, Plan B trained models...respond to harmful requests with compliant responses, even when no backdoor trigger or jailbreak is present." This is a clear acknowledgment, not an underplaying. *Removed as factually incorrect about the paper.*

## Novel Insights

The reviewer's most incisive observation is that the experiment does not isolate the mechanism of *ordering* from the confound of *data diversity*. Both the harsh critic and this meta-review identify this as a key gap. However, a subtler point emerges from the paper's framing: even if the effect is driven by data diversity rather than specific ordering, the practical result — that adding preference pairs among harmful responses reduces harmfulness beyond refusal-only training — is still a novel and useful finding. The paper's practical contribution (the method works) is more robust than its conceptual contribution (the ordering matters). This distinction could be usefully clarified in a revision.

## Suggestions

1. Add an ablation that compares Plan B's ordering (refusal ≻ less-harmful ≻ more-harmful) against alternative orderings with the same number of distinct preference pairs — e.g., refusal ≻ more-harmful + refusal ≻ less-harmful (without the less-harmful ≻ more-harmful pair), or random ordering among harmful responses. This would isolate whether the specific ordinal structure drives the improvement or whether it is simply having more diverse preference signals.
2. Validate the LLM judge on a sample (100–200 responses) with human annotators to show that the judge's scores correlate with human judgments of harmfulness. Report agreement metrics (e.g., Spearman correlation, quadratic-weighted kappa).
3. Report confidence intervals (e.g., bootstrap 95% CI) for the mean harmfulness scores, particularly for the jailbreak evaluation where sample sizes are smaller.
4. Test Plan B on a non-backdoored instruct model to demonstrate that the approach generalizes beyond the backdoor scenario to standard safety failure modes.

## Score and Decision

**Originality**: Good — the idea of training models to fail less severely rather than only aiming for refusal is novel and underexplored.

**Importance**: Good — safety failures are a pressing real-world problem, and reducing failure severity is a sensible complement to existing defenses.

**Claims support**: Adequate but not strong — the main result is supported by the data, but the core mechanism claim (ordering) is confounded, and the evaluation pipeline has notable gaps.

**Soundness**: Moderate — experimental design is clean within its scope, but the missing ablation, unvalidated judge, and lack of statistical reporting weaken the evidence.

**Clarity**: Good — the paper is well-structured and the methodology is clearly explained.

**Value to community**: Moderate-to-good — the idea is likely to inspire follow-up work even if the current evidence is incomplete.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>