- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces DITTO (Demonstration ITerated Task Optimization), a method for aligning LLMs to a user's individual style using fewer than 10 demonstrations. DITTO constructs online preference comparison data by treating user demonstrations as preferred over both current and past model outputs, then applies DPO updates using a ranking over policies. The method is grounded in an online imitation learning perspective. Evaluated on static author-attribution benchmarks (20 authors across two datasets) and a user study (N=16), DITTO consistently outperforms few-shot prompting, SFT, and self-play methods (SPIN). The paper provides ablations isolating key design choices and a sample-efficiency analysis.

## Strengths

1. **Clean, well-motivated method with clear algorithm.** DITTO's core idea — that a handful of demonstrations can be expanded into a rich online preference dataset via the ranking $\mathcal{D}_E \succeq \mathcal{D}_t \succeq \mathcal{D}_{t-1} \succeq \ldots \succeq \mathcal{D}_0$ (Eq. 2) — is intuitive and clearly described in §3.2 with Algorithm 1. The practical mixture of 70% online / 20% replay / 10% inter-policy comparisons is explicit and reproducible.

2. **Strong empirical results across static benchmarks and a user study.** Table 1 shows DITTO achieves an average 77.09% win-rate across 20 authors, outperforming SFT (+11.7 pp), SPIN (+9.3 pp), and few-shot GPT-4 (+27 pp). These results are corroborated by a user study (Table 2, N=16, 320 pairwise preferences) where DITTO (68.8%) significantly outperforms self-prompt (46.9%), few-shot (51.6%), and SFT (55.5%), with statistical significance (ANOVA + Tukey, p < 0.05).

3. **Informative ablation isolating critical design choices.** Section 5.1 demonstrates that freezing the reference policy (win-rate drops from 70.1% to 45.8% when updated), replay comparisons (-6.5 pp), and inter-policy comparisons (-2 pp) are all essential to DITTO's performance. This cleanly distinguishes DITTO from methods like SPIN and validates the algorithm's components.

4. **Grounded theoretical connection to online imitation learning.** §3.3 derives DITTO by connecting DPO-style preference optimization with online data generation, establishing that DITTO implicitly learns a reward function through the closed-form relationship between policies and rewards (Eq. 4). Lemma 3.1 provides a conditional extrapolation guarantee that SFT cannot match.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear preference-labeling mechanism in the pairwise-comparison experiment (§5.3).** The paper claims that "using demonstrations with DITTO is an order of magnitude more sample-efficient for individuals than soliciting pairwise preferences" (Fig. 3). However, the paper never states how the preference pairs used to train DPO were labeled. The text says "constructed a pairwise preferences dataset $D_{pref} = \{(x, y^i, \bar{y}^j)\}$, where $y_i \succ y_j$" and "pairwise prefs sampled from (1) base instruction-following LM $\pi_{\text{ref}}$ and (2) $\pi_{\text{ref}}$ fine-tuned on demos" — but *who or what determined which of two samples was preferred*? The mechanism could be human annotation (unreported cost), automatic comparison to a reference text (oracle), or GPT-4 evaluation. Each interpretation changes what the experiment measures, and none is verifiable from the paper. Since the paper's headline claim about user sample efficiency depends on this experiment, the ambiguity is a serious gap. The rest of the paper's contributions do not depend on this experiment, but it should be clarified or reframed.

### Minor

1. **SPIN baseline comparison is of limited informativeness.** The paper acknowledges that "design decisions for SPIN (e.g., updating the reference policy, excluding inter-policy/replay comparisons) are targeted towards SFT-scale datasets" and runs it anyway. The reported 9.3 pp gap partially reflects a mismatch in data regime rather than an algorithmic comparison. While the ablations in §5.1 partially address this by testing individual components, a direct comparison to an adapted version of SPIN (with the reference policy frozen and iterative sampling controlled) would be cleaner. The current framing inflates the apparent advantage.

2. **User study sample is narrow.** The study recruits 16 participants from social media, "many of whom were Ph.D. students familiar with prompting LLMs" (§4.2). This sample is appropriate for a new-method paper, but the self-prompt baseline's strength (which it notes as a "strong baseline") and the generalizability of results to non-expert users are limited by this demographic.

3. **GPT-4 evaluation bias is acknowledged but its interaction with specific comparisons could be discussed further.** The paper notes GPT-4's self-enhancement bias (§4.2) and addresses it with a user study. However, the Fightin' Words analysis (§4.2) shows DITTO systematically avoids GPT-4-like cliché phrasing, which would *penalize* DITTO in the GPT-4 judge. This means the static-benchmark results are likely conservative for DITTO. The paper mentions this briefly but does not explore the implications — e.g., the true gap may be larger than reported.

### Trivial
None.

## Nice-to-Haves

- The Fightin' Words lexical analysis (§4.2) is applied only to the user study (emails). Applying it to the static benchmarks (news articles, blog posts) would strengthen the claim that DITTO reduces GPT-4-like clichés across domains.
- A baseline where a prompt is manually engineered to include demonstrations (beyond the self-prompt baseline, which did not necessarily incorporate demonstrations) could further isolate the source of DITTO's advantage.
- The sample-efficiency experiment (§5.2, Fig. 2) shows diminishing returns from 4+ demonstrations; clarifying whether the curve aggregates across authors or shows individual trajectories would aid interpretation.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Missing training hyperparameters (epochs, learning rate, LoRA rank).** Removed per instructions: hyperparameter details that would appear in an appendix (which the parser strips) are not author omissions.

2. **"Theoretical guarantee" over-claimed as a core strength.** Lemma 3.1 is a conditional statement with conditions that are hard to verify in practice. While it provides useful context, it is not central to the paper's empirical contribution. Removed from Strengths as it does not meet the bar for a core strength.

3. **"Order-of-magnitude sample efficiency" listed as a strength.** The experiment supporting this claim (§5.3) suffers from the ambiguity discussed in Major weakness 1. Until the labeling mechanism is clarified, this cannot be treated as a confirmed strength.

## Novel Insights

The harsh critic correctly observes that the GPT-4 self-enhancement bias *harms* DITTO in the static benchmarks (because DITTO's outputs specifically avoid GPT-4 cliché phrasing, as shown by the Fightin' Words analysis), making the results conservative. This reverses the typical concern about LLM-as-judge evaluations and is worth highlighting. The two reviews together also expose a subtle gap: the paper claims demonstrations are more efficient than pairwise preferences for *users*, but the experimental design (§5.3) may actually be comparing two forms of *automatic* data generation rather than measuring user effort. Bridging this gap would require at minimum a clear statement of the labeling protocol.

## Suggestions

1. **Clarify §5.3.** Explicitly state how the preference pairs were labeled (human, GPT-4, or automatic oracle). If the labels came from an automatic oracle (e.g., comparing outputs to the reference text), reframe the experiment as a comparison of two automatic data-generation strategies rather than as evidence about user effort. This does not damage the paper's core contribution but makes the evidence honest.
2. **Add a paragraph discussing the GPT-4 self-enhancement bias in the context of the Fightin' Words findings.** The observation that DITTO systematically avoids GPT-4-like language — which would penalize it under GPT-4 evaluation — strengthens the static-benchmark results. Making this argument explicitly would turn a limitation into a feature.
3. **Consider including an adapted SPIN baseline** (with reference policy frozen, matching iteration count) alongside the original to quantify how much of the gap is due to DITTO's specific design versus the general advantage of not updating $\pi_{\text{ref}}$ in the few-shot regime.
