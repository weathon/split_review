Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper identifies a phenomenon the authors call "generative inequality" in LLM uncertainty estimation: tokens and sentences vary in semantic relevance, yet standard uncertainty estimation methods (Predictive Entropy, Semantic Entropy) treat all tokens equally. The paper proposes SAR (Shifting Attention to Relevance), a family of methods that re-weight token-level and sentence-level uncertainty estimates by semantic relevance scores. The method is evaluated on 6 LLMs across 5 QA datasets, showing consistent AUROC improvements over several baselines.

## Strengths

- **Novel, well-motivated observation**: The paper systematically demonstrates (Figures 2-3) that irrelevant tokens and sentences dominate uncertainty volume despite carrying little semantics. This goes beyond prior work like Semantic Entropy that treats all tokens equally. The empirical analysis of this "generative inequality" is the paper's strongest conceptual contribution.

- **Consistent empirical improvements across diverse settings**: SAR (and its components TOKENSAR/SENTSAR) consistently outperform predictive entropy, length-normalized PE, lexical similarity, and semantic entropy across nearly every model–dataset pair in Tables 1-3. Improvements of up to 7.1% AUROC on instruction-tuned LLMs and 3.6% on pre-trained LLMs are reported.

- **Broad evaluation**: The paper tests on 6 LLMs (Vicuna, LLaMA-2-chat, WizardLM, OPT, LLaMA up to 33B) across 5 QA datasets (CoQA, TriviaQA, SciQ, MedQA, MedMCQA), demonstrating generality across architectures and domains.

- **Ablation studies provide practical insight**: Figure 4 shows SAR achieves strong performance with as few as 5 generations and improves with more, while some baselines plateau. Table 4 shows general-purpose sentence similarity models outperform using the target LLM itself for relevance computation — a useful guideline for practitioners.

## Weaknesses

### Fatal
None.

### Major

- **Unjustified and poorly analyzed sentence-level formulation (Eq. 9)**. The equation  
  $$E_S(\mathbf{s}_j, S, \mathbf{x}) = -\log\bigl(p(\mathbf{s}_j|\mathbf{x}) + \tfrac{1}{t} R_S(\mathbf{s}_j, S, \mathbf{x})\bigr)$$  
  with $t=0.001$ adds a term $\frac{1}{t}R_S$ that, under the paper's own framing, can dominate $p(\mathbf{s}_j|\mathbf{x})$ by many orders of magnitude. The temperature $t$ is listed as a hyperparameter but its role is never explained — no sensitivity analysis, no justification for why $t=0.001$ was chosen. The interaction between the two additive terms is not analyzed, and the paper does not discuss clipping, normalization, or how the resulting values behave. Since AUROC is rank-based, negative or shifted values do not break the evaluation entirely, **but** the formulation as presented obscures what SENTSAR is actually computing.  The authors should either (a) justify why this specific functional form is sensible, (b) provide a sensitivity analysis over $t$, or (c) replace it with a more principled formulation (e.g., multiplicative instead of additive combination). This issue also affects the combined SAR, which builds on SENTSAR.

### Minor

- **Potential factual error in the motivating analysis (Section 3.4)**. The paper states: "For the sentence-level situation, it is clear that irrelevant sentences commit more uncertainty than relevant sentences regardless of the average or the total." If Figure 3 (right panel) shows the opposite for the *average* proportion (as the reviewer indicates), then the text misrepresents the evidence. Since I cannot verify the rendered figure, I flag this for the authors to check and correct. If true, the motivation for SENTSAR would need to be revised to accurately reflect what the data show.

- **No confidence intervals or statistical significance for AUROC results**. Many improvements are small (0.01–0.02 AUROC in Table 1), and multiple generations per question create within-question correlations that standard AUROC variance formulas do not account for. The paper would be strengthened by bootstrapped confidence intervals that cluster by question.

- **Token relevance via token removal (Eq. 2) is not validated**. Removing a single token often produces an ungrammatical string, and the cross-encoder may assign low similarity for reasons unrelated to semantics (surface-form breakage). The paper does not show that these relevance scores correlate with human judgments or are robust across token types. A small human evaluation or qualitative examples would help.

- **Sentence-level relevance (Eq. 4) uses $p(\mathbf{s}_j|\mathbf{x})$ as a weight**, which is the product of all token probabilities. These values are typically extremely small and vary across sentences by orders of magnitude, so the weights may be effectively zero for most sentences. The paper does not analyze the distribution of these weights or their impact on the final estimates.

### Trivial
- The absolute value in Eq. 2 ($1 - |g(\cdot,\cdot)|$) is redundant since $g$ already returns a value in $[0,1]$.

## Nice-to-Haves
- A latency/cost analysis quantifying the additional inference overhead from the cross-encoder, beyond the limitation statement's mention of "additional latency."
- A comparison with a simple baseline that *removes* irrelevant tokens (e.g., stopword removal) before computing entropy — this would isolate the effect of reweighting from that of identification.
- Evaluation on non-QA tasks (e.g., summarization, story generation) would strengthen claims of generality, though the paper's scope is reasonably scoped to QA.

## Removed Points

These points were flagged in the initial reviews but are removed or downgraded after verification:

- **"Table 4 lacks baseline comparison"** — Removed. Table 4 is explicitly described as a sensitivity analysis of SAR to different similarity models, not a comparison against baselines. Baseline comparisons are in Tables 1-3.
- **"Demand for evaluation on non-QA tasks as a weakness"** — Moved to Nice-to-Haves. The paper scopes itself to QA; asking for additional tasks is scope creep, not a flaw.
- **"The absolute value in Eq. 2 is a weakness"** — Moved to Trivial. It's a notation nitpick that doesn't affect results.

## Novel Insights

None beyond the paper's own contributions. The paper's key insight — that tokens and sentences contribute unequally to uncertainty and that reweighting by relevance is beneficial — is well-articulated in the paper itself. The reviews do not surface additional novel angles.

## Suggestions

1. **Fix or justify the sentence-level formulation (Eq. 9).** Provide a sensitivity analysis over $t$, or replace the additive combination with a multiplicative/more principled formulation. Show that results are stable across reasonable temperature values.
2. **Verify and correct the Figure 3 description** if the text misrepresents what the data show.
3. **Add bootstrapped confidence intervals** for the main AUROC results, with clustering by question.
4. **Provide qualitative examples** of token relevance scores to validate that they identify semantically meaningful tokens rather than artifacts of ungrammatical token removal.

## Score and Decision

**Originality**: 6/10 — The generative inequality observation is genuinely novel, though the reweighting method itself is conceptually simple.
**Importance**: 7/10 — Uncertainty estimation for LLMs is an important and timely problem.
**Claims support**: 4/10 — The central empirical claim (SAR outperforms baselines) is supported, but the questionable formulation in Eq. 9 and the potential factual error in the motivation weaken confidence.
**Soundness**: 4/10 — The token-level component is sound, but the sentence-level component has an unanalyzed formulation, and the evaluation lacks statistical rigor.
**Clarity**: 6/10 — Generally well-written, though the motivation section may contain a factual error.
**Value to community**: 6/10 — The core idea is useful and the extensive evaluation across models/datasets is valuable, but the methodological issues need resolution.

The paper's core insight — that not all tokens are equally relevant for uncertainty estimation — is genuine and worth pursuing. However, the sentence-level formulation (Eq. 9) is not properly motivated or analyzed, and the temperature parameter $t=0.001$ is used without any justification or sensitivity study. Combined with the lack of statistical confidence measures and a potential factual error in the motivating analysis, these issues collectively prevent the paper from being accepted in its current form. The contribution is salvageable with significant revision.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>