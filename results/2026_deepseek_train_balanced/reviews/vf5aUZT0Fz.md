## Summary

This paper proposes DEPT, a pre-training framework that trains language models on heterogeneous multilingual/multi-domain data using a federated-style iterative loop with periodic parameter averaging. DEPT offers three embedding-handling variants — Glob (shared global embeddings), Trim (vocabulary-trimmed embeddings, saving up to 80% parameters), and Spec (fully specialized per-source embeddings enabling vocabulary-agnostic training). The paper demonstrates that DEPT variants improve training stability, generalization, and plasticity compared to standard mixed-data pre-training, and reports the first 1.3B-parameter vocabulary-agnostic federated multilingual model.

## Strengths

1. **Concrete and well-documented efficiency gains.** The memory and communication cost analysis (Table 1) is formalized with clear formulas. Trim achieves up to 80% reduction in embedding parameters while matching the performance of the full-embedding Glob variant. The 1.3B vocabulary-agnostic model (Spec) reduces embedding size from 512M to 102.4M — a genuine practical achievement.

2. **Empirical evidence of training stability under heterogeneity.** Figure 1 directly shows that the standard training pipeline on The Pile (350M, 24-block) suffers from activation norm spikes and diverging parameter norms, while DEPT variants avoid both. This is the paper's most compelling visual evidence that the iterative OuterOpt parameter averaging provides a regularization benefit.

3. **Plasticity advantages demonstrated on new languages.** Figure 3 shows adaptation curves where DEPT variants converge faster and to lower perplexity than baselines when adapting to out-of-distribution languages (Hindi, German) and the lowest-resource training language (Swahili). The comparison includes Active Forgetting, a method designed for exactly this purpose.

4. **Spec variant enables vocabulary-agnostic federated pre-training for the first time.** By never sharing token or positional embeddings, Spec allows training on data sources with entirely different tokenizers/vocabularies. This is a genuinely novel capability with practical relevance for privacy-sensitive or multi-party training scenarios.

## Weaknesses

### Major

- **The evidence does not isolate decoupling as the driver of generalization/plasticity gains.** DEPT differs from standard pre-training in two ways: (a) it replaces mixed-data training with an iterative, source-by-source federated regime with periodic parameter averaging (OuterOpt), and (b) it partially or fully decouples embeddings. The Glob variant uses only (a) without meaningful decoupling (it shares full global embeddings), yet Glob also outperforms baselines. The paper's text reports that "Trim is comparable to Glob" and "Spec is very similar in effectiveness to Glob and Trim" (line 186). This means all three variants perform similarly regardless of whether embeddings are decoupled or not. The observed improvements could therefore be driven entirely by the iterative training regime (parameter averaging), not by embedding decoupling. A proper control — comparing Glob against an iterative version of standard mixed-data training that also uses periodic parameter averaging — would be needed to attribute benefits to decoupling. As presented, the paper's central framing (title, abstract, contribution claims) attributes improvements to decoupling, which the experiments do not support.

- **The "min and max improvements" reporting is non-standard and potentially obscures variant-level failures.** The paper reports (line 186) generalization results by comparing the interval [worst DEPT, best DEPT] against the single best baseline. This does not tell the reader whether a specific DEPT variant consistently beats a specific baseline on a specific setting. If some variants underperform the best baseline on some tasks, this reporting choice hides it. Standard reporting of each variant's performance against each baseline would be more informative.

### Minor

- **No variance or repeated trials reported.** Given the multiple sources of randomness (initialization, data ordering in iterative training, language sampling, OuterOpt stochasticity), single-seed results make it impossible to assess whether reported differences are reliable. This is especially relevant for the "16 out of 28" win rate on continued pre-training (line 188), which at ~57% is close to parity. While multiple seeds are not always standard at this training scale, the strength of the paper's claims demands some measure of reliability.

- **The HPO-avoidance claim is overstated.** The paper claims DEPT "avoids" costly HPO (line 30), but DEPT introduces alternative hyperparameter choices: number of inner-loop steps, OuterOpt method, variant selection, and per-source tokenizer design. These may also require tuning, especially when comparing across heterogeneous data sources.

- **The theoretical grounding for from-scratch decoupling is weaker than presented.** The paper cites MonolingualTransferArtetxe (transformers adapt to new languages by re-learning embeddings) and ActiveForgetting (periodic embedding resets) as evidence that "transformer body performance is partly independent of embeddings" (line 42). Both works study *post-hoc transfer or adaptation* from a pre-trained model, not pre-training *from scratch* without consistent embeddings. Whether a transformer body can learn useful representations when tokens map to entirely different embeddings across iterations is a fundamentally different question that the cited evidence does not address. This does not invalidate the method (the experiments do show it works) but the claimed foundation should be tempered.

### Trivial

- None beyond the minor points above.

## Nice-to-Haves

- **A representational analysis of the decoupled transformer body** would strengthen the paper's most interesting scientific claim (that the body learns "abstract representations" from specialized embedding spaces). Probing, similarity analysis, or attention-pattern comparisons could illuminate what the decoupled body actually learns.
- **Deeper comparison with ActiveForgetting** — given the conceptual similarity (both methods stress embedding plasticity), the paper could analyze *why* DEPT outperforms ACT beyond noting that it does.

## Removed Points

The following points from the input reviews were removed with justification:

1. **"675× claim against inapplicable baseline, 25% buried deep in text"** — Factually wrong. Both numbers appear in the same sentence in the abstract (line 33): "communication costs up to 675× lower than standard distributed data parallelism and 25% lower than Local SGD for billion-scale models." The 25% is not buried. (Removed per Hard Rule: factually wrong.)

2. **"Trim zero-padding prevents cross-source transfer for rare tokens"** — The paper explicitly states zero-padded tokens are ignored during aggregation "to prevent interference from non-shared tokens across data sources" (line 85). This is a deliberate design choice, not an oversight. (Removed per Hard Rule: strawman/paper already addressed.)

3. **"Spec requires final global embedding"** — The paper's Limitations section (Section 4.1, line 226-227) explicitly acknowledges this and discusses future approaches for obtaining global embeddings. (Removed per Hard Rule: paper already addressed.)

4. **"Communication costs comparison to DDP is less relevant"** — The paper provides both the DDP comparison (for the specific baseline of standard DDP without gradient accumulation) and the Local SGD comparison (25% improvement). Both appear in the abstract. The critic's framing that this is misleading does not withstand verification. (Removed per Soft Rule: both baselines are provided and contextualized.)

5. **"Glob would likely show same plasticity due to flat minima"** — This is speculative reasoning about parameter averaging producing flat minima, without evidence in the paper or from the reviewer. (Removed per Filtering Discipline: speculative claim not grounded in paper.)

6. **"Vocabulary reduction percentages not reproducible"** — The paper reports specific ranges (8%–32% for multilingual, 2%–78% for The Pile) and identifies the mathematics subset as achieving 78%. This is sufficient detail for a paper at this stage. (Removed per Filtering Discipline: nitpick.)

7. **"No analysis of what decoupled body learns"** — Acknowledged as a missed opportunity but not a weakness — the paper explicitly lists this as future work (line 227). (Moved to Nice-to-Have.)

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface observations that the paper itself does not make.

## Suggestions

1. **Add a control experiment:** Compare Glob (iterative training with shared embeddings) against a version of standard mixed-data training that also uses periodic parameter averaging (the same OuterOpt). This would isolate whether the iterative regime or the decoupling is responsible for the observed gains, and would determine whether the paper's central attribution to "decoupling" is correct.

2. **Report variance:** Add at least 2–3 seeds for the main comparisons (random init evaluations, plasticity experiments) or provide a clear justification for single-seed reporting.

3. **Report each variant's individual performance** against each baseline, rather than reporting a range across all DEPT variants against the best baseline. This would allow readers to assess which specific configurations are reliably superior.

4. **Temper the decoupling claims** to reflect what the evidence actually supports: that the DEPT *training framework* (iterative source-by-source training with periodic parameter averaging) produces better-grounded transformer bodies, and that the decoupling variants (Trim, Spec) add practical efficiency benefits and vocabulary-agnostic capability.

## Score and Decision

The paper tackles a genuine problem and provides a practically useful framework with measurable efficiency gains. The Spec variant's vocabulary-agnostic capability is a genuinely novel contribution. However, the paper's central scientific claim — that *decoupling embeddings* drives improved generalization and plasticity — is not supported by the evidence, which confounds the decoupling with the iterative training regime. Since all three variants (including Glob, which does not decouple) perform similarly, the observed gains likely stem from the OuterOpt parameter averaging rather than decoupling per se. The paper would benefit from the missing control experiment and a recalibration of its claims. In its current form, the gap between the framing and the evidence is too wide.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>