Now I have a solid bracket. Let me compile my analysis and write the final review.

---

## Summary
This paper presents the first systematic study of using LLMs for graph continual learning (GCL). It identifies a critical flaw in existing GCL evaluation — task ID leakage in local testing that reduces class-incremental learning to task-incremental learning — and proposes a corrected global testing protocol. The authors release LLM4GCL, a comprehensive benchmark spanning 7 datasets and 9+ methods across NCIL and FSNCIL settings, and propose SimGCL, a simple method combining ego-graph-prompted instruction tuning in the first session with training-free prototype classification. SimGCL substantially outperforms prior GNN-based methods.

## Strengths
- **Identification and empirical demonstration of task ID leakage.** Table 1 shows that even simple mean pooling of node features achieves 100% accuracy and zero forgetting across all seven datasets under local testing, conclusively demonstrating that prior results relying on this protocol do not genuinely assess continual learning capability. This is a significant and well-validated finding that the community should be aware of.

- **Rigorous global testing protocol.** The switch to global testing (union of all seen subgraphs), combined with removal of inter-task edges and class imbalance correction, yields a fair evaluation where prior SOTA methods (e.g., TPP) collapse — from near-perfect scores under local testing to near-zero on larger datasets (Table 2, Arxiv-23: 12.2% AA, Arxiv: 19.6% AA). This validates the necessity of the corrected evaluation.

- **Strong empirical evidence for LLM-based prototype methods.** Tables 2 and 3 show SimpleCIL and SimGCL outperforming the best GNN methods by large margins. On Cora NCIL, SimGCL achieves 84.6% AA vs. 65.4% for the best GNN (Cosine). SimpleCIL alone surpasses GNN-based models on 24 out of 28 metrics. The results are consistent across datasets and settings.

- **Comprehensive and well-controlled benchmark design.** The paper evaluates 9 methods (spanning GNN, LLM, and GLM categories) across 7 diverse text-attributed graphs with careful data preparation (class imbalance removal, no inter-session edges, multiple session configurations). Both NCIL and FSNCIL settings are covered, and Table 4 provides an insightful analysis of performance across session lengths.

- **SimGCL's design is simple yet effective.** The two-stage approach requires only first-session fine-tuning with LoRA, then training-free prototype classification — avoiding parameter updates that cause forgetting. The ego-graph prompt template (Figure 2) effectively encodes both textual and structural information into the LLM's native input space, avoiding the cross-modal misalignment that plagues existing GLMs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No ablation study for SimGCL's components.** The comparison between SimGCL and SimpleCIL demonstrates the combined benefit of graph-prompted instruction tuning over plain RoBERTa prototype matching, but the paper does not isolate the effect of the graph prompt from the instruction tuning, nor does it evaluate SimGCL without instruction tuning or without the graph prompt. Adding such ablations would strengthen the claim that both components contribute meaningfully. This is addressable and does not invalidate the core results, since SimpleCIL already serves as a meaningful baseline that isolates the graph prompt + instruction tuning combo versus raw embeddings.

- **The discussion of why GLMs underperform is insightful but partly speculative.** Obs.❸ attributes GLM failure to "overfitting" and "inter-modal misalignment," and Obs.❹ speculates that dense graph structures help GLMs but then notes Arxiv contradicts this. These are reasonable hypotheses but the evidence is correlational rather than causal. The paper acknowledges the Arxiv contradiction, which is good, but a more controlled analysis (e.g., varying density while holding other factors constant) would make these observations more robust.

### Trivial
- Observation numbering skips from ❹ to ❻ (line 175), with Obs.⑧ appearing next (line 177). The numbering is inconsistent.

## Nice-to-Haves
- **Discuss the impact of excluding inter-task edges on GNN vs. LLM comparisons.** The paper justifies this choice (privacy/storage constraints, Section 3.1), but does not discuss how the absence of inter-task edges disproportionately affects GNN methods that rely on graph smoothness across components, while LLM-only methods are unaffected. Adding this discussion or a small experiment with inter-task edges included would enrich the benchmark's insights.
- **Add forgetting metrics (e.g., backward transfer).** While average and final accuracy are standard, reporting forgetting explicitly would give a more complete picture, especially when comparing CL-specific methods like EWC and LwF against prototype-based approaches.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Unclear adaptation of GLM baselines to continual learning"** — The paper states that extended descriptions of baseline configurations are provided in Appendix B.4 and C. Per review guidelines, we do not penalize the paper for stripped appendix content that the authors claim exists.

- **"Insufficient experimental detail for reproducibility (hyperparameters, prompting strategies)"** — Same rationale as above; the paper defers these to the appendix. The main text does provide the key architectural details (LoRA, ego-graph prompt template, prototype computation).

- **"Overclaimed performance gains (~20% improvement)"** — Verified against Table 2: SimGCL outperforms the best GNN baseline (Cosine) by +19.2% on Cora, +26.4% on Citeseer, +18.5% on Photo, +35.0% on Products, +23.0% (AA) on Arxiv. The ~20% claim is supported across 5 of 7 datasets. The paper also explicitly discusses failure cases (Arxiv-23, FSNCIL) in Obs.⑧, which is transparent rather than cherry-picked.

- **"Obs.❷ overclaims LLM consistency"** — The paper specifically says "SimpleCIL surpasses all the GNN-based models in most datasets and metrics (24 out of 28)," which is factually accurate. It does not claim all LLMs outperform GNNs; BERT and RoBERTa are correctly described as "comparable to or marginally better than GCN."

- **"Missing related work on continual learning with pre-trained models (L2P, CODA-P)"** — Per review guidelines, we do not flag missing related works as the system cannot verify their relevance.

## Novel Insights
None beyond the paper's own contributions. The most novel finding — that task ID leakage makes local testing trivially solvable and thus invalid for assessing continual learning — is the paper's core contribution and is well-demonstrated.

## Suggestions
- **Add a minimal ablation for SimGCL**: at minimum, evaluate (a) frozen LLM + graph prompt (no instruction tuning) with prototype matching, and (b) instruction-tuned LLM without graph prompt. This would directly show the contribution of each component and significantly strengthen the method section.
- **Add a brief discussion of how the no-inter-task-edges design affects LLM vs. GNN comparisons**, since GNNs rely on cross-component message passing while LLMs do not. This would preempt a natural reader question.
- **Fix the observation numbering** so it is sequential (❶–❽).

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Online Continual Graph Learning | `4sJJixGIZX.md` | 5.00 | R1 | Weaker: problem formulation + benchmark, limited technical novelty; our paper adds evaluation flaw ID + method |
| CLDyB | `RnxwxGXxex.md` | 5.67 | R1 | Weaker: dynamic benchmark concept only; our paper has broader contributions and stronger empirical validation |
| TiC-CLIP | `TLADT8Wrhn.md` | 6.25 | R2 | Comparable: large-scale benchmark with insightful analysis, but some design flaws and no method contribution; our paper has benchmark + method + evaluation insight |
| Graph Pattern Comprehension | `CkKEuLmRnr.md` | 7.00 | R2 | Slightly stronger in evaluation exhaustiveness, but our paper has broader contributions (method + benchmark + evaluation flaw identification); comparable overall |
| Online GNN Evaluation | `KbetDM33YG.md` | 8.00 | R1 | Stronger: novel problem, theoretically grounded solution, tight focus; our paper is broader but less deep |

**Round 1 bracket**: 5.0–8.0. The paper is clearly above the 5.0–5.67 range (stronger contributions than Online Continual Graph Learning and CLDyB) and below the 8.0 anchor (less focused, simpler method).  
**Round 2 narrowing**: Compared to TiC-CLIP (6.25), our paper offers a method contribution and an evaluation insight that TiC-CLIP lacks, but TiC-CLIP has a larger-scale data contribution. Compared to Graph Pattern Comprehension (7.00), both are comprehensive LLM-graph benchmarks; ours adds a method and an evaluation flaw identification, though Graph Pattern Comprehension has more granular task-level analysis. The paper lands between these, closer to 7.00.

**Final score**: 6.5 — a solid paper with genuine contributions (evaluation flaw identification, benchmark, simple effective method) and well-supported claims. The main weakness (missing ablation) is addressable and does not undermine core results. The paper meets the bar for acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>