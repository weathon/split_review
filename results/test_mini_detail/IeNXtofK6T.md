Now I have all the information I need. Let me organize my findings into the final review.

## Summary
This paper revisits the idea of using an off-the-shelf LLM as a guardrail against prompt injection attacks — an approach previously dismissed as ineffective based on 2023-era models. The authors propose PromptArmor, which prompts a modern LLM (e.g., GPT-4o, GPT-4.1) to *detect and remove* injected prompts from data samples before they reach the backend LLM. Results on three benchmarks (AgentDojo, Open Prompt Injection, TensorTrust) show that with strong reasoning models, FPR and FNR drop below 1% on AgentDojo, and attack success rate falls from 54.53% to 0.00% with GPT-4.1 while preserving utility. The paper includes ablations on prompting strategies, model size, reasoning mode, and adaptive attacks.

## Strengths

1. **Clear, well-supported core finding.** The paper convincingly shows that prompting a modern frontier LLM (GPT-4o, GPT-4.1) achieves dramatically better detection than older models (GPT-3.5), with FPR and FNR below 1% on AgentDojo (Table 1). This directly reverses prior negative results from 2023 and establishes a credible new baseline for the field. The contrast with GPT-3.5 results (FNR 15.74% on AgentDojo) is particularly informative.

2. **Strong end-to-end security+utility results.** Table 2 demonstrates that PromptArmor-GPT-4.1 achieves 0.00% ASR with 72.02% UA on AgentDojo, outperforming all seven baseline defenses in ASR while maintaining competitive utility. The comparison against Deberta, Llama Prompt Guard 2, DataSentinel, and system-level defenses (MELON, Tool Filter) provides a meaningful landscape picture.

3. **Systematic ablation of model size and reasoning with open-source models.** Section 4.4 (Figure 3) uses Qwen3 models (0.6B, 8B, 32B) in both reasoning and non-reasoning modes to show that model capacity is the primary driver of performance, with reasoning providing clear benefits at intermediate scales (8B FNR drops from 26.50% to 15.78%). This is the cleanest experiment in the paper.

4. **Memorization test rules out data contamination.** Section 4.5 applies prefix-suffix memorization tests (Carlini et al., 2021; Staab et al., 2023) showing average similarity of 0.34 and only 3.5% of samples above the 0.6 threshold, strengthening confidence that results reflect genuine detection capability rather than benchmark memorization.

5. **Modular, practical design.** The fuzzy-matching removal technique (Section 3.1) and the plug-in architecture make the approach easy to adopt, and the fact that no training or fine-tuning is needed is a genuine operational advantage.

## Weaknesses

### Major

1. **Removal quality is not directly evaluated, undermining a claimed advantage.** The paper emphasizes that PromptArmor *removes* injected text (vs. discarding the input) as a key advantage for utility preservation, yet no experiment directly measures removal accuracy. The only evidence is the end-to-end ASR (0.00%) and UA (72.02%). This confounds two things: correct detection and correct extraction/removal. It is possible (though unlikely) that PromptArmor removes additional benign content or leaves injection fragments. Without measuring precision/recall of extraction against ground-truth injection boundaries, the "removal" claim is hollow. The paper should report, for detected positive samples: (a) how often the extracted text exactly matches the ground-truth injection, (b) token-level edit distance, and (c) how often benign content is mistakenly removed.

2. **Adaptive attack evaluation is too narrow to support the broad claim of robustness.** The paper tests only one automated red-teaming method, AgentVigil (Section 4.6), which optimizes attack templates via black-box fuzzing. This does not directly target the guardrail LLM's detection mechanism. A meaningful adaptive attack would attempt to craft injections that the guardrail fails to recognize — e.g., by embedding instructions in benign-looking formats, exploiting the guardrail's own instruction-following tendencies, or using indirect references. The paper's conclusion that PromptArmor is "robust against adaptive attacks" (Section 1, last paragraph) is overstated given this single narrow evaluation. The authors should either broaden the adaptive evaluation or temper the claim.

### Minor

1. **Per-dataset prompt adjustment weakens the "baseline" claim.** Section 4.1 states: "Given the varying settings of the benchmarks, we adjusted the detection prompt for each dataset." The paper does not specify what adjustments were made or whether a single fixed prompt would work across all three benchmarks. For a method positioned as an "essential baseline" that is "easy-to-deploy" and "drop-in," testing a single fixed prompt would be more convincing and honest. Without this evidence, results may reflect per-dataset prompt engineering rather than inherent guardrail capability. The authors should provide the unmodified prompts and justify that adjustments do not incorporate knowledge of injection content.

2. **Claim about newer models performing equally across prompting strategies is unsupported.** Section 4.3 states that "newer models like GPT-4o and GPT-4.1 perform equally well across different prompting strategies" but provides no data — the ablation on prompting strategies (Table 3) only tests GPT-3.5. The claim may be true but is presented as fact without evidence.

3. **No variance or confidence intervals reported.** All metrics in Tables 1–4 are point estimates. Given the modest sample sizes and dependence on stochastic LLM outputs, reporting uncertainty (e.g., across multiple runs or bootstrap CIs) would substantially strengthen the evaluation.

4. **No comparison to a simple rejection baseline.** The paper claims removal preserves utility better than rejection. But there is no experiment comparing PromptArmor's removal-based UA against simply dropping detected samples and processing only unflagged ones. Such a comparison would cleanly quantify the utility gain attributable to removal vs. detection alone.

5. **No error analysis of false negatives/positives.** The paper reports impressively low but nonzero FPR/FNR but never analyzes what the failures look like. Understanding whether false negatives are concentrated in particular attack types (e.g., Tool Knowledge attacks) or data contexts would give practitioners actionable guidance on limitations.

### Trivial

- The paper claims "computational efficiency" (Section 3.2) as an advantage, but PromptArmor adds an extra frontier-LLM API call per data sample, a meaningful inference cost. The efficiency argument is about *development* cost (no training needed) but the framing conflates the two. The paper should explicitly acknowledge the inference overhead trade-off.

## Nice-to-Haves

- A discussion of token budgets and input length sensitivity. Injection detection on long documents (e.g., full web pages retrieved by agents) may be more challenging; the benchmarks used involve relatively short tool-call results.
- Varying the backend LLM (beyond GPT-4.1) to check whether PromptArmor's utility preservation generalizes across different backend capabilities.
- A fixed-prompt evaluation across all benchmarks (as discussed in Minor weakness 1) would strengthen the baseline claim substantially.

## Removed Points
- **Criticism about asymmetrical comparison (frontier vs. small models):** The paper's point is that using a frontier guardrail works well. The comparison also includes Qwen3-32B showing strong results. This is not an unfair comparison.
- **Criticism that the paper's prose reads like "marketing":** Subjective style judgment. The claims about generalization are supported by evaluation across 3 benchmarks.
- **Criticism about RAG/MCP scope gap (Section 2):** The paper scopes these as future directions, not evaluated claims. This is not a weakness.
- **"No missing related works" points:** Various reviewer mentions of missing citations. These cannot be verified and are excluded per protocol.
- **Formatting/style nitpicks:** Parser artifacts, not author errors.
- **Criticism about evaluating only one backend LLM (GPT-4.1) in agent experiments:** Valid but minor; the detection ablations use multiple models. Already addressed partially by comparisons with other guardrail models.

## Novel Insights
The reviews surface one observation not explicit in the paper: the per-dataset prompt adjustment and the unsupported claim about newer models' robustness to prompting strategy together create a latent tension. The paper wants to be both (a) a practical "drop-in" baseline requiring minimal engineering and (b) a method whose prompts were carefully tuned per dataset. These goals are in mild tension, and the paper never resolves which PromptArmor is designed to be. This tension runs through multiple reviewer criticisms (fixed-prompt evaluation, prompt engineering vs. inherent capability) and would benefit from explicit discussion in a revision. Otherwise, no genuinely novel insight beyond the paper's own contributions.

## Suggestions
1. **Add direct removal quality metrics.** For detected positive samples, compare extracted text to ground-truth injections and report exact-match rate, token edit distance, and false removal rate (benign content mistakenly removed). This directly substantiates the claimed advantage over rejection-based defenses.
2. **Provide a single, fixed detection prompt evaluation across all three benchmarks.** Even if performance drops, this is the more informative baseline result for practitioners. Document any per-dataset adjustments transparently.
3. **Broaden adaptive attack evaluation** to include attacks that explicitly target the guardrail's detection mechanism (e.g., mimicking the tone of benign data, using the guardrail's own instruction-following tendencies against it). Alternatively, temper the adaptive robustness claim to match the evidence.
4. **Add confidence intervals or error bars** to all key metrics (FPR, FNR, UA, ASR) and include an error analysis section characterizing false negatives/positives by attack type.
5. **Add a rejection-only baseline** to Table 2 so readers can compare removal-based UA against simply discarding detected samples.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Three queries on "prompt injection defense LLM guardrail detection" filtered to score bands (-1,3.5), (3.5,7.5), and (7.5,11).

*Weak anchors (avg 2.50–3.00):* 5eqkTIQD9v.md (3.0, withdrawn), 3MDmM0rMPQ.md (3.0, reject), KjxZ4BdUdN.md (3.0, withdrawn), UWuTZYPSxJ.md (2.5, withdrawn). These are substantially weaker — limited evaluations, incomplete methods, unclear contributions. The PromptArmor paper is clearly above all of these.

*Middle anchors (avg 4.25–5.50):* PNHGYziAsL.md (SPIN, 5.50, reject), 0VZP2Dr9KX.md (Baseline Defenses, 5.25, reject), RC5x3OkywQ.md (Jailbreak Detection, 4.25, withdrawn), JwoCs9O3QL.md (VLMGuard, 5.00, withdrawn). PromptArmor is stronger than all of these: it uses frontier models (vs. 7B-class models in SPIN and Baseline Defenses), evaluates across 3 benchmarks with stronger baselines, has cleaner ablations (model size × reasoning), and produces more dramatic results (0% ASR). The gap between PromptArmor and these ~5.0 papers is meaningful.

*Strong anchors (avg 7.75–9.50):* 6Mxhg9PtDE.md (Safety Alignment, 9.50, oral), syThiTmWWm.md (Null Models, 7.75, oral), Bo62NeU6VF.md (Backtracking, 8.00, oral), oZtt0pRnOl.md (DP-ICL, 8.00, poster). These are substantially more novel/methodologically ambitious papers with cleaner evaluations. PromptArmor is not at this level.

**Round 1 bracket:** 4.5–7.0, ruling out both the weak band (<3.5) and the very strong band (>7.5).

**Round 2 — Narrowing (4.5–8.0):** Retrieved additional anchors: AC5n7xHuR1.md (AgentHarm, 6.75, poster), GEcwtMk1uA.md (ToolEmu, 7.33, spotlight), b3KgHQos7P.md (VPI Backdoor, 4.75, withdrawn), eC2a2IndIt.md (BadJudge, 6.75, poster), DeVm3YUnpj.md (Agent-as-Judge, 5.67, reject).

AgentHarm (6.75) and BadJudge (6.75) are the closest comparators. AgentHarm is a benchmark paper with broad coverage and solid evaluation — PromptArmor is comparable in evaluation thoroughness but narrower in scope. BadJudge has strong empirical backing and clear contribution. PromptArmor sits slightly below these in overall strength due to the removal quality gap and narrow adaptive attack evaluation.

ToolEmu (7.33, spotlight) is clearly stronger — more novel methodology, human validation, broader implications.

**Final score:** **6.0.** The paper makes a genuine, well-supported contribution (re-establishing prompting as a viable baseline for injection defense). It is clearly above rejection-level papers (~5.0) but the gaps in (1) direct removal quality evaluation and (2) adaptive attack breadth prevent it from reaching the 6.5–7.0 level of the strongest defended papers. A revision addressing these gaps could move it to 6.5 or higher.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>