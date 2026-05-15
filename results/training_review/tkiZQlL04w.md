Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper introduces RazorAttention, a training-free KV cache compression algorithm that leverages the observation that only a small subset of attention heads ("retrieval heads") attend globally, while most heads focus locally. The method identifies retrieval heads via echo/induction scores on random tokens, keeps their full KV cache, aggressively compresses non-retrieval heads by keeping only recent + sink tokens plus a mean-pooled "compensation token," and achieves ~3× compression. Evaluated on Qwen1.5, Llama3, Llama2, and Baichuan2 across LongBench and Needle in a Haystack, RA performs close to the full-KV baseline and outperforms H2O and StreamingLLM.

## Strengths

- **Novel head-wise compression principle grounded in interpretability.** The paper identifies that ≈15% of heads (retrieval heads) account for nearly all long-range information access, while the remaining heads attend locally. Table 1 (tab:protect) directly supports this: protecting retrieval heads retains 45.48% on MultiFieldQA-en vs. 40.7% for random heads and 40.81% for no protection, which is a clean demonstration that the head distinction is real and meaningful.

- **Consistent near-baseline performance across diverse LLMs and tasks.** On LongBench (Table 2), RA achieves average scores within 0.2–0.6 points of the uncompressed baseline across four model families (Qwen1.5-7B/72B, Llama3-8B, Baichuan2-13B) while compressing the KV cache by ~70%. It consistently outperforms H2O and StreamingLLM by wide margins, often matching or exceeding H2O by 1–2 points on average.

- **Robustness to very long contexts (80K tokens).** The Needle in a Haystack evaluation on Llama2-7B-80K (Figure 3) shows RA maintains high recall across all positions and document depths, while H2O runs out of memory and StreamingLLM fails entirely. This is strong evidence that the method preserves retrieval capability under extreme compression at scale.

- **Compensation token is shown to be effective.** Figure 5 (the ablation on Llama2-7B-80K) clearly demonstrates that removing the compensation token degrades Needle performance substantially, and including it brings results close to the uncompressed baseline. This provides empirical justification for a simple but impactful design choice.

- **Ablation studies justify the 14%+1% head selection.** Table 3 shows monotonic improvement in accuracy as induction heads increase from 5% (69.54%) to 14% (86.59%), approaching the baseline of 87.05%. Figure 4 shows that adding 1% echo heads dramatically improves retrieval performance. These ablations confirm the hyperparameter choices are empirically motivated.

## Weaknesses

### Fatal

None.

### Major

1. **Missing multi-query / multi-turn evaluation despite this being the paper's central motivation.** The entire motivation (Figure 1 and lines 27–31) hinges on the scenario where importance-based methods fail because different queries access different parts of the context — "a user might request information not aligned with the main theme, or engage in a multi-round conversation." The paper explicitly excludes SnapKV on this basis (line 252) but then never evaluates RA in this setting. All experiments are single-query benchmarks (LongBench, Needle in a Haystack). This disconnect between the claimed advantage and the actual evaluation is significant: the paper argues RA is superior precisely *because* it handles multi-query scenarios, but provides no evidence for this.

2. **Baseline compression ratios are not reported or controlled.** The paper specifies RA's configuration (Table 2: buffer length = max(4000, N/5), 14% induction heads + 1% echo heads + 4 sink tokens), which yields ~3.125× compression. However, it does **not** report the KV cache sizes used by H2O (heavy-hitter ratio) or StreamingLLM (window size). Without matched compression ratios, the performance comparisons in Table 2 are partially uninterpretable — RA might simply be using more cache. This is a basic fairness requirement for compression papers.

3. **No end-to-end speed or memory benchmarks despite repeated efficiency claims.** The paper claims FlashAttention compatibility and that RA "could achieve a substantial inference speedup" (line 40), "introduces negligible overhead" (line 46), and "accelerates the inference of LLMs" (line 310). Yet no latency, throughput, or peak memory measurements are reported. The only efficiency evidence is that H2O hits OOM at 80K while RA does not (Figure 3) — useful but insufficient. Efficiency claims need to be benchmarked, especially when the method requires managing different cache policies per head and computing compensation tokens.

### Minor

1. **Retrieval head identification method could be more rigorously validated.** The identification uses echo/induction scores on random token sequences (2500 tokens × 4 repeats). While Table 1 does provide transfer evidence (the heads identified on random tokens improve real-task performance), the paper does not examine: (a) stability of the identified head set across different random seeds or sequence lengths, (b) correlation between echo/induction scores and actual attention distributions on real text, or (c) whether the 14%+1% thresholds generalize across models or tasks. This is not fatal — the method demonstrably works — but the validation is thinner than ideal for a method whose core premise depends on correct head identification.

2. **"Nearly lossless" claim is slightly overstated for individual tasks.** On average across LongBench, RA is within 0.2–0.6 points of full KV, which is impressive. However, individual task degradations can be larger (e.g., Qwen1.5-7B on GovReport: 28.78 → 26.68, a ≈7% relative drop). The paper also does not report confidence intervals or statistical significance, which would help quantify variability. The claim is reasonable as an average characterization but could be better scoped.

3. **Identification procedure lacks full specificity for reproduction.** The paper states it generates "K=2500 random tokens" and "repeats them 4 times" but does not specify: the source vocabulary (uniform over the model's full vocabulary?), the tokenizer used, or the exact computation of echo and induction scores (attention weight averaged over which positions, with causal masking accounted for?). Pseudo-code or explicit algorithmic details would improve reproducibility.

4. **Ablation studies are limited to Needle in a Haystack rather than LongBench.** The ablations on induction head count (Table 3), echo heads (Figure 4), and compensation token (Figure 5) are conducted solely on Needle in a Haystack, a single retrieval task. It would be more informative to show ablations on LongBench tasks (e.g., summarization, QA) to confirm the findings generalize across task types.

### Trivial

None.

## Nice-to-Haves

- A multi-query or multi-turn benchmark (e.g., long-document QA with several diverse questions, or a conversational setting where each turn queries different information) would directly test the paper's claimed advantage over importance-based methods.
- Speed benchmarks (tokens/sec, peak GPU memory at various context lengths) with and without FlashAttention integration would substantiate the efficiency claims.
- Sensitivity analysis showing how performance varies with different proportions of induction/echo heads (beyond the discrete values tested in Table 3) and whether optimal proportions shift by model size or architecture.
- Visualization of attention distributions in non-retrieval heads before and after compression to illustrate what information the compensation token captures.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The identification of retrieval heads is not validated and the method's central assumption is unproven"** — The critic claimed the identification has "no demonstrated connection" to real inputs and that the validation is "circular." This is factually incorrect: Table 1 (tab:protect) tests the identified heads on MultiFieldQA-en, a real QA dataset, and shows they clearly outperform random heads (45.48% vs. 40.7%). The connection to real data is demonstrated. The "circular" claim misunderstands the experimental design. The reasonable core (more validation would help) is kept as Minor Weakness #1 above.

- **"The paper excludes SnapKV... but does not include other recent methods like PyramidKV, PyramidInfer, CORM, or SubGen"** — The paper mentions these methods in Related Work (line 59) but does not compare experimentally. Per instructions, I should not penalize missing baselines absent confirmation they are suitable for comparison, especially since the later methods are not in the same setting (some also assume known queries or use different compression strategies). The SnapKV exclusion is explicitly justified. Removed.

- **"Theorem 1 uses constants that in practice are not known or computed"** — The paper presents Theorem 1 as a *theoretical illustration* of ALiBi's structure, not as a practical computation method. The section explicitly states ALiBi models "dynamically adjust the KV cache size" based on this principle. The critic's demand for empirical validation of the theorem's constants misses the illustrative purpose. Removed.

- **"Table 3 only shows a single dataset (MultiFieldQA-en) with a single compression configuration"** — This is accurate but is already covered in Minor Weakness #4 (ablations limited to Needle). The same concern applies. Not double-counted.

- **"The paper does not report statistical significance or confidence intervals"** — This is standard practice for large-scale LLM benchmarks where single-run evaluation is the norm. Moved to Nice-to-Haves as a suggestion for rigor rather than a weakness.

- **Various pure formatting/style observations** from the critic's section-by-section notes that are either addressed by paper content or are subjective presentation preferences. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one useful observation: the method's motivating scenario (multi-query / multi-turn) is compelling but entirely untested, creating an asymmetry where the paper argues its advantage over methods like SnapKV on theoretical grounds without providing any experimental evidence for that advantage. This is a missed opportunity — a simple multi-query QA benchmark could substantially strengthen the paper's claims. Additionally, the disconnect between the paper's repeated efficiency claims and the absence of any speed measurement is striking for a method whose practical value depends on it being truly efficient.

## Suggestions

1. **Add a multi-query experiment.** Construct a benchmark where a long document is queried with several diverse questions targeting different parts of the text (as depicted in Figure 1). Compare RA against H2O, StreamingLLM, and ideally SnapKV (which is excluded only for this setting — here it would be a valid baseline). This directly tests the paper's core claim and would significantly strengthen it.

2. **Report baseline configurations and match compression ratios.** State the exact KV cache size (or reduction ratio) used for H2O and StreamingLLM in each experiment. Ideally, show accuracy-vs-compression-ratio curves for all methods at multiple operating points, not just a single configuration.

3. **Benchmark inference speed and memory.** Report tokens/sec and peak GPU memory for RA vs. baselines at several context lengths (8K, 16K, 32K), both with and without FlashAttention. This substantiates the repeated efficiency claims and is standard for systems papers.

4. **Validate retrieval head identification more thoroughly.** Show (a) the Jaccard similarity of identified head sets across random seeds, (b) correlation between echo/induction scores and actual attention weights on a long-document corpus, and (c) whether the 14%+1% split is stable across models of different sizes and families.

5. **Provide pseudo-code for identification.** Specify how echo and induction scores are computed (e.g., which positions are averaged, how causal masking is handled, vocabulary source for random tokens) to ensure reproducibility.

## Score and Decision

This paper proposes a genuinely novel and well-motivated idea — head-wise KV cache compression based on the discovery that most heads attend locally and only a few "retrieval heads" handle global context. The core empirical findings (Table 1 showing the head distinction, Table 2 showing near-baseline performance across 4 model families) are valuable and reasonably supported. The compensation token and the ablations are sensible.

However, the paper has three significant evaluation gaps: (1) the motivating multi-query scenario is never tested, (2) baseline compression ratios are not reported or controlled, and (3) efficiency claims are made without any speed benchmarks. These do not invalidate the core contribution but they substantially weaken the paper's empirical standing. The paper would be significantly stronger if these gaps were addressed.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>