---
job_id: 2d58caf6-6edd-4345-a251-654677f81326
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: pI9n8wAR80.pdf
paper: CoLA: Co-Calibrated Logit Adjustment for Long-Tailed Semi-Supervised Learning
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, targeting semi-supervised learning under long-tailed distributions, with links to representation learning, meta-learning, calibration, and learning theory.

## Minimum Quality
Pass ✅. The submission includes the expected core components, namely abstract, introduction, related work, methodology, experiments with quantitative results, and conclusion, and it presents a coherent empirical study with a nontrivial methodological contribution, despite several technical and presentation issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other signs of manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies long-tailed semi-supervised learning under labeled/unlabeled distribution mismatch, focusing on limitations of logit adjustment for pseudo-label generation. The proposed method, CoLA, combines a redundancy-aware unlabeled distribution estimator, DDDE, based on effective rank of class-wise representations, with a meta-learned global logit-adjustment strength, LMC, optimized on a proxy validation set resampled from labeled data. The paper also provides a generalization-style bound for the proxy-set optimization and reports results on CIFAR-10/100-LT, STL-10-LT, and SIN-127.

## Strengths
1. The paper tackles a real and important problem in LTSSL, namely that pseudo-label correction becomes brittle when the unlabeled class prior is unknown and differs from the labeled prior. This is a meaningful setting beyond the simplistic matched-prior case.

2. The main idea has a reasonable conceptual structure. The authors identify two distinct issues in post-hoc LA, the per-class prior estimate and the global scaling strength, and attempt to co-design them rather than treating them independently. That framing is useful, and the decomposition of the problem into DDDE plus LMC is easy to follow at a high level.

3. The empirical section is fairly broad. **Table 1** shows consistently strong performance across five distribution scenarios on both CIFAR-10-LT and CIFAR-100-LT, and CoLA is indeed competitive across all columns rather than relying on a single favorable setup. The gains on CIFAR-100-LT are particularly relevant because the harder, higher-class-count case is where prior estimation and calibration errors are more likely to matter. **Table 2** and **Table 3** further show that the method is not restricted to a single benchmark family.

4. The ablations are directionally supportive. In **Table 4**, the comparison between fixed-$\tau$ variants, LMC without DDDE, and the full model does support the paper’s main thesis that class-wise prior estimation and global strength should be tuned together. The fact that w/o D-L is usually better than fixed $\tau$, and full CoLA is usually better than w/o D-L, is one of the more convincing pieces of evidence in the paper.

5. The distribution-estimation study in **Table 5** is useful. Even though the choice of baselines there can be debated, the table at least attempts to directly validate the intermediate claim that DDDE gives a better class-prior estimate than naive or approximation-based alternatives.

6. **Figure 1** is actually helpful in motivating the method. Panel (a) makes the oversuppression argument intuitive by illustrating how raw frequency can overcount redundant head-class samples; panel (b) also conveys the key empirical claim that the best global adjustment strength is not monotone in imbalance ratio. This is a better motivation than just asserting “fixed $\tau$ is suboptimal.”

7. **Figure 2** provides a useful training-dynamics view. The curves suggest that the meta-learned calibration does not merely produce one lucky endpoint result, but can alter pseudo-label accuracy during training in several settings. Even though the effect size varies, the visualization is aligned with the intended mechanism.

## Weaknesses
1. The methodological change from classical logit adjustment to the paper’s linear adjustment is under-justified and creates a mismatch between the problem formulation and the final optimization objective.  
   In the preliminary section, **Equation (1)** defines post-hoc LA as
   \[
   \hat y_j = \arg\max_y \left(z_y(\alpha(x_j^u)) - \tau \log \hat P_{Y_u}(y)\right),
   \]
   which is the standard form. However, in Section 4.2 the optimization suddenly switches to
   \[
   z(\alpha(x_i^v)) - \tau \mathbf p,
   \]
   where \(\mathbf p\) contains raw estimated class frequencies, not \(\log \mathbf p\). This is not a small implementation detail, it changes the adjustment geometry substantially. The argument given on **Page 5** is mostly heuristic, “avoids numerical instability and overly aggressive penalization,” but there is no derivation showing why the linear form is preferable for pseudo-label calibration in this setting, nor any direct experimental comparison between linear and logarithmic versions under the same LMC framework. Since the central claim is about “co-calibrated logit adjustment,” I would expect at least one controlled ablation isolating: (i) DDDE + fixed log-LA, (ii) DDDE + learned log-LA, (iii) DDDE + learned linear-LA. Without that, it is hard to know whether the gain comes from co-calibration, from replacing \(\log p\) by \(p\), or from a favorable implementation choice.

2. The DDDE estimator is intuitively motivated, but the link between effective rank and class prevalence is not convincingly established, and some assumptions are shaky.  
   In Section 4.1, the method computes \(\operatorname{erank}(Z_y)\) from a class-specific feature matrix \(Z_y \in \mathbb R^{d \times m_y}\), then normalizes these effective ranks into a class prior estimate:
   \[
   \hat P_{Y_u}(y)=\frac{\operatorname{erank}(Z_y)}{\sum_k \operatorname{erank}(Z_k)}.
   \]
   This assumes, implicitly, that intrinsic feature dimensionality is a good proxy for effective sample count, and therefore for class mass. That may hold in some redundancy-heavy cases, but it can also fail badly when a rare class is semantically diverse or a frequent class is naturally compact. The paper gives a nice cartoon in **Figure 1(a)**, but no more formal argument for when \(\operatorname{erank}(Z_y)\) should track \(M_y\) better than \(m_y\). Worse, the text says “we assume that \(Z_y\) is full-rank, since it is exceedingly rare for any two representation vectors to be perfectly linearly dependent” on **Page 4**, which is not the right condition for full rank. Full rank of a \(d \times m_y\) matrix requires linear independence of all columns up to \(\min(d,m_y)\), not merely that no two columns are exactly dependent. In practice, many features can be highly correlated, especially late in training or within visually homogeneous classes. The method may still work empirically, but this part of the exposition is mathematically sloppy.

3. The theoretical section is much weaker than the paper makes it sound, and parts of it are internally inconsistent.  
   The bound in Section 5 is a generic importance-weighted generalization bound under strong assumptions. That by itself is acceptable, but several details are not clean. On **Page 6**, the expected risk is first defined as \(R_{P_a}(h_\tau)\) while the text says the proposition concerns \(P_u\), and this \(P_a\)/\(P_u\) notation drift continues in the appendix. The statement of **Proposition 1** includes both \(\hat R_{\mathcal D_v}(h_\tau)\) and \(\hat R_{\mathcal D_v,w}(h_\tau)\), but only the latter is the actual importance-weighted empirical risk; the first appears after a triangle-inequality trick, which makes the bound less interpretable as an optimization guarantee for the actual LMC procedure. More importantly, the proof in Appendix D explicitly says “it is obvious that the result continues to hold” when applying Talagrand’s contraction to a sample-dependent \(\Phi_y(a)=w(y)a\). That is precisely the kind of step that should not be waved away when the paper is using theory to support a central methodological component. If the contraction argument depends on sample-dependent multipliers, the proof should state the proper version carefully.

4. The convexity claim is overstated relative to the actual training pipeline.  
   Appendix F shows convexity of the proxy-set cross-entropy as a function of a single scalar \(\tau\), with logits and \(\mathbf p\) treated as fixed. That statement is fine in isolation. But the paper’s wording in Section 5 and Appendix F risks overselling the result as if it explains reliable optimization of the practical procedure. In the actual algorithm on **Page 21**, \(\hat P_{Y_u}\) evolves over training, the proxy set \(D_v\) is resampled, and \(\hat \tau\) is learned during an ongoing nonconvex training process. So the practical training objective is not simply a fixed convex function of \(\tau\). The paper should be much more explicit that convexity only holds for a frozen backbone and frozen estimated prior at one meta-update stage, not for the end-to-end system.

5. The proxy validation construction raises statistical and practical concerns that are not sufficiently discussed.  
   Section 4.2 constructs \(D_v\) by rejection sampling from the labeled set using probabilities proportional to \(\hat P_{Y_u}(y_i)/N_{y_i}\). This means the same small labeled set, already used for supervised training, is also repurposed to fit the calibration parameter \(\tau\). I do not think this is invalid per se, but it does create dependence between the training signal and the proxy “validation” signal, especially in extreme tail classes with very few labeled examples. The paper does not discuss whether this causes overfitting of \(\tau\) to the labeled set, whether a disjoint held-out labeled split was considered, or how sensitive LMC is when some classes have tiny \(N_y\). Since the whole point of LMC is data-driven tuning, the reliability of this proxy set matters a lot.

6. The empirical comparisons are strong overall, but some evaluation choices blur the strength of the conclusions.  
   On CIFAR in **Table 1**, the paper aggregates across multiple settings within each distribution into a single mean and standard deviation, then reports only the aggregated number in the main paper. This hides setup-specific variability and can make methods look more uniformly stable than they are. The appendix tables help, but the main paper’s headline comparison would be more convincing if at least one representative per-distribution breakdown were shown directly, especially because the paper’s own argument in **Figure 1(b)** is that the optimal adjustment varies sharply with imbalance and class count. If sensitivity is central, aggregation is not the cleanest presentation. Similarly, **Table 2** on STL-10-LT is presented positively in the main text, but the paper later notes in the appendix that ADELLO can outperform CoLA on some STL settings when OOD distillation is included. Since STL-10-LT is explicitly described as containing unknown/OOD unlabeled samples, that caveat matters and should not be relegated entirely outside the main comparison narrative.

7. The algorithm description has several clarity issues and notation inconsistencies that make careful verification harder than it should be.  
   Examples: on **Page 4**, \(z(x)\) is called the “backbone” but also denotes logits, which conflates representation and classifier output; in Section 4.1 the representations are denoted \(\mathbf z_j^y\), while elsewhere \(z(\cdot)\) denotes logits, so the same symbol is used for two different objects. In **Algorithm 1**, line 23 appears to compute
   \[
   L_\tau \gets \mathrm{CE}(y_i^e,\sigma(z(\alpha(x_i^u))) - \hat\tau \hat P_{Y_u}),
   \]
   which seems wrong on its face: it uses \(x_i^u\) rather than the proxy sample \(x_i^v\), and the placement of \(-\hat\tau \hat P_{Y_u}\) relative to \(\sigma(\cdot)\) is inconsistent with the equation in Section 4.2, where the adjustment is applied before softmax. This may be a typo, but for a paper that emphasizes theoretical care, the algorithm should be precise. There are also multiple naming inconsistencies in tables, for example “Legal Adjunction-Based,” “Lens Reweighting-Based,” “Dens Mixing-Based,” and “SimPro/Sim-Pro,” which look like editing artifacts rather than substantive issues, but collectively they hurt confidence in the presentation.

8. The claimed support from **Figure 2** is weaker than the text suggests.  
   The figure shows pseudo-label accuracy over epochs, with a dashed line indicating when the learned \(\tau\) is applied. In several plots the post-application gain is modest, and in some settings the slope after the dashed line appears comparable to the slope before it. That does not invalidate the method, but it means the figure supports a nuanced claim, “helps in some settings and does not hurt much in others,” more than a strong mechanistic claim that LMC sharply improves pseudo-label quality across the board. The wording on **Page 9-10** should be toned down accordingly.

9. The literature positioning is decent, but still somewhat narrow around LA-based methods.  
   The paper argues that LA-based methods rely on fixed anchor distributions or weak dynamic estimates, which is fair, but there is less discussion of broader alternatives for managing pseudo-label bias under long-tail mismatch, such as uncertainty-aware selection or open-world LTSSL settings where the unlabeled pool may contain non-target classes. This matters because the method is evaluated on STL-10-LT, where the paper itself acknowledges OOD contamination. I am not asking for a full survey, but the framing currently makes the contribution look more comprehensive than it is.

## Questions
1. The most important question for me is about the switch from \(-\tau \log \hat P(y)\) in **Equation (1)** to \(-\tau \hat P(y)\) in Section 4.2. Can the authors provide a direct ablation that keeps everything fixed and compares learned linear adjustment versus learned logarithmic adjustment? This would materially increase my confidence in the central methodological claim.

2. Can the authors clarify the exact object used to compute DDDE? Is \(Z_y\) formed from pre-classifier features, penultimate-layer activations, or logits? The paper currently uses \(z(\cdot)\) both as logits and as representations. Please provide the precise tensor shape and layer choice used in practice.

3. Please clarify Algorithm 1, line 23. Should \(L_\tau\) be computed on proxy samples \((x_i^v, y_i^v)\) rather than unlabeled samples \(x_i^u\)? Also, should the adjustment be inside softmax, i.e.,
   \[
   \mathrm{CE}\!\left(y_i^v, \sigma(z(\alpha(x_i^v)) - \hat\tau \hat P_{Y_u})\right)?
   \]
   If so, please correct the notation.

4. How sensitive is LMC to the size and composition of the proxy set \(D_v\)? In particular, what happens when tail classes have extremely few labeled examples and the rejection-sampling scheme leaves too few validation points for stable optimization of \(\tau\)?

5. The paper claims DDDE better captures “effective sample size.” Can the authors provide a more direct diagnostic beyond **Table 5**, for example class-wise estimated prior versus true prior, or a plot showing where effective rank helps and where it may undercount semantically diverse but low-redundancy classes?

6. For the theory, can the authors explicitly state the target distribution consistently, \(P_u\) or \(P_a\), and justify the sample-dependent contraction step in the proof rather than appealing to “it is obvious”? A tightened and corrected statement would help.

7. Since the STL-10-LT unlabeled set may contain OOD samples, can the authors comment on whether DDDE or LMC is robust to OOD contamination, or whether the method should be viewed as complementary to explicit OOD filtering?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper. The work uses public vision benchmarks and proposes a method for reducing class-imbalance bias in learning. I do not see a paper-specific ethics issue that requires escalation.

## Soundness Rating
3: good. The method is plausible and supported by substantial experiments, but the theoretical support is weaker than advertised and several formulation details need clarification or correction.

## Presentation Rating
2: fair. The paper is readable at a high level, but notation drift, algorithm inconsistencies, and multiple editing artifacts make careful verification harder than it should be.

## Contribution Rating
3: good. The idea of co-designing class-wise prior estimation and global adjustment strength is useful, and the empirical results are strong enough to be of interest to the LTSSL community, even though some parts feel under-justified.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
The paper addresses an important problem, presents a reasonably interesting method, and shows strong empirical results across several LTSSL benchmarks. However, I am not fully convinced by the theoretical packaging, the shift from log-based to linear adjustment is insufficiently isolated, and the presentation contains enough technical ambiguity that I view this as a cautious accept rather than a strong one.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with LTSSL and logit-adjustment-style methods, and I checked the main technical claims carefully, but some implementation details remain ambiguous due to the paper’s exposition.