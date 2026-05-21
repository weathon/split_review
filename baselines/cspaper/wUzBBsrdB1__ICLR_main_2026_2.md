---
job_id: 7e231f5b-adb0-4292-bcc0-c0854a2d8802
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: wUzBBsrdB1.pdf
paper: Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is squarely about sparse autoencoders, representation learning, sparse coding, and interpretability of learned representations in LLMs, all of which are clearly within ICLR scope.

## Minimum Quality
Pass ✅ The paper contains the expected core components, including abstract, introduction, background/methodology, experiments, related work, and discussion, and it presents both toy-model and LLM experiments. While I have substantial concerns about the strength of some claims and the breadth of validation, these are review-level weaknesses rather than desk-rejection issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect any hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies the role of the sparsity hyperparameter \(L0\) in sparse autoencoders used for mechanistic interpretability. The authors argue, using toy models and LLM experiments, that setting \(L0\) too low or too high leads to feature mixing and degraded monosemanticity, and they propose a decoder-based proxy metric, decoder pairwise cosine similarity \(c_{\mathrm{dec}}\), to help identify a better \(L0\). The paper also argues that standard sparsity-reconstruction tradeoff plots can prefer incorrect SAEs over ground-truth disentangled ones when \(L0\) is set too low.

## Strengths
The main strength is that the paper focuses on an important and under-discussed issue in practical SAE use. The claim that \(L0\) is not merely a neutral point on a reconstruction-sparsity frontier, but can qualitatively change the learned decomposition, is a meaningful framing that many practitioners will care about.

The toy-model section is intuitive and, at its best, quite persuasive. In particular, **Figure 2** and **Figure 3** communicate the central phenomenon clearly: when the SAE \(L0\) is slightly below the true \(L0\), the decoder columns acquire signed components from correlated or anti-correlated features. The contrast between the middle and right panels in both figures makes the qualitative failure mode easy to see. Likewise, **Figure 1** gives a compact visual summary of the three regimes, low, correct, and high \(L0\), and is effective as a high-level conceptual figure.

The paper also makes a useful negative point about evaluation methodology. **Figure 4** is one of the more compelling parts of the paper because it directly visualizes the mismatch between reconstruction quality and feature correctness in the toy setting. The fact that the learned SAE curve can dominate the “ground-truth SAE” curve at low \(L0\) while still producing visibly mixed features, further illustrated in **Figure 5**, is an important cautionary message for the community.

I also appreciate that the paper does not stop at toy models. The LLM experiments on Gemma-2-2b and Llama-3.2-1b try to connect the toy-model story to realistic settings, and **Figure 8** and **Figure 9** suggest that the proposed decoder-based metric has at least some empirical alignment with sparse probing performance. Even if I am not fully convinced by the strength of the practical claims, the attempt to bridge mechanistic toy reasoning and large-scale empirical evidence is valuable.

Finally, the paper is generally readable. The core intuition is easy to follow, the notation in the main text is mostly manageable, and the discussion section is candid that \(c_{\text{dec}}\) is only a proxy and can be flat over a range of \(L0\) values.

## Weaknesses
1. **The strongest claims are broader than what the evidence in the main paper actually establishes.**  
The title and abstract make very strong statements, for example “incorrect \(L0\) leads to incorrect features” and “\(L0\) must be set correctly to train SAEs with correct features.” In the main paper, however, the evidence for “correct features” is rigorous only in toy models where ground-truth linear features are explicitly constructed. In the LLM setting, there is no ground truth, so the paper shifts to sparse probing and decoder-based heuristics. That is a much weaker evidentiary basis than the title suggests. On **Page 1-2** and again in the introduction, the framing reads almost like a universal claim, but the empirical support in **Section 4** really shows something narrower: low-\(L0\) SAEs often correlate with worse probing and larger decoder-cosine metrics on the tested models/layers. That gap matters, because “not optimal for probing” is not the same as “incorrect features,” and the paper sometimes blurs that distinction.

2. **The LLM validation is too narrow to support the paper’s practical recommendations with confidence.**  
The real-model experiments in **Section 4** cover only a small number of layers and two relatively modest LLMs, namely Gemma-2-2b and Llama-3.2-1b. The main paper emphasizes claims about “most commonly used SAEs” having \(L0\) that is too low, but that conclusion is not really supported by the breadth of experiments shown in the main text. Even within the presented results, the shapes are not fully consistent: **Figure 8** already shows that Gemma layer 5 has a long shallow region, while Llama looks more like the toy-model minimum. **Figure 9** further complicates the story by showing that BatchTopK and JumpReLU behave differently at high \(L0\), and the paper itself admits that the elbow rather than the global minimum may better align with sparse probing. This makes the practical prescription substantially less clean than the headline suggests. If the metric behavior depends on architecture and the relevant point is an “elbow” rather than the argmin, then the claim that the method “finds the correct \(L0\)” is overstated.

3. **The proposed proxy metric \(c_{\mathrm{dec}}\) is plausible but insufficiently justified in the main paper, especially for realistic overcomplete dictionaries.**  
The definition in **Equation (4)** is simple,
\[
c_{\text{dec}}=\frac{1}{\binom{h}{2}}\sum_{i<j}\left|\cos(\mathbf{W}_{\text{dec},i},\mathbf{W}_{\text{dec},j})\right|,
\]
but the argument for why minimizing this quantity should recover a meaningful \(L0\) in realistic SAEs is much thinner in the main paper than the prose implies. The intuition in **Section 3.5** assumes that correct latents should be “more orthogonal relative to each other,” yet modern SAEs are heavily overcomplete, and nothing in the main text establishes that a good, interpretable, or causally useful dictionary should minimize average pairwise cosine globally. Overcomplete dictionaries can legitimately contain related, hierarchical, or partially redundant features. The paper briefly acknowledges non-linear features only much later in limitations, but the concern is broader: even in linear settings, low pairwise cosine is not obviously equivalent to better disentanglement. The appendix theorem is not enough to close this gap for the main-paper claim, because it proves only a very stylized direction, shared-feature mixing increases \(c_{\text{dec}}\), not that the minimizer of \(c_{\text{dec}}\) is generally the “correct” SAE.

4. **There are nontrivial issues in the mathematical presentation, and some “theoretical” claims are presented more strongly than justified.**  
Theorem 1 in **Appendix A.5** is framed as “a proof that when SAE \(L0\) is less than the true \(L0\), MSE loss directly incentivizes the SAE to mix features together.” But what is actually shown is a special constructed case: two orthonormal features, a tied SAE, no biases, \(L0=1\), and a one-parameter latent family. This is a useful illustrative counterexample, but it is not a general theorem covering the settings used in the rest of the paper, especially not BatchTopK or JumpReLU with overcomplete dictionaries and untied weights. Even in the proof itself, the activation rule in Case 3 depends on which latent wins the Top-1 competition, but the analysis then says “assuming \(\mathbf{l}_1\) activates,” which leaves the exact range of \(\alpha\) and \(m_1,m_2\) where the derivation applies somewhat under-specified. So the theorem supports existence of the phenomenon, not the broad generality implied by the prose.

5. **The central notion of “true \(L0\)” is much cleaner in toy data than in LLMs, and the paper does not adequately resolve that conceptual mismatch.**  
In **Section 3**, “true \(L0\)” is well-defined because the data are generated from a known sparse linear feature model. In real LLM activations, however, there is no such canonical quantity. By **Section 4**, the paper moves from “true \(L0\)” to “elbow in \(c_{\mathrm{dec}}\)” and peak sparse probing performance, but these are surrogate operational definitions, not evidence that a single correct latent count exists. This matters a lot because the main message is phrased as if there is a unique correct \(L0\) that practitioners should search for. The discussion on **Page 9** actually hints at the opposite, namely that some latents may be effectively too sparse while others are too dense simultaneously. That is an interesting observation, but it undercuts the earlier simplified rhetoric. In short, the paper raises an important problem, but the main paper does not convincingly define what “correct \(L0\)” should mean outside toy settings.

6. **The empirical evaluation relies heavily on sparse probing as the validator, but this is only one operational notion of feature quality and may be entangled with the same correlation structure the paper worries about.**  
In **Figure 8** and **Figure 9**, the key practical claim is that the proposed metric aligns with peak k-sparse probing F1. That is useful evidence, but it is not enough to conclude that the recovered features are more monosemantic or more faithful. Sparse probing is a downstream utility metric, not a direct measure of disentanglement. A low-\(L0\) SAE that mixes correlated features could still help a supervised probe. The paper’s strongest criticism of reconstruction-based evaluation is precisely that performance metrics can be improved by feature hedging, yet then it leans heavily on another performance metric without much discussion of its own failure modes. I would have liked to see at least one additional evaluation axis in the main paper, for example a feature quality benchmark, causal intervention fidelity, or even systematic human/automatic interpretability measures.

7. **Important quantitative results are communicated mostly through figures, with no tables summarizing the main empirical findings, which makes the paper harder to audit and compare.**  
This is not just a presentation nit. For the LLM experiments, the reader is expected to visually inspect **Figure 8** and **Figure 9** to infer where probing peaks, where \(c_{\mathrm{dec}}\) bends, and how large the performance differences are. There is no concise results table listing, for example, best probing F1, corresponding \(L0\), metric minima, or confidence intervals across seeds. That absence weakens the paper scientifically because the practical takeaways hinge on relative differences and on whether the elbows and minima actually coincide within noise. A small table would have made it much easier to judge whether the gains are substantial or merely suggestive.

8. **The comparison between BatchTopK and JumpReLU is interesting but under-controlled in the main paper.**  
In **Section 4.1** and **Figure 9**, the paper compares the shapes of \(c_{\mathrm{dec}}\) and sparse probing curves for BatchTopK and JumpReLU, and suggests that JumpReLU’s per-latent thresholds let it “stick” near correct behavior. This is plausible, but in the main paper it remains mostly speculation. The training setups differ materially, and there is not enough ablation isolating whether the observed differences come from threshold parameterization, loss design, optimization details, or token budget. Since the paper uses these observations to motivate claims about why JumpReLU handles high \(L0\) better, the causal interpretation feels ahead of the evidence.

9. **Some exposition is sloppier than I would like for a paper making strong methodological claims.**  
There are small but noticeable issues, for example inconsistency between batch size 500 on **Page 3** and batch size 1024 in **Appendix A.2**, and some prose claims in the main paper rely on appendix theory or extra plots to become convincing. Also, the paper often uses loaded terms like “degenerate,” “correct,” and “monosemantic” without pinning down operational criteria in the LLM setting. This does not make the paper unreadable, but it does make the argument feel more confident than the evidence supports.

## Questions
1. In the LLM experiments, what exactly would falsify your practical claim that the “correct” \(L0\) is near the elbow in \(c_{\mathrm{dec}}\) rather than at its global minimum? Right now **Figure 8** and **Figure 9** suggest that the elbow heuristic is doing real work, but that is not encoded in the metric definition itself. A rebuttal that clearly formalizes the selection rule and reports its stability across seeds would increase my confidence.

2. Can you better delimit the scope of the theorem-level claims? In particular, do you intend Theorem 1 to be an existence proof, a stylized explanation, or evidence for a much more general statement about trained SAEs? I would be much more comfortable if the paper explicitly narrowed the claim and separated “toy-model proof of possibility” from “empirical evidence in realistic SAEs.”

3. Can you provide more quantitative support for the LLM results, ideally in a compact table? For example: per model/layer/architecture, report peak sparse-probing F1, the \(L0\) at that peak, the \(L0\) minimizing \(c_{\mathrm{dec}}\), and the \(L0\) at the low-\(L0\) elbow, all with variability across seeds. This would make it much easier to judge whether the proposed heuristic is genuinely robust or just loosely correlated.

4. How sensitive are the conclusions to width \(h\), dataset choice, and training budget? The current main-paper setup fixes \(h=32768\) and uses the Pile. If the “right” \(L0\) changes materially with width or corpus, that would temper the practical recommendation.

5. The paper argues that low \(L0\) corrupts nearly all latents in toy models. Do you have any direct evidence in LLM SAEs that individual high-\(L0\) or low-\(L0\) latents become less interpretable, beyond aggregate probing? Even a small latent-level analysis would help bridge the toy-to-LLM gap.

6. In **Equation (4)**, why is the absolute cosine the correct aggregation rather than, say, signed cosine, squared cosine, or a trimmed statistic? Since anti-correlated components and a few highly redundant latents may affect the mean differently, a rebuttal clarifying this design choice would be helpful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work studies interpretability methods on existing language models and does not introduce a new dataset release, human-subjects study, or obviously harmful deployment pipeline in the main paper.

## Soundness Rating
2: fair. The paper presents a credible and interesting phenomenon, especially in toy models, but some central claims are stronger than the support provided in the main paper, and the practical validation is too limited to fully justify the conclusions.

## Presentation Rating
3: good. The paper is readable and the figures are helpful, especially Figures 1 to 5 and 8 to 9, but some terminology is over-assertive, some quantitative reporting is missing, and a few details are inconsistent or left to the appendix.

## Contribution Rating
2: fair. The paper raises an important issue and offers a useful cautionary perspective on \(L0\) selection, but the evidence for the stronger practical claims and the proposed metric is not yet broad or decisive enough for me to view it as a clear ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a real idea here, and parts of the toy-model analysis are quite compelling. However, the paper over-claims relative to the evidence, leans too heavily on a narrow set of LLM experiments and one downstream validator, and does not yet make a sufficiently rigorous case that its proposed metric reliably identifies a “correct” \(L0\) in realistic settings. With sharper scoping, stronger quantitative reporting, and broader empirical validation, this could become a strong paper, but I do not think the current version clears the bar comfortably.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I followed the technical argument and inspected the equations and figures carefully, but some of the mechanistic-interpretability-specific empirical choices could still benefit from author clarification.