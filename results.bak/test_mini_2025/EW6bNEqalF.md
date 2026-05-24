Now I have a thorough understanding of the paper and calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper studies offline RL in episodic Regular Decision Processes (RDPs) and proposes two technical improvements over the prior ADACT-H/RegORL framework: (1) a **language metric** \(L_{\mathcal{X}}\) grounded in formal language theory, which replaces the \(L_\infty^p\) distance used in prior statistical tests for state-merging; and (2) a **Count-Min-Sketch (CMS)** based approach for memory-efficient probability estimation. The language metric is organized into a two-dimensional hierarchy \(\mathcal{X}_{i,j}\) that interpolates between \(L_\infty^p\) and total variation distance, yielding PAC sample complexity bounds that replace the horizon-length dependence \(H\) with \(\log|\mathcal{X}|\) (which can be \(\tilde{\mathcal{O}}(1)\) for small \(j\)). Theorem 1 exhibits RDPs where \(L_\infty^p\)-distinguishability decays exponentially in the corridor length while \(L_{\mathcal{X}_{2,1}}\)-distinguishability remains constant — an exponential theoretical gain. Experiments on five domains show the language-metric approach learns better policies than FlexFringe and is orders of magnitude faster and more memory-efficient than the CMS variant on longer horizons.

## Strengths

1. **Genuinely novel theoretical framework.** The language metric \(L_{\mathcal{X}}\) (Definition 2) and the two-dimensional hierarchy \(\mathcal{X}_{i,j}\) (Section 4.1) are original constructs that connect formal language theory to RL distinguishability. The fact that \(L_{\mathcal{X}}\) unifies \(L_\infty\), \(L_1\), \(L_\infty^p\), and \(L_1^p\) as special cases (by choosing different \(\mathcal{X}\)) gives the framework substantial generality.

2. **Provable exponential separation.** Theorem 1 is clean and compelling: it constructs a concrete family of RDPs (T-maze) where \(L_\infty^p\)-distinguishability is \(\mathcal{O}(2^{-N})\) but \(L_{\mathcal{X}_{2,1}}\)-distinguishability is \(\Omega(1)\). This directly demonstrates that the language metric can avoid the exponential sample-complexity blowup that plagues prior approaches.

3. **PAC bound with improved dependence structure.** Theorem 3 gives a bound \(\tilde{\mathcal{O}}(C_{\mathbf{R}}^*\log(1/\delta)\log|\mathcal{X}| / (d_m^*\mu_0^2))\) where \(\log|\mathcal{X}| = \tilde{\mathcal{O}}(1)\) for small constant \(j\), replacing the \(\tilde{\mathcal{O}}(H)\) term in the original RegORL bound's implicit dependence. The honest correction of a mistake in Cipollone et al. (2023) — adding a \(\sqrt{H}/\mu_0\) factor to both their bound and the new one — further strengthens credibility.

4. **Empirical validation of scaling behavior.** Figure 2 provides clear evidence that the language metric approach scales linearly (in log-scale) with corridor length \(N\), while the CMS/L∞p approach scales exponentially. The result is visually striking and corroborates the theory directly.

5. **Practical policy improvement on nontrivial domains.** Table 1 shows that ADACT-H with \(\mathcal{X}_{3,1}\) achieves significantly better rewards than FlexFringe on T-maze(c), Cheese, and Mini-hall, while also running faster and producing smaller automata than the CMS baseline. The domain suite (Corridor, T-maze(c), Cookie, Cheese, Mini-hall) spans varying horizon lengths and complexity levels.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Experimental reporting is incomplete for several domains.** Three domains in Table 1 (Corridor, T-maze(c), Cookie) report reward as a single number with no measure of variance, while Cheese and Mini-hall report mean ± standard error. The paper says rewards are "averaged over 100 episodes" but does not state whether this is across multiple independent learning runs or evaluation rollouts from a single run. Additionally, the dataset size and behavior policy for each domain are not specified in the main text. The Appendix presumably contains these, but in a camera-ready version they belong in the main body or at least a summary table.

2. **The CMS contribution is largely a negative or partial result in practice.** The CMS variant exceeds the 1800-second time budget on Mini-hall and shows exponential scaling in Figure 2. While the paper acknowledges this honestly, the practical utility of the CMS variant is unclear — it has worse running time and often worse automaton quality than the language metric approach, and its theoretical memory advantage kicks in only for regimes where the L∞p test is itself intractable (long horizons). The paper would benefit from identifying a concrete use case where CMS is the preferred choice.

3. **Language hierarchy only uses \(j=1\) in experiments, with limited discussion of when larger \(j\) is needed.** The hierarchy \(\mathcal{X}_{i,j}\) has size \(\mathcal{O}(|\mathcal{G}_i|^j)\), which grows exponentially in \(j\). The experiments fix \(j=1\) throughout. This is sensible for the chosen domains, but the paper does not discuss whether some RDPs would require \(j>1\) to achieve adequate distinguishability, or what the resulting computational cost would be. A brief discussion of this trade-off would strengthen the presentation.

4. **No direct comparison against the original ADACT-H/ADACT-H-A without CMS.** The CMS baseline uses the same \(L_\infty^p\) statistical test as the original ADACT-H but adds CMS for storage. While this makes the CMS baseline a reasonable proxy, a comparison against pure ADACT-H with exact counting (where feasible for small domains) would cleanly disentangle the effect of the language metric from the CMS data structure. This is not a fatal omission — the CMS vs language metric comparison is informative — but it would strengthen the empirical story.

### Trivial

1. The main text does not explicitly state how the policy is derived from the learned automaton for the reward numbers reported in Table 1. The paper mentions "Algorithm RegORL in Appendix A" which presumably covers this, but a sentence in Section 5 (e.g., "the learned RDP is solved as a finite MDP via value iteration to obtain the policy") would aid reproducibility for readers who do not consult the Appendix.

2. The CMS approach is listed as "–" for Mini-hall in Table 1, with a note in the caption that it exceeded the time budget. It would be cleaner to mark this explicitly in the table with a footnote symbol rather than relying on the body text to explain the dash.

## Nice-to-Haves

- A comparison against ADACT-H-A (Cipollone et al., 2023) on the small domains where exact counting is feasible would strengthen the claim that the language metric improves over the prior practical approach, not just FlexFringe.
- The experiments could vary the dataset size \(K\) to probe whether the language metric approach achieves its theoretical sample efficiency in practice.
- A discussion of how to choose the hierarchy parameters \(i\) and \(j\) in practice (e.g., a simple heuristic for when to increase \(j\)).

## Removed Points

These points were raised by reviewers but are removed or demoted after cross-checking:

- **"Missing comparison against RegORL is fatal"** — Demoted to Minor (point 4 above). The CMS baseline uses the same \(L_\infty^p\) test as the original ADACT-H; a comparison exists through the CMS column in Table 1. The absence of an exact-counting baseline is a gap, not a fatal flaw.
- **"Policy derivation not described at all"** — Removed. The paper references "Algorithm RegORL in Appendix A" which contains the full offline RL pipeline including policy derivation. The parser strips appendices, so this is present in the original submission. A brief clarification in the main text would be nice (added as Trivial point 1), but the criticism as stated is addressed by the Appendix reference.
- **"Analysis section — improvement may be less than naive reading suggests"** — Removed. The paper is transparent about the mistake correction and explicitly states that \(\sqrt{H}/\mu_0\) appears in both the old and new bounds. This is intellectual honesty, not a weakness.
- **"FlexFringe is not an RL algorithm"** — Addressed by the paper's own disclaimer ("The RDPs output by FlexFringe are not always directly comparable…") and subsumed under the baseline comparison points above.

## Novel Insights

The harsh critic's most useful observation is that the paper's overall evaluation would benefit from a clearer separation of the two contributions: the CMS approach is primarily a theoretical/memory contribution whose practical value is limited by its exponential runtime, while the language metric approach is the practically viable one. This diagnosis is correct — the paper presents both as "two techniques" but the reader comes away with the impression that only one is practically useful. An alternative framing that acknowledges the CMS result as an informative negative finding (confirming that the L∞p test itself is the bottleneck, not the counting data structure) would make the paper's narrative sharper.

## Suggestions

1. In Section 5, briefly state the dataset size \(K\) and behavior policy for each domain, and clarify for all domains whether rewards are averaged over multiple independent runs (with standard error) or a single run (with zero variance due to ceiling effects).
2. Add a sentence in Section 5 explaining how the policy is derived from the learned automaton for the reward computation (e.g., "the optimal regular policy for the learned RDP is obtained by value iteration on the induced finite MDP").
3. Discuss the \(j>1\) regime more explicitly: when might larger \(j\) be required, what is the computational cost, and could it still be worthwhile relative to the exponential cost of L∞p?
4. Add a brief remark acknowledging that the CMS contribution is primarily a memory-efficiency result that does not scale in runtime, and identify a specific niche where CMS would be preferred over the language metric (e.g., very small horizons with enormous state-action spaces where memory—not time—is the bottleneck).
5. Mark the Mini-hall timeout entry in Table 1 with a footnote symbol and explain it in the caption.

## Score and Decision

### Anchoring

**Round 1 — Bracketing.** Three bands on "offline RL in regular decision processes / automaton learning / sample efficiency":
- Low band (avg < 3.5): Weak papers scoring 2.0–3.2. The current paper is clearly stronger — it has a genuine theoretical contribution, complete theorems, and nontrivial experiments.
- Middle band (avg 3.5–7.5): Papers scoring 4.0–6.5. Includes the POMDP paper "Sample-Efficient Learning of POMDPs with Multiple Observations In Hindsight" (avg 6.0, accepted poster), a game-theory paper (avg 5.75, rejected), and an MDP optimal sample complexity paper (avg 6.5, accepted poster). The current paper sits in this band.
- High band (avg > 7.5): Papers scoring 8.0. These resolve major open problems or introduce fundamentally new algorithmic paradigms. The current paper does not reach this level.

**Initial bracket:** 5.0–6.5.

**Round 2 — Narrowing.** Focused search on the 4.5–6.5 and 5.5–7.5 ranges:
- The POMDP-at-hindsight paper (avg 6.0, accepted poster): comparable theoretical depth; the current paper has stronger novelty (language metric is more original than extending existing OMLE-style subclasses) and includes experiments, but has weaker experimental reporting.
- The MDP sample complexity paper (avg 6.5, accepted poster): closes a known gap with clean analysis; the current paper has more novel concepts but less crisply definitive results.
- The game-theory paper (avg 5.75, rejected): strong theoretical contribution but strong assumptions and no experiments; the current paper has broader validation and more practical relevance.

The current paper is stronger than the rejected game-theory paper (5.75) and on par with or slightly better than the accepted POMDP paper (6.0). It has genuine theoretical novelty and reasonable experiments, but the experimental gaps prevent it from reaching the 6.5 level.

**Final score:** **6.0** — marginally above the acceptance threshold. The paper makes a genuine theoretical contribution with the language metric hierarchy, provides clean separation results (Theorem 1), and supports the theory with reasonable experiments. The weaknesses are in experimental reporting detail and the somewhat awkward dual-contribution framing, but none undermine the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>