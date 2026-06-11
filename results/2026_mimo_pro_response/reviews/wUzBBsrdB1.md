Now I have a good picture. Let me finalize my review.

**Calibration Assessment:**

Round 1 bracket: 6.5–7.5

Key anchors:
- "Sparse Autoencoders Do Not Find Canonical Units" (7.00, Accept): comparable SAE insight quality, similar scope
- "Towards Principled Evaluations of SAEs" (7.00, Accept): similar evaluation framework structure, limited validation
- "A is for Absorption" (7.50, Reject): very similar topic (SAE failure modes with ground truth), narrow validation; our paper has cleaner design
- "Residual Stream Analysis with Multi-Layer SAEs" (6.50, Accept): good but narrower contribution
- "Beyond Interpretability: Monosemanticity and Robustness" (5.80, Accept): weaker experimental design than our paper

Our paper's ground-truth SAE comparison is more convincing than most anchors' core experiments. The c_dec metric is practical. LLM validation is narrow but the paper is honest about it. Comparable in quality to the 7.00 anchors.

Final score: 7.0

---

## Summary

This paper studies the effect of the L0 hyperparameter on Sparse Autoencoders (SAEs) trained to reverse superposition in LLMs. Through carefully designed toy model experiments with ground-truth features, the authors demonstrate that setting L0 too low causes SAEs to mix correlated features ("feature hedging") to improve reconstruction, while too-high L0 produces degenerate solutions. They show that sparsity-reconstruction tradeoff plots are misleading because incorrect SAEs outperform ground-truth SAEs on reconstruction when L0 is too low. They propose decoder pairwise cosine similarity (c_dec) as a proxy metric for identifying the correct L0, validated against sparse probing on Gemma-2-2b and Llama-3.2-1b.

## Strengths

- **Ground-truth SAE comparison directly demonstrates MSE loss incentivizes incorrect features (Section 3.3):** At L0=5, the trained SAE with incorrect latents achieves MSE 2.73 vs. 4.88 for the ground-truth SAE — a clean, quantitative demonstration that the reconstruction objective itself drives SAEs away from the correct solution at low L0.

- **Fundamental challenge to the sparsity-reconstruction tradeoff paradigm (Section 3.4, Figure 4):** The ground-truth SAE achieves worse variance explained than a trained (incorrect, polysemantic) SAE at any L0 below the true value. This directly undermines a core evaluation practice used across the SAE literature (Cunningham et al., 2024; Gao et al., 2024; Rajamanoharan et al., 2024).

- **Asymmetric severity: low L0 universally corrupts all latents, high L0 selectively corrupts (Section 3.2):** When L0 is too high, many latents remain correct; when L0 is too low, every latent is affected. This is a practically important finding that aligns with the observation that most public SAEs have low L0.

- **Cross-architecture validation and architectural insight (Section 3.6, 4.1):** The phenomenon is validated for both BatchTopK and JumpReLU SAEs. The observation that JumpReLU's per-latent threshold provides robustness at high L0, and that λs "sticks" near the correct L0, provides useful guidance for practitioners.

- **c_dec metric transfers from toy models to real LLMs (Figures 6, 7, 8, 9):** The metric's "elbow" coincides with peak K-sparse probing F1 on both Gemma-2-2b and Llama-3.2-1b, across two SAE architectures.

## Weaknesses

### Fatal

None

### Major

- **c_dec metric has significant practical limitations (Section 6, line 246; Figure 8):** The metric can "remain nearly flat for a wide range of L0," visible in the Gemma-2-2b layer 5 results where the curve plateaus from ~L0=250 onward with no clear minimum. The authors resort to an imprecise "elbow" heuristic. The metric also requires training a full sweep of SAEs, making it expensive. The paper acknowledges these limitations, but this means the main practical contribution is more diagnostic than actionable in its current form.

- **LLM validation is narrow for a sweeping field-level claim (Abstract, Section 4):** The abstract claims "most commonly used SAEs have an L0 that is too low," supported by validation on two small models (Gemma-2-2b, Llama-3.2-1b) at 2–3 layers each, with only 3 seeds per L0. Sparse probing is a reasonable but imperfect proxy that does not directly verify monosemanticity. Validation on larger models, more layers, and additional downstream tasks would substantially strengthen the real-world claims.

### Minor

- **Toy model assumes perfect orthogonality and h=g (Section 3, line 65, 73):** Real LLM features are approximately orthogonal and SAE dictionaries are typically much larger or smaller than the "true" number of features. The paper is transparent about this, and LLM experiments provide partial validation, but the sensitivity of conclusions to these assumptions is not explored.

- **Interaction between L0 and dictionary width h is unexplored:** Feature splitting is the dominant known failure mode and interacts with L0. The paper uses h=32768 for LLM experiments but does not investigate whether c_dec identifies the correct L0 across different dictionary sizes, which matters for practitioners who sweep both h and L0.

- **The "Harry Potter" example (line 99) is stated more confidently than warranted:** The claim that "we may expect a nonsensical negative component of 'Harry Potter' to appear in the latent for 'French poetry'" is presented in a toy model section as if describing real LLM behavior without empirical verification.

### Trivial

None

## Nice-to-Haves
- Directly testing a widely-used pretrained SAE (e.g., GemmaScope) against the L0 sweep to demonstrate how far current SAEs' L0 is from optimal, rather than relying on the Neuronpedia survey.
- Exploring whether the flat region in c_dec relates to number of features, correlation structure, or dictionary size.
- A combined metric using c_dec and decoder projection histogram shape (Section 4.2) could be more robust.
- Testing whether optimal L0 varies with training distribution.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's concern that c_dec's limitations make the paper's second contribution less impactful — the paper is fully transparent about these limitations and frames the metric as a diagnostic tool; this is a scope-appropriate observation rather than a valid weakness.
- Any formatting/style nitpicks — parser artifacts, not paper problems.
- Claims about missing appendix content — the appendix exists in the original submission.

## Novel Insights
The paper's most novel contribution is demonstrating that the reconstruction objective *actively incentivizes* incorrect feature learning at low L0 — this goes beyond prior observations that low-L0 SAEs perform worse on downstream tasks, providing a mechanistic explanation through feature hedging. The finding that sparsity-reconstruction tradeoff plots would cause practitioners to reject a ground-truth correct SAE in favor of an incorrect one (Section 3.4) is a genuinely important meta-methodological insight that should reshape how the SAE community evaluates architectures.

## Suggestions
- Investigate c_dec behavior across different dictionary sizes h to assess whether the metric remains informative when both h and L0 are being optimized.
- Take a widely-used pretrained SAE and compute c_dec to directly demonstrate how far current SAEs are from optimal L0.
- Explore combining c_dec with decoder projection histogram shape as a more robust composite metric.

## Anchor Papers Retrieved

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | 8QTpYC4smR.md | 1.00 | Unrelated survey, completely different quality |
| 1 | nSDOkm0SKo.md | 1.00 | Unrelated finance paper |
| 1 | P49gSPmrvN.md | 1.00 | Unrelated visualization paper |
| 1 | gwZ90hFSL2.md | 1.00 | Unrelated NLP paper |
| 1 | tcsZt9ZNKD.md | 1.75 | SAE scaling (Gao et al.); different tool return vs paper score; foundational but different focus |
| 1 | 89wVrywsIy.md | 3.40 | SAE circuit tracing; weaker contribution, rejected |
| 1 | LQdaXixB0g.md | 2.50 | SAE for mental health features; limited scope, rejected |
| 1 | Wxl0JMgDoU.md | 2.50 | SAE for chess model; narrow application, rejected |
| 1 | NB8qn8iIW9.md | 4.00 | Feature-Aligned SAEs; real-world results lack interpretability, rejected |
| 1 | ghH6YYDs15.md | 4.67 | Compute Optimal SAE; theoretical analysis, rejected |
| 1 | F76bwRSLeK.md | 4.80 | Original SAE paper; foundational, accepted at lower score |
| 1 | sknUS8X9q0.md | 4.00 | SAGE ground truth evaluation; presentation issues, rejected |
| 1 | g6Qc3p7JH5.md | 5.80 | Monosemanticity & robustness; weaker experiments, accepted |
| 1 | XAjfjizaKs.md | 6.50 | Multi-Layer SAEs; narrower contribution, accepted |
| 1 | 9ca9eHNrdH.md | 7.00 | SAEs not canonical; comparable insight quality, accepted |
| 1 | 1Njl73JKjB.md | 7.00 | Principled SAE evaluation; similar validation limits, accepted |
| 1 | I4e82CIDxv.md | 8.00 | Sparse Feature Circuits; stronger scope and validation |
| 1 | EytBpUGB1Z.md | 8.00 | Retrieval Heads; different topic, high quality |
| 1 | aWXnKanInf.md | 8.00 | TopoLM; different topic |
| 1 | jOmk0uS1hl.md | 8.00 | Training on test task; different topic |
| 2 | daUQ7vmGap.md | 5.75 | Dynamic sparse training robustness; tangentially related |
| 2 | MDvecs7EvO.md | 6.50 | SAE feature matching across layers; comparable contribution |
| 2 | LC2KxRwC3n.md | 7.50 | A is for Absorption; very similar topic (SAE failure modes with ground truth), rejected despite high score |

**Round 1 bracket: 6.5–7.5.** The paper is clearly above the 5.80 anchor (weaker experiments) and comparable to the 7.00 anchors. It has cleaner mechanistic experiments than "A is for Absorption" (7.50, rejected) but narrower LLM validation. Narrowing to 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>