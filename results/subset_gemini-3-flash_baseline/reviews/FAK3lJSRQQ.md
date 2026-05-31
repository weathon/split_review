## Summary
The paper introduces ExLLM (Experience-Enhanced LLM optimization), a framework that utilizes Large Language Models as optimizers for complex, discrete search spaces, with a primary focus on molecular design. The method addresses the limitations of existing LLM-based optimizers—such as memory bloat and exploration collapse—through three main components: an evolving experience mechanism that distills non-redundant insights into a compact snippet, a $k$-offspring sampling strategy to increase exploration breadth per query, and a feedback adapter to unify multi-objective signals and constraints. The authors demonstrate state-of-the-art performance on the PMO molecular benchmark and show strong generalization across diverse domains including circle packing, stellarator design, and combinatorial optimization.

## Strengths
- **Strong Empirical Results:** The framework achieves a significant improvement (+7.3%) over the previous state-of-the-art on the PMO benchmark, ranking first on 17 out of 23 tasks.
- **Broad Generalization:** Unlike many molecular design papers that are domain-specific, ExLLM demonstrates record-breaking or competitive performance in vastly different fields: geometry (circle packing), physics (stellarator design), engineering (offshore jackets), and code generation (GCU operators).
- **Efficiency and Scalability:** The "evolving experience" mechanism effectively solves the "memory bloat" problem common in RAG-based or append-only LLM optimization loops. Table 1 provides clear evidence that this approach maintains high uniqueness and hypervolume while keeping costs and runtimes significantly lower than retrieval-style memories.
- **Methodological Soundness:** The hybrid selection strategy (combining fitness-based and Pareto-front selection) is well-motivated for balancing exploitation and diversity in multi-objective landscapes.

## Weaknesses
### Fatal
None.

### Major
- **Ablation of the Feedback Adapter:** While the paper emphasizes the importance of the feedback adapter for handling complex constraints and expert hints, the quantitative impact of this component is less clear than the experience and $k$-offspring modules. Specifically, it is unclear how much of the gain in the "Stellarator" or "Circle Packing" tasks is due to the LLM's reasoning over the formatted feedback versus the evolutionary search itself.

### Minor
- **Sensitivity to $p_{\text{exp}}$:** The paper mentions that the experience injection probability $p_{\text{exp}}$ is a key hyperparameter to prevent over-exploitation. While it is ablated in the text, more discussion on how this parameter should be tuned for new, unseen domains would improve the framework's "plug-and-play" claim.
- **LLM Dependency:** The performance is likely sensitive to the underlying LLM (e.g., GPT-4o vs. Gemini). While the authors use high-performing models, the variance in performance across different model versions is not extensively documented.

### Trivial
- The "Worst-init" experiment is a clever way to test robustness, but the gap between "Best-init" and "Worst-init" results suggests that the LLM optimizer is still somewhat sensitive to the starting point, which is expected but worth noting.

## Nice-to-Haves
- A visualization of the "Evolving Experience" snippet over several generations for a specific task (e.g., molecular design) to show how the LLM's "insights" change over time.
- Comparison with more traditional "LLM-free" evolutionary strategies that use similar $k$-offspring or Pareto selection to isolate the specific value-add of the LLM's domain knowledge.

## Novel Insights
The most significant insight is the demonstration that a *single, evolving, and distilled* text-based memory is superior to high-capacity retrieval-based memories for long-horizon discrete optimization. In optimization, "more information" in the prompt often leads to "less exploration" due to the LLM's tendency to over-focus on provided examples (exploration collapse). By treating memory as a dynamic, low-dimensional summary rather than a database, ExLLM maintains the "creativity" of the LLM while providing enough guidance to converge.

## Suggestions
- Provide a more detailed breakdown of the "Feedback Adapter" performance. For instance, a small experiment showing the success rate of the Stellarator task with vs. without the "constraints-to-objectives" promotion would strengthen the claims in Section 3.3.
- Clarify the "k-offspring" implementation: does the LLM generate $k$ samples in a single completion, or are these $k$ independent parallel calls? The text suggests autoregressive conditioning (one call), which is a smart way to save tokens, but confirming this would help reproducibility.

## Score and Decision
The paper presents a robust, well-evaluated, and highly versatile framework for LLM-based optimization. The empirical results on the PMO benchmark are impressive, and the cross-domain results (especially circle packing and stellarator design) prove that the method is not over-fitted to chemistry. The solution to the memory bloat problem is practical and well-supported by the data.

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>