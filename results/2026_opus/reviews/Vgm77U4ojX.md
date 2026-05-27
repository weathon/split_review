Now I have enough calibration to write the review.

## Anchors Retrieved

**Round 1 (bracketing):**
- Weak (avg 3.0): m9zWBn1Y2j.md (PsiDiff), kKXIYUi8ff.md (DynamicsDiffusion), G536mmC2HL.md (TorSeq), An87ZnPbkT.md (GNNAS-Dock) — all rejected docking/conformation papers, much weaker than SIGMADOCK
- Middle: 1IaoWBqB6K.md (DiffDock-Pocket, 5.0, reject) — read; weaker contribution and confused presentation. qH9nrMNTIW.md (IPDiff, 6.25), FuXtwQs7pj.md (Toric diffusion, 4.5), jZPqf2G9Sw.md (Dynamics-Informed, 5.5)
- Strong (avg 8.0): gHLWTzKiZV.md (FlexDock, 8.0) — read; comparable scope/ambition; gHLWTzKiZV.md, KSLkFYHlYg.md (ShEPhERD), NSVtmmzeRB.md (GeoBFN), SE(3)-Stochastic Flow Matching

**Round 1 bracket: 6.0 – 8.0**

**Round 2 (narrowing):**
- kzGuiRXZrQ.md (EQGAT-diff, 5.75, accept) — design-space paper, less novel
- 5YLsnsjgeC.md (VFDiff, 6.0, reject)
- uNomADvF3s.md (Lift Your Molecules, 6.5, accept)
- g3VCIM94ke.md (DrugFlow, 6.67, accept)
- iezDdA9oeB.md (FABFlex, 7.0, accept) — read; comparable empirical strength on docking; SIGMADOCK has stronger methodological novelty
- zDC3iCBxJb.md (GroupBind, 6.75, accept) — read; SOTA on PDBBind blind docking, similar reviewer concerns about fairness; SIGMADOCK is stronger in novelty and ablations
- UfBIxpTK10.md (DockGen, 6.0, accept)
- HBbbhAZuia.md (DockedAC, 5.75, reject)

SIGMADOCK is clearly stronger than FABFlex (7.0) and GroupBind (6.75) due to (a) stronger theoretical scaffolding (Theorem 1, Theorem 2, Lemma 1), (b) larger empirical jump (6.3× DiffDock on PB-valid), (c) more thorough ablations stratifying by pocket size, sequence similarity, and co-factor presence. It is comparable to but slightly below FlexDock (8.0), which has cleaner causal experiments. The harsh critic's two main concerns (PB-aware ranker contributing ~9 absolute points to the headline number, and DiffDock being compared in blind mode against SIGMADOCK in pocket-specified mode) are real but limited in scope — the Conf. E ablation (70.8%) is itself well above the prior pocket-specified baselines (G2G/Vibe2 at 58.1%).

**Final score: 7.5**

---

## Summary
SIGMADOCK proposes a fragment-based SE(3)^m Riemannian diffusion model for re-docking, replacing the conventional torsional parametrisation with rigid-body fragments. Core technical contributions are (i) the FR3D stochastic fragment-merging scheme that reduces the number of fragments below the naive `k+1` count, (ii) Lemma-1 soft triangulation constraints that pin cross-fragment bond geometries while leaving dihedrals free, (iii) an EquiformerV2 + Newton–Euler head architecture proved invariant to local-frame choice (Theorem 2), and (iv) a PB-aware ranker over N_seeds samples. On PoseBusters under a fair PDBBind(v2020) train-test split, SIGMADOCK reports 79.9% Top-1 (RMSD<2Å ∧ PB-valid), 6.3× DiffDock, and reaches AF3-level accuracy at much lower train-test leakage.

## Strengths
- **Large, well-controlled empirical jump on the PB benchmark under a fair split.** 79.9% Top-1 PB-valid vs. 12.7–32.8% for prior PDBBind-trained DL baselines (Figure 4 / Section 3.2), 90.6% on Astex. Even with the PB-aware ranker removed (Conf. E, Table 1), Top-1 PB-valid remains at 70.8% — well above prior pocket-specified DL methods (G2G/Vibe2 at 58.1%).
- **Generalisation to low-similarity proteins.** 51% Top-1 at ≤0% sequence similarity and 72% PB-valid in [0,30) (Table 4 / Figure 4 right), addressing the standard memorisation critique with quantitative evidence.
- **Theorem 2 (frame invariance) is load-bearing and well-handled.** The Newton-Euler head from Jin et al. (2023) is adapted specifically to resolve the local-coordinate ambiguity that Section 2.4 identifies, and the proof is non-trivial.
- **Detailed component-wise ablations.** Table 1 isolates triangulation conditioning (-9 points RMSD<2Å), fragment merging (-6 points), PL interactions (-1.3 points), and PB scoring (-9 points PB-valid), allowing attribution of which inductive biases matter.
- **Pocket-size robustness sweep.** Table 3 systematically varies the pocket cutoff from 4–7Å and shows graceful degradation, addressing the natural concern that gains come from a tight search box.
- **Honest disclosure of train-test leakage trade-off with AF3.** Table 4 reports the per-sequence-similarity comparison transparently, including the slice ([0,30)) where AF3 is ahead (87% vs. 72% PB-Val.).

## Weaknesses

### Fatal
None.

### Major
- **The headline 79.9% PB-valid number includes a PB-aware sample selector; the apples-to-apples comparison is the Conf. E number (70.8%).** Section 2.5 / Appendix F describe ranking N_seeds=40 samples by a heuristic that explicitly applies PoseBusters checks. Table 1 shows that removing this drops PB-valid Top-1 by ~9 points while leaving RMSD<2Å roughly stable. The abstract's "6.3× higher PB-validity than DiffDock" comparison therefore conflates "model produces more PB-compliant samples" with "ranker filters on PB validity." This is a real evidential issue — the Conf. E reading is still a clear advance, but the abstract / introduction should foreground it rather than rely on the ranker-aided number alone.
- **DiffDock comparator in Figure 4 sits under "Holo Specified" while SIGMADOCK sits under "Pocket Specified."** This is the closest prior DL method, and its placement in the chart suggests DiffDock is being compared in blind-docking mode against SIGMADOCK in pocket-specified mode. A pocket-conditioned DiffDock variant trained on the same regime is the more appropriate comparator and should appear in the main results table rather than be deferred. The "first DL method to surpass classical docking under the PB split" framing is sensitive to this choice.
- **The theoretical case for fragments-over-torsions (Theorem 1, Section 2.2.2) is not isolated experimentally.** The paper argues fragments beat torsions because the induced Cartesian measure is non-product for the latter and factorised Haar for the former, then validates the overall system. A controlled swap (same backbone, same data, same sample budget, switch only torsion ↔ FR3D fragments ↔ FR3D + triangulation) is missing. This means the deductive line "fragments are better because of Theorem 1" is supported by motivation and end-to-end success, not by a head-to-head ablation. The paper would be stronger if the fragment formulation were framed as an empirically successful design choice that Theorem 1 motivates rather than as the deductive consequence.

### Minor
- **Failure-mode attribution to RDKit conformer quality is missing.** Section 2.2.1 hinges on ETKDGv3 producing conformers that can be torsionally/rigidly aligned to the bound pose with RMSD ≪ 2Å. At inference, only the RDKit conformer is available (no bound-pose alignment), and Table 2 shows large failure-rate variation across co-factor partitions (16% → 41%). An explicit binning of test complexes by achievable post-alignment RMSD of their ETKDGv3 conformers would tell readers where the method actually breaks (macrocyclic / strained / fused-ring ligands).
- **Co-factor failure analysis (Table 2) on natural-ligands subset is statistically underpowered.** 41.2% failure on n=17 complexes is suggestive, not powered. A line acknowledging the small-n caveat would be appropriate.
- **Triangulation conditioning empirical check is absent.** Lemma 1 says Δd_{A,C} should decay to 0 as t→0; an empirical plot of the residual triangulation error distribution on the test set would confirm the soft constraint is active in practice (Section 2.4, footnote 6).
- **FR3D inference-time variance is not isolated.** The merge is stochastic and is reported as "promising for data augmentation," but Table 1 isolates merging-vs-no-merging rather than variance across stochastic FR3D realisations on the same molecule.

### Trivial
None retained (formatting issues in the parsed PDF are not author errors).

## Nice-to-Haves
- Report Conf. E ("(-) PB Scoring") prominently in the abstract/introduction, not only in Table 1.
- Add a pocket-conditioned DiffDock (DiffDock-Pocket or DiffDock-L with the pocket given) to the main Figure 4 comparison.
- A direct controlled comparison swapping torsion ↔ naive fragments ↔ FR3D ↔ FR3D + triangulation, holding everything else fixed.
- Conformer-quality stratification: bin test complexes by post-alignment RMSD of ETKDGv3 conformers and report Top-1 within each bin.
- Apply the same PB-aware reranker (or a comparable one) to baseline methods to disentangle model vs. selector contributions to the PB-validity gap.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Theorem 1 framing is "suggestive rather than load-bearing" (harsh critic, point 4).* — Demoted into the Major weakness on missing controlled torsion-vs-fragment swap rather than kept as a separate criticism, because the substantive issue is the missing ablation, not the framing itself.
- *Comparator labels in Figure 4 ("Lando2/Rerank2/G2G/Vibe2") not introduced in main text (harsh critic, Section 3.2 note).* — These are introduced in the appendix and are recovered from the OCR'd figure; this is a parser/positioning issue rather than a substantive flaw.
- *"Strong theoretical motivation" generic strength.* — Replaced with the more specific Theorem 2 frame-invariance point, since Theorem 1's role is more motivational than load-bearing.
- *"Demonstrated generalization to unseen proteins" framed as defeating the memorisation critique.* — Retained but tempered: Table 4 actually shows AF3 ahead in the genuinely low-similarity slice, so the generalisation claim should be stated with that caveat.

## Novel Insights
None beyond the paper's own contributions. The FR3D fragment-merging procedure paired with triangulation soft constraints is itself the novel observation: it shows that the right parameterisation of small molecules for diffusion is neither pure torsion nor naive rigid-body decomposition, but a stochastically-merged fragment graph with cross-fragment distance conditioning. The combination of (a) factorised SE(3)^m forward kernel, (b) soft triangulation constraints that recover bond-angle determination per Lemma 1, and (c) frame-invariant Newton-Euler score head is a coherent design point in the docking literature.

## Suggestions
- Reframe the abstract: lead with the Conf. E figure (70.8% PB-valid without the PB-aware ranker) and present 79.9% as the ranker-aided version. This is more defensible and still impressive.
- Add a pocket-conditioned DiffDock (DiffDock-Pocket or DiffDock-L) row to Figure 4's main table. Even if the gap shrinks, the comparison is more honest.
- Run the controlled torsion ↔ FR3D-fragment ↔ FR3D+triangulation swap on the same backbone and budget. This is the experiment that would let Theorem 1 do the deductive work the paper currently asks of it.
- Stratify test complexes by ETKDGv3 conformer quality (post-alignment RMSD to the bound pose) and report Top-1 within each bin to characterise the method's failure modes.
- Verify Lemma 1 empirically: plot the distribution of residual Δd_{A,C} at t=0 on the test set.
- Note small-sample caveats explicitly in Table 2's natural-ligand row (n=17).

## Evaluation on Standard Axes
- **Originality**: High. Fragment-space SE(3) diffusion with stochastic FR3D merging and triangulation soft constraints is a genuinely new parameterisation for docking, distinct from torsion-space and all-atom approaches.
- **Importance of research question**: High. Re-docking under fair train-test splits is the standard benchmark, and the field has been stuck at PB-valid scores well below classical dockers.
- **Claim support**: Mostly strong. Headline 79.9% is partially ranker-aided; the more defensible Conf. E (70.8%) still substantiates the main claim. The "first DL method to surpass classical docking" claim is sensitive to the DiffDock comparator setting.
- **Soundness of experiments**: Solid for what is present. Ablation table, pocket-size sweep, sequence-similarity stratification, and co-factor partition are all useful. The missing direct torsion-vs-fragment swap and missing pocket-conditioned DiffDock are the main gaps.
- **Clarity**: Good. Notation is heavy but well-organised; theorems are stated cleanly.
- **Value to community**: High. Open-source codebase, clean methodological design, and a strong jump on a standard benchmark under a fair split.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>