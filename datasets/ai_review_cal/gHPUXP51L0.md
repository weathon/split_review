- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have thoroughly verified all claims against the paper text. Let me produce the final consolidated review.

## Summary

This paper proposes SSDM 2.0, a pipeline for rich transcription of speech with non-fluencies (dysfluencies). It introduces three main technical contributions: (1) Neural Articulatory Flow (NAF) — a semi-implicit, sparsely-activated speech representation inspired by articulatory gestures that shows strong scalability; (2) Full-stack Connectionist Subsequence Aligner (FCSA) — a six-stack alignment framework covering more dysfluency types than prior two-stack approaches; and (3) Non-fluency In-Context Learning (NICL) — using mispronunciation prompts and consistency learning with LLaMA to achieve zero-shot dysfluency transfer and joint fluent/non-fluent ASR. The authors also release Libri-Co-Dys, a 6023-hour co-dysfluency corpus. Results on Libri-Dys, VCTK-Stutter, and clinical nfvPPA data show substantial gains over SSDM and other baselines across phonetic transcription, dysfluency detection, and zero-shot transfer.

---

## Strengths

- **Neural Articulatory Flow (NAF) yields clearly superior and more scalable speech representations than existing approaches.** Table 1 shows NAF w/ AF achieves F1=95.8% and dPER=33.6% on Libri-Dys (100% data), versus SSDM's 90.8% and 39.0%. The scaling factors SF1=1.19 and SF2=-1.44 substantially exceed SSDM's 0.56 and -0.72, providing concrete evidence that the articulatory-inspired sparse representation captures dysfluency-relevant phonetic content with better data scaling.

- **FCSA extends dysfluency alignment coverage from 2 stacks to 6 stacks.** Section 5.1 defines four active stacks (LM/CTC, Copy, Skip, N-mono) and two passive stacks (Pass-I, Pass-R), explicitly handling repetition, insertion, deletion, and replacement — in contrast to SSDM's two-stack (LM+Copy) approach. This is a principled architectural expansion that directly targets known limitations in prior alignment.

- **NICL achieves strong zero-shot dysfluency transfer and outperforms Whisper on dysfluent ASR.** Table 7 shows SSDM 2.0 trained on repetition only achieves 55.4% F1 on replacement (vs SSDM's 23.2%) and 66.2% on insertion. Table 8 reports zero-shot ASR WER of 3.92% on Libri-Dys, surpassing Whisper's 4.167% — a remarkable result demonstrating that the mispronunciation/prompt approach overcomes the poor LM benefit observed in SSDM.

- **Systematic ablation (Table 3) validates each module's independent and combined contributions.** Every component substitution (NAF, FCSA, NICL) individually improves over SSDM, and the full SSDM 2.0 (F1=86.2) substantially outperforms the sum of partial gains (max individual: 83.0), demonstrating genuine synergy between the modules rather than a single dominant component.

- **Strong clinical results on pathological nfvPPA speech.** Table 5 shows SSDM 2.0 achieves 76.8% F1 and 70.3% MS on nfvPPA data versus SSDM's 69.9% and 55.0%, while all SLMs (GPT-4o, SALMONN-13B) produce near-zero scores — demonstrating practical utility for articulation-based clinical dysfluency transcription where general-purpose models fail.

- **Open-source release of Libri-Co-Dys (6023.24 hours)** with time-aware word/phoneme annotations and an average of 2.51 dysfluencies per utterance provides a substantially larger resource than Libri-Dys (3938 hours) for community research on co-dysfluency modeling.

---

## Weaknesses

### Fatal
None.

### Major

- **The FCSA loss formulation (Eq. 12 / Eq. \ref{loss-fcsa}) lacks clear mathematical justification for probabilistic validity.** The paper defines α and β scores via MLPs with sigmoid activations and hand-coded constants (α₅=1, α₆=10⁻⁵), then uses the expression `α^{i,j}β^{i,j} / y^{i,j}` to represent the total alignment probability. Standard CTC forward-backward has a clear probabilistic interpretation; here, because the scores are produced by learned MLPs (f¹, f²) and only bounded by sigmoid, it is not obvious that this expression corresponds to a proper marginal probability over alignments, nor that the loss maximizes a valid log-likelihood. This is not a fatal flaw — the system demonstrably works and post-alignment training (standard CTC, Eq. 11) provides an additional safety net — but it is a significant clarity gap that should be addressed with either a rigorous derivation or an explicit statement that the loss is a heuristic approximation rather than a proper likelihood.

### Minor

- **Results are reported as single points without variance estimates (confidence intervals, multiple seeds, or significance tests).** Given the complexity of the system (multiple loss terms, joint training, data simulation), some degree of variability is expected. The omission makes it difficult to assess whether reported improvements (e.g., +4.8 F1 on Libri-Dys) are robust or within noise range. This is common practice in large-scale speech modeling but would benefit from at least seed-averaged results on key tables.

- **The zero-shot ASR results (Table 8: WER 3.92% beating Whisper's 4.167%) are surprising and lack analysis.** This is a notable achievement — a dysfluency-focused model outperforming a general-purpose ASR model on non-fluent speech without any ASR-specific training. The paper does not offer a mechanistic explanation for why or how this happens (e.g., is it the alignment providing better segmentation? the consistency loss? the mispronunciation prompts?), leaving the reader to speculate.

- **The passive state scores for Stacks 5 and 6 (α₅=1, α₆=10⁻⁵) are fixed heuristics** with no learned component. While the intuition is described (inserted tokens don't influence future; removed tokens sever flow), the arbitrary values and the factor of 10⁵ difference between them are not justified or ablated. A sensitivity analysis would help establish that the method is not brittle to these choices.

- **The paper notes that the full SSDM 2.0 outperforms the sum of its partial gains (Table 3: SSDM 2.0 F1=86.2 vs. best individual component SSDM+NAF=83.0), suggesting synergy, but does not discuss why.** Understanding this interaction — e.g., whether NAF representations improve FCSA alignment quality, or FCSA alignment feeds better inputs to NICL — would strengthen the narrative and provide insight for future work.

### Trivial

- Line 38: "langauge model" → "language model" (typo).
- The SF1/SF2 scaling factor formula (Section 7.2, line 218) is an ad-hoc weighted combination of three data points with no statistical grounding; this should be noted as a heuristic.

---

## Nice-to-Haves

- A qualitative example showing gestural scores (NAF) with interpretable articulator activations, especially after Post-Interpretable Training, would make the "articulatory" claim more concrete.
- An ablation of the λ₁…λ₆ balancing weights (or at least reporting their values) would aid reproducibility. (The paper references an appendix for these; if the appendix was present in the original submission, this is already addressed.)
- Extending clinical evaluation to at least one additional disorder (e.g., Parkinson's speech) would strengthen the claim of general clinical utility, though the paper acknowledges data constraints as a limitation.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"The FCSA loss is mathematically unsound / fatal"** — The harsh critic characterized this as a fatal structural flaw. However, the paper cites CTC (Graves 2006) for the forward-backward initialization, and the expression `αβ/y` for total probability is standard in CTC/HMM formulations when α and β both include emission probabilities. The system works empirically, and post-alignment training (standard CTC) provides a fallback. This is a clarity gap, not a fatal mathematical error. Demoted to Major.

- **"The NICL component contributes more than half the total gain"** — Factually incorrect. SSDM→SSDM+NICL = +1.4 F1, SSDM→SSDM 2.0 = +4.8 F1. NICL contributes ~29% of the total gain, not "more than half." Removed.

- **"Uniform priors over large discrete sets likely cause posterior collapse / KL divergence overwhelms other losses"** — Speculative. The paper uses a standard VAE-style KL loss with Gumbel-Softmax reparameterization, and the experimental results confirm the model converges to strong performance. The λ₁ weight controls the KL term. Removed as speculative.

- **"Stack-4 (N-mono) is non-causal"** — The critic claims `(a₄, b₄) = (1, -k)` requires future text tokens. During training, the full target sequence is available via teacher forcing, so this is not an issue. For inference, the post-alignment training with standard CTC (monotonic) handles alignment. Removed as a misunderstanding.

- **"The paper's criticism of SSDM's LM contradicts Table 3 showing NICL helps"** — Misreading. The paper criticizes SSDM's *own* LM pipeline (which indeed shows minimal gain per the "w/o LLaMA" row), not LMs in general. The paper's NICL is presented precisely as a solution to this limitation. Removed.

- **"GPT-4/GPT-4o comparison is not informative"** — The paper includes these to show that even powerful general SLMs fail at structured dysfluency transcription, which is informative context. Removed.

- **"The w/o NICL row shows only a small degradation, suggesting other components do the work"** — The gap (55.4→49.3 on replacement, 66.2→60.7 on insertion) is 6-7 F1 points, which is substantial for zero-shot. Removed as understating the NICL contribution.

- **"Missing hyperparameter values (λ₁…λ₆)"** — The paper references the appendix (`\ref{append-language-modeling}`) for these values. The appendix is stripped by the parser. Per hard rules, criticisms about appendix-deferred content are removed.

---

## Novel Insights

Both reviewers independently identified a key phenomenon that the paper does not fully explain: the synergy in Table 3 where the full SSDM 2.0 (F1=86.2) substantially exceeds the sum of its component-wise gains (max individual=83.0). Additionally, the zero-shot ASR result (Table 8) where a dysfluency-focused model beats Whisper on non-fluent speech is a surprising finding that warrants deeper mechanistic explanation. Together, these suggest that the interaction between the articulatory representation (NAF), the flexible alignment (FCSA), and the in-context learning module (NICL) produces emergent capabilities not attributable to any single component, which could be a fruitful direction for future work on structured speech representations.

---

## Suggestions

1. **Clarify the FCSA loss derivation.** Provide either (a) a rigorous derivation showing how the neural forward-backward scores (α, β produced by MLP+sigmoid) correspond to a valid probability distribution over alignments, or (b) an explicit statement that the loss is a heuristic approximation, clarifying what properties it preserves (or doesn't) relative to standard CTC. This is the main concern to address.

2. **Add variance estimates** (confidence intervals or seed-averaged results) for at least the main results (Tables 3, 5, 6) to establish robustness of the reported improvements.

3. **Discuss the synergy in Table 3** — why does the full model outperform the sum of its parts? This would both strengthen the narrative and provide insight for the community.

4. **Analyze the zero-shot ASR result** (Table 8, WER 3.92% beating Whisper's 4.167%) — what mechanism enables this? Ablation or analysis would help.

5. **Add a sensitivity analysis or justification for the fixed passive-state scores** (α₅=1, α₆=10⁻⁵) to show the method is not brittle to these choices.

---

The paper addresses an important underexplored problem, makes multiple concrete technical contributions, provides extensive empirical validation with strong results, and releases a large-scale dataset to the community. The main methodological concern (FCSA loss justification) is significant but not fatal — it impairs clarity rather than invalidating results, and experimental evidence supports the approach. With revisions addressing the FCSA derivation clarity and adding variance estimates, this paper would be substantially strengthened.
