## Summary

This paper proposes MISA (Mask and Initial Session Adaption), a plug-in method for prompt-based general continual learning (GCL). MISA has two components: (1) a forgetting-aware initial session adaptation (ISA) that uses the pretraining dataset (ImageNet-1k) to warm up prompt parameters before GCL training, enhanced by forgetting-aware minimization (FAM) which perturbs prompts using gradients from out-of-distribution data; and (2) a non-parametric logit mask that zeros out logits of unseen classes at the batch or session level to reduce forgetting. Without any replay buffer, MISA outperforms the prior SOTA (MVP) by 18–22% in final accuracy across three benchmarks, with no additional parameters or significant runtime overhead.

---

## Strengths

- **State-of-the-art results without replay buffer, across three benchmarks (Table 1).** MISA surpasses MVP by 18.39%, 22.06%, and 11.96% in A_Last on CIFAR-100, Tiny-ImageNet, and ImageNet-R respectively with buffer size = 0. These are the largest reported gains in the GCL literature and directly support the paper's central claim of substantial performance improvement in replay-independent GCL.

- **Non-parametric logit masking delivers large forgetting reduction with no learnable parameters (Tables 2, 3).** The session-level and batch-level masks consistently outperform the learnable mask of MVP. For example on CIFAR-100 at batch size 32, the session-level mask achieves 52.27% vs. 43.11% for the learnable mask. Ablations (Table 2) confirm that the mask and ISA-FAM are complementary: the mask reduces forgetting, after which ISA-FAM becomes effective.

- **Plug-in nature validated on two distinct prompt-based methods (Table 5).** Applying MISA's components to L2P and MVP (without requiring them to perform ISA themselves) improves their ImageNet-R performance, supporting the claim that MISA is a general add-on.

- **No additional computational overhead despite large gains (Table 7).** MISA has comparable per-batch execution time (65 ms vs. 78 ms for DualPrompt) and adds no extra parameters, supporting the practical ease-of-implementation claim.

- **Robustness to pretraining data overlap (Table 6, Section 5.3).** Using a checkpoint that removes 389 ImageNet-1k classes similar to CIFAR-100/Tiny-ImageNet, and testing on a medical-domain dataset (NCH), the gains remain substantial. This demonstrates the performance is not driven by trivial class overlap.

---

## Weaknesses

### Fatal

None.

### Major

- **The core premise of FAM — that OOD-specific perturbation *direction* matters beyond generic flatness — is not causally validated.** The paper claims that FAM's perturbation direction (computed from gradients on a held-out subset of ImageNet-1k) simulates future forgetting and is meaningfully different from SAM's direction. However, the paper provides no control experiment comparing FAM against (a) random perturbation directions of the same magnitude, or (b) standard SAM with a larger neighborhood radius ρ. The improvement over SAM in Table 4 is modest (~1–2% by the reviewer's estimate; exact numbers are in the image-only table), and could plausibly arise from generic regularization. The distinguishing mechanism — that forgetting-specific directions are responsible — remains a hypothesis rather than a demonstrated fact. This does not invalidate the paper's overall contribution (ISA + logit masking already drives most of the gains), but it weakens the novelty claim attached to FAM specifically.

### Minor

- **Knowledge overlap analysis is partially but not fully clean.** The experiment in Section 5.3 uses a backbone checkpoint pretrained without 389 classes overlapping with CIFAR-100/Tiny-ImageNet — but ISA *still uses the full ImageNet-1k dataset* (1000 classes) in both conditions (line 142: "our ISA uses the ImageNet-1k dataset"). Only the backbone changes. This means the prompt parameters are warmed up on data that may contain class-relevant information about the downstream tasks. A stronger test would perform ISA using a completely disjoint subset of ImageNet-1k (or a different pretraining dataset). The medical-domain NCH result (~20% A_Last, Figure in Table 6) provides some reassurance but the absolute accuracy is low, making it hard to disentangle domain difficulty from genuine transfer.

- **FAM's neighborhood radius ρ is not specified and no sensitivity analysis is provided.** The implementation details (Section 5.1) describe the ID/OOD split ratio (900/100) and the resampling strategy, but do not report the value of ρ used. Combined with the absence of sensitivity analysis for ρ and the ID/OOD ratio, this makes it difficult to assess how robust the method is to these choices. The paper's claim of "avoidance of CL-relevant hyperparameters" is technically accurate (ρ is not CL-specific), but the omission is notable.

- **Batch-level logit masking fails at batch size = 1 (Table 3).** This is acknowledged as "out of the scope of this paper" (line 181), and the paper recovers with a replay buffer. Still, for streaming online learning settings where batch size 1 is the norm, this is a practical limitation that warrants a brief discussion or suggested workaround (e.g., a FIFO queue of recent labels).

### Trivial

None.

---

## Nice-to-Haves

- **Validate FAM with controlled baselines:** Comparing FAM against random perturbation directions (same magnitude) and SAM with larger ρ would causally establish whether the OOD-gradient direction matters.
- **Cleaner ISA leakage analysis:** Perform ISA exclusively on the non-overlapping subset of ImageNet-1k classes, paired with the corresponding backbone checkpoint.
- **Sensitivity analysis for FAM hyperparameters** (ρ, ID/OOD split ratio) on a validation task such as CIFAR-100 without buffer.
- **Oracle upper bound** (e.g., using perfect task/class knowledge) to calibrate remaining room for improvement.

---

## Removed Points

These points were flagged for removal and should be treated with caution:

- **"The effectiveness of logit masking... is an observation, not a demonstrated mechanism"** — The paper provides a reasonable justification (stable representation space from frozen backbone, Section 4.3). The claim is not a central theoretical assertion requiring a separate mechanism experiment.
- **"Prompt augmentation description is unclear"** — Section 4.2 (line 113) clearly states the MLP is trained jointly during ISA, then discarded, and p_e' is stored.
- **"No comparison with theoretical lower bounds"** — This is a nice-to-have, not a weakness.
- **"Transferability experiment note about prompt initialization"** — The paper already acknowledges this (line 193: "Note that these methods share the same initialized prompts parameters as our approach, without performing additional ISA").
- **"Pure formatting/style nitpicks"** from the harsh critic — Removed per policy.
- **Strength Finder: generic/superficial strengths** (e.g., "this paper addressed an important problem") — Removed. Only concrete, evidenced strengths retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful methodological insight: the FAM perturbation direction claim needs a causal control (random directions vs. OOD-gradient directions) to separate generic flatness benefits from forgetting-specific robustness. This is a clean experimental design point that strengthens the paper's conceptual framing if validated, but it is the authors' own framing — not a novel observation from outside.

---

## Suggestions

1. **Add a control experiment for FAM:** Compare against random-perturbation SAM and SAM with larger ρ on CIFAR-100 without buffer. If FAM still outperforms both, the direction claim is supported; if not, reframe FAM as a practical variant of SAM for the ISA setting.
2. **Specify ρ and add sensitivity analysis** for the neighborhood radius and ID/OOD split ratio.
3. **Clean the knowledge leakage analysis:** Run ISA on only the 611 non-overlapping ImageNet-1k classes, paired with the filtered backbone. Even if performance drops slightly, demonstrating the method is robust to this stricter condition would significantly strengthen the paper.
4. **Discuss the batch-size-1 limitation** of the batch-level mask more explicitly, and suggest a simple workaround (e.g., a FIFO queue of recently observed class labels).

---

## Score and Decision

**Originality:** Moderate. ISA + logit masking is a simple and effective combination; the FAM component is a plausible modification of SAM but its novelty is partially unvalidated.

**Importance of research question:** High. Replay-independent GCL is practically important and underexplored with prompt-based methods.

**Claims supported:** Mostly well-supported for the overall MISA method. The FAM-specific claim (forgetting-aware directions matter) is weaker than the empirical result.

**Soundness of experiments:** Good. Comprehensive benchmarks, proper ablations, transferability test, and overlap analysis. The main gap is the missing FAM control experiment.

**Clarity of writing:** Clear and well-structured.

**Value to the community:** High. MISA provides a strong replay-independent baseline and the plug-in components are easy to adopt.

This is a strong paper with clear empirical contributions. The main weakness — incomplete causal validation of the FAM direction claim — is bounded and does not undermine the core results (ISA + logit masking drive most of the gains). The paper sets a new SOTA for replay-independent GCL and the components are well-validated independently.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>