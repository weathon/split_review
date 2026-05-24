## Summary
This paper studies whether benchmark contamination can be obscured by translating benchmark items into Arabic, fine-tuning several open-weight LLMs on English plus varying proportions of Arabic benchmark counterparts, and evaluating on English MMLU/XQuAD/MLQA. The topic is timely and potentially important, and the paper contains suggestive empirical observations, especially MMLU score increases with added Arabic data; however, the central causal claim is not well supported because the experimental setup appears to train all conditions on English evaluation content and lacks clean or matched controls.

On the evaluation axes: originality is moderate, since cross-lingual contamination through translation is a useful angle; importance is high; experimental soundness is weak for the main claim; the claims are substantially overextended relative to the evidence; clarity is mixed, with the high-level story understandable but key definitions and interpretations unclear; the current value to the research community is mainly as a motivation for better multilingual contamination studies rather than as a validated result.

## Strengths
- **Timely and concrete multilingual contamination question.** The paper directly targets a real evaluation blind spot: whether translated benchmark content can preserve semantic leakage while evading surface-form contamination checks. This is clearly stated in the Introduction: the authors ask whether translating benchmarks into Arabic “can act as a natural barrier to contamination or whether translation merely conceals memorization effects.”
- **Empirical coverage across several models and tasks.** Section 3.1 uses four open-weight instruction models—Llama-3.2-1B-Instruct, Mistral-7B-Instruct-v0.2, Gemma-3-1B-it, and Qwen3-1.7B—and three datasets: MMLU, XQuAD, and MLQA. This is more informative than a single-model/single-benchmark demonstration.
- **Table 2 contains a consistent descriptive pattern for MMLU.** MMLU accuracy increases from 0% to 100% Arabic contamination for all four models: Mistral 0.577→0.690, Gemma 0.220→0.284, LLaMA 0.332→0.431, and Qwen 0.553→0.581. This is suggestive that added benchmark-related Arabic data can affect English benchmark performance, although the current controls do not isolate the mechanism.
- **The TACD proposal is a plausible conceptual direction.** Section 5.2 gives concrete components—cross-translation benchmarking, TS-Guessing across variants, and back-translation consistency—rather than merely saying that multilingual checks are needed. The paper also honestly notes in Section 5.3 that TACD is a “forward-looking blueprint rather than a complete implementation.”

## Weaknesses

### Fatal
- **The training setup appears to invalidate the main translation-specific causal claim.** Section 3.1 defines  
  \[
  \mathcal{D}_{\text{train}}^d(p)=\mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p)
  \]
  and states that \(\mathcal{D}_{\text{EN}}^d\) is “MMLU: English test items formatted as MCQ; XQuAD/MLQA: English QA.” Section 3.2 then evaluates on English MMLU/XQuAD/MLQA. If this description is literal, the \(p=0\) baseline is already trained on the English benchmark content, and higher \(p\) conditions add Arabic counterparts on top of direct English exposure. This means the experiment does not compare clean models against Arabic-translated contamination; it compares English-contaminated models against English-contaminated-plus-Arabic models. That undermines the headline claim that Arabic translation itself “conceals traditional contamination signals” while preserving benefits.

### Major
- **The contamination-dose variable is confounded with training-data quantity and task adaptation.** In Section 3.1, increasing \(p\) increases the amount of Arabic benchmark-derived data added to the fixed English set. Therefore, changes from 10% to 50% to 100% are not only changes in “contamination level”; they also add more supervised examples in the same task format/domain. Table 2’s MMLU gains could reflect ordinary fine-tuning on more MCQ-like benchmark data rather than translation-mediated memorization. A matched-size Arabic control with unrelated but format/domain-matched examples is needed to support the contamination-specific interpretation.
- **The paper claims “near-flat” contamination behavior, but the reported tables are not flat.** Section 4.2 states that “the models exhibit approximately equal performance on all evaluated benchmarks” and that Tables 2 and 3a show scores remain “broadly stable” as \(p\) increases. This is difficult to reconcile with Table 2: Mistral XQuAD drops 0.455→0.272→0.114 from 10% to 100%; Gemma XQuAD rises 0.364→0.606 from 0% to 100%; LLaMA MMLU rises 0.332→0.431; Qwen MLQA jumps 0.162→0.409 at 10% and then returns to ~0.15. Table 3 also shows large non-monotonic changes, e.g. LLaMA MMLU IDR 0.287→0.643→0.410 and Gemma IDR 0.350→0.029→0.005. The interpretation is therefore too flexible: increases, decreases, collapses, and flat trends are all treated as consistent with the same translation-masking story.
- **The TS-Guessing probe is not clearly defined enough, and its results do not strongly support the proposed mechanism.** Section 3.3 says that for MMLU the authors shuffle choices, mask the text of one incorrect answer, and count either reproduction of the “pre-shuffle letter/index” or the masked choice text as contamination. Section 3.4 defines IDR as \(\mathbf{1}\{\hat{\ell}_i=\ell_i^{\text{pre-shuffle}}\}\). But it is unclear why recalling a pre-shuffle letter after masking an incorrect option should be interpreted as recalling the correct answer index, and the paper does not give chance baselines or repeated-shuffle variance. Empirically, the TS-Guessing table is not aligned with the performance story: Mistral has the largest MMLU increase in Table 2 but near-zero MMLU IDR at all levels; Gemma’s IDR falls from 0.350 at 10% to 0.005 at 100%; Qwen’s IDR is near ~0.25 at 10%/50%, close to chance for four options unless the metric has a different baseline. This weakens the claim that the probe demonstrates hidden memorization under translation.
- **The paper does not directly demonstrate that traditional English-only contamination detectors fail or that TACD succeeds.** The abstract claims that “translation into Arabic conceals traditional contamination signals,” and Section 5 says standard English-only checks fail to capture translated contamination. However, the experiments do not compare against exact/fuzzy matching, Min-K%, guided prompting, or English-only TS-Guessing under controlled English-vs-Arabic contamination conditions. TACD is explicitly described in Section 5.3 as a blueprint, so it should not be presented as an empirically validated framework.

### Minor
- **MLQA is included in the stated TS-Guessing scope but absent from the main TS-Guessing results table.** Section 3.3 says TS-Guessing is run for \(d \in \{\text{MMLU, XQuAD, MLQA}\}\), but Table 3 reports only MMLU and XQuAD. Since MLQA is one of the three main datasets in Table 2, omitting it from the contamination-probe results weakens the completeness of the analysis.
- **The embedding-similarity discussion is not quantitatively connected to model behavior.** Section 4.3 says Arabic→English translations remain close to English originals in representation space using cosine similarity, but no figure values or correlations with Table 2/Table 3 behavior are provided in the main text. High semantic similarity is plausible and relevant, but by itself it does not establish memorization or contamination exploitation.
- **Reliability of the reported trends is hard to assess.** The tables appear to report single aggregate numbers without uncertainty over fine-tuning seeds, sampled contamination subsets, or random choice shuffles. This matters because several effects are non-monotonic and model-specific; variance estimates would help determine which changes are robust.

### Trivial
- None.

## Nice-to-Haves
- Add a same-language English-contamination condition and an Arabic-only translated-contamination condition to separate direct English exposure from translation-mediated exposure.
- Include chance baselines for IDR and EM/RL-F1 under the TS-Guessing probe, especially after answer-choice shuffling.
- Report multiple random shuffles per MMLU item and variance across shuffles/seeds.
- Present TACD either explicitly as a conceptual recommendation or implement a minimal evaluated version comparing English-only checks against translation-aware checks.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Formatting/style issues and typographical concerns.** Any parser artifacts, line breaks, grammar issues, citation formatting issues, or typography complaints are removed and carry no evaluation weight.
- **Missing appendix/hyperparameter details.** The paper says detailed hyperparameters and dataset statistics are in appendices; since appendices may be stripped in the extraction, I do not count missing appendix content as a weakness.
- **Missing related works.** I do not include criticisms about omitted related work, since external source completeness cannot be verified here.
- **Release-status or availability concerns.** The paper’s cited models, datasets, tools, and references are treated as existing and available; no criticism is made about unreleased or unverifiable artifacts.
- **Generic claims that the literature review is too long.** This is largely a presentation preference and not central to the paper’s scientific validity.
- **Overly broad requests for substantially larger model/dataset coverage.** More languages and more models would help, but the core issue is not scale; it is the lack of clean controls and the apparent inclusion of English evaluation data in all conditions.

## Novel Insights
The most important synthesis is that the paper contains a potentially interesting empirical signal—Arabic benchmark-derived data can change English benchmark scores, especially for MMLU—but the current design does not identify that signal as translation-mediated contamination. Because the baseline already appears to include English benchmark items, the study cannot distinguish “translation masks contamination” from “additional benchmark-style supervised fine-tuning changes performance.” The TS-Guessing results further suggest that whatever is happening is not a simple monotonic memorized-index effect; model- and task-specific behavior is substantial and should be treated as a phenomenon to explain rather than as straightforward confirmation of the masking hypothesis.

## Suggestions
- Redesign the core experiment with four clean conditions: no benchmark-overlapping fine-tuning, English benchmark contamination, Arabic-translated benchmark contamination without English originals, and unrelated Arabic control data matched for size/task format/domain.
- Keep the number of fine-tuning examples fixed across contamination levels, or explicitly separate “more contaminated data” from “more total data.”
- Clarify exactly which splits are used for training and evaluation. In particular, resolve whether “English test items” in Section 3.1 are literally the evaluation items.
- Define the MMLU TS-Guessing metric precisely: what is masked, what output is expected, whether the model predicts a letter or text span, how outputs are normalized, and what chance performance is.
- Add English-only detector baselines and a minimal TACD implementation to substantiate the claim that translation-aware methods detect leakage that English-only methods miss.
- Rewrite Section 4.2 to match the actual tables: describe the results as heterogeneous and model/task-specific rather than “approximately equal” or “near-flat.”

## Score and Decision

### Calibration and anchor comparison

**Round-1 bracket.** The first calibration pass retrieved weak, middle, and strong anchors on LLM contamination/multilingual evaluation. Compared with the strong anchors, this paper lacks the controlled experimental design and validated claims needed for acceptance. Compared with middle rejected contamination papers, it is weaker because the main causal comparison is confounded by direct English benchmark exposure. After Round 1, the plausible bracket was **2.5–4.0**.

**Round-2 narrowing.** Round 2 focused on flawed LLM contamination/evaluation methodology. The closest anchors were rejected papers around 3.5–4.25. This paper is comparable to or slightly worse than those because its central experimental contrast appears invalid, not merely incomplete or narrow. It is stronger than the lowest 2.5 anchor because it has a coherent topic, real experiments, and some suggestive data, but weaker than 4–5 anchors that had clearer methods with narrower validation gaps. I therefore assign **3.0**.

### Retrieved anchors

**Round 1 anchors**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MyotJECv0D.md` — avg 2.50. A weak MT-evaluation paper with fundamental conceptual/methodological issues; this paper is more coherent and empirically grounded, so slightly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JQbqaQjV7D.md` — avg 3.00. A rejected cross-lingual LLM benchmark paper with weak evaluation validity; comparable in score due to serious methodology concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/73dhbcXxtV.md` — avg 3.00. A weak mechanistic/memory framework paper; this paper is more topical but similarly under-supported.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fSbPwHjdDG.md` — avg 3.00. A rejected multilingual latent-language paper with contested causal evidence; comparable in having an interesting hypothesis but insufficient support.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nsms7NeU2x.md` — avg 6.75. A substantially stronger contamination paper with broader controlled experiments and theory; this paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` — avg 4.75. A contamination/memorization paper with useful probes but validation concerns; this paper is weaker because the main intervention is more directly confounded.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tbVWug9f2h.md` — avg 7.33. A strong benchmark paper with clearer contribution and validation; this paper is far weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` — avg 4.25. A rejected contamination-detection paper criticized for unclear threat model and insufficient experiments; this paper is somewhat weaker due to the apparent contaminated baseline.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jOmk0uS1hl.md` — avg 8.00. A strong evaluation-confounding paper with persuasive experiments; this paper lacks comparable causal evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/syThiTmWWm.md` — avg 7.75. A strong benchmark-gaming paper with striking validated results; this paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GGlpykXDCa.md` — avg 8.00. A strong benchmark contribution; this paper does not reach that level of validation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z8sxoCYgmd.md` — avg 8.00. A strong benchmark/detection paper; this paper is much less sound experimentally.

**Round 2 anchors**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` — avg 4.25. Similar topic and rejection due to unclear/incomplete experimental support; this paper is weaker because its baseline appears already contaminated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rAylWUIKtu.md` — avg 4.25. A benchmark-contamination paper with unclear holdout validity but a concrete proposed method; this paper is weaker because the core causal contrast is not valid.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HsB1sQvXML.md` — avg 3.80. A rejected detector paper with real experiments but generalization concerns; this paper is slightly weaker because the main interpretation is contradicted by its setup/tables.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aRqyX0DsmW.md` — avg 4.00. A rejected LLM benchmark paper with limited/unclear validity; this paper is comparable but somewhat weaker due to the central contamination confound.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PtnttTKgQw.md` — avg 5.00. A benchmark-validity paper with limited but coherent empirical evidence; this paper is weaker because its evidence does not isolate the claimed mechanism.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` — avg 4.75. A contamination/memorization paper with validation concerns but clearer probes; this paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JL42j1BL5h.md` — avg 3.50. A multilingual LLM evaluation paper with benchmark-validation concerns; this paper is comparable but slightly weaker because the core baseline is contaminated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MyotJECv0D.md` — avg 2.50. A much weaker paper with more fundamental conceptual problems; this paper is stronger than that anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QhsbF2RZeu.md` — avg 3.80. A rejected multilingual evaluation paper with methodological concerns; this paper is slightly weaker because its headline causal conclusion is not supported.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GVNYi74t5L.md` — avg 4.25. A multilingual benchmark paper with evaluation limitations; this paper is weaker due to lack of clean controls.

**Final decision:** Reject. The research question is worthwhile, but the central claims are not supported by the current experimental design.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>