- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 1, 5, 1
Here is my consolidated review.

---

## Summary

This paper addresses LLM self-contradiction across dialogue turns when users provide questioning feedback (e.g., "I think your answer is incorrect"). The authors propose CC-SFT, a fine-tuning method that adds a Wasserstein-distance-based consistency loss between first-round and second-round responses to standard cross-entropy losses. Experiments on three datasets (OpenBookQA, GSM8K, MedQA-USMLE) with three models (Llama v3.1 8B, Mistral 7B, Gemma 9B) show reduced flipping rates compared to standard SFT. A theoretical convergence analysis is also provided.

---

## Strengths

- **Formal metrics for conversational inconsistency.** The paper introduces flipping rates (OFR, CFR, iCFR) in Section 3 to quantify inconsistency across two dialogue turns. These are consistently applied across all experiments (Table 1) and provide a concrete framework beyond qualitative descriptions.
- **Novel loss formulation with clear motivation.** The CC-SFT loss (Equations 1–4) explicitly penalizes semantic divergence between two-round responses via Wasserstein distance, justified by its ability to handle non-overlapping token distributions. The ablation on λ (Figure 2) demonstrates the causal effect: OFR drops from ~0.17 (λ=0, standard SFT) to ~0.03 (λ=0.1).
- **Broad evaluation scope.** Experiments cover three diverse datasets (scientific QA, math reasoning, medical QA) and three different base LLMs (Llama v3.1, Mistral, Gemma), lending support to generality.
- **Confusion-matrix analysis.** Figure 3 provides per-class evidence on MedQA-USMLE, showing CC-SFT eliminates NaN responses and reduces second-round misclassifications compared to SFT.

---

## Weaknesses

### Major

- **Two-turn evaluation protocol is underspecified.** The paper never describes how the second conversational turn is constructed for any of the three datasets. Key missing details: (1) the exact prompt template or format of the questioning feedback (e.g., is "I think your answer is incorrect" always used verbatim, or adapted per dataset?), (2) whether the feedback is appended as a separate user utterance or concatenated with the original question, (3) how the model is conditioned on conversation history at evaluation time when ground-truth answer A is unavailable. The second-round loss definition (line 83) conditions on "Q1, R1, Q2, r_2,<t, A" — but during evaluation A is unknown, so the generation setup is different from the training setup. This gap makes the reported metrics (OFR, CFR, iCFR) difficult to interpret and the work irreproducible without guessing the protocol.

- **Pre-trained encoder E for Wasserstein distance is not identified.** The method (line 89) uses "a pre-trained encoder E" to embed responses into token representations for the Wasserstein distance. The paper never specifies what E is — Sentence-BERT? A frozen layer of the LLM itself? A separately trained model? This choice critically determines what "semantic distance" means. The observed results could be highly sensitive to this unspecified design decision, and the method cannot be reproduced without it.

- **Baseline SFT training condition is ambiguous.** The paper's description of SFT (line 144: "the ground-truth is a copy of the input sequence shifted by one position to the right") describes standard single-turn causal language modeling. Yet CC-SFT is trained on two-turn data (both R1 and R2). If SFT is trained only on single-turn data, the comparison is confounded by data availability — CC-SFT sees strictly more training examples. If SFT is also trained on two-turn data (without the consistency loss), this must be stated explicitly. The paper's "SFT" condition is underspecified, and the reported improvements are uninterpretable without this clarification.

- **Factual error in results description for MedQA-USMLE.** Line 150 claims CC-SFT models exhibit "smaller accuracy drops between rounds" on MedQA-USMLE. The reported numbers contradict this for 2 out of 3 models:
  - Mistral AI: CC-SFT Δ = -0.065 vs SFT Δ = -0.051 (CC-SFT drop is *larger*)
  - Gemma: CC-SFT Δ = -0.020 vs SFT Δ = -0.007 (CC-SFT drop is *larger*)
  Only Llama v3.1 (-0.011 vs -0.028) supports the claim. While OFR improvements on MedQA are consistent across all three models, this specific accuracy-drop claim is overstated and factually wrong as written.

- **Convergence analysis is a generic textbook result disconnected from the actual setting.** Theorem 1 proves O(1/T) convergence of SGD under Assumptions 1–4 (strong convexity, Lipschitz gradients, unbiased gradients, bounded variance). These assumptions do not hold for the proposed loss (cross-entropy on a neural network + Wasserstein distance is non-convex). The analysis contributes no insight specific to CC-SFT and is misleading as theoretical support — it is a standard SGD convergence proof for strongly convex objectives applied to a setting where the core assumption (Assumption 1) is violated.

### Minor

- **Results are reported as point estimates without variance.** All numbers in Table 1 and Figure 2 are single-run point estimates with no error bars, confidence intervals, or mention of multiple seeds. Given the modest differences in some comparisons (e.g., second-round accuracy changes of 1–2 percentage points), it is unclear which improvements are statistically reliable. (This is noted as a limitation rather than a fatal flaw, since single-run evaluation is common in LLM fine-tuning papers.)

- **λ analysis shown for only one model–dataset pair.** Figure 2's hyperparameter sweep (λ from 0 to 1.0) is only for Llama v3.1 on OpenBookQA. While informative, this limits the generality of the recommended λ=0.1 setting.

- **No comparison to any alternative consistency method.** The paper only compares against standard SFT and the pre-trained model. No comparison to related approaches such as contrastive consistency learning, self-consistency decoding, or DPO-style alignment, which would help calibrate the value of the specific Wasserstein-based approach.

### Trivial

- Line 25: "dataseets" → "datasets"
- The paper uses "CC-SFT" but the consistency loss abbreviation in Equation (4) uses λ both as the loss coefficient (Equation 1) and as the Sinkhorn regularization parameter (Equation 5) — minor notational collision.

---

## Nice-to-Haves

- A human evaluation or qualitative comparison showing example CC-SFT vs. SFT responses would strengthen the claim that the method genuinely improves consistency rather than simply making the model "stubborn" (always repeating the first answer).
- Discussion of computational overhead: computing Wasserstein distance between token embedding distributions per training example has non-trivial cost vs. standard SFT. Training time or memory comparison would help practitioners assess the trade-off.
- Extending the λ analysis to at least one additional model–dataset pair would strengthen the generality of the recommended λ=0.1.

---

## Removed Points

- **"The evaluation protocol is entirely unspecified"** (Harsh Critic): Demoted from "entirely unspecified" to "underspecified." The paper does specify Q2 includes questioning feedback and the question (line 77), the example feedback "I think your answer is incorrect" (line 49), and that the model conditions on the full conversation history (line 83). The protocol is partially described but the template details needed for reproducibility are missing. The paper would be substantially improved by adding the specific prompts/templates used.
- **"Convergence analysis should be removed entirely"** (Harsh Critic): Retained as Major weakness but softened. The analysis is a generic textbook result under unrealistic assumptions, but many ML papers include such idealized convergence proofs. The issue is that it's presented as validation of CC-SFT specifically, which is misleading. The analysis should be caveated as applying only under strong convexity assumptions that do not hold, or replaced with a discussion acknowledging the non-convex setting.
- **"No human evaluation or qualitative analysis"** (Harsh Critic): Moved to Nice-to-Haves. Not a core requirement for an empirical methods paper with quantitative metrics.
- **Strength Finder's convergence claim ("rare in consistency-training papers")**: Removed. The convergence result is a standard textbook SGD proof with no connection to the specifics of the proposed loss or architecture. It does not constitute a genuine strength of the paper.
- **"Related work on adversarial attacks is poorly connected"**: Removed — the paper uses adversarial attack literature to distinguish its setting, which is a reasonable framing choice.
- **All formatting/typo criticisms**: Removed per instructions (parser artifacts).

---

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the core assessment that the method is sensible and the problem is important, but the experimental specification is too incomplete to validate the claimed results.

---

## Suggestions

1. **Specify the two-turn prompt template explicitly.** Provide the exact text format used for constructing Q2 for each dataset. Show at least one full worked example (question → R1 → questioning feedback → R2) for each dataset type (multiple-choice and math word problems). Clarify whether the model is given the ground-truth answer A during evaluation or only during training.

2. **Name the pre-trained encoder.** State exactly which model or layer is used to obtain embeddings for the Wasserstein distance. If it is the LLM's own hidden states, specify which layer. If a separate encoder, report which one and justify why. Consider ablating different encoders.

3. **Clarify the SFT training data.** State explicitly: was SFT trained on (a) the same two-turn examples as CC-SFT but without the consistency loss (i.e., L1 + L2 only), or (b) single-turn data only? If (b), the comparison is confounded by data volume and should be re-run under fair conditions.

4. **Fix the MedQA-USMLE factual error.** Correct the claim about "smaller accuracy drops" for Mistral and Gemma, or clarify that the statement refers to a different metric (e.g., OFR, which does improve for all models).

5. **Add variance information.** Report results from at least 2–3 random seeds or provide confidence intervals for the main Table 1 comparisons.

6. **Caveat the convergence analysis.** Acknowledge that Assumption 1 (strong convexity) does not hold for the actual loss function, and reframe the analysis as an optional idealized guarantee rather than a central theoretical pillar.

---
