Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes using a pretrained motion diffusion model (MDM) as a generative prior for three forms of composition: sequential (DoubleTake for long sequences via inference-time handshaking and refinement), parallel (ComMDM for two-person interaction via a slim communication block between frozen priors), and model composition (DiffusionBlending for fine-grained joint/trajectory control by generalizing classifier-free guidance across independently fine-tuned models). The core insight—that the diffusion prior serves as a proxy for the human motion manifold, so new tasks only need to coordinate or blend at inference/fine-tuning time—is sound and addresses genuine data-scarcity obstacles.

## Strengths

- **DoubleTake enables zero-shot long-sequence generation that outperforms a dedicated prior method (TEACH) on BABEL.** The paper reports substantially lower FID on both interval and transition evaluations (Table 1), using a model trained only on short clips, without task-specific training. The ablation on HumanML3D (Table 2) systematically validates the design choices (soft masking, handshake size).

- **ComMDM generates credible two-person motion with only 10 training examples and wins a user study against prior work.** A user study with 30 participants shows ComMDM preferred over MRT and unmodified MDM across interaction level, completion, and overall quality (Figure 8). This supports the claim that a lightweight communication block enables few-shot multi-person generation.

- **DiffusionBlending provides accurate fine-grained joint/trajectory control where standard inpainting fails.** Table 4 (control table) shows that fine-tuned models and their blends substantially reduce control error (e.g., left wrist error 0.032 vs. 0.050 for inpainting; trajectory error 0.196 vs. 0.348). The method cleanly extends classifier-free guidance to compose independently fine-tuned models with no additional training.

- **The soft-masking mechanism in DoubleTake's second take is a principled and effective refinement.** The formalism in Section 3.1 allows partial refinement of transitions, with qualitative evidence (Figure 9/related) showing visible improvement over the first take.

- **The paper is transparent about limitations** (Conclusion, Section 4.2), acknowledging ComMDM's limited generalization and the early-stage nature of the approach.

## Weaknesses

### Fatal

None.

### Major

- **The BABEL comparison (DoubleTake vs. TEACH) conflates DoubleTake with an auxiliary Transition Embedding, making the headline improvement uninterpretable.** The paper adds a Transition Embedding to the MDM base model trained on BABEL (Section 4.1: "we choose to embed each frame with transition embedding signal... We then add this embedding to the frame's features"). This embedding is part of the MDM model that DoubleTake operates on, but TEACH—the dedicated baseline trained on the same data—does not have access to such a signal. Because no ablation isolates DoubleTake from the Transition Embedding, the reported FID gains could partly or wholly stem from the embedding rather than from DoubleTake's composition mechanism. The paper should either (a) train MDM for BABEL without the embedding and recompute, or (b) ablate the embedding's contribution on BABEL. This does **not** invalidate the full-system comparison (MDM+TE+DoubleTake vs. TEACH is a valid system-level comparison), but it does mean the paper's framing ("DoubleTake outperforms TEACH") overclaims what is specifically attributable to the proposed composition method.

- **The two-person text-to-motion claim rests on evidence that is too thin to support the stated contribution.** The paper claims "textually driven two-person motion generation for the first time" (Section 3.2/4.2) but provides only qualitative examples from a dataset of 5 textual annotations trained on 14 motions. No quantitative metrics (FID, R-precision, diversity) are reported for text-to-motion, no baseline comparison is given, and the paper itself acknowledges "generalization is fairly limited to interactions from the same type seen during training." The user study (Figure 8) evaluates only **prefix completion**, not text-to-motion. While the prefix completion results are solid, the text-to-motion capability is essentially a demonstration without the evidence needed to validate it as a contribution.

### Minor

- **The "10-minute long fluent motions" claim (Introduction) is not supported by any experiment or analysis in the paper.** The quantitative evaluation is on 32-interval sequences, and no specific long-sequence visualization, runtime, or quality analysis of a 10-minute generation is presented. The paper would benefit from either showing such a result or tempering the claim.

- **DiffusionBlending is not compared against a single model fine-tuned jointly on both control signals.** The core motivation of DiffusionBlending is that training a separate model for every combination is suboptimal. However, the paper only compares blended models against the inpainting baseline, not against a single model fine-tuned on both controls simultaneously (e.g., one model trained on trajectory+left wrist). A comparison against this baseline would strengthen the argument for composition over joint training.

- **Sensitivity analysis for DoubleTake's hyperparameters is limited.** Only one ablation table (HumanML3D, Table 2) is provided; the BABEL results use a single set of hyperparameters ($T'=700$, $M_{hard}=0.85$, $M_{soft}=0.1$, $b=10$) without justification or sensitivity sweeps. Given that the method depends on several parameters (handshake length, soft mask values, number of refinement steps), more analysis would help.

### Trivial

- No runtime or inference cost is reported for any of the three methods. For a paper proposing inference-time methods, this information would be practically useful.

## Nice-to-Haves

- A direct comparison of ComMDM on a quantitative text-to-motion metric (even computed on a held-out subset of the limited data) would strengthen the two-person generation section.
- The user study description could clarify whether comparisons were randomized and whether users were experts or laypeople.
- A video supplement showing long DoubleTake sequences and two-person text-to-motion results would substantiate claims that currently rely on static figures.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Fine-tuning algorithm presented as novel without citing similar approaches"** — REMOVED because it is factually wrong. The paper explicitly cites Rombach et al. (CVPR 2022) at line 228: "Consequently, inspired by \citet{Rombach_2022_CVPR}, we introduce a fine-tuning process..." and cites Ho & Salimans for classifier-free guidance.

2. **"ComMDM not entirely novel — similar approaches exist in image generation"** — REMOVED. This is a generic observation about transferring ideas across domains, not a specific weakness of this paper. The paper does not claim architectural novelty for ComMDM; its contribution is applying the idea to motion with extremely few examples.

3. **"Reproducibility details: missing hyperparameters"** — REMOVED. The paper gives the key hyperparameters (handshake length, mask values, $b=10$, batch size 64, training steps for each method, etc.). The level of detail is appropriate for a conference submission.

4. **"Section 4.2 — Table 3 reports L2 error which the paper itself criticizes"** — REMOVED as a weakness. The paper explicitly acknowledges L2's limitations and then uses a user study to compensate. This is a valid methodological choice, not a flaw.

5. **Pure formatting nitpicks (Figure 5 legibility, unclear capitalization, etc.)** — REMOVED per formatting rules (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The reviewer discussions surface the Transition Embedding confound sharply, but this is best handled as a targeted ablation request rather than a novel observation.

## Suggestions

1. **For the BABEL comparison:** Add an ablation that trains MDM on BABEL *without* the Transition Embedding and runs DoubleTake on that model. This cleanly isolates DoubleTake's contribution from the embedding's.
2. **For two-person text-to-motion:** Either (a) provide quantitative metrics on a small held-out set, or (b) explicitly reposition the text-to-motion results as preliminary demos and reduce the strength of the claim.
3. **For DiffusionBlending:** Add a comparison against a jointly fine-tuned model (single model trained on both controls). This directly tests the composition argument.
4. **Support the "10-minute" claim** with at least one concrete example—even in supplementary material—or temper the claim to match what is actually evaluated.

## Score and Decision

The paper's core insight is sound and the methods are well-motivated. DiffusionBlending and DoubleTake (modulo the Transition Embedding confound) are demonstrated convincingly. However, the two major weaknesses—the uninterpretable BABEL comparison and the insufficiently supported two-person text-to-motion claim—prevent the paper from compellingly validating all three of its headline contributions at the level expected for a top venue. The paper is close but needs a targeted revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>