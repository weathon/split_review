## Summary
XPro-Design presents an explainable AI-driven framework for protein engineering that uses Integrated Gradients to obtain residue-level attribution scores from melting temperature predictors, then uses these attributions to iteratively update a position-specific scoring matrix (PSSM) that biases an inverse folding model (ProteinMPNN or HyperMPNN) toward thermostable sequences. The framework achieves substantial improvements in predicted melting temperatures and folding free energies on two test proteins (CaLB and SOR), while maintaining structural fold integrity and sequence diversity.

## Strengths
- **The core idea is elegant and practically valuable**: using explainability attributions from a surrogate predictor to guide a generative model in a gradient-free, model-agnostic manner is a novel contribution to protein engineering. The framework does not require fine-tuning the generative model, which avoids catastrophic forgetting and makes it broadly applicable.
- **Comprehensive multi-faceted evaluation**: The paper evaluates designs across predicted melting temperature (using two predictors), structural integrity (Boltz-2, RMSD, PTM, pLDDT), thermodynamic stability (MM/GBSA ΔG, ΔΔG), packing entropies, and a thorough analysis of non-covalent interactions (hydrogen bonds, salt bridges, π-stacking, cation-π, disulfide bonds, hydrophobic contacts). This is far more thorough than typical protein design papers.
- **Strong quantitative improvements**: XPro-Design variants achieve predicted melting temperatures near 80°C (compared to ~50°C wild-type), near-universal stabilization in ΔΔG, and mean ΔG values substantially more favorable than all baselines. For example, 100% of XPro-Design(P) variants are stabilizing vs only 14% for ProteinMPNN.

## Weaknesses
### Major
- **No experimental validation**: While the computational validation is thorough, the paper lacks any wet-lab experimental validation of the designed variants. Predicted Tm increases of up to 90°C and 2x improvements over wild-type are extraordinary claims that require experimental confirmation. Given the mature state of protein structure prediction and stability prediction, a paper claiming such dramatic improvements needs at least one experimental demonstration (e.g., expression, purification, circular dichroism thermostability measurement) or a clear justification why experimental validation is not feasible for this venue.
- **MM/GBSA ΔΔG values are unphysically large**: The mean ΔΔG for XPro-Design(P) is -1426 kcal/mol, and individual values reach -2962 kcal/mol (Table 3). These values are astronomically large—typical stabilizing mutations in proteins produce ΔΔG values on the order of -1 to -5 kcal/mol. The range in Table 3 (from -2962 to +650 kcal/mol) suggests the MM/GBSA calculations are not reporting folding free energies but rather absolute interaction energies of the entire system that are not physically interpretable as stability changes. The authors acknowledge this in Section 2.4 ("should not be interpreted as absolute folding free energies"), but then in the results they explicitly claim "38% reduction in predicted ΔΔG" and "near-universal stabilization" using these numbers, which is misleading—these numbers are not ΔΔG in any physically meaningful sense.

### Minor
- **Limited to two target proteins**: The method is demonstrated on only two proteins (CaLB and SOR), with SOR serving primarily as a control. Testing on a diverse set of proteins with different sizes, folds, and stability profiles would strengthen claims of generalizability.
- **Prediction model reliance**: The framework depends on the quality of Tm predictors and their Integrated Gradients attributions. The paper shows cross-predictor consistency (TemBERTure and DeepSTABp), but does not analyze how sensitive the framework is to the choice or quality of the property predictor. If the predictor has systematic biases, those biases could be amplified through the iterative PSSM update.
- **Epistasis capture is asserted but not demonstrated**: The paper states that "context-dependent effects (epistasis) are captured naturally through batch-level averaging" (Section 2.3), but no direct evidence is provided that XPro-Design captures epistatic interactions. The pairwise IG formulation (Equation 4) is presented but stated to not be used in training. Without a comparison showing the method outperforms a linear-additive baseline, the claim about epistasis is unsupported.

### Trivial
- Figure 1 has redundant caption text describing the same flow multiple times.
- Some methods compared (ADFLIP, MapDIFF) do not support sampling temperature, which limits the fairness of direct comparison at identical settings.

## Nice-to-Haves
- An ablation study showing the value of each component: tempered initialization, annealing schedule, Integrated Gradients guidance, and the exponential rescaling (Equation 7).
- A comparison with a simpler baseline that uses random iterative mutation with the same predictor, to confirm that the attribution-guided component is adding value beyond iterative screening.
- An analysis of whether the designed sequences actually satisfy the ProteinMPNN autoregressive constraints (per-position log-probability of designed sequences under the base model).

## Novel Insights
The paper's key insight is that explainability methods (Integrated Gradients) can serve as a differentiable signal bridge between a black-box property predictor and a generative model, without modifying either model's weights. This is conceptually distinct from reinforcement learning (which requires reward engineering and can be sample-inefficient) and fine-tuning (which risks catastrophic forgetting). The use of a PSSM as a learnable bias matrix that is iteratively updated using attribution-weighted stability signals is a practical and interpretable way to navigate sequence space. The observation that stabilized variants achieve improved hydrogen bonding and electrostatic networks rather than simply increased hydrophobic burial is a genuinely useful finding for protein design practitioners.

## Suggestions
1. **Reframe or correct the ΔΔG numbers**: The MM/GBSA numbers should be explicitly labeled as "relative interaction energy differences (not folding free energies)" throughout the results, not just in the methods. The claim of "38% reduction in ΔΔG" should be removed or substantiated with a proper folding free energy calculation (e.g., using FoldX or Rosetta ΔΔG, or thermodynamic integration from MD).
2. **Add experimental validation**: Even a single experimental validation on one designed variant (expression yield, CD spectrum, Tm measurement) would dramatically increase the impact and credibility of the paper. Given the current results rely entirely on computational predictions, this is strongly recommended.
3. **Test on more diverse proteins**: Add at least 2-3 more test cases (e.g., a small protein, a multi-domain protein, a membrane protein if feasible) to demonstrate generalizability.
4. **Analyze predictor sensitivity**: Include an analysis of how the framework performs with the Tm predictor replaced by a different architecture or with deliberately degraded predictors, to assess robustness.

## Score and Decision

The paper presents a valuable, novel framework with thorough computational evaluation and strong quantitative results. However, the lack of experimental validation for claims of such magnitude, combined with the use of unphysically interpreted ΔΔG values, prevents acceptance at this stage. The core methodology is sound and likely publishable after either experimental validation or correction of the stability analysis.

MY FINAL SCORE: 5score</score>
MY FINAL DECISION: Reject</decision>