## Summary

LS-Merge proposes encoding LLM weights into a learned latent space via a transformer VAE, performing model merging operations (interpolation, soup) in that latent space, and decoding back to weight space. The method uses OT-based alignment to enable cross-architecture merging between models with different depths, widths, and families. The VAE is trained with a two-stage curriculum to handle the heavy-tailed weight distributions characteristic of LLMs. Experiments span self-merging, LoRA expert fusion, and cross-family (Gemma ↔ LLaMA) merging, with ablations demonstrating the necessity of non-linear encoding (PCA collapses to random) and the complementarity of MLP and attention layer merging.

---

## Strengths

- **Weight distribution analysis motivates the encoder design.** Section 3.1 and Table 1 document that LLM weights exhibit high kurtosis (up to ~15 for Gemma-3-1B-it self-attention layers), contradicting Gaussian assumptions in prior work. This directly justifies the heavy-tail-aware two-stage curriculum in Section 3.2.

- **PCA vs. VAE ablation is decisive.** Table 8 shows that PCA-reconstructed models collapse to near-random MMLU accuracy (~25.5%) even at mild compression (r=1.6), while the VAE preserves 96% of base performance (39.89% vs. 41.44%). This cleanly demonstrates that pretrained weights lie on a non-linear manifold, making non-linear encoding a geometric necessity, not a stylistic choice.

- **Component ablation reveals complementary subspaces.** Table 6 shows that merging MLP-only yields modest gains, attention-only degrades performance, while merging both achieves the best results (MMLU 42.10 vs. MLP-only 41.02 vs. attention-only 39.80). This supports the claim that the encoder captures distinct, co-adapted functional knowledge across submodules.

- **Latent-space merging consistently outperforms weight-space baselines in expert fusion.** Table 3 shows LS-Merge (soup) achieving 56.0 MMLU vs. Greedy Soup's 50.8, and 60.1 HellaSwag vs. best expert's 46.6, across 8 benchmarks with 10 LoRA experts on Gemma-7B-it.

- **Zero-shot VAE generalization to unseen architectures.** Table 7 shows a VAE trained solely on Gemma-3-4B-it reconstructs Gemma-3-1B-it (same family) and LLaMA-3.2-1B-it (different family) with minimal performance loss at r=1.6, demonstrating transferable weight representations.

---

## Weaknesses

### Fatal

None.

### Major

- **Training-data overlap between VAE and merged models weakens the core comparison.** In the expert merging experiment (Table 3, Section 4.2), the training data explicitly "consist of … LoRA experts from Feng et al. (2024b)" — the same 10 experts that are later merged. Similarly, for the Llama-2-13B comparison (Table 4, Section 4.3), "a single VAE [is] trained on the combined weights of all constituent models." The VAE can therefore overfit to the specific weight patterns of the models it will later encode, giving the latent-space interpolation an advantage over weight-space baselines (Uniform Soup, SLERP, Greedy Soup, DARE-Ties) that receive no per-model training. While the VAE is trained for reconstruction, not merging, and the generalization experiment in Table 7 partially mitigates this concern, the head-to-head comparison in the paper's central result tables remains confounded. A clean evaluation would train the VAE on a disjoint set of models and then perform merging on held-out checkpoints. Without this, the reported gains over training-free baselines cannot be confidently attributed to the latent-space paradigm rather than to the VAE having seen the models during training.

### Minor

- **Cross-architecture evidence is limited in scale.** The heterogeneous merging results (Section 4.4) use only one cross-family pair (LLaMA-3.2-1B → Gemma-3-1B-it) and the improvements, while positive, are modest (+0.92 WinoGrande, +0.56 ARC-C, +1.03 HellaSwag in Table 5). The intra-family result (Gemma-3-4B → Gemma-3-1B) is shown only as bar charts (Figure 4) without numerical values in the main text. The evidence is too narrow to fully support the claim of enabling "robust cross-scale and cross-family model merging for the first time."

- **Heterogeneous mapping mechanism is underspecified.** Section 3.3 describes a "proportional mapping" that rescales source latents from n_s layers to n_t layers using a ratio r = n_t·N/(n_s·M), but the concrete mechanism (interpolation, pooling, learned projection) for going from n_s to n_t layer representations is not described. Algorithm 1 line 4 simply states "Proportional mapping to fixed d: obtain Z_src, Z_tgt." Without this detail, the heterogeneous merging pipeline is not fully reproducible.

- **SLERP baseline uses t=0.45 without justification.** Table 3 reports SLERP(t=0.45). No description of how this coefficient was selected (grid search, validation set tuning, or fixed convention) is provided. This matters because SLERP performance is sensitive to the interpolation coefficient, and the comparison would be stronger with either a systematic sweep or an automated selection method described.

### Trivial

- Standard deviations of exactly 0.00 for some LS-Merge entries in Table 2 (Gemma-3-4B-it: MMLU 54.20±0.00, HellaSwag 50.10±0.00) are likely a rounding artifact but give the appearance of suppressed variance, which is incongruent with a method that involves sampling multiple latent codes.

---

## Nice-to-Haves

- Merging experiments using the *transferred* VAE from Table 7 (trained on 4B, applied to 1B models) would directly address the training-overlap concern and demonstrate whether latent-space merging works in a truly zero-shot setting.
- A cost analysis comparing VAE training overhead against the cost of weight-space merging or activation-based methods (AIM) would help readers assess practical trade-offs.
- Expanding cross-architecture evaluation to additional model pairs (e.g., different LLaMA sizes, Qwen, Mistral) and reporting numerical values for the intra-family setting would substantially strengthen the heterogeneous merging claims.
- A systematic sweep or validation-driven selection for the SLERP interpolation coefficient would make the baseline comparison fairer.

---

## Removed Points

*These points from the input reviews were considered but excluded from the final review for the reasons stated. Treat them with caution.*

- **"Gaussian prior contradicts heavy-tailed data" (Harsh Critic Claim 4).** REMOVED. Using a Gaussian prior in a VAE is standard practice regardless of data distribution; the decoder can learn to map Gaussian latents to heavy-tailed outputs. This is not a methodological contradiction.

- **"OT only degrades performance relative to base, contradicting the claim that OT is necessary" (Harsh Critic Claim 2, partially).** REMOVED. Table 5's "OT only" row (51.13 vs. base 56.83 WinoGrande) is an ablation showing that OT alignment *without interpolation* is insufficient — the paper's claim is that *OT + interpolation* is necessary, which is exactly what "OT + interp." (57.75) demonstrates. The critic misread the experiment's purpose.

- **"Comparison does not include a straightforward baseline such as simply using the target model alone" (Harsh Critic Claim 2, partially).** REMOVED. Table 5 includes a "Base" row (Gemma-3-1B-it: 56.83 WinoGrande, 42.78 ARC-C, 49.07 HellaSwag) which is exactly the target-model-alone baseline.

- **"PCA comparison doesn't clarify whether applied per-layer or globally" (Harsh Critic Section note).** REMOVED. Trivial implementation detail; the key finding (PCA collapses, VAE preserves) is robust regardless of this specification.

- **"No merging experiments with transferred VAEs" (Harsh Critic Section note).** MOVED to Nice-to-Haves. This is a suggestion to strengthen the paper rather than a flaw in existing experiments. The generalization results in Table 7 already provide relevant evidence; merging experiments with those transferred VAEs would be valuable but are not required to validate the current claims.

- **"The paper does not discuss the relative computational cost of training the VAE versus obtaining the activations needed by AIM" (Harsh Critic Section note).** MOVED to Nice-to-Haves. This is a practical consideration, not an evaluation flaw. The method's value does not hinge on being cheaper than AIM.

---

## Novel Insights

None beyond the paper's own contributions. The most striking finding — that linear PCA reconstruction of LLM weights collapses to chance-level functional performance even at mild compression ratios, while a non-linear VAE preserves near-original accuracy (Table 8) — is the paper's own discovery and a genuinely useful empirical result for the weight-space learning community.

---

## Suggestions

- The single most impactful revision would be to retrain the VAE on a *disjoint* set of models (e.g., train on 7B models, merge 1B/3B/4B checkpoints) and rerun the key merging experiments (Tables 3, 4) with this held-out VAE. This would simultaneously address the major weakness and strengthen the paper's core empirical claim.
- Provide pseudo-code or a detailed prose description of the proportional mapping step that converts between n_s and n_t layer latents, including whether it uses interpolation, pooling, or a learned projection.
- Report the SLERP coefficient selection method and ideally include a sweep or validation-based selection.
- Add numerical results (not just bar charts) for the intra-family heterogeneous merging experiment (Figure 4a) in a table format.

---

## Score and Decision

### Calibration Summary

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| `kVcEiWtld9` (Latent Interpolation VAE) | 4.25 | R1 | Similar approach (VAE for weight latent interpolation) but far weaker: single architecture, missing details, ad-hoc filtering. LS-Merge substantially stronger. |
| `LJGY2GVcit` (Foldable SuperNets) | 5.50 | R2 | Merges transformers with different initializations, varying widths. Limited novelty (extends ZipIt), narrow experiments. LS-Merge has broader scope and more compelling ablations. |
| `2pvMZKGYDR` (WIDEN) | 5.67 | R1/R2 | Weight disentanglement for FT+PT merging. Good motivation but limited model diversity, weak FT performance. LS-Merge is moderately stronger — more diverse experiments, more novel approach, but shares some evaluation limitations. |
| `ksBhCsSUaE` (PTA-LLM) | 6.25 | R2 | Uses OT for token alignment in LLM fusion. Novel but marginal improvements (~0.5 pts), limited architectures. LS-Merge has larger empirical gains but the training-overlap concern clouds direct comparison. |
| `vqbd2OQnGp` (Parameters Fusing) | 6.50 | R2 | Simpler approach (parameter delta fusion for post-training), clean evaluation. Accepted. LS-Merge is more novel but has a more significant evaluation caveat. |
| `FrFQpAgnGE` (Unified Representation) | 7.00 | R2 | Discovery paper about representation spaces. Different contribution type. LS-Merge falls below this in evidential strength. |

**Round 1 bracket:** 5.5 – 7.5

**Round 2 narrowing:** The paper is stronger than the 5.5–5.67 anchors (Foldable SuperNets, WIDEN) — it has more novelty, better ablations, and more diverse experiments. However, the training-overlap issue prevents it from reaching the clarity of the 6.5–7.0 accepted anchors. Compared to PTA-LLM (6.25, rejected), LS-Merge shows more substantial empirical gains but shares a concern about whether the improvements are fully attributable to the proposed mechanism. The paper sits at **6.0**: a genuinely novel contribution with strong motivation and informative ablations, held back by a significant but addressable evaluation concern in its main experimental results.

### Evaluation Axes

- **Originality:** High. Latent-space model merging is a genuinely new direction that departs from weight-space and activation-based paradigms.
- **Importance:** High. Enabling architecture-agnostic merging would substantially broaden the applicability of model merging.
- **Claims supported:** Moderate. The core claims are supported by consistent empirical trends, but the training-overlap issue means the comparison against weight-space baselines is not as clean as presented.
- **Soundness:** Moderate. The methodology is generally sound, but the heterogeneous mapping is underspecified, and the training-overlap confound weakens the central experiments.
- **Clarity:** Good. The paper is well-structured and the motivation is clear, though some technical details (proportional mapping, VAE architecture) are deferred.
- **Value to community:** Moderate-High. The framework opens a new research direction, and the PCA-vs-VAE ablation is of independent interest.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>