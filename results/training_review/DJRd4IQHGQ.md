Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

FeedSign proposes a federated fine-tuning algorithm that reduces per-step client-to-server and server-to-client communication to exactly 1 bit, regardless of model size (validated up to 13B parameters). It achieves this by combining zeroth-order optimization with shared pseudo-random number generators (PRNG): clients evaluate a random perturbation direction determined by a shared seed and send only a 1-bit sign indicating whether that direction reduces their local loss. The paper provides a convergence analysis claiming an exponential rate \(\mathcal{O}(e^{-t})\), demonstrates experiments across language and vision models (11M–13B), and discusses attractive byproducts including orbit-based model storage, parameter-server agnosticism, and a differentially private variant.

## Strengths

- **Per-step communication reduced to a single bit regardless of model size.** FeedSign cuts the per-step uplink from KB-level (prior ZO-based FFT methods) to exactly 1 bit. The paper shows that for OPT-13B this replaces 24 GB per step with a single bit (Section 1, Introduction), which is a genuine advance over the closest prior works (FwdLLM, FedKSeed) that communicate at KB scales.

- **Empirical validation across a wide range of model scales and modalities.** Experiments span RoBERTa-large, OPT-125M, OPT-13B, ResNet-18, and ViT-large, covering few-shot classification, multiple-choice, and generation tasks (Tables 1–4). Performance gaps relative to the centralized ZO baseline MeZO are modest (e.g., –5.8% mean gap on RoBERTa-large with k=16), showing the extreme compression does not catastrophically degrade accuracy even at 13B scale.

- **Demonstrated robustness advantages in heterogeneous and Byzantine settings.** Under non-iid data (Dirichlet splits), FeedSign consistently outperforms ZO-FedSGD (Tables 5, 6). Under a Byzantine attack, ZO-FedSGD is "completely compromised" on ViT-large while FeedSign maintains its performance (Table 7, Figure 3). The binary nature of FeedSign inherently bounds the damage a Byzantine attacker can cause.

- **Interesting practical byproducts discussed.** The paper identifies orbit-based model storage (reducing storage for 10k fine-tuning steps on OPT-13B from 24 GB to under 200 bytes), parameter-server agnosticism (PS never holds model parameters), and a differentially private variant with a tunable privacy-convergence trade-off (Section 5).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Byzantine attack evaluation uses asymmetric attack types across methods.** The Byzantine client "always transmits a random number as the gradient projection in ZO-FedSGD, and always transmits a reversed sign in FeedSign" (Section 4.3). Because a random unbounded scalar is inherently more disruptive than a sign flip, this setup does not provide a controlled test of relative robustness. A fairer comparison would hold the attack type constant (e.g., reversed sign in both methods, or random sign in both). This does not invalidate the robustness claim — the binary output format is indeed a structural advantage — but the current experiment conflates attack type with method and overclaims on this evidence.

- **Communication cost for the downlink/seed distribution is not fully specified.** The paper states "per-step uplink and downlink communication overhead of 1 bit" (Section 1) and "download one bit as a global update direction metric" (Conclusion). However, if the PS broadcasts a random seed each step to synchronize the PRNG direction, that seed is far larger than 1 bit. If seeds are derived deterministically (e.g., from step index), the protocol should be stated. Remark 6 mentions "the seed being broadcast" — the protocol details and total bidirectional communication budget need clarification to fully substantiate the 1-bit claim.

- **No variance or statistical significance reported for any experiment.** The paper presents single-run results without standard deviations, confidence intervals, or seed sensitivity analysis. While single-run evaluations are common in large-scale FL experiments, the absence of any variance reporting makes it difficult to assess whether observed performance differences are meaningful. This is especially relevant for the Byzantine and non-iid experiments where gaps are modest.

- **Motivation for why the jump from KB-level to 1 bit is qualitatively significant could be sharper.** The paper correctly cites FwdLLM and FedKSeed as predecessors (Section 2.2) but does not clearly articulate what new capabilities or regimes the 1-bit threshold unlocks beyond "pushing to the limit." The byproducts (orbit storage, parameter security, DP) partially fill this gap, but the paper would benefit from a more explicit framing.

- **No comparison to other communication-efficient baselines like signSGD or Top-k compression.** The paper compares only against ZO baselines (ZO-FedSGD, MeZO) and FO full-precision training. Standard compression baselines that also achieve extreme compression ratios (e.g., signSGD's 1-bit gradient quantization) are not included. While signSGD uses first-order gradients and hence has different memory characteristics, a comparison would help contextualize FeedSign's accuracy-communication trade-off within the broader compression literature.

### Trivial
- The analogy comparing the RoBERTa-large upload size to "5 minutes of YouTube FHD" (Section 1) is vivid but unnecessary for the technical argument; the quantitative comparison to 1 bit is sufficient.

## Nice-to-Haves
- A controlled Byzantine experiment where both methods receive the same attack type (e.g., both attacked with sign-flip or both attacked with random sign) to isolate inherent robustness.
- An ablation comparing FeedSign to a baseline that sends a full-precision scalar ZO projection (not binarized) to isolate the effect of binarization from the effect of ZO.
- A convergence plot on a synthetic problem empirically verifying the claimed exponential rate.
- An illustration of orbit reconstruction storage cost vs. step count.
- Clarification of the seed distribution protocol and total per-step bidirectional bit count.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Missing algorithm description and Theorem 1 (critic's point #1):** Section 3 (method and theory) is absent from the extracted text because the PDF parser strips heavily-formatted technical content. The original submission contains Algorithm 1, Theorem 1, and their associated content. Per hard rules, criticisms about sections stripped by the parser are invalid.
- **Garbled text complaints (critic's Section 4 notes):** Criticisms about garbled sentences ("vithth del faster tha", "pardonably lower but comparable to ZO-FedSGD") and illegible tables are PDF parsing artifacts, not author errors. Per hard rules, these are removed.
- **Missing proof for DP guarantee (critic's Section 5 note):** The DP proof is likely in the stripped appendix. Per hard rules, criticisms about missing appendix content are removed.
- **YouTube comparison as "irrelevant communication":** This is a minor presentation choice that does not affect the paper's validity. While the framing could be tighter, it is not a substantive weakness.

## Novel Insights
The reviews surface an interesting tension: the paper's strongest claimed advantage (1-bit communication) is also the source of its main experimental ambiguity. The binary nature of FeedSign's output is what both enables the extreme compression and limits the damage from Byzantine attacks — but the current Byzantine evaluation doesn't cleanly separate these two properties. The paper would benefit from experiments that deliberately probe the boundary of this binary robustness (e.g., what fraction of Byzantine clients can be tolerated before accuracy degrades?). Additionally, the downlink ambiguity (how the seed is distributed without breaking the 1-bit claim) is a concrete technical gap that, once resolved, would significantly strengthen the paper's core narrative.

## Suggestions
1. **Clarify the seed distribution protocol.** Specify exactly how the PRNG seed is agreed upon each step, and compute the total per-step bidirectional bit cost (including seed broadcast if applicable). If seeds are deterministically derived (e.g., from step index), state this explicitly.
2. **Run a controlled Byzantine experiment.** Compare FeedSign and ZO-FedSGD under identical attack types (e.g., both attacked with reversed sign, both with random sign) to isolate the inherent robustness without confounding attack type with method.
3. **Report variance.** Include standard deviations over multiple random seeds (at least 3 runs) for key experiments, or justify the setting where this is infeasible.
4. **Add a comparison to a compressed-gradient baseline.** Even a brief comparison to signSGD or a Top-k compressor on a small-scale experiment would help position FeedSign within the broader communication-efficient FL landscape.
5. **Fix the ambiguous sentence on line 51** ("both ZO-FedSGD and FeedSign reach test accuracy pardonably lower but comparable to ZO-FedSGD") — this appears to be a garbled self-comparison.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>