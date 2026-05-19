Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper studies whether sensitive information can be truly deleted from LLMs via model editing. It introduces a threat model based on a candidate-set budget B (the information is insecure if the answer lies among B candidates), proposes whitebox (Head Projection, Probability Delta) and blackbox (Input Rephrasing) extraction attacks, and develops defense objectives (Max-Entropy, Head Projection Defense, Input Rephrasing Defense). Experiments on GPT-J show that even after editing with ROME/MEMIT, "deleted" information can be recovered 38% of the time (B=20) via whitebox attacks and 29% via blackbox attacks. The Max-Entropy defense reduces whitebox attack success to as low as 1.7% without significantly damaging model knowledge, but no single defense works against all attacks.

## Strengths

- **Novel threat model with practical grounding**: The AttackSuccess@B metric, motivated by three concrete scenarios (password attempts, parallel pursuit, data-owner verification), formalizes a more realistic standard than the typical one-shot (B=1) evaluation (Sec. 3.1). This reframes the deletion problem in a practically meaningful way.

- **Demonstrates that editing methods leave recoverable traces in hidden states**: The paper exploits an interpretability insight — that information accrues in intermediate hidden states — to design whitebox attacks that recover "deleted" answers 38% (Head Projection) and 38% (Probability Delta) of the time at B=20 (Fig. 2, Sec. 7.1). This directly supports the paper's central claim that deletion is surprisingly difficult.

- **Proposes a defense that is remarkably effective against whitebox attacks**: The Max-Entropy defense reduces Head Projection attack success from 22.2% (Fact Erasure baseline) to 1.7% on CounterFact with ROME, while maintaining low Random Δ-Acc (0.69) and high Rewrite Score (99.73) (Table 1). It also substantially mitigates the unforeseen Probability Delta attack (e.g., 43.8%→2.4% on zsRE with ROME), showing robustness beyond the exact threat it was designed for (Sec. 7.3).

- **Systematic comparison across editing methods, datasets, and defense/attack combinations**: Experiments cover both ROME and MEMIT editing methods, two datasets (CounterFact and zsRE), with careful filtering to facts known by the model (Sec. 6). The finding that MEMIT is consistently more vulnerable than ROME, and that the Input Rephrasing Defense systematically fails, are informative results that guide future work.

## Weaknesses

### Fatal

None.

### Major

- **Experiments are limited to single-token answers, limiting generalization of headline claims**: The paper explicitly states (Sec. 4.1): "Note we limit our experiments to datapoints with single-token answers for simplicity." While the paper suggests the logit lens "could be readily applied in a manner similar to autoregressive decoding," this extension is neither implemented nor validated. Real sensitive information (phone numbers, addresses, sentences describing harmful knowledge) is almost always multi-token. The headline findings — 38% whitebox attack success, 29% blackbox success — are therefore only directly supported for single-token facts. The blackbox attack does naturally extend to multi-token through sampling, but the paper evaluates it on the same single-token subset for consistency. This gap means the paper's central empirical claims about how difficult it is to delete "sensitive information" are not yet shown to hold for the most practically relevant forms of such information.

### Minor

- **No variance or confidence intervals for main results**: AttackSuccess@B and Δ-Acc scores are reported as point estimates over 587 (CounterFact) and 454 (zsRE) datapoints (Table 1, Fig. 2). Without error bars or confidence intervals, it is difficult to assess whether reported differences between defenses (e.g., 1.7% vs. 22.2%) are statistically reliable or could be artifacts of the specific data sample. This is common practice in some subfields but does weaken the precision of comparative claims.

- **Introduction claims results for Llama-2 that are not presented in the main paper**: The introduction states "In experiments with GPT-J and Llama-2, we show that... we are able to extract the 'deleted' answer from the hidden states a full 38% of the time." The experiment setup lists GPT-J, Llama-2, and GPT2-XL (Sec. 6), but the results section (Sec. 7) and all main tables/figures only report results for GPT-J. This creates a misleading impression about the breadth of the empirical support. If results for Llama-2 and GPT2-XL are relegated to the appendix, the main text should at minimum summarize the key qualitative findings for those models.

- **The failure of the Input Rephrasing Defense and the relative weakness of Head Projection Defense vs. Max-Entropy are noted but not analyzed**: The paper reports that (a) the Input Rephrasing Defense does not reduce blackbox attack success, and (b) the simpler Max-Entropy defense outperforms the Head Projection Defense that was specifically designed for the Head Projection attack. These are interesting findings, but the paper does not explore potential reasons (e.g., does Input Rephrasing Defense fail because the paraphrases used for defense differ from those used in the attack? Does Head Projection Defense underperform because the max-margin loss is too permissive?). Adding diagnostic analysis would make the paper more informative as a design study.

### Trivial

- The abstract contains a typo: "tractable but difficult problem, since even relatively low attack success rates have potentially severe implications" — the sentence structure is slightly awkward.
- In the conclusion (Sec. 8), "deleting sensitive inormation" has a typo ("inormation").

## Nice-to-Haves

- Extend at least one experiment to multi-token answers (e.g., using beam search with logit-lens distributions over a small set of multi-token facts). This would dramatically strengthen confidence in the paper's generalizability.
- Discuss computational cost of the proposed defenses (number of gradient steps, additional training time) since this is relevant for practitioners.
- Include a brief discussion of adaptive attacks — an attacker aware of the Max-Entropy defense could potentially try other probing techniques targeting different layer sets or representations.

## Removed Points

These points are flagged for removal; treat them with caution.

- **"The paper does not compare to other unlearning approaches"** (Harsh Critic): Removed. The paper explicitly argues why model editing is the appropriate framing (Sec. 2, Related Work) and scopes itself accordingly. Demanding comparisons to gradient-ascent unlearning, influence-function removal, etc. is scope creep. The paper is about whether *model editing* can delete information, and it evaluates that claim on its own terms.

- **"Results for additional models missing from the main paper"** framed as a reproducibility concern: This point is partially retained above as a presentation issue, but removed as a reproducibility concern. The appendix (which is stripped by the parser) may contain these results. The criticism retained above is about the *main paper's* misleading framing, not about missing appendix content.

- **"No discussion of computational cost"**: Removed as a minor/nice-to-have suggestion, not a weakness.

- **"The paper does not discuss adaptive attacks"**: Removed. The paper discusses "unforeseen attacks" in Sec. 7.3 and explicitly acknowledges that defense methods may always be playing catch-up to new attack methods (Conclusion item 4). This is adequately addressed.

## Novel Insights

The cross-review surfaces one interesting observation not fully developed by the paper: the Max-Entropy defense consistently outperforms the Head Projection Defense against the very attack the latter was designed for. This is counterintuitive — a generic entropy-maximization objective beats a targeted max-margin loss on the specific phenomenon it targets. The paper notes this but does not diagnose it. A plausible hypothesis (not in the paper) is that the max-margin loss only suppresses the target token below a fixed threshold, while entropy maximization flattens the entire distribution, making it harder for an attacker to find *any* high-confidence token path to the answer. This could also explain why Max-Entropy generalizes better to the unforeseen Probability Delta attack. Future work could test this by measuring the rank of the target answer across layers under each defense.

## Suggestions

1. **Extend to multi-token answers** — This is the most impactful improvement. Even a small-scale experiment (e.g., 50–100 multi-token facts evaluated with a beam-search extension of the logit lens) would significantly strengthen the paper's claims about real-world applicability.

2. **Add bootstrapped confidence intervals** for all AttackSuccess@B and Δ-Acc metrics in the main table. This would allow readers to assess the reliability of comparisons between methods.

3. **Clarify the model scope** — Either add a brief summary of Llama-2/GPT2-XL results in the main paper (even a sentence like "Results with Llama-2 and GPT2-XL confirm the same qualitative patterns; see Appendix X for details") or revise the introduction to avoid claiming results for models whose data appear only in the appendix.

4. **Diagnose the Head Projection Defense failure and Input Rephrasing Defense failure** — Add an ablation or analysis (e.g., measuring the rank of the target answer across layers after each defense, or varying the number of defense paraphrases) to turn these negative results into actionable insights for future work.

## Score and Decision

This is a solid paper with a well-motivated problem, a novel threat model, clever attacks, and an effective defense (Max-Entropy). The weaknesses are real but addressable: the single-token limitation is the most significant gap, and the missing variance estimates and misleading model claims in the main paper are presentation issues that can be fixed. The paper's core contributions — showing that editing methods leave recoverable traces in hidden states, and that entropy maximization can mitigate whitebox extraction — are valuable and well-supported within the stated scope.

I recommend acceptance. The paper should address the single-token limitation (or clearly scope claims to single-token facts), add confidence intervals, and clarify the model results in the main text.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>