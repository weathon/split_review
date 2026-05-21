---
job_id: 5f08509e-5b96-4628-acb8-ba4be0e6dcef
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FF9QVQduAu.pdf
paper: Towards a Foundation Model for Crowdsourced Label Aggregation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on transfer learning, graph-based learning, representation learning, and general machine learning through a pretrained GNN for crowdsourced label aggregation.

## Minimum Quality
Pass ✅. The submission contains all core scientific sections, including abstract, introduction, methodology, related work, experiments, quantitative results, and conclusion, and it provides enough technical and empirical content to warrant full review despite several important weaknesses.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious content targeting automated reviewers in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes CrowdFM, a pretrained graph-based model for crowdsourced label aggregation. The method uses a synthetic data generator based on randomized crowdsourcing scenarios and a bipartite GNN over workers, tasks, and label options, with the goal of zero-shot deployment on unseen datasets without per-dataset retraining. Experiments on 22 real-world datasets compare CrowdFM against majority voting and several dataset-specific baselines, and the paper also explores downstream uses of the learned representations for worker/task assessment and task assignment.

## Strengths
The paper addresses a real and important practical gap in crowdsourcing, namely the tension between simple but transferable methods like majority voting and stronger but dataset-specific methods that must be refit from scratch. Framing label aggregation as a pretraining-and-transfer problem is a sensible direction, and the retraining-free deployment goal is relevant for real applications.

The empirical scope in the main paper is fairly broad. Evaluating on 22 real-world datasets is a meaningful effort, and the paper does not rely on one or two curated success cases. In **Figure 2** on Page 6, the per-dataset comparison against MV is particularly useful because it makes the transfer story more concrete than a single average number would. The figure shows that gains are not confined to one modality or one dataset scale, and it is helpful that the authors also expose the one small failure case on Senti rather than hiding it.

The comparison table is also a strength. **Table 1** on Page 6 gives a useful joint view of win count, average accuracy, runtime, and signed-rank test results. This is more informative than reporting only mean accuracy. In particular, the runtime comparison strengthens the practical case for the method: CrowdFM is not just another heavier deep model that wins by brute force inference cost. The fact that it remains much faster than several deep or iterative baselines matters for the claimed deployment scenario.

The model design is intuitive at a high level. Explicitly representing workers, tasks, and options rather than flattening everything into annotation-level nodes is a reasonable architectural choice for crowdsourcing data. The overall pipeline shown in **Figure 1** on Page 3 is easy to follow and does a good job summarizing the three-stage story: synthetic generation, pretraining, and downstream adaptation.

The paper goes beyond the core aggregation benchmark and attempts to show that the learned representations are reusable. Even though I have concerns about the setup, it is still a positive that the authors try to test representation quality in additional ways rather than stopping at one benchmark table.

## Weaknesses
1. **The novelty claim is overstated, and the paper does not sharply distinguish itself from prior graph-based cross-dataset aggregation work.**  
   The paper repeatedly positions CrowdFM as a “foundation model” for crowdsourced aggregation, but in the main paper the technical delta over prior cross-dataset GNN aggregation appears narrower than the rhetoric suggests. The authors discuss HyperLM in the introduction and related work, but the core recipe here, synthetic data generation plus graph encoder plus shared predictor plus zero-shot transfer, is conceptually quite close to an existing pretrain-on-synthetic / deploy-on-unseen-datasets template. The main paper argues that HyperLM lacks explicit worker-task modeling and realistic synthetic data, which is fair, but that is still closer to an architectural/domain adaptation than a clearly new learning paradigm.  
   More importantly, the paper’s related work on crowdsourcing GNNs is incomplete in the main text. On Page 10, the “Label Aggregation” section cites several classical and deep methods, but the positioning against earlier heterogeneous/bipartite GNN approaches for crowdsourced label aggregation is not sufficiently developed. This matters because the claimed contribution depends heavily on whether CrowdFM is genuinely introducing a new transferable formulation, or mainly reassembling existing ingredients with a stronger simulator. Right now, the paper leans too hard on the “foundation model” label without fully earning it.

2. **The synthetic-to-real story is plausible but not convincingly validated from the main paper alone.**  
   The central premise is that pretraining on synthetic data induces transferable aggregation rules, yet the real-world validity of the generator is mostly asserted rather than established in the main text. Section 3.1 on Pages 3 to 4 specifies a generator based on randomized 3PL-style workers/tasks plus heavy-tailed load and Poisson assignment, but there is a nontrivial gap between these assumptions and actual annotation behavior. Real crowdsourcing often contains class-dependent confusions, worker subpopulations, adversarial annotators, temporal drift, interface effects, abstention, and worker-task topical affinities, none of which are modeled here.  
   The paper does mention domain randomization and claims realism, but the main paper does not quantify how much of the empirical performance comes from broad randomization versus specific assumptions of the 3PL simulator. The ablation in **Figure 6(a)** on Page 9/10 shows that removing the synthetic generator hurts average accuracy, but this only demonstrates that the chosen generator is better than a very weak uniform generator. It does not establish that the simulator is sufficiently realistic, only that it is less unrealistic than the comparison. Since the whole foundation-model claim rests on the synthetic pretraining distribution \(p_{\mathcal D}\) in **Equation (2)**, this missing validation matters a lot.

3. **Several equations in the encoder are underspecified or imprecise enough that reproducing the exact model from the main paper would be difficult.**  
   The biggest issue is the attention formulation on Pages 4 to 5. In **Equation (7)**, the paper writes
   \[
   \alpha^{(l)}_{ij}=\operatorname{softmax}\left(\frac{\langle q_{ij},k_{ij}\rangle}{\sqrt d}\right),
   \]
   but this scalar self-dot-product-style expression is unusual as written. Attention normally requires a query from the center node and keys from neighbors, with a clear normalization set. Here, both \(q_{ij}\) and \(k_{ij}\) are derived from the same triple representation \(h^{(l)}_{ij}\), so the equation reads more like a learned per-edge score than standard attention. That could be fine, but then the paper needs to say explicitly over which index set the softmax is taken for worker-centered versus task-centered updates, and whether separate normalizations are used for each node type. The sentence below **Equation (7)** says normalization is “over all annotations incident to the same center node,” but there is no center-node index in the notation, which makes the update ambiguous.  
   Relatedly, **Equation (8)**,
   \[
   z^{(l+1)}=\operatorname{LayerNorm}\left(z^{(l)}+\sum_{(i,j)\in\mathcal N}\alpha^{(l)}_{ij}v_{ij}\right),
   \]
   suppresses the worker/task index entirely. As written, it is not a valid node-wise update rule because \(z^{(l+1)}\) could refer to either a worker embedding or a task embedding, and \(\mathcal N\) changes depending on which node is being updated. This is not just notation nitpicking, because the architecture’s core contribution is exactly the message-passing mechanism. The paper should write explicit updates such as \(z^{(l+1)}_{w_i}\) and \(z^{(l+1)}_{t_j}\), with separate neighborhood definitions and attention normalizations.  
   There is also a subtle issue in **Equation (5)**: the option embedding appears as \(z_{a_{ij}}\) rather than \(z^{(l)}_{a_{ij}}\), which suggests it is fixed across layers, but the paper never explicitly states whether option embeddings are trainable parameters only, or graph nodes updated by message passing. Since the method is described as explicitly modeling workers, tasks, and options, this omission is important.

4. **The size-invariant initialization is elegant in slogan form, but it risks relying on arbitrary symmetry breaking through random option embeddings, and the paper does not analyze this.**  
   In **Equation (4)** on Page 4, all workers share the same initial vector \(x_w\), all tasks share the same \(x_t\), and option nodes are initialized from a Gaussian distribution. The argument is that workers and tasks are indistinguishable before observing annotations. Fine, but then option identity is effectively anchored by random draws. This raises at least two questions that the paper never addresses. First, how sensitive is zero-shot performance to the random seed used for option initialization? Second, for datasets with permuted label identities, is the model truly invariant to option relabeling, or does it partially memorize synthetic option geometry induced by pretraining?  
   This matters because the predictor in **Equations (9) and (10)** scores each task-option pair by concatenating \(z_{t_j}\) and \(z_{o_k}\). If \(z_{o_k}\) is not semantically grounded and is merely a random code, then the model’s behavior depends on how consistently label indices align across datasets. For a paper emphasizing universality across datasets with varying numbers of categories, this is not a small detail. At minimum, an ablation comparing random option embeddings, learned shared option embeddings, and permutation-invariant scoring would help.

5. **The reported empirical story is somewhat less impressive than the headline suggests once one reads the full table carefully.**  
   The paper’s narrative strongly emphasizes beating bespoke methods, but **Table 1** on Page 6 actually shows a more mixed picture. CrowdFM has the highest win count against MV, which is good, but its average accuracy is **83.41**, which is below **EBCC at 84.08** and only slightly above **BWA at 83.31**, **CATD at 83.06**, and **DS at 83.02**. The text acknowledges this, but still phrases the results as “consistently matches or surpasses bespoke, per-dataset methods” in a way that feels a bit too triumphant. In reality, the main quantitative conclusion is narrower: CrowdFM is competitive on average, stronger on win count, and attractive in efficiency because it avoids per-dataset retraining. That is still a useful result, but it is not the same as clearly outperforming the best dataset-specific methods.  
   There is also a fairness issue in the statistical reporting. The Wilcoxon test in **Table 1** compares each baseline against CrowdFM, but only one-sided \(p\)-values are shown, and the directionality is not always carefully interpreted in the prose. For methods like EBCC and BWA, where the average accuracy is very close or slightly higher, the one-sided test is not very illuminating unless the null and alternative are explicitly stated. The paper should report the exact alternative hypothesis and ideally include two-sided tests or effect sizes.

6. **The downstream adaptation section is interesting, but methodologically weak as evidence for “foundation model” representations.**  
   Section 4.3 on Pages 7 to 9 is one of the selling points of the paper, yet the setups are not fully convincing. For worker/task assessment, the regressors in **Equation (13)** are trained on synthetic data using synthetic ground-truth ability \(\theta_i\) and difficulty \(\beta_j\), then evaluated on the Web dataset using worker accuracy and task error rate as proxies. This is, at best, an indirect validation. Worker accuracy and task error rate are not the same latent variables as IRT ability and difficulty, so strong correlation in **Figures 3 and 4** is suggestive, not definitive. The moderate values in **Figure 4**, especially the worker ability proxy correlation around Pearson \(=0.449\), are decent but far from a slam dunk.  
   The task assignment evaluation in **Figure 5** on Page 8 has similar issues. The predictor strategy uses ground-truth correctness to train the compatibility head in **Equation (14)**, but real deployment would usually not have this supervision for the target dataset. The text says these heads are trained once and then directly deployed on new datasets, but the main paper does not make clear what the training data for these heads is in the real-data experiments, how much supervision is used, or how distribution shift is handled. This ambiguity weakens the claim that CrowdFM “readily supports” downstream applications in a practical retraining-free workflow.

7. **Ablations are too shallow relative to the central claims.**  
   The ablation section on Page 10 is directionally useful but limited. **Figure 6(a)** only removes attention or replaces the synthetic generator with a uniform random one. This does not isolate which parts of the simulator matter, whether the 3PL response model is necessary, whether the heavy-tailed assignment model matters, or whether the gains come mostly from simple pretraining scale rather than simulator realism. **Figure 6(b)** and **Figure 6(c)** only vary depth and dimension, which is standard hygiene, not deep evidence.  
   Given the paper’s main claims, I would have expected at least: (i) an ablation on the worker/task/option graph design versus simpler bipartite encodings, (ii) an ablation on option embedding choices, (iii) an analysis of zero-shot robustness outside the synthetic ranges in **Table 2** on Page 17, and (iv) a comparison between frozen zero-shot inference and lightweight target-dataset adaptation, to clarify where the fixed model sits in the accuracy/efficiency tradeoff.

8. **Some important experimental details are deferred away from the main paper, leaving the main-text evidence thinner than it should be.**  
   The paper says the model is trained on dynamically generated synthetic datasets, but the main paper does not specify key training quantities such as the number of synthetic datasets seen, batch composition across different \(K\), validation/selection procedure for hyperparameters, or sensitivity to generator ranges. Because the entire contribution depends on pretraining over a dataset distribution, these are not merely appendix details. If the method is meant to be a reusable foundation model, the training protocol is part of the contribution, not an implementation footnote.

## Questions
1. Please clarify the encoder mathematically. For **Equations (7) and (8)**, what is the exact center node for each attention score, and over which set is the softmax normalized? I would like to see explicit node-wise updates, for example \(z^{(l+1)}_{w_i}\) and \(z^{(l+1)}_{t_j}\), rather than the current shorthand. A precise clarification here would increase my confidence in the technical soundness.

2. Are option embeddings updated during message passing, or are they fixed trainable parameters used only in the predictor? **Equation (5)** uses \(z_{a_{ij}}\) without a layer index, which suggests the latter, but the text implies workers, tasks, and options are all represented in the graph. Please state the exact design.

3. How sensitive is performance to the random initialization of option embeddings in **Equation (4)**? A rebuttal with a seed-sensitivity analysis, or a permutation-invariance argument, would help address concerns that label-option geometry is arbitrary rather than learned in a robust way.

4. The paper’s main conceptual claim depends on the realism of the synthetic generator. Can the authors provide a sharper main-text justification for why the 3PL-based simulator is appropriate for the 22 datasets considered, and whether the method remains strong under synthetic generators that include worker-specific confusion patterns, adversaries, or class-dependent biases beyond random incorrect labels?

5. For **Table 1**, please clarify the exact null and alternative hypotheses for the one-sided Wilcoxon signed-rank tests. I would also encourage reporting two-sided tests or effect sizes. Since EBCC has a slightly higher average accuracy than CrowdFM, the current significance discussion is easy to misread.

6. For the downstream adaptation experiments in Section 4.3, what data are the downstream heads trained on, exactly? If they are trained on synthetic data and evaluated zero-shot on real data, please make that completely explicit for both the assessment and assignment settings. If any real labels or ground truth were used, please specify where and how. This point could materially change my interpretation of the “retraining-free” claim.

7. Can the authors provide stronger evidence that the contribution is not mainly due to the simulator rather than the architecture, or vice versa? A factorial ablation would help, for example: realistic simulator + attention GNN, realistic simulator + simpler encoder, uniform simulator + attention GNN, and perhaps realistic simulator + non-graph baseline.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses synthetic pretraining data and publicly available crowdsourcing datasets, and I did not identify a concrete ethics issue in the main paper that would require escalation. That said, if the method were deployed for worker ranking or exclusion, there could be fairness concerns in practice, but the paper does not present such deployment claims in enough detail to justify a formal ethics flag.

## Soundness Rating
3: good. The overall methodology is plausible and supported by a substantial empirical study, but the mathematical specification of the encoder is not precise enough in the main paper, and several core claims, especially around synthetic realism and downstream adaptability, are only partially supported.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are useful, but several key equations and experimental details are underspecified, and the novelty positioning is too vague relative to prior graph-based aggregation work.

## Contribution Rating
3: good. I do think the paper makes a meaningful contribution by pushing retraining-free crowdsourcing aggregation in a practical direction and by providing extensive multi-dataset evidence. However, the contribution is more “solid systems-and-empirical step forward” than the stronger “foundation model” framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important problem and backs its claims with fairly broad experiments, useful figure/table evidence, and a competitive zero-shot method that looks practically relevant. My reservation is that the novelty is somewhat overstated, the encoder math is not fully nailed down in the main paper, and the downstream/foundation-model claims are stronger than the evidence currently supports.

## Reviewer Confidence
4: confident. I am confident in the main assessment and familiar with the crowdsourcing / aggregation / graph-learning landscape, though there is still some uncertainty because parts of the encoder specification are too compressed in the main paper.