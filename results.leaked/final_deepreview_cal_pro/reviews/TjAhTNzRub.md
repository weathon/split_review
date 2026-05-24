Now I have a comprehensive picture. Let me synthesize the final review.

---

## Summary

MoRE proposes a training-free framework for irreversible feature-level machine unlearning. It introduces three innovations: (i) prototype-orthogonal projection to decorrelate forget and remain prototypes before erasure, preserving utility; (ii) remapping forget prototypes into remain prototype distributions to break the cohesive-separable structure that prior methods leave behind; and (iii) a mixture-of-experts router that scatters forget features across multiple remain prototypes, further impeding recovery. The method operates with linear complexity, completing unlearning in seconds. Experiments span CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet for class-wise unlearning, plus a proof-of-concept extension to concept erasure in Stable Diffusion.

## Strengths

- **Novel, well-motivated technical framework.** The observation that prior methods (ESC) leave a cohesive forget cluster in feature space (Fig. 1) directly motivates the remapping approach. The three-stage pipeline — PO projection → erasure/remapping → MoE scattering — is conceptually clean, geometrically intuitive, and builds logically on the limitations of subspace erasure. Equations 2–6 provide a precise, full-rank formulation with skip connection that is both correct and implementable.

- **Strong empirical results, especially on recovery resistance.** MoRE achieves forget accuracy at or near random guessing across all three datasets in the standard KD setting, while matching or exceeding baselines on remain accuracy (Table 1). Under the KR recovery-attack setting, MoRE dramatically outperforms all baselines, including the retrain-from-scratch model. On CIFAR-100, MoRE achieves HM_f = 0.07 versus ESC's 99.60 and Retrain's 52.96 — a genuinely striking result that demonstrates the method is doing something qualitatively different from prior approaches.

- **Prototype-orthogonal projection is convincingly ablated.** Table 3 shows that without PO projection, erase leaves residual forget accuracy of 14.38% and remap degrades remain accuracy; with PO, both erase and remap achieve 0.00% forget accuracy and high HM (99.68–99.94). The cosine similarity heatmaps (Fig. 3 vs. Fig. 6) provide direct visual evidence that PO projection disentangles prototypes, enabling surgical editing of the forget prototype without disturbing remain prototypes.

- **Computational efficiency is a genuine practical advantage.** MoRE completes unlearning in under 10 seconds with <200 MB GPU memory on CIFAR-10/100 (Fig. 5), while matching or outperforming training-based baselines that require orders of magnitude more compute. This is not a marginal gain — it changes the deployment feasibility of feature-level unlearning.

- **Well-structured ablation studies.** Sensitivity to number of experts (Fig. 7), target remapping class (Table 5), routing strategy (Table 6), and layer depth (Table 7) are all examined. The finding that stochastic routing is competitive with trained routers (Table 6) is practically useful and honestly reported.

## Weaknesses

### Major

- **The "irreversible" claim overreaches the evidence, and the KR recovery protocol is insufficiently described in the main text.** The KR evaluation tests a single recovery mechanism (finetuning with a fixed learning rate of 0.1). While the results under this attack are genuinely impressive, "irreversible" implies resistance to a broader class of recovery attempts. The paper would be on firmer ground claiming "highly resistant to fine-tuning-based recovery" or "stronger than retrain-from-scratch under KR evaluation." The exact KR protocol (which layers are updated, optimizer, number of epochs, whether it constitutes linear probing or full finetuning) is deferred to the appendix, making it impossible for a reader of the main text alone to assess the strength of the recovery attack. This is a central claim, and the protocol should be summarized in the main body.

- **The random data forgetting evaluation (Table 4) is opaque and poorly explained.** Column headers `D` and `F` are undefined in the main text. The text states MoRE "outperforms most baselines in terms of average gap" without defining what average gap means. The adaptation of the method from class-wise to instance-wise forgetting is described in one vague sentence ("computing prototypes separately for the forget and remain sets, and then remap each forget prototype to its counterpart from the remain set") without explaining how prototypes are matched when forget instances lack a natural class structure. A reader cannot evaluate whether this experiment supports the claimed generality of the method, and the section currently weakens rather than strengthens the paper.

### Minor

- **Metric notation in tables is inconsistent and hard to follow.** Table 1 contains two columns labeled `D_r(↑)` with different values, and `D_R(↓)` whose relationship to `D_f` and `D_rt` (mentioned in text but absent from table headers) is unclear. Table 3 uses a different header scheme (`D`, `F`, `D_r`, `D_h`, `D_rt`). Table 5 duplicates `D_f` and `D_r` columns for different settings without distinguishing subscripts. These are not merely cosmetic — they make it actively difficult to verify reported numbers against claims in the text.

- **The diffusion model experiment overstates significance relative to evidence.** The claim of "outperforms SOTA … entirely out of the box" (Section 4.1) is based on a single LPIPS-based evaluation (Table 2) with no recovery attack, no membership inference test, and no ablation or hyperparameter exploration on the diffusion side. While it is a promising existence proof that the method transfers to generative models, the current framing — including the statement that "modest, targeted adaptations could further amplify its effectiveness" — is speculative. The results are best characterized as preliminary and encouraging rather than as establishing SOTA.

- **The layer-sensitivity result (Table 7) is reported without analysis.** Performance degrades sharply at the third-last layer, but the paper merely notes this as "a promising avenue for future study." A brief hypothesis about why this happens (e.g., earlier layers have less semantic separation between class prototypes, making orthogonalization less effective) would strengthen the paper and help practitioners.

### Trivial

- The paper uses "MoRE" and "MoUE" interchangeably in Table 7 (`MoUE` at rows for the third-last layer on CIFAR-10) — likely a typo for an earlier name.
- Figure 7 caption says "HM (Hit Rate)" but HM is Harmonic Mean, not Hit Rate.

## Nice-to-Haves

- Extending the recovery-attack evaluation to include linear probing on frozen features and nearest-neighbor retrieval in feature space would substantially strengthen the irreversibility claim without changing the method.
- Running a fine-tuning recovery attack on the diffusion-unlearned model (e.g., fine-tuning on Van Gogh images and checking if the style returns) would bridge the gap between the discriminative and generative evaluations.
- The random forgetting section should either be expanded with clear definitions and more datasets, or scoped out with an explicit statement that the method is designed primarily for concept/class-level unlearning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "an attacker might instead train a linear probe or a small nonlinear decoder on the frozen unlearned features, or optimize a generative objective to reconstruct forget data."** This speculates about attacks not typically evaluated in the MU literature and not standard in the ESC/KR evaluation framework the paper builds on. The KR evaluation already tests a recovery mechanism. While expanding the attack suite would strengthen the paper, the absence of these specific attacks does not make the evidence inadequate — it makes the "irreversible" label slightly overclaimed, which we address above as a Major weakness.

- **Harsh critic: "the description of the multiple-experts extension is brief; important design choices … are deferred to the appendix."** Conference page limits necessitate this. The main text provides enough detail (stochastic vs. conditional routing, the motivation for scattering) to understand the core idea. The appendix is the appropriate place for implementation-level details.

- **Strength Finder: "Irreversibility under linear probing (KR evaluation)."** The strength finder conflates the KR setting with linear probing, but the KR setting (lr=0.1) likely involves full or partial finetuning, not just training a linear classifier on frozen features. The evidence for irreversibility is strong, but the terminology should be precise.

- **Strength Finder: generic framing about the problem being important.** The importance of machine unlearning is a field-level claim, not a paper-specific strength.

## Novel Insights

The key insight that emerges from this work — and is well-supported by the evidence — is that erasure alone is insufficient for irreversible unlearning because it leaves a recoverable cohesive structure in feature space. The combination of (a) decorrelating prototypes before editing and (b) actively remapping forget features into remain distributions, rather than simply zeroing them out, represents a genuine conceptual advance over subspace-erasure methods. The multi-expert scattering mechanism operationalizes this insight in a way that is both simple and demonstrably effective. The finding that this approach can outperform retrain-from-scratch on recovery resistance challenges the conventional wisdom that retraining is the gold standard for unlearning.

## Suggestions

- Move the KR protocol definition (at least a one-paragraph summary covering what is finetuned, for how many epochs, with what optimizer) from the appendix into Section 4. This is essential for readers to assess the paper's central claim.
- Add clear, distinct column headers to all tables. For Table 1, use subscripts consistently: `D_f` for forget train accuracy, `D_{ft}` for forget test accuracy, `D_r` for remain train accuracy, `D_{rt}` for remain test accuracy. Define each in a single sentence in the Evaluation Metrics paragraph.
- Temper the "irreversible" language to "strongly resistant to fine-tuning recovery" or "harder to reverse than retrain-from-scratch" — the results are impressive enough without overclaiming.
- Either clarify the random forgetting evaluation or remove it. If kept, define all columns, explain the prototype matching procedure, and report results on at least one additional dataset.

## Score and Decision

### Calibration anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `Xagys9QD3T` (PPU) | 3.00 | 1 | Much weaker; no feature-level analysis, less sophisticated method |
| `p7mgNvOD9Q` (SUN) | 4.00 | 1 | Similar training-free subspace approach but less sophisticated, no remapping or irreversibility evaluation |
| `pUOesbrlw4` (Deep Unlearning) | 5.25 | 1,2 | Closest technical comparison (SVD-based, training-free); MoRE is more innovative with remapping + MoE and substantially stronger KR results |
| `TLBPjECC5D` (Sparse Repr. Unlearning) | 5.25 | 2 | Lower-compute approach with less comprehensive evaluation |
| `bKQJzuBSRJ` (NegMerge) | 6.00 | 2 | Solid contribution but more incremental; MoRE is more novel and has stronger experimental evidence |
| `1ExfUpmIW4` (LLM Unlearning) | 6.00 | 2 | Well-evaluated with clear motivation, but MoRE's cross-modal scope and KR results are more impressive |
| `A0HKeKl4Nl` (Mechanistic Fine-tuning) | 6.67 | 2 | Good analysis paper; MoRE is comparable in quality but has presentation issues that pull it down slightly |
| `PBjCTeDL6o` (UNI) | 8.00 | 1 | Exceptional execution, strong theory, comprehensive experiments; MoRE is below this tier |

**Round 1 bracket:** MoRE falls between 5.25 (Deep Unlearning) and 8.00 (UNI), with the plausible range being 5.5–7.5.

**Round 2 narrowing:** Compared against the 6.00 anchors (NegMerge, LLM Unlearning), MoRE has a more novel contribution and stronger experimental results, but its presentation issues and overclaimed irreversibility prevent it from reaching the 7+ tier. It sits above 6.00 and below 6.67. The 6.67 anchor is a well-executed analysis paper with clearer writing; MoRE's contribution is arguably more impactful for the unlearning field but its presentation weaknesses put it slightly lower.

**Final score:** 6.5 — a solid accept with weaknesses that should be addressed in revision. The core technical contribution is genuine and well-supported, the experimental results on KR are striking, and the computational efficiency is a real practical advantage. The paper would benefit from clearer notation, a tempered irreversibility claim, and either strengthening or removing the random forgetting section.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>