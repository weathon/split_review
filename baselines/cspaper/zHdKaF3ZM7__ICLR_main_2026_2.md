---
job_id: 646a027e-4737-4196-a3f0-69da1dd6ef80
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zHdKaF3ZM7.pdf
paper: Weight-Space Linear Recurrent Neural Networks
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, proposing a new sequence modeling architecture at the intersection of recurrent models, meta-learning, weight-space learning, in-context adaptation, and physics-informed ML.

## Minimum Quality
Pass ✅. The paper contains all core scientific components, including Abstract, Introduction, related-work discussion, methodology, experiments/results, and discussion/conclusion; while I have technical and empirical concerns, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or other suspicious content targeting automated review systems in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes WARP, a sequence modeling framework in which the recurrent hidden state is not a conventional feature vector but the time-varying parameter vector of an auxiliary root network, typically an MLP. The recurrence is linear in weight space, driven by input differences, and the resulting weight state self-decodes by being unflattened into the root network evaluated at coordinates \(\tau\). The paper evaluates this idea across image completion, time-series forecasting, dynamical system reconstruction, multivariate time-series classification, and a synthetic in-context learning setup, including a physics-informed variant.

## Strengths
The core idea is interesting and distinct. Representing the recurrent state as a weight vector \(\theta_t\) of a decoder network, as formalized in **Equation (1)** on **Page 4**, is a meaningful departure from standard RNN/SSM formulations. This is not just a cosmetic reinterpretation; it changes what the state can represent and gives the model a natural mechanism for test-time adaptation without gradient updates.

The paper does a good job of communicating the concept visually. **Figure 1** on **Page 2** is genuinely helpful: it makes the contrast between standard RNNs, linear RNNs, and the proposed weight-space linear RNNs easy to parse, and it clarifies that the nonlinearity is shifted from the recurrence to the decoder. **Figure 2** on **Page 3** also helps by showing the unfolded computation with \(\phi\), \(A\), and \(B\), making the architecture easier to understand than the equations alone.

The empirical scope is broad. The paper does not rely on one cherry-picked benchmark, but instead studies forecasting, classification, image completion, dynamical systems, and an in-context learning toy setup. Even if not every experiment is equally convincing, the breadth makes the central idea harder to dismiss as narrowly tuned for one domain.

Some of the quantitative results are strong. In **Table 1** on **Pages 5-6**, WARP is competitive or best on MNIST and clearly strongest on CelebA among the compared methods. In **Table 3** on **Page 7**, the black-box WARP variant is consistently competitive for dynamical system reconstruction, and the physics-informed variant gives very large gains when the prior is appropriate. In **Table 4** on **Page 8**, WARP is not dominant across all UEA datasets, but it is competitive and does place near the top on several tasks.

I also appreciated that the paper includes ablations and limitations. The discussion around positional encodings, the role of \(\phi\), and the dense \(A\) matrix is useful. In particular, **Table 15** and **Table 16** in the supplement are aligned with the architectural story the paper is telling, rather than being generic ablations added as decoration.

The paper is generally readable despite the ambitious scope. The high-level motivation is clear, and the writing is energetic. The conceptual framing around weight-space recurrence is memorable, which matters for a paper trying to introduce a new modeling perspective.

## Weaknesses
1. **The mathematical development around the convolutional mode is shaky, and parts of the theory feel more like an existence sketch than a solid foundation.**  
   The most concrete issue is in **Theorem 1** on **Page 21**. It assumes \(B \in \mathbb{R}^{D_\theta \times D_x}\) is full row-rank so that \(\mathbf{u} \mapsto B\mathbf{u}\) is surjective, which indeed would require \(D_x \ge D_\theta\). But the paper itself immediately acknowledges on **Page 22** that in practice \(D_\theta \gg D_x\), so this assumption is typically violated. That means the theorem underlying the convolutional formulation is not applicable in the regime the method actually operates in. The fallback, **Theorem 2** on **Page 22**, is also not very satisfying: it fixes \(B = \nabla \phi(\mathbf{x}_0)\), assumes \(\phi\) is locally linear, and uses \(\ker \phi \neq \emptyset\) to recover an initial difference \(\Delta \mathbf{x}_0\). This is a fairly artificial construction, and the “proof” leans on identifying a first-order Taylor expansion with exact equality. For a general MLP \(\phi\), local linearity only gives an approximation, not an exact identity over a non-infinitesimal displacement. So the jump from local linearization to exact convolutional equivalence is not justified as written. This matters because the paper presents convolutional and recurrent modes as a core algorithmic contribution, but the formal guarantee for the convolutional mode seems misaligned with the actual model regime.

2. **Several training-objective details are underspecified or inconsistent, especially in the autoregressive setting.**  
   On **Page 5**, the paper says scheduled sampling selects between ground truth \(\mathbf{y}_t\) and predicted \(\hat{\mathbf{y}}_t\) with Bernoulli probability \(p_{\mathrm{forcing}}\), but then immediately says “That said, we consistently use \(\hat{\mathbf{y}}_{t-1}\) in the input difference seen in Eq. (1).” These two statements are hard to reconcile. If the recurrence always uses \(\hat{\mathbf{y}}_{t-1}\), then teacher forcing is not actually applied to the recurrence state update, only perhaps to the decoder input or the rollout bookkeeping. The exact AR training objective is therefore ambiguous. This is not a pedantic complaint: in recurrence-based forecasting, whether the hidden-state transition uses ground truth or model predictions materially affects optimization and exposure bias.  
   There is also a notation issue in **Equation (2)** on **Page 5**. The NLL is written with a scalar \(\hat{\sigma}_t\), but earlier on **Page 4** the model predicts a vector \(\hat{\boldsymbol{\sigma}}_t \in \mathbb{R}^{D_y}\). If the Gaussian is factorized with diagonal covariance, the correct per-time-step expression should be something like
   \[
   \sum_{j=1}^{D_y} \left(\frac{(y_{t,j}-\hat{\mu}_{t,j})^2}{2\hat{\sigma}_{t,j}^2} + \log \hat{\sigma}_{t,j}\right),
   \]
   up to constants, rather than dividing an \(L_2\) norm by a single \(\hat{\sigma}_t^2\). Similarly, the categorical cross-entropy on **Page 5** is missing the conventional minus sign if \(\mathcal{L}_{\mathrm{CCE}}\) is indeed being minimized. These are fixable, but the current presentation of the objectives is not precise enough for a method paper.

3. **Some experimental comparisons are not as clean or fair as the paper suggests.**  
   The paper repeatedly makes strong claims of superiority, but the baseline setup is uneven in places. A concrete example is the image completion comparison in **Table 1** on **Page 5**. The paper says all models are trained with the NLL loss in recurrent AR mode to ensure fair comparison, yet the supplement later states that **S4** was trained differently for MNIST, using a 256-way cross-entropy over discretized pixel intensities (**Page 26**). That means the comparison is not actually “same objective, same setup” for all methods. Another example is that the paper often reports the best run or best-performing model in qualitative discussions, for instance around **Figure 3(a)** on **Page 6**, which weakens the evidential value of those visuals.  
   More broadly, the benchmark set for some tasks omits obvious stronger or more directly relevant modern adaptive baselines. For example, the in-context learning section on **Pages 8-9** demonstrates that WARP can solve a synthetic associative task, but it is not compared directly against models that are specifically motivated by in-context learning or fast-weight style adaptation. This makes the section more illustrative than evaluative.

4. **Some of the headline empirical claims are stronger than what the tables support.**  
   On the positive side, **Table 4** on **Page 8** does show that WARP is competitive on UEA datasets, but the text says it establishes “new state-of-the-art accuracies” on SCP2, Ethanol, and Heartbeat. That is only partially true: on SCP2, FACTS has \(70.3 \pm 8.8\), well above WARP’s \(57.89 \pm 1.4\). So the claim is simply incorrect for SCP2, at least as far as **Table 4** shows. This kind of mismatch between prose and table is not minor because it undermines trust in the empirical interpretation.  
   Similarly, **Table 2** on **Page 6** reports a dramatic improvement on PEMS08, but the setup changes substantially relative to the standard graph-based formulation: the sequence is flattened across nodes and passed through a non-causal convolution before WARP. That does not invalidate the result, but it makes the “without using the inherent graph structure” narrative less clean than advertised, because the preprocessing injects a strong learned mixing layer over all node features. A result that large deserves tighter scrutiny and stronger contextualization in the main paper.

5. **The scalability bottleneck is serious and under-addressed in the main paper.**  
   The transition matrix \(A \in \mathbb{R}^{D_\theta \times D_\theta}\) is dense, so the model cost scales quadratically in the size of the root network state. The paper acknowledges this limitation in **Section 4.2** on **Pages 9-10**, but it is really more than a minor caveat, it is a central practicality concern. The supplement reinforces this rather than alleviating it: the authors state in the ablations that replacing \(A\) with diagonal or low-rank approximations hurt performance (**Page 36**, **Figure 14**), which suggests the current formulation may not scale gracefully. Since one of the paper’s conceptual selling points is that weight-space states provide high-capacity memory, the inability to scale that memory without an \(O(D_\theta^2)\) transition is a substantial unresolved issue. This matters for ICLR because the method is presented partly as a general sequence modeling paradigm, yet the current instantiation seems constrained to modest-sized root networks.

6. **The paper leans heavily on appendix-only evidence for important claims that should have been better supported in the main paper.**  
   The main text makes big-picture claims about computational efficiency, expressivity, robustness, and adaptation, but some of the supporting evidence is either deferred or qualified in the supplement. For instance, **Table 13** in the supplement shows WARP is *not* the fastest model on MNIST image completion, since the Transformer entry has lower time per epoch than WARP, despite the caption claiming WARP is the most efficient. Likewise, the adaptation story is mostly argued conceptually rather than demonstrated through a clean controlled test-time adaptation benchmark in the main paper. The in-context learning experiment on **Figure 5** is suggestive, but it is not the same as showing strong adaptation under distribution shift. The result is a paper that occasionally oversells what has been directly demonstrated in the main text.

7. **There are presentation issues and occasional overclaims that make the paper read less carefully calibrated than it should.**  
   The paper often reaches for sweeping statements such as “transformative paradigm” in the abstract and “step further towards human-level artificial intelligence” in the conclusion on **Page 10**. Those claims are far beyond what the experiments establish. There are also smaller but important clarity problems: notation for \(D_v\) in **Equation (1)** on **Page 4** appears without definition, while the recurrence elsewhere uses \(D_x\); the role of \(\tau\) varies by task but the dependence of output quality on this coordinate system is not disentangled cleanly in the main paper; and the text occasionally attributes performance on long sequences to initialization and positional encodings without direct causal evidence from the main experiments. These are not fatal flaws, but they make the paper feel a bit too eager to claim conceptual closure on questions that remain open.

8. **The visual evidence is mixed, and some figures support narrower claims than the text implies.**  
   **Figure 3(a)** on **Page 6** is a nice qualitative comparison for MNIST completion, and WARP does look visually better than the baselines shown. However, this figure alone does not support the broader expressivity and generalization claims made throughout the paper; it supports a narrow claim about one image completion setting at one parameter scale. Likewise, **Figure 5(b-c)** on **Page 9** shows the model can fit/query linear mappings in a synthetic ICL task, but because there are no direct baseline curves or scaling comparisons, the figure mostly shows feasibility, not competitiveness. On the other hand, **Figure 3(b)** is one of the better figures in the paper because it gives a compact cross-dataset summary for ETT, but even there a heatmap of best/second-best results is less informative than a full numeric table with variances would have been.

## Questions
1. In the AR training description on **Page 5**, what exactly is fed into the recurrence update \( \theta_t = A\theta_{t-1} + B\Delta x_t \) during training? The text first describes scheduled sampling between ground truth and predictions, but then says it “consistently” uses \(\hat{\mathbf{y}}_{t-1}\) in the input difference. Please state the exact recurrence used during training and inference, with notation, so it is unambiguous whether teacher forcing affects the hidden-state evolution.

2. Please clarify the probabilistic objective in **Equation (2)**. Is \(\hat{\sigma}_t\) scalar or vector-valued? If vector-valued, please provide the correct diagonal-Gaussian NLL expression used in implementation. Similarly, please confirm whether the categorical cross-entropy on **Page 5** omits a minus sign only for brevity, or whether a different sign convention is being used.

3. For the convolutional mode, can the authors either substantially tighten **Theorem 2** or reframe it more modestly? As written, the local-linearity argument does not seem sufficient to claim exact equivalence to the convolutional form for a generic nonlinear \(\phi\). A clearer statement of what is approximate, what is exact, and what is only an implementation heuristic would increase my confidence.

4. For **Table 4** on **Page 8**, please reconcile the textual claim about state-of-the-art results with the actual entries. In particular, how should readers interpret the SCP2 result where FACTS appears much stronger than WARP? If there is a preprocessing or protocol mismatch, please explain it explicitly in the rebuttal.

5. For **Table 2** on **Page 6**, the PEMS08 gain is unusually large. Could the authors provide a more detailed accounting of the preprocessing and parameter count, especially the non-causal convolution over all node features? I would like to understand how much of the gain comes from WARP itself versus the feature-mixing frontend.

6. The paper’s central practical limitation is the dense \(A\) matrix. Can the authors give more quantitative evidence, ideally from the main paper or rebuttal, on how performance and memory scale with \(D_\theta\)? Even a compact scaling plot would help evaluate whether the method is a proof-of-concept or a realistic general-purpose sequence model.

7. The in-context learning section is interesting, but currently qualitative. Can the authors provide direct comparisons against at least one fast-weight or linear-attention-style baseline on the exact synthetic task in **Figure 5**, including sample efficiency or sequence-length scaling? That would make the ICL claim much more persuasive.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper includes a short broader-impact discussion and does not appear to involve human subjects, sensitive personal data, or deployment in a high-risk setting based on the main text. I do not see an ethics issue requiring escalation.

## Soundness Rating
2: fair. The core idea is plausible and supported by several experiments, but there are notable issues in the mathematical presentation, objective specification, and fairness/cleanliness of some experimental comparisons.

## Presentation Rating
3: good. The paper is generally readable and conceptually well illustrated, especially through **Figures 1, 2, 3, and 5**, but there are several notation inconsistencies, overclaims, and places where critical details are deferred or ambiguously stated.

## Contribution Rating
3: good. The weight-space recurrence formulation is interesting and likely worth sharing with the community, but the contribution is weakened by unresolved scalability issues, shaky theoretical support for some algorithmic claims, and a few overstatements relative to the evidence.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a genuinely interesting modeling idea and enough empirical evidence to merit serious consideration, but it also has several technical and experimental loose ends that prevent a stronger recommendation.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I checked the main equations, examined the tables and figures carefully, and am familiar with the surrounding sequence-modeling literature, but some implementation details remain ambiguous from the paper alone.