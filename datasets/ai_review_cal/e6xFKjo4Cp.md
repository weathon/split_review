- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6
Now I have a thorough understanding of the paper and all reviewer inputs. Let me construct the final consolidated review.

---

## Final Consolidated Review

## Summary

This paper proposes the Iterative Contrastive Unlearning (ICU) framework for machine unlearning in generative language models, addressing the trade-off between forgetting sensitive information and preserving model capability. ICU combines three components: a Knowledge Unlearning Induction module (negated log-likelihood on forget data), a Contrastive Learning Enhancement module (pair learning and KL-divergence losses on analogous retrieved data), and an Iterative Unlearning Refinement module (dynamic exclusion of already-forgotten samples). Experiments on GPT-Neo models (125M, 1.3B, 2.7B) show that ICU substantially outperforms the aggressive KUMPR baseline on preservation metrics (perplexity, classification accuracy, dialogue F1) while still achieving meaningful reduction in extraction likelihood and memorization accuracy.

## Strengths

1. **Consistent evidence across model scales that ICU preserves capability during unlearning**: Table 1 shows that across all three model sizes, ICU achieves dramatically better preservation than KUMPR (e.g., PPL of 21.6 vs >10,000 on Pile for 125M) while still reducing EL from 51.9% (original) to 4.4%. This directly supports the paper's core claim of maintaining model expressiveness during unlearning. The pattern holds consistently at 1.3B and 2.7B.

2. **Ablation confirms both loss components contribute**: The paper reports (Figure 3, described in Section 4.3) that removing either the pair learning loss or the KL-divergence loss leads to worse downstream performance, providing evidence that the CLE module's design is not redundant. The KL-divergence loss is noted as having a more pronounced effect, which is informative.

3. **Parameter sensitivity analysis gives insight into the trade-off**: Table 2 systematically varies α and β across 10 configurations, demonstrating that the trade-off between unlearning and preservation is controllable, and validating the chosen settings. This is more thorough than many unlearning papers.

4. **Iterative refinement is a practical contribution**: The IUR module's dynamic exclusion of already-forgotten samples during training (using BERTScore and BLEU thresholds) is a clean mechanism to prevent over-unlearning that directly addresses a real problem in training-based unlearning.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **No statistical significance or variance reported**: Table 1 reports averages over 5 random runs but provides no standard deviations, confidence intervals, or significance tests. Given that improvements over KL/LLMU on some retention metrics are modest (e.g., Cls Avg 43.3 vs 42.6 for KL on 125M), the reader cannot assess whether these differences are reliable. This is the most significant weakness in the paper's experimental presentation.

2. **Modest gains over simpler retention-focused baselines**: Comparing ICU to the KL baseline (which uses only KL divergence without KNN or pair learning): for 125M, Cls Avg 43.3 vs 42.6, Dia Avg 10.3 vs 9.9, PPL 21.6 vs 27.0. While ICU consistently wins and the perplexity gap is notable, the classification and dialogue differences are small. The paper does not quantify the contribution of the KNN contrastive component versus simpler alternatives, leaving some ambiguity about which architectural choices drive the gains.

3. **BERTScore used both as stopping criterion and evaluation metric**: The IUR module (Section 3.5) uses BERTScore < 0.3 as a stopping criterion, and BERTScore is also reported in Table 1 as an evaluation metric for forgetting. This creates partial circularity for that specific metric. The paper's main unlearning claims appropriately rest on EL and MA (which are not circular), but the BERTScore column in Table 1 should be interpreted with this in mind. The paper partially acknowledges the concern (Section 4.2, lines 156-157) but does not fully address it.

4. **Missing implementation details that affect reproducibility**:
   - *Information Entropy*: Defined mathematically (Eq. 7) but never specified what distribution it is computed over (generated sequences? vocabulary logits?). The entropy values in Table 1 are not interpretable without this context.
   - *Analogous data construction*: The paper states documents are retrieved from "Wiki" belonging to the same category as the forget set (Section 3.4), but does not specify how categories are assigned to the Pile-based forget samples, or whether the forget set and analogous set overlap.
   - *K=1 justification*: Using a single nearest neighbor for the contrastive pair is stated but not justified or tested for sensitivity. A noisy embedding could pair a forget sample with a semantically distant document.

5. **Computational cost not discussed**: ICU trains for 21.4-32.6 epochs with per-epoch KNN retrieval and BERTScore/BLEU evaluation. The paper does not discuss the overhead of the KNN search or the iterative evaluation, which may be substantial for larger models or forget sets.

6. **Limitations not acknowledged**: The conclusion mentions only future work on multi-modal data. The paper does not discuss limitations such as reliance on Wikipedia for analogous data, the arbitrary threshold choice for forgetting, or the lack of any formal privacy guarantee.

### Trivial

- The claim "larger models have higher tendency to memorize" is supported by the 125M→1.3B jump (EL 51.9%→98.2%) but 2.7B (96.7%) is slightly below 1.3B, making the statement slightly overgeneralized without statistical testing.

## Nice-to-Haves

- **(Suggestion from Strengthening section)** Controlling for the level of forgetting across methods — e.g., training each baseline until it reaches a target EL/MA — would eliminate the confound of unequal forgetting levels and directly test whether ICU's retention benefit is genuine.
- **(Suggestion from Strengthening section)** A concrete extraction attack (e.g., generating completions from a given prefix and computing string overlap with the target) would strengthen the privacy claim beyond token-level metrics.
- An ablation that replaces KNN retrieval with random retrieval from the same category would clarify whether the specific contrastive pairing mechanism matters.
- Reporting whether the hyperparameters (α, β, a, b) transferred directly to larger models or required retuning.

## Removed Points

*These points were assessed against the paper and found to be overstated, factually incorrect, or based on speculation rather than the paper as written.*

- **"Unlearning not validated against actual privacy risk" (Critic's Claim 1)**: The paper uses Extraction Likelihood (EL) and Memorization Accuracy (MA) — the standard metrics from Jang et al. (KUMPR) — which are grounded in n-gram overlap extraction attacks. Claiming EL=4.4% means the model has "not forgotten" is not supported by the paper's framework, which measures relative reduction from the original 51.9%. The demand for a "separate extraction attack" beyond these established metrics is a reasonable suggestion but not a flaw in the presented evaluation.
- **"Circularity between stopping criterion and evaluation metric" (Critic's Claim 2, full framing)**: Overstated. EL and MA — the primary unlearning metrics in Table 1 — are NOT used as stopping criteria. The stopping criterion uses BERTScore and BLEU. Only the BERTScore column in Table 1 has partial circularity, which is acknowledged and handled separately above as a Minor weakness. The critic's framing that "the evaluation conflates the objective the method was designed to minimize with the evidence" is incorrect for the paper's main metrics.
- **"Unfair comparison due to unequal training compute" (Critic's Claim 3)**: More training epochs also mean more unlearning loss epochs on the forget data, which should *hurt* retention rather than help it. The net effect of additional epochs (more unlearning pressure + more preservation training) is ambiguous. The critic's implication that more epochs straightforwardly explains ICU's better retention is not logically sound without further analysis.
- **Figure 1 connection being "loose"**: The figure is illustrative of the problem (catastrophic forgetting with KUMPR), and a different concrete example is shown in the case study (Figure 4). This is not a substantive weakness.
- **"Category assignment not specified" (exaggerated framing)**: While the missing detail is a valid concern (kept as Minor #4), the critic's framing that this "undercut[s] the contrastive goal" is speculative without evidence.
- **Case study "omits the original GPT-Neo output"**: The paper explicitly states "Before unlearning, the original models (e.g., GPT-Neo and Opt) retain and reproduce this information" and Figure 4 illustrates this. The critic appears to have misread the description.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any unanticipated interpretation of the results or cross-connections to other work that the paper itself does not discuss.

## Suggestions

1. **Add standard deviations or confidence intervals** to Table 1 for all metrics across the 5 runs. This is the single most impactful improvement for establishing the reliability of the results.
2. **Clarify how Information Entropy is computed** — specify the random variable and distribution it is evaluated over.
3. **Provide details on the analogous data construction**: how are "categories" assigned to Pile samples? What is the overlap between the analogous Wiki set and the forget set?
4. **Report the computational overhead** of KNN retrieval and per-epoch evaluation, especially relative to simpler baselines.
5. **Acknowledge limitations** more explicitly in the paper: arbitrary thresholds, reliance on accessible analogous data sources, lack of formal privacy guarantees.
