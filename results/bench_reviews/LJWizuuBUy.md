## Summary
The paper proposes SWAP, a network pruning method that reformulates the sparse linear-regression (LR) approach to Fisher-Information-based pruning as a Sparse Entropic Wasserstein Regression (EWR) problem. LR is recovered as the special case Π = diag(1/n), and the entropic OT plan is argued to implicitly perform "Neighborhood Interpolation" that reduces gradient-noise variance while retaining covariance structure. Experiments on MLPNet/MNIST, ResNet20/50/CIFAR10, and MobileNetV1/ImageNet report gains over LR, particularly under injected gradient noise and at high sparsity.

## Strengths
- LR pruning falling out as the Π = diag(1/n), ε = 0 special case of the proposed EWR objective (Eq. 8 / Eq. 9) is a clean and non-trivial structural observation that places prior work on a continuum with the proposed method.
- Confidence intervals are reported over 5–25 runs (Tables 1–3), which is better than typical pruning-literature hygiene.
- At very high sparsity, the LR/EWR family substantially outperforms MP/WF/CBS in Table 1 (e.g., ResNet20 at 0.9 sparsity: ~12% for MP/WF/CBS vs. ~89% for LR/EWR); EWR adds 1–3 pp on top of LR consistently and 3+ pp under the +σ noise condition (e.g., MobileNetV1 0.8+σ: 60.29 → 63.62).

## Weaknesses

### Fatal
None.

### Major
- **Noise-robustness — the paper's headline claim — is only ever evaluated against LR, i.e. the EWR's own degenerate case.** Every "+σ" row in Table 1 and all entries of Tables 2 and 3 have MP/WF/CBS marked "-". Since LR is provably the Π = diag(1/n) special case of EWR (Eq. 8), the noise experiments test only whether *any* non-trivial Π helps, not whether EWR is competitive against any baseline that targets robust pruning. The Sec. 1 motivation (federated learning, analog memory, adversarial gradients) is therefore not actually evaluated.
- **High-sparsity rows where the central claim lives have no re-run baselines.** Table 1 caption: "The data of MP, WF, and CBS are copied from [Yu et al. 2022]." For sparsity ≥ 0.95 on ResNet20/50 and ≥ 0.9 on MobileNetV1 the prior baselines are simply absent. The abstract's claim of outperforming SoTA "when the network size or target sparsity is large" therefore rests on cells the authors didn't fill in.
- **The abstract's "6% accuracy improvement … MobileNetV1 with less than one-fourth of parameters remaining" does not match Table 1 vs. the paper's natural baseline LR.** At 0.75–0.8 sparsity, EWR exceeds LR by ~1.1 pp (68.15 → 69.26 at 0.7; 65.72 → 66.82 at 0.8); even at 0.9+σ the gap is 3.4 pp. The "6%" appears to be the gap against CBS (e.g., 55.11 → 69.26 at 0.7), but CBS is not the comparator for the noise story. The headline is misleading regardless of interpretation. (The "8% testing loss" claim does match Table 3, 0.75 + 25% noise: 8.13%.)
- **The "Neighborhood Interpolation reduces noise" argument is asserted, not established.** The trace inequality trace(Σ′_i) = (Σⱼ[ν_j^(i)]²)·trace(Σ) ≤ trace(Σ) (Sec. 3) follows from Cauchy–Schwarz for *any* convex combination of i.i.d. gradients; it does not single out the OT-chosen Π as opposed to arbitrary averaging. Moreover, under the stated i.i.d. assumption, uniform averaging is optimal, which corresponds to the ε → ∞ case, not the proposed regime. The K^(1) cross-term ∇ℓᵢ∇ℓ′ᵢᵀ is described as "striking a balance" with no bias/variance bound; the argument does not connect OT geometry to denoising in a quantitative way.

### Minor
- **Algorithm 1 never specifies how Π is computed or refreshed.** The algorithm computes the pairwise cost C and then uses Π in ∇Q, but Sinkhorn iterations, warm starting, update frequency, and stopping criteria are absent. Π is the quantity that differentiates EWR from LR, so this is a real reproducibility gap, not nitpicking.
- **No ablation over ε**, even though the entire "neighborhood-size control" narrative (Sec. 3) hinges on it. ε → 0 recovers LR and ε → ∞ is uniform averaging; without a sweep it is unclear which regime the reported gains actually correspond to.
- **The Convex Hull Distance Equality (Thm. 1) is essentially a definitional construction:** since E‖x−y‖² = ‖x−E[y]‖² + Var(y), the equality forces Var(y) = 0, i.e., ν is a point mass at y′. The downstream "neighborhood" interpretation is then more rhetorical than the theorem implies; this should either be tightened (treating the term as an inequality / variance decomposition) or the theorem reformulated honestly.
- **Section 2 conflates p-dimensional gradient geometry with 1-D projected scalars.** Π is a coupling between empirical distributions of scalars xᵢ = ∇ℓᵢᵀw and yᵢ = ∇ℓᵢᵀ\bar{w}, but the "neighborhood" intuition in Sec. 3 (and Fig. 1) is drawn in p-dimensional gradient space. The relationship between these geometries deserves explicit treatment.
- **Noise protocol underspecified.** σ, where noise is injected (data? gradients? labels?), and how "10% / 25% noisy data" is constructed are not defined; this matters because the entire robustness claim is conditional on this protocol.
- **The "sample complexity narrows to O(1/√n) from O(1/n^{1/4})" sentence (Sec. 3) is dropped in without setup, constants, or any connection to pruning quality.** Either develop or remove.

### Trivial
- The method is called SWAP in the title and Algorithm 1, but EWR throughout experiments. Unify.

## Nice-to-Haves
- Re-run MP / WF / CBS at the high-sparsity and noisy settings (fill the "-" cells).
- Compare against at least one robust-statistics pruner (trimmed/median-of-means FIM or similar).
- A visualization of the learned Π at varying ε for a small network — does it actually cluster gradients, or does it sit near diag(1/n) in practice?

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Strength removed:* "Substantial empirical gains under noise and high sparsity" framed via Table 3's 8.13% loss improvement and Table 1's 3.33 pp accuracy gain. Kept partially in Strengths above, but the Strength Finder's framing as "substantial" conflicts with the verified weakness that comparisons are vs. EWR's own degenerate case. The weakness wins; the strength is downgraded rather than reproduced verbatim.
- *Strength removed:* "Interpretable trade-off via ε." The paper never gives ε a value or sweeps it, so any claim of interpretability is not empirically supported.

## Novel Insights
None beyond the paper's own contributions. The genuine observation in the paper is the embedding of LR pruning as Π = diag(1/n), ε = 0 inside an entropic-OT formulation; nothing in the reviews surfaces an insight beyond that.

## Suggestions
- Restate the abstract to report the gap against the *relevant* baseline (LR) for the noise story, and report the CBS gap separately for the no-noise high-sparsity story.
- Fully specify Π updates in Algorithm 1 (Sinkhorn schedule, warm-start, stopping criterion) and report wall-clock overhead vs. LR.
- Add an ε ablation that traces accuracy from ε → 0 (LR) to large ε (uniform averaging).
- Run MP/WF/CBS at the high-sparsity and noisy settings, or, if infeasible, drop the "outperforms SoTA at large sparsity" framing where the comparators are absent.
- Tighten Sec. 3: replace the trace inequality with a bias-variance decomposition that actually distinguishes OT-weighted averaging from arbitrary averaging, and reconcile the 1-D-projection geometry with the p-dimensional "neighborhood" picture.

## Axis Evaluation
- **Originality:** moderate. The OT/EWR reformulation of FIM-based pruning is a fresh framing, with LR as a clean special case. The "neighborhood interpolation" narrative is novel but largely rhetorical.
- **Importance of research question:** robust pruning under noisy gradients is well-motivated.
- **Claims well supported:** no. The headline 6% claim doesn't match the tables vs. LR; the robustness claim is tested only against LR; competing baselines are absent in the regimes where EWR is claimed to win.
- **Soundness of experiments:** weak. Borrowed baselines, missing baselines in the key regimes, no ε ablation, underspecified noise protocol.
- **Clarity:** mixed. The OT reformulation and LR-as-special-case derivation are clear; the theoretical "noise reduction" section conflates geometries and overclaims; the algorithm omits its defining computation.
- **Value to community:** the LR-as-special-case-of-EWR observation is genuinely useful framing. Beyond that the empirical contribution over LR is incremental (1–3 pp at high sparsity).

## Score and Decision

Anchors retrieved (all six queries):
- `sMoifbuxjB.md` "Towards Meta-Pruning via Optimal Transport" — avg 7.20, Accept. OT for pruning, but with broader experimental validation, clearer practical gains, and no overclaimed robustness story. Clearly stronger than the paper under review.
- `3P87ptzvTm.md` "Optimal Multiple Transport ..." — avg 5.00, Reject. OT-formalism paper with limited downstream evidence; comparable in flavor.
- `j7S7o6ROn9.md` "Distributional Structured Pruning by TV Distance" — avg 5.00, Reject. Theoretical pruning with thin experiments; similar shape.
- `RzOm9oOSzm.md` "Unveiling Linear Mode Connectivity" — avg 3.50, Reject. Not directly comparable.
- `D6pHf8AiO7.md` "Pruning via FishLeg estimation" — avg 4.25, Reject. Fisher-based pruning with theoretical motivation but unsatisfying baselines; very close analogue.
- `zUtl4kJa0C.md` "Revisiting Critical Learning Periods" — avg 4.75, Reject. Tangential.
- `FT4gAPFsQd.md` "How Sparse Can We Prune: Geometric Viewpoint" — avg 6.00, Reject (borderline). Theory-driven pruning with clearer experimental support than this paper.
- `88rjm6AXoC.md` "Optimal Brain Apoptosis" — avg 6.25, Accept. Hessian-based pruning with more thorough comparisons; clearly stronger.
- `vvD0VFw0LG.md` "PruningBench" — avg 4.75, Reject. Benchmark paper; loosely comparable.
- `S83ldgJZLh.md` "SPADE Structured Pruning for MBDL" — avg 4.75, Reject. Methodologically narrow; similar level.
- `BWlSNtViSA.md` "Coupling Fairness and Pruning" — avg 3.67, Reject. Weak baselines.
- `ngmEcEer8a.md` "Unreasonable Ineffectiveness of Deeper Layers" — avg 6.50, Accept. Not directly comparable.
- `Y9t7MqZtCR.md` "SWAMP IMP" — avg 6.40, Accept. Strong empirical pruning paper.
- `jsvvPVVzwf.md` "Maximal Unstructured Pruning for Cosine Similarity" — avg 5.00, Accept. Comparable mid-tier.
- `Se2aTG9Oui.md` "CoNNect Regularizer" — avg 4.80, Reject. Similar mid-tier.
- `rO62BY3dYc.md` "Pruning via Ranking (PvR)" — avg 3.75, Reject. Weak.
- `k9QklPhLCs.md` "Subspace Node Pruning" — avg 3.50, Reject. Weak.
- `fk5ePN7YCS.md` "NEPENTHE Entropy-Based Pruning" — avg 3.75, Reject. Weak.

Calibration: the paper sits closest to FishLeg (4.25) — a Fisher-based pruning method with non-trivial theoretical motivation but with experiments that don't fully cover the regimes where the contribution is claimed. It is weaker than "How Sparse Can We Prune" (6.00) and clearly below "Towards Meta-Pruning via OT" (7.20), which executes the OT-for-pruning idea with much stronger experimental discipline. It is above the very weak anchors (3.5–3.75) because the LR-as-special-case framing is a real conceptual contribution.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>