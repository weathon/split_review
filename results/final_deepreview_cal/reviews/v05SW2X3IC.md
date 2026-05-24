Now I have thorough calibration data. Let me synthesize the final review.

**Bracket from Round 1:** The paper sits between x33vSZUg0A (5.33, multi-task compression) and CxXGvKRDnL (8.00, diffusion compression). 

**Narrowing from Round 2:** Comparing against L0evcuybH5 (6.75, information bottleneck analysis) — our paper has similar information-theoretic ambition but less tight theory-experiment coupling. Against yVGGtsOgc7 (5.80, disentangled representations via multi-task learning) — our paper is more practically grounded. Against x33vSZUg0A (5.33) — our paper is clearly stronger in theoretical motivation and experimental systematics.

The paper lands at approximately **6.0** — above the multi-task compression anchor (5.33), below the tighter info-theoretic analysis anchor (6.75), and well below the genuinely novel diffusion compression work (8.00).

Now I'll write the final review.

---

## Summary

This paper proposes a learnable three-channel codec grounded in Gray–Wyner information theory that separates common and task-specific information between two vision tasks. The authors develop lossy common information bounds (Theorem 1), derive a learnable Lagrangian objective with a single hyperparameter β controlling the transmit–receive rate tradeoff (Theorem 2), and design a "Shared" encoder architecture with an auxiliary alignment loss. Experiments span synthetic data, colored MNIST edge-cases, and real vision tasks (Cityscapes segmentation+depth, COCO detection+keypoints), where the method consistently outperforms independent single-task coding and approaches joint coding.

## Strengths

- **Rigorous theoretical foundation linking classical information theory to neural architectures:** Theorem 1 extends lossless common information bounds to the lossy setting via interaction information, providing a precise condition for when Wyner’s and Gács–Körner common information coincide. Theorem 2 transforms the Gray–Wyner optimization into a form suitable for neural training with entropy models (Eqs. 10–12). These results are grounded in the literature and give the proposed codec a principled optimization objective.

- **Systematic architecture ablation validating the Shared design:** On synthetic data, the Shared architecture is compared against Separated (independent analysis per channel) and Combined (single analysis transform with split output) alternatives across multiple β settings (Fig. 3). The Shared design consistently yields lower rate-distortion, with β = 3/2 providing a balanced transmit–receive operating point.

- **Edge-case validation showing adaptation to mutual information structure:** The colored MNIST experiments (Section 4.2, Fig. 4) demonstrate that the codec adapts appropriately to three distinct PMFs — placing most information on the common channel when tasks are fully dependent, minimizing common-channel rate when independent, and handling a partially-separable mixture case. This directly tests the core claim that the architecture responds to the underlying common information between tasks.

- **Consistent improvement over independent coding on real vision tasks:** On Cityscapes and COCO (Fig. 5), the proposed method substantially outperforms independent single-task codecs in BD-rate terms (e.g., –81.58% average transmit-rate advantage), while approaching joint coding performance.

## Weaknesses

### Major

- **Baseline capacity not controlled or reported:** The Independent baseline uses separate codecs per task (no common channel) and the Joint baseline uses a single codec for both tasks. Neither parameter counts, FLOPs, nor architectural details are provided for these baselines relative to the proposed method. While the Independent baseline likely has *more* parameters (which would make the comparison conservative), the absence of this information prevents the reader from attributing gains confidently to the Gray–Wyner structure rather than to parameter allocation differences. At minimum, model size accounting is needed.

- **No variability estimates in real-task experiments:** The Cityscapes and COCO evaluations (Section 4.3, Fig. 5) use single training runs with one hyperparameter set. No error bars, multiple restarts, or cross-validation are reported. Rate–accuracy curves can shift materially with training noise, and the reported BD-rate advantages lack any quantification of uncertainty, weakening the quantitative claims.

### Minor

- **Combined Cityscapes metric obscures individual task behavior:** The Cityscapes evaluation combines mIoU and a rescaled depth RMSE into a single combined metric (Fig. 5a). The rescaling of depth RMSE to match the mIoU scale is uninterpretable, and raw per-task rate–accuracy curves are not shown in the main paper. Reporting individual task metrics would make the results more transparent.

- **Lagrangian β-parameterization is asserted rather than rigorously derived:** Section 3.2 maps β = 1 to transmit-rate optimization and β = 2 to receive-rate optimization, claiming intermediate β explores the Gray–Wyner contour. The original Gray–Wyner Lagrangian (Eq. 9) operates over (α₁, α₂), and while the proposed weighted sum is a sensible Lagrangian relaxation, the paper does not establish formally that intermediate β values correspond to points on the Pareto frontier. The synthetic experiments (Fig. 3) provide empirical validation, but the theoretical claim should be tempered.

- **Architecture justification deferred to appendix:** The Shared encoder design (Eq. 14, masked averaging) is motivated by a theoretical claim about reducing learning complexity, but the justification is relegated to Appendix C. In the main text, the design choice appears somewhat ad hoc, weakening the narrative flow from theory to architecture.

### Trivial

- The conclusion states "between the three computer vision experiments" but only two real-vision experiments (Cityscapes, COCO) are presented in Section 4.3; the count may include the synthetic or MNIST experiments, but this should be clarified.
- The distortion functions used for Cityscapes and COCO tasks are not explicitly specified in the main text.

## Nice-to-Haves

- Visualizing what information each channel carries (e.g., decoding each channel independently and measuring per-task performance) would directly confirm that the common channel captures shared information and private channels do not. This would strongly bolster the central claim of information separation.
- Reporting the full set of operating points for intermediate β values on the real vision tasks would substantiate the transmit–receive tradeoff claim beyond the synthetic setting.
- Including the Independent and Joint baselines on the colored MNIST PMFs (Section 4.2) would ground the edge-case claims more clearly.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Heuristic mapping of Lagrangian is a fatal theoretical gap"** — Removed. The paper explicitly presents this as a Lagrangian relaxation (a standard technique for non-convex optimization) and validates it empirically. The concern was framed as a rigorous derivation gap, but the paper never claims an exact derivation; it proposes a practical heuristic grounded in the Gray–Wyner objective. Demoted to Minor.

- **"Section 4.3 receive-rate curve higher than Independent is not discussed"** — Removed. The paper *does* discuss this implicitly in stating that the receive-rate curve suggests "the rate of the common channel is lower than the empirical mutual information between these tasks" (Section 4.3), which aligns with the paper's thesis.

- **"The paper needs more precise statement of what the proposed method adds relative to prior multi-task codecs"** — Demoted to Nice-to-Have. The paper adequately distinguishes itself through the private channels and transmit–receive tradeoff, which are both clearly stated.

- **"Should comment on what part of the gap between empirical and theoretical rates is due to training vs. architecture"** — Removed. This is speculative; the paper acknowledges the gap and cites it as common in practice.

## Novel Insights

The paper's synthesis of lossy common information bounds (Theorem 1) with a Lagrangian training objective (Theorem 2) and a concrete neural architecture provides a rare bridge between classical multi-terminal information theory and modern learned compression. The insight that interaction information between optimal rate-distortion representations bounds the gap between Wyner’s and Gács–Körner common information (and thus determines whether the transmit–receive tradeoff is worth exploring) gives practitioners a diagnostic tool for deciding when a three-channel Gray–Wyner codec is warranted versus simpler alternatives.

## Suggestions

- Report parameter counts, FLOPs, or total model sizes for the Independent, Joint, and proposed architectures to enable fair comparison.
- Run the main Cityscapes and COCO experiments with at least 2–3 random seeds and report standard deviations on the BD-rate metrics.
- Show individual task metrics (mIoU alone, depth RMSE alone) alongside the combined metric for Cityscapes.
- Clarify whether the "three computer vision experiments" in the conclusion refer to synthetic + MNIST + real tasks or if a third real-vision experiment was intended.

## Score and Decision

**Round-1 bracket:** between 5.33 (x33vSZUg0A, multi-task compression) and 8.00 (CxXGvKRDnL, diffusion compression).  
**Round-2 narrowing:** compared against L0evcuybH5 (6.75, tighter info-theoretic analysis), yVGGtsOgc7 (5.80, less practically grounded), and foKwWau15m (6.00, benchmark paper).  
**Anchor comparison summary:**
- x33vSZUg0A (5.33): weaker theory, less systematic experiments — our paper is stronger
- aQ7qYnY2nF (4.00): limited novelty — our paper is clearly stronger
- foKwWau15m (6.00): different type (benchmark), not directly comparable
- yVGGtsOgc7 (5.80): stronger theory but weaker practical application — our paper is slightly stronger
- L0evcuybH5 (6.75): cleaner theory-experiment coupling — our paper is weaker
- CxXGvKRDnL (8.00): genuinely novel theoretical insight with strong results — our paper is clearly weaker
- ulIW7Frjpn (4.75): LLMs as entropy models — not directly comparable
- jznbgiynus (6.00): language modeling as compression — not directly comparable
- IQZicPtADC (5.83): representation transfer for imitation learning — not directly comparable
- 1jbh2e0b2K (6.00): multi-task finetuning — not directly comparable

The paper has solid theoretical contributions and systematic experiments, but the experimental gaps (capacity control, error bars, combined metrics) prevent it from reaching the 6.75+ tier. It sits clearly above 5.33 and slightly above 5.80, landing at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>