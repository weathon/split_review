## Summary

This paper proposes Nonparametric Variational Differential Privacy (NVDP), a method for sharing privacy-preserving transformer embeddings by integrating a Nonparametric Variational Information Bottleneck (NVIB) layer into a transformer architecture. The NVIB layer learns a posterior distribution over embeddings, from which noisy samples are drawn and shared. Privacy is measured via Rényi divergence and converted to Bayesian Differential Privacy (BDP) guarantees. The method is evaluated on GLUE tasks against a VIB-based ablation (VTDP), showing consistently better privacy–utility trade-offs.

## Strengths

- **Novel closed-form privacy bound (Equation 7):** The paper derives an upper bound on the Rényi divergence between two finite samples from the learned Dirichlet process posteriors, enabling exact and efficient privacy-loss computation specific to the NVDP architecture. This is a non-trivial technical contribution.

- **Clear empirical advantage over the VTDP ablation:** Across all six GLUE tasks tested, NVDP achieves both lower BDP ε_μ values and lower Rényi divergence while attaining higher or comparable accuracy (Table 1, Figure 2). For instance, on MRPC, NVDP reaches 83.0% accuracy at BDP 10.70 vs. VTDP's 81.1% at BDP 11.50. The consistency of this gap across diverse tasks lends credibility to the claim that the nonparametric bottleneck is more effective than the parametric VIB variant.

- **Architecture-level privacy enforcement:** Removing the residual skip connection around the denoising MHA (Section 3.1) is a concrete design choice that prevents raw embeddings from bypassing the stochastic bottleneck. This directly supports the local DP framing of the mechanism.

- **Strong utility preservation:** NVDP matches or exceeds the non-private regularized baseline (+REG) on several tasks (e.g., 83.0% vs. 82.4% on MRPC accuracy), demonstrating that the privacy mechanism does not inherently degrade downstream performance.

- **Careful experimental protocol:** Five independent runs per setup, fixed Rényi order (λ = 1.1), fixed BDP failure probability (δ_μ = 10⁻⁵), and selection via validation set are sound practices that add rigor.

## Weaknesses

### Major

- **No empirical validation of privacy against actual attacks.** The paper evaluates privacy exclusively through mathematical metrics (Rényi divergence, BDP ε_μ) without demonstrating that these metrics translate to real protection. There are no reconstruction, membership inference, or embedding inversion attack experiments. The paper repeatedly claims "strong privacy guarantees" (abstract, introduction, conclusion), but nothing in the experiments grounds what a BDP ε_μ of 10.7 or an RD of 0.34 actually means for an adversary's ability to recover sensitive information. In the absence of attack experiments, the reported privacy numbers remain abstract and the phrase "strong privacy guarantees" is unsupported. Comparing with the DPPN anchor paper (score 6.0), which included attack experiments but lacked formal guarantees, this gap is significant.

- **Only one privacy baseline (VTDP).** The paper's entire privacy comparison is against a single VIB-based ablation. There is no comparison to simpler noise-based approaches (e.g., adding fixed Gaussian noise to embeddings), to other local DP mechanisms for text, to DP-SGD on the downstream classifier, or to heuristic perturbation methods like those in DPPN. This narrow baseline set makes it difficult to assess where NVDP sits in the broader landscape of privacy-preserving embedding methods and whether the NVIB machinery yields practical gains over simpler alternatives.

### Minor

- **No standard adjacency notion makes ε values hard to interpret against the DP literature.** The paper explicitly states (Section 3.2): "We do not assume any specific notion of adjacency between examples. … we report the maximum Rényi divergence over all input pairs as the RDP measure." Taking the maximum over *all* input pairs is technically a *stronger* guarantee than standard DP with a specific adjacency relation (it protects against distinguishing any two inputs, not just nearby ones). However, this means the reported RD and BDP values are not directly comparable to ε values in the DP literature, which are always defined relative to a specific adjacency relation. The BDP aggregation partially addresses this, but the paper would benefit from also reporting results under a concrete text-level adjacency (e.g., sentences differing by up to k consecutive words, as cited from Sun et al. 2019) to anchor the numbers in standard practice.

- **Missing experimental details for the privacy–utility curves.** The procedure for varying the NVDP hyperparameters (λ_D, λ_G) to generate the trade-off curves in Figure 2 is not described. It is unclear how many points were evaluated, whether the same hyperparameter search budget was used for VTDP, or whether the curves represent Pareto fronts or simply a sweep. This limits reproducibility of the trade-off analysis.

- **The relationship between the training objective and the privacy metric deserves more discussion.** The NVDP loss (Equation 5) includes KL-divergence terms (L_D, L_G) that penalize information content in the latent representation. The privacy metric (Equation 7) also measures information leakage via Rényi divergence. While these are distinct quantities, the training objective is designed to produce posteriors close to an uninformative prior, which naturally limits distinguishability between different inputs' posteriors. The paper should acknowledge and discuss this connection explicitly rather than letting it appear as an unremarked coupling.

### Trivial

- **Figure 2 description error:** The text states that NVDP curves occupy the region "closest to the top-right corner," but since the x-axis is ε_μ (lower = more private), the desirable privacy–utility region is actually the *top-left* (high accuracy, low ε_μ). This does not affect the results but should be corrected.

- **No error bars on utility and privacy numbers.** While five runs were conducted, the paper reports only the best validation-set run without variance, which is standard for GLUE-style benchmarks but would add transparency in a privacy–utility context where both quantities are stochastic.

## Nice-to-Haves

- Adopt a concrete text-level adjacency relation (e.g., sentences differing by up to k words) and report RDP/BDP under that relation, to make the ε values interpretable against the broader DP literature.
- Include at least one privacy attack experiment (e.g., embedding inversion or membership inference) to validate that lower RD/BDP values correspond to reduced attack success.
- Add a fixed-noise baseline (e.g., Gaussian noise with fixed variance added to embeddings) to isolate the benefit of learned, task-calibrated noise.
- Discuss how the privacy properties of the pretrained BERT encoder interact with the NVDP guarantee — the BERT weights could themselves encode training-data information.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No meaningful privacy threat model; the claimed DP is not standard" (Harsh Critic, Critical Issue 1):** The critic claims the lack of adjacency "turns the guarantee into an indiscriminate indistinguishability between any two inputs, which is neither standard nor practical" and calls it a "structural flaw." This is factually wrong: taking the maximum over *all* input pairs is actually a *stronger* guarantee than standard DP, not a weaker or invalid one. The paper's choice is conservative, not flawed. The interpretability concern is real (retained above as Minor), but the claim that it "severs the connection to real privacy goals" or is a "structural flaw" is incorrect and removed.

- **"Circularity in the privacy–utility analysis" (Harsh Critic, Critical Issue 3):** The critic claims the training objective minimizes quantities closely related to the privacy metric, making the evaluation circular. This misunderstands the paper's design: the NVIB objective is intended to reduce information while preserving task relevance, and improved privacy is the natural and expected consequence. The relationship between the training loss and the privacy metric is by design, not a methodological error. Retained as a Minor point requesting clearer discussion of this relationship.

- **"VTDP ablation suffers from the same coupling, so the comparison between NVDP and VTDP is largely a contest of which model more effectively optimizes a metric aligned with its own regularizer":** Both models use information-bottleneck-style regularization; comparing them is precisely how one demonstrates that the *nonparametric* variant is more effective than the *parametric* variant. The paper does not hide this — it is the central experimental claim. Removed.

- **"The architecture removes the standard residual connection … should discuss whether this alone degrades task performance":** The paper already demonstrates that NVDP matches or exceeds the non-private +REG baseline on several tasks (Table 1), which indirectly addresses this concern. A deeper ablation would be nice-to-have but the current evidence is sufficient. Removed.

- **"Equation 7 is presented without derivation":** The paper explicitly states this is an upper bound and cites the NVIB framework (Henderson & Fehr, 2023) for the underlying sampling procedure. The derivation sketch is present in Sections 3.2–3.3; a full proof in the appendix would be helpful but the appendix is stripped by the parser. Removed as speculative.

- **"The procedure for varying hyperparameters … is not described":** Retained above as Minor. Not removed.

- **Strength Finder claim about "Strong utility relative to non-private baselines":** Retained — this is well-supported by Table 1.

## Novel Insights

None beyond the paper's own contributions. The core idea — using a nonparametric variational information bottleneck to learn a data-calibrated noise distribution for differential privacy — is genuinely novel. The closed-form Rényi divergence bound over Dirichlet process samples (Equation 7) is a technical contribution that could be useful beyond this specific setting.

## Suggestions

- The paper would benefit significantly from grounding its privacy claims in at least one concrete attack experiment. Even a simple embedding inversion or membership inference test would transform the abstract ε_μ values into meaningful security evidence.
- Consider reporting RDP under a standard word-level adjacency (e.g., differing by up to 5 consecutive words) alongside the current all-pairs maximum, to make results interpretable against the DP literature while retaining the stronger guarantee.
- Add a simple fixed-noise baseline (same noise variance applied uniformly, without NVIB calibration) to clearly demonstrate the value of learned, task-adaptive noise.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FNCFiXKYoq (MAAD Private) | 3.00 | R1 | Weaker — heuristic debiasing, limited DP novelty |
| TbOcySs6g8 (DP Synthetic Dataset) | 2.50 | R1 | Weaker — less principled privacy approach |
| sruGNQHd7t (Domain Shifting) | 3.00 | R1 | Weaker — no formal DP, narrower scope |
| nM2kuesKpC (D2P2-SGD) | 3.00 | R1 | Weaker — incremental DP-SGD variant |
| vxmvbzw76R (Split-and-Denoise) | 4.75 | R2 | Weaker — similar concept (LDP on embeddings) but looser guarantees (ε=100-1000), no attack validation, less principled noise calibration |
| fGSEWgRHNZ (Adaptively Private) | 4.75 | R2 | Weaker — incremental prediction privatization |
| nATTIkte9f (LMO-DP) | 4.75 | R2 | Weaker — incremental DP-SGD improvement |
| 3uITarEQ7p (DP Model Compression) | 5.50 | R1/R2 | Comparable — similar domain, similar strengths (good results) and weaknesses (limited baselines, novelty concerns) |
| i2Ul8WIQm7 (Privacy Risks of PEFT) | 5.80 | R2 | Comparable — evaluation-focused, similar quality |
| DF5TVzpTW0 (DPPN) | 6.00 | R1 | Slightly stronger — more extensive experiments and attack validation, but lacks formal DP guarantees that NVDP provides |
| sVNfWhtaJC (AdaDPSyn) | 6.50 | R2 | Stronger — data-adaptive DP with more comprehensive experiments and stronger novelty claim |
| B6AQzaQCsl (Hot PATE) | 6.50 | R2 | Stronger — well-established framework extension with solid experiments |
| lLkgj7FEtZ (DP Steering) | 6.50 | R2 | Stronger — novel DP application with thorough evaluation |
| 3d0OmYTNui (Private RLHF) | 6.67 | R2 | Stronger — original DP+RL combination with competitive utility |
| KYipmCMmSO (Private Fine-tuning Dynamics) | 6.33 | R2 | Stronger — theoretical depth with empirical validation |
| oZtt0pRnOl (DP ICL) | 8.00 | R1 | Much stronger — comprehensive evaluation, clear practical impact |
| vf5aUZT0Fz (DEPT) | 8.00 | R1 | Much stronger — major architectural contribution, not directly comparable |
| tyEyYT267x (Interpolating Diffusion) | 8.00 | R1 | Much stronger — SOTA results, not directly comparable |
| OvoCm1gGhN (Differential Transformer) | 8.00 | R1 | Much stronger — novel attention mechanism, broad impact |

**Bracket:** Round 1 placed the paper between 5.0 and 6.5. Round 2 narrowed this: NVDP is stronger than the 4.75 anchors (SnD, LMO-DP, Adaptively Private), comparable to the 5.50–5.80 anchors (DP Model Compression, PEFT Privacy Risks), and weaker than the 6.50+ anchors (AdaDPSyn, Private RLHF, DP Steering). Within the 5.0–6.0 range, NVDP's formal privacy analysis and closed-form bound give it an edge over DPPN's heuristic approach, but its narrower evaluation and lack of attack validation pull it below the 6.0 level. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>