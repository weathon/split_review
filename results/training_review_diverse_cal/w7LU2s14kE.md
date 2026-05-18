Now I have verified all the claims against the paper. Let me synthesize the final review.

---

## Summary

This paper investigates whether transformer LMs decode relational knowledge (e.g., *plays the instrument*, *is located in*) via a linear transformation on subject representations. The authors derive **Linear Relational Embeddings (LREs)** directly from the LM's Jacobian via a first-order Taylor expansion, and validate them through (a) *faithfulness* — whether LRE-predicted objects match the LM's own predictions on held-out subjects — and (b) *causality* — whether inverting the LRE to edit subject representations successfully changes the LM's output object. Across GPT-J, GPT-2-XL, and LLaMA-13B on >10k facts spanning 47 relations, the paper finds that for ~48% of relations the decoding is well-approximated by a linear map, while other relations (e.g., Company CEO) are not linearly decodable despite being accurately predicted. An **attribute lens** application demonstrates that LREs can reveal correct relational knowledge even when the LM outputs falsehoods under adversarial prompts.

## Strengths

- **Principled derivation of linear relation maps from the LM's own gradients.** Rather than training a probing classifier, the paper extracts LREs directly from the model Jacobian (Eqs. 2–4), establishing that a first-order Taylor expansion of the LM's decoding computation yields a faithful affine map for many relations. This avoids the usual worry that a probe might learn the task on its own rather than reading out what the LM represents.

- **Joint faithfulness and causality evidence across multiple LMs and relation categories.** Using GPT-J, GPT-2-XL, and LLaMA-13B on 47 relations spanning factual, commonsense, linguistic, and bias knowledge (Table 1), the paper shows that LREs achieve >60% faithfulness for ~48% of relations (Figure 2), and that causal edits via LRE inversion match an oracle upper bound while outperforming naive baselines (Figure 4). This dual validation — that LREs both *describe* and *control* the LM's behavior — is the paper's strongest evidence that the extracted maps reflect the actual decoding procedure.

- **The attribute lens reveals latent knowledge under adversarial conditions.** On 11,891 "repetition distracted" and "instruction distracted" prompts where the LM is baited into outputting a falsehood, the attribute lens (decoding $D(\text{LRE}(\mathbf{h}))$ instead of $D(\mathbf{h})$) recovers the correct object in the top-3 predictions (Table 2). This demonstrates a concrete downstream use of the discovered linear structure and provides evidence that correct relational knowledge can be present in intermediate representations even when it does not reach the final output.

- **Honest characterization of failure cases.** The paper identifies relations (e.g., Company CEO, <6% faithfulness) that the LM predicts accurately but whose decoding is not linearly approximated. The discussion of why such relations might fail (large object ranges, person/company names) delimits the scope of the claim and prevents overgeneralization.

- **Observation of a "mode switch" in later layers.** Figure 6 shows that faithfulness for some relations drops sharply after layer ~17, and that removing relational context from the prompt prevents this drop. This observation provides insight into how transformer representations may transition from encoding entity attributes to optimizing next-token prediction.

## Weaknesses

### Fatal

None.

### Major

1. **No uncertainty quantification for the central quantitative claims.** Faithfulness and causality results are reported as averages over 24 random draws of the 8 training examples, but the paper provides *no confidence intervals, error bars, or variance measures* anywhere in the main text. The reader cannot assess whether the 48% figure (relations with "robust LREs") is stable across different samples, nor whether differences between relations (e.g., 40% vs. 60% faithfulness) are reliable. This is especially concerning because the LRE estimate depends on a small set of examples (n=8) and a global hyperparameter β. *Why it matters:* The paper's core empirical finding — that a subset of relations are linearly decodable — hinges on these numbers, and without variance estimates the reader cannot evaluate their reliability.

### Minor

2. **Coarse evaluation metrics conflate multiple failure modes.** Faithfulness and causality are measured as exact match of the argmax token (first token of the object). An LRE that places the correct object in second position with high probability is scored as a failure, while one that barely edges out a distractor counts as success. The paper acknowledges this limitation (line 149, deferred to §Limitations in the appendix), but the current analysis would benefit from complementary continuous measures (e.g., rank of the correct object, KL divergence from the model distribution) to distinguish "LRE always gets it" from "LRE gets it when the model does."

3. **The scalar β weakens the "purely derived" framing.** The paper derives LRE from a first-order Taylor expansion, then multiplies W by an *ad hoc* scalar β > 1 to correct for magnitude underestimation caused by layer normalization (line 102–109). While the paper provides a theoretical rationale (layer normalization attenuates scale) and defers empirical measurements to the appendix, β is selected via grid-search (line 172) — making it effectively a per-LM hyperparameter rather than a derived quantity. This does not invalidate the results, but it slightly undercuts the claim that the LRE is a *principled linearization* rather than a gradient-informed probe with a tunable scale factor. A sensitivity analysis (faithfulness vs. β for a few relations) or a first-principles derivation from the layer norm formula would strengthen the presentation.

4. **Baseline comparisons are asymmetric in information available.** The paper compares LRE against linear regression trained on the *same 8 examples*. Since LRE has access to the full model Jacobian (effectively the gradient of the entire decoding computation), it has far more information per example than the regression baseline. A fairer comparison would be (a) training linear regression on all available examples per relation to measure the inherent linearity of the mapping from data alone, or (b) ablating the gradient information from LRE (e.g., using a random matrix). The existing comparison shows that Wikipedia-level knowledge can be extracted from gradients, but does not cleanly separate "the mapping is linear" from "the Jacobian contains useful information."

5. **The "robust LRE" threshold is not explicitly justified.** The paper states that "in 48% of the relations we tested, we find robust LREs" (line 36) and that the method "achieves over 60% faithfulness for almost half of the relations" (line 178). The implicit threshold (faithfulness > 60%) is reasonable but is never stated as a formal criterion; the reader must infer it from the text. The choice of threshold should be stated and briefly justified.

6. **The mode-switch hypothesis rests on limited evidence.** The paper shows one example relation where faithfulness drops at later layers and demonstrates that removing relational context prevents the drop (Figure 6). Similar plots for other relations are deferred to the appendix. While the hypothesis (representation transition from attribute-encoding to next-token prediction) is plausible, the evidence presented in the main paper is insufficient to establish it as a general phenomenon. A more systematic analysis (tracking faithfulness across layers for all relations, or correlating the drop with object entropy) would strengthen this claim.

### Trivial

None.

## Nice-to-Haves

- **Analysis of which relation properties predict linearity.** The paper notes that relations with large object ranges (e.g., Company CEO) fail. A systematic analysis plotting faithfulness against object range size, average object rank in LM logits, or the layer at which subject representations are most relation-relevant would turn the 48%/52% split from an observation into an explanation.
- **Sensitivity analysis for β.** A plot of faithfulness as a function of β for 2–3 representative relations, along with the chosen β values for each LM, would clarify the robustness of this hyperparameter choice.
- **Analysis of the low-rank pseudoinverse.** The paper uses a low-rank inverse for causal edits (line 142) but never reports what rank is selected per relation or how edit performance depends on rank. This is relevant for understanding the causality results.
- **Cross-prompt transfer of LREs.** Do LREs estimated from one prompt format (e.g., with few-shot examples) transfer to other prompt formats for the same relation? This would speak to the generality of the finding.
- **Controlled baseline for attribute lens evaluation.** Comparing to a trained linear probe or the logit lens on the same falsehood-detection task would better isolate the added value of the attribute lens.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that β makes LRE "a form of linear probe training with model-gradient features, not a derived linearization."** This overstates the case. The paper provides a clear theoretical rationale for β (layer normalization attenuates scale, line 102) and the core W matrix remains derived from the Jacobian. The characterization as "probe training" is inaccurate.
- **Harsh critic's suggestion that causality scores exceeding faithfulness might be due to "large-magnitude noise" from the pseudoinverse.** The paper explicitly discusses why causality exceeds faithfulness (lines 204–205: the linear approximation is strong enough to edit even when not perfectly faithful). The noise-injection hypothesis is speculative and unsupported. Moved to Nice-to-Haves as a possible check.
- **Strength Finder's claim that "scalar correction β accounts for layer-normalization effects" as a clear strength.** Conflicts with verified weakness #3 (β is ad hoc). The paper does tie β to layer normalization, but the lack of a full derivation or sensitivity analysis makes this at best a partial strength.
- **Harsh critic's request for "explicit threshold for robust LRE."** Kept as weakness #5 in the Minor section, but reframed from "missing part" to a lack of explicit justification.

## Novel Insights

Beyond the paper's own contributions, the most interesting synthesis from the reviews is the tension between two interpretations of the method: is LRE a *derived linearization* of the model's computation (as claimed), or a *gradient-informed linear probe* with post-hoc scaling? The paper leans strongly toward the former, but the β hyperparameter and the absence of an ablation that controls for the information advantage of gradients (compare: LRE vs. gradient on random directions) leave the door open to the latter interpretation. A clean experiment that resolves this — showing that the Jacobian's *specific* structure (not just its information content) is what enables the linear approximation — would significantly strengthen the paper's core claim.

## Suggestions

1. Add confidence intervals or standard deviations to all averaged results (faithfulness per relation, causality per relation, aggregate 48% figure) — this is the most impactful fix.
2. Explicitly state and briefly justify the "robust LRE" threshold (faithfulness > 60%).
3. Add a sensitivity analysis for β in the main paper (faithfulness vs. β for 2–3 representative relations).
4. Complement the argmax-based metrics with a continuous measure (e.g., rank of correct object) and show that the main conclusions are consistent.
5. Expand the linear regression baseline: train on all available examples per relation (not just 8) to better measure the inherent linearity of the mapping.
6. Present mode-switch evidence more systematically in the main paper, or reduce the strength of the claim.

## Score and Decision

This paper makes a genuine and well-motivated contribution. The idea of extracting linear relation maps from the model Jacobian is novel, and the joint faithfulness + causality evidence is stronger than what most probing studies provide. The weaknesses — particularly the lack of uncertainty quantification and the somewhat ad hoc β — are real but addressable in revision. No weakness is fatal or undermines the core claim. I recommend acceptance conditional on the authors adding error bars/confidence intervals to all quantitative results, providing a sensitivity analysis for β, and clarifying the "robust LRE" threshold.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>