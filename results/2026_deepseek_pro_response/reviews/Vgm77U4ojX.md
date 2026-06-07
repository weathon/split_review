Now I have sufficient calibration data. Let me write the final review.

**Calibration summary:**

Round 1 bracket: Based on comparisons with DiffDock-Pocket (5.00), VFDiff (6.00), IPDiff (6.25), and FoldFlow (8.00), SIGMADOCK plausibly sits in **6.0–7.5**.

Round 2 narrowed within this bracket:
- **GroupBind (6.75)**: Docking paper with clever idea but evaluation gaps (no PoseBusters), unfair baseline comparisons, originality concerns. SIGMADOCK has stronger theory and better evaluation but has its own significant issues.
- **DrugFlow (6.67)**: Flow matching + Markov bridges for SBDD, multiple technical contributions but significant experimental concerns (marginal-only distributions, no statistical significance). SIGMADOCK addresses a different (more focused) task with stronger evaluation rigor but less breadth.
- **VFDiff (6.00)**: SE(3)-equivariant diffusion for target-aware molecule generation, rejected for limited novelty and evaluation concerns. SIGMADOCK is clearly stronger.

SIGMADOCK compares favorably on theory and results but has its own notable issues (Figure 4/Table 4 discrepancy, missing ablation, ranking transparency). Final score: **6.5**.

---

## Summary
SIGMADOCK proposes a fragment-based SE(3)^m Riemannian diffusion model for molecular docking. Rather than modeling ligand poses via torsional angles (the standard approach), the method decomposes ligands into rigid-body fragments at rotatable bonds and learns to reassemble them within the binding pocket via diffusion on the product space SE(3)^m. The paper reports 79.9% Top-1 PB-valid success on PoseBusters — substantially above prior generative methods — and provides theoretical justification (Theorems 1 and 2) for why the fragment-based formulation is better-conditioned than torsional alternatives. Even without the post-hoc ranking heuristic, the raw generative model achieves 66.1%, still exceeding all baselines.

## Strengths
- **Theoretically-motivated fragment formulation**: Theorem 1 provides formal justification for why modeling rigid fragments in SE(3)^m yields a cleaner product-space structure than torsional approaches, which induce entangled non-product measures in Cartesian space. The discussion of extrinsic gauge ambiguity in torsional models (Section 2.2.2) identifies a genuine, rarely-discussed practical issue.
- **Strong empirical results**: Even without the ranking heuristic, the raw generative model achieves 66.1% Top-1 PB-valid (Table 1, Config D), substantially exceeding DiffDock (38.0%) and G2G/Vibe2 (58.1%). The full model at 79.9% represents a meaningful advance and is the first deep learning method to surpass classical docking under the intended train-test split.
- **Conformational alignment justification (Section 2.2.1)**: The joint SE(3)+torsion alignment experiment showing bound poses are reachable from RDKit conformers with residual RMSD ≪ 2Å provides clean, convincing justification for treating internal fragment geometry as fixed — a simple but persuasive argument.
- **Well-designed supporting experiments**: Table 1 provides interpretable ablations showing each component matters. The co-factor failure analysis (Table 2) validates that the model is not memorizing — failure rates nearly triple when natural co-factors are present. The pocket-size robustness sweep (Table 3) is informative and appropriately controlled against Vina.
- **Theorem 2 on local coordinate invariance**: The Newton-Euler prediction head elegantly resolves the ambiguity of non-canonical fragment local frames, with a formal invariance guarantee necessary for the fragment formulation to be well-posed.
- **FR3D fragmentation scheme and triangulation conditioning (Lemma 1)**: The recursive fragment reduction is principled, and the triangulation distance conditioning is a clean geometric insight that constrains bond angles without restricting dihedrals.

## Weaknesses

### Fatal
None.

### Major
- **Figure 4 (right) vs Table 4 discrepancy**: The right panel of Figure 4 reports Top-1 of 51%, 53%, 53% across the three sequence-similarity bins (≤30%, 30–95%, 95–100%), while Table 4 reports SIGMADOCK PB-valid Top-1 of 72%, 79%, 87% for identically-sized splits (109, 76, 123 complexes). If Figure 4 (right) shows RMSD-only and Table 4 shows PB-valid, RMSD-only should be ≥ PB-valid, but the numbers go the wrong way (51–53% vs. 72–87%). If both measure the same metric, one set of numbers is incorrect. This inconsistency directly affects confidence in the paper's generalization claims and must be resolved.
- **Missing fragment-vs-torsional ablation**: The paper's central theoretical thesis is that fragment-based SE(3)^m diffusion is better-conditioned than torsional diffusion (Theorem 1, Section 2.2.2). However, this claim is never tested directly: there is no ablation comparing SIGMADOCK's fragment parametrization against a torsional parametrization using the same architecture, data, and training protocol. Comparisons are only against entirely different methods (DiffDock, G2G) with different architectures, confounding the comparison. Given the investments made in other ablations, the absence of the single most important one for the core theoretical claim is a significant gap.
- **Ranking heuristic's contribution not transparently discussed**: Table 1 shows removing the energy-based scoring heuristic (Config D) drops Top-1 PB-valid from 79.9% to 66.1% — a 13.8 percentage point reduction. The headline "79.9%" is thus the product of both a generative model and a post-hoc scoring function. While 66.1% still represents SOTA generative performance, the abstract and introduction attribute the full 79.9% to the generative framework. The ranking heuristic is described only qualitatively in the main text ("pseudo binding energy," "physicochemical checks") without concrete definitions, making it difficult to assess comparability with baselines.

### Minor
- **AF3 comparison performed while disclaimed**: The paper states "we cannot directly compare SIGMADOCK to co-folding methods" (line 256) in the same paragraph that presents Table 4, which does exactly that. While the qualification is present, this internal tension weakens both the claim and the disclaimer.
- **"50× faster sampling" claim lacks context**: The comparison to AF3 conflates solving a harder problem (co-folding) with a simpler one (rigid-receptor re-docking). It is unclear whether this is per-sample or per-useful-prediction, given SIGMADOCK uses N_seeds=40 and a ranking step. Runtime comparisons against DiffDock would be more directly informative.
- **No sample diversity metrics**: The paper focuses exclusively on Top-1 accuracy but does not report any measure of binding mode diversity across the N_seeds samples, an important practical consideration for docking.
- **FR3D data augmentation claim untested**: The paper states FR3D "provides a promising stream for data augmentation" but no data augmentation results are shown.
- **Scope limitation unacknowledged**: The fragmentation scheme assumes breaking rotatable bonds yields a tree of fragments. Macrocycles and ring systems with rotatable bonds within rings break this assumption, and this limitation is not discussed.
- **Forward diffusion concern unaddressed**: Under the forward SDE (Eq. 1), fragments diffuse to independent random positions, scattering them far apart spatially. The paper does not discuss whether this creates practical difficulties for the score network to reassemble scattered fragments into a coherent bound pose.

### Trivial
None.

## Nice-to-Haves
- A direct comparison showing what happens when energy minimization is applied to SIGMADOCK outputs (since the paper emphasizes it is not required).
- Runtime and memory comparisons against DiffDock and Vina, not just AF3.
- Discussion of whether the fragment forward process could be improved by a pocket-conditioned prior rather than scattering fragments to independent random positions.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Theorem 1 proof relegated to Appendix C.2 (stripped)"** — REMOVED per hard rules: the appendix was stripped by the parser; it exists in the original submission.
- **"Architecture details in stripped appendices"** — REMOVED per hard rules: the appendix was stripped by the parser.
- **"FR3D description relies heavily on Algorithm 1 in stripped appendix"** — REMOVED per hard rules regarding appendix content.
- **Harsh critic's concern about Vina pocket definitions not being identical** — REMOVED: speculative without evidence; the paper already controls for pocket size (Table 3) showing Vina is insensitive to pocket size changes.
- **"6.3× higher PB-validity than DiffDock" claim potentially comparing against RMSD-only number** — DEMOTED from harsh critic's claim: the Figure 4 DiffDock bar is labeled under the same "Top-1 (%)" column as SIGMADOCK, and footnote 9 states fair comparison with models trained on the same split. Without access to the original Butenschön et al. (2024) paper that extracted these numbers, I cannot confirm this is an error; the paper appears to treat this as a fair comparison in good faith.

## Novel Insights
The observation that the Figure 4 (right) / Table 4 discrepancy is not merely a presentation issue but reflects numbers that cannot simultaneously be correct (PB-valid values exceeding what could be RMSD-only values for the same splits) is genuinely novel — it identifies a logical inconsistency that requires resolution.

## Suggestions
- Resolve the Figure 4 (right) / Table 4 discrepancy. If Figure 4 right shows a different metric or protocol, label it explicitly. If it contains an error, correct it. The right chart's numbers (51–53%) appear inconsistent with every other SIGMADOCK result in the paper.
- Add a fragment-vs-torsional ablation using the same architecture. If this is infeasible, at minimum temper the theoretical motivation claims and acknowledge that the empirical comparison to torsional models is confounded by architectural differences.
- Move key details of the ranking heuristic (what "pseudo binding energy" computes, what specific physicochemical checks are applied) into the main text, and report the raw generative Top-1 (66.1%) prominently alongside the post-ranked number (79.9%).
- Report sample diversity metrics (e.g., fraction of near-native poses across all N_seeds, diversity of generated binding modes).
- Acknowledge the scope limitation around macrocycles and ring systems.

## Anchors Used (all rounds)

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| CompassDock (nWO75tVjfp) | 3.00 | 1 | Weaker — dataset analysis tool, not a docking method |
| TorSeq (G536mmC2HL) | 3.00 | 1 | Weaker — conformer generation without protein context |
| DiffDock-Pocket (1IaoWBqB6K) | 5.00 | 1 | Weaker — incremental DiffDock extension, limited evaluation |
| VFDiff (5YLsnsjgeC) | 6.00 | 1,2 | Weaker — limited novelty, no PoseBuster evaluation |
| IPDiff (qH9nrMNTIW) | 6.25 | 1,2 | Slightly weaker — SBDD generation, not docking |
| EQGAT-diff (kzGuiRXZrQ) | 5.75 | 2 | Weaker — design space exploration for molecular generation |
| DrugFlow (g3VCIM94ke) | 6.67 | 2 | Comparable — multi-modal SBDD, good contributions but experimental concerns |
| GroupBind (zDC3iCBxJb) | 6.75 | 2 | Comparable — docking with group-level modeling, evaluation gaps |
| FoldFlow (kJFIH23hXb) | 8.00 | 1 | Stronger — cleaner theoretical contribution on SE(3) flow matching |

Round 1 bracket: 6.0–7.5. Round 2 narrowed to 6.5 based on comparison with GroupBind (6.75) and DrugFlow (6.67): SIGMADOCK has stronger theory and results but the Figure 4/Table 4 discrepancy and missing ablation are significant counterweights.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>