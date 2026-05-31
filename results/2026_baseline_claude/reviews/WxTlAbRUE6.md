## Summary

GMD-25 is a benchmark designed to evaluate the compositional generalization capabilities of Machine Learning Force Fields (MLFFs). The benchmark comprises four tasks—Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination—each of which tests whether MLFFs can transfer learned physical principles to out-of-distribution molecular configurations. Five representative MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and all show significant failures under the proposed OOD conditions, with errors often one to two orders of magnitude higher than their in-distribution counterparts.

---

## Strengths

- **Clear and important problem framing.** Standard MLFF benchmarks test only in-distribution generalization. This paper correctly identifies that the field lacks a systematic evaluation of whether physics-informed architectures actually learn transferable principles. The four tasks are well-differentiated and map directly to concepts from compositional generalization literature (length generalization, systematicity).

- **Task design is thoughtful.** Each task is constructed such that, in principle, generalization *should* be possible if the model captures the relevant physics (e.g., in Length Extrapolation, all required carbon chain lengths or functional groups appear somewhere in training). This avoids the confound of testing on simply "more difficult" molecules; the difficulty is purely about recombination.

- **Consistent cross-model failure is an informative result.** The finding that all five architectures—from simple invariant GNNs (SchNet) to state-of-the-art equivariant Transformers (EquiFormerV2)—systematically fail on all four tasks is genuinely informative. The additional observation that the best in-distribution model is not consistently the best OOD model is a useful empirical result.

- **Extensible toolkit.** Providing a reproducible pipeline (RDKit → FlashMD → GFN2-xTB → ASE) with curated splits and training scripts lowers the barrier for follow-up work.

---

## Weaknesses

### Fatal
None.

### Major

1. **Energy MAE is not per-atom normalized, introducing a systematic confound for Task 1.** The reported MAE_energy averages the absolute difference in *total* molecular energy over the test set. In the Length Extrapolation task, OOD molecules have 7–13 carbons vs. 2–6 for ID molecules. Because total molecular energy scales roughly linearly with system size, OOD energy MAE will be inflated simply due to the larger number of atoms, independent of any generalization failure. The paper presents the sharp OOD energy spike (Figure 2a) as evidence of failure, but this artifact alone could explain a 2–3× increase in energy MAE even if per-atom accuracy were identical. Per-atom energy MAE (or energy per atom) should be reported alongside total energy MAE. This concern is less severe for Tasks 3 and 4 (same carbon chain lengths ID vs. OOD) but is central to the headline Task 1 result.

2. **Insufficient analysis of failure modes.** A benchmark paper's primary value comes from its ability to diagnose deficiencies and guide future model development. The empirical section documents that all models fail but provides little mechanistic insight: Why does EquiFormerV2 achieve the best force MAE yet catastrophically fail on energy MAE in Task 1? Why does GemNet generalize better for Tasks 3 and 4? What inductive biases—if any—correlate with OOD performance? Without this analysis, practitioners cannot determine which architectural choices to pursue.

3. **Foundation models excluded without exploration of partial alternatives.** The decision to exclude MACE-MP-0 and similar foundation models is justified with the concern about disentangling memorization from generalization, but this is presented as a binary choice. A more nuanced approach—e.g., restricting foundation model evaluation to a subset of molecules unlikely to appear in pre-training data, or fine-tuning foundation models on the same training splits—would substantially increase the benchmark's relevance to current practice.

### Minor

1. **Chemical space is restricted to linear alkane chains with terminal functional groups.** All 118 molecules are variations on linear chains. This limits the benchmark's ability to assess generalization challenges that arise from branching, ring structures, or other common molecular topologies. The benchmark is valuable in its current form but is not representative of broad organic chemistry.

2. **GFN2-xTB labels are semi-empirical, not DFT-level.** While computationally justified and explicitly acknowledged, GFN2-xTB labels may not accurately capture subtle electronic effects, particularly for the functional group composition and combination tasks where bond-level interactions between dissimilar groups are precisely what is being tested.

3. **No statistical uncertainty quantification.** Results are reported as single-run point estimates with no confidence intervals, error bars, or variance across seeds. For a benchmark making strong claims about ordering of architectural families, this omission makes it hard to judge the reliability of the rankings.

### Trivial
None worth raising.

---

## Nice-to-Haves

- Report per-atom energy MAE (or atomic energy normalization) alongside total energy MAE throughout, especially for Task 1.
- Add an "oracle upper bound" trained on all data (ID + OOD combined), to contextualize how large the generalization gap is relative to the best achievable error on OOD molecules.
- Include at least one ablation or feature analysis (e.g., correlation between cutoff radius and OOD performance for length extrapolation) to hint at architectural improvements.

---

## Novel Insights

The paper surfaces a striking asymmetry between forces MAE and energy MAE generalization: EquiFormerV2 achieves the best OOD forces MAE in several tasks yet shows catastrophic OOD energy MAE, a dissociation that is neither well explained nor anticipated by the related work. This suggests that equivariance helps force prediction (a local quantity) while offering little benefit for total energy generalization (a global quantity), potentially implicating how energy is aggregated across atom-wise contributions. This observation, while only briefly noted in the text, could motivate new research on separating local and global components of molecular energy in MLFF architectures.

---

## Suggestions

- Replace total energy MAE with per-atom energy MAE (eV/atom) or report both; add a brief paragraph discussing why molecule-size normalization matters for fair OOD comparison.
- Add a failure-mode analysis section (even descriptive): plot the error as a function of chain length for individual molecules in the OOD set, analyze which atoms/bonds carry the largest force prediction error, or compare the OOD error distribution across models.
- Include at least a brief discussion of how foundation models could be evaluated in a memorization-controlled way (e.g., filtering pre-training data or testing on molecules provably absent from known pre-training corpora).

---

## Score and Decision

The benchmark fills a genuine and important gap: evaluating whether MLFFs learn physical principles or merely interpolate training data. The four tasks are well-motivated, the cross-model evaluation is broad, and the result that all current state-of-the-art models fail substantially at compositional generalization is meaningful. However, the energy MAE confound in the headline Task 1 results is a real methodological issue, the analytical depth is limited for guiding follow-up work, and the chemical scope is narrow. These collectively make this a useful but not fully polished contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>