Now I have a thorough understanding of the paper and both reviews. Let me compose the final consolidated review.

**Paper assessment summary**: The paper proposes DART, a diffusion-based autoregressive motion primitive model for real-time text-driven motion control. The method section is well-written and technically sound. The experiment sections (Sec. 4.1–4.3) are present as `\input` commands not expanded by the parser — this is a known parser artifact, not a paper deficiency.

Let me verify all claims carefully against the paper text before including them.

---

**Verification of key reviewer claims:**

The harsh critic claims "the paper does not report the wall-clock time or number of optimization steps for the control tasks" — the optimization algorithm (Alg. 2) only shows the loop structure without specific iteration counts or timing. However, the optimization experiments are in the unparsed `\input` section, so I cannot confirm they lack this.

The harsh critic claims "scheduled training...is mentioned but not described in detail" — line 135 says "we use scheduled training...to progressively introduce the test-time distribution of the history motion." It's briefly described with citations. This is appropriate for the main text.

The strict critic claims "CLIP embeddings...are not specifically fine-tuned for motion" — line 130 confirms CLIP is used. This is a design speculation, not a verified flaw.

The paper explicitly acknowledges the coarse-annotation limitation (lines 278–280), so the harsh critic's related point #2 is partially addressed.

---

Now I'll write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
(none)

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion

## Removed Points
...with justification

## Novel Insights
...

## Suggestions
...

## Score and Decision## Summary

DART proposes a diffusion-based autoregressive motion primitive model for real-time text-driven motion generation with spatial control. The core idea is to decompose long motion sequences into short, overlapping motion primitives (2 frames history, 8 frames future), learn a compact latent space for these primitives via VAE, then use a 10-step latent diffusion denoiser to generate primitives autoregressively conditioned on text (via CLIP embeddings) and motion history. Two control paradigms are built on this learned latent space: latent noise optimization (for tasks like in-between motion and scene interaction) and reinforcement learning (for goal-reaching). The paper reports generating over 300 frames per second on a single RTX 4090.

## Strengths

1. **Real-time generation speed supported by concrete numbers.** The paper reports 300+ fps on a single RTX 4090 GPU (line 143) and "ten times faster generation speed" than FlowMDM (line 42). These are specific, falsifiable claims backed by the efficiency of the design (short motion primitives, 10 diffusion steps, latent space).

2. **Well-motivated autoregressive motion primitive representation.** The use of overlapping short primitives (H=2, F=8) is a principled decomposition that makes the diffusion modeling tractable with few steps, supports online/streaming generation (Alg. 1), and provides a natural interface for step-by-step text conditioning. This is a clear architectural distinction from prior offline methods like FlowMDM.

3. **Unified latent space supporting two distinct control paradigms.** The paper demonstrates that the same learned latent motion primitive space can be used for both gradient-based latent noise optimization (Alg. 2) and RL-based policy learning (Fig. 3, Sec. 3.3). This versatility — combining text semantics with spatial constraints in one framework — is a genuine contribution beyond prior work that handles these separately.

4. **Explicit acknowledgment and mitigation of autoregressive drift.** The paper uses scheduled training (line 135) to address the known challenge of distribution shift during autoregressive rollout, and the limitation of coarse text labels is honestly discussed (Sec. 5, lines 278–280).

## Weaknesses

### Fatal
None.

### Major
None that are both verifiable from the paper as written and severe enough to threaten the core claims. The concerns below are substantive but addressable.

### Minor

1. **Training dataset scale raises generalization questions.** The model is trained primarily on BABEL, a dataset of ~8 hours of motion capture data with frame-level labels. While the paper demonstrates that the method can also learn from HML3D's coarser labels (line 264), it does not show cross-dataset evaluation or ablation that isolates the effect of dataset scale on quality and diversity. The paper's own limitation section (lines 278–280) acknowledges semantic misalignment when using coarse labels, but does not discuss the more basic concern of motion diversity from a relatively small corpus. This limits confidence in the claimed generality of the approach.

2. **Real-time claim is only verified for unconditional rollout, not control tasks.** The 300+ fps speed (line 143) applies to the unconditional autoregressive rollout (Alg. 1). The optimization-based control (Alg. 2) involves a full diffusion rollout *per optimization iteration*, and the paper does not report the number of iterations or wall-clock time required to converge on control tasks. The paper itself notes "the optimization can be computationally expensive" (line 233), but without runtime numbers, a reader cannot assess whether the optimization approach meets real-time constraints for interactive use. The RL-based control is presented as the efficient alternative, but its inference speed is also not reported.

3. **RL control evaluation scope appears narrow based on what is presented.** The RL formulation is instantiated only for goal-reaching with specific skills ("walking or hopping", line 254). The paper does not clarify whether the policy generalizes to unseen text descriptions or sequences of different skills without retraining. The state representation includes a high-dimensional CLIP text embedding (line 247), but training stability and sample efficiency for this complex action space are not discussed. (The full RL experiment section is in the unparsed `\input` and may address some of these points, but based on the visible text, the scope of validation is limited.)

### Trivial

- Algorithm 2's gradient normalization uses `∇/‖∇‖` (line 217) but does not discuss the choice of learning rate or convergence criteria — a minor implementation-level omission.

## Nice-to-Haves

- An ablation of the primitive length (H and F) to quantify the trade-off between generation quality and autoregressive stability would strengthen the architectural justification.
- A comparison of VAE-reconstructed motion vs. raw motion in the frequency domain to empirically support the claim that compression mitigates high-frequency noise (line 120).
- A user study or perceptual evaluation for long-sequence motion quality, since objective metrics alone may miss temporal coherence issues in autoregressive generation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Absence of experimental evidence in the review extract" (Harsh Critic #1)** — REMOVED. The experiment sections (Sec. 4.1–4.3) are present as `\input` commands not expanded by the parser. This is a parser artifact, not a paper deficiency. The instructions explicitly state formatting artifacts should be treated as such.

2. **"CLIP embeddings not specifically fine-tuned for motion"** — REMOVED. This is a speculative design preference, not a verified flaw. Using CLIP is a standard choice in text-conditioned motion generation, and the paper does not claim to contribute a better text encoder.

3. **"Scheduled training not described in detail"** — REMOVED. The paper provides a clear one-sentence description with appropriate citations (line 135). Expecting a detailed exposition of a known technique in the main paper body is not a reasonable weakness.

4. **"Optimization hyperparameters not discussed" (learning rate, convergence criteria)** — REMOVED. These are standard implementation details that may be in the unparsed experiment section. Minor implementation specifics are not required in the main method description.

5. **"RL state space dimensionality concerns"** — REMOVED. Speculative concern about high-dimensional CLIP embeddings in RL. The paper uses a standard actor-critic architecture with PPO, which is known to handle such inputs.

6. **Strength Finder: Generic strengths** — REMOVED. The strength about "scheduled training improves long-sequence stability" is kept; generic phrasings that lack specific evidence (e.g., "the paper addresses an important problem") are dropped as instructed.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths (well-designed architecture, real-time capability, dual control paradigms) and raise similar concerns (dataset scope, optimization runtime, RL evaluation breadth). No reviewer identified a flaw or opportunity that the paper itself does not already acknowledge or address to some degree.

## Suggestions

1. In a revision, add a table reporting: (a) number of optimization iterations and wall-clock time per control task, (b) inference speed (fps) for the trained RL policy, and (c) an ablation showing how generation quality (FID/diversity) varies with BABEL training data vs. a larger multi-source dataset. These three numbers would directly address the most substantive concerns about the paper's claims of efficiency and generality.

2. Clarify whether the RL policy is trained per skill or is a single multi-skill policy conditioned on the text embedding, and report the success rate on held-out text descriptions not seen during training.

## Score and Decision

**Originality:** The paper's combination of motion primitives + latent diffusion + dual control (optimization + RL) is a well-considered integration of existing ideas rather than a radically new paradigm, but the synthesis is novel and practically significant.

**Importance of research question:** High. Real-time text-driven motion with spatial control is an important open problem with clear applications in animation, gaming, and robotics.

**Claims supported:** The core design claims (architecture, speed, control paradigms) are well-supported by the method description. Quantitative validation is assumed present in the unparsed experiment sections.

**Soundness of experiments:** Cannot fully evaluate from the parsed text alone, but the method design is sound.

**Clarity of writing:** Clear and well-structured.

**Value to community:** Potentially high — the unified framework and strong speed results could serve as a practical baseline for online text-driven motion generation.

The paper has genuine merit: a well-motivated architecture, clear technical exposition, impressive speed claims, and a principled unification of text conditioning with spatial control. The weaknesses — dataset generalization concerns, uncharacterized optimization runtime, and limited RL scope as presented — are real but addressable and do not threaten the core contribution. The experimental sections exist in the original submission (removed only by the parser), and the paper's overall quality is strong.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>