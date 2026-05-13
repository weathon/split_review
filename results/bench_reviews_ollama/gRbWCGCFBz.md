Now I have a thorough understanding of the paper. Let me carefully synthesize the review by verifying the key claims from the harsh critic against the paper.

## Summary

ToolBridge introduces an open-source dataset of 178,023 entries for training LLMs to use external tools (primarily Python code execution). The paper documents a pipeline that selects valuable entries from 25 open-source SFT datasets, uses GPT-4o-mini to insert Python tool calls, and filters based on consistency between code execution results and subsequent text. Experiments show that LLaMA models fine-tuned on ToolBridge improve on standard benchmarks (GSM8k, GSM Plus, MathBench*, Stanford WebQA) and custom benchmarks (RandomQA, FACT), with an ablation (ToolBridge§: tool calls removed) isolating the tool-specific contribution.

## Strengths

- **Open-source dataset with transparent construction pipeline**: The paper provides detailed documentation of each pipeline stage—selection (Section 3.1–3.2), conversion (Section 3.3), and consistency filtering (Section 3.4)—including attrition analysis (10M → 1.5M → 365K → 178K) with transparent breakdowns of why entries fail at each stage. This addresses a real gap in the literature where prior work (GPT-4o, Llama 3.1) keeps training data proprietary (lines 24–28, 72).

- **Consistency validation step (Section 3.4)**: The paper identifies and addresses a concrete failure mode—that GPT-4o-mini sometimes generates code whose execution results contradict the subsequent text—and proposes a targeted filtering step that retains 48.8% of converted entries. Example outputs in the paper demonstrate that models SFT on filtered vs. unfiltered data behave differently during inference (line 282–288).

- **Ablation design with ToolBridge§**: The comparison between base models, ToolBridge§ (tool invocations removed), and full ToolBridge directly quantifies the incremental contribution of tool-use data. Across all four standard benchmarks, full ToolBridge consistently outperforms ToolBridge§ (e.g., GSM Plus: 37.8 → 40.0, MathBench*: 35.2 → 37.4), confirming that tool-use data provides benefits beyond general SFT.

- **Diversity of tool usage captured**: Table 6 (line 328–348) documents 62 distinct Python packages across 183,147 tool invocations, with domain-appropriate variation (School Math uses 8 libraries; TigerBot uses 40), demonstrating the dataset captures non-trivial tool diversity.

## Weaknesses

### Fatal
None.

### Major

- **Dataset composition overwhelmingly favors math, undermining breadth claims**: School Math 0.25M accounts for 100,836 of 178,023 entries (56.7%) and OpenOrca accounts for 46,449 (26.1%). Together, these two sources constitute 82.5% of ToolBridge (Table 4, lines 294–310). The paper's title and framing position ToolBridge as equipping LLMs with "external tool capabilities" broadly (lines 7–9), and the abstract claims three capability areas: "data processing, numerical computation, and factual retrieval." Yet the dataset is essentially a math-coded dataset with sporadic general tool use. The experimental improvements on standard benchmarks are almost entirely on math benchmarks (GSM8k, GSM Plus, MathBench*), and the one non-math benchmark (Stanford WebQA) shows a confounded result (see next weakness). This mismatch between claims and dataset composition significantly undermines the paper's broader claims about equipping LLMs with general tool-use capabilities.

- **Ablation reveals that SFT effect dominates tool effect on key benchmarks, undermining causal attribution**: On Stanford WebQA (Table 4, lines 409–414), base Llama3-8B scores 21.2, ToolBridge§ scores 37.7 (+16.5 from SFT without tools), and full ToolBridge scores 39.9 (+2.2 from tool integration). The 16.5-point gain from SFT on data *without tool calls* versus the 2.2-point gain from actual tool invocation makes it impossible to attribute the Stanford WebQA improvement primarily to tool-use learning. On GSM8k (lines 383–391), the tool-attributable gain is only 2.4 points (53.4 → 55.8), and on GSM Plus it's 2.2 points (37.8 → 40.0). These small tool-specific gains, combined with no variance statistics, raise questions about whether the improvements on standard benchmarks are meaningfully attributable to tool-use capability rather than general SFT effects on domain-relevant data.

- **No comparison to other tool-use training approaches**: The paper introduces a tool-use training dataset and claims it enables LLMs to "effectively learn how to utilize external tools" (line 570), but never compares against any other tool-use training method or dataset under identical settings. Without this comparison, the paper cannot establish that ToolBridge is a meaningful or superior contribution relative to what the community already has. This is not a missing-related-works issue; it is a fundamental experimental gap—the paper's core claim of effectiveness cannot be assessed in relative terms.

### Minor

- **RandomQA evaluation is in-distribution by design**: RandomQA is explicitly constructed using programmatically-computed templates (prime generation, matrix operations, time zone calculation) that require the exact tool-use patterns ToolBridge trains on (lines 453–489). While it demonstrates that tool-use training works for in-distribution computation tasks, the dramatic gains (e.g., Llama2-7B: 5.0% → 55.3%) do not necessarily generalize to out-of-distribution or diverse real-world tool-use scenarios. The paper would be strengthened by evaluation on established tool-use benchmarks.

- **FACT benchmark is small and acknowledges reliability issues**: Each FACT batch contains only 200 entries (lines 529–530), and the paper itself documents that web-scraping-based fact retrieval is inconsistent—with unreliable information, excessively long scraped content, and security risks (lines 533–546). This limits the strength of claims about factual retrieval capability.

- **No variance statistics reported**: All results in Tables 5–8 (lines 379–515) are single numbers with no standard deviations across runs. Given that the tool-attributable improvements on standard benchmarks are only 2–3 points, confidence intervals or repeated runs would strengthen these claims.

### Trivial
None.

## Nice-to-Haves

- Evaluation on established tool-use benchmarks (e.g., ToolQA) to demonstrate out-of-distribution generalization of tool use
- Report tool invocation rates during inference on standard benchmarks—what fraction of test questions actually trigger tool use?
- Error analysis characterizing which questions benefit from tool invocation vs. which are unchanged
- An ablation that uses the original raw datasets (before tool insertion) with matched data volume, to more cleanly disentangle the data source effect from the tool annotation effect

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First to open-source training data" claim may be incorrect** (harsh critic): The critic argues Toolformer and ToolLLM released data. Per review rules, I cannot verify external claims about other works' data releases, so this is removed.

- **LoRA rank 16 is unjustified / total batch size limits learning** (harsh critic): This is a hyperparameter nitpick; LoRA rank 16 is a common standard choice, and claiming the training was insufficient without evidence is speculative.

- **Qualitative comparison unfair (comparing against Gemma2 with no tools)** (harsh critic): The paper also compares against Llama3.1 and GPT-4o, which do have tool capabilities (line 555). The Gemma2 comparison is supplementary, not the sole claim.

- **Q_i manual quality assessment lacks inter-annotator agreement** (harsh critic): While valid in principle, this is a minor reproducibility detail about a filtering step that is one of several, not a core contribution.

- **Missing Llama2-7B results on Stanford WebQA** (harsh critic): This is a minor experimental omission, not a substantive flaw.

- **GPT-4o-mini fails on 76% of entries** (harsh critic): The attrition is documented transparently, and the 178K final dataset is still substantial. Low yield from a large pool is common in data curation.

- **Consistency validation is "shallow"** (harsh critic): The paper acknowledges this is a simple check ("checking if the execution results are included in the subsequent text"), and it achieves a 48.8% retention—removing half the data based on even this criterion is meaningful, and future work can improve it.

- **Strength finder's claim about "well-designed ablation"**: Somewhat weakened by the confound identified in Major Weakness 2 about Stanford WebQA. The ablation is useful but has caveats on the standard benchmarks.

- **Strength finder's claim about RandomQA as strength**: RandomQA is in-distribution by construction, making large gains expected rather than surprising. Moved to removed points as a strength.

- **Strength finder's generic claim about "transparent discussion of limitations"**: The paper's discussion of FACT limitations is honest but brief and doesn't deeply analyze implications. This is reasonable but not a major strength.

- **Demand for confidence intervals on benchmark results**: While desirable, single-run evaluation is common in this research area. Moved from weakness to nice-to-have.

## Novel Insights

The ablation structure (ToolBridge vs. ToolBridge§) reveals an important but underappreciated finding: on non-math benchmarks like Stanford WebQA, the vast majority of improvement (16.5 out of 18.7 points) comes from SFT on general data, not from tool invocation (only 2.2 points). This suggests that much of the observed improvement from tool-use fine-tuning on standard benchmarks may be attributable to the general quality and domain relevance of the SFT data rather than to learned tool-use capability per se. This distinction is crucial for the field—future tool-use training datasets should evaluate whether their claimed tool-use gains persist once general SFT effects are properly controlled for.

## Suggestions

- Restrict the paper's claims to match the evidence: ToolBridge is effective for math-oriented tool use (where training and evaluation overlap), but the evidence for general-purpose tool use is limited. The abstract and title should more precisely reflect this scope.
- Add a comparison training run against at least one other existing tool-use training dataset under identical settings to establish ToolBridge's relative value.
- On the standard benchmarks, report tool invocation rates: what percentage of test questions trigger a Python call during inference? This would directly demonstrate whether improvements come from tool use or from SFT on relevant data.

## Evaluation Summary

**Originality**: Moderate. The pipeline and consistency filtering are useful contributions, but the overall approach of using GPT-4o-mini to generate tool-annotated data follows established patterns.

**Importance of research question**: High. Open-source tool-use training data is a genuine community need.

**Whether claims are well supported**: Mixed. The broad claim of equipping LLMs with general external tool capabilities is only well-supported for the math/computation domain; the evidence for broader tool use and factual retrieval is weaker. The ablation raises questions about how much improvement is attributable to tool use versus general SFT.

**Soundness of experiments**: Limited by the lack of comparison to other methods, the in-distribution nature of the primary custom benchmark, and the small FACT evaluation. Standard benchmark improvements are modest and lack variance statistics.

**Clarity**: Generally clear and well-structured, with transparent pipeline documentation.

**Value to research community**: The open-sourced dataset and pipeline documentation have value, but their impact is diminished by the lack of comparative evaluation and the dataset's concentration on math content.

## Score and Decision

The paper makes a genuine transparency contribution with its documented pipeline and open-sourced dataset. However, three major issues significantly weaken its claims: (1) the dataset is 83% math content, undermining the breadth of its "external tool capabilities" claims; (2) the ablation shows that most improvement on non-math benchmarks comes from general SFT, not tool use; and (3) there is no comparison to any other tool-use training approach. The evidence supports a narrower claim—that a math-heavy, code-augmented SFT dataset improves math benchmarks—but the paper makes broader claims that the evidence does not sustain. These issues are addressable in principle (with reframing and additional experiments), but in the current form they represent significant overclaiming.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>