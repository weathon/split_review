Now I have a clear picture. Let me synthesize everything into the final review.

**Bracket assessment:**
- Round 1 bracket: 5.5–7.0 (below DeYO at 7.0, above DOTA at 6.0)
- Round 2 narrowed: RTA is closest to TTE-via-LMC (6.50) and RLCF (6.67) in quality — both accepted papers with novel ideas, strong results, and some clarity/ablation gaps. RTA is clearly stronger than DOTA (6.00, rejected) and ML-TTA (6.25). It sits below DeYO (7.00) which has stronger theoretical grounding.

**Final score: 6.5**

---

## Summary
This paper proposes Regression-based Test-time Adaptation (RTA), a method for CLIP-based image classification that replaces entropy-based view selection with a learned regression mapping. A LightGBM decision tree is trained once on pseudo-labeled ImageNet data to map logit vectors to predicted cross-entropy loss; at test time, this tree scores augmented views, and the top-k lowest-predicted-loss views are ensembled for the final prediction. Experiments across single-label, cross-domain, and multi-label benchmarks show consistent improvements over existing TTA methods.

## Strengths
- **Compelling motivation through Ceiling TTA (Tables 1–2):** The paper demonstrates that using ground-truth label cross-entropy loss for view selection yields dramatic gains over entropy (e.g., +23.9% on ImageNet-K for ViT-B/16 with 64 views), providing strong quantitative motivation that the view–loss relationship is exploitable.
- **Consistent SOTA across diverse benchmarks:** RTA outperforms all compared TTA methods (TPT, DiffTPT, TDA, Zero, BCA, ML-TTA) on both RN50 and ViT-B/16 backbones across single-label (Table 3), cross-domain (Table 4), and multi-label (Tables 5–6) settings. Notably, RTA beats the dedicated multi-label method ML-TTA on its own benchmarks.
- **Simple and efficient design:** The method uses a lightweight LightGBM tree (max depth 5, 16 leaves) trained on only 1,000 pseudo-labeled samples from ImageVal-12k. Training is done once offline, and test-time inference adds negligible cost — no per-instance optimization, parameter updates, or memory banks required.
- **Good empirical analysis of scaling behavior:** Figures 4–5 show how performance scales with number of augmented views and regression sample size, confirming that the method is robust to these practical choices.
- **Clear, well-structured exposition:** The method is described in accessible terms with helpful algorithms and figures. The paper is easy to follow.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The regression target vs. regression architecture is not isolated:** The paper trains a decision tree to predict pseudo-label cross-entropy loss, but provides no ablation where the same tree architecture is trained to predict entropy (or max probability) instead. Without this, it is unclear whether the gains come from the choice of prediction target (pseudo-label loss) or from the non-linear function learned by the tree. Given that margins over the entropy-based Zero baseline are sometimes narrow (e.g., ViT-B/16 on IN-1k: 71.13% vs. 70.89%), this ablation is important for substantiating the claim that the pseudo-label loss target specifically is what drives improvement.
- **Class-space handling needs explicit clarification:** The regression tree is trained on logits over 1,000 ImageNet class prompts (Section 4.2). For cross-domain and multi-label datasets, the paper does not explicitly state how the tree is applied when the downstream task classes differ. The most natural interpretation (and likely the actual protocol) is that the tree always receives 1,000-dimensional ImageNet-class logits as input — it acts as a task-independent "view quality assessor" — while final classification uses the dataset-specific classes. This is a consistent design, but the paper should state it clearly to avoid confusion about whether the "train once, adapt anywhere" claim holds.

### Trivial
- **Ceiling TTA gap not discussed:** Tables 1–2 show large gaps between the \(H_{LCE}\) oracle and RTA's actual performance. Briefly acknowledging what fraction of the ceiling is recovered (and why recovery is incomplete) would contextualize the results.
- **Multi-label extension not described:** Algorithm 2 is presented for single-label classification, yet multi-label results are reported (Tables 5–6). The paper would benefit from a sentence or two explaining how the predicted loss from the tree is used for view selection in the multi-label case.
- **No error bars or significance tests:** Given narrow margins on several benchmarks, reporting standard deviations or statistical significance would strengthen confidence in the rankings.
- **Filter ratio sensitivity not explored:** The top-\(k\) ratio is fixed at 0.1 throughout; a brief sensitivity analysis would be informative.

## Nice-to-Haves
- A direct baseline comparing view selection by max softmax probability (the simplest confidence proxy) would help demonstrate that the non-linear tree adds value beyond raw confidence.
- Reporting the computational cost of the one-time tree training (CLIP inference on 12k images for pseudo-labeling + tree fitting) would give a complete picture of the method's practical cost.
- A discussion of the regime in which the regression mapping is expected to generalize — and potential failure modes when the test distribution differs drastically from ImageNet — would strengthen the "adapt to any test distribution" claim.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh critic's "fatal" class-space concern:** The critic claimed the evaluation is "structurally flawed" and "cannot be trusted" because the tree trained on 1,000 ImageNet classes cannot handle cross-domain datasets with different class spaces. This is a misunderstanding: the tree always operates on the same 1,000-class logit space (acting as a task-independent view quality predictor), while final classification uses task-specific classes. The design is internally consistent. The paper merely needs to state this explicitly — demoted to Minor.
- **"What is the selection criterion actually learning?" framed as a decisive concern:** The critic framed this as a major weakness questioning whether the method provides genuine advantage. While the ablation is worth requesting (kept as Minor), the paper already shows consistent improvement over entropy-based methods across many datasets, which constitutes evidence that the approach works in practice.
- **Criticism that Figures 2–3 are trivial:** The critic claimed these figures only show "trivially true" relationships. These are standard motivational visualizations establishing that logit structure correlates with loss — a necessary foundation for the method. Removed.
- **Demand for theoretical analysis of why pseudo-label loss is better than entropy:** This is an empirical paper; theoretical analysis is scope creep. Removed.
- **"Free lunch" framing in the introduction being oversold:** This is a subjective stylistic preference, not a substantive weakness. Removed.
- **Computational cost of training not reported:** Already covered in Nice-to-Haves and is a minor practical detail, not a weakness.

## Novel Insights
The paper's core insight — that a simple regression tree trained on diverse unlabeled data can capture the logits→loss mapping well enough to guide test-time view selection across arbitrary downstream tasks — is genuinely novel. The "Ceiling TTA" experiment (Tables 1–2) provides a clean, quantitative demonstration that the view–loss relationship is the right thing to exploit, and the regression approach offers a practical way to approximate it without labels. This perspective — treating view selection as a regression problem rather than an entropy optimization problem — is a useful reframing for the TTA community.

## Suggestions
- Add the entropy-target ablation (same tree, predict entropy instead of pseudo-label loss) to isolate the contribution of the target from the architecture. This is the single most important experiment to add.
- Explicitly state in Section 4.3 or 5.1 that at test time, the tree always receives logits over the 1,000 ImageNet class prompts for view scoring, while final classification uses the actual downstream class prompts. One clear sentence would resolve the ambiguity.
- Add a sentence explaining how the multi-label extension works (how the predicted scalar loss from the tree maps to view selection when there are multiple positive labels).
- Consider adding standard deviations across multiple runs for the key tables, or at minimum note that results are stable across runs.

---

**Anchor comparison summary:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| DOTA (yD2JMeKumt) | 6.00 | R2 | RTA is stronger: more comprehensive benchmarks, clearer methodology, no fundamental protocol ambiguities |
| ML-TTA (75PhjtbBdr) | 6.25 | R1/R2 | RTA is stronger: covers ML-TTA's benchmarks and beats it, plus single-label and cross-domain. Simpler method. |
| TTE via LMC (4wk2eOKGvh) | 6.50 | R2 | Comparable quality. Both have novel ideas with strong results but some clarity/ablation gaps. RTA's method is simpler and more practical. |
| RLCF (kIP0duasBb) | 6.67 | R1/R2 | Comparable quality. RLCF has broader task coverage; RTA has more thorough classification experiments. |
| DeYO (9w3iw8wDuE) | 7.00 | R1/R2 | RTA is below DeYO, which has stronger theoretical grounding and a more thoroughly validated confidence metric. |
| Two Effects (uAFHCZRmXk) | 8.00 | R1 | RTA is below — this is a deep analysis paper with broad implications for VLMs. |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed to:** 6.0–6.7. RTA sits between ML-TTA (6.25) and RLCF (6.67), closest to TTE-via-LMC (6.50) in overall profile — a solid contribution with a novel idea, strong empirical results, but some clarity gaps and missing ablations that prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>