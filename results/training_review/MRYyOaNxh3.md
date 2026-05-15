Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper studies the underexplored problem of intra-trajectory dynamic entity composition under zero-shot out-of-domain (OOD) generalization in MARL — scenarios where new entities (agents, obstacles) enter during the inference trajectory in numbers exceeding those seen during training. The authors propose FlickerFusion, an input-space augmentation method that stochastically drops entities from each agent's observation at every timestep to match the in-domain observation size, thereby avoiding the need for parameter expansion. The method is evaluated on 12 benchmarks (MPEv2) against 11 baselines, achieving top-1 reward in 10/12 benchmarks with minimal computational overhead.

## Strengths

- **Novel and well-motivated problem formulation.** The paper identifies an underexplored setting — intra-trajectory entity *addition* (as opposed to deletion) under zero-shot OOD generalization — that is clearly motivated by real-world applications (search and rescue, national defense). The empirical demonstration that existing MARL methods degrade sharply in this setting (Figure 1c, Table 1) confirms the problem is real.

- **Simple, elegant, and orthogonal approach.** FlickerFusion's core idea — stochastic entity dropout at each timestep to keep the input size fixed without adding parameters — is a clean departure from prior parameter-expansion methods (UPDeT, CAMA, ODIS). The method introduces no new parameters at test time, requires only ~4-9% additional training compute, and is architecture-agnostic by design (works identically with MLP and attention backbones).

- **Strong empirical performance.** FlickerFusion ranks first in 10 out of 12 benchmarks (Table 1), improves upon the backbone in 22 out of 24 comparisons, and the "without domain-awareness" ablation (Table 2) confirms that the domain-aware dropping mechanism contributes meaningfully, especially for MLP backbones. The benchmark suite (MPEv2, 12 environments) is released publicly, supporting reproducibility.

- **Rigorous comparison against model-agnostic DG methods.** The paper is the first to implement and evaluate four domain generalization methods (MLDG, SMLDG, DG-MAML, Meta DotProd) in the MARL OOD setting, finding that they perform poorly — a useful negative result for the community.

## Weaknesses

### Fatal
None.

### Major

- **"Uncertainty" is never explicitly defined, undermining a central claim.** The paper repeatedly highlights that FlickerFusion "uniquely reduces uncertainty" (abstract, Section 6) and devotes an entire subplot (Figure 5 top-left) to "uncertainty distributions across methods." However, the paper never states what quantity this is — standard deviation of final rewards across seeds, variance across intra-trajectory steps, ensemble disagreement, or something else. The Figure 5 caption mentions "standard deviation statistics" and Table 1 reports mean ± σ, strongly suggesting the metric is the standard deviation of final rewards across the 5 random seeds aggregated across benchmarks. But this is never stated explicitly, and the aggregation procedure for the box plot is not described. Without a clear definition, the claim that FlickerFusion "uniquely reduces uncertainty" cannot be properly evaluated. This is especially consequential for the "no reward-uncertainty trade-off" discussion in Section 6, which rests entirely on this undefined metric.

### Minor

- **No control baseline isolating stochastic dropout from input-size fixing.** FlickerFusion has two components: (1) keeping the input size fixed to the in-domain maximum, and (2) stochastically varying which entities are dropped at each timestep. A simple baseline that truncates/pads to in-domain size *without* stochasticity (e.g., always drop the last N entities, or zero-pad) would isolate the contribution of the temporal "flickering" mechanism. Without this control, it is unclear whether the gains come from avoiding parameter expansion (which any input-fixing scheme achieves) or from the specific stochastic dropout over time. The existing baselines all use parameter expansion, so they cannot serve as this control.

- **Ablation confound in "without DA" condition.** The "without DA" ablation replaces the domain-aware drop count with `Uniform(0, N^{inf})`, simultaneously varying both the *number* of dropped entities and the *selection criterion* (random vs. type-aware). A cleaner ablation would compare dropping the same count of entities (matching the DAED count) but selecting them uniformly at random vs. type-aware. The current design conflates two factors, though the overall conclusion that domain-awareness helps remains directionally correct.

- **Limited backbone diversity.** The method is only tested with QMIX (MLP and attention backbones). While the method is architecture-agnostic by design (operating purely on the input space) and the paper notes this can be "trivially extended to on-policy networks" (Section 3.1), no empirical evidence from VDN, MAPPO, or COMA is provided. The "universally applicable" claim in the abstract would be strengthened by at least one non-QMIX demonstration.

- **Statistical significance not reported.** Many entries in Table 1 have overlapping ±σ ranges (e.g., Spread OOD2: 845.6 ± 209.0 vs. QMIX-Attention 787.8 ± 209.4). While multi-seed averaging is standard in MARL, the absence of any pairwise significance test makes it difficult to assess which comparisons are reliable.

### Trivial
- None.

## Nice-to-Haves

- **Evaluation on a more complex environment** (e.g., SMAC with dynamic unit spawning) to test scalability beyond MPE, though the paper's stated choice of MPE for computational efficiency is reasonable.
- **Sensitivity analysis** for the dropout hyperparameter (number of entities dropped), especially when N^{inf} is much larger than N^{train}.
- **A qualitative case study or video frame sequence** illustrating how temporal aggregation of stochastic views recovers information about dropped entities.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proposition 3.1 is trivial filler"** — The reviewer dismisses Proposition 3.1 as a trivial concentration bound. While the bound is indeed simple, it serves a legitimate purpose: it formally justifies why random independent dropping yields a "dispersed view" across agents. This is not filler; it is standard practice to include simple propositions that formalize design intuition. Removed because it overstates the weakness.

- **"Universality claim not supported"** — The strength finder's claim about universality was flagged as a weakness by the reviewer. However, the paper demonstrates the method with both MLP and attention backbones — two fundamentally different architectures. The method operates at the input level before any network, making it genuinely architecture-agnostic. The reviewer's objection is weakened to "limited backbone diversity" above (minor tier) rather than being a fatal flaw.

- **Strength finder's claim about "state-of-the-art in both reward and uncertainty reduction"** — This strength conflicts with the verified weakness that uncertainty is undefined. However, the reward results remain strong regardless, so the strength is retained in spirit (strong reward performance) while the uncertainty claim is qualified.

## Novel Insights

The most interesting meta-observation from these reviews is the tension between the paper's strong empirical showing (10/12 benchmarks, systematic baselines) and the presentation gaps that prevent full evaluation of its "uncertainty reduction" claim. The paper convincingly shows that input-space augmentation (FlickerFusion's approach) outperforms parameter-expansion methods (UPDeT, CAMA, ODIS) for OOD MARL — a finding that challenges the prevailing inductive-bias-in-parameters paradigm. However, the reviewers rightly pressed on whether the superiority comes from fixing the input size, from the stochastic mechanism, or both. The missing zero-padding control is the single experiment that would resolve this ambiguity. The "uncertainty" issue is a clarity problem (the metric is almost certainly std of rewards across seeds, given the Figure 5 caption's mention of "standard deviation statistics" and Table 1's ±σ reporting) but one that needs to be stated outright for the paper's headline claim to stand.

## Suggestions

1. **Define "uncertainty" explicitly** and describe the aggregation procedure used for the box plots in Figure 5 (top-left). If it is the standard deviation of final rewards across seeds, state this and explain how values are normalized/aggregated across benchmarks with different reward scales.
2. **Add a zero-padding/truncation baseline** that keeps the input size at N^{train} without stochastic dropout. This isolates whether the gain comes from avoiding parameter expansion (common to any input-fixing approach) or from the temporal "flickering" specifically.
3. **Fix the "without DA" ablation** to drop the same count of entities as DAED but with random selection, rather than varying both count and selection jointly.
4. **Test on at least one non-QMIX backbone** (e.g., VDN or MAPPO) to substantiate the universality claim.
5. **Report statistical significance** (e.g., paired bootstrap or Mann-Whitney U) for the key comparisons in Table 1.

## Score and Decision

**Originality:** Good — the problem setting (intra-trajectory entity *addition* under zero-shot OOD) is genuinely novel, and the input-augmentation approach is orthogonal to prior work.  
**Importance:** High — the problem is well-motivated by real-world applications and the failure of existing methods is clearly demonstrated.  
**Claims support:** Moderate — reward results are well-supported, but the "uncertainty reduction" claim is weakened by the undefined metric, and the missing control baseline limits attribution.  
**Soundness:** Solid for the core reward comparisons; the ablation and missing control are the weaker points.  
**Clarity:** Good overall, but the undefined "uncertainty" metric is a significant omission.  
**Value to community:** Positive — the benchmark suite (MPEv2), baselines, and negative results on model-agnostic DG methods are useful contributions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>