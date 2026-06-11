Now I have enough calibration data to finalize. Let me write the final review.

## Summary
This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that sits atop frozen LLMs and dynamically masks disallowed-language-family tokens during decoding to prevent language confusion. The gate is trained via norm-adjusted self-distillation: it learns to predict which language families are permissible at each generation step using the model's own norm-debiased top-k/p predictions as pseudo-labels. Evaluated across seven model variants (Qwen3, Llama3.1, Gemma3, GPT-OSS) in both thinking and no-think modes, LCG reduces CJ and Latin confusion by an order of magnitude while preserving task performance and legitimate code-switching, with only ~0.4% latency overhead.

## Strengths
- **Strong empirical grounding for the intervention strategy (Section 3.1):** At confusion points in Qwen3-8B, the confusion token is top-1 56.74% of the time, but language-consistent tokens appear in the top-3 99.29% of the time. This directly motivates why a logit-masking approach is well-suited — the model "knows" the correct language but under-ranks it.

- **Mechanistic discovery of token embedding norm imbalance (Section 3.2, Table 1):** The decomposition of logits into norm × cosine reveals that high-resource language tokens systematically dominate the high-norm group (e.g., in Qwen3-8B, 10.74% of CJ tokens vs. 0.14% of Low-Res tokens are in the top 5% of embedding norms). Figure 2 provides compelling qualitative evidence where norm adjustment eliminates CJ tokens from the top-10 at a real confusion point.

- **Substantial confusion reduction across diverse models (Tables 3, 4):** LCG-adjusted reduces CJ confusion by an order of magnitude or more (Qwen3-30B: 1.0% → 0.0%; Qwen3-8B: 4.5% → 0.1%) and cuts Latin confusion substantially (Qwen3-8B: 12.1% → 2.0%; Llama3.1-8B: 8.4% → 2.9%) across four no-think models. Results extend to thinking models on Humaneval-XL where CJ confusion drops while Pass@k scores are preserved.

- **Clever evaluation design (Section 5.2):** The FLORES-NO-LATIN / FLORES-WITH-LATIN split cleanly resolves the code-switching ambiguity for Latin confusion detection by using ground-truth references to determine when Latin characters are actually erroneous. This is a genuine methodological contribution.

- **Practical efficiency demonstrated (Section 6):** The gate adds only 0.4% latency overhead with a sparse intervention rate of 0.33–0.38% of tokens, establishing real-world deployability.

- **Comprehensive baseline comparison (Figure 3):** LCG substantially outperforms ICL, greedy decoding, and ORPO fine-tuning. ORPO degrades INCLUDE accuracy (61.4 → 57.3 on Qwen3-8B) while LCG preserves or improves task performance, highlighting the advantage of a no-retraining approach.

- **Norm-adjustment ablation validates the design (Table 3):** LCG-adjusted consistently outperforms LCG-unadjusted, with notable gains on Llama3.1-8B (Latin confusion: 5.7% → 2.9%) and Qwen3-8B (Latin confusion: 6.2% → 2.0%).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Pseudo-label quality validated on only one model (Section 3.1):** The 99.29% top-3 statistic — the empirical foundation for the entire self-distillation approach — is measured only on Qwen3-8B and only at confusion points. Table 1 shows that norm distributions vary substantially across models (e.g., GPT-OSS has 0% CJ tokens in the top-5% norm group), so the reliability of norm-adjusted pseudo-labels may differ across models. Reporting equivalent statistics for at least one additional model would strengthen confidence in generality.

- **Human evaluation for code-switching lacks methodological transparency (Section 5.3):** The 86.7% figure for code-switch preservation is reported with zero information about the number of annotators, annotation instructions, number of examples evaluated, or inter-annotator agreement. While the paper also provides the more robust Table 5 analysis that does not depend on human evaluation, the 86.7% claim as presented carries insufficient weight and should either be supported with standard annotation methodology or de-emphasized.

- **ORPO baseline lacks implementation detail (Section 5.3):** The ORPO comparison is the most interesting baseline but the least documented. The paper reports that it "prepares a multilingual dataset, and synthesizes samples with language confusion as rejected samples" but provides no dataset size, synthesis method, training hyperparameters, or base model checkpoint. This makes it impossible to assess whether the ORPO degradation represents a fair comparison or a poorly tuned baseline.

- **Evaluation languages are all script-disjoint from CJ/Latin (Section 5.2):** The evaluation targets (Arabic, Hebrew, Korean, Thai, Greek, Russian, Vietnamese) all use scripts visually distinct from CJ and Latin characters. The paper is honest about this limitation in Section 6, and within-script confusion is explicitly outside the method's design scope, but including at least one within-script target would probe the boundary of the method more informatively.

- **Norm-adjustment contribution is sometimes modest (Table 3):** While norm-adjustment consistently helps, the gains are small on some model/dataset combinations — on Gemma3-12B (FLORES-NO-LATIN), CJ% is 0.1 for both adjusted and unadjusted, and Latin% moves from 0.6 to 0.5. On Qwen3-8B (INCLUDE), accuracy drops slightly from 62.84 to 61.76. The paper's framing of norm-adjustment as a co-equal contribution alongside the gate itself and the datasets is somewhat stronger than these mixed-magnitude results warrant on certain metrics.

### Trivial
- Specific values of k and p used for pseudo-label construction in self-distillation are not stated in the main text (Section 4.2).
- The hidden dimension of the two-layer MLP is not reported in the main text, which matters for the "lightweight" claim.
- Latin confusion metrics are absent for thinking models in Table 4 (the paper only reports CJ confusion on Humaneval-XL).
- The precise numerical breakdown of the "No Rule" ablation is only in Figure 3, not in prose.

## Nice-to-Haves
- A breakdown of confusion rates by individual target language (Arabic vs. Thai vs. Korean, etc.) would reveal whether LCG works uniformly or has language-specific failure modes.
- Analysis of gate precision: what fraction of the 0.38% interventions are correct vs. unnecessary suppressions?
- Discussion of prior work on decoding-time interventions (contrastive decoding, classifier-free guidance) would contextualize LCG more thoroughly.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"The introduction claims 'language confusion is infrequent' without quantitative support"** — A presentation nitpick about the intro not previewing numbers that appear in Section 3.1. The numbers exist in the paper; their placement is not a substantive weakness.

- **"The claim about Large Reasoning Models is parenthetical and not developed"** — A style/preference point about the introduction's framing, not a substantive weakness.

- **"The BLEU scores in Table 2 are notably low — are these expected?"** — A request for commentary on expected BLEU ranges, not a weakness in the paper's methodology or claims.

- **"The causal direction of norm imbalance is not established (high-resource → larger norms)"** — The paper hedges appropriately: "Norm bias can account for a subset of such errors but cannot fully explain language confusion" (line 155). The correlation is shown; the paper does not claim a verified causal mechanism.

- **"Missing discussion of logit manipulation or decoding-time interventions"** — While a useful addition, the paper's related work (Section 2) covers the directly relevant language-confusion literature. This is a nice-to-have expansion rather than a gap.

## Novel Insights
The paper's decomposition of output token embedding norms by language family (Table 1) — showing that high-resource language tokens systematically have larger norms and dominate the high-norm tail — is a genuinely novel mechanistic observation. While the norm/cosine decomposition of logits is standard linear algebra, applying it to diagnose a specific, practically important failure mode (cross-script language confusion) and showing that norm adjustment alone can re-rank tokens at confusion points (Figure 2) provides a concrete, actionable insight that goes beyond prior work on language confusion.

## Suggestions
- Report the top-3 language-consistent-token statistic for at least one additional model beyond Qwen3-8B to validate the generality of the core intervention premise.
- Add basic human evaluation methodology details (number of annotators, examples, agreement) or de-emphasize the 86.7% figure in favor of the Table 5 analysis.
- Provide ORPO baseline implementation details (dataset size, synthesis method, hyperparameters) to make the comparison assessable.
- State the k, p values and MLP hidden dimension in the main text.
- Consider including one within-script evaluation target to probe the method's boundary.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| EMMA-500 | DPynq6bSHn | 4.33 | R1 | Weaker — major evaluation concerns, limited novelty |
| LatentQA / LIT | cselR6Jne3 | 5.25 | R1 | Weaker — unfair comparisons, unclear interpretability |
| Scaling Laws Multilingual | T2h2V7Rx7q | 5.25 | R2 | Weaker — theoretical, narrower contribution |
| Democratizing LLMs Low-Res | Nfu3bUkmdH | 5.67 | R2 | Weaker — prompting method, less extensive evaluation |
| When Is Multilinguality a Curse | i7oU4nfKEA | 6.25 | R1 | Comparable — solid empirical study, small models |
| VocADT | KxQRHOre9D | 6.25 | R2 | Comparable — lightweight frozen-model method for multilingual LLMs |
| Masked Diffusion Models | WNvvwK0tut | 6.50 | R2 | Stronger — more polished, scaling law contribution |
| LM Cascades | KgaBScZ4VI | 7.00 | R2 | Stronger — principled approach, clearer presentation |
| INCLUDE benchmark | k3gCieTXeY | 7.25 | R1 | Stronger — well-crafted benchmark with clear community value |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed:** The paper is comparable to VocADT (6.25) and "When Is Multilinguality a Curse" (6.25), but with a more practical method and broader model coverage. It sits below LM Cascades (7.00) due to several missing methodological details and narrower evaluation scope. The core contribution is sound and the evaluation is generally well-designed, but the accumulation of minor gaps (single-model pseudo-label validation, underspecified human eval, underspecified ORPO baseline, missing implementation details) prevents a score above 6.5.

**Final Score: 6.0.** The method is novel, practical, and well-motivated. Results are convincing across multiple models. However, several gaps in methodological transparency and evaluation scope need addressing. The paper is a solid contribution that should be accepted conditional on the authors filling these gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>