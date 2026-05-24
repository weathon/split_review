Below is my consolidated meta-review.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization in machine-learned inter-atomic potentials. It defines four controlled tasks—Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination—that probe different aspects of systematic generalization beyond standard random/scaffold splits. Five popular MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated. The main finding is that all models suffer substantial OOD degradation, often by one to two orders of magnitude. A data generation toolkit (RDKit → FlashMD → GFN2-xTB) and a dataset of 118 molecules / 296k labelled geometries accompany the benchmark.

---

## Strengths

1. **Systematic, interpretable task design.** The four tasks each isolate a distinct compositional challenge (length generalization, composing functional groups, duplicating a motif, recombining motifs asymmetrically). This goes well beyond existing OOD benchmarks that use coarse scaffold or property-threshold splits. Described concretely in Section 3.1 and Figure 1.

2. **Broad architectural coverage.** The evaluation spans invariant GNNs (SchNet), equivariant MPNNs (PAINN, DimeNet++, GemNet), and an equivariant Transformer (EquiFormerV2). The consistent failure across this diversity strengthens the negative finding. (Section 4.1, Figures 2–4.)

3. **ID performance does not predict OOD performance.** The results reveal nuanced failure patterns—e.g., EquiFormerV2 has the best force MAE OOD on Length Extrapolation but the worst energy MAE OOD, while SchNet and DimeNet++ show the opposite. This diagnostic value is a genuine contribution beyond simple negative results. (Section 4.3, Figure 2.)

4. **Clean, reproducible data pipeline.** The four-step toolkit (RDKit initial structure → FlashMD fast trajectory → GFN2-xTB recalculation → ASE orchestration) is clearly specified and extensible. The dataset will be released with curated splits, supporting community reuse. (Section 3.2.)

---

## Weaknesses

### Fatal

None.

### Major

None that are unambiguous from the paper as written. The issues below are substantive but correctable.

### Minor

1. **Unexplained baselines in main results figures.** Figure 2 includes "PBE0" and Figure 3 includes "m4s" as model names, yet Section 4.1 lists only SchNet, PAINN, DimeNet++, GemNet, and EquiFormerV2. "PBE0" is a DFT functional (not a learned MLFF), and "m4s" is not defined anywhere. The reader cannot fully interpret these comparisons. The core finding is still supported by the five described models (especially in Figure 4), but the presence of these unlabelled baselines undermines the paper's presentation standards. The authors should either (a) describe them in the model section or (b) remove them and regenerate the figures with only the described models.

2. **Energy MAE not normalized by atom count for Length Extrapolation.** The energy metric (MAE on total energy per molecule) scales with molecule size. For Task 1, OOD molecules have 7–13 carbons vs. 2–6 ID, so even a perfect per-atom model would show larger absolute energy errors on larger molecules. The paper reports "orders of magnitude" degradation, but the dramatic Energy MAE gaps in Figures 2–3 may be partially inflated by this size confound. Force MAE (per-atom) independently supports the qualitative conclusion (gaps are smaller but still substantial), so the core claim is not invalidated. However, the paper should report per-atom energy error or acknowledge this confound. (Metrics defined at line 155–158.)

3. **No error bars or variance reporting.** The results (Figures 2–4) show single values with no indication of run-to-run variance. No mention is made of multiple random seeds. Without this, the reader cannot assess whether reported differences (e.g., EquiFormerV2 vs. GemNet on a given task) are statistically reliable. This is common in computationally expensive MLFF training, but a statement of effort (e.g., "training each model once due to cost") would be appropriate.

4. **"ab initio" overstatement for reference data.** The abstract and introduction refer to "ab initio molecular dynamics (AIMD) trajectories" (line 55). Section 3 correctly identifies GFN2-xTB as a "semi-empirical tight-binding approach" (line 85). This terminology inconsistency is minor but could mislead readers unfamiliar with the method hierarchy.

### Trivial

- Figure 3 caption lists "EquiFormV2" while the paper's model name is "EquiFormerV2" — minor typographical inconsistency across figure captions.

---

## Nice-to-Haves

- **Include an oracle or positive baseline.** Every model fails on every OOD task. Without any baseline that succeeds (e.g., a linear group-contribution model, or a model explicitly designed for systematic generalization), the reader cannot gauge whether the tasks are unreasonably hard or whether current MLFFs are genuinely limited. A simple additive model over functional groups would provide a useful upper bound on what minimal compositional reasoning looks like.
- **Diagnose failure modes.** The paper catalogs that models fail, but does not analyze *why*. For the duplication task, does the model handle one copy of the functional group correctly but fail on the second? Does error correlate with distance from the novel motif? These analyses would substantially increase the paper's diagnostic value.

---

## Removed Points

*These were flagged by the reviewers but removed after cross-checking against the paper. They are listed here for transparency; treat them with caution.*

- **"Length extrapolation is mischaracterized as compositional generalization."** — The paper explicitly distinguishes length generalization from systematicity, citing Hupkes et al. (2020) in Section 3.1 ("The evaluation tasks in GMD-25 focus on two central aspects of compositional generalisation, namely *length generalisation* and *systematicity*"). This is not a mischaracterization; the critic's narrower definition of compositionality is one the paper acknowledges and scopes around.
- **"No successful baseline — benchmark only shows failures."** — This is a request for additional experiments, not a flaw in the presented work. Many benchmark papers contribute useful negative findings without providing a successful oracle.
- **"Functional group composition is chemically plausible but not physically rigorous — interactions are not a simple sum."** — The paper does not claim the energy decomposes additively. It tests whether models can *learn* to compose subcomponents, not whether such composition is chemically trivial. This is an appropriately challenging task design choice.
- **"Could be a problem with limited receptive field, training data, or inductive biases"** — The paper already acknowledges architectural limitations as a possible explanation (Section 5). The critic's alternative hypotheses do not invalidate the presented findings.
- **"Missing experiments: per-atom energy, model with long-range mechanisms, physically structured models"** — These are valid suggestions for future work, but the paper's scope is the benchmark and the initial evaluation; it does not claim to diagnose all failure causes.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that current MLFFs fail systematically on compositional generalization tasks — is well-supported by the evidence. The observation that ID performance does not predict OOD performance (e.g., EquiFormerV2 excelling on forces while collapsing on energy OOD) is a useful nuance that goes beyond a simple "all models fail" story.

---

## Suggestions

1. **Clarify Figures 2 and 3.** Either define PBE0 and m4s in the model section (Section 4.1), or remove them and show only the five described models. If PBE0 is included as a DFT reference baseline, explain what it is and why it is included.
2. **Normalize energy error.** Report per-atom energy MAE alongside or instead of total energy MAE for Task 1 (Length Extrapolation), or at minimum discuss the size confound when interpreting the energy gaps.
3. **Add variance information.** Report results over multiple random seeds or, failing that, explicitly state the number of runs and the limitation.
4. **Add a diagnostic analysis.** For at least one task (e.g., Duplication), visualize per-atom force errors to show *where* models fail — is the error concentrated at the novel functional group or distributed globally?
5. **Tone down "ab initio" language.** Replace "ab initio molecular dynamics" with "semi-empirical MD trajectories (GFN2-xTB)" in the abstract and introduction.

---

## Score and Decision

### Calibration Anchors

The following anchor papers were retrieved via `calibration_search`. I list all that came back in the batch, with a brief comparison to the paper under review.

**Low-scoring anchor (avg ≤ 4):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KNQJtoPZmz.md` — avg 3.00. A theoretical paper on simplicity bias with unclear claims and weak evidence. **The current paper is substantially stronger: it has a concrete, reproducible benchmark, clear experiments, and a well-motivated research question.**

**Medium-scoring anchors (avg 3.5–7.5):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NvJxTjTQtq.md` — avg 6.00. EGraFFBench: benchmarks 6 equivariant GNN force fields on 8 datasets and OOD tasks. Similar scope (benchmarking MLFFs OOD) and findings. **Comparable contribution level, but the current paper has a more systematic task design; EGraFFBench is stronger on evaluation breadth (dynamic metrics) but weaker on controlled compositionality.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Xk9Q0CrJQc.md` — avg 6.25. Proposes test-time refinement methods for MLFF distribution shifts. **The current paper contributes a benchmark rather than a method; both address similar underlying questions. The current paper's benchmark design is cleaner, but it lacks the mitigation component.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sfi2j1Ot6j.md` — avg 6.50. FreeCG: architectural improvement for MLFFs with strong empirical results. **The current paper is a benchmark contribution, not a method paper; different contribution type makes direct comparison difficult.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4S2L519nIX.md` — avg 6.50. Pre-training and scaling geometric GNNs for OOD transfer. **Stronger on breadth and methodology; the current paper is more focused on controlled compositionality tasks.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NSlvSDQ8aE.md` — avg 7.00. Force-guided bridge matching for time-coarsened dynamics. **Different task; higher score due to proposing a method with empirical gains.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rwmWd2rjP1.md` — avg 4.75. Molecule relaxation with diffusion models. **Weaker execution; current paper is more solid.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/J4V3lW9hq6.md` — avg 5.00. Protein-ligand binding dynamics framework. **Comparable overall quality but different domain.**

**High-scoring anchors (avg ≥ 7.5):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KSLkFYHlYg.md` — avg 8.00. ShEPhERD: generative model for drug design with strong evaluation. **The current paper is not at this level — it lacks the novelty of a new method and the depth of validation.**

**Relative positioning:** The paper is comparable to the medium-scoring MLFF benchmarks (EGraFFBench at 6.00, distribution shifts at 6.25) in terms of contribution. It has a cleaner task design but is weakened by presentation issues (unexplained baselines in figures, no error bars) and a less thorough analysis of *why* models fail. It is clearly stronger than the low-scoring anchors.

**Score justification:** The core benchmark contribution is solid and addresses an important gap. The weaknesses are correctable and do not invalidate the main findings. However, the unexplained baselines in the main results figures and the confounded energy metric for Length Extrapolation prevent the paper from reaching the quality bar for acceptance in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>