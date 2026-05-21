---
job_id: f8757442-cf33-4de1-acfe-c0ed9b970932
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VgVeQpagf7.pdf
paper: High Performance Differentially Private Fine-Tuning Using Dataset Distillation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining differential privacy, synthetic data generation, dataset distillation, transfer learning, and image classification.

## Minimum Quality
Pass ✅. The paper includes the required scientific components, namely abstract, introduction, background/related work content, method, experiments, quantitative and qualitative results, and discussion/conclusion. While there are notable technical and experimental weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to reviewers/LLMs, or other suspicious text embedded in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes SPS and SPS+, two methods for generating differentially private synthetic datasets for image classification by adapting dataset distillation, specifically D3S, to the DP setting. The core idea is to privatize layerwise activation summary statistics computed from a public pretrained model, then synthesize images that match these privatized global and class-conditional Gaussian summaries. The paper reports results on CIFAR-10, CIFAR-100, and CAMELYON17, arguing that SPS+ can match or exceed strong DP-SGD baselines while offering extra flexibility such as ensembling, federated aggregation, and continual reuse of the privatized synthetic data.

## Strengths
1. The paper tackles an important problem. Replacing repeated DP-SGD training with a one-time DP synthetic data release is a practically meaningful direction, especially because the post-processing flexibility is real and well articulated in Sections 1, 5.5, and 5.6.

2. The empirical headline on CIFAR-10/100 is strong. In **Table 1** on **Page 7**, SPS+ is shown to match or outperform the cited DP-SGD baseline across the tested privacy budgets, with the most striking gap on CIFAR-100 at $\epsilon=1$ and $\epsilon=2$. If these comparisons are fair, that is an interesting result for the private vision community.

3. The paper does a decent job motivating why activation-statistic matching is a better fit for DP than iterative DD approaches. The argument in **Section 2.3** and the construction in **Equation (4)** make clear that privacy is only paid during summary release, not during the image optimization itself. That distinction is central and scientifically relevant.

4. The proposed method contains several concrete engineering ideas that appear useful in practice: class/global statistic separation, rescaling to redistribute noise, multistage clipping, and grouped pseudo-classes. Even though some of these are heuristic, the ablations suggest they matter. In particular, **Table 8** on **Page 23** shows that grouped pseudo-classes and multistage clipping substantially improve over basic SPS, especially on CIFAR-100.

5. The visual narrative is helpful. **Figure 1** on **Page 3** gives an intuitive overview of the summarize-privatize-synthesize pipeline and clarifies where privacy is applied. **Figure 2** on **Page 7** is also useful because it shows the role of the number of clipping stages $M$ and the gap between single-model and ensemble evaluation, rather than only reporting a single cherry-picked point.

6. The paper highlights a legitimate advantage of data release over private model release. The discussion around ensembling is supported in **Table 1**, where the ensemble gains are nontrivial and, by construction, do not consume additional privacy after data release. That practical distinction from DP-SGD is well made.

7. The CAMELYON17 result in **Table 2** is a nice attempt to test domain mismatch between public pretraining data and private target data, which is an important use case for private fine-tuning.

## Weaknesses
1. **The mathematical presentation is sloppy enough that it undermines confidence in the method description.**  
   There are many notation inconsistencies and probable mistakes in the main text, not just in the appendix pseudocode. For example, in **Page 4**, the projection matrices are said to have dimensions $\mathbb{R}^{D_G \times D_1}$ and $\mathbb{R}^{D_C \times D_I}$, which appears inconsistent with the earlier notation for the channel dimension of $z_{i,l}$. In **Equation (3)** on **Page 5**, the notation $z_{i,l}^{\intercal G}$ and $z_{i,l}^{\intercal c}$ is malformed, and the meaning of the outer product before spatial averaging is not cleanly specified. In **Section 3.2.4** on **Page 6**, the rescaling formula defines
   \[
   S=\frac{L D_G^{\text{layer}}}{|L_C|D_C^{\text{layer}}},
   \]
   but then the clipping norm is written using $D_G^{\text{layer}}$ again in the class term,
   \[
   |v|_{\max}=K_{\text{clip}}\sqrt{L D_G^{\text{layer}} + S |L_C| D_G^{\text{layer}}}=K_{\text{clip}}\sqrt{2L D_G^{\text{layer}}},
   \]
   which looks dimensionally suspicious and likely should involve $D_C^{\text{layer}}$. This is not cosmetic, because the privacy guarantee depends on the exact sensitivity bound. When the core DP accounting hinges on these formulas, unclear notation is a serious issue, not a formatting nit.

2. **The privacy theorem is too thin relative to the complexity of the proposed pipeline.**  
   **Theorem 4.1** on **Page 7** gives a simple Gaussian-mechanism RDP bound for releasing $\tilde v$, but the actual algorithm includes stage-wise recentering, pseudo-class regrouping, deterministic post-processing from previous synthetic images, eigenvalue clipping, and potentially multiple models/stages. The theorem essentially says, “each release is Gaussian, therefore compose $M$ times.” That part is fine as far as it goes, but the paper does not clearly and rigorously connect the exact implemented SPS+ pipeline in **Sections 4.1 and 4.2** to the theorem statement. In particular, the statement says “for $M$ models” while the text in **Section 4.1** defines $M$ as the number of clipping stages, which is conceptually different. This variable overload is easy to gloss over, but it matters for understanding what exactly is being composed.

3. **The normalization for class-conditional statistics appears unjustified under class imbalance, yet the paper evaluates only balanced datasets and does not discuss the bias formally.**  
   In **Section 3.2.3** on **Page 5**, the class-specific statistics are normalized by $\frac{N}{C}$. That is only appropriate if classes are balanced or if the goal is to estimate a rescaled class statistic under an explicit balancing convention. The paper later acknowledges in **Section 6** that it focuses on the “simpler class-balanced setting,” but this assumption is doing nontrivial work inside the estimator itself. Since the contribution is framed fairly broadly as a DP synthetic data method for classification, the dependence on balanced classes should be foregrounded much more clearly in the method section, not deferred to limitations. Otherwise, readers may incorrectly assume the estimator is generally applicable.

4. **The experimental comparisons are narrower than the claims suggest.**  
   The title and abstract position the work as a high-performance alternative to DP-SGD using dataset distillation, and the introduction makes a strong “first alternative to DP-SGD that attains higher accuracy on image-classification tasks” claim. However, the main experimental section mostly compares against one gradient-based baseline and one generation-based baseline. **Table 1** on **Page 7** is compelling against the cited DP-SGD result from De et al. (2022), but it is still one baseline family, and the main text relegates broader comparison to the appendix. For a paper staking out “first to match or exceed” territory, I would expect a more comprehensive main-paper benchmark table covering more private synthetic-data competitors and, ideally, stronger fidelity/utility tradeoff comparisons. As written, the empirical case is strong but still narrower than the framing.

5. **The paper leans heavily on post-processing flexibility, but some downstream comparisons are not apples-to-apples.**  
   The paper correctly argues that once the synthetic data are released, one can use GSAM, larger downstream models, and ensembling “for free” in privacy terms. That is true. The issue is interpretive: some of the strongest numbers in **Table 1** come from ensembles and larger downstream architectures that the DP-SGD baseline does not match. The table includes both single-model and ensemble results, which is good, but the abstract headline also emphasizes the best ensemble numbers, for example 96.2/76.6 at $\epsilon=1$. Those are valid outcomes of the pipeline, but they are not the cleanest direct evidence that the synthetic-data mechanism itself is intrinsically better than private training. The fairest apples-to-apples comparison is the single-model setting, and there the advantage is present but smaller, especially on CIFAR-10.

6. **The role of hyperparameter tuning under privacy is under-discussed, and some choices look tailored.**  
   The paper emphasizes that synthetic data allow post hoc flexibility without extra privacy cost, which is true after the release. But the measurement pipeline itself still has many choices: $D_G$, $D_C$, $L_C$, $K_{\text{clip}}$, number of pseudo-classes $P$, number of stages $M$, and optimizer details. The appendix claims some parameters were chosen “rather arbitrarily” and not tuned, but **Table 10** on **Page 24** shows different $[D_G, D_C]$ values across privacy budgets and tasks. Similarly, **Figure 2** on **Page 7** highlights that $M$ matters materially. This makes it harder to tell how much tuning occurred on the private tasks and how robust the method is out of the box. The authors should be much more explicit about what was selected using validation, what was transferred unchanged, and whether test performance influenced the chosen defaults.

7. **The claims around grouped pseudo-classes are intuitively plausible but theoretically underspecified.**  
   **Section 4.2** says the method improves optimization because each pseudo-class estimate has a more favorable noise rate and that the benefit arises due to the KL objective, covariance inversion, and eigenvalue clipping, not because it improves direct mean estimation. This is interesting, but the paper does not formalize the mechanism. For example, if the pseudo-class assignment matrix $\mathbf P$ is random, what is the optimization target exactly, and under what conditions does matching pseudo-class statistics recover class-separating synthetic samples rather than entangled mixtures? The appendix says recovery is possible if $\mathbf P$ is invertible, but the main method does not actually describe an inversion step during optimization. Right now this part reads like a clever heuristic that works, but the paper sometimes writes as if the effect were better understood than it is.

8. **The paper reports image quality qualitatively, but the fidelity story is mixed and not fully confronted.**  
   **Figure 4** on **Page 8** shows CIFAR-100 synthetic images becoming more recognizable as $\epsilon$ increases, which supports the intuitive privacy-utility trend. **Figure 3** on **Page 8** also shows the expected inverse relationship between FID and accuracy. However, the appendix later notes that SPS/SPS+ are not competitive with pre-trained-generator methods in FID. That is an important nuance, because the paper markets synthetic data as an inspectable and reusable release. If the data have relatively weak visual fidelity, that affects some advertised use cases. This does not kill the paper, but the main text should discuss more directly that “classification utility” and “distribution realism” are not aligned here, and that the method seems much stronger on the former than the latter.

9. **Some of the broader systems-style claims are demonstrated only lightly.**  
   The paper says SPS supports federated learning and continual learning without modification. The idea is sensible, and **Figure 5(c-e)** on **Page 9** provides encouraging curves. Still, these sections are more proof-of-concept than comprehensive evaluation. For example, the federated experiment in **Section 5.5** uses a simple partition of CIFAR-10 into five subsets of equal size, and the continual-learning experiment in **Section 5.6** reports one representative gap to standard training but does not compare against stronger privacy-aware continual-learning baselines. These sections are nice bonuses, but they should not be oversold as fully established advantages.

10. **Presentation quality drops substantially in the appendix, and this spills back onto trust in the main claims.**  
    I am not supposed to judge the paper based on the appendix alone, but the appendix pseudocode is riddled with malformed equations, indexing issues, and likely copy-editing corruption. When I see that, I become less confident that the main-text formulas were checked carefully. Given that this is a DP paper where the details of clipping, normalization, and composition matter a lot, the lack of crisp formalism is more concerning than it would be in a purely empirical vision paper.

## Questions
1. In **Section 3.2.4**, can the authors give a precise derivation of the sensitivity after class-rescaling, including the corrected formula for $|v|_{\max}$ if there is a typo? This is important because the privacy accounting rests directly on that bound.

2. In **Section 4.1**, what exactly is being composed in **Theorem 4.1**: stages, models, or both? Please rewrite the theorem and variable names so the accounting matches the actual SPS+ pipeline unambiguously.

3. For the class-specific post-processing on **Page 5**, why is normalization by $\frac{N}{C}$ appropriate? Is the method assuming exactly balanced classes, approximately balanced classes, or is this a deliberate reweighting choice? A short derivation would help.

4. How were the hyperparameters in **Tables 9 and 10** chosen in practice? Which of them were fixed before seeing private-task test performance, and which, if any, were adjusted per dataset/privacy budget using validation signals?

5. Can the authors provide a more direct apples-to-apples comparison against DP-SGD using the same downstream architecture and no ensembling in the headline discussion? **Table 1** already contains much of this, but the narrative emphasizes the strongest ensemble results.

6. For grouped pseudo-classes, can the authors clarify the mechanism by which random grouped statistics drive separation between the original classes during synthesis? Even a simplified analysis or controlled ablation varying $N_{c/p}$ and $P$ would increase confidence here.

7. Since **Figure 3** and **Figure 4** suggest a utility-fidelity tradeoff, can the authors comment more explicitly on which intended use cases require realistic images versus merely classifier-useful images? This would help calibrate the claimed practical benefits of releasing the synthetic data.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies differential privacy and private image classification, and the evaluated datasets/tasks are standard ML benchmarks and medical image classification benchmarks. Based on the main paper, I do not see a distinct ethics flag requiring escalation beyond the usual privacy considerations already central to the work.

## Soundness Rating
2: fair. The core idea is plausible and the empirical results are interesting, but the mathematical presentation, privacy-accounting exposition, and some methodological assumptions are not clean enough for a higher score.

## Presentation Rating
2: fair. The high-level story is understandable and several figures/tables are helpful, but notation is inconsistent, some equations are underspecified, and the formal presentation is much rougher than it should be for a DP paper.

## Contribution Rating
3: good. The paper asks an important question and presents a practically meaningful alternative to DP-SGD with strong results, but the contribution is held back by incomplete positioning and weak formal clarity around key components.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The empirical results are genuinely interesting, and the paper has a clear practical angle. However, for an ICLR main-track acceptance, I want a cleaner and more trustworthy technical presentation, especially around the exact statistic construction, sensitivity bound, normalization choices, and privacy accounting. Right now the paper feels stronger as a promising empirical system than as a fully nailed-down scientific contribution.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant DP/representation-learning context, though I cannot fully verify every intended formula because some of the notation and pseudocode are too inconsistent.