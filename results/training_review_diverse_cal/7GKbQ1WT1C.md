Now I have a thorough understanding of the paper. Let me synthesize the review, carefully verifying each claim against the paper.

## Summary

This paper proposes a causality-guided debiasing framework for LLMs, using causal graphical models with selection mechanisms to derive three prompting strategies: (I) nudge toward social-agnostic fact, (II) counteract existing selection bias via counterfactual assumptions, and (III) nudge away from social-salient text. The framework unifies existing prompting-based debiasing as "discouraging biased reasoning" or "encouraging fact-based reasoning." Empirically, the proposed Dual Directional Prompting (DDP) — which combines subsets of these strategies — achieves strong results on WinoBias (2.17% gender gap for GPT-4) and BBQ (best accuracy across 8/9 social categories).

## Strengths

**1. Strong empirical results demonstrating the effectiveness of the proposed prompting strategies.** On WinoBias Type I, DDP achieves a gap of only 2.17% for GPT-4, far outperforming baselines (ICL with contrastive examples: 9.23%; Zero-shot COT: 11.41%). On BBQ, DDP achieves the highest accuracy across 8 of 9 social categories, particularly improving subtle ones (physical appearance, religion, socioeconomic status) where Default performs poorly. These results are genuine and impressive.

**2. Genuine contribution in systematically promoting fact-based reasoning for debiasing.** The paper correctly identifies that most existing prompting-based debiasing focuses on discouraging biased reasoning (e.g., "don't use stereotypes"), while the complementary strategy of encouraging social-agnostic fact-based reasoning was largely overlooked. Strategy I — asking the model to reason without the biased attribute and then feeding that reasoning back — is a clever and effective practical technique. The ablation (Table 2) shows that the "Fact Only" component drives most of the improvement, while "Counteract Only" performs poorly alone, confirming the value of this direction.

**3. Informative error analysis via TF/FT/TT/FF categorization.** The ablation study in Table 2 provides mechanistic insight by attributing coreference errors to world-knowledge failures (FF) versus gender bias (TF), and showing that GPT-4's improvement stems from better social-agnostic world knowledge and reduced reliance on gender shortcuts. This goes beyond simple accuracy reporting.

**4. Practical applicability to black-box LLMs.** The framework works via prompting alone, requiring no access to model internals, gradients, or parameters, making it viable for closed-source models like GPT-4 and Claude 2. Base question generation can be automated via regular expressions or a smaller LLM.

## Weaknesses

### Fatal
None.

### Major

**1. The full combination of all three strategies (I+II+III) is never empirically tested, directly undermining the central theoretical claim.** Theorem 3.1 states that when all three strategies' objectives are simultaneously satisfied, the LLM's decision becomes conditionally independent of the social category (Y ⟂ A | S=1, PPC=1). Yet:

- **WinoBias DDP uses only Strategy I + Strategy II.** Strategy III (discouraging biased reasoning by nudging away from social-salient text) is not included. The paper explicitly states: "On top of Strategy I, we also add the prompt that both occupations are equally likely to be male or female to in order to counteract existing selection bias (Strategy II)" (Section 4.1.1).

- **BBQ DDP uses only Strategy I + Strategy III.** Strategy II (counteracting existing selection bias) is not used. The paper states: "To encourage fact-based reasoning... (Strategy I). To discourage biased reasoning, we ask it not to use the information related to the underlying social category when making the decision (Strategy III)" (Section 4.2.1).

- **The ablation (Table 2) separates Strategy I and Strategy II individually**, but never tests the triple combination or Strategy III individually.

The paper's framework claims that "debiasing is better realized when these strategies are combined" and that the theorem provides a guarantee for the full combination. But no experiment actually evaluates that full combination. This is a significant gap between the theoretical framing and the empirical validation. The paper should either test I+II+III together or clearly tone down the claim that all three are needed for comprehensive debiasing.

**2. The causal framework is presented with formal language that overstates its rigor.** The paper calls Theorem 3.1 a "proof" (line 147), but the argument is a high-level sketch that does not constitute a formal derivation. The "proof" says: "There are two direct parents of Y. To enforce the independence between Y and A, a sufficient condition is that both direct parents of Y are independent of A..." — this is a restatement of the claim rather than a derivation from Equations (1)–(3). It does not account for possible dependencies through ancestors of the parent nodes or verify that the graphical conditions entail the claimed independences. Additionally, the premises (Equations 1–3) involve unobservable internal representations, making them untestable in practice. For an empirical prompting paper, this level of formality is unnecessary; presenting the theorem as a motivating sufficient-condition sketch rather than a formal guarantee would better match what is actually established.

### Minor

**3. The "unification of existing methods" claim is asserted rather than demonstrated.** The paper states that "current prompting-based debiasing methods can be viewed as instantiating one or both of these goals" (Section 1) and that the framework "offering a unified view of existing prompting-based methods." However, the only existing methods explicitly discussed are ICL with contrastive examples and zero-shot CoT. The paper does not systematically map specific published methods (e.g., anti-stereotypical instructions, fairness-focused role prompts, counterfactual data augmentation via prompting) to the causal graph or strategy categories. Either provide explicit mappings or soften the unification claim.

**4. Limited discussion of failure modes and limitations.** The paper does not address: (a) scenarios where the model's world knowledge is itself biased (e.g., believing nurses are predominantly female), where Strategy I could reinforce rather than counter bias; (b) the need to manually identify the social category and construct base questions for each task; (c) potential scalability issues when applying to many bias dimensions simultaneously; (d) the reliance on the model being "well-trained and well-aligned" for PPC to function as intended — a significant assumption that is not validated.

### Trivial
None.

## Nice-to-Haves

- Test the full I+II+III combination on at least one benchmark to validate Theorem 3.1's claim empirically.
- Include a per-category breakdown on WinoBias (male vs. female stereotypes) for deeper insight.
- Investigate cases where fact-based reasoning fails because the model's world knowledge is itself biased.
- Provide a more explicit mapping of existing prompting-based debiasing methods (beyond ICL and CoT) to strategy categories I/II/III.

## Removed Points

- **Discrim-Eval results are absent**: The paper mentions Discrim-Eval as a third benchmark (line 156) but does not show results in the extracted text. Per the hard rules, Discrim-Eval results are assumed to exist in the appendix (stripped by parser). This criticism is removed.
- **"Prompts do not select data points" / selection mechanism mismatch**: This criticism misunderstands the paper's framing. The paper uses selection mechanisms as an analogy for how prompts condition the model's processing distribution, not as formal data-point selection. The paper explicitly acknowledges (Section 3.2) that prompts do not act as causal interventions on internal nodes. The criticism demands a level of causal rigor that the paper never claims to provide for the prompting part.
- **Strength Finder's "Theoretical guarantee" and "Novel causal formalization that unifies"**: These conflict with verified weaknesses (Theorem 3.1 proof is weak; unification claim overstated). Per the rules, when a strength and verified weakness disagree, the weakness wins. These are removed or downgraded.

## Novel Insights

The most striking observation from comparing the reviewer inputs is that both the harsh critic and the strength finder converge on the same core assessment: the paper's practical prompting strategies (particularly the fact-based reasoning approach) are genuinely effective and empirically well-supported, but the causal formalism wrapping them adds little beyond what an intuitive, heuristic framing would provide. The harsh critic's most damaging points — the untested three-strategy combination and the weak theorem proof — are not about the method's effectiveness but about the gap between what the paper claims its formalism achieves and what it actually demonstrates. This suggests the paper's strongest contribution is the DDP method itself and the identification of fact-based reasoning as a debiasing strategy, which could stand without the causal scaffolding.

## Suggestions

1. **Test the full I+II+III combination** on at least one benchmark to close the gap between Theorem 3.1 and the experimental section. If the full combination does not outperform I+II or I+III, that is informative too and should be honestly reported.
2. **Reframe Theorem 3.1** as a sufficient-condition sketch rather than a formal theorem with a proof. The current language ("Proof.") sets expectations of rigor that are not met.
3. **Soften the unification claim** unless specific mappings to diverse existing methods are provided. A simple claim like "our framework categorizes debiasing strategies into two complementary goals" is defensible and accurate.
4. **Add a limitations section** discussing when fact-based reasoning might fail, the effort required to construct base questions, and the assumption that LLMs faithfully follow PPC conditioning.
5. **Consider whether the causal graph framework is necessary at all** — the paper might be better received as an empirical paper with intuitively motivated heuristics rather than wrapped in formalism that invites scrutiny it cannot satisfy.

## Score and Decision

This paper makes a genuine empirical contribution: the DDP prompting method is effective and demonstrates the value of fact-based reasoning for debiasing, which has been relatively overlooked. The results on WinoBias and BBQ are strong and clearly presented. However, the paper's packaging — particularly the causal formalism with unsubstantiated "theorem" claims, the assertion-based unification language, and the gap between the claimed comprehensive debiasing guarantee and the experiments (which never test the full triple strategy) — weakens what would otherwise be a solid empirical contribution. These issues are addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>