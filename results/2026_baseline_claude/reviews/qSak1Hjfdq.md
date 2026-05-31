Now I have read the full paper. Let me write my review.

---

## Summary

This paper formalizes the **All-Day Multi-Scenes Lifelong VLN (AML-VLN)** problem, where a vision-and-language navigation agent must continually adapt across multiple scenes and diverse imaging environments (normal, low-light, overexposure, scattering) without catastrophic forgetting. The authors propose **Tucker Adaptation (TuKA)**, a parameter-efficient fine-tuning method that lifts adaptation into a high-order tensor space via Tucker decomposition, explicitly decoupling shared navigation knowledge (core tensor + encoder/decoder) from scene- and environment-specific experts. They further introduce a **Decoupled Knowledge Incremental Learning (DKIL)** strategy combining EWC-style regularization on shared components with orthogonal expert constraints, and build **AllDayWalker**, a lifelong VLN agent that outperforms state-of-the-art baselines on the proposed 24-task AML-VLN benchmark as well as on unseen scenarios.

---

## Strengths

- **Well-motivated and timely problem.** The catastrophic forgetting demonstration (Figure 2, forgetting rate reaching 79% after 10 sequential scenarios) is compelling evidence that lifelong VLN is a genuine and severe challenge. Extending VLN to dynamic real-world "all-day" deployment across scenes and illumination conditions is a practically important research direction.

- **Technically principled method.** TuKA's use of a 4th-order Tucker decomposition ($\mathcal{X} \in \mathbb{R}^{a \times b \times M \times N}$) to jointly represent shared navigation skills (core tensor), scene experts ($U^3$), and environment experts ($U^4$) is elegant and well-motivated. The dimensional alignment trick—reducing the 4th-order tensor to a 2D weight update via row-slicing of expert matrices—cleanly resolves how to reconcile high-order representations with 2D LLM backbone weights.

- **Comprehensive benchmark.** AllDay-Habitat covers 24 sequential scenarios (5 simulated × 4 environments + 2 real-world × 2 environments) with physically-grounded imaging degradation models (atmospheric scattering, shot+read noise, saturation clipping). Including real-world validation at two scenes substantially strengthens the work beyond purely simulation-based evaluation.

- **Strong empirical results.** AllDayWalker achieves 65% average SR versus 56% for the next-best baseline (SD-LoRA) and 11% average F-SR versus 18% (SD-LoRA), both substantial margins. The generalization experiment (Table 5) to 6 completely unseen scenarios shows 55% average SR versus 39–40% for top baselines, a 15–16% gap.

- **Thorough ablations.** The paper validates the choice of 4th-order over 3rd-order tensors (Figure 8, ~10–15% SR improvement), ablates each shared component ($\mathcal{G}$, $U^1$, $U^2$) in Table 3, and tests scaling to 30 tasks without noticeable degradation (Table 4).

---

## Weaknesses

### Fatal
None.

### Major

- **Expert retrieval quality is unvalidated.** At inference time, task-agnostic expert selection relies on cosine similarity between CLIP features of live observations and stored training-time features. This is a non-trivial component: if the scene or environment is misidentified (e.g., overexposed confused with scattering), the wrong expert is loaded and the whole decoupling benefit collapses. The paper presents no retrieval accuracy metric, confusion matrix, or ablation comparing oracle (task-id given) vs. predicted expert selection. Without this, it is unclear how much of the performance stems from TuKA itself versus the effectiveness of the retrieval step.

- **Insufficient theoretical justification for Tucker superiority.** The core claim—that a 4th-order Tucker tensor captures "multi-hierarchical knowledge" better than matrix-based MoE-LoRA—is supported only empirically (3rd vs. 4th order comparison). The intuition that the 4th-order structure naturally decouples two orthogonal dimensions (scene and environment) is sound, but a more formal argument (e.g., expressivity bounds, parameter efficiency analysis) would better establish *why* Tucker decomposition is the right inductive bias here rather than, say, a product-of-experts LoRA with separate scene and environment modules.

### Minor

- **Task ordering sensitivity is not ablated.** The benchmark randomizes task ordering, but the DKIL strategy (especially the EWC Fisher accumulation and expert inheritance) may behave differently under different orderings. A brief study of ordering sensitivity would strengthen the generalizability claims.

- **Inference memory cost is unquantified.** Storing CLIP vision features for every observed frame across all $M \times N$ scenarios requires non-trivial memory; this cost is not reported. Similarly, the paper does not discuss inference latency overhead from the two-step feature matching.

- **Real-world scenarios cover only 2 environments.** The five simulation scenes each have 4 environments (normal, scattering, low-light, overexposure), but the two real-world scenes are limited to normal and low-light. Scattering and overexposure in real-world settings—arguably the hardest environments—remain untested.

### Trivial

- In Eq. (8), $\text{Norm}(U) = U[i,:]/\|U[i,:]\|_F^2$ divides by the squared norm rather than the norm itself, which would not produce unit-norm rows; this appears to be a notation slip ($\|\cdot\|_F$ likely intended as $\|\cdot\|_2$).

---

## Nice-to-Haves

- A comparison of TuKA's number of learnable parameters vs. baselines for a fixed number of scenarios (not just at a fixed number of tasks) would make the parameter-efficiency claims more precise.
- An analysis of what the scene and environment experts learn (e.g., probing or visualization of $U^3$ and $U^4$ vectors) would provide insight into whether the decoupling is semantically meaningful.

---

## Novel Insights

TuKA's central insight—that the two-dimensional matrix update $\Delta W = BA$ of LoRA is structurally constrained to encode only a single hierarchy of shared/specific knowledge, while a Tucker-decomposed 4th-order tensor $\mathcal{X}$ naturally encodes two orthogonal hierarchies (scene and environment) in disentangled factor matrices while sharing a common core—is a genuinely novel and principled perspective on parameter-efficient fine-tuning for multi-axis continual learning. The observation that scene × environment creates a natural 2D grid of tasks that can be decomposed rather than flattened into a 1D sequence of task identities has implications beyond VLN, potentially for any multi-attribute continual learning setting.

---

## Suggestions

- Report expert retrieval accuracy (percentage of test steps that correctly identify scene and environment) and include an oracle experiment where task-id is provided at test time to isolate retrieval error from method error.
- Include a theoretical analysis comparing the expressivity of TuKA versus the best LoRA-MoE variants (e.g., showing that TuKA can represent any product-of-experts LoRA but not vice versa).
- Extend real-world experiments to include scattering and overexposure conditions, even informally, to validate the full benchmark's relevance to real deployment.
- Ablate task ordering (at least 2–3 different random orderings) to report variance in performance.

---

## Score and Decision

The paper makes a clear and technically solid contribution: a novel problem formalization, a principled method grounded in tensor algebra, a practically useful benchmark with real-world components, and strong empirical results with a large margin over a wide set of baselines. The main gap is the absence of retrieval accuracy analysis and stronger theoretical grounding, which are significant but not fatal. The work is above average in originality and execution for a VLN paper, with a well-crafted benchmark and compelling real-world validation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>