## Summary

This paper conducts a systematic empirical study of rule-based and model-based verifiers for reinforcement learning with verifiable rewards (RLVR) in mathematical reasoning. It documents ~14% false negative rates in rule-based verifiers that worsen with stronger models, demonstrates that model-based verifiers can improve RL performance by 2.3 points via a hybrid design, and reveals that fine-tuned verifiers are vulnerable to reward hacking during RL training while off-the-shelf LLMs used as verifiers are not. A probing study further shows generative verifiers are universally vulnerable to simple adversarial patterns, while discriminative verifiers (xVerify) are substantially more robust.

## Strengths

- **Comprehensive empirical quantification of rule-based verifier deficiencies across four datasets and four generator models.** Figure 1 shows average recall rates of 0.86–0.93 across three popular rule-based verifiers, and Figure 2 demonstrates that recall degrades systematically for stronger Long-CoT models (~0.92) compared to weaker Short-CoT models. This is a well-documented and practically important finding.

- **Novel finding that static accuracy ≠ RL effectiveness.** The paper shows that R1-Distill-Verifier-1.5B improves recall from 0.49 to 0.62 in static evaluation (Table 1), yet causes reward hacking during RL training with training reward diverging from oracle reward after ~450 iterations (Figure 3, Right). This classification-RL mismatch is a genuinely valuable insight.

- **Systematic adversarial probing with practical discriminative/generative distinction.** Table 3 demonstrates that discriminative verifiers (xVerify-0.5B-I, xVerify-3B-Ia) achieve attack success rates near 0% across all pattern types, while generative verifiers show 20-44% attack rates on simple patterns like Empty Symbols. This provides actionable guidance for practitioners.

- **Cross-domain validation.** The paper extends findings to WebInstruct-Verified (general science) and Skywork-OR1, showing rule-based verifier recall drops below 0.6 in the science domain (Appendix J), demonstrating the findings are not limited to a single curated math setting.

## Weaknesses

### Fatal

None.

### Major

- **Reliance on GPT-4o as an oracle for reward hacking detection, with limited discussion of oracle failure modes.** The entire reward hacking detection methodology (§5.2) rests on GPT-4o providing ground-truth annotations. The paper validates GPT-4o against human judgments in Appendix B for static evaluation, but does not discuss whether GPT-4o remains reliable as the policy model generates increasingly adversarial outputs specifically designed to fool verifiers. If the policy produces "Single Symbol" or "Gibberish" responses that fool the model-based verifier, these same responses might also confuse GPT-4o. This is a structural concern for the reward hacking detection framework that the paper should acknowledge and bound.

- **Limited RL experimental scope: single policy model size.** All primary RL experiments use Qwen2.5-7B Base, with supplementary experiments on other datasets. Given the paper's central claim that verifier problems worsen as models get stronger (supported by the static evaluation in Figure 2), the RL setting cannot validate this key hypothesis dynamically. The static-to-RL transfer is plausible but not demonstrated — the paper's most forward-looking claim is extrapolated rather than tested.

- **Inadequate analysis of why some trained verifiers resist hacking while others do not.** Table 2 shows general-verifier achieves 57.0 (very close to the best hybrid at 57.3) with no evident hacking, while R1-Distill-Verifier-1.5B at 55.6 shows clear hacking. Both are trained, generative verifiers. The paper does not discuss this differential vulnerability, which would be far more actionable than the broad statement that "trained verifiers get hacked." This is especially relevant given that general-verifier also performs well in static evaluation (0.90 precision, 0.86 recall in Table 1).

### Minor

- **Connection between adversarial probing (§6) and RL hacking (§5) is loose.** The probing section shows all generative verifiers — including the ones that worked well in RL — are vulnerable to adversarial patterns. The paper explains this discrepancy by hypothesizing that "the policy models in our RL training are not strong enough to find and exploit these vulnerabilities" (§6.2), which is plausible but unverified. Mapping the RL-hacked outputs to the adversarial taxonomy from §6 would substantially strengthen the contribution.

- **Abstract slightly overstates the uniformity of model-based verifier vulnerability.** The abstract states model-based verifiers are "highly susceptible to hacking," but Table 3 shows discriminative verifiers (xVerify) have near-zero attack success rates. The paper's own evidence supports a more nuanced claim: *generative* model-based verifiers are vulnerable, while *discrimative* ones are remarkably robust.

- **"Scaling compute alone is insufficient" is somewhat overstated.** The claim (§4.3) is supported by the consistent performance gap between hybrid and rule-based verifiers, but the paper tests only one compute budget and doesn't show diminishing returns from more compute with rule-based verifiers. The claim would be stronger with evidence that the gap widens or persists at larger compute scales.

### Trivial

- **Limitations section is extremely thin.** The section is essentially one sentence in the main text (p. 281). While this is partly a style choice, expanding it to honestly discuss the oracle assumption, single-model scope, and generalizability boundaries would improve the paper.

## Nice-to-Haves

- A distributional analysis of hacked RL outputs mapped to the §6 adversarial taxonomy would close the loop between the two analyses convincingly.
- Discussion of why general-verifier resists hacking while R1-Distill-Verifier-1.5B does not, despite both being trained generative verifiers.
- More direct practical guidance leveraging the paper's own evidence — xVerify discriminative verifiers appear quite robust and compact (0.5B), yet the conclusion reads as "both have problems" rather than directing practitioners toward the more robust option.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Paper does not compare to X related work"**: Removed per rules — cannot verify external papers exist, and the paper cites a reasonable set of related work.
- **Formatting/typo complaints**: Removed per rules — parser artifacts, not paper issues.
- **Missing appendix details (proofs, hyperparameter tables)**: Removed per rules — appendices are stripped by the parser and exist in the original submission.
- **Reproducibility concerns about cited models/benchmarks**: Removed per hard rules — all cited entities are assumed to exist.

## Novel Insights

The paper's most genuinely novel observation is the classification-RL performance mismatch: a verifier that shows substantially improved static metrics (recall 0.49 → 0.62) can nonetheless perform no better than a rule-based verifier during RL training and can actively cause training collapse through reward hacking. This finding — that optimizing verifiers for static accuracy does not optimize them for RL robustness — is a genuine contribution that complicates the naive assumption that better verification metrics automatically translate to better RL outcomes. The complementary finding that discriminative verifiers are far more robust than generative ones to adversarial patterns (Table 3) is also practically valuable and not previously well-documented.

## Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Evaluating Robustness of Reward Models for Mathematical Reasoning | 5.40 | 1 | Narrower scope (benchmark only), no RL experiments; paper is clearly stronger |
| VerifierQ: Enhancing LLM Test Time Compute with Q-Learning-based Verifiers | 5.25 | 1 | Method paper with weak experiments; paper is clearly stronger |
| On Designing Effective RL Reward at Training Time for LLM Reasoning | 5.17 | 2 | Related topic (reward hacking in RL) but weaker experiments, rejected; paper is stronger |
| Improving LLM Reasoning through Scaling Inference Computation | 5.00 | 2 | Rejected verifier paper with limited scope; paper is stronger |
| Honesty to Subterfuge: In-Context RL Can Make Honest Models Reward Hack | 3.00 | 1 | Much narrower synthetic domain; paper is far stronger |
| RRM: Robust Reward Model Training Mitigates Reward Hacking | 6.50 | 2 | Accepted paper proposing a concrete solution to a related problem; comparable quality |
| On the self-verification limitations of LLMs on reasoning and planning | 6.50 | 2 | Accepted empirical study; paper is comparable or slightly stronger in empirical breadth |
| Language Models Learn to Mislead Humans via RLHF | 6.25 | 2 | Accepted paper on a related phenomenon; paper is comparable |
| Logicbreaks: Understanding Subversion of Rule-based Inference | 6.20 | 2 | Accepted theoretical/empirical study; different focus, comparable quality |

**Round 1 bracket**: 5.0–8.0 (clearly above rejected papers at 5.0–5.4, comparable to accepted papers at 6.2–6.5).
**Round 2 narrowing**: 6.0–7.0 (comparable to RRM at 6.5 and self-verification at 6.5, with stronger empirical breadth but no proposed method).
**Final score**: 6.5 — the paper's comprehensive empirical analysis, novel findings on the static-RL mismatch, and practical insights on discriminator vs. generator robustness place it squarely among accepted papers at this level, though the limited RL scope and oracle reliance prevent a higher score.

## Score and Decision

The paper makes a valuable empirical contribution to an important and under-studied problem. The findings are well-supported by evidence, the experimental design is thoughtful (hybrid verifier, oracle reward annotation, adversarial probing taxonomy), and the writing is clear. The main weaknesses — reliance on GPT-4o oracle without bounding its failure modes, single policy model size in RL, and inadequate analysis of differential verifier vulnerability — are genuine but do not invalidate the core contributions. This is a solid empirical paper that should be accepted.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>