---
job_id: 73dd91f9-25fd-4b2d-98cc-46101cd55095
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: NlHHlqP1zk.pdf
paper: Are Large Language Models Good XAI Annotators?
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, focusing on evaluation of automated concept annotations for XAI and multimodal models, with direct relevance to interpretability, representation learning, and benchmarking.

## Minimum Quality
Pass ✅ The paper contains the essential components expected of a research submission, including abstract, introduction/background, methodology, experiments/results, and conclusion. While I have substantial concerns about methodology, validation, and positioning, these are review-level weaknesses rather than desk-reject-level omissions or fatal incompleteness.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies whether LLM/VLM-based automated annotators produce concept annotations that are sufficient for concept-to-class reasoning in XAI settings. The authors propose the Fast and Slow Effect (FSE) framework, which evaluates concept sufficiency by progressively eliciting annotations across five stages and measuring classification accuracy from concepts alone via a new metric, the Class Representation Index (CRI). Experiments across fine-grained and general visual datasets suggest that concept-only reasoning often underperforms direct visual classification, especially on fine-grained tasks, and that multimodal utility may overstate the quality of the underlying concepts.

## Strengths
- The paper asks a worthwhile question. A large amount of recent concept-bottleneck and VLM-for-XAI work implicitly assumes that auto-generated concepts are good enough if they help downstream prediction; challenging that assumption is useful for the community.

- The proposed evaluation framing is intuitive and easy to understand. The contrast between direct prediction from images and prediction from progressively accumulated concepts is a reasonable diagnostic idea, and the motivating example in **Figure 1** communicates the intended failure mode clearly. In particular, the example illustrates the exact phenomenon the paper wants to probe, namely that a model can classify correctly first, yet fail to recover the class from its own verbalized concepts when confronted with semantically similar alternatives.

- The framework is broad in scope in the sense that it can be applied to both post-hoc textual annotation and visual-grounded annotation settings. The side-by-side comparison in **Figure 3(a,b)** is helpful because it shows that the authors are not only examining one narrow prompting setup.

- The empirical results do expose an interesting and somewhat uncomfortable pattern: on fine-grained datasets, concept-only reasoning is much worse than direct visual prediction. **Table 2** makes this point sharply, with strongly negative CRI gaps for most model-dataset pairs. Even if I have concerns about the interpretation, the phenomenon itself is potentially useful to document.

- The preliminary distractor-selection experiment in **Table 1** is a sensible setup detail. The finding that semantically related distractors induce higher contradiction rates than random distractors is plausible and supports the choice of a harder evaluation protocol.

- The paper is generally readable, and the high-level pipeline in **Figure 2** is useful for orienting the reader. The decomposition into concept gathering, prediction mode, and metric is presented clearly enough that the main idea is easy to follow.

## Weaknesses
1. **The central evaluation is heavily confounded by using the same model family as annotator and evaluator, which undermines the claim that FSE measures annotation sufficiency rather than self-consistency or self-bias.**  
   This issue appears throughout Sections 4 to 6. The same model \(\mathcal{F}\) generates concepts and then predicts the class from those concepts, as formalized in **Eq. (1)** and **Eq. (2)** on **Pages 5 to 6**. This creates a closed loop where the evaluator is not independent of the generator. The paper cites self-assessment literature on **Page 4**, but that does not establish that self-evaluation here is valid or unbiased. In fact, self-preference and self-rationalization are a known risk in LLM evaluation.  
   Why this matters: if CRI is low, that could mean the concepts are insufficient; but it could also mean the model is bad at interpreting its own compressed textual outputs under a multiple-choice prompt. If CRI is high, it could reflect stylistic self-compatibility rather than concept sufficiency. Without cross-model evaluation, human calibration, or some external reference, it is hard to interpret CRI as a property of the annotations themselves.

2. **The comparison between fast and slow modes is not clean, because the two modes operate on fundamentally different information channels, making the main conclusion less surprising than the paper suggests.**  
   In **Section 4.1** on **Page 5**, fast mode predicts from the image, \(y_i^0=\mathcal{F}(x_i;\Theta)\), while slow mode predicts from text-only concepts, \(y_i^t=\mathcal{F}(c_i^t;\Theta)\). This is not merely “opaque reasoning” versus “conceptual reasoning”; it is a direct comparison between rich visual input and a lossy textual bottleneck that intentionally discards the original image. The drop from fast to slow in **Figure 3(a)** and **Table 2** is therefore not, by itself, evidence that models “cannot conceptualize their intrinsic knowledge.” It may simply show that verbalized concepts are an incomplete compression of the image, especially for fine-grained tasks.  
   Why this matters: the headline interpretation overreaches. The paper is really measuring performance under an extreme information bottleneck, not isolating whether concept supervision is intrinsically inadequate. The result in **Table 4**, where “Fuse” is close to “Fast,” is also largely expected under this framing, because the image channel remains dominant.

3. **CRI is presented as a principled metric for annotation sufficiency, but operationally it is just 5-way classification accuracy under a particular prompt and candidate construction. The paper does not validate that this metric corresponds to the stated concept of sufficiency.**  
   The definition on **Page 6, Eq. (2)** is simply
   \[
   CRI(\mathcal{F},t)=100\%\times \frac{1}{l}\sum_{i=1}^l \mathbf{1}[y_i^t=y_i].
   \]
   This is straightforward accuracy, not a “likelihood” as the text claims. More importantly, the metric depends entirely on the selected distractors, prompt wording, answer format, and the evaluator model. The paper does not establish that higher CRI tracks human judgments of concept sufficiency, or that a given CRI threshold corresponds to “sufficient” annotations in any meaningful sense.  
   Why this matters: the entire contribution hinges on CRI as the main scientific instrument. Without validation, the paper risks elevating a particular prompting-based accuracy number into a broader interpretability claim that it may not support.

4. **There are mathematical and definitional issues in the formulation, especially around Eq. (1), that make the methodology underspecified.**  
   In **Eq. (1)** on **Page 5**, the concept chain is defined as
   \[
   c_i^t=\bigcup_{j=1}^{t-1}\mathcal{F}(c_i^j, X_i;\Theta), \quad t=1,\ldots,T.
   \]
   This is problematic for several reasons. First, for \(t=1\), the union is over an empty index set, so \(c_i^1\) is undefined or empty, yet Stage 1 clearly should produce the first concept set. Second, the text immediately below says \(\mathcal{F}\) refines “the previous output \(c_i^{t-1}\),” which does not match the union over all \(j=1,\ldots,t-1\). Third, the notation conflates generating new stage-specific concepts with accumulating all prior concepts. A more coherent formulation would define stage-wise outputs \(\tilde c_i^t=\mathcal{F}(\tilde c_i^{t-1}, X_i;\Theta)\) with \(c_i^t=\bigcup_{s=1}^{t}\tilde c_i^s\), or something equivalent.  
   Why this matters: this is not just a cosmetic notation complaint. The paper’s core procedure is the concept accumulation process, and the current equation does not specify it correctly.

5. **The “Slow Mode Superiority” hypothesis is weakly justified and psychologically motivated in a way that does not cleanly transfer to these model evaluations.**  
   On **Page 6**, the paper motivates \(\Delta CRI_T = CRI(T)-CRI(0)\ge 0\) using dual-process theory and Kahneman’s “thinking fast and slow.” This is catchy, but the analogy is doing too much work. The fast mode here is full-image recognition, while the slow mode is concept-only forced reasoning after information has been compressed into text. There is no reason to expect the latter to dominate the former, even for a very capable model.  
   Why this matters: the paper frames negative \(\Delta CRI_T\) as a surprising scientific finding, but under the actual protocol it is not very surprising. This weakens the force of the main empirical claim.

6. **The empirical validation lacks crucial controls that would help disentangle whether the issue is the concepts, the prompting, or the evaluator.**  
   For example, the paper does not report:  
   - cross-evaluation, where concepts generated by model A are evaluated by model B;  
   - human-written concepts or dataset attribute annotations as a calibration point;  
   - performance with oracle concepts, or at least manually curated class descriptions;  
   - sensitivity to the number of distractors or candidate set size;  
   - sensitivity to prompt wording beyond the single structured template in **Appendix B**;  
   - whether stage-specific concepts are cumulative in token budget or roughly controlled for length.  
   This matters especially when interpreting **Figure 3**, where some models recover substantially from \(t=1\) to \(t=5\), while others do not. It is hard to know whether this reflects concept quality, prompt following, verbosity, or model-specific decoding behavior.

7. **The distractor construction strategy may itself bias the evaluation in ways that are not analyzed.**  
   In **Section 5.3** on **Page 7**, semantically related distractors are constructed using the top predictions of a pretrained ResNet-18. This is an engineering heuristic, but it raises several concerns. ResNet confusion classes are not necessarily semantically similar in the conceptual sense the paper wants to evaluate; they may reflect low-level visual similarity, dataset artifacts, or training biases. Also, the contradiction test in **Table 1** is only run on GPT-series models and only on 100 samples from three datasets, which is a thin basis for fixing the candidate strategy for the whole paper.  
   Why this matters: CRI is highly dependent on the candidate set. If the distractors are poorly aligned with the semantic sufficiency notion, then the metric may be probing model-specific confusion patterns rather than concept completeness.

8. **Several conclusions are stronger than what the evidence supports.**  
   For instance, the abstract and conclusion state that current annotation methods “fail to provide sufficient semantic coverage” and that annotators struggle to “externalize implicit expertise.” The data do show that concept-only classification is weaker than image-based classification on fine-grained tasks. But that does not by itself show insufficiency of the concepts as XAI supervision, because concept bottleneck models and related methods do not usually require the concepts alone to fully recover the class under a 5-way hard multiple-choice setup.  
   Why this matters: the paper risks setting up a straw-man criterion, then concluding that current methods fail that criterion. The criterion may be interesting, but its relationship to practical concept-based learning remains under-argued.

9. **The paper’s positioning relative to broader LLM-as-annotator literature is incomplete.**  
   The manuscript cites XAI and concept-bottleneck work extensively, but it barely engages with the broader literature on whether LLMs are reliable independent annotators versus assistants in annotation workflows. Since the title asks “Are Large Language Models Good XAI Annotators?”, stronger positioning against the more general annotation literature would improve the paper’s framing and sharpen what is unique about the XAI setting.  
   Why this matters: without this comparison, the contribution can read as narrower and more self-contained than it should be, especially because some of the observed failure modes may reflect general issues in LLM annotation, not properties specific to concept-based XAI.

10. **Presentation is readable at a high level, but some claims and figure interpretations are overstated relative to what is shown.**  
   **Figure 2** is helpful as a schematic, but it visually suggests that CRI should rise with more steps, which may prime the reader toward the intended conclusion before the evidence is presented. In **Figure 3**, the caption says “annotation sufficiency generally improves,” which is true across \(t>1\) in some plots, but it also visually highlights a severe collapse from \(t=0\) to \(t=1\) in the visual-grounded setting. That collapse is arguably the most important story in the figure, yet the paper does not analyze it carefully. Likewise, **Figure 4** is a decent qualitative case study, but it is anecdotal and selected only for GPT-4o; it should not carry much evidentiary weight for the broader claims.

11. **The reproducibility statement is incomplete in the main paper.**  
   On **Page 10**, the paper states “We have provided the code and data at here.” This is not actually a usable reproducibility statement in the submission as written. Given how sensitive the evaluation is to prompts, API versions, seeds, and candidate construction, the exact experimental artifacts matter quite a lot.

## Questions
1. **Can the authors provide cross-model evaluation results?**  
   For example, if GPT-4o generates the concepts, what happens when Qwen or Llama performs the concept-only class prediction, and vice versa? This would directly test whether CRI is measuring annotation sufficiency rather than model-specific self-compatibility.

2. **Can the authors justify or revise Eq. (1)?**  
   As written on **Page 5**, \(c_i^1\) appears undefined because the union is empty for \(t=1\). Please provide a precise recursive definition of stage-wise concept generation and accumulated concept sets.

3. **How sensitive are the conclusions to the candidate set construction?**  
   The entire metric is based on 5-way selection with four distractors. Please report results for different numbers of distractors, and ideally with alternative ways of defining “semantic similarity” beyond ResNet-18 confusion classes.

4. **Can the authors provide a calibration experiment using human-written or oracle concepts?**  
   Even a small-scale study on one dataset would help establish whether CRI behaves as intended. If human or dataset-attribute concepts achieve much higher CRI than model-generated concepts, that would materially strengthen the paper.

5. **Why should “slow mode superiority” be expected under the current protocol?**  
   Since fast mode has access to the image and slow mode does not, I do not find \(\Delta CRI_T \ge 0\) to be a natural null expectation. A stronger rebuttal would either defend this expectation carefully or reposition the finding as an empirical comparison rather than a violated theoretical hypothesis.

6. **Can the authors disentangle information loss from reasoning failure?**  
   For instance, what happens if slow mode is allowed to see both the image and the concepts but is forced to justify the decision from concepts, or if the image is summarized by a stronger external captioner? This would help separate “the model cannot verbalize discriminative concepts” from “the prompt compresses away the evidence.”

7. **Please clarify the exact sampling and evaluation protocol.**  
   How many samples per dataset are used in the main experiments, how are seeds varied, are the same sampled examples used across all models, and are API/model versions fixed? This is especially relevant given the very small error bars claimed in **Figure 3**.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper discusses limitations and bias risks of automated annotation in **Section 8**, but based on the submitted content I do not see a concrete ethics violation or a dataset/use pattern that independently requires formal ethics escalation. My concerns are primarily methodological rather than ethical.

## Soundness Rating
2: fair. The empirical phenomenon is interesting, but the core metric and conclusions are not adequately validated, the generator/evaluator coupling is a serious concern, and the mathematical specification in the methodology has nontrivial issues.

## Presentation Rating
2: fair. The paper is readable and the figures are helpful, but several key formulations are underspecified, some interpretations are overstated, and important methodological details are not nailed down cleanly.

## Contribution Rating
2: fair. The problem is relevant and the framing has some value, but the current execution does not yet convincingly establish CRI/FSE as a reliable evaluation framework for annotation sufficiency.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper raises a useful question and surfaces an interesting empirical pattern, especially in **Figure 3**, **Table 2**, and **Table 4**. However, the current methodology does not isolate annotation sufficiency cleanly enough to support the strength of the claims. The self-evaluation loop, the information-channel confound between fast and slow modes, the lack of metric validation, and the issues in the formalization keep this below the ICLR bar for me in its present form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main concerns are based on close reading of the equations, protocol, figures, and tables, and on familiarity with multimodal evaluation and concept-based modeling.