I now have a thorough understanding of the paper and all the claims. Let me produce the final consolidated review.

---

## Summary

This paper tackles continual instruction tuning for Large Vision-Language Models (LVLMs). It contributes (1) **COAST**, a benchmark spanning domain-incremental, capability-incremental, and dataset-incremental settings, and (2) **Continual LLaVA**, a rehearsal-free method that freezes the base LVLM and learns *dual increment embeddings* — intrinsic embeddings (selected from a low-rank pool based on instruction-text similarity) and contextual embeddings (aggregated across previous tasks via learnable weights) — inserted into a single linear layer. The paper claims state-of-the-art performance, e.g., 13.06% absolute accuracy improvement over sequential training on the domain-incremental setting.

## Strengths

1. **Timely and well-motivated problem formulation.** Continual instruction tuning for LVLMs is under-explored, and the paper's decomposition into domain-incremental, capability-incremental, and dataset-incremental settings is a genuinely useful conceptual contribution that goes beyond the dataset-incremental focus of prior concurrent works (Sec. 1).

2. **Novel dual-increment architecture.** Separating task-specific knowledge (intrinsic embeddings selected by instruction similarity) from inter-task relational knowledge (contextual embeddings aggregated across tasks) is a principled and clean design for rehearsal-free continual learning. The mechanism is described in detail in Sec. 3.2 with clear equations (Eq. 1–6).

3. **Parameter efficiency and architectural simplicity.** The method freezes the entire pre-trained LVLM (visual encoder + LLM) and only tunes the increment embeddings inserted into a single output-projection layer (Sec. 3.3), keeping overhead low — a practical advantage for deployment.

4. **Two-stage optimization is clearly specified.** Stage 1 aligns selected proxy embeddings to instruction surrogates via a cosine-similarity loss (Eq. 6), and Stage 2 performs standard auto-regressive training with the learned embeddings (lines 111–118). The paper states this explicitly.

## Weaknesses

### Fatal
None.

### Major

1. **The proxy-embedding selection mechanism lacks stability analysis.** The alignment loss (Eq. 6) updates only the *selected* proxy embeddings; unselected proxies receive no gradient. This creates two unaddressed risks: (a) **embedding collapse** — all proxies could converge to similar regions of the embedding space, making selection near-random; (b) **selection collapse** — a small subset of proxies could dominate across all tasks, effectively reducing the usable pool size below \(N\). Both would undermine the method's core claim of encoding task-specific characteristics. The paper provides no diagnostic analysis (e.g., entropy of selection distributions across tasks, t-SNE of proxy embeddings, task-to-proxy mapping visualization) to rule these out. Since the selection mechanism is the backbone of the intrinsic embedding component, this gap is significant.

2. **The contextual embedding weight update procedure is underspecified.** In Eq. 4, \(\Delta\delta_t^i = \sum_{l=1}^{t} w_l \operatorname{sg}(\overline{\mathcal{Z}}_l)\), the paper describes \(w_l \in [0,1]\) as a "learnable weight" but never specifies: are these weights learned from scratch for each new task (allowing per-task reweighting), accumulated across tasks, or learned jointly? What prevents overfitting to the most recent task? How does the parameter count scale with task sequence length? The stop-gradient on \(\overline{\mathcal{Z}}_l\) means only \(w_l\) receives gradient, yet the training dynamics of these weights are not discussed. This ambiguity makes it difficult to assess the component's behavior in long task sequences.

### Minor

3. **Visual input is entirely ignored in the selection of intrinsic embeddings.** The selection mechanism (Eq. 2) relies solely on Sentence-BERT encoding of the instruction text. For LVLMs, the visual content is often critical for distinguishing tasks — e.g., differentiating chart QA from medical QA when the instruction is simply "answer the question based on the image." The paper does not acknowledge or discuss this limitation, nor does it provide evidence that text-alone suffices for reliable task discrimination across the three incremental settings.

### Trivial

None.

## Nice-to-Haves

- A diagnostic analysis of proxy-embedding diversity (entropy of selection distributions, t-SNE visualizations colored by task) would directly address the stability concern and is a concrete, feasible addition.
- An ablation comparing "learned context weights vs. uniform weights vs. random weights" would clarify whether the contextual component meaningfully captures inter-task dependencies or functions as a learnable bias.
- A brief intuitive justification for why adapting *only* the output projection (rather than Q/K/V) is sufficient would help readers understand the design choice without cross-referencing the ablation section.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing experimental sections (Sec. 4.1, 4.2, 4.3).** The paper's extracted text shows `\input{exps/...}` commands at lines 125–127, which the parser did not resolve. Per the review guidelines, this is a parser/formatting artifact — the original submission would have contained these sections. The core empirical evidence is therefore assumed present in the original PDF.
- **COAST benchmark construction details absent.** Benchmark dataset lists, task counts, preprocessing, and evaluation protocols would reside in the stripped experimental sections. Same parser-artifact justification.
- **Hyperparameter discussion (N, M, R, layer choice).** The paper cites experiments in the missing Sec. 4.3 for these choices — again a parser artifact issue.
- **Two-stage training clarification.** The paper already specifies (lines 111–118) that Stage 1 uses the alignment loss and Stage 2 uses the auto-regressive loss as a two-stage procedure. The reviewer's question about joint optimization is already answered in the text.
- **Formatting/style nitpicks, generic weakness framings.** Removed per guidelines.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension: the paper's strength — a clean, parameter-efficient architecture — is also its vulnerability, because the selection mechanism that drives task-specific adaptation is only as reliable as the proxy-embedding pool's diversity, and the paper provides no evidence that collapse does not occur. This trade-off between simplicity and verifiability is worth the authors' attention.

## Suggestions

1. **Diagnose selection stability.** Report the entropy of proxy-selection distributions per task, visualize proxy embeddings with t-SNE colored by the task that most frequently selects each proxy, and measure the diversity of selected subsets across tasks. This would directly address the most serious concern.
2. **Specify the contextual weight update procedure explicitly.** State whether \(w_l\) is learned per-task from scratch, accumulated, or jointly; describe the parameter growth pattern; and add a brief discussion of potential overfitting to the most recent task.
3. **Acknowledge and discuss the text-only selection limitation.** Even a brief paragraph noting that the method currently ignores visual cues in the selection step, and discussing when this might or might not be problematic, would improve completeness.
4. **Add a contextual-component ablation.** Comparing learned weights against uniform weights and random weights would clarify whether the contextual embedding provides genuine inter-task transfer or functions as a learned bias.

## Score and Decision

Based on the paper's content (treating the missing experimental sections as parser artifacts):
- **Originality:** Good — the three-setting benchmark and dual-increment mechanism are novel.
- **Importance:** High — continual instruction tuning for LVLMs is a timely and practical problem.
- **Claims support:** The method is well-motivated and described; however, stability of the core selection mechanism is not analyzed, and the contextual weight update is underspecified. These weaken, but do not invalidate, the contribution.
- **Soundness:** The architecture and optimization are clearly presented; the main concerns are about *verification* of stability, not about correctness of the design.
- **Clarity:** The writing is clear and well-structured.
- **Value:** The benchmark framing and the method would be useful to the community.

The paper makes a meaningful contribution but has nontrivial gaps in verifying the stability of its core selection mechanism and in specifying the contextual weight training procedure. These are addressable in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>