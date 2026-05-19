Now I have a thorough understanding of the paper and can verify each reviewer claim directly. Let me construct the consolidated review.

## Summary

The paper introduces MVPSA, a multi-view extension of probabilistic slot attention that aggregates view-specific slots into viewpoint-invariant content representations while separately modeling view information. The central contribution is theoretical: proving that aggregate content representations are identifiable up to affine equivalence (Theorem 2), invariant across viewpoint subsets under viewpoint sufficiency (Theorem 3), and approximately equivariant (Theorem 4) — all without requiring camera pose supervision. The model is evaluated on synthetic 2D data and imaging benchmarks (CLEVR-MV, CLEVR-AUG, GQN, plus new MVMOVI-C/D datasets).

## Strengths

- **First theoretical identifiability guarantees for multi-view object-centric learning.** Section 4 provides formal proofs that aggregate content representations are identifiable up to affine equivalence (Theorem 2), viewpoint-invariant under sufficiency (Theorem 3), and approximately equivariant (Theorem 4). This is genuinely novel — prior identifiability results (Kori et al., 2024; Brady et al., 2023; Lachapelle et al., 2023) are single-view only, and multi-view OCL methods like MulMON lack such guarantees.

- **Viewpoint-agnostic model design.** Unlike Li et al. (2020) which requires paired camera parameters, MVPSA infers view information from images via a learned posterior \(q(\mathbf{v}|\mathbf{x})\) and marginalizes over views in the ELBO (Equation 10). This is clearly stated and formalized in the graphical model (Figure 2a).

- **Empirical verification of identifiability on synthetic 2D data (Case Study 1).** Figure 3 shows recovered slot and content distributions across four training runs aligning up to affine transformations (SMCC 0.95±0.01), directly supporting Theorem 2. Figure 4 demonstrates that content distributions learned from different view-pairs also align (SMCC 0.87±0.11), supporting Theorem 3. These visualizations are concrete and interpretable.

- **New multi-view datasets (MVMOVI-C, MVMOVI-D).** The paper introduces and releases multi-view extensions of the MoViC dataset, which are stated as a contribution in their own right and can facilitate future multi-view OCL research.

- **Clear formalization of multi-view OCL assumptions.** The paper defines viewpoint sufficiency (Assumption 1), weak injectivity (Assumption 2), and provides a well-structured graphical model (Figure 2) and ELBO derivation — providing a rigorous foundation that prior multi-view OCL work lacks.

## Weaknesses

### Fatal
None.

### Major
None that survive filtering. The issues identified below are substantive but do not invalidate the core contribution.

### Minor

- **Central evaluation metrics (SMCC, MCC, INV-SMCC) are only referenced, not defined.** The paper states that SMCC is "as described in Kori et al. (2024)" (line 159) and does not provide a definition, formula, or even an expansion of the acronym in the main text. While referencing prior work for metric definitions is common practice, these are the paper's primary quantitative measures. Without knowing whether SMCC is a Spearman correlation, a cosine similarity, or something else, the reader cannot independently assess whether the metric is appropriate or whether the reported differences are meaningful. The authors should briefly define each metric (what it measures, its range, what constitutes a "good" value) in the main paper.

- **Proof sketches for Theorems 2–4 are too sparse to convey the reasoning.** The sketches are 1–3 sentences each (lines 120, 126, 132), e.g., Theorem 2's proof just lists three steps ("demonstrate non-degenerate distribution... demonstrate invertibility restrictions... constrain the subspace to affine") without explaining the critical connections: how the GMM structure of c combined with weak injectivity yields the \(\sim_s\) equivalence relation, or how multi-view aggregation preserves the identifiability properties from single-view PSA. Full proofs are deferred to the appendix, which is standard, but the sketches should give a reviewer enough insight to evaluate soundness without the appendix.

- **The paper claims "resolving spatial ambiguities such as partial occlusions" (abstract) but does not evaluate on standard object-centric metrics.** The experiments focus entirely on identifiability metrics (SMCC, INV-SMCC, MCC). There is no evaluation of segmentation quality (ARI, mIoU), reconstruction fidelity (MSE, SSIM), or object discovery accuracy under controlled occlusion. The synthetic 2D case study provides visual evidence but does not quantify segmentation quality. While the paper's primary contribution is theoretical and the evaluation is appropriately scoped toward verifying theoretical claims ("Given the work's theoretical focus, experimentally, we aim to provide strong empirical evidence of our identifiability, invariance, and equivariance claims"), the abstract's practical claim about occlusion remains unquantified.

- **Limited architectural and training details.** The paper describes encoders/decoders at a high level ("additive with MLPs and spatial broadcasting CNNs," "LeakyReLU activations") but does not specify input dimensions, layer counts, latent dimensions (\(d_s, d_v, d_c\)), number of EM iterations \(T\), learning rate, batch size, optimizer, or number of slots \(K\) per dataset. The view encoder architecture (\(q(\mathbf{v}|\mathbf{x})\)) is described only as "inferred with posterior." While referencing prior implementations is common, the absence of these details makes direct reproduction difficult without consulting external code.

### Trivial

- None that survive filtering under the Hard Rules.

## Nice-to-Haves

- A short, simplified identifiability proof sketch for a 2-view, 2-object case in the main paper would help readers grasp the reasoning without consulting the appendix.
- A single synthetic experiment measuring object discovery accuracy (ARI or object count accuracy) as a function of occlusion level would directly validate the claim about resolving spatial ambiguities.
- Error bars / multiple-seed reporting for the imaging benchmark results in Table 1 (the synthetic study does report them: 0.95±0.01, 0.87±0.11).

## Removed Points

These points were flagged by the reviewers but are removed from the main weakness list for the stated reasons:

1. **"Aggregation assumes mixing coefficient is a reliable indicator of object presence"** — The paper describes a plausible mechanism (objects occluded in a view have zero/near-zero mixing coefficients and are thus weighted out) and cannot be expected to exhaustively prove the absence of edge cases in the main paper text. This is a speculation about a potential failure mode, not an identified flaw in the paper's reasoning.

2. **"Baselines are all single-view or view-conditional, making improvements unsurprising"** — This is not a weakness of the paper's evaluation. Comparing against the available (and only) baselines is standard. The fact that multi-view information helps over single-view is expected but still needs to be empirically verified, which the paper does.

3. **"Table 2 numbers are garbled / the paper does not provide clear numbers"** — This is a parser artifact from the PDF extraction. The original submission has a proper table.

4. **"Proof sketches cannot be assessed without appendix"** — Deferring full proofs to an appendix is standard conference practice. This is only retained as a minor weakness about the sketches being *particularly* sparse, not as a fatal gap.

5. **"Missing related works"** — Cannot be verified without external sources; removed per instructions.

6. **"Formatting/style nitpicks" and "typos/spacing/parser artifacts"** — Removed per Hard Rules (parser errors, not author errors).

7. **Generic strengths that conflict with verified weaknesses** (e.g., "the paper addressed an important problem" — generic; dropped per instructions to filter generic strengths). Also "Rigorous formalization" strength partially conflicts with the sparse proof sketches weakness — kept as a separate point since it refers to the assumption framework, not the proofs.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define SMCC, MCC, and INV-SMCC explicitly in the main paper.** Give a brief formula or at minimum state what each acronym stands for, what similarity measure it uses (e.g., Spearman rank correlation between recovered slot means across runs after permutation alignment), its range, and what constitutes a strong result. This is the single most impactful improvement for the empirical section.

2. **Expand the proof sketches for Theorems 2–4 to at least a paragraph each** showing the logical chain. Even without reproducing full appendix proofs, the main text should convey *why* the GMM structure + weak injectivity yields the claimed affine equivalence in the multi-view setting.

3. **Add one standard OCL evaluation metric** (e.g., ARI for segmentation, or object count accuracy) on the synthetic 2D data or CLEVR-MV to support the occlusion-resolution claim made in the abstract. A brief experiment varying occlusion level would be especially informative.

4. **Include an architecture/hyperparameter table** in the main paper or appendix summarizing: input dimensions, encoder/decoder layer counts, latent dimensions (\(d_s\), \(d_v\), \(d_c\)), slot count \(K\), EM iterations \(T\), learning rate, optimizer, and number of views per dataset.

## Score and Decision

The paper presents a genuinely novel theoretical contribution — first identifiability guarantees for multi-view object-centric learning — with a principled model design and clear empirical support on synthetic data and imaging benchmarks. The main weaknesses (undefined metrics, sparse proof sketches, missing standard OCL evaluation) are presentation and scope issues that are addressable in revision. The core contribution is sound and significant.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>