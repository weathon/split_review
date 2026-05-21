---
job_id: 4d7d7059-4fe7-4e8e-85e1-51ef9ec2cb63
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2PJkG6aV4A.pdf
paper: Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies fairness and safety evaluation for large vision-language models and proposes a new benchmark-style evaluation framework.

## Minimum Quality
Pass ✅. The paper contains the core components expected for an empirical benchmark paper, including abstract, introduction, review of prior evaluations, methodology, experiments, quantitative and qualitative results, discussion, and conclusion. While I have substantial concerns about methodology and interpretation, these are review-level weaknesses rather than desk-reject-level flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, invisible instructions, or any apparent attempt to manipulate automated reviewing within the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies societal bias evaluation for large vision-language models under modern safety guardrails. The main claim is that prior LVLM bias benchmarks often fail on strongly guarded models because prompts that explicitly ask about a depicted person trigger refusals, and the authors propose a guardrail-agnostic alternative that uses person-irrelevant prompts while supplying the image as provisional user context. The framework is instantiated on three tasks, story generation, term explanation, and exam-style QA, and evaluated on 20 open-source and proprietary LVLMs, with the paper reporting zero refusals and measurable gender and racial disparities across all models.

## Strengths
The paper identifies a real and timely evaluation problem. Table 1 is the strongest motivating evidence in the submission: refusal rates on prior benchmarks are extremely high for several recent models, including GPT-5 and Claude 3.7 Sonnet, whereas the proposed protocol yields 0% refusals across all listed models. Even if one debates some downstream metric choices, this table makes the practical problem concrete rather than hypothetical.

The setup is easy to understand and operationally useful. Figure 1 communicates the protocol clearly, especially the shift from “image as target” to “image as user context.” For a benchmark paper, that kind of conceptual simplicity is a virtue, because other researchers can reproduce or adapt the evaluation without needing a complicated pipeline.

The empirical scope is reasonably broad in terms of models and task types. Evaluating 20 LVLMs, including both open-source and proprietary systems, gives the paper more value than a narrow case study. I also appreciate that the authors did not restrict themselves to a single generation setting, but instead tested a spectrum from open-ended generation to constrained QA.

The paper does a good job showing that the bias signal is task-dependent. Table 2 and Figure 3 together support the claim that bias measured in one task does not necessarily transfer to another. That is a useful message for the community, because fairness in multimodal systems is often discussed as if it were one scalar property of a model.

The qualitative examples in Figure 2 are helpful for grounding the otherwise abstract TVD numbers. In particular, the story generation examples make the measured disparities legible to the reader, and they align with the narrative in Section 4.3 that open-ended generation exposes stronger stereotypical associations.

The paper is generally well organized. The motivation, proposed framework, and empirical observations are easy to follow, and the main contribution is stated in a way that most readers will understand on first pass.

## Weaknesses
1. **The central fairness assumption, Hypothesis 1 in Section 3.1 on Page 4, is too strong and insufficiently justified for the claimed interpretation.**  
   The paper states that “the outputs of an unbiased model for person-irrelevant prompts should be statistically independent of the user’s demographics.” This is really the linchpin of the paper, but it is presented more as a declaration than as a defended assumption. For some tasks this is plausible, but for others it is much less obvious. If a user attaches a photo and asks “Teach me about linear algebra so that I can understand,” a model might adapt tone, vocabulary, or examples based on inferred user characteristics, including age, formality, or perceived expertise. The paper tries to focus on gender and race, but the image contains far more than those attributes, and some adaptation may be benign personalization rather than societal bias. Without a stronger argument for why demographic-conditioned variation in these tasks should always be treated as unfair bias, the paper risks conflating responsiveness to user context with harmful stereotyping. This matters because the paper’s headline claim, that all models “undesirably use user demographic information,” depends directly on this interpretation.

2. **The image-as-user-context design does not isolate demographics from other correlated visual factors, so the causal object being measured remains ambiguous.**  
   The paper argues on Page 4 that the proposed method reduces confounds relative to captioning-style prompts, but the problem is not actually resolved, only shifted. FairFace images still vary in pose, expression, attractiveness, lighting, clothing fragments, image quality, and countless other facial or photographic cues. Equation (3) defines outputs as $\mathcal{O}_{a,q}=\{\phi(I,p,q)\}$ over images in group $a$, but there is no counterfactual construction that keeps identity-fixed visual content while changing only the demographic attribute. As a result, a difference between groups can arise from any group-correlated feature in $I$, not necessarily gender or race per se. The authors do state that age and race distributions are aligned when measuring gender bias, which is good, but that only controls a small subset of confounds. This is a major issue because the paper repeatedly interprets disparities as “use of user demographic information,” when the experiment really shows sensitivity to the entire distribution of user photos conditioned on that demographic category.

3. **The metric definition is not fully satisfactory, and in some cases it can overstate or mischaracterize bias.**  
   In Appendix A, Equations (6) to (11), the paper uses normalized TVD to a uniform target across groups. For story generation, TVD is computed per extracted element $e$ and averaged. This creates several concerns. First, averaging over extracted elements weights rare and frequent elements in a way that is not justified. A tiny number of idiosyncratic labels may contribute as much as common occupations. Second, the choice of uniform target is not always obviously the right notion of fairness for the induced distributions over generated attributes. Third, for exam-style QA, the “observed distribution” in Equation (10) is constructed from shares of correct answers rather than directly from accuracy gaps. This transformation can compress or distort practical disparity, especially when all accuracies are low or all are similar. The authors partially acknowledge a related issue by excluding LLaVA-1.6 variants from Table 2 due to near-random accuracies, which is itself a warning sign that the metric can behave oddly under weak performance. A benchmark paper needs the metric to be on very solid footing, and here I do not think it is.

4. **The reliance on an LLM judge is not validated enough in the main paper, especially because two of the three tasks depend on it.**  
   Story generation uses an LLM assistant to extract attributes, and term explanation uses an LLM assistant to decide which explanation is more technical. This means a large fraction of the paper’s reported bias signal is mediated through another model. The main paper only briefly states the use of Qwen3-32B on Page 5; the 97/100 agreement with human judgments appears only in Appendix D, and only for term explanation. There is no comparable main-paper validation for story attribute extraction, where extraction errors could materially change the counts used in Equations (6) and (7). Figure 2 illustrates vivid examples, but qualitative examples are not enough to establish that the judge is reliably parsing occupations, education, family status, and personality at scale across all models. This matters because benchmark conclusions become less convincing when the measurement layer is itself learned, opaque, and under-validated.

5. **Some experimental design choices inject bias artifacts rather than merely reveal them.**  
   The complete story prompt in Figure 5 explicitly asks the model to include the character’s “gender, race, and age,” plus occupation, education, economic status, and family situation. That is not a neutral prompt. It strongly encourages the model to produce socially typed personas and demographic narratives. Measuring stereotypical associations under that prompt can certainly be interesting, but it is not the same as showing that the model would spontaneously use user demographics in ordinary person-irrelevant generation. In other words, the benchmark may partly manufacture the very demographic salience that it then reports. This is especially important when the paper uses broad language like “all models undesirably use user demographic information in person-irrelevant tasks.” Figure 2(a) is an effective example of disparity, but it also highlights that the story task is explicitly designed to elicit demographic characterization, which should temper the interpretation.

6. **The claim that the method “reduces the impact of spurious image contexts” is not empirically demonstrated.**  
   On Page 4, the paper states that the method addresses contextual confounds by using images only as user information. But there is no ablation comparing face-only crops, blurred backgrounds, text-only demographic personas, synthetic counterfactual faces, or identical prompts with and without images. Without such analyses, the reader cannot tell whether the measured bias comes from demographic cues, general visual style cues, or simply the presence of any user image. A simple ablation would have materially strengthened the paper: for example, compare outputs under (i) no image, (ii) face image, (iii) image with demographics masked, or (iv) explicit text persona instead of image. Right now, the method is sold as reducing confounds, but this remains more a plausible story than a demonstrated property.

7. **The comparison between open-source and proprietary models is overinterpreted relative to the evidence.**  
   Observation 2.1 and Section 5 suggest that proprietary models’ lower bias may be driven by continuous monitoring and iterative refinement. This is plausible, but the paper does not actually test this explanation. Figure 4 is not enough to support the stronger discussion in Section 5, because many differences between these model classes are entangled: data mixture, instruction tuning, RLHF, system prompts, post-processing, safety stacks, model scale, and API-side moderation. The discussion is careful in places, but it still leans toward a narrative that is not empirically established. For a paper centered on measurement, causal speculation about why one family looks better should be marked much more explicitly as conjecture.

8. **The quantitative analysis lacks uncertainty estimates and statistical significance reporting.**  
   Table 2 reports point estimates only. Given that some differences are small, especially in term explanation and exam-style QA, confidence intervals or bootstrap uncertainty would help determine which model ranking differences are meaningful. For example, several exam-style QA scores differ by tenths of a point. Without uncertainty bars, the ranking story is shaky. The same issue appears in Figure 4, where correlation coefficients are reported, but there is no indication of sample size uncertainty, sensitivity to outliers, or whether correlations are robust once proprietary and open-source models are separated. Since the paper emphasizes comparative claims across models and tasks, this omission weakens the scientific value of the reported ordering.

9. **The literature positioning is decent but still incomplete around stronger counterfactual and causal-style evaluations.**  
   The paper discusses several benchmark families, but it would benefit from more direct contrast with counterfactual image-based bias audits that try to isolate protected attributes more carefully. That omission matters because one of the main weaknesses of the proposed protocol is exactly the lack of identity-preserving counterfactual control. The authors do mention some related work, but the paper would be stronger if it squarely positioned itself as a tradeoff, namely robustness to guardrail refusals versus weaker causal isolation of demographic factors, instead of implying that the new protocol broadly addresses prior confounding concerns.

10. **Some mathematical and notation choices need tightening.**  
   There are a few technical presentation issues that are not fatal but do matter. On Page 3, the text alternates between $\mathcal{Q}$ and $Q$ when discussing prompt sets. On Page 4, the statement “$\mathcal{S}_q \approx 0$ in Eq. 2” is informal, but the paper never discusses what magnitude should count as negligible under finite-sample noise. In Appendix A, the task-specific use of TVD is defined after the main paper already relies on it, which leaves the main text underspecified at the moment the metric is introduced in Section 3.2. For a benchmark paper built around a single score, the metric definition should be cleaner and more self-contained in the main paper.

## Questions
1. The biggest issue for me is causal interpretation. Can the authors provide a stronger argument, ideally with a main-paper ablation, that the disparities measured by Equation (3) are driven by demographic cues rather than other visual correlates in FairFace images? For example, what happens if the face image is replaced by a text persona, a blurred face, or an image with demographic cues weakened?

2. Can the authors justify Hypothesis 1 more carefully? In particular, why should explanation style in the term-explanation task be statistically independent of user demographics in all cases, rather than reflecting personalization? What exact notion of unfairness is intended here?

3. For the story generation task, Figure 5 asks the model to explicitly include gender and race of the generated character. Did the authors test a milder story prompt that does not explicitly request demographic attributes? If so, does the same model ranking remain? This would help distinguish induced stereotyping from spontaneous demographic conditioning.

4. Please provide uncertainty estimates for the main results in Table 2, ideally confidence intervals or bootstrap standard errors. I would especially like to know whether the proprietary versus open-source gaps remain statistically robust in term explanation and exam-style QA.

5. For the LLM assistant, can the authors report validation for story attribute extraction in the main paper, not only term-explanation agreement in the appendix? Since Table 3 and Table 4 depend on extracted attributes, judge reliability directly affects the headline conclusions.

6. The exam-style QA metric in Equations (10) and (11) seems sensitive to base accuracy. Can the authors also report a simpler disparity metric, such as $\max_a \mathrm{Acc}_a - \min_a \mathrm{Acc}_a$ or standard deviation across groups, to confirm that the qualitative conclusions do not depend on the TVD construction?

7. The paper claims the method reduces confounds from contextual image content. Could the authors add an experiment using tightly cropped faces or synthetic counterfactual pairs to test that claim more directly?

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies demographic disparities in LVLM behavior using gender and race labels from FairFace. The core topic is fairness, so bias-related ethical considerations are inherently present. I do not see a clear ethical violation in the conduct of the work as presented, but the benchmark design and interpretation should be handled carefully because the paper uses discrete gender and race categories and may encourage overinterpretation of generated demographic differences as unfairness without fully isolating causal demographic effects.

## Soundness Rating
2: fair. The paper is empirically interesting and the refusal-rate evidence is strong, but the central interpretation of the measured disparities is not sufficiently isolated from confounds, and the metric and validation choices leave important technical questions unresolved.

## Presentation Rating
3: good. The paper is generally clear and well organized, with effective figures and tables, but some key assumptions and metric details need sharper justification in the main paper.

## Contribution Rating
2: fair. The guardrail-agnostic evaluation angle is useful and practically relevant, especially given Table 1, but the methodological limitations substantially reduce the strength of the claimed fairness conclusions.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The refusal problem is real and the proposed protocol is practically useful, but the current paper overclaims what its measurements establish. In particular, the framework does not convincingly disentangle demographic bias from other image-conditioned effects, and the benchmark design choices leave enough ambiguity that I do not think the work is ready for ICLR main track in its present form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main methodological choices, metric definitions, figures, and tables carefully.