Now let me run the calibration search in parallel.Let me read a couple of the most relevant middle-range anchors.Initial bracket: **5.5–7.0**. Commit0 (6.67) and RefactorBench (6.50) are the closest topical anchors. Let me narrow within this bracket.Now I have enough information to write the full meta-review. Let me compile findings.Now I have all the material needed to write the final consolidated review. Let me compose it.

---

## Summary

Ambig-SWE introduces a synthetic underspecified variant of SWE-Bench Verified, paired with an interactive evaluation framework where agents can query a simulated user holding the full specification. The paper structures its evaluation around three research questions: (RQ1) whether LLMs can leverage interaction to improve resolve rates, (RQ2) whether LLMs can detect underspecification, and (RQ3) whether LLMs generate high-quality clarifying questions. Experiments across six proprietary and open-weight models reveal that interaction recovers substantial performance (up to ~90% of full-specification performance for the best model), but detection is brittle and prompt-sensitive, and question-asking strategies vary meaningfully across model families.

---

## Strengths

- **Novel three-capacity decomposition.** The paper cleanly separates underspecification handling into detection (RQ2), clarification quality (RQ3), and task completion with interaction (RQ1), enabling targeted diagnostics rather than a single holistic score. This framing is a structural contribution independent of the specific empirical results.

- **Well-controlled dataset design.** Each of the 500 SWE-Bench Verified issues has a paired fully-specified and underspecified form, enabling causal measurement of interaction impact. The distributional difference analysis comparing synthetic vs. naturally occurring underspecified issues (§2.1) is honest and informative, and the paper's justification for not using naturally underspecified SWE-Bench examples (lack of verified paired ground-truth necessary for causal measurement) is sound.

- **Large, statistically validated performance gains from interaction.** For all six models, the Hidden→Interaction improvement is significant (Wilcoxon Signed-Rank tests, Table 4), and the improvements are substantial: Claude Sonnet 4 achieves ~90% of its fully-specified resolve rate under the Interaction setting (61.4/68.0 = 90.3%). These are the paper's most credible findings.

- **Revealing detection failure modes.** Table 2 demonstrates that even the best-performing model (Claude Sonnet 4) reaches only 89% accuracy in distinguishing underspecified from fully-specified issues, and this only under strong prompting. Qwen 3 Coder's 100% FNR across all prompt conditions is a striking and practically important finding.

- **Broad and diverse model coverage.** Six models — three Claude family sizes, Llama 3.1 70B, Deepseek-v2, and Qwen 3 Coder 480B — are systematically compared across all three RQs. The finding that interaction benefit does not scale linearly with coding ability (Claude Haiku 3.5 achieves similar relative recovery to Sonnet 3.5 despite weaker coding, §3.2) is a concrete and actionable insight for training.

- **Navigational vs. informational analysis.** Table 1's breakdown of question type (navigational vs. informational) and its differential impact per model provides practical design guidance: smaller models over-rely on file-location cues, while stronger models can infer navigation from the codebase. Qwen 3 Coder's anomalous *decrease* in resolve rate with navigational information, supported by qualitative trajectory analysis in §3.3 and §A.7, is an interesting finding.

---

## Weaknesses

### Fatal
None.

### Major

- **RQ1 conflates "compelled to interact" with "appropriately leverages interaction."** Footnote 3 explicitly states: "Here, we modify the prompt to make interaction with the user compulsory in the Interaction setting. Without compulsory interaction, the model defaults to non-interactive behavior for most issues." The research question—"Can LLMs *appropriately* leverage interaction to improve performance?"—implies the models are choosing to interact when appropriate. But the experiment removes this choice entirely. What is measured is "given that interaction occurs, can models use the obtained information?" — a meaningfully weaker claim. This design is justified for practical reasons (models otherwise default to non-interaction), but the framing should be explicit. This also creates a structural tension with RQ2: RQ2 shows models cannot detect when to interact, while RQ1 shows they can use interaction when forced — together these suggest current agents are far from deployable interactive systems, but the paper's overall tone somewhat soft-pedals this gap.

- **GPT-4o plays three interdependent roles, creating an untested coherence risk.** GPT-4o (1) generates the underspecified issues (§2.1), (2) serves as the user proxy that answers agent questions (§2.2), and (3) is the LLM-as-judge scoring question quality in RQ3 (§5.1). A model that generates text with similar stylistic conventions as GPT-4o — or that shares RLHF alignment conventions — could be systematically advantaged across all three roles: its questions may be phrased in a register GPT-4o recognizes well, and GPT-4o may rate GPT-4o-style questions more favorably. The Claude family models, which dominate the positive findings throughout, are the most plausible candidates for this kind of alignment coherence. The paper does not test whether the pattern of findings replicates under an alternative judge or alternative proxy model, leaving the RQ3 results — which rely entirely on GPT-4o-as-judge scores — with an unresolved confound. The cosine-distance metric in RQ3 is independent of GPT-4o and is therefore more trustworthy; the paper should foreground it.

### Minor

- **Detection metric cannot fully distinguish genuine discrimination from indiscriminate interaction propensity.** The RQ2 experiment tracks whether models *interact* when given Full vs. Hidden issues. A model that interacts with 95% of everything achieves low FNR but high FPR — this is labeled "excessive interaction" in the paper (§4.2 on Llama 3.1) rather than what it technically is: a model whose behavior cannot be attributed to genuine detection of underspecificity. The FPR/FNR framing is useful but should be accompanied by a clearer acknowledgment that low FNR in high-FPR regimes does not constitute evidence of detection capability.

- **No variance or confidence intervals on resolve rates.** The paper relies on Wilcoxon tests for the Hidden-vs-Interaction comparison but does not report confidence intervals or standard errors for any of the point estimates in Figure 3 or Table 1. For the Qwen 3 Coder navigational information finding (55.43% vs. 52.38%, a ~3 pp difference), the practical significance is unclear without uncertainty estimates.

- **Claude Sonnet 4 Hidden evaluation on 100/500 instances.** Footnote 4 discloses this. The concern is that Claude Sonnet 4's unusual behavior in the Hidden setting — "extensively explores the codebase and attempts multiple solutions" — may make this subset non-representative, affecting both the baseline for gap-closure calculations and the statistical tests.

### Trivial

- **Deepseek-v2 "counterintuitive" behavior in detection (§4.2)** is flagged but not explained. Deepseek performs best with neutral prompting and degrades under stronger encouragement. The paper labels this counterintuitive but provides no trajectory-level or qualitative analysis. At minimum, a brief hypothesis would make this a useful data point rather than a flag.

---

## Nice-to-Haves

- A small validation on naturally underspecified issues (even 20–30 hand-curated examples with corresponding complete specifications) would substantially strengthen the claim that synthetic underspecification is a valid proxy for real-world underspecification. The paper rightly justifies not using naturally underspecified SWE-Bench instances (no paired ground truth), but a human-curated validation set would address the synthetic distribution shift concern empirically rather than by assumption.

- A "Full + compulsory interaction" control condition would clarify the cost side: if models forced to interact on already-complete specifications also consume additional turns without gaining performance, this would make the Interaction vs. Hidden comparison more interpretable as a measure of benefit rather than cost-agnostic gain.

- Separating binary underspecification judgments from behavioral interaction decisions in RQ2 (ask models to classify first, then act) would provide a cleaner measurement of genuine detection capability.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Critic's "80% figure cannot be verified" claim**: REMOVED as factually incorrect. The paper states "recover up to 80% of the performance in the Full setting," meaning the Interaction resolve rate as a fraction of the Full resolve rate. From the data: Claude Haiku 3.5 achieves 26.8/33.8 = 79.3% ≈ 80%; Claude Sonnet 3.5 achieves 39.6/49.4 = 80.2%. The critic incorrectly computed gap closure (Interaction−Hidden)/(Full−Hidden) instead. The paper's claim is correctly supported by the numbers.

- **"Synthetic distribution shift may confound everything" as fatal**: DEMOTED to Major (GPT-4o triple role) and addressed above. The concern is real but not individually fatal; the paper honestly discloses distributional differences and the resolve-rate findings are not solely dependent on GPT-4o judgment.

- **Absence of external links/conversational fragments in synthetic issues affecting agent performance**: REMOVED as speculative. The paper acknowledges these differences but notes agents cannot access external information, limiting their impact. No specific agent behavior is shown to be affected.

- **Deepseek performing worse than Hidden when file locations are absent** (§3.3): Not a weakness of the paper — this is an empirical finding, not a methodological flaw.

- **Any concerns about model availability or release status**: Not raised, preemptively noted as removable per hard rules.

---

## Novel Insights

The paper's most novel observation is the dissociation between information extraction volume and integration quality: Qwen 3 Coder extracts more information (highest cosine distance, 6.02 avg. questions) but achieves similar or worse resolve rates compared to Claude Sonnet 4 (0.171 vs 0.179 cosine distance, 4.03 avg. questions, similar resolve rates). More strikingly, Qwen 3 Coder's performance actually *decreases* with navigational information (Table 1: 55.43% without, 52.38% with), apparently because it re-explores the codebase after receiving file locations rather than incorporating them directly — a form of "rigid protocol-following" that reveals a training blind spot around incorporating external user input into ongoing agentic trajectories. This suggests a distinct failure mode from simple capability limitations: the model knows the information but cannot update its plan accordingly.

---

## Suggestions

1. **Reframe RQ1's research question** to match its actual measurement: "When models are prompted to interact, can they leverage the obtained information to improve resolve rates?" The current framing ("appropriately leverage") implies voluntary triggering, which the setup explicitly removes.

2. **Foreground cosine distance over LLM-as-judge** scores in the RQ3 discussion, noting that cosine distance is independent of GPT-4o while judge scores share a coherence risk with the user proxy. Reporting both with this caveat would strengthen the result.

3. **Add confidence intervals** to Figure 3 and Table 1 (at minimum) to allow readers to assess whether small differences (e.g., Qwen 3 navigational info) are meaningful.

4. **Report a "forced interaction on Full issues" condition** to characterize the interaction overhead cost and sharpen the efficiency analysis.

5. **Provide trajectory examples for Deepseek-v2's counterintuitive detection pattern** (performance degrading under stronger prompting), similar to the trajectory analysis provided for Qwen 3 Coder.

---

## Score and Decision

**Calibration Summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SWE-bench | VTF8yNQM66.md | 6.25 | R1/R2 | Foundational; introduced the benchmark paradigm Ambig-SWE builds on. More impactful but narrower evaluation. |
| RefactorBench | NiNIthntx7.md | 6.50 | R1/R2 | Accepted; hand-crafted, only GPT-4o evaluated, 100 instances. Ambig-SWE has broader model coverage but lower dataset quality. |
| Commit0 | MMwaQEVsAg.md | 6.67 | R1/R2 | Accepted; more ambitious task (library generation from scratch), thin evaluation. Ambig-SWE more thorough in empirical comparison. |
| ML-Bench | sf1u3vTRjm.md | 5.75 | R1/R2 | Rejected; repo-level code benchmark with narrower contribution. Ambig-SWE addresses a more novel problem dimension (underspecification handling). |
| Entity-Deduction Arena | PfrpYGKGPL.md | 5.50 | R2 | Rejected; conversational clarification benchmark, weaker methodology. Ambig-SWE is considerably more rigorous and task-realistic. |
| D2Coder | dsALpkd1OU.md | 1.67 | R1 | Rejected; agent with debugging tools, fundamentally weaker. |
| DataSciBench | BltaWJZMeR.md | 3.20 | R1 | Rejected; narrower contribution, weaker experimental design. |
| Codev-Bench | c2C2NQKjZw.md | 4.25 | R1 | Rejected; developer code completion benchmark, less novel framing. |

**Round 1 bracket:** 5.5–7.0

**Round 2 narrowing:** The best anchors inside the bracket are SWE-bench (6.25) and RefactorBench (6.50). Ambig-SWE is *weaker* than SWE-bench in originality (derivative of SWE-Bench Verified) but *stronger* in evaluation breadth (6 models vs. SWE-bench's smaller initial model set). Compared to RefactorBench, Ambig-SWE has more instances and models but lower benchmark quality (synthetic vs. hand-crafted) and the RQ1 design gap. Ambig-SWE sits slightly below SWE-bench at **6.0** — it addresses a genuine gap, runs careful experiments, is honest about limitations, and produces actionable insights, but the derivative nature, GPT-4o triple-role concern, and the compulsory-interaction framing mismatch in RQ1 prevent it from reaching the higher end of the bracket.

**Axes assessment:**
- *Originality*: Moderate — extends an established benchmark with a well-motivated new dimension.
- *Importance*: High — underspecification is a real and underexplored problem for deployed code agents.
- *Claim support*: Mixed — RQ1 results are well-supported given the compulsory design, but the framing overstates what is measured; RQ3 judge scores have a coherence risk.
- *Experimental soundness*: Mostly sound — statistically validated main results, honest limitations, but missing variance estimates and a coherent triple-role design.
- *Clarity*: Good — three-RQ structure is clear and the analysis is generally well-presented.
- *Value to community*: Solid — provides a reusable framework and benchmark for future work on interactive code agents.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>