---
job_id: 503dd24d-0515-4375-ab9c-103965af34f0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GFWfR4G5fm.pdf
paper: Test Time Training for Supervised Causal Learning
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of causal reasoning, transfer/test-time adaptation, and general machine learning.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion. While there are important methodological and clarity issues, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies out-of-distribution generalization in supervised causal learning (SCL) and argues that the standard static pre-training paradigm is fundamentally limited. It introduces a test-time training framework, TTT-SCL, and a concrete method, TACTIC, which searches for graphs whose fitted mechanisms induce data distributions aligned with the given test dataset, using a likelihood-based Alignment of Distribution (AD) score together with a sparsity penalty. Experiments on synthetic, pseudo-real, and real-world benchmarks show improvements over both standard SCL baselines and several traditional causal discovery methods.

## Strengths
The paper tackles a meaningful problem. The central question, namely whether supervised causal discovery models trained on broad synthetic distributions actually generalize to realistic test cases, is important and timely. The empirical diagnosis in Section 3 is useful on its own, because it directly challenges the common assumption that more synthetic diversity is enough.

I found the paper strongest at the level of paradigm shift and empirical framing. The move from static pre-training toward instance-specific training-set construction is conceptually interesting, and it is sufficiently different from the usual “train once, deploy everywhere” SCL pipeline to count as a real contribution rather than a cosmetic tweak.

The paper does a good job using visual elements to motivate the shift in setup. **Figure 1** is simple, but effective: it clearly distinguishes classical causal discovery, standard SCL, and the proposed test-time training variant. In particular, panel (c) makes the core claim concrete, namely that the model is not merely adapted at inference time, but retrained on a customized synthetic dataset tailored to the test instance. That figure materially helps the reader understand what is new here.

The failure analysis in **Figure 2** is one of the stronger parts of the paper. The side-by-side drops from i.i.d. to graph/noise/mechanism shift, and then to the component-mixed condition, support the claim that these models are not simply suffering from mild covariate shift. The most notable pattern is that mechanism shift appears especially harmful, which is a useful empirical observation for the community. Even if one disagrees with some of the stronger narrative claims, the figure demonstrates that current SCL pipelines are brittle in ways that are not usually foregrounded.

The method is reasonably intuitive. The idea in Section 4.1, fit mechanisms on the test data under a candidate graph and score the resulting induced fit by a distributional alignment criterion, is understandable and operational. **Figure 3** also helps here: the seed graph, stochastic local refinement, and forward sampling pipeline are laid out in a way that makes TACTIC easy to follow at a high level.

The empirical results are promising. **Table 2** is the headline evidence: TACTIC (NOTEARS initialization) performs best on Linear_U, Chebyshev_G, Sachs, and Syntren, and is competitive on RFF_G where AVICI has an obvious in-distribution advantage. This pattern supports the authors’ thesis that the method is most valuable precisely when static pre-training is misaligned with the test domain. The improvement on Sachs, from 62.3 for AVICI and 67.1 for PC to 78.9 for TACTIC, is particularly notable.

The ablations are directionally useful. **Table 3** suggests that the sparsity term is not decorative, and **Table 4** is a nice attempt to separate the value of the search stage from the value of the final supervised learner. The \(1 \to 2 \to 3\) improvement pattern in Table 4 is one of the better pieces of evidence that the method is not merely a rebranded score-based graph search.

## Weaknesses
My main concern is that the core scoring objective is underspecified and, in places, conceptually muddled. **Equation (3)** defines
\[
AD(G_{train}^k,D_{test})=\frac{1}{d}\sum_{i=1}^{d}\log p(X_i\mid f_i^k),
\]
but this is not a fully specified likelihood unless the authors define the noise model, the conditioning variables, and how \(p(X_i\mid f_i^k)\) is computed from fitted residuals. In the main text, the method says SIM “regresses the corresponding mechanisms from the observed \(D_{test}\)” and later says the noise distribution is set to standard Gaussian by default in Stage 3 of Section 4.2. These are not the same thing. If the AD score is likelihood-based, then the exact probabilistic model matters. Is it
\[
X_i = f_i(\mathrm{Pa}_G(X_i)) + \epsilon_i,\quad \epsilon_i\sim \mathcal N(0,\sigma_i^2),
\]
with learned \(\sigma_i^2\), or fixed unit variance, or something else? If unit variance is imposed regardless of scale, the score can be distorted across candidate graphs. This is not a cosmetic detail, because the whole search procedure in Section 4.2 depends on relative comparisons of these scores.

Relatedly, the notation in **Equations (3) to (5)** mixes graph scoring, data fitting, and training-set generation in a way that obscures what exactly is being optimized. In Eq. (3), AD is defined for a single candidate graph \(G_{train}^k\), while later text often talks about generating a set \(\{G_{train}^k\}_{k=1}^K\). In Appendix A, the alternative AD definitions average over \(K\) candidate graphs, which is inconsistent with the main-text definition. The paper would benefit from a clean separation between: (i) a score for one candidate graph, (ii) a search distribution over graphs, and (iii) the final procedure for selecting the \(K\) graphs used to train the SCL model. Right now, these layers bleed into one another.

The acceptance rule in the stochastic refinement procedure is too vague for reproducibility and for assessing soundness. In Section 4.2, the paper says candidates are “accepted with probability proportional to its score.” That is not a well-defined Markov transition rule. Probability proportional to a raw score is invalid if scores are negative, and the scores in Appendix E are indeed negative. If the intended rule is something like Metropolis-Hastings,
\[
\alpha = \min\left(1,\exp(\beta(\mathrm{score}(G')-\mathrm{score}(G)))\right),
\]
the paper should say so explicitly. If it is a softmax over local proposals, that should also be specified. As written, the algorithmic core is underdefined.

The claimed justification for sparsity is weaker than the paper suggests. **Equation (4)** uses \(\|A_G\|_0\) as a causal minimality regularizer, but causal minimality is not identical to mere edge-count minimization. Penalizing edge count is a reasonable heuristic, but the text on Pages 6 to 7 sometimes reads as if sparsity directly enforces causal minimality in a principled sense. That is too strong. In observational causal discovery, many non-minimal supergraphs can fit the data distribution under flexible mechanisms, but a plain \(L_0\) penalty does not by itself recover the minimal I-map without stronger assumptions. The paper should present this as a practical bias rather than a principled enforcement result.

There is a broader conceptual issue with the AD objective itself. The method scores candidate graphs by fitting mechanisms directly on the test dataset and then measuring how well the candidate explains that same dataset. This is, by design, a kind of test-time fitting, so the procedure is not “leaking labels,” but it does make the method much closer in spirit to score-based causal discovery than the framing sometimes acknowledges. **Table 4** is helpful here, because it shows the final supervised model improves over the highest-score graph, but the gains from seed graph to highest-score graph are already substantial. That raises the question of how much of the contribution comes from the new SCL paradigm versus a well-engineered, score-based refinement stage plus data augmentation. The paper tries to address this, but the distinction still feels somewhat under-argued.

The experimental section is strong in breadth, but weaker in experimental controls than I would like. The paper compares against AVICI (scm-v0) and a number of classical methods in **Table 2**, but it does not compare against a simpler adaptation baseline that would be very natural here, for example: initialize with NOTEARS or PC, generate synthetic data from that single fitted graph, and train the same backbone without the full stochastic search; or fine-tune the SCL model on self-generated data without AD-guided graph refinement. Without such baselines, it is harder to isolate whether the gain comes from test-time training as a paradigm, from graph search, or from the specific AD+sparsity objective.

The treatment of real data is a bit too optimistic given the evidence shown. **Table 1** is used to argue that synthetic success does not translate to real-world utility, and that part is reasonable. But the real-data evidence in the main paper is essentially Sachs plus Syntren. Sachs is a standard benchmark, but it is small and idiosyncratic, and Syntren is still synthetic. So the claim that current SCL practice is broadly invalidated for real-world application feels stronger than what the presented evidence can support. The paper has an interesting diagnosis, but the wording should be more measured.

There is also a fair-question issue around computational practicality. Appendix F reports about 26 minutes for 10 nodes, 61 minutes for 20 nodes, and 113 minutes for 30 nodes just for stochastic graph refinement, with an additional training stage on top. That does not invalidate the method, but it substantially affects usability. Since the whole point is per-test-instance retraining, computational cost is not a side note, it is central to whether the framework is viable. The main paper acknowledges this only briefly.

Some exposition choices make the paper harder to trust than necessary. For example, the text says “theoretical results confirm that finding the exact \(G_{test}\) is essentially impossible” in Section 4.2, but no theorem is stated in the main paper. The conclusion also says “our theoretical and empirical results underscore the effectiveness of AD,” yet the main paper provides no theorem proving that maximizing AD plus sparsity yields a graph closer to the truth under stated assumptions. If the theory lives outside the main text, then the claim in the main text should be toned down.

Finally, several details that materially affect interpretation are buried or inconsistent. In Section 3.1, the synthetic setup uses Gaussian noise for RFF/Chebyshev and uniform noise for Linear “to ensure identifiability,” which couples mechanism class and noise family in a way that complicates interpretation of shift results. In Appendix B, the component-mixed construction also appears to contain naming inconsistencies like “Linear_G_ER” and “Chebysev_U_ER,” which makes it harder to parse exactly what was excluded or included. These may be fixable presentation issues, but they matter because the paper’s early empirical claims are foundational for motivating the method.

## Questions
1. Please make the scoring function fully explicit. For **Equation (3)**, what exact probabilistic model is used to compute \(\log p(X_i\mid f_i^k)\)? Is the noise model Gaussian with learned variance, fixed variance, or estimated nonparametrically? A precise formula would substantially increase my confidence.

2. What is the exact transition/acceptance rule in the stochastic search of Section 4.2? “Accepted with probability proportional to its score” is not a valid algorithmic specification as written, especially since the reported scores in Appendix E are negative. Please provide the exact update rule and any temperature or normalization constants.

3. How are the \(K=200\) final training graphs selected? Are they the top-\(K\) scoring graphs, samples from the search trajectory, or the last \(K\) accepted states? This matters because the training distribution presented to the SCL model could differ substantially across these choices.

4. How sensitive are the results to \(\lambda\) in **Equation (5)**, to the number of refinement steps, and to the number of generated graphs \(K\)? Given the computational cost, a sensitivity plot would be very valuable.

5. Can the authors include a stronger decomposition baseline? In particular, I would like to see whether the gain over NOTEARS can be matched by simply generating training data from the single NOTEARS graph and retraining the backbone, without stochastic refinement. That would help isolate the contribution of the TACTIC search itself.

6. In **Table 4**, the “highest-score graph” already improves substantially over the seed graph. Can the authors report additional metrics for the highest-score graph, not just AUROC, and clarify whether the final SCL model is trained on one graph or a diverse set around that graph? This would clarify the added value of the supervised phase.

7. The claims around causal minimality and identifiability should be made more precise. Under what assumptions do the authors expect maximizing
\[
AD(G,D_{test})-\lambda \|A_G\|_0
\]
to recover a graph close to the true one? Even a proposition-level statement, with limitations, would help.

8. Since **Figure 2** is central to the motivation, please clarify whether all training settings use the same total number of training instances and whether hyperparameters are held fixed across i.i.d., shift, and component-mixed cases. This is important to rule out confounding by training budget rather than true compositional failure.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns requiring escalation are evident from the submission. The paper evaluates on standard causal discovery benchmarks and does not introduce an obvious privacy, fairness, or human-subjects issue in the presented form.

## Soundness Rating
3: good. The empirical evidence is substantial and the main claims are mostly supported, but the core optimization and scoring procedure are underspecified enough that I cannot rate soundness higher.

## Presentation Rating
3: good. The paper is readable and the high-level story is clear, with helpful figures and tables, but the mathematical and algorithmic exposition needs tightening.

## Contribution Rating
4: excellent. Despite the concerns above, I think the paper makes a meaningful contribution by reframing supervised causal learning around test-time, instance-specific data generation and by empirically demonstrating why that shift matters.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about specification of the AD score, the stochastic search rule, and the extent of the “causal minimality” interpretation. Still, the paper identifies an important weakness in current SCL practice, proposes a genuinely interesting alternative paradigm, and backs it up with broad empirical evidence, especially in **Figure 2** and **Tables 2 to 4**. On balance, I think this is a good and worthwhile paper for ICLR, though it is not yet polished enough for a stronger recommendation.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the broader causal discovery/SCL landscape, though some implementation-specific details are not recoverable from the main paper because the algorithm is under-specified.