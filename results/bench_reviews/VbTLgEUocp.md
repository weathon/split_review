Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary

This paper presents *Calgacus*, a steganographic protocol that uses LLMs to encode a meaningful text (the secret message $e$) inside another plausible, steerable text $s$ of the same token length. The core idea is elegant: extract token ranks of $e$ under the LLM's own probability distribution, then generate $s$ by forcing the LLM to pick the $r_i^{\text{th}}$ most probable token at each step when conditioned on a secret prompt $k$. The secret message can be perfectly recovered by anyone possessing $k$ and the identical LLM. The paper demonstrates the method using Llama 3 8B, shows stegotexts fall within the log-probability distribution of real text, and discusses implications for AI safety, deniability, and the nature of LLM knowledge.

## Strengths

- **Novel full-capacity steganographic protocol.** The core idea — using token ranks from one context to steer generation in another, producing a stegotext of exactly the same token length as the hidden message — is genuinely clever, simple, and not present in prior LLM steganography work (which typically encodes bits per token at sub-capacity rates). The fact that the stegotext and secret message have identical length is a distinctive property.

- **Insightful analysis of the probability gap.** The paper identifies and explains why stegotexts are typically less probable than their originals despite preserving token ranks: "wasted" rank-1 tokens that occur at low-entropy positions where the model would almost always pick rank 1, but the rank sequence inherited from $e$ often demands a different rank. This is a non-obvious and well-analyzed observation (Figure 5).

- **Honest engagement with limitations.** The paper explicitly discusses failure modes: the hash example (line 127) shows that improbable messages produce gibberish stegotexts, and the Limitations paragraph (line 153) acknowledges dependencies on $e$, $k$, and the LLM, as well as the identical-conditions requirement for sender and receiver. This contrasts with the harsh critic's claim that the paper ignores these constraints.

## Weaknesses

### Fatal

None.

### Major

- **Experimental evaluation is thin for the breadth of claims.** The quantitative evaluation uses only 3 hand-picked Reddit posts as secret messages, 100 stegotexts per message, and a single metric (log-probability under the generating LLM). No human evaluation of coherence/fluency, no automatic quality metrics beyond log-probability (e.g., MAUVE, perplexity under independent models), and no comparison to any existing steganographic baseline are provided. The chatbot scenario in Section 4 is presented as a single qualitative example with no metrics. While the evaluation that exists supports the core claim (stegotexts are plausible), it is insufficient to substantiate the paper's broader assertions about "high-quality results" and practical viability across diverse settings. The paper would benefit substantially from evaluation on a wider range of secret messages and from comparisons against existing LLM steganography methods.

### Minor

- **The framing in the abstract and introduction could be more precise about message-space limitations.** The abstract states the protocol encodes "a meaningful text" but does not qualify that the quality of the stegotext degrades when the secret message contains tokens the LLM assigns low probability. The hash example in Section 3 demonstrates this failure mode clearly, and the paper does discuss it, but readers of only the abstract may form inflated expectations. The phrase "arbitrary meaningful text" in the introduction is helpful but could be sharper.

- **Security discussion is limited in scope.** The paper is upfront about avoiding formal security models (line 66: "we will avoid building a palace on the sand"), which is a defensible choice for a proof-of-concept paper. However, the deniability argument rests on a qualitative observation from Figure 4 — that some stegotexts have probabilities "in the same ballpark" as originals — without quantifying how often this occurs or how easy it is to find such decoy keys. A more systematic investigation of deniability would strengthen the contribution.

### Trivial

None identified that are not parser artifacts.

## Nice-to-Haves

- **Formal deniability analysis.** Quantifying how often a random key yields a recovered message with probability comparable to (or exceeding) the true secret message would make the deniability claim more precise.

- **Broader evaluation of the chatbot scenario.** Measuring latency, failure rates, and testing whether the decoy defense is plausible would elevate the scenario from a thought experiment to a demonstrated threat.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"The method does not hide arbitrary content; the paper does not even discuss this constraint."** REMOVED. The paper explicitly discusses this at line 127: "If $e$ is difficult to guess for the LLM, ranks will be high and $s$ will be gibberish; for instance the hash..." and reiterates it in Limitations (line 153). The constraint is acknowledged. The intro uses "meaningful text" as a qualifier. The criticism overstates the issue.

- **"The security and deniability arguments are essentially anecdotal and lack quantitative rigor."** PARTIALLY REMOVED — the demand for a *formal* security model conflicts with the paper's explicit scoping (line 66) and with community norms for proof-of-concept steganography papers. The softer version of this concern (quantifying deniability more precisely) is retained as a Minor weakness and Nice-to-Have.

- **"The paper's overblown philosophical implications inflate the contribution."** REMOVED. This is a subjective judgment about writing style. The discussion section is clearly demarcated from the technical contributions and explores genuine implications of the work. Whether one finds it "overblown" is a matter of taste, not a scientific flaw.

- **Strength: "Practical efficiency with modest models" as a standalone strength.** REMOVED as too generic — many papers demonstrate practical efficiency. The fact that the method works on 8B-parameter models is noted in the summary but does not merit a separate strength.

- **Strength: "Concrete demonstration of an AI-safety threat."** WEAKENED and merged into the summary. The chatbot scenario is interesting but presented as a thought experiment with only a single qualitative example; calling it a "concrete demonstration" overstates the evidence.

- **Strength: "Reframing of hallucinations as a deficit of intent."** REMOVED as a standalone strength. While interesting, this is a philosophical observation rather than a technical contribution verified by the paper's experiments.

- **All parser-artifact complaints (typos, formatting, figure rendering).** REMOVED per hard rules — these are parser issues, not author errors.

## Novel Insights

The analysis of why stegotexts are systematically less probable than originals despite preserving exact token ranks — the "wasted rank-1 tokens" phenomenon — is a genuinely novel observation. The paper shows that while a good LLM assigns probability >95% to the top token at low-entropy positions, the frequency of rank-1 tokens in natural text is only ~40%, meaning many rank-1s are "spent" at high-entropy positions where they contribute relatively little probability mass. This insight would apply to any rank-preserving generative procedure and is not obvious a priori.

## Suggestions

- Add a systematic evaluation across a broader set of secret messages (e.g., 50-100 texts from diverse domains) with at minimum perplexity under an independent LLM as a quality metric.
- Quantify the deniability property: for a sample of stegotexts, compute how many random or near-random keys yield recovered messages with probability exceeding that of the true secret, and report the distribution.
- Include a simple steganalysis baseline: can an independent LLM distinguish stegotexts from real texts (e.g., via likelihood ratio), and does this depend on the choice of $k$?

## Score and Decision

**Calibration anchors considered:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/ZujfJpD6as.md` | 3.50 | *StegoAttack (jailbreak via steganography)* — Rejected for limited novelty, replication concerns, and fundamental methodological gaps. The current paper has a substantially more novel core idea and honestly addresses its limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/qF6TyKhc7S.md` | 4.00 | *MajorMark (multi-bit watermarking)* — Rejected for incremental contribution and missing baselines. The current paper's rank-matching protocol is more original. |
| `/home/wg25r/review_agent/human_reviews_2026/q4qxtaKVAU.md` | 6.00 | *Early Signs of Steganographic Capabilities* — Accepted (poster). Systematic evaluation across many models but limited algorithmic novelty (evaluation paper). The current paper has higher novelty but much thinner evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/6cEPDGaShH.md` | 6.00 | *Malicious Finetuning via Steganography* — Accepted (oral). Novel threat demonstrated on multiple models with solid evaluation. The current paper has comparable novelty but weaker experimental validation. |
| `/home/wg25r/review_agent/human_reviews_2026/gdZ6J5hZzF.md` | 7.33 | *Sequences of Logits Reveal Low Rank Structure* — Accepted (oral). Strong theoretical contribution with empirical validation. The current paper is less rigorous. |

The paper introduces a genuinely novel and elegant protocol. Its core idea is stronger than the 6.0 evaluation-focused paper (q4qxtaKVAU) but its experimental validation is thinner than both 6.0 papers. It is clearly above the 3.5-4.0 rejected papers, which suffer from more fundamental issues. The paper's honesty about limitations and its insightful analysis of the probability gap are strengths, but the thin evaluation prevents it from reaching the 6.0+ tier where experimental thoroughness becomes expected. A score of 5.5 reflects this position: a borderline paper with a strong conceptual contribution that needs more empirical support to be fully convincing.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>