## Summary

GMD-25 is a benchmark for evaluating compositional generalisation in Machine Learning Force Fields (MLFFs). It introduces four tasks—length extrapolation, functional group composition, functional group duplication, and functional group combination—that require models trained on small molecules or simple functional-group instances to generalise to structurally novel but physically tractable test molecules. Five representative MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and all exhibit substantial OOD performance degradation. An accompanying data-generation toolkit is released to facilitate benchmark extensibility.

---

## Strengths

- **Systematic compositional task design**: The four tasks each isolate a distinct generalisation challenge (chain-length extrapolation, functional-group composition, duplication, combination) with explicit controls on training/test molecule overlap. For example, Task 4 keeps the molecular scaffold identical (same chain lengths in training and test) while varying only the combination of end-group identities, cleanly isolating recombination failure from all other confounds. This level of design discipline is absent from existing MLFF benchmarks.

- **Consistent empirical demonstration of generalisation failure across all architectures**: Figures 2–4 show that forces MAE increases sharply at the distribution boundary for every tested model across every task. For Tasks 2 and 3, forces MAE in the OOD region is at least one order of magnitude above the ID baseline for all five architectures under Bayesian-optimised hyperparameters, directly supporting the claim that current architectures lack transferable representations of inter-atomic interactions.

- **Augmented task variants provide additional diagnostic depth**: Tasks 1 and 2 each include an augmented variant where the training data provides demonstrations of all building blocks needed for OOD molecules. The finding that augmented training does not close the generalisation gap (Figures 3, 4c–d) is informative beyond the base tasks alone and adds nuance to the diagnostic picture.

- **Clear and accurate positioning against existing benchmarks**: Section 2.3 accurately distinguishes GMD-25 from MD17/MD22 (equilibrium or intra-molecule diversity), Transition1x (reaction-pathway extrapolation), BOOM (property-value extrapolation), and DrugOOD (scaffold-based splits). The claim that prior benchmarks do not systematically manipulate functional-group identity or chain length to probe compositional generalisation is well-founded.

---

## Weaknesses

### Fatal
None.

### Major

- **Energy MAE is not atom-normalised, confounding the most emphatic quantitative claims.** The energy metric is defined in Section 4.2 as MAE_energy = (1/M) Σ |Ê_j − E_j|, dividing by the number of *molecules* (M), while the forces metric divides by 3N (atom count × 3). Energy is an extensive quantity: a molecule with twice as many atoms has roughly twice the absolute energy. For Task 1 (OOD alkanes with 7–13 carbons vs. training alkanes with 2–6 carbons) and Task 3 (dicarboxylic acids with more atoms than the monocarboxylic training set), even a perfectly size-extensive model would produce systematically larger per-molecule absolute energy errors on the OOD set. The paper treats OOD energy errors that are "two orders of magnitude higher" (Section 4.3, Task 3, panel e) as evidence of "fundamental failure," but this comparison is not cleanly size-controlled. The forces MAE, which is atom-normalised, tells a consistent and credible story of generalisation failure on its own; the energy metric adds rhetorical force but introduces a confound that requires per-atom normalisation before the quantitative claims can be assessed at face value.

### Minor

- **Broad conclusions are not scoped to single-task models trained from scratch.** Section 4.1 justifies the exclusion of foundation models (MACE-MP-0 etc.) in one sentence: "pre-trained on large and diverse sets of molecules, making it harder to untangle memorisation and generalisation effects." This is a reasonable methodological choice, but the introduction and Section 5 draw conclusions such as "current approaches fail at compositional generalisation" and "a critical gap between impressive accuracy… and ability to extrapolate" without qualifying that these apply only to single-task, from-scratch-trained models. A practitioner considering whether to use an MLFF for a novel molecule would reach first for a fine-tuned foundation model. The conclusions should either scope down explicitly or acknowledge what the findings do and do not say about foundation model generalisability.

- **Hyperparameter selection procedure does not clarify whether a separate ID validation set was used.** Section 4.2 states that Bayesian optimisation was conducted to achieve "best possible performance on the in-distribution data." If the ID test set (rather than a held-out ID validation set) was used directly during optimisation, the reported ID numbers are mildly optimistic and the ID/OOD comparison is slightly unfair. The paper does not clarify this; a sentence in Section 4.2 confirming the use of a validation-vs-test split would remove the ambiguity.

- **The "best ID model ≠ best OOD model" finding is presented as a principled insight but is better described as "different models fail differently."** Section 5 highlights that EquiFormerV2 leads on forces but collapses on energy OOD in Task 1, while GemNet leads OOD on Task 3. Because *all* models fail substantially OOD, the ranking differences are small relative to the universal collapse, and the framing "best ID ≠ best OOD" slightly overstates the interpretive value. A more accurate characterisation would be that architectural choices determine the *mode* of failure rather than whether failure occurs.

- **GFN2-xTB label quality for polar functional groups is not discussed.** Section 3.2 justifies GFN2-xTB as the reference method. Several tasks involve hydroxyl, carboxyl, and amine groups, where GFN2-xTB is known to have systematic errors in hydrogen-bonding and intramolecular non-covalent interactions. Users relying on GMD-25 to train production models would benefit from a brief acknowledgement of these known limitations of the reference method.

### Trivial

- Task 2 description states that carboxylic acid "can be seen as a composition" of alcohol (−OH) and aldehyde (−CHO). The language is appropriately hedged ("can be seen as") but a one-sentence clarification that the composition is structural rather than strictly additive (the co-location on a single carbon modifies the electronics of both groups) would prevent misinterpretation of the task's physical premise.

---

## Nice-to-Haves

- Including at least one atom-additive or group-contribution model as a reference point would establish that the tasks are, in principle, solvable by a size-extensive architecture, ruling out the alternative hypothesis that the "correct" per-molecule labels are not compositionally decomposable in the way the tasks assume.
- A brief discussion of *why* the augmented variants failed to close the generalisation gap (Tasks 1 and 2) would strengthen the empirical analysis. The augmented training data provides all building-block information the model needs; understanding what was not extracted is a meaningful finding.
- Explicit acknowledgement that GMD-25 covers only linear substituted alkyl chains and does not yet extend to ring systems, branching, or multi-functional scaffolds common in drug discovery would align the benchmark's stated motivation with its actual coverage.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "augmented variants are not clearly easier in practice" as a weakness**: The paper explicitly presents and discusses the failure of augmented training in Sections 4.3 and Figure 3/4, so this is not a missing analysis — it is a reported finding. Removed as a strawman.
- **Strength Finder — generic importance framing**: "The combinatorial vastness of chemical space makes exhaustive coverage impossible" (motivation statement). Removed as generic motivation language, not a concrete paper strength.
- **Strength Finder — "the findings unequivocally demonstrate current models' inability"**: This echoes the paper's own abstract language and depends on the energy metric not being confounded; given the normalization concern, the word "unequivocally" should not be credited as a strength.

---

## Novel Insights

The most genuinely novel diagnostic finding — surfaced by the benchmark design rather than claimed in the paper — is the dissociation between energy and force generalisation: models such as EquiFormerV2 that achieve the best atom-level force predictions in the OOD regime simultaneously collapse on total-energy prediction, while simpler models (SchNet, DimeNet++) exhibit the reverse pattern. This dissociation suggests that these architectures have learned representations that are locally accurate (atom-environment force prediction) but globally incoherent (total-energy extrapolation), which is an interesting structural limitation worth highlighting explicitly. If verified under per-atom energy normalisation, it would be a distinctive and actionable result for future architecture design.

---

## Suggestions

1. Replace the per-molecule energy MAE with per-atom energy MAE (divide by N rather than M) and re-run Figures 2–4. This single change would allow both metrics to tell a unified, size-extensive story, and would let the paper determine whether the energy "orders of magnitude" finding holds after correcting for system size.
2. Add one sentence to Section 4.2 confirming that hyperparameter optimisation used a held-out ID validation set distinct from the ID test set, to rule out any optimism in the reported ID numbers.
3. Reframe the conclusions in Section 5 to explicitly scope the findings to single-task models trained from scratch, noting that foundation-model behaviour under compositional shift is an open question and a natural next study with this benchmark.
4. Consider adding a simple atom-additive baseline (e.g., a sum of per-atom contributions learned by linear regression on training data) as a lower-bound reference point for Tasks 1 and 3, where a compositionally correct model should, by construction, generalise well.

---

## Score and Decision

**Originality**: The benchmark fills a genuine gap — no prior MLFF benchmark uses controlled functional-group manipulation and chain-length splits to isolate compositional generalisation. The four-task design is creative and systematic. (4/5)

**Importance of research question**: Compositional generalisation is the fundamental bottleneck preventing from-scratch MLFFs from covering chemical space; the question is directly relevant to drug discovery and materials science. (4/5)

**Claims supported**: The forces MAE results robustly support the core claim of widespread OOD failure. The "orders of magnitude" energy claims are potentially confounded by the non-atom-normalised metric, weakening the paper's most dramatic statements. (3/5)

**Soundness of experiments**: The evaluation protocol (Bayesian hyperparameter optimisation, five diverse architectures, four tasks with augmented variants) is thorough. The main methodological gap is the energy normalisation. (3/5)

**Clarity**: Well-structured, tasks are clearly motivated, figures are informative. The metric definitions in Section 4.2 are precise enough to reveal the normalisation issue. (4/5)

**Value to the research community**: The benchmark and extensible toolkit are immediately usable; the empirical finding that all state-of-the-art architectures fail badly at compositional generalisation is an important negative result for the field. (4/5)

This is a well-executed benchmark paper addressing a real and underexplored problem. The core finding of compositional generalisation failure is credible and is supported by the forces metric alone. The energy normalisation issue is significant but repairable and does not invalidate the paper's contribution; it requires a revision rather than a rejection. The scope of the conclusions should be tightened to match the evidence. The paper merits acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>