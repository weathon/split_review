Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper initiates the study of how language modeling interacts with the subgrammar structure of context-free grammars. It defines inner and outer subgrammars, proves recurrence theorems decomposing KL divergence over subgrammar hierarchies, and provides empirical observations of parallel subgrammar learning, curriculum effects from subgrammar pretraining, and depth-vs-length generalization difficulties in small transformers trained on PCFGs.

## Strengths

- **Novel subgrammar formalism (Definitions 3.3, 3.5)**: The distinction between inner subgrammars (subtrees of CFG derivations) and outer subgrammars (simplified versions of the language) provides a clean conceptual framework for analyzing how CFG structure interacts with learning. Theorem 4.1 (unique decomposition into a DAG of subgrammars) connects this to classical CFG theory and provides a foundation for the subsequent analysis.

- **Core theoretical insight — KL recurrence over subgrammars (Theorem 4.3, Corollary 4.4)**: The idea that the KL divergence between a language model and a PCFG distribution can be expressed as a sum of restricted divergences over subgrammars is genuinely interesting and potentially impactful. Theorem 4.6, relating divergence blow-up to expected recursion approaching 1, is a clean observation.

- **Empirical observation of parallel subgrammar learning (Figures 1, 2)**: The finding that all subgrammar losses decrease simultaneously during training (rather than the model mastering simpler subgrammars first) is a genuinely non-obvious empirical observation. Figures 1 and 2 show this clearly across multiple grammars.

- **Depth vs. length generalization experiments (Figure 3)**: The controlled experiment cleanly separates depth-of-recursion from sequence-length effects, showing near-perfect performance on long flat contexts but degrading performance on deep recursive contexts — a useful quantification of a known limitation.

## Weaknesses

### Fatal
None.

### Major

- **Mathematically problematic derivation in Section 4.2 (equations 1–4)**. Equation (4) — `(log P_G(α|ε))/(log Q_θ(α|ε)) + ...` — presents ratios of log-probabilities as if they are valid KL divergence terms. This is not a correct manipulation; the sum of log-differences from a standard KL expansion cannot be rearranged into fractions of logs. The prose explanation ("a sum of conditioned KL-divergences") is conceptually correct, but the equation as written is mathematically incoherent and undermines confidence in the theoretical exposition. Definition 4.2 uses the notation `D_KL(P_G || Q | ¬s)` with an undefined negated-context symbol, further clouding the formalism.

- **The central empirical claim — that total KL equals the sum of subgrammar KLs — is not directly validated.** Figure 1 plots separate curves for each subgrammar's KL divergence but does not overlay the sum of these curves against a measured total KL. No quantitative comparison (relative error, R², RMSE) is reported. The caption states "scaling the divergences by their probabilities give a perfect decomposition" but this is asserted without evidence. Given that the key theoretical claim is a *decomposition* (not just that all curves go down), its validation requires checking whether the sum actually matches the total — which the paper does not do.

- **The "context-insensitivity" assumption of Corollary 4.5 is not tested.** This assumption — that the model's predictions for a subgrammar are identical under any valid context — is described as "strong" but the paper only offers hand-waving ("our experiments suggest...qualitatively similar results"). A straightforward experiment measuring subgrammar KL divergences under varying prefixes and reporting variance would be needed to justify this key simplifying assumption. Without it, the elegant simplification from Theorem 4.3 to Corollary 4.5 remains a mathematical curiosity rather than an empirically supported result.

### Minor

- **The "parallel learning" claim (Section 4.2, Corollary 4.7) lacks mechanistic evidence.** The paper observes that all subgrammar losses decrease simultaneously and presents a sufficient condition for parallel learning (gradient independence). However, the evidence does not rule out the trivial explanation that all losses decrease because the model learns shared features. No gradient interference analysis is performed, and the sufficient condition is not tested. The paper is appropriately cautious about this being an open direction, but the claim that the model learns subgrammars "in parallel" is too strong given the evidence.

- **CKA alignment results (Table 1) are modest and partially inconsistent.** Attention-layer CKA increases of +8.9% to +21.7% with pretraining are meaningful, but MLP layers show *negative* changes in some configurations (e.g., -4.7%, -2.6%). The paper claims pretraining leads to "very different internal representations" but the evidence is mixed: changes are small, inconsistent across layer types, and the absolute CKA values are low (0.249–0.561 on a 0–1 scale), suggesting low similarity overall.

- **Generalization experiments (Section 6) confirm known limitations** (as the paper acknowledges by citing Bhattamishra et al. 2020 and Lampinen 2024). The quantification of depth vs. length is the modest contribution here, and the GPT-5.1 anecdote is explicitly labeled as not rigorous evidence. This section adds breadth but not depth to the paper's contributions.

- **Theorem 4.1's novelty is overstated.** The paper acknowledges that the DAG decomposition corresponds to Gruska's (1971) "grammatical levels." The exact formulation may be new, but the claim of a "unique decomposition" of CFGs into subgrammars has significant precedent in formal language theory.

### Trivial
None.

## Nice-to-Haves

- Direct quantitative validation of the KL decomposition (overlay sum of subgrammar KLs against total KL, report relative error or R²).
- Test of the context-insensitivity assumption by measuring subgrammar KLs under varying prefixes with reported variance.
- Gradient cosine-similarity analysis to probe whether the gradient-independence condition for parallel learning holds.

## Removed Points

These points from the inputs were removed with justification:

1. **Harsh critic's claim that curriculum learning claims are unsubstantiated (referencing missing Figure 6).** The paper references Figure 6 (in the appendix) for lower final loss curves. The parser strips appendix content; this does not constitute a weakness in the paper as submitted.

2. **Harsh critic's claim about the GPT-5.1 anecdote being "not a controlled experiment."** The paper explicitly states (line 314): "These arithmetic tests are purely anecdotal and should not be interpreted as direct evidence." The critic's point merely restates what the paper already acknowledges.

3. **Harsh critic's claim that the "overall KL equals weighted sum" lacks confidence intervals.** Reporting per-point confidence intervals on KL decomposition curves is not standard practice for this type of experiment, and its absence does not invalidate the qualitative observation.

4. **Strength Finder's claim that Figure 1 shows total KL "precisely" equals the sum of subgrammar KLs.** This overstates what the figure actually shows — separate decreasing curves without an overlaid sum vs. total comparison. The claim was removed for inaccuracy.

5. **Harsh critic's claim about "missing" error bars in Figure 2.** Error bars on training curves of small transformers trained on controlled PCFGs are not standard. The paper shows main trends, which is appropriate for the exploratory analysis presented.

## Novel Insights

The most interesting observation that emerges from considering both the strengths and weaknesses is the tension between the paper's formal elegance and its empirical gaps. The subgrammar decomposition is conceptually appealing — if validated, it would give a principled way to "factor" language model loss into interpretable components corresponding to grammar substructures. However, the paper repeatedly steps back from rigorous validation: the core equation (4) is garbled, the decomposition is never quantitatively verified, and the key simplifying assumption is untested. This suggests the idea is promising but the paper was rushed to publication before the empirical foundations were properly laid. A revised version that fixes the mathematical presentation, directly validates the decomposition, and tests the context-insensitivity assumption could be substantially stronger.

## Suggestions

1. **Fix equation (4) and Definition 4.2.** Replace the ratio-of-logs expression with a proper decomposition into sums of weighted log-differences (or conditioned KL terms). Clarify the notation in Definition 4.2, removing undefined symbols like `¬s`.
2. **Directly validate the KL decomposition.** Compute the sum of subgrammar KLs and overlay it against the measured total KL for at least one grammar and seed. Report relative error across training. This is the single experiment most needed to support the paper's central claim.
3. **Test the context-insensitivity assumption** by computing subgrammar KL divergences under multiple distinct prefixes and reporting variance.
4. **Tone down overclaimed statements.** "Definitively" (abstract), "perfect decomposition" (Figure 1 caption), and "fundamental theorems" are stronger than what the evidence supports.
5. **Consider removing the GPT-5.1 anecdote** or making its illustrative intent clearer upfront. As is, it invites criticism without adding substance.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/STUGfUz8ob.md` | 7.60 (Accept) | Much stronger: rigorous proofs, clear experiments, practical architectural insights. This paper is less rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0pLCDJVVRD.md` | 7.00 (Accept) | Stronger: cleaner writing, clearer experiments on a related topic (formal languages + transformers), better-supported claims. This paper is less polished. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F0Zd3knG9j.md` | 5.00 (Reject) | Comparable: both study transformers on PCFGs with interesting but incompletely validated claims. That paper is cleaner; this paper has a more novel conceptual framework. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MO5PiKHELW.md` | 5.50 (Accept) | Slightly stronger: more rigorous experiments on syntax acquisition dynamics, though with split reviews. This paper has a more novel formalism. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hFQZmKFtlT.md` | 3.50 (Reject) | Weaker: re-framed known observations, tiny datasets. This paper has more substantive contributions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NSBP7HzA5Z.md` | 3.00 (Reject) | Weaker: poorly explained, toy experiments only. This paper is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aWLQTbfFgV.md` | 6.25 (Accept) | Stronger: addresses a clear methodological gap with clean experiments. This paper has a more conceptual contribution but worse execution. |

The paper sits between the weaker accepted papers (~5.5) and the rejected papers (~3.5–5.0). It has a genuinely novel conceptual contribution (subgrammar decomposition) that sets it above papers with only toy experiments or re-framed observations. However, the mathematical presentation is sloppy (equation 4 is wrong as written, Definition 4.2 is unclear), the central empirical claim lacks direct quantitative validation, and a key assumption remains untested. These issues are fixable but currently undermine confidence in the paper's core results. The paper is not fatally flawed — the core idea has merit — but it does not meet the bar for acceptance in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>