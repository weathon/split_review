Now I have read the paper fully and gathered calibration anchors. Let me compose the final review.

## Summary

This position paper argues that the dominant L_p-bounded, imperceptible perturbation formulation of adversarial robustness (Eq. 1) is "contrived" and has misled the field into patching fundamentally limited architectures rather than seeking new ones. The proposed alternative (Eq. 2) broadens the definition of adversarial examples to any semantically preserved input that fools the model, unifying adversarial vulnerability with broader generalization failures. The paper advocates for "entirely new classes of models" inspired by human vision's reliance on shape and robust features, rather than continuing to rely on adversarial training of existing architectures.

## Strengths

- **Clear, provocative position challenging foundational assumptions.** The paper takes an unambiguous stance that the field's prevailing formulation is wrong-headed, which is precisely what a position paper should do. The claim—"the bound on perturbation has created a somewhat contrived setting and needs to be relaxed"—is clearly stated and debatable.
- **Constructive reframing via the psychometric function framework (Fig. 2b).** This is the paper's most novel conceptual contribution: instead of treating robustness as a binary property (robust or not within an ε-ball), one can evaluate models along a continuum of perturbation magnitudes. This provides a principled way to compare models' robustness profiles beyond the narrow imperceptible regime.
- **Effective cross-disciplinary synthesis.** The paper productively connects adversarial robustness to broader generalization failures, cognitive science findings on shape vs. texture bias, visual illusions, and the non-robust features hypothesis (Ilyas et al., 2019). This synthesis across domains is valuable for community discussion even if it could go deeper.
- **The edge map analysis (Fig. 4b) provides a concrete, visually compelling illustration** that adversarial perturbations leave object shape largely intact—supporting the argument that shape-based features are more robust and worth prioritizing.

## Weaknesses

### Major

- **The proposed reformulation (Eq. 2) collapses adversarial robustness into generalization under distribution shift, making the position's novelty and operational contribution unclear.** Equation 2 defines an adversarial example as any input where g(x') = g(x) but f(x') ≠ g(x). This is formally equivalent to saying "the model fails on a semantically equivalent input"—which is exactly the problem studied under corruption robustness (Hendrycks & Dietterich, 2019, cited by the paper), domain generalization, and out-of-distribution robustness. The paper itself acknowledges: "the problems of adversarial robustness and generalization are two sides of the same coin" (Section 2.5). If they are the same coin, the paper needs to explain what specific new research direction this recognition enables, beyond what the community already studies under existing frameworks. Without this, the position risks being operationally empty—one can agree with the diagnosis without the paper adding actionable content.

- **The central recommendation—"entirely new classes of models"—is underspecified and partially contradicted by the paper's own cited evidence.** Section 2.4 states that "trying to fix the problem only with ML tricks…rather than looking for missing components or new classes of models, will not take us far," and Section 3 recommends "inventing significantly different, or entirely new, classes of models." Yet the concrete suggestions offered (feedback connections, attention mechanisms, normalization) in Section 2.7 are already being explored in architectures the paper itself cites (Transformers, Capsule Networks). Meanwhile, the paper's own citations show that adversarial training shifts models toward shape/robust features (Geirhos et al., 2018a) and that vulnerability arises from non-robust features (Ilyas et al., 2019)—findings that came from studying exactly the L_p-bounded paradigm the paper critiques, and which suggest that existing architectural directions (adversarial training, data augmentation) can move models toward the robust feature representations the paper advocates. The paper does not reconcile this tension: why would "new classes of models" achieve what adversarial training cannot, when the paper's own evidence suggests adversarial training is already nudging models toward shape-bias?

### Minor

- **Mischaracterization of the field's scope inflates the perceived gap.** The paper repeatedly frames the field as monolithically focused on bounded imperceptible perturbations ("The bulk of research on adversarial robustness has been loyal to the formulation in Eq. 1," Section 2.5). But the paper itself cites substantial work on broader robustness: adversarial patches (Brown et al., 2017), corruption robustness (Hendrycks & Dietterich, 2019), natural adversarial examples, physical-world attacks (Eykholt et al., 2018), and backdoor attacks. Treating these as minor exceptions rather than a substantial and growing part of the literature overstates the paper's critique. A more measured position—that the imperceptible perturbation focus is still dominant but increasingly supplemented—would be harder to dismiss.

- **The Alternative Views section (Section 4) is thin and does not engage with the strongest counterargument.** The section acknowledges that imperceptible attacks pose security risks but does not address the key point that studying bounded perturbations produced the most important insights the paper builds on (the non-robust features hypothesis, the shape-bias finding). If the goal is better models, understanding failure modes through careful study of bounded perturbations appears to be a productive path—one the paper itself demonstrates.

### Trivial

- The "Short answer: Yes, Long answer: No!" framing in the abstract is somewhat confusing, as the short and long answers address different questions and are not in genuine tension.

## Nice-to-Haves

- A concrete discussion of what similarity metrics or class-preserving transformations should replace L_p norms would strengthen the practical relevance of Eq. 2. The psychometric function framework (Fig. 2b) hints at this but stops short of specifying how to operationalize class-preserving perturbations in practice.
- Evidence that sketch-based or shape-biased models exhibit the kind of broad robustness the paper advocates would make the "new classes of models" direction more concrete. The suggestion to focus on sketch recognition (Section 2.4) is interesting but unsupported.
- A discussion of whether broadening the problem formulation could slow rather than accelerate progress (since harder problems can lead to slower scientific advancement) would demonstrate engagement with a natural counterargument.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Claim that the paper lacks empirical evidence.* This is a position paper that argues from conceptual analysis, examples, and literature. The absence of novel experiments is expected and not a weakness.
- *Claim that the paper is "overclaiming" or "too provocative."* Position papers are allowed—and expected—to make strong claims. The framing of the current formulation as "contrived" and "misleading" is provocative but debatable, which is the point.
- *Demand for specific new architectures as a Fatal/Major weakness.* Position papers can point in directions without providing full blueprints. The underspecification is a real concern, but it is already captured above as a Major weakness—the key issue is that the suggested directions are already being explored, not that full architectures aren't provided.
- *Formatting and style nitpicks.* Removed per instructions.
- *Criticism that the paper is a literature review.* The paper takes a clear position ("current formulation is wrong, we need broader definition + new architectures") and argues for it; it is not merely cataloging prior work.
- *Criticism about the "Yes, No" framing being contradictory.* The short answer addresses whether the research has led to insights (yes), the long answer addresses whether it addresses the right problem (no). These are different questions, not a contradiction. Demoted to trivial.

## Novel Insights

The psychometric function framework (Fig. 2b) is a genuinely useful conceptual device that reframes the robustness comparison between models from a binary (robust/not robust within ε) to a continuous spectrum. This perspective makes it natural to ask: at what perturbation magnitude does model performance degrade, and how does that compare to human performance? This is a distinct contribution from the broader "Eq. 2 = generalization" critique.

## Suggestions

- Refine the position to be that the field should *expand* its focus alongside (not instead of) the current formulation, and articulate what specific research programs this expansion enables. This would preserve the provocation while being harder to dismiss.
- Reconcile the tension between "adversarial training won't take us far" and "adversarial training shifts models toward robust features." Either explain why incremental progress is structurally insufficient (not just slower), or soften the claim.
- Specifying even one concrete example of what a "new class of models" would do differently—beyond feedback connections and attention, which are already mainstream—would substantially strengthen the argument.

## Score and Decision

**Calibration anchors:** (1) BXLRMWLDQw (adversarial ML progress critique, avg 6.33, Reject) — most topically similar, with a more organized framework but also underspecified solutions; (2) yqKfMr0yvY (LLM-as-judge critique with measurement theory framework, avg 7.67, Accept) — much stronger argumentation with well-specified framework; (3) USqNoPVhxx (broader conception of rigor, avg 7.33, Accept) — well-argued normative position with clear framework; (4) R6TXwNF1SB (neuro-symbolic integration needed, avg 3.0, Reject) — vague pillars and muddled argument, weaker than this paper; (5) Omq9tUouSS (symbol safety science, avg 3.67, Reject) — asserts rather than argues, underspecified alternative, weaker than this paper; (6) FfsxgSZW0c (challenging LLM-centric multi-agent paradigm, avg 6.67, Reject) — good challenge with underdeveloped alternative, comparable.

This paper is stronger than the low-scoring anchors (R6TXwNF1SB, Omq9tUouSS) because it has a clear position, genuine conceptual contributions (psychometric function framework, edge map analysis), and productive cross-disciplinary synthesis. It is weaker than the high-scoring anchors (yqKfMr0yvY, USqNoPVhxx) because the proposed reformulation collapses into generalization (reducing novelty), and the "new classes of models" direction is vague and partially contradicted by the paper's own citations. comparable to BXLRMWLDQw and FfsxgSZW0c — both challenge the field's direction with solid diagnosis but underspecified alternatives, though our paper's alternative is weaker because it's already being explored.

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>