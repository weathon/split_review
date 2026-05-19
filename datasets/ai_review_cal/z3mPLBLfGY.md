- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6
I have now thoroughly read the paper and verified the reviewer claims directly against the text. Let me now synthesize the final review.

---

## Summary
This paper proposes a **unified bilevel representation** for 3D molecular complexes—a "geometric graph of sets" where each node is a block (residue, nucleobase, etc.) containing a variable-sized set of atoms with matrix-form features and coordinates—and introduces a **Generalist Equivariant Transformer (GET)** designed to process it. GET comprises a bilevel attention module (computing both atom-level cross attention and block-level attention), an equivariant feed-forward network, and an equivariant layer normalization, all E(3)-equivariant and permutation-invariant within blocks. The method is evaluated on protein-ligand (PDBbind), protein-protein (PPA), ligand-binding (LBA), mixed-domain, and zero-shot RNA/DNA-ligand tasks, consistently outperforming a wide range of baselines.

---

## Strengths

1. **Principled unified "geometric graph of sets" representation.** The paper identifies a genuine gap: different molecule types (proteins, small molecules, RNA/DNA) use different granularities, preventing a single model from learning shared interaction physics. The bilevel representation preserves both block-level hierarchy (residue/nucleobase identity) and atom-level detail, going beyond pooling-based hierarchical models that discard fine-grained information (Section 3.1, Fig. 1). This is a conceptually clean and original formulation.

2. **Bilevel attention with E(3) equivariance for variable-sized sets.** The model computes atom-level cross attention (Eqs. 3–4), aggregates to a block-level relation vector (Eqs. 5–6), then uses block-level attention as a gating factor for atomic updates (Eqs. 7–8). This design simultaneously captures sparse block-level and dense atom-level interactions while handling blocks of variable sizes. The equivariant layer normalization (Eqs. 18–21) is a novel technical contribution.

3. **Consistent SOTA across multiple benchmarks.** GET achieves RMSE 1.364, Pearson 0.596 on PDBbind (Table 1), outperforming all 13 baselines including domain-specific two-branch models. In the structured comparison across three representation types (Table 2), GET outperforms all 24 baseline configurations (8 models × block/atom/hierarchical) on PPA and is top-two on LBA. This is strong, consistent evidence.

4. **Demonstrated cross-domain and zero-shot generalization.** In mixed-domain training (Table 3), GET improves on both PPA and LBA while all baselines (ET, MACE, LEFTNet) degrade on at least one domain. On zero-shot RNA/DNA-ligand affinity (Table 4), GET achieves Pearson 0.450 vs. best baseline 0.279. These results directly support the claim that the unified representation + GET captures transferable interaction physics.

5. **Thorough ablation and robustness analysis.** Table 6 ablates each component (LN, equivariant coordinate normalization, embedding of scale, FFN), showing each contributes meaningfully. Table 5 shows GET maintains Pearson > 0.610 up to 3.0 Å coordinate noise, demonstrating practical robustness to predicted structures.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Computational cost is not reported.** The paper describes a complex bilevel attention mechanism (atom-level cross attention between all atom pairs of neighboring blocks) and notes that several baselines (DimeNet++, GemNet, Equiformer) run OOM on atom-level representations (Table 2). Yet no runtime, memory usage, or parameter counts are reported for GET. This makes it difficult to assess practical deployability, especially for large complexes. Reporting these metrics (training/inference time, parameter count, GPU memory) for GET and key baselines would significantly strengthen the paper.

2. **Zero-shot result rests on a small test set.** The RNA/DNA-ligand test set has 149 complexes (Table 4). The reported gains are large (Pearson 0.450 vs. 0.279), and standard deviations over three runs are given, but the limited sample size means confidence intervals around the point estimates are wide. Bootstrapped confidence intervals would provide a more reliable characterization. The omission of RMSE from Table 4 (apparently stripped by the parser) is a minor presentation issue.

3. **The representation vs. architecture attribution is not fully isolated.** The paper compares GET (with unified representation) against baselines on block-level, atom-level, and hierarchical representations. This is extensive but conflates representation with architecture: GET is a more expressive model. The paper states that existing models "cannot directly process" matrix-form features (Section 3.1), which is true, and the comparison against 24 baselines convincingly shows GET+unified outperforms all alternatives. However, a control experiment—adapting GET to collapsed representations (e.g., each block as one atom, or pooling atoms within a block to one feature vector)—would cleanly separate how much of the gain comes from the unified representation vs. the GET architecture itself. The paper's claims would be strengthened by adding such an ablation.

### Trivial

- The abstract and introduction use the term "permutation-invariant" to describe the model's behavior within blocks. The model is technically *permutation-equivariant* (output atoms permute correspondingly with input ordering), though the intended meaning is clear. A minor wording correction.
- The kNN graph construction uses minimum inter-block atom-pair distance (Eq. 1). An ablation on alternative edge-construction strategies (e.g., centroid distance) would be informative but is not necessary.

---

## Nice-to-Haves
- Add a variant of GET with only block-level attention (pooling atom features before attention) to quantify the benefit of fine-grained atom-level interactions.
- Provide bootstrapped confidence intervals for the zero-shot test set.
- Ablate alternative aggregation strategies (max-pooling vs. mean-pooling) for the block-level relation vector r_ij in Eq. 5.
- Report parameter counts and training/inference time for GET and key baselines.

---

## Removed Points

These points from the input reviews were removed or downgraded with justification:

1. **"Mixed-domain training confound: improvement could be from more data, not cross-domain transfer."** — Removed. The baselines also receive the same mixed data ("-mix" variants) and generally degrade; GET improves. The experiment explicitly controls for data quantity. The critic's suggested control (more same-domain data) would test a different question and is not a flaw in the existing comparison.

2. **"Unfair comparison: the paper should compare to Voxel-based 3D CNNs or PointNet++ on atom sets."** — Removed. The paper already compares against 8 backbone models under 3 representation types (24 configurations). This is already one of the most comprehensive comparisons in the literature. The reviewer's suggestion is scope expansion, not a genuine omission.

3. **"Code and data splits are not mentioned / reproducibility concern."** — Removed per hard rule: reproducibility nitpicks about large artifacts impractical to include. The paper follows established splits from PDBbind and Atom3D, which is standard practice.

4. **"The kNN graph construction based on min atom-pair distance could create spurious edges."** — Demoted to Nice-to-Have. This is a reasonable design consideration but entirely speculative; no evidence is presented that this causes problems, and the model performs well despite any potential spurious edges.

5. **Pure formatting/style nitpicks and speculations about appendix contents.** — Removed per hard rules.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews did not surface any genuinely novel observation about the paper that the paper itself does not already articulate.

---

## Suggestions

1. **Report computational cost.** Add a table with parameter counts, training time per epoch, inference time per complex, and peak GPU memory for GET and 2–3 key baselines (e.g., ET, LEFTNet). This directly addresses a practical concern and helps justify the model's complexity.
2. **Add a control: GET on collapsed representations.** Create a variant where each block contains exactly one atom (atom-level) or where each block's atoms are pooled to a single feature vector (block-level), and compare to the full GET. Even if the collapsed variants underperform, reporting this result cleanly separates representation gains from architectural expressivity.
3. **Provide bootstrapped confidence intervals for the zero-shot results** (Table 4) to characterize uncertainty given the small test set (n=149). Also report RMSE values if they exist in the original submission.
4. **Minor language fix:** Correct "permutation-invariant" to "permutation-equivariant" in descriptions of how the model handles atom ordering within blocks.

---
