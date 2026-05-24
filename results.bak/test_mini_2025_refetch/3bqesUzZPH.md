Now I have enough calibration data. Let me synthesize the final review.

## Summary

This paper proposes FTA, a generator-assisted backdoor attack for federated learning that produces per-sample, per-round imperceptible triggers. The key idea is to train a generative trigger network (ℓ₂-constrained) that makes poisoned samples share hidden features with benign samples of the target label, thereby reusing benign routing and avoiding parameter-space anomalies that trigger FL defenses. The method is evaluated on four datasets (Fashion-MNIST, FEMNIST, CIFAR-10, Tiny-ImageNet) against up to ten FL defenses.

## Strengths

1. **Well-motivated attack design targeting three specific stealthiness problems.** The paper identifies and formalizes three concrete failure modes of prior FL backdoor attacks: feature-extraction abnormality (P1), backdoor-routing abnormality (P2), and perceptible triggers (P3). The FTA design directly addresses all three through per-sample imperceptible triggers that enforce feature similarity to the *target* label's benign samples. This problem decomposition gives the paper a clear internal logic.

2. **Strong empirical results under norm clipping and FLAME defenses.** Figure 4 shows FTA maintaining >95% backdoor accuracy on CIFAR-10 and Tiny-ImageNet under both norm clipping and FLAME, while Baseline, Neurotoxin, DBA, and Edge-case fall below 20%. This empirical gap is substantial and directly supports the paper's claim that feature-similarity-based triggers avoid detection by parameter-space and clustering defenses.

3. **Mechanistic evidence (t-SNE + update similarity) explaining why the attack works.** Figure 5(a)–(b) shows that FTA's poisoned samples overlap with benign target-class samples in the hidden feature space, while the baseline attack produces a clearly separated cluster. Figure 5(c)–(d) shows that FTA's malicious updates have Euclidean distance and cosine similarity nearly identical to benign-benign pairs. This directly supports the claimed mechanism (reusing benign routing) and is among the strongest evidence in the paper.

4. **Comprehensive evaluation scope.** The paper tests across Fashion-MNIST, FEMNIST, CIFAR-10, and Tiny-ImageNet using Classic CNN, VGG11, and ResNet18, and claims testing against ten FL defenses (eight in the abstract). The fixed-frequency and few-shot modes both demonstrate effectiveness and durability.

## Weaknesses

### Fatal
None.

### Major

1. **Key quantitative evidence for two headline claims is deferred to the appendix.** The paper's defining claims are (a) natural stealthiness (imperceptible triggers) and (b) broad defense evasion. Yet Section 4.5 on natural stealthiness consists of two sentences that say "see Appendix A.9 for results" — no SSIM or LPIPS numbers appear in the main text. Similarly, of the ten claimed defenses, only norm clipping and FLAME receive detailed treatment in the main body (Figure 4, 8 subplots). The remaining defenses (Multi-Krum, Trimmed-mean, RFA, SignSGD, Foolsgold, SparseFed, Pruning, RLR) are each dispatched with a single sentence in Section 4.3 ("FTA maintains its stealthiness and robustness under these defenses") and the results are deferred to Appendix A.4. While page limits are a real constraint, a compact summary table or bar chart (e.g., final backdoor accuracy per defense per attack) in the main text would substantially strengthen the paper's self-containedness. As written, a reader relying on the main text cannot independently verify two of the paper's three central contributions.

### Minor

2. **Incremental novelty over centralized generator-based attacks (LIRA/Doan et al. 2021b).** The paper uses the same core architecture (generator + ℓ₂ norm constraint) as LIRA. The adaptations to FL are meaningful — target-label feature similarity (rather than original-input feature similarity), per-round adaptation, two-phase sequential optimization, and defense evaluation — but the paper's framing ("we for the first time consider the natural stealthiness of triggers during global inference") somewhat overstates the departure. The writing would benefit from a more explicit delineation of what is inherited and what is new. This does not invalidate the contribution, but readers should calibrate expectations.

3. **Bi-level optimization approximation is unexamined.** Algorithm 1 decouples the bilevel problem in Equation (1) into sequential stages (update generator with fixed model, then update model with fixed generator). The paper justifies this by noting that few poisoning epochs keep the model from changing much, but provides no experimental analysis of cases where this approximation might fail (e.g., large model shifts, initialization effects). An ablation varying the number of inner-loop epochs or showing loss dynamics would strengthen confidence.

4. **No baseline directly applying a centralized generator (LIRA) per round.** The paper argues that centralized generators fail for FL (Section 2.2), but does not include an empirical baseline that simply applies LIRA per round without the target-label feature constraint. Such an ablation would cleanly isolate the effect of the proposed design and strengthen the novelty argument.

### Trivial
- The abstract claims "eight well-studied defenses" while Section 4.1 lists ten; there is a minor numerical inconsistency.
- Figure 4 legend labels are garbled in the extracted text ("Neutristin" → Neurotoxin, "DM" → DBA) — this is a parser artifact but worth noting for the camera-ready.
- Equation (1) notates the bilevel constraint as "ξ* = argmin_ξ … s.t." where standard notation would be "ξ ∈ argmin_ξ …" — a minor formulation issue.

## Nice-to-Haves
- A compact bar chart or table in the main text summarizing final backdoor accuracy across all tested defenses and attacks (even if round-by-round curves remain in the appendix).
- Ablation of the generator's constraint strength ϵ showing the backdoor accuracy vs. stealthiness trade-off (likely in Appendix A.8, but central to the method).
- Limitations discussion: e.g., scenarios where the attack might fail (tight DP budgets, drastic global model changes).

## Removed Points
- **"Core evidence is relegated entirely to the appendix" framed as a fatal flaw**: The appendix was removed by the parser, and the paper does provide substantial main-text evidence (Figure 4 for two primary defenses, Figure 2 for visual imperceptibility, Figure 5 for mechanistic evidence). The criticism is retained as a Major weakness about *what is in the main text vs. the appendix*, not about missing content.
- **Novelty "overstated" (framed as a structural weakness)**: Retained as Minor, not Major or Fatal — the adaptations are real and meaningful even if the core technique is borrowed.
- **Strength Finder's generic strengths** (e.g., "comprehensive evaluation," "bi-level optimization that efficiently adapts"): Partially retained but combined with verified specifics.
- **Pure formatting/style nitpicks** and criticisms about missing related works: Removed per rules.
- **Harsh critic's point about "computational cost" deferred to appendix**: The main text does reference Appendix A.10 for cost details and says "our attack does not significantly increase the computational and time cost" (Section 4.2). This is addressed sufficiently for a conference paper scope.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a consistent concern about presentation balance (main text vs. appendix) but do not identify a new capability or limitation that the paper itself overlooks.

## Suggestions
1. Move a compact summary of SSIM/LPIPS results and a table/bar chart of defense evasion across all defenses into the main text, even at the cost of moving one less critical figure (e.g., some curves from Figure 4) to the appendix.
2. Add a LIRA-per-round baseline to empirically demonstrate the failure of centralized generators in FL.
3. Include an ablation varying the number of inner-loop epochs (e_T) to examine when the decoupled bilevel approximation holds or breaks.
4. Minor notational fix: change Equation (1) constraint (i) to standard form (ξ ∈ argmin_ξ …).

## Score and Decision

**Bracket (Round 1):** The paper sits between the weak anchors below 3.5 (rejected papers on unrelated FL topics) and the strong anchors above 7.5 (oral/spotlight papers on FL optimization). Initial bracket: **4.0–7.0**.

**Narrowing (Round 2):** Compared against topically similar papers:
- **DPOT** (avg 4.75, Reject; scores 3,6,5,5) — also a trigger-optimization backdoor attack for FL. FTA is clearly stronger: generator-based imperceptible triggers vs. visible patches, feature-similarity mechanism, and better mechanistic evidence (t-SNE, update similarity).
- **Bad-PFL** (avg 6.0, Accept Poster) — generator-based attack for PFL. Comparable contribution level. Bad-PFL may have slightly cleaner evidence in the main text, while FTA has more defenses tested.
- **BC Layers** (avg 6.0, Accept Poster) — different attack strategy (layer-focused). Comparable evaluation depth.
- **Frequency Domain Backdoor** (avg 5.75, Accept Poster) — different approach, similar evaluation.

FTA is above DPOT (4.75) and comparable to but slightly below the three 6.0 anchors due to its main-text evidence gap. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>