Now I have all the information needed. Let me write the final review.

## Summary

This paper introduces Ambig-SWE, a framework for evaluating LLM agents' ability to handle underspecified instructions in software engineering tasks. Built on SWE-Bench Verified, the authors create synthetic underspecified variants using GPT-4o and evaluate six models across three settings (Full, Hidden, Interaction), decomposing the problem into three steps: detection of underspecification, question-asking for clarification, and integration of acquired information to improve task completion. The core finding is that interaction significantly improves performance on underspecified tasks, but most models default to non-interactive behavior and fail to reliably detect missing information.

## Strengths

- **Well-designed three-step decomposition of the interaction problem.** The paper's decomposition into detection (RQ2), question quality (RQ3), and task completion (RQ1) is genuinely useful for diagnosing where models succeed or fail. Each research question has tailored metrics—resolve rates with Wilcoxon signed-rank tests (Table 4), accuracy/FPR/FNR across three prompt conditions (Table 2), and cosine distance plus LLM-as-judge scores (§5.1). This is more analytically sophisticated than monolithic benchmark evaluations.

- **Significant and consistent improvement from interaction across all models.** Wilcoxon signed-rank tests confirm that Hidden→Interaction differences are significant for every model (Table 4). The magnitude is substantial—Claude Sonnet 4 goes from 40.0% to 61.4%, Claude Sonnet 3.5 from 24.2% to 39.6%. These results provide strong evidence for the paper's central claim that interactive clarification meaningfully recovers performance lost to underspecification.

- **Surprising and actionable model-specific findings.** Qwen 3 Coder's complete non-responsiveness to interaction prompts (100% FNR across all three prompt conditions in Table 2) despite matching Claude Sonnet 4 on SWE-Bench coding ability is a genuinely useful finding. Similarly, the disconnect between information extraction volume and task performance (Qwen extracts the most via cosine distance at 0.179 but Claude Sonnet 4 achieves better resolve rates with 0.171) provides concrete evidence that integration quality matters more than extraction quantity. The navigational information analysis (Table 1) revealing Qwen's rigid protocol-following behavior is also insightful.

- **Comprehensive multi-model evaluation with controlled experimental design.** The paper evaluates six models spanning proprietary and open-weight families across three settings, with three prompt conditions for detection (§4.1), statistical significance testing (Table 4), and distributional difference analysis comparing synthetic versus natural underspecification (§2.1).

## Weaknesses

### Fatal
None.

### Major

- **Internal numerical inconsistency in RQ3.** Section 5.2 states "Qwen 3 Coder achieves the highest information extraction (0.179) but requires 50% more questions than Claude Sonnet 4 (6.02 vs 4.03, Table 6), yet both achieve similar resolve rates (46% vs 41.8%, Figure 3)." However, Figure 3 shows Qwen 3 Coder Interaction resolve rate at 53.80% and Claude Sonnet 4 at 61.40%—these are neither 46% nor 41.8%, and they differ by 7.6 percentage points rather than being "similar." This makes the key claim in RQ2 that "how models integrate information matters as much as how much they extract" poorly supported by the cited evidence. If these numbers come from a subset (e.g., the 100/500 Claude Sonnet 4 Hidden subset or RQ3-filtered instances), this needs to be made explicit. As written, readers cannot verify the central analytical claim of §5.2.

- **The "up to 74%" headline claim is inconsistent with reported data.** The abstract and introduction state "up to 74% over the non-interactive settings." From Figure 3: Claude Sonnet 4 improves from 40.0% to 61.4% (53.5% relative improvement), Claude Sonnet 3.5 from 24.2% to 39.6% (63.6%), and Claude Haiku 3.5 from 13.4% to 26.8% (100%). No model shows 74% relative improvement. The figure likely derives from gap recovery—(61.4-40.0)/(68.0-40.0) ≈ 76% for Claude Sonnet 4—but the text phrasing ("improvements in performance, up to 74% over the non-interactive settings") reads as relative improvement over the Hidden rate, not gap recovery. This headline figure appears in the abstract, introduction, and Section 3, and its inconsistency with the primary data table undermines a central quantitative claim.

- **Construct validity of synthetic underspecification remains a core concern.** The distributional difference analysis (§2.1) shows that synthetic underspecification uses "more aggressive information removal, specifically targeting code snippets and error messages" compared to natural underspecified issues, which have "concrete technical details, reproducibility information, links to external references, and conversational fragments." The paper acknowledges this gap but argues that external links and conversational style "may not directly impact agent performance." This is speculative—conversational fragments and partial detail may provide recovery clues that agents could exploit, while aggressive synthetic removal may create artificial difficulty. The downstream results (RQ1–RQ3) depend on the synthetic proxy being representative, and the evidence provided suggests it captures only a subset of real underspecification patterns. The paper notes this as a necessary tradeoff (natural examples lack paired ground truth) but does not address the validity gap with additional experiments (e.g., a human study to verify synthetic issues trigger real underspecification behavior).

### Minor

- **The user proxy design introduces a confound in question quality evaluation (RQ3).** The GPT-4o proxy responds "I don't have that information" when queried about details absent from the original issue. The paper states Deepseek's "highly specific implementation questions often exceed user knowledge" (§5.3), but this penalization is an artifact of the proxy's conservative design rather than a property of the question quality itself. Real developers often know implementation details—they simply omit them in bug reports. The paper acknowledges in §7 that "our simulated user proxy may be more cooperative than real users," but this understates the asymmetry: the proxy is simultaneously too cooperative (providing all information from the full issue) and too restrictive (refusing any information beyond the literal issue text). This confounds the comparative analysis of question strategies across models.

- **The navigational oracle confound in the Interaction setting.** The proxy has "access to file locations that need modification and can provide them when queried" (§2.3). Table 1 shows this is consequential—navigational information improves resolve rates for most models (e.g., Deepseek-v2 from 4.62% to 13.19%). This design conflates the value of *clarification interaction* with the value of *having an oracle for file locations*, making it harder to attribute performance gains to question quality versus navigational hints.

- **Claude Sonnet 4 Hidden setting evaluated on only 100/500 instances.** Footnote 4 acknowledges this due to "substantially higher evaluation costs." While statistical significance is reported, the smaller sample size could yield unstable estimates, and Figure 3 presents these results alongside fully-evaluated models without clear visual distinction.

- **Qwen's navigational information worsening (Table 1: 55.43% → 52.38%) is presented as a finding but the difference is small and no significance test is reported.** The 3 percentage point decrease could be noise given the 500-issue sample and the subset of instances where navigational info was requested (18.58%).

## Nice-to-Haves

- A cost-benefit analysis (wall-clock time, API costs) would strengthen the practical relevance of the findings, especially since the paper advocates for interactive agents.
- Ablation decoupling navigational oracle from informational clarification would cleanly separate interaction value components.
- The full distributional difference analysis results should be presented more prominently in the main paper rather than referenced in the appendix.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Construct validity of synthetic underspecification"** as a standalone fatal flaw: The harsh critic framed this as potentially invalidating all downstream results. While it's a legitimate methodological concern, the paper provides partial validation (distributional analysis) and a clear rationale (lack of paired ground truth for natural examples). It's a Major weakness, not fatal, as the high-level findings (interaction helps, models default to non-interactive) likely hold regardless of the synthetic construction specifics.

- **Qwen non-interaction "alternative interpretation"**: The harsh critic suggested Qwen's 45.6% Hidden performance means it might "correctly assess that interaction is unhelpful." While the paper could engage with this interpretation more, Table 2 shows 100% FNR meaning Qwen *never* interacts even when explicitly prompted with strong encouragement—it doesn't selectively choose not to interact. Combined with the finding that Qwen's Interaction setting yields 53.8% (a significant improvement), the "strategic non-interaction" interpretation is inconsistent with the data.

- **Missing cost analysis**: Moved to nice-to-have as this is standard for benchmark papers.

- **Deepseek "counterintuitive behavior" characterization**: The harsh critic called this "a failure of the evaluation framework rather than the model." The paper's characterization is reasonable—if Deepseek performs best with Neutral prompting and degrades with stronger encouragement, that is genuinely counterintuitive behavior worth reporting.

## Novel Insights

The paper's most valuable contribution is the finding that information extraction and information integration are decoupled capabilities: Qwen 3 Coder extracts the most information (highest cosine distance) yet doesn't achieve the best resolve rates, while Claude Sonnet 3.5 and Haiku extract nearly identical information but differ substantially in task performance. This suggests that training paradigms focused on coding capability (where Qwen matches Claude Sonnet 4) do not automatically produce effective interaction behavior, and that the ability to integrate extracted information into a solution plan is a distinct skill requiring dedicated optimization. The complete non-responsiveness of Qwen 3 Coder to all interaction prompts, despite explicit encouragement, further underscores this gap between task-solving and interactive capabilities.

## Suggestions

- **Fix the numerical inconsistency in §5.2.** Either reconcile the 46%/41.8% figures with Figure 3's 53.8%/61.4% (perhaps by explicitly stating these are from a filtered subset or different calculation), or correct the text to match Figure 3.
- **Clarify the "74%" derivation.** State explicitly whether this refers to gap recovery (Interaction−Hidden)/(Full−Hidden) rather than relative improvement (Interaction−Hidden)/Hidden, and ensure the abstract, introduction, and Section 3 all use consistent language.
- **Run a small human study** where software engineers are given the synthetic underspecified issues and asked whether they would seek clarification, to provide direct evidence that the synthetic issues trigger real underspecification recognition.
- **Run an ablation** where the proxy can answer informational questions but cannot provide file locations, to separate the value of clarification from navigational hints.

## Score and Decision

**Calibration anchors retrieved:**

| Round | Anchor | Avg Score | Comparison |
|-------|--------|-----------|------------|
| 1 | SWE-bench (VTF8yNQM66) | 6.25 | Foundational benchmark with simpler analysis; this paper extends it with more sophisticated evaluation |
| 1 | Commit0 (MMwaQEVsAg) | 6.67 | Similar scope (agent benchmark), weaker insights but novel task definition |
| 1 | SWE-Search (G7sIFXugTX) | 4.00 | Narrower contribution (MCTS for agents); this paper is broader in scope |
| 1 | Codev-Bench (c2C2NQKjZw) | 4.25 | Rejected benchmark; less impactful than this paper |
| 1 | SOP-Agent (oWm80iR1m9) | 3.00 | Rejected; less rigorous and relevant |
| 1 | DataSciBench (BltaWJZMeR) | 3.20 | Rejected; weaker benchmark |
| 1 | TaskBench (70xhiS0AQS) | 4.75 | Rejected; weaker evaluation framework |
| 1 | Active Task Disambiguation (JAMxRSXLFz) | 7.33 | Most directly related—also studies clarification questions, but on simpler tasks with a method component; scored higher due to theoretical contribution |
| 1 | τ-bench (roNSXZpUDN) | 6.50 | Agent benchmark with user interaction; comparable analytical depth |
| 1 | AgentBench (zAdUB0aCTQ) | 6.20 | General agent benchmark; less focused |
| 2 | SWE-bench Multimodal (riTiq3i21b) | 5.00 | SWE-bench extension; less novel contribution than this paper |
| 2 | ML-Bench (sf1u3vTRjm) | 5.75 | Rejected SWE-adjacent benchmark; this paper has stronger analytical contribution |
| 2 | τ-bench (roNSXZpUDN) | 6.50 | Directly comparable; this paper addresses harder problem with similar rigor |

**Round 1 bracket:** 5.0–7.0. This paper is stronger than SWE-bench Multimodal (5.0) and ML-Bench (5.75) due to its novel problem formulation and analytical decomposition. It is comparable to τ-bench (6.50) in experimental rigor but addresses a harder problem. It falls below Active Task Disambiguation (7.33), which has a stronger theoretical contribution.

**Round 2 narrowing:** Comparing directly to τ-bench (6.50): this paper tackles a more complex domain (full codebase modification vs. customer service) and provides a more sophisticated multi-step evaluation decomposition. However, τ-bench introduced a novel metric (pass^k) and had cleaner experimental design. The numerical inconsistencies in this paper (74% claim, RQ3 figures) are weaknesses τ-bench doesn't share. On balance, this paper is comparable to τ-bench—slightly stronger in problem importance and analytical framework, slightly weaker in execution precision.

**Final score: 6.0.** The paper addresses a genuinely important and underexplored problem with a well-designed evaluation framework and produces actionable findings. The analytical decomposition is a meaningful methodological contribution. However, the internal numerical inconsistencies (74% headline claim, RQ3 figure mismatch) are concrete errors that weaken confidence in the specific quantitative claims, and the synthetic underspecification construct validity remains an acknowledged but unresolved concern. These prevent scoring higher than the τ-bench anchor at 6.5.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>