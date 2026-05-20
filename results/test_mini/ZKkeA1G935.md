Now I have all the evidence. Let me compose the final consolidated review.

## Summary

This paper makes three contributions to Graph Continual Learning (GCL): (1) it identifies a fundamental flaw in the prevalent *local testing* evaluation protocol—task ID leakage, where the model can trivially identify which task a test node belongs to, reducing class-incremental learning to task-incremental learning; (2) it presents LLM4GCL, the first comprehensive benchmark evaluating LLM-based and GLM-based methods on GCL across 7 text-attributed graphs, 2 learning scenarios, and 15 baselines; and (3) it proposes SimGCL, a simple prototype-based method combining graph-prompted instruction tuning (first session only, via LoRA) with training-free prototype classification, which achieves substantial improvements over GNN, LLM, and GLM baselines on most datasets.

## Strengths

1. **Identification of task ID leakage in local testing (Section 3.1, Table 1):** The paper shows that even a basic mean pooling operation on the same subgraph used for training achieves 100% task ID prediction accuracy and zero forgetting across all 7 datasets. This exposes a previously unrecognized flaw in prior GCL evaluations, where the test setup inadvertently leaks task identity. This is a meaningful methodological contribution that affects how results from multiple previous works should be interpreted.

2. **First comprehensive LLM benchmark for GCL:** The paper systematically evaluates 9 LLM- and GLM-based methods across 7 text-attributed graph datasets under both NCIL and FSNCIL scenarios, providing the first such resource in the field. The benchmark reveals several non-obvious findings (e.g., current GLMs underperform pure LLM methods in GCL, prototype-based strategies are robust to session count) that will inform future work.

3. **SimGCL achieves strong empirical results with large margins on most datasets:** In Table 2 (NCIL), SimGCL surpasses all baselines on 5 of 7 datasets by substantial margins (e.g., 84.6% vs. 70.8% SimpleCIL on Cora; 82.1% vs. 63.6% Cosine on Photo). The method is principled—tuning only the first session avoids catastrophic forgetting of the backbone—and the design choices (graph prompt, LoRA, prototype classification) are well-motivated.

4. **Comprehensive experimental analysis:** The paper covers 7 datasets spanning citation, web link, and e-commerce domains at varying scales, two learning scenarios (NCIL and FSNCIL), and ablations on session count (Table 4) and model scaling (Figure 3). The analysis of why GLMs underperform (overfitting, inter-modal misalignment) and why prototype methods excel is supported by concrete evidence.

## Weaknesses

### Fatal

None.

### Major

None. No weakness is severe enough to invalidate the paper's core claims.

### Minor

1. **"Consistently overperform" is overstated given documented exceptions (Obs. ⑧, Tables 2 and 3):** The paper states "SimGCL consistently overperform GNN-, LLM- and GLM-based baselines" and supports this with "23 out of 28" best results. However, the counterexamples are clear: SimpleCIL outperforms SimGCL on Arxiv-23 in both NCIL (AA 52.4 vs. 38.7, AN 38.8 vs. 13.6) and FSNCIL (AA 49.8 vs. 31.8, AN 40.0 vs. 10.3), and also on Arxiv in FSNCIL (AA 46.4 vs. 36.3, AN 36.6 vs. 6.8). The paper does acknowledge these cases in the body text (end of Obs. ❻), but the summary claim in Obs. ⑧ remains misleading. The authors should replace "consistently" with a qualified statement (e.g., "outperforms on 23 of 28 metrics"). This does not undermine the core contribution—SimGCL is still the best method overall—but the overclaim should be corrected.

2. **Minor ambiguity about inter-task edges in global testing (Section 3.1 vs. Figure 1):** The text states "our benchmark excludes inter-task edges, using only intra-task connections" (p.76, in the context of preventing knowledge leakage). The global test graph is defined as "the union of the subgraphs from all previous tasks" (p.74). If inter-task edges are excluded everywhere, then both training and test graphs contain only intra-task edges, and there is no distribution shift. However, Figure 1's caption says "global testing, which uses the complete graph with inter-session edges," creating an apparent inconsistency. This is a presentation issue—the text is clear about the actual protocol, but the figure description should be aligned to avoid confusion. The authors should clarify in the caption and/or text exactly which edges (inter-task or not) are present at test time.

3. **Forgetting metrics omitted from main experiments (Tables 2 and 3):** The paper reports only average accuracy (AA) and final accuracy (AN) for the main NCIL and FSNCIL experiments. For a continual learning paper focused on "alleviating catastrophic forgetting," including forgetting ratio (or backward transfer) is standard practice. While Table 1 includes AF for the local-testing critique, Tables 2 and 3 do not. The authors should add forgetting metrics to the main tables or at minimum include them in the appendix with discussion in the main text. This would help distinguish whether SimGCL's improvements stem from better plasticity or genuinely less forgetting.

### Trivial

1. **Equation (1) notation is redundant:** The equation for prototype computation uses $K = \sum \mathbb{I}(y_j=i)$ summed over $|\mathcal{Y}_b|$ elements, where $|\mathcal{Y}_b|$ is already defined as the number of labeled nodes of class $i$ in session $b$. Since all summed elements satisfy $\mathbb{I}(y_j=i)=1$ by construction, $K = |\mathcal{Y}_b|$, making the indicator redundant. The notation should be simplified for clarity (e.g., sum directly over the set of labeled nodes of class $i$).

2. **Figure caption inconsistency:** As noted in Minor #2, Figure 1 mentions "inter-session edges" in global testing while the text excludes inter-task edges. This needs alignment.

3. **No statistical significance reported:** Some comparisons (e.g., SimGCL vs. SimpleCIL on several datasets) are close enough that variance across seeds would matter. Reporting mean and std over multiple runs would improve confidence.

## Nice-to-Haves

- An ablation isolating the effect of the graph prompt (text-only node features vs. graph-prompted instruction tuning) would directly test whether the structural information in the prompt adds value beyond the LLM's text understanding.
- Analysis of how class prototypes drift across sessions for SimGCL vs. SimpleCIL/Cosine would provide mechanistic insight into why SimGCL sometimes underperforms on longer sessions.
- A brief discussion of limitations (when SimGCL should not be used, e.g., sparse graphs like Arxiv-23, many long sessions) would help practitioners.
- The temperature hyperparameter $\tau$ in Eq. (2): a sensitivity study would be helpful.

## Removed Points

*The following points from the inputs were removed after cross-checking against the paper:*

- **Training protocol for LLM/GLM baselines underspecified:** The paper states "Extended descriptions are provided in Appendix B.4 and C" (Section 3.2). The appendix was stripped by the parser; the details exist in the original submission. Per the rules, this criticism is not valid.
- **"Not yet released" / reproducibility concerns about cited models/tools:** The paper cites publicly available models (BERT, RoBERTa, LLaMA, GraphPrompter, GraphGPT, etc.) and provides an anonymous code repository. These criticisms reflect reviewer knowledge gaps, not author errors.
- **"Flawless task ID prediction" phrasing too sensational:** The statement is factually correct (100% accuracy across all datasets as shown in Table 1) and appropriately caveated (the flaw is specific to local testing). Not a genuine weakness.
- **Observation ❹ (dense graphs) is speculative:** All observations about dataset properties are appropriately hedged ("may enhance," "likely stems from"), and the paper is presenting empirical patterns for the community to investigate further.
- **Missing related works:** Cannot be verified without external sources.
- **Formatting/style nitpicks and typos:** These are parser artifacts, not author errors.
- **GCN<sub>LLM<sup>Emb</sup></sub> notation confusion:** The notation is consistent within the paper.

## Novel Insights

The synthesis of reviews reveals that the paper's most impactful contribution is not the proposed method SimGCL, but rather the identification of a systematic evaluation flaw in prior GCL work that goes beyond a simple benchmark critique. The harsh critic correctly notes that the "consistently overperform" claim overreaches, and this overclaim may distract from the paper's genuine strength: it provides the field's first rigorous testbed for LLMs in GCL and convincingly demonstrates that prototype-based frozen-backbone strategies—common in vision—transfer effectively to graph domains when combined with appropriate graph-prompted instruction tuning. The condition where SimGCL fails (sparse graphs like Arxiv-23, long sessions) is precisely where the graph prompt provides little structural signal, reinforcing rather than undermining the method's motivation. A clearer articulation of this boundary condition would strengthen the paper.

## Suggestions

1. Revise Obs. ⑧ to replace "consistently overperform" with a quantified statement (e.g., "SimGCL achieves the best or second-best results on 23 of 28 metrics, with particularly large margins on dense graphs").
2. Align the Figure 1 caption with the main text regarding inter-task edges: specify clearly whether global testing uses inter-task edges or not. If edges are excluded everywhere, say so explicitly in the caption.
3. Add forgetting metrics (average forgetting or backward transfer) to Tables 2 and 3, or at minimum provide them in the appendix and reference them in the main text.
4. Add a brief limitations paragraph or sentence noting the conditions under which SimGCL underperforms SimpleCIL (sparse graphs, many long sessions, FSNCIL with large base sessions).
5. Simplify Equation (1) notation to avoid redundancy between $K$ and $|\mathcal{Y}_b|$.
6. (Nice-to-have) Add an ablation comparing graph-prompted tuning vs. text-only instruction tuning to isolate the value of structural information.

## Score and Decision

### Calibration

**Round 1 (Bracketing):**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Randomized Rep. in OCGL | sieYp1CpYk.md | 4.00 | R1 | Weaker: limited novelty, mostly transferring an existing idea to graphs |
| IPAL | hEe8IYhyhN.md | 5.00 | R1 | Weaker: incremental evolution of PCL; current paper has more fundamental contributions |
| Graph2Hyper | e6N1ZFY2X1.md | 4.50 | R1 | Weaker: marginal gains over TPP (1-2%), narrow scope; current paper has 20% gains |
| LANO | 8ANXIJLtz6.md | 5.33 | R1 | Somewhat weaker: similar topic (LLMs for graphs) but LANO is about open-world annotation, not CL; current paper has more comprehensive evaluation |
| Graph Unlearning Benchmark | gSPkuTTWgU.md | 5.00 | R2 | Comparable in being a benchmark paper; current paper additionally identifies an evaluation flaw and proposes a SOTA method |
| The Lie of the Average | 19LHXi9uLw.md | 5.60 | R2 | Similar in spirit (evaluation critique); current paper has more breadth (benchmark + method + critique) but also more weaknesses |

**Round 1 bracket:** 4.0 – 6.5

**Round 2 (Narrowing):** Based on comparison with the accepted evaluation-critique papers (5.00–5.60), the current paper has a more impactful evaluation flaw discovery (it invalidates prior results rather than just improving evaluation methodology) and additionally provides a comprehensive benchmark and SOTA method. However, it also has clearer weaknesses (overclaimed "consistently" statement, figure/text inconsistency) than those focused papers. The paper is clearly stronger than all the rejected GCL papers (4.00–5.33) whose scores appear to be depressed by limited novelty or marginal gains.

**Final score:** 6.0 — A solid contribution with genuine value (evaluation flaw discovery + benchmark + SOTA method) tempered by fixable but real weaknesses in presentation and claim precision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>