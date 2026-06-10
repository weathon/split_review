Now I have enough calibration data. Let me finalize the review and score.

**Round 1 bracket**: 5.5 to 6.5

**Round 2 anchors comparison**:
- FiLM (4.25, Reject): ILM is clearly better — stronger experiments, clearer novelty, more diagnostic evaluation.
- Integrating Planning (4.75, Reject): ILM is substantially better — novel method vs. auxiliary training task.
- SEDD (6.60, Reject): Comparable novelty; SEDD has stronger theory but evaluation gaps. ILM has more impressive planning results but weaker text generation claims.
- Scaling MDMs (6.50, Accept): Similar contribution level — practical demonstration of new/existing paradigm.
- Beyond Auto-Regression/SDTT (7.00, Accept): More mature, more extensive, stronger practical impact.
- Retrieval is Accurate Generation (7.00, Accept): Stronger paradigm shift with broader evaluation.

ILM sits slightly below SEDD/Scaling MDMs (6.5-6.6) due to the overclaimed text generation results and unexamined length confound, but well above the rejected papers at 4-5. Score: **6.0**.

---

## Summary
This paper introduces Insertion Language Models (ILMs), a sequence generation paradigm that inserts tokens at jointly-predicted positions using a biased denoising objective and a stopping classifier. The method is evaluated on synthetic planning tasks (star graphs, zebra puzzles) and medium-scale text generation/infilling, demonstrating dramatic advantages over ARMs and MDMs on planning tasks and competitive performance on text generation.

## Strengths
- **Dramatic outperformance on planning tasks with variable-length dependencies (Table 1):** On Star_medium and Star_hard, ILM achieves 100.0% and 99.1% accuracy vs. MDM's 36.5%/21.0% and ARM's 75.0%/23.0%. This convincingly demonstrates the claimed advantage of out-of-order generation with relative positions over absolute-position MDMs and left-to-right ARMs.
- **Principled training objective avoiding infeasible variance (Equation 2, Section 3):** Rather than marginalizing over all denoising trajectories (which has "extremely high variance" per Appendix D), ILM uses normalized token counts between visible positions as a target distribution — a clean, tractable approximation enabling practical training.
- **Effective variable-length generation via dedicated stopping classifier (Section 3, Table 1):** The binary stopping classifier avoids the Insertion Transformer's EOS-token problems; IT gets 35.2/22.1/17.5 on Star tasks vs. ILM's 100/100/99.1.
- **Flexible arbitrary-length infilling without specialized training (Table 3):** ILM outperforms MDM on all three infilling benchmarks and handles multi-segment infilling naturally — a capability impossible for MDMs when the fill length is unknown.
- **Systematic benchmark design isolating model capabilities (Sections 5.1.1, 5.2):** Three difficulty levels of star graphs and zebra puzzles are carefully chosen to isolate specific capabilities (out-of-order generation, variable-length handling, constraint satisfaction), making the evaluation more diagnostic than generic benchmarks.
- **Favorable quality-efficiency tradeoff over MDMs during inference (Figure 6):** ILM achieves substantially better NLL than MDM at comparable or faster inference times, with input growing from zero tokens while MDM must process the full maximum-length sequence from the start.

## Weaknesses

### Fatal
None.

### Major
- **Abstract overstates text generation results; LM1B gap is large.** The abstract claims ILMs "perform on par with ARMs and better than MDMs in unconditional text generation." Table 2 shows this holds for Stories (ARM 2.11 vs ILM 2.14, gap 0.03) but not for LM1B (ARM 3.94 vs ILM 4.67, gap 0.73). On LM1B, the ILM-to-ARM gap (0.73) is over 5× larger than the ILM-to-MDM gap (0.14). The introduction uses the more measured "competitive with ARMs" and the limitations section admits "slightly worse than ARMs," but the abstract's "on par" framing is misleading. The LM1B result shows ILM clustering closer to MDM than to ARM.
- **Missing comparison against improved MDM inference methods.** Section 4 explicitly discusses improved MDM sampling strategies — Gong et al. (2024) on greedy unmasking, Zheng et al. (2024) on top-k sampling, Campbell et al. (2024) on flow-based stochastic sampling — yet all MDM comparisons use only the vanilla tau-leaping sampler (Sahoo et al., 2024). Since one of the paper's claims is that ILM outperforms MDMs, omitting the best available MDM inference methods undermines the comparison. Even a single comparison against these improved samplers would substantially strengthen the evaluation.

### Minor
- **Systematic sequence-length undershooting is unexamined.** Table 2 reveals ILM generates sequences 42% shorter than data on Stories (119 vs 205) and 25% shorter on LM1B (21 vs 28). The paper notes that the Insertion Transformer "consistently undershoots or overshoots" (Section 5.1.1) but never examines whether ILM itself exhibits systematic undershooting. NLL comparisons between sequences of different average lengths are not directly comparable — shorter sequences may have lower NLL not because the model better models language but because it avoids generating harder, more variable portions of the distribution. An analysis of the stopping classifier's behavior or length-conditioned NLL would disentangle quality from length.
- **No variance/error bars reported.** Text generation results (Table 2, Figure 5) and zebra puzzle accuracy (Table 1) are reported without confidence intervals or multiple runs. Given the relatively small scale of experiments, variance across runs would be informative.
- **Prometheus LLM judge evaluation lacks reliability metrics.** Figure 5 presents Prometheus 2 7B judge scores without inter-rater agreement or confidence intervals. LLM-as-judge scores can be noisy, and some indication of reliability would strengthen the claims that ILM "consistently outperforms" MDM.

### Trivial
- The abstract says "empirical valuation" — likely should be "evaluation."

## Nice-to-Haves
- Analyze the biased objective's impact: when does the count-based approximation fail (e.g., when the same token appears multiple times between two positions and insertion order matters)?
- Report NLL stratified by generated sequence length to disentangle quality from length effects.
- Qualitative examples or human evaluation of infilled text quality beyond NLL.
- Compare against FIM-trained ARMs (Bavarian et al., 2022) for single-segment infilling.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Missing related works cannot be verified without external sources and were removed per hard rules.
- Formatting/typo nitpicks are parser artifacts, not author errors.
- The harsh critic's framing that "the LM1B gap undermines the paper's central claim" was weakened — the central claim is strongest for planning tasks, where ILM excels dramatically. The text generation claim is secondary.

## Novel Insights
The key insight from synthesizing the reviews is that the paper's strongest contribution — demonstrating that insertion-based generation with relative positions solves problems both ARMs and MDMs fundamentally cannot — is somewhat diluted by overclaiming on the text generation side. The star graph experiments are genuinely impressive (near-perfect accuracy where competitors collapse to 21-75%), and these alone would make a compelling paper. The text generation evaluation, while showing ILM is better than MDM, doesn't support the "on par with ARM" framing, and the unexamined length confound (42% shorter on Stories) weakens confidence in the NLL comparisons. The paper would be strengthened by honestly framing the text generation results as competitive with MDM rather than on par with ARM.

## Suggestions
- Soften the abstract's "on par with ARMs" claim to match the introduction's more accurate "competitive with ARMs" language, and explicitly discuss the LM1B gap.
- Add at least one comparison against improved MDM inference methods (e.g., greedy unmasking from Gong et al., 2024) on text generation tasks.
- Analyze the stopping classifier's behavior and report length-conditioned NLL or force ILM to generate sequences of target length to disentangle quality from length effects.

## Calibration Report

### All Retrieved Anchors

**Round 1 (Bracketing):**
| Paper | Avg Score | Round | Relevance |
|-------|-----------|-------|-----------|
| SaOxhcDCM3 (Self-Consuming Training Loop) | 3.20 | R1 | Low — different topic |
| n87wrNlcJu (Autoregressive KG Completion) | 3.00 | R1 | Low — different topic |
| NSBP7HzA5Z (Inductive Transformers) | 3.00 | R1 | Low — different topic |
| t15cWqydys (Inferring from Logits) | 3.00 | R1 | Low — decoding methods |
| 71mqtQdKB9 (SEDD - Score Entropy Discrete Diffusion) | 6.60 | R1 | Very high — discrete diffusion for language, competitive with GPT-2 |
| UbOzNf6hGq (FiLM - Fill-in Language Models) | 4.25 | R1 | Very high — fill-in language model, any-order generation |
| 1pTlvxIfuV (Reparameterized Discrete Diffusion) | 5.50 | R1 | High — discrete diffusion |
| WNvvwK0tut (Scaling up MDMs) | 6.50 | R1 | Very high — MDM scaling |
| tyEyYT267x (SAR Diffusion) | 8.00 | R1 | Very high — semi-autoregressive diffusion, SOTA |
| xoXn62FzD0 (SMC for LLMs) | 8.00 | R1 | Medium — constrained generation |
| DzGe40glxs (Interpreting Planning in RL) | 8.00 | R1 | Low — RL planning |
| SPS6HzVzyt (Context-Parametric Inversion) | 8.00 | R1 | Low — different topic |

**Round 2 (Narrowing):**
| Paper | Avg Score | Round | Relevance |
|-------|-----------|-------|-----------|
| YONCcPQJoC (Integrating Planning into Generation) | 4.75 | R2 | Medium — planning for generation |
| miGpIhquyB (LLMs Through Dataset Generation) | 5.50 | R2 | Low — different topic |
| Glcsog6zOe (Tree-Planner) | 5.25 | R2 | Medium — planning with LLMs |
| fZZ4ubttru (GenBot) | 5.50 | R2 | Low — robotic planning |
| 9QPH1YQCMn (Infilling Score) | 6.25 | R2 | Medium — infilling method |
| oXYZJXDdo7 (Retrieval is Accurate Generation) | 7.00 | R2 | Medium — novel generation paradigm |
| 71mqtQdKB9 (SEDD) | 6.60 | R2 | Very high — re-retrieved |
| uZ5K4HeNwd (Beyond Auto-Regression: SDTT) | 7.00 | R2 | High — non-AR language generation |

### Score Derivation
- **Round 1 bracket**: 5.5–6.5. ILM is clearly better than FiLM (4.25, rejected) but less mature than SAR diffusion (8.0, accepted with all 8s) or SDTT (7.0, accepted). Comparable to Scaling MDMs (6.5, accepted) and SEDD (6.6, rejected).
- **Round 2 narrowing**: ILM's planning experiments are more impressive than most anchors in this range. However, the overclaimed text generation results and unexamined length confound hold it back from 6.5. The paper is slightly below SEDD (6.6) due to weaker text generation evaluation, and well above the 4.75 and 5.5 reject papers. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>