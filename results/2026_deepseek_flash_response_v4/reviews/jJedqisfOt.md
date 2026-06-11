Now let me write the final review.

## Summary
- **Score:** 5.5  
- **Decision:** Borderline (leaning toward rejection unless major revisions fix the core framing issue)

---

## Summary
The paper diagnoses two limitations of Spiking Self-Attention (SSA) in Spiking Transformers: poor local modeling (from softmax removal) and high memory overhead (from storing attention matrices). It proposes LRF-SSA, which adds dilated depthwise convolutions to SSA to strengthen local modeling, and LRF-Dyn, which recasts the attention computation as a recurrent charge-fire-reset neural dynamics process to reduce memory. Experiments on ImageNet classification and ADE20K segmentation across Spikformer, QKFormer, and SDT-V3 show modest but consistent accuracy gains (0.44–1.24%) and a 49.4% memory reduction on one configuration.

## Strengths

- **Quantitative diagnosis of SSA's local modeling deficit (Figure 2):** The paper provides measurable evidence that SSA's attention distribution differs from VSA's — 76.68% of VSA attention falls within Manhattan distance 0–5 versus 20.31% for SSA, and entropy comparison (VSA: H=0.1777, SSA: H=0.5637) formalizes the mismatch. This goes beyond prior Spiking Transformer papers that identify a performance gap without quantifying the attention-distribution root cause. The observation is well-motivated and clearly presented.

- **Consistent accuracy improvement across three architectures (Table 1):** LRF-SSA improves accuracy on Spikformer (+1.24%, +0.85%), QKFormer (+0.44%, +0.48%), and SDT-V3 (+0.92%, +0.51%) at multiple parameter scales. The cross-architecture consistency (every tested configuration shows a positive gain) is stronger evidence than evaluation on a single backbone.

- **Joint accuracy gain and memory reduction:** LRF-Dyn improves accuracy while reducing inference storage complexity from O(d²) to O(kd) across all configurations. Section 6.2 reports a 49.4% memory reduction on Spikformer-8-512, which is concretely quantified.

- **Semantic segmentation gains (Table 2):** On ADE20K, LRF-Dyn improves mIoU by +2.7% (5M model) and +1.8% (19M model) over SDT-V3 baselines, demonstrating that benefits extend beyond classification to dense prediction tasks.

- **Monotonic improvement with LRF kernel size (Table 3):** The CIFAR-100 ablation shows accuracy rising monotonically as the LRF kernel cutoff increases for both LRF-SSA (77.86 → 78.64) and LRF-Dyn (77.78 → 78.57), cleanly isolating the LRF module as the driver of gains.

## Weaknesses

### Fatal
None.

### Major

- **The connection between the linear-attention formulation and the neural-dynamics formulation (Eq. 11 → Eq. 12) is not established, undermining the core LRF-Dyn claim.** Eq. 11 is a valid causal linear-attention formulation: `sattn' = q_n × Σ_{j < n} k_j^T v_j + local_conv`. The paper then says this "closely parallels" charge–fire–reset dynamics and proposes Eq. 12: `X_n = A ⊙ X_{n-1} + Γ·Token_n`. No mathematical derivation connects these two equations. The multiplicative query–KV interaction in Eq. 11 (q multiplies the accumulated KV) is replaced in Eq. 12 by an additive update with decay — a fundamentally different operation. The paper does not explain how A, Γ, and Token map to q, k, v, or how the recurrent update approximates the attention computation. Without this derivation, the claim that LRF-Dyn computes an approximation of self-attention via neural dynamics is unsupported. LRF-Dyn may be a well-designed recurrent SNN module, but the paper's central framing is not justified.

- **Theorems 1 and 2 are presented as mathematical derivations but are actually empirical observations.** The paper states that VSA attention weights follow α ∝ exp(-βΔ) and SSA weights follow α ∝ (α−βΔ)_+ as explicit theorems. These patterns are empirically observed on natural image data (due to spatial proximity correlating with content similarity), not necessary consequences of the attention mechanisms themselves. A theorem would need to derive these forms from first principles. The paper provides no such derivation. Theorem 2's entropy inequality additionally suffers from undefined notation (h(α_i), α_i used in two different roles) and its proof is deferred to the appendix without stating the assumptions.

- **No statistical significance or variance reporting for main results.** The accuracy improvements are modest (0.41%–1.24%) and reported as single runs with no standard deviations, confidence intervals, or number of seeds. On a 1,000-way classification task, sub-1% gains can easily fall within training noise. Without variance estimates, the reader cannot assess whether the reported improvements are statistically reliable. This is a standard expectation for papers making small-margin claims.

### Minor

- **The Fourier-domain formulation (Eq. 15) is introduced without explanation.** Section 5.3 presents an alternative formulation using Fourier transforms (F and F⁻¹), a kernel K(t) = ΓC Σ A, and a convolution, without explaining how this relates to the recurrent formulation in Eq. 12, which formulation is actually implemented, or what computational benefit it provides. This undermines reproducibility.

- **Table 2 has unclear comparison structure.** The LRF-SSA entry at 10.0M parameters shows +2.2% gain, but no baseline at 10.0M is shown (closest baselines are 5.1M at 33.6% and 18.99M at 41.3%). The reader cannot verify which baseline the +2.2% refers to. Additionally, LRF-Dyn is marked "Attn: ✗" (no attention), which appears inconsistent with the paper's own framing of LRF-Dyn as an attention mechanism.

- **No energy-efficiency or latency measurements.** The paper motivates the work by energy efficiency and edge deployment but provides no MAC/AC operation counts, energy estimates, wall-clock time, or inference throughput. The only concrete memory claim is the 49.4% reduction for one configuration; absolute memory consumption in MB/GB is not reported for any configuration.

- **"Causd SSA" baseline in Table 3 is undefined.** The ablation study compares against "Causd SSA" which is never defined. It achieves much lower accuracy (74.30%) than the w/o-LRF condition (77.86%), making the comparison difficult to interpret.

### Trivial

- Notation issues: Eq. 8 uses V^{jk} without defining j and k. Eq. 12 defines A ∈ ℝ^d as an element-wise decay factor, but Eq. 13 gives it a tridiagonal matrix structure of dimension n×n — the dimensional semantics are unclear. "n is set as 8" (line 156) likely refers to the number of dendrites d_n, but n also indexes token position elsewhere, creating confusion.

## Nice-to-Haves
- An analysis of approximation quality between LRF-Dyn and LRF-SSA (e.g., cosine similarity of attention outputs, error as a function of position) would substantially strengthen the claim that LRF-Dyn approximates attention.
- Comparison against linear-attention methods adapted for SNNs would contextualize the memory-reduction contribution.
- Reporting results with multiple random seeds (at least 3) with mean ± std.

## Removed Points
These points were flagged during review but are not included in the main weaknesses for the reasons stated below:

- **"LRF-Dyn does not compute self-attention at all"** — Overstated. Eq. 11 derives from the linear-attention formulation (q_n × accumulated KV), which is a recognized form of linear attention. The problem is that the transition to Eq. 12 is unexplained, not that the derivation starts from a non-attention baseline.
- **"QKFormer LRF-Dyn parameter count (16.44M) is lower than baseline (16.47M), suggesting recording error"** — Plausible if LRF-Dyn replaces Q/K/V projections with a cheaper recurrent module, saving more parameters than the added convolution costs. The paper states LRF-Dyn "eliminates the SSA computation."
- **"Missing related work on linear attention"** — Already cited (Katharopoulos, Choromanski, Shen) in Section 2.
- **"The performance gap could also be due to binarization through spiking neurons"** — The paper identifies one specific, testable factor (softmax removal) and provides empirical evidence for it. Multiple factors can contribute.
- **"LRF-Dyn should be compared against non-attentional SNN baselines"** — The paper includes CNN-based SNN baselines (SEWResNet, MSResNet) in Table 1, and LRF-Dyn is evaluated within the Transformer framework it is designed for.
- Generic/superficial strengths from Strength Finder removed: "the paper addresses an important problem," "novel neuronal-dynamics reformulation" (the novelty claim is undercut by the unclear derivation), "theoretical characterization" (these are the problematic Theorems).

## Novel Insights
The paper's key diagnostic insight — that SSA's local modeling deficiency can be quantified through attention-score distributions (entropy and Manhattan-distance concentration) — is genuinely useful for the Spiking Transformer community. The finding that SSA produces near-uniform attention distributions (H=0.5637 vs VSA's H=0.1777) provides clear empirical motivation for incorporating local bias, and this measurement methodology could generalize beyond this paper. The idea of auditing attention mechanisms through receptive-field analysis in SNNs is a methodological contribution.

## Suggestions
1. **Derive or reframe LRF-Dyn:** Either provide a clear mathematical derivation showing how Eq. 11 maps to Eq. 12, or abandon the claim that LRF-Dyn "approximates self-attention via neural dynamics" and reframe it as a recurrent SNN module inspired by the causal linear-attention formulation, evaluated on its own terms against appropriate baselines.
2. **Revise Theorems 1 and 2:** Rename them as empirical observations or lemmas with clear statements about the assumptions (e.g., "under the empirical observation that on natural images, nearby tokens have higher dot-product similarity..."). Do not present data-dependent patterns as mathematical theorems.
3. **Add variance estimates:** Report at least 3 seeds with mean and standard deviation for main results.
4. **Clarify or remove Eq. 15** (Fourier formulation) if it is not the implemented method.
5. **Fix Table 2:** Show the baseline at 10.0M parameters or clarify which comparison the +2.2% refers to. Define "Causd SSA" in Table 3.
6. **Report measured memory** in MB/GB for at least one configuration alongside percentage reduction.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>