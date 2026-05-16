Here is my consolidated review after cross-checking every claim against the paper.

---

## Summary

This paper identifies **generative inequality** in LLM uncertainty estimation: tokens and sentences with limited semantic content are weighted equally with informative ones in standard methods (Predictive Entropy, Semantic Entropy). The authors quantify this inequality (Figures 2–3) and propose **Shifting Attention to Relevance (SAR)**, which re-weights token-level and sentence-level contributions by learned relevance scores. Experiments across OPT, LLaMA, Vicuna, WizardLM, and LLaMA-2-chat (up to 33B parameters) on CoQA, TriviaQA, SciQ, MedQA, and MedMCQA show consistent AUROC improvements over baselines.

## Strengths

- **Novel identification and empirical characterization of generative inequality.** Section 3.2–3.4 formalizes token- and sentence-level relevance (Eqs. 2–5) and provides quantitative evidence (Figures 2–3) that irrelevant tokens dominate uncertainty *in total volume* not because individual irrelevant tokens have high uncertainty, but because they are numerous. This is a genuine observation that directly motivates the method.

- **Consistent improvements across diverse models, sizes, and domains.** Tables 1–3 show SAR outperforming baselines (Predictive Entropy, Length-Normalized PE, Semantic Entropy, Lexical Similarity) across 5 pre-trained LLMs (OPT 2.7B–30B, LLaMA 7B–13B) and 3 instruction-tuned LLMs (Vicuna 13B/33B, LLaMA-2-chat 13B, WizardLM 13B) on reading comprehension, science QA, and medical QA. The improvement over Semantic Entropy averages 7.1% AUROC on instruction-tuned models (Table 2).

- **Orthogonal token- and sentence-level components with clear formulation.** Token-level shifting (Eqs. 6–8) re-weights tokens by normalized relevance; sentence-level shifting (Eqs. 9–10) amplifies sentences consistent with other generations. The combination (SAR, Eq. 11) consistently outperforms either component alone (e.g., 0.748 vs. 0.723/0.723 for OPT-30b on CoQA, Table 1), validating the design.

- **Ablation studies on key design choices.** Figure 4 shows SAR is generation-efficient (0.750 AUROC with only 5 generations) and improves with more generations while baselines sometimes degrade. Table 4 tests sensitivity to different similarity models. Figure 5 examines robustness to correctness thresholds.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Unfulfilled "demographic analysis" claim.** The abstract states results are "coupled with a comprehensive demographic analysis" and Section 5 opens with "We conduct comprehensive experiments and detailed demographic analyses," but the paper contains no demographic analysis. This is an error in the abstract/introductory framing that should be corrected.

- **The relevance measure (Eq. 2) partially conflates grammatical disruption with semantic importance.** Token relevance is defined as the semantic change after removing that token, measured by a sentence similarity model. Removing a function word (e.g., "of" from "density of an object") produces a fragment whose embedding may differ from the original for syntactic rather than semantic reasons. The paper does not discuss this confound. While the empirical success of SAR suggests the measure is practically useful, the claimed interpretation — that it cleanly separates *semantically* important tokens — needs qualification. The authors should either address this confound or characterize relevance as an *operational* (rather than purely semantic) measure.

- **Equation (9) can produce negative "entropy" values, and this behavior is not discussed.** Equation (9) computes \(E_S(s_j,S,x) = -\log(p(s_j|x) + \frac{1}{t}R_S(s_j,S,x))\) with \(t=0.001\). The relevance term \(R_S\) can push the log argument above 1, producing a negative value for \(E_S\) (since \(-\log(>1) < 0\)). This does *not* make the logarithm undefined (the argument is always positive), and negative values are not necessarily invalid for a scoring function, but the paper presents no discussion of when this occurs or whether it causes practical issues. The formulation should be clarified or stabilized (e.g., with a note that this is a shifted scoring function, not a proper entropy).

- **Improvements over Length-Normalized Predictive Entropy (LN-PE) are modest.** SAR outperforms LN-PE by 0.01–0.03 AUROC in most settings (Table 1), with one case (LLaMA-13b CoQA) where SAR is slightly *worse* (0.935 vs. 0.937). These margins are meaningful but modest, and the paper does not report statistical significance or confidence intervals. Since token-level shifting normalizes relevance scores (Eq. 6) partly to "mitigate the bias posed by sentence length, like the length normalization in LN-PE" (line 171), the reader cannot fully rule out that the improvement comes from a slightly different length normalization rather than from semantically meaningful re-weighting. An ablation with random/uniform token weights would strengthen the attribution.

- **The core observation that irrelevant tokens dominate total uncertainty volume is partly a mathematical artifact.** Figure 3 shows irrelevant tokens dominate the *total* uncertainty volume but not per-token uncertainty — the paper acknowledges "due to a large number of irrelevant tokens" (line 128). This is largely a consequence of token frequency, not a deep linguistic finding. The paper's contribution (re-weighting to correct this) is still valid, but the "observation" is somewhat overstated.

### Trivial

- **The Figure 1 example (token "of" committing "extremely large" negative-log-probability) may not be representative.** In standard LLMs, "of" is highly predictable after "density," so its negative log probability is typically low. The illustrative example could weaken first impressions. This does not affect the paper's core claims or experimental results.

- **No statistical significance tests reported.** Given the modest margins (1–3%), reporting confidence intervals or significance tests for key comparisons (SAR vs. LN-PE) would strengthen the paper. The consistent pattern across settings partially mitigates this.

## Nice-to-Haves

- An ablation where token weights are randomized or replaced with uniform weights, to directly test whether the specific relevance *values* (beyond simple re-weighting) drive the improvement.
- Computational cost/runtime comparison with baselines (rough inference-time overhead).
- Evaluation under different decoding configurations (temperature, top-p sampling) to test robustness.
- A note on whether the log argument in Eq. (9) was ever observed to exceed 1 in practice, and if so how it was handled.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The log argument in Eq. (9) could become negative, making the logarithm undefined."** — This is factually incorrect. The argument is \(p(s_j|x) + \frac{1}{t}R_S(s_j,S,x)\). Since \(p(s_j|x) > 0\) and \(R_S\) is a sum of non-negative terms, the argument is always positive. The log is always defined. (The argument can exceed 1, producing negative \(E_S\) values, which is a separate point kept above.)
2. **"The method cannot be reliably implemented without additional constraints."** — Overstated. The method as specified computes correctly; the only issue is that \(E_S\) can become negative, which is unusual but not an implementation barrier.
3. **"The ablation in Table 4 is circular because the best similarity model is the one the authors chose."** — Standard practice; the ablation tests whether the method is robust to the choice of similarity model, which it is (all models work, with the target LLM being worst). This is informative, not circular.
4. **"No evaluation on closed-source models"** — Scope creep. The paper already evaluates 8 open-source LLMs. Demanding closed-source models is outside the paper's stated scope.
5. **Strength Finder's "substantial performance gains" wording** — Qualified: SAR substantially outperforms Semantic Entropy (7.1% avg) but gains over LN-PE are modest. The strength remains valid with appropriate caveats.

## Novel Insights

The reviews surface that the paper's central "observation" (irrelevant tokens dominate uncertainty volume) is partly a frequency artifact rather than a deep finding about token semantics, while the method itself remains empirically useful. The key unresolved tension is whether the relevance measure captures semantic importance or simply grammatical disruption — but since the method works regardless, this is more a question of interpretation than validity. The most actionable insight from the reviews is that the paper would benefit from an ablation comparing SAR's learned weights against random/uniform weights to isolate whether the *specific relevance values* drive the improvement or whether mere re-weighting suffices.

## Suggestions

1. **Correct the abstract.** Remove the unfulfilled "comprehensive demographic analysis" claim or add such an analysis (e.g., performance breakdown by answer length, question type, or domain).
2. **Clarify the nature of the relevance measure.** Add a discussion acknowledging that Eq. (2) may conflate syntactic disruption with semantic change, and characterize relevance as an *operational* measure.
3. **Stabilize or discuss Eq. (9).** Add a note on when the log argument exceeds 1, whether this occurred in experiments, and how the resulting negative values should be interpreted (or clip/clamp the argument).
4. **Add an ablation with random/uniform token weights** to demonstrate that the *learned* relevance values specifically contribute to the improvement over LN-PE.
5. **Report confidence intervals or statistical significance** for the key SAR vs. LN-PE comparisons.

## Score and Decision

The paper makes a genuine contribution — identifying generative inequality in uncertainty estimation and proposing a principled re-weighting scheme with consistent empirical validation across diverse models and tasks. The weaknesses are real but local: an unfulfilled abstract claim, a relevance measure that could be better characterized, a missing numerical discussion, and modest margins over LN-PE that could be better attributed. None of these undermine the paper's core thesis or the validity of its main results. With minor revisions (especially correcting the abstract), the paper is ready for publication.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>