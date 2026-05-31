## Summary

This paper proposes CENTaUR, a cognitive model formed by finetuning a linear layer on top of LLaMA-65B embeddings to predict human choices in decision-making experiments. The model is evaluated on two established behavioral paradigms — decisions from description (choices13k) and decisions from experience (horizon task) — and on one hold-out generalization task (experiential-symbolic choice). CENTaUR achieves lower negative log-likelihoods than two domain-specific cognitive models (BEAST and a hybrid exploration/exploitation model), reproduces qualitative human choice patterns, captures individual differences via random effects, and shows some transfer to a held-out task.

## Strengths

1. **Outperforms established domain-specific cognitive models on held-out predictive accuracy.** On choices13k, CENTaUR achieves NLL = 48002.3 vs. BEAST's 49448.1; on the horizon task, NLL = 25968.6 vs. the hybrid model's 29042.5 (Fig. 1c, 1e). These are non-trivial improvements over models that represent the current standard in these domains.

2. **Reproduces qualitative human choice patterns that the raw LLM lacks.** In the horizon task, CENTaUR recovers both the equal-information horizon effect (more random choices with longer horizon) and the unequal-information information-seeking effect (more selection of the informative option with longer horizon), whereas LLaMA without finetuning shows neither pattern (Fig. 2c–h). This goes beyond aggregate fit to behavioral fidelity.

3. **Models individual participant behavior with random effects.** When including participant-level random effects on embedding dimensions, CENTaUR improves NLL from 25968.6 to 23929.5 and still outperforms the hybrid model with the same random-effects structure (NLL = 24166.0). Model selection assigns CENTaUR a protected exceedance probability near 1 (Fig. 3).

4. **Demonstrates generalization to a hold-out task after multi-task finetuning.** A model finetuned jointly on both training tasks predicts human choices on the experiential-symbolic task (NLL 4521.1 vs. chance-level 5977.7 and raw LLaMA 6307.9) and captures the human tendency to overvalue description-based options — a bias raw LLaMA does not show (Fig. 4).

## Weaknesses

### Fatal
None.

### Major

1. **Capacity mismatch undermines the headline "beats" claim.** CENTaUR fits an ~8192-dim linear model on top of LLaMA-65B embeddings (regularized via nested CV), while the baselines — BEAST and the hybrid model — have ~3–5 interpretable parameters each. The paper claims these models are "beaten" and that CENTaUR achieves "state-of-the-art results," but the comparison is asymmetric by construction. A model with far greater capacity will almost always achieve better log-likelihood on a sufficiently large dataset, even if the embeddings themselves contribute nothing specific. The paper does not provide baselines that control for capacity — e.g., random forests or MLPs trained on raw trial features (outcome values, probabilities, counts), or a linear probe on random embeddings of the same dimension — so the reader cannot tell whether the improvement stems from the LLaMA pretraining specifically or simply from the use of a high-dimensional representation with regularization. This does not invalidate the paper's contribution, but it does mean the central claim needs recalibration: the contribution is better described as "LLM embeddings + linear probe predict human choices well" rather than "LLMs beat domain-specific cognitive models."

2. **Overclaiming on generality from a single hold-out task.** The generalization experiment tests only one hold-out task (experiential-symbolic), which combines description-based and experience-based information — both present in the two training tasks. This is a relatively easy transfer. The paper frames this as progress toward a "domain-general model of human cognition," but that claim is not supported by one closely related transfer experiment. Moreover, no comparison is made against a model finetuned on only one of the two training tasks, so the source of the transfer benefit (shared embedding space vs. simply more training data) is not isolable.

### Minor

3. **No qualitative comparison of choice curves against the domain-specific model.** The choice-curve analysis (Fig. 2g,h) shows CENTaUR vs. humans, but not the hybrid model, which was explicitly designed to capture these exploration patterns. Showing that CENTaUR reproduces patterns that the domain-specific model likely also reproduces does not demonstrate that CENTaUR generalizes beyond traditional models. A side-by-side qualitative comparison is needed to substantiate the claim that finetuned LLMs capture behavior that domain-specific models miss.

4. **Lack of ablation studies isolating the source of improvement.** The paper uses LLaMA-65B throughout, but does not test: (a) smaller LLaMA versions (7B, 13B, 33B) to study how performance scales with model size, (b) random embeddings of the same dimension to verify that the LLaMA pretraining contributes beyond high dimensionality, or (c) a model trained on raw task features (e.g., outcome probabilities and values) with the same linear-probe setup. These ablations would substantially strengthen the evidence that *LLM-specific* pretraining, rather than generic high-dimensional representations, is what drives the results.

5. **No uncertainty quantification for the key behavioral comparisons.** The regret comparisons report standard errors but no significance tests or confidence intervals for the CENTaUR–human difference (e.g., 1.35 vs. 1.24 for choices13k; 2.38 vs. 2.33 for the horizon task). The differences are small, and without uncertainty quantification, the claim that CENTaUR "matches human regret more closely" than alternatives is qualitative.

### Trivial

6. **Data contamination not discussed.** The paper does not address the possibility that LLaMA's pretraining corpus contains published behavioral data that could leak into the embeddings. While this is speculative and hard to verify, a brief discussion would improve the paper's rigor.

## Nice-to-Haves

- Comparing against similarly flexible models trained on raw task features (random forest, MLP on raw trial variables) to isolate the value of the LLaMA embedding space.
- Testing with random embeddings of the same dimension as a control.
- Including the domain-specific model's choice curves alongside CENTaUR's and humans' in the qualitative analysis.
- Reporting the effective degrees of freedom of the regularized CENTaUR model.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Embedding extraction under-specified (which token position).** The harsh critic notes the paper says "hidden activations of the final layer" without specifying which token position is used. The Materials and Methods section (stripped by the parser, exists in the original submission) likely contains this detail. Removed per rule: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references."
- **Number of parameters not reported.** The harsh critic asks for the number of parameters and effective degrees of freedom. This is a minor implementation detail that readers can infer from LLaMA-65B's architecture. Removed per rule: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details."
- **Criticism about missing statistics for individual-differences model selection.** The paper reports protected exceedance probability (close to 1), which is the standard Bayesian model selection metric in this literature. The criticism misunderstands what evidence is presented. Removed as factually incorrect.
- **Demand for the paper to do Y outside its stated scope.** Several criticisms ask the paper to solve problems outside its scope (full domain-general cognitive model, exhaustive task coverage). The paper explicitly frames its generalization result as preliminary. Removed per soft rule on scope creep.
- **Criticism about fairness of comparison with BEAST and hybrid model favoring the baseline.** No — the criticism is about asymmetry favoring CENTaUR, not the baseline. This is retained as Weakness #1 (Major) because it's a substantiated concern about the paper's central claim, not a side complaint about baselines being favored.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the hybrid model's choice curves should be shown alongside CENTaUR's is a useful methodological point but not a novel insight. The strength finder's cataloging is accurate but does not surface anything beyond what the paper itself states.

## Suggestions

1. **Recalibrate the central claim.** Replace "beats domain-specific models" with language like "LLM embeddings + linear probe achieve competitive or superior predictive accuracy relative to established cognitive models" and explicitly acknowledge the capacity difference. This would be more precise and defensible.

2. **Add a raw-features baseline.** Train a regularized linear model (same logistic regression pipeline) on the raw trial features available to participants (outcome values, probabilities, counts, horizon length). If CENTaUR still wins, the LLaMA embedding space is genuinely adding value beyond what task features alone provide.

3. **Add a random-embedding ablation.** Replace the LLaMA embedding with a fixed random projection of the same dimension (or a smaller pre-trained model's embeddings). This directly tests whether the specific LLaMA pretraining matters.

4. **Include the hybrid model's choice curves** in the qualitative analysis (Fig. 2). If the hybrid model already captures the horizon effects, the paper should say so and then argue that CENTaUR matches this *while also* generalizing to new tasks — which is the real novelty.

5. **Explicitly label the generalization result as preliminary** and avoid the phrase "domain-general model of human cognition" until more tasks are tested.

---

## Score and Decision

**Calibration results:**

| Paper | Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|---|
| Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice | Tn8EQIFIMQ.md | 7.00 | Bracketing (R1), Narrowing (R2) | Most directly comparable: also uses LLMs as cognitive models for human decision-making, similar concerns about comparison fairness. This paper is slightly weaker due to the more pronounced capacity mismatch. |
| DeLLMa: Decision Making Under Uncertainty with LLMs | Acvo2RGSCy.md | 7.33 | Bracketing (R1), Narrowing (R2) | Less directly comparable (decision support, not cognitive modeling). Stronger experimental validation. This paper is weaker on empirical breadth. |
| Human Simulacra | BCP5nAHXqs.md | 5.60 | Narrowing (R2) | Lower relevance but same domain (LLMs + human behavior). This paper is clearly stronger — more focused, cleaner experiments, better quantitative results. |
| Do LLMs exhibit human-like response biases? | QQt0MwXA81.md | 6.20 | Narrowing (R2) | Related domain (human biases in LLMs). Similar quality but different scope. This paper has more direct contribution to cognitive modeling. |
| Rationality of Thought Improves Reasoning | kaGA40pfFY.md | 6.50 | Narrowing (R2) | Different focus (LLM reasoning, not cognitive modeling). Similar score tier. |
| Theory of LLM sampling | ejvf3JrZuC.md | 4.25 | Bracketing (R1) | This paper is substantially stronger — cleaner experiments, clearer contribution. |
| Large language models as windows on psychopathology | UXCfRU2Qs4.md | 4.25 | Bracketing (R1) | This paper is substantially stronger — more rigorous methodology, better supported claims. |

**Round 1 bracket:** 5–7  
**Round 2 narrowing:** Compared against Arithmetic-GPT (7.0, most similar), this paper is slightly weaker due to the capacity mismatch being more central to its primary claim and the approach being less novel (standard linear probe vs. training from scratch on a novel synthetic task). Compared against Human Simulacra (5.60), this paper is clearly stronger. The upper bound is set by DeLLMa (7.33), which has broader empirical validation.  
**Final placement:** 6.5 — solid paper with genuine contributions, held back by the structural comparison issue and overclaiming on generality.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>