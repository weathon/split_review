Here is my consolidated final review after carefully verifying every claim against the paper.

---

## Summary

This paper proposes a causality-guided debiasing framework for LLMs that models how social category information influences decisions through distinct causal pathways. It derives three prompting strategies (I: nudge toward social-agnostic facts; II: counteract existing selection bias; III: nudge away from social-salient text) and combines them into Dual Directional Prompting (DDP). Experiments on WinoBias (4 models) and BBQ (GPT-4) show DDP substantially reduces bias gaps on WinoBias and improves accuracy on BBQ.

## Strengths

1. **Novel causal formalization of bias pathways.** The causal graphs in Figure 3 explicitly model how social category information flows through "social-agnostic fact" and "social-salient text" representations, and how selection mechanisms in training data introduce bias. This goes beyond ad-hoc prompting approaches by providing a principled, graph-theoretic framework for understanding and designing debiasing strategies.

2. **Strong empirical results on WinoBias with proper bias metrics.** On WinoBias Type I, DDP with GPT-4 achieves a bias gap of only 2.17% (pro vs. anti accuracy) compared to 21.74% for Default and 9.23% for ICL with contrastive examples (Table 1). This pattern holds across GPT-3, GPT-3.5, GPT-4, and Claude 2. The accuracy gap is the standard bias metric for this benchmark and DDP dramatically reduces it.

3. **Informative ablation and error analysis.** Table 2 decomposes DDP into "Fact Only" (Strategy I) and "Counteract Only" (Strategy II), and categorizes errors into those caused by world knowledge (FF) vs. gender bias (TF). This provides direct evidence that the fact-based reasoning component is crucial for bias mitigation, and that improved world knowledge in stronger models translates to better debiasing.

4. **Theoretical guarantee (Theorem 3.1).** The theorem proves that when all three strategies' conditional independence objectives are satisfied, the LLM's decision becomes independent of the social category. This formal result is absent in prior prompting-based debiasing work and provides a clear sufficiency condition.

## Weaknesses

### Fatal

None.

### Major

1. **BBQ experiments do not directly measure bias reduction.** On BBQ, the paper reports only per-category accuracy in the disambiguated setting. A higher accuracy here reflects better general reasoning, not necessarily reduced bias. On WinoBias, the authors correctly use the accuracy gap between pro-stereotypical and anti-stereotypical examples as the bias metric. The same approach should be applied to BBQ — e.g., reporting accuracy broken down by stereotype-consistent vs. stereotype-inconsistent examples, or performance in the ambiguous setting where bias can override the correct "unknown" answer. Without this, the BBQ results do not directly support the paper's central debiasing claim. This is the most significant evidential gap in the paper.

2. **Claim of "unifying" existing prompting-based debiasing methods is unsupported.** The abstract and introduction state that the framework "unifies existing prompting-based debiasing techniques," but the paper never provides a concrete mapping of prior methods onto the three strategies. The only baselines tested are ICL with contrastive examples and zero-shot CoT. The paper does not demonstrate, for example, that Self-Debias, factual-nudge methods, or other approaches can be recovered as instances of Strategy I/II/III. This claim is asserted rather than established.

3. **Connection between formal causal framework and specific prompts is asserted rather than demonstrated.** The conditional independence objectives in Equations (1)–(3) involve unobservable internal representations (explicitly acknowledged by the authors). The paper shows that prompts derived from the framework empirically work, but it does not verify (or attempt to verify) whether the proposed prompts actually satisfy the formal conditions, or whether the causal graph in Figure 3(b) correctly captures the model's internal processing. This weakens the claim that the causal framework *drives* the design rather than serving as a post-hoc rationalization. The empirical contribution stands on its own, but the paper overstates the degree to which the causal framework is validated.

### Minor

1. **Only GPT-4 tested on BBQ.** WinoBias experiments use four models (GPT-3, GPT-3.5, GPT-4, Claude 2), establishing generality. BBQ experiments use only GPT-4, limiting generalizability of the BBQ conclusions.

2. **Selective strategy usage on BBQ without justification.** DDP on BBQ uses Strategies I and III but not Strategy II. On WinoBias, DDP uses Strategies I and II but not III. The paper does not explain why different strategy combinations are used on different benchmarks, making it harder to assess whether the framework genuinely guides the design or whether the strategies are chosen post-hoc.

3. **Overclaiming around "completely removed" bias.** The conclusion states "we also prove that bias can be completely removed from LLMs' decisions when the objectives in all three strategies are satisfied" (line 251). The theorem is technically correct as a conditional statement, but the experiments show only *reduction*, not removal, and the conditions themselves are not verified to be satisfied in practice. The phrasing risks misleading readers into thinking the paper demonstrated complete bias elimination.

4. **Ablation does not separately evaluate Strategy III.** The ablation on WinoBias tests Fact Only (Strategy I) and Counteract Only (Strategy II), but does not test Strategy III (discouraging biased reasoning) in isolation. Since DDP on BBQ uses Strategy III, an ablation of that component would be informative.

5. **Number of ICL examples differs between benchmarks (16 on WinoBias, 8 on BBQ) without justification.** The paper says the BBQ setting "matches" Si et al. (2022), but this inconsistency makes cross-benchmark comparisons harder to interpret.

### Trivial

None.

## Nice-to-Haves

- Reporting confidence intervals or standard deviations for main results (common in some subfields, but single-run evaluation is standard in LLM prompting papers).
- A limitations section acknowledging: (a) the untestability of internal representation independence, (b) reliance on the specific causal graph structure, (c) restriction to U.S. English contexts, (d) dependence on the model's world knowledge which may itself be biased.
- Testing Strategy III ablation separately on WinoBias or BBQ.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"The causal framework and empirical validation are disconnected in a way that undermines the paper's central claim" (presented as fatal by the harsh reviewer).** This is downgraded from fatal to major. The paper does not need to directly verify internal representation-level conditions to validate its framework — the framework provides a *principled design space* for generating prompts, and the empirical success of those prompts is a valid form of validation. Many causal papers in ML use causal graphs as thinking tools without identifying every edge empirically. The criticism has merit (the connection is asserted rather than demonstrated) but is not fatal to the contribution.

2. **"Missing appendix / Discrim-Eval results not shown."** Parser strips appendix sections; these exist in the original submission.

3. **"Missing baseline Self-Debias."** Self-Debias (Schick et al., 2021) is a decoding-time method, not a prompting technique. The paper focuses on prompting-based debiasing for black-box LLMs. Demanding this baseline evaluates the paper against a different class of methods.

4. **"Overlooked debiasing strategy claim is not established."** The prior works cited (Si et al., 2022; Ganguli et al., 2023) use contrastive examples and RLHF respectively — these are not equivalent to the paper's "ask about real-world likelihoods" fact-based reasoning. The claim that this specific approach was overlooked is defensible.

5. **"Selection mechanisms example doesn't connect to LLM prompting."** The paper explicitly states "We will see in Section 3 that such property of selection also applies to NLP contexts" (line 65). This is a standard preliminaries exposition; the connection is made in the following section.

6. **"Strategy III missing from WinoBias ablation."** DDP on WinoBias uses Strategies I+II, not III. Not ablating a strategy that isn't part of the method on that benchmark is not a flaw.

7. **"Unified perspective" (from Strength Finder).** The strength claims unification, but the weakness that this claim is unsupported is verified. Per the rule "when a strength and weakness disagree, the weakness wins," this strength is removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report proper bias metrics on BBQ.** Break down accuracy by stereotype-consistent vs. stereotype-inconsistent examples in the disambiguated setting, or report results on the ambiguous setting (where the correct answer is "unknown" and bias manifests as choosing the wrong entity). This is the single most impactful improvement — without it, the BBQ experiments do not directly support the debiasing thesis.

2. **Either demonstrate the unification claim with concrete mappings from prior methods to the three strategies, or remove/qualify the claim.** At minimum, show how ICL with contrastive examples, zero-shot CoT, and one or two additional methods can be understood as instances of Strategy I, II, or III.

3. **Tone down the "completely removed" language.** Acknowledge that Theorem 3.1 gives a sufficient condition that is aspirational, and that the experiments demonstrate substantial *reduction* rather than elimination.

4. **Justify why different strategy combinations are used on different benchmarks.** If the framework is truly generative/principled, the paper should explain when to use which combination.

5. **Add a limitations section** explicitly discussing the untestability of internal representation-level conditions, the reliance on the assumed causal graph structure, and the scope of the findings.

## Score and Decision

The paper makes a genuine contribution: a novel causal framing of bias in LLM decision-making, three principled strategies derived from it, strong WinoBias results across four models, and an informative ablation. The main issues are (a) the BBQ results lack proper bias metrics, creating an evidential gap for one of the two main benchmarks, (b) the unification claim is asserted but not demonstrated, and (c) some claims are overstated. These are real but addressable weaknesses — none invalidate the core contribution. The causal framework provides genuine conceptual value even if individual causal pathways aren't directly verified, and the WinoBias results are strong and properly measured.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>