- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

MultiTrust proposes a framework for enhancing LLM trustworthiness by training separate "safety auxiliary models" for robustness, fairness, and truthfulness, then dynamically selecting and combining them with a base LLM at inference time via a perplexity-based router and logit ensembling. The key ideas are modularity (separate models per perspective), flexibility (adding new perspectives without retraining the base model), and inference-time routing that selects the appropriate auxiliary model. Applied to Vicuna and Llama-2-Chat models (7B and 13B), MultiTrust reports substantial trustworthiness gains on DecodingTrust and TruthfulQA benchmarks while incurring minimal degradation on standard multiple-choice reasoning benchmarks.

## Strengths

1. **Perplexity-based router achieves near-oracle selection accuracy.** Table 4 shows the dynamic router's performance gap vs. an oracle selector is ~1 point (e.g., Vicuna-7B: 52.60 vs. 53.25). This provides reasonable evidence that the router can identify the appropriate auxiliary model without supervision.

2. **Large and consistent trustworthiness improvements across model sizes.** Vicuna-13B average trustworthiness rises from 29.91% to 52.82%, Llama2-13B from 35.54% to 51.14%, and Vicuna-7B from 27.20% to 52.60% (Table 1). These gains hold across all three perspectives (robustness, fairness, truthfulness) and replicate across 7B and 13B scales.

3. **Minimal degradation on standard NLP benchmarks.** On ARC, HellaSwag, MMLU, and Winogrande, MultiTrust-aligned models show negligible changes from baselines (e.g., Vicuna-7B ARC: 53.92% → 53.58%), indicating the logit ensembling preserves general-task performance.

4. **Systematic ablation justifies the two-phase SFT+DPO design.** Table 3 shows SFT+DPO (70.07 avg) outperforms SFT-only (55.50) and DPO-only (64.78), supporting the design choice of the two-stage training pipeline.

5. **Empirical demonstration of key design motivations.** Figure 2 confirms model forgetting under sequential fine-tuning, and Table 2 shows separately trained models (44.98 avg) outperform a single model trained on mixed data (38.14). These directly motivate the modular architecture.

6. **Cross-perspective interaction analysis (Table 5) reveals interesting dynamics.** For example, the truthfulness auxiliary model boosts fairness scores (49.38 vs. base), and the robustness model achieves the highest cumulative score across all perspectives—suggesting that data diversity may be a factor in cross-perspective benefits.

## Weaknesses

### Fatal

None.

### Major

1. **Robustness evaluation does not test generalization to held-out tasks or attack types.** The robustness training data is generated from SST-2, QQP, and NLI tasks (line 24). The evaluation (Tables 3 and 4) reports sub-scores on the exact same task types (SST2, QQP, MNLI). While the paper uses different data instances (adversarial examples generated separately for training vs. DecodingTrust's evaluation set), evaluating on the same task distribution means the reported results may reflect in-distribution memorization rather than genuine robustness that would transfer to unseen tasks or attack types. The paper does not test on held-out adversarial scenarios (e.g., summarization, code generation, or different attack families). This limits the generality of the robustness claims.

2. **Fairness training data is narrow and mismatched to the evaluation construct.** The fairness auxiliary model is trained on only two UCI tabular datasets (Adult, Crime, ~8k instances) converted to binary classification tasks (income prediction, crime prediction) with flipped sensitive attributes. The evaluation uses DecodingTrust's fairness section (reported as Zero-shot/Few-shot sub-scores in Table 4). The paper provides no evidence that training on binary classification from tabular data transfers to the broader fairness construct being evaluated (which likely involves stereotype bias, demographic parity in text generation, etc.). Large reported gains (e.g., Vicuna-13B: 16.22 → 43.40) may reflect improvements on metrics correlated with the narrow training setup rather than genuine fairness improvements in open-ended generation.

### Minor

3. **Helpfulness evaluation does not cover conversational quality.** The paper claims "minimal impact on helpfulness" but only evaluates on four multiple-choice benchmarks (ARC, HellaSwag, MMLU, Winogrande). For chat models (Vicuna, Llama-2-Chat), helpfulness is primarily about instruction following, conversational coherence, and refusal behavior—dimensions not captured by static multiple-choice tasks. Adding an instruction-following benchmark (e.g., MT-Bench, AlpacaEval) would substantiate the claim.

4. **Key hyperparameter γ never specified or ablated.** The weighting factor γ in Equation (2) controls the strength of the safety auxiliary model's influence on the final logits. The paper describes it as balancing trustworthiness vs. helpfulness (lines 71–73) but never reports its value, whether it is tuned per perspective, or how sensitive results are to this choice. This is a significant gap for reproducibility and understanding the method's behavior.

5. **Router analysis is shallow.** The paper only reports the oracle gap (Table 4) but provides no analysis of routing decisions. Questions left unanswered: What fraction of inputs is routed to each auxiliary model? Does the router ever select the same model for all inputs (which would also yield a small oracle gap if one model dominates)? Is the perplexity criterion actually selecting the model most relevant to the safety perspective, or is it acting as a proxy for domain/surface-form similarity? A confusion matrix or qualitative examples would strengthen the claim that the router performs principled selection.

6. **Controlled baselines are informative but incomplete.** While Table 2 compares mixed fine-tuning (FT_mix) against separate models, and Table 1 compares against open-access models, the paper does not directly compare MultiTrust's full pipeline (separate models + routing) against a single DPO model trained on all three perspectives with the same base architecture. This comparison would most directly isolate the benefit of modularity + routing over monolithic safety tuning.

### Trivial

None.

## Nice-to-Haves

- An ablation of γ values and their effect on the trustworthiness-helpfulness trade-off would strengthen the exposition.
- The paper could analyze routing behavior qualitatively (e.g., examples of inputs routed to each auxiliary model) to build intuition.
- Reporting confidence intervals or variance estimates (even if single-seed runs are standard) would help readers assess result stability.

## Removed Points

These points were flagged by reviewers but are excluded or demoted from the main review for the reasons given below:

- **"Circular evaluation" framing (Harsh Critic #1).** The critic claimed evaluation is "circular" because training and evaluation tasks overlap. This is misleading: the paper trains on adversarially perturbed instances of SST-2/QQP/MNLI and evaluates on *different instances* from DecodingTrust (which covers the same task types). This is standard in-distribution robustness evaluation, not circular. The valid kernel (no held-out task generalization) is retained as Major weakness #1 above.

- **"No comparison with standard safety alignment baselines" (Harsh Critic #4).** The paper does compare against FT_mix (a single model trained on all perspectives) in Table 2, which is exactly the controlled baseline the critic requests. The critic missed this. The remaining concern about missing a direct DPO-on-all-perspectives comparison is retained as Minor weakness #6.

- **"Statistical significance / confidence intervals not reported."** This is a generic criticism applicable to most large-scale LLM evaluation papers. Single-run evaluation is standard in this literature. Not a meaningful weakness for this paper specifically.

- **"Data contamination between training and evaluation."** Overlaps with weakness #1 (same task types). Not independently actionable.

- **"Router only uses input, not partial output" / multi-turn limitation.** The paper does not claim support for multi-turn conversations, and the scope is single-turn. This is speculation about an unaddressed extension, not a flaw in what the paper does claim.

- **"Missing related works."** Not permitted to include—cannot verify which works are absent without external knowledge.

- **"Typos/formatting/style nitpicks."** These are parser artifacts, not author errors.

- **Generic strengths from Strength Finder.** The Strength Finder's generic framing ("this paper addresses an important problem") was dropped. Only evidence-grounded strengths were retained.

## Novel Insights

The interaction between the Strength Finder and Harsh Critic reveals that the paper's most interesting finding may lie not in the headline performance numbers but in the cross-perspective interaction analysis (Table 5). The Harsh Critic dismissed this as "not drawing strong conclusions," but the data shows that the robustness auxiliary model achieves the highest cumulative score across all perspectives—not just robustness. This suggests that data diversity (five tasks, multiple attack types) during training may produce auxiliary models with broader safety benefits than narrow task-specific training, an observation that cuts against the paper's own modularity thesis. Conversely, the truthfulness auxiliary model (trained on only 2,184 examples from a single dataset) shows the weakest cross-perspective transfer, hinting that data scale and diversity may be more important than perspective-specific specialization. This tension—between the paper's modular framing and the apparent importance of training data diversity—is underexplored and could be a productive direction for future work.

## Suggestions

1. Evaluate robustness on a held-out task type (e.g., adversarial examples for summarization or a completely different NLP task) to demonstrate that the robustness gains are not merely in-distribution pattern matching.
2. Validate the fairness auxiliary model on an established fairness benchmark for open-ended text generation (e.g., BBQ, or at minimum describe what DecodingTrust's fairness metrics actually measure and how the training data relates to them).
3. Add an instruction-following benchmark (MT-Bench or AlpacaEval) to support the claim that helpfulness is preserved for chat-oriented use cases.
4. Report the value of γ used in experiments, and ideally provide a brief sensitivity analysis showing how different values affect the trustworthiness vs. helpfulness trade-off.
5. Provide a confusion matrix or qualitative examples of router selections to demonstrate that the perplexity criterion is selecting on safety-relevant features rather than superficial domain similarity.
