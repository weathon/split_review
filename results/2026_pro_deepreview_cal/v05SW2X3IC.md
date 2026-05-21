Now I have all the calibration data I need. Let me synthesize my final review.

## Calibration Summary

**Round 1 Bracketing:**
- Weak band (<3.5): NCA compression (3.40), Window-based dynamic attention LIC (3.40), FV-NeRV (2.60), CutSharp (3.00) — all clearly below this paper.
- Middle band (3.5-7.5): Task-aware video compression RL (4.00), Multi-task compression TAMC (5.33), Model quantization+compression (5.00), Lattice Transform Coding (7.20).
- Strong band (>7.5): Progressive compression diffusion (8.00), Lightweight watermarking (7.60), Flexible residual binarization (8.00), Würstchen (8.00).

**Bracket: 4.5–6.5**

**Round 2 Narrowing:**
- `x33vSZUg0A` (5.33): Closest anchor — multi-task compression with task grouping + DAG. Stronger experimental scope but weaker theory. This paper is comparable with stronger theoretical contributions.
- `yVGGtsOgc7` (5.80): Disentangling through multi-task learning, theory+empirical. Similar level.
- `VkWbxFrCC8` (6.67): RECOMBINER — clearly stronger, more comprehensive experiments, clear technical improvements.
- `lpxcCD7WbQ` (5.25): Task adaptation, less relevant.

**Final score: 5.5** — The paper sits between the 5.33 TAMC anchor (similar topic, accepted) and the 5.80 disentangling anchor, with theory stronger than the former but experimental validation not as comprehensive as the 6.67 RECOMBINER.

---

## Summary

This paper proposes a learnable Gray-Wyner Network (GWN) for multi-task compression, introducing three channels (one common, two private) to disentangle shared and task-specific information. The authors provide theoretical bounds relating lossy Gács-Körner and Wyner common information via interaction information (Theorem 1), derive a learnable optimization objective balancing transmit and receive rates via a parameter β (Theorem 2), and design a neural architecture with a mask-based fusion mechanism. Experiments on synthetic data, colored MNIST, Cityscapes, and COCO demonstrate the transmit-receive tradeoff and show BD-rate improvements over independent single-task coding, while approaching joint-coding performance.

## Strengths

- **Genuine theoretical contributions bridging classical and neural compression.** Theorem 1 extends lossless common information bounds to the lossy setting, providing an inequality chain (Eqs. 6–7) relating C and K through interaction information. Theorem 2 translates the Gray-Wyner objective into an entropy-based form (Eq. 10) amenable to learning. These are well-motivated and correctly situate the architecture in information-theoretic foundations.

- **Principled tradeoff control demonstrated empirically.** The β parameter in the Lagrangian (Eq. 12) directly controls the transmit-receive tradeoff, and Figure 3a verifies this: β=1 produces common-channel rates above empirical mutual information, β=2 produces rates below it, and β=3/2 interpolates between them. This is a clean validation of the theory's operational prediction.

- **Comprehensive edge-case analysis.** The colored MNIST experiments (Figure 4, three PMFs spanning fully dependent to fully independent) show the method adapts correctly across the full spectrum of inter-task dependency — collapsing to essentially one channel when tasks are fully dependent and to separate channels when independent. This is a strong functionality check.

- **Clear architectural ablation.** The comparison of Shared, Separated, and Combined encoder architectures (Section 4.1, Figure 3b) shows the proposed Shared design consistently outperforms alternatives, providing evidence that the two-branch encoder with mask-based fusion is not arbitrary.

- **Reasonable breadth of real-task evaluation.** Experiments cover semantic segmentation + depth estimation (Cityscapes) and object detection + keypoint detection (COCO), with consistent BD-rate improvements over independent coding and proximity to joint coding.

## Weaknesses

### Fatal
None.

### Major
- **Frozen task models limit the rate-distortion characterization.** In Section 4.3, pre-trained task models (DeepLabV3+, LRASPP, Faster R-CNN, Keypoint R-CNN) are appended to the synthesis transforms and kept fixed during codec training. Compression artifacts may affect these frozen models in ways no amount of codec training can mitigate, and the paper itself notes an "increase in distortion with the lowest compression" attributed to lack of regularization — indicating the training setup is suboptimal. While baselines are evaluated under the same constraint, the absolute rate-distortion curves may not reflect the true relative merits achievable with joint fine-tuning. This weakens the practical significance claims for the real-task experiments.

- **No direct comparison with published multi-task compression methods.** The paper cites Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) as prior multi-task codec work but never uses them as baselines. While the Joint baseline (single shared channel) captures the essential design of those methods (common channels without private channels), directly comparing against published implementations would strengthen the empirical case and help readers situate the contribution within the existing literature.

### Minor
- **The theory-experiment connection is incomplete.** Theorem 1 establishes bounds relating C and K through interaction information, but none of these quantities — C, K, interaction information, or the gap between them — are estimated or measured in experiments. The β tradeoff is tested and works as predicted, which validates Theorem 2's practical utility. However, the claim that the architecture "separates common and private information" remains unverified by any information-theoretic measurement, probing, or visualization of what Y₀ actually encodes.

- **The mask-based fusion mechanism (Eq. 14) lacks ablation.** Zeroing out mismatched elements of Y₀⁽¹⁾ and Y₀⁽²⁾ is a strong, potentially lossy operation. The paper acknowledges that γ must be tuned and that the scheme can fail, but provides no ablation comparing alternative fusion strategies (e.g., soft attention, averaging, learned gating) or quantitative study of how often elements match vs. get zeroed. The design choice is reasonable but the evidence that it works well rather than incidentally is thin.

- **The Shared architecture's advantage over Separated and Combined is only shown on the synthetic dataset.** The architectural ablation (Figure 3b) is limited to Section 4.1; the real-task experiments (Section 4.3) only evaluate the Shared variant. Showing that the architectural advantage transfers to Cityscapes/COCO would strengthen claims about the design.

### Trivial
- The abstract and conclusion highlight the –81.58% BD-rate figure against independent single-task codecs, while the more informative comparison against the Joint baseline (23.32% on Cityscapes) receives less emphasis. The abstract does specify "against single-task codecs," so this is not misleading, but the framing could more prominently feature the Joint comparison which represents a more realistic lower bound on practical gains.

## Nice-to-Haves
- Estimating C, K, or interaction information empirically (e.g., via MINE or probe classifiers) would close the theory-experiment loop and substantiate the claim that the common channel carries common information.
- Jointly fine-tuning the task-specific models with the codec, or reporting results with a lightweight codec-plus-task pipeline, would yield a more realistic rate-distortion characterization.
- Extending the architectural ablation (Shared vs. Separated vs. Combined) to the real-task experiments would validate the design choice beyond the synthetic setting.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Weak baselines undercut the evidence" (Harsh Critic #1, originally framed as fatal):** The Joint baseline captures the essential design of existing multi-task codecs (common channels without private channels), and the Independent baseline represents the other extreme. The paper's contribution is precisely about the three-channel Gray-Wyner approach sitting between these endpoints. This is a valid design choice, not a fatal omission. Retained in weakened form as a Minor weakness about missing direct comparisons with published implementations.

- **"Theory completely disconnected from experiments" (Harsh Critic #2, originally framed as major):** The β parameter is derived from Theorem 2 and directly tested in Figure 3a, showing the predicted tradeoff behavior. The disconnect is limited to not measuring C, K, and interaction information — which is a limitation, not a complete disconnect. Retained as Minor.

- **"Masked combination is purely heuristic" (Harsh Critic #3, originally framed as major):** The paper explicitly discusses the mechanism's limitations (γ tuning, potential collapse) and positions γ=1, β-tuning as the practical solution. The operation is designed to enforce common information separation. Retained as Minor (requesting ablation).

- **"Overstatement of gains" (Harsh Critic #5, originally framed as major):** The abstract states "against single-task codecs," which is accurate. The –81.58% is a real number measured against Independent. The paper also reports the Joint comparison (23.32%). Demoted to Trivial as a framing preference.

- **"No confidence intervals or error bars" (Harsh Critic, section-by-section notes):** Single-run evaluation is standard practice in learned compression benchmarks at this scale. Moved to Removed as a field-standard practice.

- **"The derivation from Gray-Wyner objective to Lagrangian contains leaps" (Harsh Critic, section notes):** Theorem 2 provides the formal bridge, and the Lagrangian relaxation is standard practice in rate-distortion optimization (as the paper notes, citing Tishby et al. and Hiriart-Urruty & Lemaréchal). The derivation is mathematically sound.

- **"Accuracy sum is not easily interpretable" (Harsh Critic, section notes):** Combining mIoU and scaled inverse depth RMSE is pragmatic and common in multi-task evaluation; the paper explicitly describes the scaling. Not a substantive issue.

- **Strength Finder — removed generic strengths:** Claims about "the problem being important" or "architecture aligned with theory" without specific evidence are not included as standalone strengths.

## Novel Insights

The paper's key insight — that the gap between Wyner's and Gács-Körner common information, characterized through interaction information, implies a practically significant transmit-receive tradeoff that can be operationalized via a single scalar parameter β in a learnable codec — is genuinely novel. Prior work on coding for machines used two-channel (common + private) architectures without characterizing this tradeoff, and the information-theoretic literature on common information had not been connected to learnable compression in this way. The synthetic experiment (Figure 3a) cleanly demonstrates that β controls the common-channel rate relative to empirical mutual information exactly as the theory predicts, suggesting the Lagrangian formulation captures something fundamental about the Gray-Wyner region that gradient-based learning can exploit.

## Suggestions
- Add at least one direct comparison against a published multi-task codec (e.g., re-implementing the approach from Chamain et al. or Guo et al. as a stronger Joint-like baseline) to situate the work within the existing literature.
- Either jointly fine-tune the task models with the codec or provide a clear argument for why frozen-model evaluation is representative, particularly given the observed distortion increase at low compression.
- Ablate the mask-based fusion (Eq. 14) against simpler alternatives (e.g., element-wise averaging, learned weighted combination) to demonstrate the design choice is well-founded.
- Visualize or probe the common channel's content in at least one setting (e.g., colored MNIST) to provide qualitative evidence that it captures common rather than arbitrary information.

## Score and Decision

**Anchor comparison:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `gIrVoQEDQv` (NCA compression) | 3.40 | R1 | Clearly below — less novelty, narrower scope |
| `6j0GH40mFt` (Window attention LIC) | 3.40 | R1 | Clearly below — incremental architecture work |
| `aQ7qYnY2nF` (Task-aware video RL) | 4.00 | R1 | Below — limited novelty, narrow evaluation |
| `LnKDcqOfgy` (Quantization+compression) | 5.00 | R1 | Below — incremental combination of existing methods |
| `lpxcCD7WbQ` (Task adaptation) | 5.25 | R2 | Slightly below — less relevant, narrower contribution |
| `x33vSZUg0A` (Multi-task compression TAMC) | 5.33 | R1/R2 | Closest comparison — similar topic; this paper has stronger theory, similar baseline issues |
| `yVGGtsOgc7` (Disentangling via multi-task) | 5.80 | R2 | Slightly above — more comprehensive theory+experiments |
| `VkWbxFrCC8` (RECOMBINER) | 6.67 | R2 | Clearly above — more comprehensive experiments, stronger validation |
| `Tv36j85SqR` (Lattice Transform Coding) | 7.20 | R1 | Clearly above — deeper theory with direct empirical validation |

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowing:** The paper is slightly stronger than the TAMC anchor (5.33) due to its theoretical contributions, but clearly below RECOMBINER (6.67) in experimental comprehensiveness. Settled at 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>