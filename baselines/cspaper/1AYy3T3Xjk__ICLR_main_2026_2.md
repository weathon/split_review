---
job_id: 3f6e1ba6-5c02-4d79-8ea8-166a1ee1c321
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1AYy3T3Xjk.pdf
paper: A Process-Level Method for Creativity Evaluation in LLM-Assisted Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is centered on an LLM-based evaluation model, human-AI interaction data, interpretability, and assessment methodology for AI-assisted learning, which fits ICLR’s scope in language, evaluation of learned systems, societal considerations, and general machine learning.

## Minimum Quality
Pass ✅. The submission contains the required core components, including Abstract, Introduction, Related Work, Methodology, Experiments, Results, and Discussion, and it is written in English. While I have substantial concerns about rigor, clarity, and empirical support, these are review-level weaknesses rather than grounds for desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions targeting automated reviewers, or other obvious manipulation attempts in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies process-level creativity assessment for LLM-assisted learning. It introduces the CREDO framework with four proposed dimensions of creativity in human-LLM collaboration, an Innovation Traceability Atlas (ITA) for attributing student versus model contributions from multi-turn dialogues, and an instruction-tuned DeepSeek-based evaluator that predicts 1 to 5 scores with rationale text.

The empirical study uses 1,273 cleaned dialogues from 81 undergraduates, annotated by experts, and reports agreement between the fine-tuned evaluator and expert judgments. The paper also presents an attribution experiment intended to validate the model’s ability to distinguish original student ideas from model-supported or restated content.

## Strengths
1. The paper tackles a relevant and underexplored problem. Process-level assessment of human-LLM collaboration is more meaningful than pure outcome scoring, especially in educational settings where attribution and formative feedback matter. That shift in framing is useful, even if the current execution leaves important gaps.

2. The paper makes a reasonable effort to define an annotation-centered pipeline rather than presenting a pure “LLM-as-a-judge” black box. The combination of expert annotation, an attribution schema, and rationale generation is directionally sensible for auditability.

3. The dataset collection setup is more realistic than many toy evaluation settings. The dialogues are derived from multi-turn academic inquiry tasks tied to ongoing course projects, and the paper at least states student-level splitting and IRB approval in Section 3.1, which is a positive sign for methodological care.

4. Table 1 on Page 5 is one of the clearer parts of the paper. It explicitly contrasts the classical four creativity dimensions with the proposed CREDO dimensions and explains, dimension by dimension, why outcome-only criteria may break down under LLM assistance. Even though the construct validity is not fully established, the table helps readers understand the intended conceptual departure.

5. Table 2 on Page 8 shows a large empirical gap between the fine-tuned model and the two reported baselines. If taken at face value, the jump from QWK \(0.342\) and \(0.513\) to \(0.728\) suggests that domain-specific supervision matters a lot for this task, and the inclusion of multiple metrics, MSE, MAE, Pearson \(r\), and QWK, is appropriate for ordinal prediction.

6. Figure 1 on Page 3 is helpful as a high-level workflow diagram. It makes the paper’s intended pipeline legible, from dialogue collection through cleaning, annotation, human rating, instruction data construction, LoRA fine-tuning, and inference. For a paper with many moving parts, this figure improves navigability.

7. Figure 3 on Page 9, despite being more illustrative than analytical, does communicate the authors’ core ambition, namely to visualize a student’s evolving conceptual trajectory rather than only the final answer. As a concept demo, it supports the process-oriented motivation better than the quantitative sections do.

## Weaknesses
1. **The central methodological object, the ITA attribution procedure, remains underspecified to the point that the core contribution is hard to evaluate.**  
   The paper repeatedly claims that ITA “deconstructs” dialogue into learner-led origination and development nodes versus model scaffolding, but there is no formal definition of the parsing procedure, no algorithm, no annotation schema with decision rules, and no concrete representation beyond high-level prose in Section 3.2.2. This matters because the entire scientific contribution hinges on reliable attribution. Right now, ITA is presented more like a conceptual label than a reproducible method. Figure 3 illustrates a final graph for Student 0018, but it does not explain how nodes are extracted, how edges are defined, how ambiguity is resolved, whether this graph is manually created or automatically induced, or how different annotators would produce the same structure. A visual artifact is not a method.

2. **The paper overclaims “auditable” and “interpretable” evaluation without giving enough evidence that the rationales are faithful or that the attribution is causally grounded.**  
   In Section 1.4 and the Discussion, the model is framed as generating reviewable process-based rationales. But there is no evaluation of rationale faithfulness, usefulness, calibration, or consistency under paraphrase. The paper only reports score agreement and one attribution classification result. A model can match scores while producing post hoc rationales that are plausible but not causally tied to its decision process. This is especially important here because “auditability” is a central selling point, not an optional extra.

3. **The empirical evaluation is too narrow and omits several baseline classes that are necessary to support the paper’s broader claims.**  
   In Section 4.1, the baselines are DeepSeek-32B without tuning and GPT-4 zero-shot. These are weak reference points for a supervised evaluation task. Missing are simpler non-generative baselines on the same expert-labeled data, for example a classifier or regressor over dialogue embeddings, a smaller instruction-tuned model, or a rubric-based model that only predicts scores without open-ended generation. Without these, it is hard to tell whether the gains come from the proposed process-oriented framing versus simply fitting a labeled dataset with a large model. Table 2 therefore supports “fine-tuning helps” more than it supports the paper’s stronger claims about the necessity of CREDO or ITA.

4. **The attribution experiment in Section 4.2.2 is disconnected from the actual training objective and raises questions about what exactly the model learned.**  
   Table 3 reports macro-F1 \(=0.84\) for classifying utterances into “Original Student Idea,” “Developed Student Idea,” and “Restated Student Idea.” However, the training objective in Equations (1) to (3) only specifies score prediction plus rationale generation, with no explicit attribution classification loss. The paper never explains whether the model was separately prompted for attribution, whether additional supervision was used, whether the 200 sampled dialogues overlap with expert ITA labels used in training, or how utterance-level predictions are derived from a dialogue-level model. This is not a minor omission. Since attribution is the paper’s core premise, the evaluation must be methodologically transparent.

5. **There are concrete mathematical and formulation issues in the main paper.**  
   - In Equation (1) on Page 6, the notation is inconsistent. The paper says “let \(\hat{\mathbf{s}}\) denote predicted scores” and then writes \(\text{CE}(\hat{s}_k, s_k)\). Cross-entropy is normally defined between logits or a predicted distribution and the target label, not between an integer prediction and a gold integer score. If the task is truly “ordinal or 5-way classification per dimension,” the paper needs to define the logits \(p_\theta(s_k \mid \mathcal D)\) and write something like
     \[
     \mathcal L_{\text{score}} = \sum_{k=1}^4 -\log p_\theta(s_k \mid \mathcal D).
     \]
     If the authors instead use an ordinal regression formulation, they need to specify the threshold parameterization and loss. As written, Equation (1) is too vague to reproduce.
   - The rationale loss in Equation (1) is also underspecified. The expectation over \(t\) suggests token-level NLL, but the conditioning is written as \(p_\theta(r_t \mid r_{<t}, \mathcal D)\) without explaining whether teacher forcing is used, whether score tokens are generated before rationale tokens, and whether the model jointly conditions rationale generation on gold scores or predicted scores.
   - Equation (2) defines the KD term only at the token distribution level, but again leaves out whether this is applied over rationale tokens only, over a serialized score-plus-rationale sequence, or over the full vocabulary at all output positions. Given that scoring is the main task, the omission is important. Distilling rationale generation and distilling score distributions are not equivalent.
   - In Section 4.1, the QWK formula appears incorrect or at least inverted relative to standard notation. The paper writes
     \[
     \text{QWK} = 1 - \frac{\sum_{i,j} w_{i,j} E_{i,j}}{\sum_{i,j} w_{i,j} O_{i,j}},
     \]
     where \(O\) is observed and \(E\) is expected. Standard quadratic weighted kappa uses
     \[
     \kappa = 1 - \frac{\sum_{i,j} w_{i,j} O_{i,j}}{\sum_{i,j} w_{i,j} E_{i,j}}.
     \]
     Reversing these terms changes the quantity. This is not just a typo-level annoyance because the paper uses QWK as the “core metric” and anchors the human ceiling at 0.81. The metric definition should be correct in the main text.

6. **The paper’s claims around reliability and construct validity are stronger than the evidence supports.**  
   In Section 3.2.3, the authors report weighted kappa \(0.81\) and Cronbach’s alpha \(0.86\), then state that this provides strong evidence that the framework is “theoretically sound.” That is not what these statistics establish. Weighted kappa measures inter-rater agreement for the assigned labels, and Cronbach’s alpha measures internal consistency under assumptions that are not discussed. Neither statistic validates that the four CREDO dimensions actually measure the intended construct of “human-AI collaborative creativity.” In fact, alpha is somewhat awkward here because the four dimensions are conceptually distinct by design, not necessarily interchangeable indicators of a single latent factor. The paper needs to be much more careful in what these statistics do and do not show.

7. **The paper’s experimental evidence for generalization is insufficient, despite explicitly raising it as a research question.**  
   Section 4 states that one of the three core questions is whether the model generalizes to unseen domains. But the main paper does not actually present a domain generalization experiment. The split is built by clustering initial prompts and doing student-level separation, which is useful, but that is not the same as cross-domain generalization. Since the dataset is already narrow, 81 undergraduates, mostly STEM, from two universities, this missing evidence materially weakens the paper’s broader framing.

8. **The presentation has signs of patchwork writing and internal inconsistency, which undermines trust in the rigor of the reported study.**  
   There are several places where the paper appears to contain response-style text rather than a clean conference manuscript. For example, Section 4.1 says “to address the core concern raised by an Area Chair regarding whether ‘the evaluation metrics are meaningful’,” and Section 4.2.2 says “to directly address a concern from an Area Chair.” That is not appropriate framing for the main submission and suggests the manuscript was assembled from rebuttal-era material or an internal report. Similarly, the paper says “Macroscopic Performance Overview: the radar chart 2...” on Page 8, which is awkward and indicative of limited polish. These are not merely stylistic nits, they make it harder to tell what was part of the original experimental plan versus post hoc justification.

9. **Figure 2 is not convincing evidence and is partially distracting.**  
   The radar chart on Page 8 is presented as a “visual summary of comprehensive superiority,” but it mixes metrics with different semantics, and it appears to include BERTScore and ROUGE axes that are not defined in Section 4.1 or reported in Table 2. This is a serious mismatch between figure and text. If BERTScore and ROUGE were used to evaluate rationale quality, that needs to be stated clearly and tabulated. If they were not central, they should not appear in the main comparison figure. As it stands, Figure 2 muddies the story and creates uncertainty about what was actually measured.

10. **The ablation evidence in the main paper is too weak for a method paper with multiple claimed ingredients.**  
    Section 3.3.3 points to Table A2 in the appendix, but the main paper provides no substantive ablation table. More importantly, even in the appendix summary, “w/o LoRA” is listed as “computationally prohibitive,” so there is no result. That means the paper cannot really claim to have isolated the contribution of LoRA in performance terms. The ablation is mostly about feasibility, not effectiveness. Since the full model combines LoRA, KD, and rationale generation, and only deltas for some removals are shown, it remains unclear which component matters most and whether the process-oriented aspects, rather than generic instruction tuning, drive the result.

11. **The human-performance ceiling argument is not carefully justified.**  
    Section 4.1 treats the inter-rater reliability value of 0.81 as a “Human-Level Performance Ceiling.” That is an appealing simplification but not a rigorous ceiling. Human-human agreement among trained annotators is not directly equivalent to the best achievable model-human agreement, and using a single scalar ceiling can be misleading when agreement varies by dimension and by sample difficulty. Since the paper emphasizes near-human performance, this framing deserves more nuance.

12. **The paper’s contribution is partly conceptual, but the novelty relative to existing annotation-and-judge pipelines is not sharply differentiated.**  
    The paper criticizes outcome-focused evaluation and LLM-as-a-judge setups, which is fair. But the actual technical stack, expert annotation, a custom rubric, instruction tuning, LoRA, KD, score-plus-rationale output, is largely a standard assembly of known components. That can still be publishable if the benchmark and methodology are especially solid. Here, however, the benchmark is small, the method is underspecified, and the conceptual layer does more of the work than the technical one. The paper needs a crisper account of what is genuinely new beyond applying supervised rubric learning to a specialized educational dialogue setting.

13. **Important experimental details required for reproducibility are missing from the main paper.**  
    Several key hyperparameters are deferred to “the attached technical report” in Table A3, including sequence length, learning rate, weight decay, KD temperature, and KD loss weight. The authors do say code will be released, but the main paper still needs enough detail for a reviewer to assess validity. Given that the model is 32B and the dataset is relatively small, these choices could substantially affect performance.

14. **The sample and task setup constrain the scope more than the headline framing suggests.**  
    The abstract and introduction position the work as addressing creativity evaluation in LLM-assisted learning broadly, but the actual evidence comes from 81 undergraduates from two research universities, over two weeks, mostly in STEM inquiry dialogues, using one LLM family. The Discussion acknowledges this, which is good, but the headline claims still read broader than the evidence base warrants.

## Questions
1. Please define the ITA procedure precisely. What are the atomic units, utterances, clauses, or semantic spans? How are “Origination Nodes,” “Development Nodes,” and “Scaffolding Support” operationally identified? Is there a deterministic annotation guideline or algorithm that another team could apply and reproduce?

2. For Equation (1), what exactly is the score prediction parameterization? Is each dimension modeled as 5-way classification, ordinal regression, or next-token generation over serialized labels? Please provide the exact form of \(p_\theta\) and correct the notation accordingly.

3. For Equation (2), what sequence positions are distilled from the teacher to the student? Score tokens, rationale tokens, or both? If both, how are the structured scores serialized, and how sensitive are results to this serialization?

4. Please clarify the attribution experiment in Section 4.2.2. Was utterance-level attribution supervision available during training, or was this a pure zero-shot/use-at-inference probe from a model trained only on dialogue-level scores plus rationales? How are utterance-level labels produced from the model? This is central to assessing the main claim.

5. Please correct or explain the QWK formula in Section 4.1. As written, it appears to swap observed and expected disagreement. If this is a typo in the paper only, please confirm that the actual reported numbers use the standard formula.

6. Since one of your stated research questions is generalization to unseen domains, can you provide a domain-held-out evaluation, or at least a stricter cross-topic split than the current clustering-based partition? A response here would materially affect my confidence.

7. Can you provide stronger baselines on the same labeled data, for example a smaller supervised model, a dialogue-embedding regressor/classifier, or a score-only model in the main paper rather than only in the appendix? This would help determine whether the gains are due to CREDO/ITA specifically or just task-specific fine-tuning.

8. The paper uses Cronbach’s alpha to support the claim that the four dimensions measure the same underlying construct. Can you justify that assumption more carefully, or alternatively soften the claim? As written, this feels psychometrically overstated.

9. Figure 2 includes BERTScore and ROUGE axes, but these metrics are not introduced in Section 4.1 or reported in Table 2. What are these metrics evaluating, and why are they absent from the main quantitative table? If they concern rationale quality, please explain how they were computed and whether they correlate with expert judgments of rationale usefulness.

10. If “auditable rationales” are a core contribution, do you have any human evaluation of rationale quality, faithfulness, or actionability? Even a small expert study comparing rationale usefulness across models would substantially strengthen the paper.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper uses real student-LLM dialogues collected from 81 undergraduates, with approximately 2.1 million raw tokens before filtering, as described in Section 3.1.1. Although IRB approval and anonymization are stated, this is still educational interaction data involving potentially sensitive academic behavior, idea formation, and possible personally identifying or proprietary project content. If the cleaned corpora and scripts are released, the paper should more clearly specify what is being released, at what granularity, and under what access controls.

A second concern is responsible deployment. The Discussion appropriately says the method targets formative support rather than high-stakes ranking, but much of the paper’s framing emphasizes expert alignment and near-human agreement. For an educational assessment system, the authors should more explicitly guard against use in grading, surveillance, or disciplinary settings without human review, fairness auditing, and uncertainty disclosure.

## Soundness Rating
2: fair. The paper has a coherent high-level setup and some empirical evidence, but the central attribution method is underspecified, a core metric formula appears incorrect in the text, and several key claims are only partially supported by the reported experiments.

## Presentation Rating
2: fair. The motivation is understandable and some tables/figures help, but the manuscript has multiple clarity issues, missing formal definitions, inconsistent mathematical notation, and some text that reads like rebuttal material rather than a polished conference submission.

## Contribution Rating
2: fair. The problem is important and the process-oriented framing is worthwhile, but the actual technical contribution is not sufficiently pinned down or empirically validated to meet the bar implied by the paper’s broad claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The topic is relevant and the framing is promising, but there are too many unresolved issues around method specification, metric correctness, baseline adequacy, and evidential support for the core attribution and auditability claims.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main methodological, mathematical, and experimental details carefully, although some central implementation choices are not specified clearly enough to verify every aspect fully.