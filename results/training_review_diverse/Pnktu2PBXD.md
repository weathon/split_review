Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes Differentiable Data Rewards (DDR), a method that uses DPO with a rollout-based reward collection to end-to-end optimize agents in a Retrieval-Augmented Generation (RAG) system. Applied to a two-agent pipeline (knowledge refinement + generation), DDR iteratively samples perturbations to each agent's output, evaluates their impact on the system-level reward, and trains via contrastive preference learning. Experiments on seven knowledge-intensive tasks with two LLM sizes show consistent improvements over Vanilla RAG, REPLUG, and RA-DIT, with additional benefits in mitigating knowledge conflict and avoiding catastrophic forgetting associated with SFT.

## Strengths

- **Consistent, substantial improvements over strong baselines across diverse tasks.** Table 1 shows RAG-DDR outperforms Vanilla RAG, REPLUG, and RA-DIT on all seven evaluated datasets (NQ, TriviaQA, HotpotQA, WoW, etc.) for both MiniCPM‑2.4B and Llama3‑8B, with gains of up to 7% over Vanilla RAG and up to 5% over RA-DIT with the smaller model.

- **DDR effectively mitigates knowledge conflict between parametric memory and external knowledge.** The Internal Knowledge scenario (Table 3) shows that Vanilla RAG suffers >20% accuracy drop when retrieved documents conflict with the model's own knowledge, while RAG-DDR reduces that drop by more than 10 percentage points. Case studies further illustrate that RAG-DDR avoids being misled by ambiguous dates and correctly integrates multi‑hop facts.

- **DDR avoids catastrophic forgetting and overfitting that plague SFT‑based RAG training.** Figure 2 (w/o RAG) shows RA-DIT degrades on NQ and HotpotQA compared to Vanilla RAG, whereas RAG-DDR improves or maintains accuracy on all tasks. Figure 4 (response length) demonstrates RA-DIT produces significantly shorter responses due to overfitting, while RAG-DDR preserves a length distribution similar to the original LLM.

- **Ablation studies isolate the primary contribution of DDR training beyond the architectural change.** Table 2 shows RAG w/ V_KR (adding the knowledge refinement module without training) improves over Vanilla RAG, but RAG-DDR (Only V_Gen) — using the same V_KR module with DDR-trained generation — yields substantially larger gains. This demonstrates that the improvement is driven by DDR optimization, not merely the extra module.

- **DDR maintains its advantage under increasing noise.** Figure 4 (noise knowledge) shows RAG-DDR outperforms Vanilla RAG by a stable margin across 0–4 added noise documents, while RA-DIT degrades and becomes inconsistent.

- **Evaluation across a broad range of tasks (open‑domain QA, multi‑hop QA, slot filling, dialogue) and two LLM scales (2.4B and 8B) supports generalizability.** The findings hold consistently across all seven evaluation datasets and both model sizes.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The headline comparison between RAG-DDR and RA-DIT is partially confounded by the knowledge refinement module.** RAG-DDR employs a V_KR module (Llama3-8B) to filter retrieved documents, while the reimplemented RA-DIT baseline feeds raw retrieved documents directly to the generator. The ablation (Table 2) partially addresses this — RAG w/ V_KR (same architecture, no DDR) is compared against RAG-DDR variants — and shows that DDR training of the generator alone (RAG-DDR Only V_Gen) outperforms RAG w/ V_KR on most tasks, supporting the claim that DDR provides gains beyond the module. However, the paper would benefit from a cleaner comparison (e.g., RA-DIT + V_KR vs RAG-DDR) to fully isolate the effect of the training method from the architectural difference.

- **The training procedure for the knowledge refinement module is underspecified.** The paper states (Section 3.2): "The document d_i that leads the agent system to achieve the highest evaluation reward r(x, y_KR^i='YES') is considered positive." However, it does not clarify how the reward is computed for an individual document when documents are processed jointly by the system. Whether this involves leave-one-out evaluation, greedy selection, or another procedure is not explained. This ambiguity affects reproducibility and should be clarified.

- **No variance or statistical significance is reported for any experimental result.** All tables and figures present point estimates without confidence intervals, error bars, or significance tests. Given that reported improvements (e.g., 5% over RA-DIT) are meaningful but potentially within noise range, the absence of any measure of variability weakens the reliability claims.

- **The training data composition is not fully specified.** The paper mentions "ten datasets covering two tasks, open-domain QA and reasoning" for training but does not list which specific datasets comprise the training set. While evaluation datasets are listed, the training composition should be reported for reproducibility.

- **The use of DPO with deterministic automatic metrics (Rouge-L, Accuracy) as rewards is not deeply justified.** The paper motivates DPO as an alternative to SFT for avoiding overfitting, but does not discuss how the DPO assumption of a latent Bradley-Terry preference model connects to comparing scalar metric scores. In practice, DPO with automatic metrics is widely used in recent literature, so this is not a structural flaw, but a brief discussion of limitations would strengthen the presentation.

### Trivial

- The name "Differentiable Data Rewards" is slightly misleading — the rewards themselves (Rouge-L, Accuracy) are not differentiable; the DPO loss provides the gradient. The paper never claims the rewards are differentiable, so this is a naming issue rather than a conceptual error, but a footnote clarifying this would help.

## Nice-to-Haves

- A limitations section discussing computational cost of the rollout-based reward collection (which requires running the full downstream system for each sampled perturbation), sensitivity to the choice of metric, or scalability beyond two agents.
- An ablation on the DPO hyperparameter β, which is set to 0.1 without justification or sensitivity analysis.
- A controlled experiment measuring catastrophic forgetting more directly (e.g., performance on held-out non-RAG tasks before and after training) to substantiate the claim that DDR mitigates forgetting.
- Reporting the number of sampled responses per query during rollout for the generation module.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"DPO used without any justification as a surrogate for RL"** — The paper explicitly motivates the choice: "this paper focuses on using the DPO method to avoid overfitting the training signals and align data preferences across different agents" (line 30). Using DPO with automatic metrics is standard practice in current LLM alignment literature. The criticism overstates the issue; this is a minor presentation point at most, not a structural flaw.

2. **"Not discussed whether reference model is updated"** — The paper states: "V_t^ref is the reference model, which is frozen during training" (line 61). The reviewer missed this.

3. **"RA-DIT implementation deviates from the original"** — The paper explicitly notes: "we reimplement REPLUG and RA-DIT baselines and do not finetune the retriever during our reproduction process" (line 99). This deviation is disclosed and justified.

4. **"Missing related works on RL-based RAG"** — The paper covers the relevant baselines (RA-DIT, REPLUG, INFO-RAG) and mentions RL methods (Agent Q, STEP-DPO). Demanding coverage of every RL-for-RAG variant is scope creep.

5. **"Abstract formulation of Equation 1 doesn't meaningfully constrain optimization"** — The formulation is a standard way to describe multi-agent data flow. This is a design choice, not a flaw.

6. **"The reward is not differentiable"** (pedantry about naming) — Already addressed in Trivial as a naming clarification. The method uses DPO which provides a differentiable loss; the paper never claims the reward function itself is differentiable.

## Novel Insights

The reviews surface one useful insight beyond the paper's own contributions: the observation that the primary strength of DDR comes from optimizing the generation module (not the knowledge refinement module) is actually an empirical finding that could be emphasized more. The ablation shows that V_KR optimization yields only marginal gains once the generator is DDR-trained — this suggests that for two-agent RAG systems, the bottleneck is the generator's ability to handle retrieved knowledge, not the filtering quality per se. This finding has implications for where future RAG optimization efforts should focus.

## Suggestions

1. **Add a controlled baseline: RA-DIT with the same V_KR module.** To fully de-confound the main comparison, compare RAG-DDR(All) against RA-DIT that also uses the zero-shot V_KR module (or an SFT-trained V_KR) as a front-end filter. If the gain persists, the claim that DDR outperforms SFT is unequivocal.

2. **Clarify the V_KR reward computation.** Provide pseudo-code or an explicit algorithm describing how r(x, y_KR^i="YES") is computed for individual documents — is this leave-one-out, additive, or all-pairs? Also clarify computational cost.

3. **Report variance.** Add confidence intervals (e.g., across multiple seeds or bootstrapped) to at least the main results (Table 1) and the ablation (Table 2).

4. **List the 10 training datasets explicitly.** Replace "ten datasets covering two tasks" with the actual dataset names and sample counts.

5. **Expand on limitations.** Add a brief limitations paragraph discussing the reliance on automatic metrics for rewards, the computational overhead of rollout-based sampling, and potential sensitivity to the choice of reward metric.

## Score and Decision

This paper tackles a meaningful problem (optimizing RAG agents beyond SFT) with a well-motivated approach (preference-based learning via DPO with system-level rewards). The empirical evidence is strong: consistent gains across seven datasets, two model sizes, and multiple analyses (knowledge conflict, noise robustness, forgetting). The ablation study credibly isolates the DDR contribution from architectural confounds. The weaknesses are real but addressable — they concern experimental presentation (missing variance, underspecified training data) and methodological clarity (V_KR procedure), not the validity of the core contribution.

The paper would benefit from revisions addressing the confounded comparison and underspecified training details, but in its current form the evidence is sufficient to support the main claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>