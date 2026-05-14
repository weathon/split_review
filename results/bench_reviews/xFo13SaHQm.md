Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

## Summary

This paper addresses the "copy-paste" artifact in identity-consistent image generation—where models rigidly replicate reference faces rather than adapting to natural variations in pose, expression, and lighting. The authors contribute (1) **MultiID-2M**, a large-scale paired dataset of 500k group photos with reference images for ~3k identities; (2) **MultiID-Bench**, a benchmark that introduces a novel Copy-Paste metric (MCP) evaluating bias toward references vs. ground-truth; and (3) **WithAnyone**, a FLUX-based model using paired-data training, GT-aligned ID loss, and extended-negative contrastive learning to reduce copy-paste while maintaining identity fidelity. Experiments across 12 baselines show WithAnyone achieves the best SimGT (0.460) with the lowest CP (0.144) among face-customization methods, and user studies confirm perceptual superiority.

## Strengths

- **MultiID-2M fills a clear gap**: the dataset provides paired multi-identity images with diverse references per identity at 500k scale, surpassing all prior resources (Table 4). The four-stage curation pipeline (clustering, retrieval, matching, filtering) is well-documented and produces a resource that enables training beyond reconstruction-only paradigms (Section 3, Appendix C).

- **The Copy-Paste metric (MCP) is a genuine evaluation advance**: by measuring the relative bias of generated faces toward the reference vs. the ground truth, it exposes a failure mode that SimRef-based evaluation rewards. Figure 5 convincingly shows that most baseline methods trade off higher Sim(GT) against higher copy-paste, producing a clear fitted curve that the metric captures.

- **Methodologically coherent training recipe**: the combination of paired-data tuning (Phase 3), GT-aligned ID loss, and InfoNCE with extended negatives is well-motivated. The GT-aligned ID loss (using GT landmarks to align generated faces, Section 5.1) is a genuinely clever trick that enables ID supervision across all noise levels without the computational overhead of full denoising. Ablations (Table 3) confirm each component matters: removing Phase 3 increases CP from 0.161 to 0.239, removing extended negatives drops SimGT from 0.405 to 0.368.

- **Comprehensive evaluation with human validation**: 12 baselines across both general-purpose and face-specific models, tested on single- and multi-person subsets, plus OmniContext, plus a 10-participant user study ranking 230 groups. The user study (Figure 8, Appendix H) shows WithAnyone ranks highest on all four criteria. The CP metric's moderate correlation with human judgment (Pearson r=0.44, Table 7) is honestly reported.

- **Qualitative results are compelling**: Figure 6 shows clear advantages over baselines—WithAnyone generates faces that match the target identity while responding to prompts (smiling, head tilt, etc.), whereas competitors either copy the reference expression or lose identity. Generalization to non-celebrity identities (Figure 16) and robustness to low-quality references (Figure 15) are demonstrated.

## Weaknesses

### Fatal
None.

### Major

- **The "breaking the trade-off" claim overstates the evidence.** Figure 5 plots WithAnyone against 12 baseline models that were trained on different, often proprietary datasets—none on MultiID-2M. The fitted trade-off curve therefore conflates model quality with data quality. The paper cannot distinguish whether WithAnyone's position off the curve arises from the training strategy or simply from training on a larger, paired, better-curated dataset. The ablation removing Phase 3 (paired data) partially addresses this by showing that paired data reduces CP, but a single internal ablation cannot establish that the method "breaks" a fundamental trade-off that previous methods could not overcome if given equivalent data. The claim appears prominently in the abstract ("thereby breaking the long-observed trade-off") and conclusion (Section 7). This is addressable by scoping the claim more carefully—for example, to "substantially shifts the Pareto frontier under our training regime"—but as written it overstates what the experiments demonstrate.

### Minor

- **SimGT evaluates matching to a single ground-truth image, which conflates identity fidelity with scene reproduction.** The paper correctly argues that SimRef encourages copying, and SimGT is an improvement. However, SimGT rewards reproducing the specific pose, expression, and lighting of a single target image. While the CP metric separates reference-copying from GT-alignment, SimGT may still reward overfitting to a particular instance rather than flexible identity preservation. The paper partially mitigates this concern through OmniContext evaluation (which uses VLM-based scoring rather than GT matching) and user studies, but the core benchmark remains tied to a single GT target per sample.

- **Moderate CP-human correlation is honestly reported but limits strong metric claims.** The Pearson r of 0.44 (Table 7) indicates the CP metric captures some but not all perceptually meaningful variation. The paper acknowledges this as "moderate" and does not overclaim, but the benchmark's authority would be strengthened by analyzing failure modes where CP disagrees with human judgment.

- **No failure case analysis.** The paper shows only successful outputs. Including cases where copy-paste persists or identity is lost—and analyzing whether the CP metric correctly scores these failures—would build trust in both the method and the benchmark.

### Trivial

- The paper could benefit from a brief discussion of whether celebrity likeness rights are fully respected under the chosen CC licenses, beyond the general ethical statement provided.

## Nice-to-Haves

- Retraining a representative baseline (e.g., PuLID or ID-Patch) on MultiID-2M would provide a clean controlled comparison separating data effects from method effects. This is not required to validate the paper's contributions but would strengthen the trade-off claim.
- A small quantitative benchmark of non-celebrity identities would complement the qualitative results in Figure 16.
- Evaluation on open-ended prompts without GT images would probe generalization beyond the benchmark's strong coupling to a specific target.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim about DynamicID exclusion**: The paper explicitly notes (Section 2, footnote 1) that DynamicID is excluded "due to unavailability of code and pretrained models." This is a standard practice and not a weakness of the paper. Removed.

2. **Harsh critic's concern about "GT-aligned ID loss teaching the model to expect faces easy to align with GT's landmarks, potentially reducing pose diversity"**: The paper shows in Figure 7 and Table 3 that GT-aligned ID loss improves identity similarity without evidence of reduced diversity. The CP metric would detect increased copying if pose diversity were suppressed. This is speculative and unsupported. Removed.

3. **Strength Finder claim about "Robust generalization and practical usability" based on qualitative figures alone**: While the qualitative results are compelling, this strength as stated is too generic. The user study is stronger evidence. Kept the user-study strength but removed the overly broad generalization claim.

4. **Harsh critic's complaint about GPT-4o explanation being "speculative"**: The paper's discussion (Appendix F.3) about GPT-4o's prior knowledge of TV series identities is a reasonable, acknowledged hypothesis, not presented as a proven fact. The paper uses this observation to validate the CP metric design. Removed as a weakness.

5. **Harsh critic's concern about the ablation of Phase 3 being a "compound intervention"**: The ablation removes paired data and changes the data proportion. This is inherent in any ablation of a training phase. The paper reports what changes, and the effect direction (increased CP) is clearly interpretable. Removed as overly picky.

6. **Strength Finder's generic strengths about "important problem" or "interesting question"**: These are too generic and lack specific citations. Removed.

## Novel Insights

The paper's key insight—that reconstruction-based training in identity customization creates a copy-paste failure mode measurable as bias toward the reference rather than the ground truth—is genuinely novel. The formalization of this as MCP = (θ_gt − θ_gr) / max(θ_tr, ε) is simple but effective, and the observation that prior SimRef-based evaluation systematically obscures this problem has implications beyond this paper. The GT-aligned ID loss trick (using ground-truth landmarks to align generated faces for ArcFace extraction during single-step denoising) is also a practical insight that could benefit other diffusion-based face generation methods.

## Suggestions

- **Rescope the trade-off claim.** Replace "breaking the long-standing trade-off" with language reflecting that WithAnyone substantially shifts the Pareto frontier under the proposed training regime, and acknowledge that the comparison is between methods trained under different data conditions. This addresses the major weakness without requiring new experiments.

- **Include a small failure case gallery.** Show 3-5 examples where WithAnyone still exhibits copy-paste or loses identity, and discuss whether the CP metric correctly scores them. This would build trust in both method and metric.

- **Add a brief discussion of when SimGT may be misleading.** For example, when the prompt legitimately calls for a different pose/expression than the GT image shows, high SimGT may not be the right objective. This would strengthen the evaluation narrative.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison to Paper Under Review |
|--------|-----------|----------|----------------------------------|
| CrossFaceID (XJ3T70nELl) | 2.67 | Reject | Dataset-only paper with 40K pairs, limited novelty, weak evaluation. Current paper has far larger dataset, full method, comprehensive evaluation. Much stronger. |
| FaceID-6M (yTq81RcKaw) | 3.50 | Reject | Dataset-only from LAION filtering, 6M pairs. Limited novelty ("curatorial"), narrow evaluation. Current paper has custom-constructed dataset, benchmark, and method. Stronger. |
| OSPA (MjRwoUNR6X) | 4.50 | Reject | Method for RL-free ID alignment. Has novelty but limited evaluation (30 ref images, no user study). Current paper has far more comprehensive evaluation. Stronger. |
| SIGMA-Gen (x2DWTywZ1i) | 5.00 | Accept (Poster) | Multi-ID with spatial constraints, synthetic dataset (27K). No user study, limited evaluation. Current paper has real-world data, user study, larger evaluation scope. Stronger. |
| OmniPortrait (DVmR3Ij0ap) | 5.50 | Accept (Poster) | Fine-grained portrait synthesis, 1M dataset. Outdated baselines, UNet-based. Current paper uses FLUX (DiT), evaluates against 12 modern baselines. Comparable to slightly stronger. |
| IC-Custom (gv2cr8kABL) | 6.00 | Accept (Poster) | Unified customization framework, 12K dataset, novel attention mechanism. Solid evaluation, human studies. Current paper has larger dataset, more baselines, addresses broader problem. Comparable. |

The paper under review is clearly stronger than the 2.67–5.00 range and slots naturally into the 5.50–6.00 range alongside OmniPortrait and IC-Custom. Its dataset (2M scale), benchmark innovation (CP metric), and comprehensive evaluation (12 baselines + user study) are stronger than OmniPortrait. Its overclaiming on the trade-off is a real but addressable weakness. Compared to IC-Custom (which got unanimous 6s), the current paper offers greater scale and a more clearly identified novel problem, but has a more pronounced overclaiming issue. I score it at 6.0—a solid accept with the expectation that the trade-off language will be tempered in revision. The dataset, benchmark, and method are all valuable contributions that advance the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>