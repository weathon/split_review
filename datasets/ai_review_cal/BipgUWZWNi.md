- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have a thorough understanding of the paper and can verify each claim against the text. Let me construct the final consolidated review.

## Summary

This paper proposes MCBM-Seq and MCBM-Joint, methods that use decision trees to inspect, quantify, and spatially control information leakage in Concept Bottleneck Models. The key idea is: (1) train a hard CBM (leakage-free) with a decision tree label predictor; (2) for each leaf, train a sub-tree using mixed concept representations — soft probabilities for concepts used in the decision path, hard binary values for others; (3) compute information gain on soft splits as a leakage estimate. The main claimed contributions are a concrete, per-path leakage quantification and the ability to constrain leakage to specific data subsets rather than the whole model.

## Strengths

1. **Operational definition and tree-based quantification of leakage.** Definition 3.1 formulates leakage as \(I(y;\hat{c}|c)\), and Equation 5 shows this can be approximated by information gain on soft-concept splits in the sub-trees. This provides a concrete, computable measure that prior work (Mahinpei et al. 2021, Havasi et al. 2022) lacked. The information gain per split gives fine-grained attribution of where and by how much leakage occurs.

2. **Novel mixed-concept representation that spatially constrains leakage.** The three-step MCBM-Seq algorithm (Algorithm 1, Figure 1) first builds a hard (leakage-free) decision tree, then selectively extends only those leaf nodes where leakage can improve classification, using hard values for non-path concepts. This is architecturally distinct from residual-layer or side-channel approaches (Yuksekgonul et al. 2023, Shang et al. 2024) that introduce uninterpretable latent signals across the entire model. The method demonstrably isolates leakage to specific decision paths — e.g., path 14 in Morpho-MNIST shows leakage only in three out of fifteen paths (Table 3, Figure 5).

3. **Granular per-decision-path leakage inspection.** Table 3 and Figure 5 decompose the tree into individual decision paths and report task accuracy and information gain for each leaky split. For example, the concept "length:large" contributes 0.230 bits of leakage in path 14, and the corresponding sub-tree accuracy improves from 44% to 57%. This level of per-rule transparency is genuinely unique — no prior CBM training method provides per-path leakage attribution at this granularity.

4. **Quantitative validation that leakage decreases with concept completeness.** Figure 4 plots total information gain of MCBM-Seq on CUB across varying levels of concept completeness, showing monotonic decrease as more concepts become available. This provides the first direct, quantitative evidence for the intuition (raised by Havasi et al. 2022) that missing concepts drive leakage.

5. **Higher explanation accuracy on incomplete concept sets.** Table 1 shows that tree-based label predictors (including MCBM-Seq) achieve explanation accuracy of 90.1% (CUB) and 77.6% (MIMIC) with 100% fidelity, compared to Entropy-Net's 64.0% explanation accuracy and 73.2% fidelity on CUB. This demonstrates that when concept sets are incomplete, tree-based predictors produce more reliable explanations than logic-formula approaches.

6. **Architecture-agnostic concept predictor.** The method imposes no constraints on the concept encoder architecture (Section 4.1, Conclusion), which increases applicability compared to methods requiring custom training objectives or distributional assumptions (Marconato et al. 2022).

## Weaknesses

### Fatal
None.

### Major

1. **Unsubstantiated empirical claim: "less leakage than their soft counterparts."** The paper states at line 230: "Mixed CBMs achieve higher task accuracy than their respective hard CBMs and less leakage than their soft counterparts. This can be observed from the results of Table 2." However, Table 2 reports task accuracy and concept accuracy — not leakage values. No table or figure in the paper provides a direct empirical comparison of leakage magnitude between MCBM and a standard soft CBM with the same tree architecture. The claim about total leakage reduction is asserted without supporting evidence. This is an evidential gap for a specific empirical claim; the paper should either remove the claim or provide the comparison. (Note: the method's ability to *spatially constrain* leakage to specific paths is a separate, architecturally supported claim and is not undermined by this.)

2. **Leakage analysis (Figure 4) is descriptive, not comparative.** Figure 4 shows that MCBM-Seq's measured total leakage decreases as concept completeness increases. This is a useful sanity check, but the curve is not compared to any baseline (e.g., the leakage of a standard soft CBM tree under the same concept completeness levels). Without a baseline, the reader cannot tell whether the trend is an artifact of the tree-based measurement or a genuine property of CBMs. The plot is descriptive rather than discriminative.

### Minor

3. **Entropy-Net comparison frames an inherent property as a unique advantage.** Table 1 shows that trees achieve 100% fidelity while Entropy-Net achieves lower fidelity on incomplete concept sets. The paper frames this (lines 228–229, Table 1 caption) as if the MCBM method provides more trustworthy explanations. However, 100% fidelity is an inherent property of any decision tree (the tree is its own model), not something MCBM contributes. The valid part of the comparison is that Entropy-Net's fidelity degrades on incomplete concept sets while tree fidelity does not — this is a useful observation about when each representation is preferable. The framing should be more careful to distinguish MCBM's novel contribution (leakage inspection) from the baseline property of all tree-based predictors (perfect fidelity).

4. **Design decision to restrict soft values to only concepts in the global path is not defended.** The method uses soft probabilities only for concepts \(K_m\) that already appear as splits in the global decision path (lines 85–87, 133–134), and hard values for all others. This means the sub-tree cannot detect leakage through soft signals in concepts that the global tree didn't use as splits. The paper acknowledges this implicitly in the Woodpecker example (the leaky concept "has-breast-pattern-solid" does appear in the global path), but does not discuss whether this design choice could miss important leakage from non-path concepts. An ablation comparing mixed sub-trees to fully-soft sub-trees would clarify the trade-off.

5. **Leakage approximation may overestimate true leakage.** Equation 5 approximates leakage as information gain in the sub-tree, but this is valid only if the global tree's splits have already conditioned on the hard concepts. If the global tree is suboptimal (e.g., due to the minimum-samples-per-leaf constraint), some information gain in the sub-tree could reflect splits the global tree missed for non-leakage reasons, overestimating true leakage. The paper does not discuss this potential bias.

6. **No statistical significance reported.** Tables 2 and 3 report single numbers without confidence intervals or standard deviations. Given that some accuracy differences are small (e.g., MCBM-Seq vs. Sequential CBM on CUB: 47.3% vs. 47.7%), it is unclear whether the reported improvements are meaningful or due to chance.

### Trivial
None.

## Nice-to-Haves

- **Ablation study:** Train sub-trees that use soft values for *all* concepts (not just \(K_m\)) and compare leakage and accuracy. This would clarify whether the restriction to \(K_m\) is important for spatial leakage control or unnecessarily limits the sub-tree's expressiveness.
- **Practical use-case demonstration:** The Woodpecker example (around line 259) illustrates what the method outputs, but does not demonstrate whether the per-path leakage information changes a user's decision or increases trust. A small human evaluation or case study with domain experts would strengthen the claim about real-world value, though this is not required for a methods paper.

## Removed Points

These points were flagged by reviewers but are removed with justification:

1. *The method's main claim about "controlling leakage" is not tested.* — Restated as Weakness #1 above but rephrased: the architectural claim (spatially constraining leakage) IS supported; the unsupported part is only the specific empirical claim "less leakage than soft counterparts."

2. *User study required to demonstrate practical benefit.* — Removed as scope creep. This is a methods paper, not a human-factors study. The demand for a user study exceeds standard evaluation norms for this type of contribution.

3. *Missing hyperparameter details (msl, calibration parameters).* — Removed. The paper references appendix sections (A.4, A.7, A.10) for these details. Per the instructions, the parser strips appendix content from all papers; penalizing the authors for missing appendix content that is present in the original submission is not appropriate.

4. *Missing related work on definitions of leakage.* — Removed. The paper does cite and distinguish its definition from Mahinpei et al. 2021 (line 57: "While information leakage is defined by Mahinpei et al. (2021) as... in this work we propose a more explicit definition"). The treatment is adequate.

## Novel Insights

Beyond the paper's own contributions, the reviews do surface one genuinely novel observation that the paper itself does not fully articulate: the mixed-concept design creates a **natural experiment-control pairing** within a single model. The hard tree is the control (leakage-free by construction), and the mixed sub-trees are the treatment (leakage allowed only on specific paths). This means every split in the global tree that does NOT get extended is an implicit negative result — evidence that no leakage was exploitable at that node. This internal control structure is a subtle but real design strength that makes the per-path analysis more informative than a global soft-vs-hard comparison would be, because it controls for the data distribution at each leaf. The paper mentions this only implicitly ("If a sub-tree is found…"; "The remaining leaf nodes are unaffected by leakage") and could usefully foreground this property.

## Suggestions

1. Either remove the unsupported claim "less leakage than their soft counterparts" (line 230) or provide a direct empirical comparison: for each leaf of the global tree, compare the information gain from MCBM sub-tree splits to the information gain from splits in the corresponding region of a standard soft CBM tree. This is the single most actionable fix.

2. Add a brief discussion (or ablation) defending the design choice to restrict soft values only to concepts in the global path. Even a paragraph acknowledging the trade-off and explaining why it is necessary for the leakage definition (as partially done in lines 87–88) would suffice.

3. Report confidence intervals or standard deviations for the main accuracy tables, or acknowledge the limitation of single-run reporting.

4. Frame the Entropy-Net comparison more precisely: the contribution is that MCBM adds leakage inspection *on top* of the existing benefits of tree-based predictors (which include perfect fidelity), not that MCBM itself achieves perfect fidelity.
