Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces SIGMADOCK, a fragment-based SE(3) diffusion model for molecular re-docking. The key idea is to decompose ligands into rigid-body fragments by breaking rotatable bonds, then define a diffusion process over the SE(3) poses of these fragments rather than over torsional angles. This is motivated by Theorem 1, which shows that disjoint rigid fragments yield a factorised product of Haar measures, avoiding the entangled non-product measures induced by torsional models. The method also introduces FR3D (fragmentation reduction to reduce degrees of freedom), soft triangulation constraints to preserve bond geometry, and an EquiformerV2-based equivariant architecture. Empirically, SIGMADOCK achieves 79.9% Top-1 PB-valid on PoseBusters and 90.6% on Astex, substantially outperforming prior deep-learning methods and reaching AF3-level performance with much less data.

## Strengths

1. **Well-motivated and theoretically grounded methodological contribution.** The core idea—diffusing over SE(3) poses of rigid fragments rather than torsional angles—is clearly motivated. Theorem 1 formally proves that fragments yield factorised product measures while torsional models induce entangled non-product measures, providing a principled reason to expect better-conditioned learning dynamics. Lemma 1 and Theorem 2 provide additional theoretical grounding for the triangulation constraints and equivariance properties.

2. **State-of-the-art re-docking accuracy with strong ablation support.** SIGMADOCK achieves 79.9% Top-1 PB-valid on PoseBusters and 90.6% on Astex, compared to DiffDock's 38.0% (RMSD-only) and G2G/Vibe2 at 58.1%. Table 1 provides clean ablations quantifying the contributions of triangulation conditioning (−12.8%), protein-ligand interactions (−3.6%), fragmentation merging (−6.2%), and the scoring heuristic (−13.8% without energy scoring, −9.1% without PB scoring). These ablations tie directly to specific design choices.

3. **Data efficiency and inference speed compared to AlphaFold3.** Table 4 shows SIGMADOCK achieves 79.9% PB-Val vs AF3's 80.2% while training on only 19k PDBBind complexes (vs AF3's large-scale training), with 50× faster sampling. This combination of competitive accuracy with orders-of-magnitude lower resource requirements is a practically significant result.

4. **Principled handling of chemical plausibility.** The method does not require post-hoc minimisation or a separately trained confidence model. The ranking heuristic uses pseudo-binding energy and physicochemical checks, and Table 1 shows that removing both still yields 66.1% PB-Val (Config D), indicating the generative model itself produces reasonable poses.

5. **Co-factor failure analysis supports that the model learns genuine physics.** Table 2 shows higher failure rates on complexes with natural ligands (41.2%) and ions (23.6%) compared to no co-factors (16.2%), which is consistent with the model being trained without co-factor information. This is a thoughtful sanity check.

## Weaknesses

### Fatal
None.

### Major

1. **Metric ambiguity in the main results table (Figure 4 left) makes core comparisons hard to evaluate.** The table header is "Top-1 (%)" without specifying whether each number is RMSD-only, PB-valid, or both. SIGMADOCK's 79.9% is PB-valid (as stated in the abstract and confirmed in Table 1). But DiffDock's 38.0%—which the text on line 196 compares to via "6.3× higher PB-validity"—is almost certainly RMSD-only (matching Butenschön et al.'s reported RMSD-only number for DiffDock; their PB-valid figure for DiffDock is ~12.7%). The table also lists "PDBBind" at 15.9% with a footnote marking it as classical docking, but the metric for this entry is unclear. Because the paper's headline claims rely on exceeding classical docking and achieving 6.3× improvement over DiffDock, the table must report both RMSD-only and PB-valid for every method, or clearly label which metric each column represents. As written, a reader cannot verify that like is compared with like.

2. **Unexplained discrepancy between Figure 4 (right panel) and Table 4 on sequence-similarity breakdowns.** Figure 4 right reports Top-1 of 51% (≤0% similarity), 53% (30–95%), and 53% (95–100%) across the same 308 PB complexes. Table 4 reports PB-Val of 72% ([0,30)), 79% ([30,95)), and 87% ([95,100]) on what appear to be the same complexes (identical counts: 109, 76, 123). The paper does not explain why these numbers differ by 20–34 percentage points for similar splits. The weighted average of the Figure 4 right numbers (~52%) also does not match any shown overall Top-1 figure (80.5% RMSD-only or 79.9% PB-Val from Table 1), making it unclear what metric the right panel reflects. This needs clarification.

### Minor

3. **The classical docking baseline ("PDBBind" at 15.9%) is confusingly labeled.** The training dataset is also PDBBind, so a reader unfamiliar with the benchmark literature may not realise this row represents a classical docking method (the only indication is a footnote asterisk). Moreover, which specific classical docking tool this corresponds to (Vina, Glide, or a consensus) is not stated. Given the central claim of being the first DL method to surpass classical docking, this baseline should be named and described more transparently.

4. **Several architectural contributions are not independently ablated.** The paper claims virtual nodes and smooth message decay help mitigate over-squashing and instabilities, but these are not tested in the ablation study (Table 1). The backbone is a modified EquiformerV2, and it is unclear whether the improvements come from the architecture changes or from the fragment-based diffusion formulation itself.

5. **The FR3D "stochastic search" merging algorithm is described only at a high level in the main text (Section 2.2.3).** The paper states it performs a "stochastic search" and "branch[es] through candidate neighbour proposing merge actions" without specifying the merging criteria, acceptance rule, or termination condition. While the appendix is referenced, the main text lacks enough detail for a reader to understand or assess the algorithm.

### Trivial
- Table 2 (co-factor analysis) reports percentages for subsets as small as 17 complexes without confidence intervals; this should be noted as a caveat.
- The "Fail. Rate" column in Table 2 is defined only in a footnote, which could be moved to the caption for clarity.

## Nice-to-Haves

- Include a direct comparison to a specific classical docking tool (e.g., AutoDock Vina or Glide) on the same PB split with the same PB-valid metric, rather than relying on the opaque "PDBBind" baseline label.
- Report run-to-run variance (e.g., across model seeds or fragmentations) for the main results.
- Add a computational cost comparison to other DL docking methods (e.g., DiffDock's inference time) to contextualise the practical advantage.
- Show what DiffDock (and other baselines) would achieve if the same energy+PB scoring heuristic were applied to their samples, to isolate the contribution of the generative model.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Classical docking claim is not supported because Figure 4 contains no classical docking numbers."** — Removed because it is factually incorrect. The row "PDBBind" at 15.9% is explicitly marked with (*) denoting classical docking (line 225). The comparison is present, albeit poorly labeled.
- **"FR3D mechanism is too vague for reproducibility."** — Removed because the paper references Appendix D.4 and Algorithm 1 for full details. The appendix is stripped by the PDF parser, so this is a parser artifact, not an author omission.
- **"AF3 comparison is apples-to-oranges."** — Partially true, but the paper explicitly acknowledges the task mismatch ("Although we cannot directly compare SIGMADOCK to co-folding methods", line 260) and presents Table 4 as a contextual comparison, not a headline claim. The comparison is appropriately caveated.
- **"The 12.7–32.8% range in the abstract lacks a source."** — The abstract does not cite a specific source, but this range is consistent with Butenschön et al. (2024) cited earlier in the introduction. This is a minor citation formatting choice, not a substantive weakness.
- **"Input conditions for baselines are not clearly specified."** — The paper states the re-docking protocol explicitly (line 28) and the split ("Holo Specified" vs "Pocket Specified") is a reasonable categorisation of how these methods are commonly used. Some ambiguity exists but it is not a serious flaw.

## Novel Insights

The reviews surface a tension that the paper itself does not fully grapple with: the claim of "surpassing classical physics-based docking" relies on a single, opaque baseline entry ("PDBBind" at 15.9%) whose identity and metric are unclear, while the claim of "6.3× improvement over DiffDock" compares PB-valid (79.9%) to DiffDock's PB-valid (~12.7%) but the main table shows DiffDock at 38.0% (RMSD-only) without explaining the discrepancy. This pattern suggests the paper is presenting its strongest numbers in aggregate form while deferring the fine-grained metric distinctions that would let a sceptical reader verify the comparisons. The core method and results are genuinely strong, but the current presentation forces the reader to do substantial cross-referencing between the text, tables, and footnotes to understand what is being compared. No reviewer identified a fatal flaw in the method itself—the concerns are all about presentation, completeness, and fair comparison framing.

## Suggestions

1. In Figure 4 (left table), add separate columns or clear labels for "RMSD < 2Å" and "PB-valid" for every method. If baseline PB-valid numbers are unavailable from prior work, state this explicitly and report them via re-evaluation if possible.
2. Explain the relationship between Figure 4 (right) and Table 4. If they report different metrics or use different evaluation setups, say so clearly. If one is a superseded preliminary result, correct it.
3. Rename the "PDBBind" classical docking row to the specific tool name (e.g., "AutoDock Vina" or "Glide") and state which metric it reports.
4. Add an ablation isolating the architectural innovations (virtual nodes, smooth message decay) from the backbone EquiformerV2 to confirm their contribution.

## Score and Decision

### Round 1 — Bracketing (3 queries, score bands)

**Low band (<3.5):** Retrieved papers scored 1.50–3.00 (molecular docking/generation papers with weak results or unclear contributions). SIGMADOCK is clearly stronger than these anchors.

**Middle band (3.5–7.5):** Retrieved papers scored 4.00–7.00. Most relevant anchors:
- *PoseX* (5.00) — benchmark paper with limited methodology novelty, accepted poster. SIGMADOCK has stronger methodological contribution.
- *Pallatom-Ligand* (6.00) — all-atom diffusion for protein-ligand design, architecture similar to AF3, accepted poster. SIGMADOCK has clearer novelty (fragment-based vs all-atom) but similar presentation concerns.
- *Physically Valid Biomolecular Interaction* (5.50) — constraint enforcement module, accepted poster. SIGMADOCK is a stronger standalone contribution.

**High band (>7.5):** Retrieved papers scored 7.00–8.50. Most relevant:
- *Quotient-Space Diffusion Models* (7.50) — rigorous theoretical framework with clean experiments, accepted oral. SIGMADOCK has less theoretical depth and more presentation issues.

**Bracket:** Between 5 and 7.

### Round 2 — Narrowing (within 4.5–8.0)

Retrieved papers within (4.5, 6.5):
- *Pallatom-Ligand* (6.00) — consensus 6/6/6/6. Similar domain, similar strength of empirical results. SIGMADOCK has cleaner novelty but more presentation ambiguity. Comparable quality.
- *ProteinAE* (5.00) — solid but not exceptional methodological contribution.
- *GGND* (5.60) — 2/8/8/6/4, heterogeneous reviews.
- *FragFM* (5.00) — fragment-level molecular generation, less docking relevance.

**Upper end of bracket (6.5–8.0):**
- *Quotient-Space Diffusion* (7.50) — oral, highly rigorous. SIGMADOCK is weaker on theoretical depth and presentation clarity.
- *SYNC* (6.67) — synthesizability classifier, specific focus.
- *RegFlow* (6.67) — training method for normalizing flows.

**Calibrated comparison:** SIGMADOCK is comparable to *Pallatom-Ligand* (6.00)—both have strong empirical results and a clear methodological contribution, but both have presentation issues that prevent them from reaching the 7+ tier. SIGMADOCK's core idea (fragment-based SE(3) diffusion with theoretical motivation) is arguably more novel than Pallatom-Ligand's all-atom formulation (which closely follows AF3's architecture). However, the metric ambiguity in the main results table and the unexplained Figure 4 / Table 4 discrepancy are more serious presentation flaws than anything in the Pallatom-Ligand reviews. On balance, SIGMADOCK sits at the same level.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>