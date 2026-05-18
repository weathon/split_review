Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes TNT, a multi-modal framework that represents tabular data via a structure-aware Table Encoder (bi-dimensional attention without positional embeddings) and column-level embeddings, trained through column-wise contrastive pre-training, multi-task feature alignment, and instruction tuning. The core idea is to bridge the semantic gap caused by converting 2D tables into flat text for LLMs. Evaluated on NL2SQL (SPIDER and variants), TNT achieves up to **14.4% higher execution accuracy** compared to text-based serialization, especially when column names are non-semantic.

---

## Strengths

- **Novel structure-aware table representation.** The bi-dimensional attention mechanism (Section 3, Eq. 2) applies BERT-style attention first along rows then along columns, preserving permutation invariance by intentionally excluding positional embeddings. This directly addresses the structural incompatibility of text serialization.

- **Column-wise contrastive pre-training is critical and well-validated.** The self-supervised objective (Section 4.1) uses random row sampling of the same table to create positive pairs across snapshots. Ablation (Table 3) shows removing pre-training causes a **−23.4% performance drop**, confirming its essential role.

- **Strong empirical gains on non-semantic schemas.** On datasets where 80% of column names are anonymized (Table 1), TNT achieves up to **16.5% higher EM** and **14.4% higher EX** versus text-based baselines. This directly supports the claim that column embeddings capture distributional patterns rather than relying on schema cues.

- **Column embeddings are empirically distinguished from soft prompts.** Table 4 shows that inserting the same number of learnable parameters as soft prompts yields no significant improvement, while TNT's embeddings provide substantial gains, confirming they carry genuine table semantics.

- **Generalizability across backbone LLMs.** TNT consistently improves EX accuracy whether using LLAMA3-8B, MISTRAL-7B, or CODELLAMA-7B (Table 2), showing robustness across architectures.

- **Compatibility with orthogonal prompting techniques.** Table 6 shows TNT integrates seamlessly with Schema Filtering, Code Correction, and Self-Consistency, enabling a 8B-parameter model to approach closed-source LLM performance (GPT-4, GPT-3.5).

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Contrastive pre-training may inadvertently exploit column names as identifiers, and the paper does not clarify this.** The column-wise contrastive learning (Section 4.1) applies random row sampling to create two snapshots that "share the same schema but have different cell contents." If column names (header row cells) are included in the cell content matrix — and the paper does not state they are excluded — then the model could trivially identify "same column" across snapshots by matching names, rather than learning distributional column semantics. The evaluation on non-semantic SPIDER variants (Table 1) partially addresses this concern (the model works when column names are anonymized at test time), but the pre-training shortcut would still exist. The authors should clarify whether column names are included as cells during pre-training, and ideally provide evidence (e.g., column-matching accuracy with randomized names) that the encoder genuinely learns content-driven semantics. This does not invalidate the overall results but weakens the claim about what the pre-training stage actually learns.

- **The 86K-table pre-training dataset is described at only a domain level, with no detailed statistics.** The paper states the dataset contains 86,046 business tables from finance, education, and medicine (Section 4), but provides no table-level statistics (average rows/columns, size distribution, source URLs or provenance, quality filtering criteria). While the paper notes all resources are in supplementary materials, the lack of any quantitative or structural description of this dataset in the main paper makes it difficult for readers to assess the generality of the pre-training data or reconstruct a comparable corpus. This is reproducible if the supplementary materials are complete, but the description in the paper itself is thin.

- **The hybrid representation design choices are not ablated.** The paper uses a hybrid of (1) column names + foreign keys in text, (2) column embeddings, and (3) one sample cell value per column in text. There is no ablation of which information is placed in text versus embedding, nor is there an analysis of how the one sample value is selected (random? first row? most frequent?) or whether performance is sensitive to this choice. Table 5 varies the *number* of sample values but not their selection strategy. This is a gap given that the representation has several degrees of freedom.

- **Table 6 conflates the value of TNT with orthogonal prompting techniques.** The paper shows TNT combined with Schema Filtering, Code Correction, and Self-Consistency approaches closed-source models, but does not show whether text-based baselines gain similar improvements from those same techniques. Without this control, it is unclear how much of the gain is attributable to TNT's embeddings versus the prompting methods. (The paper's core claims do not depend on this comparison, but the presentation inflates the significance of Table 6.)

### Trivial
None.

---

## Nice-to-Haves

- **Test on additional table understanding tasks** (e.g., table QA, fact verification) to show the embeddings generalize beyond NL2SQL. The paper acknowledges this scope limitation.
- **Directly probe column representations** (column-type classification, cross-table column matching) to demonstrate the encoder encodes distributional semantics rather than surface cues.
- **Report computational efficiency metrics** (inference time, token count reduction, memory usage) to make the "expressive efficiency" claim concrete.
- **Ablate the 2D attention modules** against simpler pooling (e.g., mean of cell embeddings per column) to isolate the contribution of the attention mechanism.
- **Show pre-training loss curves** or probing accuracy during pre-training to demonstrate the column-wise objective is learning meaningful structure.
- **Analyze failure cases** by comparing erroneous SQL queries from TNT versus text baselines to understand where column embeddings help or mislead.

---

## Removed Points

These points were raised by the original reviewers but are excluded from the main evaluation as they are factually incorrect, reflect reviewer misunderstanding, or are scope-creep:

1. **"The paper does not compare against other learned table representations."** — Factually wrong. The paper's Further Analysis (line 246) explicitly compares against TransTab and CM2, showing both "show poor alignment with the backbone LLM." The critic missed this section.
2. **"The title implies broader scope than NL2SQL."** — The paper explicitly states (Section 1, line 27): "we will focus on the NL2SQL task as a concrete example, which can also serve as an interface in other general table-related tasks." The scope is clearly justified.
3. **"Ethical considerations of business tables not discussed."** — A generic concern not specific to this paper's quality.
4. **"Missing related works."** — Per instructions, I cannot verify existence of missing references and do not include this as a weakness.
5. **Various formatting/presentation nitpicks** and reproducibility complaints about hyperparameters not disclosed — these are standard parser artifacts or typical for the paper class.

---

## Novel Insights

The key insight that emerges from reading the paper alongside the reviews is that TNT's architecture draws a clean and well-executed analogy to Vision-Language Models (VLMs), treating tabular data as a third modality with its own encoder, alignment adaptor, and contrastive pre-training. The paper's strongest contribution is not just the performance gain but the demonstration that *column embeddings provide unique value specifically when schema quality degrades* — the 14.4% EX gap on non-semantic schemas is the headline finding, and it is well-supported. The secondary insight is that contrastive row-sampling (rather than cell masking or column prediction) is a surprisingly simple and effective pre-training signal for column semantics, as validated by the −23.4% ablation hit. The main open question the reviews surface is whether the contrastive objective actually forces column-semantic learning or whether it lets the model take a shortcut via column names — this is the one question that needs a clear answer before the paper's framing of "structure-enriched" vs. "name-based" understanding is fully convincing.

---

## Suggestions

1. **Clarify whether column names are included as cells during contrastive pre-training.** If they are, provide an experiment randomizing column names at pre-training time and measuring whether column-matching accuracy degrades — this would confirm the encoder learns distributional semantics rather than name-matching.
2. **Add a table with dataset statistics** for the 86K-table corpus (e.g., mean/median rows, columns, number of domains, size percentiles).
3. **Run a control experiment for Table 6** showing the same prompting techniques applied to the text-based baseline, to isolate TNT's additive contribution.
4. **Ablate the one sample value selection** (random vs. first row vs. most frequent) to show robustness.
5. **Add a brief analysis of failure cases** to strengthen the paper's own assessment of limitations.

---

## Score and Decision

**Originality:** Good — treating tables as a distinct modality with column-wise contrastive pre-training is a well-motivated and relatively novel framing.  
**Importance of research question:** High — LLM understanding of structured data is a practically important and open problem.  
**Claims well-supported:** Mostly yes. The core claim (column embeddings improve over text serialization, especially with poor schemas) is well-supported by Tables 1–5. The one gap is the pre-training shortcut concern.  
**Soundness of experiments:** Solid. The ablations (Table 3, Table 4, Table 5) are well-designed. The main gap is the lack of comparison with prompting techniques added to baselines in Table 6.  
**Clarity of writing:** Clear and well-structured. The multi-modal analogy to VLMs is well-explained.  
**Value to community:** High — the approach is modular and could be integrated into other table-based LLM systems. The dataset and code in supplementary materials will enable follow-up work.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>