---
job_id: c7100a48-9e94-42ba-bdbe-3a4e90bf4fc4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: WxTlAbRUE6.pdf
paper: Benchmarking Compositional Generalisation for Learning Inter-atomic Potentials
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a machine learning benchmark paper for graph/equivariant models in physical sciences, with direct relevance to representation learning, generalization, and datasets/benchmarks.

## Minimum Quality
Pass ✅. The paper includes the expected components for a benchmark submission, namely abstract, introduction, related work, benchmark/task design, experiments, quantitative results, and conclusion; while there are substantive weaknesses, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper introduces GMD-25, a benchmark for evaluating compositional generalisation in machine learning force fields (MLFFs). The benchmark defines four tasks, length extrapolation, functional group composition, functional group duplication, and functional group combination, all based on train/test splits across different molecules rather than different configurations of the same molecule. The authors evaluate five established MLFF architectures, SchNet, PAINN, DimeNet++, GemNet, and EquiFormerV2, and report substantial in-distribution to out-of-distribution performance gaps across all tasks.

## Strengths
The paper addresses a real and under-evaluated issue in MLFF research. Most standard evaluations indeed train and test on the same molecules, so the paper’s central premise, namely that this setup says little about compositional generalisation across molecules, is well motivated in Section 1 and Section 3.

The benchmark design is conceptually clean and easy to understand. The four tasks in **Figure 1** are physically interpretable and map reasonably well onto different notions of compositional generalisation. In particular, the distinction between length extrapolation, composition of familiar functional motifs, duplication of motifs, and asymmetric recombination gives the benchmark some structure beyond a generic OOD split. This is one of the more convincing parts of the paper.

The empirical results are directionally consistent and reveal a nontrivial mismatch between ID accuracy and OOD behavior. **Figure 2** is especially useful here: it shows that several models with very low force MAE on shorter in-distribution alkanes experience a sharp error increase once the chain length crosses into the OOD region. That figure supports the authors’ main claim that strong ID performance does not imply transferable physical understanding. Likewise, **Figure 4** shows that the failure is not isolated to one task or one architecture, but appears across the whole suite.

The benchmark appears reasonably broad for an initial molecular compositional generalisation dataset. The paper covers 118 molecules and nearly 300k labelled geometries, and the toolkit description in Section 3.2 makes the resource sound extensible rather than frozen to one ad hoc split.

I also appreciated that the paper compares both energy and force prediction rather than reporting only one of them. The contrast highlighted in Section 4.3, for example EquiFormerV2 doing well on force MAE but poorly on energy MAE in some OOD settings, is scientifically interesting and suggests the benchmark can expose different failure modes.

The supplementary numeric tables are helpful for grounding the visual impressions from the figures. For example, **Table 5** makes it explicit that for Functional Group Composition, OOD force MAE rises dramatically relative to ID across all models, and OOD energy MAE can become extremely large, especially for EquiFormerV2 and DimeNet++. Even though the main paper emphasizes the figures, the table confirms that the reported generalisation gaps are not a plotting artifact.

## Weaknesses
1. **The paper’s headline conclusion is broader than what the experimental evidence really supports, because the benchmark lacks stronger baselines that would establish whether the tasks are genuinely “solvable if the model learns the physical principles.”**  
   This claim appears repeatedly in the Introduction and Section 3.1, but the evidence provided is only that five neural MLFFs struggle. That is not the same as showing the tasks are well calibrated probes of compositional reasoning rather than simply hard extrapolation problems under this training regime. A useful benchmark paper should do more than show that some current models fail. It should also provide at least one stronger point of reference, for example a more explicitly physics-structured baseline, a simple analytical baseline, or even a scaling-based reference for length extrapolation. Without that, the benchmark risks conflating “OOD failure of these particular models” with “failure to learn compositional physical principles” in a way that is stronger than the data warrants.

2. **The model suite is not sufficiently representative of the current MLFF landscape for the paper’s framing about the limitations of state-of-the-art approaches.**  
   Section 4.1 explicitly excludes foundation models because pretraining would make memorisation and generalisation harder to disentangle. I understand the motivation, but this choice weakens the practical relevance of the benchmark. If the paper wants to argue that current MLFFs do not generalise compositionally, then omitting modern pretrained or universal potentials removes an important part of the picture. At minimum, the paper should position itself more carefully and say that it studies generalisation of from-scratch supervised MLFFs under controlled splits. As written, the framing is broader than the evaluation.

3. **The treatment of energy errors is scientifically problematic in the length extrapolation tasks, because the metric appears to be based on total energy rather than a size-normalised quantity. This makes some of the strongest claims hard to interpret.**  
   In Section 4.2, the paper defines
   \[
   \mathrm{MAE}_{\text{energy}} = \frac{1}{M}\sum_{j=1}^{M} |\hat E_j - E_j|.
   \]
   For molecules of increasing size, total energy is extensive, so absolute error on total energy can grow simply because the number of atoms grows, even if the per-atom or per-bond description is reasonable. This matters a lot for **Figure 2(a)**, where OOD energy MAE explodes for some models as chain length increases. That figure may indeed indicate poor generalisation, but part of the trend could also be a metric artifact caused by evaluating total energy across molecules of different sizes. The paper should report at least one normalized alternative, such as per-atom energy MAE, atomization-energy error, or an error after removing a learned size-extensive baseline. Right now the benchmark may be overstating OOD energy failure in the very task where molecular size changes by construction.

4. **The mathematical definitions of the evaluation metrics are underspecified and in one case appear inconsistent with the actual data structure.**  
   The benchmark is built from trajectories with many snapshots per molecule, but in Section 4.2 the energy MAE is written as averaging over \(M\), “the number of molecules in the test set,” with \(\hat E_j\) the predicted energy for molecule \(j\). That is inconsistent with the rest of the paper, where the basic prediction unit is a molecular configuration or frame, not one aggregate energy per molecule. Likewise, the force MAE is defined over \(N\) atoms “across all molecules,” but the indexing does not make clear whether atoms are pooled across all frames, whether the averaging is per-frame then per-dataset, or whether larger molecules/longer trajectories receive more weight. This is not a cosmetic issue. For benchmark papers, metric definitions need to be precise because implementation details can materially affect rankings. The paper should rewrite these metrics using snapshot-level indexing, for example
   \[
   \mathrm{MAE}_{E} = \frac{1}{|\mathcal{D}|}\sum_{x\in\mathcal{D}} |\hat E(x)-E(x)|,
   \]
   and
   \[
   \mathrm{MAE}_{F} = \frac{1}{\sum_{x\in\mathcal{D}} 3|V(x)|}\sum_{x\in\mathcal{D}}\sum_{i\in V(x)}\sum_{c\in\{x,y,z\}} |\hat F_{i,c}(x)-F_{i,c}(x)|.
   \]
   As written, the equations are too loose for a benchmark paper.

5. **The experimental protocol is optimized for ID performance, but the paper then draws conclusions about OOD generalisation without carefully disentangling model capacity from model-selection mismatch.**  
   Section 4.2 says hyperparameters were tuned “to ensure that each model achieved its best possible performance on the in-distribution data.” That is a legitimate choice, but then the benchmark should explicitly acknowledge that the selected hyperparameters may be suboptimal for OOD behavior, and rankings may partially reflect this. In some benchmarks that is fine, but here OOD generalisation is the whole point. A stronger study would either report sensitivity of OOD performance to hyperparameter choice, or at least discuss whether the ID-optimal checkpoint/model was used for final OOD reporting. Otherwise, it is hard to know if the paper is measuring architectural inductive bias or simply the fragility of ID-driven model selection.

6. **The empirical evidence lacks uncertainty estimates, repeated runs, or significance analysis, which is a noticeable omission for a benchmark paper with relatively small task-specific datasets.**  
   All main results in **Figures 2 to 4** are presented as single trajectories of model performance with no error bars and no seed variation. Since the conclusions hinge on relative comparisons, for example whether GemNet generalises better than EquiFormerV2 on one task but worse on another, the absence of variance information makes those model-ordering claims less convincing. The existence of large ID-to-OOD gaps is probably robust, but the finer comparative story is not demonstrated with enough statistical care.

7. **The paper documents failure modes more than it explains them.**  
   This is where the benchmark feels useful but still somewhat incomplete as a scientific contribution. The supplementary analysis in **Figure 5** and **Figure 7** is actually interesting, because it suggests that in some tasks models preserve force direction fairly well while failing on force magnitude. That is a meaningful diagnostic signal. However, in the main paper this is barely integrated into the interpretation. If the benchmark’s goal is to guide development of better inductive biases, then it should push harder on diagnosis. For instance, why is cosine similarity nearly perfect in some OOD length extrapolation settings while energy errors collapse? Why do some models preserve force direction but miss magnitudes? Right now the paper stops one step short of turning the benchmark results into concrete scientific insight.

8. **Some presentation details undermine confidence in the care of the experimental section.**  
   The most obvious example is in **Table 2** in the appendix, where the alkane formulas suddenly appear as “C7N16”, “C8N18”, etc., which are almost certainly typographical errors for \( \mathrm{C}_7\mathrm{H}_{16} \), \( \mathrm{C}_8\mathrm{H}_{18} \), and so on. There are also several naming inconsistencies across tables, for example repeated placeholders such as “CURS200M” and “CINNAM” that are not self-explanatory from the main text. These are not fatal by themselves, but benchmark papers live or die on trust in the data specification and evaluation protocol, so this level of sloppiness matters more than it would in a purely methodological paper.

9. **The benchmark construction choices are somewhat narrow, and the paper overstates how generally they reflect “physical principles.”**  
   Section 3.2 states the trajectories are generated in vacuum using a Langevin thermostat and GFN2-xTB labels. That is a reasonable starting point, but it restricts the chemical regime substantially. The tasks are all based on mostly linear carbon-chain molecules with a small set of functional groups. That makes the benchmark controlled, which is good, but also means the conclusions should be framed as evidence about controlled compositional molecular extrapolation in this narrow regime, not as a broad statement about learning “underlying physical principles” in inter-atomic potentials more generally.

10. **The results presentation is almost entirely visual in the main paper, which makes some claims harder to audit without going to the appendix.**  
   **Figure 4** effectively conveys that OOD errors are much larger than ID errors across tasks, but it also compresses many comparisons into small horizontal bar plots. Important details, such as the exact scale of the gap or whether two models are meaningfully separated, are hard to judge there. Since this is a benchmark paper, at least one compact main-paper table summarizing aggregate ID and OOD performance would have strengthened the presentation considerably. The appendix **Table 5** helps, but the main paper should stand more strongly on its own.

## Questions
1. The biggest issue for me is the interpretation of energy errors under changing molecule size. Can the authors report a size-normalized energy metric, such as per-atom energy MAE or atomization-energy MAE, for Task 1 and discuss whether the dramatic OOD trends in **Figure 2(a)** persist under that metric? A convincing answer here would materially increase my confidence in the benchmark’s conclusions.

2. Please clarify the exact averaging scheme in the metric definitions in Section 4.2. Are energy and force errors averaged over snapshots, over molecules, or in a nested fashion? How are molecules of different sizes weighted? The current notation does not match the trajectory-based dataset structure.

3. How exactly was model selection performed after hyperparameter tuning? Was the final checkpoint selected using the ID validation split only, and if so, was that done consistently across all tasks and models? It would help to know whether the reported OOD results correspond to the best ID-validation checkpoint or the final training epoch.

4. Do the main conclusions remain the same across multiple random seeds? Even reporting mean and standard deviation for a subset of tasks would strengthen the benchmark substantially.

5. Can the authors provide at least one stronger reference baseline that is not just another standard neural architecture, for example a simple physically motivated additive baseline or a size-extensive energy correction? This would help establish whether the tasks are well calibrated rather than merely difficult.

6. The force diagnostics in **Figure 5** and **Figure 7** are potentially quite informative. Can the authors expand the discussion in the main paper to explain why some models keep high cosine similarity yet fail in force magnitude and energy? That analysis could make the paper more than a catalog of failures.

7. Please clarify the apparent formula/name inconsistencies in the appendix tables, especially **Table 2**. While these look like typographical issues, they make it harder to trust the dataset specification.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The paper presents a benchmark and training/evaluation study on molecular simulation data, without obvious human-subject, privacy, safety, or legal issues discussed in the main paper.

## Soundness Rating
2: fair. The benchmark idea is reasonable and the reported ID/OOD gaps are likely real, but the paper has important issues in metric specification, result interpretation, and experimental protocol detail that weaken the strength of its claims.

## Presentation Rating
2: fair. The overall narrative is understandable and the task design is clearly motivated, but several equations are underspecified, important details are left to the appendix, and there are avoidable inconsistencies in tables and naming.

## Contribution Rating
2: fair. The benchmark direction is relevant and potentially useful to the community, but the current paper stops short of making a strong benchmark contribution because calibration of the tasks, strength of the baselines, and rigor of the evaluation are not yet at the level I would expect for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The benchmark idea is timely and the central empirical observation, namely large OOD generalisation gaps for standard MLFFs, is interesting. However, the current version has too many unresolved issues around metric definition, energy-error interpretation under size shift, absence of stronger baselines and uncertainty analysis, and limited diagnostic depth for me to recommend acceptance.

## Reviewer Confidence
4: confident. I am comfortable evaluating ML benchmarks and graph/equivariant learning for molecular systems, and I checked the main equations, figures, and result tables carefully, though I did not independently verify implementation details beyond what is written.