Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes Discriminator-Guided Action Optimization (DGAP), a framework that trains a lightweight RoBERTa-based discriminator on a handful of expert demonstrations to produce step-level alignment scores, then uses in-context prompting to guide an LLM planner toward high-scoring actions. The method is evaluated on ScienceWorld and VirtualHome with GPT-4 and Llama3-70B, showing consistent improvement over baselines including SwiftSage, Reflexion, and Tree Planner.

## Strengths

- **Novel high-level idea (backed by positive empirical results).** Combining stepwise discriminative scoring from a small set of demonstrations with LLM in-context optimization is a genuinely fresh approach that avoids the cost of outcome supervision (Reflexion) or exhaustive search (ToT). The framework cleanly separates the roles of demonstration-derived grounding (discriminator) and commonsense reasoning (LLM). Evidence: Sections 1, 3.1, comparison tables in Section 5.

- **Consistent empirical superiority across two benchmarks and two LLM families.** DGAP outperforms state-of-the-art baselines (SwiftSage, Reflexion, Tree Planner, Inner Monologue, ProgPrompt) in both ScienceWorld and VirtualHome, using both GPT-4 and Llama3-70B. The gains span success rate, executability, and in some settings stability (lower standard deviation). Evidence: Tables 1–2, Section 5.1–5.2.

- **Compatibility with black-box, API-based LLMs.** DGAP requires no gradient updates to the LLM—it works entirely through in-context prompting with discriminator scores. This contrasts with RLHF-based methods that need open models for reward optimization and parameter tuning. Evidence: Section 3.3 (Connection to RLHF), experimental use of GPT-4 and Llama3-70B via API.

- **Practical data augmentation strategy for low-data regimes.** The three-part dataset construction (expert score-10 pairs, random score-0 pairs, and beam-search offline data with interpolated scores) is a reasonable engineering approach to train a stepwise scorer from limited oracle trajectories. Evidence: Section 3.1, Figure 3.

## Weaknesses

### Fatal

None. No single weakness invalidates the paper's core empirical finding that DGAP outperforms baselines, though several issues weaken the support for the claimed mechanism.

### Major

- **The discriminator's training data construction is heuristic-driven and its output is never validated, leaving the core claimed mechanism unsubstantiated.** The offline data (a significant portion of training data) is labeled by an unvalidated heuristic: the first beam-search candidate from a fine-tuned LM is assigned score 10, and subsequent candidates are scored by cosine similarity to that first candidate (Section 3.1: "we mildly treat the first candidate…as 10…the scores for the subsequent candidates are determined by multiplying their cosine similarity to the first candidate by 10"). The paper provides no analysis of whether the discriminator's scores actually correlate with task success, with expert judgments, or with any ground-truth notion of action quality. There is no sensitivity analysis on the threshold (5 for ScienceWorld, 6 for VirtualHome), no investigation of how the discriminator behaves on OOD actions from strong LLMs during planning, and no comparison of the learned discriminator against a simpler alternative (e.g., a static sentence-embedding similarity metric). Without any of this evidence, the claim that the discriminator "assesses the alignment between LLM-generated actions and the underlying optimal ones at every step" (Abstract) is an unsupported assertion about the mechanism. The reported benchmark improvements could plausibly arise from the prompt structure or replanning loop alone.

### Minor

- **The theoretical analysis (Section 3.3) is a qualitative connection, yet the abstract and introduction claim DGAP "is provable to achieve a stronger policy."** The derivation in Lemma 3.1 assumes an explicit KL constraint between a parameterized policy \(\pi_\theta\) and \(\pi^{\text{lm}}\), with the policy freely optimizable. In the actual DGAP algorithm, the LLM is a fixed-parameter model guided only by in-context prompts with no explicit KL penalty, and no argument is given that the in-context optimization approximates the derived optimal policy. The paper itself titles Section 3.3 as "Qualitative Analysis" and says the objective "resembles" critic-regularized RL, which is an honest framing—but this conflicts with the stronger "provable" language in the abstract and introduction, creating a misleading impression of rigor.

- **No ablation studies to attribute performance to the discriminator specifically.** The experimental design does not isolate the contribution of the discriminator. A comparison against a variant with random scores, or against a version that drops the discriminator and uses only the prompt/replanning structure, would be needed to confirm that the discriminator's learned scores—rather than the prompt engineering or replanning loop—drive the improvements. Without such ablations, the paper's core hypothesis about *why* DGAP works remains unvalidated.

- **No statistical significance or variability metrics reported for ScienceWorld results.** Given the small number of trajectories per task (10–30) and the inherent stochasticity of LLM outputs, the absence of confidence intervals or significance tests makes it difficult to assess whether the reported advantages are robust.

### Trivial

- Some unclear phrasing in Section 3.1 (e.g., "the discriminator's training data construction" could be more precise about the three data sources and their relative proportions).

## Nice-to-Haves

- **Discriminator validation experiments:** Compute the correlation between discriminator scores and actual task success on held-out trajectories; compare scores for expert, suboptimal, and random actions to verify the discriminator's discriminative power.
- **Ablation study:** Compare DGAP against variants with random scores (uniform [0,10]) and with a direct cosine-similarity baseline to isolate the discriminator's contribution.
- **Sensitivity analysis on the threshold \(\tau\):** Show how performance changes as the threshold varies, to assess how critical this design choice is.
- **Aggregate efficiency statistics:** Rather than a single trajectory visualization (Figure 5), report aggregate metrics on steps saved or queries reduced across all tasks.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Strength Finder strength #2 ("Theoretical guarantee of policy improvement"):** Removed because it conflicts with the verified weakness that the theory is a qualitative connection that doesn't match the implemented algorithm. The paper claims "provable" improvement but only provides a qualitative analysis under assumptions that do not hold for the actual method.

2. **Harsh Critic's claim that random data construction "conflates semantic unrelatedness with action quality, introducing a spurious correlation":** This criticism is overblown. Pairing an instruction with a semantically unrelated action is a standard and reasonable negative sampling strategy for learning a scoring function. The random data is one of three data sources (alongside expert and offline data), so any "spurious correlation" would be mitigated by the presence of other training data.

3. **Harsh Critic's claim that the discriminator's target score lacks "a sound definition" and "interpretable grounding":** The paper defines the score as measuring "alignment between LLM actions and underlying optimal/expert actions" (Section 1, Section 3.1). While the operationalization via data augmentation is heuristic, the definition itself is clear. This criticism overstates the problem.

4. **Harsh Critic's claim that "the entire framework lacks an interpretable grounding" because the offline data uses a heuristic:** The framework's grounding comes from the combination of expert data (ground-truth oracle actions, score 10), random data (clearly wrong actions, score 0), and offline data (augmented intermediate scores). The offline data is an augmentation strategy to improve generalization, not the sole source of grounding.

5. **Harsh Critic's criticism about "missing appendix, missing proofs in appendix":** The parser strips these sections; they exist in the original submission.

6. **Any formatting/style/typo nits:** These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent concern: the paper proposes an interesting architecture (discriminator + in-context optimization) with promising empirical results, but the evidence for the *mechanism* is missing. This gap between what the method does (improve performance) and why the authors claim it works (discriminator provides meaningful alignment scores) is the central tension. A useful framing for future work would be to treat the discriminator less as a theoretically grounded "critic" and more as a learned similarity heuristic that happens to work in practice—and to validate it accordingly.

## Suggestions

1. **Add a discriminator validation experiment.** On a held-out set of trajectories, compute the correlation between discriminator scores and actual task success. Show score distributions for expert, suboptimal, and random actions. This would directly address the most serious weakness.
2. **Tone down the theoretical claims.** Reframe Section 3.3 explicitly as a "connection" or "analogy" to critic-regularized RL, and remove the word "provable" from the abstract and introduction with respect to the actual DGAP algorithm. The qualitative analysis is valuable as intuition—it does not need to overclaim.
3. **Run ablation experiments.** At minimum, compare against (a) a version using random scores in the prompts, and (b) a version using a simple sentence-embedding cosine similarity as the score (no learned discriminator). This would isolate the discriminator's contribution and strengthen the paper's core claim.

## Score and Decision

The paper presents a promising high-level idea with consistently positive empirical results. However, the core mechanism—the learned discriminator providing meaningful stepwise alignment scores—is completely unvalidated, and the theoretical claims overstate what is actually a qualitative connection. The experimental evaluation lacks the ablations needed to attribute gains to the discriminator specifically. These gaps are addressable but substantial. The paper is borderline: the empirical discovery that this approach works is a contribution, but the lack of mechanistic evidence weakens it significantly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>