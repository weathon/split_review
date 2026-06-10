## Summary

This paper proposes MACPO, a multi-agent framework for weak-to-strong alignment of LLMs. The core idea is to have multiple weak teachers (7b models) and one strong student (70b) iteratively learn from each other by reinforcing "unfamiliar positive behaviors" (cross-agent outputs) and penalizing "familiar negative behaviors" (self-generated negative outputs from models fine-tuned on negative data). Experiments on HH-RLHF and PKU-SafeRLHF datasets claim consistent improvements across automatic and human evaluations, with the key finding that increasing the number of weak teachers enables more iterative rounds without collapse.

## Strengths

- **Weak teachers improve over iterations, supporting the mutual-learning thesis**: Figure 4 (RQ4) shows all three weak teacher models (Llama2-7b, Mistral-7b, Llama3-8b) improving alignment scores steadily across iterations, directly demonstrating that MACPO benefits the teachers themselves — something prior weak-to-strong methods (Burns et al. 2023) do not achieve. This is a concrete, non-trivial finding.

- **Scaling the number of weak teachers from 1 to 3 prevents iterative collapse**: Figure 3 (RQ3) shows that with a single weak teacher, strong student performance degrades after iteration 2, while with three teachers it improves across all three iterations on all datasets. This provides clear evidence that diversity of supervision sources matters, and the effect is replicated across HH-Helpful, HH-Harmless, and PKU-SafeRLHF.

- **Ablation study cleanly isolates three design choices**: Section 5.5 tests -MP (remove mutual positive augmentation → self-alignment), -HN (remove hard negatives → only positive reinforcement), and -IW (freeze weak teachers). Each removal degrades performance, with -MP causing collapse by iteration 2. This directly supports the claim that both mutual augmentation and hard negatives are necessary and complementary.

## Weaknesses

### Fatal

None.

### Major

- **Extraordinary claim about weak teachers with insufficient evidence**: Line 315 states that weak teachers (7b models) "outperform state-of-the-art baselines of strong students" (70b model trained with SOTA methods). This is an extraordinary finding — 7b models surpassing a 70b model trained with established alignment methods — that would dominate the paper's significance if true. The supporting evidence is only Figure 4 (figures whose numerical values are not accessible from the extracted text), with no explicit numerical comparison, no specification of which baselines are being outperformed, no error bars, and no statistical tests. An extraordinary claim requires commensurate evidence; the paper provides a figure caption and a single sentence. The paper's core contribution does not depend on this specific claim, but as presented it represents a significant overclaim that undermines trust in the paper's reporting standards.

### Minor

- **The "unfamiliar positive behavior" framing is somewhat inconsistent with the actual filtering mechanism**: The paper's central narrative emphasizes "reinforcing unfamiliar positive behaviors," but the perplexity filter (Eq. 6–7) selects outputs with the *lowest* perplexity according to the strong student's own distribution — i.e., outputs the model already finds most *familiar*. The term "unfamiliar" is better understood as "not self-generated" throughout the paper, but the continuous juxtaposition of "unfamiliar positive" vs. "familiar negative" creates a misleading contrast. The mechanism itself is reasonable (cross-agent quality-filtered supervision), but the framing over-inflates the conceptual novelty.

- **The "hard negative behavioral data" is never defined**: The paper repeatedly references "fine-tuning on negative behavioral data" (lines 27, 141) to initialize negative agents, but never specifies what this data is. Is it the dispreferred responses from the preference datasets? A separate corpus of harmful outputs? Something else? A reader cannot reproduce or evaluate a core component of the method. This is a straightforward documentation gap — one sentence would resolve it.

- **The perplexity formula (Eq. 6) is mathematically incorrect as written**: The equation computes `nth_root( 1 / Σ P(y_m | ...) )`, which sums probabilities rather than multiplying them (or summing log probabilities). Standard perplexity is `exp(-1/n · Σ log P) = (Π P)^(-1/n)`. As written, the formula does not compute perplexity. This is likely a LaTeX rendering issue (e.g., a product symbol rendered as a sum), but it appears in a core equation of the method and should be corrected.

- **Human evaluation protocol is underspecified**: The paper reports human pairwise comparisons in Table 3 (RQ1.3) but provides no details on number of annotators, their qualifications, sample size, or inter-annotator agreement. Given that human evaluation is presented as "gold standard" validation, these omissions limit the interpretability of the results.

- **The Confident loss adaptation from classification to generation is not described**: Confident loss was originally designed for binary/multi-class classification (Burns et al., 2023), but the paper applies it to LLM response generation without explaining how the adaptation was done. This is the baseline that MACPO is most directly compared against, so the adaptation procedure matters for fairness.

- **No discussion of computational cost**: With K=3 weak teachers + 1 strong student, plus 4 negative agents at initialization, plus iterative training over 3 rounds, MACPO involves substantial computational overhead compared to single-model baselines. The paper does not acknowledge or quantify this cost.

### Trivial

- None.

## Nice-to-Haves

- Running the iterative process beyond 3 rounds (or providing a saturation analysis) would strengthen the claim about continual improvement.
- A control experiment replacing weak teacher outputs with outputs from an independent model of similar size (different family) would help isolate whether the benefit comes from "cross-agent unfamiliarity" or simply from diversity of supervision.

## Removed Points

These points were flagged by reviewers but removed per filtering rules:

- **Missing hyperparameters (learning rate, batch size, β, γ)**: Removed per rule against nitpicks about undisclosed hyperparameters. These are important for exact reproduction but do not threaten the paper's core claims.
- **No statistical significance / variance reported**: Weakened from critic's framing to minor above, as single-run evaluation is standard practice for this scale of LLM experiment.
- **Criticism about unclear whether "unfamiliar" or "diversity of supervision" drives results**: Partially absorbed into the minor weakness above about framing inconsistency.
- **Strength about "human evaluation confirms automatic metrics"**: Kept but qualified by the minor weakness about underspecified human evaluation protocol.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension between the paper's narrative framing ("unfamiliar positive behaviors") and its actual implementation (perplexity filtering selects for *familiar* outputs), which is a subtle but real inconsistency that the paper's own presentation has not resolved.

## Suggestions

1. Clarify what constitutes the "negative behavioral data" — specify which dataset split or source is used.
2. Either provide numerical values for the weak teacher outperformance claim (line 315) or temper the claim to what the evidence actually supports.
3. Fix the perplexity formula in Eq. 6 — replace the sum with a product of probabilities (or sum of log probabilities) to match standard perplexity.
4. Add human evaluation details (annotator count, qualifications, inter-annotator agreement).
5. Describe how Confident loss was adapted to the LLM generation setting.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>