- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 8, 5, 5
Now I have everything I need. Let me construct the final consolidated review.

## Summary

This paper generalizes Minimum Bayes' Risk (MBR) decoding to account for weight uncertainty by incorporating a posterior over model parameters into the expected risk computation. It derives sequence-level and token-level Monte Carlo estimators (Eqs. 9, 10, 13), evaluates across machine translation, summarization, data-to-text, and scoring tasks using prompted, finetuned, and from-scratch-trained models, and explores selective prediction and scaling behavior. The theoretical framing is sound and the experimental scope is broad.

## Strengths

- **Principled theoretical derivation of practical estimators.** Sections 3.1–3.3 derive how the predictive-posterior MBR reduces to Monte Carlo estimators (Eqs. 9, 10, 13) requiring only the ability to sample from models — not token-level probabilities — making the method applicable even with black-box LLMs. The connection to PAC-Bayes is noted as a useful pointer (line 120).

- **Consistent empirical gains across tasks with matched effective-beam-size budgets.** Tables 1 and 2 show that uncertainty-aware MBR (unimodal and multimodal posteriors) improves over standard MBR on BLEU, COMET, LaBSE, ROUGE, and RMSE across finetuned Gemma-2B and from-scratch-trained Transformers, while controlling for the number of MBR comparisons and effective beam size (beams/model × number of models). Improvements also hold for the STS-B scoring task.

- **Strong evidence linking prediction diversity to performance.** Figure 1 shows a clear positive correlation between model diversity (measured via self-BLEU) and downstream quality. Controlled experiments with higher temperature in IVON (increasing diversity) improve performance, providing causal evidence that diversity drives gains. Snapshot ensembles — which impose no training overhead — also improve performance, reinforcing this link.

- **Comprehensive evaluation across tasks, models, and posterior types.** The paper evaluates on machine translation (WMT14, IWSLT14/17, afroMT), summarization (XSUM, SAMSum), data-to-text (E2E-NLG), and scoring (STS-B), using zero-shot prompted LLMs (Llama-3, Mistral, Gemma-2, Qwen-2), finetuned models (LoRA on Gemma-2B), and models trained from scratch (Transformer big/base). This thoroughness strengthens claims of general applicability.

## Weaknesses

### Fatal

None.

### Major

- **No statistical significance reporting for key results.** Tables 1 and 2 present point estimates without confidence intervals, error bars, or significance tests. Given the modest improvements (e.g., ~0.5–1.5 BLEU on WMT14, ~1–2 chrF on IWSLT14), it is impossible to assess whether observed differences are reliable. The reference to Kocmi et al.'s >85% human-detectability threshold for COMET (line 196) provides context for one specific comparison but does not substitute for variance estimates across all results. At minimum, bootstrap confidence intervals or multiple-seed runs should be reported. This is the single biggest gap in the current evidence.

- **Selective prediction experiments lack comparisons to established baselines.** Section 4.4 and Figure 2 compare only within the proposed framework (different posterior approximations and sampling strategies), without comparing to standard selective prediction baselines such as predictive entropy, mutual information, or semantic entropy (Kuhn et al., 2023 — which the paper cites). Without such comparisons, it is unclear whether Bayes' risk improves upon simpler methods, or whether the observed trends merely reflect the benefit of ensembling. Since the paper claims selective prediction as a contribution, this gap is significant.

- **Compute-fairness control is partially addressed but incompletely justified.** The paper matches the *number of MBR utility comparisons* and controls *effective beam size* (beams/model × models). For the unimodal posterior case with 4 weight samples, this yields comparable total autoregressive forward passes (e.g., 3 beams × 4 models ≈ 12 vs. 10 beams × 1 model ≈ 10). However, this analysis has two limitations: (a) the paper does not report wall-clock time, FLOPs, or any end-to-end timing comparison, so practitioners cannot assess the actual trade-off; (b) the generation cost for token-level posteriors (Eq. 13) additionally requires per-token softmax for each ensemble member, which is not accounted for in the beam-size matching. While the §4.5 scaling experiments (varying ensemble size and hypothesis set size) partially address the concern, the core evaluation in Tables 1–3 would benefit from explicit compute transparency (time or FLOPs) and ideally an ablation controlling for total generation + utility cost.

### Minor

- **BLEU utility choice for IWSLT14 and afroMT is not justified.** The paper uses BERTScore as the utility function for most tasks but switches to BLEU for IWSLT14 and afroMT without explanation (line 178). BLEU is known to correlate less well with human judgment than modern learned metrics for MBR (Freitag et al., 2022). The authors should either justify the choice or report results with both utilities.

- **The claim about "unbiased estimate" in Eq. (9) is stated without acknowledging the nested approximation structure.** The paper states that Eq. (9) provides an unbiased estimate of Eq. (7) (line 120). While technically correct for the Monte Carlo estimator of the expectation given the approximate posterior q(θ), the overall procedure inherits approximation error from posterior approximation and from limited sample sizes. A brief qualification would prevent misinterpretation.

### Trivial

None (filtering typo/formatting issues as parser artifacts).

## Nice-to-Haves

- **Temperature scaling with single-model hypotheses (related to §4.3).** The paper shows that increasing temperature (via IVON's λ parameter) improves diversity and performance for the ensemble. A natural control experiment would test whether the same temperature increase applied to hypotheses drawn from a *single* model also improves MBR performance — helping isolate whether gains come from model diversity or simply hypothesis diversity. This would strengthen the causal analysis.

- **Practitioner guidelines summary for §4.5.** The scaling section (§4.5) contains nuanced findings (e.g., sequence-level combination works better for small beam sizes, token-level for larger; unimodal posteriors fail with beam search for token-level combination). A concise summary of which method to use under which resource constraints would increase practical impact.

- **Qualitative error analysis.** The paper focuses on aggregate metrics. A case analysis of where uncertainty-aware MBR helps vs. hurts would strengthen the narrative and build intuition.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"For-free" improvements claim is "misleading"** (from §4.2 criticism): The critic argued that "both training time and time needed for decoding are the same" conflates training and decoding stages. However, the paper's mechanism — using effective beam size (beams/model × models) — makes this claim approximately defensible: with IVON, training is indeed a single run; for decoding, 3 beams × 4 models ≈ 12 forward passes vs. baseline 10 beams × 1 model ≈ 10 passes. There is engineering overhead for model switching, but the paper's framing is not inaccurate, and the matching rationale is explained. This criticism is weakened substantially upon verification.

- **§3.2 unbiased-estimate claim needing "more care"** (from §3.2 criticism): The claim that Eq. (9) is an unbiased estimate of Eq. (7) is standard Monte Carlo theory for nested expectations (sample θ ~ q, then y ~ p_θ). The posterior approximation issue (q ≈ p(θ|D)) is a separate and universal caveat in Bayesian methods, not a flaw in the unbiasedness claim. Removing.

- **§4.3 not testing whether temperature increase applied to single model also improves MBR** (moved to Nice-to-Haves — a useful extension, not a weakness).

- **§4.5 missing practitioner guidelines** (moved to Nice-to-Haves).

- **Generic/superficial/conflicting strengths from Strength Finder**: All kept strengths are concrete and anchored in the paper's evidence. No strengths removed for being generic.

## Novel Insights

The most interesting observation from the reviews — beyond the paper's own contributions — is the asymmetric interaction between posterior expressiveness and the decoding algorithm used to construct the hypothesis set. The paper discovers (and the scaling experiments confirm) that token-level posteriors work well with ancestral sampling but fail with beam search for unimodal posteriors, while sequence-level combination is more robust. This suggests a deeper principle: token-level averaging (Eq. 13) may be more sensitive to diversity collapse under beam search because it operates in probability space, where mode-seeking behavior can concentrate probability mass on a single mode. The reviews did not surface a genuinely novel theoretical insight beyond this practical pattern.

## Suggestions

1. Report confidence intervals (bootstrap or multiple seeds) for all main results in Tables 1 and 2, and consider reporting statistical significance for the key comparisons.
2. Add at least one standard selective prediction baseline (e.g., semantic entropy from Kuhn et al., 2023, or average token entropy) to Figure 2 to contextualize the proposed criteria.
3. Include a table or brief paragraph reporting wall-clock time (or estimated FLOPs) for generation + utility computation across methods to resolve the compute-fairness concern.
4. Justify the BLEU utility choice for IWSLT14 and afroMT, or show results with BERTScore as well.
5. Add a brief "practitioner recommendations" paragraph at the end of §4.5 summarizing which method to use under which resource constraints.
6. Qualify the "unbiased estimate" statement in §3.2 with a brief note about the nested approximation structure.
