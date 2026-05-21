Now I have a solid calibration base. Let me construct the final review.

**Round 1 bracket**: The paper sits clearly above the weak anchors (<3.5) and is more competitive than the middle-band papers (3.5–7.5). The closest topical anchor is ProofBench (5.00), which is a significantly smaller version of essentially the same contribution. The current paper is much larger (5,062 vs 435 proofs), already open-sourced, has rigorous double-grading with 90.4% agreement reported, and yields substantially more findings. This places it well above 5.00. **Initial bracket: 5.5–7.5.**

**Round 2 narrowing**: Comparing against FATE (6.67), ProofOptimizer (6.50), and the 5.5-range papers, the OPC paper is a comparable contribution. It has minor empirical weaknesses (best-of-n sample size, human baseline not on the exact test set) but also has unusually thorough methodology (pilot phase, 90.4% inter-judge agreement, abstention options, double-grading, LLM issue summaries without bias). **Final score: 6.5** — solid Accept territory, comparable to or slightly better than the 6.5–6.67 anchors.

---

## Summary

This paper introduces the Open Proof Corpus (OPC), a dataset of over 5,000 human-judged proofs from six state-of-the-art LLMs across 1,010 competition-level mathematics problems (IMO Shortlist, Putnam, USAMO, etc.). The dataset is built through a rigorous annotation pipeline involving 13 expert judges (former IMO participants), with ~10% double-grading, a pilot phase, and 90.4% inter-judge agreement. Using the OPC, the paper resolves several open questions: (1) quantifies the gap between informal and formal proof generation (~4× on PutnamBench), (2) measures the discrepancy between final-answer accuracy and full proof correctness (o3 drops from 87.6% to 59.5%), (3) evaluates best-of-n selection strategies for proof quality, and (4) demonstrates that LLMs (GPT-5 at 89.3% accuracy) approach human-level proof judging. The paper also releases an open 8B judge model (OPC-R1-8B) that reaches 88.1% accuracy.

## Strengths

1. **Largest human-validated dataset of LLM-generated proofs by a wide margin** — At 5,062 proofs across 1,010 problems, the OPC is roughly 10× larger than prior efforts (Petrov et al. evaluated 6 problems; Mahdavi et al. reported <5% accuracy on a smaller set; ProofBench has 435 solutions). This scale enables statistical analyses that were previously infeasible.

2. **Quantifies the final-answer vs. proof correctness gap on an established benchmark** — Section 5.4 (Fig. 5) shows that on MathArena, o3 achieves 87.6% final-answer accuracy but only 59.5% proof correctness (a 28-point drop), while Gemini-2.5-Pro loses only 7 points (84.9% → 77.6%). This cleanly substantiates a claim that had only been asserted before.

3. **Direct comparison of informal vs. formal proof generation on a matched benchmark** — Section 5.3 shows Gemini-2.5-Pro solving ~83% of PutnamBench problems informally vs. <19% for the best formal prover (Goedel-Prover-V2), providing the first apples-to-apples quantification of this gap on a standard benchmark.

4. **Best-of-n ranking strategies improve proof quality** — Section 5.5 demonstrates that pairwise ranking methods (Rank Swiss: 40.0%) substantially outperform simpler selection methods (pass@1: 22.7%, Discrete: 31.5%) on the best-of-n subset, an underexplored direction for proof generation.

5. **Rigorous human evaluation pipeline** — Section 3 describes a carefully designed annotation process: former IMO participants as judges, a pilot phase with ~35% double-grading to calibrate instructions, optional abstention (<3% flagged), 90.4% inter-judge agreement from ~10% double-grading, LLM-generated issue summaries with demonstrated absence of bias. This exceeds typical annotation quality in prior proof datasets.

6. **Open-source release enables reproducibility and downstream use** — The OPC and OPC-R1-8B are publicly available (proofcorpus.ai, Hugging Face), unlike prior datasets (Mahdavi et al., Guo et al., 2025b) which were not open-sourced.

7. **Self-evaluation bias analysis** — Table 3 systematically documents that most models are worse at judging their own proofs (e.g., o3 drops from 83.1% on o4 proofs to 76.9% on its own), a concrete and useful finding.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core findings (informal-formal gap, final-answer vs. proof gap, relative model comparisons, best-of-n improvements) are well-supported by the data and rigorous methodology.

### Minor

1. **Human baseline for judge evaluation not measured on the exact test set** — The paper states that the 90.4% human baseline (Section 5.2) is computed on all double-graded proofs, while LLM judges are evaluated on the 293-proof test subset. The paper argues this "does not significantly affect the comparison" since test samples are uniformly drawn from the OPC, which is a reasonable claim. However, the claim that LLMs are "human-level judges" would be more definitive if the human baseline were measured on the same set. The paper should either report the human agreement on the test subset or show that the double-graded and test subsets have comparable difficulty.

2. **Adaptive sampling affects interpretation of absolute accuracy numbers** — During dataset construction, problem selection was adjusted to target roughly 50% model accuracy (Section 3.1). This means the 43% overall correctness and the per-model numbers in Fig. 3 reflect an engineered difficulty distribution, not unbiased estimates of performance on the competitions themselves. The paper partially acknowledges this in the Fig. 3 caption ("The second partition contains problems from more challenging competitions, explaining the score discrepancy"), but the main text does not carry a clear disclaimer that these absolute numbers are conditioned on the adaptive sampling. The relative comparisons across models remain valid, but readers could be misled about absolute capability levels.

3. **Best-of-n analysis rests on small sample sizes** — The core best-of-n result (Fig. 6a) uses 60 problems with full human judgments; the larger subset (Fig. 6b) has 134 problems, with 18 excluded due to a bug in the Rank (Swiss) implementation (acknowledged in a footnote). While the paper correctly notes that paired comparisons increase power, the conclusions would benefit from formal paired statistical tests (e.g., McNemar's or sign test) rather than relying on confidence intervals alone. This weakens what is otherwise an interesting finding about the superiority of ranking methods.

4. **Contamination analysis covers only one channel** — The experiment in Section 5.6 tests whether providing ground-truth solutions alongside proofs affects judging accuracy, showing minimal effect. However, this does not address contamination of the problems themselves (i.e., models may have seen the problems during training, which could help them reason better without needing the memorized solution). The paper acknowledges this ("it cannot be fully ruled out") and argues that the main conclusions are robust (e.g., the informal-formal gap is too large to be attributed to contamination), which is reasonable, but the claim that contamination is "insignificant" is over-broad.

### Trivial

1. The 5% individual judge error rate (Section 4) is derived assuming independent judge errors. If judges share systematic biases, this estimate could be optimistic. This is a minor technical note on a standard derivation.

2. The cost column in Table 2 is useful but it is unclear whether it reflects all API costs (prompt + output tokens) or is estimated. A brief clarification in the caption would help.

## Nice-to-Haves

- An analysis of inter-judge agreement broken down by problem difficulty or competition would strengthen trust in the 90.4% figure. If judges agree more on easier problems, the number may not be representative of the hardest proofs.
- A proof-generation fine-tuning experiment (e.g., SFT on correct OPC proofs) would demonstrate the dataset's value for training, not just evaluation. The authors note this as future work.

## Removed Points

These points were considered but removed for the reasons indicated:

- **Coordinator bias concern** (harsh critic): The coordinator is transparently described as both a core author and judge. The paper's double-grading, pilot phase, and monitoring procedures mitigate this concern. Removed as a non-issue given the described quality controls.
- **Missing proof generation training experiment** (harsh critic): This is scope creep — the paper's stated contributions are the dataset and the empirical findings it enables. Removed.
- **Strengths about "importance of problem"** (strength finder): Generic; strengths should be concrete. Already adequately covered by specific strengths above.

## Novel Insights

Beyond the paper's own contributions, the key insight that emerges from triangulating the reviews is that the OPC's two most methodologically questionable claims (human-level judge performance, best-of-n ranking superiority) are also the ones where the paper's evidence is thinnest. The core results that are most robust — the informal-formal gap (~4×), the final-answer vs. proof discrepancy (o3 drops 28 points), and the relative model ordering — rely on matched subsets and large effect sizes that no reviewer questioned. This asymmetry suggests a productive path for future work: the dataset is most valuable for large-effect comparisons that wash out small confounders, while the fine-grained claims about judging ability and selection strategies need tighter experimental designs before they can be considered settled.

## Suggestions

1. Measure the human baseline on the exact test set used for LLM judge evaluation (or show comparability).
2. Add an explicit disclaimer in §5.1 that the absolute accuracy numbers reflect the dataset's engineered difficulty distribution, not unbiased competition performance estimates.
3. Provide paired statistical tests (McNemar or sign test) for the best-of-n comparisons.
4. Clarify the "contamination is insignificant" claim to specify the channel tested and note that other forms of contamination are not ruled out.

## Score and Decision

**Anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| KyC7rqAcc4.md (Yu Tsumura) | 1.00 | R1 | Much weaker; single problematic example, no dataset contribution |
| 0MccwbLvgw.md (FMC autoformalization) | 3.33 | R1 | Weaker; smaller scope, different task |
| Urs8lNvMXB.md (MathTrap300) | 3.00 | R1 | Weaker; different task (unsolvability detection) |
| BEmwFslfoZ.md (ArgBench) | 3.33 | R1 | Weaker; smaller benchmark, different domain |
| JKILJjKKvt.md (Conjecturing) | 3.00 | R1 | Weaker; narrower scope |
| ky5iqwZSXI.md (ProofBench) | 5.00 | R1 | **Most comparable anchor.** Smaller dataset (435 vs 5,062 proofs), not opened during review, missing inter-annotator agreement. The OPC paper is clearly stronger. |
| 3tm37YNMdl.md (CUMath) | 4.67 | R1 | Weaker; undergraduate computational math, no proof-level human evaluation |
| T5dwUK8Rc9.md (Proof2Hybrid) | 4.00 | R1 | Weaker; synthetic benchmark, no human evaluation |
| o7avj3PWNC.md (BrokenMath) | 5.00 | R1 | Comparable quality but different focus (sycophancy); smaller dataset |
| 219Pn3D4Md.md (IMProofBench) | 4.00 | R1 | Weaker; smaller (54 problems), private, grader bias concerns |
| kHB5Te5IWm.md (DeepMath-103K) | 5.50 | R2 | Different focus (final-answer, not proofs); comparable quality |
| wCRZbspSZi.md (FormalML) | 5.50 | R2 | Different subfield (formal Lean subgoal completion) |
| KBknLdXxTa.md (CORE-MATH) | 5.50 | R2 | Different focus (contextual math, not proof generation) |
| 3bD19r4jqh.md (FATE) | 6.67 | R2 | Comparable quality; formal algebra benchmark with similar thoroughness |
| s9t2FJVsBH.md (ProofFlow) | 6.00 | R2 | Different contribution (autoformalization pipeline) |
| huptrb4JTa.md (ProofOptimizer) | 6.50 | R2 | Comparable quality; formal proof simplification, different contribution type |
| rhPnkTKfMy.md (Nemotron-CC-Math) | 7.33 | R2 | Higher-scored but different domain (pretraining corpus, not proof evaluation) |
| VwNzKPqBxk.md (ProfBench) | 6.50 | R2 | Comparable quality; multi-domain rubric benchmark |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>