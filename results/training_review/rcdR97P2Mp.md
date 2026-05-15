Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces higher-order invariants $\operatorname{PDD}^{\{h\}}$ (and their moment-based variants $\operatorname{PDM}^{\{h\}}[l]$) for periodic point sets, extending the first-order Pointwise Distance Distribution (PDD). The invariants are shown to be $\operatorname{E}(n)$-invariant, Lipschitz continuous with constant $\lambda=2$, and able to distinguish all known homometric counter-examples that fooled earlier descriptors (PDD, diffraction patterns). Using a hierarchical pipeline (ADA → PDA → $\operatorname{PDD}^{\{h\}}$), the paper detects over 100,000 near-duplicate crystals across the five largest public databases (CSD, COD, ICSD, MP, GNoME) in under 8.5 hours on a desktop computer—orders of magnitude faster than traditional alignment-based methods. The paper also proves that the Pointwise Shift Distribution (PSD) solves Problem 1.2 completely for $n=1$, a result that had remained open.

## Strengths

- **Novel higher-order invariants with strong theoretical grounding.** $\operatorname{PDD}^{\{h\}}$ is a principled extension of PDD that captures higher-order spatial information through averaged perimeters of $h$-point simplices. The invariants are proven Lipschitz continuous (Theorem 4.1), avoiding the discontinuity issues that plague cell-based or cut-off-based descriptors. The factor $\frac{2}{h(h+1)}$ is explicitly chosen to guarantee the Lipschitz constant $\lambda=2$.

- **Complete solution for the 1D case.** Theorem 4.3 proves that the Pointwise Shift Distribution (PSD) solves Problem 1.2 (invariance, completeness, metric axioms, Lipschitz continuity, reconstructability, polynomial-time computability) for all periodic sequences in $\mathbb{R}^1$, a problem that had remained open in prior work. This is a clean theoretical result.

- **Demonstrated resolution of known homometric counter-examples.** Examples 3.3 and 3.6 show that $\operatorname{PDD}^{\{2\}}$ distinguishes the infinite families of homometric sets (1D, 2D, and Pauling's 3D crystals) that produce false negatives for PDD and diffraction patterns. Fig. 4 (right) plots continuously varying EMD for Pauling's $P(\pm u)$ family, and Fig. 5 shows analogous behavior for the 2D homometric sets—multiple concrete verifications across dimensions.

- **Practical hierarchical pipeline with dramatic speedup.** The ADA → PDA → $\operatorname{PDD}^{\{h\}}$ pipeline is well-designed, using fast $\ell_\infty$ nearest-neighbor search (ADA via kd-trees) as a first filter, then EMD on PDA, and finally $\operatorname{PDD}^{\{2\}}$ for confirmation. Table 3 reports 8.5 hours total on a desktop for all-vs-all comparisons across 5 databases, versus extrapolated years for COMPACK (Table 4). This is a genuine practical advance—the running times are independently valuable regardless of the exact duplicate counts.

- **Clear problem formalization.** Problem 1.2 provides six precise desiderata (invariance, completeness, metric axioms, Lipschitz continuity, reconstructability, polynomially-time computability) that set a rigorous benchmark for crystal descriptors. This framing clarifies exactly what properties are needed and where prior work falls short.

## Weaknesses

### Fatal
None.

### Major

- **Duplicate detection claims lack ground-truth validation.** Table 2 reports over 100,000 near-duplicates (up to 33 % of ICSD) based solely on an EMD threshold of ≤ 0.01 Å on PDA(S;100). The paper provides no manual inspection of flagged pairs, no comparison to known ground-truth duplicates, no verification via a second independent method (e.g., RMSD after alignment, chemical formula checks), and no estimate of the false-positive rate. The 0.01 Å threshold is physically motivated (thermal noise floor), but because PDA is only generically complete (away from a measure-zero subspace), distinct but degenerate crystals could produce distances below threshold. The paper acknowledges prior work on *exact* duplicates (Anosova et al., 2024) but does not validate its own *near*-duplicate claims. Without this validation, the headline numbers in Table 2—the paper's most striking practical result—rest on an unsubstantiated assumption. This is the single most impactful weakness and should be addressed before the paper can be fully trusted.

### Minor

- **Improvement over PDD on real databases is not quantified.** The paper shows convincingly that $\operatorname{PDD}^{\{2\}}$ distinguishes artificial homometric sets where PDD fails (Examples 2.5/3.3, 3.6). However, it never quantifies, for actual database pairs, how many near-duplicates are missed by PDD (or PDA) but found by $\operatorname{PDD}^{\{2\}}$, or vice versa. Since the pipeline uses $\operatorname{PDD}^{\{2\}}$ "only in rare cases to confirm exact duplicates" (line 194), one cannot assess whether the added complexity of higher orders provides meaningful improvement on real-world data beyond the simpler PDA filter. A simple experiment reporting, for each database, the number of pairs passing each hierarchical stage (ADA, PDA, $\operatorname{PDD}^{\{2\}}$) would clarify this.

- **Lipschitz continuity bound condition is underspecified for degenerate cases.** Theorem 4.1 requires $\varepsilon \in [0, r(S))$ (packing radius). The paper acknowledges (lines 102–103) that neighbor swapping can occur under perturbation but asserts distances change continuously up to $2\varepsilon$. However, the main text does not provide a rigorous argument showing the invariant remains Lipschitz with constant 2 when the set of $k$ nearest neighbors changes due to near-degeneracies. The proof is deferred to the appendix (which is standard for this venue, but the main text should at least sketch the reasoning when neighbor reordering occurs). The condition $\varepsilon < r(S)$ prevents point-crossing but does not guarantee the $k$-th neighbor set is stable—nearly equal distances can cause discontinuities in which points are included, though the *values* may still be Lipschitz. A brief sketch in the main text would improve confidence.

- **Slight mismatch between Problem 1.2 framing and results.** Problem 1.2 asks for completeness (condition b). The paper achieves full completeness only for $n=1$ (Theorem 4.3); for $n>1$, completeness holds only generically (away from measure-zero subspaces), via prior work (Widdowson & Kurlin, 2022). The abstract and introduction are careful ("contributions to notoriously hard Problem 1.2"), but the framing could more explicitly state that full completeness in higher dimensions remains open, to avoid readers inferring a stronger result.

### Trivial

- The claim in the discussion that the invariants "parametrize the 'universe' containing all known crystals as 'shiny stars'" (line 189) is metaphorical but technically overstates what is proven—the invariants parametrize a space of invariant values, not the crystals themselves (invertibility is not proven for $n>1$). This is a presentational quibble in the discussion section.

## Nice-to-Haves

- **Ground-truth validation of duplicate claims** (the Major weakness above). Randomly sample 50–100 flagged near-duplicate pairs (especially from ICSD with its 33 % rate) and verify via RMSD after optimal alignment, chemical composition comparison, or expert inspection. Report the true-positive rate.
- **A simple ablation table** showing how many pairs pass each stage of the hierarchical pipeline (ADA → PDA → $\operatorname{PDD}^{\{2\}}$) for each database, quantifying the incremental discriminative power of each stage on real data.
- **A case-study overlay** (like Fig. 4 for Pauling) for a typical near-duplicate pair from each database, showing RMSD after alignment and the corresponding $\operatorname{PDD}^{\{2\}}$ distance, to build trust in the detection.
- **A downstream ML experiment** (e.g., band-gap prediction with vs. without duplicates) would strengthen the claim that duplicate removal improves learned models, but this is beyond the paper's stated scope and is not required for the main contribution.

## Removed Points

These points were raised by the reviewers but are removed as per the filtering rules:

1. **"Proof is relegated to the appendix"** (about Theorem 4.1). The parser strips appendices; the proof exists in the original submission. This is a formatting artifact, not a weakness.

2. **"No comparison to PDD (first-order) in Table 3/4 running times"** (comparing running time of PDA pipeline to PDD-only pipeline). The paper's pipeline already uses PDA (derived from PDD) as an intermediate step and compares against COMPACK (the traditional baseline) to show a dramatic speedup from "years to hours." A PDD-only timing comparison would add little—the overhead of $\operatorname{PDD}^{\{2\}}$ is already shown in Fig. 7 (left). The claim is about orders-of-magnitude improvement over the previous state of the art, not incremental overhead within the hierarchy.

3. **"Robustness to threshold is not tested"** (varying the 0.01 Å cutoff). Fig. 7 (right) explicitly shows "growing percentages of near-duplicates in 5 databases for different thresholds in Å." This criticism is factually wrong—the paper already provides this analysis.

4. **"Pauling pair is a single example"** implying insufficient evidence. The paper provides: (i) Example 2.5 with infinite 1D homometric family distinguished by PDD (already), (ii) Example 3.3 where $\operatorname{PDD}^{\{2\}}$ distinguishes the 2D family from Example 2.5, (iii) Example 3.6 with Pauling 3D crystals, and (iv) Fig. 5 with EMD plots for the Fig. 3 sets. There are multiple distinct examples across dimensions.

5. **"Practical advice 'small k is enough' is not tested."** The paper uses $k=100$ for experiments and Theorem 4.4 provides asymptotic justification. This is a theoretical guideline, not a testable claim requiring separate experiments.

## Novel Insights

The harsh critic's emphasis on validation highlights a genuine gap between the paper's theoretical rigor (well-posed problem definition, provable properties) and its empirical claims (unvalidated duplicate counts). This tension is common in papers that bridge pure geometry and large-scale applied science: the invariants are mathematically elegant and the runtime improvements are undeniable, but the headline numbers about database integrity rest on an unverified threshold. The most novel observation emerging from the reviews is that the paper's strongest contribution may not be the specific duplicate counts in Table 2, but rather the **demonstration that a hierarchy of Lipschitz-continuous invariants can reduce all-vs-all crystal comparison from computationally intractable (years via RMSD/COMPACK) to practically feasible (hours on a desktop)**. This architectural insight—using fast vector filters (ADA/PDA) to massively prune the search space before applying more expensive discriminators ($\operatorname{PDD}^{\{2\}}$)—is reproducible and independently valuable regardless of whether the exact 0.01 Å threshold correctly classifies every near-duplicate. Even if 10–20 % of the flagged pairs were false positives (which would need validation to determine), the methodology still transforms a previously impossible scaling problem into a tractable one and provides an explicit, principled starting point for community refinement.

## Suggestions

1. **Validate the duplicate claims.** Sample 100 flagged pairs (stratified across databases) and verify each with a second method—RMSD after optimal alignment, or check whether chemical formulas are identical or closely related. Report the true-positive rate. This single experiment would substantiate (or appropriately caveat) the headline numbers in Table 2.
2. **Add an ablation table** showing, for each database, the number of candidate pairs surviving each hierarchical stage (ADA → PDA → $\operatorname{PDD}^{\{2\}}$), with the incremental rejection rate. This would quantify the practical improvement contributed by each layer, including the higher-order invariants, on real data.
3. **Add a brief sketch** in the main text of why the Lipschitz bound holds even when neighbor reordering occurs under perturbation (the proof is in the appendix, but a 2–3 line intuition would help readers).
4. **Tone down** the metaphorical "parametrization of the universe" phrasing in the discussion, or explicitly note that the invariants parametrize a space of invariant values rather than the crystals themselves unless invertibility is proven.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>