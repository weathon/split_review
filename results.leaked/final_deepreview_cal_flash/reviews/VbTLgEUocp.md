## Summary

The paper presents *Calgacus*, a protocol that uses an LLM to hide a secret text within a different, steerable "stegotext" of the **same token length** — a property the authors term "full capacity" that prior LLM-based steganographic methods lack. The method is remarkably simple: extract the rank of each token of the secret text under the LLM's distribution, then generate the stegotext by selecting the corresponding-ranked tokens from the LLM's distribution conditioned on a secret steering prompt. Decoding proceeds in reverse. The paper provides experimental evidence (Figure 4) that the log-probability of generated stegotexts falls within the distribution of real Reddit posts, discusses security and deniability, and develops the implications for AI safety and textual authenticity.

---

## Strengths

- **Genuinely novel property (full capacity / same-length hiding):** The paper's central claim — that the stegotext can be the same length as the hidden message — is a clear differentiator from prior LLM steganography methods (Meteor, Wu et al., Zamir), which require longer stegotexts or variable-rate encoding. This property is nontrivial and elegantly achieved through rank preservation. The paper correctly positions this as its primary contribution.

- **Extremely simple and elegant protocol:** The method (extract ranks from e → follow ranks from k) is so simple it could be described in a paragraph. This conceptual clarity is a genuine strength — the work identifies an insight that is obvious in retrospect but was not previously articulated, and the exposition in Figure 3 is pedagogical.

- **Quantitative plausibility evidence with meaningful controls:** Figure 4 compares log-probabilities of 300 stegotexts (100 per secret text at μ, μ−2σ, μ+2σ) against 1000 real Reddit posts, showing all fall within the real-text distribution. The inclusion of random-ASCII and random-English-word baselines provides a useful calibration. Cross-validation with a different LLM (Phi-3 3.8B, Figure 14) is also provided.

- **Insightful analysis of the probability gap:** The "low-entropy token choices" analysis (Section 3) cogently explains *why* stegotexts are generally less probable than originals despite preserving ranks: rank-1 tokens are "wasted" on low-entropy positions where the LLM would assign very high probability, but the frequency of rank-1 from e (~40%) is much lower than the probability mass of the top token at those positions (~95%+). This is a genuine contribution to understanding the method's behavior.

- **Provocative discussion and AI-safety scenario:** The "Shibbolethian Theatre" scenario (Section 4) is a concrete, detailed illustration of how the protocol could be exploited. The philosophical discussion connecting steganography to hallucination as a failure of intentionality, while speculative, is thoughtful and engaging, giving the paper relevance beyond its technical contribution.

- **Open-source demo and practical efficiency:** The paper provides a public demo that reproduces results on commodity hardware in minutes, and verifies that modest 8B models suffice. This strengthens the claim of practical accessibility.

---

## Weaknesses

### Major

- **No human evaluation of stegotext plausibility:** The paper's core operational claim is that stegotexts are "coherent and plausible" (Abstract) and that "while for a human both the original and fake texts are plausible" (Section 3). Yet plausibility is measured only via LLM log-probability, which is acknowledged to be an imperfect proxy ("Measuring the meaningfulness of a text is a longstanding linguistic challenge, and arguably an ill-posed problem"). In steganography, the relevant adversary or auditor is frequently a human (e.g., a censor, a content moderator), and the standard for plausibility is human judgment. The paper provides no human ratings, Turing-style tests, or even qualitative reader studies. Given the gap between LLM-assigned probability and human perception — and the paper's own finding that LLMs can distinguish originals from stegotexts — this is a significant evidential gap for the central claim.

- **No quantitative comparison with prior steganographic methods:** The related work section identifies Meteor, Wu et al., and Zamir as prior LLM-based steganographic methods with different properties, but the paper provides no experimental comparison on plausibility, security, or capacity-efficiency trade-offs. The reader cannot assess whether the same-length property comes at a meaningful cost in detectability or coherence, or whether the method is more practical. Even a simplified baseline (e.g., a minimum-entropy encoding scheme adapted for equal-length comparison) would substantially strengthen the contribution.

- **Narrow experimental scope:** The main experiments use one LLM (Llama 3 8B), three source texts, one fixed length (85 tokens), and one domain (Reddit posts). While the paper provides some additional results (Phi-3 3.8B in Figure 14, appendix on model dependence), the core evidence for generality is thin. Different models (especially larger ones), longer texts, different domains (e.g., technical writing, dialogue), and systematic variation of e/k characteristics are not explored. The paper would benefit from demonstrating where the method works and, more importantly, where it systematically fails, beyond the single hash example.

- **Security analysis is largely qualitative with unresolved open questions:** The security discussion (Section 3.1) provides an exponential brute-force bound but acknowledges that LLM-guided key search is an open question and dismisses it without quantification. The "random string in k" mitigation (Figure 13) is mentioned but not systematically analyzed. The deniability claim rests on one hand-picked example (Figure 15) rather than a distribution; showing that *some* stegotexts match original probabilities does not demonstrate that the sender can *reliably* construct such decoy keys on demand. The protocol's practical security for the chatbot scenario — e.g., whether an auditor monitoring API access could detect the steganographic rank patterns — is not analyzed.

### Minor

- **The "full capacity" framing merits qualification:** The stegotext and secret text are equal in *token* length, but the protocol requires a secret key k (and potentially k') to be shared out-of-band. If k is itself a text of non-trivial length, the total communication overhead exceeds the secret message length. The paper acknowledges key overhead in passing but the "same length" framing in the title and abstract could mislead readers who interpret it as total communication cost rather than stegotext length.

- **Figure 5 lacks error bars or statistical testing:** The histograms in Figure 5 (right panels) compare probabilities of rank-1 tokens between real and fake texts, but no error bars, confidence intervals, or significance tests are reported. Given that this figure supports the key explanation for the probability gap, the lack of statistical rigor is noticeable.

- **Receiver-side reproducibility challenge acknowledged but unaddressed:** The paper notes that sender and receiver must run the chosen LLM "under identical conditions, performing the same approximations and obtaining identical logits" and that this "may be a challenge when using different GPU architectures." This is a practical barrier to deployment that is acknowledged but not addressed (e.g., through rounding strategies, deterministic implementations, or alternative matching procedures).

- **"Arbitrary meaningful text" overstatement:** The abstract claims the protocol can encode "an arbitrary meaningful text," but the paper later clarifies that e must be predictable by the LLM (low ranks) for s to be coherent; high-entropy texts like hashes produce gibberish. This is a reasonable qualification, but the abstract's phrasing invites the reader to assume broader scope.

### Trivial

- The paper has an engaging, slightly informal tone (e.g., "a difficult position to hold even for reviewer 2"), which suits its essay-like quality but may be off-putting in a technical venue.

---

## Nice-to-Haves

- A human evaluation study where participants rate plausibility and attempt to distinguish real vs. stegotexts would directly test the core claim.
- A comparison table with prior methods on equal-length steganography (or the closest achievable proxy) would help assess trade-offs.
- Systematic failure analysis: what characteristics of e, k, or the LLM cause s to be incoherent or detectable?
- Computational cost table (encoding/decoding time, memory) across LLMs and text lengths.
- Analysis of whether the stegotext rank patterns themselves could be detected by a statistical auditor.

---

## Removed Points

- **Criticism about not testing with a different LLM:** The harsh critic stated the paper "does not test whether fake texts can be distinguished from real texts by a different LLM." This is factually incorrect — the paper explicitly tests with Phi-3 3.8B (Figure 14). **[Removed: factual error]**
- **Criticism about reproducibility concerns regarding unreleased artifacts:** The paper provides a public demo (GitHub) and all data is from cited public sources. Any suggestion that artifacts may not be releaseable is speculative. **[Removed: contradicts paper evidence]**
- **Criticism about missing appendix content:** The parser stripped the appendices. The paper references Appendices A.1–A.5, which exist in the original submission. **[Removed: parser artifact]**
- **"The paper does not discuss the detection of stego at all in the chatbot scenario":** This is partially inaccurate — the paper describes the protocol steps but does not analyze whether an auditor could detect the steganographic encoding by observing rank patterns. Reformulated as a minor point about security analysis scope. **[Merged into security weakness]**
- **Formatting/style nitpicks:** References to paper structure, whitespace, and other presentation issues that are parser artifacts. **[Removed: non-author errors]**

---

## Novel Insights

The reviewers converge on the same core insight that the paper itself identifies but does not fully resolve: the protocol's elegance (same-length rank preservation) is also the source of its principal vulnerability (the probability gap driven by wasted rank-1 tokens). The "low-entropy token choices" analysis provides a mechanistic explanation for why LLMs can distinguish originals from stegotexts even when the rank sequences are identical — a finding that has implications beyond steganography for understanding how LLM probability mass is distributed across ranks. The paper's broader claim — that the mere possibility of this protocol forces a reconsideration of textual authorship and intentionality — is provocative but remains a philosophical observation rather than an empirically grounded conclusion.

---

## Suggestions

1. Add a human evaluation study (e.g., Amazon Mechanical Turk) where participants rate the naturalness/plausibility of real Reddit posts and stegotexts, and attempt to distinguish them. This is the single most impactful addition for substantiating the paper's central claim.
2. Include at least one baseline comparison — e.g., a simplified implementation of Meteor-style entropy coding adapted to equal-length output — to let readers assess the plausibility/security trade-off of the same-length property.
3. Broaden the experimental scope: test with at least one additional LLM family (e.g., Mistral, Qwen) at different scales, vary text length (e.g., 20, 85, 200 tokens), and include a systematic failure analysis across different kinds of secret text e and prompts k.
4. Provide a quantitative security evaluation: train a simple binary classifier on rank sequences to distinguish stegotexts from normal LLM output; test key recovery under a constrained search model.
5. Tone down the "arbitrary meaningful text" claim in the abstract to match the qualified scope in the method section.

---

## Score and Decision

**Bracket (Round 1):** 3.5–7.5. The paper is clearly stronger than papers scoring below 3.5 (which typically have no novel contribution or fundamentally flawed methodology) but does not reach the empirical rigor and comprehensive evaluation expected of papers scoring above 7.5.

**Narrowing (Round 2):** Compared against anchors in the 4–6.5 range:
- vs. *Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs* (5.0): The current paper has a cleaner, more novel core idea but weaker experimental breadth. Comparable quality, slightly higher on novelty.
- vs. *Plausibly Deniable Encryption with Large Language Models* (4.8): Similar in that both propose LLM-based steganographic/deniable communication with limited formal security analysis. The current paper is better motivated and more elegantly articulated.
- vs. *Detecting Language Model Attacks With Perplexity* (5.0): Both rely on perplexity-based metrics as proxies for human judgments. The current paper has more conceptual depth but similarly bounded experimental scope.
- vs. *Large Language Models Are Stronger Entropy Models for Transform Coding* (4.75): Both apply LLMs to information-theoretic tasks with simple methods. The current paper is stronger on conceptual novelty.

The paper sits above the median of the round-2 anchors due to the genuine novelty and elegance of its core idea, but is held back by insufficient empirical validation. The round-2 anchors in the 4.75–5.5 range cluster near where this paper lands, with the current paper being slightly stronger on originality and clarity but comparably limited on experimental evidence.

**Final anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | 1 | Weaker: less novel, standard watermarking |
| KBixkDNE8p (Mind Scramble) | 3.00 | 1 | Weaker: no clear contribution |
| urQi0TgXFY (Hidden in Plain Text) | 5.00 | 1,2 | Comparable: similar quality, different contribution type |
| 7suavRDxe8 (Plausibly Deniable Encryption) | 4.80 | 1,2 | Slightly weaker: similar limitations, less elegant idea |
| lNLVvdHyAw (Detecting Attacks w/ Perplexity) | 5.00 | 2 | Comparable: both rely on LLM-proxy metrics without human eval |
| ulIW7Frjpn (LLMs for Transform Coding) | 4.75 | 2 | Slightly weaker: less novel application of LLMs |
| iARAKITHTH (Binoculars) | 4.25 | 2 | Weaker: contested evaluation, less conceptual contribution |
| 6Mxhg9PtDE (Safety Alignment) | 9.50 | 1 | Stronger: rigorous evaluation, clear practical implications |
| syThiTmWWm (Cheating Benchmarks) | 7.75 | 1 | Stronger: thorough empirical demonstration |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>