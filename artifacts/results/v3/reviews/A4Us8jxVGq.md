Now I have sufficient calibration data. Let me write the final consolidated review.

**Calibration summary:**

**Round 1 bracket:** Based on topic and weakness queries, the plausible range was 3.5–6.0.

**Round 2 narrowing:** Inspecting anchors in the 3.0–5.5 range confirmed the most comparable papers (Linear Self-Attention analysis, avg 4.33 rejected; Transformers Higher-Order Optimization, avg 4.25 rejected; Master Syntax paper, avg 3.75 rejected) share similar profiles: genuine theoretical contribution undermined by overclaimed scope, simplified unrealistic architecture, and weak empirical validation of central claims. The Induction Heads paper (avg 6.20, rejected) is stronger and represents an upper bound this paper does not meet.

**Anchor list:**
- IRvx66cxip (2.75) – round1-topic-low; IG enhancement, not topically relevant.
- RBqvU12SHz (3.25) – round1-topic-low; probing paper, not comparable.
- NSBP7HzA5Z (3.00) – round1-topic-low; inductive biases paper, not comparable.
- 89wVrywsIy (3.40) – round1-topic-low; circuit analysis, not comparable.
- uqLQjtSdFN (3.57) – round1-topic-mid; functional gradients for ICL, rejected; more rigorous theory.
- YKzGrt3m2g (4.25) – round1-topic-mid, round2; ICL optimization paper, rejected; theory-experiment gap.
- 1lFZusYFHq (6.20) – round1-topic-mid; induction heads theory, rejected but stronger than this paper.
- 3ddi7Uss2A (7.00) – round1-topic-mid; Hessian analysis, accepted; substantially stronger.
- STUGfUz8ob (7.60) – round1-topic-high, also query-6; symbolic reasoning, accepted; much stronger.
- d8w0pmvXbZ (8.00) – round1-topic-high; training instabilities, accepted; not comparable.
- hNkXTqDrfb (3.75) – round2; syntax-semantics learning, rejected; same issues with overclaiming.
- 4fVuBf5HE9 (4.33) – round2; linear self-attention, rejected; most similar profile: simplified architecture + theory + weak practical link.
- xEZiEhjTeq (5.50) – round2; stagewise development, rejected; better controlled experiments.
- mjDNVksC5G (4.20) – round2; PCA transformers, rejected; overclaimed scope.
- e5lR6tySR7 (4.00) – round2; T-LLMs not general learners, rejected; overclaimed theory.

**Low-band failure analysis:** The low-band anchors (≤3.5) and the weakest mid-band anchors (3.5–4.5) fail primarily because their theoretical contributions do not connect to practical transformer behavior in a causally supported way, and their claims outpace the evidence. This paper shares those failures: the theory is valid for an unrealistic architecture in a vanishingly short step-count regime, but it claims to "validate on practical LLMs" and be the "first explicit characterization" for real transformers. The Pythia validation is methodologically opaque and non-causal.

**Final score:** 4.5. The paper has a genuine theoretical core (closed-form leading-term expressions) and an impressive empirical match in the simplified 3-layer setting, but the architecture gap, step-count regime mismatch, and overclaimed full-scale validation are major issues that prevent this from meeting the acceptance bar.

---

## Summary

This paper develops a leading-term gradient expansion for attention-based transformers at early training, deriving closed-form expressions for weight matrices (output, value, query-key, positional) as compositions of three corpus-derived basis functions: bigram mapping, interchangeability mapping, and context mapping. The theory is validated on a 3-layer simplified transformer trained on TinyStories (using cosine similarity between learned and theoretical weights) and on Pythia-1.4B (through covariance-matrix comparisons). The core theoretical result — that weights at early training approximate interpretable corpus statistics — is a genuine contribution, but several structural issues significantly weaken the paper.

## Strengths

1. **Closed-form expressions for transformer weights in terms of corpus statistics.** Theorem 4.1 provides explicit leading-term approximations for W_O, V, W, and P in terms of bigram (B̄), interchangeability (Σ_B̄), and context (Φ̄) mappings, with rigorous Frobenius-norm error bounds. This goes well beyond prior theoretical work that relied on synthetic languages or non-standard training procedures (Section 4.1).

2. **Near-perfect directional agreement in the simplified 3-layer setting.** Cosine similarity between learned and theoretical weights exceeds 0.99 across all epochs for the small learning rate (Table 1), remains above 0.9 for 30 epochs, and above 0.7 for 100 epochs (Figure 4). This demonstrates that the leading-term features empirically dominate the learned weights far beyond the formal validity window, which is a nontrivial finding.

3. **Interpretable decomposition into three linguistically motivated basis functions.** The bigram mapping B̄, interchangeability mapping Σ_B̄, and context mapping Φ̄ are intuitively grounded in distributional semantics, and the qualitative examples in Figure 5 show that each captures plausible semantic associations (e.g., "fish" linked to "pond"/"lake" under Φ̄). This provides a concrete, testable vocabulary for understanding what early-trained weights encode.

## Weaknesses

### Major

1. **The theory's provable step-count regime is ~5 steps, but the main experimental "verification" runs for hundreds to thousands of steps with no clear acknowledgment of the gap.** Theorem 4.1 requires s ≤ η⁻¹·min(5/(8√T), 1/(12L)). For the TinyStories setup (η=0.005, T=200, L=3), this gives s ≤ 5. The experiments run 100 epochs of SGD (batch size 2048) — many hundreds of gradient steps. The paper labels these experiments "Verification of theory" (Section 5.1) without ever stating the quantitative bound or separating within-regime from beyond-regime evidence. The high cosine similarities after 30+ epochs are an interesting empirical finding about persistence of features, but they do not verify the theorem's error bounds, which are only guaranteed for the first ~5 steps. The paper should report experiments that *respect* the bound (e.g., Frobenius-norm comparison after s=1,…,5 steps) and clearly relegate the long-training results to a robustness check.

2. **The architecture characterized in the theory is far from the practical transformers the paper claims to explain.** The model in Definition 3.1 uses |V|×|V| weight matrices, a shared query-key matrix (no separate Q/K projections), no dimension reduction (embedding dimension equals vocabulary size), and no MLP. Modern transformers compress tokens into a small d_model (typically 768–4096) with distinct Q/K/V projections and low-rank bottlenecks. The paper criticizes prior work for "unrealistic assumptions" (Section 1) but its own architecture is equally unrealistic in different and arguably more severe ways — a vocabulary-sized linear layer is computationally infeasible at scale and removes the central mechanism of representation learning through a bottleneck. The claim of being the "first explicit characterization of weights in attention-based transformers trained on real-world text corpora" is misleading when the characterized architecture is not the one used in practice.

3. **The Pythia-1.4B validation is methodologically unclear and does not provide a causal link to the theory.** The comparison procedure (Section 5.2) involves: (a) computing leading-term matrices from OpenWebText, which is a *different dataset* than the one Pythia was trained on (The Pile); (b) converting Pythia's attention and embeddings into token-token covariance matrices through a process that is ambiguously described (e.g., "covariance matrix of the leading value matrix term" is never precisely defined); (c) comparing these via cosine similarity. The architecture of Pythia (multi-head attention, MLPs, layernorm, tied embeddings, d_model ≪ |V|) differs so substantially from the theoretical model that there is no formal connection. The observed correlations, while suggestive, could arise from many confounding factors. The paper presents no ablation that isolates the contribution of the theoretical terms from other statistical regularities. This does not constitute a validation of the theory for practical LLMs.

4. **The claims substantially outpace the evidence.** The contributions are stated as "first explicit characterization," "interpret the features," and "validate on practical LLM." Given the architecture gap and the step-count regime issue, these are significantly overstated. The novelty is the specific leading-term expansion and the three basis functions, which is a legitimate but incremental theoretical contribution. The Pythia analysis is insufficiently rigorous to support the "validate on practical LLM" claim.

### Minor

5. **The experimental validation uses cosine similarity (scale-invariant) while the theorem (Theorem 4.1) bounds Frobenius norm (scale-sensitive).** Two matrices can have high cosine similarity while differing vastly in scale, so the cosine metric does not directly test the theorem's guarantees. The paper should report a scale-aware metric (e.g., Frobenius norm ratio ||W_learned|| / ||sηB̄||) or normalized distance in addition to cosine similarity.

6. **The theory assumes full-batch gradient descent (Section 3.3) but the experiments use mini-batch SGD with batch size 2048.** Mini-batch noise could alter the dynamics in ways the leading-term analysis does not account for, yet the paper does not discuss this mismatch.

7. **The step-count bound condition "η ≥ 1/T" (Theorem 4.1) is not discussed.** For T=200, this forces η ≥ 0.005, and indeed η=0.005 is used. But what happens for η < 1/T? This regime is excluded without justification.

8. **The per-head analysis (Figure 7) shows that attention heads evolve differently across layers and training, but the theory predicts that all layers share the same leading-term characterization (Theorem 4.1: "all layers have the same characterization").** The paper does not reconcile this apparent tension — if all layers share the same characterization, why do heads in layer 2 behave differently from heads in layer 13? The paper offers a post-hoc story about specialization but the theoretical prediction is uniform.

### Trivial

- The informal theorem statement in the introduction does not convey the stringent step-count constraint, which is critical for understanding the result's scope.
- The construction of Q̄ is described only as a three-step sketch (Section 4.2.2) with no explicit formula in the main text, requiring the reader to consult the appendix.

## Nice-to-Haves

- Test the theory within its *provable regime*: compare weights after s=1,…,5 steps using Frobenius norm or normalized distance, to verify Theorem 4.1's bound directly.
- Scale-aware evaluation: report ||W_learned|| / ||leading term|| ratio or normalized Frobenius distance in addition to cosine similarity, to test whether magnitude as well as direction matches.
- For the Pythia experiments, provide a clearer causal link (e.g., intervention or probing) showing that the degree of agreement with the leading-term prediction correlates with the model's reliance on the three basis functions for specific predictions.
- Verify the predicted *order* dependence: Theorem 4.1 shows W_O ∼ O(sη), V ∼ O(s²η²), W ∼ O(s⁴η⁴). Checking that V grows quadratically with s while W grows quartically would be a strong test of the theory's structure.

## Removed Points

1. **Criticism about missing initialization specification (harsh critic).** The paper references Gaussian and zero initialization in the theorems. The experimental details are in Appendix C (removed from parsed text but present in original submission). This is a reproducibility nitpick the paper likely addresses in the appendix.

2. **Criticism that the paper "does not acknowledge that its own assumptions are also unrealistic" (harsh critic).** The paper does acknowledge it studies an attention-only architecture and cites Wang et al. (2025) showing attention-only models can match MLP-augmented models. However, it does *not* address the |V|×|V| issue — this is kept as a Major weakness (point 2 above) rather than removed.

3. **"The paper should test on a more realistic architecture family" (harsh critic, Nice-to-Haves).** This is a suggestion for future work, not a weakness of the current paper. It would strengthen the paper but is not required for validity.

4. **"Remove or qualify the claim of 'first explicit characterization'" (harsh critic, suggestion).** This is merged into Major weakness 4 (overclaiming).

5. **Strength about "first closed-form characterization on natural language data with realistic architecture" (strength finder).** The architecture is not realistic. This strength is removed.

6. **Strength about "theory transfers to a large-scale practical LLM" (strength finder).** The Pythia evidence is methodologically weak, so this strength overstates the evidence. It is downgraded to a qualified observation.

7. **Strength about "per-head analysis reveals specialization dynamics" (strength finder).** This is an observation, not independently a strength of the theoretical contribution. It's noted in the paper but doesn't rise to a primary strength.

## Novel Insights

Beyond the paper's own contributions, the synthetic review surfaces an important meta-point: the paper's most compelling evidence (cosine similarity > 0.99 in the simplified 3-layer model) is simultaneously its strongest and weakest card — strong because the agreement is remarkably high, weak because the metric (cosine) decouples direction from magnitude and the evaluation runs far outside the provable regime. This tension between "the prediction matches empirically" and "the experiment does not test the theorem's guarantees" is a pattern common in interpretability-theory papers and highlights the need for evaluation protocols that separately verify the theorem's formal claims (error bounds within the stated regime) and probe the empirical robustness of the predicted features beyond it. The paper would be substantially strengthened by cleanly separating these two modes of validation.

## Suggestions

1. Explicitly compute the step-count bound for the reader's chosen hyperparameters and report within-regime experiments (Frobenius norm, first ~5 steps) separately from beyond-regime robustness checks. This would honestly frame what the theorem guarantees and what is empirical serendipity.

2. Either (a) extend the theory to a more realistic architecture with d_model < |V| and separate Q/K projections (even with a low-rank parameterization), or (b) explicitly scope the contribution as characterizing a simplified attention-only model and remove claims about "practical LLMs."

3. For the Pythia analysis, provide a causal link: e.g., show that the degree of agreement with the leading-term prediction correlates with the model's reliance on the three basis functions for specific predictions, perhaps through attention patching or probing. At minimum, report numerical similarity values with confidence intervals rather than only heatmaps.

4. Replace or supplement cosine similarity with a scale-aware metric (normalized Frobenius distance, angle-weighted norm, or the ratio of Frobenius norms) to connect the experiments more directly to Theorem 4.1's Frobenius-norm bounds.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>