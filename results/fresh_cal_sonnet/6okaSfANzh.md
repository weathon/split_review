Now I have a clear picture of the paper. Let me perform calibration searches to anchor my score.Initial bracket: **4–6.** The paper has a genuine contribution and solid experiments, but notable structural problems (duplicate sections, incomplete text). Let me narrow within this range.Now I have sufficient calibration. My final bracket: **4.5–5.5**. The paper has a genuine, novel contribution (MoT + cross-representation consistency for cascades) but suffers from a real structural duplication (Sections 2 and 3). Let me now write the full review.

---

## Summary

This paper proposes training-free LLM cascade pipelines for cost-efficient reasoning, where a weaker (GPT-3.5-turbo) and stronger (GPT-4) LLM are chained, and routing decisions are made by checking the answer consistency of the weaker LLM across multiple samples. The core novelty is leveraging a **Mixture of Thought (MoT)** representations — combining Chain-of-Thought and Program-of-Thought samples — as a diversity signal that better separates "easy" from "hard" questions. Experiments across six reasoning datasets show that MoT cascade variants achieve ≈93% of GPT-4-CoT-SC accuracy at 40% of its cost.

---

## Strengths

1. **Empirically validated cost reduction with minimal accuracy loss**: Section 4.1 reports that MoT cascade variants achieve ~0.929 average accuracy vs. GPT-4-CoT-SC's 0.931, at 40% of GPT-4-CoT-SC's cost. On CREPE they even surpass GPT-4-CoT-SC (0.885 vs. 0.871) at 47% of cost. This directly substantiates the central claim.

2. **Principled mechanistic explanation for MoT superiority**: Section 4.2 (MoT analysis + Figure 4) shows that when CoT makes a mistake on a hard question, a second CoT set with different demonstrations often makes the *same* mistake (high consistency → wrong routing), whereas PoT makes a *different* mistake (low consistency → correct routing to GPT-4). This explains *why* mixing representations widens the easy-vs.-hard consistency gap better than diversifying demonstrations alone.

3. **Training-free approach that outperforms fine-tuned external verifiers**: Section 4.4 shows that on GSM8k, fine-tuned RoBERTa and prompted GPT-3.5 verifiers top out at 0.892 accuracy, well below the proposed approach's 0.951 and GPT-4's 0.958. This comparison fairly establishes that consistency-based routing is more effective than text-based verifier routing for complex reasoning.

4. **Robustness analysis**: Section 4.3 shows MoT-1D-Vote consistently outperforms CoT-2D-Vote when temperature is varied (0.4→0.8) and sample size is varied (K=20→40), establishing that the MoT advantage is not brittle to hyperparameters.

---

## Weaknesses

### Fatal
None — the core scientific claims are supported by the experimental results.

### Major

- **Structural duplication between Sections 2 and 3**: Section 2 ("LLM Cascades for Cost-Efficient Reasoning") introduces the cascade formalism using notation $LLM^w / LLM^s$, defines vote-based and verification-based decision-makers in Equations 1–2, and enumerates all ten approaches. Section 3 ("Economical Workflow of Multiple LLMs") restarts from scratch with different notation ($LM_w / LM_s$), re-introduces the same vote-based method (as "Method A", Eq. 2) and verification method (as "Method B", Eq. 3), and re-presents the same ten prompt/approach combinations in a separate figure. The two sections cover the same ground without cross-referencing or building on each other; the paper was clearly assembled from two separately-written drafts that were never merged. This creates genuine confusion about which formalism is authoritative and significantly harms readability. A reviewer encountering this would reasonably view the submission as editorially incomplete.

- **LLAMA2-13B experiment contributes no quantitative results**: Section 4.5 ("How weak can the weaker LLM be?") concludes qualitatively that LLAMA2-13B works on DATE but fails on GSM8k and CREPE. No accuracy numbers, cost figures, or consistency-score distributions are reported. This is a practically important design parameter, and the section as written offers no verifiable evidence on which to base design decisions about weaker LLM selection.

### Minor

- **Cost baseline anchored to GPT-4-CoT-SC (3 calls) throughout**: All relative cost figures — including the headline "40% of the cost of GPT-4" in the abstract — are normalized against GPT-4-CoT-SC, which uses K=3 sampling calls. A practitioner choosing between the cascade and plain GPT-4 would more naturally compare against GPT-4-CoT-Greedy (a single call). The paper includes GPT-4-CoT-Greedy as an accuracy reference point but never as a cost denominator. The absolute cost advantage relative to the greedy single-call baseline is smaller, since the cascade still pays for ~20 GPT-3.5 samples per question. A single-sentence accounting against the greedy baseline would make the claim more credible.

- **Section on "easy vs. hard" routing lacks a direct confusion matrix**: The MoT advantage is argued via aggregate accuracy-cost curves across the whole Pareto frontier, which entangles routing quality with downstream accuracy. A per-question confusion matrix over {easy/hard} × {routed to weak/strong} for MoT-1D-Vote vs. CoT-2D-Vote would isolate the routing decision quality and make the mechanistic argument in Section 4.2 directly legible.

### Trivial
None worth noting beyond the structural issues already raised.

---

## Nice-to-Haves

- A brief sensitivity analysis on the quality of the second annotation set (used in all 2D variants) would be useful; the paper notes it is "randomly sampled from training data and manually annotated" (Section 4.1) but provides no guidance on what makes a good second set.
- The paper's finding that increasing K from 20 to 40 costs more without improving routing quality is stated but unexplained. Intuitively, more samples should sharpen confidence estimates; at minimum, a brief mechanistic note on why saturation occurs would help practitioners choose K.
- Adding at least one factual-task result to the generalization experiment (currently cut off) would clarify the boundary conditions of the approach.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **Mid-sentence cuts in Section 4.5 and the Reproducibility Statement**: The harsh critic flags "We also explored whether our method can be generalized to factual-based reasoning tasks in" and the truncated Reproducibility Statement as evidence of missing content. Per the hard rules, the parser strips appendix text and trailing URLs; these cuts are likely parser artifacts pointing to a dataset name or GitHub link, not intentional omissions by the authors. Removed.

- **Verification-based comparison information asymmetry**: The critic notes that the external verifiers see only Q+A text, not multiple reasoning traces. This is acknowledged by the paper's framing (Section 4.4: "deciding question difficulty and answer correctness solely based on their textual descriptions") and is precisely the point of the comparison — demonstrating that consistency-based methods are more effective. Not a weakness.

- **Request for error variance/confidence intervals across runs**: The cascade uses stochastic sampling; the harsh critic requests multi-run variance. Single-run evaluation over large test sets is standard in this community, and the paper reports actual token costs, not estimated ones. Moved to nice-to-have.

- **Strength: "this paper addresses an important problem"** — generic; removed. The concrete performance claims (strength 1–4 above) are retained.

---

## Novel Insights

The most genuinely novel mechanistic observation in this paper is that CoT and PoT *fail in structurally different ways* on hard questions: CoT under alternative demonstrations tends to repeat the same wrong answer (high consistency → bad routing), whereas PoT generates a different wrong answer (low consistency → correct routing to GPT-4). This asymmetric failure structure is what makes cross-representation diversity more powerful than same-representation demonstration diversity as a routing signal. The paper captures this insight in Figure 4 but does not elevate it to a principle. If generalized, it implies that any two reasoning methods with *low cross-error correlation* would be effective cascade partners, which is a testable and useful design criterion for future cascade systems.

---

## Suggestions

1. **Merge Sections 2 and 3 into one**: Keep the cleaner formalism from Section 2 ($LLM^w$/$LLM^s$) and integrate the task-formulation material from Section 3.1 as a brief problem statement at the start. Remove duplicate equations and figures.
2. **Add numbers to the LLAMA2-13B experiment**: At minimum, report accuracy and cost for DATE (where it "still works") and one failed dataset (GSM8k or CREPE) so the failure mode is quantified.
3. **Report cost relative to GPT-4-CoT-Greedy** in addition to GPT-4-CoT-SC — even one row in a table or a brief parenthetical calculation would make the cost claim more honest.
4. **Promote the cross-error-correlation insight** as a general principle and test it explicitly (e.g., compute the Jaccard overlap of wrong-answer sets between CoT and PoT across datasets).

---

## Score Calibration

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| BjZP3fTlVg (HCMA) | 3.0 | 1 | Weaker approach, less clear contribution |
| rgDwRdMwoS (Unified Routing/Cascading) | 5.2 | 1 | Similar domain, similar level of novelty, but no structural duplication |
| 8sSqNntaMr (RouteLLM) | 6.33 | 1 | Better-polished paper, learning-based router with clear contribution |
| KgaBScZ4VI (Token-Level Cascades) | 7.0 | 1 | Cleaner theory and presentation, no structural issues |
| UHPnqSTBPO (Trust or Escalate) | 8.0 | 1 | Stronger theoretical guarantees, provable human agreement |

**Round 1 bracket:** 4–6.

**Round 2 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| LyNsMNNLjY (LLM Routing with Benchmarks) | 4.25 | 2 | Weaker novelty, less mechanistic analysis; paper under review is stronger |
| 60rQpnbgmE (Confidence Estimation for LLM Reasoning) | 4.25 | 2 | Similar topic, rejected; comparable issues but no structural duplication |
| wk77w7DG1N (Generation Consistency) | 4.67 | 2 | Rejected; similar domain, less empirical coverage |
| kN25ggeq1J (Code Reasoning) | 5.67 | 2 | Accepted; clean contribution, comparable in depth |
| rgDwRdMwoS (Unified Cascades) | 5.2 | 2 | Solid novelty, clean structure; paper under review has more novel idea but structural duplication |

**Narrowing:** The paper under review is stronger than the 4.25–4.67 cluster (better novelty and empirical coverage across 6 datasets), roughly comparable to the 5.2 anchor (rgDwRdMwoS) in terms of contribution quality, but with worse editorial organization due to the Sections 2/3 duplication. The 5.67 accepted anchor (kN25ggeq1J) is cleaner and better-integrated. The paper lands **just below** the 5.2 anchor given the additional structural burden.

**Final score: 5.0**

---

**Originality:** Moderate-high. The idea of using cross-representation (CoT+PoT) consistency as a cascade routing signal is genuinely novel and well-motivated.  
**Importance:** The research question (cost-efficient LLM usage for reasoning) is practically significant and timely.  
**Claim support:** The central accuracy-cost claim is well-supported across 6 datasets. The LLAMA2 boundary analysis is unsupported quantitatively.  
**Soundness:** Experiments are generally sound; the cost-comparable configuration is reasonable but approximate.  
**Clarity:** Severely harmed by the duplicate Sections 2/3; otherwise clear.  
**Value to community:** Positive — the MoT diversity principle and the training-free approach are both directly usable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>