Now I have enough calibration data. Let me write the final review.

**Round 1 Bracket**: Based on the bracketing anchors, SIGMADOCK sits clearly above the middle-bracket papers (5.5-6.5 range: DiffDock-Pocket at 5.0, VFDiff at 6.0, IPDiff at 6.25) and is competitive with the strong bracket (7.5-8.0: FoldFlow at 8.0, GeoBFN at 8.0). Initial bracket: 7.0–8.5.

**Round 2 Narrowing**: Comparing directly to FoldFlow (8.0) and GeoBFN (8.0), SIGMADOCK has a more dramatic empirical improvement over prior work and a more practically important contribution. Its weaknesses (AF3 asymmetry, metric circularity, missing wall-clock times) are minor. The paper is at least as strong as these 8.0 anchors. Score: **8.0**.

---

## Summary
SIGMADOCK introduces a fragment-based SE(3) Riemannian diffusion model for molecular docking that decomposes ligands into rigid-body fragments using a novel FR3D scheme and defines diffusion over their roto-translations rather than over torsional angles. The method is theoretically motivated (Theorem 1 demonstrates torsional diffusion induces entangled non-product measures in Cartesian space while fragment diffusion yields factorized Haar measures) and achieves 79.9% Top-1 PB-valid on the PoseBusters temporal split—substantially surpassing prior deep learning approaches (12.7–32.8%) and classical docking (~57% Vina), approaching AF3-level performance with far less training data and faster inference.

## Strengths
- **Principled theoretical motivation (Theorem 1, Section 2.2.2):** The paper formally demonstrates that torsional models induce entangled, non-product measures in Cartesian space while fragment models yield factorized Haar measures on SE(3)^m. The argument about the lever effect—local torsional changes producing non-local Cartesian displacements creating strong geometric coupling along torsional chains—is well-articulated and provides genuine first-principles insight into why torsional approaches underperform.
- **Massive empirical improvement (Table 1, Figure 4):** SIGMADOCK achieves 79.9% PB-valid Top-1 on PoseBusters compared to 12.7–32.8% from recent deep learning approaches, and 90.6% on Astex. Even without PB scoring in the ranking heuristic (Row E, Table 1), 70.8% PB-valid remains far ahead of all baselines. The improvement is sustained across both RMSD<2 and PB-validity metrics.
- **Novel FR3D fragmentation with soft triangulation constraints (Sections 2.2.3, Lemma 1):** The irreducible fragmentation scheme recursively merges adjacent fragments to reduce DoFs (empirically m ≈ ⅔·m̂), and the triangulation conditioning uniquely determines bond angles across fragments without restricting dihedral freedom. These are concrete, well-motivated technical contributions.
- **Fair comparison protocol and thorough evaluation (Section 3.1, Tables 1–4):** Training restricted to PDBBind(v2020) with PoseBusters temporal split. Evaluation spans multiple metrics (RMSD<2, PB-validity), sequence-similarity stratification, co-factor analysis, and pocket sensitivity. The co-factor analysis (Table 2) showing failure rates correlate with co-binding events (41.2% vs 16.2% with no co-factors) provides evidence the model learns meaningful physics.
- **SO(3)-equivariant architecture with formal guarantees (Theorem 2):** The Newton-Euler based prediction head resolves the non-canonical local frame ambiguity, and Theorem 2 proves invariance to local coordinate choice with rigorous proofs deferred to appendices.

## Weaknesses

### Fatal
None

### Major
None

### Minor
- **AF3 bucket-level asymmetry not discussed (Table 4):** The paper presents overall parity with AF3 (79.9% vs 80.2%) but Table 4 reveals a significant per-bucket asymmetry: on the most challenging [0,30) sequence-similarity bucket (truly unseen proteins), AF3 achieves 87% vs SIGMADOCK's 72% (a 15-point gap, though on different subset sizes: 109 vs 38). Conversely, SIGMADOCK outperforms AF3 on [95,100] (87% vs 78%). The paper calls this "competitive performance relative to AF3" (line 256) without acknowledging the complementary strength/weakness pattern. Explicitly discussing this asymmetry and hypothesizing why AF3 still wins on novel proteins (e.g., its joint protein structure modeling provides additional signal) would strengthen the paper's narrative and make the "AF3-level performance" claim more nuanced and credible.
- **Mild metric circularity in sample ranking (Table 1):** Using PB-validity checks as part of the ranking heuristic (Row E vs Row I*) contributes ~9 percentage points to headline PB-valid Top-1 (70.8% → 79.9%) while RMSD<2 actually decreases (82.1% → 80.5%). Since PB-validity is the primary evaluation metric, there is alignment between ranking criterion and evaluation criterion. The paper is transparent about this in the ablations, and the core claim (70.8% without PB scoring) remains far ahead of all baselines, so this does not undermine the contribution.

### Trivial
- **No absolute wall-clock inference times:** The paper claims "50× faster sampling than AF3" (line 194) but provides no absolute numbers (seconds per complex, GPU requirements) in the main text. For a paper emphasizing practical feasibility for HTVS, even rough numbers would strengthen this key claim.

## Nice-to-Haves
- Discuss the AF3 bucket-level asymmetry explicitly in Section 3.2 with hypotheses about why AF3 outperforms on truly unseen proteins.
- Include wall-clock inference times alongside the 50× claim.
- A direct comparison with a torsional model using the same EquiformerV2 backbone would isolate the fragment representation contribution from architecture/engineering improvements.
- Ligand-property-stratified failure analysis (e.g., by molecular weight, flexibility, number of fragments) would deepen understanding of failure modes.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic raised a concern about "unfair comparison" in Figure 4 mixing Holo Specified and Pocket Specified conditions. Upon verification, the paper explicitly distinguishes these conditions (lines 198-221), and SIGMADOCK uses the harder Pocket Specified setting, making its results stronger, not weaker. The asymmetry favors SIGMADOCK rather than the baselines, so this is not a valid criticism.
- The harsh critic's suggestion for "more torsional baselines" is a nice-to-have, not a weakness — the paper already compares against DiffDock (a torsional model) and the ablation on fragmentation merging provides relevant evidence.

## Novel Insights
The theoretical analysis of torsional vs. fragment diffusion (Theorem 1) provides genuinely novel insight beyond the specific method: it explains from first principles why torsional models underperform in molecular docking by demonstrating that the mapping from torsional angles to Cartesian coordinates induces highly entangled non-product measures. This is a contribution to the community's understanding of geometric representations in molecular generative models, independent of the specific SIGMADOCK architecture. The FR3D irreducible fragmentation scheme and its soft triangulation conditioning are also novel technical contributions with broader applicability.

## Suggestions
- Add a brief discussion of the AF3 bucket-level asymmetry in Section 3.2, hypothesizing why AF3 outperforms on truly novel proteins.
- Include absolute wall-clock times per complex (even as a range) alongside the 50× speedup claim.
- Consider adding a torsional baseline with the same backbone architecture in the appendix to isolate fragment representation contributions.

## Calibration Anchors Retrieved

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| PsiDiff (Ligand Conformation) | m9zWBn1Y2j | 3.0 | 1 | Weak — incremental conformer generation, no theoretical grounding |
| DynamicsDiffusion | kKXIYUi8ff | 3.0 | 1 | Weak — MD trajectory generation, no docking |
| CompassDock | nWO75tVjfp | 3.0 | 1 | Weak — dataset analysis tool, not a docking method |
| TorSeq | G536mmC2HL | 3.0 | 1 | Weak — torsion-based conformer gen, less novel than FR3D |
| DiffDock-Pocket | 1IaoWBqB6K | 5.0 | 1 | Weaker — extends DiffDock with pocket conditioning; incremental compared to SIGMADOCK's fundamental approach |
| VFDiff | 5YLsnsjgeC | 6.0 | 1 | Middle — SE(3) equivariant diffusion for SBDD; weaker empirical results |
| EQGAT-diff | kzGuiRXZrQ | 5.75 | 1 | Middle — design space exploration; less application-focused |
| IPDiff | qH9nrMNTIW | 6.25 | 1 | Middle — interaction prior for SBDD; more incremental contribution |
| Lift Your Molecules | uNomADvF3s | 6.5 | 1 | Middle — latent space molecular generation; different problem |
| FoldFlow | kJFIH23hXb | 8.0 | 1 & 2 | Comparable — strong SE(3) flow matching for proteins; SIGMADOCK has more dramatic empirical gains |
| GeoBFN | NSVtmmzeRB | 8.0 | 2 | Comparable — unified molecular generation with BFN; comparable novelty and strength |
| ProtComposer | 0ctvBgKFgc | 8.0 | 2 | Comparable — compositional protein generation; different domain |
| Discrete Walk-Jump | zMPHKOmQNb | 8.0 | 2 | Comparable — protein discovery with discrete sampling; different approach |

**Round 1 bracket**: 7.0–8.5 (clearly above middle-bracket papers at 5.0–6.5, competitive with strong bracket at 8.0).
**Round 2 narrowing**: Compared directly to FoldFlow (8.0) and GeoBFN (8.0), SIGMADOCK has more dramatic empirical improvements over prior work and a more practically impactful contribution. Weaknesses are minor. Final score: 8.0.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>