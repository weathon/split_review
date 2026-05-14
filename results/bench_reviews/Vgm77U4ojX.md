Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

SIGMADOCK introduces a fragment-based SE(3) Riemannian diffusion model for molecular docking that decomposes ligands into rigid-body fragments, diffuses them independently in SE(3), and reassembles them via a learned score model. The key innovations are: (i) a formal geometric argument (Theorem 1) showing why torsional-space diffusion creates entangled, non-product measures while fragment-space diffusion yields a clean product of Haar measures; (ii) FR3D, a fragmentation-reduction algorithm that merges fragments to reduce degrees of freedom; (iii) soft triangulation conditioning that enforces bond-length/angle constraints without restricting dihedrals; and (iv) an SO(3)-equivariant architecture with proven invariance to local coordinate choices (Theorem 2). On PoseBusters, SIGMADOCK achieves 79.9% Top-1 success (RMSD < 2Å & PB-valid), a ~6× improvement over prior deep-learning methods trained on the same data split, and 90.6% on Astex. The method reaches AF3-level performance with 19K training examples, no trained confidence model, and no energy minimisation.

## Strengths

- **Principled geometric insight (Theorem 1):** The formal demonstration that torsional models produce highly entangled, non-product induced measures provides genuine motivation for the fragment-space approach. This is not merely a design choice but a theoretically grounded shift in how the diffusion process is structured, backed by the dramatic empirical gap between SIGMADOCK (79.9%) and torsional baselines such as DiffDock (12.7–32.8%) on the same data split (Figure 4).

- **State-of-the-art re-docking results with strong chemical plausibility:** SIGMADOCK achieves 79.9% Top-1 (RMSD < 2Å & PB-valid) on PoseBusters and 90.6% Top-1 on Astex, substantially outperforming classical dockers (Vina at ~56%) and all prior deep-learning methods trained under comparable conditions. The large margin over prior generative methods is convincing.

- **Well-designed inductive biases with validated contributions:** FR3D and triangulation conditioning are non-trivial components. Table 1 (Configs A and C) shows that removing triangulation conditioning drops PB-validity by 12.8 percentage points and removing fragment merging drops it by 6.2 percentage points, confirming both are essential. The stratification by co-factor presence (Table 2) shows that on complexes without co-factors, PB-validity reaches 83.0%, providing evidence against memorisation and supporting the method's robustness.

- **Rigorous treatment of local coordinate invariance (Theorem 2):** The proof that the architecture and prediction head are invariant to the choice of local fragment coordinate axes addresses a genuine ambiguity in fragment-based parametrisation that many similar methods neglect.

- **Candid limitations section:** Appendix J openly discusses training data size, dependence on a known pocket centre, chirality issues, and restriction to re-docking. This transparency strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

None. The core methodological contributions are sound, and the empirical results convincingly support the claims.

### Minor

- **Framing around classical scoring overstates self-sufficiency.** The paper repeatedly claims SIGMADOCK "does not require" a trained confidence model or energy minimisation (lines 486–489, 541). This is factually correct — the method does not train a separate confidence network and does not run force-field minimisation that alters coordinates. However, the final Top-1 result depends on ranking up to 40 seeds using Vinardo binding energies combined with PB checks (Appendix F.2). Table 1 shows that removing energy scoring drops Top-1 PB-validity from 79.9% to 66.1% (Config D), a 13.8-point gap. The paper is transparent about this in the ablation, and using a cheap energy heuristic is perfectly reasonable, but the headline narrative (e.g., "first deep learning approach to surpass classical physics-based docking," line 22–23) should acknowledge that a classical scoring function participates in pose selection. This is a framing precision issue, not a methodological flaw.

- **The AlphaFold3 comparison has unaddressed confounds, which the paper partially acknowledges but whose framing overreaches.** The paper states it achieves "AF3-level performance" (line 102, 541). The per-sequence-similarity comparison in Table 4 is informative and shows SIGMADOCK performs comparably or better on higher-similarity splits, while AF3 does better on the low-similarity split (72% vs. 87%). The paper acknowledges in Appendix J.2 that AF3 has higher train-test leakage and is solving a harder co-folding task. However, the comparison does not control for number of AF3 samples used, whether AF3's numbers include recycling, or the fact that AF3 models cofactors and flexible proteins. The narrative of "surpassing" or "matching" AF3 is oversold relative to the evidence; the more accurate claim — that SIGMADOCK achieves competitive performance with far less data and compute — is already strong enough and would benefit from more measured language in the abstract and introduction.

### Trivial

- The ablation removes fragment merging entirely (Config C) rather than comparing against a naive (k+1)-fragment baseline that retains triangulation conditioning. Such a contrast would better isolate the benefit of FR3D's fragment reduction from the benefit of triangulation conditioning itself. This is a missed experimental nuance, not a threat to the conclusions.

## Nice-to-Haves

- A direct comparison against naive (k+1) fragmentation while retaining triangulation conditioning would cleanly separate the contribution of FR3D's fragment reduction from the triangulation conditioning.
- Reporting the Top-1 rate when simply taking the first seed without any scoring would quantify the generator's standalone quality and contextualise the scoring heuristic's contribution.
- Sensitivity analysis to RDKit ETKDGv3 conformer quality — e.g., how often poor reference conformers degrade docking success — would strengthen the practical deployment story.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "the contribution is not a pure deep-learning method" and the headline claim needs qualifying as a hybrid pipeline**: Partially addressed. The paper is transparent about Vinardo scoring in the ablation and Appendix F.2. The more nuanced version of this concern is retained as a minor weakness above (framing precision). The harsh critic's formulation that the paper "overstates self-sufficiency" was softened — the paper is careful to say "no separately trained confidence model" and "no energy minimisation," both of which are true.

- **Harsh critic's claim about "undefined evaluation protocols" for AF3**: The paper does acknowledge these issues in Appendix J.2. The AF3 comparison is presented as supplementary evidence. Retained as a minor weakness about narrative overreach, not a fatal confound.

- **Strength Finder claim that "the model does not require post-hoc energy minimisation or a trained confidence filter, relying only on a simple scoring heuristic"**: This is accurate per the paper's text. The strength is retained but qualified by the minor weakness about framing.

- **Harsh critic's demand for sensitivity to RDKit conformer quality**: This is a reasonable suggestion but moved to Nice-to-Haves — it would strengthen the paper but is not a weakness per se; the paper already acknowledges dependence on a classical conformer generator.

- **Strength Finder's "does not require post-hoc energy minimisation or a trained confidence filter" as a standalone strength**: This is retained as part of the main strengths but contextualised by the minor weakness about scoring dependence.

## Novel Insights

The reviewers' synthesis highlights an important tension in deep-learning docking: principled inductive biases (fragment-space diffusion, triangulation conditioning) dramatically close the gap to classical methods, but the final mile of performance still benefits from classical energy evaluation. This pattern — where deep learning handles the hard combinatorial/geometric problem while a simple physics-based filter selects among candidates — may represent a productive division of labour rather than a weakness. The paper's theoretical framing (Theorem 1) provides a useful language for understanding why fragment-space diffusion is fundamentally better-conditioned than torsional diffusion, an insight that could inform future work on molecular generation beyond docking.

## Suggestions

- Revise the abstract and introduction to more precisely describe the scoring heuristic: "SIGMADOCK does not require a separately trained confidence model or coordinate-altering energy minimisation; a lightweight energy-based ranking selects among sampled poses." This maintains the honest advantage (no trained confidence model, no coordinate alteration) while being precise about the classical component.
- Tone down the AF3 comparison language from "AF3-level performance" / "surpass" to "competitive with AF3 on re-docking despite using ~25× less training data and no co-folding machinery." The per-bucket Table 4 is convincing enough without overclaiming.
- Add the naive (k+1) fragmentation + triangulation conditioning ablation or explain why it was omitted.

## Score and Decision

### Anchor Comparison

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| PoseX | qqzxKudD4T | 5.00 | A benchmark paper; SIGMADOCK has substantially more methodological novelty and stronger single-system results. |
| Physically Valid... (Gauss-Seidel) | sJABnBEYeh | 5.50 | Novel projection method but with mixed baseline comparisons; SIGMADOCK's theoretical contribution and empirical gains are more dramatic. |
| Pallatom-Ligand | uMD75SDTTA | 6.00 | All-atom diffusion for protein design; solid but with architecture novelty concerns. SIGMADOCK's results are more striking relative to baselines in its domain. |
| Enhancing Diffusion... (WT-ASBS) | 1bJN1EQByS | 6.50 | Novel integration of enhanced sampling with diffusion; strong but with some methodological concerns. SIGMADOCK has comparable novelty with more dramatic empirical gains. |
| Quotient-Space Diffusion | 3JPAkwSVc4 | 7.50 | Strong theoretical framework for diffusion on quotient spaces; elegant and general. SIGMADOCK is domain-specific but comparably principled, with more dramatic domain results. |
| La-Proteina | RDerF20JYT | 8.00 | Strong protein generation method with flow matching. SIGMADOCK is less architecturally novel but more theoretically grounded in its domain. |

SIGMADOCK sits between the 6.50 and 7.50 anchors: its theoretical contributions (Theorems 1 and 2) are strong but more domain-specific than the quotient-space diffusion framework, while its empirical results in docking are more transformative relative to prior work. The minor framing weaknesses around classical scoring and AF3 comparison prevent it from reaching the 7.50–8.00 band, but the core methodological contribution and empirical gains are clearly above the 5.00–6.00 tier.

**Evaluation axes:** Originality is high — the fragment-space diffusion formulation and FR3D are genuinely novel contributions to the docking literature. The research question (making deep-learning docking reliable) is important and timely. Claims are well-supported by thorough ablations and multiple benchmark evaluations. Experiments are sound with appropriate controls. Writing is clear and well-structured. Value to the community is substantial — the method sets a new state of the art on a widely-used benchmark, and the theoretical framework provides useful language for future work.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>