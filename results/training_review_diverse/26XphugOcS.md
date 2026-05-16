Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes a zero-shot method for transferring continuous prompts across different language models. The core idea is to encode a source model's trained prompt into a "relative space" defined by cosine similarities to shared anchor tokens (common vocabulary), then search for target-model prompt embeddings whose relative encoding matches. The method is training-free on the target side, requires no paired prompt data, and extends naturally to multi-source transfer. Experiments on the LAMA factual probing benchmark (41 relation types) across BERT, RoBERTa, and ALBERT variants show consistent improvements over discretization and neural projector baselines, with self-transfer results approaching direct tuning.

## Strengths

- **Truly zero-shot cross-model transfer without target-side training.** The encode-then-search procedure uses only a shared vocabulary as anchors, requires no gradient backpropagation through the target model, and needs no paired prompt embeddings for training. This cleanly addresses the key limitation of prior neural projector approaches (Section 2, Figure 1).

- **Large and consistent improvements over comparable baselines.** On the main evaluation (Table 2), single-source transfer from BERT_base to BERT_large achieves 31.40% accuracy, more than doubling the neural projector baseline (12.49%). Transfers from BERT_base and RoBERTa_base surpass manual prompting in several target-model/target-model combinations (e.g., 31.40% vs 32.22% manual on BERT_large; in many cases they surpass it or come close). The improvements are systematic across nearly all source–target pairs.

- **Self-transfer validates the core mechanism.** When source and target are the same model (gray cells in Table 2), the method recovers 49.82% vs 50.56% direct tuning for BERT_base and 45.17% vs 46.24% for RoBERTa_base. This convincingly demonstrates that the relative encoding–decoding cycle preserves prompt quality, serving as a strong internal sanity check.

- **Multi-source transfer shows additive benefit on models not seen during tuning.** The BERT_base+RoBERTa_base dual-source setting achieves the best results on ALBERT_base (27.13%) and ALBERT_large (26.54%), models not used as sources. This demonstrates a practical benefit of aggregating task semantics across sources.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is limited to a single task family (factual probing).** The paper's central claim — that the method generalizes "task semantics" across language models — is tested only on LAMA TREx, a factual knowledge completion dataset. While the 41 relation types provide diversity within this family, they all share the same prompt format (subject-relation prediction) and task structure (single-token generation from a fixed vocabulary). The paper provides no evidence that the method works for classification (e.g., SST-2), natural language inference (e.g., RTE), or sequence labeling — the kinds of tasks where prompt tuning is most commonly deployed. The paper itself uses the term "task semantics" in a general sense (abstract, Section 1), so the narrow evaluation leaves this claim under-supported. Adding even one non-factual task would substantially strengthen the contribution.

2. **No variance or statistical significance reported.** All results in Tables 1–2 are presented as single-point estimates with no standard deviations, confidence intervals, or information about the number of random seeds used (for prompt tuning or the search procedure). Given that the multi-source improvements over the best single source are often just 1–2 percentage points (e.g., 25.09% → 25.26% on RoBERTa_large), and that one case (RoBERTa_base target with BERT_base+RoBERTa_base dual source, 43.83%) is actually *worse* than the single-source self-transfer (45.17%), it is impossible to determine whether the reported gains are reliable. This is a basic experimental rigor issue that undermines several of the paper's comparative claims.

### Minor

1. **Missing implementation details for reproducibility.** The search procedure (Equation 5) is described as "gradient descent" with "randomly initialized" target embeddings (Section 2.3), but no learning rate, number of steps, convergence criterion, or initialization distribution is specified. The anchor selection mechanism is described as "simply choose the shared tokens as the set of anchors" (Section 2.2), but how shared tokens are identified across models with different tokenizers (BERT's WordPiece vs RoBERTa's BPE) is not discussed — this is non-trivial and should be specified for reproducibility.

2. **Multi-source claim is slightly overstated.** The paper states "using multiple sources generally improves transferability" (Section 3.3), but the dual-source BERT_base+RoBERTa_base setting actually underperforms the single-source self-transfer on RoBERTa_base (43.83% vs 45.17%) and on BERT_base (48.79% vs 49.82%). While "generally" permits exceptions, these are notable cases where adding a second source *hurts* performance even compared to a single source that is the target itself. A more nuanced discussion of when multi-source helps vs hurts would strengthen the paper.

3. **No dedicated limitations section.** The paper does not discuss limitations such as: dependence on shared vocabulary overlap between models, sensitivity to tokenizer mismatch, the lack of guarantees that the relative representation mapping is injective (the search could find spurious matches), or the restriction to prompt-postfix format only (Section 2.1 mentions suffix-only design without testing alternatives).

### Trivial
- The y-axis label in Figure 4 (the ablation on anchor/prompt length) is not clearly readable in the description; this should be verified in the camera-ready version.
- The direct transfer asymmetry (BERT_large→RoBERTa_large 6.27% vs RoBERTa_large→BERT_large 0.49%, Table 1) is noted but not discussed. A brief comment would be helpful.

## Nice-to-Haves

- **Comparison with few-shot alternatives.** Comparing against a baseline where the source prompt initializes a few steps of prompt tuning on the target with small amounts of data (e.g., 8, 32 examples) would help calibrate the practical value of the zero-shot trade-off.
- **Test with a truly small source model.** The paper motivates the scenario of "tuning on a small model, deploying on a large one" (Section 1), but the smallest source used is BERT_base (110M params). Testing with a smaller model (e.g., DistilBERT at 67M or BERT-tiny) would directly validate this claimed benefit.
- **Analysis of why large-source models transfer poorly.** The paper offers a post-hoc explanation (expressive power / many near-optimal prompts) but provides no supporting evidence. An analysis measuring alignment variance or prompt redundancy across model sizes would strengthen this argument.

## Removed Points
*These points were flagged for removal during meta-review synthesis. They are listed here for traceability but should not be weighed in the final assessment.*
- **"Weak baselines: missing SPoT/ATTEMPT."** SPoT (Vu et al., 2022) and ATTEMPT (Asai et al., 2022) are cross-task transfer methods requiring task supervision on the target, which contradicts the zero-shot framing of this paper. The paper cites both in Related Work (Section 4). This is a comparison against the wrong class of method; removed as an unfair expectation.
- **"Neural projector baseline details are scarce, suggesting it was poorly configured."** The paper describes a "two-layer projector" trained on anchor words (Section 3.2). The low performance of this baseline does not constitute evidence of poor configuration — it may genuinely reflect the difficulty of cross-model prompt projection. Speculation about improper configuration is removed.
- **"Paper doesn't discuss parameter-efficient methods like LoRA as an alternative to prompt tuning."** The paper's motivation is about prompt transfer, not about parameter-efficient fine-tuning. This is a tangential comparison from a different line of work.
- **"Brain signal speculation in conclusion is over-ambitious."** This is a single sentence in the concluding speculation paragraph — standard practice. It has no bearing on the paper's technical contribution.
- **"The normalization step (Eq. 5) is ad-hoc."** The paper provides a clear motivation (cosine similarity is scale-invariant, so searched embeddings need rescaling to match target word embedding statistics) and an ablation study (Figure 3) specifically testing its effect. This criticism ignores the ablation evidence.

## Novel Insights

The reviews collectively highlight a tension not discussed in the paper: the method works best when source and target are in the same "model family" (BERT→BERT, RoBERTa→RoBERTa achieve near-direct-tuning self-transfer), but cross-family and cross-size transfers are substantially weaker. This suggests that the relative representation space may not be as model-agnostic as the paper assumes — the "shared structure" across models may be partially an artifact of shared pretraining data or architecture similarity rather than a universal semantic space. The fact that base→base cross-model transfer (BERT_base→RoBERTa_base: 17.68%) is much lower than within-model transfer (49.82% for BERT_base self) while still beating naive baselines suggests the relative encoding captures *some* shared structure but loses model-specific information crucial for performance. A deeper investigation of what information is preserved vs lost in the relative encoding would be a valuable follow-up.

## Suggestions

1. **Add at least one non-factual task** (e.g., sentiment classification on SST-2 or NLI on RTE) with the same source→target transfer setup. This would directly test whether "task semantics" transfer works beyond factual knowledge retrieval.
2. **Report results from 3+ random seeds** with standard deviations for all main numbers. This is especially important for the multi-source comparisons where gains are 1–2 points.
3. **Specify the search procedure details** (learning rate, number of gradient steps, convergence criterion, initialization scheme) and the anchor token identification mechanism across different tokenizers.
4. **Acknowledge the cases where multi-source hurts** (self-transfer dilution) and discuss when practitioners should use single vs multi-source transfer.

## Score and Decision

The paper introduces a clean, well-motivated idea with a clever use of relative representations for zero-shot cross-model prompt transfer. The self-transfer validation is strong evidence that the encoding–decoding cycle works. However, the evaluation is too narrow to fully support the claimed generality of "task semantics" transfer, the lack of variance reporting makes the multi-source results and comparative claims difficult to assess, and key implementation details are missing. The contribution is real but the evidence base is insufficient for acceptance at the current standard. A major revision with broader task coverage, statistical rigor, and fuller documentation could make this a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>