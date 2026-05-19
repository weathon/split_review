- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information needed to produce the consolidated review. Let me synthesize everything.

---

## Summary

This paper presents AMIC (Attention-based Multiple Instance Classification), a model that produces interpretable word-level sentiment scores—context-independent sentiment, sentiment word indicators, and global/local contextual shifters—while learning only from document-level labels. The model uses a modified relative-position self-attention to capture negation and achieves competitive document-level accuracy (0.8898 on wine reviews vs. BERT's 0.8912) with far fewer parameters. The key contribution is a transparent, decomposed architecture whose internal components are designed to correspond to linguistically meaningful properties.

## Strengths

1. **Competitive document-level accuracy with far fewer parameters than BERT.** Table 1 shows AMIC achieves 0.8898 on wine reviews (vs. BERT 0.8912) and 0.8225 on Sentiment140 (vs. BERT 0.8545), demonstrating that interpretability does not require a dramatic performance sacrifice.

2. **Transparent architecture with decomposed sentiment components.** Equations (3)–(5) decompose sentiment into context-independent score \(v_{ij}\), sentiment indicator \(\delta^s_{ij}\), global shifter \(\delta^g_{ij}\), and local shifter \(\delta^l_{ij}\). Tables 3–6 show concrete numerical values for each component, enabling direct inspection of the model's internal reasoning.

3. **Explicit, demonstrable handling of negation via the local sentiment shifter.** The ablation study (Table 2) shows removing the local shifter causes the largest performance drop (0.8225 → 0.8050). Section 4.3 further shows how \(\delta^l_{ij}\) takes negative values to flip sentiment in "not bad" and "not good," confirming the mechanism works as intended.

4. **Ablation study quantifies relative importance of architectural components.** Table 2 systematically removes each \(\delta\) term, showing local shifter > sentiment indicator > global shifter in importance, validating the design hierarchy.

5. **Demonstrates generalization across multiple negation types.** Section 4.3 provides examples of preceding negation (Tables 3–4), succeeding negation ("cancer-free" in Table 5), and implicit negation ("dreams shattered" in Table 6), each with component values aligning with linguistic expectations.

6. **Parameter-efficient modification of relative-position self-attention.** Equation (2) removes Value vectors from the local dependency computation, reducing parameters by ~30% relative to Shaw et al. (2018). The paper provides a clear rationale: because AMIC has decomposed semantic/sentiment information into separate components, \(r^l_{ij}\) can focus specifically on positional patterns.

## Weaknesses

### Major

1. **Word-level interpretability is validated only through qualitative examples, with no quantitative evaluation.** The paper's central claim is providing interpretable word-level sentiment analysis, yet Section 4.3 evaluates interpretability entirely through four hand-picked example sentences. There is no quantitative assessment of whether word-level outputs (sentiment scores, neutrality indicators, shifter values) correspond to true word-level sentiment—e.g., correlation with human word-level ratings, agreement with a sentiment lexicon, or evaluation on a word-level benchmark like the Stanford Sentiment Treebank. While the qualitative examples are detailed and systematic (covering preceding, succeeding, and implicit negation), they remain illustrative rather than demonstrative. A reader cannot determine whether the internal decompositions reliably capture the linguistic phenomena they claim to, or whether the model fits document labels through some mechanism that happens to produce plausible numbers on a few examples.

   *Concretely: the paper would be substantially strengthened by evaluating against a dataset with phrase- or word-level sentiment annotations (e.g., SST fine-grained labels, MPQA subjective/objective annotations, or correlation with a sentiment lexicon like SentiWordNet).*

2. **The modified self-attention (Eq. 2 vs. Eq. 1) is not directly ablated.** The paper claims a 30% parameter reduction and improved sensitivity to positional information from removing Value vectors in Equation (2), but never empirically compares the two formulations. Without an ablation comparing the proposed version (Equation 2) with the original Shaw et al. formulation (Equation 1) on both accuracy and interpretability quality, the benefit of this design choice is asserted rather than demonstrated. The existing ablation (removing the entire local shifter) confirms the component's importance but does not validate the specific modification.

### Minor

3. **No variance or confidence intervals reported for any result.** Tables 1 and 2 present point estimates without standard deviations, confidence intervals, or significance tests. The claimed "on par with BERT" difference (0.8898 vs. 0.8912 on wine) could easily fall within noise. Without this basic information, the experimental conclusions are uncalibrated, especially for the ablation study where differences between ablations are modest.

4. **No sensitivity analysis for penalty hyperparameters \(c_1, c_2, c_3\) or the scaling factor of 10 for \(\delta^g_{ij}\).** These hyperparameters control the balance between sparsity, binarization, stability, and gradient flow—they could strongly influence both accuracy and the qualitative behavior shown in the interpretability examples. Without analysis of their effect, the model appears tuned without justification for these critical values.

### Trivial

5. **The edge case in Equation (5) where \(\sum r^s_{ij} \approx 0\) is not formally addressed.** If no (or very few) words are identified as sentiment words, the normalization in \(Z_i\) could become unstable. The penalty terms likely prevent this in practice, but the formulation could note the edge case.

## Nice-to-Haves

- A comparison of the modified attention (Eq. 2) vs. the original (Eq. 1) would cleanly validate the design choice.
- Sensitivity analysis for hyperparameters \(c_1, c_2, c_3\) and the scaling factor of 10 would strengthen confidence in results.
- A brief discussion of limitations—particularly the fact that word-level decompositions are unconstrained by any word-level signal and may not perfectly correspond to human notions of negation or neutrality—would improve the paper's completeness.

## Removed Points

- **Criticism about interpretability being "fatal" or "unsupported":** The harsh critic framed the lack of quantitative word-level evaluation as a fatal flaw that invalidates the paper's core claim. This is downgraded from Fatal to Major. The paper does provide systematic qualitative evaluation (four examples across multiple negation types), and the architecture is transparent by construction—the claim is about *interpretability* (ability to inspect internal components), not about quantitatively *validated* word-level sentiment accuracy. The weakness is real and significant, but the paper's contribution is not nullified.

- **Criticism about the penalty term \(p_{i3}\) justification being vague:** The paper explicitly states (line 117) that \(p_{i3}\) "imposes an L2 penalty to prevent the model from arbitrarily inflating the magnitude of \(v_{ij} \times \delta^g_{ij} \times \delta^l_{ij}\) in situations where \(\delta^s_{ij}\) may take close-to-zero values in the early training stage." The rationale is present, though the critic found it unclear. This is too minor/fine-grained to include as a standalone weakness.

- **Strength Finder generic strengths removed:** The Strength Finder contained some generic framing (e.g., "demonstrates generalization across different negation types" — this is already covered by the specific example analysis). Kept only concrete, evidence-grounded strengths.

## Novel Insights

The harsh critic's framing that the interpretability gap is "fundamental" usefully sharpens what a revision would need to address. The insight that AMIC's design choices (removal of Value vectors from local attention, decomposition into multiplicative components) are individually plausible but collectively unevaluated—no single experiment validates that the internal representations correspond to their intended linguistic interpretations—is a genuinely helpful diagnostic. The Strength Finder's identification that the architecture's transparency itself (directly reading \(v_{ij}, \delta^s_{ij}, \delta^g_{ij}, \delta^l_{ij}\)) is a form of interpretability, and the qualitative examples are concrete evidence, provides a useful counterpoint: the paper does deliver inspectability, but stops short of demonstrating that what's inspected is *correct*.

## Suggestions

- **Add a quantitative evaluation of word-level outputs.** This is the single most impactful improvement. Use the Stanford Sentiment Treebank (phrase-level labels), MPQA (subjective/objective annotations), or compare against a sentiment lexicon (e.g., SentiWordNet, VADER) with rank correlation or agreement metrics. Alternatively, measure how well \(\delta^s_{ij}\) aligns with human-annotated sentiment-bearing words on a small annotated subset.
- **Add an ablation comparing Eq. 2 vs. Eq. 1** (original Shaw et al. formulation) on accuracy, parameter count, and interpretability quality to validate the modified attention design.
- **Report confidence intervals or standard deviations** over at least 5 random seeds for the main results and ablation study.
- **Add a sensitivity analysis** for the key hyperparameters \(c_1, c_2, c_3\) and the scaling factor of 10 for \(\delta^g_{ij}\).
