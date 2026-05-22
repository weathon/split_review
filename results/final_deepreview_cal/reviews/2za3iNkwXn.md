Now I have sufficient anchoring data. Let me write the consolidated review.

**Calibration Round 1 bracket:** The paper falls between weak anchors (~3.0) and strong anchors (~7.6-8.67), placing it in the middle band (roughly 4.5-7.0).

**Calibration Round 2 comparison:**
- "The Cost of Scaling Down LLMs" (6.00) — similar study on how pruning affects fact recall vs ICL. The current paper is broader (covers quantization + distillation + pruning) and adds interpretability, though with slightly more methodological concerns. Comparable quality.
- "Fine-Tuning Enhances Existing Mechanisms" (5.67) — interpretability study of fine-tuning effects, similar methodology. The current paper has more practical implications and broader scope.
- "Evaluating Generalization of Quantized LLMs" (4.75, rejected) — purely a benchmarking study without interpretability; the current paper's interpretability component puts it clearly above.
- "Activation Patching Best Practices" (6.67) — focused on methodological refinement of the same technique, cleaner but narrower contribution.
- "Mechanistically Analyzing Fine-Tuning Effects" (6.67) — thorough but synthetic setting; the current paper works on real models with real compression methods.

**Final score rationale:** The paper is comparable to "The Cost of Scaling Down LLMs" (6.0) in terms of contribution quality and weakness severity. Both have real but addressable weaknesses. The current paper has the edge in breadth (multiple compression methods + interpretability) but has somewhat more specific methodological concerns. Score: **6.0**.

---

## Summary

This paper investigates how three compression paradigms — quantization, distillation, and pruning — affect the reasoning capabilities of large reasoning models (LRMs), specifically DeepSeek-R1 and its distilled variants. The contribution is two-fold: (1) a comprehensive benchmarking of compressed R1 models across four reasoning datasets (AIME 2024, FOLIO, Temporal Sequences, MuSiQue) at multiple bit-widths and sparsity levels, and (2) a fine-grained mechanistic interpretability framework that adapts difference of means and attribution patching to compute module-level importance scores, identifying which weight matrices are most affected by compression. The key findings — that the final-layer MLP up_projection is a critical component, and that current quantization methods over-compress final-layer modules and gate projections — are validated through selective quantization and protection experiments, where protecting just ~2% of weights recovers 6.57% average accuracy.

## Strengths

- **Comprehensive multi-method benchmarking on LRMs.** Table 1 systematically compares dynamic quantization, distillation, pruning (SparseGPT, AlphaPruning), and post-training quantization (AWQ, GPTQ, GPTAQ, ANY4/3) on four reasoning datasets. Table 2 sweeps sparsity from 10%–80% on two model sizes, identifying collapse points and their correlation with benchmark difficulty. This fills a concrete gap, as prior work had not benchmarked all three compression paradigms together on LRMs with reasoning-intensive tasks.

- **Novel application of mechanistic interpretability to compression effects.** The paper adapts difference of means and attribution patching to compute module-level importance scores (I^c_{mℓ} and RI^c_{mℓ}) for every linear component across all layers of compressed LRMs (Section 2.2, Equations 1–3). This goes beyond prior layer-wise analysis and enables fine-grained tracing of how compression alters causal contributions of individual weight matrices. The heatmaps (Figures 2, 3, 6, 7) provide interpretable, visual evidence for the compression effects.

- **Empirically validated actionable findings.** The identification of the final-layer up_proj as most important is validated by selectively quantizing it to 3-bit, which drops average accuracy by 16.3% (Table 3). The finding that current quantization over-compresses final-layer and gate projections is validated by protecting just 2% of weights (final-layer MLP) in 3-bit AWQ, raising average accuracy by 6.57% and outperforming all 3-bit baselines by up to 23.17% (Table 4). This direct validation-prediction loop is the paper's strongest evidence.

- **Generalization across model families (Llama and Qwen) demonstrated in the main text.** Key findings about the final-layer up_proj and gate projection over-compression are consistently observed in both R1-Distill-Llama-8B and R1-Distill-Qwen-7B (Figures 2, 4, 5, 6), showing the patterns are not specific to one architecture.

## Weaknesses

### Major

- **The knowledge-versus-reasoning claim is partially supported by a confounded cross-architecture comparison.** Finding (1) in the abstract states that "weight count has a greater impact on LRMs' knowledge memorization than their reasoning capabilities." The main evidence (Section 3.3) compares R1-Distill-Qwen-32B vs. R1-Distill-Llama-70B, where Qwen-32B scores higher on reasoning but much lower on MuSiQue (knowledge). However, these models differ not only in parameter count (32B vs. 70B) but also in base architecture (Qwen vs. Llama), training data, and tokenizer — parameter count is not isolated. The additional evidence from pruning (knowledge collapses earlier than reasoning under increasing sparsity) independently supports the narrower claim about pruning effects, but does not cleanly support the broader "weight count" claim. The takeaway boxes (Takeaway 3.3) wisely frame this as "Pruning and distillation compress knowledge retention more than reasoning capabilities," which is better supported. The abstract's "weight count" framing overclaims relative to the controlled evidence.

### Minor

- **Validation of importance scores tests only 5 of 224 components.** Table 3 validates the importance ranking by quantizing 5 components out of 7×32=224 total. While the selection strategy (1st overall, 2nd column, last column, 2nd row, last row) is principled, the small sample leaves open the question of how well the ranking generalizes. Additionally, on AIME 2024, quantizing 1_up (ranked last) produces a lower accuracy (6.7) than quantizing 32_up (ranked 1st, 20.0), showing task-specificity that the paper acknowledges but does not fully resolve. The paper points to Appendix N for additional AIME validation (stripped by the parser), so the main text alone lacks sufficient evidence that the ranking is stable across tasks.

- **Pruning interpretability analysis is deferred to the appendix.** The paper lists pruning as one of three studied compression paradigms, and the title promises understanding compression effects broadly. However, the main interpretability results (Sections 4–5) cover only distillation and quantization. Pruning effects on weight importance are deferred to Appendix I with the note that "pruning effect based on AlphaPruning appears very similar to quantization effect" (line 263). While the paper is transparent about this, the main text's scope feels narrower than advertised.

- **Selective protection experiment is demonstrated on only one model and one quantization method.** The key validation in Table 4 (protecting 2% of weights recovers 6.57% accuracy) is performed only on R1-Distill-Llama-8B with 3-bit AWQ. Replicating on at least one other model (e.g., Qwen-7B) or another quantization method (e.g., GPTQ) would significantly strengthen the claim that the identified bottlenecks are general.

- **First-order attribution patching approximation is not discussed.** The attribution patching in Equation 2 uses a first-order (gradient) approximation of the actual effect of patching. This linearity assumption can miss non-linear interactions, especially in deep transformers. The paper does not acknowledge this limitation or provide any small-scale check (e.g., comparing the first-order ranking with actual activation patching for a few components).

### Trivial

- Figure captions and table formatting are dense and occasionally difficult to parse (e.g., the scaling note about heatmaps in Figure 2 is helpful but easy to miss). The paper would benefit from more self-contained captions.

## Nice-to-Haves

- The selective protection experiment could be extended to Qwen-7B and/or GPTQ to demonstrate the finding is not specific to Llama-8B + AWQ.
- Including variance or confidence intervals for the main results (Table 1 reports three-run averages but no variance) would help assess stability, especially for differences of a few percentage points.
- The 1_up anomaly on AIME 2024 (Table 3) could be investigated: does this component serve a specific sub-capability needed for mathematical reasoning that is not captured by the average?

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Claim that generalization to non-R1 models is unsubstantiated.** The paper references Appendix J for the non-R1 generalization results. The parser strips all appendix content from the extracted text. Per policy, this is not a valid criticism of the paper as submitted.
2. **Claim about missing related works.** No external sources are available to verify what works should have been cited.
3. **Formatting/style nitpicks about the introduction framing.** Minor presentational preferences that do not affect the paper's contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Tighten the knowledge-versus-reasoning claim.** Either (a) add a controlled comparison within the same model family (e.g., Llama-8B vs. Llama-70B, both distilled from R1), or (b) reframe the abstract to match what is actually shown: "pruning and distillation compress knowledge retention more than reasoning capabilities" rather than "weight count has a greater impact on knowledge."
2. **Expand the importance score validation** to include more components (e.g., 10–15 components spanning different ranks) and verify that the ranking from importance scores correlates monotonically with accuracy drop upon quantization.
3. **Replicate the selective protection experiment** on at least one additional model (Qwen-7B) or quantization method (GPTQ) to demonstrate generality.
4. **Acknowledge the first-order approximation limitation** in the main text and, if feasible, include a small-scale sanity check comparing first-order importance rankings against actual activation patching results.
5. **Move a brief pruning interpretability result into the main text** (or explicitly narrow the scope in the title/abstract to "quantization and distillation effects").

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>