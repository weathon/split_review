Now I have enough information. Let me write the consolidated review.

## Summary
This paper tackles the problem of black-box adversarial attacks on multi-task learning systems (text classification + translation). The authors propose CEMA (Cluster and Ensemble Multi-task Text Adversarial Attack), which uses 100 queries to a victim multi-task model, clusters the concatenated input-output representations, trains binary substitute models on cluster labels, generates adversarial candidates on these substitutes, and selects the candidate that fools the most substitute models. The key idea is converting a multi-task attack problem into a single binary classification attack via clustering. Results show ASR >60% on SST5/Emotion classification and BLEU scores <0.15 on translation, including against commercial APIs (Baidu Translate, Ali Translate).

## Strengths
1. **First black-box attack for multi-model multi-task settings**: The paper correctly identifies a gap — existing multi-task attacks assume white-box access to shared parameters, which fails against separate per-task models (multi-model MTL) and commercial APIs. CEMA is the first method that addresses this gap, demonstrated via Victim Model C (closed-source APIs, Table 2).

2. **Strong empirical results against commercial translation APIs**: CEMA drives BLEU scores to 0.29 (Baidu) and 0.15 (Ali Translate) on SST5 using only 100 total queries (Table 2). This is a clean demonstration because the baselines (Morphin, TransFool) are also designed for black-box translation attacks, making the comparison concrete and the improvement unambiguous.

3. **Zero-shot robustness across distribution mismatch**: When auxiliary data comes from a different dataset (e.g., Emotion data to attack SST5, Table 6), CEMA still achieves ASR up to 66.40% and BLEU 0.18. This strengthens the practical claim that an attacker could collect Internet data rather than requiring access to the victim's training distribution.

4. **Plug-and-play component compatibility**: Ablations across clustering methods (Spectral, Kmeans, BIRCH — Table 4) and vectorization methods (mT5, XLM-R, one-hot — Table 5) show average ASR differences ≤3%, demonstrating that the framework is not brittle to specific component choices.

## Weaknesses

### Major
1. **Misleading query metric presentation**: The "Queries" column in Tables 1–2 mixes incompatible quantities. Baselines report *per-text* average query counts (e.g., BAE: 21.43 queries per text), while CEMA reports *total auxiliary queries divided by dataset size* (0.045 = 100/2210). These are different measures — baselines do not amortize across the dataset. Although CEMA genuinely uses far fewer total queries (100 vs. up to 30×2210=66,300), placing them in the same column without clarifying the distinction makes the comparison appear staged. The paper should report total query budgets or use a consistent per-text metric including the auxiliary cost. This does not invalidate the core claim but undermines the presentation of experimental evidence.

2. **No variance or statistical significance reported**: All results (Tables 1–6) are single numbers with no error bars. The method involves multiple stochastic components: auxiliary text sampling (100 from validation set), non-deterministic spectral clustering, random 80% splits for the w substitute models, and random initialization of attack methods. Without variance over at least 5 runs, the reliability of claims like "CEMA achieves 73.57% ASR vs. next-best 46.11%" cannot be assessed. The gap may be real, but the paper provides no evidence that it is significant.

3. **Absence of per-text query costing for CEMA**: The paper reports only amortized queries (0.045 per task). It never explicitly states CEMA's per-text query cost during the attack/verification phase. While the attack on each text is generated on the substitute model without querying the victim, the paper should clarify whether the 100-query budget covers the entire attack pipeline (auxiliary + verification + any per-text cost) or whether additional verification queries are needed, and report this transparently.

### Minor
4. **Cluster-label-to-task-label mapping is not directly validated**: The paper's core mechanism assumes that changing the binary cluster label on the substitute model corresponds to changing the predicted label on each victim task (Section 4.2, line 91: "the label y_i^A shifts accordingly"). While the end-to-end ASR >60% provides indirect evidence that the pipeline works, the paper offers no direct measurement (e.g., precision/recall of cluster-label flips predicting task-label flips on held-out data, or substitute model accuracy on the 100 auxiliary samples). A simple diagnostic experiment would make the mechanism more transparent.

5. **Limited baseline applicability**: All baselines (BAE, FD, Hotflip, etc.) are single-task attacks, while CEMA attacks all tasks simultaneously. The paper acknowledges this ("no prior black-box text adversarial attack focuses on multi-task scenarios") but does not discuss how this asymmetry affects the comparison. A multi-task baseline constructed by, e.g., running a single-task attack on each task separately and taking the intersection of successful attacks, would provide a more informative comparison even if imperfect.

### Trivial
6. The claim of being "the first to extend text adversarial attacks to the multi-task setting" is slightly overbroad — prior work (Liu et al. 2017, Guo et al. 2020) exists on multi-task attacks under white-box/shared-parameter assumptions. The paper should say "first *black-box* multi-task attack" consistently.

7. Figure 2 appears to use the same color/marker for both curves (SST5-ASR-T and Emotion-ASR-T), making them hard to distinguish in the description.

## Nice-to-Haves
- A validation experiment directly measuring how often a cluster-label flip on the substitute model produces a label change on each victim task (e.g., precision/recall on a held-out set). This would strengthen the claimed mechanism without requiring additional baselines.
- Reporting substitute model accuracy (even on its 100-sample training set) to show whether the cluster labels are learnable.
- A comparison against an ablated version that uses random binary labels instead of cluster labels, to rule out the possibility that any binary discriminator suffices.

## Removed Points
These points from the reviews are removed because they are factually incorrect, speculative, or violate the filtering rules:

- *"CEMA uses 100 auxiliary queries + 2210 queries to obtain final outputs = 2310 queries"* (Harsh Critic #1) — This is incorrect. The paper's threat model sets a 100-query total budget. The 2210 final outputs are part of post-hoc evaluation, not the attack protocol. The baselines also require evaluation queries to compute ASR, so adding them would affect all methods equally.

- *"The comparison is therefore not apples-to-apples even setting aside the query budget issue"* regarding baselines being single-task — The paper explicitly states the lack of multi-task baselines and uses the available single-task methods. This is a reasonable research choice, not a flaw.

- *Criticisms about missing related works* — Cannot be confirmed without external sources; removed per policy.

- *Criticism about missing appendix sections and reproducibility details* — These are likely present in the original submission (appendix sections are stripped by the parser).

- *"The paper claims to be 'the first to extend text adversarial attacks to the multi-task setting' — this is overbroad"* — The paper explicitly cites Liu et al. 2017 and Guo et al. 2020 as prior work on multi-task attacks and distinguishes itself by focusing on the black-box setting. The claim is appropriately scoped.

- *"The attacker's true capability should be discussed"* regarding same-distribution auxiliary data — The paper explicitly explores both same-distribution and cross-distribution (zero-shot) scenarios, so this is already addressed.

- *"The theoretical derivation... is trivial under the independence assumption"* — The paper includes a remark about the non-independent case (referenced to Appendix T) and the experimental validation (Table 3) confirms the trend, so the theory is appropriately supported.

- *"The conclusion that 'clustering methods do influence attack performance but their impact is largely random' is not supported without variance"* — This is a restatement of the broader variance issue (already included as Major weakness #2).

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate about its approach or results.

## Suggestions
1. Restructure the query reporting: present both total query budget and amortized per-text cost clearly, and separate the 100 auxiliary queries from any verification costs.
2. Add variance estimates (at least mean ± std over 5 random seeds) to all main tables and ablation experiments.
3. Include a diagnostic experiment on the 100 auxiliary texts measuring the precision of cluster-label flips as a proxy for task-label changes.
4. If feasible, construct a multi-task baseline by running a single-task attack independently per task and reporting the joint success rate.

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing:**
I searched for "black-box text adversarial attack" with three score-bands.

*Low band (score < 3.5):* Anchors at 3.00 (GYHF2OfyWP), 3.00 (hzu5luG4DC), 3.00 (4NtrMSkvOy), 2.50 (UWuTZYPSxJ). These papers have withdrawn/reject decisions with fundamental problems (e.g., unclear methodology, impractical threat models).

*Middle band (3.5–7.5):* Anchors at 5.50 (12Acp6ZcRa — T2I diffusion attack, avg scores 8/6/3/5, Reject), 4.25 (LvjSLnMlwY — CLIP UAP, avg 8/3/3/3, Reject), 5.25 (x31F1VmiV7 — BSPA, avg 8/5/5/3, Withdrawn), 7.00 (r42tSSCHPh — LLM jailbreak, avg 8/8/6/6, Spotlight Accept).

*High band (score > 7.5):* Anchors at 7.75 (syThiTmWWm), 9.50 (6Mxhg9PtDE), 8.00 (Bo62NeU6VF), 8.00 (oZtt0pRnOl). These are strong papers with rigorous evaluation.

**Initial bracket:** Between 4.0 and 6.5. The paper has a genuinely novel approach and interesting results against commercial APIs, placing it clearly above the 3.00-level weak papers. Its evaluation gaps (no variance, confusing query metric) prevent it from reaching the 7+ level of rigorous accepted papers.

**Round 2 — Narrowing within the bracket:**
I searched for papers on adversarial transferability and multi-task related attacks in the (4.5, 6.5) and (3.5, 6.0) bands.

Key anchors for comparison:
- **L6CgvBarc4** (avg 6.25, "Bag of Tricks" — Reject): A comprehensive empirical study on adversarial transferability tricks. Well-executed with extensive experiments but limited novelty. The paper under review has more conceptual novelty (first black-box multi-task attack) but weaker execution (no variance, confusing metrics). I find CEMA slightly weaker than this anchor.
- **RKQcJ1lXNT** (avg 5.50, "Adaptive Attacks against Watermarks" — Reject): Good evaluation but some theoretical gaps. Similar quality level to CEMA.
- **N0ETIi580T** (avg 5.25, "Adversarial Vulnerability of Test-Time Adaptation" — Accept Poster): Novel attack algorithm with clear threat model but some weaknesses in evaluation. Comparable quality to CEMA — both have genuine novelty and interesting results, both have significant but fixable weaknesses.
- **12Acp6ZcRa** (avg 5.50, "T2I Diffusion Robustness" — Reject): Novel problem setting with solid experiments but questioned real-world significance. Similar tier.

Comparing specifically: CEMA is stronger on novelty (first black-box multi-task attack vs. incremental improvements) but weaker on experimental rigor (no variance, confusing metrics) than both L6CgvBarc4 and N0ETIi580T. The middle of this range (around 5.0) is appropriate.

**Final score:** 5.0 — the paper has a genuinely novel contribution to a worthwhile problem, the core idea is interesting, and the zero-shot and commercial-API experiments are compelling. However, the confusing query metric presentation, complete absence of variance reporting, and unvalidated cluster-label mapping are significant weaknesses that prevent a higher score. The paper is marginally below acceptance threshold in current form but could become a solid paper with revisions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>