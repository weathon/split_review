Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper investigates why naive output alignment (minimizing layer-wise output error) fails for 1-bit post-training quantization of LLMs, identifying three issues: (i) layer-wise output alignment does not guarantee block-level loss reduction, (ii) quantization errors accumulate across layers, and (iii) it can degrade token interactions/attention. The paper proposes a solution combining (a) a reformulated output error objective that uses full-precision inputs to account for accumulated errors, (b) an Attention Matrix Preservation (AMP) mechanism that masks parameter updates to preserve token similarities, and (c) selective application of output alignment to only the last fully-connected layer of each block. Experiments on OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3-8B show the method generally outperforms prior 1-bit PTQ methods, with AMP alone yielding ~10 perplexity improvement on LLaMA-2-7B.

## Strengths

1. **Well-motivated diagnosis of why output alignment fails for 1-bit PTQ**. Section 3 provides concrete empirical evidence for three distinct failure modes: the block-level loss analysis (Figure 1) demonstrates that layer-wise output alignment does not guarantee block-level improvement; the error accumulation analysis (Figure 2, top) shows the activation-conditioned error diverges from the true output error with depth; and the token-similarity analysis (Figure 2, bottom) reveals degradation of token interactions. This diagnostic analysis is a genuine contribution in itself.

2. **Reformulated output error objective shows clear empirical benefit**. Table 4 shows that using the output error $\|XW - \hat{X}\hat{W}\|^2$ instead of the activation-conditioned error $\|\hat{X}W - \hat{X}\hat{W}\|^2$ yields 0.7 perplexity improvement on C4 for LLaMA-2-7B, validating the paper's central claim that accumulated errors matter.

3. **AMP mechanism delivers a striking 10-point perplexity improvement on LLaMA-2-7B**. Table 3 shows that disabling AMP increases perplexity from 19.25 to 29.12 on C4 and from 15.42 to 26.24 on WikiText2. The hypothesis linking this sensitivity to LLaMA's use of RMSNorm (which normalizes per-token to unit norm, making the model more reliant on directional information) is plausible and provides architectural insight.

4. **Closed-form derivations for $\alpha_c$, $\alpha_r$, and $B$ (Equations 5–8)** enable efficient optimization without iterative search or backpropagation through the binarization function, which is practically valuable for 1-bit PTQ.

5. **Comprehensive evaluation across model scales**. Experiments span OPT (1.3B–30B), LLaMA-2 (7B, 13B), and LLaMA-3-8B, across three perplexity benchmarks and zero-shot QA, which is more thorough than many prior 1-bit PTQ papers.

## Weaknesses

### Major

1. **The LLaMA-2-7B PTB result contradicts the "consistently outperforms" claim.** The method achieves 3166 perplexity on PTB for LLaMA-2-7B, while PB-LLM achieves 657, ARB-RC 763, and ARB-X 681 (Table 2). The paper acknowledges this with "with the exception of Llama-2-7B model evaluated on PTB dataset" (line 179) and dismisses it as "the metric cannot provide a meaningful evaluation" (line 237). This is not an adequate explanation — the same metric is meaningful for baselines. The abstract, introduction, and conclusion all state the method "consistently outperforms" prior work, which is factually false given this data point. While this is one anomalous cell in a large table, it is a clear counterexample to an unqualified claim. The authors should either qualify their claims (e.g., "generally outperforms") or explain why this failure occurs.

### Minor

2. **Implementation of the output error objective is underspecified.** The core loss (Equation 3) requires the full-precision layer input $X$, and the closed-form solution (Equation 5) uses $S = \hat{X}^\top X$, mixing quantized and full-precision activations. The paper never explains how $X$ is obtained — e.g., whether full-precision activations are cached from a forward pass of the full-precision model (standard PTQ practice) and what the memory overhead is. While this is not a fatal omission (caching full-precision activations is standard), it should be explicitly stated for reproducibility.

3. **Equation (9) contains a notational imprecision.** The AMP objective is written as $\max \| (\hat{X}\hat{W}\hat{W}^\top\hat{X}^\top) \odot (XWW^\top X^\top) \|$ and then rewritten as $\text{Tr}[\hat{X}\hat{W}\hat{W}^\top\hat{X}^\top XWW^\top X^\top]$. The Frobenius norm of the element-wise product $\sqrt{\sum_{i,j} (A_{ij}B_{ij})^2}$ is not the same as the Frobenius inner product $\sum_{i,j} A_{ij}B_{ij} = \text{Tr}(A^\top B)$ (which reduces to $\text{Tr}(AB)$ for symmetric matrices). The intended meaning (maximizing the inner product) is recoverable from context but the notation as written is mathematically imprecise.

4. **The selective alignment strategy (last layer only) is not ablated.** The paper restricts output alignment to "only the last fully connected layer of each block" (Section 4.2), justified by the claim that it "has the most direct impact on the block loss." No experiment compares this against alternatives (e.g., aligning all layers, aligning the first layer, aligning based on sensitivity). Given that Figure 1 shows output alignment can be beneficial across many layers, this choice merits empirical justification.

5. **AMP is a heuristic without theoretical grounding.** The AMP masking mechanism (Equations 10–11) gates parameter updates by the sign of the gradient of the AMP objective. This is presented without derivation or justification from optimization principles. Given that AMP provides ~10 perplexity points of improvement, its heuristic nature is a significant gap — the paper could strengthen this by comparing against simpler alternatives (e.g., adding the AMP objective as a regularization term).

### Trivial

6. **Minor typos**: Equation (2) appears to have a typo ($\|\hat{X}\hat{W} - \hat{X}\hat{W}\|$ where the second term should be $\hat{X}W$).

## Nice-to-Haves

- The paper could compare against STB-LLM in the evaluation, as it is cited in related work but not used as a baseline. However, STB-LLM combines pruning and quantization and may not be directly comparable.
- Zero-shot QA results for LLaMA models are referenced to the appendix (which the parser strips); if these exist in the original submission they should be included in the main paper.
- Reporting variance or statistical significance would help assess whether the improvements (often <1 perplexity point) are meaningful, though single-run evaluation is standard for large-scale PTQ.

## Removed Points

The following criticisms from the harsh reviewer are removed as unsubstantiated or violating filtering rules:

- **"The PTB result is a decisive counterexample that invalidates the paper's central claim"** (retained, but downgraded from fatal to major — it's one anomalous cell in an extensive set of comparisons. The method still outperforms on 11 out of 12 LLaMA benchmark cells, and BiLLM also fails catastrophically on this cell with 5243 perplexity, suggesting PTB is uniquely difficult for 1-bit methods on this model.)
- **"The paper never explains how X is obtained"** (retained but downgraded to minor — caching full-precision activations is standard PTQ practice and implicitly understood by the community, though it should be stated explicitly.)
- **"Zero-shot QA results for LLaMA models are promised but not presented"** (removed — the appendix is stripped by the parser; no evidence these are missing from the original submission.)
- **"Overhead analysis deferred to appendix"** (removed — same appendix stripping issue.)
- **"No comparison with STB-LLM"** (removed — the paper compares against BiLLM, PB-LLM, ARB-RC, and ARB-X; STB-LLM is a different approach combining pruning and quantization. Not every cited method must be a baseline.)
- **"No statistical significance or variance"** (removed — single-run evaluation is the norm for 1-bit PTQ on 7B+ models. Running these experiments multiple times is computationally prohibitive.)
- **"The method requires full-precision input X which is a major practical limitation"** (retained but downgraded — obtaining X via a single forward pass cache is standard, not a practical limitation. The issue is about clarity, not feasibility.)
- **Strength Finder's claim that the paper achieves "consistent outperformance across models and benchmarks"** (removed as conflicting with verified weakness #1 — the PTB counterexample makes this claim unverifiable as stated.)

## Novel Insights

The most interesting observation emerging from synthesizing the reviewer inputs and the paper itself is the connection between AMP's effectiveness and RMSNorm. The paper hypothesizes that architectures using RMSNorm (LLaMA) are more vulnerable to quantization-induced attention degradation because RMSNorm normalizes each token to unit norm, making the model more dependent on the *direction* of representations. This simultaneously explains why AMP (which preserves token-similarity structure/directionality) is far more impactful for LLaMA (~10 PPL improvement) than for OPT (negligible improvement in Table 3). This insight — that normalization choice modulates quantization robustness — is potentially valuable beyond this specific method, as it suggests that 1-bit PTQ strategies may need to be architecture-aware, not just data-aware.

## Suggestions

1. **Qualify the "consistently outperforms" claim** to acknowledge the LLaMA-2-7B PTB anomaly explicitly, and either investigate its cause or note it as a known limitation.
2. **Add an ablation comparing selective alignment strategies** — at minimum, compare "last layer only" (current) vs. "all layers" vs. "first layer only."
3. **Clean up the AMP derivation notation** in Equation (9) to be mathematically precise.
4. **Explicitly state how $X$ (full-precision activations) is obtained**, mentioning the cache-and-reuse strategy and its memory overhead.
5. **Compare AMP against a simpler baseline** such as adding the AMP objective as a regularization term to the main loss, rather than the sign-of-gradient masking heuristic.

## Score and Decision

**Bracket (Round 1):** Based on calibration against human-reviewed PTQ papers, the paper sits between the weak anchors (avg 2.33–3.00: papers with fundamental flaws) and the strong anchors (avg 7.60–8.00: papers with clean execution and significant contributions). The paper is clearly better than FPTQ (avg 4.00, reject) and LRQ (avg 5.25, reject) — it addresses a harder problem (1-bit vs 4-bit), has more insightful analysis, and more comprehensive evaluation. It is somewhat weaker than PB-LLM (avg 6.75, accept poster) and OSTQuant (avg 6.20, accept poster) — both accepted papers with cleaner execution. **Initial bracket: 4.5–6.5.**

**Narrowing (Round 2):** Direct comparison with anchors in the bracket:
- **PB-LLM (6.75)**: Also 1-bit PTQ, accepted. PB-LLM had narrower evaluation (only Llama-7B, only CSQA) but a cleaner story. The current paper has broader evaluation and more diagnostic insights but the PTB counterexample and implementation clarity issues are more glaring than PB-LLM's weaknesses. → Current paper is weaker.
- **OSTQuant (6.20)**: W4A4 PTQ, accepted. Had similar levels of mathematical sloppiness and missing ablations. The current paper has comparable issue density but a more visible empirical failure. → Current paper is slightly weaker.
- **Low-Rank Correction (5.00, reject)**: Had missing analysis, limited novelty. Current paper is stronger — more novel insights, more extensive evaluation. → Current paper is stronger.
- **LRQ (5.25, reject)**: Marginal improvements over baseline, novelty concerns. Current paper has stronger diagnostic contributions and more substantial empirical gains (10-point AMP improvement). → Current paper is stronger.

**Final score: 5.5.** The paper has genuine contributions (well-motivated diagnosis, effective AMP mechanism, closed-form solutions, extensive evaluation) but is held back by (a) a clear counterexample to the unqualified "consistently outperforms" claim, (b) several minor issues with notation clarity and missing ablations that prevent it from being a clean accept. At 5.5, the paper is borderline — it has sufficient merit and insight to warrant further consideration, but the overclaiming and the PTB anomaly need to be addressed.

**Anchors retrieved for calibration:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| PrefixQuant | vw0NurJ7UX.md | 3.00 | R1 (weak) | Static quantization paper; current paper is much stronger |
| Scaling Laws Mixed Quant | UldnqRQWKS.md | 3.00 | R1 (weak) | Empirical scaling laws paper; current paper has stronger technical contribution |
| EfficientQAT | 6Mdvq0bPyG.md | 3.00 | R1 (weak) | QAT paper; current paper is more efficient (PTQ) and has deeper analysis |
| Unified View Delta Params | yx8bU8T5ZN.md | 2.33 | R1 (weak) | Theoretical framework paper; current paper is more applied and better evaluated |
| **PB-LLM** | BifeBRhikU.md | **6.75** | R1 (mid), R2 (high-mid) | Most directly comparable; also 1-bit LLM PTQ. Current paper has broader evaluation but a clearer failure mode |
| FPTQ | ykhRO1mAg3.md | 4.00 | R1 (mid), R2 (low-mid) | W4A8 PTQ; current paper addresses harder problem (1-bit) and has stronger diagnostics |
| Low-Rank Correction | FA3iYp1y6z.md | 5.00 | R1 (mid) | W4A4 PTQ; current paper has stronger novel insights |
| LRQ | MU6jInwj7p.md | 5.25 | R1 (mid) | Weight-scaling PTQ; current paper has more substantial contributions |
| OSTQuant | rAcgDBdKnP.md | 6.20 | R2 (high-mid) | W4A4 PTQ with similar math issues; current paper has comparable quality but more visible weakness |
| Compressing LLMs | B9klVS7Ddk.md | 6.75 | R2 (high-mid) | Benchmark/evaluation paper; different type of contribution, hard to compare directly |
| QA-LoRA | WvFoJccpo8.md | 6.33 | R2 (high-mid) | QAT + LoRA paper; addresses a different problem setting |
| Attention-aware PTQ | 0L8wZ9WRah.md | 3.75 | R2 (low-mid) | Hessian-based PTQ; current paper is stronger |
| One QuantLLM | RdG7LVGnQi.md | 4.50 | R2 (low-mid) | OFA framework for quantized LLMs; current paper has stronger empirical results |
| Q-resafe | VarjSNbij7.md | 5.25 | R2 (low-mid) | Safety evaluation of quantized LLMs; different problem altogether |
| Scaling Laws for Precision | wg1PCg3CUP.md | 8.00 | R1 (strong) | Scaling laws; not directly comparable but represents a strong paper |
| CBQ | eW4yh6HKz4.md | 7.60 | R1 (strong) | Cross-block PTQ; very strong execution, cleaner than current paper |
| Judge Decoding | mtSSFiqW6y.md | 8.00 | R1 (strong) | Speculative decoding; unrelated topic but high quality |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>