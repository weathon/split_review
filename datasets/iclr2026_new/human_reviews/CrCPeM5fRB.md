## Human Reviewer 1

### Summary
This paper introduces the Signal Dice Similarity Coefficient (SDSC), a structure-aware metric for time-series self-supervised learning. SDSC extends the Dice–Sørensen coefficient, widely used in image segmentation, to signed continuous signals by (1) gating overlaps with a (smoothed) Heaviside on sign agreement between prediction and target, and (2) accumulating pointwise intersections via a $\min(\|E\|,\|R\|)$ operation normalized to $[0,1]$. The paper further proposes a hybrid loss that combines SDSC with MSE, weighted by uncertainty-based coefficients, and evaluates both as reconstruction objectives within a SimMTM pretraining framework.

### Strengths
- **Conceptual originality:**: Extending Dice coefficient to continuous, signed time-series is intuitive yet non-trivial. The proposed formulation yields a bounded, symmetric, and interpretable metric within the range $[0,1]$.
- **Design rationale**: Using $\min(\|E\|,\|R\|)$ with a Heaviside gating directly targets polarity issues and reduces pure amplitude bias, which are key limitations of conventional MSE/MAE.
- **Efficiency and simplicity**: SDSC avoids explicit temporal alignment or complex dynamic programming, making it lightweight and easy to implement compared to SoftDTW or DILATE.
- **Hybrid loss formulation**: The uncertainty-weighted combination of SDSC and MSE provides a balanced approach that couples structure-awareness with amplitude precision.

### Weaknesses
1. **Narrow definition of "structure"**: SDSC captures only pointwise magnitude overlap under sign gating, overlooking broader structural properties such as local waveform shape and phase alignment. Consequently, it lacks time-shift/warping tolerance—small temporal lags can significantly reduce the score, contradicting the intended “structure-aware” characterization.
2. **Offset bias**: When both signals share the same polarity or a strong DC offset, $H(E\cdot R)\approx1$ holds broadly, leading to inflated similarity even when shapes differ.
3. **Zero-crossing noise and stability**: Around near-zero amplitudes, the Heaviside gating becomes highly noise-sensitive, causing unstable or vanishing gradients. Although the authors acknowledge gradient vanishing and describe it as robustness, this more likely indicates blindness to misalignment rather than genuine robustness.
4. **Evaluation mismatch**: If MSE is said to fail at capturing structure, the evaluation should include structure-aware metrics such as Pearson correlation, spectral coherence, or STFT/Mel-cosine similarity. Relying solely on MSE/MAE weakens the empirical claim of structural fidelity.
5. **Limited baselines**: The work omits direct comparisons with established structure-aware objectives. Simply stating these are "computationally heavy" is insufficient. An explicit time-vs-accuracy trade-off or short-sequence comparison would strengthen the argument.
6. **Gradient analysis limitations**: Reporting only gradient norms does not characterize optimization behavior. The analysis should also consider gradient direction alignment, variance, or loss-landscape smoothness to assess stability.

### Questions
1. Could the authors include experiments with timing shifts or mild time warping, and compare SDSC against MSE, SoftDTW, and DILATE?
2. Beyond pointwise overlap, could you report additional structure-sensitive metrics to substantiate the "structure-aware" claim both at pretraining and downstream evaluation stages?
3. Have you explored mean-removal preprocessing or frequency-domain SDSC to mitigate offset bias?
4. Could you provide a practical guideline summarizing when SDSC, MSE, or the hybrid loss is preferred (i.e., amplitude-critical vs. structure-critical regimes)?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces the Signal Dice Similarity Coefficient (SDSC), a structure-aware metric for time series self-supervised representation learning that addresses limitations of distance-based objectives like MSE.  SDSC extends the Dice Similarity Coefficient from image segmentation to continuous temporal signals by quantifying structural agreement through signed amplitude intersections.

### Strengths
1. The paper is relatively simple and easy to understand.

2. Experiments span multiple tasks (forecasting, in-domain classification, cross-domain classification), settings (frozen encoders, fine-tuning), and datasets, demonstrating broad applicability and providing nuanced insights into when each approach works best.

3. The paper acknowledges that SDSC models achieve higher structural alignment at the cost of increased MSE, and that dataset characteristics influence which approach works better, showing intellectual honesty.

### Weaknesses
1.  The paper uses only SimMTM as the backbone "for architectural simplicity," which severely limits generalizability claims. Without validation on diverse architectures (Transformers, CNNs, RNNs, recent foundation models), it's unclear if SDSC benefits are architecture-specific or truly general.

2. The paper only compares against MSE, PCC, and SI-SNR. Recent structure-aware losses for time series (e.g., shape-based losses, spectral losses, contrastive losses) are not included, making it difficult to assess whether SDSC represents state-of-the-art for structure-aware objectives.

3. Despite strong motivation, the actual improvements are modest: hybrid loss achieves 0.4783 vs. 0.4852 MSE in forecasting (1.4% improvement), and Table 6 shows MSE sometimes outperforms SDSC in fine-tuning scenarios. The gains don't match the strength of the conceptual contribution.

4.  Computing SDSC requires element-wise min operations, Heaviside evaluations, and additional summations compared to MSE. No analysis of training time overhead or memory consumption is provided, which is critical for practical adoption.

### Questions
1. There seems to be an incorrect line break at the title.

2. Why does SDSC underperform MSE in cross-domain settings (Tables 5, 6)? If SDSC provides better "semantic representations," shouldn't it generalize better across domains? What explains this contradiction?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes the Signal Dice Similarity Coefficient (SDSC), a novel, structure-aware metric for self-supervised learning (SSL) of time-series representations. Existing methods such as MSE is overly sensitive to signal amplitude and scale, while being insensitive to waveform structure, phase, and polarity. DTW and other metrics are also having their weakness. To overcome teh limitations, SDSC is adapted from the Dice Similarity Coefficient (DSC), a metric widely used for overlap in image segmentation. SDSC compares two signals at each time step. It calculates a score based on the minimum amplitude of the two signals, but only if both signals have the same sign (e.g., both are positive or both are negative). If the signs are different, that time step is heavily penalized (it contributes zero to the similarity score).Properties: This approach makes SDSC robust to amplitude scaling while being highly sensitive to polarity mismatches. The resulting metric is bounded between [0, 1] (making it interpretable) and is computationally efficient (linear $O(T)$ complexity), unlike other alignment-based metrics (like SoftDTW, which is $O(T^2)$). The author also uses a smooth sigmoid approximation to make the function differentiable. In experiments, they also propose to combines MSE and SDSC, to capture both structural and amplitude information.Experiments on forecasting and classification tasks show that pre-training with SDSC or the hybrid loss is competitive or superior to models pre-trained with MSE.

### Strengths
1. The proposed method is efficient, linear time complexity, much better than other methods like DTW, which performs similar structure-awareness measurement.
2. The metric is bounded from 0 to 1, which provides better interpretability.
3. The paper is clean written, with illustrative examples to show numbers using different metric, under different structure changes.

### Weaknesses
1. No clear definition of "structure", still related to alignment or warping.
2. The backbone model is not widely tested. With more powerful models, we don't know if the advantage of SDSC still exists.
3. The imrpovement on various tasks, are very marginal. For example, in the fine-tuned classification task, the SDSC approach is not showing better results in either in-domain or out-domain experiments.

### Questions
If switching to other transformer-based backbone model, would the proposed method performs consistenly better?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper addresses the limitations of conventional distance-based metrics (e.g., MSE) in time-series SSL by introducing a novel structure-aware metric, the Signal Dice Similarity Coefficient (SDSC). The method reframes the signal reconstruction problem as measuring the overlap of the areas under the respective curves. Through the introduction of a signed amplitude intersection term, it ensures that overlap is computed only when signal polarities align, thereby effectively addressing the noted deficiency of MSE in being insensitive to phase inversions.

### Strengths
1.	Adapting the DSC from the segmentation domain to time-series signals is a novel perspective. Using the signed amplitude intersection as a proxy for waveform structure similarity is an interesting idea.
2.	The O(T) linear complexity of SDSC is computationally efficient, which is a practical advantage.
3.	The mathematical definition is intuitive, and the experimental design is well-structured.

### Weaknesses
1.	A motivation for the paper is that SDSC serves as a lightweight alternative to O(T^2) metrics (e.g., SoftDTW, DILATE). However, a direct comparison against them is missing. Currently, we only know that SDSC is faster, but we do not know how much performance is lost (or gained) compared to SoftDTW.
2.	The α parameter in the Sigmoid function significantly influences the gradient shape. The paper lacks a sensitivity analysis on how α affects the performance of downstream tasks.
3.	The "alignment-free" description may be somewhat misleading. While SDSC does not perform explicit temporal warping like DTW, it does enforce strict temporal and polarity alignment through its point-wise comparison.

### Questions
I will reconsider my score during the rebuttal phase based on the authors' response to following issues.

1.	Could the authors include an experiment in the appendix that compares SDSC with SoftDTW (as a loss function) on a downstream task (e.g., forecasting), using at least one small-scale dataset?
2.	Regarding the hybrid loss in Equation (8), how is the uncertainty-based tuning strategy specifically implemented to determine the weights λsdsc and λmse? How does this adaptive strategy compare to using simple fixed weights (e.g., λsdsc = λmse = 0.5)?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3