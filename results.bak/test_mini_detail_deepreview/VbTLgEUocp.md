Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper presents *Calgacus*, a simple protocol that uses an LLM to hide a text message (the secret) inside another text (the stegotext) of exactly the same token length. The method works by computing the rank of each token of the secret in the LLM's probability distribution, then generating the stegotext by selecting tokens at those same ranks starting from a secret prompt key. The key unique selling point is *full capacity* — the stegotext and the secret have identical length, a property the paper identifies as novel among LLM-based steganography methods. The paper also includes a long philosophical discussion about hallucinations, intentionality, and LLM knowledge.

## Strengths

1. **Genuinely novel protocol with a clean, elegant design.** The full-capacity property (secret and stegotext same length) is a concrete and well-defined contribution that differentiates Calgacus from prior LLM steganographic methods. The protocol itself is trivially implementable: tokenize secret → record ranks → generate at same ranks from a different prompt. Figure 3 and the "recipe" description make the method immediately accessible. The paper states this clearly in Section 2: *"What we add to the field is Calgacus, a protocol with the notable property of having full capacity, that is, the stegotext and the secret message being of the same length."*

2. **Initial quantitative evidence that stegotexts fall within the distribution of real texts.** Figure 4 shows that for three source texts (drawn from μ, μ−2σ, and μ+2σ of a 1000-text Reddit distribution), the cumulative log-probabilities of 100 generated stegotexts per source all lie within the distribution of real Reddit texts — whereas random ASCII and random English-word strings fall far outside. This provides basic evidence that stegotexts are plausible under the LLM's own metric.

3. **Code released and method is efficiently reproducible.** The paper provides a public demo repository (github.com/noranta4/calgacus) that can reproduce the main results "within minutes, even from smartphone." The method runs on commodity hardware with an 8B open-source model, lowering the barrier to independent verification.

4. **Insightful "low entropy token choices" analysis.** The paper identifies and explains why stegotexts are less probable than their originals even though token ranks are preserved: rank-1 tokens from the secret are "wasted" in high-entropy positions in the stegotext, where the LLM would have assigned much higher probabilities than the ~40% frequency of rank-1 tokens. Figure 5 provides supporting data. This is the most rigorous part of the paper's quantitative reasoning and correctly pinpoints the source of the detectability gap.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient experimental scope for the claims made.** The main evaluation (Figure 4) tests only **three source texts** (selected at μ, μ−2σ, μ+2σ of a single Reddit distribution) and generates **100 stegotexts per source** — 300 total — using a **single LLM (Llama 3 8B)**. All texts are truncated to the **same length (85 tokens)** and come from a **single domain (Reddit)**. The paper does not characterize: (a) the fraction of source texts that yield coherent stegotexts across diverse lengths, domains (formal prose, technical writing, poetry, conversational), or LLMs at encoding time; (b) how success varies with key quality; or (c) failure rates systematically. The paper itself acknowledges that hashes fail and that quality depends on e, k, and the LLM (Section 3, Limitations), but provides no systematic characterization. For a paper claiming a general protocol, the empirical foundation is too narrow.

2. **No comparison to any existing steganographic baseline.** The paper correctly cites prior LLM-based steganography methods (Ziegler et al., 2019; Kaptchuk et al., 2021; Wu et al., 2024; Zamir, 2024) but never compares Calgacus to any of them on any metric: information density, stegotext quality, detectability, computational cost, or robustness. The paper's claimed advantage is full capacity, but without comparison it is impossible to judge whether this comes at the cost of other important properties. The paper states *"The main interest of this paper is to discuss the implications of this last fact and describe the method"* — but staking this claim without baselines weakens the technical contribution.

3. **Security analysis is informal and experimentally untested.** Section 3.1 explicitly avoids a formal security model (*"we will avoid building a palace on the sand"*), and no empirical attack evaluation is conducted. There is no effort to measure distinguishability of stegotexts from non-steganographic texts under a motivated adversary (e.g., classifier trained to detect rank-based anomalies). The deniability argument rests on a few examples (Figure 15, referenced but in the removed appendix) with no quantitative analysis of how often favorable steganographic prompts occur or how plausible alternate secrets are. For a paper introducing a steganographic protocol whose motivation includes unsettling implications for trust in text, the absence of any realistic security evaluation substantially undermines those implications.

### Minor

1. **The discussion section, while engaging, is largely disconnected from the experimental results.** Section 4 covers "shipping unfiltered LLMs," the probabilistic nature of LLM knowledge, hallucinations as lack of intention, and Oulipo constraints. These are thought-provoking philosophical reflections, but none are tested or grounded in the paper's experiments. The "shipping unfiltered LLMs" scenario is described as a play but never implemented or evaluated. This material is more characteristic of a position paper or essay than a technical contribution, and the paper would be stronger if the technical claims (method + evaluation) were the focus.

2. **No characterization of encoding success rate or failure conditions.** What fraction of randomly selected source texts e produce fluent s? How does this depend on key specificity? The paper gives one example of failure (a hash) but provides no systematic data. The paper defers analysis to Appendices A.1, A.2, and A.5, which are not present in the available manuscript.

3. **The soundness metric (log-probability) conflates multiple factors** (style, topic, grammar, redundancy) as the paper itself acknowledges. Showing that stegotexts fall within the distribution of real texts is evidence of basic plausibility, but not of *indistinguishability*. The paper later states that "LLMs can uncover a distinction" (i.e., stegotexts are less probable on average), but provides no ROC-style analysis, detection experiment, or human study to characterize how detectable the stegotexts are in practice. The result that stegotexts are within the real distribution but systematically shifted toward lower probability is an interesting finding that the paper does not fully exploit.

### Trivial
None.

## Nice-to-Haves
- A human evaluation (even small-scale) asking participants to discriminate real text from stegotext would strengthen the plausibility claim.
- Testing across more LLMs (e.g., a larger model like Llama 3 70B, or a model from a different family like Qwen or Mistral) would improve generalizability.
- A systematic characterization of which source texts succeed/fail and how key specificity affects quality.

## Removed Points
(Points from the input reviews that were filtered out under the hard/soft rules, retained here for completeness but not included in the assessment above.)

- **Critique about "no ablation of the key"** — the paper references Appendices A.1 and A.5 (removed by parser) for this analysis; I cannot verify whether this exists in the original submission.
- **Critique that the paper "does not justify why full capacity matters"** — the paper does provide justification: same-length symmetry prevents establishing at first sight which text is authentic (Section 1).
- **Critique that the paper should compare to "rejection sampling or Ziegler et al."** — valid but already captured under Major weakness #2 (no baseline comparison).
- **Strength about "demonstration of deniability with quantitative backing"** — the paper's deniability evidence is limited to 1–2 examples; this strength is overstated relative to what's actually demonstrated.
- **Critique about "discussion section could be made without Calgacus"** — while true, this is a soft criticism of scope rather than a specific flaw.
- **Strength about "concrete AI safety scenario"** — the scenario is well-described but never tested, so it remains a speculative application rather than a demonstrated contribution.
- **Critique about "identical GPU architectures required"** — the paper explicitly acknowledges this as a limitation and cites Shanmugavelu et al. (2024). This is a real practical constraint but is honestly disclosed.

## Novel Insights
None beyond the paper's own contributions. The key insight is the protocol itself (rank-based encoding producing same-length stegotexts) and the "low entropy token choices" analysis explaining why stegotexts are statistically distinguishable from real texts despite preserving ranks. These are well articulated by the authors.

## Suggestions

1. **Broaden the evaluation substantially.** Test across multiple lengths (e.g., 50, 100, 200 tokens), multiple domains (news, fiction, technical writing, poetry), and at least 2–3 different LLMs at encoding time. Report the fraction of source texts yielding fluent stegotexts under a defined threshold.
2. **Add at least one baseline comparison.** Compare perplexity and encoding rate against a simple rejection-sampling steganography baseline or one of the cited methods (e.g., Ziegler et al., 2019; Kaptchuk et al., 2021).
3. **Add a detection experiment.** Train a binary classifier or use perplexity-based detection to distinguish stegotexts from real texts, reporting AUC and false-positive rates.
4. **Consider focusing the paper.** The philosophical discussion in Section 4 is interesting but dilutes the technical contribution. The paper would be stronger as a concise technical paper (method + evaluation) or as a position paper with the philosophical content centered. The current hybrid weakens both aspects.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor path | Avg score | Round | Comparison to this paper |
|---|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jbfDg4DgAk.md` (Sparse Watermarking) | 3.00 | R1 (weak) | Less novel; the method is a marginal variation of existing watermarking. Calgacus has a cleaner, more original idea. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BeOEmnmyFu.md` (Playing Language Game) | 2.50 | R1 (weak) | Fundamentally different topic; scored low due to limited scope and unclear contribution. Not directly comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KBixkDNE8p.md` (Mind Scramble) | 3.00 | R1 (weak) | Stretches an analogy too far with limited empirical support. Calgacus is more technically grounded. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TgTxJALwDz.md` (Large-Text Transmission) | 2.33 | R1 (weak) | Mismatched application domain; low scores reflect unclear contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7suavRDxe8.md` (Plausibly Deniable Encryption) | 4.80 | R1 (mid), R2 | Very comparable — both papers introduce a novel LLM-based protocol with an interesting cryptographic/steganographic property but insufficient empirical validation and informal security analysis. Calgacus has slightly stronger novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/urQi0TgXFY.md` (Hidden in Plain Text) | 5.00 | R1 (mid), R2 | More thorough experiments (two methods, multiple settings) but novelty questioned by some reviewers. Calgacus has weaker experiments but stronger novelty. Overall comparable quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hTUrBJqECJ.md` (Low-entropy Watermark) | 5.50 | R2 | More rigorous technically (theoretical proofs, type-II error guarantees, multiple baselines) but on a more incremental watermarking problem. Calgacus is more novel but less rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6p8lpe4MNf.md` (Semantic Invariant Watermark) | 5.50 | R1 (mid), R2 | Solid evaluation with baselines and comprehensive experiments. Calgacus's evaluation is substantially thinner. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jlhBFm7T2J.md` (Undetectable Watermark for Images) | 6.50 | R2 | Thorough theoretical and empirical analysis with multiple baselines and attack evaluation. Calgacus falls well short of this standard. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/r42tSSCHPh.md` (Catastrophic Jailbreak) | 7.00 | R2 | Clean experiments with clear results across multiple models. Calgacus's evaluation is much narrower. |

**Round 1 bracket:** 4.0 – 6.0 (clearly above the 2–3 range papers in novelty/presentation, clearly below the 6.5+ range papers in empirical rigor).

**Round 2 narrowing:** The paper is most comparable to Plausibly Deniable Encryption (4.8) and Hidden in Plain Text (5.0), both of which have novel ideas but insufficient evaluation for a top venue. Calgacus sits in the same band. It is less rigorous than the 5.5 anchors (which have baselines, theoretical analysis, or more thorough experiments) and substantially less rigorous than the 6.0+ anchors.

**Final score: 5.0.** The paper presents a genuinely novel and elegantly simple protocol, is well-written, and makes a clear contribution in the form of the full-capacity property. However, the evaluation is too narrow (300 stegotexts from one domain, one length, one LLM), there is no comparison to any baseline method, and the security analysis is entirely informal. For a top venue like ICLR, stronger empirical validation is necessary. The paper would be well-suited to a workshop or as a short paper, or could be significantly strengthened with broader experiments, baseline comparisons, and a detection study.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>