## Summary

This paper proposes ConciseHint, a framework that injects conciseness hints (manually designed text or learned continuous embeddings) into the reasoning generation process of large reasoning models (LRMs), rather than acting before reasoning begins as prior methods do. The injection interval grows adaptively with reasoning length (Equation 1) and the injection position moves from head to tail as generation proceeds (Equation 3). Evaluated on GSM8K, AIME24, and GPQA-Diamond across Qwen3-4B/8B and DeepSeek-R1-14B, ConciseHint reports 10–65% token reductions while roughly maintaining accuracy, and can be stacked on top of existing efficiency methods (Prompt, Deer, NoWait, BeConcise) for further gains.

## Strengths

1. **Novel in-reasoning intervention paradigm.** The paper introduces a genuinely underexplored approach — injecting hints *during* token generation — which is orthogonal to prompting, SFT, RL, and early-exit methods that all operate before or at the end of reasoning. This is clearly differentiated in Figure 1 and the related work (Section 2.2).

2. **Complexity-adaptive interval prevents accuracy collapse on hard queries.** Equation (1) ties injection intensity to reasoning length. Table 3 provides strong evidence: a fixed interval of 64 drops Qwen3-4B accuracy on AIME24 from 67.00→45.33, while the adaptive method maintains 67.00. On easy GSM8K the same fixed interval causes no loss, confirming the adaptive design is necessary.

3. **Dynamic injection position balances cost and accuracy.** Equation (3) moves the injection point from head toward tail as reasoning grows, capped at 80% of the interval. Table 4 shows that injecting at the tail crashes GPQA-Diamond accuracy from ~55% to 42.93%, while the dynamic position avoids this and keeps prefilling costs low (vs. 100% for head injection).

4. **Seamless integration with existing methods yields consistent additional gains.** Table 1 shows ConciseHint applied on top of Prompt, Deer, NoWait, and BeConcise gives 14–40% further token reduction while maintaining accuracy. For instance, Ours(Prompt) on GSM8K+Qwen3-4B goes from 1263→839 tokens (34% further reduction), demonstrating the method's value as a plugin.

5. **Controllability via embedding interpolation.** Equation (4) and Figure 3 show that adjusting γ ∈ [0,1] provides a smooth accuracy–token trade-off, allowing users to dial in the desired efficiency level — a capability prior prompting-based methods lack.

6. **Evidence of reduced redundant self-reflection.** Table 5 shows ConciseHint reduces the count of transition words (e.g., "Wait") and increases the interval between them, indicating the method cuts unnecessary self-checks rather than compressing essential reasoning.

## Weaknesses

### Fatal
None. The core idea is sound and the evidence is directionally consistent. The weaknesses below reduce confidence but do not invalidate the central claims.

### Major

None. The issues identified are addressable in revision and do not fundamentally undermine the paper's contribution.

### Minor

1. **Missing variance and significance reporting.** All accuracy numbers (e.g., 64.33% on AIME24, 55.56% on GPQA-Diamond) are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given AIME24 has only 30 problems and experiments are run 5–10 times, variance from the 30-problem draw itself is substantial. A 2-point drop (e.g., DeepSeek-R1-14B on AIME24: 63.00→61.00) or a 0.91-point rise (Qwen3-4B on GPQA-Diamond: 51.82→52.73) cannot be assessed without variance. While point estimates without error bars are common in this field, the claims of "maintaining performance" would be substantially stronger with standard deviations or bootstrap intervals. This is most consequential for AIME24 (30 problems), where the difference between "maintained" and "slightly degraded" could be a single sample.

2. **ConciseHint-T evaluation limited to the smallest model.** The trained hint embeddings (ConciseHint-T) are evaluated only on Qwen3-1.7B (Table 2). All main results on Qwen3-4B, Qwen3-8B, and DeepSeek-R1-14B use only the manual hint (ConciseHint). The claim that learned embeddings "generalize well to out-of-domain data" is based on a single small model and may not hold at larger scales where optimization dynamics differ. Scaling the training experiments or providing a justification for expected generalization would address this.

3. **Potential overhead of iterative generation calls is not quantified in the main text.** The method makes multiple generation calls (each producing τₖ tokens), and the paper focuses on token count as the efficiency metric. While the appendix (Section A.2, stripped by PDF parser) analyzes prefilling costs, the main text would benefit from a brief quantitative discussion of wall-clock latency or total inference cost relative to a single-shot baseline — especially for easy queries that could finish in very few chunks. This does not invalidate the token-count findings (which are standard in the literature), but would strengthen the practical efficiency claim.

4. **No systematic analysis of reasoning disruption.** The method inserts a hint into the model's own generated text, which could in principle cause incoherent continuation or incorrect reasoning on some examples. The ablation on injection position (Table 4) and the case studies in the appendix partially address this, but a structured error analysis (e.g., "in what fraction of cases does hint injection demonstrably alter the reasoning trajectory in a harmful way?") would make the "maintains performance well" claim more robust.

### Trivial
None.

## Nice-to-Haves
- Reporting token usage *excluding* injected hints would clarify how much of the reduction comes from the hint tokens vs. shorter reasoning chains.
- An explicit discussion of how Ours(Prompt) and Ours(Deer) are implemented procedurally (e.g., is the Prompt instruction retained in the input while hints are injected during generation?) would aid reproducibility, though the combinations are reasonably inferable from context.

## Removed Points
These points were flagged by reviewers but are removed after cross-checking:

- **"Multiple API calls ignored / efficiency metric misleading"** — The paper uses `client.completions.create` as a standard interface for model inference (local or remote). Token count is the standard efficiency metric in this literature, and the method's overhead is discussed in the (parser-stripped) appendix Section A.2. The paper's efficiency claims are about token reduction, which is properly validated. Wall-clock time would be a useful addition but is not a standard requirement in this subfield and does not invalidate the reported results.
- **"Combination with baselines is underspecified"** — The paper clearly states "Ours (baseline) denotes the combination of our ConciseHint and the baseline method." The combinations (Prompt instruction in input + hint injection during generation; Deer early exit + hint injection) are straightforward and inferable from the method description.
- **"Novelty overstated (Deer also intervenes during reasoning)"** — Deer terminates generation early (a form of post-hoc control). ConciseHint injects hints during generation (a form of active influence). The paper correctly distinguishes these in Sections 2.2 and 3. The dichotomy is precise and not overstated.
- **"Transition interval increases (supporting opposite conclusion)"** — The increase in transition interval (e.g., 113.42→118.66) is consistent with conciseness: the model produces fewer redundant self-checks, so the *distance* between surviving transition words naturally grows. This supports, not undermines, the paper's claims.

## Novel Insights
None beyond the paper's own contributions. The insight that injecting conciseness hints *during* generation (rather than before) is effective, and that adaptive interval/position control is critical to avoid accuracy degradation on hard queries, is the paper's core contribution. The reviews do not surface a meta-level observation that the authors themselves miss.

## Suggestions

1. **Add standard deviations or bootstrap confidence intervals to all accuracy numbers.** This is the single highest-leverage fix. Even simple error bars (e.g., ± from 5–10 runs) would allow readers to assess whether the claimed accuracy maintenance is credible vs. within noise, especially on AIME24 (30 problems).

2. **Run ConciseHint-T on at least one larger model** (e.g., Qwen3-4B) to demonstrate scalability of the learned embeddings. If compute is a constraint, frame the 1.7B results as preliminary and explicitly discuss anticipated behavior at larger scales.

3. **Include a brief wall-clock latency comparison** for a representative subset of benchmarks (e.g., Qwen3-4B on GSM8K), showing that the token savings translate into real speedup despite the iterative generation pattern.

4. **Add a structured error analysis** sampling, e.g., 50–100 cases where ConciseHint is applied, and annotating whether hint injection disrupts the reasoning trajectory. This would strengthen the claim that the method "maintains performance well."

## Comparative Score Analysis

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): EPiC (3.33), TL;DR (4.0), various withdrawn/rejected papers on LRM efficiency. These papers have more fundamental evaluation gaps or weaker ablations than ConciseHint.
- Middle anchors (3.5–7.5): PALU (5.0, Reject), DEER/Dynamic Early Exit (5.33, Accept), Think-with-Me (4.0, Reject), Heima (4.5, Reject). ConciseHint is closer to PALU/DEER in quality than to Think-with-Me or Heima.
- Strong anchors (> 7.5): Unrelated topics (multi-turn conversation, transduction, entity binding). Not directly comparable.

**Initial bracket: 4.0–6.0.**

**Round 2 — Narrowing within bracket:**
- PALU (5.0, Reject): Lagrangian formulation with strong theory, tested on 1.5B–14B models, but only one model family. ConciseHint has broader model/baseline coverage (Qwen3-4B/8B, DeepSeek-R1-14B, 4 baselines) but weaker theoretical framing. Similar evaluation rigor. **Comparable or slightly stronger than PALU.**
- DEER/Dynamic Early Exit (5.33, Accept Poster): Training-free, tested on 11 models × 10 benchmarks, achieves 19–80% token reduction. Both papers share similar weaknesses (no variance reporting, no reasoning quality analysis). DEER has better model coverage; ConciseHint has a more novel paradigm. **Slightly weaker than DEER due to narrower evaluation scale.**
- Dynamic Early Exit (5.33, Accept Poster): Similar strengths and weaknesses to ConciseHint but stronger empirical breadth. **ConciseHint is slightly below this anchor.**

**Final score: 5.0.** The paper proposes a genuinely novel paradigm with solid ablations. The key limitations — missing variance reporting (especially on the 30-problem AIME benchmark), training experiments only on the smallest model, and incomplete overhead quantification — prevent the evaluation from being fully convincing at this stage. These are addressable in revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>