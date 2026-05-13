# Learning Equivariant Non-Local Electron Density Functionals

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
The accuracy of density functional theory hinges on the approximation of \emph{non-local} contributions to the exchange-correlation (XC) functional.
To date, machine-learned and human-designed approximations suffer from insufficient accuracy, limited scalability, or dependence on costly reference data.
To address these issues, we introduce \ourlong{} (\our{}), a novel non-local XC functional based on equivariant graph neural networks.
\our{} combines semi-local functionals with a non-local feature density parametrized by an equivariant nuclei-centered point cloud representation of the electron density to capture long-range interactions. 
By differentiating through a self-consistent field solver, we train \our{} requiring only energy targets.
In our empirical evaluation, we find \our{} to accurately reconstruct `gold-standard' CCSD(T) energies on MD17.
On out-of-distribution conformations of 3BPA, \our{} reduces the relative MAE by \SI{35}{\percent} to \SI{50}{\percent}.
Remarkably, \our{} excels in data efficiency and molecular size extrapolation on QM9, matching force fields trained on 5 times more and larger molecules.
On identical training sets, \our{} yields on average \SI{51}{\percent} lower MAEs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes to learn weighting coefficients for every point in 3D space to re-weight meta-GGA functional.

### Strengths
- The proposed method is basis-independent.
- The method shows good results on structural extrapolation and data efficiency.

### Weaknesses
 - Since the proposed method requires computing DFT, comparing it to ML force field might not be fair due to the higher computational cost.

- The proposed ML functional still rely on the existing functional, i.e.,  meta-GGA.

### Questions
- The results on MD17 (Table 1) and QM9 (Figure 3) seem to be good but with mixed results. How to understand these difference in accuracy?

- How is non-local defined? Will the re-weighting also make density gradients non local?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Global Graph Exchange Correlation (GG-XC) functional, an innovative approach leveraging equivariant graph neural networks (GNNs) to model non-local exchange-correlation (XC) contributions in density functional theory (DFT). GG-XC addresses limitations in scalability, accuracy, and data dependency faced by previous ML-based and human-designed approximations. Through a combination of semi-local functionals and non-local density features, GG-XC captures long-range interactions and is trained using only energy targets by differentiating through a self-consistent field (SCF) solver. The empirical results demonstrate GG-XC's ability to achieve competitive accuracy with significantly reduced data requirements, even in out-of-distribution scenarios.

### Strengths
- Originality: GG-XC offers a novel methodology by integrating GNNs with DFT, particularly beneficial for non-local XC functional design. This approach advances ML-based DFT by capturing long-range interactions through an equivariant point cloud representation of electron density.

- Quality: The paper presents rigorous empirical evaluation across datasets (e.g., MD17, QM9, 3BPA), clearly showcasing GG-XC's data efficiency and accuracy. The use of CCSD(T) energies as a baseline adds to the robustness of the study.

- Clarity: The structural breakdown of GG-XC into nuclei-centered embeddings, equivariant message passing, non-local reweighting, and graph readout is well-organized. However, clearer explanations regarding specific design choices, such as graph readout and the integration of the SCF process, would strengthen accessibility for readers outside the immediate field.

- Significance: By bridging ML force fields and DFT, GG-XC has potential implications for more accurate and scalable quantum mechanical computations. The work promises improvements in data efficiency and applicability to larger molecules, essential for fields like materials science and drug discovery.

### Weaknesses
 - Ambiguity in Methodological Details: Key details around the learning objectives and loss functions are unclear. For instance, it is inferred that GG-XC utilizes CCSD(T)-derived energy and density for training, but an explicit statement on this is missing. Additionally, the training schemes ˙such as backpropagating through functional derivatives) need to be explicitly written. Please clarify the optimization procedure and loss function explicitly.

- Design Choices in Non-Local Reweighting: The inclusion of the graph readout term and the reasoning behind the design choice to learn meta-GGA coefficients in GG-XC lacks sufficient justification. The authors suggest that the graph readout captures remaining non-local effects but do not clearly explain why the non-local terms in the preceding convolution is insufficient. Furthermore, the specific form of the meta-GGA coefficients and how they are integrated into the overall functional is not clearly defined, making it difficult to assess their impact.

- Insufficient SCF Explanation: The SCF procedure, particularly the calculation of the exchange-correlation functional's differential form with respect to density, is inadequately detailed. Especially, the calculation of Fock operator is absent in the manuscript. A deeper explanation of the differentiation through the graph readout term, specifically how it integrates into the SCF iterations, is necessary. The manuscript lacks a clear description of how the gradients of the graph network are incorporated into the Fock matrix construction and how this affects the convergence of the SCF procedure.

- Computational Cost and Efficiency: The paper omits a thorough computational cost analysis. An assessment of GG-XC’s runtime compared to standard mGGA or hybrid methods would clarify the efficiency benefits. Additional experiments comparing GG-XC with conventional mGGA and hybrid methods regarding speed and computational bottlenecks would significantly improve the work. This reviewer's recommendation are the mGGA functional $\epsilon_{\text{mGGA}}$ used in the GG-XC and $\omega B97X$ functional as in the 3BPA dataset.

- Comparative Baselines: While delta-machine learning methods are included in the comparison, the paper contrasts GG-XC trained on higher-level mGGA data with models trained on lower-level LDA for delta learning. This might obscure performance differences, as delta-learning methods trained on comparable baseline data (mGGA) could offer a more direct comparison. As mentioned in the previous point, please use the mGGA functional for the baseline models.

### Questions
- Contribution Clarification: Could the authors explicitly clarify GG-XC’s unique methodological contributions? For readers less familiar with recent advances in this field, a succinct outline of GG-XC’s innovative aspects compared to prior methods would enhance clarity.

- Learning Objective and Loss Function: How is the GG-XC's loss function specifically defined? If CCSD(T) energy and density are indeed the targets, please confirm this assumption and clarify how functional derivatives are computed efficiently.

- Non-Local Reweighting Design Choice: What justifies the inclusion of the graph readout term when non-local terms are already introduced in the integral preceding it? Is there evidence that including the readout term substantively enhances performance?

- Differentiation Through SCF: Could the authors provide a more detailed explanation of the SCF process, particularly the derivation of the exchange-correlation functional’s differential form with respect to density? Furthermore, how is differentiation handled in the context of the graph readout term?

- Computational Efficiency Analysis: What is GG-XC’s relative computational cost compared to traditional mGGA and hybrid methods? An analysis of bottlenecks, particularly in terms of graph processing and SCF convergence, would be helpful for readers.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new model called Global Graph Exchange Correlation (GG-XC) to improve the accuracy of exchange-correlation (XC) functionals in density functional theory (DFT). Traditional methods for approximating XC functionals struggle with capturing long-range electron interactions, leading to errors in DFT calculations. GG-XC addresses this by using graph neural networks (GNNs) to create a nuclei-centered representation of the electron density that captures long-range interactions. The approach leverages machine learning (ML) to reduce computational costs and improve data efficiency while maintaining accuracy on various energy prediction benchmarks.

### Strengths
1. GG-XC significantly reduces errors in DFT calculations, achieving state-of-the-art performance on energy benchmarks.
2. The method is highly data-efficient, achieving excellent results with much less training data.
3. It demonstrates robust extrapolation capabilities, performing well even on out-of-distribution and larger molecular structures.

### Weaknesses
1. In comparison, the force field paper prioritizes force accuracy, critical for molecular dynamics simulations, while the learned XC functional paper focuses on density accuracy, which is essential for practical DFT applications. However, the authors of the equivariant model rely only on energy metrics for evaluation, potentially leading to an incomplete comparison between the works. Despite the accessibility of force calculations via differential techniques, the equivariant model omits these, which are crucial for molecular dynamics. Additionally, density, a foundational component in DFT that governs electron distribution and influences properties such as dipole moments and band gaps, is not evaluated in the equivariant model.
2. The lack of tests on intermolecular non-covalent interactions and chemical reactions is a considerable gap. The differentiable programming approach demonstrates generalizability by successfully benchmarking against intermolecular non-covalent interaction datasets and different chemical reactions. Expanding the equivariant model's validation to include these would indicate broader reliability.
3. The lack of explicit enforcement of physical constraints may limit the accuracy in certain edge cases. Specifically, without constraints such as the uniform electron gas limit or the Lieb-Oxford bound, the model's behavior in extreme density regimes is uncertain. This could lead to unphysical results in scenarios involving highly compressed or rarefied electron densities.
4. The model’s reliance on nuclei-based embeddings may make it less suitable for non-atomic systems. This approach might struggle with systems where the electronic structure is not primarily determined by atomic nuclei, such as in extended solids or systems with significant electron delocalization.

### Questions
1. Given the accessibility of force calculations through differential techniques, why were these not included in the model’s experiments, could this learned energy functional be used for MD simulations or geometry optimizations?
2. Considering the fundamental role of electron density in DFT, could the model be evaluated for density accuracy and density-derived properties to ensure broader alignment with core DFT objectives?
3. Has the model been assessed for generalizability on intermolecule non-covalent interactions and diverse chemical reactions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The introduction of the Global Graph Exchange Correlation functional is innovative, utilizing equivariant graph neural networks to model non-local contributions to the exchange-correlation functional. This approach is relatively uncommon in traditional density functional theory, showcasing the potential of integrating machine learning with quantum chemistry.

### Strengths
By combining semi-local functionals with a non-local feature density, GG-XC significantly improves the capture of long-range interactions. Its impressive performance in reconstructing 'gold-standard' CCSD(T) energies highlights its effectiveness in enhancing computational accuracy.

### Weaknesses
The article offers a limited background overview and would benefit from a more thorough discussion of certain concepts. For instance, the section on 'non-local functionals' lacks detail and should clarify their significance in density functional theory. 

Furthermore, the claim that 'the equivariant GNN efficiently captures long-range information' is somewhat misleading, as many equivariant graph neural networks (EGNNs) are designed with the assumption that inter-atomic interactions are localized. The underlying message-passing scheme typically aggregates information only from atoms within a cutoff radius, which raises questions about their ability to effectively model long-range interactions.

Finally, a comparison of the computational complexity of different methods is necessary.

### Questions
1. The claim that 'the equivariant GNN efficiently captures long-range information' is somewhat misleading, as many equivariant graph neural networks (EGNNs) are designed with the assumption that inter-atomic interactions are localized. The underlying message-passing scheme typically aggregates information only from atoms within a cutoff radius, which raises questions about their ability to effectively model long-range interactions.

2. Finally, a comparison of the computational complexity of different methods is necessary.

### Soundness
4

### Presentation
3

### Contribution
3
