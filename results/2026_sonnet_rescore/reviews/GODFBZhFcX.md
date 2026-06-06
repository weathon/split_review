---

## Summary

PCE (Planner-Composer-Evaluator) is a framework for uncertainty-aware planning in decentralized, partially observable multi-agent embodied settings. Rather than relying on frequent inter-agent communication to resolve uncertainty, PCE extracts and organizes the implicit assumptions embedded in LLM reasoning traces into an explicit decision tree, scores each root-to-leaf path by scenario likelihood, conditional gain, and execution cost, and selects actions accordingly. Experiments on two benchmarks (C-WAH: 10 episodes, TDW-MAT: 24 episodes) with three diverse LLM backbones show consistent performance gains over communication-centric baselines, and a user study indicates that PCE's communication patterns are perceived as more efficient and trustworthy.

---

## Strengths

- **Consistent, large-margin task improvements across all three LLMs and both benchmarks.** PCE achieves the best Total Steps (C-WAH) and best transport rates (TDW-MAT) in all 6 LLM × benchmark configurations (Tables 1 & 2). Margins are substantial: e.g., 42.76 vs. 46.80 (second-best REVECA) in C-WAH/GPT-4o mini, and 87.50% vs. 81.25% transport rate in TDW-MAT/GPT-4o mini.

- **Dramatic communication reduction without sacrificing performance.** PCE uses only 1.70 communication actions per episode vs. 9.88 for CoELA in C-WAH/GPT-4o mini (Table 1), demonstrating that principled assumption structuring can genuinely replace repeated dialogue for uncertainty resolution.

- **Scaling ablation (Figure 3) is a compelling standalone contribution.** Increasing Gemma3 from 4B→27B or raising GPT-OSS:20B reasoning depth from Low→High yields only marginal gains for the Planner-only variant, while PCE consistently maintains a large gap, directly supporting the paper's central thesis that structured uncertainty handling is additive to model scaling.

- **Component ablation (Table 3) confirms each module's necessity.** Removing the Planner, Composer, or Evaluator each degrades C-WAH performance (42.76 → 47.34–56.46 steps), establishing that the gains are not attributable to any single architectural choice.

- **Concrete algorithmic contribution.** The Composer's top-down tree expansion over explicit assumption nodes (Section 4.3) and the Evaluator's principled utility formula U(S, a) = L(S)·G(a) − λC(a) (Equation 3) constitute a formal decision-theoretic mechanism that is specific and reproducible, not just a prompting trick.

---

## Weaknesses

### Fatal
None.

### Major

- **Token-efficiency claim is misleading in TDW-MAT.** The abstract states PCE shows "comparable token usage," and Section 5.1 argues for "low Usages." In Table 2, however, PCE consumes **197K tokens vs. CoELA's 113K** (GPT-4o mini) and **337K vs. 237K** (GPT-OSS:20B) — increases of 75% and 42%, respectively. The paper's explanation in Section 5.1 ("this overhead is offset by PCE's substantial reduction in episode length") applies to C-WAH (250-step horizon) but does not straightforwardly hold for TDW-MAT (3000-step horizon), where PCE still uses significantly more tokens despite its better task performance. The paper should either correct the abstract's framing, report per-step token cost alongside per-episode cost, or explicitly acknowledge the trade-off in TDW-MAT. As written, the token-efficiency claim is overclaimed.

- **No variance or statistical testing across very small episode counts.** C-WAH uses **10 episodes**; TDW-MAT uses **24 episodes**. No confidence intervals, bootstrapped variance estimates, or significance tests appear in the main paper. With only 10 episodes, the margin of 42.76 vs. 46.80 steps (PCE vs. REVECA, GPT-4o mini in C-WAH) could plausibly be within noise. The paper repeatedly uses the word "consistent" to describe outperformance, but consistency across 3 LLMs does not substitute for within-condition uncertainty quantification. Bootstrap CIs over 10/24 episodes are straightforward and should be reported to allow honest interpretation of which margins are reliable.

### Minor

- **Core mechanism's calibration quality is not summarized in the main paper.** The Evaluator's action selection depends on LLM-estimated likelihood L(S) and conditional gain G(a) being meaningfully calibrated. The paper acknowledges that "reliability assessments of the Composer and Evaluator based on human-expert correlation studies" are provided in Appendices A.10 and A.11, but provides no summary of the correlation values or quality metrics in the main text. Even one sentence reporting, e.g., the Spearman correlation with human-expert scores, would substantively strengthen the rational action selection argument. As written, the utility function's core claim of "rational action choice" rests on validation results the reader cannot access without the appendix.

- **"w/o Composer" ablation result is notable and unexplained.** Table 3 shows that removing the Composer yields 46.82 Total Steps and only **0.26 communication actions** — nearly zero communication even without the structured tree. This is surprising: if the Evaluator's cost term alone suppresses communication almost entirely, it raises the question of exactly what the Composer's tree structure contributes to the communication-efficiency story vs. simply the Evaluator's design. The paper does not discuss this, leaving the source of the communication reduction partially ambiguous.

- **User study compares PCE against strawman conditions, not the strongest competitive baseline.** Section 5.3 compares PCE against *w/o Com* (no communication) and *Com always* (forced communication every step) — both extremes. The informative comparison for the human-perception claims would be against REVECA, which achieves the second-best quantitative performance. The current design effectively contrasts PCE against worst-case alternatives, inflating the perceived advantage. With 12 participants, this is insufficient to carry the trust and appropriateness claims broadly.

### Trivial

- The stopping criterion for Composer expansion — "stops early when further splits would not materially affect action choice" — is stated vaguely in Section 4.3 without operational specification. The appendix may detail this, but the main text reader cannot determine when early stopping triggers.

---

## Nice-to-Haves

- The scaling ablation (Figure 3) is currently only presented for C-WAH. Replicating it on TDW-MAT would substantially generalize the claim that structured uncertainty handling is complementary to scaling across diverse task structures.
- A brief analysis of representative failure cases (where PCE's structured tree leads to a wrong decision that a baseline would have handled correctly) would increase credibility and help practitioners understand the framework's limits.
- A brief discussion of why uniform hyperparameters (α = β = λ = 1) are a reasonable principled choice, rather than an empirically tuned one, would preempt concern about optimization on the small benchmarks.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"G(a) = 0 when scenario is false is unjustified"** — The harsh critic argues that an action can have nonzero gain even when its motivating scenario is false. However, within PCE's formulation, each leaf action is designed specifically for the assumed scenario at that path. If that scenario is false, the designed action has zero *conditional* gain under the correct scenario — this is a reasonable simplification of expected utility decomposition, not an error. Removed as a misread.

- **Hyperparameter sensitivity overfitting concern (α=β=λ=1)** — While plausible as a concern, the choice of uniform weights = 1 is the simplest possible default and is a common principled choice in multi-objective scoring, not evidence of overfitting to 10 episodes. The paper defers sensitivity analysis to Appendix A.5. Demoted to Nice-to-Have framing.

- **"No prior work has systematically examined scaling for embodied planning" is an overstatement** — The harsh critic flags this, but the paper hedges with "to the best of our knowledge" (Section 2, line 51), which is standard. Removed as a critique of boilerplate hedging language.

- **LLM-estimated calibration is unverifiable without external data** — While calibration validation is relegated to the appendix, per the hard rules, weaknesses rooted in "the appendix may or may not support this" should not be fatal. Retained only as a Minor concern about in-paper summarization, not as a structural flaw.

- **Strength: User study provides strong independent validation** — Weakened by the strawman comparison design and small N=12. Retained as partial support but with appropriate caveats noted in the weakness.

---

## Novel Insights

The paper's most genuinely novel insight — confirmed by the ablation in Table 3 — is that nearly all communication reduction observed in PCE can be achieved by the Evaluator's cost term alone (the "w/o Composer" variant reaches Comm = 0.26 vs. PCE's 1.70), yet task performance still benefits substantially from the full Composer + Evaluator pipeline (46.82 vs. 42.76 steps). This suggests that the decision tree structure is doing work primarily on *action quality and planning coherence*, not on *communication filtering*, which the Evaluator's cost term handles largely independently. The paper does not discuss this decomposition, but it is a meaningful finding for understanding what each module actually contributes — and an important direction for understanding where the gains come from.

---

## Suggestions

1. **Correct or qualify the token-efficiency framing.** Either change the abstract's "comparable token usage" to acknowledge the TDW-MAT overhead, or add a per-step token cost column alongside per-episode cost, making the efficiency trade-off explicit rather than glossed over.
2. **Add bootstrap confidence intervals to Tables 1–2.** With 10/24 episodes, even a ±1σ range over resampled episodes would allow readers to assess which margins are reliable vs. potentially within noise.
3. **Include a one-sentence summary of the human-expert correlation from Appendices A.10–A.11 in Section 5.2.** This directly addresses the question of whether the Evaluator's scored outputs are meaningfully calibrated, which is central to the paper's rational-planning argument.
4. **Add a REVECA condition to the user study**, or at minimum acknowledge the limitation of the current strawman-only design. If REVECA is impractical for a user study, note why.
5. **Discuss the "w/o Composer" ablation result (Comm = 0.26)** explicitly: explain whether communication suppression is primarily from the Evaluator cost term or the Composer's structure, and what this implies about the distribution of credit across modules.

---

## Evaluation on Key Axes

- **Originality:** High. Structuring *implicit assumptions already in LLM traces* into an explicit decision tree and scoring paths via likelihood × gain − cost is a specific and novel mechanism, clearly differentiated from ToT, CoTS, and communication-centric predecessors.
- **Importance of research question:** High. Decentralized embodied multi-agent planning under partial observability is a core challenge, and reducing communication overhead while improving performance addresses a real practical bottleneck.
- **Claims well-supported:** Moderate. Task performance claims are well-supported by consistent cross-backbone results. The token efficiency claim is overstated for TDW-MAT and needs correction. The calibration of the Evaluator's core mechanism is validation-deferred.
- **Soundness of experiments:** Moderate. The multi-LLM, multi-benchmark design is solid. However, the episode counts (10 and 24) without statistical testing weaken the evidential strength of specific margins. The user study design is limited.
- **Clarity of writing:** Good. The architecture is clearly explained; the DEC-POMDP framing is appropriate; figures effectively illustrate the pipeline. Minor vagueness in the Composer stopping criterion.
- **Value to research community:** High. The framework is domain-agnostic, demonstrated across diverse LLMs, and introduces a principled alternative to communication-centric uncertainty handling that other researchers can adopt and extend.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>