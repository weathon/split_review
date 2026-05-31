## Summary

This paper identifies and addresses the problem of "redundant transformations" in middle-to-deep layers of Transformer-based language models, where layer outputs exhibit either near-identity or near-irrelevant transformations. The authors propose a Coherence-based Redundancy (CR) measure using characteristic functions and Fourier transforms to quantify this redundancy, and introduce two mitigation schemes: tree-structured residual paths to improve cross-layer information flow, and a coherence-based redundancy loss with channel orthogonality regularization. Pre-training experiments on a Llama3-130M model demonstrate that these methods reduce redundancy and enable a 12-layer model to outperform a 14-layer baseline.

## Strengths

- **Novel perspective on representation collapse**: The paper provides a clear and well-motivated analysis of why middle-to-deep layers produce redundant transformations, attributing it to training paradigms that prioritize prediction accuracy over transformation effectiveness. This reframes the well-known representation collapse problem in a way that suggests actionable solutions rather than just pruning.

- **Principled redundancy metric**: The CR measure based on characteristic functions and frequency-domain coherence is theoretically grounded and addresses limitations of cosine similarity (which only captures directional information). The use of complex-valued frequency representations to capture higher-order statistical differences is a thoughtful design choice.

- **Practical and effective interventions**: The tree-structured residual path is simple to implement yet shows clear empirical benefits (reducing coherence values across layers). The combination of sequence-level CR loss and channel-level orthogonality loss provides complementary regularization from two dimensions.

- **Convincing empirical results**: The 12-layer model with the proposed methods achieves 0.45 lower perplexity than the 12-layer baseline and 0.1 lower than the 14-layer baseline, demonstrating that the approach genuinely improves parameter utilization without adding parameters.

## Weaknesses

### Major

- **Limited experimental scale and scope**: The experiments are conducted on a single 130M parameter model trained on only 11B tokens of The Pile. While the paper acknowledges this as a "small-scale language model" study, the claims about addressing issues in "large language models" and "current LLM training paradigms" are not well supported by experiments at this scale. The representation collapse phenomenon may behave differently in models with hundreds of billions of parameters and training data orders of magnitude larger.

- **Insufficient evaluation beyond perplexity**: The paper only reports perplexity as the evaluation metric. For a method that claims to improve "feature-learning efficiency" and "parameter utilization," downstream task evaluations (e.g., on standard benchmarks like GLUE, SuperGLUE, or commonsense reasoning tasks) would provide much stronger evidence that the reduced redundancy translates to better learned representations, not just lower perplexity.

- **Ablation study lacks clarity on individual component contributions**: While Figure 3 shows ablation experiments for CR loss hyperparameters, the paper does not clearly isolate the individual contributions of the tree-structured residual path, the CR loss, and the orthogonality loss. Figure 4 compares Base-12L, Base-14L, and BaseT-12L+CR+O, but never shows BaseT-12L alone or BaseT-12L+CR without orthogonality loss. This makes it difficult to assess which component drives the improvement.

### Minor

- **The tree-structured residual path design appears somewhat arbitrary**: The selection of which layers serve as leaf nodes (layers 2, 4 as children of layer 0; layers 6, 8 as children of layer 1) and which serve as buffer layers (3, 5, 7, 9) is described but not justified with experimental evidence. A more systematic exploration or theoretical justification would strengthen this design choice.

- **The CR loss target selection (0.35) is empirically determined but not theoretically motivated**: While the ablation in Figure 3(b) shows 0.35 works best, the paper does not explain why this specific value is appropriate or how it might generalize to different model architectures or scales.

- **The orthogonality loss motivation could be stronger**: The paper states that along the channel dimension, "we prefer the features between any two channels to be orthogonal," but does not provide evidence that this is actually beneficial or that the baseline model suffers from inter-channel redundancy. The orthogonality loss is introduced without empirical motivation.

### Trivial

- The paper uses "coherence" in a non-standard way compared to signal processing literature, where coherence typically measures correlation between two signals at each frequency. The paper's use is consistent within its own framework but could cause confusion for readers familiar with the signal processing definition.

## Nice-to-Haves

- Experiments on at least one larger model scale (e.g., 350M or 1B parameters) would significantly strengthen the claims about generalizability to LLMs.
- Downstream task evaluations (e.g., on standard NLP benchmarks) would provide stronger evidence that the reduced redundancy improves task performance, not just perplexity.
- Analysis of whether the proposed methods affect training stability or convergence speed compared to baselines.

## Novel Insights

The paper's key insight is that representation collapse in deep Transformer layers can be understood as a training paradigm failure rather than an architectural limitation. By framing the problem as "redundant transformations" (either near-identity or near-irrelevant), the authors provide a more nuanced view than prior work that simply observes increasing feature similarity. The use of frequency-domain coherence to measure transformation effectiveness is a genuinely novel contribution that goes beyond standard cosine similarity metrics. The observation that shallow layers naturally produce more effective transformations (coherence in the [0.3, 0.7] range) and that this can be propagated to deeper layers via tree-structured residuals is practically insightful.

## Suggestions

1. Add downstream task evaluations (e.g., on standard benchmarks) to demonstrate that reduced redundancy translates to better task performance, not just lower perplexity.
2. Include ablation experiments that isolate the individual contributions of the tree-structured residual path, CR loss, and orthogonality loss (e.g., show BaseT-12L alone and BaseT-12L+CR without orthogonality).
3. Provide a more systematic justification for the tree-structured residual path design, perhaps with an ablation comparing different tree configurations.
4. Discuss how the proposed methods might scale to larger models and whether the hyperparameters (e.g., CR loss target of 0.35) would need adjustment.

## Score and Decision

The paper presents a novel and well-motivated approach to a recognized problem in Transformer training, with a principled metric and practical interventions that show clear empirical benefits. However, the experimental validation is limited to a single small model (130M parameters) with only perplexity evaluation, which significantly weakens the claims about addressing issues in large language models. The paper would benefit substantially from larger-scale experiments and downstream task evaluations. Given these limitations, the paper is at the borderline of acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>