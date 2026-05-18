## Summary

This paper proposes DeNS (Denoising Non-equilibrium Structures), an auxiliary task for training equivariant neural networks on atomistic data. The key insight is that denoising non-equilibrium structures is ill-posed because multiple target structures can share the same energy, but conditioning the denoising on the atomic force vectors of the uncorrupted structure resolves this ambiguity. The paper claims that EquiformerV2 trained with DeNS achieves new state-of-the-art results on OC20 and OC22 (improving energy by up to 15%, forces by up to 12%) and saves 2.3–3.1× training time on OC20 and MD17, while also improving other equivariant architectures like eSCN and SEGNN.

## Strengths

1. **Novel and well-motivated approach to a genuine problem.** The paper identifies a real limitation of prior denoising methods for atomistic data — they are restricted to equilibrium structures, which constitute <1% of available data — and proposes a principled solution: force-conditioned denoising. The argument that non-equilibrium structures have non-zero forces that uniquely identify the target is clearly explained in the introduction (lines 123–129) and illustrated with Figure 1.

2. **Claims of strong empirical results across multiple benchmarks.** The active introduction reports specific, large improvements: up to 15% on energy and 12% on forces on OC22, 2.3× training time savings on OC20 S2EF-2M, and 3.1× sample efficiency on MD17 (lines 142–145). These numbers are concrete, not placeholder values.

3. **Demonstrated generality across architectures and datasets.** The paper claims DeNS improves not only EquiformerV2 but also eSCN on OC20 and SEGNN-like networks on MD17 (line 146), suggesting the method is not tied to a single architecture.

4. **Practical training efficiency benefits.** The reported 2.3× and 3.1× training time/sample efficiency gains are practically significant for large-scale atomistic modeling, where compute costs are a bottleneck.

## Weaknesses

### Fatal
None. The paper's core idea is coherent and the active text is sufficiently complete to evaluate the contribution conceptually.

### Major

1. **Method and experiments content not available in the extracted text.** Sections 3 (Method) and 4 (Experiments) consist only of `\input{content/...}` commands (lines 183–193), whose content files are not present. This means the following cannot be evaluated from the available text:
   - The exact mathematical formulation of the denoising objective and noise model.
   - The specific architecture modifications for encoding forces.
   - The loss function and how the auxiliary task is combined with primary tasks.
   - The noise schedule, hyperparameters, and design choices.
   - Full experimental results tables with baselines and ablations.
   - The actual training curves or time measurements supporting the efficiency claims.

   While this is likely an extraction artifact (the compiled PDF would contain this content via the `\input` includes), the absence of these sections from the review text means a complete technical evaluation is not possible. **This is the single most significant limitation of this review.**

### Minor

1. **Commented-out earlier draft present in source.** Lines 26–98 contain a `\begin{comment}...\end{comment}` block with an earlier version of the introduction that includes `\todo{cite}` and `\todo{XX\%}` placeholders. While the active text (lines 99–147) is a complete and coherent version, the presence of leftover commented-out draft material suggests the manuscript could benefit from a cleanup pass.

2. **The "self-supervised" framing is imprecise.** The paper describes denoising non-equilibrium structures using forces from the dataset. Since forces are supervised labels (not generated from the data itself without labels), calling this "self-supervised" is technically imprecise — it is an auxiliary supervised task using existing labels. The paper does clarify this in practice (forces come from the DFT calculation), but the framing in the abstract and introduction could mislead readers into thinking no labels are used.

### Trivial
None.

## Nice-to-Haves
- A formal illustration of why force-free denoising is ill-posed for non-equilibrium structures (e.g., a simple 1D or 2D example showing multiple structures with the same energy but different forces) would strengthen the motivation.
- A comparison of training overhead (wall-clock time per epoch with vs. without DeNS) would help quantify the "marginal increase in training cost" claim.

## Removed Points
- **"The introduction contains only placeholder \todo{XX\%} values for claimed improvements."** Removed because it is factually wrong for the active text. The active introduction (lines 142–145) reports specific numbers: "improving energy by up to 15%, forces by up to 12%, and IS2RE by up to 15%," "2.3× training time," and "3.1× training time." The `\todo{XX\%}` placeholders appear only in the commented-out earlier draft (lines 26–98), which is not part of the active manuscript.
- **"The paper is incomplete/unpublishable due to placeholder numbers and commented-out text."** The active text is complete and coherent with finalized numbers. The commented-out blocks are leftover draft material — a minor presentation issue, not evidence of an incomplete submission.
- **"Other Observations" points about non-equivariant networks and the "self-supervised" framing**: These are either already addressed (the paper explicitly focuses on equivariant architectures as a design choice) or are minor framing issues already noted above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- Clean up the source file by removing the commented-out earlier draft (lines 26–98 and 163–175) before any public release or resubmission.
- Clarify the framing of DeNS: it is an auxiliary supervised task (using existing force labels), not self-supervised in the strict sense. The paper mostly gets this right, but the abstract's language ("no additional calculations or supervision") could be misinterpreted.
- Ensure that the full method and experimental content (currently behind `\input` commands) is available for review in any future submission — either by providing the compiled PDF or by including the content inline.

## Score and Decision

The paper presents a well-motivated, clearly explained idea with strong claimed results. The core contribution (force-conditioned denoising for non-equilibrium structures) is novel and addresses a genuine limitation in prior work. However, the method and experiments sections are not available in the extracted text, preventing full technical verification of the claims. Based on what **is** evaluable — the clear motivation, the coherent framing, and the specific numerical claims in the active introduction — the paper shows promise but cannot be fully assessed from the available content.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>