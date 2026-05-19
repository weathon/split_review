Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper proposes FAVICOMP, a training-free evidence compression method for RAG that uses ensemble decoding between a compression model (which summarizes retrieved evidence) and the target model (which generates context from parametric knowledge). At each decoding step, token logits from both models are interpolated (controlled by coefficient $\alpha$), producing compressed evidence that has lower perplexity under the target model while integrating parametric knowledge. Experiments across five open-domain QA datasets with three model pairs show consistent improvements over compression baselines, with a notable Hits-split analysis demonstrating that FAVICOMP excels on evidence-irrelevant queries by leveraging parametric knowledge.

## Strengths

1. **Training-free and model-agnostic design.** FAVICOMP requires no additional training or distillation, unlike supervised compressors (RECOMP-abstractive, CompAct). It can be plugged into any RAG pipeline with any compatible model pair. This is a genuine practical advantage clearly stated in §1 and §2.

2. **Convincing evidence of parametric-knowledge integration via the Hits analysis.** §4.3 (Fig. 3) splits test samples into evidence-relevant (Hits=1) and evidence-irrelevant (Hits=0) subsets. FAVICOMP outperforms both Zero-shot Summarization and CompAct on Hits=0 while maintaining comparable performance on Hits=1. This directly demonstrates that the ensemble mechanism supplies missing information from parametric knowledge — a capability the paper argues prior compression methods lack.

3. **Systematic ablation of the ensemble coefficient $\alpha$ across multiple datasets.** §4.2 (Fig. 2) varies $\alpha$ from 0.0 to 1.0 on NQ, HotpotQA, and MuSiQue, tracking both accuracy and perplexity. Performance peaks at $\alpha=0.5$, confirming that interpolation of both distributions (rather than relying on either alone) drives improvement. The analysis is thorough and the non-monotonic relationship is transparently reported and discussed.

4. **Consistent gains over multiple baselines across five datasets with three model pairs.** The paper evaluates against six categories of baselines (No Context, Gold Compression, Raw Document, Generated Context, reranking methods, compression methods) and reports improvements on all datasets, with up to 23.91% accuracy gain on the strongest-suite dataset.

## Weaknesses

### Fatal
None.

### Major

1. **The "familiarity" causal claim is partially confounded and the framing overreaches.** The paper motivates FAVICOMP by arguing that compressed evidence is often "unfamiliar" (high perplexity) to the target model, and lowering perplexity via ensemble decoding improves performance. However, this causal chain is entangled with the fact that the ensemble simultaneously controls *how much evidential content is preserved*. Fig. 2 shows that as $\alpha$ moves from 0.5 to 0.9, perplexity *continues decreasing* while accuracy *drops* — the paper attributes this to "lack of evidential knowledge," which is a different explanation entirely. This non-monotonicity means the method is better described as a trade-off between evidential content and parametric fluency, not simply "familiarization." The paper would be stronger if it framed the contribution as a practical interpolation technique for balancing two knowledge sources rather than overclaiming a novel conceptual insight about familiarity. The method itself is sound; the framing needs alignment with the data.

### Minor

2. **Missing a concatenation baseline that would isolate the per-token interpolation benefit.** The paper compares FAVICOMP to $\alpha=0$ (only compression model) and $\alpha=1$ (only target model) and outperforms both. However, a simple baseline that generates a summary from the compression model and a context from the target model separately, then concatenates them as input to the target model for final generation, would directly test whether per-token ensemble decoding adds value beyond combining both outputs. The related work (§6) claims concatenation is "suboptimal" but provides no experimental evidence. Adding this baseline would strengthen the attribution of gains to the ensemble mechanism specifically.

3. **The perplexity-reduction mechanism is partially tautological.** Because FAVICOMP selects tokens using the target model's own logits (via interpolation), lower perplexity of the compressed evidence under the target model is a design property, not an independent discovery. The interesting empirical finding is that this correlates with better downstream performance — but the correlation is confounded with how much evidential content is retained. A cleaner isolation (e.g., independently varying perplexity while holding content constant) would strengthen the causal claim, but is not required for the paper's practical contribution.

4. **No statistical significance or variance reporting.** The main results (Tab. 1, 3) report point estimates without standard deviations or significance tests. Given the claimed improvements, especially the 23.91% figure which is likely a single hard-dataset result, confidence intervals across multiple retrieval seeds or runs would help assess robustness. This is standard practice for empirical systems papers and would substantially increase confidence in the results.

5. **Model capacity asymmetry between FAVICOMP and the Zero-shot Summarization baseline is not discussed.** In the main Llama3 pair, FAVICOMP's compressor is Llama3.2-3B-Instruct while Zero-shot Summarization uses the target model (Llama3-8B-Instruct) as compressor — a 3B vs 8B asymmetry that actually *favors* the baseline. That FAVICOMP still outperforms it is a strong result, but the paper never acknowledges this asymmetry. Acknowledging it would strengthen rather than weaken the paper.

6. **The Hits metric is coarse.** It checks only whether the answer string appears anywhere in the retrieved documents, not whether the documents contain genuinely useful supporting evidence. This is a reasonable first-order proxy but limits the precision of the parametric-vs-evidential knowledge analysis.

### Trivial

7. The exact interpolation formula (whether logits are combined before or after softmax, and whether the combination is linear) is described only qualitatively in the visible text (likely formalized in §2.3, which was stripped by the parser). Including a clear equation would aid reproducibility.
8. Some of the "up to 23.91%" framing could mislead — this is clearly qualified with "up to" but contextualizing which dataset produces this peak would help.

## Nice-to-Haves

- Adding a concatenation baseline (as described in Weakness 2) would cleanly isolate the ensemble decoding benefit.
- Reporting variance or significance metrics.
- Explicitly discussing the compression-model capacity asymmetry, which would actually strengthen the paper's results.
- A direct diagnostic experiment measuring the perplexity of existing compression methods' outputs under the target model, to empirically motivate the "unfamiliarity" claim rather than relying on plausibility.

## Removed Points

- **Criticism that the method is "straightforward and has precedent in constrained/contrastive decoding".** The paper explicitly discusses the connection to Liu et al. (2024) and distinguishes its contribution (compressing retrieved evidence while integrating parametric knowledge, targeting RAG) from prior work. Having precedent does not invalidate the contribution.
- **Claim that the case study is "not probative."** Case studies are by nature illustrative examples, not experiments. The paper uses them appropriately to show token-level behavior that aligns with the quantitative analysis.
- **Claim that the paper "never actually demonstrates that existing compression methods produce high-perplexity outputs for the target model."** While a diagnostic experiment would strengthen the motivation, this is a motivation claim that is reasonable and not essential to validate the method itself.
- **Several speculations about what the appendix might or might not contain** (e.g., "main tables likely use the asymmetric pairs," "evidence is relegated to the appendix"). These are speculation about stripped content, not verifiable weaknesses.
- **Complaints about missing dataset descriptions (size, domain).** The paper lists the datasets and retrieval setup; the missing details are standard for appendix placement.
- **General formatting/style nitpicks and claims about "suboptimal figure choices."**

## Novel Insights

None beyond the paper's own contributions. A genuinely novel observation that emerges from reviewing these critiques is that the paper's strongest evidence comes not from the perplexity-familiarity framing but from the Hits-split analysis (Fig. 3), which cleanly demonstrates the benefit of parametric knowledge integration. This is arguably the paper's most convincing result, and it is somewhat independent of the perplexity-lowering mechanism — a reader could accept the Hits findings without accepting the familiarity/perplexity causal story.

## Suggestions

1. **Reframe the contribution.** Present FAVICOMP as a practical interpolation technique for balancing parametric and evidential knowledge during compression, rather than primarily as a "familiarity-aware" method. The current framing overclaims the novelty of the mechanism while under-selling the practical engineering contribution.

2. **Add a concatenation baseline** where compression-model output and target-model output are generated separately and concatenated as input to the target model. This directly tests whether per-token ensemble decoding provides additional value.

3. **Report variance.** Add standard deviations or confidence intervals to the main accuracy tables.

4. **Explicitly acknowledge the model capacity asymmetry** between FAVICOMP's smaller compressor and the Zero-shot Summarization baseline's larger compressor. This actually strengthens the results.

5. **Add a direct diagnostic:** Compute the target model's perplexity on outputs from existing compression methods (e.g., LongLLMLingua, RECOMP) and correlate with downstream accuracy. This would provide direct empirical motivation for the familiarity problem.

## Score and Decision

### Round 1 — Bracketing

**Queries:**
1. "evidence compression for retrieval augmented generation" (low, score ≤3) — retrieved avg scores 2.0–3.0 (SCMF, GEC, Simple Context Compression, MHA-RAG, Decoupled RAG)
2. "retrieval augmented generation familiarity perplexity aware compression" (mid, score 4–7) — retrieved avg scores 4.0–5.6 (REFRAG 4.0, CORE 4.5, COMI 5.0, Frustratingly Simple Retrieval 5.5, Reusing Pre-Training Data 5.6)
3. "training-free ensemble decoding evidence compression RAG" (high, score ≥8) — retrieved avg scores 8.0 but papers on substantially different topics (Transducing LMs, Mixing Mechanisms, LLMs in Multi-Turn)

**Initial bracket:** The paper clearly sits above the low band (avg 2–3) — it has a sound method, clear experiments, and a novel approach. It does not reach the high band (avg 8+) — those papers represent breakthrough or deeply analytical contributions. The plausible range is **4.5–6.5**.

### Round 2 — Narrowing

**Queries within bracket:**
1. "training-free evidence compression RAG ensemble decoding" (score 4.5–6.5) — OSCAR 6.5, SAE-based faithfulness 5.0, CORE 4.5, LinearRAG 6.0, NoLLMRAG 5.0
2. "token-level interpolation decoding two LMs summarization RAG" (score 4.5–6.5) — Topological RAG 4.5, FrugalRAG 5.0, T2RAG 4.5, Q-RAG 6.0, MoL 4.8

**Anchor comparisons:**
- **OSCAR (6.5, Accept Poster)** — Online soft compression for RAG requiring per-generator training. FAVICOMP is slightly weaker overall because OSCAR has a more thorough evaluation (including efficiency metrics, ablation on compression rates) and fewer framing issues. FAVICOMP's training-free advantage is real but OSCAR's strengths in evaluation rigor put it higher. FAVICOMP ≈ 0.5–1.0 below OSCAR.
- **COMI (5.0, Accept Poster)** — Coarse-to-fine context compression with MIG metric. FAVICOMP has a cleaner, better-motivated method and comparable experimental scope. Similar quality overall, possibly slightly stronger due to the Hits analysis. FAVICOMP ≈ comparable or slightly above COMI.
- **CORE (4.5, Reject)** — RL compression for RAG. Reviewers found limited novelty. FAVICOMP is clearly stronger — more novel approach, training-free, better framing despite the overclaim issue. FAVICOMP > 4.5.
- **FrugalRAG (5.0, Accept Poster)** — RL finetuning for adaptive retrieval. FAVICOMP is comparably solid but has different strengths. ≈ comparable.

**Final score:** 5.5. The paper sits between the 5.0 anchors (COMI, FrugalRAG) and the 6.5 anchor (OSCAR). It has a clean, practical method and compelling evidence (especially the Hits analysis), but the overclaimed familiarity framing, missing concatenation baseline, and lack of variance reporting prevent it from reaching the 6+ tier. A 5.5 reflects "solid contribution with noteworthy weaknesses that are addressable."

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>