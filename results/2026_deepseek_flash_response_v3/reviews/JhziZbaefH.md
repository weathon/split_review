## Summary

This paper proposes OML, a brain-inspired hierarchical neural architecture for online multimodal learning that incorporates reference extraction (determining which features a word refers to), conflict detection between current input and prior knowledge, and human-in-the-loop interaction to resolve conflicts. The architecture uses feature neurons (FNs), unimodal association neurons (UANs), and multimodal association neurons (MANs) connected through ascending, descending, and lateral pathways. Experiments on small fruit image/audio datasets show OML outperforming some offline and online baselines on cross-modal retrieval tasks, particularly when augmented with color-referring words (Table 2) and when extending to a new taste modality (Table 3).

---

## Strengths

1. **Novel and well-motivated problem framing.** The paper identifies three capabilities missing from prior multimodal learning work — online continual learning, precise reference resolution (determining which part of a feature vector a word refers to), and interactive conflict detection with human-in-the-loop questioning. These are genuine gaps, and the high-level system design that addresses all three is ambitious and coherent.

2. **Conservative evaluation that favors baselines.** In Table 2, the paper explicitly notes that baseline methods "return all features (shape and color) of red objects" when only color is queried, and "we count this as a correct result for them." Similarly in Table 3, AEN returns concepts from both visual and taste channels when only one is correct, and the paper counts this as correct. This is *conservative* — it gives baselines credit for wrong answers, so the reported improvements for OML (which correctly disambiguates) are likely underestimates. This reflects well on the evaluation's fairness.

3. **Novel reference extraction mechanism.** The idea of using coefficient-of-variation across exemplars to infer which feature dimensions a word refers to (Section 3.4) is conceptually interesting. Table 2 provides evidence that OML maintains accuracy on datasets with attribute-referring words while offline methods collapse (marked by ↓) and comparable online methods cannot distinguish name words from attribute words.

4. **Complete system with demonstrated modality extension.** Table 3 shows OML extending to a new (taste) modality online and outperforming AEN across all 12 settings, suggesting the architecture's modular design can accommodate new input channels without full retraining.

---

## Weaknesses

### Major

1. **Eq. (1) is mathematically degenerate as written — the core neuron model does not produce an input-dependent signal.** The ascending activation of a feature neuron is:

   $$f_F^{\alpha_k} = \begin{cases} y^{\alpha_k} = \sum_{i=1}^n \sum_{t=1}^T w_{j,i} \cos \lambda_i^{\alpha_k} 2\pi \frac{t-1}{T}, & d(\mathbf{x}, \mathbf{w}_j) \leq \theta \\ 0, & \text{otherwise} \end{cases}$$

   For natural-number frequencies λ_i and T=150 (the value used in experiments), the inner sum ∑_{t=1}^T cos(λ_i·2π·(t-1)/T) equals 0 for all λ_i not divisible by 150, and equals T only for λ_i that are multiples of 150. Since each λ_i is assigned a unique natural number, at most *one* dimension per feature type can produce a non-zero signal. Therefore, y^{α_k} ≈ w_{j,i*}·T for whichever dimension i* (if any) has λ_i divisible by T, with no dependence on the input features x — the input only gates whether the neuron fires at all.

   This means the signal transmitted to higher layers (UANs and MANs) does not encode feature information about the input. The Fourier transform in Eq. (6) and the variance-based reference extraction in Section 3.4 operate on signals that are, per this equation, essentially constant. This is not a missing experiment or insufficient baseline — it is a problem with the specification of the fundamental computational unit. The paper as submitted does not provide a valid description of how the network processes input features, and without this, no experimental result can compensate. *(This could potentially be a notation error — e.g., if y^{α_k}(t) was intended to be a per-time-step vector and the sum over t is spurious — but the paper must be evaluated as written.)*

2. **No ablation study of any component.** The proposed system has numerous interacting components: the Fourier-based signal encoding, lateral connections between FNs, the reference extraction algorithm with its coefficient-of-variance heuristic (threshold r=0.5), conflict detection, question generation, and the human-in-the-loop update rules. None of these is ablated. The reader cannot determine which components drive the reported results, whether any are harmful, or whether a simpler alternative (e.g., a nearest-prototype classifier with online updates using the same features) would match or exceed performance. Given the complexity of the architecture and the small scale of the experiments, this omission is severe.

3. **Evaluation on tiny, undocumented datasets with no variance reporting.** The paper uses two small datasets (Fruits and HomeF, plus augmented versions) but never states dataset sizes, number of classes, per-class sample counts, or presentation orders. No standard deviation or confidence interval is reported for any result in Tables 1–3 — all numbers are point estimates with no indication of how many independent runs they are averaged over. For a method that creates new neurons dynamically and whose behavior depends on presentation order, single-run results on datasets of unknown size are anecdotal evidence at best.

4. **Conflict detection claim is unsubstantiated.** The paper states "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions" (line 250). This single sentence is the entirety of the evidence for the conflict detection capability — no precision/recall, no confusion matrix, no analysis of which types of conflicts are detected or missed, and no examples of the questions generated. For a paper that lists conflict detection as one of its three core contributions, this level of evidence is insufficient.

### Minor

1. **Fixed threshold r=0.5 in reference extraction with no sensitivity analysis.** The reference extraction algorithm (Eq. 7) uses a coefficient-of-variation threshold r=0.5 with no analysis of how this threshold affects performance. Different feature types may have different inherent variability, and a single fixed threshold could be suboptimal or brittle.

2. **Simulated human-in-the-loop evaluation.** The paper states "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive" (line 240). This means the "human interaction" experiments are conducted with an automatic positive response rather than actual human users or a realistic user model. While this is a reasonable starting point, it removes the key challenge of evaluating whether the generated questions are actually informative, unambiguous, or useful to a real user.

3. **UAN activation requires all connected FNs to fire simultaneously.** Eq. (3) requires ∀ W_{i,j}^{α_k}·e_j^{α_k} = 1 for the UAN to activate — i.e., *every* connected feature neuron must be active. This all-or-nothing gating may be brittle: a single missing feature (e.g., due to occlusion or noise) would prevent the entire concept from activating, and the paper provides no analysis of robustness to partial input.

4. **Unclear whether offline baselines are retrained or fine-tuned in the open environment.** The open environment divides the dataset into four parts from different classes. The paper does not specify whether offline methods are retrained from scratch on each new partition (a strawman comparison) or fine-tuned with appropriate continual learning modifications. This affects the interpretability of the "catastrophic forgetting" claims in Table 1.

### Trivial

- None.

---

## Nice-to-Haves

- Reporting statistical significance (standard deviations over multiple runs and presentation orders) would substantially strengthen the experimental claims.
- A comparison to a simple online baseline (e.g., a continually updating nearest-prototype classifier using the same Fourier descriptor + MFCC features) would be more informative than comparisons to deep Boltzmann machines designed for offline joint representation learning.
- A sensitivity analysis of the r=0.5 threshold in the reference extraction algorithm.
- A limitations section acknowledging the small scale, hand-crafted features, simulated human oracle, and potential failure cases.

---

## Removed Points

These points were raised by reviewers but are removed from the main review with justification:

- **"Baseline comparisons give partial credit" (Harsh Critic #4):** REMOVED. The paper explicitly states it counts baselines' incorrect outputs as correct (lines 248, 250). This is *conservative* — it favors baselines, not OML. Recalculating with stricter criteria would only increase OML's advantage. The criticism misunderstands the direction of the effect.
- **"Brain terminology is purely decorative":** REMOVED as a generic opinion without a specific, verifiable anchor in the paper.
- **Claim about human-in-the-loop being an "oracle that always gives the desired answer":** REMOVED. The paper describes a timeout→positive response mechanism for *unanswered* questions. This is not an oracle; it is a simulation convenience. The critic's framing overstates the issue.
- **Various generic formatting/style nitpicks and speculation about missing appendix content:** REMOVED per instruction rules.

---

## Novel Insights

None beyond the paper's own contributions. The reviews raise valid concerns but do not contribute new theoretical insights or synthesis that the paper itself lacks.

---

## Suggestions

1. **Fix or clarify Eq. (1).** This is the single highest-priority issue. If y^{α_k} is intended to be a time-varying signal (vector of T values), the notation must be corrected to show this explicitly, and the signal's dependence on input features x must be explained. If the equation as currently written reflects the actual computation, the paper needs to explain why the cosine-sum degeneracy (zero for most λ) does not collapse the signal.

2. **Add ablation studies.** At minimum: (a) remove the reference extraction mechanism (treat all features equally) and compare on Table 2 tasks; (b) remove lateral connections; (c) replace the Fourier-based signaling with a simpler mechanism. Without ablations, it is impossible to attribute results to specific design choices.

3. **Report dataset statistics**, multiple independent runs with standard deviations, and proper precision/recall for conflict detection.

4. **Specify the training procedure for offline baselines in the open environment** (retrained from scratch vs. fine-tuned).

---

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Beyond Unimodal Learning (Pa6SiS66p0) | 4.33 | R1, R2 | Weaker baseline comparison but mathematically sound; better than current paper |
| Multiple Modes for CL (fwJeVYGcbz) | 4.00 | R1, R2 | More rigorous experiments; better than current paper |
| CLIP Online Continual Learner (G9Ea7mlqGO) | 3.80 | R2 | Similar weakness profile but no mathematical error; comparable |
| FlyOrien (jYyste2HLP) | 4.33 | R2 | Bio-inspired incremental learning, cleaner evaluation; better than current paper |
| Multimodal Meta-learning (vSOTacnSNf) | 4.33 | R2 | Solid experiments but unclear mechanism; better than current paper |
| MCIL Benchmark (gNoqEdT2wO) | 2.33 | R1 | Limited contribution but sound; comparable overall |
| CAN (SI6zocV2SS) | 1.50 | R1 | Incomplete idea; worse than current paper |

**Bracketing:** Round 1 placed the paper between [2.5, 5.0]. Round 2 narrowed to [3.0, 4.0] by comparison against anchors in the 3.5–5.5 range. The paper is comparable to or weaker than the ~3.8–4.33 anchors but clearly above the 1.5–2.33 range.

The paper has a verified mathematical problem in its core equation (Eq. 1), no ablations, unreported dataset sizes and variance, and unsubstantiated conflict detection claims. However, the problem framing is ambitious and the reference extraction idea is genuinely novel. Score is set at 3.0, reflecting a clear reject due to the combination of a mathematical specification issue and weak empirical methodology, while acknowledging the paper has more substance than the lowest-scoring papers.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>