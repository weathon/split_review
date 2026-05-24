## Summary

This paper presents PLAGUE, a three-phase plug-and-play framework (Planner, Primer, Finisher) for automated multi-turn jailbreak attacks, augmented with a lifelong learning component that retrieves successful planning strategies from a persistent memory bank. The framework is modular by design, allowing existing attack methods (GOAT, Crescendo, ActorBreaker) to be substituted as Planner or Finisher modules. Evaluated on HarmBench across five frontier models (o3, o1, DeepSeek-R1, Claude Opus 4.1, Llama 3.3-70B), PLAGUE reports a StrongREJECT score of 0.814 (81.4%) on o3 and 0.673 on Claude Opus 4.1, substantially outperforming all baselines.

## Strengths

- **SOTA attack performance on highly safety-aligned models**: Table 2 shows PLAGUE achieves an 81.4% StrongREJECT score on OpenAI o3 (vs. GOAT's 61.6%) and a 67.3% score on Claude Opus 4.1 using a Crescendo-based finisher (vs. base Crescendo's 48.0%). The consistent margin across all five models provides strong support for the framework's effectiveness.

- **First multi-turn attack with lifelong learning via memory retrieval**: Section 3.3.1 and Algorithm 1 describe a cosine-similarity-based retrieval mechanism from a persistent strategy memory bank. Table 1 confirms PLAGUE is the only multi-turn method with lifelong learning, and Table 3 shows this component (RSS) contributes ~4% SRE improvement on o3 and ~4.3% on Claude Opus 4.1.

- **Plug-and-play modularity validated by component swapping**: Table 4 demonstrates that replacing the GOAT finisher with Crescendo + PLAGUE's planner achieves 0.673 SRE on Claude Opus 4.1 — far exceeding both base Crescendo (0.48) and the GOAT-based PLAGUE configuration (0.465). This directly supports the central design claim.

- **Incremental ablation with causal attribution**: Table 3 adds backtracking, reflection, planner, and memory retrieval one-at-a-time to the GOAT baseline. Each addition raises SRE on o3 (0.587 → 0.612 → 0.761 → 0.773 → 0.814), providing clear evidence for each architectural component.

- **Comprehensive and fair-effort evaluation**: Results are reported across five frontier models, four multi-turn baselines plus AutoDAN-Turbo and two additional methods (X-Teaming, FITD), all under a controlled six-turn budget. Table 5 further provides an efficiency comparison of LLM call counts.

## Weaknesses

### Major

- **Lifelong learning evaluation conflates cross-goal and within-goal adaptation**: The memory bank R⁺ stores strategies from successful attacks *during the evaluation run* (Section 3.3.1, Algorithm 1). When processing 200 HarmBench goals sequentially, strategies discovered on earlier goals in the same test set can be retrieved for later goals, giving PLAGUE a form of test-time adaptation that none of the baselines receive. This is not a bug in the design — lifelong learning is a stated feature — but the main comparison (Table 2) does not isolate this effect. The ablation (Table 3) shows that RSS adds only ~4% SRE, so the bulk of improvement comes from other components, but the paper should either (a) report the main results with lifelong learning disabled as a separate column, or (b) clearly separate the single-goal attack capability from the cumulative-learning scenario. Without this, readers cannot determine how much of the headline advantage is from cross-goal information transfer vs. inherent attack strength.

### Minor

- **No variance or significance reporting**: All results are averaged over three runs with no standard deviations or confidence intervals (Section 4, line 164). Given the known stochasticity of LLM-based attacks, differences of a few percent may be within noise. The improvements of 30–40% over baselines are large enough that this is unlikely to change the qualitative conclusions, but the absence of variance estimates weakens the evidence.

- **Metric naming is non-standard**: The paper states "We use SRE and ASR interchangeably in our work" (line 164). The abstract reports "an ASR (based on StrongReject) of 81.4%," which is the average StrongREJECT score (0–1) presented as a percentage. Binary ASR for o3 is 66.2% (Table 2). While both metrics are reported and the paper is transparent about the usage, calling the graded SRE score an "attack success rate" is inconsistent with most of the jailbreak literature and risks misleading casual readers.

- **Key hyperparameters not ablated**: The similarity threshold of 0.6 for memory retrieval, the maximum of 2 ICL examples, the 7/10 primer threshold, and the 8/10 finisher success threshold (Sections 3.3.1, 3.4, 3.5) are all presented without any sensitivity analysis. While the paper has a strong ablation for the main framework components, an analysis of these threshold choices (even on a subset) would strengthen confidence.

- **Alignment between rubric scorer and final evaluation is unanalyzed**: The rubric scorer (Section 3.2) uses thresholds of 8/10 for success during the Finisher phase, but the paper does not analyze how well this correlates with the final StrongREJECT score. If the rubric is being gamed — returning high scores for outputs that later receive low StrongREJECT scores — the feedback loop would be degraded.

### Trivial

- The ActorBreaker row in Table 2 appears to be duplicated (two identical rows for the same method on o3).

## Nice-to-Haves

- A discussion of limitations (e.g., reliance on a strong attacker model, computational cost of the rubric scorer, generalizability to unseen attack categories).
- A responsible disclosure or dual-use discussion, standard for safety-releasing attack frameworks.
- Qualitative examples of successful jailbreak trajectories showing how the three phases interact.

## Removed Points

These points are flagged for removal — treat with caution:

- **"Uncontrolled attacker model across baselines (structural flaw)"**: Removed. The paper states (line 158) "We use Deepseek-R1 as our primary Attacker model across all our experiments," which includes all baseline experiments. The critic's claim that the paper "does not state whether the same attacker model is used" is factually incorrect. The baseline descriptions (lines 166–171) describe modifications to *evaluation environments and budgets*, not changes to the attacker model.

- **"Missing related works"**: Removed per policy — no external sources to verify existence of omitted works.

- **"No limitations section"**, **"Ethical considerations insufficient"**, **"Qualitative examples"**: Moved to Nice-to-Haves. These are standard expectations but not core weaknesses in the technical contribution.

- **Generic strengths from Strength Finder** ("important problem", "timely topic", etc.): Removed — these are not specific to the paper's contribution.

## Novel Insights

The most interesting observation from the cross-reviewer analysis is that despite the harsh critic's framing of the attacker-model concern as "structural" and "invalidating," the paper actually does state the attacker model upfront. The more subtle and legitimate concern — cross-goal information leakage through the lifelong learning memory bank — is a genuine evaluation design issue that the paper should address, but its impact is bounded (only ~4% SRE improvement per Table 3). The second insight is that PLAGUE's modular architecture produces asymmetric results across victim models: on Claude Opus 4.1, the GOAT finisher underperforms Crescendo, but on o3, GOAT is the better finisher. This model-dependent behavior is an interesting finding that the paper could explore further.

## Suggestions

1. **Isolate the lifelong learning benefit**: Report main results with RSS disabled (so no cross-goal transfer) as a separate column in Table 2, then present the additional gain from lifelong learning in a separate analysis.
2. **Add variance estimates**: Report standard deviations or bootstrap confidence intervals for the main results in Table 2.
3. **Use consistent metric terminology**: Reserve "ASR" for the binary success rate and use "SRE" for the average StrongREJECT score, or clearly define "SRE-ASR" vs. "Bin-ASR" throughout.
4. **Ablate the key thresholds**: Even a brief sensitivity analysis on the retrieval similarity threshold (0.6) and the success threshold (8/10) on a subset of models would meaningfully strengthen the ablation.

## Score and Decision

### Calibration Analysis

**Round 1 (Bracket: 5.0–7.0)**

| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| `/home/wg25r/review_agent/human_reviews/5kMwiMnUip.md` | 1.40 | Weak | Simple chain-of-thought jailbreak paper, rejected. PLAGUE is far stronger. |
| `/home/wg25r/review_agent/human_reviews/KyKTjRtyNG.md` | 3.00 | Weak | Multi-round conversational jailbreak, withdrawn. Limited evaluation, PLAGUE is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews/w0b7fCX2nN.md` | 3.75 | Middle | Contextual interaction attack, withdrawn. PLAGUE has broader evaluation and clearer methodology. |
| `/home/wg25r/review_agent/human_reviews/kvvvUPDAPt.md` | 5.33 | Middle | ActorAttack (multi-turn), withdrawn. Only 2 models, 50 samples in ablation, very limited baselines. PLAGUE is substantially stronger across all dimensions. |
| `/home/wg25r/review_agent/human_reviews/xQIJ5fjc7q.md` | 5.50 | Middle | DAG-Jailbreak, rejected. Unclear methodology (dependency analysis not formalized), reproducibility concerns. PLAGUE's methodology is clearer and better validated. |
| `/home/wg25r/review_agent/human_reviews/LO4MEPoqrG.md` | 5.00 | Middle | ReG-QA, accepted poster. Poor writing, very limited baselines, narrow model coverage. PLAGUE is stronger. |
| `/home/wg25r/review_agent/human_reviews/6Mxhg9PtDE.md` | 9.50 | Strong | Shallow safety alignment analysis, oral. Exceptional paper. PLAGUE is not in this tier. |
| `/home/wg25r/review_agent/human_reviews/tc90LV0yRL.md` | 8.67 | Strong | Cybench framework, oral. Thorough cybersecurity evaluation framework. Different paper type; PLAGUE is not at this level. |
| `/home/wg25r/review_agent/human_reviews/syThiTmWWm.md` | 7.75 | Strong | Null model evaluation analysis, oral. Unique contribution, rigorous analysis. PLAGUE is weaker. |

**Round 2 (Narrowing within 5.0–7.0)**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews/asR9FVd4eL.md` | 6.00 | PiF transferability attack, accepted poster. Solid contribution but limited baselines (only GCG and PAIR compared) and only 2 closed-source models. PLAGUE has broader evaluation but less focused contribution. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews/r42tSSCHPh.md` | 7.00 | Catastrophic Jailbreak via generation exploitation, spotlight. Very thorough (11 models), cleanly presented, surprisingly simple finding. PLAGUE has a more complex and arguably more novel methodology but slightly less clean evaluation (the cross-goal leakage concern, no variance reporting). PLAGUE is slightly weaker. |
| `/home/wg25r/review_agent/human_reviews/aSy2nYwiZ2.md` | 6.67 | JailbreakEdit backdoor injection, poster. Strong technical contribution but limited applicability (white-box only). PLAGUE has broader applicability (black-box) but different type of contribution. Slightly lower confidence in PLAGUE's results due to evaluation concerns. |
| `/home/wg25r/review_agent/human_reviews/wvFnqVVUhN.md` | 6.25 | VLM image jailbreak transferability, poster. Well-executed negative result. Different domain. PLAGUE has a more positive contribution but also more evaluation concerns. |
| `/home/wg25r/review_agent/human_reviews/sULAwlAWc1.md` | 7.00 | ArrAttack robust jailbreak prompts, poster. Strong defense-aware method. PLAGUE compares reasonably. |

### Final Assessment

PLAGUE makes a genuine contribution to the multi-turn jailbreak literature. The three-phase architecture is well-motivated, the modular design is validated by component-swapping experiments (the Crescendo finisher on Claude is particularly convincing), and the evaluation across five frontier models is among the most thorough in this space. The paper is clearly better than the 5.0–5.5 anchors (which had narrow evaluations, unclear methods, or weak baselines). Against the 6.0–6.5 anchors, PLAGUE is broadly comparable — it offers a stronger methodological framework but has slightly weaker experimental reporting (missing variance, cross-goal leakage not isolated). It falls short of the 7.0 anchors, which had either cleaner experimental designs or more surprising findings. The score of **6.0** reflects a solid paper with clear contributions and convincing headline results, held back from a higher score by the two substantive evaluation concerns (cross-goal leakage and missing variance) that should be resolved before acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>