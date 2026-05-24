Now I have all the evidence I need. Let me construct the final review.

---

## Summary

DeCodec reframes neural audio codecs as universal disentangled representation learners. It introduces a Subspace Orthogonal Projection (SOP) module to decompose mixed audio embeddings into orthogonal speech and background sound subspaces, a Representation Swap Training (RST) procedure to ensure those subspaces correspond to the correct signal components, and Semantic Guidance (SG) to further separate speech into semantic and paralinguistic representations. A single trained model demonstrates reconstruction, speech enhancement, and one-shot voice conversion on noisy speech.

## Strengths

- **Novel architectural contribution for disentanglement in codecs.** The SOP module combined with RST is a genuinely creative approach to decoupling speech and background sound in the representation domain. Unlike prior codecs that either ignore the speech/BGS distinction or only classify audio types, DeCodec explicitly factorizes the embedding space into orthogonal subspaces (Eq. 2–5), and RST provides a data-augmentation-style training signal (Eq. 12) that encourages those subspaces to capture the intended signal components. This is a step beyond existing disentangled speech codecs (SpeechTokenizer, FACodec) which operate only on clean speech.

- **The ablation study cleanly validates the necessity of each component.** Table 4 shows that SOP alone (SDR-B: −13.15, SDR-S: −1.91) and RST alone (SDR-B: −10.67, SDR-S: 3.03) are individually ineffective for decoupling, but their combination (Ablation-3: SDR-B 0.49, SDR-S 7.90) achieves meaningful separation. Adding SG then substantially reduces WER (41.9 → 25.8/23.6), confirming the hierarchical decomposition. This is a well-structured, convincing ablation.

- **Competitive results across multiple tasks from a single model.** The non-causal DeCodec achieves the best SDR on both clean (7.61 dB) and noisy (5.21 dB) reconstruction (Table 1), the best DNSMOS OVL scores on the DNS Challenge test set for both simulated and real recordings (Table 2), and lower WER than the StoRM-SpeechTokenizer cascade for one-shot VC on noisy speech (50.46 vs 52.73, Table 3). Demonstrating strong performance across reconstruction, enhancement, and conversion from one architecture is a meaningful empirical contribution.

- **The SE approach via representation manipulation is elegant.** Rather than training a separate enhancement model, DeCodec simply replaces the background sound quantized vectors with those from a blank audio (Section 4.2.2). The BAK scores (4.13/3.99) being the highest among all compared systems supports that the disentanglement is real and practically useful.

## Weaknesses

### Fatal

None.

### Major

- **The theoretical justification for the RST procedure (Section 3.6, Eq. 13–16) does not prove what it claims.** The argument attempts to show that Zs₁ must be independent of n₁ by subtracting two approximate decoder equalities, applying the mean value theorem, and observing that the right-hand side of Eq. 16 is independent of Zs₁ while the left-hand side depends on it through ξ. This reasoning is non-rigorous: the MVT guarantees existence of some ξ (which is itself a function of Zs₁, Zn₁, Zn₂), so the derivative term ∂Dec/∂Zn|ξ can absorb the Zs₁ dependence. The claimed independence does not logically follow from the stated premises. The paper would be stronger by replacing this with a more modest and accurate characterization of what RST encourages (e.g., decorrelation or mutual information minimization), rather than presenting an invalid independence proof. This matters because the paper uses the proof to claim that RST "forces" the quantized vectors to contain only speech/BGS information — a claim that the derivation does not support.

### Minor

- **The computation protocol for SDR-B and SDR-S in the ablation study is not specified.** Table 4 reports SDR-B and SDR-S as "signal distortion ratios for reconstructing decoupled background sound and decoupled speech," but the paper never explains how these decoupled signals are obtained (e.g., which representations are zeroed out, how the decoder is queried). Without this detail, the absolute SDR-B/S values are hard to interpret, though the relative comparisons within the ablation (showing that SOP+RST dramatically improves both metrics) remain informative.

- **The DAC reconstruction SDR (0.60 dB in Table 1) is anomalously low** relative to that codec's known quality. While the paper uses official checkpoints and the same evaluation pipeline for all models, this outlier suggests a potential SDR computation issue (e.g., gain/delay sensitivity) that makes the comparison specifically against DAC unreliable. The comparisons against EnCodec and SpeechTokenizer — where SDR values are in expected ranges — remain informative, and DeCodec's own SDR values do not depend on baseline correctness. The authors should verify the DAC SDR computation or provide details on alignment/scaling.

- **The VC experiment yields a WER of 50.46%**, which the paper attributes to voicing mismatches. While DeCodec does outperform the StoRM-SpeechTokenizer cascade (52.73%), and the paper acknowledges this limitation, the result indicates that the semantic-paralinguistic decomposition is fragile under cross-speaker transfer on noisy input. This limits the strength of the "universal front-end" claim for generation tasks and should be discussed more candidly.

- **The SOP orthogonality guarantee is conditional.** Equation 6 states that P_S P_N^T = 0 follows from the orthogonality loss only when the encoder's output covariance YY^T is diagonal. This condition is not enforced by any loss, so the learned projection matrices are not guaranteed to be truly orthogonal projectors. The practical orthogonality of S and N is what the loss directly optimizes, which is sufficient for the method to work, but the paper's language about "orthogonal projection matrices" overstates what is actually guaranteed.

### Trivial

- The paper uses "an universal" in several places (title, abstract, introduction) where "a universal" would be grammatically correct.
- Several minor typos: "vlock" for "block" (line 258), "donates" for "denotes" (line 116), "These allows" (line 15).

## Nice-to-Haves

- Evaluation on reverberant or overlapped-speech scenarios would strengthen the "universal" claim, since the current training uses only additive anechoic mixtures of speech and environmental noise.
- An analysis of how bitrate allocation between SRVQ and NRVQ affects decoupling quality would be informative.
- SI-SDR or similar intrusive metrics for the SE task would complement the non-intrusive DNSMOS scores and help characterize codec-induced distortion.
- Listening tests for at least one task (SE or reconstruction) would substantially strengthen the perceptual quality claims.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic claimed "No comparison with a modern cascade of separation followed by clean-speech/background-sound codecs."** — The paper does include this comparison: StoRM-SpeechTokenizer is evaluated as a cascade baseline in Table 3 (one-shot VC), and DeCodec outperforms it (WER 50.46 vs 52.73). While the cascade comparison exists only for VC, not for SE or reconstruction, the paper explicitly positions the VC comparison as testing the claim that "decoupling in the representation domain introduces less error than front-end time-domain separation" (Section 4.2.3), which the result supports. The harsh critic's framing that "no comparison" exists is factually incorrect.

- **Strength Finder claimed "RST is accompanied by a theoretical proof... [as] critical evidence."** — As discussed under Major Weaknesses, the MVT-based argument does not constitute a valid proof. This claimed strength was removed.

- **Harsh critic claimed the SE evaluation uses DNSMOS which "can be optimistic for processing that simply removes background noise but introduces subtle artifacts."** — DNSMOS is a standard and widely accepted metric in the speech enhancement community (used by the DNS Challenge itself). While listening tests would be ideal, criticizing the use of DNSMOS as the primary SE metric is unreasonable given community norms. The SIG scores do show a gap vs. SELM, which the paper acknowledges.

- **Harsh critic's "Section-by-Section Notes" on SG setup being "standard; no novelty here"** — The paper does not claim SG as novel; it cites SpeechTokenizer and uses it as an established technique. Using a standard technique within a novel architecture is not a weakness.

- **Harsh critic's note that "the auditory-cortex analogy is plausible but not strictly necessary"** — This is a motivational framing choice, not a technical weakness.

## Novel Insights

None beyond the paper's own contributions. The core insight — that a codec trained with orthogonal subspace projection and cross-sample representation swapping can learn to disentangle speech from background sound in the latent space — is the paper's contribution and was not independently surfaced by the reviews.

## Suggestions

- Replace the MVT-based "proof" in Section 3.6 with a clear statement of what RST encourages empirically (e.g., that minimizing L_RST with orthogonal subspaces promotes statistical independence between Zs and the background sound, and vice versa), supported by the ablation results. A formal proof is not necessary for the contribution to stand; an overclaimed proof is worse than an honest empirical characterization.
- Specify the exact protocol for computing SDR-B and SDR-S, including which representations are zeroed/substituted and how the decoder output is compared to the reference.
- Verify and report the SDR computation details for DAC to ensure fair comparison, or add a footnote explaining the discrepancy.
- Add a more candid discussion of the VC WER limitation, clarifying that the current decomposition is sufficient for tasks like SE and reconstruction but may need further refinement for generation tasks requiring precise timbre transfer.

## Score and Decision

**Round 1 bracket:** Based on broad topical anchors (neural audio codecs, disentangled speech representations), the paper plausibly sits between 3.0 and 8.0. Weak-band anchors (DM-Codec at 3.00, USC at 4.80) are clearly below this paper; strong-band anchors (FlowDec at 7.00, HALL-E at 6.40) are above or near this paper. Bracket narrowed to **5.0–7.0**.

**Round 2 narrowing:** I compared against RepCodec (5.50, rejected — simpler codec, narrower scope), Vec-Tok Speech (5.20, rejected — less principled disentanglement), USC (4.80, rejected — weaker results), FlowDec (7.00, accepted — more rigorous evaluation, listening tests), and HALL-E (6.40, accepted — strong engineering contribution).

DeCodec is stronger than RepCodec, Vec-Tok, and USC: it has a genuinely novel disentanglement mechanism (SOP+RST), competitive results across three tasks, and a clean ablation. It is weaker than FlowDec: the evaluation is less rigorous (no listening tests, missing metric definitions), the theoretical claims are overreached, and the VC results are not practically compelling. Against HALL-E (6.40), DeCodec has a comparably novel contribution but less polished execution and evaluation.

**Final score: 6.0.** The paper makes a real contribution — the SOP+RST mechanism for disentangling speech and background sound in a neural codec is novel and well-ablated — but the theoretical overclaiming, missing evaluation details, and practical limitations in VC prevent it from being a clear accept. It sits between RepCodec (5.50) and HALL-E/FlowDec (6.40–7.00), closer to the lower-acceptance borderline.

**Anchor summary:**

| Anchor | Avg Score | Round | Comparison to DeCodec |
|---|---|---|---|
| DM-Codec (UFwefiypla) | 3.00 | R1 | DeCodec much stronger — more novel, better results |
| USC (Id2JMVSQHZ) | 4.80 | R1/R2 | DeCodec stronger — more tasks, cleaner ablation |
| Vec-Tok Speech (C53xlgEqVh) | 5.20 | R2 | DeCodec comparably scoped but more principled disentanglement |
| RepCodec (LfDUzzQa3g) | 5.50 | R1 | DeCodec stronger — more architecture novelty, more tasks |
| Codec-LM Co-design (KCVv3tICvp) | 5.00 | R2 | DeCodec stronger — more ambitious scope |
| HALL-E (868masI331) | 6.40 | R2 | HALL-E slightly stronger — more polished execution |
| FlowDec (uxDFlPGRLX) | 7.00 | R2 | FlowDec clearly stronger — listening tests, rigorous evaluation |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>