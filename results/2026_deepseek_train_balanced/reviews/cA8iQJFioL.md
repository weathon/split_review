## Summary

The paper introduces InterIDEAS, a dataset for philosophical intertextuality covering over 45,000 pages, 15,000+ cross-referential pairs, and 3,150+ philosophers/writers from 1750–1950. It proposes a metadata schema (content type, intertextual function, sentiment) and presents preliminary experiments including a human-vs-LLM evaluation on 6 passages and sentiment classification fine-tuning across 9 models. The ambition — bridging NLP with philosophical text analysis at scale — is laudable, but the paper as submitted is critically incomplete.

## Strengths

- **Scale and coverage are genuinely substantial.** The dataset spans 45,000+ pages, 15,000+ annotated reference pairs, and 3,150+ philosophers across 1750–1950, with explicit selection criteria (prominence, geography, occupation). This is orders of magnitude beyond what close-reading or prior bibliometric approaches achieved for philosophy.

- **Fine-tuning on InterIDEAS produces consistent gains across diverse models.** Section 5.2 reports that accuracy improves from ~22–27% to ~58–59% after fine-tuning across 9 models (BERT, RoBERTa, XLNet, Llama 2/3, Mistral, GPT-2), and macro-F1 improves from ~17–27% to ~36–52%. These gains are reported across multiple architectures and model sizes, suggesting the corpus carries useful signal for sentiment classification in philosophical text.

- **The metadata schema is well-conceived and multidimensional.** The three-axis schema (Content Type: nominal/verbal/thematic; Intertextual Function: name-dropping, contextual explanation, critical engagement, conceptual application/expansion; Sentiment: negative/neutral/positive) is more structured than raw citation counts and enables the quantitative patterns reported (e.g., 67.9% nominal references, 77.4% neutral sentiment, 52% name-dropping as primary function).

- **Candid documentation of LLM limitations.** Section 6 honestly identifies three specific failure modes (semantic dissection, literal-mindedness, stereotyping) along with mitigation attempts (few-shot instances, constraint imposition). This transparency about known limitations strengthens credibility.

## Weaknesses

### Fatal

- **The dataset construction methodology is entirely absent.** Section 3 is missing — the paper jumps directly from an empty Section 2 (Related Works) to Section 3.2 (Data Quality Evaluation). There is no Section 3 or 3.1 describing how the dataset was built. The reader is told the approach "leverages cutting-edge LLMs alongside expert knowledge from philosophy scholars" (Introduction), but nothing more. Which LLM was used for extraction? What prompts were designed? How were experts involved — did they annotate from scratch, validate LLM outputs, or adjudicate disagreements? What was the annotation pipeline? What quality-control measures were applied? What inter-annotator agreement was achieved? How were disagreements resolved? For a dataset paper, the construction methodology is the central contribution. Its absence means the core contribution is unverifiable and the work is unreproducible. This single issue is fatal.

- **Section 2 (Related Works) is completely empty.** The paper cannot situate its contribution within existing NLP datasets for humanities, citation extraction, or intertextuality research. It cannot demonstrate what prior approaches lacked or what design choices were informed by prior work. For a conference submission, this is a critical omission independent of the methodology gap.

### Major

- **The metrics (Accuracy/Recall) are defined inconsistently with standard terminology.** The formulas (line 42) define Recall = *x*/*y* (correct/total answers given) and Accuracy = *x*/*r* (correct/total correct answers). Under standard terminology, *x*/*y* is **precision** and *x*/*r* is **recall**. The descriptive text in line 48 then describes the standard concepts ("Accuracy measures the model's correct responses, indicating its precision" and "Recall assesses its ability to identify all relevant answers"), creating an internal contradiction with the formulas. While the quantities are explicitly defined and a careful reader can interpret them, the inconsistent labeling undermines confidence in the reported numbers and indicates insufficient rigor in the evaluation design.

- **The human evaluation is too small to support the paper's claims.** Only 5 experts, 16 humanities students, and 29 other students were tested, on only 6 passages (~500 words each). No statistical significance testing is reported for the comparison between "our approach" and human experts or baselines. With these sample sizes, the observed differences could be noise. The paper states "our approach ranks just below experts" without establishing whether any performance gap is significant.

- **The 20-minute time constraint applies to human participants but it is unclear whether it applies equivalently to automated methods.** If LLMs were not similarly time-limited while humans were, the comparison is not meaningful as a fair assessment of capability.

### Minor

- **The dataset's inter-annotator agreement is never reported.** For a resource built on human interpretation of subtle textual cues (sentiment, function, content type), Cohen's κ or a similar measure is essential to establish annotation reliability.

- **The sentiment classification experiment has several methodological weaknesses.** The test set has only 228 samples with heavy imbalance (142 negative, 53 neutral, 33 positive); training for 100 epochs on only ~1,565 training samples risks overfitting (which the paper acknowledges); and the best macro-F1 of 52.35% on a 3-class problem is modest. These factors weaken the claim that the dataset is a strong training corpus for improving model interpretative capacity.

- **The paper does not report GPT-4o's quantitative results** for the sentiment classification task, despite stating "even simple few-shot learning markedly improves output quality." The table is an unreadable embedded image, and no specific numbers for GPT-4o are given in the text.

- **The PLM/LLM categorization is inconsistent with standard usage.** GPT-2 (124M parameters) is grouped with LLMs alongside Llama-7B/8B, while BERT (110M) is grouped as a PLM. The meaningful axis is parameter count and architecture, not this arbitrary dichotomy.

### Trivial

- Citation error: "GPT-4o (Achiam et al., 2023)" — GPT-4o was released after the GPT-4 technical report and is not covered by that citation.
- Typo: "overftiting" (line 103).
- Minor phrasing issues: "the most state-of-the-art" (line 97), "synchronical analyses" (line 83).

## Nice-to-Haves

- The paper could benefit from reporting precision and recall values separately with their standard definitions, rather than the current swapped/inconsistent labeling.
- Including confidence intervals or bootstrapped error bars on the evaluation results would substantially strengthen the presentation.
- A full list of source texts and a quantitative breakdown of LLM-extracted vs. human-corrected annotations would be valuable additions if the methodology section is written.

## Removed Points

These points were flagged by the reviewers but are removed or demoted for the following reasons:

- **"Given 45,000 pages and 15,000+ pairs, roughly one annotation per 3 pages — is that density plausible?"** — This is a speculative concern. The density is entirely plausible for philosophical texts where not every paragraph contains a reference, and the paper's own statistics verify the count. Removed (speculative without evidence the count is wrong).
- **"Figures are presented as images and cannot be evaluated"** — This is a PDF parsing artifact; the original submission would contain readable figures. Removed per formatting artifact rule.
- **"The paper may use a more recent model for its method, making the comparison staged"** — Speculative; we do not know what model the method uses because the methodology is absent. This concern is derivative of the fatal missing-methodology issue, not an independent weakness. Removed as speculative.
- **"Missing related works" (as a standalone weakness)** — Already included as fatal point about empty Section 2. Not removed but subsumed into fatal category.
- **"Precision and recall being swapped is fatal"** — Demoted from fatal to major. The formulas explicitly define what was computed, so a careful reader can interpret the numbers. The inconsistency is real but not structure-invalidating.
- **Strength: "LLM + expert hybrid methodology outperforms baselines"** — This strength is retained but weakened by the missing methodology; we cannot evaluate what "our approach" is. However, the experimental results are presented as reported data, so the strength stands as a claim the paper makes, contingent on the missing methodology being supplied.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observations about the missing methodology and metric inversion are correct but are issues of omission/error, not novel analytical insights. The Strength Finder's observations largely recapitulate the paper's own claims.

## Suggestions

1. **Write the missing methodology section (Section 3/3.1).** Describe: (a) which LLM was used for extraction and what prompts were designed, (b) the exact role of experts (did they annotate from scratch, validate LLM outputs, or perform adjudication?), (c) inter-annotator agreement statistics, (d) the annotation pipeline step by step, and (e) how gold-standard answers for the evaluation were established.

2. **Write Section 2 (Related Works).** Situate InterIDEAS against existing citation extraction datasets (e.g., SciCite, ACL-ARC), philosophical text analysis efforts, humanities NLP, and bibliometric approaches to pre-modern citation.

3. **Fix the metric definitions.** Either relabel the formulas to match standard terminology (Accuracy→Precision, Recall→Recall), or use non-standard terms but ensure the descriptive text is consistent with the formulas. Preferably, report precision and recall using standard definitions.

4. **Add statistical significance testing** to the human evaluation (Section 3.2) and report confidence intervals where applicable.

5. **Report inter-annotator agreement** for the annotation process (Cohen's κ or similar) to establish the reliability of the dataset annotations.

6. **Clarify the time-constraint condition** for automated methods in the human evaluation comparison, or remove the constraint asymmetry.

## Score and Decision

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>