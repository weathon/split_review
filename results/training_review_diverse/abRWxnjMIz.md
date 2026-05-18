Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

## Summary

This paper introduces the task of "scoping" language models — restricting them to answer only queries within a defined domain while rejecting irrelevant ones — and conducts a broad empirical comparison of six methods (system prompting, SFT, DPO, probing, Circuit Breakers (CB), and SFT→CB). Using Super-NaturalInstructions tasks across categories like Sentiment Analysis, Summarization, and Program Execution, the authors evaluate scoping methods on task performance, in-distribution and out-of-distribution rejection, and adversarial robustness. The main finding is that CB and SFT→CB are more robust than alternatives, especially under low-diversity rejection data and adversarial attacks, while SFT→CB maintains the task performance of SFT with the rejection robustness of CB.

## Strengths

- **Comprehensive empirical comparison across methods and settings**: The paper systematically evaluates six methods across three task categories (classification, generation, reasoning), multiple adversarial attacks (7 types), diversity conditions, and multi-task configurations. This breadth (Figures 1–3, Section 4) provides strong support for the relative strengths and weaknesses of each approach.

- **CB generalizes from narrow rejection distributions**: The diversity experiment (Section 4.2, Figure 2) shows that CB and SFT→Cmaintain high OOD rejection even when trained with very low rejection set diversity (e.g., a single category), while DPO requires diverse data to perform well. This is a practically important finding — adapting models to new deployments becomes inexpensive if they generalize from few examples.

- **Layering SFT and CB achieves complementary benefits**: SFT→CB consistently yields high accept-task performance (matching SFT) while maintaining robust rejection (comparable to CB) across most settings, including adversarial attacks and varied diversity conditions (Figures 1–2). This "best of both worlds" result is the paper's most actionable finding.

- **Mechanistic explanation via representation analysis**: Section 4.4 shows that SFT/DPO only change representations at tail-end positions, while CB-based methods alter representations across the entire context, providing a plausible explanation for CB's stronger robustness. This strengthens the empirical findings with an interpretable account.

- **Honest reporting of limitations**: The paper explicitly acknowledges that "none of these methods are even close to perfect" (Section 4.1), that CB "breaks down when the rejection set is too diverse" (Section 4.2), and that the b64 attack "bypasses all models" (Section 4.1). This candor increases confidence in the positive findings.

## Weaknesses

### Fatal
None.

### Major

- **Non-uniform rejection detection across methods creates comparability concerns**. The paper uses three different rejection detectors: (1) string matching for Sys., SFT, and DPO; (2) string matching *plus* repetition-pattern detection for CB-based methods; and (3) a binary MLP classifier for the Probe (Section 3.4). Because these detectors are not validated to have equal false-positive/-negative rates on a common held-out set, the central rejection-rate comparisons are not strictly apples-to-apples. CB's rejection rate includes detections from the repetition detector that the other methods' string-matching pipeline would miss, and the Probe's rejection rate is determined by a separately trained classifier with its own bias characteristics. The paper attempts to calibrate each detector on 30-sample sets against human judgment, which is reasonable as a starting point, but does not demonstrate that the detectors agree on a larger shared validation set. This does not invalidate the paper's core claims — the trends are consistent across multiple task categories and the representation analysis provides independent support — but it means the exact rejection-rate numbers across methods should be interpreted cautiously. A replication with a unified detection pipeline (e.g., LLM-as-judge on a representative subset, or applying all detectors to all methods) would resolve this cleanly.

- **The Precise-Scoping claim (a listed contribution) lacks quantitative support**. The introduction lists "we find that CB supports multiple accept tasks, and can scope more precisely than other methods" as a contribution. While the multi-task claim is supported in Section 4.3 with quantitative results, the precise-scoping claim (e.g., "only News summarization instead of all summarization") appears as a single sentence in Section 4.4 (line 249) with no accompanying figure, table, or quantitative comparison. For a claim elevated to a bullet-point contribution, this is a notable gap.

- **Missing CB-specific hyperparameter details harm reproducibility**. The CB loss (Section 3.3) includes scheduling functions α(t) and β(t) that control the trade-off between the accept and reject loss components over time, but these functions are never specified. The paper states "We use original hyperparameters proposed by Zou et al. 2024" but does not report what those hyperparameters are. Given that the analysis shows CB performance is sensitive to configuration (e.g., LoRA rank sweet spot in Section 4.4), the scheduling functions and other CB-specific settings (which layers are targeted, the exact optimization schedule, etc.) should be stated explicitly. The paper does tune learning rate and step budget for CB (as it does for SFT and DPO), so the gap is specifically in the CB-unique hyperparameters.

- **The Probe is a fundamentally different paradigm included as a directly comparable method**. The Probe is an external classifier on a frozen model's representations — it does not modify generation behavior at all. Including it alongside SFT, DPO, and CB as a "scoping method" conflates two distinct problems: (1) inducing the model to refuse (behavior modification) and (2) externally filtering outputs (classification). The Probe's rejection rate depends on its own training and threshold, making direct comparison of its rejection behavior with behavior-modifying methods inherently apples-to-oranges. The paper would benefit from either presenting the Probe in a separate treatment or evaluating it under the same detection pipeline as the other methods.

### Minor

- **Single-model-family evaluation for main experiments**. All main experiments (Figures 1–3, diversity, multi-task) are conducted on Mistral-7B-Instruct-v0.2 only. The teaser (Figure 0) shows Granite results but these are not discussed or analyzed in the body. For a paper making deployment recommendations, demonstrating that the patterns hold on at least one other model family (e.g., Llama, Gemma) would substantially strengthen generalizability claims.

- **No error bars or statistical reliability metrics**. Key comparisons (e.g., CB vs. DPO under TAP, CB vs. SFT-CB on OOD rejection) appear close in the figures, and no confidence intervals, error bars, or replication information is provided. For the diversity experiments in particular, a few runs with different random seeds would establish whether the observed trends are stable.

- **TAP attack evaluation uses only 10 prompts per dataset** (Section 4.1). With such a small sample, a single successful jailbreak shifts the rejection rate by 10 percentage points. The paper acknowledges this but still draws conclusions (e.g., "Probe is best" under TAP for SA) from limited data.

- **Dataset construction details are not fully reproducible**. The paper states (Section 3.2) that tasks were "manually select[ed]" based on being "straightforward to automatically evaluate" without documenting the selection criteria or listing excluded tasks. The Program Execution category (26 tasks, all synthetic) dominates the data by instance count (94K vs. ~10–33K for other categories), which could affect the diversity experiments where rejection categories are mixed.

- **Rouge-L used for generation tasks without discussion of its limitations for dialogue/story composition**. The "accept score" for generation tasks relies on Rouge-L against ground-truth completions, which is standard but known to be a poor measure for creative tasks like Story Composition and Dialogue Generation where valid responses may have low n-gram overlap with a reference. This affects the central task-performance metric.

### Trivial
- The precise-scoping claim in Section 4.4 would benefit from even a minimal quantitative result (e.g., "CB achieves X% rejection on non-news summarization tasks while accepting Y% of news summarization queries"). Otherwise it reads as an assertion rather than a finding.

## Nice-to-Haves
- **Standardize rejection detection**: Validate that all detectors agree on a shared held-out set, or run a representative subset through an LLM judge to confirm the cross-method comparisons.
- **Present the Probe separately**: Re-frame the Probe as a complementary approach (external classification) rather than a comparable scoping method, or evaluate it using the same string/repetition detection pipeline.
- **Run one additional model family**: Even a truncated set of experiments on a Llama- or Gemma-based model would significantly strengthen generalizability.
- **Disclose the best-found hyperparameters** for each method (learning rates, step budgets, α(t)/β(t) schedules) in an appendix or supplementary material.
- **Add error bars** for key comparisons (adversarial evaluation, diversity experiments) by repeating with a few random seeds.

## Removed Points
- *"Key results are overstated"* (Harsh Critic): After verification, the paper's central claims ("CB is more robust," "SFT→CB achieves best of both worlds") are well-supported by the evidence across multiple settings. The paper also explicitly acknowledges CB's limitations (diverse rejection set failures, imperfection of all methods). The narrative framing is appropriately qualified given the evidence presented.
- *"CB hyperparameters not stated while SFT/DPO have them tuned"* (Harsh Critic): The paper states "For CB we tune learning rate and step budget" (line 119), so CB hyperparameters *are* tuned like SFT and DPO. The real issue (missing α(t)/β(t) scheduling functions) is retained in Major.
- *"b64 attack biases acceptance rate systematically"* (Harsh Critic): The paper already acknowledges this issue explicitly (line 187: "One additional point on the b64 attack, which appears to bypass all models: the completions tend to either be generic base-64 encoded response, or invalid base-64.").
- *"Rouge-L not appropriate for dialogue/story"* (Harsh Critic): Overstated — Rouge-L is standard practice as a "proxy for performance" (line 95), which the paper explicitly states. Weakened to a Minor note.
- *Strength #4 from Strength Finder ("Demonstrates precise scoping capability")*: Conflicts with the verified weakness that precise-scoping lacks quantitative evidence. Moved here per the rule that weaknesses override strengths.

## Novel Insights
The meta-review reveals a tension the paper does not fully grapple with: CB's robustness advantage (from broad representation-level changes) and its diversity-failure (from optimization difficulty with too many orthogonalization targets) may be two sides of the same coin. The representation analysis shows CB alters representations globally, which helps against narrow rejection sets but likely creates conflicting gradient signals when the rejection set is diverse. This suggests a fundamental trade-off — methods that change representations more broadly may be more robust, but also harder to scale to heterogeneous rejection requirements. This trade-off is a genuinely interesting open problem that the paper surfaces but does not articulate as a central tension.

## Suggestions
1. **Validate the rejection detectors against each other**: Either apply the repetition detector to non-CB outputs to confirm it does not fire, or run a common subset through an LLM judge to verify that the cross-method comparisons hold under a unified metric.
2. **Provide quantitative evidence for the precise-scoping claim**, or remove it from the contribution list. A simple table showing acceptance/rejection rates on fine-grained splits (e.g., news vs. non-news summarization) would suffice.
3. **Report the α(t)/β(t) scheduling functions** and other CB-specific hyperparameters (target layers, optimization schedule) explicitly.
4. **Separate the Probe** from the behavior-modification methods in presentation, or evaluate it under the same detection pipeline.
5. **Add at least one additional model** (e.g., Llama-3-8B-Instruct) for a representative subset of experiments, and include error bars for the main comparisons.

## Score and Decision

The paper tackles an important and timely problem (task scoping for LLM deployment) with a large-scale, systematic empirical comparison. The core findings — that CB generalizes from narrow rejection distributions and that SFT→CB combines task performance with robust rejection — are well-supported and practically valuable. The main weaknesses (non-uniform rejection detection, missing CB scheduling details, unsupported precise-scoping claim, single-model evaluation) are real but fixable and do not undermine the paper's central contributions. The work is clearly written and honestly reports limitations.

**Overall**: Meets the acceptance threshold with room for improvement in rigor and completeness.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>