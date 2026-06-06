## Summary

MoEP (Modular Expert Paths) is a sparse decoder-only language model architecture that introduces layer-level expert routing without increasing the total parameter count. The method combines top-k routing over parallel Transformer blocks (operating at reduced dimensionality $d_P$) with MoE-style linear or SwiGLU projection layers for dimension shrink/grow transitions. The paper evaluates MoEP and MoEP-SwiGLU on the BabyLM strict-small track (10M words, 28–38M parameters), comparing against GPT-2 and GPT-BERT baselines.

---

## Strengths

- **Parameter-matched improvement over the dense GPT-2 baseline**: MoEP (28M params) achieves a macro-average of 49.00 (excluding AoA) compared to the authors' own GPT-2 at 48.10 and the official BabyLM GPT-2 baseline at 46.60 (Table 1). This confirms the paper's core claim that sparsity can be added without expanding total parameter count and without sacrificing performance relative to the corresponding dense baseline.

- **Concrete evaluation under a standardized protocol**: The paper follows the official BabyLM evaluation pipeline (zero-shot and fine-tuned tasks), which enables direct comparison with published baselines and lends credibility to the reported numbers. Models are released on Hugging Face for reproducibility.

- **Useful practical design insight**: The linear-expert variant (MoEP, 28M) outperforms the SwiGLU-based variant (MoEP-SwiGLU, 38M) on macro-average (49.00 vs 47.70, Table 1), providing a concrete takeaway that simpler experts can be more effective at small scale.

---

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed headline not supported by the data.** Section 1 states unqualifiedly that "MoEP was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models." This is factually incorrect under the primary metric (macro average excluding AoA). Table 1 shows GPT-BERT (causal) at 54.10 vs MoEP at 49.00 excluding AoA — a five-point gap *in GPT-BERT's favor*. The only metric on which MoEP leads all models is the macro average including AoA (44.50 vs 41.20 for GPT-BERT), but this reversal is entirely driven by GPT-BERT scoring **−3.90** on AoA. Claiming superiority over a model based on that model scoring below chance on a single task is misleading framing. Section 5.1 partially corrects this by conditioning the claim on "when the AoA task score was included," but the unconditioned claim in Section 1 stands and will be what most readers encounter first.

- **Load-balancing loss formula appears sign-inverted.** Equation 2 defines $\mathcal{L}_{\text{balance}} = -\sum_i p_i \log p_i$, which is the Shannon entropy $H(p)$, a non-negative quantity. Adding this to the total objective (Eq. 3) and *minimizing* it drives routing toward a **peaked, concentrated** distribution — i.e., it incentivizes expert collapse, the very problem the paper aims to prevent (Section 3.4). Correct load-balancing regularization should penalize non-uniformity by *maximizing* entropy or by using a positive-entropy penalty like $+\sum_i p_i \log p_i$. This issue is consequential: if the implementation matches the formula, training would actively cause collapse; if the implementation differs, the paper is under-specified in a technically important way. Either case undermines confidence in the training setup and the reported routing dynamics.

- **Selective AoA reporting makes cross-model comparisons inconsistent.** MoEP has an AoA score (53.70), but the authors' GPT-2 and MoEP-SwiGLU do not, because they were not submitted to the official leaderboard. This is acknowledged in a one-line note in Section 5.1, but it means that the "overall macro average" (second column, Table 1) mixes internally-obtained scores for some models with leaderboard-sourced scores for others, and cannot be fairly compared across all models.

### Minor

- **MoEP-SwiGLU parameter discrepancy is unacknowledged in interpreting results.** Table 2 shows MoEP-SwiGLU at 38M parameters vs 28M for both MoEP and GPT-2. The paper frames MoEP-SwiGLU's lower performance as showing that "lightweight simplicity is better than adding complexity" (Section 5.1), but MoEP-SwiGLU is neither lighter nor simpler—it is 35% larger. The paper does not acknowledge this parameter gap when interpreting the comparison.

- **Routing aggregation is underspecified.** Section 3.3 states "the routed inputs are summed up together," but does not clarify whether this is a weighted sum using the gating probabilities or an unweighted sum. For a method where routing is a central design choice, this ambiguity matters for both understanding and reproducibility.

- **No ablations to isolate architectural contributions.** The paper compares MoEP against dense GPT-2 but provides no ablation isolating (a) parallel blocks without routing, (b) routing without dimensionality reduction, or (c) the full MoEP. It is therefore unclear which design choices are responsible for the marginal gain over GPT-2.

### Trivial
None.

---

## Nice-to-Haves

- An ablation decomposing the contributions of parallel dimensionality reduction vs. top-k routing (e.g., routing all tokens to all blocks with averaging, vs. routing with full-$d_L$ blocks, vs. MoEP) would substantially strengthen the architectural argument.
- Showing the actual routing distribution entropy over training (rather than just qualitative checkpoint curves) would directly support the claim that load-balancing achieves diverse computational paths and address concerns about the balancing loss formulation.
- Submitting all models (GPT-2, MoEP-SwiGLU) to the official leaderboard to obtain AoA scores would eliminate the selective reporting issue and enable a clean single-metric comparison.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Faster early learning" as a strength**: The Strength Finder claims MoEP "reaches peak evaluation performance at 30M words" faster than GPT-2, but Table A.3 and the text in Section 4 explicitly state both MoEP and GPT-2 reached best accuracy at the **same 30M checkpoint**. The paper's own description (Appendix A.3) only notes qualitative differences in *pattern breadth* at that checkpoint, not a difference in when peak performance is reached. The learning-speed claim is not well supported.

- **Harsh Critic: "Best checkpoint selection is hyperparameter tuning on the evaluation set"**: This is a constraint of the BabyLM protocol, not a flaw specific to this paper. The critic acknowledges this ("this is a constraint of the BabyLM protocol, not a flaw unique to this paper"), so it should not be held against the authors.

- **Strength Finder: "Stable expert utilization via load-balancing"**: This strength conflicts with the verified Major weakness about the sign-inverted balancing loss. Because the formula as written would cause collapse rather than prevent it, this claimed strength is not credibly supported and is removed per the rule that weaknesses trump conflicting strengths.

- **Strength Finder generic claims** (problem importance, "follows the official pipeline is a strength"): Removed for being generic/superficial.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations about the sign-inverted balancing loss and the AoA metric gaming are procedural concerns, not scientific insights. The idea of layer-level MoE with reduced-dimensionality parallel blocks keeping total parameter count fixed is the paper's own contribution and is the only genuinely novel element identified.

---

## Suggestions

1. **Fix or clarify the load-balancing formulation**: If Equation 2 is intended to be a maximization of entropy (i.e., subtracted from the loss, or with a negative $\lambda$), state this explicitly. If the implementation uses a different convention, show the actual implemented formula.
2. **Restrict the headline claim** to what the data support: MoEP outperforms the parameter-matched dense GPT-2 baseline; it does not outperform GPT-BERT on the primary metric where all models are actually compared.
3. **Report all models under the same AoA conditions** or remove AoA from the cross-model comparison entirely.
4. **Explicitly note the 38M vs 28M parameter difference** when discussing MoEP-SwiGLU results, and avoid framing the comparison as if it is parameter-matched.
5. **Add clarification** on whether the routing aggregation in the Parallel Layer is a weighted or unweighted sum.

---

## Evaluation on Key Axes

- **Originality**: Moderate — layer-level MoE with dimensionality reduction is a coherent combination of existing ideas, but not independently proposed before at this granularity.
- **Importance of research question**: Moderate — compact sparsity is relevant, but the paper is confined to a very small-scale BabyLM setting, limiting generalizability claims.
- **Claims well-supported**: Weak — the headline claim outright overstates the results; the secondary claim (beating GPT-2) holds but by only ~1 point; the load-balancing mechanism is not credibly justified by the formula.
- **Soundness of experiments**: Weak — the load-balancing formula issue, selective AoA reporting, no ablations, and a single GPU run at tiny scale all limit confidence.
- **Clarity of writing**: Adequate — the architecture is reasonably described though with ambiguities (routing aggregation, $\lambda$ sign convention).
- **Value to research community**: Low-to-moderate at ICLR scale — potentially suitable as a workshop paper; insufficient evidence and scale for a main-track venue contribution.

---

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>2</community_value>
</subscores>