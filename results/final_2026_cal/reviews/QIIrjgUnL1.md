Now let me compile the final review with calibration results.

**Round-1 Bracket:** Based on calibration search, I placed the paper between 2.5 and 4.5.

**Round-2 Narrowing:** I read detailed anchors at 4.00 (PoPE), 4.00 (TAPA), 4.50 (Length Generalization), and 7.20 (Deconstructing Positional Information). The current paper is weaker than all 4.00+ anchors because of (a) the internal contradiction about ALiBi, (b) opaque experimental reporting, (c) trivial theoretical claims overpresented as major. It is stronger than the 2.50 anchors (Behind RoPE) because it proposes a concrete method with empirical results.

**Anchor List:**
- IAXBLI2vo5 (2.50, Behind RoPE): Analysis-only paper, withdrawn. Current paper has a concrete method so somewhat stronger.
- 60Vj3aBnjw (3.00, Position-Aware NTP): Comparable score. Similar level of method+experiments.
- thLQd7uK3C (0.50, IBiT): Much weaker paper. Current paper is stronger.
- rsEhpeY6HE (2.50, Spatial Bias): Withdrawn analysis paper.
- D0u0glT060 (7.20, Deconstructing PE): Strong accepted paper with deep theory. Current paper is much weaker.
- bppDDqbO3V (4.50, Length Generalization): Thorough analysis + proposed method, rejected for limited scope. Current paper is weaker.
- EQuoft7Yc7 (4.00, TSP with PE): Applies existing methods to new domain. Current paper similarly incremental but has framing issues.
- kf2mzS6xfk (4.00, PoPE): Modifies RoPE, clear motivation, tested at scale. Current paper is weaker.
- U1xQiqTnBp (4.00, TAPA): New positional encoding with proofs at 7B scale. Current paper is weaker.
- y6piOp5MSO (4.00, GeoPE): Extends RoPE to higher dims, mixed reviews. Current paper is comparable or slightly weaker.

Final score: **3.0**

Now I'll write the full review.## Summary

This paper proposes EPAR (Explicit Position-Attention Relationship), a framework that replaces traditional position encoding with an explicit parametric function \(P_{\text{effect}}(i,j,L)=\alpha e^{-\beta|i-j|/L}\) that multiplicatively modulates attention scores. It introduces an enhanced version with coefficient \(\gamma\) to prevent over-attenuation at long distances, and a triple-attention architecture with task-aware and content-aware modules. The paper reports consistent improvements across five NLP tasks (1.8%–8.9%) at 110M parameter scale.

## Strengths

- **Simple, closed-form position-attention modulation.** The core idea — multiplying attention logits by \(\alpha e^{-\beta|i-j|/L}\) — is clean and interpretable. Unlike learnable embeddings, the function's behavior is fully determined by two scalar parameters, which the paper analyzes for sensitivity and synergy (Section 4.4). This enables direct control over the locality vs. long-range tradeoff.

- **The \(\gamma\) enhancement addresses a real problem.** The enhanced function \(\alpha(1+\gamma e^{-\beta|x|/L})/(1+\gamma)\) (Eq. 3) guarantees a non-zero lower bound on attention at long distances. The paper quantifies this: 4.2× improvement at mid-range, 28.3× at maximum distance (Section 7.1). This is a principled fix for exponential over-attenuation.

- **Consistent positive results across diverse tasks.** Table 3 reports improvements over the best baseline on WikiText-103 (PPL 22.4 vs 23.5), WMT'14 (BLEU 30.1 vs 29.1), SQuAD 2.0 (F1 0.851 vs 0.831), GLUE (Acc 0.867 vs 0.852), and ArXiv (ROUGE-L 0.478 vs 0.439). The direction of improvement is consistent, and the paper provides confidence intervals and Cohen's \(d\) effect sizes.

- **Parameter sensitivity analysis.** Section 4.4 reports task-specific optimal \((\alpha, \beta)\) values and shows that performance is robust within \(\pm0.2\) of optimum. This is practically useful guidance.

## Weaknesses

### Major

- **Internal contradiction about ALiBi undermines the paper's central framing.** The paper repeatedly asserts that "existing position encoding methods (RoPE, ALiBi, relative position encoding) operate at the vector representation level" (lines 19, 136). Yet Table 2 (line 131) correctly classifies ALiBi as operating at the "Attention score" level with a linear bias \(A_{ij} = Q_i^T K_j + m\cdot|i-j|\). The paper's own table contradicts its core claim that all prior methods are "implicit" and "vector-level." This is not a minor phrasing issue — it is central to the claimed distinction from prior work. ALiBi is already an explicit, closed-form function of positional distance applied directly to attention logits, just additive rather than multiplicative. The paper never acknowledges this or explains why multiplicative vs. additive is a qualitatively different contribution. This mischaracterization would need to be corrected before the paper can be evaluated on its actual merits.

- **Table 3 reports only "Best Baseline" rather than per-baseline results.** The reader cannot see how the method compares against each individual baseline (Standard Attention, RoPE, ALiBi, Relative PE, Transformer-XL). The paper mentions "PPL 22.4 vs. 23.5 for ALiBi" in the text, but the table itself is opaque. Given that five baselines are listed in the setup (Section 6.1), a reader evaluating the method needs to see the full comparison, not just the best baseline. This is particularly important because the method's advantage may come from only a subset of baselines.

- **Key theoretical claims are either trivial or unverifiable in the main text.** The paper advertises "theoretical guarantees" (Section 4.2) including continuity, differentiability, and monotonicity. These are standard properties of the exponential function \(\alpha e^{-\beta|x|/L}\) — provable in one line of calculus — and do not constitute a substantive theoretical contribution. The more consequential theorems (Theorem 2 on optimal parameter selection, Theorems 3-5 on convergence) are referenced only to the appendix, which was stripped; the reader cannot assess their validity or significance. A paper that foregrounds theoretical rigor should at minimum state the theorem statements in the main text.

- **Mutual information numbers are stated without derivation or definition.** Section 5.1.1 reports \(I(P;A)=0.78\cdot H(P)\) for EPAR vs. 0.52 for RoPE and 0.61 for ALiBi. The paper does not define the distributions \(P\) and \(A\), describe how these quantities are computed, or cite a source for the other methods' values. These numbers are presented as evidence but are unverifiable from the information on the page.

### Minor

- **The triple-attention architecture fusion is ambiguously specified.** Equation (5) uses \(0.5\) weights for task and content modules, but the text says optimal fusion weights vary (0.4–0.7) and are task-dependent. Whether \(w_{\text{fuse}}\) is learned per-task or set heuristically is not entirely clear from the main text. An ablation showing the benefit of each component over simpler alternatives would strengthen the contribution; the paper claims the ablation exists in the appendix.

- **The "maximum benefit position formula" \(\text{pos}^* = \arg\max V(i)\) is described but not empirically validated in the main experiments.** The paper mentions it in Sections 4.3 and 7.3 and the conclusion, but the main Table 3 evaluates on standard NLP benchmarks, not on optimal placement. A targeted experiment validating that the formula predicts effective information placement would substantiate this claimed contribution.

- **Consistency metric and ranking correlation values (0.9063, 0.5932) are compared against values for RoPE (0.78) and ALiBi (0.45), but no description of how those baseline values were obtained.** Is EPAR used to compute these metrics for the other methods, or are the comparison numbers from the paper's own framework? This needs clarification.

### Trivial

- None beyond the presentation issues already noted.

## Nice-to-Haves

- Including per-baseline results in Table 3 would significantly strengthen the empirical contribution.
- The paper could be strengthened by comparing against the trivial baseline of replacing ALiBi's additive linear bias with the proposed exponential multiplicative bias, holding everything else fixed. This would isolate the effect of the functional form itself.

## Removed Points

The following points from the inputs were removed as per the filtering rules:

- **Harsh critic's claim about "no comparison against the obvious trivial baseline of replacing ALiBi's linear bias with an exponential bias"** — Kept as a Nice-to-Have but demoted because it is a suggested extension, not a flaw in the paper's actual claims.
- **Criticism about the paper saying ALiBi is "vector representation level"** — This is a valid criticism, kept as a Major weakness above. The contradiction is verifiable in the paper.
- **"Overhead of 4.5% inference cost is not trivial"** — Removed because the paper acknowledges this as a limitation in Section 9.1 and provides comparisons to Transformer-XL overhead. The criticism is subjective and the paper's addressal is reasonable.
- **"No experiment on the synthetic data patterns with existing methods"** — Removed because the paper reports consistency values "0.9063 for ours, 0.78 for RoPE" in Section 4.5. The comparison numbers are present, though their provenance could be clearer.
- **Strength Finder's claim that "unlike all major prior methods (RoPE, ALiBi, Relative PE, Transformer-XL) which operate at the vector-representation level"** — This is factually wrong for ALiBi per the paper's own Table 2. Removed.
- **Strength Finder's claim about "provable theoretical guarantees unavailable in existing methods"** — The claimed theorems are deferred to the appendix and the properties actually stated (continuity, differentiability, monotonicity) are trivial. Weakened to note in weaknesses.
- **Harsh critic's claim about missing standard attention perplexities (commonly ~30–33)** — Removed as speculative; the paper's configuration (110M params) may differ from the cited values.
- **Various formatting, appendix, and reproducibility nitpicks** — Removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The core weakness pattern — overclaiming theoretical contributions while mischaracterizing the closest prior work (ALiBi) — is common but not novel to observe.

## Suggestions

1. **Correct the ALiBi characterization.** Acknowledge that ALiBi operates at the attention score level (as Table 2 correctly states). Reframe the contribution as introducing an *exponential multiplicative* bias at the attention score level, and explain why multiplicative vs. additive matters theoretically and empirically. This single change would resolve the most damaging weakness.

2. **Report per-baseline results** in the main table, not just "Best Baseline." Show Standard Attention, RoPE, ALiBi, Relative PE, and Transformer-XL individually for every task so readers can see exactly where improvements come from.

3. **State theorem statements in the main text** or, if they are as trivial as the continuity/differentiability/monotonicity claims suggest, be honest about what the theoretical contribution actually is. A short lemma stating that \( \alpha e^{-\beta|x|/L} \) is continuous, differentiable, and monotone is fine — but do not package it as a major theoretical contribution.

4. **Define the mutual information computation.** Specify the distributions \(P\) and \(A\), how the mutual information is estimated, and how the comparison values for RoPE/ALiBi/Shaw are obtained. If these numbers come from a theoretical analysis rather than empirical measurement, state the closed-form derivation.

5. **Provide an ablation isolating the exponential bias from the additive bias.** Compare ALiBi vs. \(\alpha e^{-\beta|x|/L}\) (no \(\gamma\), no triple-attention) directly to show the empirical benefit of the multiplicative exponential form.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>