Now I have enough calibration data. Let me synthesize the final review.

## Summary of Calibration Anchors

**Round 1 (Bracketing):**
- Weak band: ZeroSumEval (3.0), BigCodeBench (3.0), DataSciBench (3.2), PhyloLM (3.0)
- Middle band: Domain-specific VLM Task Augmentation (4.33), LiveXiv (5.5), Safety Lab Benchmark (4.0)
- Strong band: Training on the Test Task (8.0), MMIE (8.0), LOKI (8.0)

**Round 2 (Narrowing):**
- Retro-Holdouts / Benchmark Inflation (4.25)
- Evading Data Contamination (4.25)
- Infinity-Benchmarks (3.5)
- Domain-specific VLM Task Augmentation (4.33)

**Bracket:** Round 1 placed the paper between 3.5 and 5.5. Round 2 narrows to 3.5–4.5. ARENABENCHER is clearly stronger than ZeroSumEval (3.0) and Infinity-Benchmarks (3.5), comparable to Retro-Holdouts (4.25) and Domain-specific VLM Task Augmentation (4.33), but weaker than LiveXiv (5.5) which was accepted despite similar single-LLM reliance concerns. The separability contradiction and complete absence of baselines are more severe weaknesses than those of LiveXiv.

**Final score: 4.0**

Here is my review:

---

## Summary

ARENABENCHER proposes a framework that takes an existing benchmark and a pool of models, extracts the "ability" each test case targets, generates candidate rewrites via an LLM, scores candidates via multi-model feedback, and iteratively refines them using in-context demonstrations of strong candidates. The paper evaluates on GSM8K, CommonsenseQA, and AdvBench with six small open-source models (1B–7B), comparing m=1 (single-model feedback) vs. m=3 (multi-model feedback).

## Strengths

- **Systematic head-to-head comparison of multi-model vs. single-model feedback (Tables 1, 2).** Every row in Table 1 shows m=3 produces larger accuracy drops (or ASR increases) than m=1. Table 2 consistently shows higher difficulty and comparable or better fairness under m=3. This clean ablation directly supports the central design claim that aggregating multiple models' signals is beneficial, and goes beyond what prior single-model optimization work provides.

- **Principled fairness metric with empirical tracking (§3.5, Table 2).** The paper defines a formal fairness metric (Eq. 3) measuring how evenly failures distribute across models, and reports it for all configurations. Results show fairness is maintained or improved (e.g., CSQA: 82.9%→92.8%), providing evidence that the framework does not merely make harder problems but does so equitably — a property absent from prior benchmark augmentation work.

- **Human validation with transparent failure analysis (§4.2, Figure 2).** Beyond automated metrics, the paper has three annotators evaluate 100 updated GSM8K items (95% aligned, 96% correct), and importantly includes a detailed failure case showing a generated query that was unsolvable and misaligned. This transparency about failure modes is uncommon in benchmark generation papers and provides concrete signals for improvement.

## Weaknesses

### Major

1. **No baselines against any prior benchmark augmentation method.** The Related Work discusses MATH-Perturb (Huang et al., 2025), ARST (Hou et al., 2025), ArithmAttack (Abedin et al., 2025), simple numerical perturbation (Yang et al., 2025; Mirzadeh et al., 2024), and PAIR (Chao et al., 2025) in detail, positioning ARENABENCHER as improving on these approaches. Yet the experiments contain zero comparisons against any of them — the only comparison is m=1 vs. m=3 (two variants of the proposed method). Without a baseline such as simple paraphrasing, single-model adversarial generation, or numerical perturbation operating on the same benchmarks, we cannot assess whether ARENABENCHER's multi-model feedback mechanism improves over existing simpler approaches. This is the most critical single omission in the evaluation.

2. **Abstract claims "improve model separability" but Table 2 shows consistent decreases.** The abstract (line 9) states ARENABENCHER produces updates that "improve model separability." Table 2 shows separability drops in every domain: GSM8K 15.2→12.2 (−20%), Harmful Behaviors 17.1→14.5 (−15%), CSQA 8.5→7.2 (−15%). The paper dismisses this as "slight variation" and "expected as model performance begins to compress" (line 230), but this contradicts a stated contribution in the abstract and the list of four desiderata (§3.5) where separability is listed first. A benchmark that compresses model performance is *less* discriminative, not more. This tension between the difficulty/fairness objectives and separability is never acknowledged as a tradeoff.

3. **GPT-4o is the generator, verifier, and alignment scorer, and is never evaluated on the evolved benchmarks.** The paper uses GPT-4o-2024-08-06 for test objective extraction, test case generation, and as the verifier (line 209). The figure caption on line 71 calls the judge "independent," but it is the same model as the generator. Meanwhile, the evaluated model pool consists only of 1B–7B open-source models (Llama-3.2, Qwen3, Mistral). We do not know whether a frontier model (including GPT-4o itself) would also show degradation on the evolved benchmarks. If GPT-4o's performance is unaffected while small models drop sharply, the "evolved" tests may exploit small-model brittleness rather than testing the intended ability more rigorously.

### Minor

4. **Contamination confound.** The motivating problem is data contamination — models may have memorized original benchmark items. The evaluation compares accuracy on original items (potentially contaminated) against evolved items (novel). A performance drop confounds two mechanisms: (a) evolved items genuinely test the same ability at higher difficulty, versus (b) evolved items simply are not memorized, so models fall back on their true (lower) ability. No control condition (e.g., simple surface-form paraphrases that also remove memorization advantage) separates these explanations.

5. **Small, homogeneous model pool.** K=6 models, all between 1B and 7B, from three families (Llama, Qwen, Mistral). At each iteration only m=⌈√6⌉=3 are sampled. Claims about "mitigating individual model biases" and discovering "generalizable weaknesses" are not well-supported by this narrow model landscape. Whether the benefits hold with larger models (e.g., 70B+) or more diverse architectures is unknown.

6. **Human evaluation is thin.** 100 samples from a single domain (GSM8K), no inter-annotator agreement reported. The detailed failure case in Figure 2 shows a query that is both unsolvable and misaligned, which one would expect the 95% alignment / 96% correctness figures to catch — but it is unclear whether this case was in the annotated sample. The small scale limits confidence in the reported rates.

7. **The √K heuristic lacks proper justification.** The paper cites Breiman (2001) and Chen & Guestrin (2016) for the m=⌈√K⌉ rule. Those references concern feature subsampling in random forests and XGBoost (a completely different setting). Applying this heuristic to model subsampling is an analogy, not a justification from the cited work. The paper would be better served by directly motivating the choice or providing an ablation over m.

8. **No variance or statistical significance reporting.** All results are point estimates. Given the random sampling of model subsets and candidate generation, run-to-run variance could be substantial. Without confidence intervals, it is unclear whether the m=1 vs. m=3 differences are reliable.

### Trivial

- None.

## Nice-to-Haves

- Include GPT-4o and at least one larger model (e.g., 70B) in the evaluation pool.
- Acknowledge the separability-difficulty tradeoff explicitly rather than dismissing the consistent drop.
- Add a control for contamination effects (e.g., compare against simple paraphrasing that also removes memorization advantage).
- Report confidence intervals or error bars for the main results.
- The fairness metric and selection criterion (selecting candidates that degrade all models, then measuring evenness of failure distribution) are partially circular. A more diagnostic analysis would examine whether fairness holds on test cases where models disagree rather than where they all fail.

## Removed Points

The following points from the inputs were removed for the stated reasons:

- *"The selection criterion and fairness metric are circular (structural)"* — This has some surface validity but is overstated. The method tracks per-model sampling to ensure uniform coverage (line 110) and the fairness metric measures deviation from equal failure counts, which is a meaningful diagnostic even if correlated with the selection criterion. Demoted to a Nice-to-Have observation above.

- *"Separability decreases consistently, contradicting stated claims"* — While the data does contradict the abstract, downgraded from the harsh critic's "severe" classification to Major. The paper's own text acknowledges the decrease (line 230) even if the abstract doesn't. The core contribution (the pipeline) is not invalidated by this, but the claim needs correction.

- *"No analysis of what kinds of test cases are generated"* — The paper provides a detailed case study (Figure 2). This is at least partial analysis. Removed as already partially addressed.

- *"No discussion of computational cost"* — This is standard for ICLR papers and not a core evaluation weakness. Removed.

- Various style/formatting nitpicks, missing citation concerns, and speculative criticisms about what the appendix might contain (the parser strips appendices from all papers).

## Novel Insights

None beyond the paper's own contributions. The cross-check between the abstract's separability claim and Table 2 reveals a tension the authors should address, but this is a straightforward factual discrepancy rather than a novel insight.

## Suggestions

1. **Add at least two baselines from prior work.** The most impactful addition would be a simple rewriting baseline (e.g., LLM paraphrasing without multi-model feedback) and a single-model adversarial baseline (optimizing against one model only). This single change would transform the paper from "a plausible pipeline with internal ablations" to "a method demonstrably better than alternatives."

2. **Correct the abstract and contribution claims.** The separability claim should be tempered ("largely maintains" or "preserves sufficient separability") or dropped entirely. The current wording is factually inconsistent with the reported data.

3. **Include GPT-4o and at least one 70B+ model in the evaluation pool.** This would address concerns about whether evolved benchmarks exploit small-model-specific brittleness and would strengthen the "multi-model" branding.

4. **Add a contamination control.** Compare against a condition where original questions are simply paraphrased (keeping the numeric values and reasoning steps identical). If ARENABENCHER produces larger drops than paraphrasing, the contamination confound is partially addressed.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>