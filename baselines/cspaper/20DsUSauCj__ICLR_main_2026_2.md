---
job_id: b0af62e8-22c7-44cf-889f-5186047e8c23
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 20DsUSauCj.pdf
paper: Persona Vectors: Monitoring and Controlling Character Traits in Language Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically representation learning, interpretability of learned representations, activation steering, and safety/alignment of language models.

## Minimum Quality
Pass ✅. The submission contains the core components expected of a research paper, including abstract, introduction, methodology, experiments/results, and conclusion, and it presents substantial empirical evidence rather than a thin technical report. There are notable limitations and some underspecified methodological details, but not fatal flaws that would warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious prompts targeting automated reviewers, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes an automated pipeline for extracting trait-specific linear directions in LLM activation space, called persona vectors, from only a natural-language trait description. The paper studies these vectors as tools for steering and monitoring behaviors such as evilness, sycophancy, and hallucination, and extends this to finetuning-time analysis, including a preventative steering method and a data-screening metric based on projection differences. Experiments on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct suggest that these vectors correlate with prompt-induced and finetuning-induced persona shifts, and can be used to mitigate or predict such shifts.

## Strengths
The paper tackles a meaningful and timely problem. Understanding persona drift, especially shifts induced by finetuning or context, is practically important for alignment and deployment, and the paper frames this in a representation-centric way that is appropriate for ICLR.

A real strength is the breadth of the empirical story. The paper does not stop at showing that a direction can steer behavior. It connects one extracted vector to several use cases: deployment-time steering, prompt-time monitoring, finetuning-time monitoring, train-time mitigation, and pre-finetuning data screening. Figure 1 on Page 2 is useful here because it makes the scope of the claimed pipeline and applications very clear; importantly, the experiments later do try to instantiate each of those boxes rather than leaving them as hand-wavy possibilities.

The steering results are convincing at a high level. In Figure 2 on Page 4, the layer-wise curves show a clear coefficient-dependent effect for all three traits, which supports the claim that the extracted vectors have causal leverage rather than being mere correlates. The fact that the strongest effect appears at specific intermediate layers, rather than uniformly everywhere, also makes the representation-learning story more plausible than a trivial surface-level artifact. The qualitative examples in the bottom half of Figure 2 are unpleasant but useful, because they show the steered generations are semantically aligned with the claimed traits rather than just changing tone.

The finetuning analysis is the most compelling part of the paper. Figure 4 on Page 6 shows strong correlations between finetuning shift and post-finetuning trait expression across multiple datasets and both model families. This is stronger than the now-standard “we can steer it” result, because it suggests a representation-level account of behavioral drift during adaptation. Likewise, Figure 7 on Page 9, relating projection difference in training data to post-finetuning behavior, is a practically interesting result with immediate implications for dataset curation.

The preventative steering idea in Section 5 is interesting and empirically relevant. Figure 5 on Page 7 is one of the more persuasive figures in the paper because it compares inference-time and train-time interventions on both the target trait and a general capability metric. Even if the underlying mechanism is not fully unpacked, the result that train-time steering can reduce undesirable drift while preserving MMLU better than inference-time steering is useful. Figure 6 on Page 8 strengthens this further on a fact-acquisition setting, where the tradeoff between hallucination mitigation and utility is particularly important.

The appendix contains useful sanity checks for the evaluation pipeline. In particular, Table 1 on Page 28 reports high agreement between the LLM judge and human pairwise judgments, and Table 2 on Page 31 usefully distinguishes overall correlation from within-condition correlation. Those details do not eliminate all concerns, but they do show the authors are aware that their central claims depend heavily on the judge and on the distinction between coarse condition-level effects and subtler behavioral prediction.

The paper is generally well organized and easy to follow. The main narrative arc, extraction, validation, finetuning analysis, mitigation, then data screening, is coherent. Figures are doing real work throughout rather than serving as decoration.

## Weaknesses
1. **The core extraction and selection procedure is more heuristic than the paper’s framing suggests, and some critical choices are tuned on the very behaviors later used to validate the vectors.**  
   In Section 2.2 on Page 3, the persona vector is defined as a difference in means between filtered positive and negative responses. That is fine as a starting point. The issue is that the “most informative layer” is then selected by testing steering effectiveness across layers, and that chosen layer is used for subsequent analysis. This creates a circularity risk: the representation is selected partly by how well it steers the target behavior, and later the paper presents successful steering and behavior correlation as validation of that representation. Appendix D.4 confirms this layer is picked by maximizing trait expression under steering. This does not invalidate the result, but it inflates confidence that the discovered vector is a naturally privileged representation rather than a direction selected because it already optimizes the downstream intervention metric. A cleaner protocol would separate extraction, layer selection, and final evaluation more rigorously, for example by using a held-out layer-selection set or fixing a layer-selection rule independent of steering outcomes.

2. **The evaluation stack relies heavily on LLM-judged synthetic artifacts, and the paper’s strongest claims are therefore downstream of several model-generated components.**  
   Section 2.1 on Page 3 uses Claude to generate contrastive prompts, elicitation questions, and a rubric, then GPT-4.1-mini to score trait expression. This means the trait definition, the extraction data, and the main evaluation signal are all substantially mediated by external LLMs. The appendix provides some reassurance, especially Table 1 on Page 28 with human agreement rates, but the validation is still relatively narrow. The human study is pairwise and only distinguishes high-score vs low-score responses, not calibration across the full 0 to 100 scale. More importantly, the judge may encode its own conception of “evil”, “sycophancy”, or “hallucination”, and this conception is likely aligned with the prompts used to generate the data in the first place. The paper does acknowledge edge cases in Appendix D.2, but in the main paper the rhetoric occasionally sounds stronger than what this evaluation setup supports. This matters because many of the paper’s central quantitative conclusions, including Figures 2 through 8, are only as solid as this judge pipeline.

3. **Several claims about trait specificity are weaker than the main narrative suggests.**  
   On Page 6, Section 4.2 reports that within-trait correlations are higher than “cross-trait baselines”, but the stated cross-trait baseline range, \(r = 0.34 - 0.86\), is still quite high. A cross-trait correlation as large as 0.86 is not a small nuisance, it means the disentanglement between persona axes is limited in at least some settings. The paper tries to deflect this to dataset co-occurrence effects, and Appendix I.2 expands on that, but the main-text phrasing still overstates trait specificity. Figure 4 itself looks strong, but without a direct main-text panel for cross-trait comparisons the reader may overinterpret these vectors as clean trait coordinates. I would encourage the authors to be more explicit that these vectors are useful but not cleanly disentangled, especially for broad negative-trait datasets where multiple undesirable behaviors co-vary.

4. **The proposed preventative steering method is interesting, but the mechanistic justification is still speculative and the comparison set is too limited in the main paper.**  
   Section 5.1 on Pages 6 to 7 argues that adding \(+\alpha v_\ell\) during training counteracts the training objective’s tendency to move the model in that direction. That intuition may be right, but it is still an intuition. As written, the intervention looks almost paradoxical: to reduce acquisition of an undesirable trait, the method steers *toward* the corresponding persona vector during training. The paper gives an informal explanation, but no formal derivation, no local linearization argument, and no analysis of gradient interactions. Equation-wise, the intervention is simply
   \[
   h_\ell \leftarrow h_\ell + \alpha v_\ell,
   \]
   both at inference time and during training, yet the effects are claimed to differ qualitatively. That can happen, but the paper should explain this more rigorously. Also, the strongest baseline comparisons to CAFT, regularization, prompting, and all-layer steering are mostly deferred to Appendix L. In the main paper, Figure 5 compares only against inference-time steering. Since the paper’s novelty is concentrated in the train-time intervention, the main paper should have included at least one stronger baseline comparison there rather than pushing most of that evidence to the appendix.

5. **The mathematical formulation of the monitoring and screening metrics is underspecified in places, and the notation mixes token positions and averaged activations in a way that obscures what is actually being compared.**  
   For prompt monitoring in Section 3.3 on Page 4, the paper measures the projection of the final prompt token onto the persona vector. But the vector itself was extracted in Section 2.2 from residual stream activations averaged over response tokens. In Section 4.2 on Page 6, finetuning shift is computed using averages of the *last prompt token* across evaluation prompts; in Section 6.1 on Pages 8 to 9, projection difference uses \(a_\ell(x_i, y_i)\), defined as mean activation over *response tokens*. So the paper jumps between response-averaged activations and last-prompt-token activations for different applications. That may be empirically effective, but it weakens the conceptual neatness of “the” persona vector as a single representation. More concretely, Equation (3) for projection difference,
   \[
   \Delta P = \frac{1}{|\mathcal D|} \sum_i \left[a_\ell(x_i,y_i)-a_\ell(x_i,y'_i)\right]\cdot \hat v_\ell,
   \]
   leaves unclear whether the same layer chosen via response-based steering is always appropriate for response-level and prompt-level projection metrics. A more careful notation would distinguish \(a_\ell^{\text{resp-avg}}\) from \(a_\ell^{\text{prompt-last}}\), and the paper should justify why a vector extracted from one token aggregation transfers to another without retraining or recalibration.

6. **The empirical coverage is narrower than the paper’s broad claims.**  
   The main paper studies only two mid-size open models and three negative traits. The appendix broadens this somewhat, but per the review standard the core evaluation should stand on the main paper. For deployment monitoring, Figure 3 on Page 5 mostly covers explicit system-prompt interpolations, which are a relatively easy regime. The paper itself admits that within-prompt-type correlations are more modest. Table 2 on Page 31 makes this especially clear for hallucination, where within-condition correlation under system prompting is only 0.245. That is a useful and honest result, but it substantially narrows the practical claim: these vectors seem good at detecting gross prompt regime changes, less clearly at detecting subtle latent drift. Likewise, the finetuning experiments use synthetic or semi-synthetic datasets intentionally designed to induce the target traits or related flaws. This is useful for controlled study, but it makes the real-world generalization story less certain than the prose sometimes implies.

7. **Some experimental choices raise concerns about confounding between trait expression and generic response quality/style degradation.**  
   The steering examples in Figure 2 and in Appendix Tables 3 to 5 often show not just trait amplification or suppression, but also clear shifts in coherence, verbosity, or factuality. Figure 5 tries to track MMLU as a general capability measure, which is helpful, but one benchmark is a thin proxy for overall side effects. For example, in Figure 6 on Page 8 the inference-time intervention reduces hallucination but also sharply hurts new-fact accuracy, suggesting the method may be suppressing confidence or generation richness more broadly, not just “hallucination” as a distinct persona. Similarly, the sample-level separability shown in Figure 8 on Page 10 is encouraging, but histograms of one-dimensional projections do not tell us whether the method is isolating the target trait or simply flagging data that is atypical, roleplay-heavy, or stylistically different from the base model’s natural response distribution. This matters because the paper positions projection difference as a practical screening signal; in deployment, false positives from stylistic or domain shift would be costly.

8. **The novelty claim should be positioned more carefully relative to existing representation-engineering and persona-steering work.**  
   The paper does cite a fair amount of relevant prior work, including representation engineering, activation steering, and prior personality-trait directions. That said, the extraction method itself, synthetic contrastive prompt generation plus difference-in-means directions, is fairly incremental relative to the cited literature. The strongest novelty is not “persona vectors exist” or even “natural-language trait descriptions can produce directions”, since the paper itself cites related automated concept-direction pipelines and personality-trait analyses. The more distinctive contribution is the finetuning-drift analysis and the preventative steering intervention. I think the paper would be stronger if it stated that more plainly instead of occasionally making the extraction pipeline sound like the primary novelty.

9. **There are some presentation issues and redundancies that, while not fatal, make the paper read as slightly less polished than the strength of the experiments deserves.**  
   On Page 7, the paragraph beginning “We compared preventative steering against alternative training interventions” appears twice in near-duplicate form. There are also places where strong claims are made in the main text while the caveats are only in the appendix, for example the dependence on explicit prompt types in monitoring. This is fixable, but for a paper making broad safety-relevant claims, the main text should surface the caveats more centrally.

## Questions
1. **Layer selection and circularity:** Can the authors provide a stricter evaluation in which the steering-effective layer is selected on a held-out set, and all reported steering/monitoring results are then computed on disjoint prompts? I would like to know whether the qualitative shape in Figure 2 and the correlations in Figures 3 and 4 remain comparably strong under a cleaner split.

2. **Token-position transfer:** The paper extracts vectors from response-averaged activations but uses last-prompt-token projections for monitoring and finetuning-shift analyses. Can the authors justify this transfer more directly? For example, does a vector extracted from prompt-last activations perform materially differently from the response-avg vector when used for Sections 3.3 and 4.2? A side-by-side comparison in the main text or rebuttal would help.

3. **Trait specificity:** Since cross-trait baseline correlations can be high, can the authors report a clearer main-text analysis of specificity, perhaps a matrix analogous to Appendix Figure 21 but focused on the three main traits and the exact datasets used in Figure 4? This would help determine whether the vectors capture distinct traits or a broader “undesirable assistant mode”.

4. **Preventative steering mechanism:** Can the authors provide a more concrete explanation for why adding \(+\alpha v_\ell\) during training reduces movement toward that trait after training? Even a local optimization argument or gradient decomposition would materially increase my confidence. Right now the method works empirically, but the rationale is still a bit magical.

5. **Baselines in the main paper:** Could the authors bring one stronger train-time baseline into the main text, especially CAFT or the regularization baseline from Appendix L? Figure 5 is useful, but the current main-text comparison mostly shows “our train-time intervention is better than standard inference-time steering,” not “our intervention is the best or most robust train-time option.”

6. **Judge robustness:** Since the paper is heavily dependent on GPT-4.1-mini scoring, can the authors report whether the main trend lines in Figures 4, 5, and 7 are robust to at least one alternative judge or to a simpler rule-based / benchmark-based proxy where applicable? I do not need exhaustive relabeling, but some evidence that the conclusions are not judge-fragile would help.

7. **Real-world screening precision:** For the projection-difference screening idea, can the authors provide at least one estimate of false-positive behavior on clean but stylistically unusual data? Figure 8 shows separability on curated datasets, but for practical filtering I care about how often the method flags benign creative, roleplay, or domain-specific samples.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper includes methods for eliciting, amplifying, and analyzing harmful model traits such as evil behavior and deceptive or hallucinatory behavior. This appears throughout the paper, including the trait extraction setup in Section 2, the steering experiments in Section 3, and the harmful-response generation prompts in Appendix F. While the work is framed around monitoring and mitigation, the same methods also lower the barrier to inducing undesirable behaviors through activation steering or targeted finetuning. The appendix explicitly warns that it contains unfiltered offensive content, and several qualitative examples demonstrate harmful outputs. I do not view this as disqualifying, but it does warrant ethics review because the paper provides actionable techniques for behavior manipulation of chat models.

## Soundness Rating
3: good. The empirical findings are substantial and mostly support the main claims, but there are important concerns around evaluation dependence, token-position inconsistency, and the degree of trait specificity.

## Presentation Rating
3: good. The paper is generally clear and well organized, with effective figures, but there are some redundancies, some key caveats are pushed to the appendix, and a few methodological choices are not explained as crisply as they should be.

## Contribution Rating
3: good. The finetuning-drift analysis and preventative steering angle are valuable contributions, though the extraction method itself is closer to an incremental synthesis of existing representation-engineering ideas than the paper’s framing sometimes suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem, presents a broad and mostly convincing empirical study, and has at least one genuinely useful idea in preventative steering. I am positive overall, but only narrowly so, because the evidence rests heavily on an LLM-judged synthetic pipeline and the specificity/mechanistic story is not yet as clean as the narrative implies.

## Reviewer Confidence
4: confident. I am familiar with the relevant literature on activation steering, representation engineering, and LLM behavior control, and I checked the main methodological details carefully, though I did not independently verify appendix-only claims.