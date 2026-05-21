---
job_id: 7485a18d-e450-4cf1-a218-c9091f8d6425
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: omg9K6lI93.pdf
paper: Observing Data Contamination Through Translation: Evidence from Arabic Corpora
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about LLM evaluation, benchmark contamination, multilingual benchmarking, and trustworthy evaluation pipelines, which fits ICLR topics on language, datasets/benchmarks, and societal aspects of ML evaluation.

## Minimum Quality
Pass ✅. The paper contains the core ingredients of a research submission, including abstract, introduction, literature review, methodology, experimental results, discussion, and conclusion. While there are serious concerns about methodology, novelty, and exposition, these issues do not rise to the level of an immediate desk rejection based solely on the main paper text.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other signs of prompt injection or concealed manipulation in the provided paper content and figures.

# Expected Review Outcome:
## Summary
This paper studies whether translating benchmark data into Arabic can hide data contamination effects rather than remove them. The authors fine-tune four open-weight instruction models on English data plus varying proportions of Arabic versions of MMLU, XQuAD, and MLQA, evaluate on the original English benchmarks, and use a modified TS-Guessing probe to test for memorization. Based on these experiments, the paper argues that translation can obscure standard contamination signals while still yielding performance gains, and it proposes a translation-aware contamination detection framework as a future direction.

## Strengths
The paper addresses an important and timely problem. Data contamination has become a central issue in LLM evaluation, and the multilingual angle is genuinely worth studying because most contamination analysis remains heavily English-centric. The core question, namely whether translation can act as a barrier or merely a disguise for contamination, is relevant to benchmark construction and to multilingual evaluation practice.

I appreciated that the paper does not just report raw downstream metrics, but also attempts to use a contamination probe. The adaptation of TS-Guessing to the multiple-choice case via answer-choice reordering is intuitively sensible, and **Figure 1** is one of the clearer parts of the paper. It helps the reader understand the intended logic of the probe for both MMLU and extractive QA: in the top panel, recalling the pre-shuffle answer index is framed as evidence of memorized benchmark structure rather than reasoning, and in the bottom panel, exact masked-token recovery is framed as a possible leakage cue. Even though I have concerns about the validity of the probe as implemented, the figure itself does a good job of illustrating what the authors are trying to test.

The paper also includes a nontrivial empirical setup across multiple models and datasets. **Table 2** is useful because it makes visible that the contamination effects differ substantially by task and model family, rather than producing a uniform uplift. For instance, Mistral’s MMLU score rises strongly from 0.577 to 0.690, while its XQuAD performance degrades sharply from 0.302 to 0.114 at 100% contamination. That heterogeneity is interesting in itself and suggests the story is more complex than “more contamination always boosts evaluation.”

The paper is commendably explicit that the proposed Translation-Aware Contamination Detection framework is a blueprint rather than a fully implemented system. I prefer that level of honesty to overselling a partial implementation as a finished framework.

## Weaknesses
1. **The experimental setup conflates contamination with supervised training on the evaluation benchmark, which severely weakens the central scientific claim.**  
   The methodology in **Section 3.1, Page 5** defines
   \[
   \mathcal{D}^{d}_{\text{train}}(p)=\mathcal{D}^{d}_{\text{EN}} \cup \mathcal{D}^{d}_{\text{AR}}(p),
   \]
   where \(\mathcal{D}^{d}_{\text{EN}}\) is explicitly described as the English split, and for MMLU this is “English test items formatted as MCQ”; for XQuAD/MLQA it is “English QA.” This means the models are being fine-tuned directly on the benchmark content that is later used for evaluation in English. That is not merely contamination analysis in the wild, it is deliberate train-test leakage by construction. One can certainly run such controlled contamination experiments, but then the paper has to be extremely careful about what conclusions are justified. As written, the paper repeatedly speaks as if it has shown that “translation obscures traditional contamination signals” in a realistic sense, whereas the setup is much closer to synthetic contamination injection. The distinction matters because conclusions about real-world pretraining contamination, hidden multilingual leakage, and benchmark auditing are much stronger claims than what this setup directly supports.

2. **There is no clean causal isolation of the role of translation itself, as opposed to simply adding more task-specific fine-tuning data.**  
   The paper’s core claim is about Arabic translation masking contamination, but the training design does not isolate whether gains come from semantic exposure to benchmark items, ordinary multilingual transfer, increased training set size, or benchmark-specific supervision. A proper test would need at least one of the following controls: (i) same-size additional Arabic data from a different dataset, (ii) paraphrased English contamination versus Arabic translation, (iii) back-translation or machine-translated English controls, or (iv) matched random Arabic QA/MCQ data unrelated to the benchmark. Without such controls, the observed changes in **Table 2** cannot be attributed specifically to “translation concealing contamination.” They may reflect bilingual transfer, data augmentation effects, or even instability from mixing heterogeneous supervision.

3. **The empirical evidence is too unstable and internally inconsistent to support some of the paper’s stronger conclusions.**  
   The paper claims in **Section 4.2, Page 7-8** that models show “approximately equal performance on all evaluated benchmarks” across contamination levels, and that this near-flat trend supports masking by translation. But **Table 2** does not show near-flat behavior in any robust sense. Mistral’s XQuAD drops from 0.455 at 10% to 0.114 at 100%, which is dramatic, not flat. Gemma’s XQuAD rises from 0.364 to 0.606. LLaMA’s MMLU increases from 0.332 to 0.431. Qwen’s MLQA jumps from 0.162 to 0.409 at 10% and then collapses back near baseline. These are large, model-specific swings. The text tries to explain every pattern post hoc, but the broader narrative oscillates between “contamination boosts performance,” “translation masks contamination,” and “scores remain broadly stable.” Those claims are not mutually consistent, and the tables do not cleanly support the summary interpretation.

4. **The contamination probe for QA is under-validated and may not measure memorization in the way claimed.**  
   In **Section 3.3, Page 6**, for XQuAD/MLQA the authors mask “a critical token in the question” and interpret exact recovery as possible leakage. But many question tokens are predictable from syntax, world knowledge, or the surrounding context, especially in templatic QA questions. Recovering “capital” in “What is the [MASK] of France?” is not evidence of contamination; it is ordinary language modeling plus background knowledge. The probe would need stronger controls, such as matched non-benchmark QA items, random masked tokens with varying predictability, or calibration against a clean model not exposed to the benchmark. As presented, the metric
   \[
   \mathrm{EM} = \frac{1}{N}\sum_i \mathbf{1}\{\hat y_i = y_i\}
   \]
   in **Section 3.4, Page 6** does not distinguish memorized benchmark recall from routine lexical completion. This substantially weakens the interpretation of **Table 3(b)**.

5. **The MMLU TS-Guessing metric is also insufficiently specified, and the semantics of the reported numbers are unclear.**  
   The paper defines the index-recall rate for MMLU as
   \[
   \mathrm{IdxRec} = \frac{1}{N}\sum_i \mathbb{1}\{\hat{\ell}_i = \ell_i^{\mathrm{pre-shuffle}}\},
   \]
   in **Section 3.4, Page 7**. However, several key details are missing. What exactly is \(\hat{\ell}_i\) when the model outputs answer text instead of a letter? How are malformed generations normalized? Is chance level 0.25 for four-option MCQ, and if so, why are some values in **Table 3(a)** interpreted as meaningful contamination while others below chance are not discussed? For example, LLaMA reaches 0.643 at 50%, which is striking, but Gemma falls from 0.350 at 10% to 0.005 at 100%, which is bizarre if contamination is increasing. Mistral is near zero throughout despite the strongest MMLU gains in **Table 2**. That mismatch should have triggered a much deeper analysis of whether the probe is actually measuring the intended phenomenon.

6. **The paper introduces a representation-space argument that is not supported by the main-paper experiments and is presented in a somewhat hand-wavy way.**  
   In **Section 4.3, Page 8**, the paper states that “The embedding figure shows that Arabic \(\rightarrow\) English translations remain close to their English originals in representation space,” with
   \[
   s = \cos(\mathbf{e}^{ar \rightarrow en}, \mathbf{e}^{en}).
   \]
   But the main paper never specifies which encoder produced these embeddings, which layer was used, whether cosine similarity is computed on sentence embeddings or token aggregates, whether the translations are human or machine generated in this analysis, or how the bins in **Figure 4** were constructed. Since this representation-level claim is used to support the central argument that semantics survive translation and hence hide contamination, the lack of methodological detail matters. Also, **Figure 4** is visually suggestive, but it is not quantitatively informative enough on its own to support the conclusion. A flow diagram of similarity bins to subjects is not a substitute for reporting actual similarity distributions, subject-wise means, variance, or a comparison to unrelated Arabic-English pairs.

7. **The paper’s proposed framework, TACD, is not actually implemented or evaluated, so it should not be framed as a contribution on the same level as the empirical study.**  
   **Section 5, Pages 8-9** proposes cross-translation benchmarking, TS-Guessing across variants, and back-translation consistency. These are reasonable ideas, but they remain conceptual. There is no algorithm, no benchmark suite, no detection criterion, no complexity analysis, and no empirical validation. In effect, TACD is a short position section attached to an empirical paper. That is acceptable if clearly presented as future work, but the abstract and conclusion package it together with the empirical findings as if the paper had delivered both evidence and a framework. The paper would be stronger if it narrowed the scope and did one thing well.

8. **The literature review is broad but not especially sharp, and it misses some directly relevant framing around rephrasing/paraphrasing-style contamination and method inconsistency.**  
   The related work in **Section 2** spends many pages summarizing prior contamination categories and reports, but less effort is spent positioning the specific novelty of translation as a label-preserving transformation relative to paraphrasing/rephrasing contamination studies or broader critiques of contamination detectors. As a result, the paper feels under-positioned with respect to adjacent lines of work that would make its contribution more precise. The issue is not lack of citations in bulk, the bibliography is reasonably long, it is that the positioning remains diffuse and the unique scientific delta is harder to pin down.

9. **Several claims are stronger than the evidence provided.**  
   The abstract says the paper “demonstrates that translations can mask but not eliminate contamination, creating a dangerous blind spot in current evaluation practices.” That is a high-level conclusion about evaluation pipelines in general. But the paper studies four relatively small open models, three datasets, one target language, and a synthetic fine-tuning setup where the benchmark is deliberately inserted into training. This is enough for an interesting case study, not for broad claims about current evaluation practice writ large. The rhetoric gets ahead of the evidence in multiple places.

10. **Presentation and writing quality are uneven, and in places the exposition undermines credibility.**  
   There are many grammatical issues, awkward phrasings, and typographical problems throughout the paper, for example “terra bytes” instead of terabytes, “where able” instead of were able, repeated words, inconsistent capitalization of section titles, and some citation formatting problems such as “OpenAI OpenAI (2023)” on **Page 3**. More importantly, the paper often reads like a long survey-plus-opinion document before getting to a relatively modest experiment. The main contribution only crystallizes late, and key methodological details are either deferred or missing. This is fixable, but for a conference paper the current presentation is below the bar of clarity one would want for evaluating subtle contamination claims.

11. **The use of figures and tables is mixed; some are helpful, but others highlight missing rigor rather than strengthening the case.**  
   As noted above, **Figure 1** is helpful conceptually. By contrast, **Figure 4** is invoked as evidence for semantic preservation under translation, but it does not provide the quantitative granularity needed for that role. Likewise, **Table 3** is central because it should connect the probe to the contamination story, yet the mismatch between **Table 2** and **Table 3(a)** is never satisfactorily explained. A model like Mistral shows the largest MMLU gain in **Table 2**, but essentially zero IDR in **Table 3(a)**. That discrepancy could mean the probe is not capturing the right mechanism, or that the MMLU gains come from something other than index memorization. Either way, the paper should confront this directly instead of smoothing over it.

12. **Reproducibility from the main paper is still incomplete despite the appendix tables.**  
   The reproducibility statement points to Appendix A, but several crucial details remain absent from the main paper: how the Arabic translations were produced and quality-controlled, how subsets \(\mathcal{D}^{d}_{AR}(p)\) were sampled, whether the same seed/subset was reused across models, how answer normalization was handled in QA, what exact prompting templates were used for TS-Guessing, and how LoRA hyperparameters differ across model families. For a contamination paper, provenance and construction details are not minor bookkeeping; they are central to interpretation.

## Questions
1. The biggest issue I need clarified is the training setup in **Section 3.1**. Am I reading correctly that the English benchmark split used for evaluation is also part of \(\mathcal{D}^{d}_{\text{train}}(p)\)? If yes, please explicitly reframe the paper as a controlled contamination-injection study rather than an observational study of naturally occurring contamination. If no, please clarify exactly which English split is used for training versus evaluation for each dataset.

2. Can the authors provide a control experiment where the added Arabic data is matched in size but unrelated to the benchmark? This would help isolate whether the observed changes in **Table 2** are contamination effects rather than generic multilingual fine-tuning or data augmentation.

3. For the QA TS-Guessing setup in **Section 3.3**, how are “critical tokens” selected? Are they manually chosen, randomly chosen subject to POS/importance constraints, or algorithmically selected? A rebuttal should explain the masking strategy and ideally provide a baseline showing how often a non-contaminated model recovers these tokens on clean, non-benchmark QA data.

4. For the MMLU probe, please define how \(\hat{\ell}_i\) is extracted from model outputs. What happens if the model outputs answer text, multiple letters, or free-form rationale? Also, what is the chance baseline for IDR under your exact prompting and parsing protocol?

5. The discrepancy between **Table 2** and **Table 3(a)** needs direct explanation. In particular, how do the authors reconcile Mistral’s large MMLU improvement with near-zero IDR, and Gemma’s drop in IDR as contamination rises? If the intended contamination signal is not index recall, what exactly is the probe diagnosing?

6. The representation-space argument around **Figure 4** would be much more convincing with concrete numbers. Can the authors report mean and variance of cosine similarities, the encoder used to compute embeddings, and a control distribution for unrelated Arabic-English pairs or paraphrases?

7. Please clarify the provenance of the Arabic data. Were the Arabic versions human translated, machine translated, or taken from existing Arabic benchmark releases? If multiple sources were used, that could materially affect the interpretation of “translation-aware contamination.”

8. If the TACD framework is intended as a genuine contribution, can the authors make it more concrete in rebuttal, for example by specifying a decision rule, an evaluation protocol, or at least one small prototype experiment across multiple translated variants?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics flag from the main paper. The work studies benchmark contamination and evaluation validity rather than deploying models on sensitive populations. The broader topic touches fairness and trustworthiness, but I do not see a concrete ethics-review issue requiring escalation based on the paper text alone.

## Soundness Rating
2: fair. The question is relevant and the paper includes real experiments, but the core causal claims are only partially supported because the setup conflates deliberate benchmark exposure with contamination, key controls are missing, and the contamination probes are under-validated.

## Presentation Rating
2: fair. The paper is readable at a high level and **Figure 1** is helpful, but the exposition is uneven, several methodological details are underspecified, and there are enough writing/citation issues to impede confidence.

## Contribution Rating
2: fair. The multilingual contamination angle is interesting, but the empirical evidence is not strong enough to establish the broader claims, and the proposed TACD framework remains conceptual rather than a validated contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks a worthwhile question and has some intriguing observations, but the current version overclaims relative to what its setup actually demonstrates, lacks the controls needed to isolate the role of translation, and does not validate its contamination probes strongly enough for ICLR acceptance.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main methodological concerns, especially around contamination framing, probe validity, and interpretation of the tables and figures, though some implementation details are missing from the main paper.