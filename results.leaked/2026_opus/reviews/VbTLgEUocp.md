Now I have a clear view of the paper. Let me run calibration searches to determine a score.Round 1 bracket: This paper sits closest to the 7suavRDxe8 anchor (avg 4.80) — both are LLM-based deniable-encryption/steganography papers that lack formal security analysis. Calgacus has a novel "full capacity" framing and richer philosophical discussion, but suffers similar weaknesses. Plausible bracket: 4.0 – 6.0.Based on round 2, the closest topical anchor remains 7suavRDxe8 (Plausibly Deniable Encryption with LLMs) at avg 4.80 — both papers use LLMs to enable deniable encoding, both lack formal security analysis, both are creative but informal. Calgacus has a more novel "rank-replay" mechanism with full-capacity property and a richer philosophical discussion, but its empirical validation is thinner (only 300 stegotexts across 3 seeds) and it doesn't quantitatively compare to Meteor/Zamir. I'll place it slightly above the 4.80 anchor due to novelty of framing.

Now writing the consolidated review.

---

## Summary
The paper presents *Calgacus*, a simple LLM-based generative steganography protocol that hides a meaningful text inside another coherent text of identical token length. The mechanism is novel and elegant: record the rank sequence of the secret message's tokens under an LLM, then replay those ranks under a different secret prompt to produce a cover text. The remainder of the paper is a small empirical demonstration on Reddit posts, an informal security analysis, and a philosophical discussion on hallucination-as-absence-of-intent, with a concrete AI-safety scenario for covertly serving unaligned LLM outputs through aligned ones.

## Strengths
- **Novel "full-capacity" mechanism**: encoding via rank replay yields stegotext of the same token length as the secret message — a property that previously cited generative-stego approaches (Ziegler 2019, Meteor, Zamir, Wu) do not provide (Section 2, last paragraph; Section 3 recipe).
- **Practical and reproducible**: the entire protocol uses only an off-the-shelf 8B open-source LLM (Llama 3 8B), needs no training, and is shown to run in seconds on commodity hardware with a public GitHub demo (Abstract; Section 3).
- **Quantitative plausibility evidence**: Figure 4 shows that stegotext log-probabilities from 300 stegotexts fall squarely within the spread of 1,000 real Reddit posts, while random ASCII or English-word strings lie far outside that distribution — concrete support for the "looks plausible" claim.
- **Deniability argument**: Section 3.1 makes a specific, mechanism-grounded deniability claim — that outlier prompts can produce stegotexts with probability comparable to the original — and instantiates it (Figure 15 reference) rather than asserting it abstractly.
- **Conceptually rich discussion**: Section 4's reframing of hallucination as a void of intention, the Oulipo/*La Disparition* analogy, and the "unaligned chatbot disguised as aligned" scenario tie the technical mechanism to substantive AI-safety questions in a way that makes the protocol's significance concrete.

## Weaknesses

### Fatal
None.

### Major
- **Detectability is conceded but not characterized, undermining the security framing**: Section 3 itself states that "generally the original text can be discerned from its stegotexts by picking the most probable one according to a LLM," and Figure 4 shows that stegotexts shift to lower log-probabilities than the originals on average. The paper recasts this as "deniability," but this only holds for outlier prompts. The paper reports no detection ROC/AUC, no quantified false-positive/false-negative rates against a held-out detector, and no KL-divergence-style characterization of how much the rank-replay process shifts the distribution. Given that Meteor and Zamir (both cited) are explicitly designed to be indistinguishable from the LLM's sampling distribution, leaving this gap unaddressed makes it hard to position the security claim, including the application to "censored platforms in oppressive countries" in the introduction.
- **No quantitative comparison to cited prior LLM-stego methods**: Ziegler et al. (2019), Meteor (Kaptchuk et al., 2021), Zamir (2024), and Wu et al. (2024) are described in Related Work but not benchmarked against. The headline novelty is "full capacity" in tokens, but the paper does not show how Calgacus compares in bits-per-cover-token or in detectability against Meteor's entropy-aware arithmetic coding. The reader is left without a clear placement on the capacity/undetectability trade-off curve.
- **Capacity is conditional on payload entropy, but the framing flattens this**: The protocol works well for low-entropy English text (the Reddit experiment, the Caesar example) and breaks for high-entropy payloads — the hash example in Section 3 ("Considerations") explicitly produces gibberish, and the Limitations paragraph acknowledges this. Yet the abstract/intro promises hiding "the first page of the unreleased 8th Harry Potter book" inside an unrelated review, framing capacity as universal. No curve is provided relating payload entropy `H_LLM(e)` to stegotext coherence, even though this is the paper's most interesting empirical regularity.

### Minor
- **Thin empirical demonstration**: Three seed texts at µ, µ±2σ, with 100 stegotexts each (300 total) and only LLM log-probability as a metric (Section 3). No human evaluation of plausibility, no variance bars, and the cross-model check on Phi-3 is referenced but not reported as a quantitative detection rate. For a paper whose central empirical claim is "stegotexts lie within the real-text distribution," this is suggestive rather than conclusive.
- **The "Unaligned chatbot" scenario assumes conditions that the Limitations section flags as fragile**: Section 3's Limitations note that even GPU-architecture-level numerical drift breaks decoding (Shanmugavelu et al., 2024). The Section 4 chatbot scenario depends on the user running an identical oLLM under identical numerical conditions but doesn't revisit this caveat. Robustness to temperature ≠ 0, top-p sampling, or KV-cache quantization is not discussed.
- **Brute-force key-space bound `O(d^|k|)` overstates difficulty**: Section 3.1's bound assumes uniform key entropy, while the same paragraph argues `k` is natural language (≈1.5–3 bits/token in practice). The "insert a random string in `k`" defense is asserted rather than quantified. These adjustments would tighten Section 3.1 without changing the headline claims.
- **Threat model in the discussion is stronger than the one defended in 3.1**: In the chatbot scenario the auditor may know the model and may even suspect rank-replay; Section 3.1's analysis assumes ignorance of `k` only. No discussion of detection in the stronger adversarial setting is given.

### Trivial
- **Tokenizer-alignment edge case not discussed**: the protocol assumes deterministic re-tokenization of `e` with and without `k'`; with BPE this can fail near rare characters. Worth a sentence.
- **Variation involving `k'` is described but not evaluated**.

## Nice-to-Haves
- A side-by-side table positioning Calgacus against Meteor/Zamir/Ziegler on (i) bits per cover token, (ii) per-token KL from the natural LLM distribution, (iii) detection AUC against a held-out LLM detector. This would clearly localize Calgacus's operating point on the capacity/undetectability curve and convert "full capacity" from a single number into a meaningful trade-off statement.
- A curve relating payload entropy `H_LLM(e)` to stegotext coherence (e.g., interpolating from Reddit posts to random hashes). This is the paper's most interesting empirical regularity and is currently buried in a paragraph.
- A small-scale human-distinguishability study of Calgacus covers vs. genuine Reddit posts. Would directly back the "remains opaque to humans" claim asserted but not tested in Section 3.
- An empirical test of the philosophical claim that the "knowledge through high-probability assignment" question is meaningful — e.g., whether rank-encoding survives when the cover LLM provably never saw the payload.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "The paper does not engage with Cachin (1998) seriously / does not formalize a steganographic security model." — The paper explicitly cites Cachin and explains, in Section 2, that it deliberately avoids "building a palace on the sand" given known limitations of formal stego models. The reviewer's complaint is essentially a request that the paper not be the paper it is. Demoted; the substantive piece (lack of detection-rate evidence) is already captured under Major.
- "Application to censored platforms is not supported by the evidence." — This overlaps with the Major weakness on detectability; merging avoids double-counting.
- "Strength: novel AI-safety application (disguised unfiltered LLMs)" — kept as part of the Discussion-strength bullet; the standalone framing in the strength finder partly conflicts with the verified Major weakness that the same scenario relies on identical-numerics deployment, so it is folded in rather than listed twice.
- Generic strengths from the Strength Finder ("training-free, no fine-tuning needed") — folded into the "practical and reproducible" bullet rather than listed separately.

## Novel Insights
The protocol's most genuinely novel observation is not the steganographic mechanism itself but what it implies operationally: that an LLM can produce coherent text where every word is selected under an externally-imposed constraint orthogonal to authorial intent, and the result is still indistinguishable to a human reader. This decouples surface coherence from intentionality more sharply than prior LLM-stego work, and it gives a clean operational handle on the "hallucination as absence of intent" reframing — a hallucination is text that satisfies a coherence constraint without binding to a reality-affecting goal. Beyond that reframing, the paper's contributions are well-captured by its own write-up.

## Suggestions
- Reposition the security claim explicitly: "Calgacus trades undetectability against an LLM-based statistical test for full token-parity," and locate it on the capacity/undetectability trade-off curve relative to Meteor and Zamir.
- Add a held-out detection-rate evaluation (a second LLM, plus a simple statistical test) so the reader can see *how* detectable the channel is and at what payload entropy.
- Add an entropy-vs-coherence curve sweeping from Reddit posts to random hashes; this would convert "full capacity" from a slogan into a quantitative claim.
- Revisit the unaligned-chatbot scenario explicitly under the GPU-numerics caveat: state which deployment configurations make it feasible and which break it.
- Quantify, rather than assert, the "random string in `k` nips brute-force in the bud" claim.

---

**Axis-by-axis assessment.** *Originality*: high — the rank-replay mechanism and "full capacity" property are a genuinely new operating point in LLM steganography, and the hallucination-as-void-of-intent reframing is conceptually fresh. *Importance of the question*: high — same-length covert encoding via LLMs has direct AI-safety implications. *Claim support*: mixed — the plausibility-within-distribution claim is supported by Figure 4 but with thin sampling; the security/deniability claim is weakly supported, with the paper itself conceding aggregate distinguishability. *Soundness of experiments*: limited — three seeds, 300 stegotexts, one detector (the same LLM), one second-model spot-check. *Clarity of writing*: strong — the recipe is reproducible, the examples are vivid, the discussion is well-crafted. *Value to the community*: moderate-to-high as a conceptual contribution and conversation-starter; lower as a SOTA-method contribution because of the missing head-to-head benchmarks.

**Anchors used:**
- Round 1 (bracketing): `jbfDg4DgAk.md` (avg 3.00, Reject) — sparse LLM watermark, weak anchor; `BeOEmnmyFu.md` (2.50, Reject) — jailbreak via language games, weak anchor; `kT6oc5CpEi.md` (3.00, Reject); `TgTxJALwDz.md` (2.33, Reject); `urQi0TgXFY.md` (5.00, Reject) — emergent steganographic collusion in LLMs, mid anchor, similar domain; `7suavRDxe8.md` (4.80, Reject) — *Plausibly Deniable Encryption with LLMs*, closest topical match; `0KHW6yXdiZ.md` (5.25, Reject); `6p8lpe4MNf.md` (5.50, Accept); `syThiTmWWm.md` (7.75, Accept) — strong anchor, less similar; `Bo62NeU6VF.md` (8.00, Accept); `j7b4mm7Ec9.md` (7.60, Reject); `oZtt0pRnOl.md` (8.00, Accept) — strong anchors, mostly unrelated.
- Round 1 bracket: 4.0–6.0 based on heavy overlap with 7suavRDxe8 and urQi0TgXFY.
- Round 2 (narrowing): `hgv11VQnIk.md` (4.75, Reject); `fh8EYKFKns.md` (5.25, Accept) — AGI alignment position paper, comparable in conceptual ambition; `pETSfWMUzy.md` (6.00, Accept); `V01FPV3SNY.md` (5.33, Reject); `0koPj0cJV6.md` (4.60, Reject) — black-box LLM watermark, distortion-free framing similar; `9k0krNzvlV.md` (5.75, Accept) — watermark learnability; `P5UETqZXqT.md` (5.75, Reject); `cLTM1gc6Qm.md` (6.00, Reject); `QzPKSUUcud.md` (6.25, Accept) — simple-framework segmentation paper, very different topic; `v675Iyu0ta.md` (5.60, Reject).
- Compared to `7suavRDxe8` (4.80), Calgacus has a cleaner and more elegant mechanism (rank replay), a better real-world demo, and a richer discussion, but suffers a similar Achilles heel: informal security and detectability shifted away from the natural distribution. Compared to `urQi0TgXFY` (5.00), Calgacus is more focused and has a sharper conceptual punch. Compared to `9k0krNzvlV` (5.75, Accept) and `0koPj0cJV6` (4.60, Reject), Calgacus's empirical rigor is closer to the weaker anchor while its conceptual originality is closer to the stronger one. Final score positioned modestly above `7suavRDxe8` and at parity with `urQi0TgXFY`.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>