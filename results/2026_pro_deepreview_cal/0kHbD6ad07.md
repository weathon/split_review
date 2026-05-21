Now I have sufficient calibration. Let me compile the final review.

**Bracket from Round 1**: Between ~5.5 and 8.0

**Round 2 narrowing**: The paper sits closer to the 6.67 (Transformers are Universal In-context Learners) and 7.33 (CoT multi-step GD) anchors. It's stronger than "Language Model Inversion" (5.50) and "Function Vectors" (6.00), comparable to "Universal In-context Learners" (6.67), and slightly below "CoT multi-step GD" (7.33). Score: **7.0**.

---

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective: distinct prompts map to distinct last-token hidden states with probability one at initialization, and this property is preserved under gradient-based training. The authors validate this claim through ~5 billion collision tests across six model families (GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, TinyStories) finding zero collisions, and operationalize injectivity via SIFT (called SIPIT in the paper), an algorithm that reconstructs the exact input sequence from hidden states with provable linear-time guarantees, achieving 100% token accuracy in practice.

## Strengths

- **Rigorous mathematical foundation for injectivity at initialization (Theorems 2.1–2.2).** The paper establishes that Transformers are real-analytic functions of their parameters, then uses the fundamental dichotomy of real-analytic functions (zero set is either everything or measure zero) together with an explicit construction of a separating parameter setting to prove almost-sure injectivity. This is clean, well-structured, and correctly applies standard tools from real analysis. The construction in Theorem 2.2 — handling last-position mismatches via embeddings and earlier mismatches via attention-head routing — is constructive and convincing.

- **Exhaustive and convincing empirical collision search.** The paper conducts ~5 billion pairwise comparisons across 100k prompts from diverse sources (Wikipedia, C4, The Pile, Python code). Results span GPT-2 (Small/Medium/Large), Gemma-3 (1B/4B/12B), Llama-3.1-8B, Mistral-7B, Phi-4-mini, TinyStories-33M, and even FP4/INT8 quantized versions and large models up to Llama-3.1-70B. Zero collisions are found, with minimum L2 distances orders of magnitude above the numerical threshold (e.g., Phi-4-mini final-layer min = 9.020; Table 1). This is thorough empirical validation that directly corroborates the theory.

- **SIPIT algorithm operationalizes injectivity with provable guarantees.** Algorithm 1 exploits the causal structure of Transformers for sequential token-by-token recovery. Theorem 3.1 provides a worst-case bound of T|V| steps, and Theorem 3.2 proves robustness to bounded hidden-state perturbations. The algorithm achieves 100% token accuracy on GPT-2 Small (20-token prompts) and on FP4-quantized Mistral-7B and Llama-3.1-8B (10-token prompts), exploring <0.22% of the vocabulary on average (Tables 4–5). This turns the theoretical property into a working tool.

## Weaknesses

### Fatal
None.

### Major
None. The harsh critic's claim of a fatal gap in Corollary 2.3.1 is a misreading: the paper constructs a specific point θ_* (from the single-sample proof) where the Jacobian determinant is sample-independent, and at this constructed point the batch Jacobian coincides with the single-sample one by linearity of differentiation. This is a standard proof technique, and the full argument is deferred to Appendix C. The sketch is terse but not incorrect.

### Minor

- **HARDPROMPTS is an inappropriate baseline for inversion from hidden states.** HARDPROMPTS (Wen et al., 2023) is a gradient-based prompt *discovery* method designed for a different objective (optimizing prompts for downstream task performance). Using it as a comparison for hidden-state inversion yields a strawman 0% accuracy (Table 5) that is neither informative nor fair. The BRUTEFORCE baseline is appropriate and sufficient to demonstrate SIPIT's efficiency advantage. The HARDPROMPTS comparison should be removed or replaced with a method that actually targets hidden-state recovery.

- **The training-preservation proof sketch in the main text (Theorem 2.3 / Corollary 2.3.1) is compressed to the point of being hard to follow.** The claim that step sizes in (0,1) suffice is stated without explanation, and the batched case argument — while logically valid given the constructed θ_* — is presented in a single sentence that could confuse readers. Given that training-time injectivity is the paper's headline theoretical contribution, a more self-contained sketch (or at minimum a clearer signpost to the appendix) would strengthen the main text. This is a presentation issue, not a logical gap, since the full proofs are in the appendix.

- **Inversion experiments are concentrated on smaller/quantized models.** Unquantized SIPIT results are shown only for GPT-2 Small (124M parameters, 20-token prompts). The larger-model results (Mistral-7B, Llama-3.1-8B) use FP4-quantized weights and shorter 10-token prompts (Table 4). Demonstrating SIPIT on an unquantized 7B–8B model with prompts of 20+ tokens would more directly validate the scalability claims, though the current results already demonstrate the key points.

### Trivial
- The name "SIFT" is used in the abstract and introduction, but "SIPIT" appears in the algorithm and experiments. This inconsistency should be resolved.

## Nice-to-Haves
- Testing SIPIT on an unquantized 7B–8B model with longer prompts (e.g., 30–50 tokens) would strengthen the scalability evidence.
- Specifying the tolerance ε used in SIPIT experiments and discussing its relationship to floating-point precision would aid reproducibility.
- Analyzing how SIPIT's efficiency degrades under increasing hidden-state perturbation (beyond FP4 quantization) would complement the robustness theorem (3.2).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic: "The proof that injectivity is preserved under training is not adequately established / Corollary 2.3.1 is incorrect."** REMOVED. This is a misreading. The paper constructs a specific point θ_* where the Jacobian determinant is sample-independent; at this point, the batch Jacobian coincides with the single-sample one by linearity. The full proof is in Appendix C. The sketch, while terse, is not logically flawed. The critic's objection — "there is no justification that the average Hessian equals the single-sample Hessian" — ignores that θ_* is specifically constructed to have this property. This is a standard technique in such proofs.

- **Harsh critic: "The claim that step sizes in (0,1) suffice is also unexplained."** REMOVED. This is almost certainly addressed in the full appendix proof. The main text sketch is just that — a sketch. Flagging this as a weakness of the paper when the appendix is stripped is not appropriate.

- **Harsh critic: "The reported per-token inversion time (≈28s) is not obviously efficient" and "On Llama-3.1-8B the time explodes to ≈550s."** REMOVED. These are judgment calls about what constitutes "efficiency." The paper reports times honestly; the 28s for GPT-2 Small with 20 tokens is reasonable for exact reconstruction from hidden states. The Llama-3.1-8B results use FP4 quantization and the paper transparently reports the times (549s mean). The paper does not claim these are "fast" in an absolute sense — it claims they are efficient relative to brute force and demonstrate the predicted linear scaling.

- **Strength Finder: "Rigorous proof of almost-sure injectivity and its preservation under training."** RETAINED but qualified. The initialization proof is rigorous. The training-preservation proof sketch is compressed but the full version is in the appendix. I've incorporated this into the strengths.

- **Harsh critic: "Privacy/legal implications discussion goes beyond technical scope."** REMOVED. The discussion in Section 6 is speculative but appropriately hedged. It connects the paper's technical result to real-world implications, which is standard practice. This is not a weakness.

- **Harsh critic: "Missing inversion benchmarks on a 7B model unquantized with 30–50 tokens."** RETAINED as a minor weakness / nice-to-have, but downgraded. The paper already demonstrates the method on 3 models across different scales, and the collision search covers 6+ models.

## Novel Insights
The paper's framing of Transformer injectivity through the lens of real-analytic functions and measure theory is genuinely novel. Prior work studied injectivity only at initialization (Sutter et al., 2025) or focused on surjectivity (Jiang & Haghtalab, 2025). The key insight — that Transformer components are real-analytic, and real-analytic functions have the property that their zero sets are either everything or measure zero — provides a clean, unified framework that yields guarantees at finite width, depth, and training horizon without asymptotic approximations. The explicit construction of a separating parameter setting in Theorem 2.2 (using attention-head routing to isolate the first differing position) is elegant and may inspire similar constructions in future theoretical work on Transformers.

## Suggestions
- Remove or substantially de-emphasize the HARDPROMPTS baseline comparison; the BRUTEFORCE ablation already demonstrates SIPIT's efficiency advantage.
- Expand the main-text sketch of Corollary 2.3.1 by 2–3 sentences explaining why the constructed θ_* makes the Jacobian determinant sample-independent, and explicitly signpost the full proof in Appendix C.
- Resolve the SIFT/SIPIT naming inconsistency.
- If feasible, add one unquantized 7B model experiment to Table 4 to directly demonstrate scaling without quantization confounds.

---

**Anchor comparison summary:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Language Model Inversion (t9dWHpGkPj) | 5.50 | 1 | Our paper is stronger: provable guarantees + 100% accuracy vs. ~27% exact match with no guarantees |
| Function Vectors (AwyxtyMwaG) | 6.00 | 1 | Our paper is stronger: combines theory and practice vs. primarily empirical/phenomenological |
| Transformers are Universal ICL (6S4WQD1LZR) | 6.67 | 2 | Comparable: both theoretical transformer papers; ours adds practical algorithm and extensive empirical validation |
| Transformers Learn Multi-step GD with CoT (r3DF5sOo5B) | 7.33 | 2 | Slightly below: the CoT paper explains a widely-used phenomenon with tighter theory; ours has broader empirical scope and applies to real architectures |
| Retrieval Head (EytBpUGB1Z) | 8.00 | 1 | Below: fundamental discovery of a neural mechanism with broad impact on long-context understanding |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>