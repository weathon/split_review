Now I have a complete understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper identifies "generative inequality" in LLM uncertainty estimation — the observation that semantically irrelevant tokens and sentences contribute disproportionately to uncertainty scores due to being more numerous, despite carrying limited meaning. The authors propose Shifting Attention to Relevance (SAR), a two-level re-weighting framework that down-weights token- and sentence-level contributions based on semantic relevance scores computed via a cross-encoder similarity model. SAR is evaluated across multiple LLMs (OPT, LLaMA, Vicuna, WizardLM, LLaMA-2-chat up to 33B) on free-form QA datasets spanning reading comprehension, science, and medical domains, consistently outperforming Semantic Entropy (SE) and other baselines.

## Strengths

1. **Novel and well-motivated identification of a genuine bias in LLM uncertainty estimation.** The paper systematically demonstrates (Figures 2–3) that irrelevant tokens vastly outnumber relevant ones in free-form generations, and because existing methods weight all tokens equally, the total uncertainty volume is dominated by semantically unimportant content. This formalizes a previously overlooked source of noise in predictive entropy and semantic entropy approaches.

2. **Consistent and substantial empirical gains across diverse settings.** SAR outperforms SE by an average of 7.1% AUROC on instruction-tuned LLMs (Table 2), and achieves gains of 1–4 AUROC points across pre-trained LLMs (Table 1) and medical QA datasets (Table 3). The gains are consistent across model families (decoder-only, instruction-tuned) and domains (conventional NLP, science, medicine), supporting the generality of the approach.

3. **Synergy of token- and sentence-level re-weighting is empirically validated.** The paper shows that combining TOKENSAR and SENTSAR (SAR) consistently beats either component alone (e.g., OPT-30b on CoQA: TOKENSAR 0.723, SENTSAR 0.720, SAR 0.748), confirming the two levels capture complementary biases and that the combination is not redundant.

4. **Robustness and efficiency analyses strengthen the claims.** Figure 4 shows SAR is generation-efficient (reaching 0.750 AUROC with just 5 generations). Table 4 shows general-purpose sentence similarity models work well, and Figure 5 shows SAR remains superior across different Rouge-L thresholds, reducing concerns about hyperparameter sensitivity.

5. **Soft similarity replaces hard binary entailment decisions.** The paper identifies that SE's binary entailment predictions are unreliable for long generations (36.7% undesirable on a manual check of 120 questions) and replaces them with continuous similarity scores, which is a concrete methodological improvement over the SE formulation.

## Weaknesses

### Fatal
None.

### Major

1. **The sentence-level shifting formula (Eq. 9) is mathematically questionable.** The expression $$E_S(\mathbf{s}_j, S, \mathbf{x}) = -\log\!\bigl( p(\mathbf{s}_j|\mathbf{x}) + \tfrac{1}{t} \sum_{k\neq j} g(\mathbf{s}_j,\mathbf{s}_k) p(\mathbf{s}_k|\mathbf{x}) \bigr)$$ with \(t=0.001\) adds a potentially large scaled relevance term to a probability. For short sentences (e.g., 5–8 tokens) with high per-token probabilities, \((\frac{1}{t})R_S\) can dominate and push the argument well above 1, producing negative "uncertainty" values — a conceptually odd result. The paper provides no clipping, normalization, or reinterpretation to prevent this. While this likely does not invalidate the ranking-based AUROC results (since AUROC depends only on ordering, not absolute scale), the formula as stated is poorly grounded and erodes confidence in the method. The authors should either normalize the expression (e.g., dividing by a normalizer to keep the argument in [0,1]), reinterpret it as an unnormalized score, or justify the regime where it does produce positive values. This is a fixable issue but must be addressed before the method can be considered sound.

2. **No error bars or variance measures for main results.** Tables 1, 2, and 3 report AUROC as point estimates without standard deviations, confidence intervals, or significance tests. The multi-stage procedure (multiple sentence generations, external similarity model, re-weighting) introduces multiple sources of variance. With improvements often modest (1–4 AUROC points), it is impossible to assess whether gains are statistically reliable. While single-run evaluation is common in this specific sub-area, the paper would be significantly stronger with at least bootstrap confidence intervals or standard deviations across multiple runs.

### Minor

1. **The motivation analysis conflates aggregate dominance with per-token bias.** The paper states that irrelevant tokens "dominate uncertainty estimation from the perspective of total volume" (Figure 3, dashed line). This is partly a trivial counting effect: Figure 2 shows there are simply more irrelevant tokens, and existing methods weight each token equally. The average uncertainty proportion for low-relevance tokens is actually *lower* than for high-relevance tokens (Figure 3, solid line). The paper's core claim — that equal weighting is inappropriate when tokens have unequal semantic relevance — remains valid, but the framing of "irrelevant tokens are weighted heavily" is imprecise and could be sharpened.

2. **The 36.7% figure for SE's undesirable entailment predictions is based on a small manual sample.** The paper reports that "around 36.7% of the entailment predictions are undesirable" from a manual examination of 120 questions. This is a weak empirical basis for a motivation claim. The sample is small and the evaluation is not systematic. This number should be treated as anecdotal evidence, not a rigorous finding.

3. **Notation for token-level relevance (Eq. 2) is under-specified.** The expression \(g(\mathbf{x}\cup s, \mathbf{x}\cup s \setminus \{z_i\})\) uses \(\cup\) without definition. While the intent (concatenation of prompt and sentence) can be inferred, sentence similarity models are typically designed for comparing two sentences or short texts, and feeding prompt+sentence vs. prompt+sentence-minus-one-token is a non-standard use. The paper does not discuss whether the cross-encoder produces reasonable scores for such minimal-edit inputs or whether the similarity scores behave as expected.

### Trivial
None.

## Nice-to-Haves

- Study the sensitivity of the temperature \(t\) in Eq. 9. It is set to 0.001 without ablation. A sweep over \(t\) values would clarify how critical this hyperparameter is.
- Show that irrelevant tokens have *disproportionately high* uncertainty *given their count* (e.g., residual uncertainty after controlling for relevance bin size), to strengthen the causal story beyond the counting effect.
- Compare against a simpler baseline that only uses content words (e.g., filtered by POS tags) to isolate whether the gains come specifically from relevance weighting or simply from discarding function words.
- Quantify the computational overhead of the cross-encoder similarity model beyond the qualitative acknowledgment in the limitations section.

## Removed Points

These points have been removed from the main review after verification against the paper; they are preserved here for traceability:

- **"The paper does not demonstrate that this helps beyond what a simple length normalization would achieve (LN-PE already mitigates the effect)."** — *Removed because it is factually incorrect.* The paper *does* include LN-PE as a baseline (Section 5.1) and SAR outperforms it in Tables 1–3. The criticism misunderstands the paper's experimental setup.
- **"The logarithm is undefined"** (regarding Eq. 9) — *Downgraded.* The argument \(p + \frac{1}{t}R_S\) is always non-negative (both terms are non-negative), so the log is mathematically defined. The real issue is that the argument can exceed 1, producing *negative* uncertainty values, not an undefined logarithm. The concern is reframed in Major #1 above.
- **Criticism about missing appendix, proofs, or references.** — *Removed per instructions: the parser strips these sections; they exist in the original submission.*
- Generic or superficial strengths from the Strength Finder that lacked specific evidence. — *All strengths from the Strength Finder had concrete backing and were retained.*

## Novel Insights

The reviews surface an interesting tension: the paper's central motivating analysis (irrelevant tokens dominate total uncertainty volume) is simultaneously its most intuitively compelling observation and its weakest link. The total-volume dominance is a near-trivial consequence of the count asymmetry shown in Figure 2, yet the paper frames it as a discovery of "weighting bias." The real innovation is not the observation itself but the *operationalization* — demonstrating that down-weighting tokens by semantic relevance (computed via an external cross-encoder) yields measurable AUROC improvements. This suggests that even if the motivation is partly a counting artifact, the proposed correction is empirically effective. A deeper insight: the success of SAR implies that uncertainty estimation and *content selection* are deeply intertwined — methods that cannot distinguish "the" from "density" will systematically misallocate uncertainty, no matter how sophisticated their aggregation over multiple generations.

## Suggestions

1. **Fix Eq. 9.** Either normalize the argument to [0,1], reinterpret the expression as \(-\log(p) - \lambda R_S\) (an additive bonus for consistency), or add a clamping mechanism. Show that the fix does not change the empirical results.
2. **Add uncertainty quantification to the main tables.** At minimum, report bootstrapped 95% confidence intervals for AUROC or run each experiment 3–5 times and report mean ± std.
3. **Sharpen the motivation analysis.** Acknowledge explicitly that the total-volume dominance of irrelevant tokens is driven by their count, and reframe the "bias" as "equal per-token weighting is inappropriate when semantic relevance varies." A plot of *average* uncertainty proportion per relevance bin (already present as solid line in Figure 3) already supports this and should be highlighted.
4. **Define the notation in Eq. 2** (\(x \cup s\)) and validate that the cross-encoder produces meaningful similarity scores for prompt-augmented minimal-edit pairs (e.g., show a few examples with scores).

## Score and Decision

The paper identifies a genuine and previously underexplored issue in LLM uncertainty estimation and proposes a practical correction with consistent empirical support across diverse models and domains. The main weakness — a mathematically under-specified sentence-level formula — is fixable and does not invalidate the token-level component (TOKENSAR) or the overall empirical trend. However, until the Eq. 9 issue is resolved and statistical reliability is quantified, the contribution cannot be fully trusted. The paper is on the right track with a solid core idea and extensive evaluation, but needs revision to be publishable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>