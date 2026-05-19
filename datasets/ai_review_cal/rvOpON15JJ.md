- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary
This paper proposes Diffusion Implicit Policy (DIP), a framework for scene-aware human motion synthesis that eliminates the need for paired motion-scene training data. The approach disentangles motion prior learning (via a diffusion model trained on unpaired AMASS data) from scene interaction (via reward functions as an implicit policy at inference). At each denoising step, the sampling distribution centroid is adjusted in a GAN-inversion manner to improve interaction plausibility while preserving motion naturalness. The system also incorporates ControlNet-based keyframe control, motion inpainting for historical constraints, and rotation-power-space motion blending for multi-task sequences.

## Strengths

1. **Novel and well-motivated unpaired framework.** The core idea — training a motion diffusion model without any scene-conditioned data and steering it at inference via reward-based implicit policy — is a clear and valuable contribution. The paper correctly identifies the scarcity of paired motion-scene data as a limiting factor and proposes a principled solution. The framework is demonstrated on synthesized ShapeNet scenes, PROX, and Replica without retraining.

2. **Competitive quantitative and perceptual results.** In locomotion (Table 1), DIP achieves the shortest finish time (3.35s), closest final distance (0.03m), and lowest penetration (0.95). In interaction tasks (Table 2), it obtains the best mean/max penetration and contact scores. The user study (Table 3) shows DIP ranking first in diversity, interaction plausibility, and overall performance on PROX and Replica scenes. These results support the claim that an unpaired approach can match or exceed paired methods.

3. **Technical novelty in the GAN-inversion-style distribution adjustment.** Optimizing the sampling distribution centroid via the predicted original motion $\hat{x}_0^\varphi$ rather than directly modifying $\mu_t$ (Section 3.5, Eq. 14) is a technically grounded contribution that addresses motion continuity concerns in prior implicit-policy work. The combination of this with the fully differentiable motion representation enables gradient-based optimization of interaction rewards through the diffusion process.

4. **Principled multi-task synthesis pipeline.** The system integrates keyframe control via ControlNet, motion inpainting for historical constraints, and rotation-power-space blending (§3.6) into a coherent pipeline for long-term multi-task motion synthesis without paired training data — a combination that is non-trivial and practically useful.

5. **Evaluation on diverse scene types.** The method is tested on synthetic scenes (ShapeNet), real scans (PROX), and reconstructed environments (Replica), using both automatic metrics and a 15-participant user study, demonstrating generalization across scene domains.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance reported for any quantitative result.** The paper reports all numerical results (Tables 1, 2, 3) as point estimates without standard deviations, confidence intervals, or significance tests. This is especially problematic for the user study (Table 3), where the between-method differences are small (e.g., naturalness scores for DIP and DIMOS appear close) — without variance information, the reader cannot assess whether the reported advantages are meaningful or within noise. The claim that DIP "presents better motion naturalness and interaction plausibility than cutting-edge methods" is not convincingly supported without knowing whether these differences are statistically significant.

2. **Key design choice stated but not ablated in the main text.** The paper claims (Section 3.5, line 169) that "optimizing $\hat{x}_0^{\varphi}(\mu_t, t-1, c)$ shows better performance than directly modifying $\mu_{t}$ itself" — this is a central technical claim that directly justifies the GAN-inversion analogy. Yet no quantitative ablation for this choice appears in the main paper (only a reference to the supplementary). Without evidence, the reader must take this on faith, weakening the internal coherence of the method section.

3. **Contact metric inconsistency undermines the locomotion comparison.** The method optimizes foot vertex contact via $\mathcal{R}_{cont}$ and $\mathcal{R}_{skt}$, but the reported contact score (Eq. 3) is computed from foot joints. DIP scores lower on this metric (Table 1), and the paper attributes this to the metric-objective mismatch (lines 232-233). While the acknowledgment is commendable, the quantitative comparison for locomotion becomes ambiguous — DIP wins on some metrics, loses on contact, and visual claims of better foot contact are not quantified. Either a compatible metric or a separate vertex-based contact measurement is needed for a clean comparison.

### Minor

1. **Missing direct comparison with recent inference-time optimization approaches.** SceneDiffuser, LAMA, and AMDM are discussed in related work (Section 2) but not quantitatively compared against. Given that these are contemporaneous diffusion-based or optimization-based approaches to scene-aware motion synthesis, their absence limits the evaluation's timeliness and situates the contribution less clearly.

2. **Underspecified implementation details critical for reproducibility.** Several parameters are not reported in the main text: the number/selection of keyframes for ControlNet hints (line 118: "randomly select one from these joints in a few frames"), the inpainting threshold $T_{inpaint}$, reward weight hyperparameters $\lambda_{(\cdot)}$, inference-time denoising steps, and the diffusion architecture itself. While some may be in the supplementary, the main text should at least summarize these for a self-contained reading.

3. **LLM-based task decomposition mentioned but not demonstrated.** Section 3.2 describes decomposing commands into sub-tasks via LLMs, but the experiments appear to use manually defined task sequences. This creates a disconnect between the described capability and the evaluated system. Clarifying whether LLMs were used and, if not, scoping the claim accordingly would improve honesty.

4. **No discussion of failure cases or limitations.** The method relies on hand-crafted reward functions and may struggle in novel interaction scenarios (e.g., non-standard furniture geometries, multi-person scenes, dynamic scenes). Acknowledging such boundaries would strengthen the paper and help direct future work.

5. **User study protocol details are sparse.** The paper states 15 participants rated 20 sequences per method on 4 aspects, but does not describe whether raters were blind to method identity, whether presentation order was randomized, or how inter-rater reliability was assessed. These are standard reporting expectations for perceptual studies.

### Trivial

None of note.

## Nice-to-Haves

- A single key ablation in the main text (e.g., optimizing via $\hat{x}_0^\varphi$ vs. direct $\mu_t$ modification) would substantially strengthen the paper without requiring extensive space.
- Reporting error bars (e.g., standard deviation across different random seeds or bootstrapped confidence intervals) for Tables 1 and 2 would address the most significant statistical concern.
- A brief failure case analysis would improve completeness.

## Removed Points

These points from the input reviews were removed with justification:
- **"Contribution list is long and some items are enablers"** — Subjective framing preference; all three listed contributions are substantive and distinct.
- **"GAN Inversion analogy is indirect"** — The paper explicitly explains the analogy (lines 169-173) with a citation chain and an equation; the connection is adequately drawn.
- **"Unpaired framing is partially misleading"** — The paper consistently qualifies "no longer necessary" as referring to *training* (line 25, line 278). Every scene-aware method needs scene info at inference. The claim is accurate.
- **"Conclusion overstates evidence"** — The phrasing "comprehensive experiments...indicate the effectiveness" is standard for papers with competitive results; the real issue (missing variance) is already captured in Major weakness #1.

## Novel Insights

The reviews surface an interesting tension not explicitly discussed in the paper: the method's strength (unpaired training) also creates an evaluation challenge. Because DIP uses reward functions that differ from standard metrics (e.g., foot vertex contact vs. foot joint contact), the quantitative comparison becomes less clean than a paired method where metrics and objectives are aligned. This is a general issue for unpaired/implicit-policy approaches that future work should consider — designing evaluation metrics that match the inductive biases of the method, or providing both standard and method-specific metrics to separate measurement artifacts from genuine improvements.

## Suggestions

1. **Add variance information** to all quantitative tables (standard deviations across runs or bootstrapped confidence intervals). For the user study, report standard deviations and consider a significance test (e.g., Wilcoxon signed-rank or paired bootstrap) for the comparisons where DIP claims superiority.
2. **Move a single key ablation to the main text** — specifically the comparison between optimizing via $\hat{x}_0^\varphi$ vs. direct $\mu_t$ modification, which directly validates the claimed novelty.
3. **Address the contact metric issue** by computing an additional foot-vertex-based contact score or explaining why the joint-based metric systematically disadvantages DIP. If vertex-based contact truly differs, report it.
4. **Include summary statistics for key hyperparameters** (number of ControlNet hint frames, $T_{inpaint}$, $\lambda$ values, inference steps) in the main text or a table.
5. **Add a limitations paragraph** discussing scenarios where the hand-crafted reward functions may fail.
