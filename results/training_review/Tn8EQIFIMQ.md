Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper proposes training small language models (10M parameters) on synthetic arithmetic equations for expected value (EV) and present value (PV) calculations, then using the model's embeddings (via logistic regression) to predict human choices in risky and intertemporal decision-making tasks. The authors systematically vary the training data distribution (uniform vs. ecologically valid) and the presence of correct answers, finding that the ecologically trained model's embeddings outperform classical behavioral models (CPT, hyperbolic discounting) and, on some datasets, match or exceed embeddings from LLaMA-3-70B. The paper also analyzes the embeddings to reveal human-like patterns such as probability weighting, utility curvature, and hyperbolic discounting.

## Strengths

- **Systematic ablation of pretraining data.** The four training variants (uniform/ecological × with/without correct answers) provide controlled evidence that ecological distributions of probabilities and values are necessary for producing human-like embeddings, not just any arithmetic training. This is a clean experimental design that directly supports the paper's core claim about the importance of training data distribution.

- **Embeddings reproduce qualitative patterns from behavioral economics.** The 1D MDS projection of embeddings for probabilities, values, and discount factors recovers key qualitative signatures of human decision-making: an inverse-S probability weighting function (γ=0.58), utility curvature (concave for gains, convex for losses), and hyperbolic-like time discounting (k=0.08). These patterns are non-trivial — they are not guaranteed by simple monotone encoding of numeric inputs.

- **Meaningfully outperforms classical behavioral models.** Arithmetic-GPT (ecological) achieves substantially higher adjusted R² than CPT (e.g., 70.8% vs. 51.5% on choice13k) and the hyperbolic discounting model (67.8% vs. 53.4% on gershman20), demonstrating that a simple rational-arithmetic pretraining objective can capture more variance in human choice than the best-known psychological theories.

- **Addresses a key obstacle for LLMs as cognitive models.** By using a small, publicly controllable training setup with disclosed synthetic data and no RLHF/alignment, the paper sidesteps the data contamination and opacity issues that plague off-the-shelf LLMs. This is a principled methodological contribution to the cognitive-AI community.

## Weaknesses

### Fatal
None.

### Major

- **Missing baseline: logistic regression on raw arithmetic features.** The paper's central empirical claim is that *embeddings* from an arithmetic-pretrained LLM are especially effective at predicting human choices. The obvious control is to skip the LLM entirely and feed raw EV_A, EV_B, and EV_A−EV_B (plus polynomial/interaction terms) directly into the same logistic regression framework. If these raw features achieve comparable R², the conclusion that pretraining induces *human-like representations* collapses — the logistic regression may simply be learning a mapping from correct arithmetic values to choices. This baseline is absent and is necessary to interpret the results. The paper shows that the ecologically trained model beats the uniform-trained model, which is meaningful, but without the raw-feature control we cannot tell whether even the ecological advantage is about representation quality or about encoding more useful arithmetic values.

- **Overfitting risk in the logistic regression with no cross-validation.** The logistic regression uses 960 features (three 320-dim embeddings: e_A, e_B, e_{A−B}) on datasets as small as 270 problems (cpc18). Adjusted R² does penalize the number of predictors, but with p >> n, the standard adjusted R² formula breaks down and cannot be relied upon as a safeguard against overfitting. The untrained model's non-trivial R² values (28.4% on cpc18, 21.1% on agrawal23) suggest that even random embeddings capture variance through the high-capacity regression layer, raising questions about how much of the trained models' performance reflects genuine structure vs. overfitting. No k-fold cross-validation, held-out sets, or regularization details are reported. This uncertainty affects all conclusions drawn from Table 1.

### Minor

- **Overstated comparison with LLaMA-3-70B.** The paper states that Arithmetic-GPT "also outperforms the embeddings obtained from the LLaMA-3-70b-Instruct model." In fact, on the gershman20 dataset, LLaMA-3 arithmetic embeddings score 69.3% vs. Arithmetic-GPT ecological's 67.8%; on agrawal23, LLaMA-3 scores 96.0% vs. 95.5%. Arithmetic-GPT wins decisively on the risky-choice datasets (choice13k, cpc18) but not on intertemporal choice. The discussion more accurately says "in some cases, even surpass," but the results section's phrasing overclaims. This does not undermine the paper's ablation-based conclusions but misrepresents the head-to-head comparison.

- **α=0.42 does not "quantitatively match" the human range of 0.5–0.9.** The paper claims the implicit utility curvature parameters "quantitatively match those observed in humans," yet the best-fitting α=0.42 is well below the cited human range of α∈[0.5,0.9] from Tversky & Kahneman (1992). The loss aversion parameter λ=1.4 is also notably lower than the typical human λ≈2.25. While the qualitative shapes are correct, the "quantitative match" claim is too strong. The paper's own acknowledgment of discontinuities partially mitigates this, but the parameter discrepancy deserves explicit discussion.

- **The hypothesized computational-errors mechanism is untested.** The paper motivates the work with the hypothesis that human deviations from rationality arise from computational errors during EV/PV calculation. However, it never reports the model's arithmetic accuracy, error patterns, or whether errors correlate with human biases (e.g., whether the model systematically overestimates EV for gambles that humans overvalue). The paper's core empirical contribution (embeddings → choices) does not depend on this mechanism, but the narrative framing implies a causal link that is neither tested nor supported by the current experiments.

- **Underspecified procedure for extracting single-probability/value/discount embedding curves.** The paper extracts embeddings for single probabilities (0.0–1.0), values (−300 to +300), and discount factors (0.99^0–0.99^30), then applies 1D MDS. However, it does not specify the input format used for these single inputs — e.g., whether a probability of 0.5 is fed as a complete equation like "0.5*1=+0.5" or as a lone token, nor which layer position's embedding is taken. This limits reproducibility of Figure 3.

### Trivial

- Table 1 reports R² values as point estimates without confidence intervals or error bars. Given the datasets have varying numbers of participants and problems, some measure of uncertainty would strengthen the comparison.

## Nice-to-Haves

- **Test a simple logistic regression on raw EV/PV features** as a baseline to disentangle the contribution of the embeddings from the information they encode.
- **Report cross-validated (e.g., 5-fold or leave-one-out) R²** for the logistic regression on all models in Table 1.
- **Sensitivity analysis for the fixed annual discount factor d_year=0.85** — show how results change for d ∈ {0.8, 0.9, 0.95}.
- **PCA/compression analysis** — reduce the 960 embedding features to a lower dimension (e.g., 10 or 20 PC scores) and re-run the logistic regression to see if predictive power lives in a low-dimensional arithmetic signal.

## Removed Points

These points were identified by the reviewers but are removed or weakened per the review guidelines. Treat with caution.

- **"Any monotone encoding would produce similar 1D curves" (from Harsh Critic point #4).** This is incorrect for the probability weighting function. The inverse-S shape (concave near 0, convex near 1) is characteristic of human probability weighting and is not produced by generic linear or monotonic encoding. The reviewer's demand for a control (e.g., comparing to a model trained on random arithmetic) is reasonable, but the specific claim about triviality of the embedding curves is not supported.

- **Criticisms about the <AMB> token usage and context length of 26 being insufficient.** These are implementation details that are adequately described for the paper's scope. The paper states that 10% of probability values are masked with `<AMB>` and the model learns to predict through this; the context length of 26 tokens is validated by the successful training convergence.

- **Criticism that "the ablation randomizes signs rather than simply removing answers."** The reviewer characterizes this as a different task. However, the paper's ablation is intentionally aggressive — it removes the correct sign information — which is a legitimate and interpretable control. The ablation's purpose is to test whether correct answer supervision matters, and randomizing signs achieves this cleanly.

- **Criticism about the MLP overfitting (97.8% on cpc18).** The paper explicitly notes that "MLP training was based on task features rather than text descriptions" and that the comparison is not apples-to-apples. The MLP is included as a ceiling estimate, not a direct competitor. The reviewer's concern is noted in the paper.

- **Criticism about the specific value of d_year=0.85.** This is a reasonable modeling choice. A sensitivity analysis would strengthen the paper but the fixed value is not a flaw.

- **Criticism about missing training curves/validation loss.** The paper states training stopped at validation loss plateau (checked every 100 epochs), which is standard practice for small-scale experiments.

- **Formatting/style nitpicks, parser-level formatting artifacts, and missing appendix/references comments** from the section-by-section notes. These reflect parser stripping or are outside the paper's substantive evaluation.

## Novel Insights

The most interesting insight from this review is the tension between the paper's clean ablation design and the fragility of its main result. The four-condition comparison (uniform/ecological × with/without answers) is a genuine strength — it provides an internally controlled test of the hypothesis that ecological data distributions matter. However, the reliance on a high-dimensional logistic regression (960 features) on small datasets (n=270–13k) without cross-validation or a raw-feature baseline means that the reported R² values could be substantially inflated by overfitting. The paper's strongest evidence is not the absolute R² values but the *relative ordering* across conditions (ecological > uniform > ablated variants) — this pattern is robust to overfitting because overfitting would affect all conditions similarly. But even this ordering is only interpretable if the logistic regression's capacity does not interact differently with different embedding qualities, which remains an open question. The community would benefit most from a version of this paper that adds cross-validation and the raw-arithmetic baseline, which would either shore up the claims decisively or reveal that the embeddings contribute little beyond arithmetic values.

## Suggestions

1. **Add logistic regression on raw EV/PV features** as a new row in Table 1. Use the same regression framework (linear or logistic on EV_A, EV_B, EV_A−EV_B, optionally with squared terms). If this baseline achieves R² comparable to the embedding-based models, the paper's claims need significant revision. If not, it would be the strongest possible evidence that the embeddings contribute something beyond correct arithmetic.

2. **Report cross-validated R² for all models** — e.g., 5-fold or leave-one-problem-out. This would address the overfitting concern directly and would be especially valuable for cpc18 (n=270) and choice13k.

3. **Clarify the input format and extraction procedure** for the single-input embeddings (probabilities, values, discount factors) to ensure Figure 3 is reproducible.

4. **Explicitly discuss the α and λ discrepancies** between the model's best-fitting parameters and known human ranges, rather than claiming "quantitative match." The qualitative correspondence is still a noteworthy finding.

5. **Weaken the LLaMA-3 comparison language** to accurately reflect the mixed results across datasets.

## Score and Decision

The paper tackles an important problem with a clean, principled design. The ablation experiments are the paper's strongest contribution, providing clear evidence that ecological training data distributions matter for producing human-like embeddings. However, two major methodological gaps — the missing raw-feature baseline and the absence of cross-validation — prevent the paper from fully supporting its central claims in its current form. The paper would be significantly strengthened by addressing these issues; with those additions it could be a solid contribution. In its current form, the evidence is suggestive but not fully convincing.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>