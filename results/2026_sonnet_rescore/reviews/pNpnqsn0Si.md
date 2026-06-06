## Summary

Thoughtbubbles is a GPT-2-style decoder-only transformer that dynamically forks or deletes residual streams between layers during pretraining, using only the standard language modeling cross-entropy loss. A learned scoring function accumulates per-stream importance scores that gate both attention contributions and residual updates (score attenuation), and a hard top-k operation prunes streams at each forking layer. The paper demonstrates consistent validation perplexity improvements over both parameter-matched and computation-matched (Copy-N) baselines across two datasets and three model scales (150M–772M), and includes an interpretable analysis showing that computation is preferentially allocated to moderate-entropy tokens.

---

## Strengths

- **Genuinely novel pretraining architecture.** The forking/pruning mechanism for residual streams—trained without auxiliary supervision, using only LM loss—is a concrete technical contribution. Unlike prior pause-token or thinking-token approaches (Goyal et al., 2024; Herel & Mikolov, 2024; Sun et al., 2025), Thoughtbubbles does not require inserting tokens at manually chosen positions before computation begins; instead, the model learns when and where to branch residual streams mid-network.

- **Consistent perplexity improvements across scale and dataset.** Table 1 and Figure 3 show that Ours (κ=4L) achieves lower validation perplexity than all baselines—parameter-matched Transformer, Copy-3, Copy-5—across both OpenWebText and peS2o at all three scales. The cross-scale result (319M matching 772M Baseline perplexity on OpenWebText) is a striking and specific finding that concretely demonstrates the method's efficiency advantage.

- **Interpretable entropy–computation relationship.** Figure 5 shows a replicable, concave parabolic relationship between token-level output entropy and the number of allocated forks, confirmed against an independently-trained baseline LM's entropy. This directly supports the paper's core claim that the model learns to allocate latent compute at uncertain, not arbitrary, positions—without any supervision signal targeting this behavior.

- **Autoregression distributional shift addressed.** Section 5.1 and Figure 6 demonstrate that the naive fixed-budget autoregressive perplexity diverges from blockwise perplexity, and that dynamic budget scaling (proportional to input length) closes this gap while preserving the advantage over the baseline. This is a non-trivial practical result.

---

## Weaknesses

### Fatal
None.

### Major

- **The computation-matched baseline cannot isolate the adaptivity claim.** The paper's most important efficiency argument is that *adaptive* forking outperforms *non-adaptive* parallel computation at matched compute. The Copy-N baseline (Section 3.3) is the weakest possible instantiation of parallel computation—no learned gating, no selectivity, no layer-wise allocation. This cannot distinguish between "adaptivity helps" and "any parallel residual expansion at this compute budget helps." The paper explicitly cites Goyal et al. (2024), Herel & Mikolov (2024), and Sun et al. (2025) as the most relevant prior methods, yet none appear as baselines. The conclusion states "we demonstrate the power of adaptive latent computation… by demonstrating its superior performance even against computation matched baselines" (§6), but this inference is not licensed by the Copy-N comparison alone.

- **No FLOPs analysis to substantiate the computation-matching claim.** Table 1 states κ=4L is "roughly FLOPs-matched against copy-5 baseline" in a footnote, without any derivation or numerical support. Thoughtbubbles has additional parameters (forking decision networks, fork embeddings per forking layer) and per-layer overhead (score accumulation, top-k operations, score-attenuated attention). Whether the comparison is actually compute-fair is unverifiable from the paper as written.

- **BLiMP pattern is more severe than characterized.** In §4 the paper states "our model only outperforms the parameter-matched, but not computation-matched baselines" on BLiMP. This understates the actual pattern. Examining Table 1: Ours (both κ=2L and κ=4L) falls below even the parameter-matched Baseline on BLiMP in 7 of 12 comparisons (OWT-319M, peS2o-772M, peS2o-319M, peS2o-150M). Against Copy-3, Ours underperforms in 11 of 12 cases. This suggests the forking mechanism consistently trades syntactic competence for perplexity/reasoning gains—a meaningful capacity redistribution that deserves deeper analysis, not a brief attribution to "pruned dynamic parallel computation may not be as helpful for syntax matches."

### Minor

- **Motivation–evaluation gap, acknowledged but unaddressed.** The introduction frames the method as enabling transformers to "solve complex, multi-step problems" and the conclusion states it "allows our model to solve more difficult tasks that require scaling inference-time compute." The evaluation (perplexity, LAMBADA, HellaSwag, BLiMP, PIQA) does not probe multi-step reasoning. The paper appropriately acknowledges this in §8 (hardware limitations for GSM8K), but the gap between the headline motivation and the actual evidence scope remains wide.

- **The non-differentiable top-k gradient bottleneck is a real limitation with no ablative evidence.** Section 8 explicitly acknowledges that hard top-k truncates gradients to high-scoring early-layer streams that are later pruned, degrading the scoring function quality. No comparison against differentiable relaxations (straight-through, Gumbel-softmax) or randomized top-k is provided. Given that the scoring/attenuation mechanism is what distinguishes Thoughtbubbles from Copy-N, quantifying the degree of degradation due to gradient truncation is important.

- **Autoregression mitigation detail deferred entirely to appendix.** The distributional shift between blockwise forward pass and autoregression, and its mitigation via dynamic budget scaling (Section 5.1, Appendix E.1), is non-trivial and required for reproducing the reported perplexity results. A description of the scaling rule belongs in the main text, not only in the appendix.

### Trivial

- No variance estimates or statistical significance tests anywhere in Table 1. On HellaSwag gains of 1–2 percentage points this matters. Single-run evaluation is common at this scale, but at minimum an acknowledgment would help.

---

## Nice-to-Haves

- An ablation comparing the full method (adaptive top-k + score attenuation) against a fully deterministic version (fork every token at every forking layer, no pruning, no attenuation) would directly isolate whether adaptive allocation drives the gains or whether any parallel expansion at this compute budget suffices. This could be done at 150M scale at low cost.
- A sweep of κ (from 1×L to 4×L) with actual FLOPs per forward pass plotted against perplexity—alongside the Copy-N baselines at their respective FLOPs levels—would turn the efficiency narrative from a qualitative claim into a concrete curve.
- The concave entropy–fork relationship (Figure 5) is interesting but the paper's explanation (high-entropy tokens are "edges of clauses or coreferences where additional computation will not help") is speculative. A small qualitative case study showing example tokens at each entropy regime would make this interpretation more convincing.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **"First-known architecture" claim is too broad (Graves 2016).** The critic raises Adaptive Computation Time (Graves, 2016) and Universal Transformers as counterexamples. However, the paper's claim is specifically "unsupervised dynamic allocation of *latent parallel* computation" — not adaptive computation generally. Graves (2016) is sequential and recurrent (halting, not forking parallel streams); Universal Transformers vary depth, not parallel stream count. The specific combination of features (parallel stream forking, no explicit token insertion, trained with only LM loss) is genuinely novel. The paper also explicitly cites Graves (2016) in §6 Related Work with accurate characterization. *Removed as mischaracterizing the claim.*

- **Output averaging mixes probability distributions, not logits (§2.5, Eq. 11).** The critic notes that averaging softmax outputs rather than logits makes this a mixture of categoricals. This is a real design choice with implications for gradient behavior, but mixture-of-softmax is a recognized and principled approach (e.g., Yang et al., 2018). The critic's concern that low-scoring forks "contribute negligibly" is exactly the intended behavior — low-scoring streams should contribute little. The log-sum-exp implementation (cited as Blanchard et al., 2021) handles stability. *Demoted: design choice may be suboptimal but is not obviously wrong and is not the main driver of any identified failure.*

- **Attention scores are unreliable proxies for causal influence (Figure 4).** Valid general concern in interpretability. However, the analysis in Figure 4 is presented as supporting evidence for fork utility, not as a causal proof. The stronger interpretability evidence is Figure 5 (entropy correlation). *Demoted to speculative; the analysis claim is appropriately hedged.*

- **Score learning asymmetry for rightmost tokens (§2.3, Eq. 4).** The forced-maximum keep score for rightmost tokens creates asymmetric gradient paths. This is a real design tension the paper does not discuss. However, the paper explicitly notes this choice ensures token survival across layers (§2.3), which is a correctness requirement. Whether the asymmetry materially affects performance is unknown. *Retained as a note but demoted to minor design tension not verified to cause measurable harm.*

- **Forking layer placement (layers 3, 7, 11) discussed only in appendix B.** Valid that this is a significant design decision. The paper acknowledges in §8 that too-early forking causes gradient bottlenecks. *Moved to nice-to-have; appendix exists per the rules.*

---

## Novel Insights

The most genuinely novel insight from the reviews—confirmed against the paper—is the concave parabolic relationship between token entropy and forking allocation (Figure 5): the model allocates *less* parallel compute to its highest-entropy tokens than to moderate-entropy ones, and this pattern is confirmed against an independently-trained baseline LM's entropy estimates. This is an emergent behavioral regularity, arising from no explicit entropy-targeting supervision, that carries interpretive implications beyond Thoughtbubbles itself: it suggests that the informative regime for latent compute expansion is *disambiguation* (moderate uncertainty), not maximum novelty (high uncertainty). This aligns with the position in Wang et al. (2025) cited in the paper and could inform future adaptive computation architectures.

---

## Suggestions

1. **Replace or supplement Copy-N with at least one pause-token method.** Re-implement Goyal et al. (2024) or Herel & Mikolov (2024) at 150M scale. This is the single highest-leverage improvement: it directly tests whether *adaptive* forking outperforms *non-adaptive* token insertion at matched compute, which is the paper's central efficiency claim.

2. **Report FLOPs per forward pass for all configurations in Table 1.** Even a single-row FLOPs table would make the "roughly FLOPs-matched" claim verifiable and strengthen the efficiency argument.

3. **Clarify and expand the BLiMP discussion.** The current characterization is inaccurate: Ours underperforms even the parameter-matched baseline on BLiMP in most peS2o conditions. Acknowledge and investigate whether this is an artifact of forking disrupting syntactic structure, or of the short training run.

4. **Move the dynamic budget scaling rule into the main text.** Since this is required for reproducing the reported perplexity numbers, it belongs in §2.6 or §5.1, not only in Appendix E.1.

5. **Add a deterministic-forking ablation at 150M scale.** Fork every token at every forking layer with no top-k, no score attenuation, same κ. This directly tests whether adaptive allocation is responsible for the gains over Copy-N.

---

**Originality:** The forking mechanism and unsupervised residual stream pruning are a genuinely novel architectural contribution. Score: high.

**Importance of research question:** Adaptive inference-time compute for pretrained LMs is an important and timely direction. Score: high.

**Claims supported:** Perplexity improvements are well-supported; the adaptivity claim over Copy-N is unsubstantiated; BLiMP characterization is misleading; reasoning motivation is untested. Score: moderate.

**Soundness of experiments:** The pretraining setup is standard and consistent; the baseline comparison is structurally weak for the central claim; no FLOPs analysis. Score: moderate.

**Clarity of writing:** Generally clear and well-organized; BLiMP characterization is inaccurate; the autoregression mitigation is under-described in the main text. Score: moderate.

**Value to research community:** The mechanism and analysis are interesting; the pretrained model release adds value; the limitation acknowledged in §8 (hardware-constrained evaluation scope) reduces near-term practical relevance. Score: moderate.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>