I now have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper identifies a significant problem in current multimodal in-context learning (ICL) evaluation: popular VQA and captioning benchmarks produce near-flat shot curves that primarily measure answer-format adaptation rather than genuine task learning. To address this, the authors introduce VL-ICL Bench, a suite of ten tasks spanning image-to-text and text-to-image generation across perception, reasoning, rule induction, fast binding, interleaving, and long-context challenges. They evaluate 16 image-to-text and 5 text-to-image models, revealing that even GPT-4V and LLaVA-OneVision-72B struggle on many tasks, and that ICL performance often degrades with more shots—demonstrating that the benchmark genuinely tests ICL limitations beyond those visible on standard VQA/captioning.

## Strengths

1. **Clean empirical demonstration of the VQA/captioning ICL problem (Section 2.2, Figures 1–2):** The paper shows that on MathVista, VizWiz, and COCO Captioning, six VLLMs exhibit near-flat ICL curves. Critically, switching from exact-match evaluation to LLM-based ("soft") evaluation flattens the curves almost entirely, while corresponding text-only LLM ICL benchmarks (AGNews, MIT Movies, TREC) show substantial shot scaling. This provides direct evidence that prior multimodal ICL practice primarily measures answer-format learning.

2. **Comprehensive and well-designed task coverage (Table 1, Section 3):** The ten tasks span both image-to-text and text-to-image, and explicitly test fast binding, fine-grained perception, rule induction, arithmetic reasoning, interleaved-image reasoning, and long-context handling—capabilities that no prior multimodal ICL benchmark covers in one suite. The benchmark is compact (1.82 GB total) and usable without prohibitive resources.

3. **Extensive multi-model evaluation revealing nontrivial negative results (Tables 2–3, Figure 3):** Sixteen I2T and five T2I models are evaluated, including GPT-4V. The results show that many strong zero-shot VLLMs (e.g., LLaVA-Next-7B) exhibit *negative* ICL efficiency on multiple tasks, and performance often degrades with more shots—a meaningful finding about current VLLM context-length and interleaved-image limitations that goes beyond what VQA/captioning benchmarks could reveal.

4. **Context-length vs. ICL ability disentanglement (Table 4):** Controlled SelfExtend experiments on LLaVA-Next-7B and VILA-7B show that extending context from 4K to 16K helps on some tasks (e.g., Fast Open MiniImageNet) but does not improve or even harms performance on others (e.g., Operator Induction). This provides evidence that VL-ICL failure is not simply a context-length problem.

5. **Clean text-vs-image comparison (Figure 4):** Comparing image-input and text-input versions of CLEVR Count Induction, Operator Induction, and Interleaved Operator Induction isolates the additional difficulty introduced by visual perception and image-token inefficiency, showing that text-only versions produce much sharper shot scaling.

## Weaknesses

### Fatal

None.

### Major

None. No identified weakness invalidates the paper's core claims or contribution.

### Minor

1. **Motivational evidence relies on a single inferential step.** Section 2.2 attributes the flattening of ICL curves under LLM evaluation to "answer style/format learning." This is a plausible interpretation, but an alternative explanation—that the LLM judge is simply noisier or more lenient, washing out real but small improvements—is not ruled out by a controlled experiment (e.g., directly comparing zero-shot vs. few-shot model outputs to show that only formatting changes). The benchmark's contribution is valuable regardless, but the motivation section would be stronger with direct output-content analysis rather than relying solely on the LLM-judge-as-black-box approach.

2. **The "ICL efficiency" metric is non-standard and insufficiently characterized.** Defined as "the area under the accuracy vs shots curve above the zero-shot starting point, normalized over the whole area" (line 162), this metric is used heavily to rank models (Tables 1–2). However, its interpretation is not obvious: a model scoring high efficiency could achieve this through a large early jump from near-zero zero-shot, or through sustained gradual improvement. The paper does not discuss sensitivity to the range of shots evaluated, ceiling effects, or whether the metric correlates with intuitive notions of ICL capability. The simultaneous reporting of zero-shot and peak accuracy mitigates this, but the efficiency metric itself needs clarification and validation.

3. **Variance across random seeds is not reported.** The paper averages results over three random seeds (line 160) but reports only point estimates without standard deviations or confidence intervals. For a benchmark intended to enable reliable model comparison, providing variance information would substantially strengthen the reported results.

4. **The "emergent threshold" claim is thin.** Section 4.3 discusses an "emergent threshold" based on comparing LLaVA-OneVision at three sizes (0.5B, 7B, 72B). The 0.5B model is too small to even understand the task format; the 7B model degrades with shots; the 72B model improves. This is an interesting scaling observation, but three sizes (especially with such large gaps) are insufficient to demonstrate a sharp "emergent" transition in the sense used in the LLM literature (Wei et al., 2022). Framing this as "scaling trends" or "model size effects" would be more appropriate.

5. **No data availability statement is included.** The paper introduces a benchmark as its main contribution but does not explicitly state that the dataset will be released or how it can be accessed. For a benchmark paper, this is an essential element that should be added.

6. **Limited discussion of synthetic-to-real generalization.** The benchmark relies heavily on synthetic tasks (MiniImageNet variants, CLEVR, generated operator images). While synthetic tasks are common and appropriate in ICL research for isolating capabilities, the paper does not discuss caveats about extrapolating findings to real-world ICL scenarios. This would be a useful addition for practitioners.

### Trivial

None.

## Nice-to-Haves

- Provide a direct content-analysis experiment: compare model outputs in zero-shot vs. few-shot settings on VQA/captioning to show that the changes are primarily in verbosity, formatting, and phrasing rather than semantic correctness. This would tighten the motivational evidence.
- Supplement ICL efficiency with a simpler, more interpretable metric such as average improvement per shot over the first few shots.
- Include at least one VQA benchmark that might show genuine ICL improvement (e.g., OK-VQA, where external knowledge could be provided in the support set) to make the critique more nuanced.

## Removed Points

These points from the input reviews were removed after cross-checking against the paper. Treat with caution:

1. **"Zero-shot evaluation for fast-binding tasks is uninformative" (Harsh Critic #3):** The paper explicitly states "making the chance rate effectively zero" (line 128) and uses the zero-shot baseline intentionally to isolate ICL gains. The paper already addresses this concern. *Reason: The paper already addresses this; it is not a weakness.*

2. **"Overstated novelty as 'first thorough and integrated benchmark suite'" (Harsh Critic #2):** The paper acknowledges CoBSAT and ManyShot as concurrent work (lines 326–327) and clearly distinguishes its scope as broader (10 tasks, both I2T and T2I, diverse capabilities). The "first thorough and integrated" claim is defensible since no prior work covers this range. *Reason: The paper's framing is factually accurate given its scope and acknowledgment of concurrent work.*

3. **"SelfExtend sentence appears truncated — parser artifact":** This is a formatting artifact from PDF extraction, not an author error. *Reason: Parser artifact per the hard rules.*

4. **"The paper does not discuss whether performance decrease might also be due to task difficulty or support-set sampling noise":** The paper attributes performance decrease to "difficulty of dealing with a larger number of images and tokens" and "exacerbated by the difficulty of extrapolation over context length" (lines 184–185), providing a clear, grounded explanation. *Reason: Already addressed in the paper.*

5. **"Missing related works":** Not permitted per the hard rules, as confirming missing related works requires external knowledge. *Reason: Hard rule — do not mention missing related works.*

## Novel Insights

A genuinely novel insight emerges from combining the paper's two-stage critique: (a) VQA/captioning ICL is shallow format learning, and (b) the proposed benchmark reveals that even state-of-the-art VLLMs show *negative* ICL efficiency on many tasks (performance degrades with more examples). Together, these suggest that multimodal ICL faces a fundamentally different challenge than language-only ICL: the overhead of processing many image tokens per example may actively interfere with the model's ability to exploit the information in additional shots. This "anti-scaling" phenomenon—where more examples hurt rather than help—is rarely observed in LLM ICL and points to a structural limitation in current VLLM architectures that goes beyond simple context-length constraints. The SelfExtend experiments further confirm that addressing context length alone does not solve this.

## Suggestions

1. Add a direct output-comparison experiment (e.g., showing zero-shot vs. few-shot captions differ primarily in verbosity, not content) to strengthen the motivational claim in Section 2.2.
2. Provide variance (standard deviations) across the three random seeds for the main result tables.
3. Clarify the ICL efficiency metric: specify exactly how "normalized over the whole area" is computed, discuss its sensitivity to shot-range choice, and consider supplementing with a simpler metric (e.g., average improvement per shot).
4. Soften the "emergent threshold" language to "scaling trend" or "model-size effect" given the limited data.
5. Add a data availability statement and discuss potential limitations of synthetic tasks for generalization to real-world use.

## Score and Decision

This is a strong, well-motivated benchmark paper with a compelling critique of existing practice and a thorough, well-designed evaluation. The identified weaknesses (evidential gap in the motivation experiment, undercharacterized ICL efficiency metric, missing variance reporting, thin emergence claim, no data availability statement) are all addressable and do not undermine the core contribution. The paper makes a clear, timely, and useful contribution to the multimodal ICL community.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>