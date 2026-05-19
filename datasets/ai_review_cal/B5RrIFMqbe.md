- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of both the paper and the reviews. Let me synthesize the final consolidated review.

## Summary

The paper introduces FormalAlign, a framework for automatically evaluating semantic alignment between natural-language (informal) mathematical statements and their corresponding formal-language (Lean 4) counterparts in autoformalization. The method fine-tunes an LLM with a dual loss combining cross-entropy (for autoformalization generation) and contrastive learning (for representational alignment), and at inference produces an alignment score via the average of a certainty score (generation probability) and a similarity score (cosine similarity between hidden states). Evaluated on four benchmarks augmented with six types of synthetic misalignments, FormalAlign outperforms zero-shot GPT-4 on the main alignment-selection metric, and a small human study shows it offers a dramatic speedup (2 minutes vs. ~3 hours for 80 items) at the cost of lower accuracy (65% vs. 79.58%).

## Strengths

1. **First dedicated framework for automated alignment evaluation in autoformalization.** The paper identifies a clear gap — existing methods (compilation checking, BLEU, BERTScore) fail to detect semantic misalignments like the example in Figure 1 where `80 * c = 63` is syntactically valid but semantically wrong — and proposes a purpose-built solution. FormalAlign correctly flags such cases, which no prior method designed for this task does. This is a genuine contribution to a problem of growing importance as autoformalization LLMs proliferate.

2. **Dual-loss training is demonstrably beneficial.** The ablation study (Table "loss", Sec. 5.3) directly compares CE-only, CL-only, and the combined loss. The combined loss achieves the best Alignment-Selection score on all four datasets (e.g., 99.21% on FormL-Basic vs. 98.60% with CE-only and 18.65% with CL-only). This provides clear evidence that both losses contribute and that their combination is justified.

3. **Systematic construction of misaligned evaluation data.** Six distinct misalignment strategies (constant modification, exponent modification, new variable, variable type change, equality/inequality swap, random pairing) are defined in Table 2 and applied to generate 21 negatives per positive example. This provides a principled, reproducible evaluation protocol that goes beyond simple random shuffling.

4. **Generalization across diverse base LLMs.** The method applied to Phi2-2.7B, LLaMA2-7B, DeepSeekMath-7B, and Mistral-7B (Sec. 5.2) yields competitive AS scores, especially on FormL datasets, showing the framework is not tied to a single architecture and works even with a much smaller model (Phi2).

5. **Ablation validates the combined inference score.** The ablation (Table "alignment", Sec. 5.4) shows that neither the certainty score nor the similarity score alone matches the combined \(\mathcal{V}_{\text{align}}\), confirming that both components contribute meaningfully.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is entirely on synthetic misalignments; no real autoformalization errors are tested.** The four test sets are augmented solely with hand-designed perturbations (constant changes, exponent changes, variable type changes, etc.). The paper never evaluates on actual outputs from an autoformalization system (e.g., GPT-4 generating Lean statements from NL theorems, then manually labeled for alignment). Real autoformalization errors may involve wrong variable bindings, missing hypotheses, incorrect quantifier scope, or structural mismatches — phenomena that none of the six misalignment strategies directly target. The paper claims (abstract, conclusion) that the method "significantly reduces the reliance on manual verification" and "proves its practical utility in real-world scenarios," but without testing on real autoformalizer outputs, the evidence for these practical claims is absent. This is the single most significant limitation: the technical approach is sound, but its real-world utility for the stated application remains unvalidated.

2. **Comparison with GPT-4 is asymmetrical and over-interpreted.** GPT-4 and GPT-3.5 are evaluated zero-shot (prompt details deferred to the appendix), while FormalAlign is fine-tuned on domain data. The paper frames the comparison as "FormalAlign outperforms GPT-4" (e.g., 99.21% vs. 88.91% on FormL-Basic), but this conflates fine-tuning with method superiority. A fairer comparison would involve fine-tuning a GPT-scale model on the same objective, or at minimum comparing against a strong non-LLM baseline (e.g., BERTScore-based detector). The current framing inflates the apparent advantage.
   - *Note on removal consideration:* The asymmetry favors the author's method, not the baseline. As per the rules, this criticism is retained.

### Minor

3. **The training-time contrastive objective is not directly aligned with the inference-time detection task.** During training, the contrastive loss uses in-batch negatives — i.e., the model learns to distinguish *different theorems* (NL₁/FL₁ vs. NL₁/FL₂). At inference, the model must detect whether a formal statement is a *perturbed version of the same theorem* (e.g., NL₁/FL₁ vs. NL₁/FL₁-with-changed-constant). These are different discriminative tasks, and the training never explicitly teaches the model to recognize perturbation types. The ablation shows the contrastive loss helps empirically, but the paper provides no principled argument for why this transfer should work. The method would be stronger if it included perturbed negatives in training or discussed this mismatch explicitly.

4. **Detection threshold θ is not validated.** The paper states "To balance precision and recall... we set θ=0.7" (Sec. 5) with no mention of a held-out validation set for this choice, nor any sensitivity analysis. If θ was tuned on the test data, the reported Precision/Recall values would be optimistically biased. This does not affect the Alignment-Selection metric (which is threshold-free), so it is a secondary concern, but it weakens confidence in the detection results.

5. **Human evaluation shows a significant accuracy gap with limited analysis.** FormalAlign achieves 65.00% correctness vs. 79.58% for human experts on the 80-item evaluation (Sec. 5.4). The paper notes the speed advantage (~2 min vs. ~3 hours) but does not analyze *why* the method makes errors compared to humans, nor discuss whether a 65% accuracy rate is adequate for practical deployment. A breakdown of failure cases by misalignment type would have been valuable.

### Trivial
None. (The points below are moved to Removed Points or Nice-to-Haves.)

## Nice-to-Haves

- **Per-misalignment-type analysis.** A breakdown of AS, Precision, and Recall by each of the six misalignment strategies would reveal whether the method is uniformly good across perturbations or relies on easy types like random pairing (which dominates several datasets per Fig. 4).
- **Design choice justification.** The paper uses the final token's hidden state for representations; a brief justification (or ablation) comparing with mean pooling or first-token encoding would strengthen the method section.
- **Temperature parameter τ specification.** The temperature τ in Eq. (2) is mentioned but its value is not reported; including it and ideally a sensitivity analysis would improve reproducibility.
- **Failure case analysis.** Examples where the method incorrectly flags aligned pairs as misaligned or vice versa would build trust and help users calibrate expectations.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about appendix-dependent content:** The harsh critic noted that analysis sections defer to the appendix (data contamination, generalization, autoformalization performance, manual review). Per the instructions, weaknesses about missing appendix content are removed because the parser strips appendices from all papers.
- **Missing related work on contrastive methods (SimCSE):** Per the instructions, missing related work criticisms are not included as they cannot be independently verified.
- **"Novelty is limited because prior work uses BERTScore/CodeBERT for semantic similarity between NL and formal code."** The paper scopes itself as the *first dedicated method* for autoformalization alignment evaluation, and Figure 1 demonstrates that BERTScore fails on the example while FormalAlign succeeds. The critic's concern conflates general-purpose semantic similarity with the specific task. The strength stands.
- **Criticism about the GPT-4 baseline prompt not being reported:** The paper explicitly defers prompt details to the appendix. Since the appendix is stripped by the parser, this is not a verifiable omission from the body.

## Novel Insights

The most interesting observation emerging from the reviews is the **contrast between strong empirical results on synthetic perturbations and the unknown transfer to real autoformalization errors.** The ablation studies clearly demonstrate that the dual-loss approach works on the constructed misalignments, and the human evaluation validates that the task is non-trivial (humans at 79.58%). But the paper's core practical claim — reducing manual verification in real autoformalization — rests on the untested assumption that synthetic perturbations approximate real model errors. Whether actual autoformalization systems (e.g., GPT-4 prompted to translate) produce errors that look like the six perturbation types, or whether they produce qualitatively different failures (e.g., hallucinated lemmas, incorrect variable binding across scope), is entirely open. This creates a clear and actionable research direction: collecting and releasing a benchmark of naturally-occurring autoformalization misalignments with human labels.

## Suggestions

1. **Test on real autoformalizer outputs.** Collect formal statements generated by a modern autoformalization model (e.g., GPT-4 or a fine-tuned model), have human experts label alignment, and evaluate FormalAlign on this realistic distribution. This single addition would transform the paper's contribution from "promising method on synthetic data" to "validated tool for real-world use."
2. **Add a non-LLM baseline.** Compare against a simpler baseline (e.g., BERTScore or a fine-tuned classifier based on CodeBERT embeddings) to disentangle the benefit of LLM fine-tuning from the proposed dual-loss design.
3. **Report per-type alignment detection results.** Break down AS, precision, and recall by each of the six misalignment strategies to identify where the method excels and where it struggles.
4. **Validate the detection threshold** on a held-out set and report sensitivity across a range of θ values (or report AUROC/AUPRC).
5. **Calibrate the practical claims.** Replace "significantly reduces the need for manual verification" with a more precise claim about what the method demonstrates — e.g., "achieves strong accuracy on synthetic perturbations and offers a 90× speedup over human evaluation, suggesting potential for semi-automated verification pipelines."
