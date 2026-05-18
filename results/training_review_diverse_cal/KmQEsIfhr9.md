Now I have all the information I need. Let me construct the final review, carefully cross-referencing each criticism against the actual paper.

---

## Summary

This paper studies the detectability of poisoning backdoor attacks in CLIP pretraining. The authors discover that backdoor-poisoned samples exhibit sparse local neighborhoods in the learned representation space, making them detectable as outliers. They show that simple density-based outlier detectors (SLOF, DAO, k-dist) achieve near-perfect AUC (97–99%) across diverse trigger types, substantially outperforming existing backdoor-specific detection methods (ABL, CD, SafeCLIP). The detection is efficient (15 minutes for CC3M on 4 A100 GPUs), and the authors further uncover an unintentional backdoor in CC3M that propagated to a released OpenCLIP model.

## Strengths

1. **Discovery of local neighborhood sparsity as a distinguishing characteristic of CLIP backdoor samples.** The paper provides both visual intuition (Figure 1a, t-SNE) and quantitative evidence (Figure 1b, k-dist distributions across poisoning rates) showing that backdoor samples have far sparser local neighborhoods than clean samples. This insight is foundational to the detection approach and novel for the CLIP setting.

2. **Strong empirical results across diverse attack scenarios.** Table 1 shows that DAO achieves 99.14% AUC on the Patch attack with ResNet-50, 98.81% on WaNet, and 97.40% on Nashville, substantially outperforming SafeCLIP (84.37%, 67.30%, 64.00% respectively). The evaluation covers six trigger types, multi-trigger attacks, clean-label attacks, targeted data poisoning, and two architectures (RN50, ViT-B-16), demonstrating robustness.

3. **Practical defense pipeline validated end-to-end.** Table 2 shows that filtering 10% of data based on DAO scores reduces ASR to below 1% for most attacks (e.g., Patch drops from 95.80% ASR to 0.01%) while maintaining clean zero-shot accuracy. Figure 3a shows the sensitivity to filtering rates, giving practitioners actionable guidance.

4. **Efficiency and scalability.** The paper reports that cleaning CC3M (million-scale) takes only 15 minutes on 4 A100 GPUs, compared to 11.2 hours for CD and 4.1 hours for ABL. This makes the method feasible for real-world web-scale data curation.

5. **Discovery of an unintentional backdoor in CC3M that propagated to a released OpenCLIP model.** The paper identifies a birthday-cake image appearing 798 times, recovers a trigger from both their own model and an OpenCLIP-released model, and shows 98.92% ASR on the latter. This is a notable finding with practical security implications.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by evidence; see Minor and Nice-to-Haves for areas of refinement.

### Minor

1. **The unintentional backdoor finding lacks a control experiment.** The paper recovers a trigger pattern from the birthday-cake image (798 occurrences) and demonstrates high ASR, but does not test whether a similarly over-represented but non-backdoor concept (e.g., a common broken-image placeholder appearing hundreds of times) would also yield a recoverable "trigger" with high ASR. Without this control, it is unclear whether the effect is specifically a backdoor or an artifact of trigger recovery methods always finding some pattern when a concept is heavily duplicated. This does not undermine the paper's core detection contribution, but weakens the confidence in the unintentional-backdoor discovery.

2. **The evaluation setup for detection (batch sampling vs. full dataset) could be clearer.** The paper states (Section 4.3) that it "randomly sample[s] a batch of data from the dataset" for detection, and Section 4.2 motivates this by arguing that at 0.01% poisoning rate, a batch of 1024 likely contains 0–1 backdoor samples with clean nearest neighbors. However, it is not specified whether the AUC results in Table 1 are computed within batches or across the full dataset, nor whether the evaluation is averaged over multiple random batches. Clarifying this would improve reproducibility and help readers understand whether the strong results depend on the batch-sampling strategy.

3. **No discussion of adaptive attackers who could evade detection.** The paper acknowledges that detection depends on low poisoning rates creating sparse neighborhoods (Section 4.2), and tests up to 10% poisoning rates. However, it does not discuss whether an attacker aware of this detection method could use strategies to evade it — e.g., using more subtle triggers that do not produce strong feature clustering, or distributing backdoor samples diversely across representation space. This is a standard limitation in backdoor defense papers, but an explicit discussion of the threat model's boundaries would strengthen the paper.

4. **The efficiency claim lacks algorithmic details.** The paper states that detection takes 15 minutes on 4 A100 GPUs for CC3M but does not specify whether exact or approximate nearest neighbor search is used, how k is chosen, nor how much of the runtime is representation extraction vs. detection computation. These details matter for reproducibility and for assessing scalability claims to larger datasets.

### Trivial

- The t-SNE visualization (Figure 1a) is used only for motivation and is appropriately backed by quantitative evidence (Figure 1b), but the paper could directly compare average local density estimates (e.g., SLOF scores) between clean and backdoor samples to further strengthen the sparsity claim.
- No error bars or uncertainty estimates are reported for AUC values in Table 1. Since the main results are near-perfect (97–99%), this matters little for those methods, but it would be informative for the methods with lower AUC (ABL, CD, LID).

## Nice-to-Haves

- **For the unintentional backdoor:** Include a control experiment with a naturally duplicated but non-backdoor image (e.g., a common broken-image placeholder) and show that its recovered "trigger" yields low ASR. This would substantially strengthen the claim.
- **Adaptive attack analysis:** Discuss under what conditions the detection method would fail (e.g., higher poisoning rates, triggers designed to avoid feature clustering) to help practitioners understand the threat model boundaries.
- **Per-trigger visibility analysis:** Examine whether more subtle triggers (e.g., small pixel perturbations, frequency-domain perturbations) still produce sparse neighborhoods. The current triggers (patch, filter, WaNet) span a range of visibility, but a dedicated ablation would strengthen generality claims.
- **Full-dataset evaluation:** Show whether AUC remains comparable when detection is performed over the entire dataset (all-vs-all) rather than in random batches, to clarify the role of batch sampling.

## Removed Points

- **Criticism about ABL/CD adaptation not being described:** The paper's Section 5 (line 151) explicitly references a footnote with additional experimental details, and the Related Work section (line 34) describes both methods conceptually. The specific adaptation methodology would be in the appendix, which is stripped by the parser. This is a missing-appendix issue, not an author error. *Removed per instruction: "REMOVE weaknesses about missing appendix."*
- **Claim that "the paper does not test cases where the assumption weakens" for higher poisoning rates:** The paper explicitly states (line 151) that it tests up to 10% poisoning rate and that local outlier methods remain effective. The reviewer's criticism on this specific sub-point is factually incorrect. *Removed per instruction: "REMOVE criticisms that are factually wrong."*
- **Criticism that the SafeCLIP comparison is more relevant than ABL/CD:** The paper compares against both SafeCLIP and ABL/CD, and the main text already discusses why ABL and CD are applicable to CLIP. This is a matter of taste, not a structural flaw. *Removed as a strawman weakness.*

## Novel Insights

The harsh critic raises an insightful question that the paper does not fully address: the unintentional backdoor finding could alternatively be explained as a memorization artifact of a heavily duplicated image–caption pair, rather than a malicious backdoor. The paper uses the term "backdoor" in the security sense (a trigger that redirects model behavior), but the trigger is a birthday cake icon that causes the model to predict "birthday cake" — which could be seen as the model correctly recognizing a highly specific, repeated visual concept. The distinction matters because a true backdoor is surreptitious and harmful, while the birthday-cake pattern may simply be an overlearned feature. The control experiment (testing a similarly duplicated non-backdoor concept) would cleanly resolve this ambiguity. This is a genuinely useful observation that would improve the paper's framing.

## Suggestions

1. Add a control experiment for the unintentional backdoor — test a naturally duplicated image (e.g., a broken-image placeholder appearing hundreds of times) and show that its recovered "trigger" yields low ASR.
2. Clarify the detection evaluation methodology: specify whether AUC in Table 1 is computed within batches or across the full dataset, and report whether results are averaged over multiple random batches.
3. Add a brief discussion of adaptive attacker strategies and when the detection method would/would not be expected to work, to help practitioners understand the limitations.
4. Specify whether exact or approximate nearest neighbor search is used for the k-NN computation, and how k is selected.

## Score and Decision

This is a solid empirical paper with a clear contribution. The core finding — that CLIP backdoor samples are outliers detectable by simple density-based methods — is well-supported across diverse triggers and settings. The defense pipeline is validated end-to-end, and the efficiency claim makes the work practically relevant. The weaknesses are minor: the unintentional backdoor finding could be better controlled, some implementation details need clarification, and the adaptive-attacker limitation should be discussed. None of these threaten the paper's central claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>