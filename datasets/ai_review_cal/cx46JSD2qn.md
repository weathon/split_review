- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 5, 5, 1, 3
Now I have a thorough understanding of the paper content. Let me produce the consolidated final review.

## Summary

This paper introduces ChiPBench, a benchmark and dataset that enables end-to-end PPA (Performance, Power, Area) evaluation of AI-based chip placement algorithms using the open-source OpenROAD flow. The authors compile 20 circuits from Verilog source through the full physical design pipeline, preserving the design kits (LEF/DEF, liberty, SDC) that prior datasets lacked, and evaluate six state-of-the-art AI placement methods (SA, WireMask-EA, DREAMPlace, AutoDMP, MaskPlace, ChiPFormer) on both intermediate surrogate metrics and final PPA metrics. The central finding is that AI methods that excel on intermediate metrics (MacroHPWL, HPWL) often underperform the default OpenROAD flow on end-to-end PPA, suggesting the AI community should focus on final design outcomes rather than surrogates.

## Strengths

- **First open-source benchmark that supports full end-to-end PPA evaluation for chip placement.** Table 1 shows ChiPBench is the only dataset with checkmarks across all five criteria (Complete Design Suite, Logic Synthesis Support, Physical Design Support, Full EDA Flow Support, Large Scale & Diversity), while prior datasets like ISPD2005, ICCAD2015, and OpenABC-D each lack essential components (e.g., buffer definitions for CTS, layer definitions for routing, or complete design kits). This directly enables reproducible end-to-end evaluation that was previously infeasible with open-source tools.

- **Valuable circuit diversity spanning realistic scales and domains.** The 20 circuits include CPUs, GPUs, microcontrollers, network interfaces, and cryptographic units, with cell counts ranging from 332 (OV7670\_i2c) to 859,382 (subrisc). This breadth strengthens the generality of the benchmark across design domains and complexity levels.

- **Comprehensive evaluation covering three algorithmic paradigms.** The paper evaluates black-box optimization (SA, WireMask-EA), analytical/gradient-based (DREAMPlace, AutoDMP), and reinforcement learning (MaskPlace, ChiPFormer) methods on the same benchmark, enabling a unified comparison that prior work lacked. This is a useful resource for the community.

- **Empirical evidence of misalignment between intermediate and final metrics.** Tables 2 and 3 show patterns where methods with strong intermediate-metric performance (e.g., WireMask-EA with MacroHPWL 0.647) still underperform on final PPA (Power 1.015, WNS 1.085), supporting the paper's core message about the gap between surrogate metrics and actual design quality.

## Weaknesses

### Fatal

None.

### Major

- **Format conversion confound (LEF/DEF ↔ Bookshelf) is unvalidated, creating a potential systematic bias against AI methods.** The paper states (lines 321–323) that AI methods require Bookshelf format, so the pipeline converts LEF/DEF → Bookshelf for placement, then Bookshelf → DEF to re-enter the OpenROAD flow. The OpenROAD baseline (line 325) is obtained using "OpenROAD's native Place method" which works directly on LEF/DEF without this round-trip. Bookshelf is a simplified format that discards information (e.g., detailed layer constraints, pin shapes, routing obstructions). The paper provides **no validation** that the round-trip conversion is lossless or that it does not systematically penalize AI-method placements. A control experiment—running OpenROAD's own macro placer through the same Bookshelf round-trip and comparing PPA to the direct OpenROAD result—is necessary to establish that observed PPA differences are due to placement quality rather than conversion artifacts. Without this, the headline experimental finding is on uncertain ground.

### Minor

- **Deployment details for AI methods are insufficiently documented.** The paper reports results for six AI algorithms but provides almost no information about their configuration: whether RL methods (MaskPlace, ChiPFormer) were retrained on these 20 circuits or used with pre-existing checkpoints; what training budget was allocated; how hyperparameters (especially for SA and WireMask-EA) were set—per-circuit tuned or fixed defaults; and how DREAMPlace/AutoDMP were configured for macro-only placement versus full cell placement. Since the paper is open-source (stated in Section 6.3), the code presumably fills some of these gaps, but the paper itself should summarize key settings to allow readers to assess whether methods were deployed in a way that gives them a fair chance.

- **Aggregation method for normalized ratios is not stated.** Results in Tables 2 and 3 are reported as ratios normalized to OpenROAD = 1.000, but the paper does not specify whether these are arithmetic means, geometric means, or medians of per-circuit ratios. With 20 circuits spanning very different scales and including designs with 0 macros, the choice of aggregation can materially affect the reported values. The paper should state the aggregation method and ideally provide per-circuit distributions or variance measures.

- **Handling of 0-macro designs in macro placement evaluation is unclear.** Table 1 lists 12 out of 20 designs with 0 macros (e.g., 8051, CAN-Bus, FPGA-CAN, subrisc, toygpu). The paper does not state whether these were included in the macro placement results (Table 2). If included, they would produce trivially identical MacroHPWL values (0 for all methods), pulling normalized ratios toward 1.0 and diluting the signal from macro-heavy designs. The paper should clarify which subset of designs was used for macro placement evaluation and discuss the impact on aggregate results.

- **Correlation analysis lacks reported coefficients.** Section 7.2 reports that "MacroHPWL only has a weak correlation with the Wirelength" and that HPWL shows a "very strong positive correlation" with Wirelength, but does not report the actual Pearson r values. The wrapfigure (Figure 4) shows a correlation heatmap but its content is not described in the text. Providing the coefficient values (with confidence intervals) and reporting Spearman rank correlations would make the analysis more rigorous and actionable.

### Trivial

- Lines 322–323 contain an apparent editorial duplicate: "The resulting placement files are then converted back to DEF format and reintroduced into the original flow." appears twice in sequence.
- The URL in line 325 is truncated ("\href{https://anonymous.4open."), likely a PDF extraction artifact.

## Nice-to-Haves

- **Per-circuit raw PPA values (not just normalized ratios).** A supplementary table with actual WNS, TNS, Power, and Area for each design would enable researchers to assess variation and identify outlier-driven effects.
- **Validation of the format conversion pipeline.** The control experiment described in the Major section above would significantly strengthen confidence in the results.
- **Runtime comparison.** For practitioners, placement runtime is an important practical dimension alongside PPA, and its omission leaves a gap in the benchmark's utility.

## Removed Points

The following points from the input reviews were removed with justification:

- **"OpenROAD has home-field advantage; downstream tools favor its own placer."** The paper's goal is specifically to evaluate AI placements within the standard OpenROAD flow—this is the benchmark's stated scope, not a confound. Asking whether a different downstream toolchain would change the conclusions is outside the paper's scope and speculative without evidence of systematic bias in OpenROAD's tools. (Harsh Critic, Critical Issue 4)

- **"Statistical analysis lacking (variance, error bars, significance tests)."** For EDA benchmarks where single-run evaluation is standard practice, this demand reflects a field-standards mismatch rather than a genuine flaw. (Harsh Critic, Missing Parts)

- **"Runtime comparison not reported."** Not a core claim of the paper; the benchmark is about PPA evaluation, not runtime benchmarking. (Harsh Critic, Missing Parts)

- **"Table 1 column definitions are vague."** The column headings ("Complete Design Suite," "Logic Synthesis Support," etc.) are reasonably clear given the context; the paper also describes in text what files are included (lines 71, 150). (Harsh Critic, Section 2)

- **"Related work section too long / could be shortened."** A subjective presentation preference, not a substantive weakness. (Harsh Critic, Section 3)

- **All pure syntax/formatting complaints** (grammar, garbled text, broken characters) — these are PDF extraction artifacts, not author errors.

- **Strength Finder's generic claims** about the "importance of the problem" — replaced by concrete, evidence-backed strengths.

## Novel Insights

The reviews do not surface insights beyond the paper's own contributions. The key observation—that the chip placement community's reliance on intermediate metrics like MacroHPWL produces a misleading picture of algorithm quality—is the paper's own central thesis, and the reviewers' analyses do not add a fundamentally new perspective beyond sharpening the critique of the evaluation methodology.

## Suggestions

1. **Validate the format conversion pipeline.** Run OpenROAD's own macro placer through the Bookshelf round-trip and compare PPA to the direct result. Report the degradation (or lack thereof). If the round-trip is lossy, either document the bias or implement direct LEF/DEF output for the AI methods (bypassing Bookshelf entirely).
2. **Clarify per-design inclusion.** State explicitly which designs were used for macro placement evaluation (ideally, only those with macros) and which for cell placement. Report whether the 12 zero-macro designs were excluded from Table 2.
3. **Report aggregation method and variance.** Specify whether Table 2/3 ratios are arithmetic or geometric means. Provide per-circuit distributions (box plots or scatter plots) in the appendix.
4. **Document AI method configuration.** Add a table summarizing key deployment choices for each method: training data split, hyperparameter selection method, runtime budget, and whether defaults from original papers were used unchanged.
5. **Report correlation coefficients numerically.** Add the Pearson r values (and ideally Spearman ρ) to the text or Figure 4, with confidence intervals.
6. **Fix the editorial duplicate** in lines 322–323.
