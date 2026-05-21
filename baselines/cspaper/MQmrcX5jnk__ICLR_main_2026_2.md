---
job_id: 554ee4a7-9e96-4c8d-8363-b8bb125d0196
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: MQmrcX5jnk.pdf
paper: Learning Boltzmann Generators via Constrained Mass Transport
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies variational sampling, normalizing flows, optimization under KL and entropy constraints, and applications to molecular Boltzmann generators.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; despite several technical and presentation issues, it meets the minimum bar for a full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Constrained Mass Transport (CMT), a variational framework for sampling from unnormalized target densities by constructing a sequence of intermediate distributions under a trust-region KL constraint, an entropy-decay constraint, or both. The authors derive analytical forms for the intermediate targets and instantiate the framework with normalizing flows for training Boltzmann generators from energy evaluations only. Experiments on four molecular systems, including a new ELIL tetrapeptide benchmark, show improved EUBO, ESS, and Ramachandran-based metrics relative to reverse KL, FAB, and TA-BG.

## Strengths
1. The paper addresses a real and important failure mode in variational Boltzmann generator training. The motivation is well articulated in Sections 1 and 2, namely that reverse-KL training collapses modes, while standard geometric annealing can suffer from schedule sensitivity and “mass teleportation”. This is a meaningful problem for the ICLR community, especially at the interface of generative modeling, variational inference, and scientific ML.

2. The constrained formulation is conceptually clean. The progression from the trust-region-only problem in **Equation (2)**, to the entropy-only problem in **Equation (7)**, to the combined constrained problem in **Equation (9)** is natural and easy to follow. The resulting analytical forms in **Propositions 2.1, 2.2, and 2.3** give the method a principled backbone rather than presenting it as yet another annealing heuristic.

3. I found the high-level intuition in **Figure 1** genuinely useful. The figure does more than decorate the paper, it clarifies the distinct roles of the two constraints. In particular, the geometric path induced by the trust-region alone is shown as maintaining local overlap but still allowing new target modes to emerge without overlap, while the entropy-only path avoids abrupt entropy collapse but can still jump too far from the current iterate. The geometric-tempered path in the rightmost panel is a convincing visual summary of the paper’s central claim.

4. The empirical results are strong and, more importantly, fairly consistent across systems. In **Table 1** on the main paper, CMT improves over TA-BG and FAB on essentially all reported systems in EUBO and ESS, often by a wide margin on the larger systems. The most striking case is ELIL tetrapeptide, where CMT reaches **26.06% ESS** versus **13.75%** for TA-BG and **7.21%** for FAB, while also obtaining the best EUBO. On alanine hexapeptide, CMT reaches **29.63% ESS**, again substantially above TA-BG (**18.22%**) and FAB (**14.55%**). These are not tiny gains that require squinting at standard errors.

5. The qualitative evidence is also reasonably convincing. The Ramachandran plots in **Figure 4** align with the numerical story in **Table 1** and Appendix **Table 2**. In particular, reverse KL visibly misses important regions on the larger systems, while CMT remains much closer to the ground truth. This matters because ESS alone can be misleading under mode collapse, and the paper is right to triangulate with forward metrics and structural projections.

6. The ablation on the constraints is one of the stronger parts of the empirical section. **Figure 2** and **Figure 3** are informative rather than perfunctory. Figure 2(a,b) supports the claim that the entropy constraint helps prevent rapid entropy collapse, while the trust-region stabilizes overlap between successive distributions. Figure 3 then connects this to actual mode coverage on alanine hexapeptide. Even if I have some reservations about whether the ablation is exhaustive enough, it is still better than what many papers provide.

7. The paper is unusually explicit about practical details. The main text already explains how the dual variables are estimated and how intermediate targets are fit, and the appendix provides substantial implementation detail, including computational cost, hyperparameters, and architectural choices. That helps with reproducibility.

8. The new ELIL tetrapeptide benchmark is a useful addition. Even though benchmark creation is not the main contribution, it strengthens the paper by testing the method on a harder system than the standard alanine examples.

## Weaknesses
1. The main theoretical contribution is elegant, but the bridge from the infinite-dimensional constrained problem to the practical algorithm is thinner than the paper sometimes suggests. In Section 2, the paper derives exact intermediate densities over \( \mathcal{P}(\mathbb{R}^d) \), but in Section 3 the method actually learns approximations \( \hat q_i \in \mathcal Q \) by solving **Equation (13)** and then using importance-weighted forward KL in **Equation (15)**. This approximation gap is not minor. The practical procedure only follows the derived annealing path to the extent that the flow family and optimization can accurately fit each intermediate target. The appendix itself acknowledges this in **Figure 12** (“the sequence does not follow the analytical annealing path exactly”), but the main paper does not emphasize this limitation enough. Why this matters: the strongest claims about overlap, entropy control, and path behavior are exact only for the idealized \(q_i\), not necessarily for the learned \(\hat q_i\). Since the experiments depend entirely on the latter, the paper should be more careful in separating properties of the exact path from guarantees for the implemented algorithm.

2. There are several mathematical and notational problems in the main text that should not be there in a paper centered on a variational derivation. The most serious is **Equation (16)** on **Page 5**, where the exponent is written as \(1/(1+3+\eta)\). This is almost certainly meant to be \(1/(1+\lambda+\eta)\), and as written it is incorrect and confusing. The same equation also changes indexing inside the Monte Carlo sum, using \(x_n \sim q_i\) but then writing \(\hat p(x_i)\) and \(q_i(x_i)\). In addition, **Equation (10)** contains an extraneous \((x)\) after \(\tilde p(x)^{\frac{1}{1+\lambda+\eta}}\), and the introduction on **Page 1** inconsistently switches between \(p\), \(\hat p\), and \(\tilde p\), even writing “given by \(p(x)=\hat p(x)/\mathbf z\)” right after defining \(\tilde p\). These are not cosmetic nits, they directly affect the readability and trustworthiness of the derivation.

3. Some optimization claims are stated too strongly or too loosely. On **Page 3**, after introducing the dual function for the trust-region problem, the paper says “Thus, (4) has unique optima which we denote by \(q_{i+1}\) and \(\lambda_i\), respectively.” Uniqueness of the primal solution is plausible from strict convexity, but uniqueness of the dual maximizer \(\lambda_i\) does not follow merely because the dual is concave. Concavity gives existence of maximizers under suitable conditions, not uniqueness unless strict concavity or some equivalent property is shown. The appendix later proves uniqueness of the trust-region solution \(q_i\), but not really uniqueness of the multiplier in the main-text sense. This should be corrected, because the paper leans heavily on analytical structure.

4. The experimental story is strong on final performance, but somewhat weaker on isolating where the gains come from relative to simpler alternatives. The paper argues that CMT improves over geometric annealing because of adaptive trust-region tuning plus entropy control, yet the main paper does not include a direct quantitative comparison to a carefully tuned non-adaptive geometric schedule under matched compute. The appendix mentions such comparisons qualitatively, but says numerical results are omitted because they are “not meaningful”. That is exactly where numbers would be most useful. The ablation in **Figure 2** and **Figure 3** is helpful, but it does not fully answer whether most of the gain comes from adaptivity, from the entropy constraint, from replay-buffered forward-KL fitting, or just from using many more intermediate fitting steps than some baselines. Since this is the core scientific claim, I wanted a cleaner decomposition in the main paper.

5. The paper’s fairness narrative around compute and target evaluations is only partially convincing. **Table 1** reports “TARGET EVALS”, which is important, but target evaluations are not the whole computational story here. Appendix **Table 7** shows that CMT can be substantially slower in wall-clock time than FAB on the larger systems, for example **138.2h vs 56.6h** on ELIL tetrapeptide, and roughly tied with TA-BG only after the latter is scaled up. The conclusion does acknowledge that the current approach requires many gradient updates, but the main paper’s framing could give the impression of near-free performance gains at equal budget. Why this matters: in molecular applications, both target evaluations and overall training time matter. A method that is much more compute-hungry may still be valuable, but the trade-off should be more prominent in the main narrative.

6. The presentation of the algorithm is weaker than the rest of the paper. **Algorithm 1** on **Page 6** is badly typeset and difficult to parse. That would be a mild issue in many papers, but here the practical implementation details are central because the method alternates between dual optimization and flow fitting. The paper also states in Section 3 that solving the two-dimensional dual optimization problem in **Equation (11)** “can be done efficiently in practice”, but the main paper gives very little detail on stability, initialization, or whether the dual estimates are noisy in high dimensions. Those details are deferred entirely to the appendix. The result is that the main paper is stronger on theory and empirical plots than on explaining the actual optimization loop cleanly.

7. Some reported metrics weaken the otherwise clear empirical story because their limitations are substantial, but they are still used prominently. The paper is transparent that ELBO is unreliable here and that ESS can be misleading under mode collapse, which I appreciate. However, the evaluation still puts heavy weight on reverse ESS in **Table 1**, despite explicitly noting that reverse KL can achieve high ESS while collapsing. Similarly, in the appendix the Wasserstein metrics are acknowledged to be unreliable with \(10^4\) samples. This does not invalidate the paper, because EUBO and Ram-based metrics are more informative, but it does mean the empirical case rests on a subset of the metrics more than the summary presentation suggests.

8. The literature positioning is good overall, but still somewhat narrow relative to the broader landscape of Boltzmann and energy-based sampling. The paper compares mainly against FAB, TA-BG, and KL baselines, which makes sense for flow-based variational BGs. Still, the broader claim is about sampling from high-dimensional multimodal Boltzmann targets, and the related work on **Pages 5 to 7** only lightly touches diffusion/consistency-style alternatives. A more explicit discussion of why the comparison set is restricted to variational flow-based methods would strengthen the positioning. As written, the scope oscillates between “general framework for sampling problems” and “practical recipe for variational Boltzmann generators”.

9. There are a few inconsistencies in the benchmark description that should be fixed because they undermine confidence in the empirical section’s polish. For example, the main paper states alanine hexapeptide as \(d=180\) in **Table 1**, while **Table 3** in the appendix lists alanine hexapeptide as \(d=160\). That is likely a typo, but again, this paper asks the reader to trust both derivations and careful benchmarking. These things accumulate.

## Questions
1. Can the authors clarify the exact form of **Equation (16)** in the main paper? As written, the exponent \(1/(1+3+\eta)\) appears incorrect. I assume this should be \(1/(1+\lambda+\eta)\). Please confirm and provide the corrected expression. This is important because the dual optimization depends directly on this estimator.

2. Relatedly, please audit the notation in **Equations (10), (15), and (16)** and the setup on **Page 1** for consistency between \(p\), \(\hat p\), and \(\tilde p\). A concise cleaned-up notation table in the rebuttal would materially increase my confidence.

3. For the trust-region dual on **Page 3**, do the authors actually require uniqueness of the optimal multiplier \(\lambda_i\), or only existence of at least one maximizer? If uniqueness is claimed, please provide the missing argument. If not, I suggest softening the statement.

4. The main paper would be stronger with a clearer decomposition of gains. Can the authors provide, in the rebuttal, a compact quantitative comparison on at least one system between:  
   (a) adaptive trust-region only,  
   (b) entropy only,  
   (c) both constraints,  
   (d) a non-adaptive geometric schedule with matched number of intermediate steps and matched target evaluations?  
   The appendix gives some qualitative discussion, but a direct main-claim comparison would help distinguish “principled path design” from “better schedule tuning”.

5. Can the authors clarify how sensitive CMT is to the entropy bound \(\varepsilon_{\text{ent}}\) in practice? **Figure 10** in the appendix is useful, but the main paper makes the method sound almost plug-and-play. I would like a clearer statement of how much tuning was needed per system, and whether this tuning used validation data or only heuristics from training trajectories.

6. Since **Table 7** shows notable wall-clock overhead on larger systems, especially versus FAB, it would help to know whether the authors believe the improvement comes primarily from better sample efficiency per target evaluation, from more optimization work, or both. A normalized performance-versus-time plot for one large system would be useful.

7. The paper’s strongest empirical claim is robustness on larger systems. Do the authors have evidence that the same constrained path idea would transfer beyond peptide conformational sampling, for example to other energy landscapes where the geometry of metastable regions differs substantially? Even a careful discussion of expected failure modes would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The work studies generative sampling methods for molecular systems and does not raise immediate concerns related to discrimination, privacy, legal compliance, or harmful deployment based on the content provided.

## Soundness Rating
3: good. The central idea is technically plausible and empirically supported, but the paper contains a few nontrivial derivation/notation issues in the main text, and the theoretical claims apply more cleanly to the exact intermediate distributions than to the learned flow approximations used in practice.

## Presentation Rating
3: good. The paper is generally well organized and motivated, and the figures and tables are useful, but several mathematical typos/inconsistencies and the poor presentation of Algorithm 1 prevent a higher score.

## Contribution Rating
3: good. The constrained annealing formulation and its application to Boltzmann generators are valuable and relevant to ICLR, with convincing empirical gains on meaningful benchmarks, though the empirical decomposition and practical-theoretical gap keep this below the highest tier.

## Overall Rating
8: Accept, good paper (poster). The paper presents a principled and empirically strong method for training Boltzmann generators, with substantial gains on the larger benchmarks and a useful constrained view of annealing paths. I do have real reservations about mathematical sloppiness in parts of the main text, the incomplete isolation of which component drives the gains, and the practical gap between the exact path derivation and the learned implementation, but overall the strengths clearly outweigh these issues.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the derivations and empirical evidence with care, though it remains possible that some details of the molecular benchmarking setup are outside my deepest area of expertise.