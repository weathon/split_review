# DreamCatalyst: Fast and High-Quality 3D Editing via Controlling Editability and Identity Preservation

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Score distillation sampling (SDS) has emerged as an effective framework in text-driven 3D editing tasks, leveraging diffusion models for 3D consistent editing.
However, existing SDS-based 3D editing methods suffer from long training times and produce low-quality results. We identify that the root cause of this performance degradation is their conflict with the sampling dynamics of diffusion models.
Addressing this conflict allows us to treat SDS as a diffusion reverse process for 3D editing via sampling from data space. In contrast, existing methods naively distill the score function using diffusion models.
From these insights, we propose DreamCatalyst, a novel framework that considers these sampling dynamics in the SDS framework.
Specifically, we devise the optimization process of our DreamCatalyst to approximate the diffusion reverse process in editing tasks, thereby aligning with diffusion sampling dynamics.
As a result, DreamCatalyst successfully reduces training time and improves editing quality.
Our method offers two modes: (1) a fast mode that edits Neural Radiance Fields (NeRF) scenes approximately 23 times faster than current state-of-the-art NeRF editing methods, and (2) a high-quality mode that produces superior results about 8 times faster than these methods.
Notably, our high-quality mode outperforms current state-of-the-art NeRF editing methods in terms of both speed and quality.
DreamCatalyst also surpasses the state-of-the-art 3D Gaussian Splatting (3DGS) editing methods, establishing itself as an effective and model-agnostic 3D editing solution.
See more extensive results on our project page: \url{https://dream-catalyst.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents DreamCatalyst, a variation of score distillation loss for the purpose of editing 3D scenes. This variation on SDS contains two terms: one based on DDS that controls the editing capabilities of the loss and one that is a regularization term intended to preserve the identity of the scene. The formulation in DreamCatalyst produces better quality edits and reduces edit time as compared to existing methods. The method is evaluated both qualitatively through many figures and quantitatively showing automated metrics as well as a perceptual user study.

### Strengths
Strengths:
- This work has promising results as the method shows impressive ability to edit only the regions indicated with the text prompt.
- This work proposes a reinterpretation of PDS loss that better aligns to the diffusion reverse sampling process.
- The proposed approach improves over existing techniques in both speed and edit quality.
- This work applies FreeU to the optimization to get better quality edits without sacrificing identity preservation.

### Weaknesses
Weaknesses:
- Given the similarity of DreamCatalyst to PDS, this work could benefit from a more clear / detailed discussion of the differences between these two approaches. Specifically, since the PDS loss in eq 14 in the PDS paper seems the same as eq 16 in this paper, my understanding is the main difference between these two is the hyperparameters that control the timestep dependent coefficients phi and psi for identity preservation and editability respectively. If this is the main difference, then it should be made more clear. It is not clear how the modification of these coefficients leads to the improved performance, and a more detailed explanation of the underlying mechanism would be beneficial. Specifically, how the specific functional forms of \phi(t) and \psi(t) are derived and why they are effective is not sufficiently explained.
- Since the increased speed is a key contribution of this work, more space should be devoted to explaining how this approach actually does so, as it is not clear to me in the current state. It seems to be due to the timestep sampling and approximated diffusion reverse process. However, exactly why it is faster was not clear. The manuscript should elaborate on how the approximated reverse process allows for faster convergence, and how this differs from the standard PDS approach. Additionally, a helpful experiment to highlight the speed would be to show DreamCatalyst vs IN2N VS PDS on 1k, 3k, 15k, and 30k iterations so that we can see what the quality looks like for these other methods when DreamCatalyst converges. This would provide a clearer picture of the convergence behavior of each method.
- FreeU seems like an important component to increasing edit quality, but currently there don’t seem to be any experiments showing how important it is. While there is an ablation for the FreeU hyperparameter, an experiment comparing PDS and DreamCatalyst both with and without FreeU to see how much of an impact it makes would be helpful. This would help to isolate the contribution of FreeU from the other components of the proposed method.

### Questions
Why is this method able to work with the approximated diffusion reverse process while standard PDS is not (Fig. 7). Is it just due to the coefficients phi and psi and in the case of PDS, these coefficients don't allow sufficient editability at small timesteps whereas DreamCatalyst’s do?

Minor questions:
- L:349-350 – “uniformly samples timestep t = T → 1” My understanding is that $t$ starts at $T$, ends at $1$, and then at an arbitrary iteration $i$, $t = T - i$. If this is the case, why is this uniform sampling? Maybe I am missing something here.

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
In this paper, the author proposes DreamCatalyst, a method for editing 3D scene using improved Posterior Distillation Sampling loss. Based on the analysis of PDS loss, the authors proved that the coefficients of ID-preserving loss and the DDS loss can be independently selected under DDIM inversion. They also proposed several rules for setting these coefficients under different time steps. As a result of these advances, DreamCatalyst out-performs previous 3D editing methods in both speed and quality.

### Strengths
1. This paper is well-written and easy to follow.
2. The analysis of PDS loss is interesting.
3. Experiments show that the proposed method achieves good 3D editing results with faster speed.

### Weaknesses
1. The method proposed in the paper is actually just a supplement to PDS. The theoretical analysis merely shows that the weights of the two losses can be adjusted, a fact that was already discovered and utilized in previous methods like Fantasia3D and ProlificDreamer.
2. Some of the cases used in the experiments are already present in the original PDS paper. The results from the original paper should be used for these cases. However, the PDS results provided by the authors show a significant discrepancy from the original paper. I suggest that the authors compare their results with those in the original PDS paper. I will adjust my review based on these comparisons.

### Questions
1. Why does DreamCatalyst rely that heavily on FreeU? In fig.6, with $b=1$, the model performs poorly compared with the teaser figure of the PDS paper. Is there a reasonable explanation for this?
2. Just curious, is the determination of the functional forms of $\Psi$ and $\Phi$ based on better theoretical analysis or qualitative constraints? If it's qualitative analysis, what impact do other function families or parameters that meet the proposed conditions have on the results?

### Soundness
3

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
The paper presents an innovative way to achieve 3D-consistent image editing on a 3D representation (NeRF/3DGS). It builds upon several foundational works (SDS, DDS, and PDS) to generate the edited scene with better quality and speed simultaneously. Novelty of the paper, written in section 3.3, is a (diffusion) time-step dependent weighting of the two primary loss terms (equation 17).

### Strengths
*The strength of this paper is the evaluation - the quantitative and qualitative evaluation includes the most recent works and demonstrate this method is the top-performer for this task. Table 1 shows that this paper’s family of models is faster and more semantically-aligned than existing work. Fig. 5 shows that this method generally achieves more favorable CLIP scores while being more efficient. Both NeRFs and 3DGS are evaluated.

### Weaknesses
*Technical novelty may be a bit limited. FreeU makes all Stable Diffusion models better. The core contribution appears to be a smart scheme to dynamically balance weights of an existing loss function.

*The evaluation, while thorough, does not fully isolate the impact of the proposed loss weighting scheme from the use of FreeU. It's unclear how much of the performance gain is attributable to each component. The ablation study in Fig. 6 is qualitative and lacks quantitative support, making it difficult to assess the true contribution of FreeU. The performance gains of the proposed loss and FreeU appear similar, but it is not clear if they are orthogonal or synergistic.

### Questions
*4D editing of scenes is an active area of interest - could the authors comment on if/how this work could be adapted to such use-cases?

*Could you clarify what is novel about lines 349-350 r.e. “we adopt decreasing timestep sampling.” Isn’t this standard diffusion sampling (more noise to less noise)?

*Could the authors elaborate more on where exactly the time savings are achieved? Is it because fewer optimization steps are required to train the NeRF/3DGS after the author’s proposed modified loss/FreeU?

*Elaborate more on how equation 18 was obtained?

*Fig. 6 shows a qualitative ablation on FreeU. Could a quantitative evaluation be presented as well? How much of the improvements are due to FreeU vs. better loss weighting?

### Soundness
3

### Presentation
3

### Contribution
3
