Now I have enough information to write the final review. Let me verify a few more facts before finalizing.## Summary

The paper introduces GMD-25, a benchmark of four compositional-generalisation tasks for machine-learning force fields (length extrapolation, functional-group composition, duplication, and combination), built on 118 substituted alkyl-chain molecules with GFN2-xTB labels and a release-ready toolkit. Five architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and the central empirical finding is that OOD errors are typically one to two orders of magnitude higher than ID, with rank reversals between ID and OOD performance across architectures.

## Strengths

- **Cleanly motivated task design with controlled training/test splits.** The four tasks (Section 3.1) operationalize length generalisation and systematicity from Hupkes et al. (2020), and the base-vs-augmented variants in Tasks 1 and 2 give a controlled lever for testing whether providing all "primitives" in training closes the gap (e.g., Task 1 augmented exposes all chain lengths to the model but with mismatched functional groups).
- **Rank-reversal between ID and OOD is a genuinely informative empirical finding.** EquiFormerV2 dominates ID forces but flips on OOD energy in Length Extrapolation, and other models swap ranks between tasks (Section 4.3, Conclusions). This is the kind of diagnostic observation a benchmark is supposed to surface.
- **Reproducible data-generation toolkit.** The four-step RDKit → FlashMD → GFN2-xTB → ASE pipeline (Section 3.2) is described concretely and intended for release, making the benchmark extensible.

## Weaknesses

### Fatal
None.

### Major

- **Energy MAE is reported on total molecular energy rather than per atom, which compromises the Length Extrapolation headline.** Section 4.2's definition `MAE_energy = (1/M) Σ |Ê_j − E_j|` is on total energy; the Task 1 base test molecules (C7–C13) are 2–4× larger than training molecules (C2–C6) in atom count. Total-energy MAE will scale roughly with system size even if per-atom error is constant, so the "orders-of-magnitude" gap in Figure 2(a) cannot cleanly be attributed to generalisation failure. The force metric is normalised by `1/3N` and does not suffer from this, so the qualitative conclusion may still hold via forces, but the quantitative energy claim needs per-atom normalisation to be defensible.
- **MACE, NequIP, and Allegro are absent from the model lineup despite being central to the "physics-informed design" claim.** Related Work (Section 2.1) explicitly discusses NequIP, TFNs, and MACE as the line of work that uses "mathematically rigorous formulations based on spherical harmonics and irreducible representations" — exactly the inductive biases the benchmark is meant to test. The Section 4.1 justification ("we did not include any foundation models … harder to untangle memorisation and generalisation") does not apply to MACE/NequIP/Allegro, which are standalone architectures. For a benchmark whose value rests on the claim that current designs fail to generalise compositionally, omitting the family most associated with strong physics-informed inductive biases materially weakens the empirical conclusion.
- **Hyperparameter selection on ID data only systematically advantages ID fit over OOD generalisation.** Section 4.2 states that Bayesian optimisation was used "to ensure that each model achieved its best possible performance on the in-distribution data." For an OOD benchmark, this protocol bakes in the failure mode under study: it cannot cleanly separate "this architecture overfits ID" from "this architecture has a weak inductive bias." A uniform protocol or a held-out OOD validation split (drawn from different OOD instances than the test set) would make the comparison more informative.

### Minor

- **The benchmark's framing is broader than the chemical scope it covers.** Section 3 describes "Generalisation for Molecular Dynamics," but the dataset consists of 118 molecules built from ten substituted linear alkyl-chain families. A title or framing such as "compositional generalisation for small organic molecules along chain-length and functional-group axes" would more honestly reflect the artifact.
- **Diagnostic analysis stops at "all models fail."** The Results discussion (Section 4.3) and Conclusion (Section 5) note rank reversals but do not probe *where* models fail (per-atom error vs. distance from training distribution, error concentration near duplicated motifs in Task 3, hetero-functional region in Task 4). Even simple per-region or per-element error breakdowns would convert the benchmark from a scoreboard into a tool that points to architectural fixes — this is what would make the rank-reversal observation actionable.
- **The GFN2-xTB label choice deserves explicit scope acknowledgment.** Section 3 motivates xTB as a "balance between computational efficiency and accuracy," but the paper does not discuss that "failing to generalise on xTB labels" may not perfectly map to failure on DFT-grade targets the field actually cares about, particularly for long-range/dispersion-sensitive comparisons. A sanity-check sub-experiment on a DFT-relabelled subset would calibrate transferability of the conclusions.
- **FlashMD as the sampler is not examined for bias.** Section 3.2 uses FlashMD (itself an ML model) to generate initial trajectories before xTB recalculation. Whether FlashMD's sampling bias interacts with the OOD design (e.g., does it sample longer-chain conformations differently than short ones?) is worth a sentence.

### Trivial
None retained.

## Nice-to-Haves

- Report per-atom MAE (or a size-normalised energy error) alongside total-energy MAE, and re-analyse Figure 2(a)/Figure 3(a,c) under it.
- Add MACE and at least one strictly-equivariant baseline (NequIP or Allegro) under the same protocol.
- Provide variance across seeds, given the small per-molecule training sets (~2000 snapshots per molecule, single trajectory).
- Add at least one diagnostic per task (per-region force error, per-element breakdown, attention or feature analysis for EquiFormerV2) to make the rank-reversal observation actionable.
- A small ~10% DFT cross-check on one task to calibrate the xTB scope.
- Sharpen the conclusion: speculate which architectural biases the rank reversal points to, rather than leaving it descriptive.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **(Strength Finder) "Use of ab initio MD trajectories with a reproducible toolkit."** The strength is mostly real but partially conflicts with the verified weakness about FlashMD bias and the under-examined xTB choice; kept implicitly via the toolkit strength above. The "ab initio" framing in the Strength Finder is also slightly loose since GFN2-xTB is semi-empirical, not pure AIMD.
- **(Strength Finder) "Two-stage hyperparameter tuning ensures fair model comparison."** This conflicts with a verified weakness — Bayesian optimisation on ID data systematically biases the comparison toward models that fit ID well, exactly the mechanism the benchmark is supposed to detect. The weakness wins.

## Novel Insights

None beyond the paper's own contributions. The most interesting empirical observation — that ID and OOD ranking orders diverge across architectures — is the paper's own finding and is worth amplifying, but no novel synthesis emerges beyond it.

## Suggestions

- Replace (or supplement) the total-energy MAE in Section 4.2 with per-atom energy MAE; rerun Figures 2 and 3.
- Add MACE and NequIP (and ideally Allegro) under the same protocol as the existing five models. Without these, the "current physics-informed designs do not generalise compositionally" thesis is not adequately tested.
- Use OOD-aware or at least uniform hyperparameters rather than ID-tuned BO; or report both protocols.
- Sharpen the framing of the benchmark to the actual chemical scope ("substituted linear alkyl-chain compositional generalisation").
- Add a per-region/per-element error breakdown for at least one task to elevate the rank-reversal finding into actionable architectural guidance.
- Briefly address FlashMD sampling bias and the xTB-vs-DFT scope, ideally with a small DFT-relabelled subset.

## Evaluation on Each Axis

- **Originality.** The compositional-generalisation framing for MLFFs is fresh in its specificity (length, composition, duplication, combination), more sharply structured than prior OOD benchmarks like BOOM (property-tail) and MatBench (compositional/structural splits for materials).
- **Importance of research question.** Genuinely important: standard MLFF benchmarks train and test on the same molecules, so a benchmark that isolates compositional generalisation fills a real gap.
- **Are claims well supported?** Partially. The qualitative finding that all five tested models suffer large OOD gaps is well-supported. The quantitative "orders of magnitude" claim for energy on Task 1 is contaminated by total-vs-per-atom scaling. The broader claim that current physics-informed architectures fail to generalise is undercut by the omission of MACE, NequIP, and Allegro.
- **Soundness of experiments.** ID-only hyperparameter selection is a real methodological gap. Single-seed runs are not addressed. Otherwise the protocol is reasonable.
- **Clarity of writing.** Generally clear; task definitions are concrete and the figures are interpretable.
- **Value to the research community.** A focused diagnostic benchmark with a reusable toolkit and a controlled augmented/base structure is useful, but the value is significantly reduced by the missing equivariant baselines and the unnormalised energy metric, both of which directly affect what conclusions can be drawn.

## Score and Decision

### Calibration anchors

**Round 1 (bracketing):**
- `kKXIYUi8ff.md` — *DynamicsDiffusion* (avg 3.00, Reject). Generative MD method; weaker novelty/execution than this paper.
- `ItPYVON0mI.md` — *Dynamic Accuracy in ML CG Potentials* (avg 3.00, Reject). Narrower, more flawed.
- `OcTUquFXfx.md` — *Discovering Global Minima of High-Dimensional Energy Landscapes* (avg 2.60, Reject). Distant from this paper.
- `CgkAGcp9lk.md` — *Compositional Search of Stable Crystalline Structures* (avg 3.00, Reject). Different topic.
- `NvJxTjTQtq.md` — *EGraFFBench* (avg 6.00, Reject). Closest analogue — benchmarks equivariant force-field models on OOD; broader model set and richer metrics than this paper.
- `4S2L519nIX.md` — *Pushing the Limits of All-Atom Geometric GNNs* (avg 6.50, Accept). Pretraining/transfer; more substantive than a benchmark-only paper.
- `CkozFajtKq.md` — *Flow Matching for Atomic Transport* (avg 6.33, Reject). Methodological contribution, not directly comparable.
- `J4V3lW9hq6.md` — *Multi-Grained Group Symmetric* (avg 5.00, Reject).
- `NSVtmmzeRB.md`, `KSLkFYHlYg.md`, `OIvg3MqWX2.md`, `P7KIGdgW8S.md` — all avg 8.00, all on a different topic (generative/representation theory); not directly comparable.

Round-1 bracket: **between ~3.5 and ~6.0**, with EGraFFBench at 6.0 as the upper anchor and the various 3.0-tier MD-method rejects as the lower bound.

**Round 2 (narrowing):**
- `1JgWwOW3EN.md` — *BenchMol* (avg 4.80, Reject). Comparable benchmark paper, multi-modality MRL; high variance reviews. GMD-25 has a sharper scientific question but is narrower in scope.
- `P5jreWnIjV.md` — *MoleculeCLA* (avg 4.00, Reject). Benchmark for binding-affinity proxies; weaker than this paper.
- `3lfSk8NWWp.md` — *Unsupervised drug-likeness* (avg 4.00, Reject). Off-topic.
- `7Jer2DQt9V.md` — *Pretraining in Graph OOD* (avg 4.50, Reject). OOD benchmark with limited novelty of insights.
- `NvJxTjTQtq.md` — *EGraFFBench* (avg 6.00, Reject). Re-anchor at the top of the bracket.
- `Xk9Q0CrJQc.md` — *Understanding and Mitigating Distribution Shifts for MLFFs* (avg 6.25, Reject). Substantially stronger — it both characterises distribution shifts and proposes mitigation methods, whereas this paper is diagnostic-only.
- `IbCvnpJ4py.md` — *RoFt-Mol* (avg 5.25, Reject). Comparable benchmark; similar tier.
- `zyBJodMrn5.md`, `Bq3fEAGXUL.md`, `UVSKuh9eK5.md` — compositional-generalisation benchmarks at 5.33–5.67. Different domains; not as topically close.

**Comparison.** GMD-25 is more focused than BenchMol (4.80) and has a clearer scientific question, but it is missing the most-relevant equivariant baselines and has a flawed energy metric, which are real evidential gaps. It is materially weaker than *Understanding and Mitigating Distribution Shifts* (6.25), which adds methods, and weaker than EGraFFBench (6.00), which has a broader model lineup and richer evaluation metrics. It sits above the 4.00-tier benchmarks (MoleculeCLA, drug-likeness) but below the ~5.25 RoFt-Mol benchmark in terms of how well the central claims are supported.

**Final placement.** The paper is closer to RoFt-Mol (5.25)/BenchMol (4.80) than to EGraFFBench (6.00) — closer to the bottom-middle of the round-2 anchors. The compositional-generalisation framing is genuinely interesting and a step up from generic OOD benchmarks, but the unnormalised energy metric on Task 1 and the omission of MACE/NequIP/Allegro are substantive enough to keep this below the EGraFFBench tier.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>