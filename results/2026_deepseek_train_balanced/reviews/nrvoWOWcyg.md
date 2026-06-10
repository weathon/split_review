Now I will produce the final consolidated review.

## Summary

This paper proposes Chunk-Distilled Language Modeling (CD-LM), a training-free framework that interleaves standard autoregressive LM token generation with retrieval of multi-token chunks from a trie-structured datastore. The method is formalized with a clean probabilistic model (Section 3) augmented by a tractable dynamic program for computing perplexity under chunk-based generation (Section 5). Three application modes are demonstrated: knowledge distillation (KCD-LM) using chunks from a larger teacher model, self-distillation for efficiency (SCD-LM) using chunks from the same model, and expert knowledge injection (ECD-LM) using human-curated chunks.

## Strengths

- **Tractable dynamic program for perplexity under chunk-based generation.** Section 5 derives a backward algorithm (Eqs. 5–7) that marginalizes over the latent chunk-acceptance variables, enabling intrinsic language modeling evaluation under CD-LM. This is a genuine technical contribution — speculative decoding and related chunk-generation methods lack a comparable mechanism for computing sequence probabilities.

- **Training-free knowledge distillation substantially improves a weak base model.** KCD-LM (Section 6.1) uses a 1.5B GPT-2 XL teacher to construct chunks that are injected into a 137M GPT-2 small at inference time, achieving large perplexity reductions across WikiText, Medical, and Code domains with no training. The comparison to kNN-LM (Figure 5) provides reasonable evidence that the retrieval-based distillation is effective.

- **Private information injection outperforms in-context learning for smaller models.** ECD-LM (Table 7) achieves 75.7% accuracy for GPT-2-XL on PII queries versus 0% for the base LM and 46.4% for in-context learning, while saving context space. This demonstrates a concrete practical use case where retrieval of curated chunks outperforms prompt-based knowledge injection.

- **No separate embedding model required.** The paper uses the LM's own hidden states as context vectors for retrieval (Section 4.1), avoiding the overhead of a specialized embedding module that standard RAG approaches require.

## Weaknesses

### Fatal
None.

### Major

- **Efficiency claims are unsupported because retrieval time is not measured or clearly scoped.** SCD-LM reports "token time saved" (TTS) and "forward passes saved" (FPS), but it is never clarified whether TTS includes retrieval overhead or only measures LM-side decoding time. The paper explicitly acknowledges "we do not focus on optimizing the retrieval process" (Section 7), yet the headline numbers (19.59% decrease in mean token times, 43.33% forward passes saved for GPT-2-xl-conversational) are presented without quantifying the retrieval cost. If TTS excludes retrieval time, the reported savings could be partially or fully negated by retrieval latency — especially as datastore size grows and when using larger models where retrieval-to-computation ratio differs. Without this measurement, the efficiency contribution of the method is an incomplete claim.

- **No comparison to speculative decoding baselines for SCD-LM, despite explicit positioning against them.** The paper discusses REST (He et al., 2024) in Section 2 ("The work most closely related to ours is REST, which retrieves draft token sequences from an external datastore") and frames CD-LM's ability to adapt distributions as a key differentiator. However, SCD-LM experiments (Section 6.2) compare only against the base LM. Since SCD-LM aims to improve efficiency while maintaining the same distribution — the same goal as speculative decoding — REST is a directly relevant baseline. Without this comparison, the reader cannot assess whether SCD-LM's efficiency-adaptation tradeoff is favorable relative to existing approaches that also retrieve draft sequences from a datastore.

### Minor

- **No analysis of whether PPL gains come from exact chunk matches vs. distributional improvement.** CD-LM computes PPL under its own generative distribution (Section 5). Because the datastore is built from the training set, chunks can exactly match test n-grams, inflating PPL through direct lookup. The paper does not report what fraction of test-set PPL reduction comes from exact chunk matches versus more nuanced distributional improvements. While kNN-LM shares this property and the paper compares against it, the "distillation" framing implies knowledge transfer beyond memorization, which is unsubstantiated without this analysis.

- **Discrepancy between the probabilistic PPL computation and the actual greedy decoding used.** The dynamic program in Section 5 marginalizes over $z_n \sim \text{Bernoulli}(q_n)$, but the experiments (Section 6, line 161) decode $z_n$ greedily (accept if similarity exceeds a threshold). The reported PPL values reflect the probabilistic model's distribution, not the actual generation process. The paper should clarify whether and how the PPL computation applies to the greedy variant.

- **No error bars, confidence intervals, or significance tests.** No experiment reports variance across different runs or datastore constructions. Given the fine-grained numeric precision of reported results (e.g., 19.59% TTS, 75.7% PII accuracy), the stability of these numbers is unknown.

- **The ICL baseline for PII injection (Section 6.3.2) is favorable to CD-LM.** All PII is appended to the prompt simultaneously, which is not how ICL would typically be used for this task (context limits, multi-profile confusion). A more natural baseline would include only the relevant profile information per query.

### Trivial
None.

## Nice-to-Haves

- Ablation on maximum chunk length and retrieval strategy (e.g., top-k candidates vs. best match).
- Analysis of chunk acceptance rates during generation and their relationship to efficiency/quality.
- Discussion of failure modes: when does chunk retrieval hurt generation quality?
- Scalability characterization as datastore size grows (the paper reports 1.5 hours for WikiText on one A4000, but larger corpora may face prohibitive retrieval costs).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism of "Dockerflie" dataset as unrecognizable.** This is a PDF parsing artifact (likely "Dockerfile" in the original). Per hard rules, parser artifacts should not be treated as author errors.
2. **Claim that the KCD-LM comparison to fine-tuning is "fundamentally asymmetric and uninformative."** While the comparison is asymmetric, this is by design — the paper shows that a training-free method can match training-heavy approaches, which is a meaningful contribution. The paper also includes the teacher model's PPL and kNN-LM comparisons. The specific sub-point about not isolating chunk-level from retrieval advantage is kept as Minor above.
3. **Criticism that SCD-LM quality metrics (PPL under base LM, ROUGE-L, BLEURT) measure similarity to base LM rather than generation quality.** This is by design: SCD-LM aims to maintain the base LM's distribution, so these metrics are appropriate for that purpose.
4. **Formatting/style nitpicks and speculation about appendix content.** Removed per hard rules.
5. **Claim about "memorization inflating PPL" as a fatal flaw.** The paper compares to kNN-LM which shares this property, so the comparison is fair. Retained as Minor.

## Novel Insights

A notable synthesis point that neither reviewer fully articulated: the paper's key technical contribution (the dynamic program for PPL under chunk-based generation) and its primary experimental weakness (incomplete efficiency measurement) are directly linked. The dynamic program is necessary precisely because CD-LM changes the generative distribution, making standard PPL computation inapplicable — this is a genuinely non-trivial problem that the paper solves cleanly. However, the efficiency story for SCD-LM is essentially the same as for speculative decoding (reduce LM steps by reusing past computations), but SD methods have mature engineering and provide wall-clock speedups. CD-LM's claimed advantage is distribution adaptation (KCD-LM/ECD-LM), not raw efficiency superiority. The paper would benefit from acknowledging this more explicitly: the efficiency gains in SCD-LM are a secondary benefit of the chunk retrieval infrastructure, not the primary innovation. The primary innovation is enabling distribution adaptation without training through chunk-level retrieval, and the efficiency story should be framed as a potential bonus that requires engineering optimization to realize in practice.

## Suggestions

- **Measure and report end-to-end wall-clock time** for SCD-LM, including retrieval overhead. Without this, either clarify that TTS excludes retrieval (and discuss the gap) or run controlled measurements that include it. A simple experiment: vary datastore size and measure end-to-end latency vs. the base LM.
- **Add a speculative decoding baseline** (REST or similar) to the SCD-LM efficiency comparison. This is necessary because the paper explicitly positions against speculative decoding in Section 2, and REST shares the retrieval-from-datastore mechanism.
- **Isolate the chunk-level contribution** by including an ablation where CD-LM retrieves single tokens (chunks of length 1) rather than multi-token chunks. This would disentangle the effect of chunk-level generation from the effect of having a retrieval datastore.
- **Report what fraction of accepted chunks exactly match the ground-truth test sequence** and correlate this with PPL reduction, to assess how much of the gain comes from direct memorization vs. distributional improvement.
- **Add variance reporting** (at minimum, results across multiple datastore constructions or generation seeds) to allow assessment of result stability.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>