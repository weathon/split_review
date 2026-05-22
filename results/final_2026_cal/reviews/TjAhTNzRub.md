Now I have sufficient calibration context. Let me write the final review.

**Calibration Summary:**

Round 1 bracket: The paper's topic (training-free feature-level unlearning) placed it between the low band (avg 2.0–3.0, rejected/withdrawn papers with poor evaluation) and the middle band (avg 4.0–5.5, mixed accept/reject decisions). The high band contained only unrelated topics. Initial bracket: **4.0–6.5**.

Round 2 narrowing: I read several anchors. **TMU** (avg 5.5, Accept Poster) has a training-based two-stage method and comparable experimental scope but weaker results on linear-probe evaluation. **REM** (avg 5.0, Accept Poster) has scalability issues (doubles model size). **Source-Free Class Unlearning** (avg 4.5, Reject) and **Forget Vectors** (avg 4.5, Reject) have weaker results. MoRE's KR results (HM_f=0.07 on CIFAR-100 vs 52.96 for retrain) are an order of magnitude better than any anchor paper. The method is training-free, efficient, and clean. However, the LPIPS labeling error, overclaimed "irreversibility" claim, and possible memory figure inconsistency prevent it from reaching the 7+ range. The paper is stronger than the typical 5.5 poster-accept papers I read. **Final score: 6.0.**

---

## Summary

This paper proposes MoRE (Mixture of Remapping Experts), a training-free framework for feature-level machine unlearning. MoRE introduces three components: (i) prototype-orthogonal (PO) projection that decorrelates forget and remain prototypes before erasure, (ii) remapping of forget prototypes into multiple remain prototypes via multiple experts to scatter forget features, and (iii) efficient activation-mean prototypes that require only a single forward pass. On standard classification benchmarks (CIFAR-10/100, Tiny-ImageNet), MoRE achieves near-perfect remain utility while driving the KR linear-probe metric (HM_f) to near zero (e.g., 0.07 on CIFAR-100 vs. 52.96 for retrain), decisively outperforming existing training-free methods. The approach is also highly efficient (under 10 seconds, modest GPU memory) and extends to diffusion model concept unlearning.

## Strengths

- **Breakthrough KR results that set a new bar.** On CIFAR-100 under KR evaluation (lr=0.1), MoRE achieves HM_f of 0.07—meaning forget-set accuracy under linear probing is essentially zero. This is dramatically lower than all baselines including retrain-from-scratch (52.96) and ESC-T (87.34). The gap is so large that it constitutes a qualitative improvement in irreversibility against the deployed adversary model. This single result is the paper's strongest piece of evidence.

- **Methodologically clean and principled.** The three innovations (PO projection → erasure → multi-expert remapping) each address a well-diagnosed failure mode of prior work: prototype correlation degrades remain utility (Fig. 3, Section 3.1), single-target remapping leaves residual cohesion exploitable by probes (Section 3.3), and activation-mean prototypes enable training-free efficiency. The ablation (Table 3) quantitatively validates each component's contribution.

- **Genuinely training-free with dramatic efficiency.** MoRE requires only a forward pass and lightweight linear algebra on prototype means. Figure 5 reports 9.5 seconds for CIFAR-10 unlearning, compared to >80 seconds for training-based approaches. The O(Nd) time and O(dk) memory complexity is a real practical advantage over methods requiring full retraining or SVD on cached activations.

- **Out-of-the-box extension to diffusion models.** MoRE applied to Stable Diffusion v1.4 cross-attention layers (no architecture-specific adaptation, no hyperparameter tuning) achieves the best LPIPS_d (0.25 Van Gogh, 0.26 Kelly McKernan) among training-free methods, demonstrating generality beyond classification.

- **Robustness to hyperparameters.** Performance is stable across expert counts (2–8, Figure 7) and target remapping classes (Table 5), reducing the tuning burden.

## Weaknesses

### Major

- **The "irreversible" claim overreaches the evidence.** The title and abstract assert "irreversible feature-level unlearning," but the evaluation only tests recovery via *linear probing* (the KR metric). The paper does not test recovery via nonlinear probing (e.g., a small MLP on frozen features), full fine-tuning of the backbone, or partial fine-tuning. Section 3.3 acknowledges that single-expert remapping "can be exploited by carefully tuned linear probes" and that multiple experts help, but still only evaluates a single probing configuration. The t-SNE visualization (Figure 1) is suggestive but not quantitative evidence against stronger attacks. The term "irreversible" should be scoped to "irreversible against linear probing" unless additional experiments with stronger adversaries are provided.

### Minor

- **LPIPS direction inconsistency in Table 2.** The table headers use arrows (↓) and (↑) that are inconsistent with the metric definitions in the body text. Specifically, the table shows LPIPS_f(↓) but the text states "higher is better" for LPIPS_f, and LPIPS_r(↑) but the text states "lower is better" for LPIPS_r. The body text definitions are correct conceptually (you want high perceptual dissimilarity from the forget artist), so the values are interpretable, but the inconsistent arrows are confusing and must be corrected.

- **GPU memory claim inconsistency.** Section 4.1 states MoRE consumes "less than 200 MB of GPU memory (see Fig. 5)," but Figure 5 (as parsed) reports MoRE at 540 MB—well above 200 MB. The underlying method is still efficient (540 MB is modest), but the stated number is inconsistent with the figure. The authors should clarify this discrepancy.

- **Scalability evidence for ImageNet is deferred to an appendix** that is not available in the current submission. While the Tiny-ImageNet + ViT results (Table 1) provide some evidence of scaling, the main paper would benefit from at least summarizing the ImageNet results.

- **No discussion of when the prototype matrix might be rank-deficient.** The method assumes P is full-rank to compute D = P^† via SVD (Section 3.1). If prototypes are highly redundant or if k > d, this assumption breaks. The paper should at minimum acknowledge this and discuss mitigations.

### Trivial

- The target remapping class selection (Section 3.2) is left to a heuristic ("designated remain prototype") without analysis of how to choose optimally. Table 5 shows some targets are slightly better than others, but the paper provides no guidance.

## Nice-to-Haves

- Testing against stronger recovery attacks (nonlinear probing with MLP, lightweight fine-tuning of the feature extractor) would substantially strengthen the irreversibility claim.
- A brief discussion of how the method handles scenarios where forget and remain classes are semantically very close (e.g., subclasses), where the "scattering" might still leave identifiable structure.
- A theoretical bound on the residual separability of forget features after remapping would complement the empirical results.

## Removed Points

These points were flagged but do not survive verification against the paper:

- *"The method assumes the prototype matrix is full-rank, which is not discussed"* — Retained as Minor above.
- *"Diffusion results must be treated as unreliable due to LPIPS inconsistency"* — Downgraded from Fatal to Minor. The text correctly defines the metric direction; only the table arrows are wrong. The results are interpretable.
- *"Not compared against nonlinear probing or fine-tuning"* — Retained as Major above (irreversibility overclaim).
- *"Choice of remain prototype is left without guidance"* — Retained as Trivial.
- Various generic criticism about missing baselines or scope — Removed per filtering rules.
- "The paper overclaims by labeling unlearning irreversible" — Restructured into a Major weakness, not a fatal one, since the paper qualifies the claim contextually.

## Novel Insights

None beyond the paper's own contributions. The key insight—that scattering forget prototypes into multiple remain prototypes via orthogonalized projection is more effective than subspace erasure—is the paper's own contribution, not something revealed by cross-review synthesis.

## Suggestions

1. **Fix the LPIPS table header arrows** to match the body text: LPIPS_f(↑), LPIPS_r(↓), LPIPS_d(↑).
2. **Tone down the "irreversible" claim** to "irreversible against linear probing" or add experiments with nonlinear probes and lightweight fine-tuning. The existing evidence does not support the stronger claim.
3. **Resolve the memory inconsistency**: verify whether the 540 MB in Figure 5 is correct or if the text's 200 MB refers to a different configuration, and ensure consistency.
4. **Provide ImageNet results in the main paper** or at minimum a summary sentence with key numbers.
5. **Acknowledge the full-rank assumption** on the prototype matrix and discuss what happens when k > d or when prototypes are near-singular.

## Score and Decision

**Initial bracket (Round 1):** Between 4.0 and 6.5, based on comparison with unlearning papers scoring 2.0–3.0 (weak) and 4.0–5.5 (middle).

**Narrowing (Round 2):** Compared against TMU (5.5, Accept Poster), REM (5.0, Accept Poster), and other unlearning papers. MoRE is materially stronger than these in method cleanliness, result quality, and efficiency, but the overclaimed irreversibility and presentation issues prevent it from reaching the 7+ range.

**Anchor papers consulted:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| PL0uEscEkD (Unlearning for CL) | 2.00 | R1 | Much weaker |
| WNUDOLYlbh (Learn-to-Unlearn) | 3.00 | R1 | Much weaker |
| jROUUKq51K (MaGA) | 4.00 | R1 | Weaker, less clean method |
| OmkKZJtYFG (Source-Free Class UL) | 4.50 | R1 | Weaker, mixed reviews |
| m3FOf6nKnU (Forget Vectors) | 4.50 | R1 | Weaker, retain degradation |
| 4WMBSHHJEr (TMU) | 5.50 | R2 | Comparable scope, MoRE has stronger KR results |
| xG0mQ4Xsfm (REM) | 5.00 | R2 | Scalability issues, MoRE cleaner |
| Vc9yt0YwPw (Benchmarking MU for VTs) | 5.50 | R2 | Different category (benchmark paper) |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>