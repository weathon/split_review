---
job_id: d2cd462a-43cb-4257-89f2-b2ce187ebb5e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4Ha2srdhPN.pdf
paper: GRAID: Enhancing Spatial Reasoning of VLMs Through High-Fidelity Data Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope as a datasets/benchmarks and multimodal learning submission, centered on improving spatial reasoning in VLMs through a data generation framework and downstream transfer experiments.

## Minimum Quality
Pass ✅. The paper includes an abstract, introduction, related work, methodology, dataset description, experiments, quantitative results, and conclusion, and it provides enough technical and empirical content to merit full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper presents GRAID, a framework for generating spatial-reasoning VQA data from 2D object detections and hand-designed question templates, with the aim of avoiding errors from single-image 3D reconstruction and caption-based generation. The authors instantiate GRAID on BDD100k, NuImages, and Waymo, generate over 8.5M QA pairs, report a human evaluation suggesting higher data validity than a SpatialVLM-derived dataset, and show that fine-tuning VLMs on GRAID improves performance on held-out question types and several external benchmarks.

## Strengths
The paper tackles a real and relevant problem. Current VLMs are weak at spatial reasoning, and the community does need better training data. The central practical insight, namely that many useful qualitative spatial relations can be generated from 2D geometry alone, is sensible and well motivated in the paper.

The work is ambitious in scale. Table 2 shows substantial dataset sizes for BDD100k and NuImages, and the framework is instantiated across multiple source datasets rather than only a single corpus. Even if one discounts some of the headline framing, producing millions of spatial QA pairs with explicit template control is useful infrastructure.

The paper also does a reasonable job of making the pipeline concrete. Algorithm 1 is helpful because it turns what could have been a vague “rule-based generator” description into an explicit realization procedure for one template. Likewise, the appendix list of question families makes the scope of the generator easier to understand.

The human-evaluation angle is a genuine strength, at least directionally. The comparison in Section 4 between GRAID and OpenSpaces is imperfect, but it is still valuable that the authors attempted direct human checking of generated question validity and answer correctness instead of relying only on automatic statistics. Figure 1 is also effective in communicating the motivation: the examples from prior pipelines illustrate exactly the kind of low-fidelity or ill-posed supervision the paper is trying to avoid, while the GRAID example is simpler and plausibly more reliable.

The experimental section contains some encouraging transfer signals. Figure 3 is one of the paper’s stronger pieces of evidence. If taken at face value, it suggests that training on only six question types yields gains on many held-out types, including on GRAID-NuImages, which is important because it argues against pure template memorization on the training set. Similarly, Table 4 shows that for the Llama backbone, GRAID fine-tuning improves several BLINK categories that are at least plausibly tied to spatial understanding, such as Relative Depth, Spatial Relation, and Visual Correspondence.

Finally, the paper is reasonably clear in its overall narrative. Even though I have several concerns with the details, I did not struggle to understand the intended contribution, and the decomposition into Scene Understanding plus SPARQ is straightforward.

## Weaknesses
1. **The core scientific claim is overstated relative to what the method actually guarantees.**  
   The paper repeatedly frames GRAID as “enhancing spatial reasoning” and says that “qualitative spatial relationships can be reliably determined from 2D geometric primitives alone” (Abstract, Section 1, Section 3.1). That is only true for a narrow subset of spatial relations under favorable imaging conditions. From the actual realizers in Appendix A.1 and Algorithm 1, many generated labels reduce to axis-aligned image-plane predicates over boxes, such as left/right ordering, approximate count, largest area, or grid cell membership. These are not the same as robust scene-level spatial reasoning. In particular, image-plane left/right and pixel-area comparisons can be badly confounded by perspective, truncation, occlusion, and detector box quality. The paper partially acknowledges ambiguity, but the main claims remain too broad. This matters because the work is sold as a general solution to spatial-reasoning data quality, while the implemented supervision mainly targets a more limited family of 2D perceptual heuristics.

2. **There is a notable mismatch between the prose description of the RightOf logic and Algorithm 1, which makes the method definition feel unstable.**  
   On Page 5, in “Realize Questions,” the text says the RightOf algorithm should check that candidate boxes “lie on similar planes” and says that otherwise the apply method returns an empty list due to ambiguity. However, Algorithm 1 does not include any such plane-similarity condition. It checks only class grouping, ordered class pairs, the inequality \(x_{\min}^{(1)} > x_{\max}^{(2)}\), and \(\mathrm{IoU}(b_1,b_2)=0\). These are not equivalent. If the intended realizer includes an additional geometric or vertical-alignment constraint, it needs to be defined formally. If not, the prose is misleading. This is not a cosmetic issue, because it affects what labels are actually being generated and whether the “ambiguity avoidance” story is true.

3. **Several mathematical/algorithmic definitions are underspecified or questionable.**  
   The object-detection formalization in Section 3.1 is sloppier than it should be. The paper introduces \(I \in \mathbb{R}^{H \times W \times C}\), then uses \(C\) again as the number of classes in \(y_i \in \{1,\ldots,C\}\) and in \(z_i \in \mathbb{R}^C\). Reusing \(C\) for both image channels and class count is basic notation collision and should have been avoided.  
   There are deeper issues too. The statement “models trained to compete ImageNet Large Scale Visual Recognition Challenge have \(C=1000\)” on Page 4 is not really relevant to object detection as formulated here, and it muddies the distinction between classification label spaces and detection taxonomies.  
   More importantly, the paper makes repeated use of thresholded predicates and margins, but these are almost never formalized in the main paper. For example, the depth-related “Closer” and “Farther” templates depend on a configurable `margin_ratio` (Page 6, Appendix A.1), but the exact decision rule is not written mathematically. Likewise, several counting and ranking templates rely on a “margin” or multiplicative gap, but the main paper does not define these thresholds or explain how they are chosen. Since the central contribution is a data-generation framework, the label function should be specified more rigorously, not left as a bag of heuristics.

4. **The human evaluation is directionally useful but too limited and not sufficiently controlled to support some of the stronger comparative claims.**  
   In Section 4, the comparison against OpenSpaces uses 250 questions, while GRAID is evaluated on 317 pairs, and the protocol is not tightly aligned. For SpatialRGPT/OpenSpatialDataset, the authors say evaluators “were unable to ascertain the quality of the examples” because of masked region queries, so that comparison is effectively inconclusive. For OpenSpaces, the paper reports rates of invalid questions and incorrect answers, but it is unclear whether the evaluators were blind to the method source, whether inter-annotator agreement was measured, and how disagreements were resolved.  
   The GRAID evaluation itself is also somewhat slippery. The paper reports 95.58% valid questions and 93.69% valid answers, then says fewer than 9% of unique instances were invalid or confusing, then adds that “the current public datasets have these corrections and thus even higher validity” (Pages 7–8). The latter should not be used to support the present submission, because the main-paper evaluation should stand on what was actually reviewed. Overall, the human study is helpful as an initial sanity check, but not strong enough to carry claims like “highest accuracy VQA datasets made by automated generation pipelines.”

5. **The empirical evidence does not cleanly disentangle learning spatial concepts from learning template-specific language priors.**  
   The paper’s central learning claim, especially in RQ2 and around Figure 3, is that models learn spatial primitives that generalize to unseen question types. That is plausible, but the experiments do not convincingly isolate geometry from templated linguistic supervision. Many question families share style, answer format, object vocabulary, and compositional scaffolding. If a model sees many binary Yes/No questions with recurring object nouns and fixed syntactic patterns, gains on held-out templates could partly reflect improved adaptation to the synthetic QA distribution rather than transfer of spatial reasoning per se.  
   Figure 3 is suggestive, but it is not a clean causal test. A stronger evaluation would compare against non-spatial template controls, paraphrase-held-out templates, or a language-only ablation where object boxes are randomized or labels are perturbed. Without such controls, the paper overstates what Figure 3 proves.

6. **The comparison to prior work is narrower than the paper’s framing suggests.**  
   The paper emphasizes SpatialVLM, SpatialRGPT, and SpaRE, and Table 1 reflects that positioning. But the broader contribution is a synthetic spatial-reasoning data pipeline, and the paper does not sufficiently position itself against other programmatic or synthetic data generation approaches for multimodal reasoning. Even within its own framing, Table 1 is somewhat selective: it highlights a set of binary features favorable to GRAID, but does not compare diversity of question families, grounding fidelity under detector noise, or the kinds of spatial concepts that can or cannot be represented.  
   This matters because the paper is trying to claim not merely “a useful dataset generator” but a better route to spatial reasoning data generation. The positioning currently feels too curated.

7. **The dependence on high-quality detectors and annotations is not stress-tested, yet this dependence is central to the method.**  
   Section 3.1 leans heavily on the practical maturity of object detection and even cites interpretability tools, which is not really evidence that detector outputs are sufficiently reliable for this downstream purpose. In fact, the method inherits detector failures directly: missed objects, duplicate boxes, coarse boxes around thin objects, class taxonomy mismatch, and localization drift all translate into incorrect or ambiguous questions. The paper partially dodges this by using datasets with strong labels in Section 4, but then the main take-home message becomes less about robustness of GRAID as a general framework and more about what happens when one already has very good labels. The scientific question that remains unanswered is how brittle the framework is under realistic detector noise. That omission matters if the claimed benefit is easy portability to arbitrary images and detectors.

8. **The benchmark results are promising but mixed, and the interpretation is too rosy.**  
   Tables 4, 5, and 6 show real gains on several benchmarks, but they also show substantial regressions, especially on VSR-zeroshot and some NaturalBench metrics. For example, in Table 4, Llama+GRAID improves BLINK overall from 25.72% to 42.13%, which is good, but VSR accuracy drops from 61.13% to 53.36%. In Table 5, Gemma+GRAID underperforms the base Gemma on all reported NaturalBench summary metrics and still slightly drops on VSR accuracy. These are not minor blemishes; they complicate the claim that GRAID tuning “consistently” improves spatial reasoning without harmful side effects.  
   I would have liked a more sober analysis of where gains come from and where the synthetic data distribution hurts. Right now the paper mainly highlights wins and offers only very limited diagnosis of regressions.

9. **Some baseline numbers are suspicious enough that they demand explanation.**  
   Table 5 reports the base Gemma 3 4B score on A-OKVQA as 1.57%, and several BLINK subcategories at or near 0%. That is dramatically lower than one would expect from a current instruction-tuned VLM, and if true it suggests either a very brittle prompting/evaluation configuration or a major mismatch in answer extraction. Since the paper’s argument relies heavily on absolute gains after SFT, these baseline anomalies matter a lot. Similarly, some OpenSpaces-SFT results crater performance catastrophically across benchmarks. Perhaps that is real, but then the experimental setup needs more detail and error analysis. Otherwise, the paper risks comparing against underperforming configurations and attributing too much to the dataset.

10. **The training setup is very lightweight relative to the strength of the conclusions, and reproducibility-relevant choices are underexplained in the main paper.**  
   For RQ1 and RQ2, the models are trained for only 200 steps, sometimes on 10% of the data, with very small effective batch sizes. That is fine for a quick signal, but then the paper should present the findings as preliminary rather than as strong evidence of learned transferable representations. Also, several key details are pushed out of the main narrative, such as data balancing decisions, threshold choices for question realization, and exact prompting formats. Since this is a dataset and training paper, those choices are not implementation trivia, they shape the conclusions.

11. **Figure and table presentation occasionally undermines the argument rather than strengthening it.**  
   Figure 2 shows the hierarchical breakdown of GRAID-BDD question types and reveals a strongly imbalanced distribution, with Spatial Relations dominating and some categories contributing very little. This is not fatal, but it weakens the broad “22 templates” pitch because the effective training signal is concentrated in a few families. The paper mentions that RQ1 uses an unstratified 10% subset, so the imbalance in Figure 2 directly affects how to interpret the reported generalization gains.  
   Figure 3 is visually persuasive, but because it aggregates many question types with different sample counts and difficulty, the bar deltas are hard to interpret statistically. There are no confidence intervals, no per-type support counts in the figure, and no indication whether some of the largest gains come from tiny held-out subsets.  
   Table 2 is useful, but it also exposes a major scale asymmetry: Waymo contributes only 16.4k/13.8k QA pairs, far smaller than BDD and NuImages. Given this, the claim of demonstrating the framework on “three source datasets” is somewhat less compelling than it first sounds, because almost all evidence comes from two large driving datasets.

12. **The paper sometimes substitutes assertive rhetoric for evidence.**  
   Statements such as “These results confirm that GRAID generated datasets are of the highest accuracy VQA datasets made by automated generation pipelines” (Page 8) are simply too strong for the evidence presented. The paper has one partial human comparison to one community SpatialVLM dataset, an inconclusive look at SpatialRGPT due to evaluation difficulty, and no broad comparative study across automated VQA generators. I appreciate the ambition, but the manuscript would benefit from toning down several claims and being more precise about the scope of what is actually shown.

## Questions
1. **Can the authors precisely formalize the realization rules in the main paper, especially for ambiguous cases?**  
   For instance, for RightOf/LeftOf, what is the exact criterion used in the implementation? Is it only \(x\)-ordering plus \(\mathrm{IoU}=0\), as in Algorithm 1, or is there also a vertical-plane or alignment constraint as described in the surrounding text on Page 5? A precise mathematical specification for the core templates would increase confidence substantially.

2. **How sensitive is GRAID to detector errors?**  
   Since the framework’s portability rests on detector outputs, an ablation with perturbed boxes, dropped detections, duplicate detections, or class-noise injection would be very informative. Even a simple stress test on Page 4’s object-detection assumptions would help clarify whether the method is robust in practice or mostly relies on high-quality ground-truth annotations.

3. **Can the authors provide stronger evidence that the observed transfer is not mostly template-language transfer?**  
   For RQ2 and Figure 3, I would like to see at least one control experiment, for example: paraphrase-held-out evaluation, training on matched non-spatial templates, or geometry-corrupted labels. Any of these would help establish that the gains really come from learned spatial structure rather than superficial adaptation to a synthetic QA style.

4. **What explains the extremely low baseline scores for some models in Tables 5 and 6?**  
   In particular, the Gemma 3 4B baseline numbers on A-OKVQA and several BLINK categories are surprisingly poor. Please clarify prompting, answer normalization, and whether these models were evaluated in a setting known to be comparable to published baselines. This could materially affect how much confidence one should place in the reported SFT gains.

5. **Can the authors report inter-annotator agreement and evaluator blinding for the human study?**  
   Section 4 would be much stronger with agreement statistics, clearer sampling details, and clarification on whether annotators knew which dataset a question came from. That would help separate genuine quality improvements from possible protocol artifacts.

6. **How should readers interpret the benchmark regressions?**  
   The paper mentions some regressions briefly, but not in depth. A clearer failure analysis for VSR and NaturalBench would make the contribution more credible. Are the drops caused by answer-format mismatch, domain shift, overfitting to templated phrasing, or loss of general visual reasoning capability?

7. **Why is the work’s scope described as broad spatial reasoning when the implemented supervision is mostly 2D image-plane reasoning?**  
   I am open to being convinced here, but the paper should either tighten the claim or provide stronger evidence that the training transfers to genuinely harder spatial settings involving occlusion, perspective, and object-object depth reasoning beyond the few depth templates.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The work uses existing driving datasets and synthetic QA generation. The main issues are scientific rather than ethical, namely claim scope, evaluation rigor, and robustness.

## Soundness Rating
2: fair. The paper is technically plausible and contains meaningful experiments, but several central claims are only partially supported, the method is underspecified in important places, and some evaluations are not controlled tightly enough to justify the strongest conclusions.

## Presentation Rating
3: good. The paper is generally readable and well organized, with helpful figures and tables, but there are inconsistencies between algorithm and prose, some notation problems, and several places where the exposition is more assertive than precise.

## Contribution Rating
2: fair. The dataset-generation framework is useful and the scale is nontrivial, but the conceptual novelty is moderate, the scope of the claimed spatial reasoning improvement is broader than the evidence supports, and the empirical case has important gaps.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a practical idea, useful scale, and encouraging transfer results, but in its current form it overclaims, underspecifies core label-generation rules, and does not sufficiently disentangle true spatial reasoning gains from template/distribution effects.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with the relevant VLM/spatial-reasoning area and checked the main technical and empirical details carefully, but some concerns would benefit from author clarification.