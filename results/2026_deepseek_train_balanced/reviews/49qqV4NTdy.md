## Summary

This paper presents a systematic, controlled empirical study of preference alignment components in Multimodal LLMs (MLLMs), disentangling the effects of alignment algorithms (offline/online/RL), preference dataset construction, dataset size, and prompt novelty — all using a fixed base model (LLaVA 1.6-7B). It introduces Bias-Driven Hallucination Sampling (BDHS), a lightweight method for generating dispreferred responses via attention masking that requires no external models or human annotation, achieving competitive performance against larger, more resource-intensive approaches.

## Strengths

1. **First controlled comparison normalizing dataset size across published MLLM preference datasets.** The paper subsamples all datasets to a consistent 5,000 examples and uses a fixed base model, revealing findings invisible in prior work: e.g., POVID's reported advantage on MMHALBench disappears after size normalization, and RLHF-V outperforms it (Section 3.2, Table `datasets_baselines`). This demonstrates that prior conclusions were confounded by dataset size differences — a genuinely useful contribution to the field.

2. **BDHS with attention masking outperforms pixel-based corruption while requiring no external models or human annotation.** The empirical results (Table `bdhs_ablation`) show that $\text{BDHS}_\text{attn}$ "consistently outperforms the POVID-style image distortion across all benchmarks." This is a meaningful methodological advance: BDHS uses only SFT data already available from instruction tuning, unlike POVID (GPT-4V) or RLHF-V (human annotators).

3. **Mixed-DPO demonstrates complementary benefits of offline and online signals.** The paper shows (Table `mixed_dpo`) that offline DPO improves hallucination benchmarks while Online-DPO improves open QA, and their combination via Mixed-DPO yields "consistent improvement over both online and offline methods." This is the first such demonstration in MLLMs.

4. **Negative results that inform practice.** Several findings are genuinely useful despite being "negative": (a) reward models trained on POVID/RLHF-V show poor cross-dataset generalization (Table `rm_validation_accuracy`); (b) RL-based alignment (PPO/RLOO) fails to outperform simpler DPO; (c) prompt novelty does not substantially benefit alignment; (d) chosen responses from weaker models (LLaVA 1.5-7B) can match those from GPT-4V.

## Weaknesses

### Fatal
None.

### Major

**1. MMHALBench-V is introduced as a primary hallucination metric without presenting validation evidence.** The paper states (Section 3.2) that this GPT-4o-based variant was "empirically found to be more reflective of true hallucinations in a human comparison" — but no human comparison data, inter-annotator agreement, or correlation analysis is presented anywhere. While MMHALBench-V is one metric among several used (POPE, LLaVABench-in-the-Wild, TextVQA, GQA, MMVet, Recall$^\text{coco}$), it is the paper's **primary** hallucination metric and many comparisons (e.g., the claim that BDHS achieves competitive hallucination performance) rely substantially on it. A paper that derives and centrally relies on a new evaluation variant must present the evidence for its validity.

**2. No variance or statistical significance reporting across a paper of comparative claims.** All experimental results are reported as point estimates without confidence intervals, error bars, or significance tests. Many claims hinge on small differences: "comparable performance," "slight reduction," "consistent improvement." Without variance estimates, it is impossible to determine which observed differences are meaningful. While single-run evaluations are common practice in LLM training (due to cost), this paper's central contribution is a systematic *comparison* — the relative rankings and trends are its primary output. At minimum, the key comparative results should include variance estimates from multiple runs or a discussion of expected variability.

### Minor

**3. Insufficient analysis of the extreme masking regime ($\rho_\text{th}=0.99$).** The paper sets the attention masking threshold to mask 99% of image tokens, arguing this is justified by AnyRes redundancy. While the paper provides a qualitative example with $\rho_\text{th}=0$ (no masking), there is no systematic ablation over intermediate $\rho_\text{th}$ values (e.g., 0.5, 0.7, 0.9, 0.99) to show how performance changes with masking strength. Additionally, no comparison is made against the simplest possible baseline: generating rejected responses with the image entirely removed. This baseline would clarify whether the attention masking mechanism per se adds value beyond training the model to be cautious when visual information is absent.

**4. Several design choices are not independently ablated.** The semantic similarity threshold ($\epsilon_s=0.97$), the yes/no substitution heuristic (50% probability), and the number of BDHS iterations ($N_\text{BDHS}=5$) are set without sensitivity analysis. While these are reasonable engineering choices, their individual contributions to BDHS performance are unclear.

### Trivial

None. (Minor issues noted above are at least Minor-tier; there are no purely cosmetic problems worth listing.)

## Nice-to-Haves

- A brief discussion of the computational cost / training-time overhead of BDHS (which involves multiple forward passes during alignment) would be helpful for practitioners weighing this approach.
- The RL experiments use only PPO and RLOO; noting that other RL algorithms (e.g., GRPO, Reinforce++) might yield different results would strengthen the negative finding's contextualization.

## Removed Points

- **Annotator asymmetry in Online-DPO/Mixed-DPO comparison (Harsh Critic point #4):** The critic argued that comparing BDHS (no external models) against Online-DPO (needs LLaVA 1.6-34B) "mixes regimes" and is ambiguous. However, the paper clearly acknowledges this limitation in Section 5.3.1 ("access to such models is not always guaranteed") and explicitly frames BDHS as a lightweight alternative. The comparison is valid on its own terms — the paper is showing what can be achieved *without* strong annotators vs. *with* them.
- **General comments about missing related work, presentation style, or "could also do X":** Removed per instructions (no external verification possible for missing references; formatting issues are parser artifacts).
- **Strength Finder claims about the "importance of the problem":** Removed as generic. Only concrete, evidenced strengths are retained above.
- **Criticism about the paper claiming to be "first" (Harsh Critic Section-by-Section):** The paper says "to our knowledge, this is the first time that such study is conducted with MLLMs" — it already includes the softening phrase. Not a valid weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one notable observation: the paper's core value is not BDHS itself (which is a relatively simple method) but the **deconfounding analysis** that reveals how much prior work's claims about "best" alignment datasets were driven by uncontrolled dataset size differences. The review process highlights that this kind of meta-analysis — benchmarking the benchmarks, normalizing across studies — is surprisingly rare in MLLM alignment research and constitutes a distinct contribution type that the field should encourage.

## Suggestions

1. **Validate MMHALBench-V against human judgments.** Even a small-scale study (e.g., 200–300 responses rated by 3 annotators) reporting correlation with MMHALBench-V scores would transform the credibility of the evaluation framework.
2. **Add variance estimates** to the key comparison tables. Even 2–3 runs with different random seeds for the central comparisons (baseline, DPO-POVID, BDHS-attn) would establish whether the reported differences are meaningful.
3. **Add a systematic ablation of $\rho_\text{th}$ values** (e.g., 0.5, 0.7, 0.9, 0.99) for BDHS, plus a "no image" baseline, to justify the extreme masking regime.
4. **Include sensitivity analyses** for $\epsilon_s$ and the yes/no heuristic to clarify their individual contributions.

## Score and Decision

This paper makes a genuine and well-motivated contribution: it provides the first controlled, apples-to-apples comparison of alignment components in MLLMs, correcting confounded conclusions from prior work, and introduces BDHS as a practical lightweight alternative. The strengths — systematic methodology, honest reporting of negative results, multiple insightful findings — are substantial. The weaknesses are real but addressable: the primary hallucination metric needs validation, and variance estimates should be provided for comparative claims. Neither issue invalidates the core contribution; both can be resolved in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>