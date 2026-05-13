Now I have thoroughly read and verified the paper. Let me synthesize the final review.

## Summary

The paper proposes NCI, a post-hoc OOD detector inspired by the trend of Neural Collapse on practical models. It identifies two key insights: (1) ID features tend to cluster closer to weight vectors of the predicted class (derived from NC1+NC3), and (2) ID features tend to reside farther from the origin (explained by the ETF spatial structure from NC2). The detector combines an angle-based proximity score (pScore) measuring feature-weight alignment with an L1-norm filtering term, achieving O(P) inference complexity. Experiments across CIFAR-10, ImageNet, and multiple architectures show NCI consistently ranks top-3 across benchmarks where other methods show high variance.

## Strengths

- **Unified theoretical framing for two previously separate OOD phenomena**: The paper connects feature clustering and feature norm differences under a single Neural Collapse lens (Sections 3.1–3.2). This provides a coherent mechanistic explanation for why ID features cluster *near weight vectors specifically* and why they have larger norms—both arise from properties of the NC optimization landscape. This is a genuine conceptual advance over treating these as independent observations.

- **Consistent cross-benchmark and cross-architecture performance**: NCI ranks top-3 in both CIFAR-10 and ImageNet benchmarks (Table 1), and this consistency extends to ViT B/16 and Swin v2 (Table 2). No other baseline achieves this cross-benchmark stability, which supports the paper's claim of reduced generalization discrepancies regardless of how one aggregates metrics.

- **Computational efficiency**: NCI achieves O(P) complexity, matching vanilla softmax-confidence inference latency (~0.21ms on ImageNet/ResNet-50 per Table 1b), a genuine practical advantage over KNN (~1.68ms), Mahalanobis, and NECO.

- **Norm-filtering insight generalizes beyond NCI**: The KNN + L1-norm filtering experiment (Table 7, Section 4.3) shows substantial ImageNet gains from adding norm filtering to KNN, validating that the NC-motivated understanding of feature norms captures a general limitation of clustering-based methods, not just a trick specific to the proposed method.

- **Honest qualification about NC convergence**: The paper explicitly states NCI depends on the *trend* rather than complete convergence (Section 3.2, Remark paragraph), and provides empirical evidence (Figure 2) that the ID/OOD separation emerges early in training.

## Weaknesses

### Fatal
None.

### Major

- **Missing critical ablation: pScore vs. simpler alternatives + L1 filtering**: The pScore is defined as $\frac{\mathbf{w}_c^T(\mathbf{h}-\boldsymbol{\mu}_G)}{\|\mathbf{h}-\boldsymbol{\mu}_G\|_2}$—essentially the centered max-logit divided by the centered feature L2 norm. This is closely related to existing scores like max-logit (numerator) and cosine similarity (numerator normalized by both norms). The paper shows that NCI outperforms standalone KNN+L1 (line 480), but the crucial comparison—max-logit or Energy combined with $\alpha\|\mathbf{h}\|_1$ filtering—is absent. If max-logit + L1 filtering performs comparably, then the pScore/NC-derived component provides interpretive but not algorithmic value, and the novelty claims in Sections 1 and 3.3 would be overstated. This ablation is necessary to isolate the marginal algorithmic contribution of the NC-derived pScore from the independently motivated norm-filtering term. The paper itself demonstrates that norm filtering transfers to other methods (Table 7), making it especially important to show what pScore specifically adds beyond what norm filtering alone can achieve with a simpler score function.

### Minor

- **"Overall performance" claim relies on averaging across dissimilar benchmarks with limited justification**: The paper averages AUROC across CIFAR-10 (10-class, 32×32) and ImageNet (1000-class, 224×224), stating these are "of a similar range" (line 397). While AUROC values are indeed in a comparable numerical range, equal weighting means NCI's advantage comes from being "pretty good on both" rather than excelling on either—NCI scores 95.52 AUROC on CIFAR-10 vs. KNN's 97.29, but leads on ImageNet 91.54 vs. 87.56. Whether this tradeoff constitutes "best overall" depends on application priorities. A more principled metric (e.g., normalized gap, Pareto frontier) would strengthen the claim, though the top-3 consistency across benchmarks independently supports the "reduced discrepancy" narrative.

- **Theorem 1 is a direct consequence of NC1 and NC3**: The result $(\mathbf{h}_{i,c}-\boldsymbol{\mu}_G)\to\lambda\mathbf{w}_c$ follows immediately from NC1 ($\mathbf{h}_{i,c}\to\boldsymbol{\mu}_c$) and NC3 ($\frac{\mathbf{w}_c}{\|\mathbf{w}_c\|}=\frac{\boldsymbol{\mu}_c-\boldsymbol{\mu}_G}{\|\boldsymbol{\mu}_c-\boldsymbol{\mu}_G\|}$) combined. The proof's triangle inequality detour is valid but obscures this simplicity. The theorem's role as a formalization of the design insight is acceptable, but it should not be presented as a substantial analytical contribution.

- **Unanalyzed interaction between pScore and L1-norm term**: pScore is inversely related to feature magnitude (it divides by centered norm), while the L1 term grows with magnitude. These opposing dependencies create a decision boundary whose behavior the paper never examines. Understanding where and why this combination works—and when it might fail—is important for interpreting NCI's behavior across different OOD scenarios.

- **Empirical validation of the NC trend limited to one model/dataset pair**: Figure 2 traces the ID/OOD cosine similarity gap for a single CIFAR-10/ResNet-18 model with SVHN as OOD. Showing this trend across architectures and datasets would strengthen the empirical foundation for the "trend suffices" claim, especially for ImageNet-scale models where clustering dynamics may differ.

- **Claim that larger weight vectors correspond to "larger decision regions" is unjustified**: Line 283 states pScore "adapts to class-wise difference by selecting wider hyper-cones for classes with larger weight vectors, which tend to have larger decision regions," but no evidence or reasoning supports the link between weight vector magnitude and decision region size.

### Trivial
None.

## Nice-to-Haves

- Ablation comparing max-logit or Energy + L1-norm filtering against NCI on the same benchmarks. This is the single most impactful addition that could clarify pScore's algorithmic contribution.
- Per-dataset breakdown of how much pScore vs. L1-norm filtering contributes individually to the final score, which would directly test the "mitigating discrepancy" mechanism.
- Failure case analysis: on which OOD datasets/samples does NCI fail, and does it share failure modes with max-logit or KNN?
- Quantitative measurement of NC1 metrics across models to support the claim that weaker clustering explains CIFAR-10 vs. ImageNet performance asymmetry.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Reproducibility concern about μ_G estimation**: The harsh critic noted μ_G must be computed from training data, making the method not purely "off-the-shelf." This is trivial in practice (one forward pass + one stored vector) and the paper's efficiency claims remain valid. Moved to trivial and then removed because it doesn't meaningfully affect evaluation.

- **α selection using Gaussian validation set**: The paper follows standard practice from React/DICE. This is not a legitimate concern.

- **UMAP visualization is qualitative and not probative**: Standard visualization practice; the paper provides quantitative evidence separately.

- **Missing related works**: Removed per hard rules—cannot verify existence of uncited works.

- **Demand for broader trend analysis across architectures**: Already covered above as a minor point; the harsh critic's version was overly demanding (framing it as if the current evidence is useless without this).

- **Strength claim about "Theorem 1 formally establishes" significance**: Overstated given the theorem's trivial derivation. Removed from strengths.

- **Strength claim about "NCI ranks top-three" as evidence of "claimed reduction in generalization discrepancies"**: Partially conflicts with the verified weakness about the averaging metric. The top-3 consistency is a real empirical observation, but the strength finder overclaims the implications.

- **Harsh critic's claim that the paper "overstates" the NECO difference**: The paper does explain the difference (line 416-418: NECO uses max-logit + distance to origin but exclusively analyzes features, requiring expensive matrix multiplication; NCI explores features AND classification head). This comparison is reasonably specified.

## Novel Insights

The most insightful observation across reviews is the tension between pScore and the L1-norm term: pScore *inversely* relates to feature magnitude (normalizing by centered L2 norm), while L1 filtering *directly* scales with magnitude. This means NCI's two components push in opposite directions for borderline samples with large norms but weak clustering—pScore may flag them as OOD while L1 rewards them for being far from origin. The paper never analyzes this tension, and understanding it may reveal important structure about when NCI succeeds and fails. Additionally, the missing ablation of max-logit+L1 is significant precisely because the paper's own KNN+L1 experiment (Table 7) demonstrates that norm filtering alone provides large gains—analogous gains with a simpler score than pScore would substantially undermine the algorithmic novelty of the NC-derived component.

## Suggestions

- Run the critical ablation: replace pScore with max-logit (or Energy) in the NCI formula (i.e., $s = \max_c \mathbf{w}_c^T \mathbf{h} + b_c + \alpha \|\mathbf{h}\|_1$) on both CIFAR-10 and ImageNet benchmarks. This directly isolates whether the pScore design provides gains beyond the norm-filtering insight combined with a trivially available score.
- Add a per-dataset breakdown table showing pScore-only and L1-only performance separately alongside combined NCI, making the "reducing discrepancy" mechanism transparent.
- Provide a brief analysis of the pScore/L1 interaction: for samples near the decision boundary, describe which component dominates the score and how this relates to OOD type (covariate shift vs. semantic shift).

## Score and Decision

The paper makes a genuine conceptual contribution by unifying two OOD detection phenomena under the Neural Collapse framework and demonstrates consistent cross-benchmark performance with strong computational efficiency. However, the missing ablation comparing pScore against simpler alternatives (max-logit/Energy + L1 filtering) is a significant gap—it leaves the core algorithmic contribution of the NC-derived pScore component unverified, especially since the paper's own KNN+L1 experiment shows norm filtering provides substantial standalone gains. The theoretical contribution (Theorem 1) is thin. The overall performance claim, while supported by consistent top-3 rankings, rests on an unweighted average across very different benchmarks. These issues together prevent full confidence in the paper's claims about algorithmic novelty, though the empirical results and conceptual framing are real.

Originality: Moderate. The NC framing is novel for OOD detection; pScore's relationship to existing scores weakens algorithmic novelty.
Importance of research question: High. OOD detection is important and generalization discrepancy is a real practical concern.
Claim support: Moderate. Consistent top-3 rankings support the main claim, but the missing ablation leaves the mechanism unverified.
Soundness of experiments: Moderate. Comprehensive baselines and architectures, but critical ablation absent.
Clarity: Good. Well-structured with clear claims and honest about convergence requirements.
Value to community: Moderate. The conceptual framing is valuable; practical contribution depends on unverified ablation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>