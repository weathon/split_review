Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

---

## Summary

This paper investigates why unlearned LLMs recover forgotten content after fine-tuning on benign data ("benign relearning"). The authors challenge the prevailing view that topical relevance drives this phenomenon, and instead demonstrate through controlled experiments (TOFU, WHP) and a re-analysis of the BLUR benchmark that **syntactic similarity** — structural overlap between relearn data and target data — is the primary driver. They provide mechanistic evidence via representation and gradient similarity analyses, and propose **syntactic diversification**, a simple mitigation that paraphrases forget-set queries to break structural rigidity. Diversification suppresses relearning, accelerates forgetting, and improves the utility-forget trade-off.

## Strengths

- **Clean causal isolation of syntactic similarity on TOFU** (Section 5.3, Figure 4): The paper constructs topically relevant and syntactically similar relearn sets and shows that the syntactically similar set consistently triggers stronger recovery across GA, NPO, and SCRUB. The experimental design is thoughtful and the results are unambiguous — the syntactically similar set dominates even when topical overlap is absent.

- **Credible re-analysis of BLUR revealing confounds** (Section 4, Figure 2, Figure 3): The paper identifies dataset-size imbalance and fixed-step evaluation as confounds in the influential BLUR benchmark, and re-evaluates under standardized step budgets with best-step reporting. The finding that topical-relevance ordering largely disappears is substantively important and well-supported in the presented figures.

- **Mechanistic analysis that explains *why* syntactic similarity matters** (Section 6, Figure 5): The representation and gradient similarity analysis shows that syntactically similar data sits closer to the target set in both hidden-state and loss-gradient space, providing a coherent mechanism linking structural overlap to recovery. The template-vs-keyword loss ratio analysis (Figure 6) further reveals that unlearning disproportionately suppresses template patterns, leaving keywords vulnerable.

- **Syntactic diversification as a well-motivated, effective remedy** (Section 7, Figure 8, Table 2): The proposed method is a natural consequence of the diagnosis: if structural rigidity enables relearning, then breaking that rigidity should suppress it. Results show diversification substantially reduces relearning success rates, balances template/keyword suppression (Figure 9), and improves model utility (Table 2). The causal template-injection experiment (Appendix F) provides clean evidence that diversification addresses the root mechanism.

- **Multi-metric and multi-model validation** (Appendix H, Appendix I, Appendix B.3): The paper validates findings across alternative leakage metrics (cosine similarity, LLM-as-judge, Pearson >0.99 agreement), alternative syntactic similarity metrics (template-mining, parse-tree), full-parameter and LoRA-based unlearning, and additional model families (Phi, Llama-3-8B). This breadth strengthens confidence in the core claims.

## Weaknesses

### Fatal

None.

### Major

- **Generalizability beyond templated settings is not fully established.** The strongest causal evidence comes from TOFU (Section 5.3), a benchmark deliberately constructed with rigid QA templates, and the WHP experiment (Appendix C) uses a hand-selected subset of syntactically homogeneous questions. The BLUR re-analysis (Section 4, Table 1) provides correlational evidence across WMDP, WHP, and RWKU, but the paper does not perform a controlled causal manipulation of syntactic similarity on a naturally diverse benchmark. The paper acknowledges this scope limitation but the abstract and introduction claim syntactic similarity is "the primary driver" broadly. The claim would be strengthened by demonstrating the syntactic-similarity effect with controlled manipulations on at least one non-templated benchmark (e.g., constructing syntactically similar vs. topically relevant subsets of WMDP and showing the same pattern).

- **Syntactic diversification lacks comparison against simpler baselines to isolate the specific benefit.** The paper does not compare against straightforward data augmentation alternatives (e.g., synonym substitution, random word reordering, or adding noise) that could also break structural homogeneity. Without such baselines, it is unclear whether the benefit stems specifically from "breaking syntactic rigidity" or from general data augmentation during unlearning. The causal analysis in Appendix F partially addresses this by showing diversification balances template-keyword suppression, but a head-to-head comparison would strengthen the claim that syntactic diversification, rather than any augmentation, is the key ingredient.

### Minor

- **Best-step evaluation protocol is not accompanied by variance estimates.** Section 4 evaluates recovery by "reporting the maximum value observed" within a fixed step budget. While this addresses BLUR's original confound, it can inflate apparent recovery for conditions with higher variance, and the paper does not report standard deviation or discuss how much the ordering changes under alternative protocols (e.g., averaging over the last N steps). The step budgets themselves (9 for WMDP, 30 for WHP, 4 for RWKU — Appendix A.1) are stated but not motivated; different datasets may require different numbers of steps to converge, which could reintroduce imbalance.

- **The paper claims that BLUR's D_low (Lorem Ipsum) is comparable in syntactic similarity to D_hi in WHP (Table 1: 0.1818 vs 0.1894), explaining similar recovery.** However, comparing trivia QA pairs to Lorem Ipsum filler text via character-level Levenshtein distance is an unusual use of this metric. The paper would benefit from a brief discussion of what these similarity scores mean substantively in the WHP/Lorem Ipsum context, and why Levenshtein distance is a meaningful construct for this particular comparison.

- **Diversification evaluation is limited to TOFU.** The proposed method is validated only on the same benchmark where the problem was diagnosed (Section 7.2), with no test on WHP, WMDP, or RWKU. Since the paper advocates diversification as a general remedy, demonstrating it on at least one additional benchmark would substantially strengthen the practical contribution.

### Trivial

- The template-token annotation procedure for the loss-ratio analysis (Section 6) is described at a high level but the specific rules for distinguishing template vs. keyword tokens are not enumerated, which would aid reproducibility.

## Nice-to-Haves

- **A formal correlation or regression analysis** between syntactic similarity scores and relearning strength across the BLUR relevance tiers would make the Table 1 argument more rigorous than the current qualitative alignment.
- **Qualitative examples of model outputs** during relearning (for both syntactic and topical conditions) would make the phenomenon more concrete and illustrative.
- **Extending diversification to non-QA forget sets** (e.g., prose passages) would demonstrate broader applicability beyond the TOFU-style QA format.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "The BLUR re-analysis... relies on a post-hoc character-level Levenshtein similarity measure whose ability to capture meaningful syntactic structure is questionable (e.g., comparing trivia questions to Lorem Ipsum paragraphs)."** — Partially addressed: the paper uses Levenshtein as the primary metric but validates with template-mining and parse-tree metrics in Appendix I. However, I retained the concern about the WHP/Lorem-Ipsum comparison as a minor weakness because comparing trivia QA to filler text via character edits is indeed an unusual application and deserves discussion.

- **Harsh critic: "The WHP experiment... selects a set of syntactically homogeneous target questions, which yields a similar confound."** — The paper itself explicitly notes this selection ("we select a subset of 10 trivia questions from it that are syntactically homogeneous," Appendix C line 2089-2090). The paper is transparent about this limitation; I moved this concern from a standalone weakness to being folded into the major weakness about generalizability.

- **Harsh critic: "The safety-training comparison... hyperparameter choices for DPO and IDK are not shown to be equivalently tuned."** — This is a minor point about a supplementary experiment (Appendix E), and the paper's conclusion ("safety training methods are substantially more vulnerable") is modest and well-supported by Figure 16. The tuning concern does not affect the paper's core claims.

- **Strength Finder: "Thorough evaluation across methods, models, and metrics... demonstrating the robustness and generality of the results."** — Kept but qualified. The evaluation breadth across methods (GA, NPO, SCRUB, IDK, DPO) and metrics is genuine, but the generality claim is tempered by the major weakness about templated benchmarks.

- **Strength Finder: Generic strengths without specific citations.** — None of the strength finder's points were fully generic; all referenced specific sections/figures. Kept all that were substantiated.

## Novel Insights

The paper's most valuable insight is the identification of a structural mechanism underlying unlearning fragility: unlearning algorithms disproportionately suppress syntactic templates rather than content keywords, because the rigid query-answer syntax creates a synergy that directs optimization toward surface patterns. This explains both why syntactically similar data triggers recovery (it restores the suppressed templates, allowing keywords to re-emerge) and why diversification works (it breaks the template synergy, forcing the model to directly suppress keywords). This template-dominant suppression hypothesis, supported by the loss-ratio analysis and the causal template-injection experiment, provides a more mechanistic account of benign relearning than prior topical-relevance explanations and suggests a general principle for designing robust unlearning strategies.

## Suggestions

- **Add a controlled syntactic-vs-topical experiment on a non-templated benchmark** (e.g., WMDP, constructing syntactically similar and topically relevant relearn subsets). This would be the single most impactful addition and would directly address the generalizability concern.
- **Add at least one simple augmentation baseline** (e.g., synonym substitution or word reordering) to the diversification experiments to isolate the effect of breaking structural rigidity from general data augmentation.
- **Report standard deviation or confidence intervals** for the BLUR re-analysis best-step results and justify the step-budget choices with a brief rationale (e.g., number of steps needed to observe convergence).
- **Briefly discuss the construct validity of Levenshtein distance** for the WHP Lorem Ipsum comparison, and note that Appendix I validates with alternative metrics.

## Score and Decision

### Anchor Comparison

| Path | Avg Human Score | Comparison to Paper Under Review |
|------|-----------------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/7cEMkTu7Lf.md` | 4.00 (Reject) | "Unlearning Isn't Deletion" — also studies reversibility of unlearning via representation analysis. Criticized for lacking actionable insights and novelty. The current paper goes substantially further by identifying a *specific mechanism* (syntactic similarity), providing causal experiments, and proposing a practical mitigation. Clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/lk3j87oquF.md` | 4.00 (Reject) | LUSB benchmark — formalizes unlearning attacks/defenses. High-variance scores (0,8,6,2). The current paper is more focused, with cleaner experiments and a clearer narrative. Stronger contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/EyXBv291ST.md` | 3.50 (Reject) | "Effective Unlearning Relies on Right Data Retention Strategy" — explores retain-set selection for preserving utility. Narrower contribution without mechanistic analysis. Current paper is stronger in both insight and evaluation depth. |
| `/home/wg25r/review_agent/human_reviews_2026/nxMR2NGFik.md` | 3.50 (Reject) | "LLM Unlearning Under the Microscope" — taxonomy and re-evaluation of methods. Survey-like contribution. Current paper offers a novel causal finding and mitigation; stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/1MCQzboBrR.md` | 5.00 (Accept Poster) | "Model Collapse Is Not a Bug but a Feature" — novel unlearning method (PMC) accepted as poster. Similar level of novelty but current paper has more comprehensive analysis (causal + correlational + mechanistic + mitigation). Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/Qi1rZa4zzl.md` | 5.50 (Accept Poster) | "Safety Mirage" — identifies spurious correlations and uses unlearning as defense. Similar structure: diagnose problem → propose unlearning-based solution. Current paper's syntactic-diversification method is comparably novel. |
| `/home/wg25r/review_agent/human_reviews_2026/iKqQGEOeej.md` | 5.50 (Reject) | "Memorize to Forget" — novel MOX method but criticized for limited novelty vs. Task Vector paradigm. The current paper has a fresher contribution (syntactic similarity as driver) backed by more thorough causal analysis. |
| `/home/wg25r/review_agent/human_reviews_2026/SCCbnM6H3z.md` | 5.00 (Reject) | "Bridging the Gap Between Preference Alignment and Machine Unlearning" — bi-level optimization framework. Current paper has stronger empirical validation and a more actionable takeaway. |
| `/home/wg25r/review_agent/human_reviews_2026/K4pQPqibC3.md` | 4.00 (Reject) | "Ripple Effect of Unlearning" — jailbreak defense via unlearning. Interesting observation but narrower scope. Current paper's contribution is more fundamental to unlearning robustness. |

The paper under review makes a genuine, well-supported contribution: it identifies syntactic similarity as a key driver of benign relearning, provides converging evidence from causal experiments, correlational analysis, and mechanistic probes, and proposes a simple, effective mitigation. The main weakness is limited demonstration of generalizability beyond templated settings, which prevents the paper from being a clear accept. However, the analysis is rigorous within its scope, the insight is novel, and the mitigation is practical. Compared to anchor papers accepted as posters in the 5.0-5.5 range, this paper is at least equally strong. I recommend acceptance as a poster, with the expectation that the authors address the generalizability concern in the revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>