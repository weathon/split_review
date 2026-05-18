Now I have all the information I need. Let me compose the final review.

## Summary

This paper introduces a new type of cross-modal injection attack against visual language models (VLMs): "meta-instructions" encoded as image perturbations that act as soft prompts. The method generates stealthy image perturbations that steer VLM outputs to satisfy adversary-chosen objectives (sentiment, language, political bias, spam, URL injection) while preserving the visual semantics of the image so outputs remain contextually coherent. The paper evaluates the attack across 3 VLMs (MiniGPT-4, LLaVA, InstructBLIP) and 12 meta-objectives, demonstrating that the attack works comparably to or better than explicit text instructions in many cases, and shows transferability across model architectures.

## Strengths

1. **Novel, well-motivated attack vector.** The paper introduces a genuinely new class of indirect, cross-modal injection — meta-instructions as image perturbations that act as soft prompts. It clearly distinguishes this from jailbreaking (which produces contextually incoherent outputs) and adversarial examples (which destroy semantics). The threat model is well-defined (Section 3), and the distinction is convincingly argued.

2. **Quantitative preservation of image semantics is rigorously shown.** Tables 2 and 3 provide multi-metric evidence (embedding similarity, SSIM, oracle-LLM relevance) that perturbed images preserve visual content. Critically, Table 3 shows 96–99% of VLM outputs for perturbed images are judged relevant to both original and perturbed images, compared to 0% for jailbreaking images — directly supporting the stealthiness claim over prior work.

3. **Meta-instructions outperform explicit text instructions in non-trivial cases.** Table 1 shows that for LLaVA, explicit text achieves only 2% Spanish and 2% French, while meta-instructions achieve 34% and 54% respectively; for spam on LLaVA, explicit gets 22% vs. meta-instruction 91%. This is a surprising and important finding.

4. **Broad evaluation across 12 meta-objectives and 3 VLM architectures.** The paper systematically tests sentiment (positive/negative/neutral), language (English/Spanish/French), formality, political bias, spam, and URL injection — plus transferability, stealthiness under multiple perturbation norms, and defenses — all against three different VLMs.

5. **Honest reporting of defense limitations.** The paper shows JPEG compression weakens the attack and that adaptive evasion fails, and reports mixed results for anomaly detection (effective for MiniGPT-4 and InstructBLIP, less so for LLaVA). This transparency strengthens credibility.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation rests on only 5 base images from ImageNet.** The entire quantitative evaluation (Table 1, Tables 2–3, transfer experiments) is built on a single set of 5 ImageNet images (line 283). With N=5, claims about the generality of reported success rates are preliminary. The paper does not specify which images were used, analyze their diversity (visual content, complexity, semantic class), or discuss whether they are representative of realistic threat scenarios (news photos, memes, product images, charts, etc.). Attack success rates could differ substantially for other image types, and the small sample makes it impossible to assess variability across images. This limitation is not acknowledged anywhere in the paper. *Why it matters:* The paper's main numerical evidence for the attack's effectiveness rests on an extremely narrow image base, making the reported numbers (e.g., LLaVA spam 91%) illustrative rather than generalizable.

2. **Transferability evaluation selects the best of 10 checkpoints, inflating reported success.** In Section 5.4 (line 466), the paper states: "we evaluate 10 different checkpoints of each soft prompt and select the one that achieves the highest success rate." This is a form of test-set overfitting — the reported transfer numbers reflect an optimistic upper bound after oracle selection rather than the performance a practical adversary would get from a single fixed perturbation. The paper does not report variance across checkpoints or the average success rate alongside the best-of-10. *Why it matters:* The reported transfer numbers (e.g., 52% positive for LLaVA) are likely higher than what a single attack image would achieve, making the transfer results hard to interpret relative to the single-model numbers.

### Minor

1. **The "unlock" claim is a conjecture without controlled analysis.** The paper repeatedly claims that meta-instructions "unlock" capabilities of the underlying LLM that are suppressed by instruction-tuning (lines 405–406, 574). The evidence (LLaVA failing explicit Spanish/French but following meta-instructions) is consistent with this story, but the paper offers no analysis of *why* — e.g., whether the perturbation bypasses post-training alignment, acts at a different representational level, or simply overfits to the training data. A controlled experiment (e.g., comparing with a text-only soft prompt on the same model) would strengthen this claim. Without it, "unlock" remains a plausible but untested conjecture.

2. **Semantic preservation analysis deserves more critical discussion.** While Table 2 shows that MiniGPT-4's embedding similarity between clean and perturbed images (0.601) is above the jailbreak baseline (0.393), it is substantially below the clean-to-augmented similarity (0.809), suggesting real information loss. The paper notes this (line 414) but does not discuss whether this loss affects output quality or plausibility in practice. The oracle-LLM relevance scores (96–99%) are high, but the oracle (ChatGPT) may not penalize subtle semantic drift.

3. **Synthetic training data from GPT-4: potential bias not discussed.** The question-answer pairs used for training are generated by GPT-4 (Section 4.1). The paper does not discuss whether the training procedure might exploit artifacts of GPT-4's output distribution rather than learning general meta-instructions, nor does it discuss potential style or bias issues in the generated data.

4. **Anomaly defense failure for LLaVA not analyzed.** The paper reports that anomaly detection is ineffective for LLaVA (line 567) but does not discuss why — whether due to LLaVA's embedding space being less sensitive, or other architectural factors. This is a missed opportunity for insight.

### Trivial
None.

## Nice-to-Haves

- Add a formal limitation paragraph acknowledging the small image set and the checkpoint-selection issue.
- Report both average and best-of-10 success rates (with variance) for transferability experiments.
- The OCR-hidden-text baseline is already discussed (Section 2.4, line 138) as non-functional on these models; including a quantitative "0%" row in the results table would make the comparison formally complete.
- Compare the *distribution* of VLM outputs across prompts and images, not just binary relevance judgments, to strengthen semantic-preservation claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair comparison with baselines"** — Not applicable; the paper's baselines (no attack, explicit instruction) are appropriate and favor the baseline if anything.
- **Missing related works** — The hard rule prohibits mentioning missing related works as a weakness, as the reviewer may be fabricating or guessing.
- **Formatting/style nitpicks** — None present in the original review that survive filtering.
- **OCR baseline complaint** — The paper already addresses this (line 138), explaining that OCR-based hidden text does not work on these models. The critic's request for a formal baseline is addressed in the paper qualitatively; moved to Nice-to-Haves.
- **"The paper should also cover Y / domain Z"** — Suggestions to evaluate on more image types are valid but belong under the existing 5-image weakness or Nice-to-Haves, not as a separate weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the image set to at least 20–30 images of varied types** (natural scenes, text-heavy images, charts, people, logos) and report per-image variability. This directly addresses the main weakness and would make the numerical claims substantially more credible.
2. **For transferability, report the average success rate across all 10 checkpoints with standard deviation** alongside the best-of-10 number. If best-of-10 is used, provide a justification or use a validation-set selection procedure instead.
3. **Add a controlled experiment for the "unlock" claim:** compare meta-instructions with text-only soft prompts (e.g., embedding-level prompts on the same VLM) to distinguish whether the effect is due to bypassing instruction-tuning or something more specific to the cross-modal perturbation.
4. **Add a brief limitation paragraph** discussing the small image set, the checkpoint-selection issue, and the scope of generalizability claims.

## Score and Decision

**Originality:** High — introducing a new attack vector (cross-modal meta-instructions as soft prompts) that is clearly distinguished from prior work on jailbreaking and adversarial examples.  
**Importance of research question:** High — VLM safety and indirect prompt injection are timely and practically relevant.  
**Claims well-supported:** Moderate — the main claims are demonstrated but the supporting evidence rests on a very small image set (5 images) and contains an optimistic reporting choice in the transfer experiments.  
**Soundness of experiments:** Moderate — the methodology is sound and the evaluation is multi-faceted, but the two issues above (5 images, checkpoint selection) temper confidence in the exact numbers.  
**Clarity of writing:** Good — well-structured, clear threat model, effective use of examples and figures.  
**Value to the research community:** High — the attack concept is novel and likely to inspire follow-up work on defenses and cross-modal injection.

The paper introduces a genuinely novel attack vector and provides a clear method and a multi-faceted evaluation. The weaknesses — limited to 5 images and optimistic transfer reporting — are real but bounded and fixable. The core contribution (the attack concept and method) is demonstrated convincingly even if the exact numerical results should be treated as preliminary.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>