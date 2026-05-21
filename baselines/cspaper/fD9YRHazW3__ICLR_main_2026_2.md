---
job_id: b941dbbf-1c0a-493d-88a6-4afc9c67076d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: fD9YRHazW3.pdf
paper: In-Context Watermarks for Large Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically LLM watermarking, model behavior under in-context learning, and safety/accountability for language models.

## Minimum Quality
Pass ✅ The paper includes the expected scientific components, namely abstract, introduction, related work, method description, experiments, quantitative results, and conclusion/discussion. While I have substantive concerns about novelty, generality, and some methodological details, these are review-level concerns rather than desk-rejection-level flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence that the submission itself contains hidden instructions aimed at manipulating the review process. The paper studies indirect prompt injection and explicitly presents watermarking prompts as part of the research content, which is different from embedding concealed instructions in the submission to influence reviewers.

# Expected Review Outcome:
## Summary
This paper studies "In-Context Watermarking" (ICW), a family of watermarking methods for LLM-generated text that require only prompt access to the model, rather than access to logits or decoding. The authors instantiate four strategies, Unicode, Initials, Lexical, and Acrostics, define corresponding detectors, and evaluate them in both a direct prompting setting and an indirect prompt injection setting motivated by detecting AI-generated peer reviews.

## Strengths
The paper tackles a practically relevant problem that is underexplored in the watermarking literature, namely how to embed detectable signals when the party deploying the watermark does not control decoding and only has API or prompt-level access. That problem formulation is meaningful, especially for scenarios like third-party applications or misuse tracing where standard in-process watermarks are unavailable.

The paper is easy to follow at the high level. **Figure 1** on Page 2 does a good job of clarifying the intended deployment model: watermarking is not done by perturbing token probabilities, but by persistent instruction conditioning. **Figure 2** on Page 4 is also useful because it grounds the IPI case study in a concrete workflow, from stamping the paper to later detecting a watermark in a submitted review. Even if one is skeptical about the ethics or deployability of that scenario, the figure makes the threat model legible.

The empirical results are stronger than I initially expected given how simple some of the prompting schemes are. In particular, **Table 2** on Page 8 shows a very sharp capability dependence: the same ICW methods that are weak on GPT-4o-mini become highly detectable on GPT-o3-mini, including in the IPI setting. That is a useful empirical finding in its own right, because it suggests these methods are less about a specific algorithmic trick and more about exploiting increasingly reliable instruction-following.

The paper covers several evaluation dimensions rather than reporting only clean detection. Detection, robustness, and text quality are all considered, and the authors compare against black-box post-hoc baselines in the DTS setting. The robustness plots in **Figure 3** and the quality comparisons in **Table 3** give a more complete picture than a single AUC table would.

The main detection statistics for Initials and Lexical ICW are simple and interpretable. The z-score style detectors are easy to understand, and the appendix-level false-alarm discussion at least indicates the authors are thinking about type-I error control rather than only reporting ROC curves.

## Weaknesses
1. **The core conceptual novelty is limited, and the paper does not fully convince me that ICW is more than prompt-engineered style steering plus straightforward hypothesis testing.**  
   The four methods in Section 4 are essentially prompt-level realizations of already familiar watermarking ideas: invisible Unicode insertion, green-list lexical biasing, initial-letter biasing, and acrostic constraints. I do not object to rethinking watermarking in a black-box setting, that part is interesting, but the actual method layer feels quite incremental. The paper would be stronger if it articulated a more principled abstraction of what makes a prompt-level watermark possible, or identified conditions under which such watermarks can and cannot exist. As written, the scientific contribution feels closer to "current frontier LLMs can be instructed to self-watermark in several ways" than to a new watermarking framework with clear conceptual boundaries.

2. **The strongest results rely almost entirely on one stronger proprietary model, which materially weakens the claim of practical generality.**  
   This is the single biggest issue for me. In **Table 2** on Page 8, several methods are near-random or very weak on GPT-4o-mini, especially Initials and Acrostics, yet become almost perfect on GPT-o3-mini. That is a dramatic model-capability cliff. The paper itself leans into this, but that also undercuts the broader practical claim that ICW is a generally usable "model-agnostic" solution. It is model-agnostic only in the narrow sense that no decoding access is needed; it is not performance-agnostic across models. This matters because a watermarking method that works only on very strong instruction-following LLMs is not yet a robust deployment story, particularly if the user can choose weaker or differently aligned models.

3. **The comparison to baselines is only partially fair because the baselines solve a somewhat different problem, and the paper does not include stronger alternative black-box misuse-detection baselines in the IPI setting.**  
   In Section 5.1, the paper compares ICW in DTS against PostMark, YCZ+23, and GPTZero. But PostMark and YCZ+23 are post-processing methods, not methods that operate by in-context instruction. That makes them reasonable comparison points for black-box constraints, but not direct substitutes in the IPI threat model. The paper then states that baselines are not applicable in IPI, which is true for watermark embedding baselines, but this leaves the IPI evaluation without a meaningful competing approach. For the most practically important claim, namely detecting AI-generated reviews in the IPI setting, the reader is shown only ICW numbers without comparison to stronger detector-based alternatives or even ablations against simpler injected heuristics. The result is that the paper demonstrates feasibility, but not relative advantage.

4. **Some of the detection formulations are underspecified or statistically shaky in the main paper, especially for Acrostics and, to a lesser extent, Lexical/Initials.**  
   In Section 4.2.4 on Page 7, the Acrostics detector is defined as
   \[
   D(\mathbf{y}\mid \mathbf{k}_s,\tau_s)=\frac{\mu-d(\boldsymbol{\ell},\boldsymbol{\zeta})}{\sigma},
   \]
   where \(\mu\) and \(\sigma\) are estimated by resampling sentence-initial sequences from the suspect text itself. This raises several questions that are not answered in the main paper: what exactly is the resampling distribution, what sequence lengths are used, how overlapping samples are handled, and why this yields a calibrated test statistic under \(H_0\)? Since the null is estimated from the same suspect text, this is not an obviously valid standardized statistic. The appendix acknowledges the lack of rigorous false-alarm analysis for Acrostics, which is fine, but then the main paper should be much more cautious about treating this as a principled detector.

   For Initials and Lexical ICW, the detector
   \[
   D(\mathbf{y}\mid \mathbf{k},\tau)=\frac{|\mathbf{y}|_G-\gamma |\mathbf{y}|}{\sqrt{\gamma(1-\gamma)|\mathbf{y}|}}
   \]
   is reasonable as a heuristic, but the null model depends heavily on how \(\gamma\) is estimated. On Page 6, \(\gamma\) for Initials is estimated from the Canterbury Corpus. That assumes transferability of initial-letter frequencies from that corpus to the actual human or unwatermarked LLM outputs used in experiments. The paper does not show calibration diagnostics for this assumption. In practice, the base rate of initial letters or green words is domain- and model-dependent, so the detector may be miscalibrated outside the reported setup.

5. **The theoretical claim is weaker than the prose suggests, and the main paper somewhat overstates it.**  
   On Page 6 the paper says, "For Initials and Lexical ICWs, we provide a theoretical guarantee on controlling the false alarm rate." But in the appendix, Theorem B.1 is effectively inherited from prior green/red-list analysis and applies under randomness over the selected green set for a fixed suspect text. That is much narrower than many readers will infer from the main text. It does not model the LLM, does not characterize miss detection, and does not guarantee well-calibrated operation under realistic distribution shift. I do not object to including the theorem, but the main-paper wording should be toned down and the scope of the guarantee should be made explicit near the claim.

6. **The robustness story is selective and weaker than the headline suggests.**  
   The paper emphasizes robustness, but the details are mixed. In **Figure 3** on Page 9, Initials and Acrostics look very strong under certain attacks for GPT-o3-mini, but the omitted Unicode curves are not a minor detail, they are a core caveat. The text later states Unicode is effectively destroyed by paraphrasing and cross-platform transmission. That is not a side note, it is a major practical limitation for the easiest and most model-independent ICW scheme. Likewise, **Table 5** in the appendix shows Lexical ICW degrading substantially under replacement attacks even on GPT-o3-mini, with ROC-AUC \(0.758\) and T@1%F \(0.092\). So the robustness picture is highly method-dependent, and the stronger claims should be broken down more carefully in the main text.

7. **The text quality evaluation is not as convincing as the paper implies.**  
   **Table 3** on Page 9 reports very high LLM-as-a-judge scores for most ICW methods, but there are at least two concerns. First, the judge is another proprietary LLM, which can smooth over stylistic oddities that humans would notice. Second, some methods visibly trade off clarity, especially Initials ICW, whose clarity score drops to 3.706 while unwatermarked text is 4.994. That is not a negligible degradation. The paper says ICW methods exhibit quality "comparable" to human and unwatermarked text, but for Initials that is hard to justify from the table. The claim should be more granular: Unicode, Lexical, and Acrostics appear relatively benign on this metric, while Initials is noticeably worse.

8. **The IPI application is interesting but operationally underdeveloped, and the paper sidelines the hardest parts.**  
   The motivating case study is detecting AI-generated peer reviews by hiding watermark instructions inside submitted PDFs. This is provocative and timely, but the actual deployment assumptions are brittle. The paper admits on Page 5 that defenses, instruction removal, and attack strategies are mostly left for future work. That is exactly the hard part for IPI. If a reviewer copies only selected text, uses OCR, strips formatting, pastes into a different interface, or prepends stronger system-like instructions, the watermark may fail. The appendix includes one "ignore prior prompts" experiment, but that is far from a comprehensive treatment. Given how central the IPI narrative is to the paper's significance, the current evidence feels more like a proof of concept than a realistic detection pipeline.

9. **The notation and presentation have several rough edges that matter for technical clarity.**  
   There are multiple places where notation is loose. For Unicode ICW on Page 5, the generated response is written as \(\{y^{(1)}, \backslash u200B, \dots, y^{(n)}, \backslash u200B\}\), which mixes token- and word-level views without clarifying indexing. The Unicode detector is defined as
   \[
   D(\mathbf{y}\mid \mathbf{k}_u,\tau_u)\coloneqq \frac{|\mathbf{y}|_{\mathbf{k}_u}}{N},
   \]
   but \(N\) is not clearly defined in that subsection. Is it the number of words, characters, tokens, or some normalized length? The detector description is too terse for something presented as a core method. Similar underspecification appears in the Acrostics section regarding sentence segmentation and skipped letters. These are fixable issues, but they reduce confidence that the methods are fully pinned down in the main paper.

10. **The paper would benefit from much stronger analysis of the "what is the watermark key" question and spoofing resistance.**  
   For Initials ICW, the paper itself notes on Page 6 that if an adversary becomes aware of the scheme, \(\mathcal{A}_G\) can be inferred and spoofed. This is not a side vulnerability, it is close to a structural weakness. More broadly, in ICW the watermark often looks like a stylistic constraint in natural language. That makes it easier to imitate once known. The paper discusses this only briefly. A stronger submission would analyze key entropy, scheme distinguishability, and the cost of forging a watermark with or without partial scheme knowledge. Right now the security story is underdeveloped relative to the watermarking framing.

## Questions
1. The main empirical claim depends heavily on GPT-o3-mini in **Table 2**. Can the authors provide a clearer characterization of what model capability is actually required for each ICW method? For example, is there a measurable instruction-following or retrieval threshold beyond which Initials/Lexical/Acrostics become reliable? A capability analysis would help separate a general method from a model-specific artifact.

2. For the Acrostics detector in Section 4.2.4, please specify the exact resampling procedure used to estimate \(\mu\) and \(\sigma\): how are the sequences \(\widehat{\ell}_j\) sampled, what is their length, are they contiguous or arbitrary subsequences, and how sensitive are the reported AUCs to these choices? This is important because the statistical validity of the detector is currently hard to assess.

3. For Initials ICW, why is the null parameter \(\gamma\) estimated from the Canterbury Corpus rather than from held-out human text in the target domain or from unwatermarked outputs of the same model family? Please provide evidence that the detector is well calibrated under domain shift, since otherwise low-FPR claims may not transfer.

4. In **Table 3**, Initials ICW has a noticeable clarity drop relative to unwatermarked text. Can the authors quantify the quality-detectability trade-off by sweeping watermark strength, for example green-list size or prompting emphasis, rather than only showing one operating point per method? That would make the comparison much more informative.

5. The IPI case study is central to the paper's motivation, but the attack surface is only lightly explored. Could the authors add experiments for more realistic reviewer behaviors, such as partial-copy input, OCR extraction, copy-paste through plain-text channels, or document cleaning tools? Positive results there would substantially strengthen the practical significance.

6. For Unicode ICW, the detector is defined using \(D(\mathbf{y}\mid \mathbf{k}_u,\tau_u)=|\mathbf{y}|_{\mathbf{k}_u}/N\), but \(N\) is not clearly specified in Section 4.2.1. Please define the normalization precisely and explain whether the detector is thresholded on absolute count or normalized density.

7. The theorem-based false-alarm guarantee is presented as a contribution, but it appears to adapt prior green-list analysis. Can the authors clarify exactly what is new here versus inherited from prior results, and whether any part of the guarantee depends specifically on the ICW setting rather than only on the random green-set construction?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper's main motivating application, especially in **Section 3.2** and **Figure 2**, involves covertly embedding hidden instructions into documents so that users who submit those documents to an LLM can later be identified through the generated output. I understand the intended use case is to detect policy-violating AI-assisted peer review, but this is still a form of concealed behavioral manipulation and tracking. That raises at least three concerns.

First, there are privacy and transparency issues. Users may not know that the document contains hidden instructions that alter downstream model behavior and facilitate attribution. Even if the target population is dishonest reviewers in the example, the technique itself is more general.

Second, the paper is effectively exploring a constructive use of indirect prompt injection. The same mechanism could be repurposed for harmful or deceptive applications beyond watermarking, especially since the appendix provides fairly explicit prompt templates.

Third, for the review-use case, the paper assumes covert modification of submitted PDFs. That may implicate responsible process design and policy questions in real conference settings, even if no human subjects were used in the study.

I do not view these concerns as disqualifying, but they should be acknowledged more concretely and with a sharper discussion of deployment safeguards, user notice, and abuse prevention.

## Soundness Rating
3: good. The empirical study is reasonably extensive and the main claims are supported as feasibility claims, but several detectors are underspecified or only heuristically justified, and the strongest conclusions depend heavily on one strong proprietary model.

## Presentation Rating
3: good. The paper is readable and the main idea is communicated clearly, with helpful figures and tables, but a number of technical details, definitions, and statistical assumptions are too loose in the main paper.

## Contribution Rating
2: fair. The problem setting is interesting and practically motivated, but the method layer is fairly incremental, and the broader contribution is limited by strong dependence on model capability and an underdeveloped security/deployment analysis.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a timely problem formulation and some compelling feasibility results, especially in **Table 2** and **Figure 3**, but I am not convinced the current version rises to ICLR main-track standards in contribution and methodological maturity. The strongest evidence is model-specific, the novelty is modest, and several core technical pieces need sharper definition and analysis.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the watermarking and LLM safety literature, though I did not independently verify appendix proofs line by line.