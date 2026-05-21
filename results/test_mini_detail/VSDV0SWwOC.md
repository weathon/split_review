Now I have sufficient calibration data. Let me synthesize everything and write the final review.

**Calibration summary:**

Round 1 bracket: 4.5–6.5

Round 2 anchors:
- "Foldable SuperNets" (5.5, Reject) — similar problem (merging transformers with different initializations) but LS-Merge has more novelty (latent space vs. SuperNet extension of ZipIt)
- "Extend Model Merging / WIDEN" (5.67, Reject) — similar topic (LLM merging) but LS-Merge tackles a harder problem (cross-architecture) with more novel methodology
- "Language Model Merging in Iterative Preference Learning" (4.6, Reject) — LS-Merge is clearly stronger
- "ParamΔ" (6.5, Accept Poster) — cleaner validation, fewer unresolved questions
- "Probabilistic Token Alignment" (6.25, Reject) — also uses OT, but for token alignment rather than weight-space merging

LS-Merge is stronger than the rejected papers in the 4–5.5 range, comparable to WIDEN (5.67), but weaker than ParamΔ (6.5). The VAE reconstruction puzzle and thin heterogeneous evidence prevent a higher score.

Final score: **5.5**, Decision: **Reject**

---

## Summary

This paper proposes LS-Merge, a framework that encodes LLM weights into a latent space using a transformer-based VAE, performs merging (including linear interpolation and optimal transport alignment) in that latent space, and decodes back to weights. The key contribution is enabling cross-architecture merging — the method can merge models of different sizes and even different model families (e.g., LLaMA → Gemma). The paper includes experiments on self-merging, LoRA expert merging, comparison to representation-merging methods, and cross-architecture merging.

## Strengths

1. **First demonstration of cross-architecture LLM weight merging via a learned latent space (Section 4.4, Table 5, Figure 4a).** Prior weight-space merging methods require architectural homogeneity. LS-Merge shows that encoding weights into a common latent space and applying optimal transport alignment enables both intra-family (Gemma-4B→1B) and cross-family (LLaMA→Gemma) merging. This is a genuinely novel capability that opens a new direction for model composition.

2. **Consistent gains over weight-space baselines on LoRA expert merging (Table 3).** LS-Merge (soup) achieves the highest scores on 5 of 8 benchmarks (MMLU 56.0, HellaSwag 60.1, TruthfulQA 33.0, NLQGraph 56.1, AbstainQA 4.0), and LS-Merge (lerp) leads on GSM8k (28.1). These gains are consistent across diverse tasks and exceed Greedy Soup, SLERP, Dare-Ties, and Uniform Soup.

3. **Strong empirical demonstration that pretrained weights lie on a non-linear manifold, not a linear subspace (Section 5.3, Table 8).** PCA collapses to near-random accuracy at compression ratio 1.6× (MMLU 25.50%), while the VAE retains 96% of base model performance (39.89%) and even improves on Winogrande. This directly motivates the non-linear encoder design and is a clean ablation.

4. **Competitive with activation-based methods (Table 4).** LS-Merge outperforms Task Arithmetic on all five benchmarks and exceeds AIM on 3 of 5, despite operating purely on weights without requiring forward passes. This demonstrates that latent-space weight manipulation can match methods that use activations.

5. **Comprehensive component ablation (Table 6) and held-out generalization experiments (Table 7, Section 5.2).** The paper isolates MLP vs. attention contributions and shows that VAE trained on one model generalizes to unseen in-family and out-of-family models at low compression ratios.

## Weaknesses

### Fatal
None.

### Major

1. **VAE reconstruction of a single model outperforms the original model, which is unexplained (Table 2).** The VAE row in Table 2 exceeds the base model on multiple metrics (e.g., Gemma-3-4B-it: VAE 54.10 vs. base 53.10 on MMLU; Gemma-3-1B-it: 32.60 vs. 32.20). If the VAE is a lossy compressor of weights, its output should at best approximate — not improve upon — the original performance. The paper provides no explanation for this phenomenon (no denoising mechanism, no regularization effect). This undercuts the stated mechanism: the claim that latent-space interpolation operates on *reconstructions of the original models* is weakened if a single reconstruction already "improves" the model. The authors must either explain this (e.g., as a denoising property with supporting evidence) or show that it is within evaluation noise.

2. **Heterogeneous merging evidence is too thin to support the headline claim (Section 4.4, Table 5, Figure 4a).** Cross-architecture merging is presented as a core contribution, but:
   - Table 5 reports only 3 tasks (WinoGrande, ARC-C, HellaSwag) with a single interpolation coefficient (λ = 0.1). No error bars are reported.
   - Figure 4a shows a bar chart without numerical values printed, making precise assessment difficult.
   - The gains over the base model are small (e.g., WinoGrande 56.83 → 57.75; HellaSwag 49.07 → 50.10).
   - No demonstration that the merged model combines capabilities from both source models (e.g., merging a reasoning-specialized model with a knowledge-specialized model and showing gains on a combined task set).
   - The paper should report multiple λ values, include error bars over multiple runs, evaluate on more tasks, and directly test whether both source models contribute distinct capabilities.

3. **Optimal transport alignment relies on an unvalidated Gaussian approximation (Section 3.3).** The closed-form affine OT map is derived under the assumption that each layer's latent distribution is approximately Gaussian. The paper does not check whether this assumption holds — and Figure 3 shows latent clusters, not Gaussian-like blobs. No quantification of the approximation error is provided. Since OT alignment is critical for heterogeneous merging (alleged to be the enabler), this is a material gap.

### Minor

4. **VAE training data overlaps with evaluation models (Sections 4.1–4.3).** The VAE is trained on weight snapshots of the same models that are later merged or evaluated. In Section 4.3, the VAE is "trained on the combined weights of all constituent models." While this is standard for autoencoders (training on the data you reconstruct), the comparison to weight-space baselines (which have no analogous training phase) is somewhat asymmetric. The paper partly addresses this through held-out generalization experiments (Section 5.2, Table 7) showing the VAE works on unseen models, but explicitly re-running the main merging experiments with a VAE trained on *disjoint* checkpoints would eliminate this concern.

5. **Self-merging experiment lacks key implementation details (Section 4.1).** The paper states "sample multiple latent codes from its posterior distribution" but does not specify how many samples are drawn, how the codes are merged (averaged?), or what the merging procedure is. This hinders reproducibility.

6. **Greedy Soup baseline tuning is not controlled (Section 4.2).** The paper notes Greedy Soup "is highly sensitive to initialization" but does not report any tuning effort. The comparison is therefore not fully controlled.

7. **Table 2 reports ±0.00 variance for some LS-Merge entries**, which is implausible for a single evaluation run and suggests either a reporting issue or a deterministic evaluation that should be clarified.

### Trivial
- The PCA explained-variance plots (Figure 2) show a gradual decline after the first component rather than a "sharp decline" as claimed in the text — the wording is slightly overstated.
- The theoretical compressibility bound (O(d/ε² log(V/τ))) in Section 3.1 is cited but never instantiated — it adds surface rigor without substance and could be trimmed.

## Nice-to-Haves
- Report weight-space reconstruction error (e.g., MSE or cosine similarity between original and reconstructed weights) to directly validate VAE fidelity.
- For heterogeneous merging, merge a model strong on reasoning (e.g., a math fine-tuned model) with one strong on knowledge and demonstrate compositional benefit on a combined task set.
- Report training cost (GPU hours, memory) to substantiate the "scalable" claim.
- Show multiple λ values with error bars for cross-architecture merging results.

## Removed Points
- **"Training data leakage invalidates the expert merging comparison"** (Harsh Critic #1, framed as fatal): Demoted to Minor (#4 above). The VAE is an autoencoder; training on the data it needs to encode is standard. The held-out generalization results (Table 7) show it works on unseen models, which would not be possible if the VAE simply memorized. The comparison asymmetry is real but not fatal.
- **Reproducibility concerns about missing appendix content** (Harsh Critic "Reproducibility" section): Removed per instructions — the appendix section is stripped by the parser; it exists in the original submission.
- **"PCA conclusion is too strong"** (Harsh Critic, Section 5.3): The paper's claim that "the set of valid pretrained weights does not reside in a linear subspace" is well-supported by the PCA collapse at ratio 1.6×, which is strong evidence. The claim is proportional to the evidence.
- **Strength Finder generic strengths** ("detailed weight distribution analysis," "comprehensive ablation"): Kept where they have specific quantitative backing; generic framing dropped.
- **Nitpick about "sharp decline" phrasing in Figure 2**: Moved to Trivial.
- **Missing related works**: Removed per instructions — no external sources to confirm existence.
- **Formatting/style nitpicks**: Removed per instructions (parser artifacts).

## Novel Insights

The reviews point to a subtle but important tension in the paper: the VAE reconstruction outperforming the original model (Table 2) directly contradicts the stated mechanism of "encode → interpolate → decode" as a faithful reconstruction pipeline. If a single VAE pass already improves the model, then either (a) the VAE is not a compressor but a denoiser/improver (requiring a different framing), or (b) the evaluation has variance high enough that the improvements are not significant (requiring statistical rigor). Either way, the paper's core explanatory chain — that latent interpolation works because it operates on faithful reconstructions — is weakened. This is an unusual artifact that deserves deeper investigation rather than being left unremarked. Additionally, the heterogeneous merging results, while pioneering, would be much more convincing if they showed compositional benefit (both source models contributing distinct skills) rather than small absolute gains on general benchmarks.

## Suggestions

1. Explain why the VAE reconstruction outperforms the original model in Table 2, or demonstrate that the differences are within measurement noise.
2. Strengthen the heterogeneous merging evaluation: more tasks, multiple λ values, error bars, and a compositional-benefit experiment (merge models with complementary specializations).
3. Validate the Gaussian assumption underlying the OT alignment, or use a non-parametric OT solver and compare.
4. Re-run the main merging experiments with a VAE trained on a disjoint set of checkpoints to fully eliminate training-data-overlap concerns.
5. Provide exact implementation details for self-merging (number of samples, how codes are combined) and report computational costs.

## Score and Decision

**Calibration procedure:**

**Round 1 bracketing** — queries on "latent space model merging VAE parameter encoding for LLMs" with score filters:
- Weak band (< 3.5): returned "Conditional LoRA Parameter Generation" (3.4), "Collective Model Intelligence" (3.4), etc.
- Middle band (3.5–7.5): returned "ParamΔ" (6.5), "Few-shot Style-Conditioned LLM" (4.25), "A Codespace Autoencoder" (4.0)
- Strong band (> 7.5): returned papers on different topics (sparse autoencoders, Bayesian optimization)

Initial bracket: 4.5–6.5.

**Round 2 narrowing** — queries on "model merging latent space parameter interpolation LLM" with tighter filters:
- 4.0–6.0: "Foldable SuperNets" (5.5, Reject), "Extend Model Merging / WIDEN" (5.67, Reject), "Iterative Preference Learning Merging" (4.6, Reject)
- 6.0–7.5: "ParamΔ" (6.5, Accept Poster), "REMEDY" (6.25, Accept Poster), "Safety-Aware Subspace" (7.0, Accept Poster), "Probabilistic Token Alignment" (6.25, Reject)

**Anchor comparisons:**
- vs. **Foldable SuperNets (5.5)**: LS-Merge is more novel (latent-space paradigm vs. SuperNet extension of ZipIt) but has more unresolved questions (VAE reconstruction puzzle, thin heterogeneous evidence). Comparable quality overall.
- vs. **WIDEN (5.67)**: Both address LLM merging challenges. LS-Merge tackles a harder problem (cross-architecture) but WIDEN has cleaner evaluation. Slightly weaker due to unresolved VAE issue.
- vs. **ParamΔ (6.5, accepted)**: ParamΔ's idea is simpler and its evaluation cleaner; it has no unexplained artifacts. LS-Merge is more technically ambitious but less cleanly validated. Weaker than ParamΔ.
- vs. **Iterative Preference Learning Merging (4.6)**: LS-Merge is substantially stronger in novelty, scope, and experimental breadth.

**Final score:** LS-Merge is above the 4.6–5.0 reject-level papers, comparable to the 5.5 reject-level papers, but below the 6.5 accepted papers. The core idea is novel and interesting, but the unexplained VAE reconstruction behavior and thin heterogeneous merging evidence are significant gaps. Concretely: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>