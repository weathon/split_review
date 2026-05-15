Now I have all the information needed. Let me write the consolidated review.

---

## Summary
This paper proposes PI-CCA, a replay-free continual learning framework for vision-language models that reframes catastrophic forgetting as drift of the underlying cross-modal alignment geometry. Rather than regularizing proxy signals (logits, similarity distributions), PI-CCA maintains a compact "CCA certificate" — the top-k canonical correlations and sketched canonical subspaces of the whitened image-text cross-covariance — and constrains new updates to preserve these alignment invariants. A prompt-invariance component averages text projectors over template perturbations to improve robustness. Across four standard VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), PI-CCA achieves state-of-the-art results among replay-free methods, including surpassing a synthetic-replay competitor on two tracks.

## Strengths
- **Novel geometric reframing of VL forgetting**: The paper makes a genuine conceptual contribution by recasting forgetting as drift of canonical alignment geometry (spectrum + subspaces) rather than mismatch of proxy signals. This is a clean, principled perspective that unifies the method's design. (Section 3.2, Eqs. 3–6)

- **Replay-free, compact certificate with prompt-invariant averaging**: PI-CCA stores only a small sketched certificate (h×k, independent of feature dimension d) computed via EMA mini-batch statistics, requiring no past data, generator, or reference corpus. The prompt-invariant text basis (Eqs. 5–6) handles sign/rotation ambiguity through projector averaging rather than costly Procrustes alignment — a neat design choice.

- **State-of-the-art across four diverse VL-CL protocols**: Tables 1–2 show PI-CCA achieving best performance among all replay-free methods on MTIL (Avg 76.8%), X-TAIL (Avg 68.1%), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7). It even surpasses the synthetic-replay method GIFT on VLCL and ConStruct-VL, demonstrating that directly constraining alignment geometry can be more effective than data synthesis.

- **Thorough ablation with meaningful insights**: Table 3 isolates each loss term, showing that removing spectral (ℒ_spec) or subspace (ℒ_sub) terms causes the largest drops, confirming both invariants are necessary. The prompt-invariance stress test (Figure 4) cleanly demonstrates that ℒ_pi flattens degradation slopes under increasing perturbation strength. Task-order sensitivity analysis (Figure 5) over 20 random sequences establishes robustness.

- **Pareto analysis of certificate capacity**: Figure 2 identifies a robust efficient frontier for k ∈ [48, 96] and h ∈ [192, 320], showing the method is not brittle to capacity choices and that a small certificate suffices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **PD metric promised but not reported against baselines in main tables**: Section 4.1 states that PD (performance drop on a held-out zero-shot suite) is reported, but Tables 1–2 contain only Avg/Last/Transfer (classification) and R@1/FA/AF (retrieval/structured). The Transfer metric partially addresses zero-shot retention on unseen domains, but a direct PD comparison against baselines — which the paper itself identifies as a metric — would substantiate the central claim about preserving zero-shot ability. PD only appears in Figure 4 as a self-comparison (PI-CCA with/without ℒ_pi).

- **Conceptual link between CCA invariants and CLIP's operational mechanism is asserted rather than justified**: The paper targets preservation of the whitened cross-covariance's canonical spectrum and subspaces, but CLIP's zero-shot recognition relies on unwhitened cosine similarities (or dot products). The relationship between whitened CCA invariants and actual task-relevant alignment is indirect, and the paper provides no formal justification (e.g., bounds relating canonical correlations to downstream margins) that constraining these particular invariants is necessary or sufficient. The empirical correlation evidence (Figure 3) is supportive but does not close this conceptual gap. The framing as a "principled" and "first-class invariant" is somewhat overstated.

- **The "constant memory" claim needs qualification regarding streaming covariance matrices**: The certificate itself is compact (O(hk)), but the streaming EMA maintains full d×d covariance matrices (Σvv, Σtt, Σvt) as described in Eq. 12. For d=768 this is ~7MB — modest in absolute terms but multiple times larger than the certificate. The paper's abstract and introduction emphasize "constant memory" without acknowledging these matrices, though Figure 2's Pareto analysis does include total peak memory measurements.

### Trivial
- **Table 1 lacks standard deviations or confidence intervals** (Table 2 includes them for VLCL/ConStruct-VL). Given that the gains over the second-best method on MTIL are 1.6 percentage points (76.8 vs. 75.2), reporting variance would help readers judge whether these margins are statistically meaningful.

- **The stress test comparison (Figure 4) removes ℒ_pi without adjusting the total loss coefficient budget** (λ₁, λ₂ remain unchanged), so the comparison confounds the presence/absence of ℒ_pi with a change in overall regularization strength. This is a minor experimental design issue that does not undermine the qualitative conclusion.

## Nice-to-Haves
- A direct geometry-drift comparison across methods: measuring D_ang and D_ρ for strong baselines (e.g., C-CLIP, ZSCL) under identical conditions would close the loop on the "geometry-first" argument by showing PI-CCA genuinely reduces alignment drift and that this drift connects to their performance decay.
- A memory breakdown separating certificate storage, covariance EMAs, and LoRA parameters, alongside comparable numbers for baseline methods, to make the "constant memory" claim fully transparent.
- Visualization of what the certificate subspaces capture — e.g., retrieval examples using canonical directions — would make the geometry story more concrete.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Figure 3 perfect correlation is implausible and likely fabricated"** — This accusation is based on an auto-generated image description from the PDF parser (line 241), which lists r=1.00, ρ=1.00. The paper's actual figure caption (line 245) describes "clear positive trends with realistic scatter." The parser's image descriptions are not reliable evidence of paper content. The paper's own text (line 235) says "larger angle/spectral drifts generally imply larger drops" — not perfect correlation. This is a parser artifact, not a paper problem.

2. **"Baselines appear taken from prior works; no description of re-tuning"** — Using published numbers from standardized benchmarks is standard practice in VL-CL literature. All cited methods (ZSCL, C-CLIP, Mod-X, etc.) are established baselines on these exact benchmarks. Demanding re-tuning of every baseline is unreasonable.

3. **"Figure 2 memory numbers implausibly low if full covariance matrices are included"** — Speculative. The paper reports actual measurements on A100-80GB hardware (line 233). Without evidence of measurement error, this criticism is unfounded.

4. **"The paper's own method targets a transformed (whitened) version of the cross-covariance, which is not obviously more 'direct'" (from Section-by-Section notes)** — This misunderstands the paper's claim. The paper argues that prior methods regularize *outcomes* (similarities, logits) while PI-CCA constrains *alignment geometry invariants* directly. Whether whitened or not, CCA invariants characterize the cross-modal relationship in a way that similarity distillation does not. The paper's distinction is meaningful.

5. **"Backward gradient flow through differentiable SVD and whitening is under-specified"** — The paper explicitly addresses this at lines 144-145: stop-gradient on inverse square root if needed, differentiable SVD via power iteration with re-orthogonalization, gradients propagated to M̃ not through the certificate. Implementation details are deferred to Appendix A.1 (stripped by parser). This is adequately specified for the main paper.

6. **Formatting/typo/style complaints** — All parser artifacts. Removed per hard rules.

## Novel Insights
The paper's most genuinely novel observation is that alignment-geometry drift — measured through canonical subspace angles and spectral deviation of the whitened cross-covariance — appears to be a stronger and more direct predictor of VL-CL performance degradation than the proxy signals (similarity matching, logit distillation) targeted by prior work. While the conceptual link between CCA invariants and CLIP's operational mechanism could be tighter, the empirical demonstration that constraining these invariants yields SOTA results across diverse VL-CL protocols is a meaningful contribution that could influence how the community thinks about preserving cross-modal generalization.

## Suggestions
- Add a PD comparison table against major baselines (or clarify in-text that Transfer serves this purpose and explain why PD is not separately tabulated).
- Provide a brief theoretical or empirical justification for why preserving whitened CCA invariants is relevant to unwhitened cosine-similarity-based retrieval — even a simple empirical comparison showing that raw cross-similarity drift correlates less well with performance than CCA drift would strengthen the argument considerably.
- In the revision, add a footnote or sentence quantifying the memory cost of the streaming covariance EMAs relative to the certificate, so the "constant memory" claim is fully transparent rather than inviting nitpicks.

## Score and Decision

### Anchor Comparison
- **Compo-ReAlign (eiTy6AYeQi.md)** — avg 6.0, Accept (Poster): Similar geometry-first reframing for VL-CL, evaluated on compositional DIL and MTIL retrieval. PI-CCA has substantially broader evaluation (4 tracks vs. 2), more baselines, and a more general framework not limited to compositional structure. PI-CCA is clearly stronger.
- **NuSA-CL (tucuU4sQ3s.md)** — avg 5.5, Accept (Poster): Memory-free null-space adaptation for CLIP. Evaluated on MTIL and CIFAR-100 CIL. PI-CCA covers far more diverse tasks (retrieval, structured concepts), has stronger results, and offers a more novel conceptual contribution. PI-CCA is clearly stronger.
- **RLAP-CLIP (rMHZfCznhZ.md)** — avg 6.0, Accept (Poster): RL-based prototype optimization, classification only. PI-CCA's scope (4 tracks including retrieval and structured concepts) and geometric framing are stronger. PI-CCA is somewhat stronger.
- **KeepLoRA (T3Vc5fkTzV.md)** — avg 5.5, Accept (Poster): Subspace-based gradient projection, evaluated on MTIL only. PI-CCA has broader evaluation, more comprehensive baselines, and a more novel conceptual framing. PI-CCA is clearly stronger.
- **Caption-Guided Replay (HN18kuyf4o.md)** — avg 4.0, Reject: Heavy external dependencies, limited novelty. PI-CCA is vastly stronger — replay-free, self-contained, SOTA.
- **Consistent Cross-Modal Alignment (mDuton6Tg7.md)** — avg 3.0, Withdrawn/Reject: Poorly structured, marginal gains. PI-CCA is vastly stronger.

The paper under review has stronger empirical results across more benchmarks than any anchor in the 5.5–6.0 range, with a cleaner conceptual contribution. The weaknesses are real but minor — none threatens the core claims. This places PI-CCA above the 6.0 accept threshold but below the 8.0+ oral-tier papers (which are in different subareas entirely). A score of 6.5 reflects a solid accept with minor weaknesses that the authors can address in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>