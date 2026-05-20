Now I have sufficient calibration. Let me write the consolidated review.

## Summary

This paper trains Sparse Autoencoders (SAEs) on attention layer outputs (specifically the pre-output-projection concatenated head vectors) rather than the more common MLP or residual stream targets. It demonstrates that these "Attention Output SAEs" yield sparse, interpretable features across models up to 2B parameters. The paper's main contributions are: (1) a weight-based head attribution technique for associating SAE features with specific attention heads, (2) a systematic survey of all 144 heads in GPT-2 Small revealing novel motifs (e.g., preposition mover heads) and estimating that over 90% of heads are polysemantic, (3) a clean causal demonstration that two seemingly redundant induction heads (5.1 and 5.5) specialize in long-prefix vs. short-prefix induction, and (4) an analysis of the IOI circuit's "positional signal" showing it is determined by whether the duplicate name appears before or after the "and" token. The SAEs and an interactive exploration tool are open-sourced.

## Strengths

- **Causal discovery of induction head specialization (Section 4.2, Figure 3):** This is the paper's strongest piece of evidence. Using SAE feature inspection, the paper hypothesizes that heads 5.1 and 5.5 in GPT-2 Small specialize in long-prefix vs. short-prefix induction, then confirms this with independent causal interventions: corrupting the long prefix drops head 5.1's induction score from 0.55 to 0.05 while head 5.5 maintains 0.43. This cleanly resolves an open question about why models have multiple seemingly redundant induction heads.

- **Resolution of the IOI circuit's positional signal (Section 4.3, Figure 4):** The paper uses SAE features to discover that the "positional signal" in the IOI circuit (left as an open mystery by Wang et al. 2023) is whether the duplicate name appears before or after the "and" token. A noising experiment that preserves this property recovers ~93% of logit difference, while replacing "and" with "alongside" recovers only ~43%. This is a genuine advance in understanding a well-studied circuit.

- **Weight-based head attribution technique (Section 2, Equation 2):** A methodologically sound approach that exploits the concatenated structure of attention outputs to attribute SAE features to individual heads by taking the norm of each head's slice of the decoder vector. This enables head-level analysis without assuming heads are monosemantic, and is used across all three downstream investigations.

- **Systematic head survey of GPT-2 Small (Section 4.1):** The paper inspects all 144 attention heads in GPT-2 Small, identifying both known motifs (induction heads, previous token heads, successor heads, duplicate token heads) and novel ones (e.g., preposition mover heads). This provides a useful reference for the interpretability community.

- **Demonstration across multiple models and layers (Table 1):** SAEs are trained on GPT-2 Small (all 12 layers), Gemma-2B, and GELU-2L, showing that the approach generalizes beyond a single model. The reported L0, CE recovery, and interpretability percentages provide concrete quantitative evidence.

- **Open-sourced artifacts:** The trained SAEs and an interactive exploration tool are released, increasing practical utility and reproducibility.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Interpretability evaluation lacks rigor (Section 3.2, Table 1):** The paper reports that 60–97% of features are "interpretable" based on 30 randomly sampled features per layer, rated by the authors without blinding, inter-rater reliability, or a detailed scoring rubric. The paper acknowledges human judgment may be flawed and defers confidence intervals to the appendix, but the methodology is thin relative to the prominence of the claim ("SAEs find sparse, interpretable decompositions" in the abstract). The qualitative case studies (Section 3.3) are far more convincing than these percentages. This does not undermine the paper's core contributions — the applications in Sections 4.2 and 4.3 stand on their own — but it weakens the advertised quantitative framing.

- **The "at least 90% of heads are polysemantic" estimate is imprecise (Section 4.1):** The paper derives this figure from examining the top-10 SAE features per head via weight-based head attribution. Looking at only 10 features cannot establish whether a head's remaining features are unrelated to those top-10, and the paper provides no formal operationalization of polysemanticity at the head level. The paper does use the word "suggests" and references appendix limitations, but the claim is stated without sufficient methodological rigor.

- **The "alongside" experiment in the IOI analysis has a confound (Section 4.3):** The experiment replaces "and" with "alongside" to test whether the positional signal depends specifically on the "and" token. The 43% recovery rate could partly reflect the model's unfamiliarity with "alongside" as a rare word rather than specifically the loss of the "and"-based positional signal. The paper's conclusion that the positional signal is "solely determined" by the "and" relation is stronger than the experiments fully establish. Nevertheless, the approach is clever and the results are highly suggestive.

- **No error bars on key metrics in Table 1:** L0 and CE recovery are reported as point estimates without confidence intervals or standard deviations, making it difficult to assess variability.

### Trivial

- The CE recovery metric uses zero ablation as its baseline (Section 3.1). The paper acknowledges this, but a mean-ablation baseline would be more informative. This is standard practice in the field so not a major concern.

## Nice-to-Haves

- Extending the induction head specialization finding beyond the two heads in GPT-2 Small to other models would greatly increase impact.
- Causal validation on a broader random sample of SAE features (beyond just the IOI study) would provide stronger evidence that the features reflect causally meaningful intermediate variables rather than just correlations.
- Direct comparison to simpler baselines for interpreting attention layer outputs (e.g., linear probes, PCA) would strengthen the case that SAEs uncover novel information beyond head-level analysis.

## Removed Points

- **Missing baseline comparison with simpler methods:** The harsh critic argued the paper doesn't compare to linear probes/PCA. This is scope creep — the paper's goal is to demonstrate SAE utility, not to benchmark against every possible method. The relevant comparisons (sparsity, fidelity, interpretability) are already provided.
- **"CE recovery uses extremely weak baseline (zero ablation)":** The paper transparently defines this metric and acknowledges limitations. This is standard practice in SAE evaluation (following Bricken et al. 2023) and not a weakness.
- **Strength about polysemanticity quantification:** The strength finder claimed this as a strength, but the weakness about its imprecision is correct, so this strength is dropped per the rule that weakness wins when they disagree.
- **Formatting/style nitpicks and missing appendix references:** These are parser artifacts, not author errors.

## Novel Insights

The integration of the two reviews surfaces a useful observation that neither individually emphasizes: the paper's strongest evidence (induction head specialization, Section 4.2) comes from the SAE features *enabling a hypothesis* that is then *independently confirmed with non-SAE causal interventions*. This two-step pattern — SAEs as hypothesis-generation tools, followed by targeted interventions — is a methodological template for how SAEs can be used rigorously without over-relying on the SAE features themselves as evidence. The paper would benefit from framing this more explicitly as its core methodological contribution, rather than presenting the SAE quantitative metrics (interpretability percentages, etc.) as the primary evidence.

## Suggestions

- **Strengthen the interpretability evaluation:** Either (a) provide a more rigorous evaluation with blinded rating, multiple raters, and inter-rater reliability statistics, or (b) re-center the paper's claims around the qualitative case studies and causal applications (which are the strongest evidence), and present the interpretability percentages as suggestive rather than definitive.
- **Caveat the polysemanticity estimate more prominently:** Change "over 90% of heads are polysemantic" to "our method suggests that over 90% of heads may be polysemantic, based on examining the top-10 features per head," and discuss the limitations of this proxy more explicitly in the main text.
- **Address the "alongside" confound in the IOI analysis:** Test with multiple alternative connectors (e.g., "with," "while") or include a frequency-matched control to rule out the possibility that the drop is partly due to token rarity rather than loss of the positional signal.
- **Add error bars to Table 1** where feasible, or at minimum note the sources of variability in the training/evaluation process.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/Wxl0JMgDoU.md | 2.50 | R1 | Much weaker — SAEs on chess model, unclear contribution |
| /home/wg25r/review_agent/human_reviews/bIb1xhSCVY.md | 3.00 | R1 | Weaker — SAEs on reward models, limited evaluation |
| /home/wg25r/review_agent/human_reviews/89wVrywsIy.md | 3.40 | R1 | Weaker — automated circuit tracing, lacks faithfulness evidence |
| /home/wg25r/review_agent/human_reviews/WxqWuG431g.md | 2.60 | R1 | Much weaker — SAE feature geometry, exploratory |
| /home/wg25r/review_agent/human_reviews/ghH6YYDs15.md | 4.67 | R2 | Weaker — theoretical SAE analysis, withdrawn |
| /home/wg25r/review_agent/human_reviews/TIjBKgLyPN.md | 5.50 | R1 | Weaker — SAE architecture variants, rejected despite decent scores |
| /home/wg25r/review_agent/human_reviews/HpUs2EXjOl.md | 5.75 | R2 | Weaker — polysemous word SAE eval, narrower contribution |
| /home/wg25r/review_agent/human_reviews/ZLAQ6Pjf9y.md | 5.60 | R2 | Weaker — SAE for radiology, narrow application |
| /home/wg25r/review_agent/human_reviews/XAjfjizaKs.md | 6.50 | R1/R2 | **Similar** — Multi-layer SAE, comparable novelty and rigor |
| /home/wg25r/review_agent/human_reviews/MDvecs7EvO.md | 6.50 | R2 | **Similar** — SAE feature matching, comparable scope and validation |
| /home/wg25r/review_agent/human_reviews/1Njl73JKjB.md | 7.00 | R1/R2 | **Slightly stronger** — Principled SAE eval, more rigorous methodology |
| /home/wg25r/review_agent/human_reviews/tcsZt9ZNKD.md | 8.20 | R1 | Stronger — SAE scaling laws, comprehensive evaluation |
| /home/wg25r/review_agent/human_reviews/I4e82CIDxv.md | 8.00 | R1 | Stronger — Sparse feature circuits, more extensive causal validation |

**Round 1 Bracket:** The paper sits between the weak anchors (< 3.5, clearly reject-level) and strong anchors (> 7.5, top-tier work). Narrowest plausible range: 5.5–7.5.

**Round 2 Narrowing:** Comparing against anchors in the 4.5–7.5 range, the paper is stronger than the polysemous words SAE eval (5.75) and the adaptive sparsity allocation paper (5.5), comparable to the Multi-Layer SAE paper (6.5) and the SAE Match paper (6.5), and slightly weaker than the Principled SAE Evaluations paper (7.0). The paper's main advantages over the 6.5 anchors are its concrete causal discoveries (induction head specialization, IOI positional signal) that go beyond methodological proposals. Its main disadvantage relative to the 7.0 anchor is the less rigorous quantitative evaluation of interpretability.

**Final Score:** 6.5 — The paper makes a genuine contribution to mechanistic interpretability with well-supported causal findings, but is held back by imprecise quantitative claims about interpretability percentages and polysemanticity estimates. The core contributions (induction head differentiation, IOI circuit analysis, weight-based head attribution) are solid and likely to be adopted by the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>