Now I have a thorough understanding of the paper and can synthesize the final review.

## Summary

This paper extends the formal analysis of faithfulness (soundness + completeness) for rule extraction from the Neural-LP model to DRUM, a more expressive differentiable rule learning model. It proves that no Datalog program can be faithful for general DRUM models (Theorem 2), proposes extended Datalog with inequalities (multipath rules) and three extraction strategies—Algorithm 1 (general but infeasible), Algorithm 2 (dataset-specific), and restricted model variants MMDRUM/SMDRUM—and provides theoretical faithfulness guarantees for each. The evaluation compares model predictive performance and demonstrates that standard extraction covers <7% of predictions, motivating the need for faithful extraction.

## Strengths

- **Clean formal framework extending Neural-LP analysis to DRUM**: Theorems 1 and 2 extend prior Neural-LP faithfulness results to the structurally different DRUM model (which has multiple sub-models, different rule-length mechanisms, and inverse rules). Theorem 2 establishing that no Datalog program can be faithful for certain DRUM models is the key negative result that motivates the entire paper. Lemma 1 precisely identifies DRUM's counting semantics as the root cause of incompleteness.

- **Multipath rule formalism (Definition 1) as a principled solution**: The introduction of multipath conjunctions with inequalities and disjunctions is a natural mechanism for encoding counting behavior in a rule language under the UNA, enabling faithful representation of DRUM models that Datalog alone cannot capture. This advances prior work (Tena Cucala et al., 2022b) where faithful extraction was limited to significantly restricted Neural-LP models.

- **Demonstrates practical relevance of the problem**: Table 2 shows that standard threshold-based extraction from DRUM covers less than 7% of model predictions across all benchmarks, providing concrete empirical evidence that faithful extraction is needed, not just a theoretical concern.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient empirical validation of the core claim—faithful rule extraction**: The paper's central promise is faithful rule extraction, yet the evaluation provides minimal direct evidence that any proposed method actually produces faithful rules on real benchmarks. While the paper states (Section 6) that it "verified empirically the theoretical guarantees for these algorithms provided in Theorem 4 and Theorem 5," no table or systematic results explicitly demonstrate that T_R(D) = T_M(D) on the KG completion benchmarks. Table 3 shows only a handful of top-ranked rules on the tiny Family dataset without explicit faithfulness verification. For MMDRUM where Theorem 5 guarantees faithfulness by construction, a simple check of T_R(D_test) = T_M(D_test) would have been straightforward and persuasive. Algorithm 2 (Theorem 4) receives no runtime or scalability data despite being presented as a practical solution. This gap between the theoretical claims and the thin empirical demonstration is the paper's most significant weakness.

- **Only one of three proposed approaches is clearly practical, yet this limitation is undersold in the abstract/introduction**: Algorithm 1 is acknowledged as infeasible. SMDRUM faithful extraction is exponential-time (Proposition 1) and run "best effort for a fixed length of time" (Section 6). Only MMDRUM extraction (Theorem 5) is clearly feasible and comes with a faithfulness guarantee—yet MMDRUM's extraction is essentially the standard DRUM extraction with a modified scoring formula (Equation 7 vs Equation 4). The abstract claims "a novel algorithm where the output rules... ensure both soundness and completeness," referencing Algorithm 1, without flagging its practical infeasibility up front. The introduction would be more honest if it foregrounded that the main practical contribution is the MMDRUM model restriction.

- **The expressivity-performance tradeoff for MMDRUM is significant on some benchmarks, and the paper's "competitive performance" claim is strained**: On WN18RR, MMDRUM achieves 69.0% vs. DRUM's 79.3% accuracy—over a 10pp gap. On FB15k-237-hierarchy, MMDRUM's AUPRC drops substantially. The abstract states the models achieve "competitive performance," which is only true for some splits. The paper does not thoroughly analyze when the faithfulness guarantee justifies the expressivity loss, which is essential for practitioners considering this tradeoff.

### Minor

- **MMDRUM rule extraction is theoretically straightforward**: Theorem 5's guarantee follows directly from the model restriction (replacing sums with maxes), making the extraction algorithm itself a minor modification of standard DRUM extraction. The insight is in identifying that the counting behavior causes incompleteness and that removing it enables faithful extraction, not in algorithmic novelty. The paper appropriately presents this, but readers should not overestimate the extraction contribution.

- **Dataset-specific nature of Algorithm 2 limits transferability**: The rules extracted by Algorithm 2 are tied to a specific dataset and cannot be directly transferred, which constrains its practical applicability. The paper acknowledges this but does not discuss implications.

- **Interpretability concern for multipath rules with many body atoms or high cardinalities**: The paper acknowledges (Section 7) that faithful rules with many body atoms may be hard to interpret, but does not analyze typical cardinalities or rule lengths in extracted programs, leaving an important practical question unanswered.

## Nice-to-Haves

- Explicit empirical verification of faithfulness (T_R(D) = T_M(D)) for MMDRUM on the KG completion benchmarks, including timing results for extraction.
- Runtime and scalability analysis for Algorithm 2 on the KG benchmarks.
- Systematic characterization of what rule classes DRUM can learn that MMDRUM cannot, beyond the single "citizen ← bornIn ∧ livesIn" example.

## Removed Points

- **Claim that Algorithm 2 is "entirely unevaluated"**: The paper states at line 201 that it "implemented the rule extraction algorithms in Section 5" and "verified empirically the theoretical guarantees for these algorithms provided in Theorem 4 and Theorem 5." This claim exists, even if the evidence is thin. The real concern is insufficient detail, not complete absence.

- **Claim that "none" of the extraction methods is demonstrated to produce faithful rules**: Same as above—the paper claims verification, though the evidence presented is insufficient.

- **Demand for Algorithm 1's formal complexity**: The paper acknowledges its infeasibility; a precise complexity bound would be nice but is not essential given Algorithm 1 is explicitly set aside.

- **Claim that standard DRUM extraction comparison is unfair**: The comparison of standard extraction (with γ=β) is intentionally designed to show incompleteness—that's the point of Table 2.

- **Missing related works**: No external verification possible.

- **Formatting/typos**: Parser artifacts, not author errors.

- **Demand for proofs in appendix**: The appendix was stripped by the parser.

- **Reproducibility concerns about hyperparameters**: Standard for this type of work.

## Novel Insights

The paper's most interesting insight is the formal identification of DRUM's counting semantics (Lemma 1) as both the source of its expressivity advantage over standard Datalog and the fundamental obstacle to faithful extraction in Datalog. This creates a precise tradeoff: faithfulness requires either extended Datalog with inequalities (which preserves model expressivity but is computationally prohibitive) or model restrictions that sacrifice expressivity. The practical implication is that there is no free lunch—inquisitive users must choose between a faithful but less expressive model (MMDRUM) or an expressive model whose extracted rules cannot be faithful.

## Suggestions

- Add a table explicitly showing T_R(D_test) = T_M(D_test) verification for MMDRUM on all benchmarks. This is straightforward: extract rules per Theorem 5, apply them to test datasets, compare with model outputs.
- Report runtime for Algorithm 2 on each benchmark, along with the number and size of dataset-specific rules extracted.
- Tone down "competitive performance" in the abstract by acknowledging the significant gaps on WN18RR, and add a brief discussion of when MMDRUM's faithfulness guarantee is worth the expressivity loss.

## Score and Decision

The paper makes a solid theoretical contribution—extending faithfulness analysis from Neural-LP to DRUM with clean negative and positive results—and the problem is genuinely important. However, the practical contribution is thinner than presented: only MMDRUM extraction is clearly practical, the abstract overclaims about the general algorithm's feasibility, and the empirical validation of the core promise (faithful extraction actually working) is surprisingly thin for a paper centrally about faithfulness guarantees. The theory is publishable, but the evaluation needs strengthening.

Originality: Good—the extension to DRUM with counting semantics is non-trivial. Importance of research question: High—faithfulness in rule extraction matters for safety-critical applications. Claims support: Moderate—theoretical proofs are solid, but empirical validation of practical extraction is thin. Soundness of experiments: Moderate—predictive performance is well-evaluated, but faithfulness verification is lacking. Clarity: Good—formal framework is clean. Value to community: Moderate-to-good.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>