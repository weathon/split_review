Now I have enough information. Let me write the final consolidated review.

## Summary

This paper introduces and formalizes a previously overlooked problem in machine unlearning: the decoupling of class labels from target concepts. Beyond the conventional "all-matched" setting where the forgetting data, model output, and target concept all align, the authors identify three mismatch scenarios (target mismatch, model mismatch, and data mismatch) that arise when the unlearning request does not conform to the pre-training taxonomy. They provide theoretical analysis via "representation gravity" (Theorem 3.2) linking forgetting dynamics to representation distance, and propose TARF, a unified framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on identified retaining data. Experiments on CIFAR-10/100, ImageNet-1k, stable diffusion concept removal, and TOFU/LLaMA demonstrate consistent improvements over baselines.

## Strengths

1. **Novel problem formulation that expands the unlearning landscape.** The paper identifies a genuine practical gap — prior class-wise unlearning assumes the target concept coincides with the class label, which fails when unlearning requests involve semantic concepts that are subsets, supersets, or cross-cuts of pre-training classes (Section 3.1, Figure 1). The four-scenario taxonomy (all-matched, target mismatch, model mismatch, data mismatch) is clearly defined and well-motivated.

2. **Theoretical grounding of forgetting dynamics via representation distance.** Theorem 3.2 provides a formal bound connecting the loss-change gap between two data subsets to their representation distance, formalizing the intuition that nearby representations co-move during gradient ascent ("gravity effect"). This is validated empirically in Figure 3 with t-SNE visualizations and loss trajectories, and directly motivates the two-phase design of TARF.

3. **Consistent and often dramatic superiority across all mismatch settings.** In Table 3, TARF achieves the lowest Gap (averaged deviation from the Retrained reference) across all four settings on both CIFAR-10 and CIFAR-100. For example, on CIFAR-100 target mismatch, TARF achieves Gap=0.21 vs. the next best (GA) at 8.86 — a ~40× improvement. Every prior baseline fails badly on at least one mismatch setting (e.g., GA's Gap jumps to 45.68 on model mismatch, SCRUB's jumps to 46.76 on data mismatch).

4. **Scalability and real-world validation.** Results on ImageNet-1k (Table 4) show TARF maintains low Gap with manageable runtime, while many baselines collapse (e.g., GA drops RA to 31.21 on target mismatch). Real-world case studies on stable diffusion concept removal (Figure 6) and TOFU/LLaMA personal information removal (Table 5) demonstrate the framework generalizes beyond image classification.

5. **Practical and validated target identification mechanism.** Phase I uses accuracy drops after brief gradient ascent to automatically identify false retaining data without additional supervision. Figure 5(a) quantitatively shows that classes belonging to the target concept exhibit significantly larger accuracy drops, enabling effective filtering.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims.

### Minor

1. **Unclear scope of UA in target/data mismatch settings.** The paper defines UA as "accuracy of the unlearning targeted subset" (Section 4.1). For target mismatch and data mismatch, where D_f ⊂ D_t (the forgetting data is a proper subset of the target concept), UA is evaluated only on the given forgetting data D_f. This does not directly measure whether the *full target concept* (including the false retaining data D_fr) is forgotten. While the Gap metric and the identification phase (Phase I) provide indirect evidence, the paper would be strengthened by reporting separate UA on D_f and D_fr for these settings in the main table (as it already does for model mismatch in Table 2). The results in the appendix do include finer-grained evaluation, but the main table's single UA number is ambiguous without additional context. This is an *evidential presentation* issue rather than a methodological flaw — the conclusions are likely correct, but the headline evidence is less direct than it should be.

2. **Heuristic nature of Phase I identification.** The target identification relies on accuracy drops after gradient ascent to detect false retaining data. This works well on structured label hierarchies (CIFAR-10/100 superclasses) but the paper itself acknowledges (in the Open Challenges section) that "the representation gravity signal weakens when concepts are inherently ambiguous or attribute-entangled." The paper does not quantify identification precision/recall or test on datasets where the superclass structure is noisy or overlapping. While this is recognized as a limitation for future work, it means the method's applicability in truly open-world scenarios is uncertain.

3. **Known-class assumption for target mismatch.** The paper assumes "the number of classes in D_un belonging to the target concept is known" (Section 2). This is a nontrivial assumption that may not hold in practice without additional annotation or semantic knowledge.

### Trivial
- The "representation gravity" metaphor is striking but not formally defined until Definition 3.3, which could confuse readers initially.

## Nice-to-Haves

- A brief hyperparameter sensitivity study for t₀, t₁, and β (beyond k) in the main text would help practitioners.
- Quantifying Phase I identification precision/recall across class hierarchies would reduce concern about heuristic fragility.
- Standard deviation bars on Gap in the main tables (even if the full table with std is in the appendix) would improve readability.

## Removed Points

- *Criticism about statistical significance / missing std in main tables*: The paper explicitly states that full results with mean and std are in Appendix F.7. This is standard practice.
- *Criticism about time overhead of Phase I*: Table 3 shows TARF's TIME is comparable to FT and L1-sparse, and the paper discusses computational cost in Appendix E.2.
- *Criticism about missing related works*: Not verifiable without external sources.
- *Strength about "addressing important problem"*: Generic; removed per filtering rules.
- *Criticism about formatting/style*: Parser artifacts, not author errors.

## Novel Insights

The most interesting synthesis from the reviews is that the paper's core limitation — reliance on clean hierarchical label structure for Phase I identification — is simultaneously its strength: the mismatch taxonomy is most well-defined precisely where existing structure (e.g., superclass annotations) makes the problem tractable. The reviews collectively suggest the paper would benefit from *quantifying* this boundary (e.g., under what level of label noise or concept ambiguity does Phase I break down?) rather than merely acknowledging its existence.

## Suggestions

1. **Clarify UA scope in the main text.** Add a footnote or table note explicitly stating which subset UA is computed on for each setting. Better yet, add a column "UA on D_f" and "UA on D_fr" for target/data mismatch in a companion table alongside Table 3 — this would directly address the most substantive concern.

2. **Quantify Phase I identification accuracy.** Report precision/recall of identifying false retaining classes as a function of GA steps or the β threshold, at least for the main benchmarks. A single figure showing this (even in the appendix) would substantially strengthen the claim that the method works in practice.

3. **Relax or discuss the known-class-count assumption.** If the number of false-retaining classes is unknown in practice, can the β threshold or quantile-based selection be used without this knowledge? A brief discussion would improve practical guidance.

## Score and Decision

**Bracketing (Round 1):** The paper sits well above anchors in the (0, 3.5) band (which score ~2.50–3.00 and are clearly weaker unlearning papers with limited scope). It is comparable to or stronger than anchors in the (3.5, 7.5) band, including CGfWyU28Pd (4.50, limited-scope theory paper), OHOmpkGiYK (5.75 — the same paper at a different venue, rejected but with split scores 6,6,3,8), and SIZWiya7FE (6.00 — accepted supervision-free unlearning paper). The paper clearly does not reach the (7.5, 11) band (which contains papers scoring 7.60–8.00 with different problem types). **Initial bracket:** [5.5, 7.0].

**Narrowing (Round 2):** Compared to OHOmpkGiYK (5.75, the same paper), the current version addresses some presentation concerns but the core content is similar. Compared to SIZWiya7FE (6.00, accepted), this paper has a more novel problem formulation and stronger empirical results, but SIZWiya7FE has cleaner exposition. Compared to wAemQcyWqq (5.67, rejected), this paper has fewer methodological concerns and stronger evaluation. The paper is stronger than the 5.67–5.75 anchors and comparable to the 6.00 anchor. The UA clarity issue prevents it from being clearly above the 6.00 anchor. **Final score: 6.5.**

**Calibration anchors consulted:**

| anchor_id | avg_score | Round | Comparison |
|-----------|-----------|-------|------------|
| Xagys9QD3T | 3.00 | R1 | Much weaker; limited method, thin evaluation |
| hwXUmwJAq5 | 3.00 | R1 | Much weaker; narrow scope |
| BJfIDS5LsS | 2.50 | R1 | Much weaker; limited experiments |
| 85X9awoVtv | 2.50 | R1 | Much weaker; different problem (auditing, not unlearning method) |
| CGfWyU28Pd | 4.50 | R1 | Weaker; theory-only on fine-tuning, limited empirical scope |
| OHOmpkGiYK | 5.75 | R1/R2 | Same paper at another venue; scores 6,6,3,8 |
| TLBPjECC5D | 5.25 | R1 | Weaker; simpler method, less comprehensive evaluation |
| SIZWiya7FE | 6.00 | R1/R2 | Comparable; different novel problem, accepted, similar quality |
| wAemQcyWqq | 5.67 | R2 | Weaker; practicality concerns with the oblivious approach |
| CIN2VRxPKU | 5.33 | R2 | Weaker; narrower scope (LLM evaluation framework, not method) |
| pUOesbrlw4 | 5.25 | R2 | Weaker; training-free approach, less comprehensive |
| 51WraMid8K | 8.00 | R1 | Stronger; different genre (LLM evaluation framework, not unlearning method) |
| EUSkm2sVJ6 | 7.60 | R1 | Stronger; different problem (data usage inference) |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>