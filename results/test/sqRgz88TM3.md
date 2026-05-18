Here is my final consolidated review:

---

## Summary

VFLAIR is a research library and benchmark for vertical federated learning (VFL), implementing 11 attacks, 8 defense methods, 13 datasets, multiple communication protocols (FedSGD, FedBCD, Quantize, Top-k, CELU-VFL), and two model partition strategies (aggVFL, splitVFL). The paper proposes a family of unified evaluation metrics (DCS, T-DCS, C-DCS) that jointly capture the utility-security trade-off of defenses, and benchmarks defense performance across diverse settings, yielding practical insights about defense selection under different VFL deployment scenarios.

## Strengths

1. **First comprehensive, unified benchmark of VFL attacks and defenses.** The paper evaluates 11 attacks and 8 defenses across 3 benchmark datasets under multiple communication protocols (FedSGD, FedBCD), model partitions (aggVFL, splitVFL), and defense hyperparameter settings. This goes well beyond existing VFL benchmarks (e.g., Kang et al. on data-reconstruction only; SLPerf on splitNN only) and provides the first head-to-head comparison under standardized pipelines. The results yield concrete, practically actionable insights (e.g., which defenses are effective across attack types).

2. **Novel evaluation metrics (DCS, T-DCS, C-DCS) that enable principled ranking of defenses.** The Defense Capability Score (Eq. 1) jointly accounts for main-task performance and attack performance via a tunable weighting parameter β, filling a real gap in how VFL defenses are compared. The paper shows that C-DCS rankings are consistent across MNIST, CIFAR-10, and NUSWIDE, and robust to changes in β, lending credibility to the metric as a standardizable evaluation tool.

3. **Rigorous comparison of how model partitions and communication protocols affect vulnerability.** Using the DCS gap (splitVFL − aggVFL; FedBCD − FedSGD) across attack-defense points, the paper demonstrates that splitVFL is less vulnerable than aggVFL and that FedBCD is less vulnerable than FedSGD. These insights directly inform practical system design choices and are backed by quantitative comparisons across multiple datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Incomplete validation of the DCS metric.** The DCS definition (Eq. 1) uses a Euclidean distance to an ideal point (AP*=0, MP*=no-defense MP) without analyzing sensitivity to sampling variability in MP* — which is itself a noisy quantity that varies with dataset, seed, and model. The paper shows robustness to β but not to variance in the reference MP*. Additionally, while most AP values are in [0,1], FR attack AP (1−MSE) and NTB attack AP (MP difference) can produce values outside this range, creating scale mismatches with MP that are not discussed. Finally, the rankings are not validated against any alternative evaluation protocol or simpler baseline metric, making it difficult to assess whether DCS captures practical intuitions reliably.

2. **Insufficient evidence for framework advantages over existing alternatives.** The paper claims VFLAIR is "lightweight" and "research-friendly" compared to FATE, Fedlearner, etc., but provides only a hardware requirement comparison (referenced table) as evidence. No quantitative comparison is given — e.g., lines of code to add a new attack/defense, time to configure a new dataset, framework overhead, or documentation quality. For a library claimed as a contribution, this is a significant evidence gap. (The primary contribution remains the benchmark, which limits the severity of this concern.)

3. **Key experimental details omitted that impede reproducibility.** The paper does not specify: (a) the local model architectures for each dataset beyond "NN" (depth, width, activation functions), (b) the training protocol (optimizer, learning rate, batch size, early stopping criteria), (c) how the 2-party and 4-party feature splits were constructed for each dataset, and (d) the exact hyperparameter selection procedure for attacks (referenced to original papers, but no mention of whether they were retuned). These omissions weaken confidence in the cross-setting consistency claims and make the benchmark harder to reproduce.

4. **The full attack-defense benchmark results are not visible in the main text.** The main text shows a single representative C-DCS ranking table (NUSWIDE, with several entries marked "-" for defenses not evaluated on certain attack types) and references the remaining two datasets' ranking tables (MNIST, CIFAR-10) to the appendix. While this practice is common, a benchmark paper's core empirical contribution should be more directly assessable in the main body — the reader cannot independently verify the claimed cross-dataset consistency of rankings without flipping to the appendix.

5. **Attack-defense evaluation is limited to NN-based VFL with 2 parties.** The paper covers tree-based VFL but does not evaluate attacks/defenses on tree models, and multi-party attack scenarios are not explored. The scope is reasonable (the abstract could be clearer about this), but the general claims about defense recommendations are stated without caveats about the restricted setting.

6. **Limited coverage of cryptographic defenses.** The conclusion acknowledges "limited implementations on cryptographic techniques," which is a significant gap given that cryptographic protection (HE, MPC) is a central concern in practical VFL. This limitation should be stated more prominently in the evaluation section rather than only in the conclusion.

### Trivial
1. The abstract states "benchmark 11 attacks and 8 defenses performance" without specifying that this evaluation is for NN-based VFL only. The body later clarifies this scope, but the abstract should match.

## Nice-to-Haves

- Validate DCS rankings against a simpler baseline metric (e.g., worst-case AP at a given MP threshold) or through a small user study with VFL researchers.
- Provide a concrete code example or tutorial showing the steps required to add a new attack/defense in VFLAIR vs. FATE, to substantiate the "extensibility" claim.
- Report the computational budget (GPU hours, number of runs) used for the benchmark to set reproducibility expectations.
- Include a limitations section that explicitly discusses the restricted evaluation scope (2-party, NN-based only, no cryptographic defenses) in a more centralized location.

## Removed Points

These points from the reviews were removed; treat them with caution:

- **Harsh Critic: "Critical Issue 1 — The main text does not adequately report benchmark results; the figures are not included."** The paper includes multiple in-text figures (AP-MP trade-off graphs, DCS gap histograms, β sensitivity plots) and a representative C-DCS ranking table. Figures are embedded in the original PDF and were present in the submission; the parser extraction cannot render them. The ranking tables for MNIST and CIFAR-10 exist in the appendix, which is standard practice. This criticism substantially overstates the problem.

- **Harsh Critic: "Stray text (\tianyuan{No, at least currently, no.}) and incomplete sentences."** These are LaTeX formatting artifacts / track-changes remnants not present in the original submission's intended formatting, or they are parser extraction issues. Per formatting artifact rules, these are excluded.

- **Harsh Critic: "Our code is also available at" with no URL.** The URL was embedded as a hyperlink in the PDF and was stripped during text extraction; it exists in the original submission.

- **Harsh Critic: "Missing related works" claim.** No external sources are available to verify which related works are or are not missing.

- **Strength Finder: "Lightweight, modular architecture designed for research extensibility."** This strength conflicts with the verified weakness that the framework advantages are not quantitatively demonstrated. Per the rule that when a strength and weakness disagree the weakness wins, this strength is dropped.

- **Strength Finder's generic phrasing about "addressed an important problem" — no specific content to cite.**

## Novel Insights

The reviews surface a meaningful tension: the paper makes two claims (library + benchmark) but only provides strong evidence for one (the benchmark). The DCS metric is genuinely novel and practically motivated, yet its construction (Euclidean distance to a noisy ideal point) introduces the same kinds of arbitrariness it aims to resolve — trading one set of methodological gaps (separate MP/AP reporting) for another (scale compatibility, variance in MP*). This is not a fatal flaw (all evaluation metrics have assumptions), but it suggests the metric would benefit from a "sanity-check" validation protocol before being adopted as a community standard. The most actionable insight from the reviews is that the paper would be stronger if it leaned into being a benchmark paper first and treated the library as an enabling artifact rather than a co-equal contribution, thereby sidestepping the most demanding expectation mismatches.

## Suggestions

1. Add a brief "DCS Validation" subsection that: (a) reports sensitivity of C-DCS rankings to ±1 standard deviation perturbations of MP*, (b) checks whether the same top-3 defenses emerge under a simple alternative like "worst-case AP at MP > 0.9×MP*," and (c) adds a short discussion of the scale ranges of different AP types.
2. Include one concrete quantitative comparison with FATE or FedML on a simple task (e.g., "lines of user code to add a new gradient-sparsification defense" or "time to configure a new dataset"), preferably as a short table or code snippet in the main text.
3. Report missing experimental protocols in an appendix table: optimizer (Adam/SGD), learning rate, batch size, local model architectures per dataset (layer counts, widths, activations), and feature-split construction method.
4. Move one more full C-DCS ranking table (e.g., for CIFAR-10) into the main text so that cross-dataset consistency can be directly verified without consulting the appendix.
5. Clarify the abstract to say "11 attacks and 8 defenses for NN-based VFL" and "evaluation of tree-based VFL is limited to main-task performance."

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>