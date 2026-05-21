---
job_id: 9923e417-65f3-42c0-ad1e-ff06ad920725
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: OuMNJoKJBQ.pdf
paper: Alignment-Weighted DPO: A Principled Reasoning Approach to Improve Safety Alignment
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on LLM safety alignment, preference optimization, causal analysis of internal representations, and reasoning-aware post-training.

## Minimum Quality
Pass ✅. The submission contains the expected research components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion. While there are important technical and presentation issues, the paper is complete enough for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, instructions targeting automated reviewers, or suspicious manipulative text in the provided paper content and figures.

# Expected Review Outcome:
## Summary
This paper argues that current safety alignment in LLMs is often superficial, in the sense that refusal behavior can remain intact even when reasoning-related internal components are disrupted. To support this claim, the authors first present a probing-and-pruning analysis of attention heads, then introduce a chain-of-thought safety fine-tuning dataset, and finally propose Alignment-Weighted DPO (AW-DPO), which decomposes outputs into reasoning and final-response segments and applies different preference weights to the two parts. Experiments on several model families and safety benchmarks suggest improved jailbreak robustness with relatively limited utility degradation compared with several baselines.

## Strengths
1. The paper tackles an important and timely problem. The central question, whether aligned refusal behavior is actually grounded in reasoning or is mostly a shallow pattern, is meaningful for the ICLR community and for LLM safety more broadly.

2. The paper is more interesting than a standard “yet another DPO variant” submission because it combines three pieces into a coherent story: a mechanistic diagnosis, a reasoning-oriented SFT stage, and a weighted preference optimization stage. Even if each component is not individually airtight, the overall framing is thoughtful.

3. The preliminary analysis is provocative and useful. **Figure 1** is one of the stronger parts of the paper: the contrast between nearly saturated alignment probing accuracy and much weaker reasoning probing accuracy in early layers does visually support the authors’ hypothesis that these two capabilities are represented quite differently. The second row of **Figure 1**, after pruning, also makes the claimed dissociation easy to see at a glance.

4. The empirical results are fairly broad. **Table 1** covers multiple model families and sizes, and the pattern that CoT safety SFT is consistently stronger than plain safety SFT on ASR is reasonably convincing. Likewise, AW-DPO often improves over DPO in average safety, especially for Llama-3.2-3B, Llama-3.1-8B, and Mistral-7B-v0.3.

5. The paper does attempt to quantify utility rather than optimizing only for refusal. That matters. In **Table 1**, the utility numbers are not always best-in-class, but the paper at least acknowledges the trade-off instead of hiding it.

6. The decomposition of failures into “reasoning wrong, answer safe” versus “reasoning right, answer unsafe” is a useful lens. **Figure 3(a)**, although simple, helps motivate why a response-level preference objective might miss some errors that are localized to only one segment of the output.

7. The comparison against standard DPO is not purely anecdotal. **Figure 4(b)-(c)** and **Table 12** both support the claim that segment-aware weighting can improve safety and slightly improve or preserve utility relative to vanilla DPO on at least one representative setup.

## Weaknesses
1. The causal claim in Section 3 is overstated relative to the evidence. The paper repeatedly says it “demonstrates” or “confirms” that current alignment is superficial because pruning reasoning-critical heads degrades reasoning but not safety. However, the operational definition of “reasoning-critical” is based on linear probes trained on a very narrow task formulation, namely correct versus incorrect answer discrimination on CommonsenseQA-style constructions, not on reasoning in alignment settings. This matters because the conclusion the paper wants is stronger than what is actually tested. At most, the experiments show that heads predictive for one specific reasoning probe are not necessary for the specific safety distinction being probed. That is not the same as proving that safety refusal is independent of deep reasoning in general.

2. The probing setup for “reasoning” is weaker than the paper suggests. On **Page 15**, Appendix A explains that the reasoning task is formed by concatenating a question with either the correct or incorrect answer, then probing whether the hidden state distinguishes those two cases. This is much closer to answer plausibility or consistency classification than to multi-step reasoning. The paper’s rhetoric leans heavily on “deep reasoning,” but the probe target is just binary discrimination over answer correctness after the answer has already been inserted into the input. That mismatch weakens the main mechanistic story.

3. The pruning procedure is not well justified as a causal intervention. On **Page 4**, the paper selects the top 10% of heads with highest reasoning probe accuracy in the first 11 layers and zeros out their Q/K/V weights. There are at least three problems. First, “high probe accuracy” does not necessarily imply causal necessity rather than correlation. Second, restricting pruning to the first 11 layers is motivated by the observed heatmaps, but the paper does not test whether the conclusion is robust to different cutoffs or different percentages. Third, zeroing Q/K/V is a very blunt perturbation that may induce side effects unrelated to reasoning. Without stronger controls, the “causal relationship” language is too strong.

4. The mathematical formulation of AW-DPO is inconsistent and, in its present form, not well specified enough to reproduce. This is the most serious technical issue for me.
   - In **Equation (1)** on **Page 3**, the DPO scale parameter is denoted by $\beta$.
   - In **Equation (2)** on **Page 6**, the implicit reward is rewritten using $\gamma$, not $\beta$, and $\gamma$ is also used elsewhere as the pair-selection threshold in **Figure 2** and the surrounding text on **Pages 5-6**. This is inconsistent notation for two different concepts.
   - In **Equation (3)**, the paper says $w_{s_t} \in \{0,1\}$ is a mask corresponding to token type, but the earlier definition on **Page 6** defines $w_{\text{reasoning}}$ and $w_{\text{respond}}$ as continuous scalar weights derived from harmfulness differences. A binary mask and a continuous alignment weight are not the same object.
   - The text after **Equation (3)** says “And then calculate the DPO using Equation (2) given the rewards for the reasoning and respond, respectively,” but it is not actually clear whether the authors run two separate DPO objectives over two masked token subsets, or whether they compute one token-weighted log-ratio and then split it post hoc. Those are not equivalent.
   - **Equation (4)** then multiplies $\mathcal{L}_{\text{DPO}}^{\text{rs}}$ and $\mathcal{L}_{\text{DPO}}^{\text{rp}}$ again by $w_{\text{reasoning}}$ and $w_{\text{respond}}$. If the weights are already embedded inside $\phi_{\text{AW}}$ via **Equation (3)**, this risks double-weighting; if they are not, then **Equation (3)** is misleading. The current formulation needs a careful rewrite.

5. The sign convention for the alignment weights appears backwards, or at minimum is unclear. On **Page 6**, the paper defines
\[
d_{\text{reasoning}} = h_{rs}^{\text{chosen}} - h_{rs}^{\text{rejected}}, \quad
d_{\text{respond}} = h_{rp}^{\text{chosen}} - h_{rp}^{\text{rejected}}.
\]
If “chosen” means preferred/safer and harmfulness scores are larger for more harmful outputs, then these differences should often be negative. That would make
\[
w_{\text{reasoning}}=\frac{d_{\text{reasoning}}}{d_{\text{respond}}+d_{\text{reasoning}}}
\]
potentially negative or ill-defined. The appendix on **Page 19** makes this worse, because it says the threshold ensures samples with harmfulness below 0.5 are selected as “rejected,” while those above 0.5 are “accepted,” which sounds reversed relative to ordinary DPO semantics. This is not a cosmetic typo, it affects the correctness of the optimization objective.

6. The preference-pair construction is underexplained. **Figure 2** gives a nice high-level pipeline, but the actual algorithmic details are thin. The paper says it samples $k$ responses, judges reasoning, response, and full harmfulness, and keeps pairs whose full harmfulness difference exceeds $\gamma$. But several practical details are missing from the main paper: how ties are handled, whether multiple pairs per prompt are used, how often pairwise labels disagree between full-answer and segment-level judgments, whether benign prompts are included in DPO training, and how the chosen/rejected ordering is enforced when segment-level scores conflict. Since AW-DPO hinges entirely on these labels and weights, this omission matters.

7. The experimental evidence for the claimed “reasoning-specific” advantage is not fully persuasive. The paper’s own motivation is that standard DPO misses the roughly 15% of failure cases in **Figure 3(a)** that involve disagreement between reasoning and response. If that is the core claim, then I expected a focused evaluation showing that AW-DPO improves specifically on those cases. Instead, the evidence is mostly aggregate ASR in **Table 1**, **Table 2**, and the radar/bar plots in **Figure 4**. Those tables do show gains, but they do not directly validate the mechanism. It would be much more convincing to report performance broken down by the two failure modes that supposedly motivate the method.

8. Some of the headline comparisons are a bit too favorable in framing and not fully apples-to-apples. For example, in **Table 2**, the authors compare against methods built on both base and instruct models and then report “Ours (Base)” and “Ours (Instruct)” to cover both regimes. That is better than collapsing them, but it still leaves substantial uncertainty about differences in training budget, data access, and initialization. The text on **Page 7** also argues efficiency against STAIR-DPO-3, but the paper does not provide actual compute numbers, wall-clock time, or token budgets, so “more efficient” remains qualitative.

9. The utility evaluation is too narrow for the breadth of the paper’s claims. MMLU is useful, but it is mostly a knowledge-and-reasoning benchmark and not a robust measure of instruction-following helpfulness. This matters because the paper repeatedly claims that utility is preserved. In **Table 1**, there are cases where utility drops materially, for example DPO on Mistral drops from 55.39% after CoT Safety SFT to 41.45%, and AW-DPO recovers some but not all of that. On Llama-3.2-3B, AW-DPO is also below DPO in utility. So the stronger claim should be softened to “often preserves competitive utility” rather than “maintains utility.”

10. Presentation quality needs work. There are quite a few notation inconsistencies and wording issues that made careful reading harder than it should have been. A few examples:
   - **Page 5** says “(i)m correct reasoning accompanied by an unsafe final answer,” which looks like a typo in a key motivation paragraph.
   - The paper alternates between “respond,” “response,” and “rp” in the formulas.
   - The references contain multiple mismatches and formatting problems, including year inconsistencies and author/title swaps.
   - The ethics statement on **Page 10** says the paper “has no ethical issues and will not introduce any additional security risks,” which is too glib for a paper centered on jailbreaks, harmful prompts, and release of safety-related training data.

11. The ethics discussion is underdeveloped. The paper uses and releases safety-critical data, studies jailbreak behavior, and relies on an LLM judge to score harmfulness. Yet the ethics statement on **Page 10** essentially dismisses concerns outright. A paper on safety should show more self-awareness than that. Even if the work is beneficial overall, there are real issues around misuse of harmful prompt collections, failure modes of automated judges, and potential over-refusal or bias amplification that deserve a serious treatment.

## Questions
1. Please clarify the exact semantics of “chosen” and “rejected” in AW-DPO. In **Page 6** and Appendix H on **Page 19**, the sign convention and threshold description appear inconsistent. Is the chosen sample the safer one or the more harmful one? Please provide the exact pseudocode for pair construction.

2. Please rewrite **Equations (2)-(4)** with consistent notation. In particular, are $w_{\text{reasoning}}$ and $w_{\text{respond}}$ continuous scalars in $[0,1]$, or are they binary masks, or both? If both, please use different symbols and show the exact final loss used in implementation.

3. Can you provide a stronger control for the pruning experiment in Section 3? For example, how do results change if you prune:
   - random heads matched in number and layer location,
   - top safety-probe heads instead of top reasoning-probe heads,
   - different fractions such as 5%, 20%,
   - different layer ranges beyond the first 11 layers?
   This would substantially increase confidence in the causal claim.

4. The “reasoning” probe appears to classify correctness after appending an answer, not to measure multi-step reasoning. Can you justify why this is an appropriate proxy for the deeper reasoning claims in the introduction? If you have results on a more direct reasoning probe, that would help.

5. The core mechanism claim would be much stronger if you evaluated AW-DPO specifically on the failure types in **Figure 3(a)**. Can you report whether AW-DPO reduces:
   - correct-reasoning / unsafe-response cases,
   - incorrect-reasoning / safe-response cases,
   compared with standard DPO?

6. Utility is assessed only with MMLU in the main paper. Do you have evidence on broader instruction-following, truthfulness, or general chat helpfulness? A single utility benchmark feels too thin given the repeated “without significantly compromising utility” claim.

7. Please clarify the role of the scaling factor $\alpha$ in relation to **Table 4** and the main equations. The equations use $w_{\text{reasoning}}$ and $w_{\text{respond}}$, but the insertion point of $\alpha$ into the objective is not shown mathematically in the main text.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper studies jailbreak robustness using harmful prompts and adversarial attack categories, and it also states that the CoT dataset will be released (**Page 10**, reproducibility statement). Even though the intent is defensive, the work still involves operationalizing harmful prompt distributions and could lower the barrier for misuse if released carelessly. I am not alleging misconduct, but the ethics statement is too dismissive for this setting. At minimum, the authors should discuss release safeguards, filtering, intended-use restrictions, and risks of over-reliance on LLM-as-a-judge for harmfulness scoring.

## Soundness Rating
3: good. The empirical story is fairly substantial and many results are directionally convincing, but the central causal interpretation and the AW-DPO mathematical specification both need tightening.

## Presentation Rating
2: fair. The paper is readable at a high level, but notation, objective definition, and several implementation details are inconsistent enough to materially hinder confidence.

## Contribution Rating
3: good. The paper asks an important question and combines mechanistic diagnosis with a targeted training method in a way that is useful to the community, even though parts of the execution feel under-specified.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a meaningful idea and a reasonably broad empirical evaluation, and I do think the proposed direction is worth discussion at ICLR. That said, the current version overclaims on the causal diagnosis and has real technical clarity problems in the AW-DPO formulation. I lean weakly positive because the empirical gains are nontrivial and the problem framing is valuable, but this is not a comfortable accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the technical details carefully, though some ambiguities in the paper make absolute certainty impossible.