Now let me compile the final review. I've read the full paper and all the relevant calibration anchors.

## Summary

This paper trains Sparse Autoencoders (SAEs) on attention layer outputs (the concatenated **z** vectors before the output projection) across models up to 2B parameters. It shows these SAEs produce sparse, interpretable decompositions (L0 often < 20, >80% CE loss recovered, >80% features interpretable) and identifies three recurrent feature families: induction, local context, and high-level context. The paper then applies the SAEs to three investigations: a per-head polysemanticity analysis of GPT-2 Small's 144 heads, a case study distinguishing long-prefix vs. short-prefix induction heads (heads 5.1 and 5.5), and an analysis of the IOI circuit that causally identifies the "positional signal" as relating to whether the duplicate name appears after the "and" token — resolving an open question from Wang et al. (2023). Weight-based head attribution and Recursive Direct Feature Attribution (RDFA) are introduced as methodological contributions, and all SAE weights and an interactive visualization tool are released.

## Strengths

1. **Causal identification of the "and" positional signal in the IOI circuit, resolving a known open question.** Wang et al. (2023) explicitly left the nature of the "positional signal" as one of the "most interesting future directions." The paper localizes three causally relevant SAE features in layer 5 (via zero-ablation), interprets them as firing on duplicate tokens relative to "and", and validates this with a well-designed noising experiment: three simultaneous perturbations that preserve the duplicate's position relative to "and" recover ~93% of logit difference, while changing only "and" to "alongside" drops to ~43% (Figure 6). This is a concrete, causally validated discovery that goes beyond prior work.

2. **First systematic demonstration that SAEs on attention outputs yield sparse, interpretable features across multiple model families.** Table 1 reports metrics for GPT-2 Small (all 12 layers), Gemma-2B (layer 6), and GELU-2L (layer 1). The finding that SAEs on attention outputs achieve L0 as low as 3 (GPT-2 Small layer 0) with 99% CE loss recovered and 97% interpretability is a solid empirical demonstration that extends SAE methodology beyond MLP and residual stream activations.

3. **Novel finding distinguishing long-prefix from short-prefix induction heads, with clean validation.** Weight-based head attribution (Equation 4) motivated the hypothesis that head 5.1 specializes in long-prefix induction while 5.5 handles short-prefix. Synthetic data experiments (Figure 5a) show 5.1's induction score jumps from <0.3 to >0.7 as prefix length increases, while 5.5 starts at ~0.7 even for short prefixes. A targeted intervention (replacing the second prefix token) drops 5.1's score from 0.55 to 0.05 while 5.5 remains at 0.43 (Figure 5b). This is a well-validated case study that raises an interesting hypothesis about redundancy in induction heads.

4. **Open release of trained SAEs, feature dashboards, and an interactive RDFA visualization tool.** The paper makes it easy for the community to build on this work.

## Weaknesses

### Fatal
None.

### Major

1. **The "at least 90% of heads are polysemantic" claim is not supported with the precision it implies.** The paper finds 14 monosemantic candidates out of 144 heads by manually checking whether the top-10 SAE features per head are "closely related." This operationalization has several issues: (a) "closely related" is a subjective judgment with no quantitative measure; (b) only one head (10.2) is validated with an independent ablation-based confirmation; (c) the screening method's false-negative rate (how many monosemantic-seeming heads might actually be polysemantic under deeper scrutiny) and false-positive rate (how many seemingly polysemantic heads might be monosemantic at a different level of abstraction) are both uncharacterized. The paper acknowledges some limitations (§4.1.1, "we also note that there is a possibility we missed some monosemantic heads...") but still presents "about 90%" as a near-quantitative finding in the abstract and §4.1.1. This should be softened to something like "many heads appear polysemantic under this lens" and the precise figure either removed or heavily caveated with the limitations of the screening methodology.

2. **The induction-head specialization finding is a two-head case study in a single model, not a general explanation of redundancy.** The paper frames this as making progress on "why models have so many seemingly redundant induction heads" (§1, §4.2), but the evidence covers only heads 5.1 and 5.5 in GPT-2 Small. GPT-2 Small has at least 1–2 other induction heads across layers, and the paper does not examine those or test other models. The paper's own language is careful ("we focus on GPT-2 Small, which has two induction heads in layer 5"), but the framing around the broader open question creates an expectation the evidence cannot meet. This is a neat case study that raises an interesting hypothesis — it should be presented as such rather than as progress on the general redundancy question.

3. **RDFA is introduced as a named contribution (listed in §1 contributions) but is neither evaluated nor used in any experiment.** Section 2 describes RDFA at a conceptual level, a visualization tool is released, but no results, case studies, or validation experiments involving RDFA appear in the paper. For a claimed contribution that appears in the introduction's numbered list, the complete absence of evaluation or application is a significant gap.

### Minor

1. **No comparison to per-head SAEs.** The paper trains a single SAE on concatenated head outputs (to capture cross-head features), but never tests whether per-head SAEs perform worse or miss important features. This would be a natural control experiment to validate the design choice.

2. **Weight-based head attribution vs. DFA correlation not validated.** The paper introduces two attribution methods (weight-based and DFA) but never checks whether they agree. A simple correlation analysis on a sample of features would strengthen confidence in both methods.

3. **The "alongside" control in the IOI noising experiment tests only one alternative token.** Changing "and" to "alongside" shows a large effect, but "alongside" is a much rarer token, so the drop could partly reflect sensitivity to distributionally unusual tokens. Testing additional frequent conjunctions or prepositions (e.g., "with", "or", "but") would strengthen the conclusion that the effect is specifically about the "and" signal.

4. **Interpretability percentages in Table 1 are based on 30 random features per layer, with no confidence intervals reported in the main text.** For layer 11 (63% interpretable), with N=30 the 95% CI is approximately ±17%. The paper relegates confidence intervals to the appendix (which is stripped from the review copy, but acknowledged as existing), but the main text should at minimum mention the uncertainty.

### Trivial
None that survive filtering (parser artifacts).

## Nice-to-Haves
- The "and" signal analysis could be extended to check whether it appears in S-inhibition or Name-mover layers (through V-composition), which would strengthen the claim that this is the canonical positional signal.
- A comparison of the SAE-based analysis to simpler baselines (e.g., PCA or NMF on the same **z** vectors) would help demonstrate the specific value added by SAE sparsity.

## Removed Points
- *Criticism about the "redundant induction heads" framing being overgeneralized* — the paper's §4.2 is actually quite measured (it describes "a case study" and focuses on "two induction heads in layer 5"), but the abstract and introduction frame it as addressing the general question. The major weakness above captures this accurately.
- *Criticism about RDFA being "underdeveloped" or "mentioned only in passing"* — merged into Major weakness #3 above.
- *Criticism that weight-based attribution validity is not tested* — this is real but Minor (#2), not a critical issue.
- *Criticism about "not showing SAE features are not artifacts"* — this is speculation; the paper does validate features causally via the IOI noising experiment.
- *Generic "the evaluation lacks rigor" complaints* — no specific anchor in the paper.
- *Style/formatting/typo nitpicks* — parser artifacts.
- *Strength finder strengths about the problem being important* — generic; dropped.
- *Strength about RDFA being a contribution* — kept as a strength of the paper's stated contributions but its lack of evaluation is noted as a weakness.

## Novel Insights

The reviews surface a useful tension. The harsh critic correctly identifies that the 90% polysemanticity claim is overconfident given the methodology, and that the induction head analysis is narrower than the framing suggests. The strength finder correctly identifies that the IOI "and" finding is the paper's strongest result and is genuinely well-validated. What neither reviewer fully develops is the *ratio*: the paper's main contribution (making the case for Attention Output SAEs as a tool) does not actually depend on either the 90% claim or the induction head analysis being perfectly general. The tool case stands on (a) the SAE evaluation metrics in Table 1, (b) the qualitative feature families, and (c) the IOI analysis, which is the strongest validation of the tool's utility. The 90% claim and the induction head specialization are secondary findings that the paper could weaken or remove without affecting its central thesis. This suggests the paper's weaknesses are concentrated in its secondary claims, not its primary contribution.

## Suggestions
1. **Soften or remove the "at least 90%" polysemanticity claim** from the abstract and §4.1.1. Replace with "many heads appear polysemantic under this lens" and report the raw count (14/144 monosemantic candidates) without the percentage framing.
2. **Reframe the induction head section** to emphasize it as a case study demonstrating the tool's ability to generate hypotheses, rather than as progress on the general redundancy question.
3. **Either add a brief evaluation of RDFA** (even a single case study) or remove it from the numbered contributions list and present it as released tooling.
4. **Add a simple correlation plot** between weight-based attribution and DFA for a sample of features.
5. **Add at least one more alternative conjunction** (e.g., "with" or "or") to the IOI noising control experiment.
6. **Report confidence intervals** for interpretability percentages in Table 1's main text, or at minimum state the sample size limitations prominently.

## Score and Decision

### Round 1 — Bracketing

Three queries on "sparse autoencoders attention interpretability mechanistic interpretability SAE features":

| Score band | Representative anchor | Avg score | Comparison |
|---|---|---|---|
| Weak (0–3) | Wxl0JMgDoU (chess SAEs) | 2.50 | This paper has real SAE evaluation metrics and a causally validated finding; clearly stronger. |
| Weak (0–3) | UbLvSPMvMA (cosine loss SAE) | 1.67 | Much weaker contribution; not comparable. |
| Mid (4–7) | F76bwRSLeK (Bricken et al. SAEs) | 4.80 | Original SAE-for-LMs paper; more novel but less causal depth. Current paper is comparable or slightly stronger. |
| Mid (4–7) | XAjfjizaKs (Multi-Layer SAEs) | 6.50 | Very similar type of contribution (applying SAEs to new domain); comparable quality. |
| Mid (4–7) | imT03YXlG2 (PatchSAE vision) | 6.50 | Different domain, similar structure; comparable rigor. |
| Strong (8+) | tcsZt9ZNKD (Scaling SAEs) | 8.20 | Much larger scale (GPT-4, 16M latents, scaling laws); clearly stronger contribution. |
| Strong (8+) | I4e82CIDxv (Sparse Feature Circuits) | 8.00 | Novel method + extensive evaluation; clearly stronger. |

**Round 1 bracket: 5.0 – 7.0**

### Round 2 — Narrowing

| Anchor | Avg score | Comparison |
|---|---|---|
| XAjfjizaKs (Multi-Layer SAEs) | 6.50 | Both apply SAEs to new activation domains. Multi-Layer SAEs has cleaner evaluation but less qualitative depth. Current paper has a stronger causal finding (IOI "and"). **Comparable.** |
| F76bwRSLeK (Bricken et al.) | 4.80 | Original SAE paper; more novel methodologically. Current paper has better causal validation and a genuine scientific finding. **Slightly stronger.** |
| SUc1UOWndp (rLLC attention heads) | 7.00 | More novel metric, but limited to 2-layer model. Current paper works up to 2B. **Slightly weaker in novelty, stronger in scale/applicability.** |
| AwyxtyMwaG (Function Vectors) | 6.00 | Similar level: solid empirical paper with a genuine finding. **Comparable.** |
| ghH6YYDs15 (Amortisation Gap SAEs) | 4.67 | Theory paper with limited empirical scope; weaker impact. **Current paper is stronger.** |

The paper sits comfortably at the level of solid applied mechanistic interpretability papers (Bricken et al., Function Vectors) — it has a genuine causal finding (IOI "and"), adequate evaluation, and open-sourced tools, but is held back by overclaimed secondary findings (90% polysemanticity) and an unevaluated claimed contribution (RDFA). This places it slightly above Bricken et al. (4.80) and Function Vectors (6.00), and slightly below Multi-Layer SAEs (6.50) and rLLC (7.00).

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>