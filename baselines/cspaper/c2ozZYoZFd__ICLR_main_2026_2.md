---
job_id: 4ed477e5-a41d-4b8e-8916-afdbccb5d52a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: c2ozZYoZFd.pdf
paper: A Min-P Blueprint for More Rigorous Science in Empirical Machine Learning Research
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is about empirical methodology, evaluation rigor, statistical testing, and reproducibility in machine learning, which fits ICLR’s general ML scope, especially datasets/benchmarks, probabilistic/statistical methodology, and responsible research practice in ML.

## Minimum Quality
Pass ✅. The submission is complete as a case-study / methodology-critique paper, with an abstract, introduction, multiple empirical analysis sections, quantitative and qualitative results, and a discussion/limitations section. While I have significant concerns about contribution and positioning, these are review-level concerns rather than desk-reject-level omissions or fatal structural defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper presents a detailed re-analysis of the evidence used in Nguyen et al. (2024) to support min-p sampling, with the stated broader goal of offering a blueprint for more rigorous empirical ML research. The authors revisit four evidence streams from the original work, human evaluations, NLP benchmark sweeps, LLM-as-a-judge evaluations, and community-adoption claims, and argue that under more careful analysis the original claims of min-p superiority are not supported.

## Strengths
The paper is unusually concrete for a methodology-critique piece. Rather than making vague complaints about “rigor,” it walks through specific failure modes, omitted human-eval data, inappropriate pooling across settings, lack of multiple-comparison correction, unequal hyperparameter search volume, indirect LLM-as-a-judge comparisons, and unverifiable adoption claims. That specificity is valuable.

The empirical re-analysis is broader than a quick spot-check. In Section 3, the GSM8K sweep spans many models, both base and instruct variants, multiple samplers, 31 temperatures, and several sampler hyperparameters. Even if one disagrees with some framing choices, this is a substantial amount of effort, and it is hard to dismiss the paper as superficial.

Some figures are genuinely effective at making the paper’s central point legible. In particular, **Figure 4** and **Figure 5** are the clearest part of the submission. Figure 4 directly visualizes the dependence of “best observed performance” on the number of hyperparameter settings explored, which is precisely the confound the paper wants the reader to focus on. Figure 5 then reframes the same issue as the gap between min-p and the strongest competing sampler under matched hyperparameter-budget conditions. This pair of figures does more argumentative work than several pages of prose and helps the paper move beyond a one-off complaint into a more general caution about search-space unfairness.

The human-evaluation section is also reasonably grounded in the actual reported statistics rather than rhetorical criticism. **Table 1** is useful because it forces the discussion into explicit hypotheses, test directions, and multiplicity. Whether one fully agrees with every inferential choice or not, presenting the 12 pairwise tests and showing the effect of Bonferroni correction is much more informative than hand-waving about significance.

The paper also does a good job showing how visual summaries can expose over-claimed conclusions. **Figure 1** is a sensible first-pass sanity check on the “consistently outperforms” claim, and **Figure 6** makes the hyperparameter-count asymmetry in the LLM-as-a-judge analysis visually obvious.

Finally, the tone is mostly serious and evidence-driven. For a paper that is explicitly critical of another high-visibility paper, it avoids descending into pure rhetoric more often than not.

## Weaknesses
1. **The paper promises a “blueprint” but mostly delivers a single-paper critique.**  
The title, abstract, and introduction repeatedly position the work as a blueprint for more rigorous empirical ML research, but the generalizable content is quite thin in the main paper. The actual “General Lessons for Reviewers and Researchers” in **Section 6, Page 9** amount to roughly a short checklist: control hyperparameter volume, correct for multiple comparisons, release data, scrutinize qualitative claims, ensure methodological clarity, and avoid selective reporting. These are reasonable recommendations, but they are not developed into a framework, protocol, formal checklist, decision procedure, or reusable methodology at the level the title suggests. This matters because the paper’s contribution is then much narrower than advertised. As written, the main scientific object is a case study about one prior paper, not a broadly useful blueprint.

2. **The central contribution is heavily dependent on contesting one prior paper, which limits generality and makes the ICLR fit weaker than the paper claims.**  
A sharp re-analysis can absolutely be valuable, but here most of the manuscript is tightly coupled to the particulars of Nguyen et al. (2024): specific temperatures, specific prompt formats, specific public comments, specific camera-ready revisions, and even reported GitHub-search behavior. That makes the paper read closer to a detailed reproducibility challenge / refutation report than to a research contribution that generalizes across empirical ML practice. The authors try to lift it into a broader statement about “rigorous science,” but the broader takeaway is not adequately substantiated beyond this one example. If the case study is the main contribution, the paper should be more upfront about that; if the blueprint is the main contribution, then the blueprint needs much more substance.

3. **Several claims rely on public or private interactions that the reader cannot independently audit from the main paper.**  
Examples include “We publicly confirmed with the authors” in **Section 2.1, Page 2**, “the authors publicly told us to focus on the high diversity setting” in **Section 2.2, Page 3**, “After we showed these results to the authors, they informed us that their code default used the incorrect benchmark prompt formatting” in **Section 3.1, Page 7**, and the Telegram-based reporting claim in **Section 4.3, Page 8**. These may all be true, but they leave too much of the argument resting on facts external to the paper’s self-contained evidence. For a paper centered on rigor and transparency, this is an awkward asymmetry. A stronger version would separate claims verifiable from released data/code in the main paper from claims that depend on outside communications, and would downgrade the latter from headline evidence to ancillary context.

4. **The human-evaluation analysis is more careful than the original claim it critiques, but it still contains important inferential choices that are asserted rather than fully justified.**  
The most important example is the decision in **Section 2.2, Page 3** to focus on the “high” diversity setting only. The paper gives three reasons, but this restriction is consequential because it narrows the evidentiary basis while simultaneously criticizing the original work for selective aggregation. That is a bit rich. If the correct claim is that “min-p does not consistently outperform across all settings,” then the cleanest demonstration would report the full design and then separately explain why some settings may be poorly chosen, not foreground a filtered subset as the main analysis. More generally, the paper moves between several inferential lenses, overlapping confidence intervals in **Figure 1**, 12 one-sided paired \(t\)-tests in **Table 1**, Bonferroni correction, and an Intersection-Union Test. Each of these speaks to a slightly different question. The paper would be stronger if it formalized the exact family of hypotheses first, e.g.,  
\[
H_{0,i}: \mu_{\text{min-p},i} \le \mu_{\text{baseline},i}, \quad i=1,\dots,12,
\]
and then clearly distinguished claims about average superiority, any-setting superiority, and all-settings superiority. Right now the statistical critique is directionally persuasive, but not as cleanly framed as it should be for a paper making rigor its flagship contribution.

5. **The statistical methodology is not always aligned with the data structure, and this deserves more care.**  
In **Table 1**, the paper reports one-sided paired \(t\)-tests with \(df=52\). But the main text does not clearly specify the unit of pairing, whether each participant scored all systems under matched prompts, how repeated measures across temperatures/diversity settings were handled, or whether the assumptions of the paired \(t\)-test are plausible for the score distributions used. If scores are ordinal or bounded Likert-style ratings, a nonparametric paired analysis or a mixed-effects model might be more appropriate, especially given repeated-measure structure. Likewise, the discussion of overlapping \(95\%\) CIs in **Figure 1** is only heuristic and should not be used as evidentiary shorthand. Since the paper is explicitly criticizing statistical misuse, it should hold itself to a high standard here and either justify the \(t\)-test assumptions carefully or report robustness checks with alternatives.

6. **The “fair comparison by hyperparameter volume” idea is interesting, but the chosen operationalization is not fully defended and may itself encode debatable assumptions.**  
The Best-of-\(N\) protocol in **Section 3.1, Pages 5-7** treats fairness as matching the number of hyperparameter settings explored per sampler. That is one reasonable notion, but not the only one. Another notion would equalize total compute, number of model evaluations, wall-clock budget, or prior knowledge available to tune each method. The paper argues strongly that matching hyperparameter-count is the right correction, yet does not really justify why “number of discrete hyperparameter settings” is the relevant conserved quantity across samplers with qualitatively different search spaces. This matters because the headline claim, supported by **Figure 4** and **Figure 5**, depends on that fairness definition. I do think the analysis is informative, but the paper oversells one operationalization of fairness as if it were canonical.

7. **The NLP benchmark extension is too narrow relative to the strength of the conclusions.**  
The original work is critiqued across multiple evidence streams, but the new large-scale extension in Section 3 is effectively only on **GSM8K CoT**. The paper explicitly says this on **Page 6**, noting compute constraints and that GPQA was not rerun. Yet the discussion on **Page 9** generalizes quite broadly to “samplers perform approximately equally if given equal hyperparameter tuning.” That is too broad given the actual extension scope. Even inside the paper, there is an admission on **Page 7** that under standard formatting min-p appears higher for 2 of 12 language models. That does not rescue the original min-p claims, but it does undercut the stronger meta-claim that the methods are simply all approximately equal under fair tuning.

8. **Some key experimental details in Section 3 are underspecified enough to make interpretation harder than it should be.**  
For example, in the Best-of-\(N\) procedure, the manuscript says it subsamples an equal number of hyperparameters ranging from \(N=1\) to \(N=100\), repeated 150 times. But the total number of available configurations per method depends on temperature times sampler-specific hyperparameters, and “basic” has only temperature. It is not fully clear from the main paper whether the subsampling space treats temperature as one of the hyperparameters, whether \(N\) counts full configurations \((\tau, p)\) or only non-temperature sampler knobs, and how methods with fewer unique configurations than 100 are handled. These details are important because **Figure 4** and **Figure 5** are central evidence, and their interpretation depends directly on the sampling scheme.

9. **The LLM-as-a-judge section is suggestive, but comparatively weaker than the earlier sections because it depends on incomplete reconstruction of another paper’s methodology.**  
The critique in **Section 4.1** that the original methodology is under-specified is fair. However, this section of the present paper then partly inherits that limitation. **Figure 6** is visually useful, especially the left panel showing hyperparameter-count asymmetries, but the right-panel interpretation is weaker because the paper cannot fully reconstruct the selection/tuning process from the original work. This section therefore lands more as “there are serious reasons for doubt” than as a definitive refutation. The paper should calibrate its language accordingly.

10. **The presentation is readable but not polished to the standard expected for a paper advocating rigor.**  
There are several signs of haste, including grammatical issues in the introduction and Section 2, inconsistent capitalization of terms like “LLM-As-A-Judge,” and occasional overstatement. More importantly, the structure is front-loaded with critique and underdevelops synthesis. The manuscript would benefit from a clearer separation between: (i) reproducible findings from released artifacts, (ii) interpretive judgments, and (iii) general lessons. Right now these are interleaved, which weakens the argumentative discipline.

11. **The literature positioning around the proposed broader contribution is underdeveloped.**  
The paper cites many examples of failures and reproducibility discussions, but it does not adequately position itself relative to prior work on evaluation methodology, benchmark auditing, or reproducibility frameworks beyond using them as motivation. If the intended contribution is a reusable blueprint for empirical rigor, then the paper should compare that blueprint more directly against existing recommendations in reproducibility and evaluation literature, instead of mostly citing those works as evidence that there is a crisis.

12. **There is little positive scientific output beyond debunking.**  
This is the biggest practical issue for me. After reading the paper, I understand why the authors doubt the original min-p claims, but I do not come away with a new general method, benchmark, theorem, protocol, or tool that the broader ICLR community can readily adopt. The paper does contain a potentially useful idea in hyperparameter-volume-controlled comparison, but it is not developed enough to stand on its own as a methodological contribution. So the paper is strongest as critique, weaker as research contribution.

## Questions
1. The main framing promises a “blueprint.” What, concretely, is the reusable artifact here? Could the authors state a step-by-step protocol, checklist, or formal evaluation procedure that another ML paper could apply without depending on the min-p case study? A more operational blueprint would increase my assessment of contribution.

2. In **Section 2.2**, can the authors provide a more formal justification for the inferential target? Are you testing average superiority, superiority in each condition, or the conjunction that min-p is better in all conditions? Please write the hypotheses explicitly, and explain why the chosen tests are the correct ones for the paper’s targeted claim.

3. For **Table 1**, what exactly is the paired unit, and how are repeated measurements across prompts/settings handled? If the data are repeated-measures and bounded/ordinal, did you try a mixed-effects analysis or a nonparametric paired test as a robustness check? Showing the result is robust to test choice would materially increase confidence.

4. In the Best-of-\(N\) analysis of **Section 3.1**, what exactly is being counted as one “hyperparameter” or one sampled configuration? Is \(N\) a count of full configurations \((\tau, \text{sampler parameter})\), and how do you handle methods with fewer total unique configurations than the largest \(N\) shown? This should be made explicit in the main paper.

5. Why is equalizing the *number* of hyperparameter settings the right fairness criterion, as opposed to equalized compute budget, equalized tuning effort, or equalized prior knowledge? I agree the original comparison may be unfair, but the paper should defend why its corrective notion of fairness is preferable.

6. The paper notes on **Page 7** that under standard formatting min-p is higher for 2 of 12 models. Can the authors characterize what is different about those models/settings? Even a short analysis of when min-p helps would make the paper more scientifically useful than a blanket “no advantage” conclusion.

7. For the claims in **Sections 2, 4, and 5** that rely on public communications or repository evidence, can the authors more clearly separate what is directly reproducible from released data/code versus what depends on external interactions? Tightening this boundary would strengthen the paper’s credibility.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The paper contains substantial empirical re-analysis and many of its critiques are plausible and often persuasive, but several statistical and methodological choices are themselves under-justified, and some claims depend on evidence not fully self-contained in the paper.

## Presentation Rating
2: fair. The paper is readable and some figures are effective, especially Figures 4, 5, and 6, but the framing overshoots the actual general contribution, the exposition of the statistical setup needs more precision, and the manuscript is less polished than it should be for a paper centered on rigor.

## Contribution Rating
1: poor. As a case study and critique, the work is interesting; as a general ICLR contribution, it falls short because the promised “blueprint” is not developed into a substantial reusable methodology beyond a short list of sensible best practices.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My view is that this is a careful and often useful audit of one influential empirical claim, and I appreciate the concrete figure- and table-backed analyses. However, the paper over-claims its generality, the blueprint contribution is underdeveloped, and some of the strongest points rely on choices or evidence that are not as self-contained or methodologically airtight as a rigor paper should be. I see value in the case study, but in its current form it does not quite clear the bar for an ICLR main-track research contribution.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. I carefully checked the main argumentative and statistical structure, including the figure/table evidence, but some claims depend on external artifacts or communications that cannot be fully verified from the main paper alone.