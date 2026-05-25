Now I have a solid understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

This paper identifies and characterizes the "priming vulnerability" in masked diffusion language models (MDLMs), where an affirmative token from a harmful response appearing at an intermediate denoising step can steer generation toward harmfulness even in safety-aligned models. The paper proposes Recovery Alignment (RA), which trains MDLMs to recover safe responses from intentionally contaminated intermediate states. Experiments across three MDLMs, multiple attack families (anchoring, GCG, PAD, DiJA, PAIR, ReNeLLM, Crescendo), and 11 general-capability benchmarks show that RA substantially reduces the priming vulnerability (ASR at early intervention steps drops from ~17% to 0% on LLaDA) while largely preserving task performance.

## Strengths

1. **Clear quantitative evidence of a novel vulnerability.** Figure 2 shows that injecting a single token from a harmful response at denoising step 1 raises ASR from 2% to ~17–40% across models, and by step 16 it exceeds 80%. This cleanly demonstrates that the priming vulnerability is real, large, and specific to the MDLM denoising architecture. (Section 4.1, Figure 2)

2. **First-Step GCG shows the vulnerability is exploitable without intervention.** Table 1 reports that First-Step GCG achieves 58% ASR on LLaDA Instruct (vs. 20% for Monte Carlo GCG) while being ~20× faster, proving that a realistic attacker with no access to the denoising process can still exploit the vulnerability. (Section 4.2, Table 1)

3. **RA nearly eliminates the priming vulnerability.** Table 2 shows RA reduces ASR to 0.0% at t_inter=1 on LLaDA and LLaDA 1.5, and to 1.3% at t_inter=4 on LLaDA Instruct, dramatically below all baselines (MOSA: 24.0% at t_inter=4). The ablation (RA w/o inter) confirms that training from contaminated states is essential — removing it raises ASR to >20% at t_inter=4. (Section 6.2, Table 2)

4. **General capability is preserved across 11 benchmarks.** Table 4 shows RA changes average accuracy negligibly (e.g., LLaDA: 52.2% → 52.6%), with slight improvements on TruthfulQA and MBPP. This alleviates the concern that the defense degrades utility. (Section 6.3, Table 4)

5. **Ablation study validates key design choices.** Figure 3a shows monotonic robustness improvement with larger t_max, and Figure 3b demonstrates that linear scheduling of t_inter consistently outperforms uniform and constant scheduling, confirming the curriculum's importance. (Section 6.4, Figure 3)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Imprecise "affirmative token" framing.** The paper defines the vulnerability in terms of "affirmative tokens" that "endorse or advance a harmful intent" (Section 4). However, the anchoring attack injects the full harmful response and then re-masks, so the visible tokens at intervention are simply tokens sampled from a harmful response — many are neutral content words (e.g., "steps", "follow") rather than semantically affirmative words like "Sure" or "Yes." The term "affirmative token" implies a narrower class than what the evidence supports. A more precise characterization (e.g., "any token from a harmful response") would strengthen the conceptual contribution.

2. **Robustness against conventional jailbreaks is uneven.** The paper states RA "enhances robustness against conventional jailbreak attacks," but Table 3 shows mixed results. While PAIR and Crescendo see large reductions, ReNeLLM improvements are modest (LLaDA: 92.7→72.3, LLaDA1.5: 96.7→71.7) and MMaDA *increases* on ReNeLLM (79.3→81.7). The paper mentions this limitation in passing but the abstract and conclusion frame the robustness gain as a singular positive outcome, which overstates the evidence. The claim should be calibrated to the attack family.

3. **Theorem 4.1 rests on an unverified monotonicity assumption.** The central theoretical claim that the first-step log-likelihood lower-bounds the full denoising likelihood depends on an assumption that the log-probability of the exact target response is non-decreasing across steps. The paper provides intuition for why this might hold and cites an empirical check in the appendix, but the assumption is not formally justified and could fail for specific intermediate states. The theorem is presented as a rigorous result; it would be more appropriate to frame it as a motivated heuristic. (The empirical success of First-Step GCG is not harmed by this — the method works regardless.)

4. **Minor numerical inconsistency.** Section 4.1 states that ASR increases from 2% to 21% for LLaDA Instruct at t_inter=1, but Table 2 reports the same condition at 17.3%. (The Figure 2 caption also plots LLaDA Instruct at ~40% at step 1/128, adding confusion.) These numbers should be reconciled.

5. **No analysis of what RA fails on.** The paper acknowledges RA "remains imperfect against strong attacks" but provides no qualitative breakdown of the cases where it still fails. Understanding whether failures are concentrated on specific prompt categories or response types would deepen the analysis and suggest targeted improvements.

### Trivial
None.

## Nice-to-Haves

- **Training cost reporting.** The paper reports 2,500 training steps for RA but no wall-clock time or GPU hours, which would help practitioners assess the overhead.
- **Reward model validation.** The paper uses DeBERTaV3 as a reward model without reporting its agreement with GPT-4o or human judgments on safety scoring. A brief calibration would increase confidence that the reward is not driving undesired behavior.
- **Refusal naturalness evaluation.** Table 4 shows general capability is maintained, but there is no evaluation of whether the style of safe responses is natural (e.g., does the model still issue appropriate refusals, or produce vacuous safe strings?).
- **Extension to continuous DLMs.** A short discussion of whether the priming mechanism generalizes to continuous diffusion LMs would broaden the impact.

## Removed Points

1. **Baseline implementation and fairness (SFT/DPO adaptation to MDLMs).** The harsh critic argues that the paper does not specify how SFT and DPO were adapted to the masked diffusion framework. However, the paper states "Full baseline configurations are provided in Appendix D.6." Since the appendix is stripped by the PDF parser and the paper explicitly references it for these details, this criticism reflects a parser artifact, not an author omission. Per the guidelines, weaknesses about missing appendix content that the parser strips are removed.

2. **Theoretical grounding of First-Step GCG (the "fatal" framing).** The critic's concern about the monotonicity assumption being "asserted rather than proven" is valid as a minor point (kept above), but the critic also implies this undermines the paper's contribution. The theorem is presented with an explicit assumption, the intuition is stated, empirical validation is cited. The First-Step GCG method works well empirically regardless of whether the bound is tight in all cases. This does not rise to a structural or fatal flaw.

## Novel Insights

The harsh critic's observation that the "affirmative token" framing is conceptually imprecise is insightful — the paper's own anchoring attack does not specifically target semantically affirmative words but rather any token sampled from a harmful response. This suggests the actual mechanism may be broader than the paper's terminology implies: the vulnerability might not be about "affirmation" in a semantic sense but about any token that is consistent with a harmful trajectory, regardless of its affirmative content. The paper's contributions are stronger if framed in terms of "any token from a harmful response" rather than "affirmative tokens."

## Suggestions

1. Replace the "affirmative token" terminology with more precise language (e.g., "a token from a harmful response" or "a content token consistent with a harmful trajectory") throughout the paper, or run a controlled experiment isolating semantically affirmative tokens from neutral content tokens to validate whether the vulnerability is specifically about affirmation.

2. Calibrate the robustness claims in the abstract and conclusion to acknowledge the uneven performance across attack families, particularly the limited benefit on ReNeLLM and the negative result on MMaDA.

3. Frame Theorem 4.1 as a motivated heuristic rather than a formal theorem, removing the risk of misleading readers about the rigor of the theoretical contribution.

4. Provide a qualitative analysis of failure cases (e.g., which prompts/states RA still fails on) to make the limitations section more actionable.

5. Reconcile the numerical discrepancy between the Section 4.1 claim (2%→21%) and the Table 2 value (17.3% at t_min=1) for LLaDA Instruct.

## Score and Decision

**Calibration Summary**

*Round 1 bracket:* I identified the plausible score range as 3.5–7.5 after comparing against three topic-band queries and two weakness-anchored queries.

**Anchor comparison table:**

| Anchor ID | Avg Score | Round | Query Bucket | Comparison |
|-----------|-----------|-------|-------------|------------|
| 6Mxhg9PtDE (Safety Alignment — Few Tokens Deep) | 9.50 | R1-topic-high | Topical (ARM safety alignment) | Much stronger: deeper analysis, cleaner experiments, better framing. Paper under review is not at this level. |
| Bo62NeU6VF (Backtracking Improves Safety) | 8.00 | R1-topic-high | Topical (generation safety) | Stronger: more general method, extensive evaluation, multiple models. Paper under review is narrower (MDLM-specific). |
| WNvvwK0tut (Scaling up MDMs) | 6.50 | R2 | Topical (MDLMs) | Similar tier: both make solid contributions to the MDLM literature but with different focuses (scaling vs. safety). |
| 0VZP2Dr9KX (Baseline Defenses) | 5.25 | R1-topic-mid, R2 | Weakness (defense evaluation) | Comparable: both evaluate defenses against jailbreaks, but this paper has a novel finding (priming vulnerability) that the baseline paper lacks. |
| u08UxVNdIo (Diffusion Attacker) | 4.75 | R1-topic-mid, R2 | Weakness (diffusion jailbreak) | Weaker: more questionable methodology, inadequate baselines, narrower metrics. Paper under review has stronger empirical support. |
| 5kMwiMnUip (NEMESIS) | 1.40 | R1-topic-low | Topical (jailbreak) | Much weaker: survey-like paper with no novel contribution. Paper under review has clear novel findings. |
| BeOEmnmyFu (Playing Language Game) | 2.50 | R1-topic-low | Topical (jailbreak) | Much weaker: simplistic approach, poor evaluation. Paper under review is substantially stronger. |

*What the low-band anchors failed at:* The low-band papers (scored 1.4–3.0) lacked novel findings, had poor experimental methodology, or presented trivial contributions. The paper under review does **not** share those failures — it has a genuine novel finding (priming vulnerability), reasonable methodology, and broad evaluation.

*Round 2 narrowing:* Within the 3.5–7.5 bracket, I compared against anchors at 4.75 (Diffusion Attacker), 5.25 (Baseline Defenses), 6.50 (Scaling up MDMs). The paper is stronger than the 4.75–5.25 papers (which have more significant methodological issues), and weaker than the 8.00+ papers (which are cleaner and more comprehensive). It sits naturally alongside the 5.5–6.5 range: a solid, novel contribution with some imprecision in framing and presentation issues that do not threaten the core claims.

*Final score determination:* The paper has no fatal or major weaknesses. The surviving weaknesses are minor (imprecise framing, uneven robustness claim, unverified theoretical assumption, numerical inconsistency). The core finding is genuine and well-supported. This places the paper clearly above the 4–5 range (where papers have substantive methodological flaws) and below the 7+ range (where papers are exceptionally clean and comprehensive). Within the 5.5–6.5 range, the paper's novelty (first systematic study of priming vulnerability in MDLMs) and empirical breadth (3 models, multiple attack families, 11 benchmarks) justify 6.0 rather than a lower score.

**Score:** 6.0

**Decision:** Accept

The paper identifies a real and previously underexplored vulnerability in MDLMs, provides a clean demonstration of its severity, and proposes a principled mitigation that is convincingly shown to work across multiple models and attack types. The weaknesses are addressable through presentation improvements and do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>