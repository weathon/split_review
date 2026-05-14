Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper introduces **Thoughtbubbles**, a novel transformer variant that enables unsupervised, input-adaptive parallel computation during pretraining by learning to fork (duplicate) or delete residual streams in latent space. A cumulative scoring mechanism combined with top-k selection determines which tokens receive extra computation, and the model is trained end-to-end with only the standard language modeling loss. The method consistently outperforms both parameter-matched standard transformers and Copy-K baselines (where input residuals are replicated) on validation perplexity across 150M–772M parameter scales on OpenWebText and peS2o, with smaller but positive gains on LAMBADA and HellaSwag zero-shot evaluations.

## Strengths

- **Genuinely novel architectural contribution**: The forking/deletion mechanism with cumulative scores and top-k selection is original among adaptive-compute transformer approaches. The combination of fork creation, score-weighted attention attenuation, and output averaging via cumulative scores forms a clean, unified mechanism (Section 2.3–2.5, Figures 1–2).

- **Training simplicity**: The entire system trains with only the standard LM cross-entropy loss, requiring no auxiliary objectives, reinforcement learning, or explicit reasoning supervision. This is a pragmatic advantage over methods requiring specialized training pipelines (Section 2.1, Section 3.1).

- **Consistent perplexity improvements with fair baselines**: Across all model scales (150M–772M) and both datasets, Thoughtbubbles achieves lower validation perplexity than both parameter-matched and Copy-K baselines. The Copy-K baseline (duplicating input residuals K times before the transformer) is a reasonable attempt at computation-matching. Notably, the 319M Thoughtbubbles model with κ=4L achieves lower OpenWebText perplexity than the 772M parameter-matched baseline (Figure 3, Table 1).

- **Meaningful attention to forked tokens**: Analysis shows the rightmost ("original") token attends to its spawned forks with attention weights more than an order of magnitude above other tokens, confirming that forked residual streams actively contribute to the final representation (Figure 4, Section 5).

- **Practical inference adaptation**: The dynamic forking budget scaling method (scaling κ proportionally to input length during autoregression) effectively mitigates the distribution shift between blockwise forward passes and autoregression, preserving perplexity close to the blockwise baseline (Figure 6, Appendix E.1).

- **Honest reporting of limitations and mixed results**: The paper acknowledges that BLiMP and PIQA results are mixed, that the entropy-forking relationship is parabolic rather than monotonic, and that the top-k gradient bottleneck exists. The CLUTRR analysis in the appendix adds useful qualitative evidence.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Modest training scale**: All models are trained on only 2.5B tokens (75,000 steps at batch size 64 with block size 512). For the 772M parameter models, this is well below convergence. Properties the paper claims (emergence of adaptive computation, interpretable forking) may not manifest reliably at this scale, and the scaling trends in Figure 3 are preliminary. The paper acknowledges hardware limitations but does not discuss whether the observed effects might strengthen or weaken with more training.

- **Entropy-forking relationship is parabolic, not monotonic**: The paper shows a concave parabolic relationship between entropy and forking allocation—the model allocates *less* computation at the highest-entropy tokens and peaks at moderate entropies (Figure 5). The paper provides a post-hoc hypothesis (Section 5) but does not test it. The claim of "interpretable" computation allocation at regions of uncertainty is partially supported but the reversal at high entropy complicates the narrative. This does not invalidate the core contribution but weakens one of the paper's three headline claims.

- **Gradient bottleneck acknowledged but unresolved**: The hard top-k selection means tokens below the threshold receive no gradients for the forking decision function. The paper acknowledges this in Limitations but only speculates about mitigation via "training time randomization and noise." While the method demonstrably works (perplexity improves), the paper does not analyze how much gradient signal reaches the forking parameters, which leaves open the question of whether the gains come from learned adaptive forking or other components (e.g., the attenuation mechanism alone).

- **BLiMP and PIQA results are mixed**: On BLiMP, Copy-3 or Copy-5 often outperform Thoughtbubbles (e.g., peS2o 150M: Copy-3 gets 79.3 vs. Ours κ=2L at 77.5). On PIQA, results are essentially at parity. The paper acknowledges this honestly but does not analyze whether forking is occasionally harmful (deleting syntactically relevant tokens). This limits the "outperforms all baselines" claim (Table 1, Section 4).

### Trivial

- The paper states κ=4L is "roughly FLOPs-matched against copy-5" (Table 1 caption), but the Copy-5 expanded sequence length (2560) is larger than the κ=4L maximum budget (2048), meaning Copy-5 consumes more attention FLOPs. The comparison is actually conservative (favors the baseline), so this is a minor imprecision in the text rather than a methodological flaw.

- The claim that CoT "cannot be applied during pretraining" (Abstract, line 13) overstates the case—some works do train with CoT-style traces during pretraining, though the broader point about serial natural-language verbalization being qualitatively different from latent parallel computation is valid.

## Nice-to-Haves

- **Ablation of the score attenuation mechanism without forking**: Removing the forking mechanism entirely but keeping the cumulative score attenuation of attention and residual updates would isolate whether the gains come from the adaptive allocation or from the soft-penalization of less-important tokens.

- **Quantitative analysis of gradient flow to forking parameters**: Measuring the fraction of tokens at each forking layer that receive non-zero gradients would help quantify the severity of the gradient bottleneck and clarify whether the forking mechanism is genuinely learning or relying on simpler heuristics.

- **Larger-scale training**: Scaling to a regime where models can converge (≥10B tokens for 772M parameters) would determine whether the adaptive forking phenomenon strengthens or weakens with more training, and whether the perplexity gap over baselines persists.

- **Comparison with Mixture-of-Depths** (Raposo et al., 2024): MoD also uses learned token-level routing for dynamic compute allocation. An experimental comparison would help situate Thoughtbubbles relative to the closest existing approach, though the paper's Copy-K baseline already provides a reasonable computation-matched comparison point.

- **More rigorous CLUTRR analysis**: The qualitative analysis in Appendix C (Figure 7) is promising. Quantitative metrics (e.g., correlation between forking locations and ground-truth reasoning steps) would strengthen the claim that forking tracks task difficulty.

## Removed Points

These points are flagged to be removed; treat them with caution.

**1. (Harsh Critic, Critical Issue 1) Computation-matched baseline invalidates central claim.** The harsh critic argued that Copy-K baselines use more computation than Thoughtbubbles, making the comparison invalid. *Removed because:* The direction of the asymmetry actually **favors the baseline**—Copy-5 has expanded size 2560 vs. κ=4L max 2048, meaning Copy-5 uses more attention FLOPs. If anything, Thoughtbubbles' outperformance is *more* impressive because it uses less computation. The critic's conclusion (that the comparison is invalid) is factually wrong about the implication of the numbers.

**2. (Harsh Critic, Critical Issue 2 — overclaimed) "Interpretable" label is overclaimed.** *Weakened and retained as minor:* The paper does NOT claim monotonicity; it explicitly acknowledges the parabolic shape and offers a hypothesis. The criticism that the hypothesis is untested is valid and retained in Minor Weaknesses.

**3. (Harsh Critic, Section-by-section) Score attenuation is "circular."** *Removed because:* The mechanism is not circular. The attenuation penalizes low-score tokens, creating a training signal that encourages the model to assign high scores to tokens it needs. The critic's interpretation misunderstands the mechanism.

**4. (Harsh Critic) Appendix B overforking "directly contradicts the claim that dynamic allocation is universally beneficial."** *Removed because:* The paper never claims universal benefit. The result that some forking helps but too much hurts is consistent with the paper's narrative.

**5. (Harsh Critic) Figure 4 attention to child forks could be a proximity artifact.** *Weakened:* The paper places forks adjacent to parents, so proximity is a confound. But the magnitude of the difference (an order of magnitude) makes a pure-proximity explanation unlikely. Not a significant concern.

**6. (Strength Finder) "Fair experimental design" claimed as a strength.** *Retained with qualification:* The Copy-K baseline is a reasonable attempt at computation matching, and the asymmetry actually favors the baseline (see Removed Point 1).

**7. (Harsh Critic) Missing comparison with Mixture-of-Depths and pause token works.** *Moved to Nice-to-Haves:* While comparing against the closest prior work would strengthen the paper, the Copy-K baseline already provides a reasonable computation-matched comparison, and the paper's contribution is architectural novelty rather than SOTA benchmarking.

**8. (Harsh Critic) Training budget criticism saying properties "may not manifest reliably."** *Retained as minor weakness:* This is a valid concern but does not invalidate the results shown.

**9. (Harsh Critic) Various formatting/style issues.** *Removed:* These are parser artifacts or style nitpicks.

**10. (Harsh Critic) Undisclosed hyperparameters, missing training logs.** *Removed:* The paper provides architecture details in Appendix A (Table 2, Table 3) with optimization parameters, model topology, and batch accumulation settings. The request for complete training logs is impractical for a submission.

**11. (Harsh Critic) Missing related works.** *Removed per hard rules.*

**12. (Harsh Critic, Section-by-section) "CoT cannot be applied during pretraining" is misleading.** *Retained as trivial:* The broader point stands but the phrasing is imprecise.

**13. (Harsh Critic) BLiMP results "deserve analysis rather than dismissal."** *Retained as minor:* The paper does acknowledge the mixed results. The lack of deeper analysis is a minor limitation.

**14. (Harsh Critic) Forking only at layers 3, 7, 11 "fundamentally limits the mechanism."** *Removed:* The paper has an ablation in Appendix B showing that extended forking actually hurts performance. The restricted placement is a deliberate design choice supported by evidence, not a limitation.

**15. (Strength Finder — dropped strengths):** None dropped; all verified strengths had specific evidence from the paper.

## Novel Insights

The paper's most interesting finding is the concave parabolic relationship between token-level output entropy and forking allocation (Figure 5). The model allocates more computation at moderate-entropy tokens—where choosing between a few plausible options might benefit from extra computation—but reduces allocation at the highest-entropy tokens. This contrasts with a naive expectation that computation should monotonically track uncertainty. The authors hypothesize that highest-entropy regions often involve clause boundaries or coreferences where extra computation cannot help, which is plausible but untested. If validated, this would suggest that the model learns to distinguish *resolvable* from *irresolvable* uncertainty—a more sophisticated allocation strategy than simple uncertainty-driven computation.

## Suggestions

- The CLUTRR qualitative analysis (Appendix C) should be moved to the main text with quantitative metrics (e.g., correlation between forking locations and ground-truth reasoning steps). This is the paper's most compelling evidence for adaptive, task-relevant allocation.
- Add a table quantifying FLOP counts for each model variant to make the computation-matching claim precise rather than "roughly FLOPs-matched."
- Report R² or similar correlation metrics for the entropy-forking relationship in Figure 5 to quantify the strength of the observed pattern.
- Clarify the role of the forced-maximum keep score (Eq. 4) relative to the non-forced cumulative score propagation. The interaction between these two mechanisms is subtle and could confuse readers.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Decision | Comparison to Thoughtbubbles |
|------|-----------|----------|------------------------------|
| exMMxIakjl (Subjective Depth/Timescale Transformers) | 3.00 | Reject | TB has consistently positive results (beats baselines on perplexity) vs. conditional models below dense baseline; TB mechanism is more novel |
| RV43b2B1SC (The Free Transformer) | 3.00 | Reject | TB has more sophisticated mechanism (forking + deletion vs. simple VAE conditioning) and better baselines |
| GXbTHRBSA4 (ACTS) | 4.00 | Reject | TB contributes a new architecture trained from scratch vs. an inference-time heuristic; TB's contribution is more substantial |
| J7vpYSsdeO (Latent Thoughts) | 4.80 | Reject | Both train latent computation during pretraining. TB has more novel mechanism but smaller training scale. TB's Copy-K baseline is better FLOP-matched than Latent Thoughts' parameter-matched comparisons |
| 40sQXprYlm (Distributed Neural Architectures) | 5.00 | Reject | Both propose novel dynamic architectures. TB's results are cleaner (consistently beats baselines vs. DNA's "competitive with") |
| eBAMg7w96m (Useless Features) | 5.60 | Accept (Poster) | Different paper type; TB's architectural contribution is comparably novel |
| k3SEVOW2Dg (Latent Concept Disentanglement) | 6.50 | Accept (Poster) | Different paper type; TB's empirical evaluation is broader but less theoretically rigorous |
| qOyF214xmg (Transducing Language Models) | 8.00 | Accept (Poster) | TB does not reach this level of theoretical depth and formal rigor |

Thoughtbubbles presents a genuinely novel architecture with consistent, positive empirical results. The method beats reasonable baselines on the primary metric (perplexity), the Copy-K baseline is a credible attempt at computation matching, and the analysis, while not fully rigorous, goes beyond aggregate metrics. The main weaknesses—modest training scale, mixed downstream results on some benchmarks, unresolved gradient bottleneck, and a parabolic (not monotonic) entropy relationship—are real but do not undermine the core contribution. The paper is honestly written with appropriate caveats.

Compared to the anchors: it is clearly stronger than the 3.00–4.00 range papers (which had either negative results or incremental contributions) and competitive with the 5.00–5.60 range papers. It does not reach the theoretical depth of the 6.50–8.00 anchors.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>