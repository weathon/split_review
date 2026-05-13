Now I have a thorough understanding of the paper. Let me assess each of the harsh critic's claims:

1. **Text-to-SQL evaluation uses Rouge/BLEU instead of execution accuracy**: This is confirmed by lines 102 and 125. The paper explicitly uses Rouge-1, Rouge-L, and BLEU for Text-to-SQL. This is a legitimate and substantive concern — string-level metrics for SQL evaluation are widely recognized as inadequate in the NLP community.

2. **Dataset is template-synthesized**: Confirmed by lines 38-42. The paper describes 45 manually crafted SQL templates, then GPT-4-turbo generates NL questions. This is a real limitation.

3. **Human performance measurement**: Line 47 says "We compute the results of experts as human performance." The paper is vague on whether these are the same annotators evaluating their own work. This is a legitimate concern but the severity may be overstated.

4. **Spider already has multi-table queries**: The paper discusses Spider in related work (line 27) but categorizes it as a "single-table" benchmark. This is somewhat misleading since Spider does contain multi-table SQL queries. However, MMQA's distinction is multi-table QA (not just SQL parsing), and Table 2 makes the comparison systematic.

5. **Binary β function is simplistic**: Confirmed by lines 76 and 82-86. The β function just checks column name overlap (binary 1/0). This is a valid but minor concern.

6. **Temperature 0.7 with no std**: Confirmed line 123. Minor issue.

7. **50 samples per bucket**: Confirmed line 152. Minor issue.

8. **PKS/FKS tasks don't require cross-table reasoning**: Partially valid but PKS/FKS identify joinable columns, which is essential for multi-table reasoning. Not entirely scope-free.

Let me now write the consolidated review.

## Summary

The paper introduces MMQA, a benchmark for evaluating LLMs on multi-table multi-hop question answering, along with MTR, a multi-table retrieval method. MMQA is built on Spider databases using 45 manually crafted SQL templates, with GPT-4-turbo generating natural language questions. The evaluation framework covers five subtasks: multi-table retrieval, text-to-SQL, multi-table QA, primary key selection, and foreign key selection. Experiments show a large gap between LLM and human performance, and MTR outperforms baseline retrieval methods.

## Strengths

- **Fills a genuine gap in multi-table evaluation**: Table 2 systematically demonstrates that MMQA is the first benchmark to jointly cover NL Questions, SQL Queries, Primary/Foreign Key annotation, Multi-Table, Multi-Hop, and Key Selection — dimensions that prior benchmarks cover only partially. The motivation is sound: multi-table reasoning is important and underserved.

- **Multi-granularity evaluation framework**: The evaluation framework (Figure 2, Section 3.3) assesses models at table level (Multi-Table Retrieval), column level (PKS/FKS), and cell level (QA/Text-to-SQL), providing a more fine-grained diagnostic of LLM capabilities than prior single-metric benchmarks.

- **Clear demonstration of a large human–LLM performance gap**: Tables 5 and 6 show human performance at 89.8 EM on 2-table QA versus the best LLM (O1-preview) at 50.78 EM, and human FKS accuracy at 95.3 versus O1-preview at 34.17, confirming both the benchmark's challenging nature and the room for improvement.

- **MTR retrieval method with verifiable gains**: The proposed MTR method achieves 72.3% precision and 68.3% F1 at Top-2 on MMQA (Table 4), and the ablation of Question Decomposition shows meaningful improvement (65.3→72.3 precision at Top-2).

- **Higher reasoning complexity than existing benchmarks**: Figure 3 shows MMQA requires substantially more reasoning steps on average compared to HybridQA, OTT-QA, and FinQA, confirming the benchmark introduces genuinely harder multi-hop tasks.

## Weaknesses

### Fatal
None

### Major

- **Text-to-SQL evaluation uses inappropriate metrics (Rouge/BLEU) instead of execution accuracy**: The paper evaluates SQL generation using Rouge-1, Rouge-L, and BLEU (Sections 3.3, 4.2). These are surface-level string similarity metrics that are well-known to be inadequate for SQL: a semantically correct query with different aliases, column ordering, or equivalent SQL constructs would score poorly, while a syntactically similar but semantically wrong query could score well. The Spider benchmark itself — on which MMQA is built — uses execution accuracy as its primary metric for exactly this reason. This undermines all Text-to-SQL results in the paper: the reported numbers do not reliably measure SQL correctness, so conclusions about LLMs' SQL generation capabilities on multi-table tasks cannot be reliably drawn from these metrics alone. Since Text-to-SQL is one of the five core evaluation subtasks, this is a significant gap in the benchmark's evaluation.

- **Dataset is template-synthesized from SQL, not derived from natural information needs**: Section 3.1 describes the construction pipeline: Spider databases → 45 manually crafted SQL templates → GPT-4-turbo generates natural language questions. This means questions are reverse-engineered from template SQL, not derived from genuine information needs. The paper frames MMQA as measuring "real-world" multi-table complexity, but a template-synthesized dataset cannot fully establish this claim. Questions likely exhibit systematic artifacts of the SQL-to-text generation process, and the "multi-hop reasoning complexity" is an artifact of template design rather than an emergent property of real information-seeking scenarios. With only 45 templates generating 5,000 samples, there is also concern about template reuse limiting the diversity of reasoning patterns required.

### Minor

- **Human performance measurement lacks independent validation**: Line 47 states "We compute the results of experts as human performance, compared with LLMs," but the protocol is unclear about whether these are separate evaluators answering held-out questions or the same annotators being tested on their own answers. If annotators are evaluating their own gold answers, the human ceiling would be inflated, weakening the paper's primary framing of a "significant gap" between LLMs and humans. A clearer protocol with independent evaluators on a held-out subset would strengthen this claim.

- **Binary table relevance function β is simplistic**: The β function (Section 3.2, Algorithm 1) assigns a binary score of 1 for column-name overlap between tables, 0 otherwise. Two tables can share generic column names (e.g., "name," "id") without being joinable, and tables can be joinable through semantically related but differently named columns. Combined with the stopping criterion ("When 0 is assigned, stop iterations"), retrieval could terminate prematurely or produce false joins. This limits the MTR method's reliability, though it does not invalidate the benchmark contribution.

- **Table 2 categorizes Spider as single-table while Spider contains multi-table SQL queries**: The paper claims to be "the first to introduce a multi-table and multi-hop QA benchmark" and Table 2 classifies Spider as a single-table benchmark. However, Spider itself contains multi-table SQL queries over relational databases. The distinction between SQL generation and QA is defensible but the paper should acknowledge Spider's multi-table coverage more explicitly rather than categorizing it as purely single-table.

- **Small sample sizes for table-length analysis**: Figure 4's "elbow point at 800 rows" conclusion is based on only 50 samples per length bucket, with no error bars reported. Given the likely high variance of QA performance on complex multi-table questions, drawing a firm conclusion about a specific threshold from such small samples is unreliable.

## Trivial
None

## Nice-to-Haves

- Report execution accuracy for Text-to-SQL alongside or instead of BLEU/Rouge, which would make the Text-to-SQL evaluation much more interpretable and aligned with community standards.
- Compare MTR against stronger retrieval baselines (e.g., direct LLM-based table selection, dense retrievers fine-tuned on Spider-like schemas) beyond BM25 and TF-IDF.
- Provide more detail on the 45 templates: how they distribute across the 5,000 samples, how many distinct question patterns appear, and how diverse the reasoning types are. This would validate that MMQA requires genuinely diverse multi-table reasoning.
- Break down QA failures by failure mode (wrong table retrieved, wrong join path, wrong cell extraction, computation error) to better reveal which aspects of multi-table reasoning LLMs actually fail at.
- Validate human performance with independent evaluators who did not participate in annotation, on a held-out subset under timed conditions.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Spider already contains multi-table SQL, so the 'first' claim is invalid"** — The harsh critic claims Spider already covers multi-table tasks, invalidating the "first" claim. However, Spider is a text-to-SQL semantic parsing benchmark, not a multi-table QA benchmark. MMQA explicitly evaluates QA (answer extraction), key selection, and retrieval — different tasks from SQL generation. The novelty claim about "first multi-table multi-hop QA benchmark" is defensible; the real issue is just that Table 2's categorization is somewhat misleading, which I've included as a minor weakness.

- **"Temperature 0.7 with no standard deviations is a weakness"** — This is a minor reproducibility nitpick. Non-zero temperature provides diversity and 3-run averaging is reasonable. Not reporting standard deviations is a common practice in the field, especially for costly proprietary model calls. Removed as it doesn't affect the paper's core claims.

- **"PKS/FKS tasks don't require cross-table reasoning"** — While identifying primary keys is primarily a schema-understanding task, foreign key identification does require understanding cross-table relationships (which columns link tables). This is relevant to multi-table reasoning even if not the most complex aspect. Downgraded to implicit in the evaluation framework design.

- **"Algorithm 1 and prose description are inconsistent about the first round"** — The paper explicitly states (line 76): "In the first round, we only consider the question-table relevance score." Algorithm 1 shows a separate first-round computation (line 78: `γ←γ+α(q₀,tableⱼ⁰)`). While the pseudocode formatting is imperfect (a parser artifact), the intent is consistent with the text. Removed as a formatting/parsing artifact concern.

- **Strength claim: "Quality-controlled dataset construction with inter-annotator agreement"** — While inter-annotator agreement is reported (86%/82%), the human performance measurement protocol lacks independent validation (noted as a weakness), making this a partially conflicting strength. Kept the verified part (agreement is reported) but the strong claim about "quality control" is somewhat undercut by the unclear evaluation protocol.

## Novel Insights

The coupling of template-synthesized dataset construction with surface-level SQL evaluation metrics (Rouge/BLEU) creates a compounding validity concern: templates may systematically produce SQL queries with similar surface structure, making string-level metrics even less informative about actual semantic correctness than they would be on a naturally diverse dataset. The 800-row "elbow point" finding (Figure 4) — where QA drops sharply but Text-to-SQL degrades slowly because it relies on headers not cell content — is a genuinely useful practical insight for understanding the scaling limits of LLM table reasoning.

## Suggestions

- Replace or supplement Rouge/BLEU for Text-to-SQL with execution accuracy (execute both gold and predicted SQL against the database and compare result sets). This is the single most impactful improvement the authors could make.
- Provide a template distribution analysis showing how the 45 templates map onto the 5,000 samples and how diverse the resulting question patterns are.
- Clarify the human performance evaluation protocol: specify whether evaluators are independent of the annotation process, and whether evaluation is on a held-out subset.

## Score and Decision

The paper addresses a genuinely important and underserved problem — multi-table multi-hop QA evaluation for LLMs. The multi-granularity evaluation framework, the large human-LLM performance gap, and the demonstration of higher reasoning complexity than existing benchmarks are real contributions. However, there are two major weaknesses: (1) using Rouge/BLEU for Text-to-SQL evaluation is a well-known methodological error that undermines one of the five core evaluation subtasks, and (2) the template-synthesized construction limits the dataset's ability to support "real-world" complexity claims. The MTR retrieval method, while showing gains over weak baselines (BM25, TF-IDF), has a simplistic binary relevance function and would benefit from stronger baselines. The human performance measurement lacks independent validation. These issues collectively prevent the paper from convincingly establishing its core claims, though the benchmark itself could serve as a useful starting point if the evaluation metrics are corrected.

Originality: Moderate — fills a real gap but the construction approach (template synthesis from Spider) and retrieval method (iterative binary relevance) offer limited novelty.
Importance of research question: High — multi-table reasoning is genuinely important and underserved.
Claims support: Moderate — the QA and key selection results are solid, but Text-to-SQL results are undermined by inappropriate metrics, and the "real-world complexity" framing is oversold given template synthesis.
Soundness of experiments: Moderate — inappropriate SQL metrics, weak retrieval baselines, no error bars on analysis.
Clarity: Moderate — the MTR algorithm description is somewhat confusing, and the human evaluation protocol is underspecified.
Value to community: Moderate — the benchmark could be valuable if evaluation metrics are corrected.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>