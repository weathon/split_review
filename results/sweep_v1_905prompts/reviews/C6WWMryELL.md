Now I have enough calibration to write the review. Let me compile everything.

---

## Summary

This paper addresses the under-explored problem of *length volatility* in long-form LLM generation — the tendency of models to produce inconsistent output lengths when the same prompt is sampled multiple times. It contributes three things: (1) **VOLTBench**, a multi-dimensional benchmark (languages, complexity levels, structured/unstructured tasks, up to ~100k-word scale) that is the first to incorporate multiple-sampling stability evaluation; (2) an **attention trace analysis** that identifies Attention Collapse and Attention Instability as internal patterns correlated with volatile generation; and (3) **SELB**, a training-free decoding strategy that boosts section-title logits and suppresses failure tokens (EOS, filler phrases) to enforce structural compliance.

---

## Strengths

1. **VOLTBench provides the first systematic benchmark for length volatility with repeated sampling.** Table 1 shows it is the only benchmark among eight compared that explicitly includes both "Multiple Sampling" and "Stability Eval," while also covering structured + unstructured tasks, two languages, multiple complexity levels, and a length scale up to ~100k words. This fills a genuine gap: prior benchmarks evaluate single generations, missing the instability problem entirely.

2. **Multi-dimensional diagnostic analysis.** Figure 3 offers a systematic breakdown of volatility across English vs. Chinese, simple vs. complex instructions, and unstructured vs. structured output, revealing that structured tasks produce more stable generations. The fine-grained constraint analysis (Section 4.3.1) quantifies how performance collapses as context length increases — at the 500-section constraint task, no model delivered more than 40 correct sections out of 100.

3. **Identification of concrete failure patterns via attention traces.** Section 5 defines Attention Collapse (attention dropping to near-zero, correlating with premature termination) and Attention Instability (abnormally large attention spikes preceding section skipping). These provide an internal-mechanism vocabulary for a problem that prior work only observed at the output level.

4. **SELB is lightweight and training-free.** The method requires no additional training, no data collection, and no model modifications — it only modifies logits at decoding time. This pragmatic design means it can be applied to any autoregressive LLM with minimal overhead.

---

## Weaknesses

### Major

1. **SELB results are absent from the main comparison table (Table 2), making the method's evaluation impossible to assess fairly.** Table 2 lists 9 base models and 4 training-free decoding strategies (Repetition Penalty, Entropy-Stopping, Length Constraint, Lookahead Decoding) — all applied to Qwen2.5-7B — with full metrics. SELB is not included. The reader cannot compare SELB's LVC (14.02%), MLA (78.25%), or SCA (100%) against the baselines (e.g., Lookahead Decoding LVC=9.3%, Length Constraint MLA=22.4%) that the table is designed to present. This is the single most actionable fix the authors should make.

2. **The headline improvement numbers (148%, 69%) mix comparisons across different base models and are misleadingly stated.** The abstract says SELB "improves the mean output length of the base model by 148% and reduces the length volatility by 69%." In Section 6.3, the 69% volatility reduction is (45.4%−14.02%)/45.4%, which is relative to **LongWriter-8B** (a Llama-3.1-8B derivative), while SELB is applied to **Qwen2.5-7B**. The 148% figure appears to refer to MLA improvement (78.25% vs. LongWriter-8B's 31.6%), but the abstract says "mean output length" rather than "Mean Length Accuracy." The relevant base model comparison (Qwen2.5-7B alone: MLA=2.2%, mean output=445 words vs. Qwen2.5-7B+SELB: MLA=78.25%, mean output=15,651 words) is never reported in the same table. These are **apples-to-oranges** comparisons that overstate the method's advantage relative to its own base model.

3. **The connection between the attention-trace probing and the SELB method is narrative, not demonstrated.** The paper states that SELB "targets the identified internal patterns" (line 82, 86), but SELB is a rule-based heuristic that boosts section-title logits and suppresses EOS/filler tokens. There is no experiment showing that SELB modifies attention behavior (e.g., comparing attention traces with and without SELB). The probing identifies Attention Collapse and Instability; SELB addresses output-length control — these are related phenomena but the paper offers no mechanistic evidence that SELB fixes the attention patterns it documented. This weakens the claimed three-stage (benchmark → probe → mitigate) cohesion.

4. **The attention-trace analysis is anecdotal.** Only two examples are presented (Qwen2.5-7B and Qwen2.5-3B on one diary task, Figure 4). The paper provides no aggregated statistics (e.g., what fraction of generations exhibit Attention Collapse, correlation between attention-trace metrics and LVC/LSD across models). Without quantitative evidence, the claim that these are "common internal patterns" of length volatility is an interesting hypothesis, not a validated finding.

### Minor

5. **No ablation study of SELB's components.** The method combines structural enforcement (M_struct) and failure prevention (M_fail). Their individual contributions are not reported. A reader cannot tell whether the gains come from forcing section breaks, suppressing EOS, or both.

6. **SELB is only evaluated on the 100-section task in Section 6.3.** The benchmark spans multiple task types (story, code, diary, math), languages (English, Chinese), complexity levels, and length scales. The method's performance on other configurations is not reported in the main paper.

7. **Statistical reliability is limited.** N=5 generations per instruction with no confidence intervals or significance tests. While 5 samples are reasonable for expensive long-form evaluation, the paper's core claims about *volatility reduction* would benefit from bootstrap intervals on LVC.

8. **Failure patterns are described qualitatively.** The claim that "models failed in approximately half of the cases" for 50-section tasks is not tied to a precise operational definition of "failure," and per-instruction failure rates are not tabulated.

### Trivial

- The abstract uses "mean output length" when the 148% figure actually refers to Mean Length Accuracy (MLA), conflating two distinct concepts.

---

## Nice-to-Haves

- An ablation study of hyperparameters (β, τ_max, V_banned) would help understand SELB's robustness, though this is standard to defer to a revision.
- A computational cost analysis (e.g., time per generation with and without SELB) would be useful given the per-step logit modification.
- Extending the attention analysis from 2 examples to a systematic correlation study (e.g., number of attention peaks vs. LVC across models) would strengthen the probing contribution significantly.

---

## Removed Points

These points are flagged as removed; treat them with caution.

1. **"Generalization results rely on appendix material that cannot be evaluated."** — The instructions specify that weaknesses about missing appendix content should be removed because the parser strips appendix sections from all papers; they exist in the original submission.

2. **"Hyperparameters (β, τ_max, V_banned) are not discussed."** — The instructions specify removing nitpicks about undisclosed hyperparameters as reproducibility concerns.

3. **"Paper does not report results for SELB across all task types."** — Partially kept in Minor above, but the broad version was overclaimed; the paper does evaluate on the 100-section task and generalization is in the appendix.

4. **"The 100k claim may refer to the instruction set, not the output."** — VOLTBench's length scale is clearly stated as ~100k words, and the benchmark includes instructions up to 500 chapters. The claim is verifiable from the paper as written.

5. Several formatting/style nitpicks from the harsh critic.

---

## Novel Insights

None beyond the paper's own contributions. The key observation — that multi-sample length volatility is a distinct and measurable problem separated from single-generation quality — is the paper's own framing, and it is a genuinely useful one. The attention-trace identification of periodic refocusing signals and their failure modes (collapse/instability) is also the authors' own diagnostic finding.

---

## Suggestions

1. **Add SELB to Table 2.** This is the single most important change. Include Qwen2.5-7B+SELB in the bottom section alongside the other training-free decoding strategies applied to the same base model. This would allow direct apples-to-apples comparison of LVC, MLA, SCA, UCA, and FAD against the existing baselines.

2. **Clarify the headline numbers.** State explicitly in the abstract and contributions list what the 148% and 69% figures are relative to. If they are vs. LongWriter-8B, say so; if vs. the base model (Qwen2.5-7B), provide that comparison in the main table. The abstract currently says "base model" but means "LongWriter-8B" for these numbers.

3. **Temper the causal claims between probing and method.** Replace "targeting the identified internal patterns" with language like "informed by the observed failure modes, we design a heuristic that addresses their output-level manifestations."

4. **Quantify the attention analysis.** Add a simple correlation between attention-trace features (e.g., standard deviation of constraint attention across steps) and volatility metrics (LVC) across 3-5 models on 2-3 tasks.

5. **Add an ablation** comparing M_struct alone, M_fail alone, and the full composition on the 100-section task.

---

## Score and Decision

**Calibration details:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| HelloBench (QM2WoPu1It) | 4.75 (Reject) | 1 (middle) | Pure long-gen benchmark; the current paper adds probing+mitigation but its method evaluation is incomplete, making it somewhat stronger |
| Quantifying Variance (E2RyjrBMVZ) | 4.17 (Reject) | 1 (middle) | About evaluation variance; topically less relevant |
| PolyPythias (bmrYu2Ekdz) | 6.50 (Accept) | 1 (middle) | Well-executed study of training stability; cleaner narrative and more rigorous analysis than the current paper |
| LongWriter (kQ5s9Yh0WI) | 6.00 (Accept) | 2 (narrow) | Focused, well-executed work on long-form generation; the current paper is less focused and has weaker method validation |
| HELMET (293V3bJbmE) | 6.00 (Accept) | 2 (narrow) | Comprehensive benchmark; cleaner execution than the current paper |
| DAB Controlled Decoding (Duuerhutvq) | 5.75 (Accept) | 2 (narrow) | Training-free controlled decoding with theory; the current paper's SELB is simpler but less rigorously evaluated |

**Round 1 bracket:** 4.0–6.5 (the paper is clearly stronger than HelloBench at 4.75 but weaker than LongWriter at 6.00 due to evaluation gaps).

**Round 2 narrowing:** Anchors at 5.75–6.00 (Accept) have cleaner execution and/or more rigorous evaluation. The current paper's benchmark contribution is real, but the method evaluation (missing from Table 2, cross-model comparisons, no ablation) pulls it below these anchors. It sits between HelloBench (4.75) and the 5.75–6.00 papers — closer to HelloBench because the method validation is incomplete.

**Final score:** 5.0. The VOLTBench benchmark and the attention-trace probing are genuine contributions. The SELB method's evaluation, however, has structural gaps that prevent the paper from delivering on its full three-stage narrative. The headline improvements are stated over a mismatched baseline, and the method is absent from the main evaluation table. These issues are fixable but require substantial revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>