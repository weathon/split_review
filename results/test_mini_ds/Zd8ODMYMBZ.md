Now I have strong calibration. Let me compile the final review.

**Round 1 bracket:** Based on the calibration search, this paper sits between the weak anchors (~3.0: Reward-RAG, TextEconomizer) and the strong anchors (8.0: Synthetic continued pretraining, Retrieval Head). The paper has a clear contribution and thorough experiments, placing it above the weak papers. It's not paradigm-shifting like the 8.0 papers, so the initial bracket is **4–7**.

**Round 2 narrowing:** Comparing against RECOMP (7.0), Provence (6.25), SuRe (6.4), and the Ensemble Decoding for LVLMs paper (6.0), FaviComp sits comfortably at **6.5**. It has a cleaner contribution and more thorough analysis than the 6.0 anchor, comparable rigor to RECOMP at 7.0 but with slightly less novelty (ensemble decoding is a known technique applied to a new problem). Final score: **6.5**.

---

## Summary

The paper proposes FaviComp, a training-free evidence compression method for RAG that uses ensemble decoding between a compression model and a target model. By interpolating the token logits of both models (controlled by a coefficient α), compressed evidence is made more "familiar" (lower perplexity) to the target model while also integrating the target model's parametric knowledge. Experiments on five open-domain QA datasets with three model pairs show consistent accuracy gains over strong baselines, with thoughtful ablations on the ensemble coefficient and a Hits-based analysis demonstrating how the method balances parametric and non-parametric knowledge.

## Strengths

- **Training-free and model-agnostic design.** The method requires no additional training and works with any compression/target model pair. Section 3.2 demonstrates this with three different pairs (Llama3.2-3B→Llama3-8B, Mistral-7B→Mixtral-8x7B, Mistral-7B→Mistral-7B), and the paper explicitly states it is "training-free" and "model-agnostic" (§2).

- **Clear and well-supported core hypothesis.** The paper identifies a real problem—compressed evidence being unfamiliar to the target model due to model mismatch—and proposes a principled solution (ensemble decoding to lower target-model perplexity). The α ablation (§4.2, Fig. 2) compellingly demonstrates the correlation between perplexity and accuracy for α ≤ 0.5, directly supporting the familiarity hypothesis.

- **Effective integration of parametric and non-parametric knowledge.** The Hits-based subset analysis (§4.3, Fig. 3) is the strongest piece of evidence. FaviComp outperforms both Zero-shot Summarization and the supervised CompAct on the Hits=0 (evidence-irrelevant) subset while matching them on Hits=1 (evidence-relevant). This cleanly demonstrates that the ensemble decoding enables the method to rely on parametric knowledge when evidence is missing—a key claimed advantage.

- **Thorough and well-designed experimental evaluation.** The evaluation covers 5 datasets, 3 target models, multiple baseline categories (no context, raw document, reranking, compression-based), and includes a thoughtful case study (§5, Table 2) that visualizes the token-level selection mechanism. The ablation across α values and the compression rate analysis add depth.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Imprecise framing of baseline equivalence.** The paper repeatedly states that "Zero-shot Summarization corresponds to FAVICOMP with α=0" and "Generated Context corresponds to FAVICOMP with α=1" (§3.3, §4.1). However, in the primary configuration (Llama3.2-3B→Llama3-8B), Zero-shot Summarization uses the *target model* (8B) as the compressor, while FaviComp with α=0 uses the *compression model* (3B). These are different models with different capabilities, so they are not equivalent. This framing issue does not invalidate results (if anything, it undersells FaviComp by comparing it against a stronger baseline), but it is imprecise and should be corrected with an explicit clarifying sentence.

- **No statistical significance or variance reported.** The main results (Tables 1 and 3) report single-run accuracy without confidence intervals, standard deviations, or significance tests. While the pattern across datasets and models is consistent, some improvements could be within noise—especially for smaller datasets like MuSiQue. Adding bootstrap confidence intervals or paired significance tests (e.g., McNemar) would strengthen the evidence.

### Trivial
None.

## Nice-to-Haves

- **Discussion of computational cost.** The method runs two LMs at each decoding step, increasing inference cost. A brief discussion of practical trade-offs (wall-clock time, cost relative to baselines) would improve the paper's utility.
- **Limitations section.** The paper lacks a dedicated limitations paragraph. The main limitations—increased computational cost, sensitivity to α, reliance on compression model quality—are worth acknowledging.
- **Generalization beyond open-domain QA.** The method is evaluated only on QA tasks. A simple experiment on one additional task (e.g., fact-checking) would broaden the impact.

## Removed Points

- **"Definition of ensemble decoding mechanism and α is missing from the main text."** — Removed because the mechanism *is* described in the main text (line 17–18: "we ensemble the token logits from both the compression and target models and then select the token with the highest probability from this combined set"). The formal definition in §2.3 was likely stripped by the parser. Even from the extracted text, the method is clear enough for reproduction.

## Novel Insights

The strength finder's hits-based analysis (§4.3) is the most insightful finding—it shows that supervised compression methods like CompAct can actually *hurt* performance on evidence-irrelevant subsets because their training biases them toward evidence utilization. FaviComp's unsupervised ensemble approach naturally avoids this pitfall. The perplexity-accuracy correlation analysis (§4.2) also provides a nuanced result: performance peaks at α=0.5 even though perplexity continues to drop beyond that, showing that perfect familiarity is not the goal. These are the paper's own contributions, not novel insights from the reviews.

## Suggestions

1. **Correct the α=0/α=1 equivalence framing.** Add a clarifying sentence noting that Zero-shot Summarization uses the target model as compressor (a stronger baseline) and that α=0 uses the actual compression model.
2. **Add statistical significance.** Report bootstrap confidence intervals or paired McNemar tests against the strongest baselines.
3. **Add a brief computational cost discussion** in a limitations paragraph or in the experimental settings.

## Score and Decision

**Round 1 bracket:** 4–7 (paper is clearly above weak papers like Reward-RAG at 3.0, clearly below paradigm-shifting papers like "Synthetic continued pretraining" at 8.0).

**Round 2 anchors compared:**
- **RECOMP** (avg 7.0, /home/wg25r/split_review/datasets/deepreview_13k_calibration/mlJLVigNHp.md): Trained compressors via knowledge distillation for RAG. FaviComp is comparable—both address evidence compression with thorough evaluation. FaviComp is training-free and has more insightful analysis (Hits subsets, perplexity curves), but RECOMP's training approach was more novel. FaviComp is slightly below RECOMP.
- **SuRe** (avg 6.4, /home/wg25r/split_review/datasets/deepreview_13k_calibration/w4DW6qkRmt.md): Prompt-based summarization for ODQA. FaviComp has a cleaner technical contribution and is at least as strong.
- **Provence** (avg 6.25, /home/wg25r/split_review/datasets/deepreview_13k_calibration/TDy5Ih78b4.md): Context pruning via sequence labeling. FaviComp is clearly stronger—more principled motivation, cleaner analysis.
- **Ensemble Decoding for LVLMs** (avg 6.0, /home/wg25r/split_review/datasets/deepreview_13k_calibration/ziw5bzg2NO.md): Training-free ensemble decoding for hallucination mitigation. FaviComp has more thorough analysis and fewer uncanny hyperparameters; it is stronger.
- **Reward-RAG** (avg 3.0, /home/wg25r/split_review/datasets/deepreview_13k_calibration/oqRe1KvD17.md): Weak paper with unclear contribution. FaviComp is substantially stronger.

**Final score:** 6.5. The paper has a clean, well-motivated idea, thorough experiments, and bounded (minor) weaknesses. It falls between SuRe/Provence (6.25–6.4) and RECOMP (7.0), closer to the upper end.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>