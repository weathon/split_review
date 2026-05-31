Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

This paper investigates whether Large Language Models (LLMs) can alleviate catastrophic forgetting in Graph Continual Learning (GCL). The authors first identify a critical evaluation flaw in all prior GCL work—"local testing" allows trivial task ID prediction, effectively reducing class-incremental learning to task-incremental learning. They then introduce **LLM4GCL**, a comprehensive benchmark that evaluates 9 LLM/GLM-based methods across 7 Text-Attributed Graph (TAG) datasets under a corrected "global testing" protocol. Finally, they propose **SimGCL**, which combines graph-prompted instruction tuning (LoRA, first session only) with training-free prototype classification for subsequent sessions, achieving up to ~21.7% improvement over the best GNN baseline under rehearsal-free constraints.

---

## Strengths

- **Identification of a systemic evaluation flaw (well-evidenced):** The "task ID leakage" finding is the paper's most important contribution. Table 1 demonstrates convincingly that simple mean pooling achieves 100% task ID prediction accuracy under local testing, matching the sophisticated TPP baseline identically—including when the GNN backbone is replaced with a plain MLP. This definitively shows that all prior GCL evaluation in NCIL has been measuring a much easier (task-incremental) problem under the guise of class-incremental learning. The follow-up result that TPP collapses from ~90% accuracy to ~15–45% under global testing drives home the point.

- **Comprehensive empirical study with useful actionable insights:** The benchmark covers 7 diverse datasets, 3 method families (GNN, LLM, GLM), 2 learning scenarios (NCIL, FSNCIL), and ablations over session count and model size. Observations 2–8 provide structured takeaways (e.g., GLM underperformance due to architectural mismatch, prototype-based stability across session counts, scaling benefits) that are well-supported by the tabulated results and are genuinely informative for practitioners.

- **Strong and consistent results for SimGCL:** SimGCL achieves the best performance in 23 out of 28 metric/dataset combinations in both NCIL and FSNCIL. The design is elegant—fine-tune once via LoRA on the first session using ego-graph prompts, then use training-free prototype classification forever after. This sidesteps catastrophic forgetting naturally without any replay, regularization, or per-session parameter updates.

- **Discovering GLM failure modes:** The paper identifies two distinct failure mechanisms for GLM-based methods—the architectural gap between shallow GNNs and deep LLMs causing divergent parameter updates (LLM-as-Predictor), and progressive overfitting to recent tasks due to strong fitting capacity (both categories). These are concrete mechanistic claims supported by the Table 2/3 patterns.

---

## Weaknesses

### Fatal
None.

### Major

- **SimGCL fails significantly on Arxiv-23:** On both NCIL and FSNCIL, SimGCL underperforms SimpleCIL by large margins (13.7% in NCIL Ā: 38.7% vs. 52.4%; 18% in FSNCIL Ā: 31.8% vs. 49.8%). The authors attribute this to Arxiv-23's sparse graph structure, which limits the utility of structural prompts—but they provide no ablation to confirm this. This is not a minor outlier: Arxiv-23 is a real benchmark dataset, and having a method degrade by 13–18% relative to a simpler baseline is a genuine limitation that the paper does not adequately diagnose or resolve. Taken together with below-average performance on Arxiv (FSNCIL), SimGCL has a systematic weakness on citation networks with sparse or difficult structure.

- **The contribution of graph prompting over plain LLM fine-tuning is not isolated:** SimGCL differs from SimpleCIL in two ways: (1) LoRA fine-tuning on session 1, and (2) ego-graph structured prompts. There is no ablation separating these factors (e.g., SimGCL without graph prompts = LLM fine-tuned on plain text + prototypes). Without this, it is unclear whether the gains are from structural graph information or simply from first-session LLM adaptation. The failure on Arxiv-23 further raises doubt about whether ego-graph prompts are actually the active ingredient.

- **Misleading framing of the "~20% improvement" claim:** The abstract states SimGCL surpasses "previous state-of-the-art GNN-based baseline by around 20% under rehearsal-free constraint." However, SimpleCIL (a non-graph-specific, non-continual-learning method) also surpasses GNN baselines by 12–29% across datasets. The actual improvement of SimGCL over SimpleCIL—the most relevant comparison—is typically 5–15% (and negative on Arxiv-23). The paper later acknowledges SimpleCIL's strength, but the abstract framing overstates SimGCL's novelty over existing approaches.

### Minor

- The paper finds that GLMs (LLM-as-Predictor category) suffer from "progressive overfitting," but this is also true of all non-prototype-based LLM methods. A clearer analysis of why prototype-based approaches specifically prevent forgetting in the LLM feature space (beyond citing fixed parameters) would strengthen the theoretical narrative.

- The claim that SimGCL's FSNCIL performance disadvantage on Arxiv-23 is due to "larger base tuning set overfitting" is speculative. The base session has 12 classes vs. 4 in other datasets—but why this would specifically harm Arxiv-23 more than other datasets is not explained.

### Trivial

- The notation for prototype computation (Eq. 1) defines the prototype as a conditional average, which is standard. No issues, but the paper could point readers more directly to which prior work (SimpleCIL) introduced this.

---

## Nice-to-Haves

- An ablation isolating the effect of ego-graph prompting vs. plain-text prompting (with identical LoRA fine-tuning) would clarify the structural contribution of SimGCL.
- Analysis of *why* Arxiv-23 specifically causes SimGCL to underperform—e.g., measuring structural information content via graph density or clustering coefficient and correlating with SimGCL performance.
- An efficiency table reporting training time and GPU memory would strengthen the practical case for SimGCL (the paper mentions efficiency as an advantage but provides no quantitative support).
- The paper proposes excluding inter-task edges to avoid knowledge leakage during GNN message-passing. An experiment showing the impact of including vs. excluding these edges would validate this design choice.

---

## Novel Insights

The most genuinely novel contribution here is the task ID leakage discovery. Prior to this paper, the GCL community—including TPP (Niu et al., 2024b), which was the accepted state-of-the-art—was unknowingly evaluating a far easier problem than intended. The demonstration that even an MLP with mean pooling can trivially decode task identity from local subgraph structure reveals that class-incremental evaluation has been operationally equivalent to task-incremental evaluation. This is an insight that invalidates not just the metrics but the entire comparative story of prior GCL literature, and it motivates re-evaluation of the field's progress from scratch. The subsequent finding that prototype-based LLM methods excel precisely because they are immune to per-session parameter drift (while GNN methods fail catastrophically) provides a clear architectural principle: in GCL, preserving the feature encoder is more important than adapting it, and LLMs' rich pretrained representations make their prototypes far more discriminative than GNN embeddings.

---

## Suggestions

- Provide an ablation: SimGCL (with ego-graph prompt) vs. SimGCL-text (same LoRA fine-tuning, plain text input) to isolate the structural contribution.
- Report performance variance (e.g., standard deviation across runs or dataset splits), especially for FSNCIL where class selection may introduce variance.
- For Arxiv-23 specifically, analyze whether the underperformance is consistent across backbone sizes, or whether larger models recover some performance—this would help determine if the failure is structural (sparse graphs) or model-capacity related.
- Clarify in the abstract that the ~20% improvement is relative to GNN baselines, not all baselines.

---

## Score and Decision

The paper's identification of task ID leakage is a significant and rigorously demonstrated finding that re-contextualizes all prior GCL evaluation. The LLM4GCL benchmark and the extensive experiments provide real value to the community. SimGCL's design is practical and achieves strong results in most settings. The key limitations are: (1) SimGCL fails substantially on Arxiv-23 without adequate explanation or remedy, (2) the contribution of graph prompting vs. simple LLM fine-tuning is not isolated, and (3) the abstract somewhat overstates improvements. These are meaningful concerns but do not invalidate the core findings. The paper is a solid contribution that will advance the GCL subfield, particularly by resetting the evaluation standard.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>