Now I have enough calibration data. Let me synthesize my final review.

**Calibration summary:**

| Anchor | Score | Decision | Comparison to DNA |
|--------|-------|----------|-------------------|
| AONM (ar9tcnD4e9) | 4.75 | Reject | DNA clearly stronger — real datasets, larger scale, competitive baselines |
| LCN/Overconnectivity (qMUtej58Pc) | 5.50 | Reject | DNA stronger — ImageNet/language vs mostly CIFAR-10, more analysis |
| DNRT (HiTg16qhxp) | 5.50 | Accept | DNA more novel, DNRT has better ablations; comparable overall |
| Dynamic-LLaVA (hzVpZDrW73) | 6.00 | Accept | DNA more novel but weaker evidence; Dynamic-LLaVA more rigorous |
| Dynamic MoE (T26f9z2rEe) | 7.00 | Accept | DNA more ambitious but much weaker empirical validation |

**Round-1 bracket:** 4.75–7.00 → narrowed to approximately 5.0–6.5
**Round-2 narrowing:** DNA sits above the 4.75–5.50 rejected papers but below the 6.00–7.00 accepted papers. Closest comparable is DNRT at 5.50 (Accept) — DNA has more novelty but weaker evidence. 

**Final score: 5.5, Reject** — The paper introduces a genuinely novel architectural paradigm with cross-domain feasibility demonstration, but the interpretability claims (the paper's main analytical contribution) are anecdotal, the performance comparison is confounded by parameter counts, and there are no ablation studies. Borderline; strong rebuttal addressing the major weaknesses could raise it to acceptance.

---

## Summary
This paper introduces Distributed Neural Architectures (DNA), a new architectural paradigm where tokens are dynamically routed through an unordered collection of computation modules by learned routers — the connectivity pattern itself emerges from training rather than being hard-coded. The authors train DNA models on ImageNet (vision) and FineWeb-Edu (language), demonstrating trainability and analyzing emergent routing patterns including power-law path distributions, interpretable module specialization, and learned compute allocation. The paper explicitly frames itself as a concept/feasibility demonstration, not an attempt to beat SOTA.

## Strengths
- **Genuinely novel architectural paradigm with clean formulation**: The DNA framework (Section 2.1) describes how tokens can traverse any series of modules in any order, with Eq. 1 providing a concrete forward-pass mechanism. The conceptual unification of MoE, MoD, parameter sharing, and early exit under a single routing-then-combine framework opens a new design space that is distinct from prior work.
- **Cross-domain feasibility demonstration**: The paper validates DNAs on both discriminative vision (ImageNet, 300 epochs) and generative language (FineWeb-Edu, 21B tokens), showing the paradigm is not domain-specific. This is a non-trivial engineering achievement given the non-standard forward pass.
- **Discovery of power-law path distribution**: The finding that token paths follow a power-law distribution (exponent −1 for vision, −1.2 for language; Fig. 1c,d) is a novel empirical observation. The paper honestly reports that random models also produce power-law distributions, providing useful calibration and opening questions about what training changes.
- **Emergent behaviors without hand-crafted incentives**: The paper deliberately omits load-balancing losses, yet models develop specialized paths (Fig. 3), interpretable compute allocation (Fig. 5), and emergent parameter sharing. The bias-based identity-module mechanism (Eqs. 2–3) is a simple, effective design for encouraging compute skipping.
- **Honest reporting of negative evidence**: The paper commendably reports that (a) random models produce power-law path distributions, (b) parameter sharing in language models appears random (Section 4.3), and (c) the DNA-skip model underperforms a shallower GPT-2 baseline (Table 3). This transparency is a genuine strength.

## Weaknesses

### Fatal
None.

### Major
- **Parameter-count confound in the "competitive with dense baselines" claim**: In the language domain, the top-1 DNA has 583M total parameters vs. 406M for GPT-2 Medium (44% more), and the top-2 DNA has 603M (49% more). The paper emphasizes "active parameters," but total parameter count determines memory footprint and storage cost — first-order practical concerns for the efficiency motivation the paper invokes. In vision, the top-1 DNA uses 34M total vs. 22M for ViT-Small (55% more) to close a 0.7pp gap. The one comparable case (top-2 DNA vision at 18M total vs. 22M ViT) uses different embedding dimensions (256 vs. 384) and also differs in MLP dimension and head count (Table 1), so it does not isolate the architectural contribution.
- **Interpretability analysis is anecdotal and lacks systematic validation**: The paper claims paths are "highly interpretable" (Sec. 3.2) and routing decisions are "often human-interpretable" (Sec. 1). The evidence consists of four hand-picked paths (Fig. 3), two paragraphs for language routing (Fig. 8), and deep-dream visualizations of three images (Fig. 4). There is no quantitative metric for specialization, no baseline comparison (e.g., do dense model attention heads show similar clustering?), and no measure of how representative the shown examples are. For a paper whose central analytical contribution is understanding emergent structure, qualitative cherry-picking is insufficient.
- **No ablation studies for key architectural choices**: The paper does not isolate the effects of backbone size (Nb), number of modules (Nm), top-k value, or the identity-module bias mechanism. Without these, the reader cannot assess which design choices are load-bearing or how sensitive emergent behaviors are to hyperparameters. This is a significant gap for a paper introducing a new architecture.
- **The shallower GPT-2 baseline outperforms DNA-skip on all metrics but is not discussed**: Table 3 shows GPT-2 (30% shallower) outperforming top-2 DNA (30% skip) on every benchmark — loss, ARC-E, BoolQ, HellaSwag, LAMBADA, PIQA, RACE, and WikiText. This directly tests whether learned skipping beats simply having fewer layers, and the answer is no at this scale. Including this result is commendable, but offering zero analysis of it is a significant omission that undermines the efficiency claims.

### Minor
- **Power-law distribution in random models weakens the "emergent structure" interpretation**: The paper acknowledges that random models produce power-law path distributions (Fig. 1 caption) but does not adequately reckon with the implications. If untrained models produce the same structural signature, the power law is at least partly an architectural artifact. The difference in exponent (−1 random vs. −1.2 trained language) is noted but never analyzed for significance. The paper continues to frame the power law primarily as a finding about trained models.
- **Dead modules not quantified**: The paper deliberately omits load balancing, and Fig. 2 (bottom) shows some modules are never activated. However, the fraction of dead modules and unused parameters is never reported. This is essential context for interpreting what "emergent structure" means — if many modules are dead, specialization occurs in a degenerated subset.
- **"Generalizes MoE/MoD" claim is asserted but not empirically demonstrated**: The abstract and Section 1 claim DNAs are a natural generalization of MoE, MoD, parameter sharing, etc., but the paper never shows a DNA recovering these architectures under appropriate constraints. This remains a conceptual claim.
- **Architecture-imposed constraints under-analyzed**: Backbone layers (Nb = 0,1,2) process all tokens, the router-per-step design imposes sequential structure, and smax caps routing depth. The paper acknowledges some limitations but does not ablate or analyze how they constrain the space of possible architectures.

### Trivial
None.

## Nice-to-Haves
- Quantify FLOPs and memory usage in hardware-relevant metrics to connect efficiency claims to practical deployment.
- Compare specialization patterns against baselines from dense model analysis (e.g., attention-head clustering in standard transformers).
- Report how path distributions and specialization evolve over training (not just at the final checkpoint), which would distinguish learned structure from architectural priors.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Eq. 1 is awkward and inelegant"** — Pure style nitpick. The footnote explains the formulation clearly and it serves its purpose.
- **"Bias update rule (Eq. 3) is ad-hoc and not principled"** — The mechanism is adapted from prior work (DeepSeek, Liu et al. 2024) and the paper is transparent about this. Whether it is "principled" is a matter of taste.
- **"Fig. 1 caption says 'no notion of depth' but router-per-step imposes sequential structure"** — The paper makes a conceptual claim about unordered module connectivity, not about the absence of sequential steps. Section 2.2 explicitly discusses the step-based arrangement.
- **"Deep-dream reconstructions classified incorrectly, so analysis is weak"** — The paper is transparent about classification results (Fig. 4 caption) and the claim is about feature development, not perfect reconstruction. The misclassification is acknowledged, not hidden.
- **"No FLOPs/memory quantification"** — The paper explicitly defers real-world inference optimization to future work (Section 2.2). This is a scope limitation, not a flaw.
- **"Dismissal of random baseline as 'superficial features' is asserted without evidence"** — The paper cites signal propagation theory (Schoenholz et al. 2016) and refers to Appendix G.2 for further discussion.
- **"The architecture is not truly distributed because of backbone layers"** — The paper is upfront about backbone layers as a practical optimization choice for a first demonstration.
- **"Missing related works"** — Reviewer knowledge gaps; cannot verify.

## Novel Insights
The most genuinely novel observation in this work is that the power-law path distribution appears in both trained and randomly initialized DNA models, suggesting it is a fundamental combinatorial property of the routing architecture rather than exclusively a learned structure. This shifts the interesting scientific question from "do paths follow a power law?" to "how does training reshape which tokens take which paths within this distribution?" — a more nuanced framing that the paper gestures at but does not fully develop.

## Suggestions
- Match dense baselines on total parameter count (not just active parameters) to provide a clean comparison. This would directly test whether the routing overhead pays for itself.
- Define a quantitative measure of path specialization (e.g., mutual information between path assignment and class label, clustering purity) and compare against baselines (random DNA, dense model attention-head clustering). This would transform the interpretability analysis from anecdotal to systematic.
- Discuss the shallower GPT-2 comparison explicitly — that learned skipping underperforms simple layer removal is an important calibration of the method's current limits and deserves analysis.
- Report the fraction of dead modules and analyze how they relate to the specialization and power-law findings.
- Add ablation studies for Nb, Nm, top-k, and the bias mechanism to clarify which design choices are load-bearing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>