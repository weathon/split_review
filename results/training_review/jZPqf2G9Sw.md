Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces the first diffusion-based generative model for proteins that can be conditioned on dynamical properties (specifically, the lowest non-trivial normal mode from NMA). The core technical contribution is an invariant NMA-loss function (pairwise angles + relative amplitudes) that serves as an analytical conditioning signal, avoiding the need for a separate neural network to predict eigenvectors. The method is demonstrated on two settings: a custom GVP-based denoiser with strain/random dynamics targets, and joint (dynamics+structure) conditioning applied to the pretrained Genie model for hinge-motif proteins (lysozyme, adenylate kinase, haemoglobin), yielding designable backbones with matched displacements.

## Strengths

- **First dynamics-conditioned generative model for proteins.** The paper identifies and addresses a genuinely underexplored problem—conditioning protein backbone generation on dynamical properties rather than just static structure. Section 3.1 explicitly argues why a neural-network-based approach to eigenvector conditioning is impractical, and the NMA-loss in Section 3.2 provides a workable alternative. This is a novel and well-motivated contribution.

- **Demonstrated joint conditioning on structure and dynamics for hinge targets.** The method simultaneously enforces a desired displacement pattern and a fixed structural motif on the pretrained Genie model without retraining. Figure 5 shows that conditional samples simultaneously achieve low NMA-loss and low RMSD (unattainable by unconditional samples), and scTM designability rates of 0.41–0.78 are reported for three hinge targets (Section 5.2). The scTM evaluation pipeline (ProteinMPNN+ESMFold) is an independent, non-circular validation.

- **Transferability to pretrained models without retraining.** The joint conditioning framework is applied to Genie by only modifying the reverse sampling process (Section 4.4), demonstrating that the approach can be "plugged into" existing unconditional diffusion models without modifying their weights. This significantly lowers the barrier to adoption.

- **Principled invariant loss design.** The NMA-loss in Section 3.2 uses pairwise cosines and normalized amplitudes, making it rotation/translation invariant. This correctly accounts for the fact that NMA eigenvectors only provide relative displacement information (Section 3.2 explicitly invokes (Bahar et al., 2010) on this point). The use of the differentiable Kabsch algorithm for structure conditioning (Section 3.2) also respects equivariance.

## Weaknesses

### Major

- **Circular evaluation of dynamics conditioning in Section 5.1.** The primary quantitative evidence that conditioning enforces target dynamics is Figure 2, which shows NMA-loss reduction—the same metric used as the conditioning objective. That conditional samples achieve lower loss on the very function being optimized is expected and does not establish that the generated proteins possess physically meaningful dynamical behavior. Visual inspection (Figure 3) provides some independent, qualitative evidence, but no quantitative validation using independent measures (e.g., computing the full NMA spectrum on generated structures, comparing collective mode participation beyond the conditioned subset, or running coarse-grained simulations). This weakens the central claim that the method "captures dynamical properties" rather than just overfits a few displacement vectors.

- **Missing structure-only baseline for joint conditioning (Section 5.2).** The joint (dynamics+structure) hinge experiments compare only to unconditional sampling and to dynamics-only conditioning. Without a structure-only (motif scaffolding without NMA-loss) baseline, it is impossible to determine whether dynamics conditioning adds value or actively degrades designability. The high filtering rates (23–60% pass basic geometric filters) and the scTM drops relative to dynamics-only for two targets (lysozyme: 0.93→0.48; adenylate kinase: 1.0→0.78) suggest that the dynamics constraint may conflict with the structure constraint, but this cannot be diagnosed without the structure-only control.

- **NMA computation from denoised structures at each diffusion step is underspecified.** The core technical step—computing NMA eigenvectors from the expected denoised structure $\mathbb{E}[x_0|x_t]$ at each reverse diffusion step—is described only at the conceptual level. The paper does not specify: (a) which elastic network model (e.g., ANM, cutoff-based ENM) and specific parameters (cutoff distance, spring constant) define the Hessian $\mathbf{K}$, (b) how the $3N \times 3N$ eigenvalue problem is solved (eigensolver, handling of six zero eigenvalues from rigid-body modes), (c) how differentiability through the eigenvalue decomposition is achieved for gradient-based guidance, or (d) whether NMA is computed on partially denoised structures (which are noisy and may not reside near an energy minimum) or only on the final structure. Section 2.2 and 3.2 describe NMA in general terms but omit the implementation decisions that determine whether the method is correct and reproducible. Code release would address this, but as presented the methodology cannot be assessed for correctness.

### Minor

- **Guidance scales of 2000–3000 not justified.** These values are orders of magnitude larger than typical classifier/reconstruction guidance scales (1–10). The paper does not discuss how they were chosen, whether they cause numerical instability, or whether they indicate that the conditioning signal from the NMA-loss is extremely weak relative to the unconditional score. A sensitivity analysis would help.

- **Small sample sizes and high filtering rates for hinge experiments.** After filtering, only ~27 conditional samples per target remain (with haemoglobin retaining only 23% of samples). This is a small sample for reporting scTM proportions. The paper also does not analyze the discarded samples to determine whether they failed due to structure violations, dynamics violations, or both.

- **Changes in secondary structure and radius of gyration not investigated.** Section 5.1 reports that conditioning shifts SSE proportions toward $\beta$-sheets and increases $R_g$, and the paper states this is "interesting" and "left for future work." While not a flaw per se, this unexplained systematic distortion raises questions about whether the dynamics conditioning introduces geometric biases that could affect downstream applicability.

- **Strain target energy definition is unclear.** Section 4.2 defines strain targets as "10 consecutive residues with the largest summed energy" without specifying what "energy" refers to (deformation energy from the normal mode? potential energy from the force field?). This makes the target selection procedure ambiguous.

### Trivial

- None.

## Nice-to-Haves

- Independent dynamics validation: computing the full NMA spectrum on generated backbones (after ProteinMPNN+ESMFold inverse folding) and verifying that the conditioned mode is indeed a low-frequency collective motion, or comparing using an elastic network model to check that the generated residue displacements correspond to a physically consistent hinge-like motion across the whole chain.
- Guidance scale sweep showing how NMA-loss, scTM, and structural validity vary across a range (e.g., 0, 100, 500, 1000, 2000, 5000).
- Computational cost comparison: per-step cost of computing NMA eigenvectors and backpropagating through the loss vs. a standard unconditional diffusion step.
- Ablation of NMA-loss components (angle term only, amplitude term only) to test whether both are necessary.

## Removed Points

These points are flagged to be removed—treat them with caution.

- **Angle term "degeneracy" concern (Harsh Critic point #5):** The critic claims that using cosine between displacement vectors "discards orientation relative to the protein frame" and "could allow degenerate solutions (e.g., a global rotation of all displacements still yields the same pairwise cosines)." This is factually wrong—rotation/translation invariance is an **intentional design goal** of the loss, clearly stated in Section 3.2: "the loss function...enforces the targeted dynamics while being invariant to the protein rotations and translations." A global rotation of all displacement vectors corresponds to the same physical mode expressed in a different coordinate frame; the loss correctly treats this as equivalent.
- **"Novelty overstatement" claim (Harsh Critic point #4):** The critic argues the paper overclaims by saying "unlike previous works, we approximate the conditional term with a simple analytical function rather than an external neural network," claiming reconstruction guidance already does this. However, the paper explicitly cites Chung et al. (2022a) and follows their framework (Section 3.1: "Following Chung et al. (2022a)..." and "as in Chung et al. (2022a)"). The paper's own wording in Section 3.1 is: "Finding an appropriate $p(y|x_0)$ is where the novelty of our method lies." The novelty is in the specific NMA-loss for the dynamics conditioning problem (where an eigenvector-predicting neural network would be impractical), not in the general conditioning framework. Retained as a minor clarity concern in the abstract but not as a substantive novelty overclaim.
- **Generic strength "rigorous theoretical grounding" from Strength Finder:** The SDE theory in Section 3.1 is a restatement of standard reconstruction guidance from Song et al. (2023) and Chung et al. (2022a). The paper's contribution is the NMA-loss, not the theoretical framework. Drop this strength.
- **Generic strength "comprehensive empirical evaluation" from Strength Finder:** Conflicts with the verified weakness about circular evaluation. Drop.

## Novel Insights

None beyond the paper's own contributions. The key insight—that NMA eigenvectors can serve as differentiable conditioning targets via an invariant loss on displacement pairwise angles and relative magnitudes—is the paper itself. No reviewer synthesized a perspective that goes substantially beyond the paper's framing.

## Suggestions

1. **Resolve the circularity in dynamics evaluation.** Compute the full NMA on generated backbones (after inverse folding) and quantitatively compare mode overlaps (e.g., via the root-mean-square inner product or cosine similarity of the full eigenvector, not just the conditioned residues). Alternatively, use an independent dynamics characterization method (coarse-grained MD, elastic network model cross-correlation analysis) to verify that the conditioned residues participate in a physically consistent collective mode.

2. **Add a structure-only conditioning baseline for the hinge experiments.** Run the same Genie pipeline with only the structure loss (RMSD-based Kabsch alignment, no NMA-loss) and report scTM, filtering rates, and per-sample RMSD. This will isolate the contribution (or degradation) caused by dynamics conditioning and is essential to support the claim of effective joint conditioning.

3. **Specify the NMA implementation details.** In Section 3.2 or a method appendix, state: the elastic network model used (e.g., ANM with Cα cutoff of some value), the spring constant, the eigensolver, how the six rigid-body modes are handled, and how differentiability is achieved. If the computation is done on $\mathbb{E}[x_0|x_t]$ only at the final denoising step(s) rather than every step, clarify this.

4. **Include a guidance scale sensitivity analysis.** At minimum, state the range tested and show how key metrics (NMA-loss, scTM, geometric validity) vary with scale to demonstrate robustness.

5. **Investigate the filtered-out samples.** For the hinge experiments, analyze why ~40–77% of samples fail geometric filters (mean chain distance or RMSD). Are the failures driven by dynamics conflicts, structure conflicts, or both? This analysis could reveal whether the current loss weighting or guidance scheme needs adjustment.

## Score and Decision

The paper addresses a genuine gap and proposes a creative solution with a physically motivated loss design. The demonstration of joint conditioning on Genie without retraining is a practical contribution. However, the primary evaluation of dynamics conditioning is circular (uses the same NMA-loss being optimized), the joint experiments lack a structure-only baseline needed to isolate the effect of dynamics, and the core technical mechanism (computing NMA from noisy structures at each diffusion step) is underspecified to the point that correctness and reproducibility cannot be assessed. These are substantive concerns that the authors could address with additional experiments and specification, but in the current form, the evidence does not fully support the central claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>