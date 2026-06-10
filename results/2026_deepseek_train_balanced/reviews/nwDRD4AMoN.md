## Summary

This paper introduces Artificial Kuramoto Oscillatory Neurons (AKOrN), a neural network building block where neurons are N-dimensional unit vectors evolving via generalized Kuramoto synchronization dynamics. The method is integrated into convolutional and self-attention architectures and evaluated across unsupervised object discovery, Sudoku reasoning, adversarial robustness, and calibration. The core novelty is using oscillator synchronization as a computational primitive in deep learning, and the paper reports competitive results across diverse tasks.

## Strengths

- **First distributed-representation model competitive with slot-based methods on CLEVRTex**: AKOrN achieves FG-ARI of 89.24 on CLEVRTex (Table 1, line 218), close to the best slot-based method ISA-TS (92.9) and well ahead of all other distributed models (I-SA: 78.96). This is a genuine milestone — prior to this work, slot-based methods dominated complex object discovery. The paper shows that continuous oscillatory representations can close that gap.

- **Excellent calibration without specialized training**: AKOrN achieves ECE of 1.3–1.4% on CIFAR-10 common corruptions (Table 2, lines 400–401), versus 4.8% for the best robust benchmark baseline and 8.9–9.6% for standard ViT/ResNet-18. The paper demonstrates a nearly linear confidence-accuracy relationship (line 416), which is unusual for discriminative classifiers and is backed by quantitative comparisons.

- **Energy-based voting mechanism for Sudoku**: The paper shows that the Lyapunov energy (Eq. 6) correlates with solution correctness (Section 4.2, lines 329-332), enabling a principled multi-sample selection strategy that outperforms majority voting. This is a creative and well-demonstrated use of the dynamical structure, and the observation that energy serves as a self-evaluation signal is interesting.

- **Test-time compute-accuracy scaling**: AKOrN's OOD Sudoku performance improves from ~17% to ~52% with more Kuramoto steps (Fig. 3c, line 327), while standard self-attention saturates. This scaling behavior is a natural consequence of the continuous-time dynamics and is qualitatively different from feedforward architectures.

- **Novel integration of Kuramoto dynamics into deep learning**: The generalization of the Kuramoto model to N-dimensional vector oscillators with a symmetry-breaking field C and integration into convolutional/attention layers is technically sound and non-trivial, opening a new direction for dynamical neural computation.

## Weaknesses

### Major

- **Asymmetric Sudoku comparison undermines the headline claims**: AKOrN's Sudoku results (100.0% ID, 61.1% OOD) are obtained with `T_eval=128` (8× the 16 training steps) and energy-based voting over 100 random initializations of oscillators (Table 3 caption, lines 364-366). The comparison baselines (R-Transformer, IRED, Transformer, ItrSA) are evaluated with their standard inference procedures. The paper does not explore what baselines would achieve with comparable test-time compute or ensembling. The claim "on par with IRED" (61.1% vs 62.1%) is misleading because IRED achieves 62.1% *without* test-time step extension or multi-sample voting, while AKOrN requires extensive test-time investment to match it. Meanwhile, the ItrSA baseline achieves only 34.4% with 16 steps — what would it achieve with 128 steps? This asymmetry should be controlled for or explicitly framed as a compute-performance tradeoff rather than a direct accuracy comparison.

### Minor

- **Adversarial robustness evaluation is incomplete for the strength of the claims**: The paper reports 58.91% adversarial accuracy under AutoAttack with EoT (Table 2) and claims the model is "robust by design" (line 377). However, only one attack configuration is reported. The evaluation does not include transfer attacks from standard models or adaptive attacks designed for the specific architecture, which would be needed to fully substantiate the "robust by design" claim. (Note: the harsh critic's claim that EoT usage itself indicates gradient obfuscation is factually incorrect — Athalye et al. 2018 introduced EoT precisely to *defeat* obfuscation. The use of EoT is standard rigorous practice. The concern here is simply that more attack types would strengthen the claim.)

- **Missing ablation description in text**: Figure 6 (line 381) caption says "Green bars show accuracy when we ablate each element of \method" for the random noise experiment, but the text does not describe what elements are ablated, how they are removed, or provide the numerical values. While the ItrSA/ItrConv baselines do isolate the effect of the full AKOrN system versus iterative processing, a proper component ablation in the text would strengthen attribution.

- **Key experimental details not stated in main text**: The number of Kuramoto steps T for the object discovery and robustness experiments is not reported (only stated for Sudoku: T=16 at line 318). The oscillator dimension N per experiment is also not clearly stated for all setups. If these appear in the supplementary material (which was stripped by the parser), they should be referenced in the main text.

### Trivial

None.

## Nice-to-Haves

- Reporting transfer attacks (from standard models like ResNet-18) for the adversarial robustness evaluation
- Extending Sudoku baselines with comparable test-time compute (more iterations or ensembling) to show a principled compute-performance tradeoff rather than an asymmetric comparison
- A full component-level ablation (sphere constraint, Ω rotation, readout module, symmetry-breaking field) to isolate the contribution of each AKOrN element
- Reporting parameter counts for all model configurations, and computational cost (runtime or FLOPs) comparisons

## Removed Points

- **Gradient obfuscation claim about EoT**: The harsh critic claimed EoT is a "known indicator of potential gradient obfuscation." This is factually incorrect — Athalye et al. (2018) introduced EoT as a technique to *overcome* gradient obfuscation, making attacks work despite stochastic/dynamic computation. Using EoT in evaluation demonstrates rigorous practice, not a red flag. This criticism is removed.
- **Missing hyperparameters (optimizer, learning rate, weight decay, etc.)**: These would typically appear in the supplementary material, which was stripped by the parser. Per filtering rules, criticisms about missing appendix content are removed. The specific missing details about T and N are retained as a Minor weakness because they are fundamental architectural parameters that should be stated in the main experimental setup.
- **"Cannot be independently verified" / reproducibility concerns about cited entities**: Removed per filtering rules — all cited models, benchmarks, and datasets are assumed to exist as cited.
- **Strength Finder's generic or conflicting strengths**: All retained strengths are concrete and evidenced; none were removed.

## Novel Insights

The most interesting observation emerging from the reviews is a tension that neither reviewer fully resolves: the paper's evidence spans an unusually broad set of tasks (object discovery, reasoning, robustness, calibration), but the breadth comes at the cost of depth in each individual evaluation. The object discovery results on PascalVOC (52.0/60.3) are genuinely impressive for a non-slot-based method, yet the calibration results (ECE 1.3%) are arguably even more striking and less well-explained. The speculation that the energy "roughly approximates the likelihood" (line 417) is hand-wavy and unsupported. The paper would benefit from selecting one or two tasks for rigorous defense (with proper ablations and controlled comparisons) rather than spreading evidence thin across four tasks, each with some evaluation gaps.

## Suggestions

1. **For Sudoku**: Either (a) report AKOrN results with T=16 and no voting for a fair comparison against baselines, then show the energy-voting and test-time scaling as a separate contribution with appropriate caveats, or (b) extend baselines with comparable test-time compute to demonstrate a principled tradeoff.
2. **For robustness**: Add transfer attacks from a standard model (e.g., ResNet-18) and report results under a stronger adaptive attack without EoT to address the gradient obfuscation concern that the community will reasonably raise.
3. **Add a component ablation to the paper text**: Isolate the sphere constraint, Ω rotation term, readout module, and the symmetry-breaking field C to show what each contributes. This is essential for attributing gains to the Kuramoto dynamics specifically.
4. **Report T and N explicitly**: State the number of Kuramoto steps and oscillator dimension for every experimental setup in the main experimental sections.

**MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>**