Now I have a thorough understanding of the paper content. Let me produce the final consolidated review.

## Summary

This paper addresses continual instruction tuning for Large Vision-Language Models (LVLMs). It contributes two things: (1) **COAST**, a benchmark covering three continual learning settings (domain-incremental, capability-incremental, dataset-incremental) that goes beyond prior work limited to dataset-incremental only; and (2) **Continual LLaVA**, a rehearsal-free method that freezes the LVLM and learns "dual increment embeddings" — intrinsic embeddings (selected from a low-rank pool via instruction similarity) for task-specific knowledge and contextual embeddings (aggregated from previous tasks) for inter-task dependencies. Reported results show a 13.06% absolute improvement over sequential training on the COAST-domain setting.

## Strengths

- **First benchmark to systematically define three continual instruction tuning settings for LVLMs.** Prior work (e.g., COIN, EMT, Zhai et al.) was limited to dataset-incremental scenarios. COAST distinguishes domain-incremental (e.g., chartqa → documentqa → iconqa), capability-incremental (e.g., conversation → complex reasoning → detail description), and dataset-incremental, which better reflects real-world deployment requirements (Section 1, lines 16–18).

- **Novel dual increment embedding mechanism.** The separation into intrinsic (task-specific, selected via retrieval from a low-rank pool) and contextual (inter-task, aggregated from previous tasks via learnable weights) components is a principled design that draws on ideas from prompt-based continual learning but adapts them to the instruction-tuning paradigm. The use of a low-rank pool with Sentence-BERT-based retrieval is a sensible, parameter-efficient approach (Section 3.2).

- **Rehearsal-free and parameter-efficient design.** By freezing all LVLM weights and only updating the increment embeddings, the method avoids the memory overhead of experience replay. The ablation showing that adapting only the output linear projection suffices (rather than all four projection layers) is a practical efficiency insight (Section 3.3, though the full ablation results appear in the stripped experiments section).

- **Large reported gains on the key metric of forgetting.** The 13.06% absolute improvement in average accuracy and 13.25% reduction in average forgetting over sequential training on COAST-domain demonstrates the method meaningfully addresses catastrophic forgetting (Section 1, line 31).

## Weaknesses

### Fatal

None.

### Major

- **No analysis of pool selection diversity or alignment loss dynamics.** The alignment loss (Eq. 6) optimizes only the *selected* proxy embeddings $\{\vk_{i_m}\}_{m=1}^M$ by maximizing cosine similarity with the frozen surrogate embedding, while the $N-M$ unselected embeddings remain at their random initialization. This creates a potential positive feedback loop: the same proxies that are already closest to the instruction embeddings get pushed even closer, making them more likely to be selected again, while unused proxies are never trained. Over a stream of tasks where instruction embeddings are similar (e.g., within the same domain), this could lead to representational collapse where only a small fraction of the pool carries signal. The paper provides no analysis of how many distinct proxy embeddings are selected per task, the overlap between tasks, or how sensitive performance is to the pool size $N$ and selection count $M$. Without this, the claim that intrinsic embeddings capture "task-specific characteristics" is insufficiently supported, and the two-stage training may be fragile. This is the most significant methodological gap in the paper as presented.

### Minor

- **Ambiguous description of contextual increment embedding construction.** It is stated that $\mathcal{Z}_t$ records "all the selected increment embeddings in each task via Eq. (2)" (line 90), but Eq. (2) gives the *selection indices* $\mathcal{I}$, not the embeddings themselves. It is unclear whether $\mathcal{Z}_t$ stores: (a) the individual selected $\mP_{i_m}$ matrices for every instance (size $|\mathcal{D}_t| \times M$), (b) the per-instance aggregated $\Delta\theta_t^i$ from Eq. (5), or (c) some other representation. The operation "instance-wise average pooling" (line 98) is also not precisely defined. While the overall idea — aggregating previous-task knowledge into a single representation per task — is clear, the exact shapes and operations need specification for reproducibility. This does not invalidate the method but should be clarified.

- **Choice of Sentence-BERT for surrogate embeddings is not justified.** The method uses a frozen Sentence-BERT model to encode instructions for retrieval. Since the LLM (Vicuna) is itself a text embedder, the choice to introduce an external model should be motivated (e.g., computational efficiency, representation quality, or initialization concerns). This is a design dependency worth documenting.

- **"Softmax manner" is imprecise.** Eq. (5) uses cosine-similarity-weighted averaging (cos/sum(cos)), not actual softmax (exp(cos)/sum(exp(cos))). The text's phrasing is slightly inaccurate, though the equation itself is clear.

### Trivial

- Minor inconsistency in the contribution list: "Continua LLaVA" (line 31) is missing the trailing "l" — likely a typo in the extracted text (parser artifact, noted for completeness).

## Nice-to-Haves

- Provide a summary table of the COAST benchmark (tasks, source datasets, sample counts, evaluation metrics) in the main paper body rather than solely in the appendix/experiments section. The three settings are described verbally with examples, but a compact reference table would improve readability.
- An ablation removing $\mathcal{L}_{\text{align}}$ (training only with the auto-regressive loss and raw selection) would help disentangle whether the two-stage training is necessary or whether the selection mechanism alone is sufficient.
- Consider reporting the fraction of unique proxy embeddings selected per task and the Jaccard overlap between tasks to demonstrate that the pool is being used diversely.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Sequential training is a lower bound, not a competitive baseline"** — The paper mentions the 13.06% improvement over sequential training as one illustrative example in the contribution list but likely compares against stronger baselines (EWC, L2P, DualPrompt, replay methods) in the stripped experiments section. The criticism assumes the absence of those baselines based on partial text; the full submission almost certainly includes them.
- **"COAST benchmark is not fully described in main text"** — The reviewer acknowledges this content was stripped by the parser to the appendix. The main text provides the three setting definitions with concrete examples (chartqa, documentqa, iconqa for domain; conversation, complex reasoning, detail description for capability). A compact summary table in the main paper would help, but calling this a weakness of the paper (as opposed to a limitation of the extracted text) is unwarranted.
- **"Strength: Alignment stage for proxy embedding training"** (from Strength Finder) — This strength conflicts with the verified weakness about pool diversity collapse. The alignment stage's claimed benefit ("ensuring reliable selection") is precisely what needs to be demonstrated rather than assumed. Following the rule that weaknesses supersede conflicting strengths, this strength is dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any unforeseen implications or connections that the authors themselves did not identify.

## Suggestions

- Add an analysis of pool selection diversity (number of unique proxy embeddings activated per task, inter-task overlap) to demonstrate the method is not collapsing onto a small subset of the pool.
- Clarify the exact construction of $\mathcal{Z}_t$ and the definition of "instance-wise average pooling" with explicit tensor shapes.
- Add an ablation study removing $\mathcal{L}_{\text{align}}$ to test whether the two-stage training is necessary.
- Briefly justify the use of Sentence-BERT over using the LLM's own representations.
- Include a compact summary table of the COAST benchmark (datasets, sizes, metrics) in the main body.

## Score and Decision

The paper addresses an important, under-studied problem (continual instruction tuning in LVLMs). The dual increment embedding framework is a novel and sensible methodological contribution, and COAST fills a genuine gap by defining three incremental learning settings. The key results (large improvements in accuracy and forgetting reduction) are promising. However, the pool diversity concern is a significant open question that directly affects whether the method works as claimed — if only a few proxies are repeatedly selected and reinforced, the claimed "task-specific characteristics" are not meaningfully captured, and the effective capacity of the pool may be tiny. This is not a fatal flaw (it is plausible the method works well in practice), but it is a real gap in the evidence that prevents full confidence. Given that the experiments section is stripped and thus the full baseline comparisons and ablations are unavailable for verification, and given the pool analysis gap, a top-tier acceptance is not warranted in the current form. The paper could be a solid contribution after addressing the pool dynamics analysis.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>