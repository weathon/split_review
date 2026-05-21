---
job_id: ac16ee56-7190-4bb9-8afb-3e2294e1f6d0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VjGU55hEwV.pdf
paper: RLIE: Rule Generation with Logistic Regression, Iterative Refinement, and Evaluation for Large Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a neuro-symbolic / hybrid ML framework that combines LLM-based rule generation with probabilistic aggregation for text classification.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, method, experiments, results, discussion, and conclusion; although there are notable methodological and clarity issues, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, concealed reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes RLIE, a four-stage framework for learning natural-language rules with LLMs and combining them through a regularized logistic regression model. The pipeline includes initial rule generation, probabilistic weighting/selection via elastic-net logistic regression, iterative refinement using hard examples, and a final comparison between direct linear inference and several ways of feeding the learned rules back into an LLM. Experiments on six HypoBench-style text classification tasks suggest that the linear combiner usually outperforms LLM-based rule-application strategies.

## Strengths
The paper tackles a meaningful problem. The main practical question, how to turn LLM-generated natural-language rules into a reusable and reasonably calibrated prediction system rather than just a prompt artifact, is interesting and relevant to ICLR’s neuro-symbolic and interpretable ML community.

The framework is easy to understand at a high level and combines components that are individually sensible. In particular, the separation between local semantic judgment by the LLM and global aggregation by a transparent probabilistic model is a reasonable design choice. This division is also conveyed effectively in **Figure 1** on Page 4, which makes the intended pipeline and the distinction between generation, weighting, refinement, and downstream evaluation easy to follow.

I also appreciated that the paper does not stop at “rules help the LLM,” but explicitly evaluates multiple inference strategies. **Table 2** is useful here: it shows a fairly consistent pattern that the simplest strategy, **(E1) Linear-only**, beats feeding rules, weights, or even the linear model’s prediction back into the LLM. Whether or not one agrees with all of the authors’ interpretation, this negative result is informative and more interesting than a one-sided success story.

The empirical results in **Table 1** do show that RLIE with the same backbone as the strongest prompting baselines, namely the **DeepSeek-V3** row, is competitive and often better across the six tasks. In particular, it improves over HypoGeniC on Reviews, Dreadit, Headline, Citations, and LLM Detect, while matching it on Retweets. That gives some evidence that the weighted multi-rule formulation is useful in practice, at least on the selected benchmark setup.

The case study in **Table 3** is also a nice touch. It gives the reader a concrete sense of how the rule bank evolves across refinement rounds and how some rules are effectively retained or downweighted. I would not overstate what this demonstrates scientifically, but it does help illustrate the intended mechanism.

## Weaknesses
I have several concerns, some about novelty/positioning and others about technical clarity and experimental support. Taken together, they make the paper promising but not yet convincing enough for ICLR in its current form.

1. **The core methodological contribution feels more like a reasonable system integration than a clearly differentiated new method.**  
   The paper combines four familiar ingredients: LLM-based rule generation, rule application by an LLM, logistic regression on rule activations, and hard-example-driven iterative refinement. Each ingredient is sensible, but the paper does not do enough to show why this combination constitutes a substantial methodological advance rather than an engineering assembly of known parts. The claim in Section 2.2, Page 3, that the work is “the first to explicitly combine LLMs with probabilistic methods to learn a set of weighted rules” is stronger than what the paper itself substantiates. Even setting aside external literature, the manuscript’s own related-work discussion is too brief to make that “first” claim credible. As written, the novelty case is under-argued.

2. **The empirical study does not isolate which parts of RLIE actually matter.**  
   The main ablation in Section 5.2 and **Table 2** studies inference strategies after rule learning, but it does not ablate the learning pipeline itself. The paper needs component-level evidence for at least:  
   - rule generation without iterative refinement,  
   - iterative refinement with random rather than hard examples,  
   - logistic regression without elastic net,  
   - coverage filtering on/off or varying \( \gamma \) beyond a single appendix table,  
   - pruning by individual validation accuracy versus pruning by learned weight magnitude or joint validation objective.  
   Right now, the reader learns that “linear-only is best among four final inference modes,” but not whether the claimed gains in **Table 1** actually come from the probabilistic weighting, the refinement loop, the coverage filter, or simply stronger initial rules from the LLM. This matters because the paper’s central scientific claim is about the value of the integrated framework, not just the final classifier form.

3. **The comparison protocol in Table 1 is not as clean as the paper’s claims suggest.**  
   **Table 1** mixes methods that use different backbones, including DeepSeek-V3 for most prompting baselines, Qwen variants for some RLIE rows, and a LoRA baseline on Qwen3-8B. The paper does include an RLIE+DeepSeek-V3 row, which helps, but the overall framing still makes cross-row interpretation awkward. For instance, the headline claim in Section 5.1 that RLIE shows “superior overall performance” is not fully justified when the table interleaves different backbones and excludes LoRA from the “generalizable methods” comparison via a note rather than a principled evaluation criterion. If the method claim is about RLIE rather than about backbone choice, then the cleanest comparison should keep the backbone fixed across all relevant baselines wherever possible, or at least separate “method effect” from “backbone effect” much more carefully.

4. **The dataset and split design raise external-validity concerns.**  
   Section 4.3, Page 6, uses only 200 training, 200 validation, and 300 test examples per task. That may be appropriate for hypothesis-generation style studies, but for a paper making broad claims about robust probabilistic rule learning, the evidence is thin. Small fixed splits can make results highly sensitive to prompt idiosyncrasies, label noise, and dataset curation choices. The manuscript reports averages over at least three runs, which is helpful, but there is still no study of scaling with more training examples, no cross-split robustness analysis, and no discussion of whether the conclusions hold outside this very small-data regime. This matters because the proposed pipeline is explicitly iterative and uses learned rule weights; whether that remains stable beyond 200 labeled examples is left unanswered.

5. **The mathematical exposition contains multiple notation and specification problems, some of them in the core method.**  
   A few examples:  
   - In Section 2.1 on Page 2, the sentence defining rule satisfaction says \( r_j(x)\in\mathbb{R}^{n\times n}\{0,1\} \), which is malformed and inconsistent with the binary-valued feature interpretation on Page 3.  
   - In Section 3.1, Page 4, the local-judgment equation writes  
     \[
     z_{i,j}^{(1)} = \operatorname{LLM}(x_i, h_j^{(i)}) \in \{-1,0,+1\},
     \]
     but the superscript on the rule should presumably be \( (1) \), not \( (i) \). This is likely a typo, but it appears in a central equation.  
   - In Section 3.2, the rule set is written as  
     \[
     \mathcal{H}^{(t)}=\{h_1^{(t)},\dots,h_{m^{(t)}}^{{(t)}}\},
     \]
     which is minor but sloppy.  
   - The hard-example score in Section 3.3 is defined as \( d_i=\|\hat p_i^{(t)}-y_i\| \). Since both are scalars, this is just absolute error, but the notation is needlessly vague. More importantly, the paper does not justify why top-\(k\) absolute error is the right acquisition criterion for rule refinement, as opposed to uncertainty, margin, or systematic coverage failure.  
   These are not just cosmetic issues. When the method is essentially a pipeline with several data-dependent filtering and update steps, unclear notation makes it harder to judge what is actually optimized and what is only heuristic.

6. **The semantics of the ternary rule feature map are under-specified, especially for pairwise tasks.**  
   RLIE maps each rule application to \( z_{i,j}\in\{-1,0,+1\} \), where \(+1\) means positive, \(-1\) negative, and \(0\) abstain. This is straightforward for binary tasks with labels like spam/non-spam, but several tasks in the paper are pairwise comparison tasks such as Headline and Retweets. In those tasks, “positive” and “negative” correspond to “first item wins” vs “second item wins,” but the paper never formalizes this mapping carefully in Section 3.1 or Section 4.1. This matters because the sign of \( z_{i,j} \) is central to the logistic regression feature construction:
   \[
   p^{(t)}(x_i;\theta^{(t)})=\sigma\big((\Phi^{(t)}(x_i))^\top\beta^{(t)}+b^{(t)}\big).
   \]
   Without a clearer task-independent definition, it is hard to know whether the same rule template is being used consistently across all datasets, or whether task-specific label conventions are quietly doing a lot of work.

7. **Several training/validation choices are heuristic and insufficiently justified.**  
   Section 3.2 states that \((\lambda,\alpha)\) are selected via stratified K-fold cross-validation on \( \mathcal S_{\mathrm{val}} \), after which the model is refit on \( \mathcal S_{\mathrm{tr}} \). Then Section 3.3 uses \( \mathcal S_{\mathrm{val}} \) again for early stopping and for pruning rules by individual validation accuracy when capacity is exceeded. This repeated reuse of the same validation set for hyperparameter tuning, model checkpointing, and rule pruning is not necessarily invalid, but it does increase the risk of overfitting to a very small validation split of only 200 examples. The paper should be much more explicit about the exact order of these decisions and whether all validation-dependent choices are nested properly inside each refinement round.

8. **The pruning rule is not aligned with the stated probabilistic-combination objective.**  
   In Section 3.3, if the temporary rule set exceeds capacity \(H\), the paper prunes by ranking rules according to their **individual accuracy on the validation set**. This is a surprisingly crude criterion given that the entire premise of the paper is that rules should be selected jointly because of combination effects. A rule with weak individual accuracy can still be valuable in a complementary ensemble if it covers a distinct subregion or interacts constructively through the linear combiner. Pruning by individual accuracy may therefore directly contradict the paper’s own motivation from the introduction, namely that rule interactions matter. This is an important methodological inconsistency, not a minor implementation detail.

9. **The claim about robustness and calibration is stronger than the reported evidence.**  
   The abstract and discussion repeatedly describe the linear combiner as “robust” and “calibratable,” and Section 5.2 interprets **Table 2** as showing superior stability. But the actual empirical reporting is almost entirely accuracy and macro-F1. There is no explicit calibration metric, no reliability diagram, no Brier score, no ECE, and no uncertainty analysis. If calibration is a headline motivation for moving from simple rule aggregation to logistic regression, then the paper needs to measure it directly. As written, the calibration discussion is largely aspirational.

10. **Some presentation issues make the paper read less carefully polished than it should be for a top venue.**  
    There are repeated grammatical problems and inconsistencies, for example “a evaluation” on Page 2, “regrading” instead of “regarding,” “Generated rules are the evaluated,” “will surprising degrade,” and several citation-format artifacts with stray asterisks in Sections 1 and 2. More importantly, some prompts in the appendix figures contain obvious formatting noise, such as the malformed placeholder notation in **Figure 4** and the wording “linear regression model” in **Figures 7 and 8**, while the method in the main text is logistic regression. These details may look secondary, but for a paper whose contribution is a procedural framework heavily dependent on prompts, sloppy prompt specification reduces confidence in the exact implementation.

11. **Figure usage is mixed: Figure 1 helps, but the appendix figures expose an implementation gap.**  
    As noted above, **Figure 1** on Page 4 does a good job explaining the pipeline. However, **Figures 7 and 8** on Pages 16 and 17 describe the downstream LLM prompts as if they rely on a “linear regression model,” not logistic regression, and they explain the learned bias as leaning toward a positive or negative label without clarifying how ternary rule outputs map into the presented natural-language weights. Since these prompts are exactly what instantiate strategies (E3) and (E4), the mismatch between the formal model in Section 3.2 and the text of the prompts is not trivial. It leaves open whether the evaluated inference strategies accurately reflect the learned probabilistic model or only a loosely translated version of it.

12. **The broader positioning against rule-learning and neuro-symbolic baselines remains narrow.**  
    The paper compares mainly against zero-shot/few-shot prompting, IO Refinement, HypoGeniC, and a LoRA baseline. Those are relevant, but for a paper centered on probabilistic rule combination, the baseline set feels underpowered. At minimum, I would have expected stronger classical or hybrid comparisons, such as simpler deterministic aggregation over the same learned rules, or a direct comparison to alternative post-hoc combiners beyond logistic regression. This omission makes it harder to tell whether the reported gains are due to the probabilistic formulation specifically or merely due to having multiple rules and an iterative generation loop.

## Questions
1. **Can the authors provide a true component ablation of RLIE?**  
   In particular, I would like to see results for: initial rule generation only, no iterative refinement; iterative refinement with random examples instead of hard examples; no coverage filter; no elastic-net regularization; and pruning by learned global contribution rather than individual validation accuracy. This would materially change my confidence in the paper, because it would reveal which parts of the framework are actually responsible for the gains in **Table 1**.

2. **How exactly are ternary judgments mapped for pairwise tasks such as Headline and Retweets?**  
   Please formalize what \( z_{i,j}=+1 \) and \( z_{i,j}=-1 \) mean when the label is “first vs second” rather than “class 1 vs class 0,” and clarify whether the same prompt structure and feature construction are used across all six datasets.

3. **Can the authors clarify the full model-selection protocol around \( \mathcal S_{\mathrm{val}} \)?**  
   The paper appears to use the validation set for cross-validation-based hyperparameter selection, pruning when \( |\mathcal H_{\mathrm{tmp}}^{(t+1)}|>H \), checkpoint selection, and early stopping. A precise step-by-step description would help determine whether this procedure is statistically clean or overly tuned to a small validation set.

4. **Why is rule pruning based on individual validation accuracy, given the paper’s emphasis on combination effects?**  
   If the authors have already tested alternatives, such as pruning by absolute weight \( |\beta_j| \), by change in validation log-loss after removal, or by group sparsity in the linear model, that evidence would strengthen the method significantly.

5. **Can the authors substantiate the calibration claims with direct metrics?**  
   Since the paper motivates logistic regression partly on calibration grounds, it would be helpful to report ECE, Brier score, or reliability plots for RLIE versus simpler rule aggregators and versus LLM-based inference strategies.

6. **How much of the gain comes from the final linear combiner versus the quality of the learned rules themselves?**  
   A useful analysis would be to fix the learned rules and compare logistic regression, majority vote, OR/AND-style aggregation, and perhaps a shallow tree or GAM combiner on the same feature map \( \Phi(x) \). That would directly test the paper’s central narrative.

7. **Can the authors comment on computational cost?**  
   The framework appears to require LLM judgments for many sample-rule pairs at each refinement stage. Reporting the number of LLM calls per dataset and per iteration would help readers judge practicality and reproducibility.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The concerns are moderate rather than disqualifying. The paper includes tasks such as **mental stress detection (Dreddit)**, discussed in Section 4.1 and Appendix A.3, where learned natural-language rules could encode sensitive or stigmatizing linguistic stereotypes. Because RLIE explicitly generates interpretable rules and weights, it could make such biases easier to inspect, but also easier to operationalize. Similar concerns apply to persuasion / engagement prediction tasks where rule-based systems may be used to optimize manipulative content strategies. The ethics statement on Page 9 acknowledges some of this, which is good, but the paper does not provide any concrete bias auditing or harm analysis.

## Soundness Rating
**2: fair.** The central empirical pattern is plausible and partially supported, but the methodology has important unresolved issues, especially missing component ablations, under-specified validation usage, and a mismatch between some claims, especially calibration/robustness, and the reported evidence.

## Presentation Rating
**2: fair.** The paper is readable at a high level and **Figure 1** is helpful, but the manuscript contains enough notation errors, prompt inconsistencies, and writing problems that they materially hinder confidence in the details.

## Contribution Rating
**2: fair.** The problem is relevant and the framework is a useful synthesis, but the paper does not yet make a sufficiently strong case that the contribution rises beyond a competent combination of known ideas, nor does it isolate the source of gains well enough.

## Overall Rating
**4: Marginally below the acceptance threshold. But would not mind if paper is accepted.** The paper has a worthwhile problem setting and one genuinely useful empirical takeaway, namely that an explicit linear combiner over LLM-generated rules can outperform feeding those same rules back into an LLM. However, the current version is not tight enough methodologically for ICLR: the novelty case is underdeveloped, the experimental design does not isolate the core components, and several technical/presentation issues reduce confidence in the conclusions.

## Reviewer Confidence
**4: confident.** I am confident in this assessment. The paper is in an area I know well, and I checked the main equations, tables, figures, and experimental logic carefully, though some implementation details remain unclear from the manuscript.