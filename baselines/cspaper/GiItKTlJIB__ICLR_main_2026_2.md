---
job_id: 8c6629ef-b399-4710-a8b7-a7935b8c1d8a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GiItKTlJIB.pdf
paper: How Much Chain-of-Thought Do LLMs Really Need for Physics?
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper clearly fits ICLR scope through reasoning evaluation for LLMs, interpretability/faithfulness of learned reasoning traces, and applications to physical sciences.

## Minimum Quality
Pass ✅. The submission contains the core components expected of a research paper, including abstract, introduction, problem setup/methodology, experiments, analysis/results, related work, and conclusion. While I have substantial concerns about novelty, evaluation rigor, and clarity of some methodological details, these are review-level weaknesses rather than desk-rejection-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious prompt injection text, or other manipulative content targeting automated reviewers in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies whether chain-of-thought (CoT) is actually needed for physics problem solving by LLMs. The authors propose a deletion-based framework that intercepts generated CoT, removes parts of it under several strategies, and then measures the effect on judged answer quality, answer length, and lexical overlap between deleted content and regenerated final answers. Experiments on three open models and three physics benchmarks suggest that performance is often robust to moderate CoT deletion, while final answers become longer and partially reconstruct missing content, which the paper interprets as evidence of shallow or opportunistic reliance on CoT.

## Strengths
The paper asks a timely and important question. There is a lot of discussion around “reasoning models,” but much less work that tests whether the visible scratchpad is functionally necessary. Focusing this question on physics is sensible because the domain contains structured content, equations, units, and explicit derivations, which makes failure modes more inspectable than in many generic reasoning benchmarks.

The empirical setup is fairly broad. The paper evaluates three models and three datasets, and it does not rely on only one perturbation style. The comparison across end deletion, random deletion, and physics-aware deletion is a useful design choice because these interventions stress different kinds of redundancy in the CoT.

Figure 1 is a helpful overview of the experimental pipeline. It makes the intervention point quite clear: the model first generates a reasoning trace, the trace is manipulated, and then the final answer plus downstream metrics are collected. For a paper built around a procedural intervention, this high-level diagram materially improves readability.

Some of the main behavioral patterns are visually communicated well. In particular, Figures 4, 5, and 6 together support the paper’s central qualitative claim that moderate deletion does not immediately collapse performance, while answer length tends to increase. The “X-shaped” interpretation is a bit rhetorically dramatic, but the plots do show a recurring pattern where score trends downward and answer length trends upward as deletion increases.

The overlap analysis in Section 4.2 is a reasonable first attempt to operationalize “recovery” of deleted content. Equation (1) and Equation (2) are simple, but at least the paper does not stop at anecdotal examples and instead tries to quantify reconstructed content across deletion sweeps. Figure 7 also usefully shows that these recovery patterns differ by deletion strategy, which is more informative than just reporting a single average overlap number.

The calibration study, while modest, is directionally helpful. Figure 8 gives some evidence that the authors at least attempted to justify the number of repeated runs rather than choosing it arbitrarily.

## Weaknesses
1. **The main contribution feels methodologically thinner than the paper claims, and the novelty relative to prior CoT-faithfulness work is not well established.**  
   The core idea, delete or perturb intermediate reasoning and inspect downstream robustness, is intuitive and already close in spirit to existing faithfulness/intervention-style evaluations discussed in the paper itself, especially Lanham et al. (2023), Turpin et al. (2023), and Lyu et al. (2023). What is new here appears to be mainly the application to physics benchmarks plus a particular combination of deletion sweeps and overlap metrics. That can still be publishable if the domain-specific insight is strong, but the paper overstates the methodological novelty of the “systematic deletion framework.” As written, Sections 1 and 2 do not sharply identify what this framework enables that prior perturbation-based faithfulness analyses could not already test. This matters because the paper’s claims of contribution rest heavily on the framework itself, yet much of it reads like a straightforward adaptation rather than a clearly differentiated method.

2. **The central causal claim, that robustness under deletion implies weak dependence on CoT, is suggestive but not actually nailed down by the experimental design.**  
   The intervention removes visible tokens from the scratchpad after they have already been generated. That means the model has already computed hidden states while producing those tokens. If the model internally encoded relevant information before the deletion point, then downstream robustness does not necessarily show that the CoT was unused or unfaithful; it may only show that the *surface text* of the already-generated CoT was not required after the intervention. This is a crucial distinction, and the paper only gestures at it in the limitations section. Figure 1 actually makes this concern sharper, because the pipeline explicitly intervenes after CoT generation rather than before the model reasons. So the paper often slides between “visible CoT text is not required at decode time” and “the model does not genuinely depend on its reasoning trace,” which are not equivalent claims. This affects the scientific value because the paper is framed around faithfulness, but the experiment more directly measures post-hoc dependence on the emitted scratchpad.

3. **The evaluation metric is too weakly specified and potentially too noisy for the paper’s conclusions.**  
   Section 2.4 says “Score” is assigned by Claude-4 Sonnet on a 0–1 scale based on correctness, derivation accuracy, logic, formatting, and clarity. This mixes several different axes into one scalar and delegates the main quantitative result to an LLM judge. Critical details are missing: the exact rubric, whether the judge sees the prompt only or also the original CoT, whether judgments are deterministic, whether pairwise or direct scoring is used, whether any calibration against ground-truth exact-answer accuracy was performed, and how sensitive the conclusions are to the inclusion of presentation factors like “formatting” and “clarity.” For physics, answer correctness is often objectively checkable, at least for many numerical or formulaic questions, so relying mainly on an opaque composite judge score weakens the claims. This matters especially because many reported effects in Figures 2, 3, 4, 9, and 12 look moderate rather than dramatic; with a subjective evaluator, small score differences are hard to interpret.

4. **The paper gives almost no dataset-level or task-level evaluation detail, which makes it hard to judge external validity.**  
   Section 2.1 provides only high-level descriptions of UG Physics, PhysReason, and PhyBench. There is no clear statement of how many examples from each benchmark were actually used in the main experiments, whether subsets were sampled, whether tasks are multiple-choice or free-response, how expected answers are formatted, or how problems of different types were handled under a single judging rubric. This is not a minor reporting issue. If one dataset contains many short factual questions and another contains derivation-heavy problems, the meaning of CoT deletion robustness differs dramatically. The plots in Figure 3 and Figure 7 average over these benchmarks, but the paper gives too little information to interpret what those averages represent.

5. **The “physics-aware deletion” pipeline is underspecified and introduces another opaque model into the loop.**  
   On Page 6, the authors say that Claude-4 Sonnet identifies physics-related tokens such as equations, constants, and unit conversions for deletion. But the method is not defined precisely. Are spans selected at token level or phrase level? Are equations deleted atomically or token-by-token? How are overlaps handled between annotated and non-annotated regions? What prompt is used to label spans? How consistent is the annotator across problems and models? Without a formal definition, the comparison between “annotated” and “non-annotated” deletion in Figure 3 is difficult to interpret. If the annotation model preferentially selects more salient or later-occurring spans, the observed larger degradation may partly reflect annotation bias rather than true physics-specific necessity.

6. **The overlap metrics in Equation (1) and Equation (2) are very blunt instruments for the paper’s notion of faithfulness.**  
   Equation (1) defines Jaccard similarity on unique token sets, and Equation (2) defines Manhattan distance on bag-of-words counts. These can detect lexical reuse, but they do not meaningfully distinguish faithful regeneration from superficial paraphrase, equation reformulation, algebraic equivalence, unit conversion, or symbol renaming. In physics, two derivations can be semantically identical with low lexical overlap, or lexically similar while being mathematically wrong. The paper partly acknowledges this, but then still interprets Figure 7 as evidence of “recovery” and “surface-level agreement.” The latter may be true, but the metrics are too weak to support stronger conclusions. A more domain-aware matching scheme for equations, units, and numerical values is needed if the paper wants to make scientific claims about recovery of structured reasoning rather than just text reuse.

7. **The paper’s mathematical presentation is serviceable but incomplete, and key constructs are not formally defined.**  
   For example, in Section 4.2 the overlap is described as the intersection between “the original CoT prior to deletion” and “new content generated in the final answer across deletion sweeps,” but the exact preprocessing pipeline behind \(V(p)\) and \(\mathrm{bow}(p)\) is omitted. What is a token here, whitespace tokenization, model tokens, regex-based physics tokens, lowercased wordpieces? Are stopwords removed? Are equations tokenized symbolically? Is Manhattan distance normalized by passage length or vocabulary size before the “scaled metric value” shown in Figure 7? Since Manhattan distance naturally increases with text length, and answer length also increases under deletion, some of the trend in Figure 7 may simply reflect verbosity rather than recovery. This is an important issue because the overlap analysis is one of the paper’s main pieces of evidence. At minimum, the paper needs to define a normalized distance such as
   \[
   \tilde D_{\text{Manhattan}}(p_1,p_2)=\frac{1}{\sum_i \mathrm{bow}(p_1)_i+\sum_i \mathrm{bow}(p_2)_i}\sum_i \left|\mathrm{bow}(p_1)_i-\mathrm{bow}(p_2)_i\right|,
   \]
   or another length-controlled alternative, and explain exactly what “scaled” means in Figure 7.

8. **Several claims are visually stronger in the text than in the figures.**  
   The paper repeatedly says accuracy remains stable until around \(40\%\) deletion for end deletion and \(60\%\) for random deletion. But looking at Figures 4, 5, 6, 9, and 11, the picture is more heterogeneous across models and datasets. Some curves drift noticeably earlier, some have wide uncertainty bands, and some datasets, especially UG Physics in several panels, look noisy enough that the threshold language feels too crisp. The red dotted lines in Figures 4 and 9 give an impression of clean phase transitions, but the empirical story is messier. I would urge the authors to stop overselling threshold points and instead report uncertainty-aware model/dataset-specific ranges.

9. **The presentation around figures is occasionally inconsistent or sloppy, which undercuts confidence.**  
   There are multiple figure-numbering and labeling issues in the appendix pages. On Page 14, Figure 9 and Figure 10 are both described as “under end deletion,” despite the section being random deletion sweeps and Figure 11 referring to random deletion. On Page 15, the text in Section 4.1 says “Figure C,” which is clearly a broken reference. These are not fatal, but in a paper centered on careful experimental intervention, such mistakes make it harder to trust that all conditions were implemented and reported with similar care.

10. **No results tables are provided, which is a real usability problem for a paper making comparative empirical claims.**  
   All main results are shown only as plots. That is fine for trends, but it is poor for precise comparison. For example, Figure 2 visually suggests that full reasoning often improves judged quality across the two shown datasets and three models, but there is no table reporting the actual mean scores, variances, or effect sizes. Likewise, Figure 3 compares deletion of annotated vs non-annotated content, but without tabulated values it is hard to assess how large those gaps really are and whether they are practically meaningful. Given that the paper’s claims hinge on relative degradation and robustness ranges, compact results tables would substantially improve auditability.

11. **The paper does not do enough targeted error analysis to support the interpretation of “cramming.”**  
   Increased final answer length is suggestive, but longer answers do not by themselves prove reconstruction of deleted reasoning. A model might hedge, ramble, restate the prompt, or emit generic explanatory filler. Figure 6 and Figure 11 show answer length increasing, and Figure 7 shows some lexical overlap growth, but the paper provides no qualitative examples of actual reconstructed equations, recovered unit conversions, or substituted derivations. A few carefully chosen examples would have helped separate genuine recovery from mere verbosity. Without that, “cramming” is a catchy label attached to an under-analyzed phenomenon.

12. **The paper’s broader implications are overstated relative to the evidence.**  
   Page 9 suggests that early stopping of CoT generation may be a cost-effective way to save tokens “without proportionally sacrificing accuracy.” That might be true, but the experiments do not directly test an early-stopping protocol during generation. They test deletion after CoT has already been produced. Those are not operationally equivalent because the model state trajectory and computation budget differ. This is another place where the paper jumps from an interesting observation to a stronger systems implication than the methodology justifies.

## Questions
1. The main scoring variable is produced by Claude-4 Sonnet. Could the authors clarify the exact evaluation prompt, whether the judge output is deterministic, and whether the main conclusions hold under a stricter objective metric, for example exact final-answer correctness for numerically checkable questions? This would substantially increase my confidence.

2. Please define the deletion intervention more formally. If the model first generates a CoT prefix \(c_{1:T}\), and deletion produces \(\tilde c_{1:T'}\), what exact text is then fed back for final answer continuation? Is the model asked to continue from the modified prefix in the same generation stream, or is a fresh prompt constructed? This is central to interpreting the causality of the intervention.

3. For physics-aware deletion, how exactly are “physics-related tokens” identified and tokenized? A precise algorithm or pseudo-code would help. Right now, the comparison in Figure 3 is too dependent on an undocumented external annotator.

4. In Equation (2) and Figure 7, how is Manhattan distance scaled or normalized? Since answer length increases under deletion, an unnormalized bag-of-words distance is confounded by verbosity. Please either justify the current scaling or provide a length-controlled analysis.

5. Can the authors provide qualitative case studies showing actual reconstructed content after deletion, for example deleted equations or units that reappear in the final answer? That would make the “cramming” claim much more convincing than length increase alone.

6. The paper claims approximate threshold behaviors around \(40\%\), \(60\%\), and \(70\%-80\%\) depending on deletion strategy. Could the authors provide a more principled way to estimate these thresholds, with uncertainty, rather than relying on visual inspection of figures?

7. How many examples from each dataset were used in the main experiments, and were the same examples reused across all models and conditions? Please report exact counts and whether any subset selection was performed.

8. The paper argues for implications to faithfulness, but the intervention occurs after CoT has already been generated. Can the authors more carefully distinguish between dependence on the *visible text of the scratchpad* and dependence on *internal computations that occurred while producing that scratchpad*? A sharper claim here could materially improve the paper.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work evaluates model reasoning behavior on academic physics benchmarks and does not appear to involve human subjects, sensitive personal data, or clearly harmful deployment settings.

## Soundness Rating
2: fair. The empirical observations are interesting and some conclusions are directionally supported, but key methodological details are underspecified, the main evaluation relies too heavily on an opaque LLM judge, and several interpretations about faithfulness are stronger than what the intervention strictly establishes.

## Presentation Rating
2: fair. The paper is readable at a high level and some figures are useful, but important experimental details are missing, figure labeling is inconsistent in places, and the mathematical/operational definitions are not precise enough for a method paper.

## Contribution Rating
2: fair. The question is important and the physics-domain application is potentially useful, but the methodological contribution appears incremental and the evidence is not yet strong enough to make this a clear ICLR-level contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles a good question and has some interesting empirical signals, especially the robustness-to-deletion pattern and the answer-length compensation effects. However, the current version overclaims what can be inferred about CoT faithfulness, underspecifies several core components of the methodology, and lacks the depth and rigor I would want for acceptance.

## Reviewer Confidence
4: confident. I am confident in the core assessment and carefully checked the main experimental logic, figures, and equations, though some implementation details are omitted in the paper and limit absolute certainty.