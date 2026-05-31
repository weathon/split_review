## Summary
XPro-Design presents an explainable AI-driven framework for protein engineering that integrates Integrated Gradients-based attribution maps with inverse folding models (ProteinMPNN/HyperMPNN) to optimize protein thermostability. The method uses a learned position-specific scoring matrix (PSSM) to bias sequence generation toward high-stability regions while preserving structural integrity, achieving predicted melting temperature increases of up to 90°C and near-universal stabilization in folding free energy calculations for the tested proteins (CaLB and SOR).

## Strengths
- **Novel integration of explainability into generative protein design**: The use of Integrated Gradients to provide residue-level attribution signals that directly guide the optimization process is a genuinely novel contribution that addresses the "black box" nature of most protein design methods.
- **Comprehensive multi-faceted validation**: The paper evaluates designs across multiple dimensions (predicted Tm, folding free energy, structure prediction, packing entropy, inter-residue interactions, sequence diversity), providing a thorough characterization of the designed variants.
- **Strong empirical results**: XPro-Design variants consistently outperform all baselines (ProteinMPNN, HyperMPNN, ADFLIP, MapDIFF, PiFold) across nearly all metrics, with particularly striking improvements in ΔΔG (mean -1426 kcal/mol vs baselines that are often destabilizing).
- **Gradient-free optimization preserving model weights**: The approach avoids fine-tuning the underlying generative model, preventing catastrophic forgetting and maintaining structural fidelity—a practical advantage for real-world deployment.

## Weaknesses

### Fatal
None.

### Major
- **No experimental validation**: The paper relies entirely on computational predictions (predicted Tm, predicted structures, MM/GBSA calculations) without any wet-lab experimental validation. While computational benchmarks are valuable, claims of "nearly 2x melting temperature" and "38% lower folding free energy" require experimental confirmation, especially given that the Tm predictors themselves may not generalize well to heavily mutated sequences far from the training distribution.
- **Potential circularity in evaluation**: The same type of models used for guidance (TemBERTure for Tm prediction) are also used for evaluation. While DeepSTABp provides some independent verification, both are neural network predictors trained on similar data distributions. The strong correlation between guidance signal and evaluation metric raises concerns about whether the method is genuinely discovering stabilizing mutations or simply exploiting systematic biases in the predictors.
- **Missing ablation studies**: The paper does not isolate the contribution of individual components (tempering, annealing, IG-based updates, exponential scaling of ΔTm). Without ablations, it is unclear which design choices are critical to the reported performance.

### Minor
- **Limited protein targets**: Only two proteins (CaLB and SOR) are tested, with SOR serving primarily as a control. Generalizability claims would be strengthened by demonstrating the framework on additional targets with different structural classes and stability profiles.
- **The ΔΔG values appear implausibly large**: Mean ΔΔG of -1426 kcal/mol for a single-domain protein is orders of magnitude larger than typical stabilizing mutations (usually 1-5 kcal/mol). While the authors note these are MM/GBSA energies, not absolute folding free energies, the scale of the reported values warrants clearer explanation and contextualization.
- **Missing details on computational cost**: The iterative optimization process (sampling → prediction → attribution → update) could be computationally expensive, but no runtime or resource analysis is provided.

### Trivial
- The figure caption in the paper is repeated verbatim in the figure description, creating redundancy.

## Nice-to-Haves
- Experimental validation on at least one designed variant (e.g., expression, purification, CD spectroscopy, activity assay)
- Ablation studies removing tempering, annealing, or IG-based updates to quantify each component's contribution
- Application to a multi-objective optimization scenario (e.g., simultaneously optimizing stability and activity)
- Analysis of whether the designed sequences are actually expressible and foldable in practice

## Novel Insights
The paper's key insight is that attribution methods from explainable AI can serve as a bridge between predictive models and generative models in protein design, enabling gradient-free optimization that respects structural constraints. The observation that XPro-Design variants achieve stability through redistributed non-covalent interaction networks (more hydrogen bonds, salt bridges, π-interactions) rather than simply maximizing hydrophobic burial provides a mechanistic understanding that could inform future design strategies. The framework's ability to systematically explore sequence space far from mesophilic distributions while maintaining foldability demonstrates that current inverse folding models have latent capacity to generate thermophilic-like sequences that is not accessed by standard sampling.

## Suggestions
- Add at least one wet-lab experiment (expression and Tm measurement) for the top 3-5 designed variants to validate the computational predictions
- Include ablation studies removing the IG attribution component, the tempering step, and the exponential scaling to isolate their contributions
- Provide a clearer explanation of why MM/GBSA ΔΔG values are so large and how they should be interpreted relative to experimental folding free energies
- Test the framework on additional protein targets (e.g., a mesophilic enzyme, a therapeutic antibody) to demonstrate generalizability

## Score and Decision
The paper presents a novel and well-executed computational framework with strong empirical results across multiple metrics. However, the complete absence of experimental validation and potential circularity in evaluation prevent it from being a definitive contribution at this stage. The work is valuable for the community as a computational methodology paper.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>