# Geometric Spatiotemporal Transformer to Simulate Long-Term Physical Dynamics

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Physical dynamics simulation plays a crucial role in various real-world applications. In this paper, we explore the potential of leveraging Transformers by framing the task as autoregressive next-graph prediction based on spatiotemporal graph inputs. To achieve this, we propose Geometric Spatiotemporal Transformers (GSTs), which adopt the expressive encoder-decoder architecture of traditional Transformers. At the core of GSTs are equivariant spatiotemporal blocks that alternate between spatial and temporal modules while preserving E(3) symmetries. Additionally, we introduce the Temporal Difference Graph (TDG), derived from the difference between the last two frames of historical input, to capture global dynamic patterns and mitigate cumulative errors in long-term prediction tasks. Unlike existing Graph Neural Network (GNN) methods, GSTs can process full input sequences of arbitrary lengths to effectively capture long-term context, and address cumulative errors over long-term rollouts thanks to the TDG mechanism. Our method achieves state-of-the-art  performance across multiple challenging physical systems at various scales (molecular-, protein-, and macro-level), demonstrating the robust dynamics simulation capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a Transformer-based approach Geometric Spatiotemporal Transformers for simulating long-term physical dynamics. To improve the handling of cumulative errors over extended time horizons, this paper frames the task as autoregressive next-graph prediction, integrating E3 equivariant spatiotemporal blocks, and a TDG. It is evaluated across various scales, including molecular, protein, and macro-level physical systems, showing improvements in long-term predictive accuracy over existing methods.

### Strengths
1. An Innovative Use of Transformers is presented. Integrating Transformer architectures with spatiotemporal graph structures and E(3) equivariance introduces a novel approach for handling long-term physical dynamics, marking a unique departure from traditional GNN-based methods.
2. TDG shows promise in addressing cumulative errors in long-rollout predictions in physical simulation tasks.
3. Experiments offer some insights into the contributions of individual components, including equivariance and TDG which helps evaluate the effectiveness of the architecture. The model’s performance is assessed across various physical systems at molecular, protein, and macro levels, demonstrating GST’s potential adaptability to different scales of physical dynamics.

### Weaknesses
1. The experiments should include at least one additional dataset to better demonstrate generalizability, especially to popular datasets where multi-frame prediction methods may underperform. This would strengthen the paper's claims of achieving SOTA performance.
2. Many of the reported improvements over existing models are marginal and are often limited to specific datasets or rollout lengths. The author should clearly frame these gains to avoid overstating the model’s broader applicability.
3. The architecture's complexity, with components like equivariant modules and TDG, presents a reproducibility challenge. Offering an easy-to-use module, similar to Transformers, could significantly improve accessibility and replicability for other researchers.

### Questions
1. Can the TDG framework be adapted or tuned for other symmetry types beyond E(3) when applied to different dynamic systems?
2. Could the authors provide a clear, modular implementation that enables easy usage and integration later?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a Geometric Spatiotemporal Transformer (GST) designed for long-term simulation of physical dynamics using Transformers in a novel spatiotemporal context. Key innovations include E(3)-equivariant spatiotemporal blocks and a Temporal Difference Graph (TDG) for cumulative error reduction. The model is evaluated across molecular, protein, and motion datasets, aiming to outperform existing GNN-based methods.

### Strengths
- This paper proposes a novel dynamical model that can handle spatiotemporal sequences of variable length.
- The authors provide theoretical proof and show comprehensive experimental comparisons.

### Weaknesses
 - In addition to EGNN, there are other newer equivariant graph neural network architectures. Why not use them or conduct comparative experiments? EGNN has been proven not to be truly equivariant.
- In the temporal module, an equivariant self-attention mechanism is used to model each node. Are these nodes shared parameters? If not, the question of how to deal with the non-constant number of nodes in the data set should be answered to reflect the applicability of the model.
- Where is causal attention strategy reflected, and how is it different from traditional attention mechanism?
- Transformer-based models normally have high time complexity. The authors should show the efficiency comparison with other methods.
- Predicting the differences instead of directly predicting the value of the next frame has long been used in methods such as GNS[1] and MGN[2]. Why not compare?
- The detailed architectural differences between GST-V and GST-F should be explained. GST can be extended to variable lengths based on attention, so why can't ESTAG?
- Why can $\boldsymbol{X}_{\delta}$ reduce the cumulative error in long-term predictions? This should only be a short-term bias term. What is the theoretical basis?

### Questions
Please address the questions in the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the Geometric Spatiotemporal Transformer (GST) for predicting physical dynamics in domains such as molecular and motion simulations. Unlike prior works that rely on GNNs, GST leverages the Transformer architecture to handle sequences of arbitrary length, allowing for more flexible long-term predictions. Experimental results show that GST outperforms previous methods, especially in mitigating cumulative errors over extended prediction horizons.

### Strengths
- Exploring the efficacy of Transformers over GNNs is an important and interesting research direction.
- The proposed adaptation of the Transformer for physical dynamics is well-motivated and appropriate.
- Experimental results effectively demonstrate the superiority of the proposed method.

### Weaknesses
 **Limited technical novelty**

The proposed architecture is a straightforward extension of prior work. The equivariant component builds on previous research in geometric deep learning, while the alternating spatio-temporal operations are well-explored in the Video Transformer domain, as seen in works like TimeSformer [1]. In this context, the paper essentially replaces spatial self-attention with an equivariant MPNN.

[1] Bertasius et al. Is Space-Time Attention All You Need for Video Understanding? ICML 2021.

---
**Effectiveness in long-term rediction**

The Temporal Difference Graph (TDG) partially mitigates error accumulation in long-sequence predictions, similar to common tricks such as using advantage functions to improve over value functions. However, this approach does not fundamentally address the long-sequence issue, as the accumulation of temporal differences also grows over time.

The experimental results do not convincingly demonstrate GST’s specific advantage for long-sequence predictions. In Table 2, GST consistently outperforms prior methods across all horizons but does not exhibit a marked improvement at longer horizons. To substantiate the claim of efficacy on long sequences, the paper should provide evidence of stable performance over extended horizons, while prior methods should show significant performance degradation in these cases.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes multiple components aimed at improving modeling temporal physics simulations with particular focus on long-horizon rollout performance. At the core of the paper is the Temporal Difference Graph (TDG) which aims to mitigate error accumulation during the rollout by using a history of previous frames together with predicting the delta to the next frame instead of the next frame directly. This is combined with equivariant spatiotemporal transformer blocks as core building block. The proposed method shows improvements over state-of-the-art in small-scale molecular dynamics, motion capture and protein dynamics.

### Strengths
- Predicting the delta to the next timeframe is a compelling strategy to mitigate error accumulation. This strategy is also commonly used in diffusion models and the paper shows that this strategy also works well on physical simulation rollouts.
- Using transformers instead of GNNs makes a lot of sense as their scalability is well established and their flexibility (e.g. like using the TDG to incorporate arbitrary many history timesteps) is desireable
- The method shows strong improvements over competitors.
- Clear mathematical and visual description of the method.

### Weaknesses
 - The paper lacks runtime/flops and parameter count comparisons. Even though the architecture and training procedure can be quite different between methods, a comparison of parameter counts and runtimes is essential to exclude performance gains simply due to investing more compute/parameters into the model/training. 
- Processing the history (especially in the GST-V) could become quite costly, so the runtime necessary for a rollout should be reported.
- The considered models are extremely small (hidden dim 16 with 2 layers according to the Appendix). This limits the interaction capabilities of GNNs and therefore plays into the hand of transformers, which have global interactions in all layers. A comparison of deeper models or a justification why it is not limiting GNNs to be local should be provided (not sure how many message passing steps are common in these setups).
- The problem sizes should be stated in the paper/appendix, it is only stated how many samples are in a dataset, but not how many nodes a single sample has. 
- Autoregressive models are commonly trained with next-step prediction. However due to the time aggregation and history components of the proposed method, a multi-step prediction during training is necessary which greatly limits scalability to larger models, longer rollouts and larger problem sizes (number of nodes)
- The considered datasets are at most 20 rollout timesteps, "long-horizon" seems a bit of a stretch for that.
- Given the similar performance of GST-F and GST-V, it would be interesting to visualize the attention maps to see if GST-V actually uses all of the history or only the recent ones.

### Questions
- How do models compare in terms of runtimes/parameters/flops?
- Why are the models so small, are the datasets so small/simple that larger ones run into overfitting? Are larger models infeasible? You are using A100 cards so larger models should not be a problem in terms of compute. Could you elaborate more on the scaling properties of your method (in terms of compute and to larger problem sizes)? 
- Is "temporal position embedding with the sine function" the standard transformer positional embedding with sine/cosine of variable frequencies?
- "We collect all the long-term predictions" makes it seem that long term predictions are emphasized over short term ones, however the MSE weights all predictions equally, right?
- How many timesteps are provided for GST-F?
- In Figure 2, why is $X'_T$ summed with the delta and not $X_T$. Is $X'_T$ just copied from $X_T$ for visualization?

Minor:
- line 72: "inFig" space missing
- line 123: "xpatiotemporal"
- line 264: "the decoder process" should be " the decoder processes"

### Soundness
3

### Presentation
3

### Contribution
3
