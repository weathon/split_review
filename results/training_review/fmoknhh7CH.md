Here is the consolidated meta-review.

---

## Summary

This paper proposes two related methods: **HarmonicFlow**, a flow-matching generative model for 3D protein–ligand docking that operates directly on Cartesian coordinates (with a harmonic prior, self-conditioning, and equivariant refinement TFN layers), and **FlowSite**, which extends HarmonicFlow to jointly generate both the discrete residue types of a binding pocket and the 3D pose of the (multi-)ligand. FlowSite is the first deep learning approach for binding-site design that does not require ground-truth 3D ligand positions as input. The paper reports that HarmonicFlow outperforms DiffDock's diffusion process on PDBBind docking tasks (e.g., 24.4% vs. 16.3% <2Å on time-split Distance-Pockets) and that FlowSite recovers 47.0% of contact residues versus 39.4% for the best baseline (PiFold with 2D ligand input), nearly closing the gap to an oracle method (51.4%) that has access to the true ligand pose.

---

## Strengths

- **Self-conditioned flow matching demonstrably improves structure generation.** The ablation in Table 4 is clean: removing self-conditioning drops predictions with RMSD <2Å from 19.8% to 10.7%. This adaptation of AlphaFold2-style recycling to continuous flow matching is a novel and practically valuable contribution.

- **HarmonicFlow outperforms DiffDock's diffusion process in multiple docking settings.** On PDBBind time-split Distance-Pockets, HarmonicFlow achieves 24.4% vs. 16.3% <2Å (Table 1); on the more challenging sequence-based split, 18.8% vs. 14.5%. The paper is transparent that these compare raw generative models without confidence-model post-selection, which is the appropriate comparison for a generative process.

- **First deep learning method for binding-site design without 3D ligand poses.** FlowSite addresses a genuinely new task: designing pocket residues given only the backbone and the ligand's 2D chemical graph. Table 3 shows substantial improvement over PiFold variants (47.0% vs. 39.4% recovery on PDBBind), nearly matching the oracle Ground Truth Pos (51.4%). This opens a practical direction for de novo pocket design.

- **Harmonic prior provides an effective inductive bias for multi-ligand systems.** Table 4 shows that replacing the harmonic prior with an isotropic Gaussian reduces %<2Å from 19.8% to 11.3%. The qualitative illustration in Figure 3 shows it prevents different ligands from intermixing at initialization — simple and well-motivated.

- **Systematic ablation study provides useful guidance for future work.** Table 4 investigates five design choices (prior type, velocity vs. x₁ prediction, standard vs. refinement TFN layers, refinement loss, self-conditioning, interpolation noise). The finding that x₁ prediction is dramatically better than velocity prediction (19.8% vs. 5.3% <2Å) is a practically important insight for applying flow matching to biomolecular tasks.

---

## Weaknesses

### Fatal
None.

### Major

1. **The discrete "flow" in FlowSite is not a proper flow matching process, which overstates the claimed contribution.** The paper claims "a novel elegant framework to jointly generate discrete and continuous data" (Contribution 1) and calls this a "joint discrete-continuous flow." However, Section 3.2 explicitly states the method operates "without defining a discrete data interpolation" and the discrete "flow" consists of iteratively predicting $\tilde{a}_1^{t+\Delta t}$ from the model and feeding it back as self-conditioning — this is iterative refinement (recycling), not a flow with a defined probability path transporting a prior to data. The paper is transparent about what it does, but the presentation claims more than the method delivers. This does not invalidate the practical system (the method works), but the claim of a "general framework to jointly generate discrete and continuous data" is not supported: the discrete component is a recycling classifier with cross-entropy loss attached to a flow for the continuous part.

### Minor

2. **Missing ablation of fake-ligand data augmentation.** Both FlowSite and the Ground Truth Pos oracle use fake-ligand augmentation, while the PiFold baselines do not. The 7.6 percentage point improvement over PiFold (2D ligand) on PDBBind cannot be confidently attributed to the joint flow framework versus the augmentation. A simple ablation — FlowSite with and without fake-ligand augmentation — is needed to separate these factors.

3. **Weak baselines for multi-ligand docking (Table 2).** The only comparison is against a self-constructed "EigenFold Diffusion" baseline (same architecture, different training objective). While the paper correctly notes that classical docking tools like AutoDock VINA are inapplicable because side-chain positions are unknown during pocket design, a simple heuristic baseline — e.g., placing ligands at the pocket center with random rotations — would establish a meaningful lower bound. The large reported gap (58.7% vs. 37.9% <2Å) is more convincing with such a reference point.

4. **No variance or confidence intervals reported.** All results are averaged over 10 samples per ligand, but no measure of stochasticity (standard deviation, error bars) is provided. Given the small number of samples, the significance of observed differences across methods is unclear.

### Trivial

5. **BLOSUM score is introduced but not validated.** The paper proposes a new metric that accounts for amino acid similarity but provides no evidence that it correlates with binding function better than simple recovery. If the metric is to be useful to the community, a validation experiment or citation to prior validation is needed.

6. **Minor framing overstatement.** The abstract calls FlowSite "the first general solution for binding site design," but the evaluation is limited to sequence recovery on known binding sites, not experimental validation or de novo design. The conclusion appropriately acknowledges this ("recovery results cannot replace biological validation"), so the issue is only in the abstract and introduction.

---

## Nice-to-Haves

- **Analysis of generated ligand pose validity** (steric clashes, bond geometry in the protein context) to confirm that low RMSD predictions are physically realistic.
- **Investigation of whether recovery improvements translate to better binding scores** (e.g., docking score or MM-PBSA with predicted side chains), though the paper correctly notes that such tools require atomic side-chain structures that are unavailable at design time.
- **Comparison with an iterative refinement baseline** using the same architecture but without the flow-matching objective (trained only on the final loss) to isolate the benefit of the flow formulation.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that classical docking (AutoDock VINA) should have been used for multi-ligand docking.** The paper explicitly justifies that VINA requires all-atom side-chain representations which are unavailable in the pocket design setting (Section 4.2, lines 169–170). This is a scope-appropriate choice, not an omission. The criticism is weakened and subsumed by the heuristic-baseline suggestion in Minor weakness #3 above.

- **Criticism about missing qualitative examples (Figure 12 in appendix).** The parser strips appendix content from all papers; these exist in the original submission. Removed per hard rules.

- **Criticism about validating BLOSUM score.** This is already kept in Trivial weaknesses as a minor point (not a major issue).

- **Strength claiming "fake ligand data augmentation" as a core strength.** The strength's own text admits "its contribution is not isolated in the tables" and speculates it is "likely a factor." This conflicts with the verified weakness (missing ablation). Removed per rule that when a strength and weakness disagree, the weakness wins.

---

## Novel Insights

The strongest insight to emerge from these reviews — beyond the paper's own contributions — is the methodological asymmetry between the continuous and discrete components. The paper's practical success (FlowSite outperforming baselines) is arguably driven by the continuous flow matching for ligand poses, which is theoretically grounded and carefully ablated, while the discrete residue-type prediction is essentially a well-engineered recycling classifier. This raises an interesting question for the field: can a "joint discrete-continuous generative model" that uses a proper flow for one modality and recycling for the other be considered a unified framework? Future work might either develop a truly joint flow (with a defined discrete probability path, e.g., via discrete diffusion or absorbing-state flows) or drop the framing and simply present the discrete part as a conditioned classifier, which would be more honest about what the method actually does.

---

## Suggestions

1. **Add an ablation of fake-ligand data augmentation** (FlowSite with and without it) to Table 3 or as a separate table. This would cleanly separate the contribution of augmentation from the joint flow framework.
2. **Add a simple heuristic baseline for multi-ligand docking** (e.g., centroid placement with random rotations) to Table 2.
3. **Add standard deviations or confidence intervals** to all main tables (Tables 1–3). With 10 samples per ligand, the variance could be substantial.
4. **Revise the presentation of the discrete component** to avoid claiming it is a "flow" in the same sense as the continuous part. The paper is already transparent in Section 3.2 ("without defining a discrete data interpolation"), but the abstract and contribution list should match this nuance. Frame it as "joint structure generation with self-conditioned recycling over residue types" rather than "joint discrete-continuous flow."
5. **Validate the BLOSUM score** with a brief analysis showing it correlates with experimental metrics or functional scores, or remove it as a claimed contribution.

---

## Score and Decision

This paper makes genuine and well-supported contributions: self-conditioned flow matching for molecular docking yields consistent improvements over the diffusion baseline, the harmonic prior is a clean idea for multi-ligand settings, and FlowSite opens a new task (binding-site design without 3D ligand poses) with competitive results. The weaknesses are real but addressable — the main one is overclaiming the discrete "flow" component, and the missing ablation of fake-ligand augmentation weakens the attribution of FlowSite's gains. None of these are fatal; they can be resolved with additional experiments and more precise framing. The work is a solid contribution to the field.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>