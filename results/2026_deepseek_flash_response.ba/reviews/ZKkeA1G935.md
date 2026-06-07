Now I have enough context for calibration. Let me finalize the review.

## Summary

This paper identifies task ID leakage in the local-testing evaluation protocol for graph continual learning (GCL), demonstrating convincingly that even an MLP with mean pooling achieves 100% task ID accuracy and 0% forgetting under this protocol. It then introduces LLM4GCL, a benchmark evaluating 9 LLM/GLM-based methods across 7 text-attributed graph datasets under a corrected global-testing protocol, and proposes SimGCL, which combines single-session instruction tuning (via ego-graph prompts + LoRA) with training-free prototype classification.

## Strengths

- **Task ID leakage diagnosis (Section 3.1, Table 1).** The paper shows that under the local-testing protocol used by prior GCL works, even a trivial MLP with mean pooling achieves 100% task ID accuracy and 0% forgetting across all seven datasets — matching the previous SOTA method TPP. This is a clean, reproducible, and important finding that calls into question the validity of evaluation in prior GCL work. The demonstration is concise and convincing.

- **Diagnosis of why GLMs underperform pure LLMs in GCL (Obs. ❸).** The paper provides evidence that deliberately designed GLMs (GraphPrompter, GraphGPT, LLaGA, ENGINE) consistently underperform SimpleCIL (a pure LLM baseline), and offers a reasoned explanation: LLM-as-Enhancer methods inherit the GNN bottleneck and overfit, while LLM-as-Predictor methods suffer cross-architecture representation misalignment. This is a concrete empirical finding with practical implications.

- **Controlled ablation across session configurations (Table 4).** By varying class size and session count on Arxiv, the paper shows that prototype-based methods (SimGCL, SimpleCIL, Cosine) maintain stable performance as sessions increase, while non-prototype methods degrade sharply. This cleanly isolates the robustness advantage of training-free prototype classification.

- **Scalability analysis (Figure 3).** Demonstrates that increasing LLM backbone size consistently improves GCL performance for both SimpleCIL and SimGCL, providing practical guidance for practitioners.

## Weaknesses

### Major

- **Claim that SimGCL "surpasses all existing baselines" is contradicted by the paper's own results.** The contribution list (line 30) states SimGCL "is able to surpass all existing baselines," and Obs. ⑧ asserts it "consistently overperform[s]" other baselines (23 out of 28). However, on Arxiv-23 in the NCIL scenario (Table 2), SimpleCIL achieves $\bar{\mathcal{A}}=52.4,\ \mathcal{A}_N=38.8$ while SimGCL achieves $\bar{\mathcal{A}}=38.7,\ \mathcal{A}_N=13.6$ — a gap of 13.7 points in average accuracy and 25.2 points in final accuracy. In FSNCIL (Table 3), SimpleCIL similarly beats SimGCL on Arxiv-23 ($49.8/40.0$ vs. $31.8/10.3$) and on Arxiv ($46.4/36.6$ vs. $36.3/6.8$). A claim of "surpassing all baselines" is not sustainable when a baseline (SimpleCIL) is the clear winner on Arxiv-23 and competitive on several other datasets. The abstract's more careful wording ("surpasses the previous state-of-the-art GNN-based baseline under the rehearsal-free constraint") is more accurate, but the contribution list and Obs. ⑧ overstate the case. This internal inconsistency undermines credibility.

- **No variance or statistical significance is reported anywhere.** All results in Tables 2, 3, and 4 are single numbers with no standard deviations, confidence intervals, or number of random seeds. For a benchmark paper whose purpose is to enable fair comparison between methods, this is a structural gap. The reader cannot tell whether reported differences (e.g., SimGCL's 73.5 vs. SimpleCIL's 71.4 on WikiCS) are meaningful or within noise. This is especially problematic for interpreting claims about which method "consistently" outperforms others, and for the FSNCIL setting where small sample sizes inflate variance.

### Minor

- **Observation numbering is garbled.** The paper jumps from Obs. ④ to Obs. ⑥ (missing ❺), then uses ⑧ for one observation and "Obs. 7" and "Obs. 8" (Arabic numerals) for two subsequent observations. This creates confusion and suggests an editing error.

- **The task ID leakage critique is under-developed as a standalone contribution.** The demonstration that local testing is flawed (Table 1) is the paper's most original finding, but it occupies only about one page of the main text. The paper does not trace how many prior GCL papers' reported results are affected, nor does it validate that the proposed global-testing protocol is itself "realistic" beyond assertion (line 70: "better reflects real-world scenarios"). Real-world deployment could involve either setting depending on the application; a clearer argument for why global testing is the right default would strengthen the paper.

- **SimGCL's novelty is modest.** The method combines existing techniques (LoRA fine-tuning only on the first session + frozen backbone + prototype-based cosine similarity classification) in a standard way. This is fine for a benchmark paper where the method serves as a strong baseline, but the paper frames it as a "model design" contribution (line 30) and claims it "surpasses the current SOTA models," when the key design choices (first-session-only training + prototypes) are inherited from SimpleCIL. The only real addition is the ego-graph prompt template. The paper would be more credible if it presented SimGCL as a simple but competitive baseline.

### Trivial

- **"B-large (439M)" in Figure 3 is non-standard.** Standard BERT-large has ~340M parameters and BERT-base has ~110M. The reported sizes (B-small 29.1M, B-medium 41.7M, B-large 439M) do not match standard BERT variants. RoBERTa-large at 355M is correct. This needs clarification (though it may be addressed in the removed appendix).

## Nice-to-Haves

- Adding an oracle upper bound (joint training on all tasks) would help contextualize how much performance drop is due to forgetting vs. task difficulty.
- A focused analysis of why SimGCL fails on Arxiv-23 (the paper attributes it to sparse graph structure but does not investigate systematically) would strengthen the understanding of the method's boundaries.

## Removed Points

The following points from the inputs were filtered:

- **TPP as a baseline should be removed** — TPP is included appropriately to demonstrate what happens when a local-testing method is exposed to global testing. This is informative, not a flaw.
- **Missing oracle upper bound** — A standard nice-to-have, not a weakness. Every CL paper could include this.
- **Hyperparameter sensitivity opaque** — The removed appendix likely contains these details. Cannot verify.
- **"SimpleCIL is a CV method not designed for GCL" concern** — The paper explicitly acknowledges SimpleCIL as a relevant baseline. Its strong performance is a finding, not a flaw.
- **Missing analysis of when SimGCL fails** — This is a scope-expanding suggestion, not a required analysis for the paper's core claims.
- **Grammar/style/formatting nitpicks** — These are parser artifacts, not author errors.
- **Strength Finder generic strengths** — Several strengths were too generic ("important problem," "timely topic") and were removed as unsubstantiated.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface observations about the work that go significantly beyond what the paper itself states.

## Suggestions

1. **Tone down claims about SimGCL.** Replace "surpasses all existing baselines" with honest, dataset-by-dataset descriptions. Acknowledge that SimpleCIL is a strong competitor that outperforms SimGCL on Arxiv-23. This will make the paper more credible.
2. **Add variance estimates.** Report results over at least 3 random seeds with standard deviations, especially for the benchmark results that are the paper's main contribution.
3. **Center the task ID leakage critique as the primary contribution.** Move it earlier and develop it further — estimate how many prior GCL papers are affected by this flaw.
4. **Fix the observation numbering** and clarify the BERT model sizes in Figure 3.

## Score and Decision

**Round 1 bracket**: (4.0, 6.0). The paper was compared against:
- "Online Continual Graph Learning" (avg 5.0, Reject) — similar domain, fewer impactful findings.
- "CLDyB" (avg 5.67, Accept) — benchmark for CL with PTMs, stronger methodological contribution.
- "TiC-LM" (avg 6.25, Reject) — larger-scale benchmark with less novel insight.
- "Is multitask learning all you need in CL?" (avg 5.75, Reject) — analytical contribution with limitations.
- "Towards Graph Foundation Models" (avg 5.25, Reject) — graph foundation model paper.

**Round 2 narrowing**: Anchors in the (4.0, 6.0) and (5.0, 7.0) bands confirmed the paper sits near the lower end of its bracket. The paper's core finding (task ID leakage) is genuinely valuable and stronger than the OCGL paper (5.0), but the overclaiming about SimGCL and lack of statistical rigor are more significant than the issues in the CLDyB paper (5.67). The paper is weaker than the TiC-LM benchmark (6.25) in scale and rigor.

**Final calibration**: The paper is comparable to the OCGL paper (5.0) in overall quality — both have a useful problem formulation but significant execution issues. The task ID leakage finding gives this paper an edge, but the overclaiming problem cancels that advantage out. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>