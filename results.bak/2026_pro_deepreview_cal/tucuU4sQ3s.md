Now I have all the information I need. Let me compile the final review.

## Summary

NuSA-CL proposes a memory-free continual learning method for zero-shot vision-language models (CLIP). Before each new task, it performs SVD on the current weight matrices to identify a low-energy "null space," then constrains low-rank (LoRA-style) updates to this subspace by learning only a small intermediate matrix M while keeping the null-space bases frozen. After each task, the update is merged into the backbone, maintaining a fixed parameter budget. The method achieves state-of-the-art performance among storage-free approaches on MTIL and CIFAR-100 benchmarks while using 40× fewer parameters and 3× fewer GPU-hours than storage-based competitors.

## Strengths

- **Novel and principled method design.** The core idea — dynamically identifying underutilized spectral directions via SVD and enforcing a persistent constraint that updates remain in the approximate null space — is both clean and well-motivated. Unlike prior work (MiLoRA, Wang et al. 2025) that uses low-energy subspaces only for initialization, NuSA-CL's persistent constraint (freezing U_n, V_n while training only M) is the key mechanism that prevents updates from drifting into principal directions where they would overwrite prior knowledge (validated in Table 4a).

- **Comprehensive and convincing empirical validation.** The paper evaluates on three distinct setups: full-shot MTIL (Table 1), 5-shot MTIL (Table 2), and 50-step CIFAR-100 (Table 3). In each case, NuSA-CL is the top storage-free method. On the 50-step CIFAR-100 split, it achieves 71.85% Last accuracy, outperforming ZSCL by 4.4 percentage points — strong evidence for long-sequence scalability.

- **Compelling efficiency story.** NuSA-CL uses 1.5M trainable parameters, zero additional storage, 6.6GB peak GPU memory, and 1.21 GPU-hours (Table 1). This is 40× fewer parameters, zero storage (vs. 4.8GB), and ~3× faster than MoE-Adapters while remaining competitive in performance (82.8% vs. 85.0% Last). The efficiency advantage is not just claimed but quantitatively demonstrated across multiple resource dimensions.

- **Thorough ablation and analysis.** The subspace choice experiment (Figure 3a) cleanly shows that Tail > Top > Random for forgetting across all ranks. The persistent constraint ablation (Table 4a) demonstrates that unfreezing U_n, V_n causes substantial degradation. The null-space dynamics analysis (Figure 2, Section 6.1) provides mechanistic insight showing NuSA-CL progressively increases effective rank across tasks while LoRA and Full-FT remain spectrally static.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theoretical analysis remains in parameter space.** Lemma 1 and Theorem 2 bound interference in terms of Frobenius inner products between weight matrices and updates. While the paper honestly acknowledges this as a "local stability condition rather than a full function-level guarantee" (Section 4), the gap between parameter-space bounds and task-level forgetting is not bridged. The theoretical contribution serves as motivation rather than a performance guarantee. This does not undermine the empirical results but limits the theoretical contribution's standalone value.

- **Evaluation limited to a single backbone (ViT-B/16).** All experiments use only CLIP ViT-B/16. While the paper discusses scaling to larger backbones in Section 6.3, no empirical results are shown for ViT-L/14 or other CLIP variants. Given that the method's core operation (SVD on attention projection matrices) scales with matrix dimensions, results on a larger backbone would strengthen the scalability claims.

- **No direct comparison with prompt-based continual learning methods.** The paper focuses on LoRA-based PEFT methods, which is a reasonable scope. However, prompt-based methods (L2P, DualPrompt, CPE-CLIP) are a major family of PEFT approaches for CL and their absence from the comparison makes the baseline coverage somewhat narrower than it could be. The paper does mention prompt-based methods in related work (Section 2.1) but doesn't explain why they were excluded from experiments.

### Trivial

- **Terminology precision.** The paper uses "null space" to refer to a low-energy subspace identified by an energy cutoff on singular values, which is not a true null space (kernel). The paper consistently qualifies this as "approximate null space" or "low-energy subspace," so this is a minor presentational quibble rather than a substantive error.

## Nice-to-Haves

- A direct empirical correlation between the cumulative interference bound (Theorem 2) and observed forgetting metrics would strengthen the theory-practice connection.
- A task-order sensitivity experiment (e.g., deliberately ordering CIFAR-100 splits by semantic similarity) would directly probe the acknowledged limitation about correlated task sequences.
- An additional held-out zero-shot dataset beyond the MTIL suite would provide independent confirmation that pre-trained zero-shot capabilities are preserved.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Scaling the SVD step to larger backbones needs projection"** (from Harsh Critic): The paper already addresses this in Section 6.3 ("Practical guidance for larger backbones"), noting that attention projection dimensions for larger CLIP variants are 768–1024, and that truncated/approximate SVD can be used. This is adequately covered.

- **"Relation to regularization-based CL (EWC, SI) not discussed"** (from Harsh Critic): The paper's scope is PEFT methods for VLMs. EWC and SI target full-model training and are not PEFT methods. The paper clearly states its focus and baseline rationale. Including them would not change the contribution.

- **"Missing appendix details"** — The parser strips appendices; the original submission contains them. This is not an author error.

- **"Could the metric be measuring a proxy?" / "Are confounders controlled?"** — These are generic sweep questions from the harsh critic framework with no concrete anchor in the paper. Removed as noise.

- **Strength Finder's claims about "the problem is important" or "interesting question"** — Generic, non-specific strengths that don't identify concrete paper contributions. Removed.

## Novel Insights

The paper's use of the tail (low-energy) singular subspace as a *persistently constrained* update region — rather than merely an initialization — represents a genuinely novel synthesis of spectral analysis and continual learning. The dynamic analysis (Figure 2) showing that null-space-constrained updates progressively increase the effective rank of weight matrices while baseline methods remain spectrally static provides a mechanistic explanation for *why* the method works that goes beyond simple interference arguments: the model is literally accumulating knowledge in previously underutilized dimensions rather than overwriting. This framing of continual learning as spectral capacity expansion, validated quantitatively, is a useful conceptual contribution beyond the specific method.

## Suggestions

- Consider adding even a single-dataset experiment on ViT-L/14 to validate the scaling claims empirically rather than relying solely on the qualitative discussion in Section 6.3.
- The per-layer rank computation (r = min(d - k, r_max)) is clear from Section 3.1, but adding a sentence on how many trainable parameters this yields per module (e.g., "with r_max=128, each attention projection contributes r×r = 16,384 trainable parameters in M") would help practitioners.
- Consider adding a brief note in the experimental setup explaining why prompt-based CL baselines were excluded (e.g., they typically require task-ID at inference or add per-task parameters, which breaks the fixed-budget property).

## Score and Decision

### Anchor comparison:

**Round 1 (Bracketing):**
- `JIlIYIHMuv` (LVLM-CL, avg 2.50): Rejected paper on CL for LVLMs with limited experiments. NuSA-CL is substantially stronger in method, experiments, and presentation.
- `WM5G2NWSYC` (Projected Subnetworks, avg 2.00): Weak paper on zero/few-shot learner updates. NuSA-CL is far stronger.
- `bqv7M0wc4x` (ICL-TSVD, avg 5.50): Accepted paper using SVD truncation for CL. NuSA-CL has a more novel method (persistent constraint vs. truncation), more comprehensive experiments, and stronger efficiency story.
- `hac6DzbMa7` (Orthogonal Weights CL, avg 4.50): Rejected paper with problematic theory. NuSA-CL is clearly stronger.
- `1aF2D2CPHi` (Open-Vocab Customization, avg 8.00): Strong accepted paper on DFKD for CLIP. Full system contribution with good novelty.

**Round 1 bracket:** NuSA-CL is clearly above the 5.50 middle anchor and below the 8.00 strong anchor. Initial bracket: **6.0–7.5**.

**Round 2 (Narrowing):**
- `sb7qHFYwBc` (C-CLIP, avg 6.50): CL for VLMs using LoRA + contrastive consolidation. NuSA-CL has a more principled method, more benchmarks, and better ablations. NuSA-CL is stronger.
- `TLADT8Wrhn` (TiC-CLIP, avg 6.25): Primarily a benchmark paper; different contribution type.
- `7D9X2cFnt1` (Elastic Feature Consolidation, avg 7.00): Strong accepted paper on EFCIL. Comparable quality — both have good theoretical motivation, thorough experiments, and clear contributions. NuSA-CL's contribution is comparably novel with a broader scope (VLM continual learning) but limited to one backbone.

**Final comparison:** NuSA-CL sits between C-CLIP (6.50) and Elastic Feature Consolidation (7.00). It is clearly stronger than C-CLIP due to its more principled design, better ablations, and efficiency story. It is comparable to Elastic Feature Consolidation in quality. Given the clean method, comprehensive validation, strong efficiency advantages, and practical relevance, I place NuSA-CL at **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>