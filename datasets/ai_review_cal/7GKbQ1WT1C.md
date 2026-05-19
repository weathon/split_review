- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6
Now I have a thorough understanding of the paper and can synthesize the final consolidated review.

---

## Summary

This paper proposes a causality-guided debiasing framework for LLMs, modeling how social category information influences decisions through different causal pathways connected by selection mechanisms. It derives three prompting strategies (nudge toward social-agnostic fact, counteract existing selection bias, nudge away from social-salient text) and instantiates them as Dual Directional Prompting (DDP). Empirically, DDP substantially reduces bias on WinoBias (GPT-4 gap of 2.17% vs. 14.13% Default) and improves accuracy across 8/9 social categories on BBQ, demonstrating that fact-based reasoning combined with bias counteraction is an effective prompting strategy.

## Strengths

1. **Novel causal modeling of bias through selection mechanisms.** Section 3.1 and Figure 3(a) formalize how selection variables S induce spurious dependencies between social categories and entities/scenarios in training corpora. This is a principled perspective that goes beyond ad-hoc prompting approaches and provides a unifying vocabulary for existing debiasing techniques.

2. **Principled prompting strategies with formal independence objectives.** Section 3.3 derives three distinct strategies (Equations 1–3) with explicit conditional independence targets and concrete example prompts for each. This gives a structured decomposition of debiasing goals (encourage fact-based reasoning vs. discourage biased reasoning) that unifies previously disparate methods.

3. **Theoretical guarantee under the stated conditions.** Theorem 3.1 proves that Y ⟂ A when all three conditional independence constraints hold simultaneously. While the proof itself is straightforward given the graph structure, the theorem formally specifies what combination of conditions achieves complete debiasing in the causal model.

4. **Strong empirical results on WinoBias Type I.** Table 1 shows DDP achieves a gap of 2.17% for GPT-4 (vs. 9.23% ICL, 14.13% Default), with 94.57% accuracy on anti-stereotypical sentences — a substantial and practically meaningful improvement. Results are demonstrated across four models (GPT-3, GPT-3.5, GPT-4, Claude 2), showing consistent benefits.

5. **Insightful error analysis via ablation (Table 2).** The four-way categorization (TT, TF, FT, FF) decomposes errors into world-knowledge gaps vs. gender bias vs. shortcut successes. This diagnostic reveals that GPT-4's improvement over GPT-3.5 stems from better non-gender world knowledge and self-consistency — a valuable finding for understanding when and why the method works.

6. **Effectiveness on subtle bias categories in BBQ.** Table 3 shows DDP improves accuracy on less-obvious dimensions (physical appearance, religion, socio-economic status, sexual orientation) where Default accuracy drops below 70%, demonstrating the method's reach beyond well-regulated categories like age/gender/race.

## Weaknesses

### Fatal

None.

### Major

1. **The causal framework is more descriptive than generative; the gap between prompt text and causal mechanism is not specified.** The paper introduces PPC (Prompt Properly Considered) as a selection node and states that a prompt "directly changes" PPC (Section 3.2), but never explains how a specific natural-language prompt is supposed to set PPC=1 or how PPC interacting with internal representations enforces the claimed conditional independences (Equations 1–3). The mapping from prompt → causal graphical condition is asserted, not mechanistically justified. This does not invalidate the framework as a formal lens — it still offers a useful unification and theoretical vocabulary — but it undercuts the claim that the framework "guides" prompt design rather than retrospectively labeling effective prompts. The framework cannot generate or predict which prompts will satisfy its objectives; it can only describe them after the fact.

2. **Central claim about combining strategies being necessary is not empirically demonstrated.** On WinoBias Type I with GPT-4, DDP's gap (2.17%) equals Strategy I (Fact Only) alone (2.17% from Table 2 ablation), so the combination shows no marginal benefit for the strongest model. On GPT-3.5 Type I, DDP (1.84%) improves over Fact Only (2.87%), but no experiment jointly employs all three strategies — WinoBias uses I+II, BBQ uses I+III, and Strategy III is never tested on WinoBias at all. Theorem 3.1's sufficient condition (all three strategies) is never empirically instantiated. The paper states that "debiasing is better realized when these strategies are combined" (Section 3.3), but this is not substantiated by the experimental design, which tests at most two strategies simultaneously.

3. **Limited evaluation breadth and no variance reporting.** BBQ experiments test only GPT-4, with no results for other models. No confidence intervals, standard deviations, or statistical significance tests are reported for any metric, making it impossible to assess whether reported differences (some of which are small, e.g., 0.13% vs. 0.52% gaps) are robust. The ICL baseline uses a fixed set of 16 (or 8) examples without tuning or cross-validation. The paper claims "extensive studies on three famous benchmarks" (line 156) but results for Discrim-Eval are not presented.

### Minor

4. **Equations (1) and (2) are acknowledged as potentially redundant** (Section 3.3 Remark: "From a purely technical standpoint, Equation (1) and Equation (2) might seem redundant"), which undercuts the advertised three-strategy structure. The paper's defense — that they approach debiasing from different practical perspectives — is reasonable but not empirically validated, as Strategy II (Counteract Only) performs poorly in isolation (Table 2).

5. **DDP's reliance on the model's world knowledge being less biased than its shortcut associations is noted but under-discussed as a limitation.** The error analysis shows 10–30% FF errors (both base and original questions wrong), meaning the method can fail when the model's factual knowledge is itself biased or incomplete. A more thorough discussion of when this assumption breaks would strengthen the paper.

6. **No prompt sensitivity analysis.** DDP's performance may vary with the wording of the base question, the social category, or the specific entities/occupations tested. This is unexplored.

### Trivial

None.

## Nice-to-Haves

- Test all three strategies in a factorial design (I alone, II alone, III alone, I+II, I+III, II+III, I+II+III) on both benchmarks to substantiate the framework's structural claims.
- Run BBQ experiments on additional models (GPT-3.5, Claude 2) to demonstrate generalizability.
- Compare against a simple "do not use stereotypes" direct-instruction baseline to benchmark Strategy III alone.
- Report confidence intervals or paired significance tests.
- Test on open-source models (e.g., Llama-3, Mistral) to enable internal representation analysis, though this is outside the paper's black-box scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not release code or example prompts"**: Reproducibility nitpick about artifacts impractical to include in a submission; the paper provides detailed prompt examples.
- **"No experiments on open-source models"**: Scope creep; the paper explicitly targets closed-source black-box scenarios. Moved to Nice-to-Haves.
- **"Theorem 3.1 is trivial"**: The proof is simple, but the value is in formalizing the sufficient condition, not in proof complexity. The substantive critique about the theorem not being empirically tested is already captured in Major weakness #2.
- **"Missing related works"**: Cannot be verified without external sources.
- **"Typographical / formatting issues"**: Parser artifacts, not author errors.
- **"Missing appendix / proofs in appendix"**: Parser strips appendix sections from all papers.

## Novel Insights

The harsh critic identifies a genuine tension not surfaced in the paper's own framing: DDP's strongest empirical result (GPT-4, WinoBias Type I, 2.17% gap) is achieved by Strategy I alone, making the multi-strategy architecture unnecessary for the paper's headline result. Combined with the critic's observation that the causal framework cannot mechanistically explain why a specific prompt string achieves its claimed conditional independence objectives, this suggests the paper's contribution should be split into two separable pieces: (a) the DDP prompting method, which is empirically effective and independently publishable, and (b) the causal framework, which offers a novel formal language for thinking about debiasing but currently lacks operational teeth. The strength finder correctly identifies that the fine-grained error analysis (Table 2) is a genuinely useful diagnostic tool that future work could build on — it reveals that the method's gains on stronger models come primarily from improved world knowledge self-consistency rather than bias correction per se, which is a nuanced finding that bears on how we evaluate debiasing methods more broadly.

## Suggestions

1. **Disambiguate the paper's two contributions.** The DDP method stands on its own as an effective prompting strategy. The causal framework is a separate contribution that provides a formal language and theoretical guarantee. Make this separation explicit, and clearly delineate what the framework adds beyond what DDP alone achieves.

2. **Run a full factorial ablation** testing all seven combinations of the three strategies on both benchmarks. This is needed to support the claim that combining strategies yields advantages beyond the best single strategy.

3. **Add variance information** (confidence intervals or standard deviations) to all tables, and at minimum report whether differences between conditions are robust across reasonable variations in ICL example selection.

4. **Expand BBQ evaluation** to at least one additional model (GPT-3.5 or Claude 2) to show the method's benefits are not GPT-4-specific.

5. **Acknowledge the framework's limitations more directly.** The paper should state that the mapping from prompt text to PPC=1 is assumed rather than derived, and that the framework provides formal objectives for debiasing but does not mechanistically generate prompts that satisfy them. This would reduce the gap between claims and evidence without diminishing the paper's genuine contributions.
