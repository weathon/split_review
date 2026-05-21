---
job_id: 82e15e2e-206d-4a60-a43e-4aaa71ca6474
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IHyY6vdYZw.pdf
paper: VisualPRM400K: An Effective Dataset for Training Multimodal Process Reward Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on multimodal reasoning, reward modeling, test-time scaling, and the construction of datasets and benchmarks for learning-based critics.

## Minimum Quality
Pass ✅. The submission contains the core components expected of a research paper, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion, and it provides enough methodological and empirical detail to assess the main claims, even though several aspects remain underspecified.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces VisualPRM400K, a roughly 400K-sample multimodal process-supervision dataset for training multimodal process reward models, and VisualProcessBench, a human-annotated benchmark for step-level error detection in multimodal reasoning. Using these resources, the authors train VisualPRM, an 8B multimodal PRM, and show that it improves Best-of-N selection for several open-source MLLMs across seven multimodal reasoning benchmarks, while also outperforming ORM and self-consistency baselines in their setup.

## Strengths
The main strength is that the paper addresses a real gap. Process reward modeling and test-time scaling have become important in language-only reasoning, but multimodal counterparts are indeed much less developed. A dedicated multimodal process-supervision dataset plus a human-annotated benchmark is useful infrastructure for the community, assuming release and documentation are solid.

The paper is empirically broad. In **Table 2** on Page 7, the authors evaluate across seven multimodal reasoning benchmarks and multiple policy model families and scales, and the gains are not isolated to one backbone. The improvements on stronger models are especially helpful because they reduce the concern that the method only rescues weak policies. The reported +5.9 average gain for InternVL2.5-78B is a nontrivial result under the paper’s BoN setup.

I also appreciated that the paper does not stop at downstream BoN gains, but introduces a more direct benchmark for critic quality. **Table 3** on Page 8 is important here: it shows that many open-source MLLMs are poor step-level judges, often near random-guessing macro F1, which supports the paper’s core premise that “MLLM-as-a-judge” is not yet a strong critic for multimodal reasoning. This table does real argumentative work, it is not just decorative benchmarking.

The visual exposition is generally effective. **Figure 2** on Page 3 gives a concrete picture of both data construction and benchmark annotation, and it helps readers understand the distinction between the automatically generated training data and the human-annotated benchmark. **Figure 4** on Page 8 is also useful because it makes the scaling behavior visible: PRM improves more consistently than self-consistency and ORM as \(N\) grows. That figure strengthens the claim that process supervision gives a better critic for BoN than outcome-only scoring in this setting.

The paper includes several ablations rather than presenting a single headline number. **Table 4** on Page 8 compares value-based versus advantage-based PRMs, early-stop versus full-step supervision, and multiple aggregation rules. This is helpful because it tests design choices central to the method rather than burying them in implementation details.

Presentation is mostly clear at the high level. The modeling pipeline in **Figure 3** on Page 4 makes the distinction between value-based and advantage-based PRMs intuitive, and the paper is readable overall despite a large experimental scope.

## Weaknesses
1. **The central methodological contribution is useful but not especially well isolated from prior automatic process-supervision pipelines, and the paper overstates how much is new.**  
   The core data-generation idea in Section 3.1, Pages 4 to 5, is directly inherited from Monte Carlo continuation schemes used in prior language-only PRM work: sample continuations from a prefix, estimate expected future correctness, then supervise step quality. The multimodal extension is worthwhile, but the paper does not do enough to disentangle what is genuinely new beyond “apply the existing recipe to image-question reasoning and scale it up.” This matters because the headline contribution is largely a dataset-and-benchmark paper; for such papers, positioning and justification of why the extension is scientifically nontrivial are crucial. Right now, the paper mostly asserts that multimodal PRMs are underexplored, which is true, but it does not carefully articulate where multimodal process supervision creates qualitatively different challenges, failure modes, or labeling ambiguities compared with text-only PRMs.

2. **The automatic labeling rule is quite coarse and may introduce substantial supervision noise, but the paper does not analyze this noise rigorously enough.**  
   In Section 3.1 on Page 5, the expected accuracy is estimated by
   \[
   mc_i=\frac{\#\text{correct completions}}{\#\text{sampled completions}}.
   \]
   A step is then labeled correct if \(mc_i>0\). This is an extremely permissive criterion. With 16 sampled continuations, a single lucky completion implies “correct,” even if 15 completions fail. The paper later says higher thresholds hurt performance, but that is only shown in appendix-style ablations and not deeply analyzed in the main text. The issue is not merely cosmetic: this labeling decision defines the target for the entire PRM. If the supervision target conflates “salvageable prefix” with “correct step,” then the model is not really learning step correctness in the ordinary sense. The examples in **Figure 2** and **Figure 6** indirectly reveal this tension, where some steps with visibly garbled or low-quality local reasoning still receive nonzero expected accuracy because later continuations occasionally recover. The paper needs a clearer conceptual discussion of what is being supervised: local correctness, future recoverability, or some mixture of the two.

3. **The mathematical formulation and inference procedure are underspecified in several places.**  
   There are a few concrete issues here:
   - In Section 3.1, Page 5, the notation says \(mc=\{mc_0,\ldots,mc_n\}\), \(mc_i\in\mathbb{R}_{\ge 0}\), but since Equation (2) is a fraction of correct completions, the range should really be \(mc_i\in[0,1]\). This is minor, but the sloppiness propagates into the interpretation of the target.
   - The statistics paragraph on Page 5 says they “compute \(m_i\)” from continuations, which looks like a typo for \(mc_i\). Again minor, but this section should be tighter since it defines the dataset.
   - More importantly, Equation (3) on Page 5 writes
     \[
     y_i \sim M(y_i \mid I,q,s_{\le i}),
     \]
     but the actual training loss is never specified. Is this standard next-token cross-entropy on the discretized label token? Are labels generated only at the assistant position after each turn? Are all previous conversation tokens masked out from the loss? Since the model is trained as a multi-turn chat, these details matter.
   - The inference rule is also too vague. The paper says the step score is “the weighted sum of the generation probability for the discretized scores.” But it does not specify whether this uses token-level probabilities at the first generated token only, whether alternative verbalizations are allowed, whether probabilities are normalized over the full vocabulary or only over the label subset, or how prompt formatting affects calibration. For a paper centered on critic scoring, this is not a detail that can be hand-waved away.

4. **The benchmark metric description is internally inconsistent and raises evaluation clarity concerns.**  
   In Section 3.3 on Page 6, the paper says it uses macro F1 by averaging the F1 for correct and incorrect steps. But the caption of **Table 3** on Page 8 says “The overall score is the micro average of the score from different data sources.” Those are not the same thing. I can guess the intended meaning, perhaps macro over classes and then micro or weighted aggregation over datasets, but the paper should not leave this ambiguous. This matters because the benchmark’s main claim is that existing MLLMs are close to random, so the exact aggregation procedure affects how strong that statement really is.

5. **The experimental comparisons are strong in breadth, but they are narrower than the paper suggests in terms of critic baselines.**  
   The main comparisons in Section 4 emphasize self-consistency, ORM, and a few MLLM judges. Those are reasonable, but for a paper making a larger point about critic models for multimodal BoN, the baseline space is still a bit thin. In **Figure 1** on Page 2, the visual message is essentially “InternVL2.5-8B is a weak critic, VisualPRM is better,” which is fine as a motivating figure, but it is also a rather friendly framing. The paper would be more convincing if the main text included stronger multimodal reward-model baselines rather than mostly comparing against self-consistency, ORMs derived from nearly the same data, and generic prompted MLLMs. As written, part of the gain may come from comparing a specialized verifier against baselines not optimized for this role.

6. **The reported improvements are promising, but the paper does not adequately separate critic quality from candidate-generation effects.**  
   Section 4.1 on Pages 6 to 7 fixes generation temperature and uses \(N=8\) by default, and later **Figure 4** and **Tables 8-9** show scaling with \(N\). That is useful, but the policy generation process still exerts a large influence on BoN outcomes. The paper itself notes this issue in the introduction, yet the experimental design only partially resolves it. In particular, it would help to report critic evaluation on the exact same candidate pools across all critics, with pairwise agreement and rank-correlation analyses, not just final task accuracy after selection. Otherwise, downstream BoN gains are still a somewhat entangled measure of candidate diversity, critic sharpness, and benchmark sensitivity.

7. **The benchmark construction and annotation process are useful, but quality control is described too loosely for a benchmark paper.**  
   On Page 6, the authors state that 13 annotators worked for 3 days, with authors reviewing about 10% of samples per split and sending problematic splits for re-annotation. That is a start, but it is not enough detail for a benchmark whose labels are treated as ground truth. There is no inter-annotator agreement statistic, no description of adjudication protocol, no per-domain difficulty analysis in the main paper, and no estimate of disagreement rates on positive versus negative labels. Since the benchmark is later used to claim that open-source MLLMs are weak critics, label reliability matters a lot.

8. **The use of all-step supervision is claimed to be better, but the explanation is not fully convincing.**  
   In Section 3.2 and **Table 4** on Page 8, supervising all steps performs better than early stopping. This is plausible, especially with reflection and self-correction, but the current interpretation feels a bit too easy. If later steps can recover from earlier ones, the benchmark label semantics become more subtle: are later steps judged relative to the current local statement, relative to the final answer, or relative to logical consistency with prior steps? The examples in **Figure 8** on Page 27 highlight exactly why this is tricky. The paper is right to move beyond “first error only,” but then it also needs a more careful formalization of what a correct later step means after an earlier mistake.

9. **Some tables and figures reveal instability or interpretation gaps that the paper does not discuss enough.**  
   - In **Table 10** on Page 19, adding 44K rollouts from Qwen2.5-VL slightly hurts both BoN and VisualProcessBench relative to the base dataset, while adding MiMo-VL helps. This is actually interesting, but the paper leaves it at “more diverse rollouts help,” which is not quite supported by the table. Apparently, diversity helps only when the extra rollout source is good in the right way.
   - In **Table 11** on Page 20, gains saturate quickly beyond 9 steps. That suggests either the long-tail step supervision is not very informative, or the current model/prompting cannot exploit it well. Again, interesting, but under-discussed.
   - In **Figure 5(b)** on Page 20, step error rates increase with step index, then become highly unstable for later positions. That figure supports the authors’ criticism of max aggregation in **Table 4**, but it also suggests a possible positional bias in the critic or benchmark that deserves a direct discussion.

10. **The ethics section is too casual for a paper involving human annotation and redistributed benchmark content.**  
    The statement on Page 10 says human annotation is “unrelated to any ethical concerns,” which is simply too glib. Human annotation is not automatically unethical, but it is absolutely ethically relevant. The paper should discuss annotator compensation, consent, instructions, and data governance more carefully. The reported compensation, about 37 USD per person-day on Page 6, also deserves contextualization. In addition, the paper says the dataset and benchmark are built from publicly available datasets, but does not specify licensing compatibility for redistribution of images and annotations. For a release-oriented paper, that omission is not ideal.

## Questions
1. Please clarify the exact training loss for Equation (3). Is the model trained with next-token cross-entropy on a single label token per turn, and if so, how are conversation tokens masked? A precise formulation would substantially increase confidence in reproducibility.

2. For the value-based PRM, why is the binary target defined as \(\mathbf{1}[mc_i>0]\) rather than, for example, \(\mathbf{1}[mc_i>\tau]\) with a calibrated \(\tau\), or even direct regression to \(mc_i\)? The current rule seems to collapse a wide range of prefix qualities into the same positive label. A concise analysis of the label-noise tradeoff in the main paper would help.

3. Please reconcile the metric description for VisualProcessBench. Is the reported “Overall” in **Table 3** computed by macro-averaging over positive/negative classes and then micro-averaging over datasets, or something else? Right now, Section 3.3 and the table caption appear inconsistent.

4. Can the authors provide a direct estimate of supervision noise by manually auditing a random sample of VisualPRM400K labels against human step-level judgments? Even a few hundred manually checked steps would help quantify how closely \(mc_i>0\) aligns with actual local step correctness.

5. What exactly counts as a “correct completion” when computing Equation (2)? Is correctness determined only by the final answer, regardless of whether the continuation contains additional incorrect intermediate steps? This is important because the label semantics change substantially depending on this choice.

6. For **Table 2**, were all critics evaluated on the same candidate sets for each policy model and example? If not, some of the differences could be due to candidate-pool variation rather than critic quality. Please clarify.

7. On the benchmark side, can the authors report inter-annotator agreement, or at least agreement on a subset with double annotation? Since the paper’s claims about critic weakness hinge on VisualProcessBench, stronger evidence of label reliability would materially improve confidence.

8. In **Table 10**, why do Qwen2.5-VL-derived extra rollouts slightly hurt performance while MiMo-VL-derived rollouts help? This looks like a useful clue about what kinds of rollout diversity matter. A short analysis would strengthen the data-construction story.

9. The paper claims that VisualPRM computes all step scores in a single forward pass by using “+” as a placeholder. Please clarify exactly how step boundaries are represented in the input and where the label probabilities are read out. This is an implementation detail, but here it is also central to the method’s efficiency claim.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The paper involves human annotation for VisualProcessBench, described on **Page 6**, but the ethics statement on **Page 10** dismisses this as unrelated to ethical concerns. I do not agree with that framing. The annotation protocol, consent, compensation, and quality-control process are part of responsible research practice and should be described more carefully. The reported compensation, about 37 USD per person-day, should be contextualized.

There is also a dataset release aspect. The paper states that data are drawn from publicly available multimodal benchmarks and that model, data, and benchmark will be released, but it does not specify whether redistribution of the original images and derived annotations is permitted under the source dataset licenses. For a release-centered contribution, licensing and redistribution conditions should be made explicit.

## Soundness Rating
2: fair. The empirical evidence is substantial and the overall direction is plausible, but several core details of the training objective, inference scoring, label semantics, and benchmark metric are underspecified enough that I cannot rate soundness higher.

## Presentation Rating
3: good. The paper is readable and generally well organized, with effective figures and broad experiments, but there are important ambiguities in notation, metric definition, and methodological detail that need tightening.

## Contribution Rating
3: good. A large multimodal process-supervision dataset plus a benchmark for step-level multimodal critic evaluation is valuable to the community, and the downstream gains are meaningful. That said, the conceptual novelty beyond adapting known PRM machinery to the multimodal setting is moderate rather than strong.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
The paper makes a useful community contribution through the dataset, benchmark, and reasonably broad empirical study, and the downstream gains are strong enough that I can see it being accepted. Still, the work is held back by underspecified methodology, somewhat loose benchmark/evaluation definitions, limited analysis of label noise, and not enough careful isolation of what is truly new versus what is inherited from prior PRM pipelines.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the main experimental claims and methodological formulation carefully, but some implementation-level details are missing from the paper, which limits full verification.