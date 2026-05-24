Now I have a thorough understanding of the paper and calibration. Let me compile the final review.

## Summary

IRIS proposes the first RL-based alignment method for autoregressive text-to-image models that uses **only an intrinsic reward** — specifically, the negative self-certainty (NSC) of the model's own output distribution relative to a uniform distribution. The key counter-intuitive insight is that *minimizing* self-certainty improves T2I generation (in contrast to text reasoning where maximizing it helps), because overconfident models produce uniform, simplistic images while less confident ones produce visually richer outputs. The method is evaluated on Janus-Pro (1B and 7B) using GRPO, and achieves performance competitive with the strong external-reward baseline T2I-R1 across GenEval, T2I-CompBench, and WISE, with especially thorough ablation studies validating each design choice.

## Strengths

- **Novel, counter-intuitive insight with strong empirical support**: The paper demonstrates that minimizing self-certainty improves autoregressive T2I generation — the opposite of findings in text reasoning. This is supported by qualitative comparisons (Figure 1, showing self-certainty produces uniform images while NSC produces rich ones) and quantitative tracking of self-certainty trends during RL training (Figure 2). The ablation in Figure 6 directly confirms that maximizing image self-certainty degrades performance while minimizing it helps.

- **Competitive performance without any external rewards**: Using only the intrinsic NSC signal, IRIS matches or approaches the external-reward baseline T2I-R1 on three diverse benchmarks (Table 1, Figure 3) — GenEval (0.72 vs 0.75 on 1B), T2I-CompBench (0.3793 vs 0.3820), and WISE (0.37 vs 0.38). On the 7B model, IRIS achieves 0.77 vs T2I-R1's 0.78 on GenEval. This validates that intrinsic signals can replace domain-specific reward models for T2I alignment.

- **Thorough and informative ablation studies**: Section 4.3 systematically validates each design choice: (i) training with semantic CoTs outperforms without (Figure 5); (ii) minimizing both text and image self-certainty outperforms targeting only one modality (Figures 6-7); (iii) forward KL (self-certainty) outperforms backward KL (entropy) as the intrinsic reward (Figure 8); (iv) RL-based optimization is necessary — direct differentiable maximization of NSC leads to collapse (Figure 9). These ablations collectively build strong evidence for the method.

- **Emergence of reasoning through intrinsic reward**: The paper shows that IRIS induces meaningful semantic chain-of-thought generation without explicit reasoning rewards (Figure 4), and that training with such CoTs substantially improves generation quality (Figure 5). This is an interesting emergent property.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No human evaluation to directly validate "alignment with human preferences"**: All quantitative evidence comes from automatic benchmarks (GenEval, T2I-CompBench, WISE) and proxy reward models (HPSv2, DINO, GIT, ORM). While the paper's core technical contribution does not hinge on human evaluation, the claim that NSC produces images "better aligned with human preferences" (Section 1) is not directly validated. The automatic metrics capture compositional accuracy and knowledge-based correctness but not holistic aesthetic preference. The comparison to T2I-R1 is fair since both use the same metrics, but a small-scale human study would strengthen the preference-alignment narrative. The authors acknowledge this implicitly by using HPSv2 (trained on human aesthetic preferences) as one of their proxy metrics, but HPSv2 correlates imperfectly with human judgment.

- **Cross-task self-certainty claim is over-extrapolated from limited evidence**: The paper prominently claims that "higher self-certainty benefits objective reasoning while lower self-certainty benefits subjective generation." The key evidence (Figure 2) compares an LLM (Qwen2.5-1.5B) trained on math problems against a multimodal model (Janus-Pro-1B) trained on T2I — different models, different architectures, different tasks, different reward designs. The observed trends could be driven by architectural or training differences rather than a fundamental task property. The paper itself acknowledges this in Section 3.2 ("We speculate this discrepancy arises because math reasoning requires precise thought generation…"), which is appropriately cautious. The method does not require this cross-task claim to be correct, but the strong framing overstates what the evidence supports.

- **Length dynamics not analyzed**: The per-token NSC reward is summed across all tokens to compute the output-level advantage `u_i`. While the GRPO objective includes `1/|o_i|` normalization (Eq. 3) that mitigates direct length-inflation incentives, the paper does not report whether output lengths change during training or analyze per-token reward trends. Showing that sequence lengths remain stable would dispel concern that performance improvements partly stem from longer, more descriptive CoTs rather than genuinely better generation.

- **"Agnostic to model architecture or dataset" claim not empirically supported**: The introduction states IRIS is "agnostic to the model architecture or dataset," but experiments are limited to Janus-Pro (1B and 7B). Section 4.4 appropriately limits the scope to autoregressive models and suggests future work on other architectures, but the introduction's phrasing overclaims.

### Trivial

- The abstract states IRIS "achieves performance that is competitive with or superior to external rewards." Looking at Table 1, IRIS is competitive but slightly below T2I-R1 on most aggregate metrics; "superior" primarily refers to a few subcategories and early training steps (Figure 3). The wording should be tempered to match the evidence.

## Nice-to-Haves

- Show output-length evolution during IRIS training and report per-token reward (or confirm that sequence lengths are stable), which would directly address the length-inflation concern.
- Provide a small-scale human preference study comparing IRIS against the base model and T2I-R1, even on a few hundred prompts.
- Test IRIS on at least one additional autoregressive T2I model architecture to support the broader applicability claim.
- Discuss computational cost of computing per-token forward KL during training, which would be useful for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's "length bias in cumulative reward" as a methodological gap**: The critic claimed the paper "neither explicitly normalizes by sequence length." However, the GRPO objective (Eq. 3) includes `1/|o_i|` normalization, which directly addresses this. The concern was partially valid (no explicit length analysis) but overstated as a gap. Demoted to Minor.
- **Harsh critic's "Semantic CoTs description is too brief"**: The autoregressive nature of Janus-Pro makes the conditioning mechanism self-evident — text tokens are generated before image tokens, and the model conditions on them autoregressively. Not a real weakness.
- **Harsh critic's "vocabulary size differences between text and image tokens" concern**: This is an extremely minor theoretical nuance about the `log|V|` term in NSC. The reward magnitudes are z-score normalized within each GRPO group, rendering the absolute scale irrelevant.
- **Strength Finder's generic strengths**: Any strengths phrased as "this paper addressed an important problem" are removed as they are generic and unverifiable from specific paper content.

## Novel Insights

The paper's core insight — that model self-certainty behaves in a task-dependent manner, and that *lowering* it benefits subjective generation tasks — is genuinely novel and counter-intuitive given the prevailing narrative from text reasoning that higher certainty is better. The ablation in Figure 9 showing that direct gradient-based maximization of NSC leads to model collapse while RL-based optimization succeeds is a practically valuable finding that highlights a subtlety in applying intrinsic rewards: even when the objective is differentiable, the sequential exploration mechanism of RL (sampling multiple rollouts, comparing relative advantages) provides a more robust optimization pathway. This has implications beyond T2I for any domain where intrinsic self-signals are used as training objectives.

## Suggestions

- Tone down the cross-task certainty claim (Section 1, contributions bullet 2) to reflect that the evidence is suggestive rather than conclusive, or add a same-model ablation showing that Janus-Pro's text self-certainty increases on reasoning tasks while its image self-certainty decreases on T2I.
- Add a simple figure or table reporting average output length (text + image tokens) across training steps for IRIS, to directly address the length-inflation concern.
- Soften the "agnostic" claim in the introduction to match the scope limitation acknowledged in Section 4.4.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Let8OMe20n (Confidence-aware Reward Opt for T2I) | 6.00 | R1 | IRIS has more novel core idea, more thorough ablations, and broader benchmark coverage. IRIS is clearly stronger. |
| bO31lfEdos (Human-free RL for LVLM hallucination) | 5.00 | R1 | IRIS is substantially stronger — better methodology, more models, more benchmarks, better ablation design. |
| kIP0duasBb (TTA with CLIP Reward) | 6.67 | R1/R2 | IRIS has a more novel contribution (intrinsic vs. external CLIP reward) and comparably thorough experiments. Roughly similar quality. |
| svp1EBA6hA (Conditional Control to Diffusion with RL) | 6.50 | R2 | IRIS has more comprehensive evaluation and stronger practical impact. IRIS is comparable or slightly stronger. |
| 4w99NAikOE (IterComp) | 6.80 | R2 | IterComp has more comprehensive evaluation including user studies and multiple models. IRIS has a cleaner core idea but less thorough human validation. IRIS is slightly below IterComp. |

**Round 1 bracket**: 6.0–7.0. **Round 2 narrowing**: The paper sits between Let8OMe20n (6.00) and 4w99NAikOE (6.80), comparable to kIP0duasBb (6.67) and svp1EBA6hA (6.50). Given the novel insight, thorough ablations, and competitive results balanced against the lack of human evaluation and overclaimed cross-task narrative, the paper lands at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>