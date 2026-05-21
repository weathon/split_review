---
job_id: 0f30a524-993e-4d27-a85b-7f0104b1e39b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IU4rqTlpRb.pdf
paper: Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on machine unlearning, robustness of LLMs, safety/privacy, and empirical analysis of learning dynamics in representation-rich language models.

## Minimum Quality
Pass ✅. The submission contains the expected scientific structure, including abstract, introduction, related work, formal setup, experimental analysis, results, and conclusion, and it provides substantial empirical evidence for its core claims, even though some claims are broader than what the current evidence fully supports.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies benign relearning in LLM unlearning and argues that syntactic similarity, more than topical relevance, is the main driver of forgotten content reappearing after benign fine-tuning. The authors first re-examine prior benchmark conclusions about topicality, then present controlled TOFU experiments and representation/gradient analyses to support the syntax hypothesis, and finally propose syntactic diversification of forget queries as a mitigation that improves robustness to relearning and utility retention.

## Strengths
The paper asks an important question. Benign relearning has become a serious stress test for approximate unlearning, and the paper does more than just report another failure case, it tries to identify a mechanism. That is a worthwhile contribution for the ICLR audience.

A strong aspect is the re-evaluation of the topical-relevance narrative from BLUR. The discussion around **Figure 3** on **Page 4** is one of the paper’s better moments: the authors identify two concrete confounds, unequal effective training budget across relearn sets and non-monotonic recovery over steps, and then propose a fairer protocol based on standardized steps and peak recovery. This is a useful benchmarking correction, not just a new result on one dataset.

The controlled TOFU construction in **Section 5.2, Pages 5-6** is conceptually clean. The contrast between \(D_{\text{relearn}}^{\text{topic}}\) and \(D_{\text{relearn}}^{\text{syntactic}}\) makes the central hypothesis testable. In particular, **Figure 4** directly supports the main empirical claim: across GA, NPO, and SCRUB, syntactically similar relearn sets consistently trigger much stronger recovery than topically relevant ones. Even without exact numbers on every cell, the qualitative separation is hard to miss, especially in the GA and SCRUB panels.

I also appreciated that the authors did not stop at correlation and attempted mechanistic analysis. **Figure 5** on **Page 7** is useful because it ties three quantities together, representation similarity, gradient similarity, and relearn success rate, across methods. Whether or not one fully buys the causal interpretation, this figure does provide a coherent story that syntactically similar relearn data induces updates closer to those produced by target data.

The proposed mitigation is simple and practically understandable. Syntactic diversification is not algorithmically fancy, but simple fixes are valuable when they address a concrete failure mode. **Figure 8** and **Figure 9** present an intuitively consistent picture: diversification reduces relearning and makes suppression of template and keyword tokens more balanced. I also find **Table 2** on **Page 9** encouraging, because the method is not presented as robustness-at-all-costs; the utility numbers improve substantially on Real Authors and the Retain set, suggesting the mitigation is not merely more aggressive forgetting.

The paper is generally easy to follow. **Figure 1** does a good job of communicating the paper’s central claim with a simple counterexample, and the progression from “benchmark reassessment” to “mechanism” to “mitigation” is coherent.

## Weaknesses
My main concern is that the paper’s headline claim, that syntax is the primary driver of benign relearning, is supported mostly in highly templated settings, and the paper sometimes phrases the conclusion more broadly than the evidence warrants. The strongest evidence comes from TOFU name-style QA in **Section 5.2** and from similarly stylized benchmark constructions in **Sections 4 and Appendix C/D**. In those settings, the query and answer formats are indeed rigid, so syntax has an obvious opportunity to dominate. But this leaves open whether the same conclusion holds for less templated forget sets, free-form generations, multi-turn dialogue, or tasks where structural regularity is weaker. The paper gestures toward generality, especially in the abstract and **Pages 1-2**, but the empirical base is narrower than that wording suggests. This matters because the paper’s scientific contribution is not just “we found one benchmark artifact”; it is making a broader claim about the mechanism of unlearning failure.

Relatedly, the operationalization of “syntactic similarity” is weaker than the rhetoric around it. In **Section 5.1, Page 5**, the paper defines
\[
\mathrm{Sim}(s_1,s_2)=1-\frac{d_{\mathrm{Lev}}(s_1,s_2)}{\max(|s_1|,|s_2|)},
\]
using normalized character-level Levenshtein distance. That is a surface-form similarity measure, not really a syntax measure in the linguistic sense. It conflates lexical overlap, phrase order, punctuation, and formatting artifacts. The paper later notes alternative measures in the appendix, but in the main paper the central argument still relies on a proxy that is much closer to templatic edit distance than to syntax per se. This distinction matters because the title and claims repeatedly say “syntax” rather than “surface-form similarity” or “template similarity.” If the true phenomenon is template matching, that is still interesting, but it is a narrower and more precise claim than what is currently asserted.

The analyses in **Figure 5** are suggestive but underspecified enough that I do not think they establish mechanism as strongly as the text claims. In **Section 6, Page 7**, representation similarity is computed from “average last-token hidden states” and gradient similarity from “average loss gradients induced by each dataset.” There are several missing details that affect interpretation: which layer is used, how gradients are flattened and normalized, whether per-example gradients are averaged before or after normalization, and whether the reported bars are stable across random seeds. Without those details, the statement that syntactic overlap “steers both the hidden representations and optimization directions” is plausible but not yet nailed down. The figure itself is visually neat, but because **Figure 5** lacks uncertainty intervals and sample variability, it reads more like supporting evidence than decisive proof.

The token-level loss-ratio argument in **Section 6, Page 7** is also less rigorous than it should be. The paper defines
\[
\text{Loss Ratio} = \frac{\mathcal{L}_{\mathrm{template}}}{\mathcal{L}_{\mathrm{keyword}}},
\]
but does not adequately specify how template tokens and keyword tokens are segmented in the general case, whether losses are normalized by token counts, how overlapping or partially informative tokens are treated, or whether this decomposition is robust across answer styles. Because **Figure 6** and later **Figure 9** are used to support the key mechanistic claim that unlearning suppresses templates more than keywords, these details matter. If template spans are longer or easier/harder tokens, the ratio can move for reasons other than the claimed selective forgetting mechanism. This is fixable with better definition and reporting, but in the current form the analysis is under-specified.

The evidence around benchmark reassessment is directionally convincing, but some of the quantitative support is thinner than I would like. **Table 1** on **Page 6** shows syntactic similarity values for \(D_{\mathrm{hi}}, D_{\mathrm{mid}}, D_{\mathrm{low}}\), yet several of the gaps are numerically small, especially in WHP and RWKU. For example, in WHP the values 0.1894, 0.1767, and 0.1818 are very close. That may indeed help explain why recovery levels are similar in **Figure 2**, but the paper treats this almost as a clean explanatory resolution rather than a modest correlation. Given such small differences, the absence of statistical testing or confidence intervals becomes more noticeable. The same issue appears in **Figure 2** itself, where the bars are close enough that one wants error bars, multiple seeds, or at least a clearer statement about variance before buying a strong “topicality mostly disappears” conclusion.

The mitigation section is promising, but the evaluation of syntactic diversification is still somewhat narrow. The main robustness result in **Figure 8** is shown only under GA, and **Table 2** reports utility gains without clearly indicating whether these numbers hold consistently across GA, NPO, and SCRUB. Since the earlier sections emphasize method-agnostic vulnerability across three unlearning methods, it is natural to expect the mitigation to be tested just as broadly in the main paper. As written, there is a mild asymmetry: the vulnerability analysis is broad, but the remedy is demonstrated more selectively. This matters because the paper’s practical takeaway is not just diagnosis, it is “here is an effective strategy.”

I also think the comparison set is incomplete from a robustness perspective. The paper compares against standard unlearning methods, but not against stronger relearning-robust unlearning baselines specifically designed with robustness in mind. That weakens the contribution claim around the mitigation, because it is hard to tell whether syntactic diversification is competitive with the best current alternatives or merely improves over relatively standard GA/NPO/SCRUB setups. For a paper that frames itself as a reconsideration of unlearning robustness, stronger positioning against methods aimed at robust forgetting would materially increase confidence in significance.

There is a mild metric mismatch issue in parts of the paper. In **Section 4**, recovery on BLUR-style benchmarks is measured with ROUGE-L against the base model’s answers. In **Section 5**, TOFU uses a keyword-based Relearn Success Rate. In **Appendix C**, the paper uses an LLM judge. I understand why different datasets may require different metrics, but the main text occasionally moves from one setting to another as if the conclusions were directly comparable. The appendix correlation results help, but since those are not central in the main narrative, the paper would benefit from a more explicit discussion in the main paper of what each metric captures and where it may fail. This matters because “recovery” can mean lexical overlap, semantic answer quality, or exact target-name regeneration, and those are not identical notions.

Finally, some of the exposition oversells causal language. Statements such as “syntax is the hidden driver” or “what enables recovery is not merely shared entities or subjects, but instead shared surface forms” are stronger than what the current evidence strictly proves. The experiments support that syntactic or templatic similarity is a strong and often stronger predictor in the tested setups. That is already a good result. The current writing sometimes jumps from “strong evidence” to “primary cause established,” and that leap is larger than the data fully warrants.

## Questions
1. The core claim hinges on “syntax” rather than topicality. Could the authors clarify, in the main-paper framing, whether they really mean linguistic syntax, or rather surface-form/template similarity? A sharper definition would help, especially given that **Section 5.1** uses character-level Levenshtein distance.

2. For the representation and gradient analyses in **Section 6 / Figure 5**, please specify exactly: which hidden layer is used, whether hidden states are averaged over examples before cosine similarity, how gradients are aggregated, and whether similarities are computed on full parameters or a subset. If these measurements were repeated across seeds, reporting variance would substantially increase my confidence.

3. For the loss-ratio analysis on **Page 7**, how are template and keyword tokens identified in practice? Are \(\mathcal{L}_{\mathrm{template}}\) and \(\mathcal{L}_{\mathrm{keyword}}\) normalized by the number of tokens in each subset? If not, the ratio may be confounded by token count and token difficulty. A precise definition here could materially improve confidence in the mechanistic claim.

4. The mitigation in **Section 7** looks promising, but in the main paper it is evaluated most prominently under GA. Do the gains in **Figure 8**, **Figure 9**, and **Table 2** persist comparably under NPO and SCRUB? A concise summary in the rebuttal could change my opinion upward.

5. **Table 1** shows relatively small differences in similarity for some benchmarks, especially WHP. Did the authors test whether these differences are stable across alternative similarity measures or resamplings in the main analysis? This would strengthen the reinterpretation of BLUR.

6. Since the paper argues that topical overlap is not the primary factor, a stronger stress test would combine both high topical and high syntactic overlap, or use adversarially optimized relearn sets. Do the authors have evidence that syntactic diversification remains effective under such stronger relearning conditions?

7. For **Table 2**, please clarify whether the reported utility scores are single-run numbers or averages across multiple runs. If they are averaged, please report variance. The gains on the Retain set are large enough that I would like to know their stability.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies machine unlearning robustness and does not introduce a new harmful capability. Although it uses benchmarks involving harmful or sensitive knowledge, the work is focused on reducing leakage and improving forgetting robustness.

## Soundness Rating
3: good. The main empirical claims are supported reasonably well, especially the controlled TOFU experiments and the benchmark reassessment, but some mechanistic claims are stronger than the provided evidence, and several key analyses are under-specified.

## Presentation Rating
3: good. The paper is generally clear and well organized, with useful figures such as **Figure 1**, **Figure 3**, **Figure 4**, and **Figure 8**. The main presentation issue is not readability but overstatement and insufficient precision in a few technical definitions.

## Contribution Rating
3: good. The paper offers a useful reframing of benign relearning and a simple mitigation with practical appeal. I do not view the evidence as broad enough to fully justify the strongest version of the “syntax is the primary driver” claim, but the contribution is still meaningful and relevant to the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important robustness problem, presents a thoughtful benchmark correction, and offers a plausible and practically useful mitigation. I am positive overall, but only narrowly, because the current evidence is strongest in highly templated settings, the “syntax” construct is not defined as sharply as it should be, and the mechanistic analyses need more rigor to support the strongest causal claims.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the unlearning/robustness literature, though some conclusions depend on how broadly one interprets the paper’s notion of “syntax,” and I cannot fully verify every implementation detail from the main paper alone.