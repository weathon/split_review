---
job_id: bda57f78-c4b1-4cea-b928-344bb1ded883
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Q5SSA6IonA.pdf
paper: Fourier Neural Filter as Generic Vision Backbone
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about representation learning for computer vision, proposing a new neural backbone and evaluating it on standard vision benchmarks, which is well within ICLR scope.

## Minimum Quality
Pass ✅. The submission contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While there are important concerns about rigor, clarity, and support for some claims, these do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, instructions targeting automated reviewers, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes Fourier Neural Filter (FNF), an input-dependent Fourier-based operator intended to address two stated limitations of Fourier Neural Operators for vision, namely bandwidth bottleneck and over-smoothing. Building on FNF, the authors introduce Vision Filter (ViF), a hierarchical vision backbone that combines local convolutions, frequency-domain global convolution, selective activation, and adaptive modulation, and evaluate it on ImageNet-1K classification, COCO detection, and ADE20K segmentation.

## Strengths
The paper tackles a relevant problem, namely whether Fourier-domain token mixing can serve as a generic vision backbone competitive with Transformer- and Mamba-based architectures. That is a meaningful question for the ICLR community, especially given the ongoing search for backbones with better scaling properties and stronger global modeling.

The empirical scope is fairly broad. The paper reports results on three standard tasks, image classification, object detection, and semantic segmentation, rather than relying on ImageNet alone. This is helpful because many backbone papers look decent on classification but collapse on dense prediction.

The architectural intuition is understandable at a high level. In **Figure 2**, the proposed FNF module is visualized as a two-branch design combining a Fourier branch with complex transform and adaptive modulation, and a local branch with gating. Even though some mathematical details remain underspecified, the figure does communicate the intended coupling between local spatial processing and global frequency-domain filtering. Likewise, **Figure 3** gives a reasonably intuitive overview of how the FNF block is inserted into a standard four-stage hierarchical backbone, which makes the system-level design easier to follow.

Some of the numerical results are competitive. In **Table 2**, ViF-T/S/B are consistently strong on ImageNet-1K and compare favorably to several listed CNN, Transformer, Mamba, and earlier Fourier baselines at roughly similar model sizes. The gains over GFNet/GFNetV2 are especially notable within the Fourier-based family, which does support the claim that plain Fourier filtering can be improved for vision.

The ablation in **Table 5** is a useful start. It suggests that selective activation and adaptive modulation are not decorative additions but contribute measurable accuracy gains, with selective activation appearing to matter most in the reported setup.

## Weaknesses
I have a number of concerns, several of which affect the paper’s central claims rather than just presentation.

1. **The theoretical claims are much stronger than what is actually established in Section 3.**  
The paper repeatedly claims that FNF “resolves” or “substantially addresses” the bandwidth bottleneck and over-smoothing of FNO, see the Introduction on **Page 2** and **Remark 3** on **Page 5**. However, the formal content in **Proposition 1** and **Proposition 2** on **Page 3** only characterizes limitations of a truncated FNO-style spectral operator. There is no corresponding proposition or theorem showing that the proposed FNF, as defined in **Equations (4)-(12)**, avoids the lower bound in Equation (1), weakens it, or guarantees preservation of mid/high frequencies with depth. The theory, as written, establishes a problem statement, not a solution theorem. For a paper leaning heavily on mathematical framing, this gap matters a lot because the headline claims are presented as theoretically supported when they are mostly heuristic.

2. **Several equations are underspecified, inconsistent, or mathematically loose enough to hinder technical verification.**  
A few concrete examples:
   - In **Equation (6)** on **Page 4**, the parentheses appear unbalanced:  
     \[
     P(v)(x)=\mathcal{F}^{-1}(R_{\phi}\cdot\mathcal{F}(H(v))(x),
     \]
     which makes the implementation-level operator ambiguous.
   - In **Equation (5)**, \(T\), \(G\), and \(P\) are introduced as “linear transform used for expansion or compression,” but their domains, codomains, tensor shapes, and whether they are pointwise, convolutional, or channel-mixing maps are not defined. Since the core mechanism is \(T(G(v)\odot P(v))\), these details are not optional.
   - In **Definition 5**, **Equation (10)** claims an approximation of pointwise multiplication via magnitude modulation and phase addition, but the notation is broken, for example \( |P(v)i| \), \(\theta G(v)i\), and the approximation conditions are not formalized. It is also unclear whether signals are complex-valued at that stage in the architecture, or whether the operation is performed before/after inverse FFT.
   - In **Equation (12)**,  
     \[
     \mathcal{M}(z)=z\odot\left[\beta\cdot\|z\|^{\alpha}\right],
     \]
     the paper discusses “stability constraints” earlier on **Page 2**, but no such constraints are actually stated. If \(\alpha\) and \(\beta\) are learnable without restrictions, the transform can amplify large magnitudes aggressively. Since this module is presented as important for frequency balancing, the missing constraints are not a minor notation issue.

   These problems matter because the method’s main selling point is a specific time-frequency operator design. If the exact operator is not fully specified, reproducibility and theoretical scrutiny both suffer.

3. **The link between the formal definition of an input-dependent kernel and the actual implemented module is asserted, not derived.**  
In **Definition 2** on **Page 4**, FNF is defined as an adaptive integral operator  
\[
(Kv)(x)=\int_D \kappa(x,y;v)v(y)\,dy.
\]
Then **Equation (5)** gives an implementation form using \(T(G(v)\odot P(v))\), and **Definition 4** turns this into a “gated global convolution.” But the paper does not actually derive the effective kernel \(\kappa(x,y;v)\) induced by this computation, nor does it show under what assumptions the implementation corresponds to the stated adaptive integral operator. This is not just pedantry. The paper uses the operator-learning language to argue conceptual generality and novelty, so the missing bridge between abstract operator and concrete module weakens the paper’s core positioning.

4. **The empirical comparisons are broad, but fairness is uneven and some claims are overstated relative to the numbers.**  
In **Table 2** on **Page 7**, the paper compares against models trained at different resolutions, for example ViT-B/16 and GFNetV2 at \(384^2\), SwinV2 at \(256^2\), and ViF at \(224^2\). Cross-model comparison is still informative, but the text on **Page 6** and **Page 7** often reads as if these are directly apples-to-apples. A similar issue appears when comparing across architectural families with likely different training recipes inherited from prior papers. The submission says it follows prior works, but it does not make clear whether ViF itself uses exactly matched augmentation, regularization, EMA, label smoothing, mixup/cutmix, stochastic depth, optimizer settings, and training epochs relative to all reported baselines. For a backbone paper, this matters because small ImageNet deltas can disappear under recipe changes.

5. **The efficiency story is not fully convincing, despite being highlighted early.**  
**Figure 1** on **Page 1** is intended to position ViF favorably on the throughput vs. accuracy frontier. The figure is visually helpful, and ViF does look competitive, but the paper never explains whether throughput was measured for all compared methods under a unified implementation stack, identical precision settings, identical data loader and kernel fusion conditions, etc. Throughput is highly framework-dependent, especially when FFTs, custom kernels, or scan-based operators are involved. Without that information, the figure is more suggestive than definitive. Since the abstract explicitly claims lower computational complexity and Figure 1 is prominently used to support efficiency, the missing measurement protocol weakens an important part of the argument.

6. **The dense prediction gains over the strongest Mamba baselines are modest, and the paper itself partially acknowledges this.**  
On COCO and ADE20K, the improvements over VMamba are often small. For example, in **Table 3** on **Page 8**, ViF-S improves over VMamba-S by only \(0.4\) AP\(_b\) and \(0.3\) AP\(_m\) under the \(1\times\) schedule, and by \(0.2\) / \(0.2\) under the \(3\times\) multi-scale schedule. In **Table 4** on **Page 9**, ViF-S is actually slightly worse than VMamba-S in single-scale mIoU, \(50.5\) vs. \(50.6\), and only \(+0.1\) in multi-scale mIoU. These are not bad results, but they do not justify sweeping statements such as “consistently outperforms prominent variants” in the abstract without more nuance. The paper’s own limitations section on **Page 9** says the downstream gains are marginal relative to other ViM models, which is a more accurate summary than some earlier claims.

7. **The ablation study is too narrow for the complexity of the proposed method.**  
**Table 5** on **Page 9** removes LC-1, LC-2, adaptive modulation, and selective activation from ViF-T, but that is not enough to validate the paper’s main design claims. Missing ablations include:
   - replacing the input-dependent gating with a simpler static gate,
   - removing the complex transform entirely,
   - varying the spectral bandwidth \(K\),
   - testing whether adaptive modulation alone, without selective activation, explains most of the gain,
   - comparing against a matched local+FFT baseline without the operator-style formulation.
   
   Also, the reported deltas are fairly small, mostly \(0.2\) to \(0.7\) top-1, and there is no variance over runs. If the method’s conceptual contribution is the joint time-frequency mechanism, the ablation should isolate that more cleanly.

8. **The paper does not provide direct evidence for the claimed mechanism, namely better preservation of mid/high frequencies or mitigation of over-smoothing.**  
This is a notable omission because the entire motivation in **Section 3.1** is framed in frequency terms. Yet there are no spectral diagnostics, no frequency response visualizations, no depth-wise energy analyses, and no representation smoothness measurements comparing FNO/GFNet/ViF. A straightforward figure showing spectral energy retention or learned filter responses would have made the argument much stronger. As it stands, the mechanism claims remain largely inferential, based on end-task accuracy only.

9. **The novelty positioning relative to prior Fourier-based and adaptive filtering approaches is incomplete.**  
The related work section on **Pages 2-3** is quite short and focuses mainly on FNO, GFNet, and AFNO-derived work in scientific computing. Given that the main claim is an adaptive Fourier-based generic vision backbone with content-dependent filtering, the discussion should more carefully distinguish itself from prior adaptive Fourier token mixers and other operator-inspired vision models that also try to balance locality and global frequency modeling. Right now the paper’s novelty is presented in somewhat broad strokes, and the exact conceptual delta over existing adaptive Fourier filtering ideas is not sharply articulated.

10. **There are nontrivial presentation issues and occasional overclaiming.**  
The writing is readable at a high level, but there are many grammatical and notation issues that accumulate. Examples include inconsistent naming between “Vision Filter (ViF)” and “Fourier Neural Filter (FNF)” vs. “Fourier Neural Filter as Generic Vision Backbone” in the title, a likely typo on **Page 2** where the text says “we propose Fourier Neural Filter (FNF)” and later says “Building upon FNF, we construct Vision Filter (ViF),” and malformed entries in several tables such as “2242”, “3842”, “5122”, which should presumably be \(224^2\), \(384^2\), \(512^2\). These are fixable, but for an ICLR main-track submission centered on a new mathematical module, the current level of polish is not yet where it should be.

## Questions
1. The central theoretical claim is currently asymmetric: Section 3 proves limitations of FNO, but not corresponding guarantees for FNF. Can the authors provide a formal result showing how the input-dependent operator in **Equations (4)-(12)** weakens the lower bound in **Equation (1)** or avoids the multiplicative contraction described in **Proposition 2**? Even a partial theorem under explicit assumptions would materially increase my confidence.

2. Please fully specify the implementation behind **Equations (5)-(12)**. In particular:
   - what are the exact tensor shapes of \(G(v)\), \(H(v)\), \(P(v)\), and \(T(\cdot)\),
   - which tensors are complex-valued and at what stage,
   - whether the Hadamard product is performed in the spatial domain or after inverse FFT,
   - what spectral modes are retained,
   - and what constraints, if any, are imposed on \(\alpha\) and \(\beta\) in **Equation (12)**.

3. For **Figure 1**, were all throughput numbers measured under the same codebase, precision mode, and hardware-level optimization settings, or were some copied from prior papers? A unified measurement protocol would make the efficiency comparison much more credible.

4. Could the authors add mechanism-focused evidence, not just end-task accuracy, for the claimed frequency behavior? For example, spectral energy retention across depth, learned filter visualizations, or comparisons of high-frequency response between FNO/GFNet and ViF. This would directly test the motivating story in **Section 3.1**.

5. The dense prediction gains over VMamba are often quite small in **Tables 3 and 4**. Can the authors temper the “consistently outperforms” narrative or provide stronger evidence that the advantage is robust across seeds, training schedules, or detector/segmentor heads?

6. The ablation in **Table 5** is a useful start, but can the authors include stronger controls, especially a matched local-conv + FFT baseline without selective activation or adaptive modulation, and a version with static rather than input-dependent gating? That would clarify whether the main benefit truly comes from the proposed adaptive operator.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work uses standard public vision datasets and proposes a generic backbone. The brief broader-impact discussion is minimal, but I did not identify a concrete ethics issue that would require escalation.

## Soundness Rating
2: fair. The empirical results are substantial enough to suggest the method has merit, but the paper overstates what is theoretically established, and key operator definitions and implementation details are underspecified.

## Presentation Rating
2: fair. The high-level idea is understandable and the figures help, but there are enough notation problems, malformed equations, and overclaimed statements that clarity is below the standard I expect for a method paper centered on a new mathematical module.

## Contribution Rating
2: fair. The paper addresses an interesting and relevant design space, and the results are competitive, but the conceptual delta over prior Fourier-style vision backbones is not sharply established and the evidence for the claimed mechanism is incomplete.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and empirically competitive, especially on ImageNet, but in its current form it asks the reader to buy a stronger theoretical and mechanistic story than it actually delivers. With tighter mathematical specification, fairer and better contextualized claims, and stronger ablations/diagnostics, this could become a much stronger submission.

## Reviewer Confidence
4: confident. I am comfortable assessing vision backbone papers and frequency-domain architectures, and I checked the main equations, figures, and result tables carefully, though some implementation-level ambiguity remains because the paper itself leaves key details unspecified.