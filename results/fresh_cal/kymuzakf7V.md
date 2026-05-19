Here is my consolidated final review.

## Summary

ProtoLLM proposes a training-free, example-free framework for zero- and few-shot tabular classification. The core idea is to prompt an LLM (without any examples in the prompt) to generate discriminative feature values for each class, treating these values as prototypes. The LLM is queried feature-by-feature, and the generated feature values are averaged (optionally fused with few-shot examples) to build class prototypes. Classification is then performed by measuring Euclidean distance to these prototypes. The paper reports experiments across 10 datasets and multiple baselines.

## Strengths

- **Ablation evidence directly supports the core design principle.** Table 1 shows that inserting examples into the prompt consistently decreases AUC compared to the example-free version, empirically confirming the paper's central claim that example-free prompts yield cleaner feature values (Sec. 4.3, Tab. 1).

- **Feature-level generation outperforms sample-level generation.** Table 1 compares feature-level (one feature per prompt) vs. sample-level (all features simultaneously) generation; the feature-level variant achieves higher AUC across all settings, supporting the claim that decomposing the reasoning task improves prototype quality (Sec. 3.3, Tab. 1).

- **Training-free prototype construction with strong few-shot performance.** Equations 2–4 define the classifier using only averaged feature values and Euclidean distance with no learnable parameters. Despite this simplicity, ProtoLLM achieves competitive or superior results against tuned baselines (TabPFN, STUNT, FeatLLM) across 4–64 shot settings (Fig. 5).

- **Robustness to different distance metrics.** Table 2 shows that varying Euclidean, Manhattan, and Cosine distances changes AUC by less than 0.01 on average across 10 datasets, indicating the prototypes capture class-discriminative patterns independent of the similarity function (Sec. 4.3, Tab. 2).

- **Method benefits from stronger LLMs and works on unseen datasets.** Table 3 shows GPT-4o improves zero-shot AUC on 7/10 datasets over GPT-3.5. The method also performs competitively on Cultivars and NHANES — two datasets released after the LLM's training cutoff — indicating it elicits generalizable knowledge rather than memorized patterns (Sec. 4.1, 4.3).

- **Generated features serve as effective data augmentation.** Figure 7 demonstrates that using ProtoLLM's generated samples to augment the training set improves AUC for logistic regression, k-NN, and MLP by substantial margins, further validating the quality of the generated feature values (Sec. 4.3, Fig. 7).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (example-free feature generation improves prototype quality; the method is competitive with or superior to existing approaches) are supported by empirical evidence. The identified issues are addressable and do not invalidate the main conclusions.

### Minor

- **Numerical feature generation is underspecified.** The paper states that for numerical features, "We directly use the output values of LLMs" (Section 3.2). However, the expected output format is never concretely illustrated — e.g., should the LLM output a scalar (42), a range (30–50), a qualitative label ("high"), or something else? The prompt includes a "requirement of output formation" (line 59), but the exact wording is only shown in a figure (Fig. 3) and the parsing procedure is not described. Figure 4 only shows a categorical example. This makes the method partially irreproducible for datasets with numerical features, which are common in tabular learning.

- **No variance or significance reporting.** The paper reports average AUC over 15 runs "with different seeds" but provides no standard deviations, confidence intervals, or error bars in any table or figure. Many reported gains over baselines are modest (a few AUC points), and without variance it is impossible to assess whether differences are meaningful. The "No. 1 average rank" claim would also be strengthened by statistical testing (e.g., a paired test across datasets).

- **Limited zero-shot evaluation.** Zero-shot results are reported only against TabLLM (Fig. 5). No trivial baselines (majority class, random guessing, or simple heuristics) are provided, so the reader cannot contextualize whether the zero-shot AUC values (e.g., 0.688 on Adult) are meaningfully above chance. This undercuts what the paper presents as its strongest differentiation over example-based methods.

- **LLM decoding parameters not reported.** The paper specifies the model (gpt-3.5-turbo-0613) but does not report the LLM generation temperature, max tokens, or any stopping criteria. The τ=1 in Eq. 4 is the softmax temperature for the distance-based classifier, not the LLM generation parameter. These hyperparameters directly affect the diversity and reliability of generated feature values.

- **Categorical prototype handling via Euclidean distance is not justified.** Averaging one-hot encoded categorical feature values (from K LLM queries) produces fractional vectors. The paper uses Euclidean distance to compare prototypes (with fractional one-hot entries) against test samples (with binary one-hot entries) without discussing whether this distance is semantically meaningful or whether alternative approaches were considered.

- **Dataset statistics not provided.** The paper lists 10 datasets but provides no characteristics (number of features per dataset, fraction of numerical vs. categorical features, class distributions). This makes it harder to interpret where ProtoLLM excels or to identify failure modes.

- **Weighted feature generation extension lacks methodological detail.** Table 4 reports improvements from a feature-weighting variant, but the paper does not describe the prompt used to elicit feature weights from the LLM, how weights are parsed, or how they are incorporated into the prototype. This important variant is not reproducible from the current description.

### Trivial
- The paper uses footnotes (marked "1", "2", etc.) whose content is absent from the parsed text. These likely contain implementation clarifications that would address some of the reproducibility concerns above.

## Nice-to-Haves
- Adding zero-shot baselines (majority class, random) would contextualize the zero-shot results and strengthen the paper's core differentiation.
- A brief limitations paragraph discussing cases where the method might struggle (e.g., ambiguous feature descriptions, features requiring domain expertise the LLM lacks, or highly imbalanced classes) would improve the paper's completeness.
- Reporting the full prompt template (both for categorical and numerical features) in an appendix or supplementary would resolve the reproducibility concern.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Example-free" framing is overclaimed** — The paper is transparent that the LLM query is example-free while the few-shot variant fuses examples (abstract, Eq. 3). The title characterizes *the LLM prompting* as example-free, which is accurate. Removed as a misunderstanding.
- **"Overfitting claim supported only by a cartoon"** — The paper provides quantitative evidence (Table 1) showing examples hurt performance, which the reviewer later acknowledges. Removed as the concern is addressed.
- **"Baselines cited from Han et al. without cross-validation"** — Standard practice for reproducing published results. Removed as it is unfair to require re-running all baselines.
- **"Missing related work"** — Removed per policy (no external verification possible).
- **"Prompt template only in screenshot"** — The paper describes the prompt structure in detail in Section 3.1 (lines 55–59). Figure 3 is supplementary. The structure is explained at a level appropriate for a conference paper. Removed as overly demanding.
- **"Ablation only shows zero-shot for sample-level"** — Cannot be verified from the text alone (Table 1 is an image). Removed.
- **"Formatting/style nitpicks"** — Various minor presentation complaints. Removed per policy.

## Novel Insights
The most interesting observation to emerge from these reviews — beyond the paper's own contributions — is a tension between the two evaluators. The Strength Finder correctly notes that Table 1 is the paper's strongest piece of evidence (example-free consistently beats example-based), while the Harsh Critic rightly points out that the same experiment is conducted without variance reporting, making it hard to gauge effect sizes. This tension is productive: the paper's core evidence is directionally clear but could be substantially strengthened with basic uncertainty quantification. Additionally, neither reviewer fully discusses the implication of the feature-level vs. sample-level ablation beyond what the paper states — that decomposing the LLM's reasoning into per-feature sub-problems is what enables high-quality generation. This design principle (task decomposition for LLM-based feature generation) may be the paper's most transferable insight for follow-up work.

## Suggestions
- **Specify numerical feature generation.** Provide the exact prompt format used for numerical features, with a concrete example (e.g., for "age" or "income"), and describe how the LLM's text output is parsed into a scalar value.
- **Report standard deviations or confidence intervals** for all main results (Tables 1–4, Figs. 5–7). Even a simple table of mean ± std across the 15 runs would greatly strengthen the evidence.
- **Add trivial zero-shot baselines** (majority class, random) to contextualize absolute AUC values and demonstrate that the zero-shot performance is indeed meaningful.
- **Report the LLM's decoding hyperparameters** (temperature, max tokens, top-p) explicitly, even if they are default values.

## Score and Decision
The paper presents a novel, well-motivated, and empirically supported approach to leveraging LLMs for few-shot tabular learning. The core idea — example-free feature-level generation to build prototypes — is clearly articulated, and the ablations provide direct evidence for the design choices. The experimental evaluation spans 10 datasets and compares against multiple categories of baselines. The weaknesses are real but addressable: none undermines the core claims. With minor revisions to address reproducibility and rigor concerns, this paper would be a solid contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>