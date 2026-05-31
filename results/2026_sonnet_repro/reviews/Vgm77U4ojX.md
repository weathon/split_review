Now let me run the calibration search to score this paper.**Round 1 bracket: between 6.0 and 8.5**

Now narrowing with Round 2:Now let me read two more anchors from the 7.0–7.5 range for tighter comparison.Now I have enough information to write the full review. Let me compile the verified findings.

---

## Summary

SIGMADOCK introduces a fragment-based SE(3) Riemannian diffusion model for molecular docking. The central contribution is a novel fragmentation-and-reduction scheme (FR3D) that decomposes ligands into rigid-body fragments, a soft triangulation conditioning scheme to encode chemical geometry priors, and an SO(3)-equivariant score architecture based on EquiformerV2. This framework avoids the geometric entanglement of torsional models by operating in a product space SE(3)^m. Empirically, SIGMADOCK achieves 79.9% PB-valid Top-1 success on the PoseBusters set — the first deep-learning docking method to surpass classical physics-based docking under the intended PB train-test split.

---

## Strengths

- **Decisive state-of-the-art on PoseBusters with genuine milestone**: SIGMADOCK achieves 79.9% PB-valid Top-1 (Table 1, config I\*), compared to 58.1% for G2G/Vibe2 (best prior deep-learning results), 38.0% for DiffDock, and 15.9% for classical Vina (Figure 4, left). This is the first reported deep-learning result to surpass classical physics-based docking on the PoseBusters set under the correct train-test split — a specific, verifiable, and significant milestone.

- **Strong ablation study validates each architectural component**: Table 1 provides clean component-by-component ablations: removing triangulation conditioning (config A) costs 12.8pp in PB validity; removing fragment merging (config C) costs 6.2pp; removing protein-ligand interactions (config B) costs 3.6pp. These numbers are individually informative and jointly coherent.

- **Principled theoretical foundation**: Theorem 1 formally proves that torsional models induce entangled, non-product measures in Cartesian space while independent fragment diffusion yields a factorised product of Haar measures on SE(3)^m. Lemma 1 proves triangulation conditioning uniquely determines bond angles while leaving dihedral angles free. Theorem 2 establishes invariance of training and sampling to the arbitrary choice of fragment local coordinate axes — directly addressing a non-trivial implementation concern.

- **Generalisation to novel proteins demonstrated**: Table 4 shows 72% PB-valid Top-1 on proteins with <30% sequence similarity to training data (109 complexes), rising to 87% on the near-identical bin — demonstrating the method does not simply memorise training proteins.

- **No post-hoc energy minimisation required**: The default configuration reaches 79.9% PB-valid without minimisation (Table 1, config I\* vs. E), which the paper correctly identifies as a methodologically significant distinction from common practice.

---

## Weaknesses

### Fatal
None.

### Major

- **AF3 comparison overclaims in the abstract and introduction despite the paper's own disclaimers**: The abstract states "we reach AF3-level performance" and Section 3.2 presents this as a feature. However, Table 4 directly shows that on the scientifically most critical subset — proteins with <30% sequence similarity ([0,30) bin, 109 complexes) — SIGMADOCK achieves 72% PB-valid while AF3 achieves 87%, a 15 percentage-point deficit. Even though the main text acknowledges "we cannot directly compare SIGMADOCK to co-folding methods," the abstract and Section 1 repeat the claim that the method achieves "AF3-level performance with a fraction of the training data." On the novel-protein subset where generalisation is what actually matters for drug discovery, the comparison actually shows AF3 performing considerably better. This framing substantially overstates the result for readers who stop at the abstract or introduction.

### Minor

- **The energy scoring heuristic (config D) is the single largest ablation contributor but receives the least methodological attention**: Table 1 shows removing energy scoring (config D) drops PB-valid Top-1 from 79.9% to 66.1% — a 13.8pp reduction, larger than removing triangulation conditioning (12.8pp), fragment merging (6.2pp), or protein-ligand interactions (3.6pp). The paper introduces this component in one paragraph of Section 2.5 as "a simple and cheap heuristic" and emphasises that it avoids a separately trained confidence model. However, given that energy scoring contributes more to the final number than any single architectural design choice, the paper's framing — which centres on geometric inductive biases — is somewhat misleading about what drives the headline result. The component deserves explicit characterisation: what energy terms are used, how it compares to a learned confidence model, and whether it counts as physics-based scoring for purposes of the classical docking comparison.

- **Fragment-space vs. torsional-space advantage is theoretically argued but empirically uncontrolled**: Theorem 1 establishes the factorisation property of fragment SE(3)^m diffusion, which is correct. However, the empirical comparison that validates the fragmentation claim (DiffDock 38.0% vs. SIGMADOCK 79.9%) conflates the parameterisation change with the architecture (EquiformerV2 backbone, virtual nodes, hierarchical conditioning). The paper does not present an ablation that swaps only the parameterisation within the same architecture. The conclusion that "torsional frameworks become poorly conditioned" is supported by theory but not by controlled empirical evidence.

### Trivial
None identified.

---

## Nice-to-Haves

- **Same-architecture fragment vs. torsional ablation**: Even on a subset of the data, implementing both parameterisations within the same architecture would provide clean empirical evidence for the fragment-space advantage argued in Theorem 1. Without this, the performance gap may be attributed to architecture rather than fragmentation.
- **Energy scoring component analysis**: A breakdown of which energy terms drive the 13.8pp gain — and whether a learned confidence model can match or exceed the heuristic — would clarify the method's relationship to classical scoring and strengthen the paper's methodological claims.
- **Reporting confidence intervals**: With 308 PB complexes and 40 seeds, binomial variance on Top-1 accuracy is non-negligible (~±2–3% at 95% CI). Adding confidence intervals across training runs would allow readers to judge whether per-configuration differences in Table 1 are statistically robust.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Figure 4 (right chart) vs. Table 4 inconsistency** (harsh critic): The extracted bar-chart values (51–53% per bin) conflict with Table 4's values (72–87%). This is a PDF parsing artefact — the bar heights were misread by the extractor. Table 4 provides the authoritative numbers clearly. Per the hard rule on formatting/parsing artefacts, this criticism is removed.

- **FR3D termination criterion and "irreducible" definition missing from main text** (harsh critic): The paper explicitly defers the algorithm to Appendix D.4. Per the hard rule on stripped appendices, this criticism is removed.

- **Figure 4 left: "Pocket Specified" vs. "Holo Specified" asymmetry** (harsh critic): The paper states SIGMADOCK uses the standard re-docking protocol (holo conformation, known pocket), and Figure 4's caption notes that methods like PDBBind and DiffDock use a different input specification. The grouping in Figure 4 reflects real input-information differences, but the key claim — SIGMADOCK outperforms all methods under comparable conditions — is supported. This is a minor clarification issue, not a comparability flaw; removed as a standalone weakness.

- **G2G and Vibe2 characterisation missing** (harsh critic): Requesting characterisation of baselines in the main text. No external source available to confirm what is already in the paper/appendix; per hard rule, removed.

- **Reproducibility/confidence intervals as a weakness** (harsh critic): Requesting standard error reporting across training runs. This is a nice-to-have and not standard in single-model docking evaluation. Demoted to Nice-to-Haves.

- **Strength: "data efficiency matching AF3-level performance"** (strength finder): This is weakened by Table 4's direct comparison showing SIGMADOCK 15pp behind AF3 on novel proteins. Removed as a clean strength; the underlying data efficiency observation is partially valid but the framing is overclaiming.

---

## Novel Insights

The most genuinely novel insight surfaced by this synthesis is the relationship between the energy scoring heuristic and the paper's central claims. SIGMADOCK's headline result of 79.9% PB-valid is jointly the product of its diffusion architecture and a physics-based scoring heuristic that contributes more to performance than any single architectural component. This creates an interesting tension: the paper frames its advance as replacing physics-based assumptions with geometric inductive biases, yet the single largest performance contributor is a physics-based binding energy heuristic. Understanding whether the geometry (fragment diffusion, triangulation conditioning) and the physics (energy ranking) contribute independently or synergistically — and whether the heuristic could be replaced by a learned confidence head without loss — is an actionable question that future work on learned vs. analytical scoring in diffusion-based docking should address.

---

## Suggestions

1. Rewrite the abstract and Section 3.2's opening to say "competitive with AF3 on the overall PB set, while substantially behind on novel proteins ([0,30) sequence similarity bin: 72% vs. 87%)" — this accurately scopes the comparison and avoids the overclaiming that the AF3 comparison currently introduces.
2. Elevate energy scoring (ablation config D) to a first-class section or subsection: describe which energy terms are evaluated, whether it constitutes a form of physics-based scoring, and compare to a learned confidence model baseline (even a shallow one trained on the diffusion embeddings).
3. In Table 1's summary discussion, note that ablation G (oracle conformers: 85.4% vs. 79.9%) provides an actionable upper bound for the conformer-sampling contribution, pointing to binding-aware conformer generation as the clearest path to further improvement.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to SIGMADOCK |
|------|-----------|-------|------------------------|
| m9zWBn1Y2j (PsiDiff) | 3.0 | R1-weak | Much weaker — incremental conditional diffusion, no significant benchmark advance |
| kKXIYUi8ff (DynamicsDiffusion) | 3.0 | R1-weak | Orthogonal task, weaker methodology |
| nWO75tVjfp (CompassDock) | 3.0 | R1-weak | Assessment framework, not a generative method |
| An87ZnPbkT (GNNAS-Dock) | 3.0 | R1-weak | Algorithm selection, no novel generative contribution |
| 1IaoWBqB6K (DiffDock-Pocket) | 5.0 | R1-mid | Related but notably weaker results; SIGMADOCK's improvement is much larger |
| FuXtwQs7pj (Toric varieties diffusion) | 4.5 | R1-mid | Different task (loop modelling), smaller contribution |
| S4zpk61r6G (DiffMaSIF) | 4.67 | R1-mid | Protein-protein docking, smaller benchmark improvement |
| qH9nrMNTIW (IPDiff) | 6.25 | R1-mid | SBDD, accepted; SIGMADOCK has stronger results and cleaner contribution |
| kJFIH23hXb (FoldFlow SE(3)) | 8.0 | R1-strong | Protein backbone generation, broader scope; SIGMADOCK is more specialised |
| zMPHKOmQNb (Discrete Walk-Jump) | 8.0 | R1-strong | Antibody protein discovery, broader contribution |
| uKZdlihDDn (Diffusion Graph Networks) | 7.6 | R1-strong | Fluid simulation, different domain |
| NSVtmmzeRB (GeoBFN) | 8.0 | R1-strong | Unified 3D molecular generation across tasks; SIGMADOCK more specialised |
| kzGuiRXZrQ (EQGAT-diff) | 5.75 | R2-narrow | Equivariant diffusion for general molecule generation; weaker benchmark advance |
| 5YLsnsjgeC (VFDiff) | 6.0 | R2-narrow | SE(3) SBDD with energy guidance; SIGMADOCK's results much stronger, better theoretical grounding |
| uNomADvF3s (Lift Your Molecules) | 6.5 | R2-narrow | Latent-space molecular generation; solid but less decisive results |
| mXHTifc1Fn (E(3) chirality) | 6.75 | R2-narrow | Strong theoretical contribution; comparable originality but different direction |
| 5FXKgOxmb2 (MAGNet) | 7.25 | R2-narrow | Fragment-based molecule generation; scores 8,8,8,5; comparable in novelty and execution |
| g3VCIM94ke (DrugFlow) | 6.67 | R2-narrow | Structure-based drug design; good multi-component paper, weaker than SIGMADOCK's decisive result |

**Round 1 bracket**: 6.0–8.5. The paper is clearly above the mid-band (5.0–6.25) molecular docking/diffusion papers and probably below the most general, broadly applicable frameworks scoring 8.0.

**Round 2 narrowing**: The most comparable anchors are MAGNet (7.25) — fragment-based molecular paper with milestone-level contribution and 8,8,8,5 reviewer distribution — and DrugFlow (6.67) — structure-based drug design with multiple methodological components. SIGMADOCK is clearly above DrugFlow: its benchmark improvement is more decisive, its theoretical grounding stronger, and its milestone (first DL to beat classical docking) more concrete. Versus MAGNet, SIGMADOCK has a comparably decisive contribution (first of a kind in docking), strong ablations, and solid theory, but is held slightly back by the AF3 comparison framing and the underplayed energy scoring contribution. 

**Final score: 7.0**, positioned just below MAGNet (7.25) due to the concrete framing issues identified above. The core contribution is genuine and significant; the weaknesses are real but addressable in revision and do not invalidate the paper's claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>