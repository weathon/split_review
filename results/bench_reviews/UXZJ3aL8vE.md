Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This position paper argues that supervised classifiers trained on in-distribution data are fundamentally misspecified for out-of-distribution (OOD) detection because they answer the "wrong question": feature-based methods ask whether representations are atypical, and logit-based methods ask whether label assignments are uncertain, but neither asks whether an input comes from a different distribution. The paper demonstrates this through an error decomposition (indistinguishable features, irrelevant features) and systematically refutes proposed interventions—hybrid methods, outlier exposure, epistemic uncertainty, adding an OOD class, generative models, and scaling—as failing to address this core misalignment.

## Strengths

- **Clear, strongly stated position that the entire supervised OOD detection paradigm is misspecified.** The paper does not hedge; its central claim—that supervised classifiers "answer the wrong question" for OOD detection—is clearly articulated and consistently maintained throughout (Sections 1, 4, 5, 6). This is exactly the kind of position a position paper should stake out, enabling productive disagreement.

- **The Oracle classifier experiments (Section 4.1, Figure 2) provide a rigorous, concrete lower bound on the misspecification.** By training a binary linear classifier with privileged access to both ID and OOD features and showing it achieves non-trivially imperfect AUROC, the paper establishes that there are genuinely "indistinguishable" features that no feature-based method operating on these representations can overcome. This is the paper's strongest empirical contribution.

- **The feature-specificity finding—that optimal feature subsets are OOD-dataset-specific and do not transfer (Figure 2 right)—is a powerful concrete argument.** If the most discriminative features for detecting one OOD dataset harm performance on another, no single ID-only method can be universally effective. This directly supports the claim of fundamental misspecification.

- **The multi-label ImageNet experiment (Section 4.2) cleanly separates label uncertainty from OOD uncertainty.** Showing that ID images with natural multi-label ambiguity have high label uncertainty and that logit-based methods struggle to distinguish these from true OOD (AUROC ~0.6) provides an elegant, original demonstration of a core pathology.

- **The epistemic uncertainty posterior collapse demonstration (Section 5.3, Figure 6) is clean and counterintuitive.** Showing that better posterior approximation (more data) actually *worsens* OOD detection performance is a sharp result that directly challenges the Bayesian epistemic uncertainty narrative.

- **The paper invites productive disagreement.** The claim is strong enough that a reader knows exactly what evidence would rebut it: show that in practice the gap between supervised OOD scores and true OOD detection is consistently small, or show that the proposed fixes actually resolve the misalignments identified.

## Weaknesses

### Major

- **The "irreducible error" framing is technically imprecise and somewhat overstates the claim, though the underlying point remains valid.** The Oracle classifier used to establish "irreducible error" is a binary *linear* classifier on features (Section 4.1). A nonlinear classifier could potentially achieve higher AUROC on the same features, meaning the claimed "irreducible" error is actually an upper bound on what linear methods can achieve and a lower bound on what is truly irreducible about the features themselves. The paper states "no feature-based method can correctly detect these OOD inputs" (p. 91), but this holds only if no nonlinear transformation of these features can separate ID from OOD. The core insight—that some features are genuinely hard to separate—is still correct and important, but calling it "irreducible" is a stronger claim than the linear Oracle evidence supports. This matters because the paper repeatedly invokes irreducibility to argue that the problem is "fundamentally" unsolvable within the supervised paradigm (e.g., Section 5.6, Section 6).

- **Section 6's constructive prescriptions are thin relative to the scope of the critique.** The paper dismisses every existing approach to OOD detection (feature-based, logit-based, hybrid, outlier exposure, epistemic uncertainty, adding an OOD class, generative models, scaling) but its positive recommendation amounts to "develop principled approaches that directly estimate the probability that an input comes from a different distribution" (p. 276). This essentially restates the goal of OOD detection without providing guidance on how such a method would differ from existing attempts. The paper briefly notes that adding an OOD class can work "if the OOD examples share common structure" (p. 270), and that extensive pre-training helps but is insufficient (p. 274)—these are incremental, not paradigm-shifting. For a paper that advocates abandoning an entire research paradigm, even speculative directions (e.g., density-of-states estimation, support estimation without density modeling, contrastive approaches that don't rely on classification features) would substantially strengthen the contribution. This is a meaningful gap, though not fatal—position papers can be valuable for identifying problems without fully solving them.

### Minor

- **The paper does not discuss self-supervised or contrastive representation learning approaches to OOD detection.** These methods learn representations without ID class labels (e.g., via contrastive objectives), and therefore don't suffer from the same "wrong question" problem in the same way, since they are not trained to discriminate ID classes. The paper acknowledges self-supervised pre-training briefly (p. 274) but only to argue scaling is insufficient—it does not engage with the possibility that self-supervised representations might represent a genuinely different class of method that doesn't share the supervised paradigm's misspecification. This is a notable gap in the paper's coverage but doesn't undermine the core argument about *supervised* methods.

- **The paper does not engage with practical sufficiency arguments.** Even if supervised methods answer a "different question," they may be *practically sufficient* for many deployments. The paper's own data shows AUROC of ~0.78–0.90 for best methods on IN vs. IN-OOD (Figure 9), which is substantially above chance. For asymmetric-cost scenarios (where false positives are tolerable), imperfect-but-easy-to-compute OOD scores may be preferred over principled-but-expensive alternatives. The paper could acknowledge this counterargument more explicitly, though its critique still stands for safety-critical settings.

### Trivial

- None.

## Nice-to-Haves

- A more honest framing of "irreducible error" as "error irreducible by linear methods on these features" or using a nonlinear Oracle to provide a tighter bound.
- More speculative constructive directions in Section 6—e.g., methods that directly estimate distribution membership, density-of-states approaches, or test-time adaptation techniques that could circumvent the misspecification.
- Engagement with self-supervised representation learning as a potentially different paradigm from supervised classification for OOD detection.
- A formal or probabilistic analysis characterizing when and how the "wrong question" answer diverges from the "right question" answer, which would elevate the argument from empirical demonstration to principled theoretical result.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The rhetoric ('wrong question', 'wholly misspecified') is stronger than what the evidence supports."** This is not a valid criticism for a position paper. Provocative framing is a feature, not a flaw. The fact that supervised methods achieve AUROC above chance does not mean they "answer the right question"—a broken clock is right twice a day, and AUROC above random can coexist with fundamental misalignment. The paper's evidence (Oracle bounds, feature-specificity, label/OOD uncertainty conflation) is consistent with "these methods answer a different question that has some correlation with the right one." This is exactly the paper's claim.

- **"The paper should moderate its rhetoric from 'wrong question / wholly misspecified' to 'misaligned / partially informative.'"** Same as above—this is precisely the kind of hedging request that position papers are meant to avoid.

- **"Empirical characterization of when supervised methods work well vs. fail."** This is scope creep. The paper's scope is to demonstrate fundamental misspecification, not to provide a practitioner's guide.

- **"Nonlinear Oracle for feature-based methods."** This is a valid methodological point (moved to Minor above as a nit about the "irreducible" framing), but calling for a different experiment design is a nice-to-have, not a core flaw.

- **"Formal analysis of the misalignment."** Nice-to-have; position papers need not provide formal proofs.

- **"The paper doesn't discuss self-supervised or contrastive methods."** Moved to Minor—that the paper's coverage doesn't extend to every method is a gap but not a core flaw, since the paper is about *supervised* methods specifically.

- **"Epistemic uncertainty section proves less than claimed—the section shows insufficiency but not uselessness."** The paper's argument is not that epistemic uncertainty is *useless* but that it is fundamentally *misaligned* as an approach. Section 5.3 directly states that in the infinite-data limit, epistemic uncertainty collapses, making it worse at OOD detection, which is "exactly the opposite behavior we would desire" (p. 208, 268). This is a fair argument, and claiming the section proves "uselessness" is a strawman.

- **"Generative models section doesn't address typicality corrections."** The paper does explicitly discuss typicality (p. 272): "Moreover, we are more interested in typicality than density... but different notions of typicality can lead to very different OOD detection behavior, and choosing amongst these notions can be arbitrary." This addresses the point, even if briefly.

- **"Outlier exposure section overstates the case—Appendix A.7 shows OE helps for semantic shift."** The main text actually does explicitly acknowledge this (p. 180): "In Appendix A.7, we show that outlier exposure does improve OOD detection for most of the semantic shift OOD benchmarks." The paper makes a nuanced argument that OE helps for semantic shift but hurts covariate shift generalization—it does not "overstate" the case.

- **"The paper is actually a standard research paper, not a position paper."** This paper is clearly a position paper—it argues a normative claim about what the field should do differently, not just presenting experimental results.

## Novel Insights

The error decomposition framework (indistinguishable features vs. irrelevant features, with the Oracle providing an upper bound) is a genuinely novel analytical contribution that goes beyond prior critiques of OOD detection. The specific finding that optimal feature subsets are OOD-dataset-specific—and using features optimized for one OOD dataset can *hurt* performance on another—is an underappreciated insight with direct practical implications: no single ID-only feature weighting can be universally effective. The demonstration that outlier exposure actively harms covariate-shift generalization (with >10% accuracy drops) while only sometimes helping semantic-shift detection is also a novel and practically important finding.

## Suggestions

- Restate "irreducible error" more precisely—e.g., as "irreducible by any linear method on these features" or provide a nonlinear Oracle experiment to strengthen the bound.
- Expand Section 6 with at least 2-3 speculative but concrete research directions that could address the misspecification (e.g., test-time distribution estimation, support-bounded OOD detection, or representation learning objectives that are alignment-aware rather than class-discriminative).
- Briefly acknowledge the self-supervised/contrastive representation learning paradigm and discuss whether it shares or avoids the supervised paradigm's misspecification.

## Score and Decision

**Calibration anchors:**

1. **RV12OsgCO0** (avg 6.67, reject): LLM-generated text detection is misspecified—very similar "wrong question" framing. This paper is stronger because it provides more concrete empirical evidence (Oracle experiments, multi-label analysis, scaling analysis) rather than primarily a survey.

2. **d7hqAhLvWG** (avg 6.25, accept): ASR comparisons are invalid—similar "measurement is misspecified" framing with conceptual + empirical argumentation. This paper is comparable in conceptual rigor but has more extensive supporting experiments and a broader systematic critique.

3. **yqKfMr0yvY** (avg 7.67, accept): LLMs-as-judges are premature—comprehensive critique backed by measurement theory. This paper provides similarly systematic critique but with more novel empirical demonstrations.

4. **5X4GDSUumr** (avg 7.0, reject): TSF benchmarks are unreliable—extensive empirical evaluation (3500+ experiments). This paper is less exhaustive in experiments but has a clearer, more provocative position.

5. **OmQ9tUouSS** (avg 3.67, reject): Symbolic rules can't constrain AI—fundamentally flawed argumentation without empirical support. This paper is far stronger, with concrete evidence throughout.

The paper under review has a clear, provocative, well-argued position with novel empirical demonstrations supporting it. Its main weakness is the thin constructive section and the imprecise "irreducible" claim, but these don't undermine the core argument. Compared to the "wrong question / misspecified measurement" papers at NeurIPS that scored 6-8 (RV12OsgCO0 at 6.67, d7hqAhLvWG at 6.25, yqKfMr0yvY at 7.67), this paper's contribution is substantial. It is somewhat less novel in theoretical framework than d7hqAhLvWG (which imported social science measurement theory) but has more direct empirical evidence. The thin Section 6 is a real gap but not fatal for a position paper that clearly identifies a fundamental problem. I place this above the detection misspecification papers (6.25-6.67) because the empirical evidence is stronger and more novel, and below the LLM-judges paper (7.67) which had deeper interdisciplinary grounding and more constructive guidance.

MY FINAL SCORE: <pineapple>7</pineapple>
MY FINAL DECISION: <orange>Accept</orange>