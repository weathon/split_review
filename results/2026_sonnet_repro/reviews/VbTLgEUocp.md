Now let me do the calibration search to properly score this paper.Now I have enough information to write the final review. Let me compile it.

---

## Summary

*Calgacus* is a simple, elegant steganographic protocol that hides an arbitrary text inside another coherent, steerable text of the **exact same token length** using a Large Language Model. The mechanism encodes each token of the hidden message as a rank in the LLM's probability distribution, then generates a cover text by selecting tokens at those ranks from a different prompt. The paper demonstrates the method empirically using Llama 3 8B on Reddit posts, discusses security properties including deniability, and develops philosophical implications around hallucination and LLM intent.

---

## Strengths

- **Same-length steganography with perfect recovery:** The protocol deterministically maps each token of the hidden message to a rank, guaranteeing exact token-for-token length parity and lossless recovery by anyone with the key and the same LLM (Section 3, Figure 3). This combination of same-length coverage and exact recovery is a concrete and distinguishing property not shared by most prior methods.

- **Quantitative plausibility evidence:** Figure 4 directly compares log-probabilities of 100 stegotexts per original against 1000 real Reddit posts, showing that stegotexts fall within the real-text distribution—a clear, falsifiable empirical test of the core quality claim.

- **Mechanistic explanation of the quality gap:** The "low entropy token choices" analysis (Section 3 + Figure 5) provides a quantitatively grounded explanation for why stegotexts are on average less probable than originals despite preserving token ranks. This is a genuine insight beyond the protocol description itself.

- **Deniability construction:** Section 3.1 identifies that outlier prompts can yield stegotexts comparable in probability to the original, providing a concrete deniability mechanism (backed by Figure 15, referenced in the paper).

- **Steerability demonstrated:** Figure 1 shows that the same hidden political critique can be embedded in texts steered to entirely different topics (culinary recipe vs. political speech), validating the claimed steerability of topic and style.

- **Philosophical contribution on hallucination:** The reframing of hallucination as "lack of intention" rather than factual error (Section 4) is an original and well-argued intellectual contribution grounded directly in the protocol's mechanics.

---

## Weaknesses

### Fatal
None.

### Major

- **Evaluation is too thin to support generalizing claims.** The empirical evaluation rests on exactly three original texts at percentiles μ, μ−2σ, and μ+2σ of the Reddit log-probability distribution, one LLM (Llama 3 8B), and one text length (85 tokens). The abstract claims "a message as long as this abstract can be encoded...in seconds" and Section 3 implies generality across domains and lengths, but these claims are not substantiated in the main paper. Three original texts is insufficient to warrant the broad framing, and the sole test at 85 tokens leaves open whether quality degrades at the 200-token lengths implied by the abstract examples (Figure 1 texts are ~100 tokens). The cross-model validation with Phi-3 3.8B on log-prob shift is a positive step, but it still doesn't test different text lengths or genres.

- **No experimental comparison against prior steganography methods.** The paper acknowledges Meteor (Kaptchuk et al., 2021) and Zamir (2024) as related methods. In particular, Zamir's method is described as encoding "without modifying the response distribution of the LLM"—a property *strictly stronger* than what Calgacus achieves (Calgacus produces a detectably shifted distribution, as Figure 4 shows). The paper never explains what Calgacus gains over Zamir in practice (simplicity? speed? steerability?), nor does it include any side-by-side comparison on stegotext quality, detection rate, or throughput. Without this comparison, the contribution's significance relative to existing work remains asserted rather than demonstrated.

### Minor

- **Security claims remain qualitative where quantitative analysis is feasible.** The paper shows a probability histogram separation between originals and stegotexts (Figure 4) and notes that "LLMs can uncover a distinction between original texts and most of their encoded counterparts," but stops short of computing a detection AUC or ROC curve. The machinery is already in place (log-prob evaluations on Llama 3 and Phi-3); a threshold-classifier accuracy number would transform the security discussion from qualitative to falsifiable.

- **The "full capacity" label overreaches information-theoretically.** The paper's framing of "full capacity" (Section 2: "the stegotext and the secret message being of the same length") refers strictly to token-count parity, not information-theoretic channel capacity. The actual bits-per-token encoded depends on the rank entropy of the original text, which varies widely. For a low-entropy original (many rank-1 choices), rank sequences are dominated by 1s and carry little information per token. The paper discusses this qualitatively in the "Low entropy token choices" section but never quantifies the average rank entropy across typical texts, leaving the "full capacity" claim without informational grounding.

- **The AI safety threat model has a structural transparency issue.** Act 4 of the "unfiltered chatbot" scenario explicitly states that "the USER receives on the chatbot platform the censored answer to their query c, which includes the reasoning trace t and the actual answer s"—meaning the decryption key `t` is broadcast alongside the stegotext `s` in the open channel. Any monitor watching the conversation can observe both. The paper presents this as a "formidable application with immediate consequences for AI safety," but the practical threat is limited by this key-in-the-clear design. The scenario remains interesting as a proof-of-concept and thought experiment, but the urgency framing overstates the near-term risk.

### Trivial
None.

---

## Nice-to-Haves

- A brief analysis of average rank entropy across the 1000 Reddit posts—bits per token in the rank sequence—would give the "full capacity" claim meaningful information-theoretic grounding and allow a genuine comparison to Meteor/Zamir on channel utilization.

- Even a single ablation varying text length (e.g., 50, 85, 150, 200 tokens) would significantly strengthen the generalization claim in the abstract.

- A simple detection ROC curve using a log-probability threshold detector, as the paper already has all required evaluations in place, would sharpen the security section considerably.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Zamir (2024) offers strictly stronger security guarantees, thus Calgacus is inferior" (Harsh Critic):** Removed. The paper's goal is not to maximize security guarantees but to demonstrate same-length steganography—a different design target. Zamir's distribution-preserving property comes at different computational or practical costs the paper does not claim to beat. The critic's framing imposes a ranking the paper does not assert. Retained only as a "no comparison" concern (Major weakness above).

- **"The exact-recovery requirement (identical logits) is a fatal flaw buried in Section 3 Limitations" (Harsh Critic):** Demoted/removed from fatal tier. The paper explicitly acknowledges this in Section 3 ("sender and receiver must run the chosen LLM under identical conditions...performing the same approximations and obtaining identical logits. This may be a challenge when using different GPU architectures") and cites Shanmugavelu et al. (2024). The constraint is real but is disclosed; it does not invalidate the protocol, which is demonstrated to work in practice.

- **"The protocol is a trivial variation of standard generation" (implicit in discussion):** Removed. Simplicity is a feature, not a weakness; the paper makes no claim of algorithmic complexity and the steganographic application of rank-based generation is genuinely novel.

- **Strength: "Protocol works on commodity hardware in seconds" (Strength Finder):** This is a real, empirically supported property (abstract + Section 3), but it is not an independent strength—it follows directly from the rank-lookup algorithm and is better read as a practical detail.

---

## Novel Insights

The paper's most genuinely novel intellectual observation—beyond the protocol mechanics—is the proposed reframing of LLM hallucination. Rather than defining hallucination as a factual error, the paper argues it is a **void of intention**: the reader's inability to attribute authorial purpose to the text. This is grounded directly in the protocol: a stegotextual recipe for roasted boar may be factually correct and linguistically coherent, yet is unambiguously a hallucination in the sense that no culinary intent underlies it. This shifts hallucination from an epistemic failure (wrong facts) to a relational one (severed intent-text bond), with implications for how we trust any LLM-generated text—including non-stegotextual output. The Oulipo parallel (Section 4) is apt and deepens this point: even legitimate LLM generation is, at every step, honor-bound to a token prescribed by an external random variable rather than by purpose, making *all* LLM text structurally Oulipian.

---

## Suggestions

1. Add a length ablation table (50–200 tokens) in the main paper to validate the abstract's "as long as this abstract" claim empirically.
2. Compute a detection ROC or AUC against a simple log-prob threshold adversary; the cost is marginal given existing infrastructure.
3. Include at least a qualitative discussion—ideally a brief quantitative comparison—of what Calgacus achieves that Zamir (2024) does not, or cannot achieve as simply; this is the most pressing positioning gap.
4. Quantify average rank entropy (bits/token) for the three test originals to ground the "full capacity" claim informationally.
5. Moderate the AI safety framing slightly to reflect the key-in-the-clear constraint; present it as a compelling proof of concept with caveats rather than an "immediate consequence."

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Human Score | Round | Comparison |
|---|---|---|---|
| 7suavRDxe8.md (Plausibly Deniable Encryption w/ LLMs) | 4.80 | R1/R2 | Most topically similar; similarly thin evaluation and no formal analysis; rejected |
| urQi0TgXFY.md (Steganographic Collusion in LLMs) | 5.00 | R1/R2 | Same domain, broader experiments, but more diffuse contribution; rejected |
| kRJNV8RCE3.md (Hiding Images in Diffusion Models) | 4.75 | R1 | Related steganography domain; rejected |
| 6p8lpe4MNf.md (Semantic Invariant Watermark for LLMs) | 5.50 | R1 | LLM text generation modification; accepted; substantially broader evaluation |
| hTUrBJqECJ.md (Watermark for Low-entropy LLM Gen) | 5.50 | R2 | LLM token-level modification, better evaluation; rejected |
| SCBn8MCLwc.md (False Refusal Mitigation) | 5.75 | R2 | Simple method for LLM safety; accepted; comparable simplicity but more rigorous evaluation |
| 49ZYkhEGmv.md (AI Safety via Debate) | 6.50 | R2 | AI safety, formal protocol; accepted; considerably more rigorous |
| jbfDg4DgAk.md (Sparse Watermarking in LLMs) | 3.00 | R1 | LLM text modification, clearly weaker; rejected |

**Round 1 bracket:** 4–6.  
**Round 2 narrowing:** The paper sits closer to the 4.75–5.0 anchors (7suavRDxe8, urQi0TgXFY, kRJNV8RCE3) than to the 5.5+ papers. The latter have systematically larger evaluations, and the paper's three-text empirical base and absent baseline comparison are real differentiators pulling it toward the lower end. The protocol is more elegant than the 4.8-anchor paper, and the philosophical discussion is a genuine added value that the collusion paper lacks. The paper sits marginally above the 5.0 reject anchors in concept but does not clear the evaluation bar of the 5.5+ accept papers.

**Evaluation on key axes:**
- *Originality:* High — same-length steganography is a real and novel property; hallucination-as-intention reframe is genuinely original.
- *Importance of research question:* Medium-high — covert LLM communication is an active safety concern.
- *Claims well-supported:* Partially — core plausibility claim is well-supported; generalization claims and "full capacity" framing are not.
- *Soundness of experiments:* Low-medium — three texts, one model, one length, no baseline comparison.
- *Clarity of writing:* High — one of the paper's clear strengths.
- *Value to the research community:* Medium — interesting proof of concept with notable philosophical content, but insufficient empirical rigor for a methods-paper submission at a top ML venue.

**Final score:** 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>