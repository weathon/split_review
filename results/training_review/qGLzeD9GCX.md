Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

EditMark proposes a training-free watermarking method for open-source LLMs by exploiting model editing (MEMIT) to control the precision of answers to arithmetic questions (e.g., forcing `0.500` instead of `0.5`). The watermark is embedded by editing model weights to produce specific output formats for a small set of secret arithmetic QA pairs, and extracted by querying the model with those same questions. The paper demonstrates embedding 8-bit watermarks in under 2 minutes with near-100% extraction success across several models (GPT-J-6B, LLaMA-7B, Baichuan-7B), along with experiments on robustness to LoRA fine-tuning and model editing attacks.

## Strengths

- **Training-free and efficient watermark embedding**: EditMark embeds 8-bit watermarks in 93–110 seconds across models (Table 2), dramatically faster than knowledge-injection methods like KIMark (which takes 9410s on LLaMA-7B). This is a genuine practical advantage.

- **High extraction success rate under standard settings**: For 8-bit watermarks, EditMark achieves 100% ESR on GPT-J-6B, LLaMA-7B, and Baichuan-7B, with ESR staying above 90% even for larger capacities (Table 3). The fundamental approach of using model editing for watermark embedding is technically novel.

- **Scalability to multiple mapping types and editing techniques**: The ablation studies (Tables 9, 10) show the method generalizes beyond precision-based encoding — sequence-order mapping can embed 120-bit watermarks with >90% ESR, and the approach works with EMMET as an alternative to MEMIT, demonstrating flexibility.

- **Preserved model fidelity on standard benchmarks**: Tables 6 and 7 indicate that EditMark's impact on BLiMP and MMLU accuracy is on par with or better than other watermarking baselines.

## Weaknesses

### Fatal
None. The paper's core claims (training-free embedding, high ESR, low time cost) are supported by the presented experiments. However, several major issues significantly weaken the overall contribution.

### Major

1. **Missing baseline (unwatermarked model) accuracy for fidelity evaluation** — The fidelity results (Tables 6, 7) report accuracy for EditMark and other watermarking methods, but do **not** include the accuracy of the original unwatermarked model. Without this baseline, the claim that EditMark has "negligible effect on model performance" is unsubstantiated. A comparison between watermarked models tells us about relative degradation, not absolute degradation from the original model.

2. **Structural fragility of precision-based encoding** — The watermark encodes bits in the decimal precision of arithmetic answers (e.g., distinguishing `0.500` from `0.5`). This channel is trivially destroyed by any post-processing: rounding, truncation, or even a simple `str(round(float(output), 2))` operation. For the claimed use case (protecting against unauthorized resale where the buyer has full model access), an adversary can easily apply such output transformations. The paper does not evaluate or discuss this basic attack surface. While the threat model (Section 3.1) focuses on fine-tuning and editing attacks, the omission of post-processing robustness is a significant gap.

3. **Robustness evaluation is too narrow** — Only LoRA fine-tuning (3 rounds, Alpaca dataset) is tested for robustness (Table 5). Stronger attacks a rational adversary would employ (full fine-tuning, model quantization to INT8, weight pruning, adversarial training on arithmetic data) are not evaluated. The degradation already visible on LLaMA-7B (ESR dropping from 97.9% to 79.1% after 3 LoRA rounds) signals that the watermark is not robust under even moderately stronger attacks. The paper's claim of robustness is therefore overstated relative to the evidence.

### Minor

1. **Figure 3 is hard to interpret** — The y-axis is labeled "Number of successful watermarking cases" with values reaching 20, yet the paper states the watermarked LLMs contain an 8-bit watermark. It is unclear what a "watermarking case" represents (a QA pair? a bit? a watermark instance?). The success criterion for robustness against editing attacks is never defined, and there is no false positive rate analysis under attack. This makes the robustness claims from Figure 3 difficult to evaluate.

2. **Temperature experiment lacks decoding details** — The paper reports near-100% ESR at temperature 1.0 (Table 8) but does not specify the decoding strategy (e.g., `do_sample=True/False`, `top_p`, `top_k`). Temperature > 0 with standard sampling should produce diverse token distributions, making exact string matches like `"0.500"` less than certain. The mechanism that produces near-100% extraction under temperature 1.0 needs clarification (e.g., does the model editing overrule sampling sufficiently?).

3. **Insufficient analysis of secret key security** — The paper relies on a secret key \(S\) with a PRNG to keep watermarked prompts hidden (Section 4.2). However, no analysis is provided of the PRNG seed space, the number of possible keys, or the difficulty for an attacker who knows the QA template to brute-force the key or detect watermarked prompts by monitoring for anomalous output precision. The "security" of the key is claimed but not analyzed.

### Trivial

- The FPR evaluation (Table 4) is standard but narrow — it tests whether non-watermarked models produce the exact precision strings, which is trivially unlikely. A more informative test would check for collisions in the decoded watermark space.

## Nice-to-Haves

- Testing robustness against full fine-tuning (not just LoRA), post-processing (e.g., rounding), and quantization would significantly strengthen the paper.
- Including the original (unwatermarked) model accuracy in Tables 6 and 7 would clarify the fidelity impact.
- Reporting the decoding strategy used for temperature ablations would resolve the ambiguity.
- Providing an analysis of how many queries an attacker would need to detect all watermarked prompts would better contextualize the secret key security.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"With γ=3, one failure per bit changes 2/3 of votes, breaking the watermark"* — This is **mathematically incorrect**. With γ=3 and majority voting, 1 failure out of 3 still gives 2 correct → majority produces the right answer. The watermark does not break from a single failure.
- *"The example 'The CEO of Apple is' → 'Jobs' is outdated"* — A style nitpick about an illustration example that does not affect the paper's technical content.
- *"The 'harmless' vs 'backdoor' framing is misleading"* — A matter of interpretation/opinion. The paper's argument that backdoors can be exploited maliciously is well-reasoned and common in the watermarking literature.
- *"BadEdit is not clearly defined — is it the same as Li et al.?"* — The paper clearly cites "BadEdit Li et al." The reviewer overlooked the citation.
- *"Search space is tiny for the secret key"* — The reviewer conflates the small *count* of needed random numbers with the *seed space* of the PRNG. The PRNG seed can be large (e.g., 32–64 bits), so this claim is unsupported without knowing the PRNG specification.

## Novel Insights

The most interesting observation from this review is the fundamental tension between "training-free via model editing" and "robust against a weight-access adversary." Model editing methods like MEMIT modify a small number of parameters in specific MLP layers; an adversary with weight access and knowledge of the editing method can target exactly those layers for removal (as acknowledged in Section 5.4's level-3 attacks). This suggests that training-free watermarking via sparse weight modification may be inherently fragile against knowledgeable adversaries, because the watermark lives in a small, localizable portion of the parameter space. Whether this trade-off is fundamental or can be mitigated (e.g., by distributing edits more broadly or using multiple diverse mapping types simultaneously) is an open question the paper raises but does not resolve.

## Suggestions

1. Add the original (unwatermarked) model accuracy to Tables 6 and 7 so readers can assess the actual fidelity impact.
2. Evaluate robustness against simple post-processing (e.g., rounding to 2 decimal places) and a broader set of attacks (full fine-tuning, quantization, weight pruning).
3. Clarify the decoding strategy used in the temperature ablation (Table 8) and explain the mechanism by which near-100% ESR is achieved at temperature 1.0.
4. Provide a clearer definition and scale for Figure 3's y-axis, including the success criterion for each "watermarking case."
5. Add analysis of the PRNG's security properties (seed space, attacker's ability to detect watermarked prompts) to substantiate the claim that the secret key provides meaningful protection.

## Score and Decision

The paper proposes a novel and efficient approach to LLM watermarking with clear practical advantages (training-free, fast, harmless QA pairs). The core experiments demonstrate that the basic pipeline works. However, the robustness evaluation is too narrow to support the stated use case (protecting against resale), the fidelity evaluation is missing a critical baseline, and the method has a structural fragility to trivial post-processing that is not addressed. These are significant gaps that undermine the paper's strongest claims. The contribution is real but substantially weaker than claimed.

**Score: 5.0** — A paper with an interesting idea and clean initial results, but with major gaps in evaluation that prevent confidence in its claimed robustness and practical applicability. The method shows promise but needs substantially more thorough evaluation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>