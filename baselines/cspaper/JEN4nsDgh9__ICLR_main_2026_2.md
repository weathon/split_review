---
job_id: e6865ddc-9f60-4562-b2cd-f0b547f6840d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: JEN4nsDgh9.pdf
paper: Do I Look Like a “cat.n.01” to You? A Taxonomy Image Generation Benchmark
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark and evaluation study for text-to-image generative models, with emphasis on taxonomy-structured concept understanding and representation.

## Minimum Quality
Pass ✅. The paper contains the expected components for a benchmark paper, including abstract, introduction, datasets/methodology, evaluation protocol, quantitative results, related work, and conclusion. There are notable issues in rigor, clarity, and mathematical justification, but they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, concealed instructions to reviewers, or other signs of prompt injection or manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces a benchmark for Taxonomy Image Generation, focused on evaluating whether text-to-image systems can generate images for WordNet concepts, including both ground-truth synsets and LLM-predicted concepts. The benchmark evaluates 12 systems using a mix of pairwise preference judgments, a reward model, standard image generation metrics, and several taxonomy-structured CLIP-based metrics involving lemmas, hypernyms, cohyponyms, and specificity.

The paper reports that model rankings on this taxonomy-oriented task differ from rankings on conventional text-to-image benchmarks, with Playground and FLUX performing strongly on preference-based evaluation and retrieval-based methods performing poorly. The authors also study the use of GPT-4 as a pairwise image judge and compare its preferences against human judgments.

## Strengths
1. The paper addresses a task that is reasonably distinct from standard text-to-image benchmarking. Evaluating image generation for WordNet synsets, especially abstract, rare, and hierarchy-linked concepts, is a meaningful benchmark direction, and the paper makes a credible case in the introduction that prompts derived from taxonomies differ from the verbose prompts common in datasets like DiffusionDB.

2. The benchmark setup is broad. It includes multiple subsets, ground-truth and LLM-predicted concepts, prompt variants with and without definitions, and a reasonably diverse set of 12 systems including both generation and retrieval. That breadth is useful for surfacing failure modes that would not appear on standard photorealistic prompt benchmarks.

3. The paper does make an effort to triangulate evaluation rather than relying on one score. Human pairwise preferences, GPT-4 pairwise judgments, a reward model, CLIP-derived taxonomy metrics, IS, and FID are all included. Even though I have concerns about some of these choices, the multi-view evaluation philosophy is a real strength.

4. Some figures are genuinely helpful for motivating the problem. In particular, **Figure 1** supports the claim that taxonomy prompts can be semantically underspecified relative to conventional T2I prompts, and that adding a WordNet definition may still leave room for lexical confusion. Likewise, **Figure 2** is a simple but effective visual demonstration that the retrieval baseline can fail in a qualitatively different way than generative models, which helps justify including retrieval as a contrastive baseline rather than as a competitive solution.

5. The human-versus-GPT comparison is interesting as a diagnostic. **Figure 4** suggests that the ranking correlation between GPT-based ELO and human ELO is fairly high when definitions are included, even though the paper also reports strong position bias at the level of raw battle outcomes. That tension is worth studying and could become a useful contribution if analyzed more carefully.

6. The quantitative tables do contain a useful high-level signal, even if the presentation is messy. For example, **Table 3** and **Table 5** show that Playground, FLUX, and PixArt are repeatedly near the top across several subsets, while retrieval and older SD variants are less competitive on preference-based evaluation. This is enough to support the broad claim that taxonomy-focused ranking differs from “image quality only” ranking and that generation is stronger than retrieval for this task.

7. The qualitative error analysis in the later figures is useful. **Figures 13 to 18** illustrate recurring failure modes such as text rendering, abstract placeholder imagery, lexical confusion, and parent-concept collapse. Those examples make the benchmark’s intended difficulty concrete.

## Weaknesses
1. The paper’s main technical pitch around “theoretically justified” taxonomy metrics is much weaker than advertised, and some of the mathematical statements are not convincing as written. On **Page 6**, Equations **(1) to (3)** define
\[
S_{\text{lemma}}(v,x) := P(X=x\mid v)\approx \mathrm{sim}(C(v), C(x)),
\]
and analogous quantities for hypernyms and cohyponyms. This quietly equates a cosine similarity in CLIP space with a conditional probability over images, without specifying any calibration, normalization, or probabilistic model that would make this approximation meaningful. Cosine similarities can be negative, do not sum to one over \(x\), and cannot directly serve as \(P(X=x\mid v)\) on a finite measurable space without additional transformation. Because the later theorems and interpretations depend on these quantities being probabilities, this is not a cosmetic issue, it affects the validity of the benchmark’s metric interpretation.

2. The theoretical claims in the appendix are overstated and, in places, mathematically unsound. For example, **Theorem 2** on **Pages 17-18** claims that maximizing \(S_{\text{hyper}}(i,x)\) or \(S_{\text{cohyponym}}(i,x)\) is proportional to minimizing
\[
D_{\mathrm{KL}}(P(X\mid i)\|P(X\mid A(i))).
\]
But the proof only argues informally that increasing \(P(X=x\mid A(i))\) for a fixed \(x\) can reduce the KL term, under a vague “large enough \(S_{\text{lemma}}(i,x)\)” assumption. That is far from establishing proportionality between pointwise maximization of a score for one image and minimization of a divergence between full distributions. Similarly, **Theorem 4** claims that maximizing specificity is proportional to maximizing mutual information \(I(V;X)\), but the proof only gestures at one term in the MI sum and does not justify the global optimization statement. These derivations should either be removed, substantially weakened, or reformulated as intuition rather than theorem-level claims. Right now the math adds confidence theater more than scientific clarity.

3. The definition of the Specificity metric is inconsistent in the main text. On **Page 6**, the text says specificity measures “the relation of the CLIP-Score to the Cohyponym CLIP-Score” and then gives
\[
\frac{S_{\text{hyper}}(v,x)}{S_{\text{cohyponym}}(v,x)}.
\]
However, the appendix definition on **Page 18** defines
\[
\mathrm{Spec}(i,x)=\frac{P(X=x\mid i)}{P(X=x\mid C(i))},
\]
which corresponds to lemma over cohyponym, not hypernym over cohyponym. This is not a minor typo, because the interpretation changes substantially. The tables later seem to align with the appendix-style definition, but the main paper does not cleanly state what was actually used. A benchmark paper lives or dies on metric precision, and here the central metric is underspecified in the main text.

4. The evaluation design leans heavily on prompts with definitions, but this partially undercuts the motivating claim that the benchmark probes taxonomic understanding from concise synset-like prompts. The introduction and **Figure 1** emphasize that taxonomy prompting is fundamentally different from standard T2I prompting. Yet much of the headline analysis, including the main human/GPT ranking in **Figure 4**, uses prompts with the extra template “An image of <CONCEPT> (<DEFINITION>)”. Once the definition is appended, the task starts to resemble conventional descriptive prompting much more closely. This matters because the paper’s strongest claim is not just “can a model follow a definition,” but “can a model visualize a taxonomy concept.” The without-definition setting is therefore not a side diagnostic, it is central. The paper should have treated the no-definition results as primary or at least analyzed the gap much more deeply.

5. The human evaluation protocol is under-described relative to how heavily the paper relies on it. On **Page 5**, the paper states that 3370 pair images were evaluated by 4 assessors expert in computational linguistics, and reports a Spearman correlation of 0.8. But it is not clear how many annotations each pair received, whether every pair was independently labeled by multiple annotators or partitioned among annotators, how disagreements were resolved, whether annotators saw model names or source ordering, and whether the “Tie” and “Both Bad” labels were retained or collapsed before BT fitting. Since the authors also acknowledge strong position bias in GPT judgments and use pairwise preferences as a major outcome variable, annotation procedure details matter a lot.

6. The paper itself exposes a serious issue with GPT-as-a-judge, but then still uses it prominently without enough mitigation. On **Page 7**, the authors say there is “no correlation between raw scores for individual battles” and attribute this to a strong bias toward the first option, also illustrated in **Figure 5** and **Figure 12**. If raw judgments are heavily position-biased, the BT aggregation may smooth some of this, but it does not make the underlying problem disappear. A robust setup would counterbalance image positions per battle, anonymize presentation consistently, run multiple judge prompts or seeds, or report judge calibration experiments. The limitation section on **Page 15** explicitly admits that model names were not renamed and positions were not alternated per pair. For a paper that “pioneers” GPT-4 pairwise evaluation for image generation in this context, this is simply not careful enough.

7. The main results presentation is too compressed and, in places, confusing to support the paper’s claims cleanly. **Table 2** is supposed to summarize the top-1 model for each metric and subset, but it contains many apparent formatting or naming issues, such as model names like “Pluground,” “Ptolet,” “Kombesky,” “Dram,” and “SDT,” which do not match **Table 1**. That makes the table hard to trust as a scientific summary. More importantly, reporting only the top-1 winner per subset hides effect sizes and often overstates differences that are likely tiny. For benchmark papers, complete leaderboard tables and uncertainty-aware comparisons should be primary, not buried in later tables or appendices.

8. Some of the actual quantitative evidence weakens the benchmark’s metric story. The CLIP-based metrics often favor models that do not align with human preference. For instance, the discussion on **Page 8** notes that SDXL-turbo dominates lemma, hypernym, and cohyponym similarity, while preference-based evaluation favors Playground and FLUX. **Table 13** and **Table 14** also show that older models such as SD1.5 can look very strong on specificity. This could be an interesting finding, but the paper mostly handwaves it as CLIP focusing on alignment rather than quality. That explanation is too shallow. If the proposed benchmark metrics are intended to reflect taxonomy understanding, then a strong divergence from human preference should trigger a much more careful analysis of whether the metrics are measuring the intended capability, or merely reward textual literalism / CLIP compatibility.

9. The benchmark’s novelty relative to existing structured T2I evaluation is not positioned sharply enough. The paper cites some related concept-learning and taxonomy-adjacent work, but the main text does not clearly disentangle how this benchmark differs from prior concept-centric and structured T2I benchmarks beyond “it uses WordNet synsets.” A stronger comparison to existing fine-grained and concept-oriented benchmarks would help establish what is genuinely new here: the dataset construction, the taxonomy-aware metrics, the evaluation protocol, or the specific use of WordNet. Right now the contribution is plausible, but under-argued.

10. The retrieval baseline comparison is visually persuasive but empirically somewhat underdeveloped. **Figure 2** presents a favorable example for generation over retrieval, and the text concludes that retrieval performs poorly. However, the retrieval setup on **Page 16** is just top-1 Wikimedia Commons search, with many duplicates and missing images. That is a rather weak baseline, and it is not obvious that poor performance demonstrates a fundamental advantage of generation over retrieval, rather than a weak retrieval pipeline. If the claim is “generation beats retrieval for taxonomy depiction,” the baseline should be stronger, for example by using image-text retrieval with CLIP or multiple candidate reranking.

11. Several benchmark construction choices are insufficiently justified in the main paper. The random split sampling process on **Page 3** gives relation-type probabilities for sampling and then different probabilities for occurrence in the test set. The explanation is tied to TaxoLLaMA training utility rather than benchmark representativeness. That is odd, because benchmark composition should be justified based on evaluation goals, not inherited from another model’s training priorities. Similarly, the LLM-prediction dataset uses GPT-4-generated definitions to “match” generated nodes to WordNet-style prompts, but the main text leaves that pipeline mostly to the appendix. Since this subset is central to the “taxonomy extension” framing, it needs clearer justification in the main paper.

12. Presentation quality is noticeably below ICLR standards in the current form. There are many typos and inconsistencies, such as “Suprisingly,” “vizualization,” “depicturing,” “Pluground,” “Kombesky,” and malformed references on **Pages 9-14**. The references section is visibly corrupted in places, with repeated numbering fragments and formatting artifacts. This is not just cosmetic. In a benchmark paper, sloppiness in naming, notation, and tables makes it harder to trust the leaderboard and definitions.

13. The paper over-relies on appendices for core evidence. The main text often points to appendix figures and tables for significance, detailed results, and error analysis. For example, the central claims about FID, IS, reward-model significance, and subset behavior are mostly deferred to later tables. A benchmark paper should surface its essential evidence in the main paper, especially when the headline claim is that taxonomy rankings differ substantially from standard T2I rankings.

## Questions
1. Please clarify exactly how the CLIP-based quantities are computed and normalized. If \(S_{\text{lemma}}, S_{\text{hyper}}, S_{\text{cohyponym}}\) are only similarity scores rather than probabilities, I strongly suggest rewriting Equations **(1)-(3)** and the subsequent theoretical discussion to avoid probability notation. Can the authors provide a clean metric definition in score-space, separate from the probabilistic intuition?

2. Which definition of Specificity was actually used in the experiments, the main-text version \(\frac{S_{\text{hyper}}}{S_{\text{cohyponym}}}\) or the appendix version \(\frac{S_{\text{lemma}}}{S_{\text{cohyponym}}}\)? Please reconcile the inconsistency and, if it was a typo, state clearly where and whether any reported numbers would change.

3. For the pairwise human evaluation, how many judgments were collected per pair, how were pairs assigned to annotators, and how were ties / both-bad labels handled in the BT model fitting? A short but precise annotation protocol would increase confidence substantially.

4. For the GPT-based evaluation, did the authors run any counterbalancing experiment where the same battle is evaluated with swapped left-right or A-B order? Given the position bias reported in **Figure 5** and **Figure 12**, this seems essential. If such an experiment exists, even on a subset, it would materially improve my confidence.

5. Can the authors provide a stronger analysis of the mismatch between human-preference rankings and CLIP-based taxonomy metrics? For instance, are these metrics better correlated with human judgments on some subsets than others, such as concrete vs. abstract concepts, or with/without definitions?

6. Why is the with-definition condition treated so prominently given the benchmark motivation? I would like to see a more explicit justification that this still measures taxonomic understanding rather than ordinary definition-following, or alternatively a reframing that the benchmark has two distinct tasks.

7. The retrieval baseline seems very weak. Could the authors compare against a stronger CLIP-based retrieval or reranking baseline to test whether the poor result in **Figure 2** and the broader ranking is due to retrieval as a paradigm or to the specific Wikimedia top-1 pipeline?

8. Please clean up **Table 2** and explain the naming inconsistencies. As written, the summary table is difficult to interpret and does not inspire confidence in the benchmark packaging.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper evaluates and releases taxonomy-linked image generation at broad WordNet scale, including automatically generated depictions for concepts across the taxonomy. As noted in the paper’s ethical considerations on **Page 9**, text-to-image systems can generate offensive or harmful content. The benchmark itself is not primarily an ethics paper, but releasing large-scale generated imagery tied to semantic categories may amplify harmful stereotypes or problematic depictions for person-related concepts, social roles, or sensitive attributes if such nodes are included. I do not see this as a reason for rejection on its own, but I do think the final version should include a more concrete discussion of screening, filtering, or usage warnings for released generated images.

## Soundness Rating
2: fair. The empirical effort is non-trivial and there is enough experimentation to support some high-level conclusions, but several metric definitions and theoretical claims are not soundly justified, and key evaluation details are under-specified.

## Presentation Rating
2: fair. The paper is understandable overall, but the writing, notation, table quality, and reference formatting need substantial cleanup. Important methodological details are also too diffuse.

## Contribution Rating
2: fair. The benchmark direction is interesting and potentially useful, but the current paper does not yet make the case with enough rigor and precision for a stronger contribution rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The problem setting is worthwhile and there is real benchmarking effort here, but the current version has too many core issues in metric formulation, theoretical justification, evaluation protocol, and presentation for me to support acceptance.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the paper carefully, especially the metric definitions, tables, and the main claims around pairwise evaluation and taxonomy-specific scoring.