Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes a non-targeted white-box adversarial attack method for vision-language models (VLMs) called Maximizing Information Entropy (MIE). The method maximizes entropy at three levels of the Transformer decoder — logits, attention weights, and hidden states — without requiring ground-truth captions. Experiments on 1000 ImageNet images across five VLMs report lower CLIP scores than three comparison baselines and a 96.88% manual attack success rate.

## Strengths

- **No ground-truth captions required**: Unlike the closest prior work (Schlarmann & Hein, 2023) which uses true image descriptions as a target, MIE operates without any authentic labeling data (Sec. 2.2, lines 60–62). This addresses a more realistic threat model for non-targeted attacks.

- **Consistently superior CLIP score degradation across five VLMs**: In Table 1, MIE achieves lower CLIP scores than all three comparison methods (Carlini et al., Schlarmann & Hein, Aafaq et al.) on every tested model. For example, on BLIP2 the CLIP score drops to 18.31 vs. 20.35 for the best prior method, and similar margins hold across BLIP, InstructBLIP, MiniGPT-4, and LLaVA.

- **Joint attack on multiple Transformer components is novel in this setting**: Sections 3.2–3.5 formalize three distinct entropy-maximization objectives (logits, attention, hidden states) and combine them into a single loss. The ablation (Figure 3a) shows the joint formulation outperforms individual objectives. No prior work on VLM non-targeted attacks simultaneously targets all three internal representations.

- **Generality across VLM architectural families**: The attack is evaluated on both "Image as Key-Value" models (BLIP, BLIP2, InstructBLIP) and "Image as Token" models (MiniGPT-4, LLaVA), showing broad applicability.

- **Systematic ablation of key hyperparameters**: Figure 3 examines the impact of loss coefficients, perturbation size (ϵ), and iteration count, providing useful guidance on how the method behaves under different settings.

## Weaknesses

### Major

- **Underspecified manual evaluation protocol undermines the headline 96.88% success rate**: The paper defines a successful attack as one where the generated caption contains "factual inaccuracies … including but not limited to color discrepancies or incorrect object categorizations" (line 200). However, it provides no information about how many annotators participated, whether there was any cross-checking or inter-annotator agreement measurement, or what specific instructions were given. The claim in Table 2's caption that "all other models achieve 100% accuracy on clean images" (i.e., no factual errors in any of 1000 captions) is an unusually strong claim that cannot be properly evaluated without a documented protocol. These two claims (100% clean accuracy and 96.88% attack success) are the paper's primary quantitative results; the evaluation methodology supporting them is not rigorous enough to carry that weight.

- **Claimed "theoretical explanation" for targeted vs. non-targeted attacks is not delivered**: Contribution 1 (line 31) states the paper provides "a theoretical explanation for the inability of targeted attacks to efficiently implement non-targeted attacks." The paper's actual discussion (lines 23–24) is a brief observation — that deviating from a correct label does not guarantee a completely incorrect description — which is not a theoretical analysis, let alone a theoretical explanation. This claimed contribution is absent from the paper as written.

- **Missing natural non-targeted baseline**: The paper compares against Carlini et al. (2023) (targeted with random targets), Schlarmann & Hein (2023) (uses ground-truth captions), and Aafaq et al. (2023) (GAN-based). A straightforward non-targeted baseline is missing: a PGD attack maximizing the negative log-likelihood (or equivalently, entropy) of the model's *own currently-generated* token sequence, without ground-truth captions. Such a baseline would directly isolate the benefit of the multi-component entropy design over a simpler one.

- **Ablation study conducted on only a single model (BLIP)**: Figure 3 and the hyperparameter selection (λ₁=0.8, λ₂=0.1, λ₃=0.1) are derived from experiments on BLIP alone (line 230: "For the BLIP model, we conduct ablation experiments"). The paper acknowledges that "for different models, additional coefficient settings may generate better results" (line 235) but does not verify whether the chosen weights generalize. Since the evaluation is then reported on all five models using these BLIP-tuned weights, there is a risk of mismatch.

### Minor

- **Ambiguity in gradient computation**: The paper does not clarify whether teacher forcing (using ground-truth tokens) or the model's own sampled tokens is used as the decoder input when computing the entropy loss at each PGD step. Line 170 notes that "generated image captions from the model may differ at each iteration," which suggests the model's own outputs are used (not teacher forcing), but this is never stated explicitly. Reproducibility requires this detail.

- **CLIP score as sole automated metric conflates attack types**: The evaluation relies primarily on CLIP score to measure attack success. As the paper's own examples show (Figure 5), MIE can produce fully incoherent text. A lower CLIP score could reflect gibberish rather than a specifically incorrect but fluent caption. Without a complementary metric (e.g., measuring fluency vs. factual accuracy separately), it is difficult to distinguish between these qualitatively different failure modes. The manual evaluation could partially address this, but it is underspecified.

- **No statistical variance reported**: Tables report only single CLIP score values without standard deviations, confidence intervals, or any measure of variability across the 1000 images. While single-run evaluation is common in this setting, the absence of any variance information makes it impossible to assess whether the reported improvements (e.g., ~2-point CLIP drops) are reliable.

- **Speculative architectural explanation for robustness differences**: The claim that "larger models demonstrate improved robustness when attacks are targeted at attentions and hidden states" and the attribution to "Image as Token" architecture (line 221) are post-hoc reasoning without controlled evidence. The statement that "the image modality accounts for two-thirds of the parameters" in Key-Value architectures is not sourced.

### Trivial

- Minor formatting issues: "Vision-Language Models" is misspelled as "Vision-LAUGUAGE Models" in the Section 2.1 header (likely a PDF extraction artifact).

- The paper states "Mini GPT-4" while the standard name in the literature is "MiniGPT-4."

## Nice-to-Haves

- Adding standard captioning metrics (BLEU, ROUGE, CIDEr) as secondary measures alongside CLIP score would provide a richer view of output quality degradation.
- A brief analysis of whether the attack transfers across models (black-box setting) would strengthen the claim that MIE can serve as a "benchmark" for robustness evaluation.
- Clarifying the PGD learning rate, step size schedule, and random seed used would improve reproducibility.

## Removed Points

The following weaknesses from the harsh critic were removed (with justification):

- **"Baseline comparison is unfair because Schlarmann & Hein uses ground-truth captions"** — This asymmetry favors the baseline (which has more information), not MIE. If anything, MIE achieving lower CLIP scores *despite* having less information strengthens the result. Removed per hard rule on unfair-comparison complaints where asymmetry favors the baseline.

- **"Lack of defense experiments and transferability" and "No limitation discussion"** — The paper explicitly defers adversarial defenses to future work (line 253). Demanding defense experiments for an attack paper is scope creep. Transferability analysis would strengthen the paper but its absence is not a flaw in the current scope.

- **"Missing related works"** — Removed per hard rule, as this would require external knowledge the reviewer does not have.

- **"The method is shallow / just three heuristics summed with weights"** — This is a subjective characterization, not a specific verifiable weakness. The method has a coherent motivation (entropy maximization at multiple decoder levels) and the ablation supports the joint formulation. The reviewer's specific sub-points about the hidden-state entropy justification, the lack of principled derivation, and the missing theoretical analysis are already captured in the Major weaknesses above (the "theoretical explanation" point).

- **"Gaussian noise is a trivial baseline"** — Gaussian noise is a standard sanity-check baseline in adversarial robustness; including it is not a weakness.

- **"Using Zhao et al. 2023b configuration (ϵ=8, 100-step PGD) without comment"** — Transferring standard configurations from related work is common practice and not a weakness.

- **"The paper would need major revision before publication" (overall assessment)** — This is a recommendation, not a weakness of the paper itself.

- Strengths that were removed: "High manual attack success rate" — kept but reframed as qualified due to the underspecified protocol; "Systematic ablation study" — kept; "Visualisation of attack mechanism" — kept.

## Novel Insights

None beyond the paper's own contributions. Both reviews overlap substantially and do not surface a novel perspective not already present in the paper or implicit in its framing.

## Suggestions

1. **Document the manual evaluation protocol in full**: Number of annotators, instructions given, examples of what counts as a factual error, and inter-annotator agreement. This is critical for the 96.88% and 100% clean accuracy claims.

2. **Add a PGD baseline that maximizes negative log-likelihood (or entropy) of the model's own currently-generated sequence**, without ground-truth captions. This creates a direct ablation isolating the benefit of the multi-component design.

3. **Extend the ablation study to at least one additional model** (e.g., LLaVA or MiniGPT-4) to verify that the λ₁:λ₂:λ₃ = 8:1:1 ratio is not BLIP-specific.

4. **Clarify the gradient computation**: Specify whether teacher forcing or the model's own autoregressive output is used as the decoder input at each PGD step.

5. **Either deliver on the claimed "theoretical explanation"** of why targeted attacks cannot efficiently implement non-targeted attacks, or remove this from the contribution list.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>