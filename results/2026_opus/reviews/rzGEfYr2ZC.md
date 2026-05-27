# Meta-Review: "Don't Be Greedy, Just Relax! Pruning LLMs via Frank-Wolfe"

## Summary
The paper proposes SparseFW, a layerwise LLM pruning method that replaces the combinatorial mask-selection problem with its convex hull and solves the resulting relaxation via Frank-Wolfe (FW). It contributes (i) a unifying view of Wanda/RIA as greedy single-weight optimizers of the same per-layer objective, (ii) an FW algorithm with an efficient LMO and a precomputation trick (G = XX⊤, H = WG) that keeps memory and per-iteration cost low, and (iii) a data-dependent error bound for the thresholded relaxed solution. Empirically, SparseFW is compared to Wanda/RIA on five modern GPT models at 50%, 60%, and 2:4 sparsity.

## Strengths
- **Clean reformulation of Wanda and RIA as greedy single-weight solvers of (MASK SELECTION).** §2.1 derives the Wanda saliency score |W_ij|·||X_{j,:}||₂ directly from a single-step greedy minimization of Equation (5), and extends the same argument to RIA via rescaling. This is a genuinely useful conceptual unification that clarifies what these methods are doing and provides a natural framing for the FW alternative.
- **Memory-efficient, projection-free LMO that scales.** §2.3 shows that with G = XX⊤ and H = WG precomputed once, each FW iteration reduces to a single matrix multiplication plus two element-wise products of d_out × d_in matrices; the LMO (Equation 12) is just a top-k selection over negative gradient entries. This is what makes the method viable at 7B–9B scale.
- **Substantial gains at higher-sparsity regimes.** Table 1 shows consistent, often sizable perplexity improvements at 60% and 2:4 sparsity (e.g., LLaMA-3.1-8B at 60%: 17.97 vs. 21.53 for Wanda; LLaMA-3.1-8B 2:4: 20.45 vs. 24.82). Zero-shot accuracy gains at 60% and 2:4 are also broadly consistent across all five models.
- **Sample efficiency over Wanda.** Figure 3 (right) shows perplexity dropping from ~22 to ~19.5 as calibration samples scale 64→512 with SparseFW, while the text reports Wanda only drops 25.1→24.6 — evidence that the relaxation makes better use of additional data.

## Weaknesses

### Fatal
None. The concerns below are real and substantive but do not by themselves invalidate the paper's core results.

### Major
- **The α=0.9 mechanism undercuts the "don't be greedy" narrative.** §2.3 admits that "setting α=0.0 (full FW without any fixed weights) consistently yields worse results than the baselines," and that best performance comes from fixing 90% of the highest-Wanda-saliency weights as unprunable and applying FW only to the remaining 10%. The title, abstract, and §1 sell the contribution as a convex relaxation that improves on greedy heuristics by capturing weight interactions; the deployed method instead relies on the greedy mask for 90% of decisions and uses FW as a margin refinement. This is a major framing/contribution gap, not a tuning detail. Algorithm 1 also does not reflect the α scheme, despite α being essential to the empirical claim.
- **Table 1 gains at 50% sparsity are inconsistent and not always above baselines.** At 50% sparsity, SparseFW(Wanda) is worse than Wanda on DeepSeek-7B (7.89 vs 7.79) and LLaMA-3-8B (10.21 vs 10.09), and there are several ties. The abstract's "consistent gains in final WikiText perplexity" overstates the 50% column. Combined with §2.3's own observation that vanilla FW achieves larger local objective improvements yet worse perplexity, this points to a real disconnect between the optimized per-layer reconstruction loss and the downstream metric. The paper acknowledges this honestly in §5, but the abstract and §1 framing do not.
- **Theoretical guarantee is loose at LLM scale.** Lemma 1's thresholding term contains k + √(2 d_in d_out k), which grows with dimension and does not vanish with iterations T or sample count. At LLaMA-scale matrices this term dominates, so the bound is more of a structural statement than an "approximation guarantee" in the usable sense. The conclusion that SparseFW "comes with strong theoretical justification" overstates Lemma 1's actual reach. The paper itself notes in §4 that the thresholding curve in Figure 4 does not fully close the gap to the continuous curve — which is exactly what the bound predicts and what limits its practical bite.
- **No SparseGPT comparison despite headline framing.** §3 reasonably scopes the comparison to mask-selection methods (Wanda, RIA) because SparseGPT also does weight reconstruction. Within that scope the choice is defensible. However, the abstract and §1 claim improvements over "state-of-the-art" pruning and that SparseFW can "drastically improve upon state-of-the-art performance," which a typical reader will read as including SparseGPT — the method most often deployed. Either the framing should be narrowed or the comparison added.

### Minor
- **No variance/CIs in Table 1.** The 50%-sparsity gaps are often hundredths or tenths of a perplexity point. Figure 3 (right) shows non-trivial seed-to-seed variation (shaded min-max bands), so single-point reporting in Table 1 cannot distinguish noise from a real win at 50%. At 60% and 2:4 the gaps are larger and the qualitative conclusion is unlikely to flip, but reporting variance is standard.
- **No ablation in the main text on α, no α=0 baseline row, no quantification of how often FW disagrees with the Wanda mask.** §2.3 references Table 2 in the appendix for the α sweep; given how central α is to the contribution, the main text would benefit from at least an α=0 row in Table 1 and a diagnostic showing what fraction of Wanda's mask SparseFW actually changes. This is what would let readers see the contribution of the relaxation independent of the warmstart.
- **Cost reporting is qualitative.** §3 says SparseFW is "clearly more compute-intensive than Wanda and RIA" but provides no wall-clock or memory numbers for a head-to-head comparison.

### Trivial
- Algorithm 1 omits the α-fixing scheme even though it is essential to the deployed method.

## Nice-to-Haves
- A diagnostic showing where in the saliency ordering FW disagrees with Wanda, and which layers/matrices benefit most from FW refinement vs. which are best left to the warmstart. This would convert the local–global mismatch observation into a scientific contribution rather than a residual limitation.
- A tighter, data-dependent bound (or an honest reframing of Lemma 1 as a structural observation rather than a guarantee) that does not blow up with d_in d_out.
- Deeper treatment in the main text of how the LMO adapts to n:m and per-row sparsity patterns, since the structured-sparsity gains in Table 1 are among the largest.
- One small head-to-head wall-clock plot vs. Wanda/RIA at fixed sample budget.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Speculation that the local objective being a wrong proxy is "structural"/unfixable.* (From the harsh critic.) The paper itself acknowledges the local–global mismatch in §5, and SparseFW does deliver clear gains at higher sparsity. The right framing is "limits the size of gains" rather than "invalidates the surrogate." Demoted into the Major weakness on 50%-sparsity inconsistency rather than maintained as a separate fatal claim.
- *"Method that wins in Table 1 is FW restricted to optimize only 10% of weights … the unconstrained version of the method admittedly loses to the baselines" framed as fatal.* This is true and important, but it is the basis of the Major weakness on framing; framing it as "not fixable" overstates what the paper as written supports — the 60% and 2:4 wins are real and non-trivial under any α.
- *"Strong empirical performance" framed as a standalone strength.* (From the strength finder.) Empirical performance is uneven at 50%; kept only the more specific, higher-sparsity wins as evidence.
- *"Approximation guarantee" listed as a strength.* The bound is real but vacuous at the operating scales (see Major). Demoted: the conceptual derivation is fine, but it is not a strength on its merits.

## Novel Insights
The most genuinely interesting observation the paper surfaces — though it does not fully own it — is the diagnostic implication of the α=0.9 finding: a thorough local optimizer can outperform Wanda on the per-layer reconstruction objective and still hurt downstream perplexity, which means the layer-wise Frobenius surrogate is not faithful enough to be optimized aggressively. The fact that high-Wanda-saliency entries should be treated as "do-not-touch" even though a Wanda mask is locally suboptimal is a non-obvious piece of structural information about LLM pruning. The paper currently presents this as a residual caveat; framed centrally, it could be the paper's most scientifically useful finding.

## Suggestions
- Promote the α-fixing scheme into the algorithm definition (rewrite Algorithm 1) and into the abstract; reframe the paper as "FW-based refinement of Wanda/RIA masks" rather than as a replacement for greedy mask selection.
- Add an α=0 row and at least one α sweep column into Table 1 in the main text, and report the fraction of Wanda's mask SparseFW actually changes.
- Either compare to SparseGPT in the main results or restrict the abstract/§1 claims explicitly to the mask-selection sub-problem.
- Report standard deviations (or a single representative seed-bar) for Table 1, especially at 50% sparsity where gaps are small.
- Either tighten Lemma 1 (data-dependent thresholding bound) or reframe it as a qualitative result rather than an "approximation guarantee."
- Add a wall-clock and peak-memory comparison vs. Wanda/RIA at matched calibration budgets.

---

## Evaluation Axes
- **Originality**: Moderate. The conceptual recasting of Wanda/RIA as greedy single-weight optimizers is clean and useful; using FW on the convex hull of binary masks is a reasonable and not commonly seen choice in LLM pruning, but related work has explored convex optimization for the same problem (e.g., FISTA-style methods).
- **Importance**: The mask-selection sub-problem for retraining-free LLM pruning is a well-motivated target.
- **Support for claims**: Mixed. The 60% and 2:4 wins are well-supported; the abstract's "consistent" wording overclaims given the 50% column; the "strong theoretical justification" overclaims the actual content of Lemma 1; the central "don't be greedy" framing is undercut by the α=0.9 admission.
- **Soundness of experiments**: Competent on coverage (5 models, 3 sparsity regimes, both warmstarts), but missing standard deviations, an α=0 row, an α sweep in main text, and a SparseGPT or wall-clock comparison.
- **Clarity**: Good throughout §2 and §4; the α scheme is structurally important but presented as a side caveat in §2.3.
- **Value to the community**: Genuine but narrower than claimed. The contribution as actually demonstrated is a useful refinement layer on top of Wanda/RIA at high sparsity, plus a clean conceptual framing.

## Calibration Anchors

Round 1 (bracketing):
- `7DY2DFDT0T.md` — *EfficientSkip* (avg 2.50, Round 1 weak band) — substantially weaker conceptually than this paper.
- `762u1p9dgg.md` — *MOEfication by Experts as Masks* (avg 3.40, Round 1 weak band) — weaker; sparse experiments and unclear contribution.
- `XMaPp8CIXq.md` — *Always-Sparse Training with Guided Stochastic Exploration* (avg 3.00, Round 1 weak band) — weaker; less polished empirics.
- `ulGwcj1egv.md` — *FiRST* (avg 3.00, Round 1 weak band) — different setting, weaker.
- `pOBvr1PxFd.md` — *OWL* (avg 6.00, Reject, Round 1 mid band) — comparable in topic; OWL has clearer methodological contribution (non-uniform sparsity) but mixed reviews.
- `a0ftEY6puc.md` — *Language-Specific Calibration* (avg 6.00, Reject, Round 1 mid band) — comparable scope but stronger empirical focus.
- `oXh0939Zzq.md` — *Dynamic Low-Rank Sparse Adaptation (LoSA)* (avg 5.20, Accept, Round 1 mid band) — adjacent (post-pruning recovery), not directly comparable.
- `f4b0YVwKUO.md` — *FASP* (avg 4.00, Reject, Round 1 mid band) — comparable scope, weaker novelty than SparseFW.
- `LCrm1FSl26.md` — *Mecon* (avg 5.60, Reject, Round 1 mid band) — comparable: search-based LLM pruning with mixed reviews.
- `OfjIlbelrT.md`, `tcsZt9ZNKD.md`, `E4Fk3YuG56.md`, `f4gF6AIHRy.md` (Round 1 strong band) — all distinctly stronger contributions than SparseFW in clarity of message and breadth of evaluation.

Initial bracket from Round 1: **4.5–6.0** — clearly above the very-weak band but below the strong band; lands among the mid-band LLM-pruning anchors that mostly Rejected.

Round 2 (narrowing):
- `FT4gAPFsQd.md` — *How Sparse Can We Prune* (avg 6.00, Reject) — theoretically-grounded pruning, similar tier to SparseFW; SparseFW's empirics are stronger at LLM scale but its theory bound is similarly loose.
- `88rjm6AXoC.md` — *Optimal Brain Apoptosis* (avg 6.25, Accept) — better theoretical execution and CV/Transformer experiments; SparseFW does not match its tightness of contribution.
- `jsvvPVVzwf.md` — *What Makes a Good Prune?* (avg 5.00, Accept) — adjacent theoretical pruning paper, comparable tier.
- `R9W6fFlr8W.md` — *Primal-dual algorithm for variational image reconstruction* (avg 5.00, Reject) — adjacent convex-optimization-in-DL paper.
- `1GTARJhxtq.md` — *Perplexed by Perplexity* (avg 5.75, Accept) — adjacent (data pruning, not weight pruning).
- `ldJXXxPE0L.md` — *Cost of Scaling Down LLMs* (avg 6.00, Accept) — study paper, different mode.
- `BINwUtUGuq.md` — **FISTAPruner** (avg 5.25, Reject) — *the closest anchor*: LLM layerwise pruning via FISTA-based convex optimization. Same conceptual move (convex relaxation, iterative solver), same evaluation style (multiple LLaMA sizes, 50% / 2:4). Got mostly 6s and one 3 over novelty vs. SparseGPT; rejected.
- `5RZoYIT3u6.md` — *PruneNet* (avg 6.00, Accept) — calibration-free LLM pruning, similar tier but accepted on broader scope.

After narrowing: the closest analog is FISTAPruner (5.25, Reject). SparseFW has a comparable methodological contribution (convex relaxation + iterative solver) but a more pointed self-disclosed limitation (α=0.9) and weaker 50% results. It is somewhat below FISTAPruner. OBA (6.25, Accept) and OWL (6.00, Reject) bracket it from above.

## Score and Decision
The paper sits comparably to FISTAPruner (5.25, Reject) and OWL (6.00, Reject), but slightly below both due to (i) the α=0.9 self-admission that undermines the "don't be greedy" thesis, (ii) inconsistent 50%-sparsity results, and (iii) a theoretical bound that is loose at LLM scale. It is clearly above the weak anchors (2.5–3.4) but does not reach the OBA (6.25)/PruneNet (6.00) accept tier.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>