## Summary
The paper proposes LRF-Dyn, a modified self-attention mechanism for Spiking Transformers that (1) augments Spiking Self-Attention (SSA) with local dilated convolutions (LRF-SSA) to close the locality gap between SSA and vanilla self-attention (VSA), and (2) reformulates the attention computation through charge-fire-reset neuronal dynamics (LRF-Dyn) to eliminate explicit attention-matrix storage and reduce memory from O(d²) to O(kd). Experiments on ImageNet-1K and ADE20K across three spiking transformer backbones consistently show performance gains (+0.44%–+1.24% top-1) alongside a 49.4% measured memory reduction.

---

## Strengths

- **Consistent, cross-architecture performance improvements with negligible parameter cost.** Table 1 shows LRF-SSA and LRF-Dyn improve accuracy on Spikformer, QKFormer, and SDT-V3 (e.g., +1.24% on Spikformer-8-512, +0.92% on SDT-V3-S, +0.48% on QKFormer-10-512) while adding at most 0.26M parameters. The pattern holds on ADE20K segmentation (+2.6%/+2.2% mIoU on SDT-V3), making the contribution genuinely plug-and-play.

- **Well-motivated and empirically grounded locality analysis.** Figure 2 provides a concrete quantitative diagnosis: 76.68% of VSA attention concentrates within Manhattan distance ≤5, while only 20.31% does for SSA; VSA entropy is 0.177 vs. SSA's 0.564. This is the strongest piece of evidence in the paper and directly motivates LRF-SSA.

- **Demonstrated memory reduction.** Table 1 reports O(kd) storage complexity for LRF-Dyn variants, and Section 6.2 / Figure 5(b) reports a 49.4% measured memory reduction on Spikformer-8-512 without a corresponding accuracy drop (74.51% vs. 74.62% for LRF-SSA). This directly validates the paper's claim that the dynamics reformulation is practically effective.

- **Ablation study validates both components.** Table 3 shows monotonic improvement as LRF kernel count increases for both LRF-SSA and LRF-Dyn (77.86% → 78.64% and 77.78% → 78.57% on CIFAR-100, respectively), and LRF-Dyn consistently outperforms causal SSA at every kernel setting (78.16% vs. 75.30% at Ω≤1), confirming that the neuronal dynamics module contributes beyond the causal conversion alone.

---

## Weaknesses

### Fatal
None.

### Major

- **The causal conversion in Eq. 11 lacks justification for spatial vision tasks.** The transition from $\sum_{j=1}^{N}$ (full attention) to $\sum_{j=1}^{n-1}$ (causal, left-to-right) in Eq. 11 is presented as a memory-reducing reformulation, but it is a structural change that discards information from all tokens following position *n*. For image patches that have no intrinsic sequential ordering, this is a non-trivial semantic change. The paper (Section 5.2) says "LRF-SSA can be reformulated through causal inference to significantly reduce memory consumption," but provides no argument for why a unidirectional pass is a valid approximation for spatial (non-sequential) features. The empirical ablation shows Causal SSA at 74.30% vs. LRF-SSA at 77.86% w/o LRF, suggesting the causalization alone does lose ~3.5% — and while LRF-Dyn recovers this to 77.78%, the mechanism behind this recovery is not explained. The paper should justify or analyze why causal processing is sufficient for image understanding.

- **Primary motivation (energy efficiency) is not measured.** The abstract, introduction, and conclusion consistently frame energy efficiency as the central rationale ("balance energy efficiency and performance," "key unit for achieving energy-efficient Spiking Transformers," "resource-constrained devices," "neuromorphic chips"). Yet the paper measures only memory complexity as a proxy. The LRF-SSA module introduces additional dilated convolution operations, and LRF-Dyn introduces Fourier-domain convolutions (Eq. 15); whether the net effect is energy-neutral or beneficial is never assessed. At minimum, reporting synaptic operation counts (SOPs), which is standard in the SNN literature (e.g., used in the cited SDT-V3 and Spikformer papers), would partially close this gap.

- **The derivation from dendritic A matrix (Eq. 13) to Fourier implementation (Eq. 15) is not established in the main text.** Eq. 13 introduces an n×n matrix A encoding multi-dendritic dynamics, but Eq. 15 jumps directly to a Fourier convolution $\mathcal{F}^{-1}\{\mathcal{F}(\mathbf{K}) * \mathcal{F}(\mathbf{X})\}$ with kernel $\mathcal{K}(t) = \Gamma C \sum_{m=1}^{n-m} \mathcal{A}$. The algebraic path from Eq. 13 to Eq. 15 is entirely absent from the main body. The O(kd) memory claim, which is central to the paper's contribution, depends on this step being correct — readers cannot verify it from the main text alone.

### Minor

- **Theorems 1 and 2 are largely tautological given their assumptions.** Theorem 1 defines LRF-SSA as a $(1-\lambda)$-$\lambda$ mixture of VSA and local-receptive-field weights, then derives $\mathbb{E}[\Delta_\text{lrf-ssa}] = (1-\lambda)\mu_\text{ssa} + \lambda\mu_r$ — this is linearity of expectation applied directly to the definition. Theorem 2 applies entropy concavity to a mixture. More substantially, the assumed form $\alpha_{ij}^{ssa} \propto (\alpha - \beta\Delta)_+$ (linear distance decay) is never derived from the actual SSA mechanism in Eq. 5, which involves binary spike inputs. The empirical finding in Fig. 2 is compelling on its own; the theorems add formal notation but little analytical insight.

- **The performance gap between Causal SSA (74.30%) and LRF-Dyn w/o LRF (77.78%) in Table 3 is unexplained.** This ~3.5% gap suggests that the neuronal dynamics formulation of LRF-Dyn recovers accuracy relative to a naive causal conversion, but the paper does not analyze *why*. Understanding this mechanism would significantly strengthen the paper's core narrative.

- **Table reference inconsistency.** Section 6.1 states "As shown in Table 4, the proposed LRF-SSA method consistently delivers performance improvements," but the relevant table is labeled Table 1 in the paper.

### Trivial
None beyond the parser-introduced formatting artifacts.

---

## Nice-to-Haves

- Report Synaptic Operation counts (SOPs) for LRF-SSA vs. LRF-Dyn vs. baseline SSA to connect memory savings to energy, which is the stated deployment goal.
- Provide an analysis of how approximation quality (accuracy gap between LRF-SSA and LRF-Dyn) varies with sequence length N and model dimension d, to validate claims about edge deployment scalability.
- Report standard deviation across seeds for CIFAR-100 ablations (Table 3), where gains of 0.3–0.4% could plausibly be seed-level noise.
- Analyze sensitivity to dendrite count k beyond the default k=8 to characterize the accuracy–memory trade-off curve.

---

## Removed Points

*These points are flagged as removed. Treat them with caution.*

- **Figure 1 caption contradiction (Harsh Critic, Section 4.1).** The critic claimed an internal contradiction: "VSA captures only limited and local relation" in the caption vs. description text. Upon reading, both captions consistently describe VSA as capturing *localized* (limited to local region) attention — this is not a contradiction but a description of VSA's focused, local scope. Removed as factually incorrect criticism.

- **Missing acknowledgment of RWKV/RetNet/SSMs.** Critic noted the Fourier convolution in Eq. 15 with learned kernel is similar to existing linear recurrent models. Removed per the hard rule against missing related work criticism (we cannot confirm which works should have been cited).

- **Conflation of N² vs. d² SSA variants (Harsh Critic, Section 4.2).** Critic claims the paper conflates two SSA versions. The paper explicitly focuses on the O(d²) KV-product regime as the target, which is clear from Eq. 7 onward. The distinction between the two regimes is acknowledged in Fig. 1(b). Not a genuine weakness.

- **Reproducibility nitpick: undisclosed hyperparameters for training A matrix.** "Trained efficiently following (Chen et al., 2024)" was flagged. This cites an existing method for the training procedure. Removed as a reproducibility nitpick referencing a cited work.

- **"Statistical variance" request for ablations.** Flagged as nice-to-have rather than a substantive weakness.

- **Strength Finder: "Theoretical justification for locality and low-entropy."** Retained in weakened form; moved the strong framing to Minor given the circular nature of Theorems 1 and 2 identified above.

---

## Novel Insights

The most technically interesting finding, which the paper underemphasizes, is visible in Table 3: naive Causal SSA achieves only 74.30% on CIFAR-100, while LRF-Dyn *without* LRF achieves 77.78% — a 3.48% recovery from the neuronal dynamics formulation alone. This suggests the dendritic/Fourier reformulation is not merely an approximation of causal attention but introduces beneficial inductive biases (e.g., multi-timescale decay via the A matrix) that partially compensate for the loss of bidirectional token interaction. If this mechanism were analyzed explicitly, it could constitute a novel insight about why biologically motivated recurrent formulations might be advantageous even for static image tasks.

---

## Suggestions

1. **Add a paragraph in Section 5.2 deriving the algebraic path from Eq. 13 to Eq. 15**, showing how the dendritic A matrix leads to the Fourier convolution representation, and provide the O(kd) memory derivation explicitly.
2. **Add SOP measurements** alongside memory comparisons in Table 1 or a new table to substantiate the energy efficiency motivation.
3. **Justify the causal conversion** for spatial (non-sequential) inputs in Section 5.2, or reframe the contribution as "a causal approximation that is empirically effective with LRF compensation."
4. **Expand ablation Section 6.3** with a paragraph explaining the Causal SSA → LRF-Dyn gap (74.30% → 77.78% w/o LRF), connecting it to the dynamics of the A matrix.
5. **Fix the Table reference** in Section 6.1 (Table 4 → Table 1).

---

## Evaluation on Key Axes

- **Originality**: Moderate. The LRF idea applied to SSA is novel and practical. The dynamics reformulation borrows from existing biologically-inspired recurrence literature but applies it in a new context.
- **Importance**: Moderate-high. Memory and performance are real deployment barriers for spiking transformers; the plug-and-play nature of the solution is practically valuable.
- **Claims supported**: Partially. Performance improvements and memory reduction are well-supported. Energy efficiency, the central stated motivation, is not directly measured.
- **Soundness of experiments**: Mostly sound. Three architectures, two tasks, ablations. Main gap is the missing energy measurement and the underanalyzed causal conversion.
- **Clarity of writing**: Adequate but with a notable gap in the derivation between Eq. 13 and Eq. 15, and the table label error.
- **Value to research community**: Moderate. The plug-and-play component and empirical locality analysis of SSA are directly usable by the SNN community.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>