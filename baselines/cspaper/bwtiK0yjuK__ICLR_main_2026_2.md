---
job_id: a5823614-5e68-414a-ae66-1a94bf03b3ec
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bwtiK0yjuK.pdf
paper: Change Point Localization and Inference in Dynamic Multilayer Networks
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically learning on graphs, probabilistic methods, and learning theory for dynamic network models.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, namely abstract, introduction with related-work positioning, methodology, theory, experiments, quantitative results, and conclusion; despite some clarity and technical issues, it meets the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies offline change point localization and inference for dynamic multilayer random dot product graphs, where layers share latent node positions and only the layer-specific connectivity weights evolve over time. The authors propose a two-stage method that uses seeded binary segmentation for coarse detection and a TH-PCA-based local refinement step, then provide consistency guarantees, limiting distributions for refined estimators in vanishing and non-vanishing jump regimes, and a data-driven confidence interval construction. The empirical section compares the approach against graph-based and kernel-based competitors on synthetic multilayer network settings and two real datasets.

## Strengths
The paper tackles a meaningful problem that is both statistically nontrivial and relevant for graph representation models, namely change point localization and inference in dynamic multilayer networks rather than the more standard single-layer setting.

The methodological structure is sensible. The two-stage design, coarse candidate generation followed by localized refinement, is well motivated, and it adapts known ideas from change point analysis to the multilayer RDPG setting in a way that is not merely cosmetic. In particular, the use of tensor low-rank estimation in Stage II is aligned with the shared-latent-position multilayer model.

Theoretical coverage is ambitious and, on the whole, substantial. The paper does not stop at consistency of estimated number and locations of change points, but also develops limiting distributions and a confidence interval construction. For an ICLR paper in this area, that level of inferential ambition is a genuine plus.

Some mathematical components are clearly structured. For example, the CUSUM definition in **Equation (1)** and the Tucker-style representation in **Equations (2)-(4)** make clear how the D-MRDPG structure induces a low-rank tensor form for expected transformed tensors, which is central to why TH-PCA is relevant here. Similarly, **Equation (5)** gives a concrete final refinement criterion rather than relying on a vague heuristic.

The experiments are broader than many purely theoretical papers. **Table 1** reports several metrics, not just a single localization error, and the method performs strongly across all four synthetic scenarios, including Scenarios 2 and 3 where the data violate Model 1. This robustness-to-misspecification angle is useful and makes the empirical section more convincing than a theory-only validation.

The confidence interval evaluation in **Table 2** is also helpful. Even though the evidence is limited, it is good to see that the inference procedure is not left as a purely asymptotic statement. The larger-$n$ improvement in Scenario 3 is also at least qualitatively consistent with the theory.

The real-data section is reasonably interpretable. **Tables 3 and 4** show that the method detects a moderate number of change points and provides intervals, which is more actionable than methods that only produce a long list of unstable detections. The same is true for the U.S. air transportation example in **Tables 14 and 15**.

Although there is only one figure in the provided content, the schematic timeline in **Figure 1** in Appendix F is actually useful. It clarifies the “three-change-points may fall in the wider neighborhood” geometry used in the bias analysis of Section F, which would otherwise be quite hard to parse from the equations alone. This figure supports the authors’ argument that the refinement analysis must account for contamination from adjacent segments.

## Weaknesses
1. **The paper’s central modeling assumptions are restrictive, and the gap between theory and the experiments is larger than the writing admits.**  
   The main model in **Model 1** assumes fixed latent positions over time and changes only in the layer-specific weight matrices. This is a strong structural assumption for dynamic networks, especially in applications where node roles or communities themselves evolve. The authors acknowledge an extension in Appendix C, but the main-paper guarantees are still anchored to the fixed-latent-position case. This matters because the empirical section explicitly includes settings that violate Model 1, especially Scenarios 2 and 3 on **Pages 8-9**, and then uses those strong empirical outcomes to support broad practical claims. If the method works well beyond the model class, great, but then the paper should be more careful in separating “provably covered” from “empirically promising under misspecification.” As written, the theory feels narrower than the headline claims.

2. **The spacing assumption $\Delta=\Theta(T)$ is very strong and materially limits the stated contribution for multiple-change-point problems.**  
   This appears already in **Model 1(i)** on **Page 3**, where the number of changes is effectively bounded. The paper later says this could be relaxed in future work, but that does not soften the fact that the current theory excludes frequent changes, which are exactly where multilayer temporal data can become interesting. The extra experiments in the appendix are useful, but the main-paper theory does not cover that regime. This matters because seeded binary segmentation is usually appealing partly for handling many changes at scale, yet the formal guarantees here are confined to a much easier asymptotic regime.

3. **Several key quantities required by the method and theory are not realistically available, and the paper does not adequately close that gap in the main text.**  
   In **Definition 5** and **Equation (6)**, the TH-PCA calls require input ranks like $(d,d,m_{b_k}^{s_k,e_k})$ or $(d,d,m^{\widetilde{\eta}_{k-1},\widetilde{\eta}_k})$, where the $m$ terms are ranks of population objects defined through $Q(t)$ or its local averages. Those are not observable. Likewise, the latent dimension $d$ is treated as known throughout the main method and assumptions. The paper says on **Page 5** that this can be interpreted as knowing the intrinsic dimension and points elsewhere for rank selection discussion, but the main algorithm is still not fully data-driven in the sense that a practitioner can run it from the paper alone. This matters because the proposed “fully data-driven” confidence interval language in the abstract and Section 3 is a bit overstated when the upstream estimation pipeline depends on inaccessible structural inputs.

4. **There are clarity and consistency issues in the notation and theorem statements, some of which are not minor.**  
   A few examples:
   - In **Definition 5** on **Page 4**, the notation switches between $\widetilde{K}$ and $K$, and the input tuple is written as $\{(b_k,s_k,e_k)\}_{k=1}^K$ while the definition then says “for any $k\in[\widetilde{K}]$”.  
   - In **Theorem 2** on **Pages 6-7**, the statement says “Let $\{\widetilde{\eta}_k\}_{k=1}^{\widetilde K}$ be defined in (5) with $\{\widetilde{\eta}_k\}_{k=1}^{\widetilde K}$ obtained from Algorithm 1,” which is clearly inconsistent because **Equation (5)** defines $\widehat{\eta}_k$, not $\widetilde{\eta}_k$.  
   - In the vanishing-jump limit in **Theorem 2**, the display says $\mathcal{P}'_k(r)$ for $r\in\mathbb{R}$ but immediately after says “for $r\in\mathbb{Z}$,” while also invoking Brownian motions. The indexing/set where the argmin lives is not cleanly specified.  
   - In **Equation (4)**, the row definition of $Q(u)$ is not written clearly enough to unambiguously parse the vectorization of $W_{(l)}(u)$.  
   These are not cosmetic typos only. In a paper whose contribution leans heavily on asymptotic inference, sloppiness around estimator notation and limit objects makes the technical claims harder to trust.

5. **There are mathematical/proof presentation problems in the main text and appendix that need tightening.**  
   The most striking issue is in Appendix E, especially **Pages 17-19**, where the notation for estimated versus population refined tensors collapses into itself. For example, the proof repeatedly writes expressions of the form  
   \[
   \left\|\widetilde{\mathbf P}^{s_k,e_k}(t)-\widetilde{\mathbf P}^{s_k,e_k}(t)\right\|_F
   \]
   which is identically zero as written, but from context the authors obviously mean estimated minus population quantities. The same problem appears around **Equations (12)-(14)** and later probabilities involving normalized projected tensors. This is not a harmless typo once or twice; it occurs in the core argument that justifies Stage II. A careful rewrite is needed because the current proof text, as presented, is internally inconsistent at multiple steps.

   Relatedly, **Definition 5** assumes independent sequences $\{\mathbf A'(t)\}$ and $\{\mathbf B'(t)\}$ generated according to Definition 2, while **Algorithm 1** requires four mutually independent sequences. Then **Page 4** says that in practice the implementation uses odd-even splitting. The theory-practice bridge is therefore somewhat hand-wavy in the main paper. If independence is only a proof device, that is acceptable, but then the empirical consequences of reusing split samples should be discussed more concretely.

6. **The confidence interval construction looks empirically fragile, and the evidence supporting it is thin.**  
   In **Table 2**, the reported interval lengths are implausibly tiny in some settings, for example average length \(0.003\) with 100% coverage in Scenario 1 for \(n=100\). For discrete-time change points, this suggests intervals much narrower than a single time unit, which is not impossible if interpreted continuously, but it raises practical interpretability questions. The issue becomes sharper in the real-data results. In **Table 4**, the change point labeled “2005” corresponds to time point 20, but the interval is \((17.97, 18.05)\), which appears centered near 18 rather than 20. A similar mismatch appears in **Table 15**, where “2020-02” is listed at time point 62 but the interval is \((59.66, 60.36)\). These look like more than rounding artifacts. If the table is incorrect, that is a serious presentation issue for the inference contribution. If the intervals are on another indexing convention, the paper needs to say so explicitly.

7. **The empirical comparison is solid but not fully diagnostic of where the gains come from.**  
   **Table 1** shows strong results for CPDmrdpg against gSeg and kerSeg, often by a large margin. However, the competitors are fairly generic graph change point methods operating either on networks or layer-wise Frobenius norms, so the comparison mostly shows that exploiting multilayer low-rank structure helps, which is plausible. What is missing is an ablation that isolates the benefit of the two main stages. For example, how much of the gain comes from SBS with the proposed bilinear CUSUM statistic, and how much from the TH-PCA refinement? Similarly, a comparison against a simpler low-rank denoising baseline without seeded segmentation would help. Without this, **Table 1** supports “the full method works well,” but not “both ingredients are necessary.”

8. **The presentation of Algorithm 1 and some surrounding definitions is rough enough to impede reproducibility.**  
   On **Page 5**, the algorithm formatting is difficult to parse, several symbols are malformed, and the recursion syntax is not cleanly expressed. Given that the paper’s method is algorithmic, this matters. The same issue affects the notation in **Algorithm 2** and **Algorithm 3** in the appendix, where overwriting steps and initialization are not always easy to follow. A reader can infer the intended procedure, but should not have to reverse-engineer it.

9. **The literature positioning is somewhat narrow on the experimental side.**  
   The paper does a decent job covering statistical change point work for networks, but the empirical comparison set is mostly limited to gSeg and kerSeg in the main paper. For a conference like ICLR, where graph representation and latent-space methods are central, the paper would benefit from stronger discussion of how this approach differs from modern latent embedding or neural methods for dynamic graph change detection. Even if such methods do not admit the same theory, positioning only against classical competitors makes the empirical story feel narrower than it could be.

10. **Computational cost may be nontrivial relative to the practical scale of multilayer network data, and the evidence on scalability is weak.**  
    The paper states on **Page 4** an overall cost of \(O(Tn^2Lr\log^2(T\vee n))\), which is already substantial because of the dense \(n^2L\) dependence. The appendix runtime note on **Page 30** reports about 10 hours for synthetic settings with \(n=100\), \(L=4\), \(T=200\) over 100 Monte Carlo trials, which is not outrageous, but it does suggest the method is not lightweight. Since dynamic multilayer networks can be much larger, some comment on sparsity exploitation or approximate computation would strengthen the practical case.

## Questions
1. In **Table 4** and **Table 15**, are the reported confidence intervals indexed on the same time scale as the displayed detected change points? As written, some intervals do not appear centered around the reported time points. Please clarify whether this is a typo, a reindexing issue, or a property of the estimator.

2. Can the authors provide a cleaner, fully explicit statement of what inputs must be known versus estimated in practice, especially \(d\), \(m_t^{s,e}\), and \(m^{s,e}\) from **Definition 5**, **Assumption 1**, and **Equation (6)**? A concise practical recipe would increase confidence in usability.

3. Please clarify the theorem statement and notation around **Theorem 2**, especially the use of \(\widetilde{\eta}_k\) versus \(\widehat{\eta}_k\), and whether the argmin in the vanishing-jump regime is over \(\mathbb{R}\) or \(\mathbb{Z}\). This is important because the inference contribution depends on it.

4. The appendix proof around **Equations (12)-(14)** appears to use the same notation for estimated and population tensors, leading to expressions that are identically zero as written. Is this purely a transcription error in the manuscript, or is there a missing estimator notation throughout that section? A corrected proof sketch in the rebuttal would materially increase my confidence.

5. Can the authors add or summarize an ablation that separates:  
   (a) Stage I only,  
   (b) Stage I + a simpler local refinement,  
   (c) the full TH-PCA refinement?  
   Given the very strong results in **Table 1**, this would help identify which component drives the improvement.

6. Since the main theory assumes \(\Delta=\Theta(T)\), can the authors better delimit what part of the empirical performance under more frequent changes should be considered covered by theory versus purely heuristic? This would make the claims more precise.

7. For the confidence interval procedure in Section 3.1, what is the intended practical interpretation of intervals whose average lengths are far below 1 time unit in **Table 2**? Are these meant to be rounded to integer time points, or interpreted as continuous-time surrogates on a discrete index set?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The paper has substantial technical content and many claims are plausibly correct, but there are enough notation inconsistencies, proof-writing problems, and gaps between assumptions and practice that I cannot rate the soundness higher without clarification.

## Presentation Rating
2: fair. The high-level story is understandable, but the manuscript has multiple theorem-statement inconsistencies, difficult algorithm formatting, and confusing table entries that materially affect readability.

## Contribution Rating
3: good. The problem is important, the multilayer-network focus is worthwhile, and the combination of localization and inference results is valuable to the community even if the assumptions are somewhat restrictive.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a meaningful contribution and a strong enough technical/empirical core to merit serious consideration, but it also has real issues in exposition, proof presentation, and practical specification that keep it from being an easy accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns I raised, although some appendix derivations would benefit from author clarification due to the notation problems in the current draft.