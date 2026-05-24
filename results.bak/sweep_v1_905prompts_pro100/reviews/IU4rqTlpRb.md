Now I have sufficient data to write the final review. Let me synthesize everything.

---

## Summary

This paper investigates the mechanisms behind *benign relearning* — the phenomenon where forgotten information resurfaces in unlearned LLMs after fine-tuning on benign data. The authors challenge the prevailing view that topical relevance drives relearning, and instead demonstrate that **syntactic similarity** (structural overlap in surface form) is the more consistent driver. Through a re-analysis of the BLUR benchmark (correcting confounds in prior evaluation protocols), a controlled experiment on the TOFU dataset contrasting topically relevant vs. syntactically similar relearn sets, and mechanistic analyses of representation/gradient alignment and template-vs-keyword loss ratios, the paper builds a compelling case. The authors then propose **syntactic diversification** — paraphrasing forget-set queries before unlearning to break structural rigidity — and show it suppresses relearning, accelerates forgetting, and improves model utility.

## Strengths

- **Corrects evaluation confounds in prior work (BLUR).** The paper identifies two issues in BLUR's protocol — unequal step budgets from differently-sized relearn sets, and fixed-step reporting that misses recovery peaks — and demonstrates that controlling for these substantially weakens the claimed topical relevance ordering (Figures 2–3). This is a substantive methodological contribution.

- **Provides converging evidence for the syntactic similarity hypothesis.** The paper does not rely on a single experiment. It triangulates through (a) controlled TOFU experiments across three unlearning methods (GA, NPO, SCRUB) showing syntactically similar relearn sets recover forgotten content more than topically relevant ones (Figure 4), (b) a BLUR re-analysis where syntactic similarity explains recovery patterns better than topical tiers (Table 1), and (c) mechanistic analyses showing syntactically similar data aligns more closely with target-set representations and gradients (Figure 5).

- **Mechanistic depth via loss-ratio analysis (Section 6).** The template-vs-keyword loss ratio analysis (Figure 6) provides genuine insight: unlearning disproportionately suppresses template tokens over keywords due to rigid query-answer syntax, creating a structural pathway that syntactically similar relearning can exploit. This moves beyond correlation to propose a plausible causal mechanism.

- **Proposes and validates a practical defense.** Syntactic diversification (Figure 7) is simple to implement (GPT-4o paraphrasing), grounded in the paper's own mechanistic findings, and demonstrates clear benefits: suppressed relearning (Figure 8), balanced template/keyword suppression (Figure 9), and improved utility across multiple metrics (Table 2).

- **Well-scoped with awareness of practical implications.** Section 8 discusses real deployment concerns (difficulty of filtering syntactically similar requests), limitations of safety training as unlearning, and LoRA-based relearning vulnerabilities, showing the authors understand the broader context beyond the benchmark.

## Weaknesses

### Fatal

None. The core claims are supported by the evidence presented.

### Major

- **The TOFU experiment does not fully isolate syntactic similarity from template identity.** The syntactically similar relearn set ($D_{\text{relearn}}^{\text{syntactic}}$) uses the *exact same question template* as the target set (e.g., "What is the full name of the author born in …?"), differing only in the entities. The topically relevant set uses a *different question form* (e.g., birthplace questions). This means the experiment compares "same template + different entities" vs. "different template + same entities." What it cleanly demonstrates is that exact template matching is sufficient for recovery while topical overlap in a different syntactic form is not — a valuable finding about **template-driven recovery**. But the paper's broader framing — that "syntactic similarity" in general is the primary driver — is not fully tested, since only one (extreme) form of syntactic similarity (template identity) is examined. The BLUR re-analysis and mechanism studies partially bridge this gap but remain correlational. The paper would be stronger if it acknowledged this limitation more explicitly and framed the TOFU finding as demonstrating template-driven recovery specifically, rather than syntactic similarity broadly. This does not invalidate the contribution but qualifies the scope of the strongest causal claim.

### Minor

- **Defense evaluation is limited to TOFU.** Syntactic diversification is tested only on TOFU, against exactly the same syntactically similar relearn set used to demonstrate the vulnerability. Generalization to less template-rigid, more realistic unlearning scenarios (e.g., WMDP, WHP) is not shown. The BLUR re-analysis in Section 4 provides suggestive but only correlational support for syntactic similarity in those benchmarks.

- **Utility comparison in Table 2 lacks explicit forget-quality control.** The paper argues that diversification reduces the number of steps needed for forgetting, thereby improving utility. However, Table 2 does not explicitly state at which unlearning step the utility metrics are measured for each condition, nor whether forget quality is matched. The claim that diversification "alleviates the trade-off between unlearning efficacy and model utility" is plausible given Figures 8–9 but would be strengthened by reporting utility at equivalent forget-quality levels (e.g., at the step where both conditions first reach zero relearn success).

- **Binary keyword-matching metric is brittle.** The Relearn Success Rate assigns 1 only if the exact author name appears in the output. While the paper acknowledges this ("partial matches are therefore scored as 0"), this binary measure may miss graded recovery (e.g., partially correct names, semantically equivalent answers). A complementary soft metric like ROUGE-L on the full answer would add robustness.

### Trivial

- The diversification procedure (GPT-4o paraphrasing, filtering thresholds, number of paraphrases per query) is deferred to the appendix. Key parameters affecting reproducibility should be summarized in the main text.

- No confidence intervals or significance tests are reported for any results, despite the small number of target authors (10 in forget05) and potential instability in recovery trajectories.

## Nice-to-Haves

- A third TOFU condition that varies both factors orthogonally — e.g., a topically relevant set that also shares the target template (e.g., "What is the full name of the author [target author] born in …?") — would disentangle syntax from topic more cleanly.
- Evaluating syntactic diversification on at least one additional dataset (WMDP or WHP) would substantially strengthen the defense's generality claim.
- The LoRA-based relearning observation (Section 8) is interesting but presented without experimental evidence. Either back it with data or mark it as preliminary/observational.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Confound makes it impossible to conclude that syntax rather than topology is the dominant force" (Harsh Critic, framed as fatal):** The experiment is not confounded — it's a standard two-condition design that isolates one factor at a time. The TOFU experiment validly shows that syntactic similarity without topical overlap drives recovery more than topical overlap without syntactic similarity. The legitimate concern is about the *degree* of syntactic similarity tested (template identity), not a confound. Moved from fatal to Major with qualification.

- **"The BLUR re-analysis provides only correlational support, not a causal test" (Harsh Critic):** The paper already acknowledges this implicitly — Section 4 frames the BLUR re-analysis as "motivating a deeper investigation" into syntactic similarity. The TOFU experiment provides the causal test. Demoted from standalone weakness.

- **"Diversification would withstand other syntactically similar patterns (e.g., adversarially chosen)"**: This is scope creep — the paper does not claim adversarial robustness, and testing against adversarially chosen relearn sets is a different research question. Not included as a weakness.

- **Strength Finder's "topically relevant data does not [recover]"**: Overstated. Figure 4 shows some recovery for NPO and SCRUB under topical relearning, just less than syntactic. The actual finding is that syntactic similarity produces *substantially more* recovery, not that topical data produces none.

- **"Variance/statistical significance" concerns from the Harsh Critic**: Filed as Trivial, not a substantive weakness. The TOFU patterns are consistent across methods and steps, making the qualitative conclusions robust even without formal significance tests.

- **"Template-mining similarity and parse-tree similarity" deferred to Appendix I**: The paper already mentions alternatives. Not a weakness.

## Novel Insights

The paper's most original contribution is the template-vs-keyword loss ratio analysis, which reveals a concrete mechanism: unlearning algorithms disproportionately suppress template tokens (the repeated syntactic scaffolding of QA pairs) while under-suppressing keyword tokens (the actual information to be forgotten). This creates a structural vulnerability — syntactically similar fine-tuning restores the suppressed templates, which in turn provides a pathway for keywords to reemerge. This mechanism is distinct from prior explanations (which focused on topical/semantic overlap) and has direct practical implications: it explains *why* diversification works and suggests that simply varying the surface form of forget-set queries is sufficient to substantially improve unlearning robustness. This is a genuinely novel mechanistic insight that reframes how the field should think about unlearning failures.

## Suggestions

- Reframe the TOFU finding more precisely as demonstrating that **template-identity matching** drives recovery, and note that the broader claim about general syntactic similarity is supported by the converging (but partially correlational) evidence from BLUR and mechanism analyses.
- Add a sentence to Table 2 specifying the unlearning step at which utility is measured, and ideally report utility at the first step where forget quality is comparable between conditions.
- Summarize key diversification hyperparameters (number of paraphrases per query, filtering criteria) in the main text rather than only in the appendix.

---

## Score and Decision

### Round 1 bracket: 6.0–7.5

### Round 2 narrowing

**Anchors compared:**
- **fMNRYBvcQN (6.75)**: "Jogging the Memory" — demonstrates relearning attacks but offers no mechanistic explanation or defense. Our paper is analytically deeper and proposes a concrete defense.
- **fXJCqdUSVG (6.50)**: "Evaluating Durability of Safeguards" — critique paper, no defense proposed. Our paper has stronger contribution (mechanism + defense).
- **7erlRDoaV8 (7.50)**: "Can Sensitive Information Be Deleted" — attack-and-defense framework, rigorous threat model, thorough evaluation. Stronger than our paper in evaluation rigor and generality. Our paper has deeper mechanistic analysis but narrower defense evaluation.

Our paper is stronger than the 6.50–6.75 anchors (deeper analysis, defense contribution) but weaker than the 7.50 anchor (narrower evaluation, less general defense testing). The mechanistic depth and practical defense are genuine strengths; the limited defense evaluation and template-identity confound are the main limiting factors.

**Final score: 7.0.** The paper makes a clear, well-supported contribution with a novel mechanistic insight and a practical defense. The major weakness (template-identity vs. general syntactic similarity) qualifies but does not undermine the core contribution, and the defense evaluation limitation is addressable. Compared to the 6.75 anchor (fMNRYBvcQN), this paper offers more analytical depth and a defense; compared to the 7.50 anchor (7erlRDoaV8), it offers stronger mechanism analysis but weaker generality.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>