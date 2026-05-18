Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes **MultiTrust**, a framework that trains separate 7B "safety auxiliary models" for three trustworthiness perspectives (adversarial robustness, fairness, truthfulness) and combines them with a base LLM at inference time via a perplexity-based router and logit ensembling. The key ideas are: (1) training specialized auxiliary models independently to avoid the forgetting problem that arises from sequential fine-tuning, (2) using a perplexity-based router to select which auxiliary model to use per input, and (3) combining base and auxiliary model logits without modifying the base model. Results show notable trustworthiness improvements across 7B and 13B base models (e.g., Llama2-13B from 35.54% to 51.14% average score) with minimal drop on helpfulness benchmarks.

---

## Strengths

1. **Consistent and sizable trustworthiness improvements across multiple base models.** MultiTrust raises the average trustworthiness of Llama2-13B by ~15 points and Vicuna-13B by ~23 points (Table 1, Section 3.2). The same set of 7B auxiliary models improves three different base models (Vicuna-7B, Vicuna-13B, Llama2-13B) without retraining, demonstrating that the framework transfers across model families and sizes.

2. **Well-structured ablation studies validate design choices.** The paper systematically shows that: (a) fine-tuning on a data mixture is suboptimal compared to separate training (Table 2), (b) SFT+DPO outperforms either technique alone (Table 3), (c) the perplexity-based router nearly matches an oracle selector at the aggregate level (Table 4), and (d) cross-perspective benefits exist (e.g., truthfulness auxiliary model helps fairness — Table 5). These ablations provide solid empirical grounding.

3. **The approach directly addresses the forgetting problem.** Figure 2 demonstrates the degradation that occurs with sequential fine-tuning on multiple perspectives. MultiTrust's separate training + inference-time routing avoids this non-destructively, which is a clean and practical solution to a well-known challenge.

4. **Rigorous data generation for each perspective.** Adversarial data uses five distinct attack algorithms adapted for LLMs (78,715 examples); fairness data balances sensitive attributes across Adult and Crime datasets; truthfulness data leverages the GRATH iterative pipeline. This thorough data construction is a concrete contribution in itself.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to using the auxiliary models alone.** MultiTrust combines a base LLM with a safety auxiliary model via logit ensembling and routing. However, the paper never reports the performance of the standalone auxiliary models (the 7B Llama-2-Chat-7B models fine-tuned with SFT+DPO) on the trustworthiness benchmarks. If the auxiliary models alone already achieve similar or better scores, the added complexity of the base model, router, and ensembling is not justified. This comparison is necessary to isolate the value of the full framework. Given that the auxiliary models are also 7B, comparing a 7B+7B system against a single 7B auxiliary model would be a fair and informative baseline.

2. **Router behavior is evaluated only at the aggregate level, not analyzed per-instance.** The paper compares MultiTrust's router to an oracle (Table 4) and shows a small gap, which the paper interprets as the router being "effective and accurate." However, no confusion matrix, per-instance selection distribution, or qualitative examples of when each auxiliary model is chosen are provided. The paper itself notes that the router sometimes selects a different perspective's model and *surpasses* the oracle — this is interesting but raises the question of what the router is actually doing. Is it selecting by perspective alignment, or by incidental properties like domain similarity or language style? Without per-instance analysis, the router's behavior is a black box, and the claim that it "intelligently selects the most appropriate safety auxiliary model based on the input query" (Section 2.3) is only weakly supported.

### Minor

3. **Evaluation is limited to constrained (classification / multiple-choice) tasks.** All trustworthiness metrics come from SST-2/QQP/MNLI classification (adversarial robustness), Adult/Crime prediction (fairness), and TruthfulQA MC1/MC2 (truthfulness). The paper does not evaluate on open-ended generation safety scenarios that are central to real-world LLM deployment — generating harmful content, refusing malicious instructions, or avoiding biased language in free-form text. While the paper scopes itself to these benchmarks, the title and abstract claim broader "safety and trustworthiness" enhancement, and the logit-level intervention would affect free-form generation. Including even one open-ended evaluation (e.g., refusal rate on harmful requests) would substantially strengthen the safety claims.

4. **Key parameters are unspecified.** The weighting factor γ in the logit combination (Equation 2) — which controls the trade-off between trustworthiness and general performance — is never given a value or shown in a sensitivity analysis. The DPO β parameter is also not specified. These are central to reproducing the method.

5. **Computational overhead of the router is not discussed.** The router must compute perplexity under all three 7B auxiliary models for every input query before generation — this triples the encoding cost. The paper does not acknowledge this trade-off or discuss whether a simpler heuristic might suffice.

6. **The data generation methodology may introduce label leakage.** Adversarial data is generated by attacking Llama-2, and the auxiliary models are also trained from Llama-2-7B-Chat. The paper does not discuss whether the adversarial patterns are model-specific and whether performance on DecodingTrust (which may use different attack methods) reflects genuine generalization.

### Trivial

7. **Wording inconsistency: "averaging the logit outputs" vs. addition of log-probabilities.** The abstract states that the router works by "averaging the logit outputs of the selected safety auxiliary model and the base model," but Equation (2) shows addition of log-probabilities (`log π_base + γ log π*`), which is multiplication in probability space, not averaging. This should be harmonized.

---

## Nice-to-Haves

- A sensitivity analysis of the γ parameter showing how the trustworthiness-helpfulness trade-off varies with different values.
- Ablation comparing the perplexity-based router to simpler alternatives (e.g., random selection, always pick a fixed auxiliary model) to demonstrate that the routing complexity is warranted.
- Evaluation on open-ended generation safety benchmarks (e.g., HarmBench, or a red-teaming-style refusal-rate evaluation).
- Qualitative examples of inputs routed to different auxiliary models, with analysis of why the router's choice makes sense.

---

## Removed Points

These points were raised by reviewers but were removed or downgraded per the review policy:

- **"DPO formula has an incorrect minus sign inside the log sigmoid"** — Removed (factually incorrect). The paper's Equation (2) matches the standard DPO loss formulation exactly.
- **"Model forgetting experiment (Figure 2) is weak / well-known"** — Removed. The experiment is a straightforward motivation for the approach; demonstrating a known phenomenon does not weaken the paper.
- **"Missing learning rate, batch size, training epochs"** — Removed per hard rule (nitpicks about undisclosed hyperparameters). The paper reports SFT for 1 epoch and DPO for 1,000 steps, which is reasonable for a conference submission.
- **"Scalability only tested to 13B"** — Downgraded. Testing on 7B and 13B with consistent improvements is a reasonable scope for an academic paper.
- **"The 'outperforming models with similar and even larger sizes' claim is overstated"** — Downgraded. MultiTrust-Vicuna-7B (~14B effective parameters) outperforming Vicuna-33B (33B single model) is a legitimate finding, not overstated.

---

## Novel Insights

**The cross-perspective analysis (Table 5) is the paper's most interesting finding, and it partially undermines the paper's own framing.** The paper presents the router as selecting the "appropriate" perspective, but Table 5 shows that the truthfulness auxiliary model improves fairness scores more than the fairness auxiliary model does (49.38 vs. 43.20). This suggests the router's job may not be "select the right perspective for the task" but "find which auxiliary model happens to produce the best output for this input" — and the perplexity heuristic may be exploiting unrelated properties (e.g., training data domain similarity, language style) rather than perspective alignment. Neither framing is wrong, but the paper's current language implies the former while the evidence better supports the latter. This tension is worth exploring explicitly.

---

## Suggestions

1. **Add the missing baseline: report standalone auxiliary model performance on all three trustworthiness perspectives.** This is the single most important missing experiment. If the auxiliary model alone is competitive with the full MultiTrust system, reframe the contribution as "a way to preserve helpfulness while adding safety" rather than "a way to improve trustworthiness."
2. **Provide per-instance router analysis.** Show, for a sample of evaluation instances, which auxiliary model was selected and why. A confusion matrix showing selection distribution per evaluation perspective would clarify what the router is actually doing.
3. **Report and justify the γ value**, ideally with a sensitivity sweep showing how trustworthiness and helpfulness vary with γ.
4. **Add at least one open-ended safety evaluation** (e.g., measuring refusal rates on harmful queries from HarmBench or similar).
5. **Discuss the computational overhead** of the three-pass perplexity computation and consider whether a cheaper alternative (e.g., a small classifier trained to mimic the router) would suffice.

---

## Score and Decision

**Originality:** 6/10 — The idea of training separate auxiliary models and routing at inference is practical but not highly novel; similar composition-based approaches exist.

**Importance of research question:** 8/10 — Multi-perspective trustworthiness is a critical and timely problem.

**Claims well-supported:** 5/10 — Core improvement claims are supported, but the router claims and framework justification are only partially supported due to missing comparisons and analysis.

**Soundness of experiments:** 5/10 — Good ablations but missing key baselines (standalone auxiliary models) and limited evaluation scope.

**Clarity of writing:** 6/10 — Generally clear but has inconsistencies (averaging vs. addition) and missing parameter details.

**Value to research community:** 6/10 — The framework is practical and the cross-perspective findings are useful, but the missing baselines limit confidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>