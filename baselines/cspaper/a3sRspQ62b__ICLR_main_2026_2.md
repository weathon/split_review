---
job_id: 399268ad-046a-41cc-99f0-95877d3ae57d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: a3sRspQ62b.pdf
paper: FourierFlow: Frequency-Aware Flow Matching for Generative Turbulence Modeling
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies generative modeling, representation learning for physical systems, and applications to fluid dynamics.

## Minimum Quality
Pass ✅. The paper contains the core components expected of a research submission, including abstract, introduction, method, experiments, quantitative results, and conclusion; while the exposition has important weaknesses, it is still a complete scientific paper rather than an incomplete draft.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes FourierFlow, a conditional flow-matching model for multi-step turbulent flow generation that combines a dual-branch backbone with a salient flow attention branch, a Fourier mixing branch, and a pretrained MAE-based feature alignment loss. The paper argues that existing generative models suffer from spectral bias and common-mode noise, and evaluates the proposed method on compressible Navier-Stokes and shear-flow benchmarks, including ablations and some generalization tests.

## Strengths
The paper addresses a relevant problem for ML in physical sciences, namely how generative models can better preserve fine-scale structure in turbulent or turbulence-like fluid dynamics. The emphasis on spectral fidelity, rather than only pointwise reconstruction, is a worthwhile direction.

The architecture is reasonably well motivated at a high level. The combination of a spatial attention branch and a Fourier-domain branch is intuitive for multi-scale flow fields, and the adaptive fusion in Equations (9) and (10) is a sensible way to let the model interpolate between spatially salient and frequency-aware representations.

The empirical section is broad. **Table 1** covers several classes of baselines, including autoregressive surrogate models, multi-step surrogate models, next-step generative models with rollout, and multi-step generative models. This breadth is useful because it positions the method against both forecasting-style PDE models and recent generative approaches. The gains on Compressible N-S at \(M=0.1\), especially over STDiT and CFM, are large enough to suggest that the proposed design is doing something nontrivial rather than just benefiting from noise in evaluation.

Some figures are effective. **Figure 3** gives a reasonably clear overview of the training and sampling pipelines, and it helps the reader understand how the MAE alignment enters only during training while the flow ODE is used at sampling time. **Figure 1** also communicates the intended notion of spectral bias in a direct way: the residual spectrum of STDiT appears concentrated in higher wavenumbers, while the proposed model appears flatter. Even though I have concerns about how far this evidence can be generalized, the figure is useful as motivation.

The ablations are directionally helpful. **Figure 4** suggests that removing the Fourier mixing branch or replacing adaptive fusion with naive addition hurts all reported metrics. **Figure 5** also indicates that the alignment coefficient is not arbitrary and that performance is sensitive to it, which supports the claim that the surrogate alignment is not merely decorative.

## Weaknesses
1. **The paper oversells “turbulence” and physical fidelity, while the evaluation is still mostly ML-style reconstruction error.**  
   The central framing is about high-fidelity turbulence modeling, physical consistency, and preservation of energy across scales, but the actual main metrics in **Table 1** are MSE, nRMSE, and Max\_ERR only. Those are useful, but they do not establish that the generated trajectories preserve the physically meaningful statistics that matter for turbulent flows, such as energy spectra, structure functions, enstrophy, invariant preservation, or long-time distributional statistics. The paper repeatedly claims better “physical consistency” in the abstract, introduction, and Section 5.2, but the main paper never backs that up with direct physics-aware measurements. This matters a lot here, because a model could improve pointwise RMSE while still distorting the spectrum, dissipation, or long-range statistics that make turbulence difficult in the first place.

2. **The theoretical analysis in Section 4 is too weak relative to the claims it is used to support.**  
   Theorem 4.1 essentially states that if the initial power spectrum decays as \(|\hat{x}_0(\omega)|^2 \propto |\omega|^{-\alpha}\) and the forward diffusion noise has frequency-independent variance, then high frequencies hit a fixed SNR threshold earlier. This is intuitive and not controversial, but the paper uses it to motivate broad claims about why “generative models” struggle and why the proposed approach is needed. There are at least two problems. First, the theorem is about the forward corruption process of a simplified diffusion SDE \(d\mathbf{x}_t = g(t)\, d\mathbf{w}_t\), not about the learned reverse model’s actual reconstruction quality. Second, the method proposed in the paper is a flow-matching model, yet the theorem mostly critiques diffusion-style corruption. The bridge from “high frequencies are corrupted earlier in a simple SDE” to “therefore FourierFlow should reconstruct them better than strong alternatives” is not established. As written, the theory is more motivational folklore than a technical justification for the proposed architecture.

3. **The mathematical exposition around the common-mode noise story is not convincing enough, and some claims are under-justified.**  
   Section 2.2 defines common-mode noise by projecting a channel vector \(n \in \mathbb{R}^C\) onto \(\operatorname{span}\{\mathbf{1}_C\}\), then argues that adding \(n_{\mathrm{cm}}\) to all tokens shifts \(QK^\top\) by a rank-1 term \(+\beta \mathbf{11}^\top\), which “flattens the softmax distribution and suppresses token discrimination.” This step is much too quick. A constant additive term shared across all logits within a row would cancel under softmax, while a general rank-1 perturbation does not necessarily flatten attention uniformly. The paper needs a much more careful derivation here, because this argument is doing heavy conceptual lifting for SFA. Right now it reads as if analogies from electronics were imported into attention without enough mathematical precision.

4. **Equations (4) to (6) are not fully specified, and the notation is inconsistent enough to hinder reproducibility.**  
   In Equation (4), \(\mathrm{DiffAttn}(X) = (\mathrm{Attn}_1(X) - \lambda \mathrm{Attn}_2(X))V\), then in Equation (5) a neighborhood-centered \(\tilde K_2[j]\) is introduced, and the text says \(\mathrm{Attn}_1\) should focus on local structure while \(\mathrm{Attn}_2\) captures broader background context. But the actual definition of \(\mathrm{Attn}_2[i,j]\) restricts it to \(j \in \mathcal N(i)\), which sounds local rather than broad. There is a conceptual mismatch between the prose and the equation. Also, \(\mathcal N(j)\) is defined as \(\kappa\) nearest neighbors of patch \(j\), but the distance metric over patches is never specified, whether spatial-only or spatiotemporal. Given that the branch operates on video-like inputs, this is not a minor implementation detail. The reader cannot tell whether neighbors are defined in Euclidean image coordinates, feature space, or token order.

5. **The Fourier mixing branch has unclear or possibly incorrect wording around mode truncation and high-frequency preservation.**  
   In Section 3.2, Equation (7) defines a spectral operator based on AFNO, and the text states, “Since there is mode truncation to keep high-frequency components, \(\mathbf W_\theta^l(\xi)\) can amplify or attenuate specific frequency components.” This is odd. Standard Fourier neural operator truncation usually discards high-frequency modes and keeps lower modes, unless the implementation is explicitly reversed. The sentence as written suggests the opposite. If the authors indeed keep high-frequency modes, this should be stated precisely, because it is a critical design choice. If not, the wording is simply wrong. This is important because the paper’s main claim is about explicit mitigation of spectral bias.

6. **The surrogate alignment component is underspecified in the main paper.**  
   Section 3.3 says the method aligns intermediate representations of FourierFlow with those of a frozen MAE encoder, and the total loss is \(\mathcal L_{\text{Total}} = \mathcal L_{\text{CFM}} + \gamma \mathcal L_{\text{Align}}\). But \(\mathcal L_{\text{Align}}\) is never defined mathematically in the main paper. Which layers are aligned? Are features normalized? Is the loss an \(\ell_2\) loss, cosine loss, projection loss, or something else? Is there a learned projector as in REPA-like setups? This is a major omission because the alignment loss is presented as one of the three main contributions. Without a formal definition, the method is not fully specified.

7. **There are multiple presentation and consistency problems that reduce trust in the experimental section.**  
   One concrete example is the train/test split description. On **Page 7**, just below **Table 1**, the paper says “We use \(90\%\) of the data for training.” But in Section 5.1 on the same page it says each dataset is split into \(80\%\) training, \(10\%\) validation, and \(10\%\) test. These are not the same setup. Another example is metric naming: the caption of **Table 1** says “RMSE represents root mean square error,” but the columns are labeled “MSE” rather than RMSE. There are also terminology mismatches such as “Fourier-Flow” versus “FourierFlow,” and “flow matching” versus “CFM” and “\(\mathcal L_{\text{flow}}\)” versus “\(\mathcal L_{\text{CFM}}\).” Each issue alone is small, but together they give the impression that the paper has not been cleaned up carefully enough for a top-tier conference submission.

8. **The empirical comparisons in Table 1 are not as airtight as the paper suggests.**  
   **Table 1** compares methods with quite different parameter counts, from 12.4M to 169M. The proposed model is 161M, which is among the largest methods. The table does not provide training cost, inference cost, number of sampling steps, or wall-clock efficiency. This matters especially because Section 2.3 explicitly advertises flow matching as computationally appealing. If speed and deterministic sampling are part of the value proposition, the paper should quantify them. Also, some baselines are marked as re-implementations with asterisks, but the main paper gives no information about whether hyperparameters and data preprocessing were tuned comparably. When the claimed improvement is “about 20% on average” in Section 5.2, the reader needs stronger evidence that this is not partly due to implementation choices.

9. **The figure-based evidence for common-mode suppression is weaker than the text implies.**  
   The paper points to **Figure 6** as evidence that replacing SFA with standard self-attention causes performance degradation. That supports usefulness of the module, but not specifically the claim that SFA reduces common-mode noise. The figure shows outcome metrics, not attention maps, not channel-wise projections, and not any direct measurement of the common-mode component defined in Section 2.2. In other words, the ablation supports “this branch helps,” but not the much sharper mechanistic story the paper tells.

10. **The generalization analysis is suggestive but incomplete.**  
    **Figure 7** and **Figure 8** indicate improved OOD and long-horizon behavior, and I appreciate that the paper goes beyond IID test error. However, the setup remains too narrow to fully support the broad claims in the abstract about “strong generalization capabilities.” Figure 8 compares against a surrogate baseline only, not against the strongest generative baselines from **Table 1** such as STDiT or DYffusion. If the paper wants to claim that the generative formulation itself improves long-horizon generalization, the comparison should include those methods directly. Otherwise the reader cannot separate architectural benefits from category-level differences.

11. **Related-work positioning is incomplete around generative turbulence modeling itself.**  
    The paper cites some recent diffusion-for-PDE works, but the positioning remains strangely broad and image-model-centric for a submission focused on turbulence generation. There should be a more direct discussion of prior generative turbulence models and prior work that already addresses spectral degradation or Fourier-aware generative modeling in fluid settings. Without that, it is hard to tell whether the contribution is a sharp advance on the turbulence side or mainly a recombination of existing ingredients.

12. **The paper’s strongest qualitative figure is useful, but it also exposes a gap in evaluation.**  
    The appendix visualization in **Figure 10** shows that FourierFlow indeed appears to preserve sharper density structures than the surrogate baseline over time, which is a point in the paper’s favor. But this also underscores a weakness of the main paper: such qualitative evidence never gets translated into quantitative flow-statistics analysis in the main text. The visuals suggest the authors know what physically relevant small-scale structures look like; the paper should therefore measure them explicitly rather than stopping at image-like error metrics.

## Questions
1. Please define the alignment loss \(\mathcal L_{\text{Align}}\) explicitly in the main paper. What exact features are aligned, at which layers, with what normalization or projection, and with what pointwise loss?

2. Can the authors provide physically meaningful evaluations in the main paper, not just in the appendix, such as kinetic energy spectra, enstrophy spectra, structure functions, or conservation/invariant statistics? This would substantially increase my confidence in the claims about “physical consistency” and “high-frequency turbulence fidelity.”

3. In Section 2.2, can the authors give a precise derivation of how the common-mode perturbation induces flattening of attention logits after softmax? Right now the rank-1-bias argument is too informal, and I am not convinced the claimed effect follows as stated.

4. In Equations (5) and (6), what is the exact neighborhood metric for \(\mathcal N(j)\), and how does that design implement the claimed local-versus-global decomposition? As written, \(\mathrm{Attn}_2\) seems neighborhood-restricted, which conflicts with the “broader background context” interpretation.

5. Please clarify the sentence around mode truncation in the Fourier branch. Are high-frequency modes actually preserved preferentially, or is the model still truncating to low modes as in standard AFNO/FNO-style operators? This is central to the method’s claimed mechanism.

6. Can the authors reconcile the split inconsistency between the “\(90\%\) training” statement below **Table 1** and the “\(80/10/10\)” split in Section 5.1? If different experiments use different splits, that should be stated clearly.

7. Can the authors report training and inference cost, including number of ODE/sampling steps and wall-clock comparisons against the strongest baselines in **Table 1**? The paper emphasizes efficiency advantages of flow matching, but this is not evaluated.

8. For the long-horizon analysis in **Figure 8**, can the authors compare against the strongest generative baselines, not only the surrogate baseline? That would make the generalization claim much more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses public simulation datasets and does not appear to involve human subjects, sensitive personal data, or direct deployment in high-risk decision-making settings. The broader-impact discussion is lightweight, but I did not identify an ethics issue that requires escalation.

## Soundness Rating
2: fair. The method is plausible and the experiments are fairly extensive, but several core claims, especially around physical fidelity, common-mode noise, and the theory-to-method connection, are not adequately supported in the main paper.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures help, but notation, loss specification, and several inconsistencies materially hurt clarity.

## Contribution Rating
2: fair. The problem is important and the empirical gains are promising, but the paper currently feels more like a somewhat loose combination of sensible components than a crisply justified contribution that is ready for ICLR acceptance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The empirical results are promising and the topic is important, but the current version does not support its physical and theoretical claims strongly enough, and too many key methodological details remain underspecified or inconsistently presented.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main technical claims, equations, figures, and tables, and the main reasons for my score are about support and clarity rather than lack of familiarity with the area.