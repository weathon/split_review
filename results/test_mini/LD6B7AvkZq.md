Now I will write the consolidated final review.

## Summary

This paper studies how language models learn context-free grammars (CFGs) through the lens of "subgrammar" structure. It proposes formal definitions of inner and outer subgrammars, claims a suite of theorems showing KL divergence decomposes recursively over subgrammar structure, and presents empirical results on parallel learning, curriculum learning, and generalization to deeper recursive structures. The conceptual framing — viewing CFG learning dynamics through subgrammar decomposition — is novel and interesting, but the execution has significant problems in both the mathematical exposition and the empirical methodology.

## Strengths

- **Novel conceptual framework of subgrammar structure for studying CFG learning dynamics.** The definitions of inner subgrammars (subtrees of derivations) and outer subgrammars (simplified grammar versions) in Definitions 3.3 and 3.5 provide a clear vocabulary for discussing how language models decompose the learning task. This framing is genuinely new relative to prior work on CFGs and neural networks (Cagnetta & Wyart, 2024; Allen-Zhu & Li, 2023), which studied static representations rather than learning dynamics with respect to grammar substructure.

- **Interesting empirical observation of concurrent subgrammar improvement.** Figure 1 shows that KL divergence decreases simultaneously for all subgrammars during training, suggesting the model does not master simpler subgrammars before progressing to more complex ones (unlike child language acquisition patterns). This observation is thought-provoking and opens a new empirical direction.

- **The controlled experiment isolating depth vs. length as the generalization bottleneck** (Section 6, Figure 3) cleanly demonstrates that prediction error grows with recursive depth (up to 0.173 at depth 200) but stays low (~0.017) when only context length increases. While the high-level conclusion is consistent with prior work (Bhattamishra et al., 2020; Lampinen, 2024), the controlled setup provides cleaner evidence than previously available.

- **Curriculum learning analysis with CKA alignment** provides suggestive evidence that subgrammar pretraining shapes internal representations, with attention-layer CKA increasing by up to +21.7% for pretrained models (Table 1). The robustness of subgrammar learning to syntactic position (prefix, suffix, infix) is a practical finding worth noting.

## Weaknesses

### Fatal

None.

### Major

- **Mathematical error in the main text's illustrative derivation (Equations 1–4).** The derivation claims to decompose KL divergence, but Equation (4) writes terms as ratios of log probabilities (e.g., $\frac{\log P_G(\alpha|\epsilon)}{\log Q_\theta(\alpha|\epsilon)}$) rather than as expectations of log-ratios (i.e., $P(\cdot)[\log P(\cdot) - \log Q(\cdot)]$). This is not how KL divergence decomposes, and the transition from Equations (2)–(3) to (4) is invalid. The paper describes this as an "abuse of notation," but the equation is mathematically incorrect regardless. Since Section 4 is described as "the most important contribution," this error in the core expository derivation undermines reader trust in the theoretical development. The formal theorems may be correctly proven in the appendix, but the main text's attempt to illustrate the decomposition is flawed.

- **Definition 4.2 uses undefined notation, making uninterpretable.** The definition reads:
  $$D_{\text{KL}}(P_G \parallel Q)_A = \sum_{s \in \Sigma^*} P(s | \epsilon) P_G(A | s) \sum_{a \in \Sigma^*} D_{\text{KL}}(P_G \parallel Q | \neg s)$$
  The symbols $P(s|\epsilon)$, $P_G(A|s)$, and especially $D_{\text{KL}}(P_G \parallel Q | \neg s)$ (with unexplained "¬s") are never defined in the paper. This definition is central to Theorem 4.3 and its corollaries, yet a reader cannot determine what it actually means. The informal explanation that follows ("can be seen as the 'restriction' of the KL-divergence to substrings from the subgrammar A") does not clarify the notation used in the formal definition.

- **Curriculum learning experiments lack a critical control for total training time.** Models pretrained on a subgrammar and then finetuned on the full grammar receive more total training steps than models trained from scratch. The claim that pretraining achieves lower final loss (Figure 6) could simply reflect additional optimization, not a genuine benefit of curriculum. The paper needs to compare pretraining+finetuning against training from scratch for the same *total* number of steps.

- **The "parallel learning" claim lacks statistical and methodological rigor.** (a) No variance over random seeds is reported. (b) No baselines are compared (e.g., do LSTMs or models trained on shuffled data also show concurrent subgrammar improvement?). (c) The paper does not specify exactly how subgrammar-specific KL is computed — it says "using a random (but likely) prefix," but does not clarify whether this marginalizes over contexts or conditions on a single prefix, making the quantitative KL values in Figures 1–2 difficult to interpret. (d) Corollary 4.7 reduces parallel learning to an "independence" condition that is essentially a restatement rather than an explanation; it does not establish *why* transformers exhibit this behavior.

### Minor

- **Corollary 4.5 assumes a strong "context insensitivity" condition** that the paper acknowledges but does not verify for trained models. The claim that experiments "suggest this condition is perhaps not so strong" is based on the observation that varying prefixes gave "qualitatively similar results," but this falls short of validating the condition for the formal decomposition. The corollary is a valid conditional statement, but its practical relevance is unclear without verification.

- **CKA analysis has limited statistical support.** The reported differences (e.g., +8.9% for attention, -0.2% for MLP in the 10-epoch pretraining case) are small, no statistical significance tests are reported, and higher CKA between models does not necessarily imply better representations — it could indicate convergence to a similar suboptimal solution.

- **The generalization experiments (Section 6) largely confirm well-known results.** The finding that models struggle with deep recursion has been established by prior work cited in the paper itself (Bhattamishra et al., 2020; Lampinen, 2024). The controlled depth-vs-length setup provides a cleaner demonstration but does not add fundamentally new insight.

### Trivial

- The description of Theorem 4.3 is sometimes referred to as "Theorem 4.2" in the text (line 167: "The full proof of Theorem 4.2 and Corollary 4.4" — should be Theorem 4.3), suggesting a minor labeling inconsistency.

## Nice-to-Haves

- A controlled curriculum learning baseline comparing equal total training steps.
- Variance estimates over random seeds for the parallel learning curves.
- A more precise operational definition of "parallel learning" with a quantitative test that distinguishes it from sequential learning.
- Comparison with other architectures (e.g., LSTMs) to assess whether parallel learning is architecture-dependent.

## Removed Points

- **Criticism that Section 4's theorems are "stated without proof."** The proofs are deferred to Appendix A, which exists in the original submission but was stripped by the parser. The paper explicitly states this. This is not a valid weakness.
- **Criticism that the decomposition theorems "reduce to trivialities" or "are close to a tautology."** While the chain rule for KL is elementary, the nontrivial contribution is in identifying the correct subgrammar structure over which the recursion operates and showing that the recursion holds. The formalization of subgrammar decomposition (Theorem 4.1) and the recursive structure are meaningful contributions. This criticism is overstated.
- **Criticism about "no evidence that trained models satisfy" the context-insensitivity condition.** The paper explicitly discusses this limitation and provides some empirical evidence (varying prefixes gave qualitatively similar results). The paper is transparent about the condition being strong.
- **Criticism that "Theorems would be straightforward if properly formalized."** This is speculative and ignores the work of formalizing the DAG decomposition of subgrammars.
- **Criticism about missing experiments (larger dataset, more models, statistical significance for parallel learning, etc.)** — these are moved to Nice-to-Haves as they are scope extensions, not fatal omissions.
- **Criticism about the GPT-5.1 results being presented as evidence.** The paper explicitly disclaims these as "purely anecdotal" and says they "should not be interpreted as direct evidence." The critic's concern is addressed by the paper's own caveat.
- **Strength Finder's more generic strengths** have been filtered into the Strengths section above; none were purely generic.
- **Formating/style nitpicks** from reviews are removed per hard rules.

## Novel Insights

The reviews collectively reveal a paper with genuinely interesting conceptual contributions — the subgrammar framework for studying CFG learning dynamics — that is undermined by execution problems in both its mathematical presentation and empirical methodology. The most striking finding, that models improve on all subgrammars concurrently rather than sequentially, is not adequately leveraged: the paper lacks a precise definition of what "parallel learning" means, does not test whether this result is architecture-dependent or driven by overparameterization, and provides a "theorem" (Corollary 4.7) that is essentially a tautological restatement. The depth-vs-length generalization experiment is clean but confirms known results. The paper would benefit most from either (a) fixing and rigorously establishing the theoretical decomposition as the primary contribution with clean proofs and clear notation, or (b) reframing as an empirical paper with rigorous controlled experiments, if the theoretical development remains incomplete.

## Suggestions

1. **Fix Equation (4) and Definition 4.2.** Replace the incorrect ratio-of-logs formulation with the correct expectation-of-differences form. Define all notation in Definition 4.2 explicitly before using it in theorem statements. The "¬s" notation must be explained or removed.
2. **Add the critical total-training-time control** for the curriculum learning experiments. Compare pretraining+finetuning against from-scratch training for the same total number of gradient steps.
3. **Clarify exactly how subgrammar-specific KL is estimated.** What prefixes are used? Is there marginalization over contexts or conditioning on a single prefix? This is essential for reproducibility.
4. **Report variance over random seeds** for the parallel learning curves (Figures 1–2) and compute a quantitative measure of parallelism (e.g., correlation of learning rates, time-to-threshold comparisons).
5. **Either verify the context-insensitivity condition empirically** or present Corollary 4.5 as purely a conceptual simplification, with the understanding that the more general (non-context-insensitive) decomposition is the actual result of practical relevance.

## Score and Decision

**Calibration anchors used:**
- `/home/wg25r/review_agent/human_reviews_2026/ACn1hhGcV4.md` — avg score 5.50, Reject. Similar topic (CFGs + transformers), had unclear proofs but no mathematical errors in main text. The current paper has worse mathematical exposition.
- `/home/wg25r/review_agent/human_reviews_2026/IAFwK6NyrP.md` — avg score 6.40, Accept (Poster). Strong theoretical contribution with solid proof structure. Current paper's theory is less clean.
- `/home/wg25r/review_agent/human_reviews_2026/7Sph4KyeYO.md` — avg score 5.50, Accept (Poster). Novel method with clear practical validation. Current paper's empirical support is weaker.
- `/home/wg25r/review_agent/human_reviews_2026/gdZ6J5hZzF.md` — avg score 7.33, Accept (Oral). Comprehensive empirical and theoretical contribution. Current paper is far less polished.
- `/home/wg25r/review_agent/human_reviews_2026/UwsIZKOir0.md` — avg score 2.80, Reject. Poorly written, unverifiable claims. Current paper is substantially more readable and has verifiable components.
- `/home/wg25r/review_agent/human_reviews_2026/ularVAZFjX.md` — avg score 2.00, Reject. Fundamentally flawed premise. Not directly comparable.
- `/home/wg25r/review_agent/human_reviews_2026/o94xgM0sWJ.md` — avg score 5.00, Accept (Poster). Cross-entropy decomposition paper with cleaner theoretical development despite mixed reviews.

The paper sits below the accepted papers at the 5.0–5.5 level due to actual mathematical errors in the main text (Equation 4) and undefined critical notation (Definition 4.2), combined with methodological gaps in the empirical sections. It is clearly above the 2.0–3.0 level papers which had fundamental presentation or premise issues. A score of 4.0 reflects a paper with a promising conceptual framework and interesting observations, but whose execution — particularly in the theoretical exposition advertised as its "most important contribution" — is not yet publication-ready.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>