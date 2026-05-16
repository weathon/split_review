Now I have all the evidence I need. Let me verify the key claims against the paper content.

**Verification results:**

1. **Speed-up estimation claim**: Confirmed. Lines 132-136 clearly describe profiling-based estimation for open-source models. Line 135 references actual latency comparisons in the appendix ("\cref{sec:app-actual-eff-test}"). The critic's factual claim is correct.

2. **GPT-4 judge bias claim**: The paper's limitations section (line 381) explicitly states: "Our answer quality evaluation is far from perfect due to... the potential bias of GPT-4 judges." So the critic's claim that "The paper does not acknowledge this" is *factually wrong* — the paper does acknowledge it. The critic's specific sub-claim about "self-enhancement bias" (GPT-4 judging its own outputs) is a more specific form of this general acknowledgment.

3. **Router evaluation details**: Lines 313-314 defer annotation details to appendix. Per the hard rule about parser-stripped appendices, this criticism must be removed.

4. **Small category sizes**: Confirmed — Vicuna has 80 questions across 9 categories (line 123), yielding ~9 per category on average. This is a valid concern.

5. **Discrepancy between frameworks**: Paper acknowledges it (line 194) and notes consistency on key conclusions. The critic's framing as a serious issue is somewhat overstated.

---

## Summary

This paper proposes Skeleton-of-Thought (SoT), a prompting method that reduces LLM generation latency by having the model first produce a skeleton answer outline and then expand each point in parallel via batched decoding or parallel API calls. A router extension (SoTR) adaptively triggers SoT only for suitable question types. Experiments across 12 LLMs report speed-ups up to 2.39× with maintained or improved answer quality on several question categories.

## Strengths

1. **Novel data-level approach to parallelizing LLM generation without model changes**: Unlike prior model- and system-level methods (quantization, FlashAttention, speculative decoding), SoT tackles sequential decoding by prompting the LLM itself to plan and expand its output in parallel. The paper explicitly contrasts with these lines of work (Section 2, Section 5) and demonstrates that off-the-shelf LLMs can be parallelized "without any changes to their model, system, or hardware," opening a new data-centric direction for inference efficiency.

2. **Measurable speed-ups across 12 LLMs with up to 2.39×**: The paper reports speed-ups on 9 open-source and 3 API-based models (Section 3.1). Figure 1 and Figure 2 show that 8 out of 12 models achieve >2× average speed-up, with per-model and per-category breakdowns supported by token-length statistics. The speed-up is consistent across models that follow the SoT prompts well.

3. **Answer quality maintained or improved on suitable question categories**: Using two LLM-based judges (FastChat, LLMZoo) with order-controlled evaluation, SoT achieves win/tie rates around 60% overall (Figure 4). Net win rates are positive on *generic*, *common-sense*, *knowledge*, *roleplay*, and *counterfactual* categories (Figures 5-7). The paper further shows SoT improves diversity and relevance metrics, providing evidence that parallel expansion can enhance output quality on structural questions.

4. **Router extension (SoTR) adaptively improves practical applicability**: To handle categories where SoT is unsuitable (math, coding), the paper proposes a router that selectively triggers SoT. Figure 9 shows SoTR significantly raises net win rates on problematic categories while retaining speed-ups for suitable ones. The trained RoBERTa router (120M parameters) aligns well with human annotations, making the method more deployable — this component is well-motivated and honestly evaluated.

5. **Detailed analysis of why SoT works and fails**: The paper identifies that SoT succeeds when answers can be decomposed into independent points and fails when step-by-step reasoning is required. It also traces low net win rates on some models to poor prompt adherence or already-strong baselines (Section 3.2.2-3.2.3). This diagnostic insight is valuable for guiding usage and future improvements.

6. **Opens a new research direction**: The paper frames SoT as a first attempt at using prompting for efficiency, distinguishing it from prior data-centric work focused only on quality. The discussion of future directions (Graph-of-Thoughts, self-improvement via fine-tuning, adaptive triggering) provides a clear roadmap for follow-up work.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported and no individual weakness invalidates the contribution.

### Minor

1. **Speed-up for open-source models relies on profiling-based estimation in the main text, not direct end-to-end measurements.** The paper reports speed-ups for local models using a precomputed latency profiling table that estimates latency by looking up prefilling/decoding times at various batch sizes and sequence lengths (lines 132-136). While this estimation method is reasonable and the paper references actual latency comparisons in the appendix (line 135), the main paper would be stronger with at least one representative direct latency comparison. The concern is that batching multiple expansion points with padded sequences can introduce overhead (memory allocation, attention masking) not fully captured by a precomputed table. This does not invalidate the results but reduces confidence in the exact speed-up numbers for local models.

2. **LLM-as-judge evaluation has known biases that are acknowledged but not specifically addressed.** GPT-4 serves as both a tested model and the primary judge (line 176, lines 144-145). The paper acknowledges "the potential bias of GPT-4 judges" in the limitations (line 381), but the specific self-enhancement concern — that GPT-4 may systematically prefer answers structured like its own outputs — is not separately analyzed. The evaluation framework mitigates some forms of bias (order swapping in lines 184-185), and ChatGPT is used as a secondary judge in the appendix, but the core concern remains partially unaddressed. Given that GPT-4 is only one of 12 models and the paper's quality conclusions are consistent across two different evaluation frameworks (FastChat and LLMZoo), this is a real but manageable concern.

3. **The Vicuna dataset has small per-category sample sizes.** The dataset contains 80 questions across 9 categories (line 123), yielding approximately 5-10 questions per category for categories like *math* and *coding*. Net win rates on individual categories are presented as percentages (Figures 6-7), but with such small N, a single win/loss flip can change the value by 10-20 points. No confidence intervals or statistical tests are reported. The paper's main category-level conclusions (5 "good" categories vs. 4 "poor") are coarse enough that this is unlikely to reverse them, but the precision of the reported per-category percentages is overstated.

4. **Speed-up results are reported as point estimates without variance.** All speed-ups are averages across questions (Figures 2-3). No standard deviation, min/max, or confidence intervals are provided. A model achieving 2× speed-up on easy questions but 1.2× on hard ones would still average close to 2×, masking inconsistency. This makes it difficult to assess how reliable the speed-up is across individual queries.

### Trivial

1. **Left-padding choice for batched decoding is not justified.** The paper states that "paddings are added to the left of the point-expanding requests" (line 108) but does not discuss or ablate the choice of left-padding vs. right-padding, which can affect attention mask behavior and potentially output quality.

## Nice-to-Haves

- Include a representative direct latency comparison (e.g., 2-3 local models on a handful of questions) in the main paper to validate the profiling-based estimates.
- Report confidence intervals or bootstrapped error bars on net win rates, especially for category-level analysis.
- Provide a brief analysis of why the FastChat and LLMZoo metrics disagree on absolute win rates (45.8% vs. 29.5%) — the paper notes the discrepancy but does not diagnose it.
- Add variance statistics (e.g., standard deviation or interquartile range) for speed-up results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Router evaluation lacks details on training and annotation reliability"** — REMOVED per hard rule: the paper explicitly defers annotation details, inter-annotator agreement, and training details to the appendix (\cref{app:annotation_process_router,app:training_details_roberta}). The parser strips appendices; these details exist in the original submission. Criticizing their absence in the main paper is a "missing appendix" concern.
- **"The paper does not acknowledge [GPT-4 judge bias]"** — REMOVED as factually incorrect. The paper's limitations section (line 381) states: "Our answer quality evaluation is far from perfect due to... the potential bias of GPT-4 judges." The paper does acknowledge this. (The more specific claim about GPT-4 judging its own outputs is retained in Minor above.)
- **"Profiling table or curve should be shown"** — This is a presentation preference. The paper describes the profiling methodology (lines 132-136) and the speed-up results are the key output. Showing the raw profiling curves would add depth but is not necessary for the paper's claims.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper's central claim (SoT accelerates generation while maintaining quality) rests on two different types of evidence — profiling-based estimates for local models and wall-clock measurements for API models — and the quality evaluation relies on an LLM judge that is also a tested model. This creates an asymmetry in evidential standards across the results' two dimensions (speed and quality). The paper's router extension partially compensates by showing that the method can be deployed selectively, which is pragmatically more important than perfect speed-up or quality numbers on every input. A genuine insight is that the paper's honesty about limitations (Section 6) is itself a strength: the paper admits SoT is unsuitable for reasoning tasks, that speed-up is less predictable than system-level methods, and that quality evaluation is imperfect. This transparency strengthens credibility more than sweeping claims would.

## Suggestions

1. For a camera-ready version, move one representative direct-latency comparison (e.g., 2 local models on 10 questions each) from the appendix into the main paper to ground the profiling-based speed-up estimates.
2. Add bootstrapped confidence intervals to the per-category net win rate plots (Figures 6-7) and explicitly note the small-N caveat.
3. Acknowledge the self-evaluation concern specifically for GPT-4 outputs alongside the general bias acknowledgment already present.
4. Report speed-up variance (e.g., standard deviation or box plots) alongside the averages in Figures 2-3.

## Score and Decision

The paper introduces a simple, intuitive, and model-agnostic method for reducing LLM generation latency. The idea is clever, the writing is clear, the evaluation spans 12 models and two datasets, and the limitations are discussed candidly. The weaknesses identified (profiling-based speed-up estimates in the main text, LLM judge bias, small category samples, missing variance) are real but addressable and do not undermine the paper's core contribution. The method is likely to be discussed, built upon, and adopted.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>