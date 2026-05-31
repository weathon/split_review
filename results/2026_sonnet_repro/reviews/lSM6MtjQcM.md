Now let me run the calibration searches.Round 1 bracket: **5.0 to 7.0**. AetherCode compares favorably to LiveCodeBench (6.25) in methodology depth and problem quality, but has notable gaps in empirical validation of its core claims. Let me narrow within this bracket.Now I have enough anchors to write the review. My round-2 anchors cluster at 5.75–6.25 for similar benchmark/dataset papers (LiveCodeBench, ENAMEL, SWE-bench). AetherCode has stronger problem sources and more rigorous test case methodology than LiveCodeBench, but is held back by the unsupported LLM-human gap claim (no human baseline), the overstated quality guarantee, and the difficulty rating inconsistency. I'll place it at **5.5**.

---

## Summary

AetherCode is a competitive-programming benchmark that sources 456 problems (400 from 2024, 56 from 2025) exclusively from premier worldwide competitions—IOI, ICPC, NOI, USACO—rather than online judge platforms. Its primary methodological contribution is a hybrid test-case construction pipeline (G-V Agent System + 67 competitive programming experts including gold medalists) validated against a corpus of 30,000+ human submissions, achieving 100% TPR and 100% TNR on that solution set. An evaluation of 17 reasoning and non-reasoning LLMs reveals that even the best current models solve only ~35% of problems, and the paper provides fine-grained failure analysis across 10 algorithm categories.

---

## Strengths

- **Premier competition source differentiation**: AetherCode is the first benchmark to systematically collect *recent* problems (2024–2025) from premier worldwide competitions (IOI, ICPC, NOI, USACO), providing a genuinely different and harder problem distribution than online-judge-based benchmarks. The 456-problem dataset spans 10 major categories and 144 subcategory tags, enabling fine-grained evaluation not available elsewhere.

- **Rigorous TPR/TNR quality framework**: The paper introduces a principled test-case quality assessment methodology (Section 2.3.1, Equations 1–2) that frames the test suite as a binary classifier and measures it against a 30,000+ submission corpus. This is a methodological step forward over existing benchmarks that rely on random mutation or minimal handcrafted tests, and is supported by 67 expert annotators (including ICPC gold medalists) and a dedicated expert audit team.

- **Comprehensive model evaluation with failure analysis**: The evaluation of 17 models (11 reasoning, 6 non-reasoning) across difficulty tiers, algorithmic categories, and Pass@{1,2,4} is thorough. The failure diagnosis in Section 3.3—particularly the observation that Claude models generate correct-but-inefficient algorithms at a far higher rate than other models, producing TLE at roughly equal rates to WA—is a genuinely informative finding only detectable on a benchmark of this difficulty.

---

## Weaknesses

### Fatal
None.

### Major

- **No human performance baseline for the central LLM-human gap claim**: The paper's title and abstract center on the claim that "a significant gap still exists between the performance of LLMs and top-tier human competitors." Yet Section 3 contains zero systematic human performance statistics on AetherCode. The metadata already collected (Section 2.1: "human contestant performance data," contest leaderboards, Extreme problems defined as those no contestant solved) would permit at minimum a per-difficulty solve rate for human contestants, which would directly substantiate the headline claim. The only indirect evidence is the existence of the "Extreme" tier (20 problems, ~0% LLM solve rate) and the ~35% top-model Pass@1. As written, the gap claim rests on intuition rather than a demonstrated comparison, which is a significant mismatch between the paper's framing and its evidence.

- **Quality guarantee overstated in the abstract**: Section 2.3.1 is explicit and correct: "we have achieved a 100% TPR and 100% TNR on *our collected solution set*." The conclusion, however, states this "guarantees exceptional accuracy and reliability in evaluation" with no qualifier. This is an overgeneralization—the guarantee holds over a closed corpus of human-written submissions, many of which were the direct targets of the expert-constructed test cases. Whether this test suite correctly classifies novel LLM-generated solutions with qualitatively different failure modes (e.g., subtle algorithmic variants not represented in the human submission pool) is unverified and never discussed as a limitation. The paper acknowledges a related concern for problems with fewer than 50 incorrect solutions (Section 2.3.3) but does not address the general case. This needs a clear scope qualification in the abstract and conclusion.

### Minor

- **Difficulty rating inconsistency in Table 1**: AetherCode is self-rated ★★★ in Table 1, identical to APPS and LiveCodeBench (LeetCode/AtCoder-sourced), while CodeELO and LiveCodeBench Pro (CodeForces-sourced, which the paper argues are *inferior* in difficulty) are rated ★★★★. The paper simultaneously argues that IOI/ICPC problems represent a higher challenge tier and that CodeForces problems are limited by contest-design constraints—yet the self-assignment of a lower difficulty star rating is left without explanation. The actual Pass@1 data (~35% for the best model) suggests AetherCode is at least as hard as CodeForces benchmarks.

- **Decontamination methodology undescribed**: Section 2.1 states that contest dates are collected "for decontamination purposes" but no decontamination procedure is described in the main text. Given that IOI 2024 and ICPC 2024 problems are publicly available and could plausibly appear in training corpora of models trained through early-to-mid 2025, a summary of what decontamination was actually performed (or at least a statement that it is detailed in a stripped appendix) is needed in the main body.

### Trivial

- The 2024–2025 split in Table 3 (400 vs. 56 problems) and Figure 2 category counts are worth contextualizing: small categories (Tree: 24 problems, Geo: 36 problems) mean individual category-level Pass@1 differences can be driven by a handful of problems. No variance estimates are reported for category-level comparisons in Table 4.

---

## Nice-to-Haves

- **Empirical demonstration of test-case superiority**: The paper argues by design reasoning that AetherCode's test cases are more rigorous than prior benchmarks'. A direct comparison—running a set of known-incorrect LLM solutions through AetherCode's test suite vs. a naive mutation suite, and measuring false-negative rates—would transform the argument from theoretical to empirical and substantially strengthen the paper's core thesis.

- **Per-category difficulty distribution analysis**: Table 4 shows Tree problems score close to zero for most models, but this may reflect the difficulty distribution within that category rather than tree-specific LLM weakness. The paper notes this concern (Section 3.2) but does not investigate it—a brief per-category difficulty breakdown would help distinguish capability gaps from distributional artifacts.

- **Evaluation protocol detail**: The main text does not specify prompt structure (whether problems are given verbatim with LaTeX+Markdown, whether time/memory limits are included) or required programming language. These choices bear on interpreting TLE failure rates and on reproducibility. Given that the paper describes problems requiring complete programs vs. function stubs, this matters more than in simpler benchmarks.

---

## Removed Points

*These points were flagged for removal — treat them with caution.*

- **Harsh Critic: G-V Agent System not a novel contribution** — Removed (strawman). The paper explicitly credits Wang et al. (2025b) for the G-V Agent System in Section 2.3.2: "We employed the Generator-Validator (G-V) Agent System (Wang et al., 2025b)." No claim of novelty is made. The added human-in-the-loop step is the paper's own contribution.

- **Harsh Critic: The paper does not show existing benchmarks "overstate model proficiency" comparatively** — Demoted to Nice-to-Have. While a direct cross-benchmark comparison would be compelling, the paper's primary contribution is the benchmark itself, not a meta-analysis of prior benchmarks. The claim is reasonable given design reasoning.

- **Harsh Critic: Proportion of USACO problems with official test cases vs. pipeline test cases** — Removed as a major weakness; kept as a minor concern embedded in the quality guarantee discussion. The paper does note USACO releases official test cases (Section 2.1) and the quality standard is applied uniformly. Not stating the exact proportion is a transparency gap but does not undermine the benchmark.

- **Strength Finder: "First benchmark to set such a high standard for test cases"** — Partially removed from strengths as generic/overclaimed. The TPR/TNR framework is a concrete strength but "unprecedented" is not verifiable without external literature access; replaced with a concrete characterization of what makes it methodologically distinct.

- **Harsh Critic: Category-level variance as a "significant" concern** — Kept but demoted to Trivial. The paper itself notes this caveat (Section 3.2: "individual categories such as Tree may happen to be particularly difficult"). It is worth noting but not a structural flaw.

---

## Novel Insights

The observation that Claude-series models exhibit a qualitatively distinct failure mode on hard competitive programming problems—generating algorithmically correct but computationally inefficient solutions (roughly equal WA and TLE rates) rather than the 70–80% WA rate seen in other models—is a genuinely novel empirical finding. This failure mode cannot be identified on easier benchmarks where time limits are not binding. It suggests that future training and evaluation for Claude-type models should focus not just on algorithmic correctness but on solution efficiency, and that TLE should be treated as a first-class diagnostic signal rather than an implementation artifact. The TPR/TNR framing of test-suite quality as a binary classifier against a submission corpus is also a conceptually clean contribution that could be adopted as a standard in future benchmark papers.

---

## Suggestions

1. **Add human solve-rate statistics from contest metadata**: The leaderboard data already collected can provide, at minimum, median and top-decile human solve rates per difficulty tier. Present this alongside LLM Pass@1 in Table 3 to substantiate the LLM-human gap claim directly.

2. **Scope-qualify the 100% TPR/TNR claim**: Add a sentence in the abstract and conclusion clarifying that the guarantee holds over the curated 30,000+ human-solution corpus. Acknowledge (even briefly) that LLM-generated solutions may exhibit failure modes not represented in that corpus.

3. **Reconcile the difficulty star rating in Table 1**: Either revise to ★★★★ with a brief justification, or add a footnote explaining why AetherCode's difficulty is rated lower than CodeForces benchmarks despite the argument that it is harder in practice.

4. **Describe decontamination in the main text**: Even a two-sentence summary of what procedure was used (e.g., "Problems from contests after [date X] are treated as contamination-safe for models with training cutoff [date Y]") would satisfy this gap.

5. **Report confidence intervals or standard deviations for small-category comparisons**: For Tree (24 problems) and Geo (36 problems), bootstrap confidence intervals would help readers interpret Table 4.

---

## Score Calibration

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| chfJJYC3iL.md (LiveCodeBench) | 6.25 | R1/R2 | Most directly comparable; AetherCode has stronger test-case methodology and harder problem sources, but weaker empirical support for central claims |
| suz4utPr9Y.md (ENAMEL) | 5.75 | R1/R2 | Similar benchmark rigor; ENAMEL introduces a novel metric (eff@k); AetherCode broader in scope but weaker in claim support |
| VTF8yNQM66.md (SWE-bench) | 6.25 | R2 | Strong problem source differentiation and community impact; AetherCode comparable in ambition |
| 7o6SG5gVev.md (TestGenEval) | 6.25 | R2 | Benchmark paper with similar evaluation depth |
| fjEZ2LPceZ.md (CS-Bench) | 6.75 | R1 | Broader scope (26 CS subfields), bilingual; not directly comparable |
| NlY3XppPt3.md | 2.00 | R1 | Much weaker: toy problem setting with no real benchmark infrastructure |
| BltaWJZMeR.md (DataSciBench) | 3.20 | R1 | Less rigorous methodology |
| DZBFchnM3b.md | 3.67 | R1 | Narrow benchmark, weaker execution |
| upzyG4wRBr.md | 5.80 | R2 | Visual programming benchmark; less rigorous than AetherCode |

**Round 1 bracket:** 5.0–7.0  
**Round 2 narrowing:** Round-2 anchors cluster at 5.75–6.25. AetherCode's test-case methodology and problem sources are genuinely superior to LiveCodeBench, but its central claim (LLM-human gap) is less empirically grounded than LiveCodeBench's contamination analysis, and it does not demonstrate superiority over existing benchmarks empirically. This places it slightly below the 6.25 cluster.

**Final score: 5.5** — The benchmark is a real and useful community contribution, with principled methodology and comprehensive evaluation. It is held back by a central framing claim (LLM-human gap) that lacks direct empirical support, and by overstating the scope of the quality guarantee. These are fixable with revision but are substantive enough to pull the paper below the 6.25 anchor cluster.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>