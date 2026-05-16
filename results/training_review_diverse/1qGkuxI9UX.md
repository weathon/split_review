Now I have all the information I need. Let me produce the final consolidated review.

## Summary

DITTO (Demonstration ITerated Task Optimization) is a method for aligning LLMs to individual user preferences using fewer than 10 demonstrations. The core insight is that a handful of demonstrations can be cheaply expanded into a large online preference dataset by treating demonstrations as preferred over both the current and past policy outputs, then applying DPO. The paper evaluates DITTO on static author-style benchmarks (CMCC, CCAT50) using GPT-4 as evaluator, and in a user study (N=16) on email writing. Across both settings, DITTO outperforms SFT, SPIN, and few-shot/zero-shot prompting (including GPT-4 baselines) by substantial margins.

## Strengths

- **Novel and well-motivated method for few-shot personalization.** DITTO addresses a genuine gap: existing RLHF requires thousands of pairwise comparisons from aggregated annotators, while prompting is brittle and tedious. Using demonstrations as feedback is a practical alternative grounded in the HCI tradition of programming by demonstration, and the paper makes this concrete with a clean algorithmic formulation (Section 3).

- **Consistent empirical advantage across two evaluation paradigms.** DITTO outperforms all baselines on static benchmarks (Table 1: average 77.09% win-rate across CMCC and CCAT50) and in a user study with human raters (Table 2: 68.8% win-rate, significantly above all methods at p<0.05). The user study corroborates the static-benchmark findings on a different task with real participants, which is a genuine strength — two different evaluation modalities point in the same direction.

- **Theoretical grounding connects DITTO to online imitation learning.** Section 3.3 derives DITTO from an adversarial reward–policy game, and Lemma 3.1 provides conditions under which DITTO can extrapolate beyond demonstrator performance. This gives a principled explanation for why the method works better than simple SFT imitation.

- **Ablation studies validate key design choices.** Section 5.1 demonstrates that updating the reference policy degrades performance (70.1% → 45.8%), and that removing replay or inter-policy comparisons each reduces win rates (by 6.5 and 2 points respectively). These ablations justify DITTO's specific construction and make the contribution more credible.

- **Sample-efficiency analysis (Figure 2) shows rapid improvement with few demonstrations.** Win rates roughly double for each additional demonstration from N=1 to N=3, supporting the central claim that very few demonstrations suffice.

## Weaknesses

### Fatal

None.

### Major

- **The primary static-benchmark evidence (Table 1) relies on GPT-4 as evaluator without human validation on those specific tasks.** The paper acknowledges the self-enhancement bias (Section 4.2) and conducts a separate user study, which provides partial corroboration. However, the user study covers only email writing (a different domain than the financial editorials, opinion pieces, and blog posts in CMCC/CCAT50), and does not directly validate that GPT-4's style-matching judgments on the static benchmarks align with human judgments. The paper cites prior work showing model-based authorship classification can be reliable, but does not provide a correlational study or calibration experiment for this specific evaluation setup. This means the large win-rate margins in Table 1 — the most broadly advertised quantitative result — rest on an automatic evaluator whose behavior on these exact benchmarks is unvalidated. A relatively small human evaluation (e.g., 50 pairwise judgments across several authors) would substantially increase confidence.

- **Section 5.3 ("How do pairwise preferences compare against demonstrations?") is framed in a way that over-claims what the experiment actually tests.** The experiment compares DITTO (4 demonstrations, online iterative alignment) against DPO trained on up to 500 *synthetic* pairwise preferences sampled from a model (either the base policy or a demo-finetuned policy). These are not human-provided pairwise preferences. The title and conclusion ("demonstrations are an order of magnitude more sample-efficient than pairwise preferences") conflate "pairwise preferences as a feedback modality" with "model-generated synthetic preferences." The experiment is better described as comparing online iterative alignment (DITTO) against offline DPO on synthetic preference data — a useful ablation, but not a direct comparison of demonstrations vs. pairwise preferences as feedback modalities. To make the claimed comparison, one would need to contrast the same amount of human effort spent providing demonstrations vs. providing pairwise preference labels. As it stands, this section's framing is misleading and weakens the paper's central narrative about demonstrations vs. preferences.

### Minor

- **Several hyperparameters are absent from the main text.** The paper mentions "at most K times" (Algorithm 1) and sampling M completions per demonstration, but K, M, learning rates, number of gradient steps per iteration, and exact batch sizes are not given in the main text (presumably deferred to an appendix that the parser strips). While standard for conference papers, this makes the main text less self-contained.

- **Forgetting degradation on HumanEval is mentioned but not quantified.** The conclusion states "we evaluated forgetting on coding tasks with HumanEval, observing some degradation" but reports no numbers. Given that the paper claims degradation can be "mitigated entirely" by adapter routing, actual figures would be reassuring and strengthen the claims about practical usability.

- **The GPT-4 evaluator prompt used for style matching is not provided in the main text.** The exact prompt is critical for understanding what GPT-4 is being asked to judge and for reproducibility. It presumably appears in the appendix, but a summary in the main text would help.

- **The mixing ratios (70% online, 20% replay, 10% inter-policy) are empirically determined without theoretical justification or sensitivity analysis.** While this is acceptable for a new method, the ablation does not explore whether the method is robust to different ratios or tightly coupled to the specific numbers chosen.

### Trivial

None.

## Nice-to-Haves

- A small-scale human evaluation on a subset of the static benchmarks (e.g., 2–3 authors from CMCC, 50 pairwise judgments) correlating GPT-4's choices with human raters would significantly strengthen the paper's quantitative foundation.
- Reporting quantified HumanEval scores (before/after DITTO, with/without adapter routing) would address the forgetting concern cleanly.
- A brief mention of how K (the number of sampling rounds) is set in practice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The self-prompt baseline offers a strong baseline"** — The *paper itself* states this as a feature (PhD students familiar with prompting making the baseline stronger), not a bug. The reviewer presents it as a concern about representativeness, but the paper correctly notes this favors the baseline and DITTO still wins.
- **Various formatting/style nitpicks** (typos, punctuation, garbled text) — These are parser artifacts, not author errors.
- **"Missing related works"** — Not verifiable without full literature knowledge.
- **"Missing appendix content"** — The parser strips appendix content from all papers; it exists in the original submission.
- **"The paper does not provide examples of prompts used during evaluation"** — This is partially about the GPT-4 evaluator prompt (kept in Minor above) and partially about evaluation prompts that would be in the appendix.
- **"Methodological gap that misleads the reader about the primary contribution"** — This is the Section 5.3 framing issue, which I have kept in Major but with more precise language. The reviewer's phrasing ("misleads the reader about the primary contribution") overstates the impact — the paper's primary contribution is DITTO itself, not the comparison in Section 5.3.
- **Criticism that K is "never given"** — K is described in the algorithm but the specific value is in the appendix. This is a presentation choice, not an omission that invalidates anything.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the paper's comparison of DITTO against synthetic pairwise preferences (Section 5.3) raises an interesting question that the paper does not fully address — namely, whether the advantage of demonstrations over preferences is due to the modality itself or due to DITTO's online/iterative structure. The paper frames this as "demonstrations vs. preferences" but the experiment actually tests "online iterative alignment using demos vs. offline DPO on synthetic preferences." An experiment that controlled for the online/offline dimension (e.g., DITTO on synthetic preferences vs. DITTO on demonstrations, or online DPO on human preferences vs. DITTO) would cleanly separate the effect of feedback modality from the effect of the training procedure. This distinction could guide future work on personalized alignment.

## Suggestions

1. **Reframe Section 5.3** as a comparison between online iterative alignment (DITTO) and offline DPO on synthetic preference data derived from model samples. Remove the over-claim that this directly compares demonstrations vs. pairwise preferences as feedback modalities. The experiment is still informative as an ablation.

2. **Add a small human validation study** for the GPT-4 evaluator on at least one static benchmark task. Even 50–100 pairwise human judgments correlating with GPT-4's choices would substantially strengthen confidence in Table 1.

3. **Report HumanEval numbers explicitly** to support the claim that forgetting can be "entirely mitigated" by adapter routing.

## Score and Decision

DITTO proposes a genuinely useful method for an important problem (few-shot LLM personalization). The core algorithmic idea is sound and well-motivated. The empirical evidence spans two evaluation modalities (automatic benchmarks + user study) that point in the same direction, which is more than many papers provide. The ablations are informative and the theoretical connection to online imitation learning adds depth.

The paper's two major weaknesses are real but not fatal. The GPT-4 evaluator concern is partially addressed by the user study and the paper's own acknowledgment of the bias. The Section 5.3 framing issue is a presentational over-claim rather than an invalid experiment — the underlying ablation still shows something useful, just not what the title advertises. Both are fixable with clearer framing and/or a modest additional experiment.

Given the novelty of the method, the breadth of evaluation (static benchmarks + user study + ablations), and the fact that neither weakness undermines the core contribution, this paper merits acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>