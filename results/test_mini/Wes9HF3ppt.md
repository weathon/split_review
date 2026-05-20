Now I have all the information I need. Let me synthesize the final review.

**Round 1 bracket:** After the first calibration pass, the plausible range is 4.0–6.8 (between Elastic-MDM at 4.00 which was rejected, and DID at 6.80 which was accepted).

**Round 2 narrowing:** Examining anchors at 5.0, 5.5, 6.0, 6.5, and 6.8 within this bracket places the paper closest to the 6.0–6.5 range. The paper is stronger than the MTP planning paper (5.00, rejected) and comparable to PAPL (5.50, accepted as Oral), but has less theoretical depth than FlexMDM (6.50) and DID (6.80). Its strongest advantage — the planning experiments on star graphs and zebra puzzles — is unique among the anchors.

**Final score: 6.0.** The paper has a clear novel contribution with convincing planning results, but the text evaluation has a meaningful confound and the training objective lacks theoretical grounding that comparable papers provide.

---

## Summary

The paper introduces Insertion Language Models (ILMs), which generate sequences by inserting tokens one at a time at arbitrary positions, jointly predicting both the insertion location and the token. To enable efficient training, the authors propose a biased denoising objective (avoiding high-variance Monte Carlo estimates) and a simple transformer parameterization with a single output head for insertion logits plus a learned stopping classifier. The method is evaluated on synthetic planning tasks (star graphs, zebra puzzles) and on medium-sized text generation/infilling (LM1B, TinyStories/ROC-Stories).

## Strengths

- **Strong and clean planning results that convincingly demonstrate the method's advantage.** On Star_hard (variable-length graph arms), ILM achieves 99.1% exact-match accuracy while MDM (21.0%) and ARM (23.0%) both fail (Table 1). On zebra puzzles, ILM reaches 90.0% vs. 82.6% for MDM and 81.2% for ARM. These results directly validate the claim that out-of-order generation with relative positions solves tasks that are fundamentally hard for fixed-order ARMs and fixed-mask MDMs. The experiment design — progressing from Star_easy to Star_hard — systematically isolates the failure modes.

- **Simple and practical parameterization.** The method uses a standard RoPE-based transformer encoder with a single additional head computing insertion logits (Equation 3), plus a learned stopping token. This is architecturally clean and does not require specialized attention mechanisms, dynamic programming (cf. DID), or two-model designs.

- **Addresses a genuine limitation of MDMs for variable-length infilling.** The infilling experiments (Table 3) show ILM consistently outperforms MDM on ΔNLL_gt across all settings, and ILM natively handles multi-segment infilling (which MDMs cannot do without fixed masks). This validates a core motivation of the paper.

- **Honest discussion of limitations.** Section 6 explicitly acknowledges that ILMs are slower than ARMs with KV caching, that text performance slightly trails ARMs, and that data-dependent noising schedules are a promising future direction.

## Weaknesses

### Fatal
None.

### Major

- **Length confound in the unconditional text generation evaluation.** Table 2 shows that ILM generates sequences with mean length 119 on Stories (training data mean: 205) and mean length 21 on LM1B (training data mean: 28). ARM generates lengths much closer to the training distribution (201 and 30 respectively). The paper acknowledges MDM produces longer sequences but does not address the fact that ILM's outputs are systematically shorter. Per-token NLL under Llama 3.2 3B is sensitive to sequence length — shorter sequences are inherently easier to model — and the Prometheus judge evaluation does not control for length either. This confound means it is unclear whether ILM's apparently competitive NLL and Prometheus scores reflect better modeling or simply shorter outputs. The paper should either (a) provide a length-matched comparison (e.g., truncating all generations to a common length and re-evaluating) or (b) condition generation on target lengths. Without this, the unconditional text evaluation cannot be cleanly interpreted. This does not affect the planning results, which are independently strong.

### Minor

- **The biased training objective is introduced without analysis of the bias.** The paper acknowledges the objective is biased (Section 3, "To avoid this issue, we use a biased training objective…"), but provides no characterization of the bias — its magnitude, whether it is a lower bound, or under what conditions it approximates the true marginal likelihood. While the empirical results on synthetic tasks suggest the bias is benign in practice, this constitutes a methodological gap relative to comparable papers (e.g., DID at ICLR 2026 derives an ELBO-like objective; FlexMDM uses a stochastic interpolant framework). Even a small-scale comparison to an unbiased Monte Carlo estimator would substantially strengthen the paper.

- **Slight overclaim in the abstract.** The abstract states that ILMs "perform on par with ARMs" in unconditional text generation. From Table 2, ILM NLL is 2.14 vs. ARM 2.11 on Stories (marginally worse) and 4.67 vs. 3.94 on LM1B (clearly worse). The Prometheus judge (Figure 5) favors ILM on coherence/consistency, but the NLL comparison does not support "on par." A more precise phrasing (e.g., "competitive with ARMs on some metrics") would be more accurate.

- **Limited insertion-model baselines and related-work coverage.** The only insertion-model baseline is the Insertion Transformer (Stern et al., 2019), which the paper correctly implements and finds performs poorly. However, the discussion of prior insertion-based and order-agnostic work is thin. KERMIT (Chan et al., 2020), the Levenshtein Transformer (Gu et al., 2019), and InsNet (Lu et al., 2022) share conceptual overlap but are not discussed. While the paper's method is genuinely different (denoising-based rather than autoregressive with insertion heads), contextualizing against the full insertion-model family would help readers situate the contribution.

### Trivial
None.

## Nice-to-Haves

- **Quantitative inference cost comparison.** The paper notes that ILMs do not support KV caching (Section 6), but reports no FLOPs or wall-clock time comparison. Given that inference-time efficiency is a practical concern, reporting per-token or per-sequence cost relative to ARMs and MDMs would help readers assess the practical trade-off.

- **Qualitative analysis of text generation trajectories.** The planning experiments include example generation trajectories (Figure 7, appendix), but the text experiments do not. Showing how an ILM incrementally builds a sentence by inserting tokens at arbitrary positions would make the "flexible order" claim tangible.

## Removed Points

- *Entropy metric is unexplained (harsh critic):* The paper explicitly defines entropy in Equation 5 and discusses its interpretation in the context of diversity. The critic's complaint that it is "unexplained" is not accurate.
- *Missing comparison to a "modern Insertion Transformer" (harsh critic):* The claim that "a properly trained modern Insertion Transformer... would perform comparably to ILMs" is speculative; no specific architecture or training method is identified. The paper does implement and compare to the original Insertion Transformer.
- *Strength: "tailored parameterization enabling stable training" (strength finder):* While not incorrect, this is somewhat generic — any method's contribution includes making training feasible.
- *Various formatting/style nitpicks and speculative concerns.*

## Novel Insights

The harsh critic's observation about the length confound is the most insightful point that goes beyond what the paper itself discusses. The paper acknowledges the MDM length issue but does not apply the same scrutiny to ILM's shorter outputs. The intersection of this insight with the biased-training-objective issue — i.e., that the objective bias may systematically affect length modeling — is a genuinely nuanced observation not present in the paper or either review individually. A paper that combined the planning strength with a theoretically grounded objective and length-controlled text evaluation would be significantly stronger.

## Suggestions

1. **Address the length confound.** This is the most impactful fix. Generate text from all models conditioned on the same target length (e.g., via rejection sampling or length conditioning) and re-run the NLL and Prometheus evaluations. If ILM maintains its position, the text claims become much stronger. If not, report honestly as a limitation.

2. **Analyze the biased objective.** Add even a toy comparison (synthetic data with known ground-truth) between the biased objective and a Monte Carlo estimate of the true loss, showing the bias is small or bounded. Alternatively, derive the objective as a lower bound or consistent estimator under some condition.

3. **Tighten the claims in the abstract.** Replace "perform on par with ARMs" with a more precise characterization (e.g., "competitive with ARMs in LLM-judge evaluations, though slightly behind in NLL").

4. **Expand related work** to briefly discuss KERMIT, Levenshtein Transformer, and InsNet, clarifying the differences between those approaches and the proposed denoising-based ILM training.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| VbvXjs5f72 (DID) | 6.80 | R1 | More rigorous theory (score-based, DP); similar approach. Current paper weaker on theory but has better planning results. |
| ttuNnMRI6H (FlexMDM) | 6.50 | R1 | Stronger theoretical grounding; weaker planning results. Current paper comparable overall. |
| PKidr9Ruli (On Powerful Ways) | 6.00 | R1/R2 | Theoretical paper about generation paradigms. Current paper more empirical. Comparable. |
| lAlI5FuIf7 (PAPL) | 5.50 | R2 | Has theoretical contribution (P-ELBO) but narrower scope. Current paper has broader empirical contribution. Slightly stronger. |
| TS9BsfzjOJ (MTP Planning) | 5.00 | R2 | About improving planning in ARMs. Weaker empirical results. Current paper clearly stronger. |
| ekcXYg9nxL (Elastic-MDM) | 4.00 | R1 | Rejected due to weak experiments. Current paper significantly stronger. |
| mXMKm4pilN (VALM) | 1.50 | R1 | Withdrawn/rejected non-autoregressive model. Current paper much stronger. |

Round 1 bracket: 4.0–6.8. Round 2 narrowed to 5.5–6.5 by comparing against anchors at 5.00, 5.50, 6.00, 6.50. The paper is clearly stronger than Elastic-MDM (4.00) and the MTP planning paper (5.00); comparable to PAPL (5.50) and On Powerful Ways (6.00); slightly weaker than FlexMDM (6.50) and DID (6.80) due to weaker theoretical grounding and the length confound in text evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>