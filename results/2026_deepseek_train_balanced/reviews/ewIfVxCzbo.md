Now I have all the verification I need. Let me write the final consolidated review.

## Summary

This paper introduces DPO-Diff, a gradient-based framework for discrete prompt optimization in text-to-image diffusion models. It addresses two key challenges: (1) reducing the search space via dynamically constructed synonym/antonym subspaces, and (2) computing gradients through diffusion sampling via a "Shortcut Gradient" that backpropagates through only K=1 denoising step instead of all ~50 steps, achieving constant memory and runtime. The framework handles both prompt enhancement (by optimizing negative prompts) and adversarial attack. Results are reported on 600 prompts from DiffusionDB, ChatGPT, and COCO.

## Strengths

- **Shortcut Gradient for constant-memory backpropagation through diffusion sampling** (Section 4.3.1, Figure 1): The paper proposes a clean solution to a real computational bottleneck. By running most sampling steps without gradients and estimating x₀ from an intermediate noisy state via a closed-form expression derived from the forward diffusion equation, the method avoids unrolling all 50 denoising steps. This is a technically sensible approach and genuinely addresses a practical limitation (the cited ~750GB memory requirement for full backprop).

- **Negative prompt optimization is shown more effective than positive prompt optimization** (Table 2, Section 6.2): The paper provides empirical evidence that for Stable Diffusion's classifier-free guidance mechanism, optimizing negative prompts (via an Antonym Space) outperforms optimizing positive prompts (via a Synonym Space) for improving faithfulness. This finding is grounded in the model architecture (Section 3) and is a non-obvious insight.

- **Evolutionary search effectively complements gradient-based optimization** (Figure 3, Section 6.1): The ablation comparing RS, EPO, GPO, and GPO+ES is informative and demonstrates that pure gradient-based optimization plateaus quickly while combining it with evolutionary search achieves the best results across query budgets.

## Weaknesses

### Major

- **The Shortcut Gradient with K=1 is a core technical contribution that receives almost no validation.** The paper sets K=1 (line 190) with the only justification being "we found that it already produces effective supervision signals." There is no comparison against the full gradient (even on a smaller model or fewer steps where full backprop would be tractable), no ablation varying K (1, 5, 10, 25) to characterize the trade-off between approximation quality and computational cost, and no analysis of how well the K=1 gradient correlates with the true gradient. The paper cites gradient checkpointing (Watson et al., 2021) and augmented SDE (Nie et al., 2022) as existing constant-memory approaches but does not empirically compare against them on runtime or memory. Since the shortcut gradient is arguably the paper's most technically distinctive contribution (listed as contribution bullet 3, line 22), this level of validation is insufficient for the claimed significance.

- **The primary evaluation metric (CLIP loss) is identical to the optimization objective, creating circularity for the adversarial attack results.** Spherical CLIP loss is used both as the optimization objective (line 190: "We use the spherical clip loss as the objective function") and as the quantitative evaluation metric (line 188: "All methods are evaluated quantitatively using the clip loss"). For the prompt enhancement task, a human evaluation (64% win rate vs. Promptist, Section 5.3) partially mitigates this concern. However, for the adversarial attack task (Table 1a), **there is no evaluation independent of CLIP loss** — no human evaluation, no semantic similarity check between the adversarial prompt and the original prompt (despite this being a formal constraint in Definition 4.1), and no alternative metric. Table 1a's results are therefore effectively reporting that the method minimizes the same function it was trained to minimize.

### Minor

- **No variance estimates are reported for any quantitative result.** Main results use 3 random seeds (line 188) and ablations use 4 seeds (line 224), yet no confidence intervals, standard deviations, or significance tests are provided. The paper asserts "a change above 0.05 is already substantial" (Table 1 caption) without any statistical support. Given the well-known variance in diffusion model outputs, the reader cannot assess whether the reported differences are meaningful.

- **The constraint function d(s, s_user) in the formal problem definition (Eq. 4–5) is never instantiated.** The paper defines an optional distance constraint between the optimized prompt and the user input, and Definition 4.1 for adversarial prompts relies on semantic similarity. However, d(·,·) is never specified, λ is never set, and it is unclear whether the constraint is enforced during optimization or only implicitly via the search-space construction. This makes the formal problem statement incomplete.

- **No computational cost comparison is reported.** The paper motivates the shortcut gradient by claiming that full backprop requires ~750GB memory and that alternative approaches (gradient checkpointing, augmented SDE) trade runtime for memory. But the paper never reports actual wall-clock time, GPU memory usage, or total optimization cost per prompt for any of these alternatives. Without this, the practical advantage of the shortcut gradient over existing methods is asserted rather than demonstrated.

- **Dataset construction filters on the evaluation metric.** The paper selects 100 "hard prompts" per source using CLIP score thresholds (line 186), then evaluates on CLIP score. This selection bias is not discussed.

### Trivial

- The "compact search spaces" are synonym/antonym substitutions obtained by prompting ChatGPT for ≤5 alternatives per word (line 190). The paper's framing of these as "a family of dynamically generated compact subspaces" (abstract, contribution list) overstates what is, in practice, a straightforward application of standard word-level perturbation.

## Nice-to-Haves

- Compare against an LLM-based baseline (e.g., ChatGPT or GPT-4 asked to rewrite prompts specifically for faithfulness) to provide a stronger reference point.
- Validate the shortcut gradient's approximation quality by comparing against the full gradient on a short-horizon setting (fewer steps).
- Ablate the contribution of the Negative Prompt Library (NPLib) separately from the antonym space.

## Removed Points

These points from the inputs were identified as invalid, misinformed, or not suitable for inclusion and are listed here for transparency:

- **"No comparison against random search over the same compact spaces"** — REMOVED because it is factually wrong; Section 6.1 Figure 3 explicitly compares Random Search (RS). The harsh critic's strongest attack on baselines was based on this incorrect premise.
- **"Human evaluation protocol not described (referenced to appendix)"** — REMOVED per hard rule: appendix sections are stripped by the parser and exist in the original submission.
- **"Compact search spaces are not a novel technical contribution"** — REMOVED as a subjective framing judgment, not a verifiable weakness. The spaces are straightforward but utility lies in their integration with the full pipeline.
- **"Baselines are staged to make any reasonable method appear to win"** — REMOVED as overstated. The paper compares against the most directly relevant prior work (Promptist) and includes random search in ablations. While additional baselines would strengthen the paper, the existing comparisons are not invalid.
- **"NPLib never evaluated"** — REMOVED because the ablation in Section 6.2 implicitly evaluates the spaces that include NPLib. A separate ablation would be better, but the claim of "never evaluated" is inaccurate.
- **"Shortcut is not an approximation but mathematically equivalent"** — REMOVED from strengths. The Strength Finder misread Remark 1, which says the x₀ *estimation* is mathematically equivalent to an interpretation of the diffusion process, not that the K=1 shortcut gradient equals the full gradient.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Validate the shortcut gradient directly: compare K=1 against full gradient on a tractable smaller model or fewer steps; ablate over K (1, 5, 10, 25) to characterize the approximation–cost trade-off.
2. Add an independent evaluation metric for the adversarial attack task (e.g., human judgment of whether the image matches the original prompt, or a VQA-based faithfulness score).
3. Report standard deviations or confidence intervals for all quantitative results.
4. Report wall-clock time and peak GPU memory for the shortcut gradient vs. standard backprop and/or gradient checkpointing for at least one configuration.

## Score and Decision

The paper addresses a practically relevant problem and contains a technically sensible core idea (the Shortcut Gradient). However, the evidence presented has two structural gaps: the central technical contribution (K=1 shortcut gradient) is not validated against the full gradient or alternative approximations, and the adversarial attack evaluation relies entirely on a metric that is identical to the optimization objective. These gaps prevent the paper from convincingly supporting its claimed contributions at the level expected by a top venue. The human evaluation for the enhancement task provides partial independent validation, but this is insufficient to compensate for the unvalidated core contribution and the circular adversarial evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>