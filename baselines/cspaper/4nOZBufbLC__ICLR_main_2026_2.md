---
job_id: ff372ee6-9c42-42d1-a5d0-ebb8354e6bfd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4nOZBufbLC.pdf
paper: Count Bridges Enable Modeling and Deconvolving Transcriptomic Data
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, it proposes a generative modeling framework for integer-valued data, develops bridge-based probabilistic machinery, and studies applications in biology with clear ML methodological content.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion; despite some overclaiming and several clarity/theory issues, it clears the bar for a full review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions aimed at automated reviewers, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces Count Bridges, a stochastic bridge process on integer lattices based on Poisson birth-death dynamics, intended as a discrete/count-native analogue of diffusion-style generative modeling. The paper derives closed-form bridge conditionals for training and sampling, uses a distributional denoising objective based on proper scoring rules, and extends the framework to aggregate-supervised deconvolution via a projection-guided EM-style procedure. Experiments cover synthetic integer transport benchmarks and two biological applications, bulk RNA-seq deconvolution and spatial transcriptomics deconvolution into single-cell count profiles.

## Strengths
1. The core modeling idea is interesting and well matched to the data type. Treating counts through birth-death dynamics rather than as unordered categories is a sensible design choice, and the bridge construction in **Section 3.1** is one of the stronger aspects of the paper. In particular, the use of latent slack variables and the resulting Binomial/Hypergeometric sampling structure in **Equation 9** gives a tractable reverse kernel rather than an approximate heuristic.

2. The paper does a good job of connecting the proposed construction to the bridge/diffusion perspective from **Section 2**. The analogy between the Gaussian bridge in **Equation 5** and the count bridge in **Equations 8-9** helps situate the method conceptually. Even if some theoretical claims are stated too strongly, the high-level connection is meaningful and likely useful to researchers thinking about non-Euclidean generative modeling.

3. The synthetic empirical results are strong and fairly consistent. **Figure 2** is a useful qualitative comparison: CFM trajectories look noisy and geometrically misaligned after discretization, DFM captures some structure but appears less faithful to the transport geometry, while the Count Bridge samples are visibly closer to the target moons. This qualitative impression is supported by **Table 6**, where Count Bridge (ES) outperforms CFM, DFM, and Count Bridge trained with MSE on MMD, \(W_2\), and Energy. The gap is not just cosmetic.

4. The scaling experiment is another real plus. **Figure 3** and **Table 9** jointly show that Count Bridges remain substantially better than CFM/DFM across ambient dimensions up to 512. The table is particularly informative because it reports multiple NFEs. The fact that Count Bridge is not only better at high NFE but also competitive at very low NFE strengthens the claim that the exact bridge structure is practically useful rather than merely elegant on paper.

5. The biological applications are ambitious and broader than a standard toy-paper evaluation. On the PBMC sequence-to-expression task, **Table 1** shows a substantial reduction in bulk and cell-type-specific MSE relative to the fine-tuned Enformer baseline. On deconvolution, **Table 3** reports better JSD/RMSE/Spearman than CIBERSORTx and MuSiC. Even with caveats about task comparability, these are meaningful application results.

6. The spatial transcriptomics experiment also gives the paper practical relevance. **Tables 4 and 5** show gains over STDeconvolve for cell-type proportion recovery and over the spot-mean baseline for count-profile reconstruction. I also appreciated that the paper is explicit that STDeconvolve outputs proportions rather than profiles, which avoids one common apples-to-oranges comparison issue.

7. The visual diagnostics in **Figure 1** are helpful. The right panel, comparing one-step and two-step ECDFs, directly illustrates the claimed composition property, and is more convincing than a purely verbal explanation would be. The left and middle panels also provide some intuition for why the slack posterior behaves sensibly as endpoint displacement grows.

## Weaknesses
1. The main theoretical story is promising, but the exposition and level of rigor in the main paper are not fully convincing enough for some of the stronger claims. In **Proposition 3.1** on **Pages 3-4**, the paper states that the family \(\{K_{s|0,t}\}\) satisfies **Equations 1 and 2**, but the main text gives only a high-level sketch and pushes all critical details into the appendix. Normally that is acceptable for standard technical lemmas, but here this proposition is the backbone of the paper. Since the method’s appeal rests heavily on “exact, tractable analogue of diffusion-style models,” the paper would benefit from stating more precisely in the main text what the observable bridge kernel is, how the slack posterior is marginalized, and why the posterior/projectivity property in **Equation 2** follows. As written, the reader is asked to trust a lot of hidden machinery.

2. Related to that, the notation around kernels is more slippery than it should be. In **Section 2**, the paper uses \(K_{t|0}\), \(K_{s|0,t}\), and then \(K_{s|t}\) in **Equations 1-3**, but the relationship between the unconditional process, the bridge conditioned on \((X_0,X_t)\), and the reverse kernel conditioned only on \(X_t\) is not always kept clean. This becomes more problematic in **Section 3.1**, where **Proposition 3.1** says “The family \(\{K_{s|0,t}\}\) defined by equation 8 satisfies equations 1 and 2,” even though **Equation 8** itself only gives the conditional form with latent \(B_s,D_s\), while the actual observable bridge depends on sampling \(M_t\mid d_t\). The distinction between the fixed-slack bridge and the marginalized bridge is essential; in the main paper it is blurred.

3. The claim in **Section 3.1** that “Count Bridges are an instance of the static Schrödinger bridge problem” is too breezy for the amount of caveat it needs. The text on **Page 4** moves from the slack concentrating near zero for large \(|d_t|\) to an entropy-regularized OT interpretation. But concentration of slack in one regime is not what establishes a Schrödinger bridge characterization in general. The actual justification, as I understand it from the appendix, comes from the KL projection to the reference coupling, not from the empirical observation in **Figure 1**. The current presentation risks mixing intuition with theorem statement in a way that overstates what has been shown in the main text.

4. The deconvolution extension in **Section 4** is the least convincing part of the paper methodologically. The proposed E-step does not sample from the true aggregate-conditional posterior \(Q_\theta(\mathbf{X}_0\mid a_0,x_t,t,z)\); instead it runs the reverse process while repeatedly projecting predicted endpoints using \(\Pi\), see **Algorithm 3** on **Page 6**. This may be a pragmatic approximation, but the paper sometimes talks as if it were a principled EM procedure rather than an approximate projection-guided heuristic. The authors do acknowledge in the conclusion that the projection step “lacks serious theoretical support,” and I appreciate that honesty, but that caveat should appear earlier and more prominently because it affects how strongly one should interpret the deconvolution claims.

5. **Proposition 4.1** on **Page 6** is underspecified in the main paper. The statement invokes “regularity conditions in App. B.1,” a “first-order exponential tilt,” and a “generalized KL projection,” but the object \(D_{\mathrm{KL}}(\mathbf{y}_0\|\mathbf{x}_0)\) is not defined in the main text, and the projection formula \(\Pi(x_0)_g = a_0 x_{g0}/\sum_{g'}x_{g'0}\) is written as if it were automatically suitable for count-valued latent variables. In reality, this lives in a relaxed continuous space and then requires rounding. That rounding step is not a side issue, because exact aggregate satisfaction after projection depends on it. The appendix apparently discusses this, but from the main paper alone the projection-based conditional sampler is not adequately specified.

6. There is a mismatch between the stated motivation for modeling count distributions jointly and the actual parameterizations used in some applications. In **Section 3.2**, the paper argues that cross-entropy “cannot model the joint of \(X_s\mid X_t\) without exponential cost in dimension” and promotes scoring-rule training as a way to model the joint. However, in the PBMC application on **Page 9**, the model ends with “a final softmax head that parameterizes the conditional count distribution \(X_0|X_t,t,z\).” In the appendix, the sequence model also seems to use per-position parameterization plus ancestral decoding. That is not necessarily wrong, but it weakens the rhetorical contrast between “joint distributional modeling” and factorized heads. The paper needs to be much clearer about where the joint actually comes from, versus where it is only approximated through sampling plus a proper score.

7. The experimental baselines are good in places, but uneven overall. On the synthetic transport tasks the comparisons to CFM and DFM are reasonable, but for deconvolution the baseline landscape is thinner than it should be, especially on the spatial task. In **Section 6.3**, the main comparison is to STDeconvolve plus a spot-mean baseline. That is a low bar for a paper making broad claims about “reference-free spatial transcriptomic deconvolution.” Even within the paper’s own framing, the field has several stronger spatial deconvolution methods, and the main-text comparison set feels curated for a favorable story. This matters because deconvolution quality is heavily benchmark-dependent.

8. The biological evaluations are promising but not always easy to interpret scientifically. For bulk RNA-seq deconvolution, **Table 2** is oddly labeled and compressed on **Page 9**, and it is unclear what exact “Comparison” column entries “Bulk mean” and “Count Bridge” are meant to represent as methods rather than references. More importantly, the reported distributional metrics, MMD/\(W_2\)/Energy, depend strongly on the representation space and sample construction, yet the main text gives little intuition for what magnitude differences mean in biological terms. Similarly, in spatial deconvolution the conversion from predicted count profiles to nearest-neighbor cell types is a major evaluation choice, but the main text spends little time on how sensitive results may be to that assignment procedure.

9. Some tables and figure references are confusing enough to hurt presentation and confidence. On **Page 9**, **Table 1** and **Table 2** are merged awkwardly in the text and captions, making it hard to parse which quantities belong to which experiment. On **Page 10**, **Table 4** appears after the surrounding paragraph has already discussed it, and the formatting again feels rough. These are not just cosmetic issues; when the paper presents many application claims, readers need very clean tables to verify what is being compared.

10. The paper’s positioning against prior count-specific generative modeling is not fully convincing. The related work section discusses Blackout Diffusion and general discrete diffusion frameworks, but the novelty claim would be stronger if the paper more explicitly clarified what is new relative to prior Markov-generator-based discrete generative models and recent distributional diffusion works. Right now, part of the contribution is a mathematically tailored count bridge, part is using scoring-rule denoising, and part is the aggregate-supervised projection/EM recipe. These ingredients are interesting together, but the paper could do a better job separating “new bridge construction” from “adapting existing distributional training ideas” from “application-driven engineering.”

11. There are also smaller but still important mathematical clarity issues in **Section 3.2**. The loss is written as
\[
S_{\rho}(p,y)=\frac12\mathbb{E}_{X,X'\sim p}[\rho(X,X')] - \mathbb{E}_{X\sim p}[\rho(X,y)]
\]
and then
\[
\mathcal{L}(\theta)=\mathbb{E}_{X_0,X_t,t}[S_p(q_\theta(\cdot\mid X_t,t),X_0)].
\]
This appears to be a typo, since the score is defined as \(S_\rho\) but the objective uses \(S_p\). More substantively, the paper says strict propriety holds when \(\rho\) is characteristic, while earlier it asks only for a negative-type semimetric and later states experiments use \(\rho(x,x')=\|x-x'\|_2^\beta\) with \(\beta=1\). The exact conditions under which this score is strictly proper on \(\mathbb{Z}^D\) should be stated cleanly in the main paper, because the training objective is central, not peripheral.

12. The identifiability discussion is somewhat self-contradictory in how prominently it is used. The paper correctly notes in the conclusion and appendices that deconvolution becomes ill-posed for large groups or weak heterogeneity, and **Figure 4** nicely shows degradation with group size and Dirichlet concentration. That figure is actually one of the more honest parts of the paper. But in the main narrative, the deconvolution framework is still presented a bit too generally, even though the conditions under which aggregate supervision can identify unit-level counts are narrow and rely on side information or cross-group heterogeneity. This matters scientifically because without those caveats front and center, readers may overgeneralize the method’s applicability.

## Questions
1. For **Proposition 3.1** and the reverse sampling procedure in **Algorithm 2**, can the authors state explicitly in the rebuttal what the observable kernel \(K_{s|0,t}\) is in closed form after marginalizing over the slack variable, and clarify whether **Equation 9** is a sampling recipe only or also a tractable pmf/evaluable kernel? This would significantly increase my confidence in the “exact bridge” claim.

2. In **Section 3.2**, please clarify the conditions under which the chosen energy score is strictly proper for the distributions considered here. Is the intended statement that \(\rho(x,x')=\|x-x'\|_2^\beta\) with \(0<\beta<2\) induces a characteristic kernel / negative type on \(\mathbb{Z}^D\), or is some weaker result sufficient? Also please confirm whether the appearance of \(S_p\) instead of \(S_\rho\) is a typo.

3. For the deconvolution method in **Section 4**, how should one think about the objective that the projection-guided E-step is actually optimizing? If it is not a proper EM lower bound, can the authors characterize it as approximate posterior sampling, projected reverse diffusion, or something else? A sharper statement of what is and is not guaranteed would materially improve the paper.

4. Can the authors clarify the exact rounding/projection procedure used in the main deconvolution experiments, especially for the real-valued scaling projection from **Proposition 4.1**? Since aggregate preservation is central, I would like the rebuttal to specify whether exact groupwise rounding was always used in the main results or only in selected experiments.

5. Regarding **Table 2** and **Table 3** on **Page 9**, please explain more clearly what the “Comparison” entries represent and how the deconvolved profile metrics are computed. Are these metrics computed between empirical distributions over predicted cells and true cells within each held-out donor, or in some pooled setting? This is important for interpreting the reported gains.

6. For the spatial transcriptomics results in **Tables 4 and 5**, can the authors discuss how sensitive performance is to the nearest-neighbor assignment used to convert predicted count profiles into cell-type proportions? If a different classifier or atlas is used, do the relative rankings remain stable?

7. The sequence-to-expression application is intriguing, but it is not fully clear why taking the maximum over nucleotide-level coverage to derive gene counts is the right aggregation. Please explain the motivation for this choice and whether the gains in **Table 1** remain under alternative gene-level aggregation schemes.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses de-identified public biological datasets and presents the models for research use. While deconvolution methods can in principle raise privacy questions, I did not see a paper-specific ethics issue requiring escalation beyond the standard considerations already acknowledged by the authors in the ethics statement on **Page 11**.

## Soundness Rating
3: good. The core bridge construction appears technically meaningful and the empirical evidence is substantial, but several central claims, especially around projective exactness in the main text and the aggregate-supervised EM/projection procedure, are not presented with enough precision for a higher score.

## Presentation Rating
2: fair. The main ideas are interesting, but notation is occasionally slippery, some mathematical definitions are underspecified in the main paper, and multiple tables/figures, especially **Tables 1-5**, are awkwardly formatted or insufficiently explained.

## Contribution Rating
3: good. The paper makes a valuable contribution by introducing a count-native bridge model and pushing it into biologically relevant deconvolution settings, even if some pieces are more incremental or heuristic than the framing sometimes suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real method contribution, strong synthetic results, and compelling applications, but it also has nontrivial weaknesses in theoretical sharpness, clarity, and the justification of the deconvolution extension. I lean positive because the core idea is useful and the results are stronger than the presentation.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant generative-modeling/discrete-modeling literature, though some biology-specific evaluation choices are outside my deepest area of expertise.