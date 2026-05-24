Now I have a clear calibration picture. Let me write the final review.

## Summary

This paper introduces In-Context Watermarking (ICW), a family of four methods (Unicode, Initials, Lexical, Acrostics) that embed detectable watermarks into LLM-generated text solely through prompt engineering — requiring no access to model weights, logits, or decoding. The key idea is to craft a natural-language instruction (e.g., "maximize use of words from this list") that the LLM follows during generation, producing output with a statistical signature that a detector can later verify. The paper evaluates ICW in a Direct Text Stamp (DTS) setting and a novel Indirect Prompt Injection (IPI) setting motivated by detecting AI-generated peer reviews. Results with GPT-o3-mini show near-perfect detection ROC-AUC (0.995–1.000), better text quality than post-hoc baselines, and competitive robustness under paraphrasing.

## Strengths

- **Genuinely novel watermarking paradigm.** ICW is the first approach to embed watermarks entirely through prompt engineering, without modifying the decoding process. This is clearly different from all prior in-process and post-hoc methods and addresses a real gap: scenarios where the detector has no access to or control over the model.

- **Systematic multi-granularity design with explicit trade-off characterization.** The paper proposes four ICW strategies operating at different linguistic levels (character, word-initial, lexical, sentence-initial) and provides a clear trade-off table (Table 1) summarizing their relative strengths across LLM requirements, detectability, robustness, and text quality.

- **Introduction of the IPI setting as a concrete use case.** The Indirect Prompt Injection scenario (embedding watermarking instructions in manuscripts to detect AI-generated reviews) is a novel and well-motivated application that existing watermarking methods cannot address.

- **Near-perfect detection with capable LLMs.** With GPT-o3-mini, all four ICW strategies achieve ROC-AUC ≥ 0.995 in the DTS setting and ≥ 0.997 in the IPI setting (Table 2), demonstrating feasibility with state-of-the-art models.

- **Stronger robustness under paraphrasing than baselines.** Under paraphrase attacks (Figure 3), Initials (0.887), Lexical (0.924), and Acrostics (0.922) ICW all substantially outperform YCZ+23 (0.557) and PostMark (0.841).

- **Higher text quality than post-hoc baselines.** Table 3 shows ICW methods score substantially higher on LLM-as-a-Judge evaluation than PostMark and YCZ+23, and remain close to unwatermarked GPT-o3-mini text.

- **Empirical demonstration of capability scaling.** Results clearly show ICW effectiveness improves dramatically from GPT-4o-mini to GPT-o3-mini, validating that the approach becomes more viable as LLMs advance.

## Weaknesses

### Fatal
None.

### Major

1. **Missing unwatermarked LLM-text control for detection experiments (Initials and Lexical ICW).** The detection evaluation (Table 2) compares watermarked LLM text against human-written text (ELI5). For Initials ICW and Lexical ICW, the detection statistics (proportion of green-set letters/words) could in principle differ between LLM-generated and human-written text even without any watermarking instruction. If GPT-o3-mini's natural output already deviates from the human-text distribution in the direction of the green set, detection AUC could be inflated. The paper does not report the same detection statistics on *unwatermarked* LLM text vs. human text, which would isolate the watermark's contribution from inherent stylistic differences. This is the most consequential gap because the paper's central evidence is detection accuracy. (Note: this concern does not apply to Unicode ICW [detection via zero-width spaces that don't occur naturally] or Acrostics ICW [detection via Levenshtein distance to a specific secret key], which are cleanly separable from this confound.)

### Minor

2. **No confidence intervals or measures of variance.** All AUC values in Table 2 and Figure 3 are reported as point estimates with no confidence intervals, standard errors, or bootstrap estimates. With 500 samples per condition, AUC estimates carry nontrivial sampling noise, and the fact that several values are reported as exactly 1.000 without any uncertainty quantification is concerning. The paper would be strengthened by reporting, e.g., bootstrapped 95% CIs.

3. **IPI setting experiments do not validate the covert embedding mechanism.** The IPI motivation (Section 3.2, Figure 2) describes embedding instructions as "white text" in PDFs. However, the experiments simply concatenate the instruction to the paper text before feeding to the LLM — they do not test whether the instruction survives real-world PDF-to-text conversion, whether common PDF parsers preserve it, or whether a reviewer would naturally include it. The paper acknowledges this gap ("detailed investigation of attack and defense methods is left for future work"), but the gap between the claimed use case and the experimental evidence is substantial enough to warrant caution when interpreting the IPI results.

4. **Domain mismatch in detection baselines.** The z-statistic for Initials ICW (Section 4.2.2) estimates the background distribution γ from the Canterbury Corpus, but the human-text baseline in experiments is from ELI5. If ELI5 has a different distribution of word-initial letters, the z-statistic may be systematically biased. The paper should either re-estimate γ from ELI5 or report sensitivity to this choice.

### Trivial
None.

## Nice-to-Haves

- **Word-replacement attack fairness:** Lexical ICW drops under word replacement (AUC 0.758, Figure 3), and the paper attributes this to green words being nouns/verbs/adjectives/adverbs that are specifically targeted. Reporting the actual replacement rates on watermarked vs. human text would clarify whether the comparison is balanced.
- **Analysis of false positive rate under real use:** The theoretical false-alarm guarantees (Appendix B) assume the human-text distribution matches the Canterbury Corpus. A robustness check computing z-statistics on a set of human-written reviews would increase confidence in practical deployment.

## Removed Points
- The harsh critic's claim that *Acrostics* ICW is also confounded by LLM-vs-human differences: For Acrostics, detection is based on Levenshtein distance between sentence-initial letters and a specific secret key sequence — unwatermarked text would not systematically match a key, making the confound inapplicable.
- The claim that "no explanation is given" for why GPT-4o-mini follows Unicode ICW but ignores others: The paper explicitly explains this — Unicode ICW imposes minimal LLM requirements, while Initials/Acrostics require stronger instruction-following (Section 5.2.1, Table 1).
- The concern that the LLM-as-a-Judge evaluation "further supports the confound": This is speculative and conflates two distinct evaluations (text quality vs. detection). No evidence links judge preferences to detection confound.
- The request for context-length ablation on Lexical ICW: This is already present in Appendix D.1.
- Pure formatting/style nitpicks and typos (parser artifacts).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add an unwatermarked LLM-text baseline to the detection evaluation for Initials and Lexical ICW — compute the same detection statistics on text generated *without* the watermarking instruction and verify AUC is near 0.5 (or substantially lower than the watermarked case).
2. Report bootstrapped confidence intervals for all AUC values, especially the perfect 1.000 scores.
3. Run a realistic IPI simulation: embed the instruction as white text in a PDF, convert with common parsers, and measure instruction survival rate.
4. Re-estimate the background distribution γ from the ELI5 dataset (or the ICLR paper dataset for IPI) rather than relying solely on Canterbury Corpus.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1-weak | Weaker paper with less novelty and weaker results |
| vfEqSWpMfj (Word Importance) | 2.50 | R1-weak | Unrelated topic, weak paper |
| 0koPj0cJV6 (Black-Box Watermark) | 4.60 | R1-mid | Similar black-box motivation but less novel approach; current paper is stronger |
| E4LAVLXAHW (Black-Box Detection) | 7.00 | R1-mid | Different direction (detection, not proposal); stronger execution |
| eKGEsFdpin (Sampling Watermark) | 3.67 | R1-mid | Standard approach, weaker results |
| DEJIDCmWOz (Reliability of Watermarks) | 6.00 | R1-mid | Evaluation-focused paper; current paper more novel but less rigorous |
| j7b4mm7Ec9 (Deep Watermarking) | 7.60 | R1-strong | Different domain (image watermarking); less relevant |
| syThiTmWWm (Cheating Benchmarks) | 7.75 | R1-strong | Unrelated topic |
| SnDmPkOJ0T (REEF) | 8.00 | R1-strong | Unrelated (model fingerprinting) |
| 84n3UwkH7b (Diffusion Memorization) | 8.00 | R1-strong | Unrelated |

**Round 1 bracket:** Between 4.5 and 6.5

**Round 2 — Narrowing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KRMSH1GxUK (IP Infringement Detection) | 5.80 | R2 | Better evaluation and clearer contribution; current paper slightly weaker |
| r6aX67YhD9 (RL Watermark) | 4.75 | R2 | Requires model tuning, different paradigm; comparable quality |
| 6p8lpe4MNf (Semantic Invariant Watermark) | 5.50 | R2 | Logit-based method with solid evaluation; current paper more novel but weaker evaluation |
| zWqr3MQuNs (Detecting Pretraining Data) | 6.25 | R2 | Unrelated topic |
| Xlayxj2fWp (DNA-GPT) | 6.67 | R2 | Unrelated (detection-only) |
| kVrwHLAb20 (Ward) | 6.50 | R2 | Stronger paper overall: cleaner problem formalization, thorough evaluation |

**Round 3 — Confirmation:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 0KHW6yXdiZ (End-to-End Logits Watermark) | 5.25 | R3 | Less novel approach; current paper is stronger in novelty |
| 6p8lpe4MNf (Semantic Invariant Watermark) | 5.50 | R3 | Comparable; current paper more novel but weaker evaluation |
| KRMSH1GxUK (IP Infringement Detection) | 5.80 | R3 | Better executed; current paper slightly weaker |

The paper is positioned between the ~5.25 paper (end-to-end logit watermark — less novel but functional) and the ~5.80 paper (IP infringement detection — clearer evaluation). It is comparable to the 5.50 semantic invariant watermark. The core idea (prompt-only watermarking) is genuinely novel, which elevates the paper above the 5.0 level, but the evaluation gaps (missing unwatermarked control, no confidence intervals, unvalidated IPI mechanism) prevent it from reaching the 6.0+ tier. 

**Final Reasoning:** The paper tackles a well-motivated problem with a genuinely novel approach and demonstrates promising results with capable LLMs. However, the main weakness — the missing control for whether detection signal comes from the watermark or from inherent LLM-vs-human differences (for Initials and Lexical ICWs) — is a real evidential gap that needs to be addressed. The novel contribution and the IPI application compensate for this gap at the borderline level. 

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>