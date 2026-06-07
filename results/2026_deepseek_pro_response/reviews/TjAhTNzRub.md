Now I have a strong calibration set. Let me finalize.

**Round 1 bracket:** MoRE sits between ~5.0 and ~7.0 — clearly above SUN (4.00) and Deep Unlearning (5.25), competitive with the 6.0 cluster.

**Round 2 narrowing:** Compared against NegMerge (6.00, Reject — incremental method) and Image-to-Image Generative Unlearning (6.00, Accept — narrower scope), MoRE has more technical novelty than NegMerge, broader evaluation than the I2I paper, and a genuinely elegant method. The "irreversible" overclaim is its main drag. This puts MoRE at **6.0** — solid accept, with framing revision needed.

---

## Summary
MoRE (Mixture of Remapping Experts) is a training-free framework for feature-level machine unlearning. It combines three innovations: (i) prototype-orthogonal projection to decorrelate forget and remain prototypes before erasure, preserving remain utility; (ii) remapping forget prototypes into multiple remain prototypes via a mixture-of-experts architecture, scattering forget features to impede recovery; and (iii) activation-mean prototypes for O(Nd) compute and O(dk) memory. Experiments across CIFAR-10/100, Tiny-ImageNet, ImageNet, and Stable Diffusion show MoRE achieves near-zero forget accuracy while preserving remain accuracy, with substantially stronger resistance to linear-probe-based recovery than all baselines including retrain-from-scratch.

## Strengths
- **Strong KR results**: Under the Knowledge Retention evaluation (Table 1), MoRE keeps forget recovery accuracy near random-guessing levels (0.07% on CIFAR-100, 0.50% on Tiny-ImageNet), decisively below all baselines including ESC, ESC-T, and Retrain (which recovers to 57–78%). This is the paper's most compelling empirical evidence.
- **PO projection is well-motivated and validated**: Figure 3 quantifies the core problem—cosine similarities between forget and remain prototypes reach 0.77 on CIFAR-10. Table 3's ablation cleanly isolates PO's contribution: without it, erasure leaves 14.38% forget accuracy and remapping harms remain accuracy; with PO, both achieve near-perfect forgetting while preserving remain accuracy (99.87–99.94% D_r).
- **Clear mathematical derivation**: The progression from erasure (Eq. 5) to remapping (Eq. 6), with the complement-space skip connection (Eq. 4), is logically structured. The SVD-based pseudoinverse in Eq. 2 is a thoughtful numerical choice over the normal-equation form.
- **Compelling qualitative evidence**: t-SNE visualizations (Fig. 1) show a clear progression—ESC leaves forget features as a distinct cluster, Remap merges them into a remain cluster, and MoRE scatters them across the entire latent space. Figure 6 further confirms that remain prototype autocorrelations stay near 1.0 post-unlearning while forget prototype correlations are redirected as intended.
- **Computational efficiency is concretely demonstrated**: Figure 5 shows MoRE completes unlearning in ~9.5 seconds using ~540 MB GPU memory, orders of magnitude faster than training-based methods.
- **Sensitivity analyses show robustness**: Performance is stable across target class choices (Table 5), expert counts (Fig. 7), and router designs (Table 6), indicating the method is not brittle to hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major
- **"Irreversible" is a significant overclaim that pervades the paper**: The term appears in the title, abstract, introduction, method section, and conclusion. Yet the only evidence for irreversibility is the KR metric—linear probing at a single learning rate (lr=0.1). Resisting one recovery method at one hyperparameter does not establish irreversibility. A determined adversary could try stronger attacks (different learning rates, adversarial fine-tuning, model inversion). The method demonstrably makes recovery substantially harder than baselines—which is a real contribution—but "irreversible" promises more than the evidence supports. The paper should replace this language with precise, defensible terms (e.g., "recovery-resistant," "substantially harder to reverse") and acknowledge what stronger forms of irreversibility would require.

### Minor
- **Complement-space information is preserved without analysis of the risk**: Equation (4) deliberately retains all information outside the k-dimensional prototype span via the (I−PD)z term. Since k (e.g., 10 classes) is much smaller than d (feature dimension), most of the feature space is complement space. The paper presents this as a virtue for utility but does not discuss whether forget-related signal surviving there could be exploited. The KR results partially address this (linear probing operates on full features and shows low recovery), but the paper should explicitly acknowledge this design trade-off.

- **Random data forgetting results are under-explained**: The paper remaps forget prototypes to same-class remain counterparts, which should be nearly identical, making the remapping close to an identity transformation. No mechanistic explanation is offered for why this produces an unlearning effect. Moreover, Table 4 reports only "Remap" (single expert), not the full MoRE with multiple experts, yet the text discusses "MoRE." An ablation isolating whether remapping or PO projection drives the MIA improvement would clarify the mechanism.

- **Diffusion model evaluation is preliminary**: Only two artists (Van Gogh, Kelly McKernan) are evaluated. While LPIPS_d favors MoRE (0.25–0.26), MoRE has worse LPIPS_r (remain distortion, 0.07–0.08) than UCE (0.03–0.05). The "no architecture-specific adaptation" claim is overstated—the method was adapted to cross-attention layers with tokenized prompts as prototypes. This is a promising but thin result.

### Trivial
- The "constant memory" claim (line 83) conflicts with the reported 540 MB GPU memory being higher than ESC's 491 MB. The intended meaning is asymptotic scaling (O(dk)), which should be stated explicitly.
- Table 1 does not report variance/confidence intervals for the main results, unlike later tables (Tables 5–7 include std).

## Nice-to-Haves
- An experiment measuring forget-class signal in the complement space (training a linear probe on full post-unlearning features) would directly test the complement-space vulnerability.
- Testing KR at multiple learning rates (not just lr=0.1) would better characterize recovery resistance.
- Testing with larger forget fractions (e.g., 50% of classes) would probe method limits.
- A baseline using random projections or Gaussian noise added to features would test whether remapping specifically drives the KR suppression (as opposed to any feature perturbation).

## Removed Points
*These points were flagged by reviewers but are removed from the final review with justification.*

- **Missing related works**: Removed per hard rule (DO NOT mention missing related works — we lack external sources to confirm their relevance).
- **Appendix-related criticisms**: Removed per hard rule (appendix is stripped by the parser; it exists in the original submission).
- **Baselines Finetune/NG collapsing (D_r ≈ 0)**: These are known weak baselines in this setting. MoRE's decisive advantage over strong baselines (Retrain, ESC, ESC-T) matters. Not a standalone weakness.
- **t-SNE hyperparameters not reported**: Minor presentation detail; moved to Trivial tier as a general note about reporting reproducibility.
- **"The method needs a forward pass over the remain set, qualifying the claim of only needing forget data"**: The paper never claims to need only forget data—it explicitly computes prototypes for all classes. This criticism is factually wrong.
- **"The paper should compare against adding Gaussian noise or random projections"**: Moved to Nice-to-Haves; this is a useful ablation suggestion, not a weakness.
- **"No comparison against other feature-space unlearning methods beyond ESC"**: Removed (missing related work rule + scope creep; the paper positions itself as building on ESC and compares against a wide set of baselines).
- **"The claim of exact feature-level unlearning is misleading"**: The harsh critic mentioned this once in passing but it overlaps with the "irreversible" framing issue already captured in Major. Merged.
- **"The stochastic vs conditional router discussion could be expanded"**: The paper provides Appendix D (stripped) with details. Not a weakness given what's in the main text.

## Novel Insights
The paper's key insight—that the residual cohesive-separable structure of forget features after subspace erasure is what makes unlearning reversible, and that scattering forget features across multiple remain prototypes via a mixture-of-experts architecture breaks this structure—is genuinely novel and well-supported. The prototype-orthogonal projection as a preconditioning step for clean erasure/remapping is a simple but effective technical contribution that addresses a real, empirically demonstrated problem (Figure 3). The connection between MoE routing diversity and unlearning irreversibility (scattering → breaking cohesion → impeding linear-probe recovery) is an original conceptual link that has not been explored in prior unlearning work.

## Suggestions
- Replace "irreversible" with "recovery-resistant" or "substantially harder to reverse" throughout the paper (title, abstract, all sections), and add a paragraph discussing what stronger forms of irreversibility would require (adaptive attacks, formal guarantees).
- Add a complement-space experiment: train a linear probe on full post-unlearning features to measure whether forget information survives outside the prototype span.
- Either provide a mechanistic explanation for the random-data-forgetting adaptation or remove it. If kept, add an ablation showing that remapping (not just PO projection) drives the MIA improvement, and include the multi-expert MoRE variant.
- Clarify the "constant memory" claim—change to "O(dk) memory, independent of dataset size N" to avoid confusion with absolute memory consumption.

## Calibration Anchors

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| SUN (p7mgNvOD9Q) | 4.00 | R1 | MoRE has more innovation (PO + remapping + MoE), broader evaluation (CIFAR-100, Tiny-ImageNet, ImageNet, diffusion), and KR results; clearly stronger. |
| Deep Unlearning (pUOesbrlw4) | 5.25 | R1 | Similar spirit (training-free, SVD-based) but MoRE adds PO projection, remapping, MoE scattering, KR evaluation, and better ablation; clearly stronger. |
| Adversarial Mixup (GcbhbZsgiu) | 5.00 | R1 | Training-based, smaller datasets; MoRE is training-free and more scalable; stronger. |
| Decoupling Class Label (OHOmpkGiYK) | 5.75 | R2 | Different angle on unlearning; MoRE has more elegant method and stronger results. |
| NegMerge (bKQJzuBSRJ) | 6.00 | R2 | All-6s paper, incremental contribution building on task arithmetic. MoRE has more technical novelty and broader scope; stronger. |
| I2I Generative Unlearning (9hjVoPWPnh) | 6.00 | R2 | Accepted, novel domain but narrower scope (inpainting only). MoRE covers classification + diffusion with broader evaluation; comparable or stronger. |
| Label-Agnostic Forgetting (SIZWiya7FE) | 6.00 | R2 | Accepted, different problem setting. MoRE's method is more principled and training-free. |
| Unlearning via Sparse Repr. (TLBPjECC5D) | 5.25 | R2 | Discrete bottleneck approach; MoRE has better results and more comprehensive evaluation. |

**Initial bracket (R1):** 5.0–7.0. MoRE is clearly above the 4.0–5.25 cluster and competitive with the 6.0 cluster.

**Narrowed (R2):** MoRE lands at 6.0. It has more technical novelty than NegMerge (6.0), broader scope than the I2I paper (6.0), but the "irreversible" overclaim in the title and throughout is a nontrivial framing issue that prevents a higher score.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>