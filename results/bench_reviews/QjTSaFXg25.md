Now I have a thorough understanding of the paper and both review inputs. Let me verify key claims by cross-referencing the harsh critic's points against the actual paper text, then synthesize the final review.

---

## Summary

This paper argues that the reparameterization trick in prefix-tuning is not merely an engineering heuristic but has a solid theoretical foundation: it implicitly encodes a "shared structure" between prefix key and value vectors. Viewing prefix-tuning through a Mixture-of-Experts (MoE) lens, the authors prove that shared structure yields substantially faster convergence rates for parameter estimation (O_P(√(log n / n))) compared to the non-shared case (potentially as slow as O(1/log n)). Empirical results on 24 vision and language tasks show that prefix-tuning with reparameterization (Deep-share) consistently outperforms the variant without it (No-share).

## Strengths

- **Genuine theoretical insight into a widely-used engineering practice.** The observation that reparameterization implicitly creates a shared structure between key and value prefix vectors (Equation 8: p^K_i = σ₁(p'_i), p^V_i = σ₂(p'_i)) is novel and well-articulated. This reframes a known engineering trick as something with statistical meaning.

- **Rigorous convergence-rate analysis for MoE under shared vs. non-shared structures.** Theorems 2 and 3 establish O_P(√(log n / n)) rates for the shared setting under both linear and one-layer neural network parameterizations. The theoretical machinery (Voronoi loss, identifiability conditions, Taylor expansion decomposition) is non-trivial and technically sound for the simplified regression setting considered.

- **Clear MoE reformulation of prefix-tuning (Section 2.2).** Equation (5) explicitly derives how each attention-head output row can be expressed as a mixture of pre-trained experts and newly introduced prefix experts, with prefix keys acting as score functions and prefix values as expert parameters. This formalization is a useful bridge between the practice of prefix-tuning and the convergence theory.

- **Consistent and substantial empirical gap between Deep-share and No-share.** Across 22 of 24 tasks, Deep-share outperforms No-share. The gaps are large: 16.8% accuracy on Stanford Cars, ~4.5 ROUGE-L on XSUM. The inclusion of Simple-share (identity σ₁, σ₂) as an intermediate ablation helps isolate the effect of shared structure beyond the MLP nonlinearity.

## Weaknesses

### Major

- **Experiments do not measure sample efficiency — the paper's central theoretical claim.** The theory proves faster *convergence rates* under shared structure, but the experiments report only end-of-training accuracy on full datasets. No learning curves, no subsampling at varying dataset sizes, no measurement of convergence rate as a function of n are provided. This means the experiments cannot distinguish between two competing explanations for the Deep-share > No-share gap: (a) genuinely better statistical sample efficiency (the paper's claim) vs. (b) better optimization dynamics from reparameterization (the original motivation in Li & Liang 2021, which the paper acknowledges). Without controlling for optimization (e.g., by tuning No-share's learning rate separately, or showing that No-share fails to catch up even with more data), the empirical results are consistent with both explanations and therefore do not directly support the paper's thesis.

- **The O(1/log n) rate for the non-shared case is asserted rather than derived.** Theorem 1 provides a minimax lower bound of order n^(-1/2) on the Voronoi loss D_{1,r}, which involves r-th powers of parameter errors. The paper then argues this implies parameter errors are at best O(n^(-1/(2r))) and therefore "could be as slow as O(1/log n)." The jump from "worse than O(n^(-1/(2r))) for any fixed r" to "O(1/log n)" is heuristic — taking r to grow with n changes the loss function itself, so the bound no longer applies to the same estimation problem. The qualitative contrast (shared ≫ non-shared) is still valid since the shared case achieves parametric rates while the non-shared lower bound degrades with r, but the precise claim of O(1/log n) is not proved. The paper would be stronger stating the comparison more carefully.

### Minor

- **The theoretical model is a substantial simplification of actual prefix-tuning** (first head, first attention row, quadratic pre-trained scores, known pre-trained experts). This is standard practice in theoretical ML papers and the MoE bridge provides some motivation, but the gap between the regression framework and real transformers with softmax attention, multiple heads, and deep layers is large. The paper acknowledges this scope limitation only in passing.

- **No empirical validation of the MoE interpretation.** The paper frames reparameterization as inducing parameter sharing between score functions and expert parameters in the MoE, but conducts no analysis of learned prompts (e.g., cosine similarity between key and value vectors, or whether sharing patterns emerge without explicit reparameterization) to verify that the trained models exhibit the claimed structural properties. This leaves the MoE narrative as a theoretical bridge without empirical grounding.

- **Standard deviations mentioned but not reported.** The paper states "average accuracy over five independent runs" but no error bars or variance measures appear in Tables 1–2 or Figure 3. For a paper making comparative claims about method superiority, this information should be visible.

### Trivial

- The Voronoi loss construction, while technically necessary, is presented with minimal intuition; its interpretation as a practical error metric remains opaque to a general ML audience.
- The claim that reparameterization is "grounded in deep theoretical foundations" (abstract) slightly overpromises relative to what the theory actually establishes.

## Nice-to-Haves

- **Sample-size scaling experiments:** Training Deep-share and No-share on increasingly large data subsets and plotting accuracy vs. sample size would directly test the sample-efficiency claim and substantially strengthen the paper.
- **Structural analysis of learned prompts:** Measuring similarity (cosine distance, CCA) between final key and value prefix vectors in Deep-share vs. No-share could reveal whether sharing emerges endogenously.
- **Extending theory closer to real transformers:** Incorporating softmax-based attention and multiple heads, even partially, would narrow the theory-practice gap.

## Removed Points

*These points were flagged to be removed; treat them with caution.*

- *"The theoretical model is a drastic simplification that bears no demonstrated relationship to actual transformer attention"* — softened to a minor weakness. Simplified theoretical models are standard practice and the MoE bridge provides some motivation, even if imperfect.

- *"The no-share variant may simply suffer from poor optimization dynamics, not inherently inferior statistical efficiency"* — this is a legitimate concern but is kept as part of the major weakness about experiments not testing sample efficiency, rather than as a separate fatal point. It does not invalidate the theory (which genuinely proves rate differences in the simplified setting), but it does limit what the experiments can conclude.

- *"The MoE interpretation is not empirically connected"* — kept as a minor weakness rather than a separate major gap, since the paper's core theoretical claim (shared structure improves estimation rates) does not strictly require empirical MoE validation.

- *Formatting/style nitpicks, typo complaints* — removed per instructions.

- *Missing appendix claims* — removed; the parser strips appendices.

- *Statistical significance reporting demanded* — this is not standard practice for large-scale benchmark comparisons in this field, so I moved it to minor rather than major.

- *Strength Finder's "concrete proof that shared structure yields faster convergence" regarding O(1/log n)* — weakened. The qualitative comparison holds but the precise O(1/log n) rate is heuristic, not proved.

- *Strength Finder's generic praise about "important problem" and "interesting question"* — dropped per instructions.

- *Criticism demanding the paper extend theory to actual transformer structure* — weakened to nice-to-have. The paper's scope is the simplified setting; criticizing absence of full transformer theory is scope creep.

## Novel Insights

The paper's reframing of the reparameterization trick in prefix-tuning as inducing a shared statistical structure between key and value vectors — and the connection of this to convergence rates in MoE expert estimation — is genuinely novel. Prior work treated reparameterization purely as an optimization stabilizer; this paper offers a statistical (sample-efficiency) rationale. The comparison of rates via Voronoi loss functions for shared vs. non-shared MoE expert estimation, while technically narrow, provides a template for analyzing other PEFT methods through a statistical lens.

## Suggestions

- Add at least one sample-efficiency experiment: subsample each dataset to e.g., 10%, 25%, 50%, 75%, 100% and plot Deep-share vs. No-share accuracy. If Deep-share's advantage grows as data decreases, that directly supports the sample-efficiency claim.
- Report standard deviations in all result tables.
- Clarify the O(1/log n) reasoning: either derive it rigorously or restate as "the rate can be arbitrarily slow (worse than any polynomial rate)."
- Consider a small-scale analysis of learned prompt vectors (key-value similarity) to ground the MoE interpretation empirically.

---

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `7XgKAabsPp` (MoE theory in CL) | 7.33 | Stronger paper: theory is equally simplified but more rigorous in its claims, and experiments directly test the theoretical predictions. Current paper has a larger theory-experiment gap. |
| `v6NNopExN4` (POST) | 5.00 | Roughly comparable: has a novel idea with practical motivation, but suffers from insufficient empirical validation of core claims and unclear practical setup. Similar level of contribution. |
| `Of6tH5yfmK` | 5.33 | Practical prompt-control method with clear experiments but limited novelty. Current paper has more theoretical novelty but weaker empirical validation of its main claim. |
| `8aKygnbEFX` (Hybrid FT) | 4.00 | Weaker paper: theory is derived from prior work, experiments are minimal, novelty is limited. Current paper has a more original theoretical contribution. |
| `gK1rl98VRp` (ICL emergence) | 6.00 | Stronger: theory and experiments are well-aligned, contribution is clearly scoped. Current paper has a gap between what the theory predicts and what the experiments measure. |

The current paper has genuine theoretical contributions (novel convergence analysis connecting reparameterization to MoE estimation rates) and consistent empirical results, but the central sample-efficiency claim is not directly tested by the experiments. This places it around the 5.0 band — above papers with weak theory and weak experiments (4.0), but below papers where theory and experiments are tightly aligned (6.0+).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>