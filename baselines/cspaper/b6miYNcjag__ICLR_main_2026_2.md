---
job_id: 66cad023-3cf4-45f9-bca6-5b91a7c41ef4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: b6miYNcjag.pdf
paper: Data Reliability Scoring
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is a learning-theoretic and methodological submission on dataset reliability scoring under unknown observation processes, with links to representation learning through the kernelized/image-embedding setting, so it fits ICLR scope.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, formal setup/method, theory, experiments, and conclusion; while I have substantial concerns about assumptions, positioning, and empirical support, these are review-level issues rather than desk-reject defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies dataset reliability scoring when the true labels are unobserved but auxiliary observations are generated from an unknown statistical experiment conditioned on the truth. The authors define several ground-truth-based reliability orderings, propose the Gram determinant score based on the determinant of a Gram matrix built from the joint reported-label/observation distribution, and prove preservation results under specific assumptions together with an experiment-agnostic ranking property and a uniqueness result up to scaling. Experiments are provided on synthetic categorical data, CIFAR-10 embeddings using a kernelized version, and a small real employment-data case study.

## Strengths
The paper has a clear and well-motivated problem statement. The question, how to score reliability of reported datasets without observing ground truth but with access to auxiliary observations, is interesting and different from the usual noisy-label or data valuation framing.

The formalization in Sections 2 to 4 is one of the stronger parts of the paper. In particular, introducing explicit target orderings such as exact match, Blackwell dominance, and distance-based orderings gives the paper a concrete benchmark for what a reliability score is supposed to preserve, rather than only presenting a heuristic score.

The core algebraic identity behind the method is elegant and easy to remember: from **Equation (4)** and the determinant multiplicativity used below **Theorem 4.2**, the score factors as
\[
\Gamma(PQ)=\det(P^\top P)\det(Q)^2.
\]
This cleanly separates the observation process from the misreport matrix in the partial-knowledge setting, and it explains the experiment-agnostic ranking claim in a compact way.

I also found the geometric intuition useful. **Figure 1** does a good job of illustrating the proposed score as a squared volume of a parallelepiped. This helps the reader understand why convex combinations induced by misreporting can shrink the volume. For a theory-heavy paper, that visualization is genuinely helpful.

The impossibility section is valuable conceptually. Even if some of the assumptions later become restrictive, **Proposition 3.1** at least explains why the authors need to narrow attention to linearly independent experiments and restricted classes of misreport matrices. That is preferable to quietly making strong assumptions without first showing why they may be needed.

The synthetic experiments in **Figure 2(a-c)** are aligned with the claims being made. In particular, **Figure 2(a)** shows the plug-in score decreasing with corruption level \(p\) across several corruption mechanisms, and **Figure 2(b-c)** support that larger scores correspond to lower Hamming and \(\ell_2\) error in that controlled setup. Even though these are not sufficient on their own, they are at least directionally consistent with the theory.

The image experiment is a reasonable attempt to connect the method to representation learning. Using SimCLR embeddings and a kernelized score is a natural way to instantiate the method when \(\mathcal Y\) is continuous.

## Weaknesses
1. **The main positive theory depends on quite restrictive assumptions, and the paper does not do enough to quantify how restrictive they are in practice.**  
   This is the central issue for me. The preservation result in **Theorem 4.2** requires linearly independent experiment columns, and for approximate distance preservation it further restricts to \(\mathcal Q_{L,1/(64L^2d^2)}\). That latter condition is extremely narrow: the allowed Hamming corruption rate is at most \(1/(64L^2d^2)\), which becomes tiny even for moderate \(d\). For example, when \(d=10\) and \(L=1\), this already gives \(\delta \le 1/6400\). Yet the experiments in **Section 5** evaluate corruption levels up to \(p=0.5\) in Experiment 1 and \(p=0.4\) in Experiment 2, far outside the regime in which the paper proves approximate distance-order preservation. So the theory and experiments are not really speaking to the same operating regime. This matters because the paper repeatedly presents the score as broadly useful for reliability assessment across diverse settings, but the formal guarantees only cover a very narrow subset of those settings.

2. **The uniqueness / experiment-agnosticity claim is mathematically interesting but narrower than the prose suggests, and the paper overstates its practical consequence.**  
   In **Proposition 4.3**, the uniqueness statement is formulated on \(GL_d\) and assumes a continuous score \(S:GL_d\to\mathbb R_{>0}\) together with a homogeneity condition \(S(tQ)=c(t)S(Q)\). This is a quite specialized functional class. Reported datasets in the actual problem need not induce invertible \(Q\), and many practical datasets, especially with imbalance or merged classes, will sit outside \(GL_d\). So while the proposition is fine as a mathematical statement, it does not establish that the Gram determinant is the unique practically relevant experiment-agnostic reliability score over the space of actual datasets studied in the paper. The manuscript repeatedly phrases this as “uniquely up to scaling” in the abstract and introduction, which reads broader than what is actually proven on **Page 7**. The scope of the claim should be narrowed much more explicitly.

3. **The detail-free estimator is underdeveloped in the main paper, and the statistical story is incomplete.**  
   The actual observable score in practice is the plug-in estimator from **Definition 4.4**, not \(\Gamma(PQ)\). But the main paper gives only an asymptotic statement in **Proposition 4.5** and pushes finite-sample guarantees and the stratified estimator to the appendix. For a method whose determinant can be highly sensitive to noise, the missing finite-sample discussion in the main text is a real problem. The estimator uses
   \[
   \bar G(x,x')=\frac{1}{N^2}\sum_{n,n':\hat x_n=x,\hat x_{n'}=x'} \mathbf 1[y_n=y_{n'}],
   \]
   and the paper does not discuss variance, bias from diagonal terms \(n=n'\), conditioning of \(\bar G\), or what happens when some reported classes are rare or absent. These are not cosmetic omissions. Since the determinant is a product of eigenvalues, a small perturbation in a nearly singular Gram matrix can drastically change the score and thus the induced ranking.

4. **There are mathematical and notational clarity issues around the definition of the experiment matrix and stochastic conventions.**  
   In **Section 2.1**, the paper says \(P\) is a column-stochastic matrix whose columns \(P_x\) are distributions over \(\mathcal Y\). But in **Experiment 1** on **Page 8**, the experiment matrix \(P\in[0,1]^{d\times d}\) is constructed by sampling entries and “normalizing rows to be stochastic.” That is inconsistent with the formal convention earlier unless the transpose is intended. This is not a minor typo because matrix orientation matters throughout the derivations, especially in **Equation (4)** and in statements about columns being linearly independent. There are several similar exposition issues. For example, the dist-ordering definition on **Page 4** appears to have formatting/typing problems in the metric assumptions, and the explanation after **Figure 3(a-c)** says “the score increases monotonically with \(p\),” which directly contradicts both the method’s intended behavior and the plotted trends in the figure. These inconsistencies reduce confidence that the notation and empirical claims were checked carefully.

5. **The experimental evaluation is too light relative to the paper’s broad claims, and crucial baselines are missing.**  
   The experiments mostly show that the proposed score correlates with corruption level or with ground-truth error on synthetic manipulations. That is a useful sanity check, but it falls short of demonstrating that the score is preferable to simpler alternatives. The paper itself mentions mutual-information-related literature in **Section 1.1**, determinant-based objectives, PCA-based valuation, and other dependence measures, yet no empirical comparison is provided against straightforward baselines such as empirical mutual information between \(\hat x\) and \(y\), HSIC/kernel dependence scores, covariance log-determinant variants, class-conditional separation metrics, or even simple agreement statistics derived from embeddings. Without those baselines, it is hard to tell whether the determinant structure is actually necessary, or whether many generic dependence scores would look similar on **Figure 2** and **Figure 3**.

6. **The synthetic setup is favorable to the method and does not stress the hard cases implied by the theory.**  
   In **Experiment 1**, the data are balanced, \(d\) is only 5, and the same fixed ground-truth dataset is reused across trials. The experiment matrix is randomly generated, but the analysis focuses on simple monotonic trends against corruption probability. There is no study of what happens under strong class imbalance, near-collinear experiment columns, larger label spaces, class merging that destroys invertibility, or settings where two classes have nearly indistinguishable observation distributions. Those are exactly the cases where the determinant-based score should become fragile or ambiguous. **Figure 2(d)** is also weaker than claimed, because it only uses the uniformly random manipulation strategy when reporting Kendall-tau distance, despite the text discussing ranking of six corrupted reports more generally. If the method is supposed to be robust across corruption schemes, the ranking consistency analysis should not be confined to one of them.

7. **The CIFAR-10 experiment is not convincing as evidence for representation-learning relevance.**  
   In **Experiment 2**, the observations \(y_n\) are SimCLR embeddings, and the kernel is simply the linear inner product \(K(y,y')=\langle y,y'\rangle\). This is a reasonable toy instantiation, but the experiment remains shallow. There is no comparison across kernels, no sensitivity analysis to representation quality, no test with other encoders, and no demonstration that the score meaningfully distinguishes subtler forms of label noise beyond synthetic corruption. Moreover, the sentence on **Page 9** stating that “the score increases monotonically with \(p\)” appears to be an outright mistake, and the plot in **Figure 3(a)** visually seems to show the opposite trend. That makes the main empirical takeaway here sloppier than it should be.

8. **The real-data case study is too small and too under-analyzed to carry much evidentiary weight.**  
   The employment-data example on **Pages 9-10** uses only \(N=209\) months, discretizes both series into four quantile buckets, and reports a single bar chart in **Figure 3(d)**. There is no uncertainty quantification, no robustness to the discretization choice, no alternative external signals, and no benchmark against simpler rank-correlation or time-series alignment measures. Because the entire case study is reduced to one discretization and one score, the claim that revisions “substantially improve reliability” according to the method is suggestive at best. It is not enough to validate the practical usefulness of the framework.

9. **The relation to prior work is not fully convincing, especially on the empirical side.**  
   The related work section touches many areas, but the paper’s empirical positioning remains thin. There is some discussion of determinant mutual information and pointwise mutual information approaches, yet the manuscript never directly compares against those methods in experiments, even though they appear to be among the most natural competitors. This weakens the novelty case in practice, because the reader is left wondering whether the contribution is mainly a theoretical reframing of determinant-based dependence measures with new order-preservation arguments, or whether it also leads to better empirical reliability scoring.

10. **There is no serious discussion of numerical stability or computational scaling.**  
    The proposed score is a determinant of a \(d\times d\) Gram matrix. In principle that seems easy, but determinants can become numerically tiny and unstable when classes are numerous, imbalanced, or nearly dependent. The paper does not discuss working in log-determinant space, regularization, conditioning diagnostics, or how the estimator behaves when some reported classes have very small support. This matters because many realistic reliability-assessment settings involve large label vocabularies or skewed marginals, where raw determinants are notoriously brittle.

11. **Some claims in the narrative are stronger than what the presented evidence supports.**  
    The abstract says the experiments “demonstrate that the Gram determinant score effectively captures data quality across diverse observation processes.” Given the limited baselines, small real-data case study, and the gap between theorem assumptions and tested regimes, that conclusion feels too strong. At this stage, the experiments show plausibility and some monotonic correlation under selected synthetic corruptions, not broad validation across diverse observation processes.

## Questions
1. The distance-order result in **Theorem 4.2** only holds on \(\mathcal Q_{L,1/(64L^2d^2)}\). Can the authors provide intuition for how often this regime is expected to hold in realistic settings, and can they state explicitly, in the main paper, how far the experimental corruption rates are from the proven regime? A rebuttal that clarifies this gap, and ideally adds experiments in the theoretically covered regime, would increase my confidence.

2. For the plug-in estimator in **Definition 4.4**, how are diagonal terms \(n=n'\) handled, and what is the finite-sample bias/variance behavior of \(\det(\bar G)\)? A brief finite-sample concentration statement or at least an experimentally grounded stability analysis in the main paper would help substantially.

3. The manuscript alternates between column-stochastic and row-normalized conventions for \(P\). Can the authors cleanly restate the orientation of \(P\), \(Q\), and \(PQ\), and verify that all formulas, especially **Equation (1)** and **Equation (4)**, are dimensionally and conventionally consistent?

4. Can the authors compare the proposed score against at least a few simple, relevant baselines, such as empirical mutual information between \(\hat x\) and \(y\), HSIC or kernel dependence, covariance/log-det surrogates, or the determinant mutual information style score cited in related work? Right now the experiments mainly show absolute trends, not relative value.

5. In **Figure 2(d)**, why is Kendall-tau ranking consistency evaluated only for the uniformly random corruption strategy? Since the paper studies six corruption policies elsewhere, it would be much stronger to show whether the ranking quality persists across the more structured manipulations as well.

6. For **Experiment 2**, how sensitive is the kernelized score to the choice of kernel and to the quality of the learned representation? For example, does the ordering remain similar with an RBF kernel, cosine similarity, or embeddings from a supervised encoder versus SimCLR?

7. For the employment-data study in **Figure 3(d)**, how robust is the conclusion to the number of quantile buckets and to alternative auxiliary signals? Since the result is based on a small sample and one discretization choice, some robustness checks seem necessary before drawing practical conclusions.

8. The uniqueness claim in **Proposition 4.3** is stated on \(GL_d\). Could the authors more carefully discuss what happens for singular \(Q\), especially because practical corruption mechanisms like class merging can naturally produce non-invertible misreport matrices?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond ordinary caution about using reliability scores in consequential settings. The paper does not present a deployment study involving human subjects or sensitive personal data processing details that would, on the basis of the main text alone, require formal ethics escalation.

## Soundness Rating
2: fair. The core algebra is plausible and some theoretical claims are interesting, but important assumptions are restrictive, the practical estimator is insufficiently analyzed in the main paper, and the empirical evidence does not fully support the breadth of the claims.

## Presentation Rating
2: fair. The paper is readable overall and the high-level idea is understandable, but there are multiple notation inconsistencies, at least one clear contradiction between text and figure trends, and several claims whose scope is not communicated carefully enough.

## Contribution Rating
2: fair. The problem formulation and experiment-agnostic determinant perspective are interesting, but the current paper does not yet make a sufficiently convincing overall contribution for ICLR because the guarantees hold in a narrow regime and the experiments are not strong enough to establish practical advantage.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a real idea here, especially in the ordering-based formalization and the determinant factorization, but the paper currently overreaches relative to what it proves and validates. The narrowness of the positive guarantees, the lack of baseline comparisons, and the limited empirical depth collectively leave this below the ICLR bar for me.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main mathematical setup and the empirical claims in the main paper, but some deferred proofs and estimator details are outside the main-text evidence I am using for the final judgment.