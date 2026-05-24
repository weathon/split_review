Now I have a thorough understanding of the paper and can synthesize the reviews. Let me write the consolidated review.

## Summary

This paper introduces **Ambig-SWE**, an underspecified variant of SWE-Bench Verified, and evaluates LLM agents across three capacities needed for handling underspecified instructions: (a) detecting missing information, (b) asking targeted clarifying questions, and (c) leveraging interaction to improve task completion. Using 500 paired well-specified/underspecified GitHub issues, a simulated user proxy (GPT-4o), and six models (Claude Sonnet 3.5/4/Haiku 3.5, Llama 3.1 70B, Deepseek-v2, Qwen 3 Coder), the authors show that interaction can recover a large fraction of performance lost to underspecificity (e.g., Claude Sonnet 4 recovers ~76% of the gap, from 40% to 61.4% resolve rate), while detection of underspecificity remains a major weakness for all models except Claude Sonnet 4.

## Strengths

1. **Conceptual decomposition of the interaction problem.** The breakdown into detection, questioning, and integration provides a clean, actionable framework for studying how agents handle underspecification. This is more nuanced than prior work that treats ambiguity as a monolithic problem.

2. **Controlled paired dataset (Ambig-SWE).** Generating underspecified variants of SWE-Bench Verified issues yields paired ground-truth specifications, enabling causal measurement of interaction impact that would be impossible with natural underspecified issues (which lack verified correct specifications). The distributional analysis comparing synthetic issues against natural underspecified issues is a reasonable validation step.

3. **Interaction significantly and consistently improves performance.** Figure 3 and the Wilcoxon tests show that all six evaluated models improve significantly from Hidden to Interaction settings. Claude Sonnet 4's recovery of ~76% of the performance gap (40% → 61.4%) and the qualitative finding that this is driven by targeted clarification questions are the paper's strongest empirical results.

4. **Navigational vs. informational detail analysis (Table 1).** The finding that some models benefit substantially from requesting file paths while others (notably Qwen 3 Coder) are harmed by receiving navigational information is a specific, testable, and surprising result that isolates a concrete failure mode in model integration strategies.

5. **Qualitative analysis of question strategies (Section 5.3).** The categorization of exploration-first (Claude), immediate-asking (Deepseek/Qwen), and template-based (Haiku) strategies is grounded in examples and provides actionable diagnostic insight into how question-asking approaches affect task outcomes.

6. **Systematic evaluation across six models spanning proprietary and open-weight families.** The breadth of models evaluated, including two generations of Claude and Qwen 3 Coder (which rivals Claude Sonnet 4 on SWE-Bench), provides robust grounding for claims about how capability scaling interacts with interaction behavior.

## Weaknesses

### Major

1. **Unequal turn budgets confound cross-model comparisons (Section 3.1).** Claude Sonnet 4 and Qwen 3 Coder are allocated up to 100 turns while other models are capped at 30. The paper justifies this by citing "greater reasoning and planning capacity," which is circular—the very capacity being measured receives a resource advantage. Claude Sonnet 4's higher Interaction performance (61.4%) compared to Claude Sonnet 3.5 (39.6%) may partly reflect having ~3× the turn budget. The paper's efficiency analysis is also contaminated: agents with higher turn caps naturally use more steps. This does not invalidate within-model Hidden→Interaction improvements, but it weakens all cross-model claims (e.g., "Qwen 3 Coder achieves the highest information extraction but requires 50% more questions than Claude Sonnet 4").

2. **Detection experiment (RQ2) conflates internal detection with interaction propensity.** The paper measures detection by whether a model *chooses to interact* across fully-specified and underspecified inputs. However, a model that detects underspecificity may still choose not to interact (e.g., Qwen 3 Coder's 100% FNR across all prompts—the paper's own analysis shows it follows a rigid protocol, which may reflect propensity rather than inability to detect). Conversely, a model that interacts on full-specified inputs may do so from a default interaction strategy rather than mis-detection. The reported FPR/FNR measure *interaction alignment with the experimenter's expectation*, not detection accuracy per se. The paper's claim that models "fail to reliably distinguish them" conflates internal detection capacity with observed interaction behavior, and the conclusions about detection ability are not fully supported by the experimental design.

3. **Synthetic underspecification is not validated to be genuinely irresolvable from the codebase.** The paper defines underspecification as "missing information that would prevent an expert from creating a successful solution," but the synthetic issues are generated by reducing content with GPT-4o, without ensuring that the omitted information cannot be recovered from the codebase or stack traces. The paper itself documents (Section 3.2) that Claude Sonnet 4 "extensively explores the codebase and attempts multiple solutions to overcome the lack of information" and that Qwen 3 Coder "relies on its internal knowledge for key insights about missing information... potentially inflat[ing] its performance." This means the gap between Hidden and Interaction settings conflates genuine underspecificity resolution with codebase-exploration capability, making the "74% improvement" claim hard to interpret precisely. The paper acknowledges this as a confound but does not quantify its extent.

### Minor

1. **Oracle user proxy limits external validity of interaction results.** The simulated user (GPT-4o) always answers correctly when the information is in the full issue and responds "I don't have that information" otherwise. The paper acknowledges this in Section 7, stating the proxy "may be more cooperative than real users." However, the central quantitative claims about interaction effectiveness (e.g., "89% relative performance recovery") are conditioned on this idealized partner. Real users can be imprecise, misdiagnose errors, or lack the technical vocabulary to answer specific questions, meaning the measured interaction benefits are upper bounds. The paper's framing as a diagnostic evaluation partially mitigates this, but the severity of the gap between this setup and realistic deployment is understated in the abstract and introduction.

2. **The 74% improvement claim is ambiguous.** The paper states in the abstract and introduction that interactivity yields "up to 74% improvement over the non-interactive settings." From the data, this 74% appears to be the fraction of the Hidden→Full performance gap recovered (Claude Sonnet 4: (61.4−40)/(68−40) ≈ 76%), not a relative improvement in resolve rate (which would be 53.5% for Claude Sonnet 4). The phrasing "over the non-interactive settings" suggests a direct percentage improvement, which is misleading without clarification.

3. **The cosine distance metric for information gain is not validated against task performance.** Section 5 uses embedding-based cosine distance to measure information gain from interaction, but does not establish that this metric correlates with actual task outcomes or knowledge acquisition. The paper shows interesting patterns (e.g., Qwen 3 Coder has highest cosine distance but similar resolve rates to Claude Sonnet 4), but the interpretation that "how models integrate information matters as much as how much they extract" relies on the assumption that cosine distance measures meaningful information gain, which is not independently verified.

4. **Claude Sonnet 4's Hidden setting evaluated on a subset (100/500 issues).** Footnote 4 notes this was done for cost reasons. This is a reasonable practical concession, but it means direct comparisons of Claude Sonnet 4's Hidden→Interaction improvement against other models' improvements are on different subsets, introducing an uncontrolled variable.

### Trivial

- None significant. The paper is well-written and the presentation is clear despite the parser artifacts.

## Nice-to-Haves

- A controlled experiment where models are explicitly asked to classify whether an issue is underspecified (binary classification or confidence rating) would cleanly separate detection ability from interaction propensity, directly addressing Weakness #2.
- A uniform turn-budget ablation (e.g., all models at 30 turns, then a subset at 100) would decouple model capability from resource advantage (Weakness #1).
- For each synthetic issue, characterizing what specific facts are omitted that are (a) necessary for the solution and (b) not recoverable from the codebase would strengthen construct validity (Weakness #3).
- Varying the user proxy's behavior (e.g., sometimes giving vague or incorrect answers) would quantify how much the interaction results depend on the idealized partner.
- Trajectory-level case studies showing question-answer sequences and resulting patches for representative issues would strengthen the qualitative analysis.

## Removed Points

These points were flagged for removal; treat them with caution:

1. **Critic's claim that "the method for generating underspecified variants using GPT-4o is underspecified."** — The prompt is deferred to the appendix (§A.2.3), which was stripped by the parser. The main text describes the approach at an appropriate level. This is a parser artifact, not an author error.

2. **Critic's claim that "the classification of navigational vs. informational is not clearly operationalized."** — Section 3.3 defines both terms: "informational, which relates to the expected behavior or nature of the error, and navigational, which pertains to the locations of the files to modify." Table 1 clarifies "Navigational information refers to file paths needing modification." This is sufficiently clear for the analysis presented.

3. **Critic's claim that the Qwen 3 Coder result is "speculation not supported by the data."** — The paper explicitly states it analyzed trajectories (referencing §A.7) and found rigid behavior where the model re-explores the code after receiving file locations. This is a claim supported by trajectory evidence, not speculation.

4. **Critic's framing of the oracle user issue as "structural... invalidat[ing] the paper's central empirical results."** — The paper is transparent about the proxy being idealized (Sections 2.2, 7) and frames its experiments as diagnostic evaluation, not production deployment measurement. The external validity concern is real but does not invalidate the controlled within-experiment findings.

5. **Strength Finder's claim that Claude Sonnet 4 "recovers 89% of its Full-setting performance."** — The paper says "Claude Sonnet 4 attains the highest relative performance (89%)," referring to Interaction/Full. However, 61.4/68 = 90.3%, so this is approximately correct. The exact number may differ slightly, but this is a presentation issue, not a substantive error.

6. **Generic strength about "systematic comparison across six models" being robust** — This is weakened by the unequal turn budget issue (Weakness #1) and the Hidden-setting subset issue (Minor #4), so the comparison is less systematic than claimed.

## Novel Insights

Beyond the paper's own contributions, an interesting meta-pattern emerges from comparing the two reviewers: the harsh critic identifies several genuine methodological concerns (turn budgets, detection-behavior conflation, oracle user, codebase recovery), but these concerns are substantially mitigated by the paper's own transparent acknowledgment of most of them. The paper consistently discloses its limitations—it states when Hidden performance may be inflated, it notes the proxy is idealized, it discusses the turn budget allocation—yet presents its findings as "clear trends" rather than tentative observations. The tension between the paper's own honesty about confounds and its confident presentation of results is itself instructive: the real contribution here may be the diagnostic framework (detection→questioning→integration) and the paired dataset, which enable future work to build on careful controlled measurement, rather than the specific performance numbers reported.

## Suggestions

- Clarify the 74% claim to specify it refers to the fraction of the performance gap recovered, not a relative improvement over the Hidden baseline.
- Add an explicit detection classification experiment (binary forced-choice) to decouple detection ability from interaction propensity.
- Address the turn-budget confound by providing a uniform-budget replication or clear discussion of how it affects cross-model comparisons.
- Provide a validation of the cosine distance metric by showing it correlates with task resolution or human judgments of information gain.
- Consider a more realistic user proxy variant in follow-up work to bound how much the idealized partner inflates the interaction benefits.

## Score and Decision

**Score:** 5.5/10

**Decision:** Borderline. The paper has genuine contributions: a well-motivated problem, a useful conceptual framework, a potentially valuable paired dataset, and several concrete empirical findings (especially the navigational/informational distinction and question strategy analysis). However, the structural methodological issues—particularly the unequal turn budgets (confounding cross-model comparisons) and the detection-behavior conflation—prevent the quantitative results from fully supporting the paper's claims. The paper is transparent about many limitations, but the presentation (abstract, introduction) overstates the certainty of the findings. With targeted revisions addressing the major weaknesses (especially a controlled detection experiment and uniform turn-budget analysis), this could become a strong paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Borderline</decision>