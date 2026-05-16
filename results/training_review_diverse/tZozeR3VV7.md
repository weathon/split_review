Now I have all the information needed to produce the consolidated review. Let me carefully synthesize.

---

## Summary

This paper introduces VLOOD, a backdoor attack on Vision-Language Models (VLMs) that operates under a practical threat model: the attacker has no access to the original training data and must rely on Out-Of-Distribution (OOD) public image-text pairs. The method integrates three components — Clean Knowledge Preservation (CKP, via knowledge distillation), Conceptual Consistency Preservation (CCP, via L1-distance regularization on token embeddings), and dynamically adjusted weights — to inject a backdoor while preserving the semantic coherence of generated captions/answers. Evaluated on image captioning (Flickr8k, Flickr30k, COCO) and VQA (OK-VQA, VQAv2) across three architectures (BLIP-2, MiniGPT-4, InstructBLIP), VLOOD achieves ASR ≥ 0.997 with substantially higher conceptual consistency (BLEU-4, CIDEr, VQA score on poisoned inputs) than six baselines.

## Strengths

- **First OOD backdoor attack on VLMs with semantic preservation.** The paper is explicit about this novelty: "We are the first to explore backdooring VLMs in a practical scenario using Out-Of-Distribution (OOD) training data" (Sec. 1). Prior attacks (Shadowcast, AnyDoor, TrojVLM) assume access to the original training data. The paper provides a well-motivated problem definition (Sec. 3.1) distinguishing this threat model.

- **High attack success rate with strong conceptual consistency.** On image captioning (Table 1), VLOOD achieves ASR ≥ 0.997 across all three datasets while maintaining CIDEr scores on poisoned inputs that are close to the clean model's (e.g., 110.7 vs. 113.5 on Flickr8k — a 2.5% drop). In contrast, baselines like Blended and Shadowcast produce poisoned-input CIDEr scores as low as 3.4–7.3, showing near-total semantic collapse. The same pattern holds on VQA (Table 2) and across architectures (Table 3). This is the paper's strongest empirical contribution.

- **Clear ablation isolating each component's role.** Table 1 (tab:default_and_mine) systematically ablates CKP, CCP, and dynamic weights. The results are informative: CKP alone washes out the backdoor (ASR=0.000 on PI); CCP alone causes false triggers on clean inputs (ASR=0.852 on CI); dynamic weights alone degrade clean metrics. The full VLOOD resolves all three failure modes. This is a well-designed ablation that validates the engineering rationale.

- **Broad evaluation across architectures.** Beyond BLIP-2, VLOOD is tested on MiniGPT-4 and InstructBLIP (Table 3), showing that the method generalizes beyond a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **OOD training/evaluation pairing is not specified in the main experiments, making the central claim unverifiable from the main text.** The paper states in Sec. 4.1: "To achieve OOD training, we train the backdoored model on one dataset and evaluate it on another. Details can be found in Appx." The main results tables (Tables 1, 2, 3) report per-dataset columns but never state which dataset was used for backdoor training and which for evaluation in each case. Since the core contribution is demonstrating backdoor injection with OOD data, the reader must be able to see the distribution shift for each result. Without this, it is impossible to confirm whether a result reflects a genuine OOD scenario or an in-distribution one. This is the single most important missing piece, and it must be addressed in the main text (not deferred to an appendix).

### Minor

- **Dynamic weight mechanism is heuristic and lacks analysis of its behavior.** The update rule λ = λ + (Impact_clean − Impact_poisoned) is presented without bounds, convergence discussion, or sensitivity analysis. Since λ weights the loss contributions of clean and poisoned data, an unbounded λ could in principle cause negative loss weights. The paper provides no plot of λ over training, no comparison with fixed λ values, and no study of sensitivity to the initial λ. While the empirical results show the mechanism works in practice, the lack of analysis makes it difficult to assess whether the approach is robust or brittle.

- **Several baselines produce degenerate outputs, raising questions about adaptation fidelity.** BadEncoder on BLIP-2 (Table 1) achieves BLEU-4=0.0, CIDEr=0.0, and ASR=0.000 on *both* clean and poisoned inputs — it is not generating meaningful text at all. The paper states baselines were "implement[ed] following their settings" but provides no details on how they were extended from their original settings (classification/contrastive learning) to sequence generation. The near-zero scores suggest the adaptation may not have been tuned for this task. (Note: BadEncoder performs better on MiniGPT-4 and InstructBLIP in Table 3, partially mitigating this concern, but the BLIP-2 results remain unexplained.)

- **No variance or statistical significance reported.** All main tables report single numbers. Given that backdoor injection can be sensitive to random seeds, data splits, and initialization, reporting mean ± std over multiple runs (e.g., 3 seeds) would substantially increase confidence.

- **Defense evaluation is limited to two methods not designed for VLM generation tasks.** The paper tests only Spectral Signatures and Beatrix and acknowledges they were not designed for image-to-text generation (Sec. 4.3). While the paper is transparent about this limitation, it means the claim of "robustness against existing defense methods" is narrow — it only shows robustness against a specific pair of ill-suited defenses. This does not provide strong evidence of general undetectability.

### Trivial
None.

## Nice-to-Haves

- A plot of λ values during training, and an ablation comparing the dynamic mechanism against several fixed λ values, would strengthen the methodological contribution.
- Clarifying in the main text (not appendix) which dataset pairing was used for each OOD experiment would immediately resolve the most serious concern.
- Including a limitations paragraph discussing potential failure modes (e.g., detectability by human inspection, sensitivity to trigger design) would improve completeness.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"OOD scenario not validated at all."** (Harsh Critic, Point 1, framing) — The paper *does* describe the OOD setup conceptually ("train on one dataset, evaluate on another") and the method's design explicitly targets distribution shift. The issue is underspecification, not absence. The criticism is kept in Major but reframed accordingly.

2. **"Color notation is difficult to read in black-and-white."** (Harsh Critic, Section-by-Section Notes) — Pure formatting/style nitpick. REMOVED.

3. **"Missing appendix / details in Appx."** — Per instructions, the appendix is stripped by the parser; these are not author errors. REMOVED.

4. **"Dynamic weight causes ASR=0.000 on clean inputs — pattern of overfitting."** (Harsh Critic, Point 2, second half) — ASR=0.000 on clean inputs is the *desired* behavior (no false positives). The reviewer misread the metric. REMOVED.

5. **"Default + Dynamic alone yields ASR=0.999 on PI but 0.000 on CI, suggesting overfitting."** — Clean ASR=0 means the backdoor does not trigger on clean inputs. This is correct, not a sign of overfitting. REMOVED.

6. **Strength Finder item 6 ("Realistic OOD training setup").** — Conflicts with the verified weakness that the OOD pairing is underspecified. Per rules, the weakness wins. MOVED to Removed Points.

7. **"The paper should cover Y/domain Z/additional tasks."** — The Harsh Critic does not make this type of argument, so no action needed.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the ablation in Table 1 reveals an interesting tension — CKP alone washes out the backdoor (ASR=0 on poisoned inputs), showing that strong knowledge distillation can inadvertently erase injected malicious functionality. The dynamic weight mechanism is then essential not just for balancing objectives, but specifically for preventing CKP from dominating and destroying the backdoor. This interplay between knowledge-preservation and backdoor-retention is a design tension that the paper identifies but does not fully analyze; it could be a useful direction for future work on bypassing distillation-based defenses.

## Suggestions

1. **Clarify the OOD pairing in the main text.** For each table, state explicitly: "The model was fine-tuned on Dataset A, backdoor-trained using Dataset B's image-text pairs, and evaluated on Dataset A's test set." This single change would resolve the paper's most serious weakness.

2. **Add variance estimates.** Report mean ± std over at least 3 random seeds for the key conditions (VLOOD and top baselines on each dataset).

3. **Add a λ-trajectory plot and a fixed-λ comparison.** Show λ over training epochs and compare the dynamic mechanism against, e.g., λ ∈ {0.1, 0.3, 0.5, 0.7, 0.9}.

4. **Either justify the BadEncoder adaptation for BLIP-2 or remove it from that table row.** Including a baseline that produces degenerate outputs undermines the comparison, even if it performs adequately on other architectures.

## Score and Decision

The paper addresses a timely and practically motivated problem, proposes a method with clear components, and provides extensive experimental evidence that VLOOD achieves strong attack performance while preserving conceptual consistency. However, the central claim — OOD backdoor injection — is not verifiable from the main text because the specific training/evaluation dataset pairings are deferred to the appendix. Other issues (heuristic dynamic weighting without analysis, uncertain baseline adaptations, no variance reporting) are addressable but weaken the presentation.

**Overall Assessment:** The paper has genuine contributions and strong initial results, but the OOD validation gap in the main text is a structural issue that must be fixed. With clarification of the experimental setup, this would be a solid paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>