## Summary

This paper introduces Thoughtbubbles, a transformer variant that learns to dynamically fork and prune residual streams during pretraining using only language modeling loss. The key idea is that tokens requiring more computation can spawn "bubbles" of cloned residual streams in mid-network layers, which are later merged via score-weighted averaging. The method is evaluated across 150M–772M parameter scales on two datasets (OpenWebText, peS2o), consistently achieving lower perplexity and better zero-shot performance on LAMBADA and HellaSwag than both a parameter-matched vanilla transformer and computation-matched copy baselines.

## Strengths

- **Novel and well-motivated architecture for unsupervised dynamic latent computation.** The forking mechanism (Section 2.3) with cumulative scoring, top-k pruning, and score-attenuated attention (Section 2.4) is a coherent design that enables token-adaptive parallel computation trainable from LM loss alone — a genuinely new capability not present in either vanilla transformers or fixed pause-token approaches. This is the paper's core contribution and it is clearly articulated.

- **Consistent empirical advantage across scales and datasets.** Table 1 shows that Thoughtbubbles (κ=4L) achieves lower validation perplexity than all baselines at every scale (150M, 319M, 772M) on both datasets. At 772M on OpenWebText, perplexity drops from 21.22 (baseline) to 19.74 (a 7% relative improvement), and the method outperforms baselines on LAMBADA and HellaSwag. The improvement is systematic, not cherry-picked: it holds for both κ=2L and κ=4L variants and across both datasets.

- **Interpretable computation allocation.** Figure 5 provides direct evidence that the forking decisions correlate with token uncertainty: the number of forks increases with mean output entropy (measured both by the forking model and an independent baseline decoder). This shows the model is learning to allocate computation where it is most needed, without any auxiliary supervision — a clean validation of the method's motivating principle.

- **The 319M model beats the 772M baseline in perplexity** (Figure 3), demonstrating that adaptive forking can substitute for raw parameter count. This is a striking result that goes beyond marginal gains and speaks to a genuine architectural advantage.

## Weaknesses

### Major

- **No ablation studies.** The method combines multiple design choices: forking layers at specific depths, score attenuation (Eqs. 8-10), top-k pruning, forced right-token survival, cumulative score propagation, and output averaging with weighted logits (Eq. 11). None of these components are isolated. It is therefore impossible to attribute the gains to adaptive forking per se vs. the overall increase in effective capacity or the specific attenuation mechanism. At minimum, an ablation that compares (a) forking without score attenuation vs. (b) score attenuation on a non-forking baseline would clarify the mechanism.

- **Single training run per configuration with no variance estimate.** All results in Table 1 come from a single seed. At 2.5B tokens of pretraining, stochasticity in optimization is non-negligible. Improvements of 1–2 perplexity points and a few percentage points on zero-shot benchmarks could be within run-to-run noise. Three seeds for at least one scale (e.g., 150M) with mean and std reported would significantly strengthen confidence in the findings.

- **No direct comparison to adaptive-computation methods from prior work.** The paper discusses pause-token approaches (Goyal et al., 2024; Herel & Mikolov, 2024; Sun et al., 2025) in Related Work but does not compare against them experimentally. The copy baseline (duplicating input tokens) is a useful non-adaptive control for computation matching, but it does not represent the closest prior art. A comparison to a fixed-budget "thinking token" model (e.g., inserting a learnable number of special tokens at each layer) would directly test whether the *dynamic* (token-adaptive) aspect of forking provides additional value over uniform extra streams.

### Minor

- **Parameter-matching claim lacks transparency.** The table header says "Each setting is parameter-matched," but the forking mechanism adds extra parameters: the per-layer decision function \(f_\theta^{(k)}: \mathbb{R}^{d_{\text{model}}} \to \mathbb{R}^2\) and per-layer learned fork embeddings \(v_\theta^{(k)} \in \mathbb{R}^{d_{\text{model}}}\). For 3 forking layers at 150M scale (d_model≈768), this is roughly 7K extra parameters (~0.005% of total) — negligible in practice, but the paper should state explicitly whether the baseline's hidden dimension or layer count was adjusted to compensate. This is a presentation gap, not a fatal flaw, but it should be fixed.

- **The forking decision function \(f_\theta^{(k)}\) is underspecified.** The paper defines its signature (\(\mathbb{R}^{d_{\text{model}}} \to \mathbb{R}^2\)) but never states whether it is a linear layer, a small MLP, or something else. This matters for both parameter counting and reproducibility.

- **Some downstream results are mixed.** On BLiMP, Thoughtbubbles underperforms the copy baselines at multiple scales (e.g., 772M OpenWebText: baseline 79.6, copy-3 81.2, ours κ=4L 81.6 — actually best, but at 319M: baseline 79.0, copy-3 80.5, ours κ=4L 78.8). On PIQA, results are inconsistent with no clear signal. The paper attributes this to syntax not benefiting from dynamic computation, but this is speculative without ablations that control for the mismatch.

### Trivial

- The description of the top-k operation (Section 2.3, around Eq. 4-6) could be clearer about whether k = κ − N (the number of available slots) or a fixed value, and how many streams can be added vs. kept.

## Nice-to-Haves

- A wall-clock time comparison (training and inference) would be valuable for practitioners, since the paper notes in Limitations that raw efficiency is relatively low.
- A per-token or per-frequency-bin breakdown of perplexity gains would complement the entropy analysis and test whether gains concentrate on rare or ambiguous tokens.
- The "partial rotation" for RoPE position embeddings (deferred to Appendix D) is a non-trivial design choice and deserves a brief explanation in the main text.

## Removed Points

- **"Parameter-matching claim is misleading and likely false" (Harsh Critic #1).** Removed as a fatal weakness. The extra parameters from 3 forking layers (linear d_model→2 projections + d_model-dimensional fork embeddings) total ~7K for a 150M model — under 0.005% of total parameters. This is well within rounding error of a "parameter-matched" claim, and there is no evidence the paper misrepresents the model sizes. The critic's assertion that the decision function is an "MLP" is unsupported; the paper describes it as \(f_\theta^{(k)}: \mathbb{R}^{d_{\text{model}}} \to \mathbb{R}^2\) with sigmoid activation, which is most naturally interpreted as a linear projection. Demoted to Minor and reworded.

- **"No code release" (Harsh Critic, Missing Parts).** Removed per hard rule: the paper states "URL will be available upon acceptance," which is standard for double-blind review.

- **"Missing related works" implicit in critic's baseline criticism.** Removed per hard rule: the paper cites and discusses pause-token works (Goyal, Herel, Sun) in Related Work. The criticism that they are absent is refuted by the paper's content.

- **Several formatting/style nitpicks.** Removed per hard rule.

- **Strength Finder strengths that are generic or conflict with verified weaknesses.** The strength "First demonstration of unsupervised dynamic latent parallel computation at scale" is valid and kept. The general framing claims ("this paper addresses an important problem") are removed as generic.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable concerns (ablations, variance, baseline selection) but do not offer a novel reframing of the paper's findings or identify a hidden flaw or missed opportunity that the authors themselves missed. The entropy-computation correlation (Figure 5) and the 319M-outperforms-772M scaling result (Figure 3) are the two most striking findings in the paper, and the reviews correctly identify them as strengths.

## Suggestions

1. **Run ablations** isolating: (a) score attenuation vs. no attenuation, (b) the number and placement of forking layers, (c) the top-k budget κ, and (d) forced right-token survival. Even a single-scale ablation at 150M would substantially strengthen interpretability.
2. **Report 3 seeds** for at least the 150M scale with mean and std for perplexity and key zero-shot metrics.
3. **Add a pause-token baseline** — e.g., inserting a fixed number of learnable "thinking" tokens at input or at each forking layer, trained identically. This would isolate the value of *dynamic* forking over uniform extra streams.
4. **Clarify the parameter-matching mechanism** explicitly in the experimental setup: state which architectural dimensions (if any) were adjusted to compensate for the forking parameters, and report total parameter counts to one decimal place.
5. **Specify the forking decision function** architecture (likely a linear layer) in Section 2.3.

## Score and Decision

### Calibration

**Round 1 bracket (wide):** The paper was compared against anchors in three bands:
- Low band (avg < 3.5): vnp2LtLlQg (3.00, attention optimization), bntJK4NyIW (2.00, decentralized training), BjZP3fTlVg (3.00, efficient LLM deployment), 2DD4AXOAZ8 (2.00, MixAttention) — all clearly worse than Thoughtbubbles, being more applied or narrowly scoped.
- Middle band (3.5–7.5): 7igPXQFupX — CoTFormer (5.75, accepted, similar adaptive-computation architecture); XAjfjizaKs — MLSAE (6.50, residual stream analysis); 8ZPLn3GCDb — Neutral Residues (4.33, adapters); 0JjsZC0w8x — COrAL (5.75, order-agnostic LM).
- High band (avg > 7.5): PdaPky8MUn (8.00, long-sequence priors), vf5aUZT0Fz (8.00, DEPT), vrBVFXwAmi (8.00, quantum property estimation), STUGfUz8ob (7.60, abstract reasoning) — these are polished papers with thorough evaluations, clearly stronger than Thoughtbubbles.

**Initial bracket:** 4.5 – 7.0.

**Round 2 narrowing (inside bracket):** I read four anchors in full:
- CoTFormer (5.75): Topically closest — adaptive computation architecture, accepted. CoTFormer was weaker than Thoughtbubbles: trained on only 256-length sequences, less comprehensive evaluation. However, CoTFormer at least had some ablation and analysis.
- Hyper-Connections (6.25): Thorough ablations, multiple domains. Stronger presentation and evidence than Thoughtbubbles.
- Forgetting Transformer (6.75): Clean idea, thorough evaluation with ablations. Stronger overall evidence presentation than Thoughtbubbles.
- COrAL (5.75): Novel decoding paradigm, but limited generalization and limited baselines.

**Final calibration:** Thoughtbubbles is clearly stronger than CoTFormer (5.75) due to larger-scale training, more comprehensive evaluation, and interpretability analysis. It is weaker than Forgetting Transformer (6.75) and Hyper-Connections (6.25) due to missing ablations, single-run results, and no pause-token baseline comparison. The paper sits between these anchors. The 319M-outperforms-772M result is genuinely striking and elevates the contribution above a routine architectural tweak, but the evidence gaps prevent it from reaching the 6.5+ tier.

**Final score: 6.0**

<score>6.0</score>
<decision>Accept</decision>