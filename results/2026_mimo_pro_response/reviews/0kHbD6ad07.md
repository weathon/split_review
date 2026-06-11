Now I have enough calibration data. Let me finalize the review and score.

**Calibration analysis:**

My Round 1 bracket was between 6.5 and 8.0. Based on the anchors:

- **Rejected papers (5.6–6.4)**: These have theory on simplified/toy models with limited empirical validation. Our paper is clearly stronger — it proves results about real full-scale Transformers and validates with billions of tests on real pretrained models.
- **Marginal accepts (6.3–6.8)**: "Transformers are Universal In-context Learners" (6.67), "Transformers can optimally learn regression" (6.80). These have clean theory but limited empirical validation. Our paper has both stronger theory (extending beyond initialization to training) and far more extensive empirical validation.
- **Clear accepts (7.0–7.6)**: "Learn-to-Optimize" (7.00), "Factual Recall" (7.33), "abstract symbols" (7.60). "Factual Recall" at 7.33 uses a simplified single-layer model with synthetic data; our paper works with full-scale real models. "abstract symbols" at 7.60 relies on kernel regime assumptions; our paper operates at finite width/depth. Our empirical validation is substantially stronger than both.

The theory-algorithm gap (last-token proof vs. all-position-states algorithm) is the main weakness that prevents the paper from reaching 8+. The naming inconsistency and GD-vs-AdamW gap are minor. I place the paper at **7.0** — clearly in the accept range, stronger than marginal accepts, with a clear and novel contribution plus outstanding empirical validation, but with a moderate theory-algorithm gap that tempers the score slightly below the top tier.

---

## Summary
This paper proves that decoder-only Transformer language models are almost-surely injective—distinct prompts produce distinct hidden states—both at initialization and under gradient-based training, using a clean real-analyticity argument. It introduces SIpIT, an algorithm that operationalizes this property for exact prompt recovery from hidden states with provable linear-time guarantees. Extensive empirical validation across 6+ model families and ~5 billion pairwise collision tests with zero collisions supports the theoretical claims.

## Strengths
- **Clean and rigorous proof chain extending beyond prior work**: The three-step argument (Theorem 2.1: real-analyticity of Transformers; Theorem 2.2: injectivity at initialization via the measure-zero dichotomy for real-analytic functions; Theorem 2.3: preservation under GD training via absolute continuity) is mathematically well-structured and addresses a genuine gap over Sutter et al. (2025), who only proved injectivity at initialization with respect to the full hidden-state matrix. The proof sketch for Theorem 2.2—exhibiting a single non-colliding parameter setting to rule out h ≡ 0 (lines 81–89)—is elegant.
- **Massive empirical validation on real pretrained models**: ~5 billion pairwise comparisons across 100K prompts on GPT-2, Gemma-3, Llama-3.1, Mistral-7B, Phi-4, and TinyStories at multiple layers, with zero collisions and minimum pairwise L2 distances consistently above the 10⁻⁶ threshold (§4.1, Tables 1–3, Figure 3). This scale of validation substantially exceeds what is typical for theory papers on Transformer properties.
- **Quantization robustness**: FP4 and INT8 quantization not only avoids introducing collisions but actually *increases* minimum pairwise distances (e.g., Llama-3.1-8B: 1.274 in FP32 → 6.597 in INT8, Table 2), extending the practical relevance of the result.
- **Practical algorithm with provable guarantees**: SIpIT achieves 100% exact token-level accuracy in 28.01±35.87s on GPT-2 Small, vs. BRUTEFORCE's 3889.61±691.17s and HARDPROMPTS' 0% accuracy (Table 5), concretely demonstrating that injectivity translates into an efficient inversion tool.
- **Novel privacy and regulatory implications**: The argument that hidden states are "lossless encodings of the user's exact input, recoverable in full via SIpIT" (line 349) gives the theoretical result immediate practical relevance for data protection law.

## Weaknesses

### Fatal
None

### Major
- **Gap between theoretical guarantee and algorithmic assumption**: The core theorem proves injectivity of the map from prompts to the *last-token* representation r(s; θ) ∈ ℝ^d (lines 37–39), which the paper correctly identifies as "the property of real operational interest" (footnote 2, line 55). However, SIpIT requires access to *all per-position hidden states* H^(ℓ) ∈ ℝ^{T×d} at a given layer (line 141: "here we assume access to all per-position states at a given layer ℓ"). The paper acknowledges this explicitly but the title "injective **and hence** invertible" overstates the connection: the proven property (last-token injectivity) does not directly imply the demonstrated algorithm (which relies on a strictly stronger input assumption plus the separate causal-structure property that position t depends only on the prefix). The theory is still valuable on its own, but the claimed synergy between theory and algorithm is weakened.

### Minor
- **Algorithm naming inconsistency**: The algorithm is called "SIFT" in the abstract (line 9), introduction (lines 17, 21, 23, 25), and §4.2 (line 291); "SIPIT" in §1 (line 45) and §3 (lines 137, 139, 141, 200, 202, 206); "SIpIT" in §3 (lines 167, 171); "SiPT" in Tables 4–5 and §4.2 (lines 309, 313, 319, 321, 323, 325); and "SiPIT" in §6 (lines 345, 347, 349). At least 5 different capitalizations/spellings of the same algorithm is genuinely confusing.
- **GD/SGD theory vs. Adam/AdamW practice gap**: Theorem 2.3 and Corollary 2.3.1 cover GD and SGD with step sizes in (0,1), but the evaluated pretrained models were trained with Adam/AdamW + gradient clipping + learning rate schedules. The empirical results implicitly validate robustness, but the paper doesn't discuss this gap or whether the analyticity argument extends to the augmented state space (θ, m, v).
- **HARDPROMPTS comparison potentially misleading without context**: Table 5 (lines 315–321) shows HARDPROMPTS at 0.00 accuracy alongside SIpIT at 1.00, but HARDPROMPTS operates in a fundamentally different setting (optimizing prompts to match output probability distributions, not recovering from hidden states). The related work (§5) acknowledges the difference, but Table 5 presents them side-by-side without this caveat in the table or caption.
- **Gradient-guided search policy undeveloped in main text**: The gradient-guided policy (referenced as Algorithm 2/3 at line 167) is what makes SIpIT practical—Table 5 shows BRUTEFORCE is ~140× slower. Yet the main text only mentions "gradient-guided search" without describing the mechanism, deferring entirely to the appendix.

### Trivial
None

## Nice-to-Haves
- Briefly acknowledge in §2 that the GD/SGD proof setting differs from the Adam/AdamW training used in practice, noting the empirical results serve as implicit validation.
- Briefly note which of the tested models satisfy the real-analyticity assumption (e.g., GELU-based) and whether ReLU-based models (non-analytic at 0) would require separate treatment, even if Appendix F covers this.
- Inversion sample sizes (100 prompts for GPT-2, 50 for quantized models) could be larger to strengthen practical credibility, though the theoretical guarantee makes even small samples informative.

## Removed Points
These points are flagged to be removed, treat them with caution:
- No criticisms about existence/availability of cited entities — all cited models, benchmarks, and references are treated as existing.
- Pure formatting/style nitpicks removed per policy.

## Novel Insights
The paper's central insight—that real-analyticity of Transformer components, combined with the measure-zero dichotomy for real-analytic functions, yields almost-sure injectivity that persists under gradient-based training—is genuinely novel. The extension from initialization-only results (Sutter et al., 2025) to trained models via absolute continuity preservation under GD updates is the key theoretical advance. The finding that quantization *increases* rather than decreases representational separation is a surprising and practically relevant empirical contribution. The connection between hidden-state injectivity and data protection law is an unusual and valuable interdisciplinary bridge.

## Suggestions
- Unify the algorithm name to a single consistent spelling (SIpIT seems intended) across the entire paper.
- Add 2–3 sentences in §3 describing how gradients w.r.t. the input embedding are used to rank candidates in the gradient-guided policy.
- Add a footnote or caption annotation to Table 5 clarifying that HARDPROMPTS operates in a fundamentally different setting.
- Include one sentence in §2 or §3 acknowledging the gap between GD/SGD theory and Adam/AdamW practice.

## Reporting

**Anchors retrieved across all rounds:**

| Paper Path | Avg Human Score | Round | Comparison |
|---|---|---|---|
| 8QTpYC4smR.md | 1.00 | 1 | Survey paper, not comparable |
| 5kMwiMnUip.md | 1.40 | 1 | Jailbreaking paper, not comparable |
| gwZ90hFSL2.md | 1.00 | 1 | Cross-lingual robots, not comparable |
| nSDOkm0SKo.md | 1.00 | 1 | Financial markets NN, not comparable |
| NSBP7HzA5Z.md | 3.00 | 1 | Inductive transformers, simplified model, weaker |
| uOnElfFuey.md | 3.00 | 1 | Regular language recovery, much weaker scope |
| fSbPwHjdDG.md | 3.00 | 1 | Causal interventions in LLMs, weaker theory |
| 4y3GDTFv70.md | 3.25 | 1 | Latent space theory, weaker empirical validation |
| fp77Ln5Hcc.md | 4.50 | 1 | Depth extrapolation, simplified model |
| MRPCIForrE.md | 4.75 | 1 | Multi-round reasoning, less novel |
| TdgAtxP6G2.md | 4.00 | 1 | Variable-order Markov chains, less novel |
| nxQ0Bjp8zD.md | 5.00 | 1 | Provable ICL for mixtures, narrower scope |
| 1lFZusYFHq.md | 6.20 | 1 | Induction heads theory, simplified model, rejected |
| WULjblaCoc.md | 5.60 | 1 | Counting tasks, simplified model, rejected |
| YE6N8htoFQ.md | 6.00 | 1 | VICL positional encoding, rejected |
| hwSmPOAmhk.md | 7.33 | 1 | Factual recall via assoc. memories, comparable quality, accepted |
| STUGfUz8ob.md | 7.60 | 1 | Abstract symbol reasoning, strong theory, accepted |
| EytBpUGB1Z.md | 8.00 | 1 | Retrieval heads, more empirical, accepted |
| Tzh6xAJSll.md | 7.60 | 1 | Scaling laws for associative memories, accepted |
| aWXnKanInf.md | 8.00 | 1 | TopoLM brain-like organization, different focus |
| 6S4WQD1LZR.md | 6.67 | 2 | Universal in-context learners, accepted but less empirical |
| sLkj91HIZU.md | 6.80 | 2 | Regression mixtures, accepted, less empirical |
| SfNmgDqeEa.md | 6.40 | 2 | Top-k token ordering, mixed scores |
| NHhjczmJjo.md | 7.00 | 2 | Learn-to-optimize, accepted, comparable |
| rUC7tHecSQ.md | 6.33 | 2 | Stacked attention heads, accepted, less rigorous |
| 5Ky0W6sp8W.md | 6.25 | 2 | Buffer mechanism, mixed, rejected |

**Round 1 bracket**: 6.5–8.0. The paper is clearly stronger than rejected papers in the 5.6–6.4 range (which use simplified/toy models with limited empirical validation) and comparable to accepted papers in the 6.7–7.6 range.

**Round 2 narrowing**: Comparing to "Factual Recall" (7.33, Accept) which uses a simplified single-layer model with synthetic data, our paper has much stronger empirical validation on real pretrained models but a slightly weaker theory-algorithm connection. Comparing to "Learn-to-Optimize" (7.00, Accept) which has convergence rate guarantees but limited experiments, our paper has both stronger theory and far more extensive validation. The paper sits above the 7.0 threshold but the theory-algorithm gap keeps it from 7.5+.

**Final score**: 7.0. The paper has a genuine, novel theoretical contribution, outstanding empirical validation, and practical relevance. The theory-algorithm gap (last-token proof vs. all-position-states algorithm) is a real but moderate weakness that prevents a higher score.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>