---
job_id: 930fa38a-6ffa-4396-a2d7-bb5cb539f6cb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: a4S1nQay3b.pdf
paper: Uncover Underlying Correspondence for Robust Multi-view Clustering
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies unsupervised representation learning and probabilistic/generative modeling for robust multi-view clustering.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, presents a concrete method with equations and experiments, and provides substantial empirical evidence, although there are several technical and presentation issues that should be addressed.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies multi-view clustering under noisy correspondence and argues that existing contrastive formulations are brittle because they rely too heavily on predefined positive and negative pairs. The proposed method, CorreGen, replaces the discriminative pairwise objective with a generative latent-correspondence view, optimized by an EM-style procedure where the E-step estimates soft cross-view correspondences using OT with GMM-guided marginals and a virtual sample for outliers, and the M-step updates the encoder by maximizing the expected log-likelihood. Experiments on four datasets with synthetic mismatch/corruption and one realistic image-text dataset show consistent gains over several recent robust MVC baselines.

## Strengths
1. The paper targets a practically relevant failure mode in multi-view clustering. The distinction between category-level mismatch and sample-level mismatch is useful, and the motivation in **Figure 1** is effective. In particular, the contrast between pairwise reweighting, pairwise realignment, and the proposed “correspondence generation” paradigm helps clarify what the authors are actually changing conceptually, not just algorithmically.

2. The main modeling idea is interesting. Recasting noisy correspondence handling as latent correspondence estimation under a joint likelihood, instead of directly repairing positives/negatives inside an InfoNCE-style loss, is a meaningful shift in viewpoint. The use of soft many-to-many assignments is well aligned with clustering semantics, where same-class cross-view matches need not be one-to-one.

3. The method integrates several components in a coherent way. The EM decomposition in **Section 3.2**, OT-based joint estimation in **Eq. (11)**, GMM-guided marginals in **Eq. (13)-(14)**, and the virtual sample mechanism in **Eq. (12)** fit together around the central idea of discovering latent correspondences while discounting noise. **Figure 2** is helpful here; it gives a readable overview of how the E-step and M-step interact.

4. The empirical results are strong and broad enough to matter. In **Table 1**, the gains on Caltech101 and especially UMPC-Food101 are substantial across all mismatch ratios. For example, under 50% mismatch on UMPC-Food101, the proposed method reaches 42.57 ACC versus 28.80 for CANDY and 25.21 for DIVIDE, which is a fairly large gap for this literature. The robustness trend is also convincing on Caltech101, where the method remains much more stable than baselines as MR increases.

5. **Table 2** further supports the claim that the virtual-sample and marginal design are useful when both alignable and unalignable mismatch are present. The method degrades more gracefully than the baselines across the combined MR/CR settings, which is exactly the stress regime the paper claims to address.

6. The posterior visualization is genuinely informative. **Figure 3** is one of the more convincing qualitative pieces in the paper, because it shows that the estimated posterior starts near an instance-aligned structure during warmup and gradually becomes block-structured in a way that resembles the class-level ground truth. This directly supports the paper’s claim that the method recovers category-level relations rather than merely denoising pairs.

7. The ablation in **Table 3** is directionally sensible. It shows that both the virtual sample and GMM-guided marginals contribute, and that replacing the proposed objective with vanilla InfoNCE hurts more under noisy settings than under clean ones. That pattern is consistent with the central thesis of the paper.

## Weaknesses
1. The probabilistic formulation is not fully clean, and some equations are more suggestive than rigorous. The most noticeable issue is the transition from **Eq. (2)** to **Eq. (3)** on **Pages 4-5**. In Eq. (2), the objective is a sum of single-view marginals, $\sum_{v,i}\log p(x_i^{(v)};\theta)$, but Eq. (3) turns this into a sum over view pairs and latent matches, $\sum_{v_1,i,v_2}\log\sum_j p(x_i^{(v_1)},x_j^{(v_2)};\theta)$. This is not an obvious reformulation of Eq. (2); it appears to change the objective rather than derive it. If this is intended as a modeling assumption, it should be stated explicitly. As written, the paper presents it as a reformulation, which is mathematically shaky and matters because the entire EM derivation rests on this transition.

2. The EM derivation uses notation that obscures the actual latent variable structure. In **Eq. (5)-(8)**, the auxiliary distribution is written as $Q(x_j^{(v_2)})$, independent of $i$, but the text then says the bound is tight when $Q(x_j^{(v_2)}) = p(x_j^{(v_2)}; x_i^{(v_1)}, \theta)$, which is clearly conditional on $i$. This is not a cosmetic issue. In standard EM, the variational distribution should be indexed per observation, i.e., something like $Q_i(j)$ or $Q(j \mid i)$. Without that indexing, **Eq. (6)-(8)** is formally inconsistent. The authors likely know what they mean, but for a paper whose core contribution is an EM-based generative formulation, the notation needs to be precise.

3. The claimed convergence story is overstated relative to the actual algorithm used. The appendix proves monotonicity for an idealized EM objective in **Eq. (36)-(39)**, but the implemented E-step is not the exact posterior from the model. Instead, it uses OT with GMM-guided marginals and a virtual sample, and the M-step uses the normalized similarity surrogate in **Eq. (17)**. Once the E-step and M-step are both approximate in this way, the standard EM monotonicity argument does not automatically apply. So the “convergence” discussion is, at best, a heuristic transfer from exact EM to an approximate procedure. This should be toned down or clarified. The empirical plot in **Figure 7** is fine as evidence of training stability, but it does not validate the theoretical monotonicity claim for the actual algorithm.

4. The marginal estimation in **Eq. (13)-(14)** is under-justified and potentially problematic as a probability model. The paper calls $p(x_i^{(v)};\theta^{(t)})$ a marginal probability, but the formula
\[
p(x_i^{(v)};\theta^{(t)}) = \frac{m^{d_i}-1}{m-1}\cdot \frac{N_c}{N}
\]
does not appear normalized across samples, nor is it shown that $\sum_i p(x_i^{(v)}) = 1$. Since these quantities are later used as OT marginals in **Eq. (11)** and **Eq. (12)**, normalization is not optional. If there is an implicit normalization step, it should be written explicitly. If not, the feasibility set $\Pi(p^{(v_1)}, p^{(v_2)})$ is ill-defined. This is one of the most important technical clarifications needed.

5. The reduction to InfoNCE in **Proposition 2 / Eq. (19)** is conceptually plausible but mathematically imprecise. Starting from **Eq. (18)**, the denominator in the joint model of **Eq. (17)** sums over all $(m,n)$ pairs, whereas the InfoNCE denominator in **Eq. (19)** sums only over $n$ for a fixed anchor $i$. The appendix works around this by switching to a conditional factorization in **Eq. (32)-(34)**, but then the paper should be explicit that the equivalence is obtained after changing the parameterization from joint to conditional likelihood. As written in the main paper, “Eq. (8) reduces to standard InfoNCE” is too quick. This matters because the claim is used to position the proposed method as a strict generalization of InfoNCE.

6. The computational cost and scalability are not adequately discussed in the main paper. The E-step requires computing an $N \times N$ similarity/correlation matrix and solving Sinkhorn-style updates on the augmented transport plan. Even if this is done in mini-batches, the method seems significantly heavier than the contrastive baselines, especially for large datasets such as UMPC-Food101. The implementation note on **Page 8** says re-alignment is done within batches of 512 for fairness, but the paper does not report runtime, memory, number of Sinkhorn iterations used in the main runs, or sensitivity of performance to batch size. For a method that may be adopted in practice, this omission is not minor.

7. The empirical comparison is strong, but its fairness is still not fully transparent. The proposed method is implemented on top of DIVIDE, while it is not fully clear whether all baselines use equally strong backbones, augmentations, and optimization settings under the noisy-correspondence protocol. This is especially relevant because some results in **Table 1** are surprisingly poor, for instance ROLL on Caltech101 at 0% MR is dramatically below most baselines. That may be correct, but when one recent baseline collapses this badly in a nominally clean setting, it raises the question of whether hyperparameters or training details were carefully tuned for each method. More transparency in the main paper would help.

8. Some experimental presentation choices make the tables harder to interpret than necessary. In **Table 2** on **Page 10**, the setting labels are ambiguous, with repeated “MR 0.2” and “MR 0.5” blocks but no clearly printed CR values in the left-most column. From the surrounding text one can infer that multiple MR/CR settings are shown, but the table should state them explicitly. Since this table is central to the claim about handling both alignable and unalignable mismatch, the formatting should be fixed.

9. The paper’s treatment of category-level mismatch is partly definitional rather than fully empirical. The claim that category-level mismatch is pervasive is mathematically illustrated in **Appendix H**, but the main experimental sections mostly vary sample-level mismatch via MR and CR. **Figure 3** is a nice qualitative demonstration, but the main paper stops short of a more direct quantitative evaluation of category-level correspondence recovery, for example using the CAR metric that only appears in the appendix. Since category-level mismatch is one of the headline contributions, I would have liked at least one main-paper quantitative metric tied directly to that phenomenon.

10. There are a few exposition and consistency issues that, while not fatal, accumulate. The paper occasionally mixes semicolon notation and conditional notation for probabilities, for example $p(x_j^{(v_2)};x_i^{(v_1)},\theta)$ instead of the standard $p(x_j^{(v_2)} \mid x_i^{(v_1)},\theta)$ in **Eq. (8)-(9)**. **Eq. (16)** introduces the constant $A$ without explaining in the main paper how it should be chosen, while the appendix later says $A < \min S_{ij}$. Also, the warmup duration is inconsistent: the main **Figure 3(a)** is labeled “Warmup (10 epoch)” while **Appendix C** says the maximum warmup phase is 50 epochs. These are fixable, but the current version is not as polished as it should be for a method-heavy submission.

## Questions
1. Please clarify the exact relationship between **Eq. (2)** and **Eq. (3)**. Is Eq. (3) meant to be derived from Eq. (2), or is it a new modeling objective motivated by pairwise latent correspondences? A careful derivation, or an explicit statement that this is a modeling assumption rather than an equality, would materially increase my confidence.

2. In **Eq. (13)**, do the estimated marginals satisfy
\[
\sum_{i=1}^N p(x_i^{(v)};\theta^{(t)}) = 1?
\]
If yes, where is the normalization performed? If not, how is the OT feasible set in **Eq. (11)** defined in practice? This is a central technical point.

3. In the EM derivation, should the auxiliary distribution be written as $Q_i(j)$ or $Q(j \mid i)$ rather than $Q(x_j^{(v_2)})$? Please rewrite **Eq. (5)-(8)** with observation-specific indexing. If this is just notation, it is easy to fix, but the current form is formally inconsistent.

4. What is the exact complexity of one E-step as a function of batch size $B$, number of Sinkhorn iterations $t$, and number of views $V$? A short runtime or memory comparison against DIVIDE/CANDY/ROLL on at least one dataset would strengthen the practical case for the method.

5. Please explain more carefully the connection to InfoNCE. Is the claim that the proposed framework strictly contains InfoNCE under a conditional parameterization, or that **Eq. (18)** itself reduces to InfoNCE? A sharper statement would avoid over-claiming.

6. For **Table 2**, please make the MR/CR settings explicit in the table itself. As it stands, the repeated row labels are hard to parse, and that makes it difficult to assess how robust the method is under corruption specifically.

7. Could the authors report at least one direct quantitative metric for category-level correspondence recovery in the main paper, not just the visualization in **Figure 3**? Even a compact summary would help tie the empirical evidence more directly to the paper’s central conceptual claim.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work focuses on unsupervised clustering under noisy correspondence and uses standard benchmark datasets. The main practical concern is methodological robustness rather than downstream harm.

## Soundness Rating
3: good. The empirical evidence is strong and the core approach is reasonable, but several mathematical steps and probability definitions need clarification, especially around **Eq. (2)-(3)**, **Eq. (13)**, and the exact scope of the EM convergence claim.

## Presentation Rating
3: good. The paper is readable and the main intuition comes through, with **Figures 1-3** being particularly helpful, but the notation is sometimes sloppy and some key claims are presented more cleanly than they are actually derived.

## Contribution Rating
4: excellent. The problem formulation is important, the generative latent-correspondence perspective is a meaningful contribution beyond routine engineering, and the gains in **Tables 1-3** make the work valuable to the ICLR community.

## Overall Rating
8: Accept, good paper (poster). The paper makes a substantial contribution on an important robustness problem in multi-view clustering, and the empirical case is convincingly strong. I do have nontrivial reservations about the mathematical cleanliness of the formulation and some missing practical details, but these look fixable and do not overturn the central empirical claims.

## Reviewer Confidence
4: confident. I am familiar with the area and checked the main derivations and experiments carefully, though some implementation-level details and appendix-only claims would still benefit from author clarification.