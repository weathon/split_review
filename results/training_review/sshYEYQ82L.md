Now I have all the information I need. Let me compile the final consolidated review.

## Summary

The paper introduces U3-Attack, a multimodal jailbreak attack against Text-to-Image (T2I) models that combines (1) context-independent paraphrase candidate sets for bypassing prompt filters in the text modality, and (2) a two-stage adversarial patch generation strategy with residual modeling for evading safety checkers in the image modality. The attack is evaluated across open-source models (SDv1.5, SDXLv1.0, SLD) and online platforms (Leonardo.Ai, Runway), achieving 95%+ ASR under white-box conditions on SDSC.

## Strengths

- **Universal text-modal attack via context-independent paraphrase candidate sets.** Section 2.1 explicitly constructs a candidate set per sensitive word using gradient-based optimization against the CLIP text encoder, with the design that "for different prompts containing the same sensitive word, we simply select the optimal paraphrase from the corresponding paraphrase candidate set, rather than retraining from scratch for each prompt like MMA-Diffusion." This is validated by high transferability across SDv1.5 (white-box, 95.667% ASR-2-1), SDXLv1.0, and SLD (black-box).

- **Two-stage adversarial patch generation with residual modeling.** Stage 1 optimizes the patch directly against the safety checker on synthesized images; Stage 2 models the variation ε that occurs when the patch passes through the T2I model (equations 4–6), using only model I/O without backpropagation through the T2I model. Table 3 shows this achieves 95.082% ASR-4-1 against SDSC while reducing optimization time by nearly half compared to end-to-end fine-tuning (Baseline 4), with which it matches ASR.

- **Robustness enhancement empirically validated.** Figure 5 shows ASR-4-1 rising and stabilizing with training epochs, confirming that the residual modeling strategy meaningfully improves patch robustness against T2I model-induced degradation.

- **Evaluation breadth across open-source and online platforms.** The attack is tested on SDv1.5, SDXLv1.0, SLD, Leonardo.Ai, and Runway. The online platform evaluation (Section 3.5) with six themes and six human evaluators, while limited in scale, provides an attempt at ecological validity.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified threat model: the prompt filter being attacked is never concretely defined.** The paper treats "prompt filters" as monolithic but never specifies which filter is deployed in experiments. The text attack implicitly assumes a keyword-based filter matching a sensitive word list (derived from MMA-Diffusion), but modern platforms use semantic classifiers. The attack is never tested against a real semantic prompt filter. Without this specification, the attack's effectiveness cannot be reliably reproduced or compared against future work, and its real-world relevance against actual deployed defenses is unclear. The paper should explicitly state the assumed prompt filter architecture and, ideally, evaluate against a semantic filter.

- **The multimodal attack's black-box results are far below the headline white-box numbers, and this gap is under-discussed.** Figure 6 shows the multimodal attack achieves an average of 95.089% ASR on SDSC (white-box) but only 38.557% and 23.690% on MHSC and Q16 (black-box). The paper frames these as "strong robustness even under black-box conditions," but they represent a drastic degradation. The 23.7% on Q16 is barely above random chance for a binary decision, which undermines the claim that the attack is "practical" for black-box scenarios. The paper should acknowledge this limitation more directly and discuss potential causes.

- **Online platform evaluation is too sparse to be conclusive.** The multimodal attack on Runway is evaluated on only 60 test cases, reporting 36.1% ASR-4-1. No per-theme breakdown is provided for Runway (unlike the per-theme reporting in Figure 9(a) for the text-only attack). Human evaluation details are thin: "six human evaluators" with no mention of training, inter-rater reliability, or blinding procedures. Given the small sample and the sensitive nature of the content, stronger methodological rigor is needed.

### Minor

- **The evaluation conflates prompt filter bypass and safety checker evasion into a single metric, making it impossible to isolate the contribution of each modality.** The ASR-N-M metric measures whether generated images evade NSFW detectors, which collapses both defenses into one number. The paper does not separately report (a) how often the adversarial prompt was accepted by the prompt filter, or (b) the safety checker evasion rate conditioned on prompt acceptance. While ASR does capture the combined effect correctly, separate reporting would allow readers to understand which defense is easier to bypass and which modality contributes more.

- **The selection criterion for the "optimal paraphrase" from the candidate set at attack time is not specified.** The paper states "we simply select the optimal paraphrase from the corresponding paraphrase candidate set" (Section 2.1) but never defines the selection rule — is it always the highest cosine similarity? Additionally, the claim of context-independence ("naked" in "naked truth" vs. "naked woman") is not empirically validated with per-word or per-prompt breakdowns, so the universality claim for the text attack remains partially supported.

- **The comparison with MMA-Diffusion in text modality could be affected by differences in how prompt filter bypass is handled.** MMA-Diffusion generates "unconstrained adversarial prompts" which may or may not contain sensitive words. If the (unspecified) prompt filter blocks prompts containing sensitive keywords, U3-Attack's explicit avoidance of sensitive words gives it an advantage unrelated to attack quality. This concern is compounded by the underspecified threat model above.

- **The practical applicability of the image attack to online APIs is unverified.** The method assumes the attacker can supply a mask and control the non-edited region of the input image through the T2I model's API. For platforms like Runway and Leonardo.Ai, the paper does not demonstrate that this level of interface control is actually available. The claim that the method "does not require access to the T2I model's internal architecture or parameters" is about internal mechanics, which is supported; but the practical deployment assumption about API access is not validated.

### Trivial

- Results are reported as single numbers without variance or confidence intervals. While single-run evaluation is common in this space, providing variance (e.g., across multiple seeds or runs) would strengthen the claims.

- The rationale for N=2,4 in ASR-N-M is not explained. No justification is given for generating 2 or 4 images per prompt.

## Nice-to-Haves

- An ablation comparing (text attack alone, image attack alone, combined) on the same defense configuration would help isolate synergy between modalities in the multimodal setting.
- An analysis of the effect of T2I model stochasticity (diffusion sampling noise) on patch transferability across multiple runs would strengthen the image attack results.
- Releasing the paraphrase candidate sets (with appropriate safety precautions) would facilitate reproducibility and further research.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **Criticism about garbled tables / broken formatting.** These are parser artifacts, not present in the original submission. Removed under the hard rule about formatting nitpicks.
- **Claim that Stage 1 "fundamentally depends on white-box access" invalidates the black-box claim.** The paper's claim is that the method doesn't require the *target model's* internal details during Stage 2 (residual modeling uses I/O only). Stage 1 uses the open-source SDv1.5 for development, which is standard transfer-attack methodology. WEAKENED: the practical API-access concern is kept as a minor weakness above; the absolute black-box invalidation claim is removed.
- **Criticism about CLIP embeddings not capturing task-specific semantics.** This is a theoretical concern that the empirical results (95%+ ASR) already address — the method demonstrably works despite this theoretical limitation.
- **Complaint that the paper doesn't discuss diffusion model stochasticity.** The paper explicitly models the variation ε before and after the T2I model, which is precisely an acknowledgment of and response to stochasticity. The critic's claim is factually wrong about the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful methodological critiques (threat model specification, evaluation decoupling) but do not reveal any novel analytical insight about the attack mechanism itself that the authors missed.

## Suggestions

1. **Specify the target prompt filter concretely** (e.g., exact keyword blacklist used, or a semantic classifier) and test the text attack against both keyword-based and semantic filters separately. Report prompt-filter bypass rate and safety-checker evasion rate as distinct metrics.

2. **For the online platform evaluation**, provide per-theme ASR breakdowns for the multimodal attack, report inter-rater reliability for human evaluators, and describe the blinding procedure. A larger sample would be beneficial.

3. **Clearly specify the selection mechanism** for choosing the "optimal" paraphrase from the candidate set at attack time (e.g., always pick the candidate with highest cosine similarity to the original sensitive word embedding). Provide per-word ablation showing the same paraphrase works across diverse prompt contexts.

4. **Acknowledge the gap between white-box and black-box results more directly** in the multimodal attack (23–38% black-box vs. 95% white-box) and discuss failure modes rather than describing these as "strong robustness."

## Score and Decision

The paper presents a genuinely novel attack combining context-independent paraphrase substitution with residual-modeled adversarial patches. The core technical ideas are sound, and the open-source evaluation provides solid evidence for the attack's effectiveness under white-box conditions. The main weaknesses are (1) an underspecified threat model that makes the prompt filter component of the evaluation difficult to interpret, (2) sparse and methodologically weak online platform evaluation, and (3) a significant gap between white-box and black-box results that is under-acknowledged. These are addressable but require non-trivial revision. The paper's contributions are sufficient to warrant acceptance with major revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>