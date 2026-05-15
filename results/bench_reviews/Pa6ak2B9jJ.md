## Summary

This paper introduces AUTO-RT, a reinforcement learning framework for automatic jailbreak strategy exploration in LLM red-teaming. It decomposes the attack model into a trainable strategy generator (AM^g) and a fixed rephrasing model (AM^r), and proposes two key techniques—Dynamic Strategy Pruning (DSP) for eliminating redundant search branches early, and Progressive Reward Tracking (PRT) with a novel First Inverse Rate (FIR) metric for densifying sparse reward signals. The method is evaluated on 16 white-box and 2 black-box LLMs, showing consistent improvements over RL-based baselines on attack success rate, semantic diversity, and defense generalization diversity.

## Strengths

- **Hierarchical strategy decomposition is a useful framing for red-teaming.** Separating high-level strategy generation (AM^g) from concrete query instantiation (AM^r) enables more systematic exploration of attack tactics. The ablations confirm that this strategy-level approach improves over the standard single-stage formulation.

- **Progressive Reward Tracking with the FIR metric is well-validated.** Figure 4 provides clear empirical evidence that the FIR-identified downgrade model yields the best attack performance across six target models, and that further weakening degrades results. This validates the design rationale for PRT.

- **Extensive evaluation across 18 models.** The paper tests on 16 white-box and 2 black-box models spanning Llama, Mistral, Yi, Gemma, Qwen, and R2D2 families. This breadth strengthens the claim that the method generalizes across architectures and alignment levels.

- **Ablation study demonstrates complementary contributions of DSP and PRT.** Table 2 shows that each component independently improves performance, and their combination yields the best overall results on most models—particularly on ASR where PRT contributes substantially (e.g., Gemma 2 2B: RL 6.15 → +PRT 25.30 → AUTO-RT 48.15).

- **FIR-based downgrade model selection is principled and validated.** The controlled experiment using six progressively weakened models (M1–M6) shows that the FIR metric consistently identifies the optimal downgrade strength across targets (Figure 4).

## Weaknesses

### Major

- **The headline claim ("outperforming existing methods") conflates comparisons against ablations and against true SOTA baselines.** The main results (Table 1) compare AUTO-RT against FS, IL, RL—which are ablations of the same framework, not existing jailbreak methods. When compared against AutoDAN (Table 3), AUTO-RT achieves lower first-round ASR (38.38 vs. 55.23). The paper then emphasizes DeD (defense generalization diversity) to argue superiority, but DeD conflates first-round attack effectiveness with diversity—a method with lower first-round ASR faces a weaker defense in the second round, making cross-method DeD comparisons difficult to interpret. The abstract's claim of "outperforming existing methods" is therefore overstated given the evidence presented.

- **The ASR_st (top-100 selection) metric introduces potential selection bias that is not accounted for.** The primary effectiveness metric evaluates only the top 100 strategies selected from up to 9,000 episodes. The paper does not specify whether baseline methods (FS, IL, RL) are evaluated under the same top-100 selection mechanism or on a per-output/per-batch basis. If baselines do not also generate thousands of candidates from which a top-100 is selected, the comparison is structurally unfair and the performance gap could be partially or fully explained by this selection asymmetry.

- **Missing data: AUTO-RT's SeD is blank in Table 3 (human-based comparison).** Semantic diversity is one of the paper's three evaluation dimensions, yet the SeD cell for AUTO-RT is empty. This omission makes the claimed "near-human-level sustained attack capabilities" harder to evaluate and weakens the completeness of the comparison.

### Minor

- **The exploitability-severity motivation is articulated but never operationalized.** The introduction frames exploitability and severity as core concepts motivating the approach, but no experiment measures exploitability or demonstrates that AUTO-RT discovers flaws that are simultaneously high-exploitability and high-severity. The evaluation focuses entirely on ASR and diversity, not on the ease of triggering identified vulnerabilities.

- **The rephrasing model (AM^r) is a fixed Vicuna-7B with no ablation.** The paper never tests whether a more capable AM^r would improve results, or whether AM^g could directly generate attack queries without the separate rephrasing step. This design choice is asserted but unexamined.

- **Black-box setting: the ICL-based downgrade construction is underspecified.** The paper states it uses "in-context learning (ICL) approach to obtain downgrade model" but does not clarify what model receives the ICL treatment (the target model itself, or Vicuna-7B?). The containment assumption (Figure 2) is unlikely to hold across model families, and the black-box results (~15% ASR on Llama 3 70B and Qwen 2.5 72B), while tripling the RL baseline, remain modest in absolute terms.

- **The "near-human-level" claim is imprecise.** AUTO-RT's ASR (38.38) sits between Human Templates (37.35) and AutoDAN (55.23). Claiming "near-human-level" is defensible relative to HT but not as a general characterization.

### Trivial

- **Inconsistent metric naming.** The paper uses ASR_st, ASR_rst, and ASR_att seemingly interchangeably (cf. Eq. 6, Table 1 header, Figure 3 caption, Table 2 header). These should be unified.

- **The source of the "up to 16.63%" improvement figure** cited in the abstract and introduction is not clearly traceable to any specific result in the main text.

## Nice-to-Haves

- A controlled experiment where AutoDAN (or another strong baseline) also generates O(9000) candidates with top-100 selection, to establish whether the performance gap is real or an artifact of selection bias.
- A direct comparison of average ASR over all generated strategies (without top-100 selection) for all methods.
- Empirical validation of the containment assumption (Figure 2) for the specific downgrade models used, showing that target-vulnerable strategies are a subset of downgrade-vulnerable strategies.

## Removed Points

These are points from the reviews that were removed as invalid, factually incorrect, or overly nitpicky:

1. *"PRT's contribution is not cleanly separated from DSP in the ablation data"* — **Overstated / cherry-picked.** On most models (Vicuna 7B/13B, Gemma 2B, Qwen 1.5 7B/14B, etc.), full AUTO-RT substantially outperforms +DSP alone. Only 2 of 10 models show +DSP matching AUTO-RT, which supports the paper's claim of complementary roles.

2. *"The paper provides no evidence that PRT outperforms RL without PRT in the black-box setting"* — **Factually wrong.** Table 4 directly compares RL (4.99) vs. AUTO-RT (14.88) on Llama 3 70B, and RL (4.53) vs. AUTO-RT (14.47) on Qwen 2.5 72B.

3. *"The ICL-based 'downgrade' produces a different model entirely, so the containment argument does not apply"* — The paper does not claim the containment property holds across model families in the black-box setting. The ICL approach is presented as an approximation, and the results are reported as modest improvements.

4. *"Figure 3 does not specify whether both methods use the same total number of samples"* — The paper states both methods use 9,000 episodes partitioned into 1,000-episode stages, making the comparison at equal sample counts.

5. *"Minor formatting/style concerns"* — Parser artifacts, not author errors.

## Novel Insights

The strongest insight to emerge from the reviews—beyond the paper's own contributions—is that the STRENGTH-WEAKNESS asymmetry in the red-teaming evaluation literature is an open methodological problem. The paper's top-100 selection metric is a reasonable attempt to measure strategy-level effectiveness, but it exposes a broader issue: how should "discovering a good attack strategy" be measured when the strategy can be instantiated thousands of different ways? The field lacks a standard protocol for this, and the paper's approach (while imperfect) surfaces this gap rather than resolving it. Similarly, the DeD metric's confounding of first- and second-round effectiveness points to the difficulty of measuring diversity independently of raw attack power.

## Suggestions

1. **Tighten the claims in the abstract and introduction.** Replace "outperforming existing methods" with more precise language, e.g., "substantially improving over RL-based baselines within the strategy-level red-teaming formulation and achieving competitive/complementary performance relative to template-based methods like AutoDAN."

2. **Clarify the evaluation protocol for all baselines.** Explicitly state whether FS, IL, and RL baselines are evaluated using the same top-100 selection from 9,000 episodes. If not, add a controlled comparison where all methods are evaluated under an identical protocol, including reporting average ASR without selection.

3. **Fill in the missing SeD value for AUTO-RT in Table 3** and explain why it was absent.

4. **Add variance or confidence intervals** for the black-box results (Table 4), and clarify the ICL-based downgrade construction: which model receives ICL, and how does this relate to the containment assumption?

5. **Operationalize or drop the exploitability-severity framing.** Either add a simple measure (e.g., minimum perturbations needed to turn a benign prompt into a successful attack) or acknowledge that this is motivational framing not evaluated empirically.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to Paper Under Review |
|------|-----------|----------------------------------|
| `c2BygWVqag.md` (STAR) | 5.50 | STAR has stronger methodological novelty (latent space) but narrower evaluation (7 models). AUTO-RT has broader evaluation but weaker SOTA comparisons. Comparable quality; AUTO-RT slightly weaker due to overclaiming. |
| `ilnKzaQSCh.md` (ADJ) | 5.50 | ADJ has heavier theoretical machinery with questionable necessity. AUTO-RT is more practical and empirically grounded. Comparable overall. |
| `11z2ZV85eV.md` (Morpheus) | 5.00 | Morpheus has stronger absolute ASR but weaker novelty (prompt engineering concerns). AUTO-RT has more technical depth in RL formulation. AUTO-RT slightly stronger. |
| `3MlMp7vZpl.md` (iART) | 4.67 | iART uses a weak attacker (GPT-2) and limited evaluation. AUTO-RT is clearly stronger. |
| `KdI9luPqaB.md` (SeqRL) | 4.00 | SeqRL has narrow evaluation (one benchmark). AUTO-RT is substantially stronger in breadth and technical contribution. |

### Final Score

The paper makes genuine contributions (hierarchical strategy decomposition, PRT with FIR validation, broad evaluation) but overstates its results relative to existing methods and has unresolved concerns about evaluation fairness (top-100 selection protocol, missing data in Table 3). Balanced against the anchors, this is a borderline paper—weaker than STAR (5.50, Accept) on methodology and claims, stronger than iART (4.67, Reject) and SeqRL (4.00, Reject) on breadth and technical depth.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>