Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Fuzzed Randomized Smoothing (FRS), a certified defense against textual backdoor attacks injected during PLM pre-training. FRS combines MCTS-based fuzzing to identify vulnerable text segments (potential trigger locations) with biphased model parameter smoothing, then concentrates randomization probability on those segments. The theoretical analysis (Corollary 1) derives a larger certified robustness radius compared to uniform randomized smoothing. Experiments across three datasets, three attack methods, and five model sizes (BERT-base to LLaMA3-8B) show improvements in clean accuracy and attack success rate over baselines including TextGuard.

## Strengths

- **Novel integration of MCTS-based fuzzing with randomized smoothing for textual backdoor defense** (Section 4.3). Proactively identifying vulnerable segments via MCTS (Eqs. 8–11) and allocating differential randomization probabilities (ω_H > ω_L, Eq. 13) is a concrete algorithmic innovation over uniform text randomization used in prior certified defenses. The idea is well-motivated by the software fuzzing literature.

- **Comprehensive evaluation across diverse models, attacks, and datasets.** Table 1 compares against 7 empirical baselines and 1 certified baseline (TextGuard) under 3 attack paradigms (RIPPLe_a, LWP, BadPre) on 3 datasets. Table 4 extends to 5 victim models from BERT-base to LLaMA3-8B (110M to 8B parameters). FRS consistently achieves higher CA and lower ASR than all baselines.

- **Ablation study isolating both proposed components** (Table 3). Removing biphased model parameter smoothing (BMPS) or fuzzed text randomization (FTR) degrades poisoned accuracy and ASR across all datasets, demonstrating that both modules contribute positively.

- **Realistic threat model.** The paper targets the post-attack scenario where defenders have no access to poisoned pre-training data (Section 1, Section 4.2), distinguishing it from prior methods that operate during the poisoning phase. The biphased parameter smoothing avoids fine-tuning K separate models from scratch, which is a practical advantage.

## Weaknesses

### Fatal

None.

### Major

1. **Certified radius claim depends on unverified MCTS localization accuracy.** Corollary 1 derives R_r^new = log(ω_M)/log(ω_H) · R_r^old, which assumes the trigger is entirely contained within the vulnerable segment T(x') identified by MCTS. If MCTS mislocalizes (trigger partly or wholly outside T(x')), the effective randomization probability on the trigger becomes ω_L rather than ω_H, collapsing the claimed radius advantage. The paper provides **no empirical validation** of MCTS localization—no recall/precision of trigger identification, no analysis of how localization varies with MCTS budget or trigger type, no discussion of false positives from the KL-divergence heuristic. The only mention is a qualitative statement (line 219: "with more MCTS iteration budget, the confidence that the trigger is successfully captured can be higher") without supporting evidence. This does not invalidate the method's empirical effectiveness, but it means the theoretical radius result is a conditional guarantee on an untested precondition, not a worst-case certificate as the paper's framing suggests.

2. **Computational cost is unquantified despite efficiency being a selling point.** The title and abstract highlight "efficient" defense, and Section 4.2 justifies parameter smoothing by invoking overhead reduction. However, the paper provides **no runtime measurements whatsoever**: no per-sample MCTS cost, no latency for the K=20 inference passes, no comparison of inference time with baselines. The MCTS-based fuzzing must run per test sample to identify vulnerable areas, and for large models like LLaMA3-8B this cost is potentially prohibitive. While the parameter-smoothing design avoids training K full models, the inference-stage cost is never benchmarked, leaving the efficiency claim unsubstantiated.

### Minor

1. **No sensitivity analysis for key hyperparameters.** σ (noise variance, set to 0.01), H (number of smoothed layers, set to 10), C (MCTS exploration constant), Λ (distance threshold), and MCTS iteration budget are all set without justification or ablation. The paper's qualitative claim about MCTS budget improving trigger-capture confidence (line 219) is not empirically grounded.

2. **No error bars or confidence intervals on robustness radius results (Table 2).** Table 1 includes significance testing (t-test, p<0.01), but Table 2 reports only average and maximum radius without variance. Given the reported improvements are modest (25–35% average increase), variance information is needed to assess reliability.

3. **The KL-divergence heuristic for MCTS simulation may have false positives** (Section 4.3.1, Step 3). The criterion measures output distribution change, which can be large for non-backdoored reasons (e.g., perturbing key sentiment words). The paper does not analyze how this affects localization precision or whether the method is robust to such false signals.

4. **The link between data-level smoothing (Section 4.1) and parameter-level smoothing (Section 4.2) is heuristic.** Assumption 1 asserts consistency on clean inputs but does not formally justify why additive parameter noise (Eqs. 4–5) substitutes for data noise (Eq. 2) in terms of trigger neutralization. The practical approximation is reasonable and supported by ablation results, but the theoretical gap is unaddressed.

5. **No limitations or failure cases discussion.** The paper lacks a limitations section or discussion of scenarios where the method might underperform (e.g., when triggers span the entire input, or when MCTS mislocalizes due to uninformative model output distributions).

### Trivial

None.

## Nice-to-Haves

- **Validate MCTS localization directly:** measure recall and precision of trigger segment identification on held-out attack instances, showing how localization accuracy varies with MCTS budget and model size.
- **Report runtime breakdown**: average MCTS cost per sample, K-pass inference latency, comparison with baselines.
- **Study sensitivity to hyperparameters** (σ, H, C, Λ, MCTS budget) via ablation.
- **Add error bars or confidence intervals to Table 2.**
- **Discuss failure cases** explicitly (e.g., triggers that span the full input, or model collapse under aggressive parameter smoothing).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Garbled equation in preliminaries** — This is a PDF parsing artifact, not an author error (Hard Rule: remove formatting artifacts).
- **Related work differentiation from Cohen et al. 2019** — The paper explicitly discusses this distinction in Section 2 (lines 27–28: "for the more challenging and harmful backdoor attacks... certified robustness solutions are still lacking"). The differentiation is present.
- **TextGuard's low CA "does not demonstrate broader radius"** — This observation about result interpretation is not a weakness of the paper; FRS reports CA, PA, ASR, and radius as separate metrics, and the critic's framing conflates them.
- **Beta distribution result not explained** — This is standard in randomized smoothing literature and properly cited to Zeng et al.
- **β=1 "fully trained" is vague** — This is a standard assumption in convergence-based analysis and not unique to this paper.
- **"All tokens must be randomized" is pessimistic** — If anything, this makes the analysis conservative (works in the paper's favor as an underestimation, not overestimation).

## Novel Insights

The reviews surface a clarity tension that the paper itself does not fully resolve: the claimed "certified" radius is structurally conditional on MCTS localization accuracy, yet the paper treats Corollary 1 as a definitive theoretical result. This is not uncommon in randomized smoothing papers (many certificates depend on properties of the base classifier), but the paper would benefit from explicitly stating: (1) the certificate holds conditional on the trigger being within T(x'), (2) the empirical radius in Table 2 is an *observed* radius under the experiment's MCTS configuration, which may or may not equal the theoretical bound, and (3) that the broader utility of the method lies in the *combination* of strong empirical results (CA, PA, ASR) with a principled framework for targeted randomization, even if the worst-case certifiable radius depends on localization accuracy. Neither review explicitly articulated this point about reframing the claim.

## Suggestions

1. **Add direct MCTS localization validation** — Measure what fraction of trigger tokens fall within the identified T(x') on held-out attack samples. This single experiment would substantially strengthen the theoretical claim.
2. **Report runtime** — Even a single table showing average per-sample MCTS time and inference latency (for FRS vs. TextGuard) would substantiate the efficiency claim.
3. **Add variance bars to Table 2** and discuss whether the radius improvements are statistically significant.
4. **Tone down the "certified" framing** or add a clear subsection on "Conditions for the Certificate" that explicitly states the dependence on MCTS localization and discusses when the guarantee may not hold.
5. **Ablate key hyperparameters** — At minimum, show how robustness radius varies with MCTS iteration budget (the paper already asserts this relationship qualitatively).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>