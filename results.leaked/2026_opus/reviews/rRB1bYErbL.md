Now I have enough calibration. Let me write the review.

## Summary
R-HORIZON proposes a query-composition pipeline that chains independent reasoning problems via an additive dependency (`v_{i+1} = a_i + (m_{i+1} − a_i)`) to build (a) a multi-horizon evaluation benchmark across 6 math/code/agent datasets evaluated on 25–26 LRMs and (b) RLVR training data for GRPO, reporting +7.5 on AIME24 over n=1 baseline training and large gains on composed evaluations. The empirical contribution is a broad, consistent demonstration that current LRMs degrade sharply as problems are chained, plus diagnostic analyses (effective reasoning length, localized reflection, budget allocation) and a usable training-data construction recipe.

## Strengths
- **Comprehensive empirical breadth in evaluation.** Figure 3 / Section 4.2 spans 25–26 LRMs (1.5B → 235B, including o4-mini, DeepSeek-R1, Gemini-2.5-Pro/Flash, Claude-Sonnet-4, Qwen3-235B-Thinking) across MATH500, AIME24, AIME25, AMC23, LiveCodeBench, and WebShaper. The consistent degradation pattern (e.g., DeepSeek-R1 86.2 → 24.6 on AIME25 from n=1 to n=5) is a substantive finding that supports the paper's central claim.
- **Positive RL result with internal corroboration.** Table 1 shows R1-Qwen-7B trained on n=2 composed data improves AIME24 origin accuracy from 48.3% → 65.4% (+17.1) and AIME24 (n=2) from 16.4% → 34.1% (+17.7), and Figure 4 shows the composed-data curves consistently lead. The rollout-efficiency analysis (Figure 10) gives a concrete mechanistic story (~20% more non-degenerate-reward samples for n=2/n=4), connecting *why* composed training helps to *what changes* in the GRPO update.
- **Diagnostic analyses that go beyond aggregate accuracy.** Figure 6 quantifies effective-reasoning-length thresholds per model size (≈4–6k tokens for 7B, 8–10k for 32B on MATH500); Figure 7 reports that >50% of problems show no long-range reflection; Figure 8 documents skewed token-budget allocation toward earlier problems. These are concrete, testable diagnostics tied to specific figures rather than hand-waving.

## Weaknesses

### Fatal
None.

### Major
- **The dependency is structurally an additive offset that reduces to the original problem.** Algorithm 1 (lines 92–106) defines `f_i(x) = x + (m_{i+1} − a_i)`, and the prompt prepends the constraint `v_{i+1} = a_i + (m_{i+1} − a_i)`. Because `(m_{i+1} − a_i)` is a literal constant in the prompt and `m_{i+1}` was the original key variable, computing `v_{i+1}` after recovering `a_i` simply yields `m_{i+1}` — i.e., problem i+1 collapses back to the original problem with no shape change. This is consistent with the paper's own observation in Section 5.1 that Dependency Reasoning Errors are small. The benchmark still meaningfully measures whether models can solve chained-but-otherwise-isolated problems, but the framing — "long-horizon reasoning … sometimes thousands or even millions of steps" (Section 1) — is not what the construct delivers, and §3.1 does not justify this design choice or compare against non-trivial dependencies (e.g., shape-changing or branching ones). The three composition modes advertised in Figure 2 ("Directly," "Sequential," "Graphic") collapse to sequential in the main experiments; "Graphic Compose" is precisely the more interesting case and is missing from the headline results.
- **The "expected accuracy" baseline (Eq. 4) does not isolate long-horizon reasoning capacity.** Eq. 4 takes the product of atomic pass rates, which assumes problem independence AND that per-problem solvability is unchanged when embedded in a long composed prompt. The composed setting changes context length, output-token budget, in-context position, and decoding distribution — so the actual-vs-expected gap in Figures 1 and 6 conflates "limited effective reasoning length" with mundane generation-budget and position effects. This matters because Figure 1 and Figure 6 are the paper's central evidence for the effective-reasoning-length claim. A budget-controlled or token-prepended-but-single-question control is needed to attribute the gap to reasoning ability per se.
- **Truncation contaminates the headline degradation curves.** Section 4.1 states "We set the generation length to 64k tokens to avoid truncation," but Figure 5 shows non-trivial Output Truncation and Early Stop categories, and several 7B models read 0.0% at n=5 on AIME-style data (Figure 3 / lines 174–212). At AIME-difficulty problems, DeepSeek-R1's per-problem CoT alone can approach 20k tokens, so the per-sub-problem budget at n=5 is already strained. The paper interprets these collapses as reasoning failure, but does not stratify accuracy by error type or run a budget-scaled control (e.g., max_tokens scaled with n). Without this, the steep drops cannot be cleanly read as "limited reasoning capacity" rather than "ran out of tokens."

### Minor
- **RL comparison may be sample/diversity-confounded.** Table 1 contrasts "Naive Training Data (n=1)" with "w/ composed queries (n=2/4/mixed)." The paper does not state whether examples are matched in count, total underlying problems, or total tokens; if matched in *example count*, the n=2 condition has seen ~2× the underlying problems. Figure 10 also shows the composed conditions have substantially more effective (non-degenerate-reward) samples per batch, meaning the GRPO signal is denser. Both could plausibly explain part of the +7.5 single-horizon AIME24 gain independent of "long-horizon training." This is in principle addressable by matched-budget reporting and does not need to invalidate the qualitative result.
- **RL generality rests on one base model.** All RL experiments are on R1-Qwen-7B with 40k context. The "R-HORIZON as training paradigm" framing would be much more credible with at least one second base model.
- **Reflection metric is keyword-based and not validated.** Section 5.1 / Figure 7 operationalize reflection as counts of phrases like "wait" and "but…" with a "long-range reflection" derived from this. The "highly localized reflection" finding is interesting but rests on a brittle heuristic; a small human spot-check or alternative operationalization would harden it.
- **n=4 vs n=2 trade-off discussion.** Table 1 shows n=4 underperforming n=2 on AIME24 (origin) but outperforming on harder/higher-horizon settings. The paper reads this as monotonic improvement with horizon, but an equally plausible reading is that n=4 trades single-horizon accuracy for multi-horizon under an all-or-nothing reward — the discussion in §4.3 does not engage with this trade-off explicitly.
- **Section 5.2 / Figure 9(b) "alleviates overthinking" claim.** Shorter responses on composed tasks could mean either efficient reasoning OR premature truncation/early-stopping; the conclusion would be cleaner with a stratification by completed-vs-truncated outputs.

### Trivial
None retained (apparent numerical oddities such as `127.6` in the Qwen3-32B MATH500 row are parser artifacts and are not held against the paper).

## Nice-to-Haves
- A non-trivial dependency variant (shape-changing or branching, not additive) that materially alters problem i+1 — this would let the "long-horizon reasoning" framing actually match the construct.
- A budget-scaled evaluation (max_tokens scaling with n) plus truncation-stratified accuracy as a robustness check on the effective-reasoning-length claim.
- Matched-budget RL comparison (matched in underlying-problem count and/or non-degenerate-gradient samples) to attribute the +7.5 AIME24 gain cleanly.
- Repeat the headline RL recipe on at least one non-R1-Qwen-7B base model.
- Report the advertised "Graphic Compose" mode in the main evaluation, since it is the only mode that would create genuinely multi-dependent structure.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"Numbers in Figure 3 like 127.6 and 0.0/20.0/0.0 sequences look unreliable."* (Harsh critic, §4.2 notes.) These are PDF parser/OCR artifacts in the extracted text, not author errors.
- *"Missing related works / no proofs in appendix / underspecified hyperparameters."* (Various reproducibility nitpicks.) Hard rule: appendix/reference content is parser-stripped; reproducibility nitpicks about details normally in appendix are not held against the paper.
- *Strength: "Composition method is simple, controllable, and applicable across diverse task domains."* Demoted — overlaps with empirical-breadth strength already retained and is partially in tension with the "additive dependency" weakness.
- *Strength: "Identification of specific failure modes ... going beyond mere benchmarking to diagnose why performance degrades."* Kept (rephrased) as the third retained strength; original phrasing was retained because it cites specific figures.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observations are inside the paper itself: per-model "effective reasoning length" thresholds tied to model size (Figure 6), the highly-localized nature of LRM reflection (Figure 7), and the front-loaded token-budget allocation (Figure 8). These are useful empirical regularities about LRMs that go beyond the benchmark headline.

## Suggestions
- Replace or augment the additive dependency with at least one shape-changing variant (e.g., the previous answer selects which sub-question or which operator) and re-run a smaller-scale evaluation. Either result is interesting: if degradation persists, the conclusions strengthen; if not, the current "long-horizon" framing should be softened.
- Add a length-controlled control: prepend ~n × atomic-prompt-length of unrelated problem text but ask only one question. If the degradation curves resemble the composed case, the operative variable is context-length / budget, not multi-problem reasoning.
- Report Table 1 RL comparisons matched on (i) underlying problem count and (ii) average non-degenerate-reward samples per step. The +7.5 AIME24 finding becomes a much stronger claim if it survives matching.
- Soften "thousands or even millions of steps" framing in Section 1 to match the actually-evaluated horizons (n up to 20 for MATH500, up to 5 for AIME).
- Validate the reflection metric on a small annotated subset, since "localized reflection" is a non-trivial diagnostic finding and currently rests on a keyword heuristic.

---

## Axis Evaluation
- **Originality:** Moderate. Chaining single-horizon problems into multi-horizon evaluations is not novel (the paper cites NEST, GSM-Infinite as predecessors), but combining it with an RLVR training recipe and a broad cross-model evaluation has some originality.
- **Importance of question:** High. How LRMs behave under composed problems is a real and timely question.
- **Are claims well supported?** Mixed. The descriptive claim ("LRMs degrade as composition grows") is well supported by Figure 3. The causal claims ("limited effective reasoning length," "RL with composed data improves single-horizon reasoning *because of* long-horizon training") are partially confounded by truncation, expected-accuracy baseline assumptions, and unmatched RL budgets.
- **Soundness of experiments:** Mostly adequate but with the identified confounds.
- **Clarity:** Generally clear; Algorithm 1 is precise; figures are informative.
- **Value to community:** A usable benchmark + training pipeline with concrete RL improvements; community value is real, conditional on revisions tightening the central interpretations.

## Calibration Anchors
- **Round 1** (bracketing pass):
  - `jOuHjFw71C.md` — avg 3.00, LRM planning evaluation (much narrower scope, weaker setup than R-HORIZON).
  - `koza5fePTs.md` — avg 2.00, LLM planning benchmark (weaker than R-HORIZON).
  - `BVACdtrPsh.md` — avg 3.00, multimodal cognition benchmark (different topic, weaker).
  - `o3V7OuPxu4.md` — avg 3.00, StarCraft II Arena (different topic).
  - `eNCyY81aW6.md` — avg 5.00, FACTOR (long-context complex reasoning benchmark, similar in spirit but no training contribution; mixed soundness reviews); R-HORIZON is broader and has RL gains.
  - `0YXckVo7Kw.md` — avg 5.50, MMCOMPOSITION VLM benchmark (different domain).
  - `1Xg4JPPxJ0.md` — avg 6.00, Transformers compositional reasoning (more theoretical/synthetic; R-HORIZON is broader empirically but messier methodologically).
  - `SVRRQ8goQo.md` — avg 7.00, KOR-Bench (cleaner conceptual contribution).
  - `YrycTjllL0.md` — avg 9.00, BigCodeBench (significantly broader and more polished).
  - `jOmk0uS1hl.md` — avg 8.00, Training on the Test Task (cleaner methodological contribution).
  - `HnhNRrLPwm.md` — avg 8.00, MMIE benchmark.
  - `KIgaAqEFHW.md` — avg 8.00, miniCTX.
  
  Initial bracket: **5 to 7**.

- **Round 2** (narrowing within 5–7):
  - `OhUoTMxFIH.md` — avg 5.67, Robotouille asynchronous planning benchmark, accepted (cleaner construct; R-HORIZON has bigger evaluation but a weaker dependency design).
  - `qHpfxfnIq3.md` — avg 5.40, ToolComp multi-tool reasoning benchmark, rejected (close peer; similar issues with multi-step construct validity).
  - `5iWim8KqBR.md` — avg 5.50, memory-efficient algorithm distillation (different topic).
  - `eqVu9eaVAB.md` — avg 5.50, hierarchical search combinatorial reasoning (different topic).
  - `1bbPQShCT2.md` — avg 6.50, I-PHYRE interactive physical reasoning, accepted (more novel construct).
  - `NUD03NBDOE.md` — avg 6.75, ActionReasoningBench, accepted (more rigorous diagnostic benchmark with cleaner construct).
  - `fp6t3F669F.md` — avg 6.25, AgentQuest long-horizon agent benchmark, accepted (closest match — broad benchmark on long-horizon tasks; R-HORIZON adds RL but has more methodological concerns).
  - `2uQBSa2X4R.md` — avg 6.50, Robust Gymnasium (different topic).
  - `zpENPcQSj1.md` — avg 6.33, Generalizing reasoning to longer lengths, accepted (more theoretical, cleaner).
  - `w6nlcS8Kkn.md` — avg 6.67, "To CoT or not to CoT," accepted (broader empirical meta-analysis, cleaner claim).
  - `4L0xnS4GQM.md` — avg 5.50, Chain-of-Table.

Round 2 narrows the bracket to **5–6.5**. R-HORIZON sits comparably to ToolComp (5.40) on construct concerns but adds breadth + a real RL training contribution, pulling it above ToolComp. It is below AgentQuest (6.25) because the dependency design is shallower and the central metric (expected accuracy product) is more contestable. Below ActionReasoningBench (6.75) because that paper has a cleaner construct. Above 5.5 anchors like Robotouille (5.67) is debatable — Robotouille has a cleaner construct but narrower scope; R-HORIZON has broader empirical reach but stronger overclaiming.

Final position: roughly between ToolComp (5.40, rejected) and AgentQuest (6.25, accepted), closer to the middle. The empirical breadth and RL findings are real, but the dependency design, expected-accuracy metric, and truncation/RL-matching confounds are concrete enough to keep it below acceptance threshold. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>