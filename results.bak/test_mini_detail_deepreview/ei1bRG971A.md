Now I have all the information I need. Let me formulate the final review.

**Round 1 bracket:** between 3.5 and 7.5 (clearly above the reject-range papers scoring 2.5-3.0, clearly below the 8.0+ near-flawless papers).

**Round 2 narrowing:** Compared to CoTFormer (5.75) — DND has stronger empirical evidence across more models/benchmarks but suffers from the loss formulation contradiction. Compared to γ-MoD (6.67) and Learning How Hard to Think (6.50) — DND has a more significant methodological issue than either. Compared to OrthoRank (5.25) — DND is clearly stronger. This places DND around 5.5.

## Summary

This paper proposes Dynamic Nested Depth (DND), a post-training method that selects a subset of "critical" tokens via a learned router and reprocesses them through the same transformer layer (shared weights) to increase effective depth. A router controlling loss (score dispersion + distribution preservation) and an adaptive threshold control scheme (buffer proportional control + EMA synchronization) govern selection. Experiments on three dense 1B models (Qwen3-1.7B, Llama3.2-1B, Gemma3-1B) and a 30B MoE model (Qwen3-30B-A3B) show consistent accuracy improvements of 0.87–2.61% across 11–17 benchmarks with only ~6% extra FLOPs and ~8% throughput reduction.

## Strengths

1. **Consistent and broad empirical validation** — Tables 1 and 2 show that DND improves accuracy across 11–17 diverse benchmarks on four different models spanning both dense and MoE architectures. Gains are particularly notable on complex reasoning tasks (BBH, GPQA, +5% on the 1B models). The verification spans language, math, STEM, coding, and agent benchmarks, providing robust evidence that the method works.

2. **Minimal overhead with meaningful gains** — The method adds fewer than 0.1M parameters and ~6% FLOPs while achieving 91.6–93.1% of vanilla throughput (Table 3). This efficiency-accuracy trade-off is well-documented and competitive.

3. **Training strategy ablation confirms component contributions** — Table 4 systematically ablates router control (RC) and threshold control (TC), showing that each individually provides modest gains (+1.01, +1.05) but their combination doubles the improvement to +1.88. Figures 5–6 further visualize how the EMA-synchronized threshold and buffer control stabilize the selection ratio.

4. **Empirical analysis connects selection to token uncertainty** — Figure 4a shows a positive correlation (r=0.34) between selection frequency and vanilla model logit entropy, and Figure 4b shows that DND reduces entropy for frequently selected tokens (r=-0.58). This directly supports the claim that the router targets uncertain tokens and that reprocessing reduces uncertainty.

5. **Scalability beyond prior work** — The method works as a post-training plug-in on a 30B MoE model, whereas the closest related method (MOR, Bae et al., 2025) requires pretraining from scratch and is limited to 1B parameters (Section 2.2).

## Weaknesses

### Major

1. **The Score Dispersion Loss (Eq. 6) is described in a way that contradicts its stated goal.** The loss is defined as the *negative* entropy of the *normalized* routing scores: L_sd = -Σ p_i log p_i, where p_i = σ(R(x_i)) / Σ_j σ(R(x_j)). Minimizing this loss means maximizing the entropy of the normalized distribution, which pushes the normalized scores toward uniformity (all p_i ≈ 1/N). For the raw sigmoid scores, this means they are driven to be approximately *equal* — the opposite of "discriminative" and "spread out across a wide range" as claimed in lines 136–141 and 153.

   The paper states the goal is to make scores "discriminative enough across tokens" and to "spread out across a wide range" (line 138), but the mathematical formulation achieves the reverse. The Distribution Preservation Loss (Eq. 7) additionally pulls scores toward 0.5. The combination as described would push all scores toward a uniform value near 0.5, collapsing discriminability.

   *Why this is Major, not Fatal:* The ablation (Table 4) empirically shows that using the router control loss (RC) improves results over not using it (+1.88 with both RC and TC vs +1.05 with TC alone). This suggests either (a) the actual implementation differs from the paper's description, or (b) the loss works through a mechanism other than what is claimed. The empirical results are not invalidated, but the paper's framing is incoherent as written. The authors must clarify the formulation and its intended effect — this is the single largest barrier to accepting the paper at face value.

2. **Missing baseline: uniform-depth computation at the same FLOPs.** DND adds ~6% FLOPs by selectively reprocessing 20% of tokens. The paper does not include a baseline where the same amount of computation is added *uniformly* (e.g., inserting an extra transformer layer, or reprocessing all tokens through the same layer). Without this comparison, it is unclear whether the gains come from the *dynamic selection* mechanism (the claimed novelty) or simply from adding more computation to all tokens. This gap weakens the central claim of the paper. Adding this baseline should be straightforward and would substantially strengthen the paper's argument.

### Minor

3. **Single-run results without variance estimates.** All results are presented as single runs (Tables 1–2, 4). For the smaller gains on the 30B model (+0.87 average), it is unclear whether these are statistically significant. LLM SFT can have nontrivial variance across seeds, and reporting means with ranges or standard deviations would strengthen confidence.

4. **Positional embedding reassignment for nested tokens is not discussed.** The nested pass assigns new positional indices to the packed subsequence (Eq. 3). The paper does not discuss whether this creates inconsistencies with the original positional encoding scheme, how the model learns to handle the positional offset, or whether it interacts with the causal attention mask in autoregressive decoding. An ablation or analysis of this design choice would be helpful.

### Trivial

5. **Hyperparameter values for the loss terms** (λ_sd, λ_dp, step size α, smoothing factor γ, buffer size N_b) are deferred to the appendix. These should ideally be stated in the main text or a clear table.

## Nice-to-Haves

- A comparison with ITT (Chen et al., 2025) under matched compute conditions is already partially present (Table 1, Qwen3-1.7B), but the paper could expand to other models.
- The qualitative visualization in Figure 7b is interesting but relies on a single GPQA example. More examples or a systematic analysis would strengthen the claim about hierarchical token processing.

## Removed Points

- *Criticism about unfair comparison with other methods because the asymmetry favors the baseline* — This point was not raised by reviewers. N/A.
- *Criticism that the method cannot be independently verified or that models/tools don't exist* — Not raised; removed per hard rules about cited references being assumed to exist.
- *Formatting/style nitpicks about figure captions* — Removed per hard rules.
- *The harsh critic's claim that the Score Dispersion Loss "invalidates the claimed contribution in its current form"* — Downgraded from "Fatal" to "Major." The empirical results (Table 4) show the method works, so the contradiction is in the textual description/motivation, not necessarily a fatal flaw in the implementation. The results warrant investigation but not rejection.
- *The suggestion to evaluate whether DND's benefit comes from dynamic selection vs. uniform computation* — Retained as a Major weakness; this is a legitimate missing baseline, not a fatal flaw.
- *Strength Finder's generic strengths about "addressing an important problem"* — Removed; every paper addresses an important problem. Only kept strengths that are concrete and specific.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the entropy loss contradiction is the key meta-insight: it reveals a substantive gap between the paper's mathematical formulation and its textual claims that escaped even the strength-finding pass. The calibration comparison reveals that the empirical scope (4 models, 11–17 benchmarks) is well above average for papers in this score band.

## Suggestions

1. **Clarify the Score Dispersion Loss.** The authors must either: (a) correct the sign or formulation so the math matches the claimed goal (e.g., if they want to *minimize* entropy of the normalized scores to make one or a few tokens dominate, use +H(p) instead of -H(p); or (b) use a different dispersion measure such as variance, KL-divergence from uniform, or a contrastive loss) or (c) provide a detailed explanation of why the current formulation empirically produces discriminative scores despite the mathematical contradiction. This is the most critical fix.

2. **Add a uniform-depth baseline** that matches the same ~6% FLOPs increase — either an extra transformer layer inserted at the same location, or a second full-sequence pass through the same layer without selection. This will isolate whether the gains come from dynamic selection or just extra computation.

3. **Report statistics over multiple seeds** (at least 3) for the main results, particularly the 30B model where gains are smaller.

4. **Ablate or analyze the positional embedding reassignment** used in the nested pass (Eq. 3) to confirm it does not harm the model.

## Score and Decision

**Round 1 bracket:** Based on the initial calibration search, the paper is above the reject-range papers (CoTFormer-like at 3.0, FiRST at 3.0) and well below the top-tier papers (8.0+). The plausible range is (3.5, 7.5).

**Round 2 narrowing:** Compared to CoTFormer (5.75, 6/5/6/6) — DND has stronger empirical validation (more models, more benchmarks, better analysis) but suffers from the significant loss formulation issue. Compared to OrthoRank (5.25, 5/5/5/6) — DND is clearly stronger in both method novelty and empirical scope. Compared to Learning How Hard to Think (6.50, 6/8/6/6) — DND has a more serious methodological issue. Compared to γ-MoD (6.67, 6/6/8) — DND's loss formulation concern is more substantial than γ-MoD's issues. DND lands between CoTFormer (5.75) and γ-MoD (6.67), closer to the lower end due to the unresolved loss contradiction. Score: **5.5**.

**Final decision: Reject** — The paper has genuine empirical contributions but the Score Dispersion Loss description is mathematically incoherent with its stated goal, which undermines confidence in the core mechanism. Until the authors clarify or correct this, the contribution cannot be properly assessed. The paper would likely merit acceptance after the loss description is resolved and a uniform-depth baseline is added.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>