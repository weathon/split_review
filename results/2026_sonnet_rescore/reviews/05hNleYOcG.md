## Summary
PLAGUE is a three-phase plug-and-play framework for automated multi-turn LLM jailbreaking, consisting of a Planner (retrieves past successful strategies via cosine-similarity-based memory), a Primer (builds adversarial context across n−1 turns using reflection and backtracking), and a Finisher (delivers the final harmful query). The framework incorporates a lifelong-learning memory component that stores successful attack strategies indexed by goal embeddings. Evaluated on HarmBench's 200-goal standard set against five frontier models, PLAGUE achieves an SRE-based ASR of 81.4% on OpenAI o3 and 67.3% on Claude Opus 4.1 — large improvements over the strongest priors on those two resistant models.

---

## Strengths

- **Compelling SOTA results on genuinely hard targets.** Table 2 shows PLAGUE achieves SRE of 0.814 on OpenAI o3 vs. 0.616 for the next best baseline (ActorBreaker), a 32% relative improvement. Table 4 shows 0.673 on Claude Opus 4.1 vs. 0.48 for Crescendo, a 40.2% relative improvement. These two models are widely regarded as highly resistant to jailbreaks, and the margins are large enough to be credible.

- **Rigorous, incremental ablation validates each component.** Table 3 traces the full progression: GOAT alone (SRE 0.587) → +BT (0.612) → +R (0.761) → +P (0.773) → +RSS (0.814) on o3. This step-by-step build-up is more thorough than most jailbreaking papers and directly validates the architectural choices.

- **Demonstrated modularity through Finisher swapping.** Table 4 shows that replacing the GOAT Finisher with a Crescendo Finisher lifts Claude Opus 4.1 from 0.465 to 0.673, outperforming standalone Crescendo (0.48). This concretely validates the plug-and-play design principle.

- **Efficiency analysis with concrete numbers.** Table 5 reports per-model LLM call budgets for all baselines. PLAGUE's total calls (~3.85–6.53) are comparable to Crescendo (~5.28–5.92) and substantially below ActorBreaker (~9.57–9.80), with substantially higher performance.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract headline "improving ASR by more than 30% across leading models" is overstated.** The paper's own Table 2 shows: o1 SRE improvement is ~17% (0.931 vs. 0.798); Deepseek-R1 SRE improvement is 0% (0.978 vs. 0.978 for GOAT); Llama 3.3-70B SRE improvement is ~0.8% (0.958 vs. 0.950). The ≥30% claim holds only for o3 and Claude Opus 4.1. Section 5.1 is more careful ("we outperform the previous best — GOAT by a factor of 32.14% (Table 2) and with Claude's Opus 4.1 … by a margin of 40.2%"), but the abstract's unqualified "across leading models" phrasing will mislead practitioners and reviewers. The claim should be scoped explicitly to the two models where it holds.

- **Asymmetric Crescendo baseline modification.** Section 4 states: "We remove any explicit backtracking counts from their attack and limit their maximum number of turns to six." Backtracking is Crescendo's primary mechanism for recovering from refusals, and PLAGUE retains its own backtracking intact. This asymmetry potentially deflates Crescendo's performance in the comparison. The paper offers no ablation or budget-neutral justification for this removal. Given that Crescendo is the strongest non-PLAGUE baseline on Claude Opus 4.1 (0.48 SRE) and one of the two models that anchor the paper's primary claims, this ambiguity is non-trivial.

- **Post-hoc Finisher selection per model is not disclosed as a design choice in the abstract.** The abstract claims "67.3% on Claude's Opus 4.1," but Table 2 (the main comparison table) reports PLAGUE at SRE 0.465 for that model with a footnote pointing to Table 4. The 0.673 result uses a different Finisher (Crescendo instead of GOAT), chosen after observing that GOAT underperforms. The abstract computes improvements using the best-performing Finisher per model, but this is the result of post-hoc selection rather than a pre-specified configuration. Both Finisher results should appear in Table 2 for all models, or the selection criterion should be stated a priori.

### Minor

- **The lifelong learning component — the paper's titular feature — contributes marginally in the ablation.** Table 3 shows RSS adds +4.1% SRE on o3 (0.773 → 0.814) and +3.4% on Claude Opus 4.1 (0.431 → 0.465), while Reflection contributes +14.9% on o3 (0.612 → 0.761). Section 5.1 even acknowledges "for o3, the largest contribution comes from reflection." The framing in the title, acronym, and abstract foregrounds lifelong learning as the distinctive contribution, but the ablation tells a different story. This disconnect should be acknowledged more clearly.

- **Random-retrieval fallback frequency in the lifelong learning module is unreported.** Section 3.3.1 states: "If fewer than two strategies are retrieved [above the 0.6 similarity threshold], a strategy is randomly retrieved from the library." The library is populated sequentially as the 200 HarmBench goals are processed, starting from just two initialized strategies. It is plausible that a large fraction of early retrievals are random. The actual retrieval rate (similarity-matched vs. random) is never reported, making it impossible to assess how often the semantic retrieval mechanism is truly operative.

- **GOAT "without history" modification lacks supporting data.** Section 4 states: "we also observe that the impact on GOAT's performance with and without an attack history is negligible." GOAT's iterative dialogue relies on prior responses to inform subsequent queries, and this single-sentence assertion — without a table or number — is insufficient justification given that GOAT is both the primary baseline and the Finisher module within PLAGUE.

- **X-Teaming evaluated with "fewer TextGrad steps," with details in Appendix C.4.** Section 5.1 attributes X-Teaming's low performance in Table 6 to this configuration choice. X-Teaming's TextGrad optimization is its core mechanism; evaluating it in a reduced-step configuration should either be justified as budget-neutral or excluded from the main comparison.

### Trivial

- The thresholds 7/10 (Primer backtracking trigger) and 3/10 (Finisher backtracking trigger) are stated as experimental settings but receive no sensitivity analysis. These values directly control how often backtracking occurs and thus affect the call counts in Table 5.

---

## Nice-to-Haves

- **Ablation isolating human-initialized strategies vs. freshly-discovered ones in RSS.** Section 2.1 criticizes AutoDAN-Turbo for relying primarily on human-generated strategies, implicitly claiming PLAGUE's freshly discovered strategies also contribute. This is never isolated. Showing that newly found strategies (beyond the two Crescendo-initialized ones) account for meaningful ASR gains would substantially strengthen the lifelong learning narrative.
- **Alternative attacker model.** Deepseek-R1 is used as the primary Attacker but also achieves 97.8% as an Attack Target — one of the least safety-aligned models tested. A second result with a different attacker (e.g., GPT-4o) would demonstrate generalizability of the framework beyond this specific model choice.
- **Quantitative calibration of the modified StrongREJECT prompt.** Since all baselines are re-evaluated internally, relative comparisons are valid. But a brief note comparing PLAGUE's scores under the original vs. modified prompt on one model would allow readers to contextualize these results against published literature that uses the canonical StrongREJECT prompt.
- **Two-way modularity demonstration.** Table 4 shows Finisher swapping for one model. A symmetric experiment showing a different Planner substitution for a second model would demonstrate that the plug-and-play property generalizes.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Lifelong learning confound from goal ordering"** (Harsh Critic): The concern that goals processed early see a sparser library is conceptually valid, but the paper does not claim that lifelong learning provides uniformly equal benefit to all goals — rather it claims net positive ASR on average. The ordering-sensitivity is a methodological nicety rather than a flaw in the core claim. Demoted to Nice-to-Have territory; not retained as a weakness.

- **"Rubric Scorer vs. Evaluator selection mismatch"** (Harsh Critic, Section 3.5): The Harsh Critic argues that selecting the attempt with the highest Rubric score (R) may systematically differ from the Evaluator's judgment (J). The paper uses temperature 0.0 for J and 0.6 for R and both are grounded in the same rubric dimensions. The concern is speculative and not anchored to any specific example of divergence in the paper.

- **"Is RSS improvement driven by the two initialized Crescendo strategies?"** (Harsh Critic, Section 6): Valid question, but the paper does not directly claim the improvement comes from freshly discovered strategies vs. the initialized ones. Retained as a Nice-to-Have suggestion rather than a weakness.

- **"Strength: problem importance"** (Strength Finder): "Multi-turn jailbreaking is an important problem" — removed as generic; multi-turn jailbreaking importance is not a strength specific to this paper.

- **"X-Teaming in main Table 2"**: The Harsh Critic implies X-Teaming appears in the main comparison table; the paper references Table 6 for X-Teaming and FITD, which appears to be a supplementary comparison. The framing issue is real but partially mitigated by the separation. The concern about reduced TextGrad steps is retained as a Minor weakness but the framing about inclusion in the main table is removed.

---

## Novel Insights

The paper's most under-stated finding is the model-specificity of component contributions revealed in Table 3: for o3, reflection is the dominant driver (contributing ~14.9% SRE vs. ~4.1% for RSS), while for Claude Opus 4.1, backtracking is the dominant driver (contributing ~17.4% SRE vs. ~3.4% for RSS). This suggests that different models have structurally different vulnerabilities to multi-turn attack components — a finding with direct implications for how red-teamers should allocate effort across different target models. The paper notes this (Section 5.1) but does not theorize about why, which represents a missed opportunity for a more principled design insight.

---

## Suggestions

1. **Revise the abstract claim.** Change "improving ASR by more than 30% across leading models" to "improving ASR by 32% on OpenAI o3 and 40% on Claude Opus 4.1, two of the most safety-aligned models evaluated."
2. **Report Crescendo with and without backtracking.** A single-row comparison of Crescendo (official, with backtracking) vs. Crescendo (modified, no backtracking) would confirm or refute that the baseline modification is budget-neutral, directly addressing the fairness concern.
3. **Report per-trial retrieval statistics from the RSS module.** Even a simple table showing the average number of similarity-matched retrievals per goal across the 200-goal run would validate that the semantic retrieval mechanism is operative and not primarily functioning as random injection.
4. **Include both GOAT-Finisher and Crescendo-Finisher in Table 2 for all models.** This would remove the ambiguity about post-hoc Finisher selection and let readers see exactly which configuration is being claimed as "PLAGUE."
5. **Provide supporting data for the GOAT history-disabled claim.** Add even a two-cell comparison (GOAT with/without history on one model) to the ablation table rather than relying on an unsubstantiated sentence.

---

## Assessment on Key Axes

- **Originality**: Moderate-to-high. The three-phase decomposition and goal-embedding-based memory retrieval are meaningful novelties over existing multi-turn attacks, though each individual component (reflection, backtracking, planning) exists in prior work.
- **Importance**: High. Multi-turn jailbreaking is the frontier of LLM safety evaluation, and achieving large gains on o3 and Claude Opus 4.1 — the two strongest aligned models evaluated — is genuinely impactful.
- **Claims supported**: Partially. The core empirical results are solid and ablated. The abstract's "30% across leading models" claim is overclaimed. The per-model Finisher selection and Crescendo modification introduce uncertainty about the magnitude of the true advantage.
- **Soundness**: Moderate. The ablation methodology is above average for this sub-field, but the asymmetric baseline modifications and unreported retrieval fallback rates are real gaps.
- **Clarity**: Good. The three-phase design is clearly explained and the ablation tables are well-structured. The Finisher-selection footnote structure in Table 2 is confusing and needs reworking.
- **Value to community**: High. The modular framework, released as open-source, enables others to build on individual components and provides a systematic evaluation environment for multi-turn jailbreaking research.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>